from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import regchain

expected_verilog = """
module reg_chain
(
  input CLK,
  input RST,
  input [8-1:0] sw,
  output [8-1:0] dout
);

  reg [3-1:0] _tmp_0;
  reg [2-1:0] _tmp_1;
  reg [2-1:0] _tmp_2;
  reg _tmp_3;
  reg [8-1:0] _tmp_4;
  reg [8-1:0] _tmp_5;
  reg [8-1:0] _tmp_6;
  reg [8-1:0] _tmp_7;
  reg [8-1:0] _tmp_8;
  reg [8-1:0] _tmp_9;
  reg [8-1:0] _tmp_10;
  reg [8-1:0] _tmp_11;
  reg [8-1:0] _tmp_12;
  reg [8-1:0] _tmp_13;
  reg [8-1:0] _tmp_14;
  reg [8-1:0] _tmp_15;
  reg [8-1:0] _tmp_16;
  reg [8-1:0] _tmp_17;
  reg [8-1:0] _tmp_18;
  reg [8-1:0] _tmp_19;
  reg [8-1:0] _tmp_20;
  reg [8-1:0] _tmp_21;
  reg [8-1:0] _tmp_22;
  reg [8-1:0] _tmp_23;
  reg [8-1:0] _tmp_24;
  reg [8-1:0] _tmp_25;
  reg [8-1:0] _tmp_26;
  reg [8-1:0] _tmp_27;
  reg [8-1:0] _tmp_28;
  reg [8-1:0] _tmp_29;
  reg [8-1:0] _tmp_30;
  reg [8-1:0] _tmp_31;
  reg [8-1:0] _tmp_32;
  reg [8-1:0] _tmp_33;
  reg [8-1:0] _tmp_34;
  reg [8-1:0] _tmp_35;
  reg [8-1:0] _tmp_36;
  reg [8-1:0] _tmp_37;
  reg [8-1:0] _tmp_38;
  reg [8-1:0] _tmp_39;
  reg [8-1:0] _tmp_40;
  reg [8-1:0] _tmp_41;
  reg [8-1:0] _tmp_42;
  reg [8-1:0] _tmp_43;
  reg [8-1:0] _tmp_44;
  reg [8-1:0] _tmp_45;
  reg [8-1:0] _tmp_46;
  reg [8-1:0] _tmp_47;
  reg [8-1:0] _tmp_48;
  reg [8-1:0] _tmp_49;
  reg [8-1:0] _tmp_50;
  reg [8-1:0] _tmp_51;
  reg [8-1:0] _tmp_52;
  reg [8-1:0] _tmp_53;
  reg [8-1:0] _tmp_54;
  reg [8-1:0] _tmp_55;
  reg [8-1:0] _tmp_56;
  reg [8-1:0] _tmp_57;
  reg [8-1:0] _tmp_58;
  reg [8-1:0] _tmp_59;
  reg [8-1:0] _tmp_60;
  reg [8-1:0] _tmp_61;
  reg [8-1:0] _tmp_62;
  reg [8-1:0] _tmp_63;
  reg [8-1:0] _tmp_64;
  reg [8-1:0] _tmp_65;
  reg [8-1:0] _tmp_66;
  reg [8-1:0] _tmp_67;
  reg [8-1:0] _tmp_68;
  reg [8-1:0] _tmp_69;
  reg [8-1:0] _tmp_70;
  reg [8-1:0] _tmp_71;
  reg [8-1:0] _tmp_72;
  reg [8-1:0] _tmp_73;
  reg [8-1:0] _tmp_74;
  reg [8-1:0] _tmp_75;
  reg [8-1:0] _tmp_76;
  reg [8-1:0] _tmp_77;
  reg [8-1:0] _tmp_78;
  reg [8-1:0] _tmp_79;
  reg [8-1:0] _tmp_80;
  reg [8-1:0] _tmp_81;
  reg [8-1:0] _tmp_82;
  reg [8-1:0] _tmp_83;
  reg [8-1:0] _tmp_84;
  reg [8-1:0] _tmp_85;
  reg [8-1:0] _tmp_86;
  reg [8-1:0] _tmp_87;
  reg [8-1:0] _tmp_88;
  reg [8-1:0] _tmp_89;
  reg [8-1:0] _tmp_90;
  reg [8-1:0] _tmp_91;
  reg [8-1:0] _tmp_92;
  reg [8-1:0] _tmp_93;
  reg [8-1:0] _tmp_94;
  reg [8-1:0] _tmp_95;
  reg [8-1:0] _tmp_96;
  reg [8-1:0] _tmp_97;
  reg [8-1:0] _tmp_98;
  reg [8-1:0] _tmp_99;
  reg [8-1:0] _tmp_100;
  reg [8-1:0] _tmp_101;
  reg [8-1:0] _tmp_102;
  reg [8-1:0] _tmp_103;
  reg [8-1:0] _tmp_104;
  reg [8-1:0] _tmp_105;
  reg [8-1:0] _tmp_106;
  reg [8-1:0] _tmp_107;
  reg [8-1:0] _tmp_108;
  reg [8-1:0] _tmp_109;
  reg [8-1:0] _tmp_110;
  reg [8-1:0] _tmp_111;
  reg [8-1:0] _tmp_112;
  reg [8-1:0] _tmp_113;
  reg [8-1:0] _tmp_114;
  reg [8-1:0] _tmp_115;
  reg [8-1:0] _tmp_116;
  reg [8-1:0] _tmp_117;
  reg [8-1:0] _tmp_118;
  reg [8-1:0] _tmp_119;
  reg [8-1:0] _tmp_120;
  reg [8-1:0] _tmp_121;
  reg [8-1:0] _tmp_122;
  reg [8-1:0] _tmp_123;
  reg [8-1:0] _tmp_124;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_5 <= 0;
      _tmp_6 <= 0;
      _tmp_7 <= 0;
      _tmp_8 <= 0;
      _tmp_9 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_12 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_17 <= 0;
      _tmp_18 <= 0;
      _tmp_19 <= 0;
      _tmp_20 <= 0;
      _tmp_21 <= 0;
      _tmp_22 <= 0;
      _tmp_23 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_28 <= 0;
      _tmp_29 <= 0;
      _tmp_30 <= 0;
      _tmp_31 <= 0;
      _tmp_32 <= 0;
      _tmp_33 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
      _tmp_42 <= 0;
      _tmp_43 <= 0;
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_48 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_55 <= 0;
      _tmp_56 <= 0;
      _tmp_57 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_63 <= 0;
      _tmp_64 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _tmp_69 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_72 <= 0;
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_78 <= 0;
      _tmp_79 <= 0;
      _tmp_80 <= 0;
      _tmp_81 <= 0;
      _tmp_82 <= 0;
      _tmp_83 <= 0;
      _tmp_84 <= 0;
      _tmp_85 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _tmp_90 <= 0;
      _tmp_91 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _tmp_99 <= 0;
      _tmp_100 <= 0;
      _tmp_101 <= 0;
      _tmp_102 <= 0;
      _tmp_103 <= 0;
      _tmp_104 <= 0;
      _tmp_105 <= 0;
      _tmp_106 <= 0;
      _tmp_107 <= 0;
      _tmp_108 <= 0;
      _tmp_109 <= 0;
      _tmp_110 <= 0;
      _tmp_111 <= 0;
      _tmp_112 <= 0;
      _tmp_113 <= 0;
      _tmp_114 <= 0;
      _tmp_115 <= 0;
      _tmp_116 <= 0;
      _tmp_117 <= 0;
      _tmp_118 <= 0;
      _tmp_119 <= 0;
      _tmp_120 <= 0;
      _tmp_121 <= 0;
      _tmp_122 <= 0;
      _tmp_123 <= 0;
      _tmp_124 <= 0;
      _tmp_4 <= 0;
    end else begin
      _tmp_0 <= sw[2:0];
      _tmp_1 <= sw[4:3];
      _tmp_2 <= _tmp_2 + 1;
      _tmp_3 <= _tmp_2 < _tmp_0;
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_5 <= _tmp_4 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_6 <= _tmp_5 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_7 <= _tmp_6 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_8 <= _tmp_7 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_9 <= _tmp_8 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_10 <= _tmp_9 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_11 <= _tmp_10 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_12 <= _tmp_11 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_13 <= _tmp_12 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_14 <= _tmp_13 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_15 <= _tmp_14 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_16 <= _tmp_15 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_17 <= _tmp_16 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_18 <= _tmp_17 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_19 <= _tmp_18 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_20 <= _tmp_19 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_21 <= _tmp_20 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_22 <= _tmp_21 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_23 <= _tmp_22 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_24 <= _tmp_23 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_25 <= _tmp_24 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_26 <= _tmp_25 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_27 <= _tmp_26 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_28 <= _tmp_27 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_29 <= _tmp_28 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_30 <= _tmp_29 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_31 <= _tmp_30 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_32 <= _tmp_31 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_33 <= _tmp_32 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 0)) begin
        _tmp_34 <= _tmp_33 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_35 <= _tmp_34 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_36 <= _tmp_35 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_37 <= _tmp_36 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_38 <= _tmp_37 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_39 <= _tmp_38 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_40 <= _tmp_39 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_41 <= _tmp_40 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_42 <= _tmp_41 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_43 <= _tmp_42 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_44 <= _tmp_43 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_45 <= _tmp_44 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_46 <= _tmp_45 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_47 <= _tmp_46 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_48 <= _tmp_47 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_49 <= _tmp_48 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_50 <= _tmp_49 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_51 <= _tmp_50 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_52 <= _tmp_51 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_53 <= _tmp_52 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_54 <= _tmp_53 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_55 <= _tmp_54 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_56 <= _tmp_55 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_57 <= _tmp_56 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_58 <= _tmp_57 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_59 <= _tmp_58 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_60 <= _tmp_59 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_61 <= _tmp_60 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_62 <= _tmp_61 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_63 <= _tmp_62 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 1)) begin
        _tmp_64 <= _tmp_63 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_65 <= _tmp_64 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_66 <= _tmp_65 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_67 <= _tmp_66 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_68 <= _tmp_67 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_69 <= _tmp_68 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_70 <= _tmp_69 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_71 <= _tmp_70 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_72 <= _tmp_71 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_73 <= _tmp_72 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_74 <= _tmp_73 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_75 <= _tmp_74 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_76 <= _tmp_75 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_77 <= _tmp_76 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_78 <= _tmp_77 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_79 <= _tmp_78 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_80 <= _tmp_79 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_81 <= _tmp_80 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_82 <= _tmp_81 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_83 <= _tmp_82 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_84 <= _tmp_83 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_85 <= _tmp_84 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_86 <= _tmp_85 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_87 <= _tmp_86 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_88 <= _tmp_87 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_89 <= _tmp_88 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_90 <= _tmp_89 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_91 <= _tmp_90 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_92 <= _tmp_91 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_93 <= _tmp_92 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 2)) begin
        _tmp_94 <= _tmp_93 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_95 <= _tmp_94 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_96 <= _tmp_95 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_97 <= _tmp_96 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_98 <= _tmp_97 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_99 <= _tmp_98 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_100 <= _tmp_99 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_101 <= _tmp_100 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_102 <= _tmp_101 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_103 <= _tmp_102 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_104 <= _tmp_103 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_105 <= _tmp_104 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_106 <= _tmp_105 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_107 <= _tmp_106 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_108 <= _tmp_107 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_109 <= _tmp_108 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_110 <= _tmp_109 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_111 <= _tmp_110 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_112 <= _tmp_111 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_113 <= _tmp_112 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_114 <= _tmp_113 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_115 <= _tmp_114 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_116 <= _tmp_115 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_117 <= _tmp_116 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_118 <= _tmp_117 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_119 <= _tmp_118 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_120 <= _tmp_119 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_121 <= _tmp_120 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_122 <= _tmp_121 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_123 <= _tmp_122 + 1;
      end 
      if(_tmp_3 && (_tmp_1 >= 3)) begin
        _tmp_124 <= _tmp_123 + 1;
      end 
      if(_tmp_3 && (_tmp_1 == 0)) begin
        _tmp_4 <= _tmp_34 + 3;
      end 
      if(_tmp_3 && (_tmp_1 == 1)) begin
        _tmp_4 <= _tmp_64 + 2;
      end 
      if(_tmp_3 && (_tmp_1 == 2)) begin
        _tmp_4 <= _tmp_94 + 1;
      end 
      if(_tmp_3 && (_tmp_1 == 3)) begin
        _tmp_4 <= _tmp_124 + 0;
      end 
    end
  end

  assign dout = _tmp_4;

endmodule
"""

def test():
    veriloggen.reset()
    test_module = regchain.mkRegChain(length=120)
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
