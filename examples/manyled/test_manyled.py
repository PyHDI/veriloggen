from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import manyled

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
   output reg [WIDTH-1:0] LED_3
  );
  reg [32-1:0] count_0;
  always @(posedge CLK) begin
    if(RST) begin
      count_0 <= 0;
    end else begin
      if(count_0 == 9) begin
        count_0 <= 0;
      end else begin
        count_0 <= count_0 + 1;
      end
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED_0 <= 0;
    end else begin
      if(count_0 == 9) begin
        LED_0 <= LED_0 + 1;
      end 
    end
  end
  reg [32-1:0] count_1;
  always @(posedge CLK) begin
    if(RST) begin
      count_1 <= 0;
    end else begin
      if(count_1 == 19) begin
        count_1 <= 0;
      end else begin
        count_1 <= count_1 + 1;
      end
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED_1 <= 0;
    end else begin
      if(count_1 == 19) begin
        LED_1 <= LED_1 + 1;
      end 
    end
  end
  reg [32-1:0] count_2;
  always @(posedge CLK) begin
    if(RST) begin
      count_2 <= 0;
    end else begin
      if(count_2 == 29) begin
        count_2 <= 0;
      end else begin
        count_2 <= count_2 + 1;
      end
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED_2 <= 0;
    end else begin
      if(count_2 == 29) begin
        LED_2 <= LED_2 + 1;
      end 
    end
  end
  reg [32-1:0] count_3;
  always @(posedge CLK) begin
    if(RST) begin
      count_3 <= 0;
    end else begin
      if(count_3 == 39) begin
        count_3 <= 0;
      end else begin
        count_3 <= count_3 + 1;
      end
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED_3 <= 0;
    end else begin
      if(count_3 == 39) begin
        LED_3 <= LED_3 + 1;
      end 
    end
  end
endmodule
"""

def test():
    veriloggen.reset()
    test_module = manyled.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
