import led

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
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
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
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  reg [32-1:0] _d1_fsm;
  reg [8-1:0] _valid_reg_4_1_0;
  reg _fsm_cond_4_1_1;
  reg [32-1:0] _d2_fsm;
  reg [8-1:0] _valid_reg_4_2_2;
  reg [8-1:0] _valid_reg_4_2_3;
  reg _fsm_cond_4_2_4;
  reg _fsm_cond_4_2_5;
  reg [32-1:0] _d3_fsm;
  reg [8-1:0] _valid_reg_4_3_6;
  reg [8-1:0] _valid_reg_4_3_7;
  reg [8-1:0] _valid_reg_4_3_8;
  reg _fsm_cond_4_3_9;
  reg _fsm_cond_4_3_10;
  reg _fsm_cond_4_3_11;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  reg [8-1:0] _valid_reg_13_1_12;
  reg _fsm_cond_13_1_13;
  reg [8-1:0] _valid_reg_13_2_14;
  reg [8-1:0] _valid_reg_13_2_15;
  reg _fsm_cond_13_2_16;
  reg _fsm_cond_13_2_17;
  reg [8-1:0] _valid_reg_13_3_18;
  reg [8-1:0] _valid_reg_13_3_19;
  reg [8-1:0] _valid_reg_13_3_20;
  reg _fsm_cond_13_3_21;
  reg _fsm_cond_13_3_22;
  reg _fsm_cond_13_3_23;
  reg [32-1:0] _d4_fsm;
  reg [8-1:0] _valid_reg_13_4_24;
  reg [8-1:0] _valid_reg_13_4_25;
  reg [8-1:0] _valid_reg_13_4_26;
  reg [8-1:0] _valid_reg_13_4_27;
  reg _fsm_cond_13_4_28;
  reg _fsm_cond_13_4_29;
  reg _fsm_cond_13_4_30;
  reg _fsm_cond_13_4_31;
  localparam fsm_14 = 14;
  reg [8-1:0] _valid_reg_14_1_32;
  reg _fsm_cond_14_1_33;
  reg [8-1:0] _valid_reg_14_2_34;
  reg [8-1:0] _valid_reg_14_2_35;
  reg _fsm_cond_14_2_36;
  reg _fsm_cond_14_2_37;
  reg [8-1:0] _valid_reg_14_3_38;
  reg [8-1:0] _valid_reg_14_3_39;
  reg [8-1:0] _valid_reg_14_3_40;
  reg _fsm_cond_14_3_41;
  reg _fsm_cond_14_3_42;
  reg _fsm_cond_14_3_43;
  reg [8-1:0] _valid_reg_14_4_44;
  reg [8-1:0] _valid_reg_14_4_45;
  reg [8-1:0] _valid_reg_14_4_46;
  reg [8-1:0] _valid_reg_14_4_47;
  reg _fsm_cond_14_4_48;
  reg _fsm_cond_14_4_49;
  reg _fsm_cond_14_4_50;
  reg _fsm_cond_14_4_51;
  localparam fsm_15 = 15;
  reg [8-1:0] _valid_reg_15_1_52;
  reg _fsm_cond_15_1_53;
  reg [8-1:0] _valid_reg_15_2_54;
  reg [8-1:0] _valid_reg_15_2_55;
  reg _fsm_cond_15_2_56;
  reg _fsm_cond_15_2_57;
  reg [8-1:0] _valid_reg_15_3_58;
  reg [8-1:0] _valid_reg_15_3_59;
  reg [8-1:0] _valid_reg_15_3_60;
  reg _fsm_cond_15_3_61;
  reg _fsm_cond_15_3_62;
  reg _fsm_cond_15_3_63;
  reg [8-1:0] _valid_reg_15_4_64;
  reg [8-1:0] _valid_reg_15_4_65;
  reg [8-1:0] _valid_reg_15_4_66;
  reg [8-1:0] _valid_reg_15_4_67;
  reg _fsm_cond_15_4_68;
  reg _fsm_cond_15_4_69;
  reg _fsm_cond_15_4_70;
  reg _fsm_cond_15_4_71;
  localparam fsm_16 = 16;
  reg [8-1:0] _valid_reg_16_1_72;
  reg _fsm_cond_16_1_73;
  reg [8-1:0] _valid_reg_16_2_74;
  reg [8-1:0] _valid_reg_16_2_75;
  reg _fsm_cond_16_2_76;
  reg _fsm_cond_16_2_77;
  reg [8-1:0] _valid_reg_16_3_78;
  reg [8-1:0] _valid_reg_16_3_79;
  reg [8-1:0] _valid_reg_16_3_80;
  reg _fsm_cond_16_3_81;
  reg _fsm_cond_16_3_82;
  reg _fsm_cond_16_3_83;
  reg [8-1:0] _valid_reg_16_4_84;
  reg [8-1:0] _valid_reg_16_4_85;
  reg [8-1:0] _valid_reg_16_4_86;
  reg [8-1:0] _valid_reg_16_4_87;
  reg _fsm_cond_16_4_88;
  reg _fsm_cond_16_4_89;
  reg _fsm_cond_16_4_90;
  reg _fsm_cond_16_4_91;
  localparam fsm_17 = 17;
  reg [8-1:0] _valid_reg_17_1_92;
  reg _fsm_cond_17_1_93;
  reg [8-1:0] _valid_reg_17_2_94;
  reg [8-1:0] _valid_reg_17_2_95;
  reg _fsm_cond_17_2_96;
  reg _fsm_cond_17_2_97;
  reg [8-1:0] _valid_reg_17_3_98;
  reg [8-1:0] _valid_reg_17_3_99;
  reg [8-1:0] _valid_reg_17_3_100;
  reg _fsm_cond_17_3_101;
  reg _fsm_cond_17_3_102;
  reg _fsm_cond_17_3_103;
  reg [8-1:0] _valid_reg_17_4_104;
  reg [8-1:0] _valid_reg_17_4_105;
  reg [8-1:0] _valid_reg_17_4_106;
  reg [8-1:0] _valid_reg_17_4_107;
  reg _fsm_cond_17_4_108;
  reg _fsm_cond_17_4_109;
  reg _fsm_cond_17_4_110;
  reg _fsm_cond_17_4_111;
  localparam fsm_18 = 18;
  reg [8-1:0] _valid_reg_18_1_112;
  reg _fsm_cond_18_1_113;
  reg [8-1:0] _valid_reg_18_2_114;
  reg [8-1:0] _valid_reg_18_2_115;
  reg _fsm_cond_18_2_116;
  reg _fsm_cond_18_2_117;
  reg [8-1:0] _valid_reg_18_3_118;
  reg [8-1:0] _valid_reg_18_3_119;
  reg [8-1:0] _valid_reg_18_3_120;
  reg _fsm_cond_18_3_121;
  reg _fsm_cond_18_3_122;
  reg _fsm_cond_18_3_123;
  reg [8-1:0] _valid_reg_18_4_124;
  reg [8-1:0] _valid_reg_18_4_125;
  reg [8-1:0] _valid_reg_18_4_126;
  reg [8-1:0] _valid_reg_18_4_127;
  reg _fsm_cond_18_4_128;
  reg _fsm_cond_18_4_129;
  reg _fsm_cond_18_4_130;
  reg _fsm_cond_18_4_131;
  localparam fsm_19 = 19;
  reg [8-1:0] _valid_reg_19_1_132;
  reg _fsm_cond_19_1_133;
  reg [8-1:0] _valid_reg_19_2_134;
  reg [8-1:0] _valid_reg_19_2_135;
  reg _fsm_cond_19_2_136;
  reg _fsm_cond_19_2_137;
  reg [8-1:0] _valid_reg_19_3_138;
  reg [8-1:0] _valid_reg_19_3_139;
  reg [8-1:0] _valid_reg_19_3_140;
  reg _fsm_cond_19_3_141;
  reg _fsm_cond_19_3_142;
  reg _fsm_cond_19_3_143;
  reg [8-1:0] _valid_reg_19_4_144;
  reg [8-1:0] _valid_reg_19_4_145;
  reg [8-1:0] _valid_reg_19_4_146;
  reg [8-1:0] _valid_reg_19_4_147;
  reg _fsm_cond_19_4_148;
  reg _fsm_cond_19_4_149;
  reg _fsm_cond_19_4_150;
  reg _fsm_cond_19_4_151;
  localparam fsm_20 = 20;
  reg [8-1:0] _valid_reg_20_1_152;
  reg _fsm_cond_20_1_153;
  reg [8-1:0] _valid_reg_20_2_154;
  reg [8-1:0] _valid_reg_20_2_155;
  reg _fsm_cond_20_2_156;
  reg _fsm_cond_20_2_157;
  reg [8-1:0] _valid_reg_20_3_158;
  reg [8-1:0] _valid_reg_20_3_159;
  reg [8-1:0] _valid_reg_20_3_160;
  reg _fsm_cond_20_3_161;
  reg _fsm_cond_20_3_162;
  reg _fsm_cond_20_3_163;
  reg [8-1:0] _valid_reg_20_4_164;
  reg [8-1:0] _valid_reg_20_4_165;
  reg [8-1:0] _valid_reg_20_4_166;
  reg [8-1:0] _valid_reg_20_4_167;
  reg _fsm_cond_20_4_168;
  reg _fsm_cond_20_4_169;
  reg _fsm_cond_20_4_170;
  reg _fsm_cond_20_4_171;
  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      valid_reg <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _valid_reg_4_1_0 <= 0;
      _fsm_cond_4_1_1 <= 0;
      _d2_fsm <= fsm_init;
      _valid_reg_4_2_2 <= 0;
      _valid_reg_4_2_3 <= 0;
      _fsm_cond_4_2_4 <= 0;
      _fsm_cond_4_2_5 <= 0;
      _d3_fsm <= fsm_init;
      _valid_reg_4_3_6 <= 0;
      _valid_reg_4_3_7 <= 0;
      _valid_reg_4_3_8 <= 0;
      _fsm_cond_4_3_9 <= 0;
      _fsm_cond_4_3_10 <= 0;
      _fsm_cond_4_3_11 <= 0;
      _valid_reg_13_1_12 <= 0;
      _fsm_cond_13_1_13 <= 0;
      _valid_reg_13_2_14 <= 0;
      _valid_reg_13_2_15 <= 0;
      _fsm_cond_13_2_16 <= 0;
      _fsm_cond_13_2_17 <= 0;
      _valid_reg_13_3_18 <= 0;
      _valid_reg_13_3_19 <= 0;
      _valid_reg_13_3_20 <= 0;
      _fsm_cond_13_3_21 <= 0;
      _fsm_cond_13_3_22 <= 0;
      _fsm_cond_13_3_23 <= 0;
      _d4_fsm <= fsm_init;
      _valid_reg_13_4_24 <= 0;
      _valid_reg_13_4_25 <= 0;
      _valid_reg_13_4_26 <= 0;
      _valid_reg_13_4_27 <= 0;
      _fsm_cond_13_4_28 <= 0;
      _fsm_cond_13_4_29 <= 0;
      _fsm_cond_13_4_30 <= 0;
      _fsm_cond_13_4_31 <= 0;
      _valid_reg_14_1_32 <= 0;
      _fsm_cond_14_1_33 <= 0;
      _valid_reg_14_2_34 <= 0;
      _valid_reg_14_2_35 <= 0;
      _fsm_cond_14_2_36 <= 0;
      _fsm_cond_14_2_37 <= 0;
      _valid_reg_14_3_38 <= 0;
      _valid_reg_14_3_39 <= 0;
      _valid_reg_14_3_40 <= 0;
      _fsm_cond_14_3_41 <= 0;
      _fsm_cond_14_3_42 <= 0;
      _fsm_cond_14_3_43 <= 0;
      _valid_reg_14_4_44 <= 0;
      _valid_reg_14_4_45 <= 0;
      _valid_reg_14_4_46 <= 0;
      _valid_reg_14_4_47 <= 0;
      _fsm_cond_14_4_48 <= 0;
      _fsm_cond_14_4_49 <= 0;
      _fsm_cond_14_4_50 <= 0;
      _fsm_cond_14_4_51 <= 0;
      _valid_reg_15_1_52 <= 0;
      _fsm_cond_15_1_53 <= 0;
      _valid_reg_15_2_54 <= 0;
      _valid_reg_15_2_55 <= 0;
      _fsm_cond_15_2_56 <= 0;
      _fsm_cond_15_2_57 <= 0;
      _valid_reg_15_3_58 <= 0;
      _valid_reg_15_3_59 <= 0;
      _valid_reg_15_3_60 <= 0;
      _fsm_cond_15_3_61 <= 0;
      _fsm_cond_15_3_62 <= 0;
      _fsm_cond_15_3_63 <= 0;
      _valid_reg_15_4_64 <= 0;
      _valid_reg_15_4_65 <= 0;
      _valid_reg_15_4_66 <= 0;
      _valid_reg_15_4_67 <= 0;
      _fsm_cond_15_4_68 <= 0;
      _fsm_cond_15_4_69 <= 0;
      _fsm_cond_15_4_70 <= 0;
      _fsm_cond_15_4_71 <= 0;
      _valid_reg_16_1_72 <= 0;
      _fsm_cond_16_1_73 <= 0;
      _valid_reg_16_2_74 <= 0;
      _valid_reg_16_2_75 <= 0;
      _fsm_cond_16_2_76 <= 0;
      _fsm_cond_16_2_77 <= 0;
      _valid_reg_16_3_78 <= 0;
      _valid_reg_16_3_79 <= 0;
      _valid_reg_16_3_80 <= 0;
      _fsm_cond_16_3_81 <= 0;
      _fsm_cond_16_3_82 <= 0;
      _fsm_cond_16_3_83 <= 0;
      _valid_reg_16_4_84 <= 0;
      _valid_reg_16_4_85 <= 0;
      _valid_reg_16_4_86 <= 0;
      _valid_reg_16_4_87 <= 0;
      _fsm_cond_16_4_88 <= 0;
      _fsm_cond_16_4_89 <= 0;
      _fsm_cond_16_4_90 <= 0;
      _fsm_cond_16_4_91 <= 0;
      _valid_reg_17_1_92 <= 0;
      _fsm_cond_17_1_93 <= 0;
      _valid_reg_17_2_94 <= 0;
      _valid_reg_17_2_95 <= 0;
      _fsm_cond_17_2_96 <= 0;
      _fsm_cond_17_2_97 <= 0;
      _valid_reg_17_3_98 <= 0;
      _valid_reg_17_3_99 <= 0;
      _valid_reg_17_3_100 <= 0;
      _fsm_cond_17_3_101 <= 0;
      _fsm_cond_17_3_102 <= 0;
      _fsm_cond_17_3_103 <= 0;
      _valid_reg_17_4_104 <= 0;
      _valid_reg_17_4_105 <= 0;
      _valid_reg_17_4_106 <= 0;
      _valid_reg_17_4_107 <= 0;
      _fsm_cond_17_4_108 <= 0;
      _fsm_cond_17_4_109 <= 0;
      _fsm_cond_17_4_110 <= 0;
      _fsm_cond_17_4_111 <= 0;
      _valid_reg_18_1_112 <= 0;
      _fsm_cond_18_1_113 <= 0;
      _valid_reg_18_2_114 <= 0;
      _valid_reg_18_2_115 <= 0;
      _fsm_cond_18_2_116 <= 0;
      _fsm_cond_18_2_117 <= 0;
      _valid_reg_18_3_118 <= 0;
      _valid_reg_18_3_119 <= 0;
      _valid_reg_18_3_120 <= 0;
      _fsm_cond_18_3_121 <= 0;
      _fsm_cond_18_3_122 <= 0;
      _fsm_cond_18_3_123 <= 0;
      _valid_reg_18_4_124 <= 0;
      _valid_reg_18_4_125 <= 0;
      _valid_reg_18_4_126 <= 0;
      _valid_reg_18_4_127 <= 0;
      _fsm_cond_18_4_128 <= 0;
      _fsm_cond_18_4_129 <= 0;
      _fsm_cond_18_4_130 <= 0;
      _fsm_cond_18_4_131 <= 0;
      _valid_reg_19_1_132 <= 0;
      _fsm_cond_19_1_133 <= 0;
      _valid_reg_19_2_134 <= 0;
      _valid_reg_19_2_135 <= 0;
      _fsm_cond_19_2_136 <= 0;
      _fsm_cond_19_2_137 <= 0;
      _valid_reg_19_3_138 <= 0;
      _valid_reg_19_3_139 <= 0;
      _valid_reg_19_3_140 <= 0;
      _fsm_cond_19_3_141 <= 0;
      _fsm_cond_19_3_142 <= 0;
      _fsm_cond_19_3_143 <= 0;
      _valid_reg_19_4_144 <= 0;
      _valid_reg_19_4_145 <= 0;
      _valid_reg_19_4_146 <= 0;
      _valid_reg_19_4_147 <= 0;
      _fsm_cond_19_4_148 <= 0;
      _fsm_cond_19_4_149 <= 0;
      _fsm_cond_19_4_150 <= 0;
      _fsm_cond_19_4_151 <= 0;
      _valid_reg_20_1_152 <= 0;
      _fsm_cond_20_1_153 <= 0;
      _valid_reg_20_2_154 <= 0;
      _valid_reg_20_2_155 <= 0;
      _fsm_cond_20_2_156 <= 0;
      _fsm_cond_20_2_157 <= 0;
      _valid_reg_20_3_158 <= 0;
      _valid_reg_20_3_159 <= 0;
      _valid_reg_20_3_160 <= 0;
      _fsm_cond_20_3_161 <= 0;
      _fsm_cond_20_3_162 <= 0;
      _fsm_cond_20_3_163 <= 0;
      _valid_reg_20_4_164 <= 0;
      _valid_reg_20_4_165 <= 0;
      _valid_reg_20_4_166 <= 0;
      _valid_reg_20_4_167 <= 0;
      _fsm_cond_20_4_168 <= 0;
      _fsm_cond_20_4_169 <= 0;
      _fsm_cond_20_4_170 <= 0;
      _fsm_cond_20_4_171 <= 0;
    end else begin
      count <= (count + 1);
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;
      case(_d4_fsm)
        fsm_13: begin
          if(_fsm_cond_13_4_31) begin
            valid_reg <= _valid_reg_13_4_27;
          end 
        end
        fsm_14: begin
          if(_fsm_cond_14_4_51) begin
            valid_reg <= _valid_reg_14_4_47;
          end 
        end
        fsm_15: begin
          if(_fsm_cond_15_4_71) begin
            valid_reg <= _valid_reg_15_4_67;
          end 
        end
        fsm_16: begin
          if(_fsm_cond_16_4_91) begin
            valid_reg <= _valid_reg_16_4_87;
          end 
        end
        fsm_17: begin
          if(_fsm_cond_17_4_111) begin
            valid_reg <= _valid_reg_17_4_107;
          end 
        end
        fsm_18: begin
          if(_fsm_cond_18_4_131) begin
            valid_reg <= _valid_reg_18_4_127;
          end 
        end
        fsm_19: begin
          if(_fsm_cond_19_4_151) begin
            valid_reg <= _valid_reg_19_4_147;
          end 
        end
        fsm_20: begin
          if(_fsm_cond_20_4_171) begin
            valid_reg <= _valid_reg_20_4_167;
          end 
        end
      endcase
      case(_d3_fsm)
        fsm_4: begin
          if(_fsm_cond_4_3_11) begin
            valid_reg <= _valid_reg_4_3_8;
          end 
        end
        fsm_13: begin
          if(_fsm_cond_13_3_23) begin
            valid_reg <= _valid_reg_13_3_20;
          end 
          _valid_reg_13_4_27 <= _valid_reg_13_4_26;
          _fsm_cond_13_4_31 <= _fsm_cond_13_4_30;
        end
        fsm_14: begin
          if(_fsm_cond_14_3_43) begin
            valid_reg <= _valid_reg_14_3_40;
          end 
          _valid_reg_14_4_47 <= _valid_reg_14_4_46;
          _fsm_cond_14_4_51 <= _fsm_cond_14_4_50;
        end
        fsm_15: begin
          if(_fsm_cond_15_3_63) begin
            valid_reg <= _valid_reg_15_3_60;
          end 
          _valid_reg_15_4_67 <= _valid_reg_15_4_66;
          _fsm_cond_15_4_71 <= _fsm_cond_15_4_70;
        end
        fsm_16: begin
          if(_fsm_cond_16_3_83) begin
            valid_reg <= _valid_reg_16_3_80;
          end 
          _valid_reg_16_4_87 <= _valid_reg_16_4_86;
          _fsm_cond_16_4_91 <= _fsm_cond_16_4_90;
        end
        fsm_17: begin
          if(_fsm_cond_17_3_103) begin
            valid_reg <= _valid_reg_17_3_100;
          end 
          _valid_reg_17_4_107 <= _valid_reg_17_4_106;
          _fsm_cond_17_4_111 <= _fsm_cond_17_4_110;
        end
        fsm_18: begin
          if(_fsm_cond_18_3_123) begin
            valid_reg <= _valid_reg_18_3_120;
          end 
          _valid_reg_18_4_127 <= _valid_reg_18_4_126;
          _fsm_cond_18_4_131 <= _fsm_cond_18_4_130;
        end
        fsm_19: begin
          if(_fsm_cond_19_3_143) begin
            valid_reg <= _valid_reg_19_3_140;
          end 
          _valid_reg_19_4_147 <= _valid_reg_19_4_146;
          _fsm_cond_19_4_151 <= _fsm_cond_19_4_150;
        end
        fsm_20: begin
          if(_fsm_cond_20_3_163) begin
            valid_reg <= _valid_reg_20_3_160;
          end 
          _valid_reg_20_4_167 <= _valid_reg_20_4_166;
          _fsm_cond_20_4_171 <= _fsm_cond_20_4_170;
        end
      endcase
      case(_d2_fsm)
        fsm_4: begin
          if(_fsm_cond_4_2_5) begin
            valid_reg <= _valid_reg_4_2_3;
          end 
          _valid_reg_4_3_8 <= _valid_reg_4_3_7;
          _fsm_cond_4_3_11 <= _fsm_cond_4_3_10;
        end
        fsm_13: begin
          if(_fsm_cond_13_2_17) begin
            valid_reg <= _valid_reg_13_2_15;
          end 
          _valid_reg_13_3_20 <= _valid_reg_13_3_19;
          _fsm_cond_13_3_23 <= _fsm_cond_13_3_22;
          _valid_reg_13_4_26 <= _valid_reg_13_4_25;
          _fsm_cond_13_4_30 <= _fsm_cond_13_4_29;
        end
        fsm_14: begin
          if(_fsm_cond_14_2_37) begin
            valid_reg <= _valid_reg_14_2_35;
          end 
          _valid_reg_14_3_40 <= _valid_reg_14_3_39;
          _fsm_cond_14_3_43 <= _fsm_cond_14_3_42;
          _valid_reg_14_4_46 <= _valid_reg_14_4_45;
          _fsm_cond_14_4_50 <= _fsm_cond_14_4_49;
        end
        fsm_15: begin
          if(_fsm_cond_15_2_57) begin
            valid_reg <= _valid_reg_15_2_55;
          end 
          _valid_reg_15_3_60 <= _valid_reg_15_3_59;
          _fsm_cond_15_3_63 <= _fsm_cond_15_3_62;
          _valid_reg_15_4_66 <= _valid_reg_15_4_65;
          _fsm_cond_15_4_70 <= _fsm_cond_15_4_69;
        end
        fsm_16: begin
          if(_fsm_cond_16_2_77) begin
            valid_reg <= _valid_reg_16_2_75;
          end 
          _valid_reg_16_3_80 <= _valid_reg_16_3_79;
          _fsm_cond_16_3_83 <= _fsm_cond_16_3_82;
          _valid_reg_16_4_86 <= _valid_reg_16_4_85;
          _fsm_cond_16_4_90 <= _fsm_cond_16_4_89;
        end
        fsm_17: begin
          if(_fsm_cond_17_2_97) begin
            valid_reg <= _valid_reg_17_2_95;
          end 
          _valid_reg_17_3_100 <= _valid_reg_17_3_99;
          _fsm_cond_17_3_103 <= _fsm_cond_17_3_102;
          _valid_reg_17_4_106 <= _valid_reg_17_4_105;
          _fsm_cond_17_4_110 <= _fsm_cond_17_4_109;
        end
        fsm_18: begin
          if(_fsm_cond_18_2_117) begin
            valid_reg <= _valid_reg_18_2_115;
          end 
          _valid_reg_18_3_120 <= _valid_reg_18_3_119;
          _fsm_cond_18_3_123 <= _fsm_cond_18_3_122;
          _valid_reg_18_4_126 <= _valid_reg_18_4_125;
          _fsm_cond_18_4_130 <= _fsm_cond_18_4_129;
        end
        fsm_19: begin
          if(_fsm_cond_19_2_137) begin
            valid_reg <= _valid_reg_19_2_135;
          end 
          _valid_reg_19_3_140 <= _valid_reg_19_3_139;
          _fsm_cond_19_3_143 <= _fsm_cond_19_3_142;
          _valid_reg_19_4_146 <= _valid_reg_19_4_145;
          _fsm_cond_19_4_150 <= _fsm_cond_19_4_149;
        end
        fsm_20: begin
          if(_fsm_cond_20_2_157) begin
            valid_reg <= _valid_reg_20_2_155;
          end 
          _valid_reg_20_3_160 <= _valid_reg_20_3_159;
          _fsm_cond_20_3_163 <= _fsm_cond_20_3_162;
          _valid_reg_20_4_166 <= _valid_reg_20_4_165;
          _fsm_cond_20_4_170 <= _fsm_cond_20_4_169;
        end
      endcase
      case(_d1_fsm)
        fsm_4: begin
          if(_fsm_cond_4_1_1) begin
            valid_reg <= _valid_reg_4_1_0;
          end 
          _valid_reg_4_2_3 <= _valid_reg_4_2_2;
          _fsm_cond_4_2_5 <= _fsm_cond_4_2_4;
          _valid_reg_4_3_7 <= _valid_reg_4_3_6;
          _fsm_cond_4_3_10 <= _fsm_cond_4_3_9;
        end
        fsm_13: begin
          if(_fsm_cond_13_1_13) begin
            valid_reg <= _valid_reg_13_1_12;
          end 
          _valid_reg_13_2_15 <= _valid_reg_13_2_14;
          _fsm_cond_13_2_17 <= _fsm_cond_13_2_16;
          _valid_reg_13_3_19 <= _valid_reg_13_3_18;
          _fsm_cond_13_3_22 <= _fsm_cond_13_3_21;
          _valid_reg_13_4_25 <= _valid_reg_13_4_24;
          _fsm_cond_13_4_29 <= _fsm_cond_13_4_28;
        end
        fsm_14: begin
          if(_fsm_cond_14_1_33) begin
            valid_reg <= _valid_reg_14_1_32;
          end 
          _valid_reg_14_2_35 <= _valid_reg_14_2_34;
          _fsm_cond_14_2_37 <= _fsm_cond_14_2_36;
          _valid_reg_14_3_39 <= _valid_reg_14_3_38;
          _fsm_cond_14_3_42 <= _fsm_cond_14_3_41;
          _valid_reg_14_4_45 <= _valid_reg_14_4_44;
          _fsm_cond_14_4_49 <= _fsm_cond_14_4_48;
        end
        fsm_15: begin
          if(_fsm_cond_15_1_53) begin
            valid_reg <= _valid_reg_15_1_52;
          end 
          _valid_reg_15_2_55 <= _valid_reg_15_2_54;
          _fsm_cond_15_2_57 <= _fsm_cond_15_2_56;
          _valid_reg_15_3_59 <= _valid_reg_15_3_58;
          _fsm_cond_15_3_62 <= _fsm_cond_15_3_61;
          _valid_reg_15_4_65 <= _valid_reg_15_4_64;
          _fsm_cond_15_4_69 <= _fsm_cond_15_4_68;
        end
        fsm_16: begin
          if(_fsm_cond_16_1_73) begin
            valid_reg <= _valid_reg_16_1_72;
          end 
          _valid_reg_16_2_75 <= _valid_reg_16_2_74;
          _fsm_cond_16_2_77 <= _fsm_cond_16_2_76;
          _valid_reg_16_3_79 <= _valid_reg_16_3_78;
          _fsm_cond_16_3_82 <= _fsm_cond_16_3_81;
          _valid_reg_16_4_85 <= _valid_reg_16_4_84;
          _fsm_cond_16_4_89 <= _fsm_cond_16_4_88;
        end
        fsm_17: begin
          if(_fsm_cond_17_1_93) begin
            valid_reg <= _valid_reg_17_1_92;
          end 
          _valid_reg_17_2_95 <= _valid_reg_17_2_94;
          _fsm_cond_17_2_97 <= _fsm_cond_17_2_96;
          _valid_reg_17_3_99 <= _valid_reg_17_3_98;
          _fsm_cond_17_3_102 <= _fsm_cond_17_3_101;
          _valid_reg_17_4_105 <= _valid_reg_17_4_104;
          _fsm_cond_17_4_109 <= _fsm_cond_17_4_108;
        end
        fsm_18: begin
          if(_fsm_cond_18_1_113) begin
            valid_reg <= _valid_reg_18_1_112;
          end 
          _valid_reg_18_2_115 <= _valid_reg_18_2_114;
          _fsm_cond_18_2_117 <= _fsm_cond_18_2_116;
          _valid_reg_18_3_119 <= _valid_reg_18_3_118;
          _fsm_cond_18_3_122 <= _fsm_cond_18_3_121;
          _valid_reg_18_4_125 <= _valid_reg_18_4_124;
          _fsm_cond_18_4_129 <= _fsm_cond_18_4_128;
        end
        fsm_19: begin
          if(_fsm_cond_19_1_133) begin
            valid_reg <= _valid_reg_19_1_132;
          end 
          _valid_reg_19_2_135 <= _valid_reg_19_2_134;
          _fsm_cond_19_2_137 <= _fsm_cond_19_2_136;
          _valid_reg_19_3_139 <= _valid_reg_19_3_138;
          _fsm_cond_19_3_142 <= _fsm_cond_19_3_141;
          _valid_reg_19_4_145 <= _valid_reg_19_4_144;
          _fsm_cond_19_4_149 <= _fsm_cond_19_4_148;
        end
        fsm_20: begin
          if(_fsm_cond_20_1_153) begin
            valid_reg <= _valid_reg_20_1_152;
          end 
          _valid_reg_20_2_155 <= _valid_reg_20_2_154;
          _fsm_cond_20_2_157 <= _fsm_cond_20_2_156;
          _valid_reg_20_3_159 <= _valid_reg_20_3_158;
          _fsm_cond_20_3_162 <= _fsm_cond_20_3_161;
          _valid_reg_20_4_165 <= _valid_reg_20_4_164;
          _fsm_cond_20_4_169 <= _fsm_cond_20_4_168;
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
          _valid_reg_4_1_0 <= up;
          _fsm_cond_4_1_1 <= (count >= 16);
          _valid_reg_4_2_2 <= up;
          _fsm_cond_4_2_4 <= (count >= 16);
          _valid_reg_4_3_6 <= down;
          _fsm_cond_4_3_9 <= (count >= 16);
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
          _valid_reg_13_1_12 <= up;
          _fsm_cond_13_1_13 <= (count >= 32);
          _valid_reg_13_2_14 <= up;
          _fsm_cond_13_2_16 <= (count >= 32);
          _valid_reg_13_3_18 <= up;
          _fsm_cond_13_3_21 <= (count >= 32);
          _valid_reg_13_4_24 <= down;
          _fsm_cond_13_4_28 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          _valid_reg_14_1_32 <= up;
          _fsm_cond_14_1_33 <= (count >= 32);
          _valid_reg_14_2_34 <= up;
          _fsm_cond_14_2_36 <= (count >= 32);
          _valid_reg_14_3_38 <= up;
          _fsm_cond_14_3_41 <= (count >= 32);
          _valid_reg_14_4_44 <= down;
          _fsm_cond_14_4_48 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          _valid_reg_15_1_52 <= up;
          _fsm_cond_15_1_53 <= (count >= 32);
          _valid_reg_15_2_54 <= up;
          _fsm_cond_15_2_56 <= (count >= 32);
          _valid_reg_15_3_58 <= up;
          _fsm_cond_15_3_61 <= (count >= 32);
          _valid_reg_15_4_64 <= down;
          _fsm_cond_15_4_68 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          _valid_reg_16_1_72 <= up;
          _fsm_cond_16_1_73 <= (count >= 32);
          _valid_reg_16_2_74 <= up;
          _fsm_cond_16_2_76 <= (count >= 32);
          _valid_reg_16_3_78 <= up;
          _fsm_cond_16_3_81 <= (count >= 32);
          _valid_reg_16_4_84 <= down;
          _fsm_cond_16_4_88 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          _valid_reg_17_1_92 <= up;
          _fsm_cond_17_1_93 <= (count >= 32);
          _valid_reg_17_2_94 <= up;
          _fsm_cond_17_2_96 <= (count >= 32);
          _valid_reg_17_3_98 <= up;
          _fsm_cond_17_3_101 <= (count >= 32);
          _valid_reg_17_4_104 <= down;
          _fsm_cond_17_4_108 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          _valid_reg_18_1_112 <= up;
          _fsm_cond_18_1_113 <= (count >= 32);
          _valid_reg_18_2_114 <= up;
          _fsm_cond_18_2_116 <= (count >= 32);
          _valid_reg_18_3_118 <= up;
          _fsm_cond_18_3_121 <= (count >= 32);
          _valid_reg_18_4_124 <= down;
          _fsm_cond_18_4_128 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          _valid_reg_19_1_132 <= up;
          _fsm_cond_19_1_133 <= (count >= 32);
          _valid_reg_19_2_134 <= up;
          _fsm_cond_19_2_136 <= (count >= 32);
          _valid_reg_19_3_138 <= up;
          _fsm_cond_19_3_141 <= (count >= 32);
          _valid_reg_19_4_144 <= down;
          _fsm_cond_19_4_148 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          _valid_reg_20_1_152 <= up;
          _fsm_cond_20_1_153 <= (count >= 32);
          _valid_reg_20_2_154 <= up;
          _fsm_cond_20_2_156 <= (count >= 32);
          _valid_reg_20_3_158 <= up;
          _fsm_cond_20_3_161 <= (count >= 32);
          _valid_reg_20_4_164 <= down;
          _fsm_cond_20_4_168 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_21;
          end 
        end
      endcase
    end
  end
endmodule
"""

def test_led():
    test_module = led.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
