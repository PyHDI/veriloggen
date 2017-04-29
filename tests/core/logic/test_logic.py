from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import logic

expected_verilog = """
module blinkled
(
  input a,
  input b,
  input c,
  output exp
);

  assign exp = a & b ^ ~c;

endmodule
"""

def test():
    veriloggen.reset()
    test_module = logic.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
