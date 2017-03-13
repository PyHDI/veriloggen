from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_regionadd_valid

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg [32-1:0] ydata;
  reg ivalid;
  wire ovalid;
  wire [32-1:0] zdata;
  wire [1-1:0] vdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .ivalid(ivalid),
    .ovalid(ovalid),
    .zdata(zdata),
    .vdata(vdata)
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
    ivalid = 0;
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
  localparam send_fsm_3 = 3;
  localparam send_fsm_4 = 4;

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
          ivalid <= 0;
          send_count <= send_count + 1;
          if(send_count == 10) begin
            send_count <= 0;
          end 
          if(send_count == 10) begin
            send_fsm <= send_fsm_2;
          end 
        end
        send_fsm_2: begin
          xdata <= 0;
          ydata <= 0;
          ivalid <= 1;
          send_count <= send_count + 1;
          send_fsm <= send_fsm_3;
        end
        send_fsm_3: begin
          xdata <= xdata + 1;
          ydata <= ydata + 2;
          ivalid <= 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 65) begin
            ivalid <= 0;
          end 
          if(send_count == 65) begin
            send_fsm <= send_fsm_4;
          end 
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;

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
          if(ovalid && vdata) begin
            $display("zdata=%d", zdata);
            recv_count <= recv_count + 1;
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
  input ivalid,
  output ovalid,
  output [32-1:0] zdata,
  output [1-1:0] vdata
);

  reg _ivalid_0;
  reg _ivalid_1;
  assign ovalid = _ivalid_1;
  reg [32-1:0] _data_5;
  reg [32-1:0] _data_2;
  reg [1-1:0] _data_6;
  reg [1-1:0] _data_8;
  reg [1-1:0] _data_9;
  reg [32-1:0] _data_11;
  reg [1-1:0] _data_12;
  assign zdata = _data_11;
  assign vdata = _data_12;

  always @(posedge CLK) begin
    if(RST) begin
      _ivalid_0 <= 0;
      _ivalid_1 <= 0;
      _data_5 <= 1'd0;
      _data_2 <= 0;
      _data_6 <= 0;
      _data_8 <= 0;
      _data_9 <= 0;
      _data_11 <= 1'd0;
      _data_12 <= 0;
    end else begin
      _ivalid_0 <= ivalid;
      _ivalid_1 <= _ivalid_0;
      _data_5 <= (_data_5 >= 7)? 0 : _data_5 + 2'd1;
      _data_2 <= xdata + ydata;
      _data_6 <= _data_5 == 4'd7;
      _data_8 <= _data_6;
      _data_9 <= _data_8;
      if(_ivalid_0) begin
        _data_11 <= _data_11 + _data_2;
      end 
      if(_ivalid_0 && _data_9) begin
        _data_11 <= 1'd0 + _data_2;
      end 
      _data_12 <= _data_8;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_regionadd_valid.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
