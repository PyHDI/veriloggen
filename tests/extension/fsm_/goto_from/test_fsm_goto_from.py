from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_goto_from

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
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      LED <= 0;
      count <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          LED <= 0;
          fsm <= fsm_1;
        end
        fsm_1: begin
          count <= 0;
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(count < 1024) begin
            fsm <= fsm_3;
          end 
          if(!(count < 1024)) begin
            fsm <= fsm_7;
          end 
        end
        fsm_3: begin
          count <= count + 1;
          fsm <= fsm_4;
        end
        fsm_4: begin
          count <= count + 1;
          fsm <= fsm_5;
        end
        fsm_5: begin
          count <= count + 1;
          fsm <= fsm_6;
        end
        fsm_6: begin
          count <= count + 1;
          fsm <= fsm_2;
        end
        fsm_7: begin
          LED <= LED + 1;
          fsm <= fsm_1;
        end
      endcase
    end
  end

endmodule
"""


def test():
    veriloggen.reset()
    test_module = fsm_goto_from.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
