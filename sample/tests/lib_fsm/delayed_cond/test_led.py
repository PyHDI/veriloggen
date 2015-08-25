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
  reg [(32 - 1):0] d2_fsm;
  reg [(32 - 1):0] d3_fsm;
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
  reg fsm_cond_13_3_3;
  reg fsm_cond_13_3_4;
  reg fsm_cond_13_3_5;
  localparam fsm_14 = 14;
  reg fsm_cond_14_3_6;
  reg fsm_cond_14_3_7;
  reg fsm_cond_14_3_8;
  localparam fsm_15 = 15;
  reg fsm_cond_15_3_9;
  reg fsm_cond_15_3_10;
  reg fsm_cond_15_3_11;
  localparam fsm_16 = 16;
  reg fsm_cond_16_3_12;
  reg fsm_cond_16_3_13;
  reg fsm_cond_16_3_14;
  localparam fsm_17 = 17;
  reg fsm_cond_17_3_15;
  reg fsm_cond_17_3_16;
  reg fsm_cond_17_3_17;
  localparam fsm_18 = 18;
  reg fsm_cond_18_3_18;
  reg fsm_cond_18_3_19;
  reg fsm_cond_18_3_20;
  localparam fsm_19 = 19;
  reg fsm_cond_19_3_21;
  reg fsm_cond_19_3_22;
  reg fsm_cond_19_3_23;
  localparam fsm_20 = 20;
  reg fsm_cond_20_3_24;
  reg fsm_cond_20_3_25;
  reg fsm_cond_20_3_26;
  localparam fsm_21 = 21;
  localparam fsm_22 = 22;
  localparam fsm_23 = 23;
  localparam fsm_24 = 24;
  localparam fsm_25 = 25;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      d1_fsm <= fsm_init;
      d2_fsm <= fsm_init;
      d3_fsm <= fsm_init;
    end else begin
      count <= count + 1;
      d1_fsm <= fsm;
      d2_fsm <= d1_fsm;
      d3_fsm <= d2_fsm;
      case(d3_fsm)
        fsm_4: begin
          if(fsm_cond_4_3_2) begin
            valid <= 0;
          end 
        end
        fsm_13: begin
          if(fsm_cond_13_3_5) begin
            valid <= 0;
          end 
        end
        fsm_14: begin
          if(fsm_cond_14_3_8) begin
            valid <= 0;
          end 
        end
        fsm_15: begin
          if(fsm_cond_15_3_11) begin
            valid <= 0;
          end 
        end
        fsm_16: begin
          if(fsm_cond_16_3_14) begin
            valid <= 0;
          end 
        end
        fsm_17: begin
          if(fsm_cond_17_3_17) begin
            valid <= 0;
          end 
        end
        fsm_18: begin
          if(fsm_cond_18_3_20) begin
            valid <= 0;
          end 
        end
        fsm_19: begin
          if(fsm_cond_19_3_23) begin
            valid <= 0;
          end 
        end
        fsm_20: begin
          if(fsm_cond_20_3_26) begin
            valid <= 0;
          end 
        end
      endcase
      case(d2_fsm)
        fsm_4: begin
          fsm_cond_4_3_2 <= fsm_cond_4_3_1;
        end
        fsm_13: begin
          fsm_cond_13_3_5 <= fsm_cond_13_3_4;
        end
        fsm_14: begin
          fsm_cond_14_3_8 <= fsm_cond_14_3_7;
        end
        fsm_15: begin
          fsm_cond_15_3_11 <= fsm_cond_15_3_10;
        end
        fsm_16: begin
          fsm_cond_16_3_14 <= fsm_cond_16_3_13;
        end
        fsm_17: begin
          fsm_cond_17_3_17 <= fsm_cond_17_3_16;
        end
        fsm_18: begin
          fsm_cond_18_3_20 <= fsm_cond_18_3_19;
        end
        fsm_19: begin
          fsm_cond_19_3_23 <= fsm_cond_19_3_22;
        end
        fsm_20: begin
          fsm_cond_20_3_26 <= fsm_cond_20_3_25;
        end
      endcase
      case(d1_fsm)
        fsm_4: begin
          fsm_cond_4_3_1 <= fsm_cond_4_3_0;
        end
        fsm_13: begin
          fsm_cond_13_3_4 <= fsm_cond_13_3_3;
        end
        fsm_14: begin
          fsm_cond_14_3_7 <= fsm_cond_14_3_6;
        end
        fsm_15: begin
          fsm_cond_15_3_10 <= fsm_cond_15_3_9;
        end
        fsm_16: begin
          fsm_cond_16_3_13 <= fsm_cond_16_3_12;
        end
        fsm_17: begin
          fsm_cond_17_3_16 <= fsm_cond_17_3_15;
        end
        fsm_18: begin
          fsm_cond_18_3_19 <= fsm_cond_18_3_18;
        end
        fsm_19: begin
          fsm_cond_19_3_22 <= fsm_cond_19_3_21;
        end
        fsm_20: begin
          fsm_cond_20_3_25 <= fsm_cond_20_3_24;
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
          if((count >= 16)) begin
            valid <= 1;
          end 
          fsm_cond_4_3_0 <= (count >= 16);
          if((count >= 16)) begin
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
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_13_3_3 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_14_3_6 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_15_3_9 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_16_3_12 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_17_3_15 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_18_3_18 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_19_3_21 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
          if((count >= 32)) begin
            valid <= 1;
          end 
          fsm_cond_20_3_24 <= (count >= 32);
          if((count >= 32)) begin
            fsm <= fsm_21;
          end 
        end
        fsm_21: begin
          fsm <= fsm_22;
        end
        fsm_22: begin
          fsm <= fsm_23;
        end
        fsm_23: begin
          fsm <= fsm_24;
        end
        fsm_24: begin
          fsm <= fsm_25;
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
