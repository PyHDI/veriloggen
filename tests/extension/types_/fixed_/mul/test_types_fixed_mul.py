from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_fixed_mul

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

  reg [32-1:0] a;
  reg [32-1:0] b;
  reg [32-1:0] c;
  reg [32-1:0] d;
  reg signed [32-1:0] sa;
  reg signed [32-1:0] sb;
  reg signed [32-1:0] sc;
  reg signed [32-1:0] sd;

  always @(posedge CLK) begin
    if(RST) begin
      a <= 16;
      b <= 512;
      c <= 131072;
      d <= 128;
      sa <= 16;
      sb <= 512;
      sc <= 131072;
      sd <= 128;
    end else begin
      a <= ($signed(a) * $signed(b) >> 4) >> 4;
      b <= $signed(a) * $signed(b) >> 4;
      c <= ($signed(a) * $signed(b) >> 4) << 8;
      d <= ($signed(b) * $signed(a) >> 4) >> 2;
      sa <= ($signed(sa) * $signed(sb) >>> 4) >>> 4;
      sb <= $signed(sa) * $signed(sb) >>> 4;
      sc <= ($signed(sa) * $signed(sb) >>> 4) << 8;
      sd <= ($signed(sb) * $signed(sa) >>> 4) >>> 2;
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = types_fixed_mul.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
