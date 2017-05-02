from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import embeddedcode

expected_verilog = """

module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);


  // Embedded code
  reg [31:0] count;
  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      LED <= 0;
    end else begin
      if(count == 1024 - 1) begin
        count <= 0;
        LED <= LED + 1;
      end else begin
        count <= count + 1;
      end 
    end
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = embeddedcode.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    #parser = VerilogParser()
    #expected_ast = parser.parse(expected_verilog)
    #codegen = ASTCodeGenerator()
    #expected_code = codegen.visit(expected_ast)
    expected_code = expected_verilog

    assert(expected_code == code)
