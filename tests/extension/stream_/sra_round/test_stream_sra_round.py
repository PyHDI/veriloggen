from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_sra_round

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
    ydata = 1;
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
          xdata <= xdata + 9;
          ydata <= 2;
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

  reg signed [32-1:0] _sra_data_2;
  reg signed [32-1:0] _minus_data_3;
  reg [1-1:0] _eq_data_9;
  reg signed [32-1:0] __delay_data_12;
  reg signed [32-1:0] _sra_data_5;
  reg signed [32-1:0] __delay_data_13;
  reg [1-1:0] __delay_data_15;
  reg signed [32-1:0] __delay_data_18;
  reg [1-1:0] _pointer_data_6;
  reg signed [32-1:0] __delay_data_14;
  reg [1-1:0] __delay_data_16;
  reg signed [32-1:0] __delay_data_19;
  reg [32-1:0] _plus_data_10;
  reg [1-1:0] __delay_data_17;
  reg signed [32-1:0] __delay_data_20;
  reg signed [32-1:0] _cond_data_11;
  assign zdata = _cond_data_11;

  always @(posedge CLK) begin
    if(RST) begin
      _sra_data_2 <= 0;
      _minus_data_3 <= 0;
      _eq_data_9 <= 0;
      __delay_data_12 <= 0;
      _sra_data_5 <= 0;
      __delay_data_13 <= 0;
      __delay_data_15 <= 0;
      __delay_data_18 <= 0;
      _pointer_data_6 <= 0;
      __delay_data_14 <= 0;
      __delay_data_16 <= 0;
      __delay_data_19 <= 0;
      _plus_data_10 <= 0;
      __delay_data_17 <= 0;
      __delay_data_20 <= 0;
      _cond_data_11 <= 0;
    end else begin
      _sra_data_2 <= xdata >>> ydata;
      _minus_data_3 <= ydata - 2'sd1;
      _eq_data_9 <= ydata == 1'sd0;
      __delay_data_12 <= xdata;
      _sra_data_5 <= __delay_data_12 >>> _minus_data_3;
      __delay_data_13 <= _sra_data_2;
      __delay_data_15 <= _eq_data_9;
      __delay_data_18 <= __delay_data_12;
      _pointer_data_6 <= _sra_data_5[1'sd0];
      __delay_data_14 <= __delay_data_13;
      __delay_data_16 <= __delay_data_15;
      __delay_data_19 <= __delay_data_18;
      _plus_data_10 <= __delay_data_14 + _pointer_data_6;
      __delay_data_17 <= __delay_data_16;
      __delay_data_20 <= __delay_data_19;
      _cond_data_11 <= (__delay_data_17)? __delay_data_20 : _plus_data_10;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_sra_round.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
