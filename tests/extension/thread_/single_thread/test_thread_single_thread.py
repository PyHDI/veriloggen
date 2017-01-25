from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_single_thread

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
  reg [32-1:0] _thread_fsm_times_0;
  reg [32-1:0] _thread_fsm_inc_1;
  reg [32-1:0] _thread_fsm_dump_2;
  reg [32-1:0] _thread_fsm_i_3;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      LED <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          _thread_fsm_times_0 <= 10;
          _thread_fsm_inc_1 <= 1;
          _thread_fsm_dump_2 <= 1;
          fsm <= fsm_1;
        end
        fsm_1: begin
          LED <= 0;
          fsm <= fsm_2;
        end
        fsm_2: begin
          _thread_fsm_i_3 <= 0;
          fsm <= fsm_3;
        end
        fsm_3: begin
          if(_thread_fsm_i_3 < _thread_fsm_times_0) begin
            fsm <= fsm_4;
          end else begin
            fsm <= fsm_8;
          end
        end
        fsm_4: begin
          LED <= LED + _thread_fsm_inc_1;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_thread_fsm_dump_2) begin
            fsm <= fsm_6;
          end else begin
            fsm <= fsm_7;
          end
        end
        fsm_6: begin
          $display("led =  %d", LED);
          fsm <= fsm_7;
        end
        fsm_7: begin
          _thread_fsm_i_3 <= _thread_fsm_i_3 + 1;
          fsm <= fsm_3;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_single_thread.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
