from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_fixed_add

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

  reg signed [16-1:0] a;
  reg signed [16-1:0] b;
  reg signed [32-1:0] c;
  reg signed [32-1:0] d;
  reg signed [32-1:0] e;

  always @(posedge CLK) begin
    if(RST) begin
      a <= 64;
      b <= 'sd1;
      c <= -2048;
      d <= 'sd1;
      e <= 0;
    end else begin
      a <= b - 'sd256 >>> 4;
      b <= a - 'sd16 << 4;
      c <= b[15:0] + 1;
      d <= c + 'sd256;
      e <= e + 'sd65536;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_fixed_add.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
