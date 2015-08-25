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
  reg [32-1:0] d2_fsm;
  reg [32-1:0] d3_fsm;

  reg fsm_cond_4_3_0;
  reg fsm_cond_4_3_1;
  reg fsm_cond_4_3_2;

  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;

  reg fsm_cond_13_1_3;
  reg [32-1:0] d4_fsm;

  reg fsm_cond_13_4_4;
  reg fsm_cond_13_4_5;
  reg fsm_cond_13_4_6;
  reg fsm_cond_13_4_7;

  localparam fsm_14 = 14;
  reg fsm_cond_14_1_8;
  reg fsm_cond_14_4_9;
  reg fsm_cond_14_4_10;
  reg fsm_cond_14_4_11;
  reg fsm_cond_14_4_12;

  localparam fsm_15 = 15;
  reg fsm_cond_15_1_13;
  reg fsm_cond_15_4_14;
  reg fsm_cond_15_4_15;
  reg fsm_cond_15_4_16;
  reg fsm_cond_15_4_17;

  localparam fsm_16 = 16;
  reg fsm_cond_16_1_18;
  reg fsm_cond_16_4_19;
  reg fsm_cond_16_4_20;
  reg fsm_cond_16_4_21;
  reg fsm_cond_16_4_22;

  localparam fsm_17 = 17;
  reg fsm_cond_17_1_23;
  reg fsm_cond_17_4_24;
  reg fsm_cond_17_4_25;
  reg fsm_cond_17_4_26;
  reg fsm_cond_17_4_27;

  localparam fsm_18 = 18;
  reg fsm_cond_18_1_28;
  reg fsm_cond_18_4_29;
  reg fsm_cond_18_4_30;
  reg fsm_cond_18_4_31;
  reg fsm_cond_18_4_32;

  localparam fsm_19 = 19;
  reg fsm_cond_19_1_33;
  reg fsm_cond_19_4_34;
  reg fsm_cond_19_4_35;
  reg fsm_cond_19_4_36;
  reg fsm_cond_19_4_37;

  localparam fsm_20 = 20;
  reg fsm_cond_20_1_38;
  reg fsm_cond_20_4_39;
  reg fsm_cond_20_4_40;
  reg fsm_cond_20_4_41;
  reg fsm_cond_20_4_42;

  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      d1_fsm <= fsm_init;
      d2_fsm <= fsm_init;
      d3_fsm <= fsm_init;
      fsm_cond_4_3_0 <= 0;
      fsm_cond_4_3_1 <= 0;
      fsm_cond_4_3_2 <= 0;
      fsm_cond_13_1_3 <= 0;
      d4_fsm <= fsm_init;
      fsm_cond_13_4_4 <= 0;
      fsm_cond_13_4_5 <= 0;
      fsm_cond_13_4_6 <= 0;
      fsm_cond_13_4_7 <= 0;
      fsm_cond_14_1_8 <= 0;
      fsm_cond_14_4_9 <= 0;
      fsm_cond_14_4_10 <= 0;
      fsm_cond_14_4_11 <= 0;
      fsm_cond_14_4_12 <= 0;
      fsm_cond_15_1_13 <= 0;
      fsm_cond_15_4_14 <= 0;
      fsm_cond_15_4_15 <= 0;
      fsm_cond_15_4_16 <= 0;
      fsm_cond_15_4_17 <= 0;
      fsm_cond_16_1_18 <= 0;
      fsm_cond_16_4_19 <= 0;
      fsm_cond_16_4_20 <= 0;
      fsm_cond_16_4_21 <= 0;
      fsm_cond_16_4_22 <= 0;
      fsm_cond_17_1_23 <= 0;
      fsm_cond_17_4_24 <= 0;
      fsm_cond_17_4_25 <= 0;
      fsm_cond_17_4_26 <= 0;
      fsm_cond_17_4_27 <= 0;
      fsm_cond_18_1_28 <= 0;
      fsm_cond_18_4_29 <= 0;
      fsm_cond_18_4_30 <= 0;
      fsm_cond_18_4_31 <= 0;
      fsm_cond_18_4_32 <= 0;
      fsm_cond_19_1_33 <= 0;
      fsm_cond_19_4_34 <= 0;
      fsm_cond_19_4_35 <= 0;
      fsm_cond_19_4_36 <= 0;
      fsm_cond_19_4_37 <= 0;
      fsm_cond_20_1_38 <= 0;
      fsm_cond_20_4_39 <= 0;
      fsm_cond_20_4_40 <= 0;
      fsm_cond_20_4_41 <= 0;
      fsm_cond_20_4_42 <= 0;
    end else begin
      count <= count + 1;
      d1_fsm <= fsm;
      d2_fsm <= d1_fsm;
      d3_fsm <= d2_fsm;
      d4_fsm <= d3_fsm;
      case(d4_fsm)
        fsm_13: begin
          if(fsm_cond_13_4_7) begin
            valid <= 0;
          end 
        end
        fsm_14: begin
          if(fsm_cond_14_4_12) begin
            valid <= 0;
          end 
        end
        fsm_15: begin
          if(fsm_cond_15_4_17) begin
            valid <= 0;
          end 
        end
        fsm_16: begin
          if(fsm_cond_16_4_22) begin
            valid <= 0;
          end 
        end
        fsm_17: begin
          if(fsm_cond_17_4_27) begin
            valid <= 0;
          end 
        end
        fsm_18: begin
          if(fsm_cond_18_4_32) begin
            valid <= 0;
          end 
        end
        fsm_19: begin
          if(fsm_cond_19_4_37) begin
            valid <= 0;
          end 
        end
        fsm_20: begin
          if(fsm_cond_20_4_42) begin
            valid <= 0;
          end 
        end
      endcase
      case(d3_fsm)
        fsm_4: begin
          if(fsm_cond_4_3_2) begin
            valid <= 0;
          end 
        end
        fsm_13: begin
          fsm_cond_13_4_7 <= fsm_cond_13_4_6;
        end
        fsm_14: begin
          fsm_cond_14_4_12 <= fsm_cond_14_4_11;
        end
        fsm_15: begin
          fsm_cond_15_4_17 <= fsm_cond_15_4_16;
        end
        fsm_16: begin
          fsm_cond_16_4_22 <= fsm_cond_16_4_21;
        end
        fsm_17: begin
          fsm_cond_17_4_27 <= fsm_cond_17_4_26;
        end
        fsm_18: begin
          fsm_cond_18_4_32 <= fsm_cond_18_4_31;
        end
        fsm_19: begin
          fsm_cond_19_4_37 <= fsm_cond_19_4_36;
        end
        fsm_20: begin
          fsm_cond_20_4_42 <= fsm_cond_20_4_41;
        end
      endcase
      case(d2_fsm)
        fsm_4: begin
          fsm_cond_4_3_2 <= fsm_cond_4_3_1;
        end
        fsm_13: begin
          fsm_cond_13_4_6 <= fsm_cond_13_4_5;
        end
        fsm_14: begin
          fsm_cond_14_4_11 <= fsm_cond_14_4_10;
        end
        fsm_15: begin
          fsm_cond_15_4_16 <= fsm_cond_15_4_15;
        end
        fsm_16: begin
          fsm_cond_16_4_21 <= fsm_cond_16_4_20;
        end
        fsm_17: begin
          fsm_cond_17_4_26 <= fsm_cond_17_4_25;
        end
        fsm_18: begin
          fsm_cond_18_4_31 <= fsm_cond_18_4_30;
        end
        fsm_19: begin
          fsm_cond_19_4_36 <= fsm_cond_19_4_35;
        end
        fsm_20: begin
          fsm_cond_20_4_41 <= fsm_cond_20_4_40;
        end
      endcase
      case(d1_fsm)
        fsm_4: begin
          fsm_cond_4_3_1 <= fsm_cond_4_3_0;
        end
        fsm_13: begin
          if(fsm_cond_13_1_3) begin
            valid <= 1;
          end 
          fsm_cond_13_4_5 <= fsm_cond_13_4_4;
        end
        fsm_14: begin
          if(fsm_cond_14_1_8) begin
            valid <= 1;
          end 
          fsm_cond_14_4_10 <= fsm_cond_14_4_9;
        end
        fsm_15: begin
          if(fsm_cond_15_1_13) begin
            valid <= 1;
          end 
          fsm_cond_15_4_15 <= fsm_cond_15_4_14;
        end
        fsm_16: begin
          if(fsm_cond_16_1_18) begin
            valid <= 1;
          end 
          fsm_cond_16_4_20 <= fsm_cond_16_4_19;
        end
        fsm_17: begin
          if(fsm_cond_17_1_23) begin
            valid <= 1;
          end 
          fsm_cond_17_4_25 <= fsm_cond_17_4_24;
        end
        fsm_18: begin
          if(fsm_cond_18_1_28) begin
            valid <= 1;
          end 
          fsm_cond_18_4_30 <= fsm_cond_18_4_29;
        end
        fsm_19: begin
          if(fsm_cond_19_1_33) begin
            valid <= 1;
          end 
          fsm_cond_19_4_35 <= fsm_cond_19_4_34;
        end
        fsm_20: begin
          if(fsm_cond_20_1_38) begin
            valid <= 1;
          end 
          fsm_cond_20_4_40 <= fsm_cond_20_4_39;
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
          fsm_cond_4_3_0 <= (count >= 16);
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
          fsm_cond_13_1_3 <= (count >= 32);
          fsm_cond_13_4_4 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          fsm_cond_14_1_8 <= (count >= 32);
          fsm_cond_14_4_9 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          fsm_cond_15_1_13 <= (count >= 32);
          fsm_cond_15_4_14 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          fsm_cond_16_1_18 <= (count >= 32);
          fsm_cond_16_4_19 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          fsm_cond_17_1_23 <= (count >= 32);
          fsm_cond_17_4_24 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          fsm_cond_18_1_28 <= (count >= 32);
          fsm_cond_18_4_29 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          fsm_cond_19_1_33 <= (count >= 32);
          fsm_cond_19_4_34 <= (count >= 32);
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          fsm_cond_20_1_38 <= (count >= 32);
          fsm_cond_20_4_39 <= (count >= 32);
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
