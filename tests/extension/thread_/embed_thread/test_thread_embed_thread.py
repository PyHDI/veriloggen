from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_embed_thread

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
  reg signed [32-1:0] __tmp_thread_0_times_1;
  reg signed [32-1:0] __tmp_thread_0_i_2;
  reg signed [32-1:0] __tmp_thread_3_times_4;
  reg signed [32-1:0] __tmp_thread_3_i_5;
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
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  localparam fsm_16 = 16;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      LED <= 0;
      __tmp_thread_0_times_1 <= 0;
      __tmp_thread_0_i_2 <= 0;
      __tmp_thread_3_times_4 <= 0;
      __tmp_thread_3_i_5 <= 0;
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
          __tmp_thread_0_times_1 <= 5;
          fsm <= fsm_3;
        end
        fsm_3: begin
          LED <= 0;
          fsm <= fsm_4;
        end
        fsm_4: begin
          __tmp_thread_0_i_2 <= 0;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(__tmp_thread_0_i_2 < __tmp_thread_0_times_1) begin
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
          __tmp_thread_0_i_2 <= __tmp_thread_0_i_2 + 1;
          fsm <= fsm_5;
        end
        fsm_9: begin
          __tmp_thread_3_times_4 <= 10;
          fsm <= fsm_10;
        end
        fsm_10: begin
          LED <= 0;
          fsm <= fsm_11;
        end
        fsm_11: begin
          __tmp_thread_3_i_5 <= 0;
          fsm <= fsm_12;
        end
        fsm_12: begin
          if(__tmp_thread_3_i_5 < __tmp_thread_3_times_4) begin
            fsm <= fsm_13;
          end else begin
            fsm <= fsm_16;
          end
        end
        fsm_13: begin
          LED <= LED + 1;
          fsm <= fsm_14;
        end
        fsm_14: begin
          $display("led =  %d", LED);
          fsm <= fsm_15;
        end
        fsm_15: begin
          __tmp_thread_3_i_5 <= __tmp_thread_3_i_5 + 1;
          fsm <= fsm_12;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_embed_thread.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
