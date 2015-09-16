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
  reg [32-1:0] _d2_fsm;
  reg [32-1:0] _d3_fsm;

  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;

  reg [32-1:0] _d4_fsm;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  localparam fsm_16 = 16;
  localparam fsm_17 = 17;
  localparam fsm_18 = 18;
  localparam fsm_19 = 19;
  localparam fsm_20 = 20;
  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _d2_fsm <= fsm_init;
      _d3_fsm <= fsm_init;
      _d4_fsm <= fsm_init;
      valid <= 0;
    end else begin
      count <= count + 1;
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      _d4_fsm <= _d3_fsm;

      case(_d4_fsm)
        fsm_13: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= 0;
          end 
        end
      endcase

      case(_d3_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= 0;
          end 
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
      endcase

      case(_d2_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= 1;
          end 
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
      endcase

      case(_d1_fsm)
        fsm_4: begin
          if(count >= 16) begin
            valid <= 1;
          end 
        end
        fsm_13: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            valid <= 1;
          end 
        end
        fsm_20: begin
          if(count >= 32) begin
            valid <= 1;
          end 
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
          if(count >= 32) begin
            fsm <= fsm_14;
          end 
        end
        fsm_14: begin
          if(count >= 32) begin
            fsm <= fsm_15;
          end 
        end
        fsm_15: begin
          if(count >= 32) begin
            fsm <= fsm_16;
          end 
        end
        fsm_16: begin
          if(count >= 32) begin
            fsm <= fsm_17;
          end 
        end
        fsm_17: begin
          if(count >= 32) begin
            fsm <= fsm_18;
          end 
        end
        fsm_18: begin
          if(count >= 32) begin
            fsm <= fsm_19;
          end 
        end
        fsm_19: begin
          if(count >= 32) begin
            fsm <= fsm_20;
          end 
        end
        fsm_20: begin
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
