from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import multiple_definition_instance_variable

expected_verilog = """
"""

def test():
    veriloggen.reset()
    try:
        test_module = multiple_definition_instance_variable.mkLed()
    except ValueError as e:
        assert(e.args[0] == "Object 'inst_sub' is already defined.")
        return 

    assert(False)
        
    #code = test_module.to_verilog()

    #from pyverilog.vparser.parser import VerilogParser
    #from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    #parser = VerilogParser()
    #expected_ast = parser.parse(expected_verilog)
    #codegen = ASTCodeGenerator()
    #expected_code = codegen.visit(expected_ast)

    #assert(expected_code == code)
