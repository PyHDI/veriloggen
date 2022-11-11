from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import op_reverse

expected_verilog = """
module blinkled #
(
  parameter WIDTH = 8
)
(
  input [32-1:0] A,
  output [WIDTH-1:0] B
);

  assign B = A[31:32-WIDTH];

endmodule
"""

def test():
    veriloggen.reset()
    test_module = op_reverse.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
