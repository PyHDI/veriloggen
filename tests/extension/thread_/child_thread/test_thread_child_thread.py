from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_child_thread

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
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _thread_fsm_times_0;
  reg [32-1:0] _thread_fsm_inc_1;
  reg [32-1:0] fsm_child_countup_2;
  localparam fsm_child_countup_2_init = 0;
  reg [32-1:0] _thread_fsm_child_countup_2_times_3;
  reg [32-1:0] _thread_fsm_child_countup_2_inc_4;
  reg [32-1:0] _thread_fsm_child_countup_2_i_5;
  reg [32-1:0] _thread_fsm_th_6;
  reg [32-1:0] _thread_fsm_i_7;
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
      fsm <= fsm_init;
      _thread_fsm_times_0 <= 0;
      _thread_fsm_inc_1 <= 0;
      LED <= 0;
      _thread_fsm_i_7 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          _thread_fsm_times_0 <= 10;
          _thread_fsm_inc_1 <= 1;
          fsm <= fsm_1;
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          $display("# child thread start");
          fsm <= fsm_3;
        end
        fsm_3: begin
          LED <= 0;
          fsm <= fsm_4;
        end
        fsm_4: begin
          _thread_fsm_i_7 <= 0;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_thread_fsm_i_7 < _thread_fsm_times_0) begin
            fsm <= fsm_6;
          end else begin
            fsm <= fsm_9;
          end
        end
        fsm_6: begin
          LED <= LED + _thread_fsm_inc_1;
          fsm <= fsm_7;
        end
        fsm_7: begin
          $display("  led = %d", LED);
          fsm <= fsm_8;
        end
        fsm_8: begin
          _thread_fsm_i_7 <= _thread_fsm_i_7 + 1;
          fsm <= fsm_5;
        end
        fsm_9: begin
          if(fsm_child_countup_2 == 8) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          $display("# child thread done");
          fsm <= fsm_11;
        end
      endcase
    end
  end

  localparam fsm_child_countup_2_1 = 1;
  localparam fsm_child_countup_2_2 = 2;
  localparam fsm_child_countup_2_3 = 3;
  localparam fsm_child_countup_2_4 = 4;
  localparam fsm_child_countup_2_5 = 5;
  localparam fsm_child_countup_2_6 = 6;
  localparam fsm_child_countup_2_7 = 7;
  localparam fsm_child_countup_2_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      fsm_child_countup_2 <= fsm_child_countup_2_init;
      _thread_fsm_child_countup_2_times_3 <= 0;
      _thread_fsm_child_countup_2_inc_4 <= 0;
      count <= 0;
      _thread_fsm_child_countup_2_i_5 <= 0;
    end else begin
      case(fsm_child_countup_2)
        fsm_child_countup_2_init: begin
          if(fsm == 1) begin
            fsm_child_countup_2 <= fsm_child_countup_2_1;
          end 
        end
        fsm_child_countup_2_1: begin
          _thread_fsm_child_countup_2_times_3 <= _thread_fsm_times_0 * 2;
          _thread_fsm_child_countup_2_inc_4 <= 10;
          fsm_child_countup_2 <= fsm_child_countup_2_2;
        end
        fsm_child_countup_2_2: begin
          count <= 0;
          fsm_child_countup_2 <= fsm_child_countup_2_3;
        end
        fsm_child_countup_2_3: begin
          _thread_fsm_child_countup_2_i_5 <= 0;
          fsm_child_countup_2 <= fsm_child_countup_2_4;
        end
        fsm_child_countup_2_4: begin
          if(_thread_fsm_child_countup_2_i_5 < _thread_fsm_child_countup_2_times_3) begin
            fsm_child_countup_2 <= fsm_child_countup_2_5;
          end else begin
            fsm_child_countup_2 <= fsm_child_countup_2_8;
          end
        end
        fsm_child_countup_2_5: begin
          count <= count + _thread_fsm_child_countup_2_inc_4;
          fsm_child_countup_2 <= fsm_child_countup_2_6;
        end
        fsm_child_countup_2_6: begin
          $display("count = %d", count);
          fsm_child_countup_2 <= fsm_child_countup_2_7;
        end
        fsm_child_countup_2_7: begin
          _thread_fsm_child_countup_2_i_5 <= _thread_fsm_child_countup_2_i_5 + 1;
          fsm_child_countup_2 <= fsm_child_countup_2_4;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_child_thread.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
