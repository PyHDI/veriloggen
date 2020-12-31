from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_select_thread

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
  reg [32-1:0] th_func_a;
  localparam th_func_a_init = 0;
  reg _th_func_a_called;
  reg signed [32-1:0] _th_func_a_v_2;
  reg signed [32-1:0] _th_func_a_v_3;
  reg signed [32-1:0] _th_func_a_tmp_4_5;
  reg [32-1:0] th_func_b;
  localparam th_func_b_init = 0;
  reg _th_func_b_called;
  reg signed [32-1:0] _th_func_b_v_6;
  reg signed [32-1:0] _th_func_b_v_7;
  reg signed [32-1:0] _th_func_b_tmp_8_9;
  reg signed [32-1:0] _th_blink_v_10;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_v_10 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 20;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_16;
          end
        end
        th_blink_3: begin
          if((_th_blink_i_1 & 1) == 0) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_6;
          end
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          th_blink <= th_blink_7;
        end
        th_blink_6: begin
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          if(_th_func_a_called) begin
            th_blink <= th_blink_8;
          end else begin
            th_blink <= th_blink_11;
          end
        end
        th_blink_8: begin
          if(th_func_a == 3) begin
            th_blink <= th_blink_9;
          end 
        end
        th_blink_9: begin
          _th_blink_v_10 <= _th_func_a_tmp_4_5;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          $display("func_a: %d", _th_blink_v_10);
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          if(_th_func_b_called) begin
            th_blink <= th_blink_12;
          end else begin
            th_blink <= th_blink_15;
          end
        end
        th_blink_12: begin
          if(th_func_b == 3) begin
            th_blink <= th_blink_13;
          end 
        end
        th_blink_13: begin
          _th_blink_v_10 <= _th_func_b_tmp_8_9;
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          $display("func_b: %d", _th_blink_v_10);
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
      endcase
    end
  end

  localparam th_func_a_1 = 1;
  localparam th_func_a_2 = 2;
  localparam th_func_a_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      th_func_a <= th_func_a_init;
      _th_func_a_called <= 0;
      _th_func_a_v_2 <= 0;
      _th_func_a_v_3 <= 0;
      _th_func_a_tmp_4_5 <= 0;
    end else begin
      case(th_func_a)
        th_func_a_init: begin
          if(th_blink == 4) begin
            _th_func_a_called <= 1;
          end 
          if(th_blink == 4) begin
            _th_func_a_v_2 <= _th_blink_i_1;
          end 
          if(th_blink == 4) begin
            th_func_a <= th_func_a_1;
          end 
        end
        th_func_a_1: begin
          _th_func_a_v_3 <= _th_func_a_v_2;
          th_func_a <= th_func_a_2;
        end
        th_func_a_2: begin
          _th_func_a_tmp_4_5 <= _th_func_a_v_3 + 100;
          th_func_a <= th_func_a_3;
        end
        th_func_a_3: begin
          if(th_blink == 9) begin
            _th_func_a_called <= 0;
          end 
          if(th_blink == 9) begin
            th_func_a <= th_func_a_init;
          end 
        end
      endcase
    end
  end

  localparam th_func_b_1 = 1;
  localparam th_func_b_2 = 2;
  localparam th_func_b_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      th_func_b <= th_func_b_init;
      _th_func_b_called <= 0;
      _th_func_b_v_6 <= 0;
      _th_func_b_v_7 <= 0;
      _th_func_b_tmp_8_9 <= 0;
    end else begin
      case(th_func_b)
        th_func_b_init: begin
          if(th_blink == 6) begin
            _th_func_b_called <= 1;
          end 
          if(th_blink == 6) begin
            _th_func_b_v_6 <= _th_blink_i_1;
          end 
          if(th_blink == 6) begin
            th_func_b <= th_func_b_1;
          end 
        end
        th_func_b_1: begin
          _th_func_b_v_7 <= _th_func_b_v_6;
          th_func_b <= th_func_b_2;
        end
        th_func_b_2: begin
          _th_func_b_tmp_8_9 <= _th_func_b_v_7 + 200;
          th_func_b <= th_func_b_3;
        end
        th_func_b_3: begin
          if(th_blink == 13) begin
            _th_func_b_called <= 0;
          end 
          if(th_blink == 13) begin
            th_func_b <= th_func_b_init;
          end 
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_select_thread.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
