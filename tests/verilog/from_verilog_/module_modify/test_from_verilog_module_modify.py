from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import from_verilog_module_modify

expected_verilog = """
module top #
  (
   parameter WIDTH = 8
  )
  (
   input CLK, 
   input RST, 
   output [32-1:0] LED,
   input enable,
   output busy
  );
  modified_led #
  (
   .WIDTH(WIDTH)
  )
  inst_blinkled
  (
   .CLK(CLK),
   .RST(RST),
   .LED(LED),
   .enable(enable),
   .busy(busy)
  );
endmodule

module modified_led #
  (
   parameter WIDTH = 8
  )
  (
   input CLK, 
   input RST, 
   output reg [32-1:0] LED,
   input enable,
   output busy
  );
  reg [32-1:0] count;
  always @(posedge CLK) begin
    if(RST) begin        
      count <= 0;
    end else if(enable) begin
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
  assign busy = count < 1023;
endmodule
"""

def test():
    veriloggen.reset()
    test_module = from_verilog_module_modify.mkTop()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
