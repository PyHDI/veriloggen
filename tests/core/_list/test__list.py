from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import _list

expected_verilog = """
module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [WIDTH-1:0] LED_0,
  output reg [WIDTH-1:0] LED_1,
  output reg [WIDTH-1:0] LED_2,
  output reg [WIDTH-1:0] LED_3,
  output reg [WIDTH-1:0] LED_4,
  output reg [WIDTH-1:0] LED_5,
  output reg [WIDTH-1:0] LED_6,
  output reg [WIDTH-1:0] LED_7
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


  always @(*) begin
    case(count % 8)
      0: begin
        LED_0 = count[WIDTH-1:0];
      end
      1: begin
        LED_1 = count[WIDTH-1:0];
      end
      2: begin
        LED_2 = count[WIDTH-1:0];
      end
      3: begin
        LED_3 = count[WIDTH-1:0];
      end
      4: begin
        LED_4 = count[WIDTH-1:0];
      end
      5: begin
        LED_5 = count[WIDTH-1:0];
      end
      6: begin
        LED_6 = count[WIDTH-1:0];
      end
      7: begin
        LED_7 = count[WIDTH-1:0];
      end
    endcase
  end
endmodule
"""

def test():
    veriloggen.reset()
    test_module = _list.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
