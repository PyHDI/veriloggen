from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_reset

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
  output [8-1:0] LED
);

  assign LED = 0;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_a_1;
  reg signed [32-1:0] _th_blink_b_2;
  reg signed [32-1:0] _th_blink_c_3;
  reg [32-1:0] th_subth;
  localparam th_subth_init = 0;
  reg _th_subth_called;
  reg signed [32-1:0] _th_subth_a_4;
  reg signed [32-1:0] _th_subth_b_5;
  reg signed [32-1:0] _th_subth_c_6;
  reg signed [32-1:0] _th_subth_a_7;
  reg signed [32-1:0] _th_subth_b_8;
  reg signed [32-1:0] _th_subth_c_9;
  reg signed [32-1:0] _th_subth_i_10;
  reg signed [32-1:0] _th_subth_ret_11;
  reg signed [32-1:0] _th_subth_tmp_12_13;
  reg signed [32-1:0] _th_blink_rslt_14;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_a_1 <= 0;
      _th_blink_b_2 <= 0;
      _th_blink_c_3 <= 0;
      _th_blink_rslt_14 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 20;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_a_1 <= 100;
          _th_blink_b_2 <= 200;
          _th_blink_c_3 <= 300;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          $display("# subth run");
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          if(th_subth == 10) begin
            th_blink <= th_blink_5;
          end 
        end
        th_blink_5: begin
          _th_blink_rslt_14 <= _th_subth_tmp_12_13;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          $display("# subth join: rslt=%d", _th_blink_rslt_14);
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_a_1 <= 100;
          _th_blink_b_2 <= 200;
          _th_blink_c_3 <= 300;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          $display("# subth run");
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          if(th_subth == 10) begin
            th_blink <= th_blink_11;
          end 
        end
        th_blink_11: begin
          _th_blink_rslt_14 <= _th_subth_tmp_12_13;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          $display("# subth join: rslt=%d", _th_blink_rslt_14);
          th_blink <= th_blink_13;
        end
      endcase
    end
  end

  localparam th_subth_1 = 1;
  localparam th_subth_2 = 2;
  localparam th_subth_3 = 3;
  localparam th_subth_4 = 4;
  localparam th_subth_5 = 5;
  localparam th_subth_6 = 6;
  localparam th_subth_7 = 7;
  localparam th_subth_8 = 8;
  localparam th_subth_9 = 9;
  localparam th_subth_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      th_subth <= th_subth_init;
      _th_subth_called <= 0;
      _th_subth_a_4 <= 0;
      _th_subth_b_5 <= 0;
      _th_subth_c_6 <= 0;
      _th_subth_a_7 <= 0;
      _th_subth_b_8 <= 0;
      _th_subth_c_9 <= 0;
      _th_subth_i_10 <= 0;
      _th_subth_ret_11 <= 0;
      _th_subth_tmp_12_13 <= 0;
    end else begin
      case(th_subth)
        th_subth_init: begin
          if(th_blink == 2) begin
            _th_subth_called <= 1;
          end 
          if(th_blink == 2) begin
            _th_subth_a_4 <= _th_blink_a_1;
          end 
          if(th_blink == 2) begin
            _th_subth_b_5 <= _th_blink_b_2;
          end 
          if(th_blink == 2) begin
            _th_subth_c_6 <= _th_blink_c_3;
          end 
          if(th_blink == 8) begin
            _th_subth_called <= 1;
          end 
          if(th_blink == 8) begin
            _th_subth_a_4 <= _th_blink_a_1;
          end 
          if(th_blink == 8) begin
            _th_subth_b_5 <= _th_blink_b_2;
          end 
          if(th_blink == 8) begin
            _th_subth_c_6 <= _th_blink_c_3;
          end 
          if(th_blink == 2) begin
            th_subth <= th_subth_1;
          end 
          if(th_blink == 8) begin
            th_subth <= th_subth_1;
          end 
        end
        th_subth_1: begin
          _th_subth_a_7 <= _th_subth_a_4;
          _th_subth_b_8 <= _th_subth_b_5;
          _th_subth_c_9 <= _th_subth_c_6;
          th_subth <= th_subth_2;
        end
        th_subth_2: begin
          $display("# subth start: %d, %d, %d", _th_subth_a_7, _th_subth_b_8, _th_subth_c_9);
          th_subth <= th_subth_3;
        end
        th_subth_3: begin
          _th_subth_i_10 <= 0;
          th_subth <= th_subth_4;
        end
        th_subth_4: begin
          if(_th_subth_i_10 < 10) begin
            th_subth <= th_subth_5;
          end else begin
            th_subth <= th_subth_7;
          end
        end
        th_subth_5: begin
          $display("# subth wait: %d", _th_subth_i_10);
          th_subth <= th_subth_6;
        end
        th_subth_6: begin
          _th_subth_i_10 <= _th_subth_i_10 + 1;
          th_subth <= th_subth_4;
        end
        th_subth_7: begin
          _th_subth_ret_11 <= _th_subth_a_7 + _th_subth_b_8 + _th_subth_c_9;
          th_subth <= th_subth_8;
        end
        th_subth_8: begin
          $display("# subth end: %d", _th_subth_ret_11);
          th_subth <= th_subth_9;
        end
        th_subth_9: begin
          _th_subth_tmp_12_13 <= _th_subth_ret_11;
          th_subth <= th_subth_10;
        end
        th_subth_10: begin
          if(th_blink == 7) begin
            _th_subth_called <= 0;
          end 
          if(th_blink == 7) begin
            th_subth <= th_subth_init;
          end 
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_reset.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
