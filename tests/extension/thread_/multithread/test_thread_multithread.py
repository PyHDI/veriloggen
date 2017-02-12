from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_multithread

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

  reg [8-1:0] count;
  reg [32-1:0] fsm_blink;
  localparam fsm_blink_init = 0;
  reg [32-1:0] _thread_fsm_blink_times_0;
  reg [32-1:0] _thread_fsm_blink_inc_1;
  reg [32-1:0] _thread_fsm_blink_i_2;
  reg [32-1:0] fsm_countup;
  localparam fsm_countup_init = 0;
  reg [32-1:0] _thread_fsm_countup_times_3;
  reg [32-1:0] _thread_fsm_countup_inc_4;
  reg [32-1:0] _thread_fsm_countup_i_5;
  localparam fsm_blink_1 = 1;
  localparam fsm_blink_2 = 2;
  localparam fsm_blink_3 = 3;
  localparam fsm_blink_4 = 4;
  localparam fsm_blink_5 = 5;
  localparam fsm_blink_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      fsm_blink <= fsm_blink_init;
      _thread_fsm_blink_times_0 <= 0;
      _thread_fsm_blink_inc_1 <= 0;
      LED <= 0;
      _thread_fsm_blink_i_2 <= 0;
    end else begin
      case(fsm_blink)
        fsm_blink_init: begin
          _thread_fsm_blink_times_0 <= 10;
          _thread_fsm_blink_inc_1 <= 1;
          fsm_blink <= fsm_blink_1;
        end
        fsm_blink_1: begin
          LED <= 0;
          fsm_blink <= fsm_blink_2;
        end
        fsm_blink_2: begin
          _thread_fsm_blink_i_2 <= 0;
          fsm_blink <= fsm_blink_3;
        end
        fsm_blink_3: begin
          if(_thread_fsm_blink_i_2 < _thread_fsm_blink_times_0) begin
            fsm_blink <= fsm_blink_4;
          end else begin
            fsm_blink <= fsm_blink_6;
          end
        end
        fsm_blink_4: begin
          LED <= LED + _thread_fsm_blink_inc_1;
          fsm_blink <= fsm_blink_5;
        end
        fsm_blink_5: begin
          _thread_fsm_blink_i_2 <= _thread_fsm_blink_i_2 + 1;
          fsm_blink <= fsm_blink_3;
        end
      endcase
    end
  end

  localparam fsm_countup_1 = 1;
  localparam fsm_countup_2 = 2;
  localparam fsm_countup_3 = 3;
  localparam fsm_countup_4 = 4;
  localparam fsm_countup_5 = 5;
  localparam fsm_countup_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      fsm_countup <= fsm_countup_init;
      _thread_fsm_countup_times_3 <= 0;
      _thread_fsm_countup_inc_4 <= 0;
      count <= 0;
      _thread_fsm_countup_i_5 <= 0;
    end else begin
      case(fsm_countup)
        fsm_countup_init: begin
          _thread_fsm_countup_times_3 <= 10;
          _thread_fsm_countup_inc_4 <= 1;
          fsm_countup <= fsm_countup_1;
        end
        fsm_countup_1: begin
          count <= 0;
          fsm_countup <= fsm_countup_2;
        end
        fsm_countup_2: begin
          _thread_fsm_countup_i_5 <= 0;
          fsm_countup <= fsm_countup_3;
        end
        fsm_countup_3: begin
          if(_thread_fsm_countup_i_5 < _thread_fsm_countup_times_3) begin
            fsm_countup <= fsm_countup_4;
          end else begin
            fsm_countup <= fsm_countup_6;
          end
        end
        fsm_countup_4: begin
          count <= count + _thread_fsm_countup_inc_4;
          fsm_countup <= fsm_countup_5;
        end
        fsm_countup_5: begin
          _thread_fsm_countup_i_5 <= _thread_fsm_countup_i_5 + 1;
          fsm_countup <= fsm_countup_3;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_multithread.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
