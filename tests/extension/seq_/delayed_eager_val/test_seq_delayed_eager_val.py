from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_delayed_eager_val

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire led0;
  wire led1;
  wire led2;
  wire led3;
  wire led4;
  wire led5;
  wire led6;
  wire led7;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .led0(led0),
    .led1(led1),
    .led2(led2),
    .led3(led3),
    .led4(led4),
    .led5(led5),
    .led6(led6),
    .led7(led7)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg led0,
  output reg led1,
  output reg led2,
  output reg led3,
  output reg led4,
  output reg led5,
  output reg led6,
  output reg led7
);

  wire up;
  wire down;
  assign up = 1;
  assign down = 0;
  reg [3-1:0] count;
  reg _led0_0_1;
  reg _led0_0_2;
  reg _seq_cond_1_1;
  reg _seq_cond_1_2;
  reg _led1_2_1;
  reg _led1_2_2;
  reg _seq_cond_3_1;
  reg _seq_cond_3_2;
  reg _led2_4_1;
  reg _led2_4_2;
  reg _seq_cond_5_1;
  reg _seq_cond_5_2;
  reg _led2_6_1;
  reg _led2_6_2;
  reg _seq_cond_7_1;
  reg _seq_cond_7_2;
  reg _led3_8_1;
  reg _led3_8_2;
  reg _seq_cond_9_1;
  reg _seq_cond_9_2;
  reg _led3_10_1;
  reg _led3_10_2;
  reg _seq_cond_11_1;
  reg _seq_cond_11_2;
  reg _led4_12_1;
  reg _led4_12_2;
  reg _seq_cond_13_1;
  reg _seq_cond_13_2;
  reg _led4_14_1;
  reg _led4_14_2;
  reg _seq_cond_15_1;
  reg _seq_cond_15_2;
  reg _led5_16_1;
  reg _led5_16_2;
  reg _seq_cond_17_1;
  reg _seq_cond_17_2;
  reg _led5_18_1;
  reg _led5_18_2;
  reg _seq_cond_19_1;
  reg _seq_cond_19_2;
  reg _led6_20_1;
  reg _led6_20_2;
  reg _seq_cond_21_1;
  reg _seq_cond_21_2;
  reg _led6_22_1;
  reg _led6_22_2;
  reg _seq_cond_23_1;
  reg _seq_cond_23_2;
  reg _led7_24_1;
  reg _led7_24_2;
  reg _seq_cond_25_1;
  reg _seq_cond_25_2;
  reg _led7_26_1;
  reg _led7_26_2;
  reg _seq_cond_27_1;
  reg _seq_cond_27_2;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      led0 <= 0;
      _led0_0_1 <= 0;
      _led0_0_2 <= 0;
      _seq_cond_1_1 <= 0;
      _seq_cond_1_2 <= 0;
      led1 <= 0;
      _led1_2_1 <= 0;
      _led1_2_2 <= 0;
      _seq_cond_3_1 <= 0;
      _seq_cond_3_2 <= 0;
      led2 <= 0;
      _led2_4_1 <= 0;
      _led2_4_2 <= 0;
      _seq_cond_5_1 <= 0;
      _seq_cond_5_2 <= 0;
      _led2_6_1 <= 0;
      _led2_6_2 <= 0;
      _seq_cond_7_1 <= 0;
      _seq_cond_7_2 <= 0;
      led3 <= 0;
      _led3_8_1 <= 0;
      _led3_8_2 <= 0;
      _seq_cond_9_1 <= 0;
      _seq_cond_9_2 <= 0;
      _led3_10_1 <= 0;
      _led3_10_2 <= 0;
      _seq_cond_11_1 <= 0;
      _seq_cond_11_2 <= 0;
      led4 <= 0;
      _led4_12_1 <= 0;
      _led4_12_2 <= 0;
      _seq_cond_13_1 <= 0;
      _seq_cond_13_2 <= 0;
      _led4_14_1 <= 0;
      _led4_14_2 <= 0;
      _seq_cond_15_1 <= 0;
      _seq_cond_15_2 <= 0;
      led5 <= 0;
      _led5_16_1 <= 0;
      _led5_16_2 <= 0;
      _seq_cond_17_1 <= 0;
      _seq_cond_17_2 <= 0;
      _led5_18_1 <= 0;
      _led5_18_2 <= 0;
      _seq_cond_19_1 <= 0;
      _seq_cond_19_2 <= 0;
      led6 <= 0;
      _led6_20_1 <= 0;
      _led6_20_2 <= 0;
      _seq_cond_21_1 <= 0;
      _seq_cond_21_2 <= 0;
      _led6_22_1 <= 0;
      _led6_22_2 <= 0;
      _seq_cond_23_1 <= 0;
      _seq_cond_23_2 <= 0;
      led7 <= 0;
      _led7_24_1 <= 0;
      _led7_24_2 <= 0;
      _seq_cond_25_1 <= 0;
      _seq_cond_25_2 <= 0;
      _led7_26_1 <= 0;
      _led7_26_2 <= 0;
      _seq_cond_27_1 <= 0;
      _seq_cond_27_2 <= 0;
    end else begin
      if(_seq_cond_1_2) begin
        led0 <= _led0_0_2;
      end 
      if(_seq_cond_3_2) begin
        led1 <= _led1_2_2;
      end 
      if(_seq_cond_5_2) begin
        led2 <= _led2_4_2;
      end 
      if(_seq_cond_7_2) begin
        led2 <= _led2_6_2;
      end 
      if(_seq_cond_9_2) begin
        led3 <= _led3_8_2;
      end 
      if(_seq_cond_11_2) begin
        led3 <= _led3_10_2;
      end 
      if(_seq_cond_13_2) begin
        led4 <= _led4_12_2;
      end 
      if(_seq_cond_15_2) begin
        led4 <= _led4_14_2;
      end 
      if(_seq_cond_17_2) begin
        led5 <= _led5_16_2;
      end 
      if(_seq_cond_19_2) begin
        led5 <= _led5_18_2;
      end 
      if(_seq_cond_21_2) begin
        led6 <= _led6_20_2;
      end 
      if(_seq_cond_23_2) begin
        led6 <= _led6_22_2;
      end 
      if(_seq_cond_25_2) begin
        led7 <= _led7_24_2;
      end 
      if(_seq_cond_27_2) begin
        led7 <= _led7_26_2;
      end 
      _led0_0_2 <= _led0_0_1;
      _seq_cond_1_2 <= _seq_cond_1_1;
      _led1_2_2 <= _led1_2_1;
      _seq_cond_3_2 <= _seq_cond_3_1;
      _led2_4_2 <= _led2_4_1;
      _seq_cond_5_2 <= _seq_cond_5_1;
      _led2_6_2 <= _led2_6_1;
      _seq_cond_7_2 <= _seq_cond_7_1;
      _led3_8_2 <= _led3_8_1;
      _seq_cond_9_2 <= _seq_cond_9_1;
      _led3_10_2 <= _led3_10_1;
      _seq_cond_11_2 <= _seq_cond_11_1;
      _led4_12_2 <= _led4_12_1;
      _seq_cond_13_2 <= _seq_cond_13_1;
      _led4_14_2 <= _led4_14_1;
      _seq_cond_15_2 <= _seq_cond_15_1;
      _led5_16_2 <= _led5_16_1;
      _seq_cond_17_2 <= _seq_cond_17_1;
      _led5_18_2 <= _led5_18_1;
      _seq_cond_19_2 <= _seq_cond_19_1;
      _led6_20_2 <= _led6_20_1;
      _seq_cond_21_2 <= _seq_cond_21_1;
      _led6_22_2 <= _led6_22_1;
      _seq_cond_23_2 <= _seq_cond_23_1;
      _led7_24_2 <= _led7_24_1;
      _seq_cond_25_2 <= _seq_cond_25_1;
      _led7_26_2 <= _led7_26_1;
      _seq_cond_27_2 <= _seq_cond_27_1;
      count <= count + 1;
      if(count == 0) begin
        led0 <= up;
      end 
      _led0_0_1 <= down;
      _seq_cond_1_1 <= count == 0;
      if(count == 1) begin
        led1 <= up;
      end 
      _led1_2_1 <= down;
      _seq_cond_3_1 <= count == 1;
      if(count == 2) begin
        led2 <= up;
      end 
      _led2_4_1 <= down;
      _seq_cond_5_1 <= count == 2;
      _led2_6_1 <= up;
      _seq_cond_7_1 <= count == 0;
      if(count == 3) begin
        led3 <= up;
      end 
      _led3_8_1 <= down;
      _seq_cond_9_1 <= count == 3;
      _led3_10_1 <= up;
      _seq_cond_11_1 <= count == 0;
      if(count == 4) begin
        led4 <= up;
      end 
      _led4_12_1 <= down;
      _seq_cond_13_1 <= count == 4;
      _led4_14_1 <= up;
      _seq_cond_15_1 <= count == 0;
      if(count == 5) begin
        led5 <= up;
      end 
      _led5_16_1 <= down;
      _seq_cond_17_1 <= count == 5;
      _led5_18_1 <= up;
      _seq_cond_19_1 <= count == 0;
      if(count == 6) begin
        led6 <= up;
      end 
      _led6_20_1 <= down;
      _seq_cond_21_1 <= count == 6;
      _led6_22_1 <= up;
      _seq_cond_23_1 <= count == 0;
      if(count == 7) begin
        led7 <= up;
      end 
      _led7_24_1 <= down;
      _seq_cond_25_1 <= count == 7;
      _led7_26_1 <= up;
      _seq_cond_27_1 <= count == 0;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_delayed_eager_val.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
