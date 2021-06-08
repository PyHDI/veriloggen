from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_fixed_mul

expected_verilog = """
module test;

  reg uut_CLK;
  reg uut_RST;

  blinkled
  uut
  (
    .CLK(uut_CLK),
    .RST(uut_RST)
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



module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST
);

  reg [32-1:0] a;
  reg [32-1:0] b;
  reg [32-1:0] c;
  reg [32-1:0] d;
  reg signed [32-1:0] sa;
  reg signed [32-1:0] sb;
  reg signed [32-1:0] sc;
  reg signed [32-1:0] sd;

  always @(posedge CLK) begin
    if(RST) begin
      a <= 131072;
      b <= 4096;
      c <= 65536;
      d <= 65536;
      sa <= 131072;
      sb <= -4096;
      sc <= -65536;
      sd <= -65536;
    end else begin
      a <= a;
      b <= b;
      c <= b * a >> 8;
      d <= a * b >> 8;
      sa <= sa;
      sb <= sb;
      sc <= sb * sa >>> 8;
      sd <= $signed(a) * sb >>> 8;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_fixed_mul.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
