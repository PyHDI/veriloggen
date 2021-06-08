from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_delayed

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

  reg [3-1:0] count;
  reg _seq_cond_0_1;
  reg _seq_cond_0_2;
  reg _seq_cond_1_1;
  reg _seq_cond_1_2;
  reg _seq_cond_2_1;
  reg _seq_cond_2_2;
  reg _seq_cond_3_1;
  reg _seq_cond_3_2;
  reg _seq_cond_4_1;
  reg _seq_cond_4_2;
  reg _seq_cond_5_1;
  reg _seq_cond_5_2;
  reg _seq_cond_6_1;
  reg _seq_cond_6_2;
  reg _seq_cond_7_1;
  reg _seq_cond_7_2;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      led0 <= 0;
      _seq_cond_0_1 <= 0;
      _seq_cond_0_2 <= 0;
      led1 <= 0;
      _seq_cond_1_1 <= 0;
      _seq_cond_1_2 <= 0;
      led2 <= 0;
      _seq_cond_2_1 <= 0;
      _seq_cond_2_2 <= 0;
      led3 <= 0;
      _seq_cond_3_1 <= 0;
      _seq_cond_3_2 <= 0;
      led4 <= 0;
      _seq_cond_4_1 <= 0;
      _seq_cond_4_2 <= 0;
      led5 <= 0;
      _seq_cond_5_1 <= 0;
      _seq_cond_5_2 <= 0;
      led6 <= 0;
      _seq_cond_6_1 <= 0;
      _seq_cond_6_2 <= 0;
      led7 <= 0;
      _seq_cond_7_1 <= 0;
      _seq_cond_7_2 <= 0;
    end else begin
      if(_seq_cond_0_2) begin
        led0 <= 0;
      end 
      if(_seq_cond_1_2) begin
        led1 <= 0;
      end 
      if(_seq_cond_2_2) begin
        led2 <= 0;
      end 
      if(_seq_cond_3_2) begin
        led3 <= 0;
      end 
      if(_seq_cond_4_2) begin
        led4 <= 0;
      end 
      if(_seq_cond_5_2) begin
        led5 <= 0;
      end 
      if(_seq_cond_6_2) begin
        led6 <= 0;
      end 
      if(_seq_cond_7_2) begin
        led7 <= 0;
      end 
      _seq_cond_0_2 <= _seq_cond_0_1;
      _seq_cond_1_2 <= _seq_cond_1_1;
      _seq_cond_2_2 <= _seq_cond_2_1;
      _seq_cond_3_2 <= _seq_cond_3_1;
      _seq_cond_4_2 <= _seq_cond_4_1;
      _seq_cond_5_2 <= _seq_cond_5_1;
      _seq_cond_6_2 <= _seq_cond_6_1;
      _seq_cond_7_2 <= _seq_cond_7_1;
      count <= count + 1;
      if(count == 0) begin
        led0 <= 1;
      end 
      _seq_cond_0_1 <= count == 0;
      if(count == 1) begin
        led1 <= 1;
      end 
      _seq_cond_1_1 <= count == 1;
      if(count == 2) begin
        led2 <= 1;
      end 
      _seq_cond_2_1 <= count == 2;
      if(count == 3) begin
        led3 <= 1;
      end 
      _seq_cond_3_1 <= count == 3;
      if(count == 4) begin
        led4 <= 1;
      end 
      _seq_cond_4_1 <= count == 4;
      if(count == 5) begin
        led5 <= 1;
      end 
      _seq_cond_5_1 <= count == 5;
      if(count == 6) begin
        led6 <= 1;
      end 
      _seq_cond_6_1 <= count == 6;
      if(count == 7) begin
        led7 <= 1;
      end 
      _seq_cond_7_1 <= count == 7;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_delayed.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
