from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_call_from_different_point

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST)
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
  input RST
);

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg [32-1:0] th_func_a;
  localparam th_func_a_init = 0;
  reg _th_func_a_called;
  reg signed [32-1:0] _th_func_a_a_2;
  reg signed [32-1:0] _th_func_a_b_3;
  reg signed [32-1:0] _th_func_a_a_4;
  reg signed [32-1:0] _th_func_a_b_5;
  reg signed [32-1:0] _th_func_a_i_6;
  reg signed [32-1:0] _th_func_a_tmp_7_8;
  reg signed [32-1:0] _th_blink_j_9;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_j_9 <= 0;
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
            th_blink <= th_blink_14;
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
          _th_blink_j_9 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_j_9 < 10) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_10;
          end
        end
        th_blink_9: begin
          _th_blink_j_9 <= _th_blink_j_9 + 1;
          th_blink <= th_blink_8;
        end
        th_blink_10: begin
          if(th_func_a == 6) begin
            th_blink <= th_blink_11;
          end 
        end
        th_blink_11: begin
          _th_blink_v_10 <= _th_func_a_tmp_7_8;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          $display("func_a: %d", _th_blink_v_10);
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
      endcase
    end
  end

  localparam th_func_a_1 = 1;
  localparam th_func_a_2 = 2;
  localparam th_func_a_3 = 3;
  localparam th_func_a_4 = 4;
  localparam th_func_a_5 = 5;
  localparam th_func_a_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      th_func_a <= th_func_a_init;
      _th_func_a_called <= 0;
      _th_func_a_a_2 <= 0;
      _th_func_a_b_3 <= 0;
      _th_func_a_a_4 <= 0;
      _th_func_a_b_5 <= 0;
      _th_func_a_i_6 <= 0;
      _th_func_a_tmp_7_8 <= 0;
    end else begin
      case(th_func_a)
        th_func_a_init: begin
          if(th_blink == 4) begin
            _th_func_a_called <= 1;
          end 
          if(th_blink == 4) begin
            _th_func_a_a_2 <= _th_blink_i_1 + 200;
          end 
          if(th_blink == 4) begin
            _th_func_a_b_3 <= 2000;
          end 
          if(th_blink == 6) begin
            _th_func_a_called <= 1;
          end 
          if(th_blink == 6) begin
            _th_func_a_a_2 <= _th_blink_i_1 + 100;
          end 
          if(th_blink == 6) begin
            _th_func_a_b_3 <= 1000;
          end 
          if(th_blink == 4) begin
            th_func_a <= th_func_a_1;
          end 
          if(th_blink == 6) begin
            th_func_a <= th_func_a_1;
          end 
        end
        th_func_a_1: begin
          _th_func_a_a_4 <= _th_func_a_a_2;
          _th_func_a_b_5 <= _th_func_a_b_3;
          th_func_a <= th_func_a_2;
        end
        th_func_a_2: begin
          _th_func_a_i_6 <= 0;
          th_func_a <= th_func_a_3;
        end
        th_func_a_3: begin
          if(_th_func_a_i_6 < 4) begin
            th_func_a <= th_func_a_4;
          end else begin
            th_func_a <= th_func_a_5;
          end
        end
        th_func_a_4: begin
          _th_func_a_i_6 <= _th_func_a_i_6 + 1;
          th_func_a <= th_func_a_3;
        end
        th_func_a_5: begin
          _th_func_a_tmp_7_8 <= _th_func_a_a_4 + _th_func_a_b_5;
          th_func_a <= th_func_a_6;
        end
        th_func_a_6: begin
          if(th_blink == 11) begin
            _th_func_a_called <= 0;
          end 
          if(th_blink == 11) begin
            th_func_a <= th_func_a_init;
          end 
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_call_from_different_point.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
