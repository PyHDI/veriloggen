from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_regionadd

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg [32-1:0] ydata;
  reg [32-1:0] edata;
  wire [32-1:0] zdata;
  wire [32-1:0] vdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .edata(edata),
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
    edata = 0;
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
          xdata <= 0;
          ydata <= 0;
          edata <= 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          send_fsm <= send_fsm_2;
        end
        send_fsm_2: begin
          xdata <= xdata + 1;
          ydata <= ydata + 2;
          edata <= 1;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 64) begin
            send_fsm <= send_fsm_3;
          end 
        end
        send_fsm_3: begin
          edata <= 0;
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;
  localparam recv_fsm_2 = 2;

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
          if(vdata) begin
            $display("zdata=%d", zdata);
            recv_count <= recv_count + 1;
          end 
          if(recv_count == 8) begin
            recv_fsm <= recv_fsm_2;
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
  input [32-1:0] edata,
  output [32-1:0] zdata,
  output [32-1:0] vdata
);

  reg [32-1:0] _data_3;
  reg [32-1:0] _data_6;
  reg [32-1:0] _data_14;
  reg [1-1:0] _data_7;
  reg [32-1:0] _data_15;
  reg [32-1:0] _data_16;
  reg [1-1:0] _data_9;
  reg [32-1:0] _data_10;
  reg [32-1:0] _data_17;
  reg [32-1:0] _data_18;
  reg [32-1:0] _data_11;
  reg [32-1:0] _data_13;
  reg [32-1:0] _data_19;
  assign zdata = _data_13;
  assign vdata = _data_19;

  always @(posedge CLK) begin
    if(RST) begin
      _data_3 <= 0;
      _data_6 <= 1'd0;
      _data_14 <= 0;
      _data_7 <= 0;
      _data_15 <= 0;
      _data_16 <= 0;
      _data_9 <= 0;
      _data_10 <= 0;
      _data_17 <= 0;
      _data_18 <= 0;
      _data_11 <= 0;
      _data_13 <= 1'd0;
      _data_19 <= 0;
    end else begin
      _data_3 <= xdata + ydata;
      if(edata) begin
        _data_6 <= (_data_6 >= 7)? 0 : _data_6 + 2'd1;
      end 
      _data_14 <= edata;
      _data_7 <= _data_6 == 4'd7;
      _data_15 <= _data_14;
      _data_16 <= _data_3;
      _data_9 <= _data_7;
      _data_10 <= _data_9 && _data_15;
      _data_17 <= _data_16;
      _data_18 <= _data_15;
      _data_11 <= _data_10;
      if(_data_18) begin
        _data_13 <= _data_13 + _data_17;
      end 
      if(_data_11) begin
        _data_13 <= 1'd0;
      end 
      if(_data_18 && _data_11) begin
        _data_13 <= 1'd0 + _data_17;
      end 
      _data_19 <= _data_10;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_regionadd.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
