from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_delayed_cond

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

  reg [32-1:0] count;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_4_0_1;
  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_4_1_1;
  reg _fsm_cond_4_1_2;
  reg [32-1:0] _d3_fsm;
  reg _fsm_cond_4_2_1;
  reg _fsm_cond_4_2_2;
  reg _fsm_cond_4_2_3;
  reg _fsm_cond_13_3_1;
  reg _fsm_cond_13_4_1;
  reg _fsm_cond_13_4_2;
  reg _fsm_cond_13_5_1;
  reg _fsm_cond_13_5_2;
  reg _fsm_cond_13_5_3;
  reg [32-1:0] _d4_fsm;
  reg _fsm_cond_13_6_1;
  reg _fsm_cond_13_6_2;
  reg _fsm_cond_13_6_3;
  reg _fsm_cond_13_6_4;
  reg _fsm_cond_14_7_1;
  reg _fsm_cond_14_8_1;
  reg _fsm_cond_14_8_2;
  reg _fsm_cond_14_9_1;
  reg _fsm_cond_14_9_2;
  reg _fsm_cond_14_9_3;
  reg _fsm_cond_14_10_1;
  reg _fsm_cond_14_10_2;
  reg _fsm_cond_14_10_3;
  reg _fsm_cond_14_10_4;
  reg _fsm_cond_15_11_1;
  reg _fsm_cond_15_12_1;
  reg _fsm_cond_15_12_2;
  reg _fsm_cond_15_13_1;
  reg _fsm_cond_15_13_2;
  reg _fsm_cond_15_13_3;
  reg _fsm_cond_15_14_1;
  reg _fsm_cond_15_14_2;
  reg _fsm_cond_15_14_3;
  reg _fsm_cond_15_14_4;
  reg _fsm_cond_16_15_1;
  reg _fsm_cond_16_16_1;
  reg _fsm_cond_16_16_2;
  reg _fsm_cond_16_17_1;
  reg _fsm_cond_16_17_2;
  reg _fsm_cond_16_17_3;
  reg _fsm_cond_16_18_1;
  reg _fsm_cond_16_18_2;
  reg _fsm_cond_16_18_3;
  reg _fsm_cond_16_18_4;
  reg _fsm_cond_17_19_1;
  reg _fsm_cond_17_20_1;
  reg _fsm_cond_17_20_2;
  reg _fsm_cond_17_21_1;
  reg _fsm_cond_17_21_2;
  reg _fsm_cond_17_21_3;
  reg _fsm_cond_17_22_1;
  reg _fsm_cond_17_22_2;
  reg _fsm_cond_17_22_3;
  reg _fsm_cond_17_22_4;
  reg _fsm_cond_18_23_1;
  reg _fsm_cond_18_24_1;
  reg _fsm_cond_18_24_2;
  reg _fsm_cond_18_25_1;
  reg _fsm_cond_18_25_2;
  reg _fsm_cond_18_25_3;
  reg _fsm_cond_18_26_1;
  reg _fsm_cond_18_26_2;
  reg _fsm_cond_18_26_3;
  reg _fsm_cond_18_26_4;
  reg _fsm_cond_19_27_1;
  reg _fsm_cond_19_28_1;
  reg _fsm_cond_19_28_2;
  reg _fsm_cond_19_29_1;
  reg _fsm_cond_19_29_2;
  reg _fsm_cond_19_29_3;
  reg _fsm_cond_19_30_1;
  reg _fsm_cond_19_30_2;
  reg _fsm_cond_19_30_3;
  reg _fsm_cond_19_30_4;
  reg _fsm_cond_20_31_1;
  reg _fsm_cond_20_32_1;
  reg _fsm_cond_20_32_2;
  reg _fsm_cond_20_33_1;
  reg _fsm_cond_20_33_2;
  reg _fsm_cond_20_33_3;
  reg _fsm_cond_20_34_1;
  reg _fsm_cond_20_34_2;
  reg _fsm_cond_20_34_3;
  reg _fsm_cond_20_34_4;
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
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  localparam fsm_16 = 16;
  localparam fsm_17 = 17;
  localparam fsm_18 = 18;
  localparam fsm_19 = 19;
  localparam fsm_20 = 20;
  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _d2_fsm <= fsm_init;
      _d3_fsm <= fsm_init;
      _d4_fsm <= fsm_init;
      valid <= 0;
      _fsm_cond_4_0_1 <= 0;
      _fsm_cond_4_1_1 <= 0;
      _fsm_cond_4_1_2 <= 0;
      _fsm_cond_4_2_1 <= 0;
      _fsm_cond_4_2_2 <= 0;
      _fsm_cond_4_2_3 <= 0;
      _fsm_cond_13_3_1 <= 0;
      _fsm_cond_13_4_1 <= 0;
      _fsm_cond_13_4_2 <= 0;
      _fsm_cond_13_5_1 <= 0;
      _fsm_cond_13_5_2 <= 0;
      _fsm_cond_13_5_3 <= 0;
      _fsm_cond_13_6_1 <= 0;
      _fsm_cond_13_6_2 <= 0;
      _fsm_cond_13_6_3 <= 0;
      _fsm_cond_13_6_4 <= 0;
      _fsm_cond_14_7_1 <= 0;
      _fsm_cond_14_8_1 <= 0;
      _fsm_cond_14_8_2 <= 0;
      _fsm_cond_14_9_1 <= 0;
      _fsm_cond_14_9_2 <= 0;
      _fsm_cond_14_9_3 <= 0;
      _fsm_cond_14_10_1 <= 0;
      _fsm_cond_14_10_2 <= 0;
      _fsm_cond_14_10_3 <= 0;
      _fsm_cond_14_10_4 <= 0;
      _fsm_cond_15_11_1 <= 0;
      _fsm_cond_15_12_1 <= 0;
      _fsm_cond_15_12_2 <= 0;
      _fsm_cond_15_13_1 <= 0;
      _fsm_cond_15_13_2 <= 0;
      _fsm_cond_15_13_3 <= 0;
      _fsm_cond_15_14_1 <= 0;
      _fsm_cond_15_14_2 <= 0;
      _fsm_cond_15_14_3 <= 0;
      _fsm_cond_15_14_4 <= 0;
      _fsm_cond_16_15_1 <= 0;
      _fsm_cond_16_16_1 <= 0;
      _fsm_cond_16_16_2 <= 0;
      _fsm_cond_16_17_1 <= 0;
      _fsm_cond_16_17_2 <= 0;
      _fsm_cond_16_17_3 <= 0;
      _fsm_cond_16_18_1 <= 0;
      _fsm_cond_16_18_2 <= 0;
      _fsm_cond_16_18_3 <= 0;
      _fsm_cond_16_18_4 <= 0;
      _fsm_cond_17_19_1 <= 0;
      _fsm_cond_17_20_1 <= 0;
      _fsm_cond_17_20_2 <= 0;
      _fsm_cond_17_21_1 <= 0;
      _fsm_cond_17_21_2 <= 0;
      _fsm_cond_17_21_3 <= 0;
      _fsm_cond_17_22_1 <= 0;
      _fsm_cond_17_22_2 <= 0;
      _fsm_cond_17_22_3 <= 0;
      _fsm_cond_17_22_4 <= 0;
      _fsm_cond_18_23_1 <= 0;
      _fsm_cond_18_24_1 <= 0;
      _fsm_cond_18_24_2 <= 0;
      _fsm_cond_18_25_1 <= 0;
      _fsm_cond_18_25_2 <= 0;
      _fsm_cond_18_25_3 <= 0;
      _fsm_cond_18_26_1 <= 0;
      _fsm_cond_18_26_2 <= 0;
      _fsm_cond_18_26_3 <= 0;
      _fsm_cond_18_26_4 <= 0;
      _fsm_cond_19_27_1 <= 0;
      _fsm_cond_19_28_1 <= 0;
      _fsm_cond_19_28_2 <= 0;
      _fsm_cond_19_29_1 <= 0;
      _fsm_cond_19_29_2 <= 0;
      _fsm_cond_19_29_3 <= 0;
      _fsm_cond_19_30_1 <= 0;
      _fsm_cond_19_30_2 <= 0;
      _fsm_cond_19_30_3 <= 0;
      _fsm_cond_19_30_4 <= 0;
      _fsm_cond_20_31_1 <= 0;
      _fsm_cond_20_32_1 <= 0;
      _fsm_cond_20_32_2 <= 0;
      _fsm_cond_20_33_1 <= 0;
      _fsm_cond_20_33_2 <= 0;
      _fsm_cond_20_33_3 <= 0;
      _fsm_cond_20_34_1 <= 0;
      _fsm_cond_20_34_2 <= 0;
      _fsm_cond_20_34_3 <= 0;
      _fsm_cond_20_34_4 <= 0;
    end else begin
      count <= count + 1;
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;
      case(_d4_fsm)
        fsm_13: begin
          if(_fsm_cond_13_6_4) begin
            valid <= 0;
          end 
        end
        fsm_14: begin
          if(_fsm_cond_14_10_4) begin
            valid <= 0;
          end 
        end
        fsm_15: begin
          if(_fsm_cond_15_14_4) begin
            valid <= 0;
          end 
        end
        fsm_16: begin
          if(_fsm_cond_16_18_4) begin
            valid <= 0;
          end 
        end
        fsm_17: begin
          if(_fsm_cond_17_22_4) begin
            valid <= 0;
          end 
        end
        fsm_18: begin
          if(_fsm_cond_18_26_4) begin
            valid <= 0;
          end 
        end
        fsm_19: begin
          if(_fsm_cond_19_30_4) begin
            valid <= 0;
          end 
        end
        fsm_20: begin
          if(_fsm_cond_20_34_4) begin
            valid <= 0;
          end 
        end
      endcase
      case(_d3_fsm)
        fsm_4: begin
          if(_fsm_cond_4_2_3) begin
            valid <= 0;
          end 
        end
        fsm_13: begin
          if(_fsm_cond_13_5_3) begin
            valid <= 1;
          end 
          _fsm_cond_13_6_4 <= _fsm_cond_13_6_3;
        end
        fsm_14: begin
          if(_fsm_cond_14_9_3) begin
            valid <= 1;
          end 
          _fsm_cond_14_10_4 <= _fsm_cond_14_10_3;
        end
        fsm_15: begin
          if(_fsm_cond_15_13_3) begin
            valid <= 1;
          end 
          _fsm_cond_15_14_4 <= _fsm_cond_15_14_3;
        end
        fsm_16: begin
          if(_fsm_cond_16_17_3) begin
            valid <= 1;
          end 
          _fsm_cond_16_18_4 <= _fsm_cond_16_18_3;
        end
        fsm_17: begin
          if(_fsm_cond_17_21_3) begin
            valid <= 1;
          end 
          _fsm_cond_17_22_4 <= _fsm_cond_17_22_3;
        end
        fsm_18: begin
          if(_fsm_cond_18_25_3) begin
            valid <= 1;
          end 
          _fsm_cond_18_26_4 <= _fsm_cond_18_26_3;
        end
        fsm_19: begin
          if(_fsm_cond_19_29_3) begin
            valid <= 1;
          end 
          _fsm_cond_19_30_4 <= _fsm_cond_19_30_3;
        end
        fsm_20: begin
          if(_fsm_cond_20_33_3) begin
            valid <= 1;
          end 
          _fsm_cond_20_34_4 <= _fsm_cond_20_34_3;
        end
      endcase
      case(_d2_fsm)
        fsm_4: begin
          if(_fsm_cond_4_1_2) begin
            valid <= 1;
          end 
          _fsm_cond_4_2_3 <= _fsm_cond_4_2_2;
        end
        fsm_13: begin
          if(_fsm_cond_13_4_2) begin
            valid <= 1;
          end 
          _fsm_cond_13_5_3 <= _fsm_cond_13_5_2;
          _fsm_cond_13_6_3 <= _fsm_cond_13_6_2;
        end
        fsm_14: begin
          if(_fsm_cond_14_8_2) begin
            valid <= 1;
          end 
          _fsm_cond_14_9_3 <= _fsm_cond_14_9_2;
          _fsm_cond_14_10_3 <= _fsm_cond_14_10_2;
        end
        fsm_15: begin
          if(_fsm_cond_15_12_2) begin
            valid <= 1;
          end 
          _fsm_cond_15_13_3 <= _fsm_cond_15_13_2;
          _fsm_cond_15_14_3 <= _fsm_cond_15_14_2;
        end
        fsm_16: begin
          if(_fsm_cond_16_16_2) begin
            valid <= 1;
          end 
          _fsm_cond_16_17_3 <= _fsm_cond_16_17_2;
          _fsm_cond_16_18_3 <= _fsm_cond_16_18_2;
        end
        fsm_17: begin
          if(_fsm_cond_17_20_2) begin
            valid <= 1;
          end 
          _fsm_cond_17_21_3 <= _fsm_cond_17_21_2;
          _fsm_cond_17_22_3 <= _fsm_cond_17_22_2;
        end
        fsm_18: begin
          if(_fsm_cond_18_24_2) begin
            valid <= 1;
          end 
          _fsm_cond_18_25_3 <= _fsm_cond_18_25_2;
          _fsm_cond_18_26_3 <= _fsm_cond_18_26_2;
        end
        fsm_19: begin
          if(_fsm_cond_19_28_2) begin
            valid <= 1;
          end 
          _fsm_cond_19_29_3 <= _fsm_cond_19_29_2;
          _fsm_cond_19_30_3 <= _fsm_cond_19_30_2;
        end
        fsm_20: begin
          if(_fsm_cond_20_32_2) begin
            valid <= 1;
          end 
          _fsm_cond_20_33_3 <= _fsm_cond_20_33_2;
          _fsm_cond_20_34_3 <= _fsm_cond_20_34_2;
        end
      endcase
      case(_d1_fsm)
        fsm_4: begin
          if(_fsm_cond_4_0_1) begin
            valid <= 1;
          end 
          _fsm_cond_4_1_2 <= _fsm_cond_4_1_1;
          _fsm_cond_4_2_2 <= _fsm_cond_4_2_1;
        end
        fsm_13: begin
          if(_fsm_cond_13_3_1) begin
            valid <= 1;
          end 
          _fsm_cond_13_4_2 <= _fsm_cond_13_4_1;
          _fsm_cond_13_5_2 <= _fsm_cond_13_5_1;
          _fsm_cond_13_6_2 <= _fsm_cond_13_6_1;
        end
        fsm_14: begin
          if(_fsm_cond_14_7_1) begin
            valid <= 1;
          end 
          _fsm_cond_14_8_2 <= _fsm_cond_14_8_1;
          _fsm_cond_14_9_2 <= _fsm_cond_14_9_1;
          _fsm_cond_14_10_2 <= _fsm_cond_14_10_1;
        end
        fsm_15: begin
          if(_fsm_cond_15_11_1) begin
            valid <= 1;
          end 
          _fsm_cond_15_12_2 <= _fsm_cond_15_12_1;
          _fsm_cond_15_13_2 <= _fsm_cond_15_13_1;
          _fsm_cond_15_14_2 <= _fsm_cond_15_14_1;
        end
        fsm_16: begin
          if(_fsm_cond_16_15_1) begin
            valid <= 1;
          end 
          _fsm_cond_16_16_2 <= _fsm_cond_16_16_1;
          _fsm_cond_16_17_2 <= _fsm_cond_16_17_1;
          _fsm_cond_16_18_2 <= _fsm_cond_16_18_1;
        end
        fsm_17: begin
          if(_fsm_cond_17_19_1) begin
            valid <= 1;
          end 
          _fsm_cond_17_20_2 <= _fsm_cond_17_20_1;
          _fsm_cond_17_21_2 <= _fsm_cond_17_21_1;
          _fsm_cond_17_22_2 <= _fsm_cond_17_22_1;
        end
        fsm_18: begin
          if(_fsm_cond_18_23_1) begin
            valid <= 1;
          end 
          _fsm_cond_18_24_2 <= _fsm_cond_18_24_1;
          _fsm_cond_18_25_2 <= _fsm_cond_18_25_1;
          _fsm_cond_18_26_2 <= _fsm_cond_18_26_1;
        end
        fsm_19: begin
          if(_fsm_cond_19_27_1) begin
            valid <= 1;
          end 
          _fsm_cond_19_28_2 <= _fsm_cond_19_28_1;
          _fsm_cond_19_29_2 <= _fsm_cond_19_29_1;
          _fsm_cond_19_30_2 <= _fsm_cond_19_30_1;
        end
        fsm_20: begin
          if(_fsm_cond_20_31_1) begin
            valid <= 1;
          end 
          _fsm_cond_20_32_2 <= _fsm_cond_20_32_1;
          _fsm_cond_20_33_2 <= _fsm_cond_20_33_1;
          _fsm_cond_20_34_2 <= _fsm_cond_20_34_1;
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
          fsm <= fsm_3;
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          if(count >= 16) begin
            valid <= 1;
          end 
          _fsm_cond_4_0_1 <= count >= 16;
          _fsm_cond_4_1_1 <= count >= 16;
          _fsm_cond_4_2_1 <= count >= 16;
          if(count >= 16) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          fsm <= fsm_6;
        end
        fsm_6: begin
          fsm <= fsm_7;
        end
        fsm_7: begin
          fsm <= fsm_8;
        end
        fsm_8: begin
          fsm <= fsm_9;
        end
        fsm_9: begin
          fsm <= fsm_10;
        end
        fsm_10: begin
          fsm <= fsm_11;
        end
        fsm_11: begin
          fsm <= fsm_12;
        end
        fsm_12: begin
          fsm <= fsm_13;
        end
        fsm_13: begin
          _fsm_cond_13_3_1 <= count >= 32;
          _fsm_cond_13_4_1 <= count >= 32;
          _fsm_cond_13_5_1 <= count >= 32;
          _fsm_cond_13_6_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          _fsm_cond_14_7_1 <= count >= 32;
          _fsm_cond_14_8_1 <= count >= 32;
          _fsm_cond_14_9_1 <= count >= 32;
          _fsm_cond_14_10_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          _fsm_cond_15_11_1 <= count >= 32;
          _fsm_cond_15_12_1 <= count >= 32;
          _fsm_cond_15_13_1 <= count >= 32;
          _fsm_cond_15_14_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          _fsm_cond_16_15_1 <= count >= 32;
          _fsm_cond_16_16_1 <= count >= 32;
          _fsm_cond_16_17_1 <= count >= 32;
          _fsm_cond_16_18_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          _fsm_cond_17_19_1 <= count >= 32;
          _fsm_cond_17_20_1 <= count >= 32;
          _fsm_cond_17_21_1 <= count >= 32;
          _fsm_cond_17_22_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          _fsm_cond_18_23_1 <= count >= 32;
          _fsm_cond_18_24_1 <= count >= 32;
          _fsm_cond_18_25_1 <= count >= 32;
          _fsm_cond_18_26_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          _fsm_cond_19_27_1 <= count >= 32;
          _fsm_cond_19_28_1 <= count >= 32;
          _fsm_cond_19_29_1 <= count >= 32;
          _fsm_cond_19_30_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          _fsm_cond_20_31_1 <= count >= 32;
          _fsm_cond_20_32_1 <= count >= 32;
          _fsm_cond_20_33_1 <= count >= 32;
          _fsm_cond_20_34_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_21;
          end 
        end
      endcase
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = fsm_delayed_cond.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
