from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import patternmux

expected_verilog = """
module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [WIDTH-1:0] LED
);

  reg [32-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      count <= (count < 10)? count + 1 : 
               (count == 1023)? 0 : count + 1;
      LED <= (count < 10)? LED : 
             (count == 1023)? LED + 1 : LED;
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = patternmux.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
