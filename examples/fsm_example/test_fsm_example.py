from __future__ import absolute_import
from __future__ import print_function
import fsm_example

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
      #5 CLK = !CLK;
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
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  reg _fsm_cond_4_1_1;
  reg _fsm_cond_7_2_1;
  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_7_3_1;
  reg _fsm_cond_7_3_2;
  reg [32-1:0] _d3_fsm;
  reg _fsm_cond_7_4_1;
  reg _fsm_cond_7_4_2;
  reg _fsm_cond_7_4_3;
  reg _fsm_cond_8_5_1;
  reg _fsm_cond_8_6_1;
  reg _fsm_cond_8_6_2;
  reg _fsm_cond_8_7_1;
  reg _fsm_cond_8_7_2;
  reg _fsm_cond_8_7_3;
  reg _fsm_cond_9_8_1;
  reg _fsm_cond_9_9_1;
  reg _fsm_cond_9_9_2;
  reg _fsm_cond_9_10_1;
  reg _fsm_cond_9_10_2;
  reg _fsm_cond_9_10_3;
  reg _fsm_cond_10_11_1;
  reg _fsm_cond_10_12_1;
  reg _fsm_cond_10_12_2;
  reg _fsm_cond_10_13_1;
  reg _fsm_cond_10_13_2;
  reg _fsm_cond_10_13_3;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _d2_fsm <= fsm_init;
      _d3_fsm <= fsm_init;
      valid <= 0;
      _fsm_cond_2_0_1 <= 0;
      _fsm_cond_4_1_1 <= 0;
      _fsm_cond_7_2_1 <= 0;
      _fsm_cond_7_3_1 <= 0;
      _fsm_cond_7_3_2 <= 0;
      _fsm_cond_7_4_1 <= 0;
      _fsm_cond_7_4_2 <= 0;
      _fsm_cond_7_4_3 <= 0;
      _fsm_cond_8_5_1 <= 0;
      _fsm_cond_8_6_1 <= 0;
      _fsm_cond_8_6_2 <= 0;
      _fsm_cond_8_7_1 <= 0;
      _fsm_cond_8_7_2 <= 0;
      _fsm_cond_8_7_3 <= 0;
      _fsm_cond_9_8_1 <= 0;
      _fsm_cond_9_9_1 <= 0;
      _fsm_cond_9_9_2 <= 0;
      _fsm_cond_9_10_1 <= 0;
      _fsm_cond_9_10_2 <= 0;
      _fsm_cond_9_10_3 <= 0;
      _fsm_cond_10_11_1 <= 0;
      _fsm_cond_10_12_1 <= 0;
      _fsm_cond_10_12_2 <= 0;
      _fsm_cond_10_13_1 <= 0;
      _fsm_cond_10_13_2 <= 0;
      _fsm_cond_10_13_3 <= 0;
    end else begin
      count <= count + 1;
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      case(_d3_fsm)
        fsm_7: begin
          if(_fsm_cond_7_4_3) begin
            valid <= 0;
          end 
        end
        fsm_8: begin
          if(_fsm_cond_8_7_3) begin
            valid <= 0;
          end 
        end
        fsm_9: begin
          if(_fsm_cond_9_10_3) begin
            valid <= 0;
          end 
        end
        fsm_10: begin
          if(_fsm_cond_10_13_3) begin
            valid <= 0;
          end 
        end
      endcase
      case(_d2_fsm)
        fsm_7: begin
          if(_fsm_cond_7_3_2) begin
            valid <= 1;
          end 
          _fsm_cond_7_4_3 <= _fsm_cond_7_4_2;
        end
        fsm_8: begin
          if(_fsm_cond_8_6_2) begin
            valid <= 1;
          end 
          _fsm_cond_8_7_3 <= _fsm_cond_8_7_2;
        end
        fsm_9: begin
          if(_fsm_cond_9_9_2) begin
            valid <= 1;
          end 
          _fsm_cond_9_10_3 <= _fsm_cond_9_10_2;
        end
        fsm_10: begin
          if(_fsm_cond_10_12_2) begin
            valid <= 1;
          end 
          _fsm_cond_10_13_3 <= _fsm_cond_10_13_2;
        end
      endcase
      case(_d1_fsm)
        fsm_2: begin
          if(_fsm_cond_2_0_1) begin
            valid <= 0;
          end 
        end
        fsm_4: begin
          if(_fsm_cond_4_1_1) begin
            valid <= 0;
          end 
        end
        fsm_7: begin
          if(_fsm_cond_7_2_1) begin
            valid <= 1;
          end 
          _fsm_cond_7_3_2 <= _fsm_cond_7_3_1;
          _fsm_cond_7_4_2 <= _fsm_cond_7_4_1;
        end
        fsm_8: begin
          if(_fsm_cond_8_5_1) begin
            valid <= 1;
          end 
          _fsm_cond_8_6_2 <= _fsm_cond_8_6_1;
          _fsm_cond_8_7_2 <= _fsm_cond_8_7_1;
        end
        fsm_9: begin
          if(_fsm_cond_9_8_1) begin
            valid <= 1;
          end 
          _fsm_cond_9_9_2 <= _fsm_cond_9_9_1;
          _fsm_cond_9_10_2 <= _fsm_cond_9_10_1;
        end
        fsm_10: begin
          if(_fsm_cond_10_11_1) begin
            valid <= 1;
          end 
          _fsm_cond_10_12_2 <= _fsm_cond_10_12_1;
          _fsm_cond_10_13_2 <= _fsm_cond_10_13_1;
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
          _fsm_cond_2_0_1 <= 1;
          fsm <= fsm_3;
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          if(ready == 1) begin
            valid <= 1;
          end 
          _fsm_cond_4_1_1 <= ready == 1;
          if(ready == 1) begin
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
          _fsm_cond_7_2_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_7_3_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_7_4_1 <= (count >= 16) && (ready == 1);
          if((count >= 16) && (ready == 1)) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          _fsm_cond_8_5_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_8_6_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_8_7_1 <= (count >= 16) && (ready == 1);
          if((count >= 16) && (ready == 1)) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          _fsm_cond_9_8_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_9_9_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_9_10_1 <= (count >= 16) && (ready == 1);
          if((count >= 16) && (ready == 1)) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          _fsm_cond_10_11_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_10_12_1 <= (count >= 16) && (ready == 1);
          _fsm_cond_10_13_1 <= (count >= 16) && (ready == 1);
          if((count >= 16) && (ready == 1)) begin
            fsm <= fsm_11;
          end 
        end
      endcase
    end
  end


endmodule
"""

def test():
    test_module = fsm_example.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
