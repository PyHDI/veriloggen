from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_hook_nested

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

  blinkled
  #(
    .WIDTH(WIDTH)
  ) 
  inst_blinkled
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED)
  );
endmodule

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
      if(count<1023) begin
        count <= count + 1;
      end
      if(count>=1023) begin
        count <= 0;
      end
      if(count>=1023) begin
        LED <= LED + 1;
      end
    end
  end

endmodule
"""

def test():
    veriloggen.reset()
    test_module = seq_hook_nested.mkTop()
    dummy = test_module.to_verilog()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
