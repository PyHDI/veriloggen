from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import multiple_instances

expected_verilog = """
module top #
(
  parameter A_WIDTH = 8,
  parameter B_WIDTH = 8
)
(
  input CLK,
  input RST,
  output [A_WIDTH-1:0] A_LED,
  output [B_WIDTH-1:0] B_LED
);

  blinkled
  #(
    .WIDTH(A_WIDTH)
  )
  inst_blinkled_a
  (
    .CLK(CLK),
    .RST(RST),
    .LED(A_LED)
  );

  blinkled
  #(
    .WIDTH(B_WIDTH)
  )
  inst_blinkled_b
  (
    .CLK(CLK),
    .RST(RST),
    .LED(B_LED)
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
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end

  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 1;
      end 
    end
  end

endmodule
"""

def test_led():
    test_module = multiple_instances.mkTop()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
