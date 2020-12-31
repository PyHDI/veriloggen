from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_slice

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

  reg [8-1:0] count;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_x_2;
  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;
  localparam th_blink_12 = 12;
  localparam th_blink_13 = 13;
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;
  localparam th_blink_26 = 26;
  localparam th_blink_27 = 27;
  localparam th_blink_28 = 28;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      LED <= 0;
      count <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_x_2 <= 0;
      LED[_th_blink_x_2] <= (0 >> _th_blink_x_2) & 1'd1;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          LED <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          count <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_5;
          end else begin
            th_blink <= th_blink_12;
          end
        end
        th_blink_5: begin
          _th_blink_x_2 <= 0;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          if(_th_blink_x_2 < 8) begin
            th_blink <= th_blink_7;
          end else begin
            th_blink <= th_blink_9;
          end
        end
        th_blink_7: begin
          LED[_th_blink_x_2] <= count[_th_blink_x_2];
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_x_2 <= _th_blink_x_2 + 1;
          th_blink <= th_blink_6;
        end
        th_blink_9: begin
          $display("led =  %d", LED);
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          count <= count + 1;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_4;
        end
        th_blink_12: begin
          LED <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          count <= 0;
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_16;
          end else begin
            th_blink <= th_blink_20;
          end
        end
        th_blink_16: begin
          LED <= count[1:0];
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          $display("led =  %d", LED);
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          count <= count + 1;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_15;
        end
        th_blink_20: begin
          LED <= 0;
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          count <= 0;
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_24;
          end else begin
            th_blink <= th_blink_28;
          end
        end
        th_blink_24: begin
          LED <= { count[6], count[4], count[2], count[0] };
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          $display("led =  %d", LED);
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          count <= count + 1;
          th_blink <= th_blink_27;
        end
        th_blink_27: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_23;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_slice.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
