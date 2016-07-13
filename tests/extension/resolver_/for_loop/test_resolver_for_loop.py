from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import resolver_for_loop

expected_verilog = """
module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [32-1:0] count [0:8-1];
  integer i;

  always @(posedge CLK) begin
    if(RST) begin
      count[0] <= 0;
      count[1] <= 0;
      count[2] <= 0;
      count[3] <= 0;
      count[4] <= 0;
      count[5] <= 0;
      count[6] <= 0;
      count[7] <= 0;
    end else begin
      if(count[0] == 1023) begin
        count[0] <= 0;
      end else begin
        count[0] <= count[0] + 0;
      end
      if(count[1] == 1023) begin
        count[1] <= 0;
      end else begin
        count[1] <= count[1] + 1;
      end
      if(count[2] == 1023) begin
        count[2] <= 0;
      end else begin
        count[2] <= count[2] + 2;
      end
      if(count[3] == 1023) begin
        count[3] <= 0;
      end else begin
        count[3] <= count[3] + 3;
      end
      if(count[4] == 1023) begin
        count[4] <= 0;
      end else begin
        count[4] <= count[4] + 4;
      end
      if(count[5] == 1023) begin
        count[5] <= 0;
      end else begin
        count[5] <= count[5] + 5;
      end
      if(count[6] == 1023) begin
        count[6] <= 0;
      end else begin
        count[6] <= count[6] + 6;
      end
      if(count[7] == 1023) begin
        count[7] <= 0;
      end else begin
        count[7] <= count[7] + 7;
      end
    end
  end

  reg [32-1:0] _sum;

  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      _sum = 0;
      _sum = _sum + count[0];
      _sum = _sum + count[1];
      _sum = _sum + count[2];
      _sum = _sum + count[3];
      _sum = _sum + count[4];
      _sum = _sum + count[5];
      _sum = _sum + count[6];
      _sum = _sum + count[7];
      if(_sum == 8184) begin
        LED <= LED + 1;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = resolver_for_loop.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
