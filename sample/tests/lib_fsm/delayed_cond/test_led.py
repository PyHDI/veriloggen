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
   output reg valid
   );

  reg [32-1:0] count;
  reg [32-1:0] fsm;

  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;

  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_4_1_0;

  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_4_2_1;
  reg _fsm_cond_4_2_2;

  reg [32-1:0] _d3_fsm;
  reg _fsm_cond_4_3_3;
  reg _fsm_cond_4_3_4;
  reg _fsm_cond_4_3_5;

  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;

  reg _fsm_cond_13_1_6;
  reg _fsm_cond_13_2_7;
  reg _fsm_cond_13_2_8;
  reg _fsm_cond_13_3_9;
  reg _fsm_cond_13_3_10;
  reg _fsm_cond_13_3_11;

  reg [32-1:0] _d4_fsm;
  reg _fsm_cond_13_4_12;
  reg _fsm_cond_13_4_13;
  reg _fsm_cond_13_4_14;
  reg _fsm_cond_13_4_15;

  localparam fsm_14 = 14;

  reg _fsm_cond_14_1_16;
  reg _fsm_cond_14_2_17;
  reg _fsm_cond_14_2_18;
  reg _fsm_cond_14_3_19;
  reg _fsm_cond_14_3_20;
  reg _fsm_cond_14_3_21;
  reg _fsm_cond_14_4_22;
  reg _fsm_cond_14_4_23;
  reg _fsm_cond_14_4_24;
  reg _fsm_cond_14_4_25;

  localparam fsm_15 = 15;

  reg _fsm_cond_15_1_26;
  reg _fsm_cond_15_2_27;
  reg _fsm_cond_15_2_28;
  reg _fsm_cond_15_3_29;
  reg _fsm_cond_15_3_30;
  reg _fsm_cond_15_3_31;
  reg _fsm_cond_15_4_32;
  reg _fsm_cond_15_4_33;
  reg _fsm_cond_15_4_34;
  reg _fsm_cond_15_4_35;

  localparam fsm_16 = 16;

  reg _fsm_cond_16_1_36;
  reg _fsm_cond_16_2_37;
  reg _fsm_cond_16_2_38;
  reg _fsm_cond_16_3_39;
  reg _fsm_cond_16_3_40;
  reg _fsm_cond_16_3_41;
  reg _fsm_cond_16_4_42;
  reg _fsm_cond_16_4_43;
  reg _fsm_cond_16_4_44;
  reg _fsm_cond_16_4_45;

  localparam fsm_17 = 17;

  reg _fsm_cond_17_1_46;
  reg _fsm_cond_17_2_47;
  reg _fsm_cond_17_2_48;
  reg _fsm_cond_17_3_49;
  reg _fsm_cond_17_3_50;
  reg _fsm_cond_17_3_51;
  reg _fsm_cond_17_4_52;
  reg _fsm_cond_17_4_53;
  reg _fsm_cond_17_4_54;
  reg _fsm_cond_17_4_55;

  localparam fsm_18 = 18;

  reg _fsm_cond_18_1_56;
  reg _fsm_cond_18_2_57;
  reg _fsm_cond_18_2_58;
  reg _fsm_cond_18_3_59;
  reg _fsm_cond_18_3_60;
  reg _fsm_cond_18_3_61;
  reg _fsm_cond_18_4_62;
  reg _fsm_cond_18_4_63;
  reg _fsm_cond_18_4_64;
  reg _fsm_cond_18_4_65;

  localparam fsm_19 = 19;

  reg _fsm_cond_19_1_66;
  reg _fsm_cond_19_2_67;
  reg _fsm_cond_19_2_68;
  reg _fsm_cond_19_3_69;
  reg _fsm_cond_19_3_70;
  reg _fsm_cond_19_3_71;
  reg _fsm_cond_19_4_72;
  reg _fsm_cond_19_4_73;
  reg _fsm_cond_19_4_74;
  reg _fsm_cond_19_4_75;

  localparam fsm_20 = 20;

  reg _fsm_cond_20_1_76;
  reg _fsm_cond_20_2_77;
  reg _fsm_cond_20_2_78;
  reg _fsm_cond_20_3_79;
  reg _fsm_cond_20_3_80;
  reg _fsm_cond_20_3_81;
  reg _fsm_cond_20_4_82;
  reg _fsm_cond_20_4_83;
  reg _fsm_cond_20_4_84;
  reg _fsm_cond_20_4_85;

  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _fsm_cond_4_1_0 <= 0;
      _d2_fsm <= fsm_init;
      _fsm_cond_4_2_1 <= 0;
      _fsm_cond_4_2_2 <= 0;
      _d3_fsm <= fsm_init;
      _fsm_cond_4_3_3 <= 0;
      _fsm_cond_4_3_4 <= 0;
      _fsm_cond_4_3_5 <= 0;
      _fsm_cond_13_1_6 <= 0;
      _fsm_cond_13_2_7 <= 0;
      _fsm_cond_13_2_8 <= 0;
      _fsm_cond_13_3_9 <= 0;
      _fsm_cond_13_3_10 <= 0;
      _fsm_cond_13_3_11 <= 0;
      _d4_fsm <= fsm_init;
      _fsm_cond_13_4_12 <= 0;
      _fsm_cond_13_4_13 <= 0;
      _fsm_cond_13_4_14 <= 0;
      _fsm_cond_13_4_15 <= 0;
      _fsm_cond_14_1_16 <= 0;
      _fsm_cond_14_2_17 <= 0;
      _fsm_cond_14_2_18 <= 0;
      _fsm_cond_14_3_19 <= 0;
      _fsm_cond_14_3_20 <= 0;
      _fsm_cond_14_3_21 <= 0;
      _fsm_cond_14_4_22 <= 0;
      _fsm_cond_14_4_23 <= 0;
      _fsm_cond_14_4_24 <= 0;
      _fsm_cond_14_4_25 <= 0;
      _fsm_cond_15_1_26 <= 0;
      _fsm_cond_15_2_27 <= 0;
      _fsm_cond_15_2_28 <= 0;
      _fsm_cond_15_3_29 <= 0;
      _fsm_cond_15_3_30 <= 0;
      _fsm_cond_15_3_31 <= 0;
      _fsm_cond_15_4_32 <= 0;
      _fsm_cond_15_4_33 <= 0;
      _fsm_cond_15_4_34 <= 0;
      _fsm_cond_15_4_35 <= 0;
      _fsm_cond_16_1_36 <= 0;
      _fsm_cond_16_2_37 <= 0;
      _fsm_cond_16_2_38 <= 0;
      _fsm_cond_16_3_39 <= 0;
      _fsm_cond_16_3_40 <= 0;
      _fsm_cond_16_3_41 <= 0;
      _fsm_cond_16_4_42 <= 0;
      _fsm_cond_16_4_43 <= 0;
      _fsm_cond_16_4_44 <= 0;
      _fsm_cond_16_4_45 <= 0;
      _fsm_cond_17_1_46 <= 0;
      _fsm_cond_17_2_47 <= 0;
      _fsm_cond_17_2_48 <= 0;
      _fsm_cond_17_3_49 <= 0;
      _fsm_cond_17_3_50 <= 0;
      _fsm_cond_17_3_51 <= 0;
      _fsm_cond_17_4_52 <= 0;
      _fsm_cond_17_4_53 <= 0;
      _fsm_cond_17_4_54 <= 0;
      _fsm_cond_17_4_55 <= 0;
      _fsm_cond_18_1_56 <= 0;
      _fsm_cond_18_2_57 <= 0;
      _fsm_cond_18_2_58 <= 0;
      _fsm_cond_18_3_59 <= 0;
      _fsm_cond_18_3_60 <= 0;
      _fsm_cond_18_3_61 <= 0;
      _fsm_cond_18_4_62 <= 0;
      _fsm_cond_18_4_63 <= 0;
      _fsm_cond_18_4_64 <= 0;
      _fsm_cond_18_4_65 <= 0;
      _fsm_cond_19_1_66 <= 0;
      _fsm_cond_19_2_67 <= 0;
      _fsm_cond_19_2_68 <= 0;
      _fsm_cond_19_3_69 <= 0;
      _fsm_cond_19_3_70 <= 0;
      _fsm_cond_19_3_71 <= 0;
      _fsm_cond_19_4_72 <= 0;
      _fsm_cond_19_4_73 <= 0;
      _fsm_cond_19_4_74 <= 0;
      _fsm_cond_19_4_75 <= 0;
      _fsm_cond_20_1_76 <= 0;
      _fsm_cond_20_2_77 <= 0;
      _fsm_cond_20_2_78 <= 0;
      _fsm_cond_20_3_79 <= 0;
      _fsm_cond_20_3_80 <= 0;
      _fsm_cond_20_3_81 <= 0;
      _fsm_cond_20_4_82 <= 0;
      _fsm_cond_20_4_83 <= 0;
      _fsm_cond_20_4_84 <= 0;
      _fsm_cond_20_4_85 <= 0;
    end else begin
      count <= count + 1;
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;

      case(_d4_fsm)
        fsm_13: begin
          if(_fsm_cond_13_4_15) begin
            valid <= 0;
          end 
        end
        fsm_14: begin
          if(_fsm_cond_14_4_25) begin
            valid <= 0;
          end 
        end
        fsm_15: begin
          if(_fsm_cond_15_4_35) begin
            valid <= 0;
          end 
        end
        fsm_16: begin
          if(_fsm_cond_16_4_45) begin
            valid <= 0;
          end 
        end
        fsm_17: begin
          if(_fsm_cond_17_4_55) begin
            valid <= 0;
          end 
        end
        fsm_18: begin
          if(_fsm_cond_18_4_65) begin
            valid <= 0;
          end 
        end
        fsm_19: begin
          if(_fsm_cond_19_4_75) begin
            valid <= 0;
          end 
        end
        fsm_20: begin
          if(_fsm_cond_20_4_85) begin
            valid <= 0;
          end 
        end
      endcase

      case(_d3_fsm)
        fsm_4: begin
          if(_fsm_cond_4_3_5) begin
            valid <= 0;
          end 
        end
        fsm_13: begin
          if(_fsm_cond_13_3_11) begin
            valid <= 1;
          end 
          _fsm_cond_13_4_15 <= _fsm_cond_13_4_14;
        end
        fsm_14: begin
          if(_fsm_cond_14_3_21) begin
            valid <= 1;
          end 
          _fsm_cond_14_4_25 <= _fsm_cond_14_4_24;
        end
        fsm_15: begin
          if(_fsm_cond_15_3_31) begin
            valid <= 1;
          end 
          _fsm_cond_15_4_35 <= _fsm_cond_15_4_34;
        end
        fsm_16: begin
          if(_fsm_cond_16_3_41) begin
            valid <= 1;
          end 
          _fsm_cond_16_4_45 <= _fsm_cond_16_4_44;
        end
        fsm_17: begin
          if(_fsm_cond_17_3_51) begin
            valid <= 1;
          end 
          _fsm_cond_17_4_55 <= _fsm_cond_17_4_54;
        end
        fsm_18: begin
          if(_fsm_cond_18_3_61) begin
            valid <= 1;
          end 
          _fsm_cond_18_4_65 <= _fsm_cond_18_4_64;
        end
        fsm_19: begin
          if(_fsm_cond_19_3_71) begin
            valid <= 1;
          end 
          _fsm_cond_19_4_75 <= _fsm_cond_19_4_74;
        end
        fsm_20: begin
          if(_fsm_cond_20_3_81) begin
            valid <= 1;
          end 
          _fsm_cond_20_4_85 <= _fsm_cond_20_4_84;
        end
      endcase

      case(_d2_fsm)
        fsm_4: begin
          if(_fsm_cond_4_2_2) begin
            valid <= 1;
          end 
          _fsm_cond_4_3_5 <= _fsm_cond_4_3_4;
        end
        fsm_13: begin
          if(_fsm_cond_13_2_8) begin
            valid <= 1;
          end 
          _fsm_cond_13_3_11 <= _fsm_cond_13_3_10;
          _fsm_cond_13_4_14 <= _fsm_cond_13_4_13;
        end
        fsm_14: begin
          if(_fsm_cond_14_2_18) begin
            valid <= 1;
          end 
          _fsm_cond_14_3_21 <= _fsm_cond_14_3_20;
          _fsm_cond_14_4_24 <= _fsm_cond_14_4_23;
        end
        fsm_15: begin
          if(_fsm_cond_15_2_28) begin
            valid <= 1;
          end 
          _fsm_cond_15_3_31 <= _fsm_cond_15_3_30;
          _fsm_cond_15_4_34 <= _fsm_cond_15_4_33;
        end
        fsm_16: begin
          if(_fsm_cond_16_2_38) begin
            valid <= 1;
          end 
          _fsm_cond_16_3_41 <= _fsm_cond_16_3_40;
          _fsm_cond_16_4_44 <= _fsm_cond_16_4_43;
        end
        fsm_17: begin
          if(_fsm_cond_17_2_48) begin
            valid <= 1;
          end 
          _fsm_cond_17_3_51 <= _fsm_cond_17_3_50;
          _fsm_cond_17_4_54 <= _fsm_cond_17_4_53;
        end
        fsm_18: begin
          if(_fsm_cond_18_2_58) begin
            valid <= 1;
          end 
          _fsm_cond_18_3_61 <= _fsm_cond_18_3_60;
          _fsm_cond_18_4_64 <= _fsm_cond_18_4_63;
        end
        fsm_19: begin
          if(_fsm_cond_19_2_68) begin
            valid <= 1;
          end 
          _fsm_cond_19_3_71 <= _fsm_cond_19_3_70;
          _fsm_cond_19_4_74 <= _fsm_cond_19_4_73;
        end
        fsm_20: begin
          if(_fsm_cond_20_2_78) begin
            valid <= 1;
          end 
          _fsm_cond_20_3_81 <= _fsm_cond_20_3_80;
          _fsm_cond_20_4_84 <= _fsm_cond_20_4_83;
        end
      endcase

      case(_d1_fsm)
        fsm_4: begin
          if(_fsm_cond_4_1_0) begin
            valid <= 1;
          end 
          _fsm_cond_4_2_2 <= _fsm_cond_4_2_1;
          _fsm_cond_4_3_4 <= _fsm_cond_4_3_3;
        end
        fsm_13: begin
          if(_fsm_cond_13_1_6) begin
            valid <= 1;
          end 
          _fsm_cond_13_2_8 <= _fsm_cond_13_2_7;
          _fsm_cond_13_3_10 <= _fsm_cond_13_3_9;
          _fsm_cond_13_4_13 <= _fsm_cond_13_4_12;
        end
        fsm_14: begin
          if(_fsm_cond_14_1_16) begin
            valid <= 1;
          end 
          _fsm_cond_14_2_18 <= _fsm_cond_14_2_17;
          _fsm_cond_14_3_20 <= _fsm_cond_14_3_19;
          _fsm_cond_14_4_23 <= _fsm_cond_14_4_22;
        end
        fsm_15: begin
          if(_fsm_cond_15_1_26) begin
            valid <= 1;
          end 
          _fsm_cond_15_2_28 <= _fsm_cond_15_2_27;
          _fsm_cond_15_3_30 <= _fsm_cond_15_3_29;
          _fsm_cond_15_4_33 <= _fsm_cond_15_4_32;
        end
        fsm_16: begin
          if(_fsm_cond_16_1_36) begin
            valid <= 1;
          end 
          _fsm_cond_16_2_38 <= _fsm_cond_16_2_37;
          _fsm_cond_16_3_40 <= _fsm_cond_16_3_39;
          _fsm_cond_16_4_43 <= _fsm_cond_16_4_42;
        end
        fsm_17: begin
          if(_fsm_cond_17_1_46) begin
            valid <= 1;
          end 
          _fsm_cond_17_2_48 <= _fsm_cond_17_2_47;
          _fsm_cond_17_3_50 <= _fsm_cond_17_3_49;
          _fsm_cond_17_4_53 <= _fsm_cond_17_4_52;
        end
        fsm_18: begin
          if(_fsm_cond_18_1_56) begin
            valid <= 1;
          end 
          _fsm_cond_18_2_58 <= _fsm_cond_18_2_57;
          _fsm_cond_18_3_60 <= _fsm_cond_18_3_59;
          _fsm_cond_18_4_63 <= _fsm_cond_18_4_62;
        end
        fsm_19: begin
          if(_fsm_cond_19_1_66) begin
            valid <= 1;
          end 
          _fsm_cond_19_2_68 <= _fsm_cond_19_2_67;
          _fsm_cond_19_3_70 <= _fsm_cond_19_3_69;
          _fsm_cond_19_4_73 <= _fsm_cond_19_4_72;
        end
        fsm_20: begin
          if(_fsm_cond_20_1_76) begin
            valid <= 1;
          end 
          _fsm_cond_20_2_78 <= _fsm_cond_20_2_77;
          _fsm_cond_20_3_80 <= _fsm_cond_20_3_79;
          _fsm_cond_20_4_83 <= _fsm_cond_20_4_82;
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
          _fsm_cond_4_1_0 <= (count >= 16);
          _fsm_cond_4_2_1 <= (count >= 16);
          _fsm_cond_4_3_3 <= (count >= 16);
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
          _fsm_cond_13_1_6 <= (count >= 32);
          _fsm_cond_13_2_7 <= (count >= 32);
          _fsm_cond_13_3_9 <= (count >= 32);
          _fsm_cond_13_4_12 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          _fsm_cond_14_1_16 <= (count >= 32);
          _fsm_cond_14_2_17 <= (count >= 32);
          _fsm_cond_14_3_19 <= (count >= 32);
          _fsm_cond_14_4_22 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          _fsm_cond_15_1_26 <= (count >= 32);
          _fsm_cond_15_2_27 <= (count >= 32);
          _fsm_cond_15_3_29 <= (count >= 32);
          _fsm_cond_15_4_32 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          _fsm_cond_16_1_36 <= (count >= 32);
          _fsm_cond_16_2_37 <= (count >= 32);
          _fsm_cond_16_3_39 <= (count >= 32);
          _fsm_cond_16_4_42 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          _fsm_cond_17_1_46 <= (count >= 32);
          _fsm_cond_17_2_47 <= (count >= 32);
          _fsm_cond_17_3_49 <= (count >= 32);
          _fsm_cond_17_4_52 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          _fsm_cond_18_1_56 <= (count >= 32);
          _fsm_cond_18_2_57 <= (count >= 32);
          _fsm_cond_18_3_59 <= (count >= 32);
          _fsm_cond_18_4_62 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          _fsm_cond_19_1_66 <= (count >= 32);
          _fsm_cond_19_2_67 <= (count >= 32);
          _fsm_cond_19_3_69 <= (count >= 32);
          _fsm_cond_19_4_72 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          _fsm_cond_20_1_76 <= (count >= 32);
          _fsm_cond_20_2_77 <= (count >= 32);
          _fsm_cond_20_3_79 <= (count >= 32);
          _fsm_cond_20_4_82 <= (count >= 32);
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
