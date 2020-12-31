from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_thread_pool

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

  reg [4-1:0] _th_myfunc_start;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_tid_1;
  reg [32-1:0] th_myfunc_0;
  localparam th_myfunc_0_init = 0;
  reg [32-1:0] th_myfunc_1;
  localparam th_myfunc_1_init = 0;
  reg [32-1:0] th_myfunc_2;
  localparam th_myfunc_2_init = 0;
  reg [32-1:0] th_myfunc_3;
  localparam th_myfunc_3_init = 0;
  reg _th_myfunc_0_called;
  reg signed [32-1:0] _th_myfunc_0_tid_2;
  reg signed [32-1:0] _th_myfunc_0_tid_3;
  reg signed [32-1:0] _th_myfunc_0_i_4;
  reg signed [32-1:0] _th_myfunc_0_tmp_5_6;
  reg _th_myfunc_1_called;
  reg signed [32-1:0] _th_myfunc_1_tid_7;
  reg signed [32-1:0] _th_myfunc_1_tid_8;
  reg signed [32-1:0] _th_myfunc_1_i_9;
  reg signed [32-1:0] _th_myfunc_1_tmp_10_11;
  reg _th_myfunc_2_called;
  reg signed [32-1:0] _th_myfunc_2_tid_12;
  reg signed [32-1:0] _th_myfunc_2_tid_13;
  reg signed [32-1:0] _th_myfunc_2_i_14;
  reg signed [32-1:0] _th_myfunc_2_tmp_15_16;
  reg _th_myfunc_3_called;
  reg signed [32-1:0] _th_myfunc_3_tid_17;
  reg signed [32-1:0] _th_myfunc_3_tid_18;
  reg signed [32-1:0] _th_myfunc_3_i_19;
  reg signed [32-1:0] _th_myfunc_3_tmp_20_21;
  reg signed [32-1:0] _th_blink_sum_22;
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
      _th_blink_tid_1 <= 0;
      _th_myfunc_start[_th_blink_tid_1] <= (0 >> _th_blink_tid_1) & 1'd1;
      _th_blink_sum_22 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 20;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_tid_1 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          if(_th_blink_tid_1 < 4) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_7;
          end
        end
        th_blink_3: begin
          _th_myfunc_start[_th_blink_tid_1] <= 1;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_myfunc_start[_th_blink_tid_1] <= 0;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_tid_1 <= _th_blink_tid_1 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_7: begin
          _th_blink_sum_22 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_tid_1 <= 0;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          if(_th_blink_tid_1 < 4) begin
            th_blink <= th_blink_10;
          end else begin
            th_blink <= th_blink_13;
          end
        end
        th_blink_10: begin
          if((_th_blink_tid_1 == 0)? th_myfunc_0 == 7 : 
          (_th_blink_tid_1 == 1)? th_myfunc_1 == 7 : 
          (_th_blink_tid_1 == 2)? th_myfunc_2 == 7 : 
          (_th_blink_tid_1 == 3)? th_myfunc_3 == 7 : 0) begin
            th_blink <= th_blink_11;
          end 
        end
        th_blink_11: begin
          _th_blink_sum_22 <= _th_blink_sum_22 + ((_th_blink_tid_1 == 0)? _th_myfunc_0_tmp_5_6 : 
                              (_th_blink_tid_1 == 1)? _th_myfunc_1_tmp_10_11 : 
                              (_th_blink_tid_1 == 2)? _th_myfunc_2_tmp_15_16 : 
                              (_th_blink_tid_1 == 3)? _th_myfunc_3_tmp_20_21 : 'hx);
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          _th_blink_tid_1 <= _th_blink_tid_1 + 1;
          th_blink <= th_blink_9;
        end
        th_blink_13: begin
          $display("sum = %d", _th_blink_sum_22);
          th_blink <= th_blink_14;
        end
      endcase
    end
  end

  localparam th_myfunc_0_1 = 1;
  localparam th_myfunc_0_2 = 2;
  localparam th_myfunc_0_3 = 3;
  localparam th_myfunc_0_4 = 4;
  localparam th_myfunc_0_5 = 5;
  localparam th_myfunc_0_6 = 6;
  localparam th_myfunc_0_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_0 <= th_myfunc_0_init;
      _th_myfunc_0_called <= 0;
      _th_myfunc_0_tid_2 <= 0;
      _th_myfunc_0_tid_3 <= 0;
      _th_myfunc_0_i_4 <= 0;
      _th_myfunc_0_tmp_5_6 <= 0;
    end else begin
      case(th_myfunc_0)
        th_myfunc_0_init: begin
          if(_th_myfunc_start[0] && (th_blink == 4)) begin
            _th_myfunc_0_called <= 1;
          end 
          if(_th_myfunc_start[0] && (th_blink == 4)) begin
            _th_myfunc_0_tid_2 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_start[0]) begin
            th_myfunc_0 <= th_myfunc_0_1;
          end 
        end
        th_myfunc_0_1: begin
          _th_myfunc_0_tid_3 <= _th_myfunc_0_tid_2;
          th_myfunc_0 <= th_myfunc_0_2;
        end
        th_myfunc_0_2: begin
          $display("tid = %d", _th_myfunc_0_tid_3);
          th_myfunc_0 <= th_myfunc_0_3;
        end
        th_myfunc_0_3: begin
          _th_myfunc_0_i_4 <= 0;
          th_myfunc_0 <= th_myfunc_0_4;
        end
        th_myfunc_0_4: begin
          if(_th_myfunc_0_i_4 < 30 - _th_myfunc_0_tid_3) begin
            th_myfunc_0 <= th_myfunc_0_5;
          end else begin
            th_myfunc_0 <= th_myfunc_0_6;
          end
        end
        th_myfunc_0_5: begin
          _th_myfunc_0_i_4 <= _th_myfunc_0_i_4 + 1;
          th_myfunc_0 <= th_myfunc_0_4;
        end
        th_myfunc_0_6: begin
          _th_myfunc_0_tmp_5_6 <= _th_myfunc_0_tid_3 + 100;
          th_myfunc_0 <= th_myfunc_0_7;
        end
      endcase
    end
  end

  localparam th_myfunc_1_1 = 1;
  localparam th_myfunc_1_2 = 2;
  localparam th_myfunc_1_3 = 3;
  localparam th_myfunc_1_4 = 4;
  localparam th_myfunc_1_5 = 5;
  localparam th_myfunc_1_6 = 6;
  localparam th_myfunc_1_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_1 <= th_myfunc_1_init;
      _th_myfunc_1_called <= 0;
      _th_myfunc_1_tid_7 <= 0;
      _th_myfunc_1_tid_8 <= 0;
      _th_myfunc_1_i_9 <= 0;
      _th_myfunc_1_tmp_10_11 <= 0;
    end else begin
      case(th_myfunc_1)
        th_myfunc_1_init: begin
          if(_th_myfunc_start[1] && (th_blink == 4)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(_th_myfunc_start[1] && (th_blink == 4)) begin
            _th_myfunc_1_tid_7 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_8 <= _th_myfunc_1_tid_7;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          $display("tid = %d", _th_myfunc_1_tid_8);
          th_myfunc_1 <= th_myfunc_1_3;
        end
        th_myfunc_1_3: begin
          _th_myfunc_1_i_9 <= 0;
          th_myfunc_1 <= th_myfunc_1_4;
        end
        th_myfunc_1_4: begin
          if(_th_myfunc_1_i_9 < 30 - _th_myfunc_1_tid_8) begin
            th_myfunc_1 <= th_myfunc_1_5;
          end else begin
            th_myfunc_1 <= th_myfunc_1_6;
          end
        end
        th_myfunc_1_5: begin
          _th_myfunc_1_i_9 <= _th_myfunc_1_i_9 + 1;
          th_myfunc_1 <= th_myfunc_1_4;
        end
        th_myfunc_1_6: begin
          _th_myfunc_1_tmp_10_11 <= _th_myfunc_1_tid_8 + 100;
          th_myfunc_1 <= th_myfunc_1_7;
        end
      endcase
    end
  end

  localparam th_myfunc_2_1 = 1;
  localparam th_myfunc_2_2 = 2;
  localparam th_myfunc_2_3 = 3;
  localparam th_myfunc_2_4 = 4;
  localparam th_myfunc_2_5 = 5;
  localparam th_myfunc_2_6 = 6;
  localparam th_myfunc_2_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_2 <= th_myfunc_2_init;
      _th_myfunc_2_called <= 0;
      _th_myfunc_2_tid_12 <= 0;
      _th_myfunc_2_tid_13 <= 0;
      _th_myfunc_2_i_14 <= 0;
      _th_myfunc_2_tmp_15_16 <= 0;
    end else begin
      case(th_myfunc_2)
        th_myfunc_2_init: begin
          if(_th_myfunc_start[2] && (th_blink == 4)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(_th_myfunc_start[2] && (th_blink == 4)) begin
            _th_myfunc_2_tid_12 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_13 <= _th_myfunc_2_tid_12;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          $display("tid = %d", _th_myfunc_2_tid_13);
          th_myfunc_2 <= th_myfunc_2_3;
        end
        th_myfunc_2_3: begin
          _th_myfunc_2_i_14 <= 0;
          th_myfunc_2 <= th_myfunc_2_4;
        end
        th_myfunc_2_4: begin
          if(_th_myfunc_2_i_14 < 30 - _th_myfunc_2_tid_13) begin
            th_myfunc_2 <= th_myfunc_2_5;
          end else begin
            th_myfunc_2 <= th_myfunc_2_6;
          end
        end
        th_myfunc_2_5: begin
          _th_myfunc_2_i_14 <= _th_myfunc_2_i_14 + 1;
          th_myfunc_2 <= th_myfunc_2_4;
        end
        th_myfunc_2_6: begin
          _th_myfunc_2_tmp_15_16 <= _th_myfunc_2_tid_13 + 100;
          th_myfunc_2 <= th_myfunc_2_7;
        end
      endcase
    end
  end

  localparam th_myfunc_3_1 = 1;
  localparam th_myfunc_3_2 = 2;
  localparam th_myfunc_3_3 = 3;
  localparam th_myfunc_3_4 = 4;
  localparam th_myfunc_3_5 = 5;
  localparam th_myfunc_3_6 = 6;
  localparam th_myfunc_3_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_3 <= th_myfunc_3_init;
      _th_myfunc_3_called <= 0;
      _th_myfunc_3_tid_17 <= 0;
      _th_myfunc_3_tid_18 <= 0;
      _th_myfunc_3_i_19 <= 0;
      _th_myfunc_3_tmp_20_21 <= 0;
    end else begin
      case(th_myfunc_3)
        th_myfunc_3_init: begin
          if(_th_myfunc_start[3] && (th_blink == 4)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(_th_myfunc_start[3] && (th_blink == 4)) begin
            _th_myfunc_3_tid_17 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_18 <= _th_myfunc_3_tid_17;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          $display("tid = %d", _th_myfunc_3_tid_18);
          th_myfunc_3 <= th_myfunc_3_3;
        end
        th_myfunc_3_3: begin
          _th_myfunc_3_i_19 <= 0;
          th_myfunc_3 <= th_myfunc_3_4;
        end
        th_myfunc_3_4: begin
          if(_th_myfunc_3_i_19 < 30 - _th_myfunc_3_tid_18) begin
            th_myfunc_3 <= th_myfunc_3_5;
          end else begin
            th_myfunc_3 <= th_myfunc_3_6;
          end
        end
        th_myfunc_3_5: begin
          _th_myfunc_3_i_19 <= _th_myfunc_3_i_19 + 1;
          th_myfunc_3 <= th_myfunc_3_4;
        end
        th_myfunc_3_6: begin
          _th_myfunc_3_tmp_20_21 <= _th_myfunc_3_tid_18 + 100;
          th_myfunc_3 <= th_myfunc_3_7;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_thread_pool.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
