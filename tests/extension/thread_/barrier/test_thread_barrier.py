from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_barrier

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

  reg [4-1:0] _mybarrier_barrier_count;
  reg _mybarrier_barrier_done;
  reg __mybarrier_barrier_mutex_lock_reg;
  reg [32-1:0] __mybarrier_barrier_mutex_lock_id;
  reg [32-1:0] clock_counter;
  reg [8-1:0] _th_myfunc_start;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_tid_0;
  reg [32-1:0] th_myfunc_0;
  localparam th_myfunc_0_init = 0;
  reg [32-1:0] th_myfunc_1;
  localparam th_myfunc_1_init = 0;
  reg [32-1:0] th_myfunc_2;
  localparam th_myfunc_2_init = 0;
  reg [32-1:0] th_myfunc_3;
  localparam th_myfunc_3_init = 0;
  reg [32-1:0] th_myfunc_4;
  localparam th_myfunc_4_init = 0;
  reg [32-1:0] th_myfunc_5;
  localparam th_myfunc_5_init = 0;
  reg [32-1:0] th_myfunc_6;
  localparam th_myfunc_6_init = 0;
  reg [32-1:0] th_myfunc_7;
  localparam th_myfunc_7_init = 0;
  reg _th_myfunc_0_called;
  reg signed [32-1:0] _th_myfunc_0_tid_1;
  reg signed [32-1:0] _th_myfunc_0_tid_2;
  reg signed [32-1:0] _th_myfunc_0_step_3;
  reg signed [32-1:0] _th_myfunc_0_i_4;
  reg _th_myfunc_1_called;
  reg signed [32-1:0] _th_myfunc_1_tid_5;
  reg signed [32-1:0] _th_myfunc_1_tid_6;
  reg signed [32-1:0] _th_myfunc_1_step_7;
  reg signed [32-1:0] _th_myfunc_1_i_8;
  reg _th_myfunc_2_called;
  reg signed [32-1:0] _th_myfunc_2_tid_9;
  reg signed [32-1:0] _th_myfunc_2_tid_10;
  reg signed [32-1:0] _th_myfunc_2_step_11;
  reg signed [32-1:0] _th_myfunc_2_i_12;
  reg _th_myfunc_3_called;
  reg signed [32-1:0] _th_myfunc_3_tid_13;
  reg signed [32-1:0] _th_myfunc_3_tid_14;
  reg signed [32-1:0] _th_myfunc_3_step_15;
  reg signed [32-1:0] _th_myfunc_3_i_16;
  reg _th_myfunc_4_called;
  reg signed [32-1:0] _th_myfunc_4_tid_17;
  reg signed [32-1:0] _th_myfunc_4_tid_18;
  reg signed [32-1:0] _th_myfunc_4_step_19;
  reg signed [32-1:0] _th_myfunc_4_i_20;
  reg _th_myfunc_5_called;
  reg signed [32-1:0] _th_myfunc_5_tid_21;
  reg signed [32-1:0] _th_myfunc_5_tid_22;
  reg signed [32-1:0] _th_myfunc_5_step_23;
  reg signed [32-1:0] _th_myfunc_5_i_24;
  reg _th_myfunc_6_called;
  reg signed [32-1:0] _th_myfunc_6_tid_25;
  reg signed [32-1:0] _th_myfunc_6_tid_26;
  reg signed [32-1:0] _th_myfunc_6_step_27;
  reg signed [32-1:0] _th_myfunc_6_i_28;
  reg _th_myfunc_7_called;
  reg signed [32-1:0] _th_myfunc_7_tid_29;
  reg signed [32-1:0] _th_myfunc_7_tid_30;
  reg signed [32-1:0] _th_myfunc_7_step_31;
  reg signed [32-1:0] _th_myfunc_7_i_32;

  always @(posedge CLK) begin
    if(RST) begin
      _mybarrier_barrier_done <= 0;
      _mybarrier_barrier_count <= 0;
    end else begin
      _mybarrier_barrier_done <= 0;
      if(_mybarrier_barrier_count == 8) begin
        _mybarrier_barrier_count <= 0;
        _mybarrier_barrier_done <= 1;
      end 
      if(th_myfunc_0 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_1 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_2 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_3 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_4 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_5 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_6 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
      if(th_myfunc_7 == 9) begin
        _mybarrier_barrier_count <= _mybarrier_barrier_count + 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __mybarrier_barrier_mutex_lock_reg <= 0;
      __mybarrier_barrier_mutex_lock_id <= 0;
    end else begin
      if((th_myfunc_0 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 10) && (__mybarrier_barrier_mutex_lock_id == 0)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_1 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 10) && (__mybarrier_barrier_mutex_lock_id == 1)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_2 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 10) && (__mybarrier_barrier_mutex_lock_id == 2)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_3 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 10) && (__mybarrier_barrier_mutex_lock_id == 3)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_4 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 10) && (__mybarrier_barrier_mutex_lock_id == 4)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_5 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 10) && (__mybarrier_barrier_mutex_lock_id == 5)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_6 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 10) && (__mybarrier_barrier_mutex_lock_id == 6)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_7 == 7) && !__mybarrier_barrier_mutex_lock_reg) begin
        __mybarrier_barrier_mutex_lock_reg <= 1;
        __mybarrier_barrier_mutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 10) && (__mybarrier_barrier_mutex_lock_id == 7)) begin
        __mybarrier_barrier_mutex_lock_reg <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      clock_counter <= 0;
    end else begin
      clock_counter <= clock_counter + 1;
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
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_tid_0 <= 0;
      _th_myfunc_start[_th_blink_tid_0] <= (0 >> _th_blink_tid_0) & 1'd1;
    end else begin
      case(th_blink)
        th_blink_init: begin
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_tid_0 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          if(_th_blink_tid_0 < 8) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_7;
          end
        end
        th_blink_3: begin
          _th_myfunc_start[_th_blink_tid_0] <= 1;
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
          _th_myfunc_start[_th_blink_tid_0] <= 0;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_tid_0 <= _th_blink_tid_0 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_7: begin
          _th_blink_tid_0 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_tid_0 < 8) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_11;
          end
        end
        th_blink_9: begin
          if((_th_blink_tid_0 == 0)? th_myfunc_0 == 14 : 
          (_th_blink_tid_0 == 1)? th_myfunc_1 == 14 : 
          (_th_blink_tid_0 == 2)? th_myfunc_2 == 14 : 
          (_th_blink_tid_0 == 3)? th_myfunc_3 == 14 : 
          (_th_blink_tid_0 == 4)? th_myfunc_4 == 14 : 
          (_th_blink_tid_0 == 5)? th_myfunc_5 == 14 : 
          (_th_blink_tid_0 == 6)? th_myfunc_6 == 14 : 
          (_th_blink_tid_0 == 7)? th_myfunc_7 == 14 : 0) begin
            th_blink <= th_blink_10;
          end 
        end
        th_blink_10: begin
          _th_blink_tid_0 <= _th_blink_tid_0 + 1;
          th_blink <= th_blink_8;
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
  localparam th_myfunc_0_8 = 8;
  localparam th_myfunc_0_9 = 9;
  localparam th_myfunc_0_10 = 10;
  localparam th_myfunc_0_11 = 11;
  localparam th_myfunc_0_12 = 12;
  localparam th_myfunc_0_13 = 13;
  localparam th_myfunc_0_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_0 <= th_myfunc_0_init;
      _th_myfunc_0_called <= 0;
      _th_myfunc_0_tid_1 <= 0;
      _th_myfunc_0_tid_2 <= 0;
      _th_myfunc_0_step_3 <= 0;
      _th_myfunc_0_i_4 <= 0;
    end else begin
      case(th_myfunc_0)
        th_myfunc_0_init: begin
          if(_th_myfunc_start[0] && (th_blink == 4)) begin
            _th_myfunc_0_called <= 1;
          end 
          if(_th_myfunc_start[0] && (th_blink == 4)) begin
            _th_myfunc_0_tid_1 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[0]) begin
            th_myfunc_0 <= th_myfunc_0_1;
          end 
        end
        th_myfunc_0_1: begin
          _th_myfunc_0_tid_2 <= _th_myfunc_0_tid_1;
          th_myfunc_0 <= th_myfunc_0_2;
        end
        th_myfunc_0_2: begin
          _th_myfunc_0_step_3 <= 0;
          th_myfunc_0 <= th_myfunc_0_3;
        end
        th_myfunc_0_3: begin
          if(_th_myfunc_0_step_3 < 10) begin
            th_myfunc_0 <= th_myfunc_0_4;
          end else begin
            th_myfunc_0 <= th_myfunc_0_14;
          end
        end
        th_myfunc_0_4: begin
          _th_myfunc_0_i_4 <= 0;
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_5: begin
          if(_th_myfunc_0_i_4 < 20) begin
            th_myfunc_0 <= th_myfunc_0_6;
          end else begin
            th_myfunc_0 <= th_myfunc_0_7;
          end
        end
        th_myfunc_0_6: begin
          _th_myfunc_0_i_4 <= _th_myfunc_0_i_4 + 1;
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_8;
          end 
        end
        th_myfunc_0_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 0))) begin
            th_myfunc_0 <= th_myfunc_0_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_9;
          end 
        end
        th_myfunc_0_9: begin
          th_myfunc_0 <= th_myfunc_0_10;
        end
        th_myfunc_0_10: begin
          th_myfunc_0 <= th_myfunc_0_11;
        end
        th_myfunc_0_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_0 <= th_myfunc_0_12;
          end 
        end
        th_myfunc_0_12: begin
          $display("Thread %d Time %d", _th_myfunc_0_tid_2, clock_counter);
          th_myfunc_0 <= th_myfunc_0_13;
        end
        th_myfunc_0_13: begin
          _th_myfunc_0_step_3 <= _th_myfunc_0_step_3 + 1;
          th_myfunc_0 <= th_myfunc_0_3;
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
  localparam th_myfunc_1_8 = 8;
  localparam th_myfunc_1_9 = 9;
  localparam th_myfunc_1_10 = 10;
  localparam th_myfunc_1_11 = 11;
  localparam th_myfunc_1_12 = 12;
  localparam th_myfunc_1_13 = 13;
  localparam th_myfunc_1_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_1 <= th_myfunc_1_init;
      _th_myfunc_1_called <= 0;
      _th_myfunc_1_tid_5 <= 0;
      _th_myfunc_1_tid_6 <= 0;
      _th_myfunc_1_step_7 <= 0;
      _th_myfunc_1_i_8 <= 0;
    end else begin
      case(th_myfunc_1)
        th_myfunc_1_init: begin
          if(_th_myfunc_start[1] && (th_blink == 4)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(_th_myfunc_start[1] && (th_blink == 4)) begin
            _th_myfunc_1_tid_5 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_6 <= _th_myfunc_1_tid_5;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          _th_myfunc_1_step_7 <= 0;
          th_myfunc_1 <= th_myfunc_1_3;
        end
        th_myfunc_1_3: begin
          if(_th_myfunc_1_step_7 < 10) begin
            th_myfunc_1 <= th_myfunc_1_4;
          end else begin
            th_myfunc_1 <= th_myfunc_1_14;
          end
        end
        th_myfunc_1_4: begin
          _th_myfunc_1_i_8 <= 0;
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_5: begin
          if(_th_myfunc_1_i_8 < 20) begin
            th_myfunc_1 <= th_myfunc_1_6;
          end else begin
            th_myfunc_1 <= th_myfunc_1_7;
          end
        end
        th_myfunc_1_6: begin
          _th_myfunc_1_i_8 <= _th_myfunc_1_i_8 + 1;
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_8;
          end 
        end
        th_myfunc_1_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 1))) begin
            th_myfunc_1 <= th_myfunc_1_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_9;
          end 
        end
        th_myfunc_1_9: begin
          th_myfunc_1 <= th_myfunc_1_10;
        end
        th_myfunc_1_10: begin
          th_myfunc_1 <= th_myfunc_1_11;
        end
        th_myfunc_1_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_1 <= th_myfunc_1_12;
          end 
        end
        th_myfunc_1_12: begin
          $display("Thread %d Time %d", _th_myfunc_1_tid_6, clock_counter);
          th_myfunc_1 <= th_myfunc_1_13;
        end
        th_myfunc_1_13: begin
          _th_myfunc_1_step_7 <= _th_myfunc_1_step_7 + 1;
          th_myfunc_1 <= th_myfunc_1_3;
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
  localparam th_myfunc_2_8 = 8;
  localparam th_myfunc_2_9 = 9;
  localparam th_myfunc_2_10 = 10;
  localparam th_myfunc_2_11 = 11;
  localparam th_myfunc_2_12 = 12;
  localparam th_myfunc_2_13 = 13;
  localparam th_myfunc_2_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_2 <= th_myfunc_2_init;
      _th_myfunc_2_called <= 0;
      _th_myfunc_2_tid_9 <= 0;
      _th_myfunc_2_tid_10 <= 0;
      _th_myfunc_2_step_11 <= 0;
      _th_myfunc_2_i_12 <= 0;
    end else begin
      case(th_myfunc_2)
        th_myfunc_2_init: begin
          if(_th_myfunc_start[2] && (th_blink == 4)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(_th_myfunc_start[2] && (th_blink == 4)) begin
            _th_myfunc_2_tid_9 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_10 <= _th_myfunc_2_tid_9;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          _th_myfunc_2_step_11 <= 0;
          th_myfunc_2 <= th_myfunc_2_3;
        end
        th_myfunc_2_3: begin
          if(_th_myfunc_2_step_11 < 10) begin
            th_myfunc_2 <= th_myfunc_2_4;
          end else begin
            th_myfunc_2 <= th_myfunc_2_14;
          end
        end
        th_myfunc_2_4: begin
          _th_myfunc_2_i_12 <= 0;
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_5: begin
          if(_th_myfunc_2_i_12 < 20) begin
            th_myfunc_2 <= th_myfunc_2_6;
          end else begin
            th_myfunc_2 <= th_myfunc_2_7;
          end
        end
        th_myfunc_2_6: begin
          _th_myfunc_2_i_12 <= _th_myfunc_2_i_12 + 1;
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_8;
          end 
        end
        th_myfunc_2_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 2))) begin
            th_myfunc_2 <= th_myfunc_2_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_9;
          end 
        end
        th_myfunc_2_9: begin
          th_myfunc_2 <= th_myfunc_2_10;
        end
        th_myfunc_2_10: begin
          th_myfunc_2 <= th_myfunc_2_11;
        end
        th_myfunc_2_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_2 <= th_myfunc_2_12;
          end 
        end
        th_myfunc_2_12: begin
          $display("Thread %d Time %d", _th_myfunc_2_tid_10, clock_counter);
          th_myfunc_2 <= th_myfunc_2_13;
        end
        th_myfunc_2_13: begin
          _th_myfunc_2_step_11 <= _th_myfunc_2_step_11 + 1;
          th_myfunc_2 <= th_myfunc_2_3;
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
  localparam th_myfunc_3_8 = 8;
  localparam th_myfunc_3_9 = 9;
  localparam th_myfunc_3_10 = 10;
  localparam th_myfunc_3_11 = 11;
  localparam th_myfunc_3_12 = 12;
  localparam th_myfunc_3_13 = 13;
  localparam th_myfunc_3_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_3 <= th_myfunc_3_init;
      _th_myfunc_3_called <= 0;
      _th_myfunc_3_tid_13 <= 0;
      _th_myfunc_3_tid_14 <= 0;
      _th_myfunc_3_step_15 <= 0;
      _th_myfunc_3_i_16 <= 0;
    end else begin
      case(th_myfunc_3)
        th_myfunc_3_init: begin
          if(_th_myfunc_start[3] && (th_blink == 4)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(_th_myfunc_start[3] && (th_blink == 4)) begin
            _th_myfunc_3_tid_13 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_14 <= _th_myfunc_3_tid_13;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          _th_myfunc_3_step_15 <= 0;
          th_myfunc_3 <= th_myfunc_3_3;
        end
        th_myfunc_3_3: begin
          if(_th_myfunc_3_step_15 < 10) begin
            th_myfunc_3 <= th_myfunc_3_4;
          end else begin
            th_myfunc_3 <= th_myfunc_3_14;
          end
        end
        th_myfunc_3_4: begin
          _th_myfunc_3_i_16 <= 0;
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_5: begin
          if(_th_myfunc_3_i_16 < 20) begin
            th_myfunc_3 <= th_myfunc_3_6;
          end else begin
            th_myfunc_3 <= th_myfunc_3_7;
          end
        end
        th_myfunc_3_6: begin
          _th_myfunc_3_i_16 <= _th_myfunc_3_i_16 + 1;
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_8;
          end 
        end
        th_myfunc_3_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 3))) begin
            th_myfunc_3 <= th_myfunc_3_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_9;
          end 
        end
        th_myfunc_3_9: begin
          th_myfunc_3 <= th_myfunc_3_10;
        end
        th_myfunc_3_10: begin
          th_myfunc_3 <= th_myfunc_3_11;
        end
        th_myfunc_3_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_3 <= th_myfunc_3_12;
          end 
        end
        th_myfunc_3_12: begin
          $display("Thread %d Time %d", _th_myfunc_3_tid_14, clock_counter);
          th_myfunc_3 <= th_myfunc_3_13;
        end
        th_myfunc_3_13: begin
          _th_myfunc_3_step_15 <= _th_myfunc_3_step_15 + 1;
          th_myfunc_3 <= th_myfunc_3_3;
        end
      endcase
    end
  end

  localparam th_myfunc_4_1 = 1;
  localparam th_myfunc_4_2 = 2;
  localparam th_myfunc_4_3 = 3;
  localparam th_myfunc_4_4 = 4;
  localparam th_myfunc_4_5 = 5;
  localparam th_myfunc_4_6 = 6;
  localparam th_myfunc_4_7 = 7;
  localparam th_myfunc_4_8 = 8;
  localparam th_myfunc_4_9 = 9;
  localparam th_myfunc_4_10 = 10;
  localparam th_myfunc_4_11 = 11;
  localparam th_myfunc_4_12 = 12;
  localparam th_myfunc_4_13 = 13;
  localparam th_myfunc_4_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_4 <= th_myfunc_4_init;
      _th_myfunc_4_called <= 0;
      _th_myfunc_4_tid_17 <= 0;
      _th_myfunc_4_tid_18 <= 0;
      _th_myfunc_4_step_19 <= 0;
      _th_myfunc_4_i_20 <= 0;
    end else begin
      case(th_myfunc_4)
        th_myfunc_4_init: begin
          if(_th_myfunc_start[4] && (th_blink == 4)) begin
            _th_myfunc_4_called <= 1;
          end 
          if(_th_myfunc_start[4] && (th_blink == 4)) begin
            _th_myfunc_4_tid_17 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[4]) begin
            th_myfunc_4 <= th_myfunc_4_1;
          end 
        end
        th_myfunc_4_1: begin
          _th_myfunc_4_tid_18 <= _th_myfunc_4_tid_17;
          th_myfunc_4 <= th_myfunc_4_2;
        end
        th_myfunc_4_2: begin
          _th_myfunc_4_step_19 <= 0;
          th_myfunc_4 <= th_myfunc_4_3;
        end
        th_myfunc_4_3: begin
          if(_th_myfunc_4_step_19 < 10) begin
            th_myfunc_4 <= th_myfunc_4_4;
          end else begin
            th_myfunc_4 <= th_myfunc_4_14;
          end
        end
        th_myfunc_4_4: begin
          _th_myfunc_4_i_20 <= 0;
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_5: begin
          if(_th_myfunc_4_i_20 < 20) begin
            th_myfunc_4 <= th_myfunc_4_6;
          end else begin
            th_myfunc_4 <= th_myfunc_4_7;
          end
        end
        th_myfunc_4_6: begin
          _th_myfunc_4_i_20 <= _th_myfunc_4_i_20 + 1;
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_8;
          end 
        end
        th_myfunc_4_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 4))) begin
            th_myfunc_4 <= th_myfunc_4_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_9;
          end 
        end
        th_myfunc_4_9: begin
          th_myfunc_4 <= th_myfunc_4_10;
        end
        th_myfunc_4_10: begin
          th_myfunc_4 <= th_myfunc_4_11;
        end
        th_myfunc_4_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_4 <= th_myfunc_4_12;
          end 
        end
        th_myfunc_4_12: begin
          $display("Thread %d Time %d", _th_myfunc_4_tid_18, clock_counter);
          th_myfunc_4 <= th_myfunc_4_13;
        end
        th_myfunc_4_13: begin
          _th_myfunc_4_step_19 <= _th_myfunc_4_step_19 + 1;
          th_myfunc_4 <= th_myfunc_4_3;
        end
      endcase
    end
  end

  localparam th_myfunc_5_1 = 1;
  localparam th_myfunc_5_2 = 2;
  localparam th_myfunc_5_3 = 3;
  localparam th_myfunc_5_4 = 4;
  localparam th_myfunc_5_5 = 5;
  localparam th_myfunc_5_6 = 6;
  localparam th_myfunc_5_7 = 7;
  localparam th_myfunc_5_8 = 8;
  localparam th_myfunc_5_9 = 9;
  localparam th_myfunc_5_10 = 10;
  localparam th_myfunc_5_11 = 11;
  localparam th_myfunc_5_12 = 12;
  localparam th_myfunc_5_13 = 13;
  localparam th_myfunc_5_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_5 <= th_myfunc_5_init;
      _th_myfunc_5_called <= 0;
      _th_myfunc_5_tid_21 <= 0;
      _th_myfunc_5_tid_22 <= 0;
      _th_myfunc_5_step_23 <= 0;
      _th_myfunc_5_i_24 <= 0;
    end else begin
      case(th_myfunc_5)
        th_myfunc_5_init: begin
          if(_th_myfunc_start[5] && (th_blink == 4)) begin
            _th_myfunc_5_called <= 1;
          end 
          if(_th_myfunc_start[5] && (th_blink == 4)) begin
            _th_myfunc_5_tid_21 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[5]) begin
            th_myfunc_5 <= th_myfunc_5_1;
          end 
        end
        th_myfunc_5_1: begin
          _th_myfunc_5_tid_22 <= _th_myfunc_5_tid_21;
          th_myfunc_5 <= th_myfunc_5_2;
        end
        th_myfunc_5_2: begin
          _th_myfunc_5_step_23 <= 0;
          th_myfunc_5 <= th_myfunc_5_3;
        end
        th_myfunc_5_3: begin
          if(_th_myfunc_5_step_23 < 10) begin
            th_myfunc_5 <= th_myfunc_5_4;
          end else begin
            th_myfunc_5 <= th_myfunc_5_14;
          end
        end
        th_myfunc_5_4: begin
          _th_myfunc_5_i_24 <= 0;
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_5: begin
          if(_th_myfunc_5_i_24 < 20) begin
            th_myfunc_5 <= th_myfunc_5_6;
          end else begin
            th_myfunc_5 <= th_myfunc_5_7;
          end
        end
        th_myfunc_5_6: begin
          _th_myfunc_5_i_24 <= _th_myfunc_5_i_24 + 1;
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_8;
          end 
        end
        th_myfunc_5_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 5))) begin
            th_myfunc_5 <= th_myfunc_5_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_9;
          end 
        end
        th_myfunc_5_9: begin
          th_myfunc_5 <= th_myfunc_5_10;
        end
        th_myfunc_5_10: begin
          th_myfunc_5 <= th_myfunc_5_11;
        end
        th_myfunc_5_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_5 <= th_myfunc_5_12;
          end 
        end
        th_myfunc_5_12: begin
          $display("Thread %d Time %d", _th_myfunc_5_tid_22, clock_counter);
          th_myfunc_5 <= th_myfunc_5_13;
        end
        th_myfunc_5_13: begin
          _th_myfunc_5_step_23 <= _th_myfunc_5_step_23 + 1;
          th_myfunc_5 <= th_myfunc_5_3;
        end
      endcase
    end
  end

  localparam th_myfunc_6_1 = 1;
  localparam th_myfunc_6_2 = 2;
  localparam th_myfunc_6_3 = 3;
  localparam th_myfunc_6_4 = 4;
  localparam th_myfunc_6_5 = 5;
  localparam th_myfunc_6_6 = 6;
  localparam th_myfunc_6_7 = 7;
  localparam th_myfunc_6_8 = 8;
  localparam th_myfunc_6_9 = 9;
  localparam th_myfunc_6_10 = 10;
  localparam th_myfunc_6_11 = 11;
  localparam th_myfunc_6_12 = 12;
  localparam th_myfunc_6_13 = 13;
  localparam th_myfunc_6_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_6 <= th_myfunc_6_init;
      _th_myfunc_6_called <= 0;
      _th_myfunc_6_tid_25 <= 0;
      _th_myfunc_6_tid_26 <= 0;
      _th_myfunc_6_step_27 <= 0;
      _th_myfunc_6_i_28 <= 0;
    end else begin
      case(th_myfunc_6)
        th_myfunc_6_init: begin
          if(_th_myfunc_start[6] && (th_blink == 4)) begin
            _th_myfunc_6_called <= 1;
          end 
          if(_th_myfunc_start[6] && (th_blink == 4)) begin
            _th_myfunc_6_tid_25 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[6]) begin
            th_myfunc_6 <= th_myfunc_6_1;
          end 
        end
        th_myfunc_6_1: begin
          _th_myfunc_6_tid_26 <= _th_myfunc_6_tid_25;
          th_myfunc_6 <= th_myfunc_6_2;
        end
        th_myfunc_6_2: begin
          _th_myfunc_6_step_27 <= 0;
          th_myfunc_6 <= th_myfunc_6_3;
        end
        th_myfunc_6_3: begin
          if(_th_myfunc_6_step_27 < 10) begin
            th_myfunc_6 <= th_myfunc_6_4;
          end else begin
            th_myfunc_6 <= th_myfunc_6_14;
          end
        end
        th_myfunc_6_4: begin
          _th_myfunc_6_i_28 <= 0;
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_5: begin
          if(_th_myfunc_6_i_28 < 20) begin
            th_myfunc_6 <= th_myfunc_6_6;
          end else begin
            th_myfunc_6 <= th_myfunc_6_7;
          end
        end
        th_myfunc_6_6: begin
          _th_myfunc_6_i_28 <= _th_myfunc_6_i_28 + 1;
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_8;
          end 
        end
        th_myfunc_6_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 6))) begin
            th_myfunc_6 <= th_myfunc_6_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_9;
          end 
        end
        th_myfunc_6_9: begin
          th_myfunc_6 <= th_myfunc_6_10;
        end
        th_myfunc_6_10: begin
          th_myfunc_6 <= th_myfunc_6_11;
        end
        th_myfunc_6_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_6 <= th_myfunc_6_12;
          end 
        end
        th_myfunc_6_12: begin
          $display("Thread %d Time %d", _th_myfunc_6_tid_26, clock_counter);
          th_myfunc_6 <= th_myfunc_6_13;
        end
        th_myfunc_6_13: begin
          _th_myfunc_6_step_27 <= _th_myfunc_6_step_27 + 1;
          th_myfunc_6 <= th_myfunc_6_3;
        end
      endcase
    end
  end

  localparam th_myfunc_7_1 = 1;
  localparam th_myfunc_7_2 = 2;
  localparam th_myfunc_7_3 = 3;
  localparam th_myfunc_7_4 = 4;
  localparam th_myfunc_7_5 = 5;
  localparam th_myfunc_7_6 = 6;
  localparam th_myfunc_7_7 = 7;
  localparam th_myfunc_7_8 = 8;
  localparam th_myfunc_7_9 = 9;
  localparam th_myfunc_7_10 = 10;
  localparam th_myfunc_7_11 = 11;
  localparam th_myfunc_7_12 = 12;
  localparam th_myfunc_7_13 = 13;
  localparam th_myfunc_7_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_7 <= th_myfunc_7_init;
      _th_myfunc_7_called <= 0;
      _th_myfunc_7_tid_29 <= 0;
      _th_myfunc_7_tid_30 <= 0;
      _th_myfunc_7_step_31 <= 0;
      _th_myfunc_7_i_32 <= 0;
    end else begin
      case(th_myfunc_7)
        th_myfunc_7_init: begin
          if(_th_myfunc_start[7] && (th_blink == 4)) begin
            _th_myfunc_7_called <= 1;
          end 
          if(_th_myfunc_start[7] && (th_blink == 4)) begin
            _th_myfunc_7_tid_29 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[7]) begin
            th_myfunc_7 <= th_myfunc_7_1;
          end 
        end
        th_myfunc_7_1: begin
          _th_myfunc_7_tid_30 <= _th_myfunc_7_tid_29;
          th_myfunc_7 <= th_myfunc_7_2;
        end
        th_myfunc_7_2: begin
          _th_myfunc_7_step_31 <= 0;
          th_myfunc_7 <= th_myfunc_7_3;
        end
        th_myfunc_7_3: begin
          if(_th_myfunc_7_step_31 < 10) begin
            th_myfunc_7 <= th_myfunc_7_4;
          end else begin
            th_myfunc_7 <= th_myfunc_7_14;
          end
        end
        th_myfunc_7_4: begin
          _th_myfunc_7_i_32 <= 0;
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_5: begin
          if(_th_myfunc_7_i_32 < 20) begin
            th_myfunc_7 <= th_myfunc_7_6;
          end else begin
            th_myfunc_7 <= th_myfunc_7_7;
          end
        end
        th_myfunc_7_6: begin
          _th_myfunc_7_i_32 <= _th_myfunc_7_i_32 + 1;
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_7: begin
          if(!__mybarrier_barrier_mutex_lock_reg || (__mybarrier_barrier_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_8;
          end 
        end
        th_myfunc_7_8: begin
          if(!(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 7))) begin
            th_myfunc_7 <= th_myfunc_7_7;
          end 
          if(__mybarrier_barrier_mutex_lock_reg && (__mybarrier_barrier_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_9;
          end 
        end
        th_myfunc_7_9: begin
          th_myfunc_7 <= th_myfunc_7_10;
        end
        th_myfunc_7_10: begin
          th_myfunc_7 <= th_myfunc_7_11;
        end
        th_myfunc_7_11: begin
          if(_mybarrier_barrier_done) begin
            th_myfunc_7 <= th_myfunc_7_12;
          end 
        end
        th_myfunc_7_12: begin
          $display("Thread %d Time %d", _th_myfunc_7_tid_30, clock_counter);
          th_myfunc_7 <= th_myfunc_7_13;
        end
        th_myfunc_7_13: begin
          _th_myfunc_7_step_31 <= _th_myfunc_7_step_31 + 1;
          th_myfunc_7 <= th_myfunc_7_3;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_barrier.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
