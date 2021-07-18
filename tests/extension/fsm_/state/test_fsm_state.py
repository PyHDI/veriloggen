from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_state

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire valid;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .valid(valid)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg valid
);

  reg [8-1:0] counter;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      valid <= 0;
      counter <= 0;
    end else begin
      if(counter <= 255) begin
        counter <= counter + 1;
      end else begin
        counter <= 0;
      end
      case(fsm)
        fsm_init: begin
          if(counter == 10) begin
            valid <= 0;
          end else begin
            valid <= 1;
          end
          if(counter == 40) begin
            valid <= 0;
          end else begin
            valid <= 1;
          end
          if(valid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(counter == 20) begin
            valid <= 0;
          end else begin
            valid <= 1;
          end
          if(valid) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(counter == 30) begin
            valid <= 0;
          end else begin
            valid <= 1;
          end
          if(counter[0] == 0) begin
            fsm <= fsm_3;
          end 
          if(!(counter[0] == 0) && (counter[1] == 1)) begin
            fsm <= fsm_1;
          end 
          if(!(counter[0] == 0) && !(counter[1] == 1)) begin
            fsm <= fsm_2;
          end 
        end
        fsm_3: begin
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = fsm_state.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
