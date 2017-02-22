from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_fixed_div

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
      a <= (a << 4) / b >> 4;
      b <= (a << 4) / b;
      c <= (a << 4) / b << 8;
      d <= b / (a << 4) >> 2;
      sa <= ((($signed((sa << 4)) >> 31) & 1 && ($signed(sb) >> 31) & 1 || !(($signed((sa << 4)) >> 31) & 1) && !(($signed(sb) >> 31) & 1))? (((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) / (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1) : ~((((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) / (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1)) + 1) >>> 4;
      sb <= (($signed((sa << 4)) >> 31) & 1 && ($signed(sb) >> 31) & 1 || !(($signed((sa << 4)) >> 31) & 1) && !(($signed(sb) >> 31) & 1))? (((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) / (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1) : ~((((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) / (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1)) + 1;
      sc <= ((($signed((sa << 4)) >> 31) & 1 && ($signed(sb) >> 31) & 1 || !(($signed((sa << 4)) >> 31) & 1) && !(($signed(sb) >> 31) & 1))? (((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) / (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1) : ~((((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) / (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1)) + 1) << 8;
      sd <= ((($signed(sb) >> 31) & 1 && ($signed((sa << 4)) >> 31) & 1 || !(($signed(sb) >> 31) & 1) && !(($signed((sa << 4)) >> 31) & 1))? (((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1) / (((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1) : ~((((($signed(sb) >> 31) & 1) == 0)? $signed(sb) : ~$signed(sb) + 1) / (((($signed((sa << 4)) >> 31) & 1) == 0)? $signed((sa << 4)) : ~$signed((sa << 4)) + 1)) + 1) >>> 2;
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = types_fixed_div.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
