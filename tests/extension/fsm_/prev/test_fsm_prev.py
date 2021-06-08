from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_prev

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

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg _valid_1;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  reg _fsm_cond_7_1_1;
  reg _fsm_cond_8_2_1;
  reg _fsm_cond_9_3_1;
  reg _fsm_cond_10_4_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      valid <= 0;
      _fsm_cond_2_0_1 <= 0;
      _fsm_cond_7_1_1 <= 0;
      _fsm_cond_8_2_1 <= 0;
      _fsm_cond_9_3_1 <= 0;
      _fsm_cond_10_4_1 <= 0;
      _valid_1 <= 0;
    end else begin
      _valid_1 <= valid;
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_2: begin
          if(_fsm_cond_2_0_1) begin
            valid <= 0;
          end 
        end
        fsm_7: begin
          if(_fsm_cond_7_1_1) begin
            valid <= 0;
          end 
        end
        fsm_8: begin
          if(_fsm_cond_8_2_1) begin
            valid <= 0;
          end 
        end
        fsm_9: begin
          if(_fsm_cond_9_3_1) begin
            valid <= 0;
          end 
        end
        fsm_10: begin
          if(_fsm_cond_10_4_1) begin
            valid <= 0;
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          fsm <= fsm_1;
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(_valid_1 == 0) begin
            valid <= 1;
          end 
          _fsm_cond_2_0_1 <= 1;
          if(_valid_1 == 1) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          fsm <= fsm_5;
        end
        fsm_5: begin
          fsm <= fsm_6;
        end
        fsm_6: begin
          fsm <= fsm_7;
        end
        fsm_7: begin
          valid <= 1;
          _fsm_cond_7_1_1 <= 1;
          fsm <= fsm_8;
        end
        fsm_8: begin
          valid <= 1;
          _fsm_cond_8_2_1 <= 1;
          fsm <= fsm_9;
        end
        fsm_9: begin
          valid <= 1;
          _fsm_cond_9_3_1 <= 1;
          fsm <= fsm_10;
        end
        fsm_10: begin
          valid <= 1;
          _fsm_cond_10_4_1 <= 1;
          fsm <= fsm_11;
        end
      endcase
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = fsm_prev.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
