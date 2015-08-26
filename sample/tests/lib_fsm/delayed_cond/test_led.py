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

  reg [32-1:0] d1_fsm;
  reg fsm_cond_4_1_0;

  reg [32-1:0] d2_fsm;
  reg fsm_cond_4_2_1;
  reg fsm_cond_4_2_2;

  reg [32-1:0] d3_fsm;
  reg fsm_cond_4_3_3;
  reg fsm_cond_4_3_4;
  reg fsm_cond_4_3_5;

  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;

  reg fsm_cond_13_1_6;
  reg fsm_cond_13_2_7;
  reg fsm_cond_13_2_8;
  reg fsm_cond_13_3_9;
  reg fsm_cond_13_3_10;
  reg fsm_cond_13_3_11;

  reg [32-1:0] d4_fsm;
  reg fsm_cond_13_4_12;
  reg fsm_cond_13_4_13;
  reg fsm_cond_13_4_14;
  reg fsm_cond_13_4_15;

  localparam fsm_14 = 14;

  reg fsm_cond_14_1_16;
  reg fsm_cond_14_2_17;
  reg fsm_cond_14_2_18;
  reg fsm_cond_14_3_19;
  reg fsm_cond_14_3_20;
  reg fsm_cond_14_3_21;
  reg fsm_cond_14_4_22;
  reg fsm_cond_14_4_23;
  reg fsm_cond_14_4_24;
  reg fsm_cond_14_4_25;

  localparam fsm_15 = 15;

  reg fsm_cond_15_1_26;
  reg fsm_cond_15_2_27;
  reg fsm_cond_15_2_28;
  reg fsm_cond_15_3_29;
  reg fsm_cond_15_3_30;
  reg fsm_cond_15_3_31;
  reg fsm_cond_15_4_32;
  reg fsm_cond_15_4_33;
  reg fsm_cond_15_4_34;
  reg fsm_cond_15_4_35;

  localparam fsm_16 = 16;

  reg fsm_cond_16_1_36;
  reg fsm_cond_16_2_37;
  reg fsm_cond_16_2_38;
  reg fsm_cond_16_3_39;
  reg fsm_cond_16_3_40;
  reg fsm_cond_16_3_41;
  reg fsm_cond_16_4_42;
  reg fsm_cond_16_4_43;
  reg fsm_cond_16_4_44;
  reg fsm_cond_16_4_45;

  localparam fsm_17 = 17;

  reg fsm_cond_17_1_46;
  reg fsm_cond_17_2_47;
  reg fsm_cond_17_2_48;
  reg fsm_cond_17_3_49;
  reg fsm_cond_17_3_50;
  reg fsm_cond_17_3_51;
  reg fsm_cond_17_4_52;
  reg fsm_cond_17_4_53;
  reg fsm_cond_17_4_54;
  reg fsm_cond_17_4_55;

  localparam fsm_18 = 18;

  reg fsm_cond_18_1_56;
  reg fsm_cond_18_2_57;
  reg fsm_cond_18_2_58;
  reg fsm_cond_18_3_59;
  reg fsm_cond_18_3_60;
  reg fsm_cond_18_3_61;
  reg fsm_cond_18_4_62;
  reg fsm_cond_18_4_63;
  reg fsm_cond_18_4_64;
  reg fsm_cond_18_4_65;

  localparam fsm_19 = 19;

  reg fsm_cond_19_1_66;
  reg fsm_cond_19_2_67;
  reg fsm_cond_19_2_68;
  reg fsm_cond_19_3_69;
  reg fsm_cond_19_3_70;
  reg fsm_cond_19_3_71;
  reg fsm_cond_19_4_72;
  reg fsm_cond_19_4_73;
  reg fsm_cond_19_4_74;
  reg fsm_cond_19_4_75;

  localparam fsm_20 = 20;

  reg fsm_cond_20_1_76;
  reg fsm_cond_20_2_77;
  reg fsm_cond_20_2_78;
  reg fsm_cond_20_3_79;
  reg fsm_cond_20_3_80;
  reg fsm_cond_20_3_81;
  reg fsm_cond_20_4_82;
  reg fsm_cond_20_4_83;
  reg fsm_cond_20_4_84;
  reg fsm_cond_20_4_85;

  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      d1_fsm <= fsm_init;
      fsm_cond_4_1_0 <= 0;
      d2_fsm <= fsm_init;
      fsm_cond_4_2_1 <= 0;
      fsm_cond_4_2_2 <= 0;
      d3_fsm <= fsm_init;
      fsm_cond_4_3_3 <= 0;
      fsm_cond_4_3_4 <= 0;
      fsm_cond_4_3_5 <= 0;
      fsm_cond_13_1_6 <= 0;
      fsm_cond_13_2_7 <= 0;
      fsm_cond_13_2_8 <= 0;
      fsm_cond_13_3_9 <= 0;
      fsm_cond_13_3_10 <= 0;
      fsm_cond_13_3_11 <= 0;
      d4_fsm <= fsm_init;
      fsm_cond_13_4_12 <= 0;
      fsm_cond_13_4_13 <= 0;
      fsm_cond_13_4_14 <= 0;
      fsm_cond_13_4_15 <= 0;
      fsm_cond_14_1_16 <= 0;
      fsm_cond_14_2_17 <= 0;
      fsm_cond_14_2_18 <= 0;
      fsm_cond_14_3_19 <= 0;
      fsm_cond_14_3_20 <= 0;
      fsm_cond_14_3_21 <= 0;
      fsm_cond_14_4_22 <= 0;
      fsm_cond_14_4_23 <= 0;
      fsm_cond_14_4_24 <= 0;
      fsm_cond_14_4_25 <= 0;
      fsm_cond_15_1_26 <= 0;
      fsm_cond_15_2_27 <= 0;
      fsm_cond_15_2_28 <= 0;
      fsm_cond_15_3_29 <= 0;
      fsm_cond_15_3_30 <= 0;
      fsm_cond_15_3_31 <= 0;
      fsm_cond_15_4_32 <= 0;
      fsm_cond_15_4_33 <= 0;
      fsm_cond_15_4_34 <= 0;
      fsm_cond_15_4_35 <= 0;
      fsm_cond_16_1_36 <= 0;
      fsm_cond_16_2_37 <= 0;
      fsm_cond_16_2_38 <= 0;
      fsm_cond_16_3_39 <= 0;
      fsm_cond_16_3_40 <= 0;
      fsm_cond_16_3_41 <= 0;
      fsm_cond_16_4_42 <= 0;
      fsm_cond_16_4_43 <= 0;
      fsm_cond_16_4_44 <= 0;
      fsm_cond_16_4_45 <= 0;
      fsm_cond_17_1_46 <= 0;
      fsm_cond_17_2_47 <= 0;
      fsm_cond_17_2_48 <= 0;
      fsm_cond_17_3_49 <= 0;
      fsm_cond_17_3_50 <= 0;
      fsm_cond_17_3_51 <= 0;
      fsm_cond_17_4_52 <= 0;
      fsm_cond_17_4_53 <= 0;
      fsm_cond_17_4_54 <= 0;
      fsm_cond_17_4_55 <= 0;
      fsm_cond_18_1_56 <= 0;
      fsm_cond_18_2_57 <= 0;
      fsm_cond_18_2_58 <= 0;
      fsm_cond_18_3_59 <= 0;
      fsm_cond_18_3_60 <= 0;
      fsm_cond_18_3_61 <= 0;
      fsm_cond_18_4_62 <= 0;
      fsm_cond_18_4_63 <= 0;
      fsm_cond_18_4_64 <= 0;
      fsm_cond_18_4_65 <= 0;
      fsm_cond_19_1_66 <= 0;
      fsm_cond_19_2_67 <= 0;
      fsm_cond_19_2_68 <= 0;
      fsm_cond_19_3_69 <= 0;
      fsm_cond_19_3_70 <= 0;
      fsm_cond_19_3_71 <= 0;
      fsm_cond_19_4_72 <= 0;
      fsm_cond_19_4_73 <= 0;
      fsm_cond_19_4_74 <= 0;
      fsm_cond_19_4_75 <= 0;
      fsm_cond_20_1_76 <= 0;
      fsm_cond_20_2_77 <= 0;
      fsm_cond_20_2_78 <= 0;
      fsm_cond_20_3_79 <= 0;
      fsm_cond_20_3_80 <= 0;
      fsm_cond_20_3_81 <= 0;
      fsm_cond_20_4_82 <= 0;
      fsm_cond_20_4_83 <= 0;
      fsm_cond_20_4_84 <= 0;
      fsm_cond_20_4_85 <= 0;
    end else begin
      count <= count + 1;
      d1_fsm <= fsm;
      d2_fsm <= d1_fsm;
      d3_fsm <= d2_fsm;
      d4_fsm <= d3_fsm;

      case(d4_fsm)
        fsm_13: begin
          if(fsm_cond_13_4_15) begin
            valid <= 0;
          end 
        end
        fsm_14: begin
          if(fsm_cond_14_4_25) begin
            valid <= 0;
          end 
        end
        fsm_15: begin
          if(fsm_cond_15_4_35) begin
            valid <= 0;
          end 
        end
        fsm_16: begin
          if(fsm_cond_16_4_45) begin
            valid <= 0;
          end 
        end
        fsm_17: begin
          if(fsm_cond_17_4_55) begin
            valid <= 0;
          end 
        end
        fsm_18: begin
          if(fsm_cond_18_4_65) begin
            valid <= 0;
          end 
        end
        fsm_19: begin
          if(fsm_cond_19_4_75) begin
            valid <= 0;
          end 
        end
        fsm_20: begin
          if(fsm_cond_20_4_85) begin
            valid <= 0;
          end 
        end
      endcase

      case(d3_fsm)
        fsm_4: begin
          if(fsm_cond_4_3_5) begin
            valid <= 0;
          end 
        end
        fsm_13: begin
          if(fsm_cond_13_3_11) begin
            valid <= 1;
          end 
          fsm_cond_13_4_15 <= fsm_cond_13_4_14;
        end
        fsm_14: begin
          if(fsm_cond_14_3_21) begin
            valid <= 1;
          end 
          fsm_cond_14_4_25 <= fsm_cond_14_4_24;
        end
        fsm_15: begin
          if(fsm_cond_15_3_31) begin
            valid <= 1;
          end 
          fsm_cond_15_4_35 <= fsm_cond_15_4_34;
        end
        fsm_16: begin
          if(fsm_cond_16_3_41) begin
            valid <= 1;
          end 
          fsm_cond_16_4_45 <= fsm_cond_16_4_44;
        end
        fsm_17: begin
          if(fsm_cond_17_3_51) begin
            valid <= 1;
          end 
          fsm_cond_17_4_55 <= fsm_cond_17_4_54;
        end
        fsm_18: begin
          if(fsm_cond_18_3_61) begin
            valid <= 1;
          end 
          fsm_cond_18_4_65 <= fsm_cond_18_4_64;
        end
        fsm_19: begin
          if(fsm_cond_19_3_71) begin
            valid <= 1;
          end 
          fsm_cond_19_4_75 <= fsm_cond_19_4_74;
        end
        fsm_20: begin
          if(fsm_cond_20_3_81) begin
            valid <= 1;
          end 
          fsm_cond_20_4_85 <= fsm_cond_20_4_84;
        end
      endcase

      case(d2_fsm)
        fsm_4: begin
          if(fsm_cond_4_2_2) begin
            valid <= 1;
          end 
          fsm_cond_4_3_5 <= fsm_cond_4_3_4;
        end
        fsm_13: begin
          if(fsm_cond_13_2_8) begin
            valid <= 1;
          end 
          fsm_cond_13_3_11 <= fsm_cond_13_3_10;
          fsm_cond_13_4_14 <= fsm_cond_13_4_13;
        end
        fsm_14: begin
          if(fsm_cond_14_2_18) begin
            valid <= 1;
          end 
          fsm_cond_14_3_21 <= fsm_cond_14_3_20;
          fsm_cond_14_4_24 <= fsm_cond_14_4_23;
        end
        fsm_15: begin
          if(fsm_cond_15_2_28) begin
            valid <= 1;
          end 
          fsm_cond_15_3_31 <= fsm_cond_15_3_30;
          fsm_cond_15_4_34 <= fsm_cond_15_4_33;
        end
        fsm_16: begin
          if(fsm_cond_16_2_38) begin
            valid <= 1;
          end 
          fsm_cond_16_3_41 <= fsm_cond_16_3_40;
          fsm_cond_16_4_44 <= fsm_cond_16_4_43;
        end
        fsm_17: begin
          if(fsm_cond_17_2_48) begin
            valid <= 1;
          end 
          fsm_cond_17_3_51 <= fsm_cond_17_3_50;
          fsm_cond_17_4_54 <= fsm_cond_17_4_53;
        end
        fsm_18: begin
          if(fsm_cond_18_2_58) begin
            valid <= 1;
          end 
          fsm_cond_18_3_61 <= fsm_cond_18_3_60;
          fsm_cond_18_4_64 <= fsm_cond_18_4_63;
        end
        fsm_19: begin
          if(fsm_cond_19_2_68) begin
            valid <= 1;
          end 
          fsm_cond_19_3_71 <= fsm_cond_19_3_70;
          fsm_cond_19_4_74 <= fsm_cond_19_4_73;
        end
        fsm_20: begin
          if(fsm_cond_20_2_78) begin
            valid <= 1;
          end 
          fsm_cond_20_3_81 <= fsm_cond_20_3_80;
          fsm_cond_20_4_84 <= fsm_cond_20_4_83;
        end
      endcase

      case(d1_fsm)
        fsm_4: begin
          if(fsm_cond_4_1_0) begin
            valid <= 1;
          end 
          fsm_cond_4_2_2 <= fsm_cond_4_2_1;
          fsm_cond_4_3_4 <= fsm_cond_4_3_3;
        end
        fsm_13: begin
          if(fsm_cond_13_1_6) begin
            valid <= 1;
          end 
          fsm_cond_13_2_8 <= fsm_cond_13_2_7;
          fsm_cond_13_3_10 <= fsm_cond_13_3_9;
          fsm_cond_13_4_13 <= fsm_cond_13_4_12;
        end
        fsm_14: begin
          if(fsm_cond_14_1_16) begin
            valid <= 1;
          end 
          fsm_cond_14_2_18 <= fsm_cond_14_2_17;
          fsm_cond_14_3_20 <= fsm_cond_14_3_19;
          fsm_cond_14_4_23 <= fsm_cond_14_4_22;
        end
        fsm_15: begin
          if(fsm_cond_15_1_26) begin
            valid <= 1;
          end 
          fsm_cond_15_2_28 <= fsm_cond_15_2_27;
          fsm_cond_15_3_30 <= fsm_cond_15_3_29;
          fsm_cond_15_4_33 <= fsm_cond_15_4_32;
        end
        fsm_16: begin
          if(fsm_cond_16_1_36) begin
            valid <= 1;
          end 
          fsm_cond_16_2_38 <= fsm_cond_16_2_37;
          fsm_cond_16_3_40 <= fsm_cond_16_3_39;
          fsm_cond_16_4_43 <= fsm_cond_16_4_42;
        end
        fsm_17: begin
          if(fsm_cond_17_1_46) begin
            valid <= 1;
          end 
          fsm_cond_17_2_48 <= fsm_cond_17_2_47;
          fsm_cond_17_3_50 <= fsm_cond_17_3_49;
          fsm_cond_17_4_53 <= fsm_cond_17_4_52;
        end
        fsm_18: begin
          if(fsm_cond_18_1_56) begin
            valid <= 1;
          end 
          fsm_cond_18_2_58 <= fsm_cond_18_2_57;
          fsm_cond_18_3_60 <= fsm_cond_18_3_59;
          fsm_cond_18_4_63 <= fsm_cond_18_4_62;
        end
        fsm_19: begin
          if(fsm_cond_19_1_66) begin
            valid <= 1;
          end 
          fsm_cond_19_2_68 <= fsm_cond_19_2_67;
          fsm_cond_19_3_70 <= fsm_cond_19_3_69;
          fsm_cond_19_4_73 <= fsm_cond_19_4_72;
        end
        fsm_20: begin
          if(fsm_cond_20_1_76) begin
            valid <= 1;
          end 
          fsm_cond_20_2_78 <= fsm_cond_20_2_77;
          fsm_cond_20_3_80 <= fsm_cond_20_3_79;
          fsm_cond_20_4_83 <= fsm_cond_20_4_82;
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
          fsm_cond_4_1_0 <= (count >= 16);
          fsm_cond_4_2_1 <= (count >= 16);
          fsm_cond_4_3_3 <= (count >= 16);
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
          fsm_cond_13_1_6 <= (count >= 32);
          fsm_cond_13_2_7 <= (count >= 32);
          fsm_cond_13_3_9 <= (count >= 32);
          fsm_cond_13_4_12 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          fsm_cond_14_1_16 <= (count >= 32);
          fsm_cond_14_2_17 <= (count >= 32);
          fsm_cond_14_3_19 <= (count >= 32);
          fsm_cond_14_4_22 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          fsm_cond_15_1_26 <= (count >= 32);
          fsm_cond_15_2_27 <= (count >= 32);
          fsm_cond_15_3_29 <= (count >= 32);
          fsm_cond_15_4_32 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          fsm_cond_16_1_36 <= (count >= 32);
          fsm_cond_16_2_37 <= (count >= 32);
          fsm_cond_16_3_39 <= (count >= 32);
          fsm_cond_16_4_42 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          fsm_cond_17_1_46 <= (count >= 32);
          fsm_cond_17_2_47 <= (count >= 32);
          fsm_cond_17_3_49 <= (count >= 32);
          fsm_cond_17_4_52 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          fsm_cond_18_1_56 <= (count >= 32);
          fsm_cond_18_2_57 <= (count >= 32);
          fsm_cond_18_3_59 <= (count >= 32);
          fsm_cond_18_4_62 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          fsm_cond_19_1_66 <= (count >= 32);
          fsm_cond_19_2_67 <= (count >= 32);
          fsm_cond_19_3_69 <= (count >= 32);
          fsm_cond_19_4_72 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          fsm_cond_20_1_76 <= (count >= 32);
          fsm_cond_20_2_77 <= (count >= 32);
          fsm_cond_20_3_79 <= (count >= 32);
          fsm_cond_20_4_82 <= (count >= 32);
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
