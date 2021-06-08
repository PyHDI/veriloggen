from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_average

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg signed [32-1:0] xdata;
  reg signed [32-1:0] ydata;
  wire signed [32-1:0] zdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .ydata(ydata),
    .zdata(zdata)
  );

  reg reset_done;

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
          xdata <= xdata + 1;
          ydata <= ydata + 2;
          $display("xdata=%d", xdata);
          $display("ydata=%d", ydata);
          send_count <= send_count + 1;
          if(send_count == 20) begin
            send_fsm <= send_fsm_2;
          end 
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
          $display("zdata=%d", zdata);
          recv_count <= recv_count + 1;
          if(recv_count == 30) begin
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
  input signed [32-1:0] xdata,
  input signed [32-1:0] ydata,
  output signed [32-1:0] zdata
);

  reg signed [32-1:0] _plus_data_2;
  reg signed [32-1:0] _plus_data_4;
  reg signed [32-1:0] _plus_data_6;
  reg signed [32-1:0] _plus_data_8;
  reg signed [32-1:0] _plus_data_10;
  reg signed [32-1:0] _plus_data_12;
  reg signed [32-1:0] _plus_data_14;
  reg signed [32-1:0] _plus_data_16;
  reg signed [32-1:0] __delay_data_29__variable_1;
  reg signed [32-1:0] _plus_data_19;
  reg signed [32-1:0] _plus_data_20;
  reg signed [32-1:0] _plus_data_22;
  reg signed [32-1:0] _plus_data_23;
  reg signed [32-1:0] __delay_data_30__delay_29__variable_1;
  reg signed [32-1:0] _plus_data_21;
  reg signed [32-1:0] _plus_data_24;
  reg signed [32-1:0] __delay_data_31__delay_30__delay_29__variable_1;
  reg signed [32-1:0] _plus_data_25;
  reg signed [32-1:0] __delay_data_32__delay_31__delay_30__delay_29__variable_1;
  wire signed [32-1:0] _sra_data_26;
  assign _sra_data_26 = _plus_data_25 >>> 3'sd3;
  reg signed [32-1:0] _plus_data_28;
  assign zdata = _plus_data_28;

  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_2 <= 0;
      _plus_data_4 <= 0;
      _plus_data_6 <= 0;
      _plus_data_8 <= 0;
      _plus_data_10 <= 0;
      _plus_data_12 <= 0;
      _plus_data_14 <= 0;
      _plus_data_16 <= 0;
      __delay_data_29__variable_1 <= 0;
      _plus_data_19 <= 0;
      _plus_data_20 <= 0;
      _plus_data_22 <= 0;
      _plus_data_23 <= 0;
      __delay_data_30__delay_29__variable_1 <= 0;
      _plus_data_21 <= 0;
      _plus_data_24 <= 0;
      __delay_data_31__delay_30__delay_29__variable_1 <= 0;
      _plus_data_25 <= 0;
      __delay_data_32__delay_31__delay_30__delay_29__variable_1 <= 0;
      _plus_data_28 <= 0;
    end else begin
      _plus_data_2 <= xdata + 1'sd0;
      _plus_data_4 <= xdata + 2'sd1;
      _plus_data_6 <= xdata + 3'sd2;
      _plus_data_8 <= xdata + 3'sd3;
      _plus_data_10 <= xdata + 4'sd4;
      _plus_data_12 <= xdata + 4'sd5;
      _plus_data_14 <= xdata + 4'sd6;
      _plus_data_16 <= xdata + 4'sd7;
      __delay_data_29__variable_1 <= ydata;
      _plus_data_19 <= _plus_data_2 + _plus_data_4;
      _plus_data_20 <= _plus_data_6 + _plus_data_8;
      _plus_data_22 <= _plus_data_10 + _plus_data_12;
      _plus_data_23 <= _plus_data_14 + _plus_data_16;
      __delay_data_30__delay_29__variable_1 <= __delay_data_29__variable_1;
      _plus_data_21 <= _plus_data_19 + _plus_data_20;
      _plus_data_24 <= _plus_data_22 + _plus_data_23;
      __delay_data_31__delay_30__delay_29__variable_1 <= __delay_data_30__delay_29__variable_1;
      _plus_data_25 <= _plus_data_21 + _plus_data_24;
      __delay_data_32__delay_31__delay_30__delay_29__variable_1 <= __delay_data_31__delay_30__delay_29__variable_1;
      _plus_data_28 <= _sra_data_26 + __delay_data_32__delay_31__delay_30__delay_29__variable_1;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_average.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
