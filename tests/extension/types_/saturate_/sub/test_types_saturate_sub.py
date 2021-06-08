from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_saturate_sub

expected_verilog = """
module test;

  reg uut_CLK;
  reg uut_RST;
  wire signed [8-1:0] uut_LED;

  blinkled
  uut
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .LED(uut_LED)
  );


  initial begin
    uut_CLK = 0;
    forever begin
      #5 uut_CLK = !uut_CLK;
    end
  end


  initial begin
    uut_RST = 0;
    #100;
    uut_RST = 1;
    #100;
    uut_RST = 0;
    #100000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg signed [8-1:0] LED
);

  reg [10-1:0] count;
  reg [8-1:0] a;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 1023;
      LED <= 127;
      a <= 0;
    end else begin
      count <= (count < 1)? 0 : count - 1;
      if(count == 0) begin
        LED <= (LED < 'sd1 + -128)? -128 : 
               (LED - 'sd1 > 'sd127)? 'sd127 : LED - 'sd1;
      end 
      $display("LED:%d count:%d", LED, count);
      a <= 255;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_saturate_sub.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
