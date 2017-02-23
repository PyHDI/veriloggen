from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_extend

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] LED;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #10000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      LED <= 0;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          LED <= 100;
          fsm <= fsm_1;
        end
        fsm_1: begin
          LED <= 200;
          fsm <= fsm_2;
        end
        fsm_2: begin
          _th_blink_times_0 <= 10;
          fsm <= fsm_3;
        end
        fsm_3: begin
          LED <= 0;
          fsm <= fsm_4;
        end
        fsm_4: begin
          _th_blink_i_1 <= 0;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            fsm <= fsm_6;
          end else begin
            fsm <= fsm_9;
          end
        end
        fsm_6: begin
          LED <= LED + 1;
          fsm <= fsm_7;
        end
        fsm_7: begin
          $display("led =  %d", LED);
          fsm <= fsm_8;
        end
        fsm_8: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          fsm <= fsm_5;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_extend.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
