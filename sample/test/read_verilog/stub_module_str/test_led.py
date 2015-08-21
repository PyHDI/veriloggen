import led

expected_verilog = """
module top #
  (
   parameter WIDTH = 8
  )
  (
   input CLK, 
   input RST, 
   output [WIDTH-1:0] LED
  );
  blinkled #
  (
   WIDTH
  )
  inst_blinkled
  (
   CLK,
   RST,
   LED
  );
endmodule
"""

def test_led():
    top_module = led.mkTop()
    top_code = top_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == top_code)
