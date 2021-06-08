from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_delayed_eager_val

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
  output valid
);

  reg [32-1:0] count;
  reg [8-1:0] valid_reg;
  assign valid = valid_reg[0];
  wire up;
  wire down;
  assign up = 1;
  assign down = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg [8-1:0] _valid_reg_4_0_1;
  reg _fsm_cond_4_1_1;
  reg [32-1:0] _d2_fsm;
  reg [8-1:0] _valid_reg_4_2_1;
  reg [8-1:0] _valid_reg_4_2_2;
  reg _fsm_cond_4_3_1;
  reg _fsm_cond_4_3_2;
  reg [32-1:0] _d3_fsm;
  reg [8-1:0] _valid_reg_4_4_1;
  reg [8-1:0] _valid_reg_4_4_2;
  reg [8-1:0] _valid_reg_4_4_3;
  reg _fsm_cond_4_5_1;
  reg _fsm_cond_4_5_2;
  reg _fsm_cond_4_5_3;
  reg [8-1:0] _valid_reg_13_6_1;
  reg _fsm_cond_13_7_1;
  reg [8-1:0] _valid_reg_13_8_1;
  reg [8-1:0] _valid_reg_13_8_2;
  reg _fsm_cond_13_9_1;
  reg _fsm_cond_13_9_2;
  reg [8-1:0] _valid_reg_13_10_1;
  reg [8-1:0] _valid_reg_13_10_2;
  reg [8-1:0] _valid_reg_13_10_3;
  reg _fsm_cond_13_11_1;
  reg _fsm_cond_13_11_2;
  reg _fsm_cond_13_11_3;
  reg [32-1:0] _d4_fsm;
  reg [8-1:0] _valid_reg_13_12_1;
  reg [8-1:0] _valid_reg_13_12_2;
  reg [8-1:0] _valid_reg_13_12_3;
  reg [8-1:0] _valid_reg_13_12_4;
  reg _fsm_cond_13_13_1;
  reg _fsm_cond_13_13_2;
  reg _fsm_cond_13_13_3;
  reg _fsm_cond_13_13_4;
  reg [8-1:0] _valid_reg_14_14_1;
  reg _fsm_cond_14_15_1;
  reg [8-1:0] _valid_reg_14_16_1;
  reg [8-1:0] _valid_reg_14_16_2;
  reg _fsm_cond_14_17_1;
  reg _fsm_cond_14_17_2;
  reg [8-1:0] _valid_reg_14_18_1;
  reg [8-1:0] _valid_reg_14_18_2;
  reg [8-1:0] _valid_reg_14_18_3;
  reg _fsm_cond_14_19_1;
  reg _fsm_cond_14_19_2;
  reg _fsm_cond_14_19_3;
  reg [8-1:0] _valid_reg_14_20_1;
  reg [8-1:0] _valid_reg_14_20_2;
  reg [8-1:0] _valid_reg_14_20_3;
  reg [8-1:0] _valid_reg_14_20_4;
  reg _fsm_cond_14_21_1;
  reg _fsm_cond_14_21_2;
  reg _fsm_cond_14_21_3;
  reg _fsm_cond_14_21_4;
  reg [8-1:0] _valid_reg_15_22_1;
  reg _fsm_cond_15_23_1;
  reg [8-1:0] _valid_reg_15_24_1;
  reg [8-1:0] _valid_reg_15_24_2;
  reg _fsm_cond_15_25_1;
  reg _fsm_cond_15_25_2;
  reg [8-1:0] _valid_reg_15_26_1;
  reg [8-1:0] _valid_reg_15_26_2;
  reg [8-1:0] _valid_reg_15_26_3;
  reg _fsm_cond_15_27_1;
  reg _fsm_cond_15_27_2;
  reg _fsm_cond_15_27_3;
  reg [8-1:0] _valid_reg_15_28_1;
  reg [8-1:0] _valid_reg_15_28_2;
  reg [8-1:0] _valid_reg_15_28_3;
  reg [8-1:0] _valid_reg_15_28_4;
  reg _fsm_cond_15_29_1;
  reg _fsm_cond_15_29_2;
  reg _fsm_cond_15_29_3;
  reg _fsm_cond_15_29_4;
  reg [8-1:0] _valid_reg_16_30_1;
  reg _fsm_cond_16_31_1;
  reg [8-1:0] _valid_reg_16_32_1;
  reg [8-1:0] _valid_reg_16_32_2;
  reg _fsm_cond_16_33_1;
  reg _fsm_cond_16_33_2;
  reg [8-1:0] _valid_reg_16_34_1;
  reg [8-1:0] _valid_reg_16_34_2;
  reg [8-1:0] _valid_reg_16_34_3;
  reg _fsm_cond_16_35_1;
  reg _fsm_cond_16_35_2;
  reg _fsm_cond_16_35_3;
  reg [8-1:0] _valid_reg_16_36_1;
  reg [8-1:0] _valid_reg_16_36_2;
  reg [8-1:0] _valid_reg_16_36_3;
  reg [8-1:0] _valid_reg_16_36_4;
  reg _fsm_cond_16_37_1;
  reg _fsm_cond_16_37_2;
  reg _fsm_cond_16_37_3;
  reg _fsm_cond_16_37_4;
  reg [8-1:0] _valid_reg_17_38_1;
  reg _fsm_cond_17_39_1;
  reg [8-1:0] _valid_reg_17_40_1;
  reg [8-1:0] _valid_reg_17_40_2;
  reg _fsm_cond_17_41_1;
  reg _fsm_cond_17_41_2;
  reg [8-1:0] _valid_reg_17_42_1;
  reg [8-1:0] _valid_reg_17_42_2;
  reg [8-1:0] _valid_reg_17_42_3;
  reg _fsm_cond_17_43_1;
  reg _fsm_cond_17_43_2;
  reg _fsm_cond_17_43_3;
  reg [8-1:0] _valid_reg_17_44_1;
  reg [8-1:0] _valid_reg_17_44_2;
  reg [8-1:0] _valid_reg_17_44_3;
  reg [8-1:0] _valid_reg_17_44_4;
  reg _fsm_cond_17_45_1;
  reg _fsm_cond_17_45_2;
  reg _fsm_cond_17_45_3;
  reg _fsm_cond_17_45_4;
  reg [8-1:0] _valid_reg_18_46_1;
  reg _fsm_cond_18_47_1;
  reg [8-1:0] _valid_reg_18_48_1;
  reg [8-1:0] _valid_reg_18_48_2;
  reg _fsm_cond_18_49_1;
  reg _fsm_cond_18_49_2;
  reg [8-1:0] _valid_reg_18_50_1;
  reg [8-1:0] _valid_reg_18_50_2;
  reg [8-1:0] _valid_reg_18_50_3;
  reg _fsm_cond_18_51_1;
  reg _fsm_cond_18_51_2;
  reg _fsm_cond_18_51_3;
  reg [8-1:0] _valid_reg_18_52_1;
  reg [8-1:0] _valid_reg_18_52_2;
  reg [8-1:0] _valid_reg_18_52_3;
  reg [8-1:0] _valid_reg_18_52_4;
  reg _fsm_cond_18_53_1;
  reg _fsm_cond_18_53_2;
  reg _fsm_cond_18_53_3;
  reg _fsm_cond_18_53_4;
  reg [8-1:0] _valid_reg_19_54_1;
  reg _fsm_cond_19_55_1;
  reg [8-1:0] _valid_reg_19_56_1;
  reg [8-1:0] _valid_reg_19_56_2;
  reg _fsm_cond_19_57_1;
  reg _fsm_cond_19_57_2;
  reg [8-1:0] _valid_reg_19_58_1;
  reg [8-1:0] _valid_reg_19_58_2;
  reg [8-1:0] _valid_reg_19_58_3;
  reg _fsm_cond_19_59_1;
  reg _fsm_cond_19_59_2;
  reg _fsm_cond_19_59_3;
  reg [8-1:0] _valid_reg_19_60_1;
  reg [8-1:0] _valid_reg_19_60_2;
  reg [8-1:0] _valid_reg_19_60_3;
  reg [8-1:0] _valid_reg_19_60_4;
  reg _fsm_cond_19_61_1;
  reg _fsm_cond_19_61_2;
  reg _fsm_cond_19_61_3;
  reg _fsm_cond_19_61_4;
  reg [8-1:0] _valid_reg_20_62_1;
  reg _fsm_cond_20_63_1;
  reg [8-1:0] _valid_reg_20_64_1;
  reg [8-1:0] _valid_reg_20_64_2;
  reg _fsm_cond_20_65_1;
  reg _fsm_cond_20_65_2;
  reg [8-1:0] _valid_reg_20_66_1;
  reg [8-1:0] _valid_reg_20_66_2;
  reg [8-1:0] _valid_reg_20_66_3;
  reg _fsm_cond_20_67_1;
  reg _fsm_cond_20_67_2;
  reg _fsm_cond_20_67_3;
  reg [8-1:0] _valid_reg_20_68_1;
  reg [8-1:0] _valid_reg_20_68_2;
  reg [8-1:0] _valid_reg_20_68_3;
  reg [8-1:0] _valid_reg_20_68_4;
  reg _fsm_cond_20_69_1;
  reg _fsm_cond_20_69_2;
  reg _fsm_cond_20_69_3;
  reg _fsm_cond_20_69_4;
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
      valid_reg <= 0;
      _valid_reg_4_0_1 <= 0;
      _fsm_cond_4_1_1 <= 0;
      _valid_reg_4_2_1 <= 0;
      _valid_reg_4_2_2 <= 0;
      _fsm_cond_4_3_1 <= 0;
      _fsm_cond_4_3_2 <= 0;
      _valid_reg_4_4_1 <= 0;
      _valid_reg_4_4_2 <= 0;
      _valid_reg_4_4_3 <= 0;
      _fsm_cond_4_5_1 <= 0;
      _fsm_cond_4_5_2 <= 0;
      _fsm_cond_4_5_3 <= 0;
      _valid_reg_13_6_1 <= 0;
      _fsm_cond_13_7_1 <= 0;
      _valid_reg_13_8_1 <= 0;
      _valid_reg_13_8_2 <= 0;
      _fsm_cond_13_9_1 <= 0;
      _fsm_cond_13_9_2 <= 0;
      _valid_reg_13_10_1 <= 0;
      _valid_reg_13_10_2 <= 0;
      _valid_reg_13_10_3 <= 0;
      _fsm_cond_13_11_1 <= 0;
      _fsm_cond_13_11_2 <= 0;
      _fsm_cond_13_11_3 <= 0;
      _valid_reg_13_12_1 <= 0;
      _valid_reg_13_12_2 <= 0;
      _valid_reg_13_12_3 <= 0;
      _valid_reg_13_12_4 <= 0;
      _fsm_cond_13_13_1 <= 0;
      _fsm_cond_13_13_2 <= 0;
      _fsm_cond_13_13_3 <= 0;
      _fsm_cond_13_13_4 <= 0;
      _valid_reg_14_14_1 <= 0;
      _fsm_cond_14_15_1 <= 0;
      _valid_reg_14_16_1 <= 0;
      _valid_reg_14_16_2 <= 0;
      _fsm_cond_14_17_1 <= 0;
      _fsm_cond_14_17_2 <= 0;
      _valid_reg_14_18_1 <= 0;
      _valid_reg_14_18_2 <= 0;
      _valid_reg_14_18_3 <= 0;
      _fsm_cond_14_19_1 <= 0;
      _fsm_cond_14_19_2 <= 0;
      _fsm_cond_14_19_3 <= 0;
      _valid_reg_14_20_1 <= 0;
      _valid_reg_14_20_2 <= 0;
      _valid_reg_14_20_3 <= 0;
      _valid_reg_14_20_4 <= 0;
      _fsm_cond_14_21_1 <= 0;
      _fsm_cond_14_21_2 <= 0;
      _fsm_cond_14_21_3 <= 0;
      _fsm_cond_14_21_4 <= 0;
      _valid_reg_15_22_1 <= 0;
      _fsm_cond_15_23_1 <= 0;
      _valid_reg_15_24_1 <= 0;
      _valid_reg_15_24_2 <= 0;
      _fsm_cond_15_25_1 <= 0;
      _fsm_cond_15_25_2 <= 0;
      _valid_reg_15_26_1 <= 0;
      _valid_reg_15_26_2 <= 0;
      _valid_reg_15_26_3 <= 0;
      _fsm_cond_15_27_1 <= 0;
      _fsm_cond_15_27_2 <= 0;
      _fsm_cond_15_27_3 <= 0;
      _valid_reg_15_28_1 <= 0;
      _valid_reg_15_28_2 <= 0;
      _valid_reg_15_28_3 <= 0;
      _valid_reg_15_28_4 <= 0;
      _fsm_cond_15_29_1 <= 0;
      _fsm_cond_15_29_2 <= 0;
      _fsm_cond_15_29_3 <= 0;
      _fsm_cond_15_29_4 <= 0;
      _valid_reg_16_30_1 <= 0;
      _fsm_cond_16_31_1 <= 0;
      _valid_reg_16_32_1 <= 0;
      _valid_reg_16_32_2 <= 0;
      _fsm_cond_16_33_1 <= 0;
      _fsm_cond_16_33_2 <= 0;
      _valid_reg_16_34_1 <= 0;
      _valid_reg_16_34_2 <= 0;
      _valid_reg_16_34_3 <= 0;
      _fsm_cond_16_35_1 <= 0;
      _fsm_cond_16_35_2 <= 0;
      _fsm_cond_16_35_3 <= 0;
      _valid_reg_16_36_1 <= 0;
      _valid_reg_16_36_2 <= 0;
      _valid_reg_16_36_3 <= 0;
      _valid_reg_16_36_4 <= 0;
      _fsm_cond_16_37_1 <= 0;
      _fsm_cond_16_37_2 <= 0;
      _fsm_cond_16_37_3 <= 0;
      _fsm_cond_16_37_4 <= 0;
      _valid_reg_17_38_1 <= 0;
      _fsm_cond_17_39_1 <= 0;
      _valid_reg_17_40_1 <= 0;
      _valid_reg_17_40_2 <= 0;
      _fsm_cond_17_41_1 <= 0;
      _fsm_cond_17_41_2 <= 0;
      _valid_reg_17_42_1 <= 0;
      _valid_reg_17_42_2 <= 0;
      _valid_reg_17_42_3 <= 0;
      _fsm_cond_17_43_1 <= 0;
      _fsm_cond_17_43_2 <= 0;
      _fsm_cond_17_43_3 <= 0;
      _valid_reg_17_44_1 <= 0;
      _valid_reg_17_44_2 <= 0;
      _valid_reg_17_44_3 <= 0;
      _valid_reg_17_44_4 <= 0;
      _fsm_cond_17_45_1 <= 0;
      _fsm_cond_17_45_2 <= 0;
      _fsm_cond_17_45_3 <= 0;
      _fsm_cond_17_45_4 <= 0;
      _valid_reg_18_46_1 <= 0;
      _fsm_cond_18_47_1 <= 0;
      _valid_reg_18_48_1 <= 0;
      _valid_reg_18_48_2 <= 0;
      _fsm_cond_18_49_1 <= 0;
      _fsm_cond_18_49_2 <= 0;
      _valid_reg_18_50_1 <= 0;
      _valid_reg_18_50_2 <= 0;
      _valid_reg_18_50_3 <= 0;
      _fsm_cond_18_51_1 <= 0;
      _fsm_cond_18_51_2 <= 0;
      _fsm_cond_18_51_3 <= 0;
      _valid_reg_18_52_1 <= 0;
      _valid_reg_18_52_2 <= 0;
      _valid_reg_18_52_3 <= 0;
      _valid_reg_18_52_4 <= 0;
      _fsm_cond_18_53_1 <= 0;
      _fsm_cond_18_53_2 <= 0;
      _fsm_cond_18_53_3 <= 0;
      _fsm_cond_18_53_4 <= 0;
      _valid_reg_19_54_1 <= 0;
      _fsm_cond_19_55_1 <= 0;
      _valid_reg_19_56_1 <= 0;
      _valid_reg_19_56_2 <= 0;
      _fsm_cond_19_57_1 <= 0;
      _fsm_cond_19_57_2 <= 0;
      _valid_reg_19_58_1 <= 0;
      _valid_reg_19_58_2 <= 0;
      _valid_reg_19_58_3 <= 0;
      _fsm_cond_19_59_1 <= 0;
      _fsm_cond_19_59_2 <= 0;
      _fsm_cond_19_59_3 <= 0;
      _valid_reg_19_60_1 <= 0;
      _valid_reg_19_60_2 <= 0;
      _valid_reg_19_60_3 <= 0;
      _valid_reg_19_60_4 <= 0;
      _fsm_cond_19_61_1 <= 0;
      _fsm_cond_19_61_2 <= 0;
      _fsm_cond_19_61_3 <= 0;
      _fsm_cond_19_61_4 <= 0;
      _valid_reg_20_62_1 <= 0;
      _fsm_cond_20_63_1 <= 0;
      _valid_reg_20_64_1 <= 0;
      _valid_reg_20_64_2 <= 0;
      _fsm_cond_20_65_1 <= 0;
      _fsm_cond_20_65_2 <= 0;
      _valid_reg_20_66_1 <= 0;
      _valid_reg_20_66_2 <= 0;
      _valid_reg_20_66_3 <= 0;
      _fsm_cond_20_67_1 <= 0;
      _fsm_cond_20_67_2 <= 0;
      _fsm_cond_20_67_3 <= 0;
      _valid_reg_20_68_1 <= 0;
      _valid_reg_20_68_2 <= 0;
      _valid_reg_20_68_3 <= 0;
      _valid_reg_20_68_4 <= 0;
      _fsm_cond_20_69_1 <= 0;
      _fsm_cond_20_69_2 <= 0;
      _fsm_cond_20_69_3 <= 0;
      _fsm_cond_20_69_4 <= 0;
    end else begin
      count <= count + 1;
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;
      case(_d4_fsm)
        fsm_13: begin
          if(_fsm_cond_13_13_4) begin
            valid_reg <= _valid_reg_13_12_4;
          end 
        end
        fsm_14: begin
          if(_fsm_cond_14_21_4) begin
            valid_reg <= _valid_reg_14_20_4;
          end 
        end
        fsm_15: begin
          if(_fsm_cond_15_29_4) begin
            valid_reg <= _valid_reg_15_28_4;
          end 
        end
        fsm_16: begin
          if(_fsm_cond_16_37_4) begin
            valid_reg <= _valid_reg_16_36_4;
          end 
        end
        fsm_17: begin
          if(_fsm_cond_17_45_4) begin
            valid_reg <= _valid_reg_17_44_4;
          end 
        end
        fsm_18: begin
          if(_fsm_cond_18_53_4) begin
            valid_reg <= _valid_reg_18_52_4;
          end 
        end
        fsm_19: begin
          if(_fsm_cond_19_61_4) begin
            valid_reg <= _valid_reg_19_60_4;
          end 
        end
        fsm_20: begin
          if(_fsm_cond_20_69_4) begin
            valid_reg <= _valid_reg_20_68_4;
          end 
        end
      endcase
      case(_d3_fsm)
        fsm_4: begin
          if(_fsm_cond_4_5_3) begin
            valid_reg <= _valid_reg_4_4_3;
          end 
        end
        fsm_13: begin
          if(_fsm_cond_13_11_3) begin
            valid_reg <= _valid_reg_13_10_3;
          end 
          _valid_reg_13_12_4 <= _valid_reg_13_12_3;
          _fsm_cond_13_13_4 <= _fsm_cond_13_13_3;
        end
        fsm_14: begin
          if(_fsm_cond_14_19_3) begin
            valid_reg <= _valid_reg_14_18_3;
          end 
          _valid_reg_14_20_4 <= _valid_reg_14_20_3;
          _fsm_cond_14_21_4 <= _fsm_cond_14_21_3;
        end
        fsm_15: begin
          if(_fsm_cond_15_27_3) begin
            valid_reg <= _valid_reg_15_26_3;
          end 
          _valid_reg_15_28_4 <= _valid_reg_15_28_3;
          _fsm_cond_15_29_4 <= _fsm_cond_15_29_3;
        end
        fsm_16: begin
          if(_fsm_cond_16_35_3) begin
            valid_reg <= _valid_reg_16_34_3;
          end 
          _valid_reg_16_36_4 <= _valid_reg_16_36_3;
          _fsm_cond_16_37_4 <= _fsm_cond_16_37_3;
        end
        fsm_17: begin
          if(_fsm_cond_17_43_3) begin
            valid_reg <= _valid_reg_17_42_3;
          end 
          _valid_reg_17_44_4 <= _valid_reg_17_44_3;
          _fsm_cond_17_45_4 <= _fsm_cond_17_45_3;
        end
        fsm_18: begin
          if(_fsm_cond_18_51_3) begin
            valid_reg <= _valid_reg_18_50_3;
          end 
          _valid_reg_18_52_4 <= _valid_reg_18_52_3;
          _fsm_cond_18_53_4 <= _fsm_cond_18_53_3;
        end
        fsm_19: begin
          if(_fsm_cond_19_59_3) begin
            valid_reg <= _valid_reg_19_58_3;
          end 
          _valid_reg_19_60_4 <= _valid_reg_19_60_3;
          _fsm_cond_19_61_4 <= _fsm_cond_19_61_3;
        end
        fsm_20: begin
          if(_fsm_cond_20_67_3) begin
            valid_reg <= _valid_reg_20_66_3;
          end 
          _valid_reg_20_68_4 <= _valid_reg_20_68_3;
          _fsm_cond_20_69_4 <= _fsm_cond_20_69_3;
        end
      endcase
      case(_d2_fsm)
        fsm_4: begin
          if(_fsm_cond_4_3_2) begin
            valid_reg <= _valid_reg_4_2_2;
          end 
          _valid_reg_4_4_3 <= _valid_reg_4_4_2;
          _fsm_cond_4_5_3 <= _fsm_cond_4_5_2;
        end
        fsm_13: begin
          if(_fsm_cond_13_9_2) begin
            valid_reg <= _valid_reg_13_8_2;
          end 
          _valid_reg_13_10_3 <= _valid_reg_13_10_2;
          _fsm_cond_13_11_3 <= _fsm_cond_13_11_2;
          _valid_reg_13_12_3 <= _valid_reg_13_12_2;
          _fsm_cond_13_13_3 <= _fsm_cond_13_13_2;
        end
        fsm_14: begin
          if(_fsm_cond_14_17_2) begin
            valid_reg <= _valid_reg_14_16_2;
          end 
          _valid_reg_14_18_3 <= _valid_reg_14_18_2;
          _fsm_cond_14_19_3 <= _fsm_cond_14_19_2;
          _valid_reg_14_20_3 <= _valid_reg_14_20_2;
          _fsm_cond_14_21_3 <= _fsm_cond_14_21_2;
        end
        fsm_15: begin
          if(_fsm_cond_15_25_2) begin
            valid_reg <= _valid_reg_15_24_2;
          end 
          _valid_reg_15_26_3 <= _valid_reg_15_26_2;
          _fsm_cond_15_27_3 <= _fsm_cond_15_27_2;
          _valid_reg_15_28_3 <= _valid_reg_15_28_2;
          _fsm_cond_15_29_3 <= _fsm_cond_15_29_2;
        end
        fsm_16: begin
          if(_fsm_cond_16_33_2) begin
            valid_reg <= _valid_reg_16_32_2;
          end 
          _valid_reg_16_34_3 <= _valid_reg_16_34_2;
          _fsm_cond_16_35_3 <= _fsm_cond_16_35_2;
          _valid_reg_16_36_3 <= _valid_reg_16_36_2;
          _fsm_cond_16_37_3 <= _fsm_cond_16_37_2;
        end
        fsm_17: begin
          if(_fsm_cond_17_41_2) begin
            valid_reg <= _valid_reg_17_40_2;
          end 
          _valid_reg_17_42_3 <= _valid_reg_17_42_2;
          _fsm_cond_17_43_3 <= _fsm_cond_17_43_2;
          _valid_reg_17_44_3 <= _valid_reg_17_44_2;
          _fsm_cond_17_45_3 <= _fsm_cond_17_45_2;
        end
        fsm_18: begin
          if(_fsm_cond_18_49_2) begin
            valid_reg <= _valid_reg_18_48_2;
          end 
          _valid_reg_18_50_3 <= _valid_reg_18_50_2;
          _fsm_cond_18_51_3 <= _fsm_cond_18_51_2;
          _valid_reg_18_52_3 <= _valid_reg_18_52_2;
          _fsm_cond_18_53_3 <= _fsm_cond_18_53_2;
        end
        fsm_19: begin
          if(_fsm_cond_19_57_2) begin
            valid_reg <= _valid_reg_19_56_2;
          end 
          _valid_reg_19_58_3 <= _valid_reg_19_58_2;
          _fsm_cond_19_59_3 <= _fsm_cond_19_59_2;
          _valid_reg_19_60_3 <= _valid_reg_19_60_2;
          _fsm_cond_19_61_3 <= _fsm_cond_19_61_2;
        end
        fsm_20: begin
          if(_fsm_cond_20_65_2) begin
            valid_reg <= _valid_reg_20_64_2;
          end 
          _valid_reg_20_66_3 <= _valid_reg_20_66_2;
          _fsm_cond_20_67_3 <= _fsm_cond_20_67_2;
          _valid_reg_20_68_3 <= _valid_reg_20_68_2;
          _fsm_cond_20_69_3 <= _fsm_cond_20_69_2;
        end
      endcase
      case(_d1_fsm)
        fsm_4: begin
          if(_fsm_cond_4_1_1) begin
            valid_reg <= _valid_reg_4_0_1;
          end 
          _valid_reg_4_2_2 <= _valid_reg_4_2_1;
          _fsm_cond_4_3_2 <= _fsm_cond_4_3_1;
          _valid_reg_4_4_2 <= _valid_reg_4_4_1;
          _fsm_cond_4_5_2 <= _fsm_cond_4_5_1;
        end
        fsm_13: begin
          if(_fsm_cond_13_7_1) begin
            valid_reg <= _valid_reg_13_6_1;
          end 
          _valid_reg_13_8_2 <= _valid_reg_13_8_1;
          _fsm_cond_13_9_2 <= _fsm_cond_13_9_1;
          _valid_reg_13_10_2 <= _valid_reg_13_10_1;
          _fsm_cond_13_11_2 <= _fsm_cond_13_11_1;
          _valid_reg_13_12_2 <= _valid_reg_13_12_1;
          _fsm_cond_13_13_2 <= _fsm_cond_13_13_1;
        end
        fsm_14: begin
          if(_fsm_cond_14_15_1) begin
            valid_reg <= _valid_reg_14_14_1;
          end 
          _valid_reg_14_16_2 <= _valid_reg_14_16_1;
          _fsm_cond_14_17_2 <= _fsm_cond_14_17_1;
          _valid_reg_14_18_2 <= _valid_reg_14_18_1;
          _fsm_cond_14_19_2 <= _fsm_cond_14_19_1;
          _valid_reg_14_20_2 <= _valid_reg_14_20_1;
          _fsm_cond_14_21_2 <= _fsm_cond_14_21_1;
        end
        fsm_15: begin
          if(_fsm_cond_15_23_1) begin
            valid_reg <= _valid_reg_15_22_1;
          end 
          _valid_reg_15_24_2 <= _valid_reg_15_24_1;
          _fsm_cond_15_25_2 <= _fsm_cond_15_25_1;
          _valid_reg_15_26_2 <= _valid_reg_15_26_1;
          _fsm_cond_15_27_2 <= _fsm_cond_15_27_1;
          _valid_reg_15_28_2 <= _valid_reg_15_28_1;
          _fsm_cond_15_29_2 <= _fsm_cond_15_29_1;
        end
        fsm_16: begin
          if(_fsm_cond_16_31_1) begin
            valid_reg <= _valid_reg_16_30_1;
          end 
          _valid_reg_16_32_2 <= _valid_reg_16_32_1;
          _fsm_cond_16_33_2 <= _fsm_cond_16_33_1;
          _valid_reg_16_34_2 <= _valid_reg_16_34_1;
          _fsm_cond_16_35_2 <= _fsm_cond_16_35_1;
          _valid_reg_16_36_2 <= _valid_reg_16_36_1;
          _fsm_cond_16_37_2 <= _fsm_cond_16_37_1;
        end
        fsm_17: begin
          if(_fsm_cond_17_39_1) begin
            valid_reg <= _valid_reg_17_38_1;
          end 
          _valid_reg_17_40_2 <= _valid_reg_17_40_1;
          _fsm_cond_17_41_2 <= _fsm_cond_17_41_1;
          _valid_reg_17_42_2 <= _valid_reg_17_42_1;
          _fsm_cond_17_43_2 <= _fsm_cond_17_43_1;
          _valid_reg_17_44_2 <= _valid_reg_17_44_1;
          _fsm_cond_17_45_2 <= _fsm_cond_17_45_1;
        end
        fsm_18: begin
          if(_fsm_cond_18_47_1) begin
            valid_reg <= _valid_reg_18_46_1;
          end 
          _valid_reg_18_48_2 <= _valid_reg_18_48_1;
          _fsm_cond_18_49_2 <= _fsm_cond_18_49_1;
          _valid_reg_18_50_2 <= _valid_reg_18_50_1;
          _fsm_cond_18_51_2 <= _fsm_cond_18_51_1;
          _valid_reg_18_52_2 <= _valid_reg_18_52_1;
          _fsm_cond_18_53_2 <= _fsm_cond_18_53_1;
        end
        fsm_19: begin
          if(_fsm_cond_19_55_1) begin
            valid_reg <= _valid_reg_19_54_1;
          end 
          _valid_reg_19_56_2 <= _valid_reg_19_56_1;
          _fsm_cond_19_57_2 <= _fsm_cond_19_57_1;
          _valid_reg_19_58_2 <= _valid_reg_19_58_1;
          _fsm_cond_19_59_2 <= _fsm_cond_19_59_1;
          _valid_reg_19_60_2 <= _valid_reg_19_60_1;
          _fsm_cond_19_61_2 <= _fsm_cond_19_61_1;
        end
        fsm_20: begin
          if(_fsm_cond_20_63_1) begin
            valid_reg <= _valid_reg_20_62_1;
          end 
          _valid_reg_20_64_2 <= _valid_reg_20_64_1;
          _fsm_cond_20_65_2 <= _fsm_cond_20_65_1;
          _valid_reg_20_66_2 <= _valid_reg_20_66_1;
          _fsm_cond_20_67_2 <= _fsm_cond_20_67_1;
          _valid_reg_20_68_2 <= _valid_reg_20_68_1;
          _fsm_cond_20_69_2 <= _fsm_cond_20_69_1;
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
            valid_reg <= up;
          end 
          _valid_reg_4_0_1 <= up;
          _fsm_cond_4_1_1 <= count >= 16;
          _valid_reg_4_2_1 <= up;
          _fsm_cond_4_3_1 <= count >= 16;
          _valid_reg_4_4_1 <= down;
          _fsm_cond_4_5_1 <= count >= 16;
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
          _valid_reg_13_6_1 <= up;
          _fsm_cond_13_7_1 <= count >= 32;
          _valid_reg_13_8_1 <= up;
          _fsm_cond_13_9_1 <= count >= 32;
          _valid_reg_13_10_1 <= up;
          _fsm_cond_13_11_1 <= count >= 32;
          _valid_reg_13_12_1 <= down;
          _fsm_cond_13_13_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          _valid_reg_14_14_1 <= up;
          _fsm_cond_14_15_1 <= count >= 32;
          _valid_reg_14_16_1 <= up;
          _fsm_cond_14_17_1 <= count >= 32;
          _valid_reg_14_18_1 <= up;
          _fsm_cond_14_19_1 <= count >= 32;
          _valid_reg_14_20_1 <= down;
          _fsm_cond_14_21_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          _valid_reg_15_22_1 <= up;
          _fsm_cond_15_23_1 <= count >= 32;
          _valid_reg_15_24_1 <= up;
          _fsm_cond_15_25_1 <= count >= 32;
          _valid_reg_15_26_1 <= up;
          _fsm_cond_15_27_1 <= count >= 32;
          _valid_reg_15_28_1 <= down;
          _fsm_cond_15_29_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          _valid_reg_16_30_1 <= up;
          _fsm_cond_16_31_1 <= count >= 32;
          _valid_reg_16_32_1 <= up;
          _fsm_cond_16_33_1 <= count >= 32;
          _valid_reg_16_34_1 <= up;
          _fsm_cond_16_35_1 <= count >= 32;
          _valid_reg_16_36_1 <= down;
          _fsm_cond_16_37_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          _valid_reg_17_38_1 <= up;
          _fsm_cond_17_39_1 <= count >= 32;
          _valid_reg_17_40_1 <= up;
          _fsm_cond_17_41_1 <= count >= 32;
          _valid_reg_17_42_1 <= up;
          _fsm_cond_17_43_1 <= count >= 32;
          _valid_reg_17_44_1 <= down;
          _fsm_cond_17_45_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          _valid_reg_18_46_1 <= up;
          _fsm_cond_18_47_1 <= count >= 32;
          _valid_reg_18_48_1 <= up;
          _fsm_cond_18_49_1 <= count >= 32;
          _valid_reg_18_50_1 <= up;
          _fsm_cond_18_51_1 <= count >= 32;
          _valid_reg_18_52_1 <= down;
          _fsm_cond_18_53_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          _valid_reg_19_54_1 <= up;
          _fsm_cond_19_55_1 <= count >= 32;
          _valid_reg_19_56_1 <= up;
          _fsm_cond_19_57_1 <= count >= 32;
          _valid_reg_19_58_1 <= up;
          _fsm_cond_19_59_1 <= count >= 32;
          _valid_reg_19_60_1 <= down;
          _fsm_cond_19_61_1 <= count >= 32;
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          _valid_reg_20_62_1 <= up;
          _fsm_cond_20_63_1 <= count >= 32;
          _valid_reg_20_64_1 <= up;
          _fsm_cond_20_65_1 <= count >= 32;
          _valid_reg_20_66_1 <= up;
          _fsm_cond_20_67_1 <= count >= 32;
          _valid_reg_20_68_1 <= down;
          _fsm_cond_20_69_1 <= count >= 32;
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
    test_module = fsm_delayed_eager_val.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
