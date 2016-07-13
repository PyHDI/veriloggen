from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import generate_instance

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

  genvar i;
  generate for(i=0; i<WIDTH; i=i+1) begin: gen_for
    submod # ( .POS(i+2) ) 
    inst_submod ( .CLK(CLK), .RST(RST), .LED(LED[i]) );
  end endgenerate

endmodule

module submod #
(
  parameter POS = 0
)
(
  input CLK, 
  input RST,
  output LED
);
  reg [32-1:0] count;
  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end
  assign LED = count[POS];
endmodule
"""

def test():
    veriloggen.reset()
    test_module = generate_instance.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
