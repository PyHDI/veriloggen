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
  reg [32-1:0] th_countup;
  localparam th_countup_init = 0;
  reg [32-1:0] _th_countup_times_0;
  reg [32-1:0] _th_countup_i_1;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg [32-1:0] _th_blink_times_2;
  reg [32-1:0] _th_blink_i_3;
  localparam th_countup_1 = 1;
  localparam th_countup_2 = 2;
  localparam th_countup_3 = 3;
  localparam th_countup_4 = 4;
  localparam th_countup_5 = 5;
  localparam th_countup_6 = 6;
  localparam th_countup_7 = 7;
  localparam th_countup_8 = 8;
  localparam th_countup_9 = 9;
  localparam th_countup_10 = 10;
  localparam th_countup_11 = 11;

  always @(posedge CLK) begin
    if(RST) begin
      th_countup <= th_countup_init;
      _th_countup_times_0 <= 0;
      count <= 0;
      _th_countup_i_1 <= 0;
    end else begin
      case(th_countup)
        th_countup_init: begin
          _th_countup_times_0 <= 20;
          th_countup <= th_countup_1;
        end
        th_countup_1: begin
          count <= 0;
          th_countup <= th_countup_2;
        end
        th_countup_2: begin
          _th_countup_i_1 <= 0;
          th_countup <= th_countup_3;
        end
        th_countup_3: begin
          if(_th_countup_i_1 < _th_countup_times_0) begin
            th_countup <= th_countup_4;
          end else begin
            th_countup <= th_countup_9;
          end
        end
        th_countup_4: begin
          count <= count + 1;
          th_countup <= th_countup_5;
        end
        th_countup_5: begin
          $display("count = %d", count);
          th_countup <= th_countup_6;
        end
        th_countup_6: begin
          if(count == (_th_countup_times_0 >>> 1)) begin
            th_countup <= th_countup_7;
          end else begin
            th_countup <= th_countup_8;
          end
        end
        th_countup_7: begin
          $display("child thread start");
          th_countup <= th_countup_8;
        end
        th_countup_8: begin
          _th_countup_i_1 <= _th_countup_i_1 + 1;
          th_countup <= th_countup_3;
        end
        th_countup_9: begin
          if(th_blink == 8) begin
            th_countup <= th_countup_10;
          end 
        end
        th_countup_10: begin
          $display("child thread finish");
          th_countup <= th_countup_11;
        end
      endcase
    end
  end

  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_2 <= 0;
      LED <= 0;
      _th_blink_i_3 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          if(th_countup == 7) begin
            th_blink <= th_blink_1;
          end 
        end
        th_blink_1: begin
          _th_blink_times_2 <= _th_countup_times_0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          LED <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _th_blink_i_3 <= 0;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          if(_th_blink_i_3 < _th_blink_times_2) begin
            th_blink <= th_blink_5;
          end else begin
            th_blink <= th_blink_8;
          end
        end
        th_blink_5: begin
          LED <= LED + 1;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          $display("  led = %d", LED);
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_i_3 <= _th_blink_i_3 + 1;
          th_blink <= th_blink_4;
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
