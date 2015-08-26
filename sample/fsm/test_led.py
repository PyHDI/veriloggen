import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg ready;
  wire valid;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .ready(ready),
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
    ready = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    @(posedge CLK);
    @(posedge CLK);
    @(posedge CLK);
    @(posedge CLK);
    @(posedge CLK);
    @(posedge CLK);
    @(posedge CLK);
    @(posedge CLK);
    ready = 1;
    #1000;
    $finish;
  end

endmodule

module blinkled
  (
   input CLK, 
   input RST, 
   input ready,
   output reg valid
   );

  reg [32-1:0] count;
  reg [32-1:0] fsm;

  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  reg [(32 - 1):0] d1_fsm;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  reg fsm_cond_4_1_0;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  reg fsm_cond_7_1_1;
  reg [(32 - 1):0] d2_fsm;
  reg fsm_cond_7_2_2;
  reg fsm_cond_7_2_3;
  reg [(32 - 1):0] d3_fsm;
  reg fsm_cond_7_3_4;
  reg fsm_cond_7_3_5;
  reg fsm_cond_7_3_6;
  localparam fsm_8 = 8;
  reg fsm_cond_8_1_7;
  reg fsm_cond_8_2_8;
  reg fsm_cond_8_2_9;
  reg fsm_cond_8_3_10;
  reg fsm_cond_8_3_11;
  reg fsm_cond_8_3_12;
  localparam fsm_9 = 9;
  reg fsm_cond_9_1_13;
  reg fsm_cond_9_2_14;
  reg fsm_cond_9_2_15;
  reg fsm_cond_9_3_16;
  reg fsm_cond_9_3_17;
  reg fsm_cond_9_3_18;
  localparam fsm_10 = 10;
  reg fsm_cond_10_1_19;
  reg fsm_cond_10_2_20;
  reg fsm_cond_10_2_21;
  reg fsm_cond_10_3_22;
  reg fsm_cond_10_3_23;
  reg fsm_cond_10_3_24;
  localparam fsm_11 = 11;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      d1_fsm <= fsm_init;
      fsm_cond_4_1_0 <= 0;
      fsm_cond_7_1_1 <= 0;
      d2_fsm <= fsm_init;
      fsm_cond_7_2_2 <= 0;
      fsm_cond_7_2_3 <= 0;
      d3_fsm <= fsm_init;
      fsm_cond_7_3_4 <= 0;
      fsm_cond_7_3_5 <= 0;
      fsm_cond_7_3_6 <= 0;
      fsm_cond_8_1_7 <= 0;
      fsm_cond_8_2_8 <= 0;
      fsm_cond_8_2_9 <= 0;
      fsm_cond_8_3_10 <= 0;
      fsm_cond_8_3_11 <= 0;
      fsm_cond_8_3_12 <= 0;
      fsm_cond_9_1_13 <= 0;
      fsm_cond_9_2_14 <= 0;
      fsm_cond_9_2_15 <= 0;
      fsm_cond_9_3_16 <= 0;
      fsm_cond_9_3_17 <= 0;
      fsm_cond_9_3_18 <= 0;
      fsm_cond_10_1_19 <= 0;
      fsm_cond_10_2_20 <= 0;
      fsm_cond_10_2_21 <= 0;
      fsm_cond_10_3_22 <= 0;
      fsm_cond_10_3_23 <= 0;
      fsm_cond_10_3_24 <= 0;
    end else begin
      count <= (count + 1);
      d1_fsm <= fsm;
      d2_fsm <= d1_fsm;
      d3_fsm <= d2_fsm;
      case(d3_fsm)
        fsm_7: begin
          if(fsm_cond_7_3_6) begin
            valid <= 0;
          end 
        end
        fsm_8: begin
          if(fsm_cond_8_3_12) begin
            valid <= 0;
          end 
        end
        fsm_9: begin
          if(fsm_cond_9_3_18) begin
            valid <= 0;
          end 
        end
        fsm_10: begin
          if(fsm_cond_10_3_24) begin
            valid <= 0;
          end 
        end
      endcase
      case(d2_fsm)
        fsm_7: begin
          if(fsm_cond_7_2_3) begin
            valid <= 1;
          end 
          fsm_cond_7_3_6 <= fsm_cond_7_3_5;
        end
        fsm_8: begin
          if(fsm_cond_8_2_9) begin
            valid <= 1;
          end 
          fsm_cond_8_3_12 <= fsm_cond_8_3_11;
        end
        fsm_9: begin
          if(fsm_cond_9_2_15) begin
            valid <= 1;
          end 
          fsm_cond_9_3_18 <= fsm_cond_9_3_17;
        end
        fsm_10: begin
          if(fsm_cond_10_2_21) begin
            valid <= 1;
          end 
          fsm_cond_10_3_24 <= fsm_cond_10_3_23;
        end
      endcase
      case(d1_fsm)
        fsm_2: begin
          valid <= 0;
        end
        fsm_4: begin
          if(fsm_cond_4_1_0) begin
            valid <= 0;
          end 
        end
        fsm_7: begin
          if(fsm_cond_7_1_1) begin
            valid <= 1;
          end 
          fsm_cond_7_2_3 <= fsm_cond_7_2_2;
          fsm_cond_7_3_5 <= fsm_cond_7_3_4;
        end
        fsm_8: begin
          if(fsm_cond_8_1_7) begin
            valid <= 1;
          end 
          fsm_cond_8_2_9 <= fsm_cond_8_2_8;
          fsm_cond_8_3_11 <= fsm_cond_8_3_10;
        end
        fsm_9: begin
          if(fsm_cond_9_1_13) begin
            valid <= 1;
          end 
          fsm_cond_9_2_15 <= fsm_cond_9_2_14;
          fsm_cond_9_3_17 <= fsm_cond_9_3_16;
        end
        fsm_10: begin
          if(fsm_cond_10_1_19) begin
            valid <= 1;
          end 
          fsm_cond_10_2_21 <= fsm_cond_10_2_20;
          fsm_cond_10_3_23 <= fsm_cond_10_3_22;
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
          valid <= 1;
          fsm <= fsm_3;
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          if((ready == 1)) begin
            valid <= 1;
          end 
          fsm_cond_4_1_0 <= (ready == 1);
          if((ready == 1)) begin
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
          fsm_cond_7_1_1 <= ((count >= 16) && (ready == 1));
          fsm_cond_7_2_2 <= ((count >= 16) && (ready == 1));
          fsm_cond_7_3_4 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          fsm_cond_8_1_7 <= ((count >= 16) && (ready == 1));
          fsm_cond_8_2_8 <= ((count >= 16) && (ready == 1));
          fsm_cond_8_3_10 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          fsm_cond_9_1_13 <= ((count >= 16) && (ready == 1));
          fsm_cond_9_2_14 <= ((count >= 16) && (ready == 1));
          fsm_cond_9_3_16 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          fsm_cond_10_1_19 <= ((count >= 16) && (ready == 1));
          fsm_cond_10_2_20 <= ((count >= 16) && (ready == 1));
          fsm_cond_10_3_22 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_11;
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
