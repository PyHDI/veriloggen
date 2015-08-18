import led

expected_verilog = """
module blinkled #
  ( 
   parameter WIDTH = 8
  )
  ( 
   input CLK, 
   input RST,
   output [WIDTH-1:0] LED
  );
  reg [WIDTH-1:0] value;
  always @(posedge CLK) begin
    value <= 10;
  end
  assign LED = value;
endmodule
"""

def test_led():
    led_module = led.mkLed()
    led_code = led_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == led_code)
