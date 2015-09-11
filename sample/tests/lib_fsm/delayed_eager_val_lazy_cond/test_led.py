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
  reg _valid_4_0_1;
  reg [32-1:0] _d2_fsm;
  reg _valid_4_1_1;
  reg _valid_4_1_2;
  reg [32-1:0] _d3_fsm;
  reg _valid_4_2_1;
  reg _valid_4_2_2;
  reg _valid_4_2_3;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  reg _valid_13_3_1;
  reg _valid_13_4_1;
  reg _valid_13_4_2;
  reg _valid_13_5_1;
  reg _valid_13_5_2;
  reg _valid_13_5_3;
  reg [32-1:0] _d4_fsm;
  reg _valid_13_6_1;
  reg _valid_13_6_2;
  reg _valid_13_6_3;
  reg _valid_13_6_4;
  localparam fsm_14 = 14;
  reg _valid_14_7_1;
  reg _valid_14_8_1;
  reg _valid_14_8_2;
  reg _valid_14_9_1;
  reg _valid_14_9_2;
  reg _valid_14_9_3;
  reg _valid_14_10_1;
  reg _valid_14_10_2;
  reg _valid_14_10_3;
  reg _valid_14_10_4;
  localparam fsm_15 = 15;
  reg _valid_15_11_1;
  reg _valid_15_12_1;
  reg _valid_15_12_2;
  reg _valid_15_13_1;
  reg _valid_15_13_2;
  reg _valid_15_13_3;
  reg _valid_15_14_1;
  reg _valid_15_14_2;
  reg _valid_15_14_3;
  reg _valid_15_14_4;
  localparam fsm_16 = 16;
  reg _valid_16_15_1;
  reg _valid_16_16_1;
  reg _valid_16_16_2;
  reg _valid_16_17_1;
  reg _valid_16_17_2;
  reg _valid_16_17_3;
  reg _valid_16_18_1;
  reg _valid_16_18_2;
  reg _valid_16_18_3;
  reg _valid_16_18_4;
  localparam fsm_17 = 17;
  reg _valid_17_19_1;
  reg _valid_17_20_1;
  reg _valid_17_20_2;
  reg _valid_17_21_1;
  reg _valid_17_21_2;
  reg _valid_17_21_3;
  reg _valid_17_22_1;
  reg _valid_17_22_2;
  reg _valid_17_22_3;
  reg _valid_17_22_4;
  localparam fsm_18 = 18;
  reg _valid_18_23_1;
  reg _valid_18_24_1;
  reg _valid_18_24_2;
  reg _valid_18_25_1;
  reg _valid_18_25_2;
  reg _valid_18_25_3;
  reg _valid_18_26_1;
  reg _valid_18_26_2;
  reg _valid_18_26_3;
  reg _valid_18_26_4;
  localparam fsm_19 = 19;
  reg _valid_19_27_1;
  reg _valid_19_28_1;
  reg _valid_19_28_2;
  reg _valid_19_29_1;
  reg _valid_19_29_2;
  reg _valid_19_29_3;
  reg _valid_19_30_1;
  reg _valid_19_30_2;
  reg _valid_19_30_3;
  reg _valid_19_30_4;
  localparam fsm_20 = 20;
  reg _valid_20_31_1;
  reg _valid_20_32_1;
  reg _valid_20_32_2;
  reg _valid_20_33_1;
  reg _valid_20_33_2;
  reg _valid_20_33_3;
  reg _valid_20_34_1;
  reg _valid_20_34_2;
  reg _valid_20_34_3;
  reg _valid_20_34_4;
  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _valid_4_0_1 <= 0;
      _d2_fsm <= fsm_init;
      _valid_4_1_1 <= 0;
      _valid_4_1_2 <= 0;
      _d3_fsm <= fsm_init;
      _valid_4_2_1 <= 0;
      _valid_4_2_2 <= 0;
      _valid_4_2_3 <= 0;
      _valid_13_3_1 <= 0;
      _valid_13_4_1 <= 0;
      _valid_13_4_2 <= 0;
      _valid_13_5_1 <= 0;
      _valid_13_5_2 <= 0;
      _valid_13_5_3 <= 0;
      _d4_fsm <= fsm_init;
      _valid_13_6_1 <= 0;
      _valid_13_6_2 <= 0;
      _valid_13_6_3 <= 0;
      _valid_13_6_4 <= 0;
      _valid_14_7_1 <= 0;
      _valid_14_8_1 <= 0;
      _valid_14_8_2 <= 0;
      _valid_14_9_1 <= 0;
      _valid_14_9_2 <= 0;
      _valid_14_9_3 <= 0;
      _valid_14_10_1 <= 0;
      _valid_14_10_2 <= 0;
      _valid_14_10_3 <= 0;
      _valid_14_10_4 <= 0;
      _valid_15_11_1 <= 0;
      _valid_15_12_1 <= 0;
      _valid_15_12_2 <= 0;
      _valid_15_13_1 <= 0;
      _valid_15_13_2 <= 0;
      _valid_15_13_3 <= 0;
      _valid_15_14_1 <= 0;
      _valid_15_14_2 <= 0;
      _valid_15_14_3 <= 0;
      _valid_15_14_4 <= 0;
      _valid_16_15_1 <= 0;
      _valid_16_16_1 <= 0;
      _valid_16_16_2 <= 0;
      _valid_16_17_1 <= 0;
      _valid_16_17_2 <= 0;
      _valid_16_17_3 <= 0;
      _valid_16_18_1 <= 0;
      _valid_16_18_2 <= 0;
      _valid_16_18_3 <= 0;
      _valid_16_18_4 <= 0;
      _valid_17_19_1 <= 0;
      _valid_17_20_1 <= 0;
      _valid_17_20_2 <= 0;
      _valid_17_21_1 <= 0;
      _valid_17_21_2 <= 0;
      _valid_17_21_3 <= 0;
      _valid_17_22_1 <= 0;
      _valid_17_22_2 <= 0;
      _valid_17_22_3 <= 0;
      _valid_17_22_4 <= 0;
      _valid_18_23_1 <= 0;
      _valid_18_24_1 <= 0;
      _valid_18_24_2 <= 0;
      _valid_18_25_1 <= 0;
      _valid_18_25_2 <= 0;
      _valid_18_25_3 <= 0;
      _valid_18_26_1 <= 0;
      _valid_18_26_2 <= 0;
      _valid_18_26_3 <= 0;
      _valid_18_26_4 <= 0;
      _valid_19_27_1 <= 0;
      _valid_19_28_1 <= 0;
      _valid_19_28_2 <= 0;
      _valid_19_29_1 <= 0;
      _valid_19_29_2 <= 0;
      _valid_19_29_3 <= 0;
      _valid_19_30_1 <= 0;
      _valid_19_30_2 <= 0;
      _valid_19_30_3 <= 0;
      _valid_19_30_4 <= 0;
      _valid_20_31_1 <= 0;
      _valid_20_32_1 <= 0;
      _valid_20_32_2 <= 0;
      _valid_20_33_1 <= 0;
      _valid_20_33_2 <= 0;
      _valid_20_33_3 <= 0;
      _valid_20_34_1 <= 0;
      _valid_20_34_2 <= 0;
      _valid_20_34_3 <= 0;
      _valid_20_34_4 <= 0;
    end else begin
      count <= (count + 1);
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;
      case(_d4_fsm)
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_6_4;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_10_4;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_14_4;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_18_4;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_22_4;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_26_4;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_30_4;
          end 
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_34_4;
          end 
        end
      endcase
      case(_d3_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= _valid_4_2_3;
          end 
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_5_3;
          end 
          _valid_13_6_4 <= _valid_13_6_3;
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_9_3;
          end 
          _valid_14_10_4 <= _valid_14_10_3;
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_13_3;
          end 
          _valid_15_14_4 <= _valid_15_14_3;
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_17_3;
          end 
          _valid_16_18_4 <= _valid_16_18_3;
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_21_3;
          end 
          _valid_17_22_4 <= _valid_17_22_3;
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_25_3;
          end 
          _valid_18_26_4 <= _valid_18_26_3;
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_29_3;
          end 
          _valid_19_30_4 <= _valid_19_30_3;
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_33_3;
          end 
          _valid_20_34_4 <= _valid_20_34_3;
        end
      endcase
      case(_d2_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= _valid_4_1_2;
          end 
          _valid_4_2_3 <= _valid_4_2_2;
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_4_2;
          end 
          _valid_13_5_3 <= _valid_13_5_2;
          _valid_13_6_3 <= _valid_13_6_2;
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_8_2;
          end 
          _valid_14_9_3 <= _valid_14_9_2;
          _valid_14_10_3 <= _valid_14_10_2;
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_12_2;
          end 
          _valid_15_13_3 <= _valid_15_13_2;
          _valid_15_14_3 <= _valid_15_14_2;
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_16_2;
          end 
          _valid_16_17_3 <= _valid_16_17_2;
          _valid_16_18_3 <= _valid_16_18_2;
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_20_2;
          end 
          _valid_17_21_3 <= _valid_17_21_2;
          _valid_17_22_3 <= _valid_17_22_2;
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_24_2;
          end 
          _valid_18_25_3 <= _valid_18_25_2;
          _valid_18_26_3 <= _valid_18_26_2;
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_28_2;
          end 
          _valid_19_29_3 <= _valid_19_29_2;
          _valid_19_30_3 <= _valid_19_30_2;
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_32_2;
          end 
          _valid_20_33_3 <= _valid_20_33_2;
          _valid_20_34_3 <= _valid_20_34_2;
        end
      endcase
      case(_d1_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= _valid_4_0_1;
          end 
          _valid_4_1_2 <= _valid_4_1_1;
          _valid_4_2_2 <= _valid_4_2_1;
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= _valid_13_3_1;
          end 
          _valid_13_4_2 <= _valid_13_4_1;
          _valid_13_5_2 <= _valid_13_5_1;
          _valid_13_6_2 <= _valid_13_6_1;
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= _valid_14_7_1;
          end 
          _valid_14_8_2 <= _valid_14_8_1;
          _valid_14_9_2 <= _valid_14_9_1;
          _valid_14_10_2 <= _valid_14_10_1;
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= _valid_15_11_1;
          end 
          _valid_15_12_2 <= _valid_15_12_1;
          _valid_15_13_2 <= _valid_15_13_1;
          _valid_15_14_2 <= _valid_15_14_1;
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= _valid_16_15_1;
          end 
          _valid_16_16_2 <= _valid_16_16_1;
          _valid_16_17_2 <= _valid_16_17_1;
          _valid_16_18_2 <= _valid_16_18_1;
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= _valid_17_19_1;
          end 
          _valid_17_20_2 <= _valid_17_20_1;
          _valid_17_21_2 <= _valid_17_21_1;
          _valid_17_22_2 <= _valid_17_22_1;
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= _valid_18_23_1;
          end 
          _valid_18_24_2 <= _valid_18_24_1;
          _valid_18_25_2 <= _valid_18_25_1;
          _valid_18_26_2 <= _valid_18_26_1;
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= _valid_19_27_1;
          end 
          _valid_19_28_2 <= _valid_19_28_1;
          _valid_19_29_2 <= _valid_19_29_1;
          _valid_19_30_2 <= _valid_19_30_1;
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= _valid_20_31_1;
          end 
          _valid_20_32_2 <= _valid_20_32_1;
          _valid_20_33_2 <= _valid_20_33_1;
          _valid_20_34_2 <= _valid_20_34_1;
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
          _valid_4_0_1 <= up;
          _valid_4_1_1 <= up;
          _valid_4_2_1 <= down;
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
          _valid_13_3_1 <= up;
          _valid_13_4_1 <= up;
          _valid_13_5_1 <= up;
          _valid_13_6_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          _valid_14_7_1 <= up;
          _valid_14_8_1 <= up;
          _valid_14_9_1 <= up;
          _valid_14_10_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          _valid_15_11_1 <= up;
          _valid_15_12_1 <= up;
          _valid_15_13_1 <= up;
          _valid_15_14_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          _valid_16_15_1 <= up;
          _valid_16_16_1 <= up;
          _valid_16_17_1 <= up;
          _valid_16_18_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          _valid_17_19_1 <= up;
          _valid_17_20_1 <= up;
          _valid_17_21_1 <= up;
          _valid_17_22_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          _valid_18_23_1 <= up;
          _valid_18_24_1 <= up;
          _valid_18_25_1 <= up;
          _valid_18_26_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          _valid_19_27_1 <= up;
          _valid_19_28_1 <= up;
          _valid_19_29_1 <= up;
          _valid_19_30_1 <= down;
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          _valid_20_31_1 <= up;
          _valid_20_32_1 <= up;
          _valid_20_33_1 <= up;
          _valid_20_34_1 <= down;
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
