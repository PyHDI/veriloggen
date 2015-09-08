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
  reg _valid_4_1_0;
  reg [32-1:0] _d2_fsm;
  reg _valid_4_2_1;
  reg _valid_4_2_2;
  reg [32-1:0] _d3_fsm;
  reg _valid_4_3_3;
  reg _valid_4_3_4;
  reg _valid_4_3_5;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  reg _valid_13_1_6;
  reg _valid_13_2_7;
  reg _valid_13_2_8;
  reg _valid_13_3_9;
  reg _valid_13_3_10;
  reg _valid_13_3_11;
  reg [32-1:0] _d4_fsm;
  reg _valid_13_4_12;
  reg _valid_13_4_13;
  reg _valid_13_4_14;
  reg _valid_13_4_15;
  localparam fsm_14 = 14;
  reg _valid_14_1_16;
  reg _valid_14_2_17;
  reg _valid_14_2_18;
  reg _valid_14_3_19;
  reg _valid_14_3_20;
  reg _valid_14_3_21;
  reg _valid_14_4_22;
  reg _valid_14_4_23;
  reg _valid_14_4_24;
  reg _valid_14_4_25;
  localparam fsm_15 = 15;
  reg _valid_15_1_26;
  reg _valid_15_2_27;
  reg _valid_15_2_28;
  reg _valid_15_3_29;
  reg _valid_15_3_30;
  reg _valid_15_3_31;
  reg _valid_15_4_32;
  reg _valid_15_4_33;
  reg _valid_15_4_34;
  reg _valid_15_4_35;
  localparam fsm_16 = 16;
  reg _valid_16_1_36;
  reg _valid_16_2_37;
  reg _valid_16_2_38;
  reg _valid_16_3_39;
  reg _valid_16_3_40;
  reg _valid_16_3_41;
  reg _valid_16_4_42;
  reg _valid_16_4_43;
  reg _valid_16_4_44;
  reg _valid_16_4_45;
  localparam fsm_17 = 17;
  reg _valid_17_1_46;
  reg _valid_17_2_47;
  reg _valid_17_2_48;
  reg _valid_17_3_49;
  reg _valid_17_3_50;
  reg _valid_17_3_51;
  reg _valid_17_4_52;
  reg _valid_17_4_53;
  reg _valid_17_4_54;
  reg _valid_17_4_55;
  localparam fsm_18 = 18;
  reg _valid_18_1_56;
  reg _valid_18_2_57;
  reg _valid_18_2_58;
  reg _valid_18_3_59;
  reg _valid_18_3_60;
  reg _valid_18_3_61;
  reg _valid_18_4_62;
  reg _valid_18_4_63;
  reg _valid_18_4_64;
  reg _valid_18_4_65;
  localparam fsm_19 = 19;
  reg _valid_19_1_66;
  reg _valid_19_2_67;
  reg _valid_19_2_68;
  reg _valid_19_3_69;
  reg _valid_19_3_70;
  reg _valid_19_3_71;
  reg _valid_19_4_72;
  reg _valid_19_4_73;
  reg _valid_19_4_74;
  reg _valid_19_4_75;
  localparam fsm_20 = 20;
  reg _valid_20_1_76;
  reg _valid_20_2_77;
  reg _valid_20_2_78;
  reg _valid_20_3_79;
  reg _valid_20_3_80;
  reg _valid_20_3_81;
  reg _valid_20_4_82;
  reg _valid_20_4_83;
  reg _valid_20_4_84;
  reg _valid_20_4_85;
  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _valid_4_1_0 <= 0;
      _d2_fsm <= fsm_init;
      _valid_4_2_1 <= 0;
      _valid_4_2_2 <= 0;
      _d3_fsm <= fsm_init;
      _valid_4_3_3 <= 0;
      _valid_4_3_4 <= 0;
      _valid_4_3_5 <= 0;
      _valid_13_1_6 <= 0;
      _valid_13_2_7 <= 0;
      _valid_13_2_8 <= 0;
      _valid_13_3_9 <= 0;
      _valid_13_3_10 <= 0;
      _valid_13_3_11 <= 0;
      _d4_fsm <= fsm_init;
      _valid_13_4_12 <= 0;
      _valid_13_4_13 <= 0;
      _valid_13_4_14 <= 0;
      _valid_13_4_15 <= 0;
      _valid_14_1_16 <= 0;
      _valid_14_2_17 <= 0;
      _valid_14_2_18 <= 0;
      _valid_14_3_19 <= 0;
      _valid_14_3_20 <= 0;
      _valid_14_3_21 <= 0;
      _valid_14_4_22 <= 0;
      _valid_14_4_23 <= 0;
      _valid_14_4_24 <= 0;
      _valid_14_4_25 <= 0;
      _valid_15_1_26 <= 0;
      _valid_15_2_27 <= 0;
      _valid_15_2_28 <= 0;
      _valid_15_3_29 <= 0;
      _valid_15_3_30 <= 0;
      _valid_15_3_31 <= 0;
      _valid_15_4_32 <= 0;
      _valid_15_4_33 <= 0;
      _valid_15_4_34 <= 0;
      _valid_15_4_35 <= 0;
      _valid_16_1_36 <= 0;
      _valid_16_2_37 <= 0;
      _valid_16_2_38 <= 0;
      _valid_16_3_39 <= 0;
      _valid_16_3_40 <= 0;
      _valid_16_3_41 <= 0;
      _valid_16_4_42 <= 0;
      _valid_16_4_43 <= 0;
      _valid_16_4_44 <= 0;
      _valid_16_4_45 <= 0;
      _valid_17_1_46 <= 0;
      _valid_17_2_47 <= 0;
      _valid_17_2_48 <= 0;
      _valid_17_3_49 <= 0;
      _valid_17_3_50 <= 0;
      _valid_17_3_51 <= 0;
      _valid_17_4_52 <= 0;
      _valid_17_4_53 <= 0;
      _valid_17_4_54 <= 0;
      _valid_17_4_55 <= 0;
      _valid_18_1_56 <= 0;
      _valid_18_2_57 <= 0;
      _valid_18_2_58 <= 0;
      _valid_18_3_59 <= 0;
      _valid_18_3_60 <= 0;
      _valid_18_3_61 <= 0;
      _valid_18_4_62 <= 0;
      _valid_18_4_63 <= 0;
      _valid_18_4_64 <= 0;
      _valid_18_4_65 <= 0;
      _valid_19_1_66 <= 0;
      _valid_19_2_67 <= 0;
      _valid_19_2_68 <= 0;
      _valid_19_3_69 <= 0;
      _valid_19_3_70 <= 0;
      _valid_19_3_71 <= 0;
      _valid_19_4_72 <= 0;
      _valid_19_4_73 <= 0;
      _valid_19_4_74 <= 0;
      _valid_19_4_75 <= 0;
      _valid_20_1_76 <= 0;
      _valid_20_2_77 <= 0;
      _valid_20_2_78 <= 0;
      _valid_20_3_79 <= 0;
      _valid_20_3_80 <= 0;
      _valid_20_3_81 <= 0;
      _valid_20_4_82 <= 0;
      _valid_20_4_83 <= 0;
      _valid_20_4_84 <= 0;
      _valid_20_4_85 <= 0;
    end else begin
      count <= (count + 1);
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;
      case(_d4_fsm)
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_4_15;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_4_25;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_4_35;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_4_45;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_4_55;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_4_65;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_4_75;
          end 
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_4_85;
          end 
        end
      endcase
      case(_d3_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= _valid_4_3_5;
          end 
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_3_11;
          end 
          _valid_13_4_15 <= _valid_13_4_14;
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_3_21;
          end 
          _valid_14_4_25 <= _valid_14_4_24;
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_3_31;
          end 
          _valid_15_4_35 <= _valid_15_4_34;
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_3_41;
          end 
          _valid_16_4_45 <= _valid_16_4_44;
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_3_51;
          end 
          _valid_17_4_55 <= _valid_17_4_54;
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_3_61;
          end 
          _valid_18_4_65 <= _valid_18_4_64;
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_3_71;
          end 
          _valid_19_4_75 <= _valid_19_4_74;
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_3_81;
          end 
          _valid_20_4_85 <= _valid_20_4_84;
        end
      endcase
      case(_d2_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= _valid_4_2_2;
          end 
          _valid_4_3_5 <= _valid_4_3_4;
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_2_8;
          end 
          _valid_13_3_11 <= _valid_13_3_10;
          _valid_13_4_14 <= _valid_13_4_13;
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_2_18;
          end 
          _valid_14_3_21 <= _valid_14_3_20;
          _valid_14_4_24 <= _valid_14_4_23;
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_2_28;
          end 
          _valid_15_3_31 <= _valid_15_3_30;
          _valid_15_4_34 <= _valid_15_4_33;
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_2_38;
          end 
          _valid_16_3_41 <= _valid_16_3_40;
          _valid_16_4_44 <= _valid_16_4_43;
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_2_48;
          end 
          _valid_17_3_51 <= _valid_17_3_50;
          _valid_17_4_54 <= _valid_17_4_53;
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_2_58;
          end 
          _valid_18_3_61 <= _valid_18_3_60;
          _valid_18_4_64 <= _valid_18_4_63;
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_2_68;
          end 
          _valid_19_3_71 <= _valid_19_3_70;
          _valid_19_4_74 <= _valid_19_4_73;
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_2_78;
          end 
          _valid_20_3_81 <= _valid_20_3_80;
          _valid_20_4_84 <= _valid_20_4_83;
        end
      endcase
      case(_d1_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= _valid_4_1_0;
          end 
          _valid_4_2_2 <= _valid_4_2_1;
          _valid_4_3_4 <= _valid_4_3_3;
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_1_6;
          end 
          _valid_13_2_8 <= _valid_13_2_7;
          _valid_13_3_10 <= _valid_13_3_9;
          _valid_13_4_13 <= _valid_13_4_12;
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_1_16;
          end 
          _valid_14_2_18 <= _valid_14_2_17;
          _valid_14_3_20 <= _valid_14_3_19;
          _valid_14_4_23 <= _valid_14_4_22;
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_1_26;
          end 
          _valid_15_2_28 <= _valid_15_2_27;
          _valid_15_3_30 <= _valid_15_3_29;
          _valid_15_4_33 <= _valid_15_4_32;
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_1_36;
          end 
          _valid_16_2_38 <= _valid_16_2_37;
          _valid_16_3_40 <= _valid_16_3_39;
          _valid_16_4_43 <= _valid_16_4_42;
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_1_46;
          end 
          _valid_17_2_48 <= _valid_17_2_47;
          _valid_17_3_50 <= _valid_17_3_49;
          _valid_17_4_53 <= _valid_17_4_52;
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_1_56;
          end 
          _valid_18_2_58 <= _valid_18_2_57;
          _valid_18_3_60 <= _valid_18_3_59;
          _valid_18_4_63 <= _valid_18_4_62;
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_1_66;
          end 
          _valid_19_2_68 <= _valid_19_2_67;
          _valid_19_3_70 <= _valid_19_3_69;
          _valid_19_4_73 <= _valid_19_4_72;
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_1_76;
          end 
          _valid_20_2_78 <= _valid_20_2_77;
          _valid_20_3_80 <= _valid_20_3_79;
          _valid_20_4_83 <= _valid_20_4_82;
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
            valid <= up;
          end 
          _valid_4_1_0 <= up;
          _valid_4_2_1 <= up;
          _valid_4_3_3 <= down;
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
          _valid_13_1_6 <= up;
          _valid_13_2_7 <= up;
          _valid_13_3_9 <= up;
          _valid_13_4_12 <= down;
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          _valid_14_1_16 <= up;
          _valid_14_2_17 <= up;
          _valid_14_3_19 <= up;
          _valid_14_4_22 <= down;
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          _valid_15_1_26 <= up;
          _valid_15_2_27 <= up;
          _valid_15_3_29 <= up;
          _valid_15_4_32 <= down;
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          _valid_16_1_36 <= up;
          _valid_16_2_37 <= up;
          _valid_16_3_39 <= up;
          _valid_16_4_42 <= down;
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          _valid_17_1_46 <= up;
          _valid_17_2_47 <= up;
          _valid_17_3_49 <= up;
          _valid_17_4_52 <= down;
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          _valid_18_1_56 <= up;
          _valid_18_2_57 <= up;
          _valid_18_3_59 <= up;
          _valid_18_4_62 <= down;
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          _valid_19_1_66 <= up;
          _valid_19_2_67 <= up;
          _valid_19_3_69 <= up;
          _valid_19_4_72 <= down;
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          _valid_20_1_76 <= up;
          _valid_20_2_77 <= up;
          _valid_20_3_79 <= up;
          _valid_20_4_82 <= down;
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
