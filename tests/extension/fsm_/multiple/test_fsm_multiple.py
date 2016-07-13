from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_multiple

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
  
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [WIDTH-1:0] tmp_0;
  reg [WIDTH-1:0] tmp_1;
  reg [WIDTH-1:0] tmp_2;
  reg [WIDTH-1:0] tmp_3;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  
  always @(posedge CLK) begin
    if(RST) begin        
      fsm <= fsm_init;
      tmp_0 <= 0;
      tmp_1 <= 0;
      tmp_2 <= 0;
      tmp_3 <= 0;
      LED <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          tmp_0 <= 0;
          fsm <= fsm_1;
        end
        fsm_1: begin
          tmp_1 <= 1;
          fsm <= fsm_2;
        end
        fsm_2: begin
          tmp_2 <= 2;
          fsm <= fsm_3;
        end
        fsm_3: begin
          tmp_3 <= 3;
          fsm <= fsm_4;
        end
        fsm_4: begin
          LED <= (LED + 1);
          fsm <= fsm_init;
        end
      endcase
    end 
  end 
endmodule
"""

def test():
    veriloggen.reset()
    test_module = fsm_multiple.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
