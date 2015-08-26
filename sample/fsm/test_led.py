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
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  reg fsm_cond_8_1_0;

  reg [32-1:0] d2_fsm;
  reg fsm_cond_8_2_1;
  reg fsm_cond_8_2_2;

  reg [32-1:0] d3_fsm;
  reg fsm_cond_8_3_3;
  reg fsm_cond_8_3_4;
  reg fsm_cond_8_3_5;

  localparam fsm_9 = 9;
  reg fsm_cond_9_1_6;
  reg fsm_cond_9_2_7;
  reg fsm_cond_9_2_8;
  reg fsm_cond_9_3_9;
  reg fsm_cond_9_3_10;
  reg fsm_cond_9_3_11;

  localparam fsm_10 = 10;
  reg fsm_cond_10_1_12;
  reg fsm_cond_10_2_13;
  reg fsm_cond_10_2_14;
  reg fsm_cond_10_3_15;
  reg fsm_cond_10_3_16;
  reg fsm_cond_10_3_17;

  localparam fsm_11 = 11;
  reg fsm_cond_11_1_18;
  reg fsm_cond_11_2_19;
  reg fsm_cond_11_2_20;
  reg fsm_cond_11_3_21;
  reg fsm_cond_11_3_22;
  reg fsm_cond_11_3_23;

  localparam fsm_12 = 12;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      d1_fsm <= fsm_init;
      fsm_cond_8_1_0 <= 0;
      d2_fsm <= fsm_init;
      fsm_cond_8_2_1 <= 0;
      fsm_cond_8_2_2 <= 0;
      d3_fsm <= fsm_init;
      fsm_cond_8_3_3 <= 0;
      fsm_cond_8_3_4 <= 0;
      fsm_cond_8_3_5 <= 0;
      fsm_cond_9_1_6 <= 0;
      fsm_cond_9_2_7 <= 0;
      fsm_cond_9_2_8 <= 0;
      fsm_cond_9_3_9 <= 0;
      fsm_cond_9_3_10 <= 0;
      fsm_cond_9_3_11 <= 0;
      fsm_cond_10_1_12 <= 0;
      fsm_cond_10_2_13 <= 0;
      fsm_cond_10_2_14 <= 0;
      fsm_cond_10_3_15 <= 0;
      fsm_cond_10_3_16 <= 0;
      fsm_cond_10_3_17 <= 0;
      fsm_cond_11_1_18 <= 0;
      fsm_cond_11_2_19 <= 0;
      fsm_cond_11_2_20 <= 0;
      fsm_cond_11_3_21 <= 0;
      fsm_cond_11_3_22 <= 0;
      fsm_cond_11_3_23 <= 0;
    end else begin
      count <= count + 1;
      d1_fsm <= fsm;
      d2_fsm <= d1_fsm;
      d3_fsm <= d2_fsm;

      case(d3_fsm)
        fsm_8: begin
          if(fsm_cond_8_3_5) begin
            valid <= 0;
          end 
        end
        fsm_9: begin
          if(fsm_cond_9_3_11) begin
            valid <= 0;
          end 
        end
        fsm_10: begin
          if(fsm_cond_10_3_17) begin
            valid <= 0;
          end 
        end
        fsm_11: begin
          if(fsm_cond_11_3_23) begin
            valid <= 0;
          end 
        end
      endcase

      case(d2_fsm)
        fsm_8: begin
          if(fsm_cond_8_2_2) begin
            valid <= 1;
          end 
          fsm_cond_8_3_5 <= fsm_cond_8_3_4;
        end
        fsm_9: begin
          if(fsm_cond_9_2_8) begin
            valid <= 1;
          end 
          fsm_cond_9_3_11 <= fsm_cond_9_3_10;
        end
        fsm_10: begin
          if(fsm_cond_10_2_14) begin
            valid <= 1;
          end 
          fsm_cond_10_3_17 <= fsm_cond_10_3_16;
        end
        fsm_11: begin
          if(fsm_cond_11_2_20) begin
            valid <= 1;
          end 
          fsm_cond_11_3_23 <= fsm_cond_11_3_22;
        end
      endcase

      case(d1_fsm)
        fsm_4: begin
          valid <= 0;
        end
        fsm_8: begin
          if(fsm_cond_8_1_0) begin
            valid <= 1;
          end 
          fsm_cond_8_2_2 <= fsm_cond_8_2_1;
          fsm_cond_8_3_4 <= fsm_cond_8_3_3;
        end
        fsm_9: begin
          if(fsm_cond_9_1_6) begin
            valid <= 1;
          end 
          fsm_cond_9_2_8 <= fsm_cond_9_2_7;
          fsm_cond_9_3_10 <= fsm_cond_9_3_9;
        end
        fsm_10: begin
          if(fsm_cond_10_1_12) begin
            valid <= 1;
          end 
          fsm_cond_10_2_14 <= fsm_cond_10_2_13;
          fsm_cond_10_3_16 <= fsm_cond_10_3_15;
        end
        fsm_11: begin
          if(fsm_cond_11_1_18) begin
            valid <= 1;
          end 
          fsm_cond_11_2_20 <= fsm_cond_11_2_19;
          fsm_cond_11_3_22 <= fsm_cond_11_3_21;
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
          valid <= 1;
          fsm <= fsm_5;
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
          fsm_cond_8_1_0 <= (count >= 16);
          fsm_cond_8_2_1 <= (count >= 16);
          fsm_cond_8_3_3 <= (count >= 16);
          if(count >= 16) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          fsm_cond_9_1_6 <= (count >= 16);
          fsm_cond_9_2_7 <= (count >= 16);
          fsm_cond_9_3_9 <= (count >= 16);
          if(count >= 16) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          fsm_cond_10_1_12 <= (count >= 16);
          fsm_cond_10_2_13 <= (count >= 16);
          fsm_cond_10_3_15 <= (count >= 16);
          if(count >= 16) begin
            fsm <= fsm_11;
          end 
        end
        fsm_11: begin
          fsm_cond_11_1_18 <= (count >= 16);
          fsm_cond_11_2_19 <= (count >= 16);
          fsm_cond_11_3_21 <= (count >= 16);
          if(count >= 16) begin
            fsm <= fsm_12;
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
