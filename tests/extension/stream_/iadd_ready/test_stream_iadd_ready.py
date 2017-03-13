from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_iadd_ready

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg [32-1:0] ydata;
  wire iready;
  reg oready;
  wire [32-1:0] zdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .iready(iready),
    .oready(oready),
    .zdata(zdata)
  );

  reg reset_done;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
    xdata = 0;
    ydata = 0;
    oready = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] send_fsm;
  localparam send_fsm_init = 0;
  reg [32-1:0] send_count;
  reg [32-1:0] recv_fsm;
  localparam recv_fsm_init = 0;
  reg [32-1:0] recv_count;
  localparam send_fsm_1 = 1;
  localparam send_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      send_fsm <= send_fsm_init;
      send_count <= 0;
    end else begin
      case(send_fsm)
        send_fsm_init: begin
          if(reset_done) begin
            send_fsm <= send_fsm_1;
          end 
        end
        send_fsm_1: begin
          if(iready) begin
            xdata <= xdata + 1;
            ydata <= ydata + 2;
            $display("xdata=%d", xdata);
            $display("ydata=%d", ydata);
            send_count <= send_count + 1;
          end 
          if(send_count == 20) begin
            send_fsm <= send_fsm_2;
          end 
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;
  localparam recv_fsm_2 = 2;
  localparam recv_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      recv_fsm <= recv_fsm_init;
      recv_count <= 0;
    end else begin
      case(recv_fsm)
        recv_fsm_init: begin
          if(reset_done) begin
            recv_fsm <= recv_fsm_1;
          end 
        end
        recv_fsm_1: begin
          recv_count <= recv_count + 1;
          if(recv_count == 20) begin
            recv_count <= 0;
          end 
          if(recv_count == 20) begin
            recv_fsm <= recv_fsm_2;
          end 
        end
        recv_fsm_2: begin
          oready <= !oready;
          if(oready) begin
            $display("zdata=%d", zdata);
            recv_count <= recv_count + 1;
          end 
          if(recv_count == 20) begin
            oready <= 0;
          end 
          if(recv_count == 20) begin
            recv_fsm <= recv_fsm_3;
          end 
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  input [32-1:0] xdata,
  input [32-1:0] ydata,
  output iready,
  input oready,
  output [32-1:0] zdata
);

  assign iready = oready;
  reg [32-1:0] _data_2;
  reg [32-1:0] _data_4;
  assign zdata = _data_4;

  always @(posedge CLK) begin
    if(RST) begin
      _data_2 <= 0;
      _data_4 <= 1'd0;
    end else begin
      if(oready) begin
        _data_2 <= xdata + ydata;
      end 
      if(oready) begin
        _data_4 <= _data_4 + _data_2;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_iadd_ready.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
