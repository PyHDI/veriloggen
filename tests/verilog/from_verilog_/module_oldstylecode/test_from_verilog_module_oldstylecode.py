from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import from_verilog_module_oldstylecode

expected_verilog = """
module top
  (
   input CLK, 
   input RST, 
   output [8-1:0] LED
  );

  blinkled inst_blinkled
  (
   .CLK(CLK),
   .RST(RST),
   .LED(LED)
  );

endmodule

module blinkled
  (
   input CLK, 
   input RST, 
   output [7:0] LED
  );

  reg [31:0] count;
  reg [7:0] led_count;

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
      led_count <= 0;
    end else begin
      if(count == 1023) begin        
        led_count <= led_count + 1;
      end  
    end 
  end 
  assign LED = led_count;
endmodule
"""

def test():
    veriloggen.reset()
    test_module = from_verilog_module_oldstylecode.mkTop()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
