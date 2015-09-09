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
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
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
  reg [(32 - 1):0] _d1_fsm;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  reg _fsm_cond_4_1_0;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  reg _fsm_cond_7_1_1;
  reg [(32 - 1):0] _d2_fsm;
  reg _fsm_cond_7_2_2;
  reg _fsm_cond_7_2_3;
  reg [(32 - 1):0] _d3_fsm;
  reg _fsm_cond_7_3_4;
  reg _fsm_cond_7_3_5;
  reg _fsm_cond_7_3_6;
  localparam fsm_8 = 8;
  reg _fsm_cond_8_1_7;
  reg _fsm_cond_8_2_8;
  reg _fsm_cond_8_2_9;
  reg _fsm_cond_8_3_10;
  reg _fsm_cond_8_3_11;
  reg _fsm_cond_8_3_12;
  localparam fsm_9 = 9;
  reg _fsm_cond_9_1_13;
  reg _fsm_cond_9_2_14;
  reg _fsm_cond_9_2_15;
  reg _fsm_cond_9_3_16;
  reg _fsm_cond_9_3_17;
  reg _fsm_cond_9_3_18;
  localparam fsm_10 = 10;
  reg _fsm_cond_10_1_19;
  reg _fsm_cond_10_2_20;
  reg _fsm_cond_10_2_21;
  reg _fsm_cond_10_3_22;
  reg _fsm_cond_10_3_23;
  reg _fsm_cond_10_3_24;
  localparam fsm_11 = 11;

  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _fsm_cond_4_1_0 <= 0;
      _fsm_cond_7_1_1 <= 0;
      _d2_fsm <= fsm_init;
      _fsm_cond_7_2_2 <= 0;
      _fsm_cond_7_2_3 <= 0;
      _d3_fsm <= fsm_init;
      _fsm_cond_7_3_4 <= 0;
      _fsm_cond_7_3_5 <= 0;
      _fsm_cond_7_3_6 <= 0;
      _fsm_cond_8_1_7 <= 0;
      _fsm_cond_8_2_8 <= 0;
      _fsm_cond_8_2_9 <= 0;
      _fsm_cond_8_3_10 <= 0;
      _fsm_cond_8_3_11 <= 0;
      _fsm_cond_8_3_12 <= 0;
      _fsm_cond_9_1_13 <= 0;
      _fsm_cond_9_2_14 <= 0;
      _fsm_cond_9_2_15 <= 0;
      _fsm_cond_9_3_16 <= 0;
      _fsm_cond_9_3_17 <= 0;
      _fsm_cond_9_3_18 <= 0;
      _fsm_cond_10_1_19 <= 0;
      _fsm_cond_10_2_20 <= 0;
      _fsm_cond_10_2_21 <= 0;
      _fsm_cond_10_3_22 <= 0;
      _fsm_cond_10_3_23 <= 0;
      _fsm_cond_10_3_24 <= 0;
    end else begin
      count <= (count + 1);
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      case(_d3_fsm)
        fsm_7: begin
          if(_fsm_cond_7_3_6) begin
            valid <= 0;
          end 
        end
        fsm_8: begin
          if(_fsm_cond_8_3_12) begin
            valid <= 0;
          end 
        end
        fsm_9: begin
          if(_fsm_cond_9_3_18) begin
            valid <= 0;
          end 
        end
        fsm_10: begin
          if(_fsm_cond_10_3_24) begin
            valid <= 0;
          end 
        end
      endcase
      case(_d2_fsm)
        fsm_7: begin
          if(_fsm_cond_7_2_3) begin
            valid <= 1;
          end 
          _fsm_cond_7_3_6 <= _fsm_cond_7_3_5;
        end
        fsm_8: begin
          if(_fsm_cond_8_2_9) begin
            valid <= 1;
          end 
          _fsm_cond_8_3_12 <= _fsm_cond_8_3_11;
        end
        fsm_9: begin
          if(_fsm_cond_9_2_15) begin
            valid <= 1;
          end 
          _fsm_cond_9_3_18 <= _fsm_cond_9_3_17;
        end
        fsm_10: begin
          if(_fsm_cond_10_2_21) begin
            valid <= 1;
          end 
          _fsm_cond_10_3_24 <= _fsm_cond_10_3_23;
        end
      endcase
      case(_d1_fsm)
        fsm_2: begin
          valid <= 0;
        end
        fsm_4: begin
          if(_fsm_cond_4_1_0) begin
            valid <= 0;
          end 
        end
        fsm_7: begin
          if(_fsm_cond_7_1_1) begin
            valid <= 1;
          end 
          _fsm_cond_7_2_3 <= _fsm_cond_7_2_2;
          _fsm_cond_7_3_5 <= _fsm_cond_7_3_4;
        end
        fsm_8: begin
          if(_fsm_cond_8_1_7) begin
            valid <= 1;
          end 
          _fsm_cond_8_2_9 <= _fsm_cond_8_2_8;
          _fsm_cond_8_3_11 <= _fsm_cond_8_3_10;
        end
        fsm_9: begin
          if(_fsm_cond_9_1_13) begin
            valid <= 1;
          end 
          _fsm_cond_9_2_15 <= _fsm_cond_9_2_14;
          _fsm_cond_9_3_17 <= _fsm_cond_9_3_16;
        end
        fsm_10: begin
          if(_fsm_cond_10_1_19) begin
            valid <= 1;
          end 
          _fsm_cond_10_2_21 <= _fsm_cond_10_2_20;
          _fsm_cond_10_3_23 <= _fsm_cond_10_3_22;
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
          _fsm_cond_4_1_0 <= (ready == 1);
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
          _fsm_cond_7_1_1 <= ((count >= 16) && (ready == 1));
          _fsm_cond_7_2_2 <= ((count >= 16) && (ready == 1));
          _fsm_cond_7_3_4 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          _fsm_cond_8_1_7 <= ((count >= 16) && (ready == 1));
          _fsm_cond_8_2_8 <= ((count >= 16) && (ready == 1));
          _fsm_cond_8_3_10 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          _fsm_cond_9_1_13 <= ((count >= 16) && (ready == 1));
          _fsm_cond_9_2_14 <= ((count >= 16) && (ready == 1));
          _fsm_cond_9_3_16 <= ((count >= 16) && (ready == 1));
          if(((count >= 16) && (ready == 1))) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          _fsm_cond_10_1_19 <= ((count >= 16) && (ready == 1));
          _fsm_cond_10_2_20 <= ((count >= 16) && (ready == 1));
          _fsm_cond_10_3_22 <= ((count >= 16) && (ready == 1));
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
