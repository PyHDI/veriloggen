from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_to_thread_pool

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

  reg [8-1:0] _th_myfunc_a_0_start;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_tid_1;
  reg [32-1:0] th_myfunc_a_0;
  localparam th_myfunc_a_0_init = 0;
  reg [32-1:0] th_myfunc_a_1;
  localparam th_myfunc_a_1_init = 0;
  reg [32-1:0] th_myfunc_a_2;
  localparam th_myfunc_a_2_init = 0;
  reg [32-1:0] th_myfunc_a_3;
  localparam th_myfunc_a_3_init = 0;
  reg [32-1:0] th_myfunc_b_0;
  localparam th_myfunc_b_0_init = 0;
  reg [32-1:0] th_myfunc_b_1;
  localparam th_myfunc_b_1_init = 0;
  reg [32-1:0] th_myfunc_b_2;
  localparam th_myfunc_b_2_init = 0;
  reg [32-1:0] th_myfunc_b_3;
  localparam th_myfunc_b_3_init = 0;
  reg _th_myfunc_a_0_called;
  reg signed [32-1:0] _th_myfunc_a_0_tid_2;
  reg signed [32-1:0] _th_myfunc_a_0_tid_3;
  reg signed [32-1:0] _th_myfunc_a_0_i_4;
  reg signed [32-1:0] _th_myfunc_a_0_tmp_5_6;
  reg _th_myfunc_a_1_called;
  reg signed [32-1:0] _th_myfunc_a_1_tid_7;
  reg signed [32-1:0] _th_myfunc_a_1_tid_8;
  reg signed [32-1:0] _th_myfunc_a_1_i_9;
  reg signed [32-1:0] _th_myfunc_a_1_tmp_10_11;
  reg _th_myfunc_a_2_called;
  reg signed [32-1:0] _th_myfunc_a_2_tid_12;
  reg signed [32-1:0] _th_myfunc_a_2_tid_13;
  reg signed [32-1:0] _th_myfunc_a_2_i_14;
  reg signed [32-1:0] _th_myfunc_a_2_tmp_15_16;
  reg _th_myfunc_a_3_called;
  reg signed [32-1:0] _th_myfunc_a_3_tid_17;
  reg signed [32-1:0] _th_myfunc_a_3_tid_18;
  reg signed [32-1:0] _th_myfunc_a_3_i_19;
  reg signed [32-1:0] _th_myfunc_a_3_tmp_20_21;
  reg _th_myfunc_b_0_called;
  reg signed [32-1:0] _th_myfunc_b_0_tid_22;
  reg signed [32-1:0] _th_myfunc_b_0_tid_23;
  reg signed [32-1:0] _th_myfunc_b_0_i_24;
  reg signed [32-1:0] _th_myfunc_b_0_tmp_25_26;
  reg _th_myfunc_b_1_called;
  reg signed [32-1:0] _th_myfunc_b_1_tid_27;
  reg signed [32-1:0] _th_myfunc_b_1_tid_28;
  reg signed [32-1:0] _th_myfunc_b_1_i_29;
  reg signed [32-1:0] _th_myfunc_b_1_tmp_30_31;
  reg _th_myfunc_b_2_called;
  reg signed [32-1:0] _th_myfunc_b_2_tid_32;
  reg signed [32-1:0] _th_myfunc_b_2_tid_33;
  reg signed [32-1:0] _th_myfunc_b_2_i_34;
  reg signed [32-1:0] _th_myfunc_b_2_tmp_35_36;
  reg _th_myfunc_b_3_called;
  reg signed [32-1:0] _th_myfunc_b_3_tid_37;
  reg signed [32-1:0] _th_myfunc_b_3_tid_38;
  reg signed [32-1:0] _th_myfunc_b_3_i_39;
  reg signed [32-1:0] _th_myfunc_b_3_tmp_40_41;
  reg signed [32-1:0] _th_blink_sum_42;
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
      _th_myfunc_a_0_start[_th_blink_tid_1] <= (0 >> _th_blink_tid_1) & 1'd1;
      _th_blink_sum_42 <= 0;
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
          if(_th_blink_tid_1 < 8) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_7;
          end
        end
        th_blink_3: begin
          _th_myfunc_a_0_start[_th_blink_tid_1] <= 1;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_myfunc_a_0_start[_th_blink_tid_1] <= 0;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_tid_1 <= _th_blink_tid_1 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_7: begin
          _th_blink_sum_42 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_tid_1 <= 0;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          if(_th_blink_tid_1 < 8) begin
            th_blink <= th_blink_10;
          end else begin
            th_blink <= th_blink_13;
          end
        end
        th_blink_10: begin
          if((_th_blink_tid_1 == 0)? th_myfunc_a_0 == 7 : 
          (_th_blink_tid_1 == 1)? th_myfunc_a_1 == 7 : 
          (_th_blink_tid_1 == 2)? th_myfunc_a_2 == 7 : 
          (_th_blink_tid_1 == 3)? th_myfunc_a_3 == 7 : 
          (_th_blink_tid_1 == 4)? th_myfunc_b_0 == 7 : 
          (_th_blink_tid_1 == 5)? th_myfunc_b_1 == 7 : 
          (_th_blink_tid_1 == 6)? th_myfunc_b_2 == 7 : 
          (_th_blink_tid_1 == 7)? th_myfunc_b_3 == 7 : 0) begin
            th_blink <= th_blink_11;
          end 
        end
        th_blink_11: begin
          _th_blink_sum_42 <= _th_blink_sum_42 + ((_th_blink_tid_1 == 0)? _th_myfunc_a_0_tmp_5_6 : 
                              (_th_blink_tid_1 == 1)? _th_myfunc_a_1_tmp_10_11 : 
                              (_th_blink_tid_1 == 2)? _th_myfunc_a_2_tmp_15_16 : 
                              (_th_blink_tid_1 == 3)? _th_myfunc_a_3_tmp_20_21 : 
                              (_th_blink_tid_1 == 4)? _th_myfunc_b_0_tmp_25_26 : 
                              (_th_blink_tid_1 == 5)? _th_myfunc_b_1_tmp_30_31 : 
                              (_th_blink_tid_1 == 6)? _th_myfunc_b_2_tmp_35_36 : 
                              (_th_blink_tid_1 == 7)? _th_myfunc_b_3_tmp_40_41 : 'hx);
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          _th_blink_tid_1 <= _th_blink_tid_1 + 1;
          th_blink <= th_blink_9;
        end
        th_blink_13: begin
          $display("sum = %d", _th_blink_sum_42);
          th_blink <= th_blink_14;
        end
      endcase
    end
  end

  localparam th_myfunc_a_0_1 = 1;
  localparam th_myfunc_a_0_2 = 2;
  localparam th_myfunc_a_0_3 = 3;
  localparam th_myfunc_a_0_4 = 4;
  localparam th_myfunc_a_0_5 = 5;
  localparam th_myfunc_a_0_6 = 6;
  localparam th_myfunc_a_0_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_a_0 <= th_myfunc_a_0_init;
      _th_myfunc_a_0_called <= 0;
      _th_myfunc_a_0_tid_2 <= 0;
      _th_myfunc_a_0_tid_3 <= 0;
      _th_myfunc_a_0_i_4 <= 0;
      _th_myfunc_a_0_tmp_5_6 <= 0;
    end else begin
      case(th_myfunc_a_0)
        th_myfunc_a_0_init: begin
          if(_th_myfunc_a_0_start[0] && (th_blink == 4)) begin
            _th_myfunc_a_0_called <= 1;
          end 
          if(_th_myfunc_a_0_start[0] && (th_blink == 4)) begin
            _th_myfunc_a_0_tid_2 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[0]) begin
            th_myfunc_a_0 <= th_myfunc_a_0_1;
          end 
        end
        th_myfunc_a_0_1: begin
          _th_myfunc_a_0_tid_3 <= _th_myfunc_a_0_tid_2;
          th_myfunc_a_0 <= th_myfunc_a_0_2;
        end
        th_myfunc_a_0_2: begin
          $display("myfunc_a: tid = %d", _th_myfunc_a_0_tid_3);
          th_myfunc_a_0 <= th_myfunc_a_0_3;
        end
        th_myfunc_a_0_3: begin
          _th_myfunc_a_0_i_4 <= 0;
          th_myfunc_a_0 <= th_myfunc_a_0_4;
        end
        th_myfunc_a_0_4: begin
          if(_th_myfunc_a_0_i_4 < 30 - _th_myfunc_a_0_tid_3) begin
            th_myfunc_a_0 <= th_myfunc_a_0_5;
          end else begin
            th_myfunc_a_0 <= th_myfunc_a_0_6;
          end
        end
        th_myfunc_a_0_5: begin
          _th_myfunc_a_0_i_4 <= _th_myfunc_a_0_i_4 + 1;
          th_myfunc_a_0 <= th_myfunc_a_0_4;
        end
        th_myfunc_a_0_6: begin
          _th_myfunc_a_0_tmp_5_6 <= _th_myfunc_a_0_tid_3 + 100;
          th_myfunc_a_0 <= th_myfunc_a_0_7;
        end
      endcase
    end
  end

  localparam th_myfunc_a_1_1 = 1;
  localparam th_myfunc_a_1_2 = 2;
  localparam th_myfunc_a_1_3 = 3;
  localparam th_myfunc_a_1_4 = 4;
  localparam th_myfunc_a_1_5 = 5;
  localparam th_myfunc_a_1_6 = 6;
  localparam th_myfunc_a_1_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_a_1 <= th_myfunc_a_1_init;
      _th_myfunc_a_1_called <= 0;
      _th_myfunc_a_1_tid_7 <= 0;
      _th_myfunc_a_1_tid_8 <= 0;
      _th_myfunc_a_1_i_9 <= 0;
      _th_myfunc_a_1_tmp_10_11 <= 0;
    end else begin
      case(th_myfunc_a_1)
        th_myfunc_a_1_init: begin
          if(_th_myfunc_a_0_start[1] && (th_blink == 4)) begin
            _th_myfunc_a_1_called <= 1;
          end 
          if(_th_myfunc_a_0_start[1] && (th_blink == 4)) begin
            _th_myfunc_a_1_tid_7 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[1]) begin
            th_myfunc_a_1 <= th_myfunc_a_1_1;
          end 
        end
        th_myfunc_a_1_1: begin
          _th_myfunc_a_1_tid_8 <= _th_myfunc_a_1_tid_7;
          th_myfunc_a_1 <= th_myfunc_a_1_2;
        end
        th_myfunc_a_1_2: begin
          $display("myfunc_a: tid = %d", _th_myfunc_a_1_tid_8);
          th_myfunc_a_1 <= th_myfunc_a_1_3;
        end
        th_myfunc_a_1_3: begin
          _th_myfunc_a_1_i_9 <= 0;
          th_myfunc_a_1 <= th_myfunc_a_1_4;
        end
        th_myfunc_a_1_4: begin
          if(_th_myfunc_a_1_i_9 < 30 - _th_myfunc_a_1_tid_8) begin
            th_myfunc_a_1 <= th_myfunc_a_1_5;
          end else begin
            th_myfunc_a_1 <= th_myfunc_a_1_6;
          end
        end
        th_myfunc_a_1_5: begin
          _th_myfunc_a_1_i_9 <= _th_myfunc_a_1_i_9 + 1;
          th_myfunc_a_1 <= th_myfunc_a_1_4;
        end
        th_myfunc_a_1_6: begin
          _th_myfunc_a_1_tmp_10_11 <= _th_myfunc_a_1_tid_8 + 100;
          th_myfunc_a_1 <= th_myfunc_a_1_7;
        end
      endcase
    end
  end

  localparam th_myfunc_a_2_1 = 1;
  localparam th_myfunc_a_2_2 = 2;
  localparam th_myfunc_a_2_3 = 3;
  localparam th_myfunc_a_2_4 = 4;
  localparam th_myfunc_a_2_5 = 5;
  localparam th_myfunc_a_2_6 = 6;
  localparam th_myfunc_a_2_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_a_2 <= th_myfunc_a_2_init;
      _th_myfunc_a_2_called <= 0;
      _th_myfunc_a_2_tid_12 <= 0;
      _th_myfunc_a_2_tid_13 <= 0;
      _th_myfunc_a_2_i_14 <= 0;
      _th_myfunc_a_2_tmp_15_16 <= 0;
    end else begin
      case(th_myfunc_a_2)
        th_myfunc_a_2_init: begin
          if(_th_myfunc_a_0_start[2] && (th_blink == 4)) begin
            _th_myfunc_a_2_called <= 1;
          end 
          if(_th_myfunc_a_0_start[2] && (th_blink == 4)) begin
            _th_myfunc_a_2_tid_12 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[2]) begin
            th_myfunc_a_2 <= th_myfunc_a_2_1;
          end 
        end
        th_myfunc_a_2_1: begin
          _th_myfunc_a_2_tid_13 <= _th_myfunc_a_2_tid_12;
          th_myfunc_a_2 <= th_myfunc_a_2_2;
        end
        th_myfunc_a_2_2: begin
          $display("myfunc_a: tid = %d", _th_myfunc_a_2_tid_13);
          th_myfunc_a_2 <= th_myfunc_a_2_3;
        end
        th_myfunc_a_2_3: begin
          _th_myfunc_a_2_i_14 <= 0;
          th_myfunc_a_2 <= th_myfunc_a_2_4;
        end
        th_myfunc_a_2_4: begin
          if(_th_myfunc_a_2_i_14 < 30 - _th_myfunc_a_2_tid_13) begin
            th_myfunc_a_2 <= th_myfunc_a_2_5;
          end else begin
            th_myfunc_a_2 <= th_myfunc_a_2_6;
          end
        end
        th_myfunc_a_2_5: begin
          _th_myfunc_a_2_i_14 <= _th_myfunc_a_2_i_14 + 1;
          th_myfunc_a_2 <= th_myfunc_a_2_4;
        end
        th_myfunc_a_2_6: begin
          _th_myfunc_a_2_tmp_15_16 <= _th_myfunc_a_2_tid_13 + 100;
          th_myfunc_a_2 <= th_myfunc_a_2_7;
        end
      endcase
    end
  end

  localparam th_myfunc_a_3_1 = 1;
  localparam th_myfunc_a_3_2 = 2;
  localparam th_myfunc_a_3_3 = 3;
  localparam th_myfunc_a_3_4 = 4;
  localparam th_myfunc_a_3_5 = 5;
  localparam th_myfunc_a_3_6 = 6;
  localparam th_myfunc_a_3_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_a_3 <= th_myfunc_a_3_init;
      _th_myfunc_a_3_called <= 0;
      _th_myfunc_a_3_tid_17 <= 0;
      _th_myfunc_a_3_tid_18 <= 0;
      _th_myfunc_a_3_i_19 <= 0;
      _th_myfunc_a_3_tmp_20_21 <= 0;
    end else begin
      case(th_myfunc_a_3)
        th_myfunc_a_3_init: begin
          if(_th_myfunc_a_0_start[3] && (th_blink == 4)) begin
            _th_myfunc_a_3_called <= 1;
          end 
          if(_th_myfunc_a_0_start[3] && (th_blink == 4)) begin
            _th_myfunc_a_3_tid_17 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[3]) begin
            th_myfunc_a_3 <= th_myfunc_a_3_1;
          end 
        end
        th_myfunc_a_3_1: begin
          _th_myfunc_a_3_tid_18 <= _th_myfunc_a_3_tid_17;
          th_myfunc_a_3 <= th_myfunc_a_3_2;
        end
        th_myfunc_a_3_2: begin
          $display("myfunc_a: tid = %d", _th_myfunc_a_3_tid_18);
          th_myfunc_a_3 <= th_myfunc_a_3_3;
        end
        th_myfunc_a_3_3: begin
          _th_myfunc_a_3_i_19 <= 0;
          th_myfunc_a_3 <= th_myfunc_a_3_4;
        end
        th_myfunc_a_3_4: begin
          if(_th_myfunc_a_3_i_19 < 30 - _th_myfunc_a_3_tid_18) begin
            th_myfunc_a_3 <= th_myfunc_a_3_5;
          end else begin
            th_myfunc_a_3 <= th_myfunc_a_3_6;
          end
        end
        th_myfunc_a_3_5: begin
          _th_myfunc_a_3_i_19 <= _th_myfunc_a_3_i_19 + 1;
          th_myfunc_a_3 <= th_myfunc_a_3_4;
        end
        th_myfunc_a_3_6: begin
          _th_myfunc_a_3_tmp_20_21 <= _th_myfunc_a_3_tid_18 + 100;
          th_myfunc_a_3 <= th_myfunc_a_3_7;
        end
      endcase
    end
  end

  localparam th_myfunc_b_0_1 = 1;
  localparam th_myfunc_b_0_2 = 2;
  localparam th_myfunc_b_0_3 = 3;
  localparam th_myfunc_b_0_4 = 4;
  localparam th_myfunc_b_0_5 = 5;
  localparam th_myfunc_b_0_6 = 6;
  localparam th_myfunc_b_0_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_b_0 <= th_myfunc_b_0_init;
      _th_myfunc_b_0_called <= 0;
      _th_myfunc_b_0_tid_22 <= 0;
      _th_myfunc_b_0_tid_23 <= 0;
      _th_myfunc_b_0_i_24 <= 0;
      _th_myfunc_b_0_tmp_25_26 <= 0;
    end else begin
      case(th_myfunc_b_0)
        th_myfunc_b_0_init: begin
          if(_th_myfunc_a_0_start[4] && (th_blink == 4)) begin
            _th_myfunc_b_0_called <= 1;
          end 
          if(_th_myfunc_a_0_start[4] && (th_blink == 4)) begin
            _th_myfunc_b_0_tid_22 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[4]) begin
            th_myfunc_b_0 <= th_myfunc_b_0_1;
          end 
        end
        th_myfunc_b_0_1: begin
          _th_myfunc_b_0_tid_23 <= _th_myfunc_b_0_tid_22;
          th_myfunc_b_0 <= th_myfunc_b_0_2;
        end
        th_myfunc_b_0_2: begin
          $display("myfunc_b: tid = %d", _th_myfunc_b_0_tid_23);
          th_myfunc_b_0 <= th_myfunc_b_0_3;
        end
        th_myfunc_b_0_3: begin
          _th_myfunc_b_0_i_24 <= 0;
          th_myfunc_b_0 <= th_myfunc_b_0_4;
        end
        th_myfunc_b_0_4: begin
          if(_th_myfunc_b_0_i_24 < 30 - _th_myfunc_b_0_tid_23) begin
            th_myfunc_b_0 <= th_myfunc_b_0_5;
          end else begin
            th_myfunc_b_0 <= th_myfunc_b_0_6;
          end
        end
        th_myfunc_b_0_5: begin
          _th_myfunc_b_0_i_24 <= _th_myfunc_b_0_i_24 + 1;
          th_myfunc_b_0 <= th_myfunc_b_0_4;
        end
        th_myfunc_b_0_6: begin
          _th_myfunc_b_0_tmp_25_26 <= _th_myfunc_b_0_tid_23 + 200;
          th_myfunc_b_0 <= th_myfunc_b_0_7;
        end
      endcase
    end
  end

  localparam th_myfunc_b_1_1 = 1;
  localparam th_myfunc_b_1_2 = 2;
  localparam th_myfunc_b_1_3 = 3;
  localparam th_myfunc_b_1_4 = 4;
  localparam th_myfunc_b_1_5 = 5;
  localparam th_myfunc_b_1_6 = 6;
  localparam th_myfunc_b_1_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_b_1 <= th_myfunc_b_1_init;
      _th_myfunc_b_1_called <= 0;
      _th_myfunc_b_1_tid_27 <= 0;
      _th_myfunc_b_1_tid_28 <= 0;
      _th_myfunc_b_1_i_29 <= 0;
      _th_myfunc_b_1_tmp_30_31 <= 0;
    end else begin
      case(th_myfunc_b_1)
        th_myfunc_b_1_init: begin
          if(_th_myfunc_a_0_start[5] && (th_blink == 4)) begin
            _th_myfunc_b_1_called <= 1;
          end 
          if(_th_myfunc_a_0_start[5] && (th_blink == 4)) begin
            _th_myfunc_b_1_tid_27 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[5]) begin
            th_myfunc_b_1 <= th_myfunc_b_1_1;
          end 
        end
        th_myfunc_b_1_1: begin
          _th_myfunc_b_1_tid_28 <= _th_myfunc_b_1_tid_27;
          th_myfunc_b_1 <= th_myfunc_b_1_2;
        end
        th_myfunc_b_1_2: begin
          $display("myfunc_b: tid = %d", _th_myfunc_b_1_tid_28);
          th_myfunc_b_1 <= th_myfunc_b_1_3;
        end
        th_myfunc_b_1_3: begin
          _th_myfunc_b_1_i_29 <= 0;
          th_myfunc_b_1 <= th_myfunc_b_1_4;
        end
        th_myfunc_b_1_4: begin
          if(_th_myfunc_b_1_i_29 < 30 - _th_myfunc_b_1_tid_28) begin
            th_myfunc_b_1 <= th_myfunc_b_1_5;
          end else begin
            th_myfunc_b_1 <= th_myfunc_b_1_6;
          end
        end
        th_myfunc_b_1_5: begin
          _th_myfunc_b_1_i_29 <= _th_myfunc_b_1_i_29 + 1;
          th_myfunc_b_1 <= th_myfunc_b_1_4;
        end
        th_myfunc_b_1_6: begin
          _th_myfunc_b_1_tmp_30_31 <= _th_myfunc_b_1_tid_28 + 200;
          th_myfunc_b_1 <= th_myfunc_b_1_7;
        end
      endcase
    end
  end

  localparam th_myfunc_b_2_1 = 1;
  localparam th_myfunc_b_2_2 = 2;
  localparam th_myfunc_b_2_3 = 3;
  localparam th_myfunc_b_2_4 = 4;
  localparam th_myfunc_b_2_5 = 5;
  localparam th_myfunc_b_2_6 = 6;
  localparam th_myfunc_b_2_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_b_2 <= th_myfunc_b_2_init;
      _th_myfunc_b_2_called <= 0;
      _th_myfunc_b_2_tid_32 <= 0;
      _th_myfunc_b_2_tid_33 <= 0;
      _th_myfunc_b_2_i_34 <= 0;
      _th_myfunc_b_2_tmp_35_36 <= 0;
    end else begin
      case(th_myfunc_b_2)
        th_myfunc_b_2_init: begin
          if(_th_myfunc_a_0_start[6] && (th_blink == 4)) begin
            _th_myfunc_b_2_called <= 1;
          end 
          if(_th_myfunc_a_0_start[6] && (th_blink == 4)) begin
            _th_myfunc_b_2_tid_32 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[6]) begin
            th_myfunc_b_2 <= th_myfunc_b_2_1;
          end 
        end
        th_myfunc_b_2_1: begin
          _th_myfunc_b_2_tid_33 <= _th_myfunc_b_2_tid_32;
          th_myfunc_b_2 <= th_myfunc_b_2_2;
        end
        th_myfunc_b_2_2: begin
          $display("myfunc_b: tid = %d", _th_myfunc_b_2_tid_33);
          th_myfunc_b_2 <= th_myfunc_b_2_3;
        end
        th_myfunc_b_2_3: begin
          _th_myfunc_b_2_i_34 <= 0;
          th_myfunc_b_2 <= th_myfunc_b_2_4;
        end
        th_myfunc_b_2_4: begin
          if(_th_myfunc_b_2_i_34 < 30 - _th_myfunc_b_2_tid_33) begin
            th_myfunc_b_2 <= th_myfunc_b_2_5;
          end else begin
            th_myfunc_b_2 <= th_myfunc_b_2_6;
          end
        end
        th_myfunc_b_2_5: begin
          _th_myfunc_b_2_i_34 <= _th_myfunc_b_2_i_34 + 1;
          th_myfunc_b_2 <= th_myfunc_b_2_4;
        end
        th_myfunc_b_2_6: begin
          _th_myfunc_b_2_tmp_35_36 <= _th_myfunc_b_2_tid_33 + 200;
          th_myfunc_b_2 <= th_myfunc_b_2_7;
        end
      endcase
    end
  end

  localparam th_myfunc_b_3_1 = 1;
  localparam th_myfunc_b_3_2 = 2;
  localparam th_myfunc_b_3_3 = 3;
  localparam th_myfunc_b_3_4 = 4;
  localparam th_myfunc_b_3_5 = 5;
  localparam th_myfunc_b_3_6 = 6;
  localparam th_myfunc_b_3_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_b_3 <= th_myfunc_b_3_init;
      _th_myfunc_b_3_called <= 0;
      _th_myfunc_b_3_tid_37 <= 0;
      _th_myfunc_b_3_tid_38 <= 0;
      _th_myfunc_b_3_i_39 <= 0;
      _th_myfunc_b_3_tmp_40_41 <= 0;
    end else begin
      case(th_myfunc_b_3)
        th_myfunc_b_3_init: begin
          if(_th_myfunc_a_0_start[7] && (th_blink == 4)) begin
            _th_myfunc_b_3_called <= 1;
          end 
          if(_th_myfunc_a_0_start[7] && (th_blink == 4)) begin
            _th_myfunc_b_3_tid_37 <= _th_blink_tid_1;
          end 
          if((th_blink == 4) && _th_myfunc_a_0_start[7]) begin
            th_myfunc_b_3 <= th_myfunc_b_3_1;
          end 
        end
        th_myfunc_b_3_1: begin
          _th_myfunc_b_3_tid_38 <= _th_myfunc_b_3_tid_37;
          th_myfunc_b_3 <= th_myfunc_b_3_2;
        end
        th_myfunc_b_3_2: begin
          $display("myfunc_b: tid = %d", _th_myfunc_b_3_tid_38);
          th_myfunc_b_3 <= th_myfunc_b_3_3;
        end
        th_myfunc_b_3_3: begin
          _th_myfunc_b_3_i_39 <= 0;
          th_myfunc_b_3 <= th_myfunc_b_3_4;
        end
        th_myfunc_b_3_4: begin
          if(_th_myfunc_b_3_i_39 < 30 - _th_myfunc_b_3_tid_38) begin
            th_myfunc_b_3 <= th_myfunc_b_3_5;
          end else begin
            th_myfunc_b_3 <= th_myfunc_b_3_6;
          end
        end
        th_myfunc_b_3_5: begin
          _th_myfunc_b_3_i_39 <= _th_myfunc_b_3_i_39 + 1;
          th_myfunc_b_3 <= th_myfunc_b_3_4;
        end
        th_myfunc_b_3_6: begin
          _th_myfunc_b_3_tmp_40_41 <= _th_myfunc_b_3_tid_38 + 200;
          th_myfunc_b_3 <= th_myfunc_b_3_7;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_to_thread_pool.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
