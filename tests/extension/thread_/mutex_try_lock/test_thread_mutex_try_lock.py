from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_mutex_try_lock

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

  reg _mymutex_lock_reg;
  reg [32-1:0] _mymutex_lock_id;
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
  reg _tmp_0;
  reg signed [32-1:0] _th_myfunc_0_lock_3;
  reg signed [32-1:0] _th_myfunc_0_waitcount_4;
  reg _tmp_1;
  reg signed [32-1:0] _th_myfunc_0_i_5;
  reg _th_myfunc_1_called;
  reg signed [32-1:0] _th_myfunc_1_tid_6;
  reg signed [32-1:0] _th_myfunc_1_tid_7;
  reg _tmp_2;
  reg signed [32-1:0] _th_myfunc_1_lock_8;
  reg signed [32-1:0] _th_myfunc_1_waitcount_9;
  reg _tmp_3;
  reg signed [32-1:0] _th_myfunc_1_i_10;
  reg _th_myfunc_2_called;
  reg signed [32-1:0] _th_myfunc_2_tid_11;
  reg signed [32-1:0] _th_myfunc_2_tid_12;
  reg _tmp_4;
  reg signed [32-1:0] _th_myfunc_2_lock_13;
  reg signed [32-1:0] _th_myfunc_2_waitcount_14;
  reg _tmp_5;
  reg signed [32-1:0] _th_myfunc_2_i_15;
  reg _th_myfunc_3_called;
  reg signed [32-1:0] _th_myfunc_3_tid_16;
  reg signed [32-1:0] _th_myfunc_3_tid_17;
  reg _tmp_6;
  reg signed [32-1:0] _th_myfunc_3_lock_18;
  reg signed [32-1:0] _th_myfunc_3_waitcount_19;
  reg _tmp_7;
  reg signed [32-1:0] _th_myfunc_3_i_20;
  reg _th_myfunc_4_called;
  reg signed [32-1:0] _th_myfunc_4_tid_21;
  reg signed [32-1:0] _th_myfunc_4_tid_22;
  reg _tmp_8;
  reg signed [32-1:0] _th_myfunc_4_lock_23;
  reg signed [32-1:0] _th_myfunc_4_waitcount_24;
  reg _tmp_9;
  reg signed [32-1:0] _th_myfunc_4_i_25;
  reg _th_myfunc_5_called;
  reg signed [32-1:0] _th_myfunc_5_tid_26;
  reg signed [32-1:0] _th_myfunc_5_tid_27;
  reg _tmp_10;
  reg signed [32-1:0] _th_myfunc_5_lock_28;
  reg signed [32-1:0] _th_myfunc_5_waitcount_29;
  reg _tmp_11;
  reg signed [32-1:0] _th_myfunc_5_i_30;
  reg _th_myfunc_6_called;
  reg signed [32-1:0] _th_myfunc_6_tid_31;
  reg signed [32-1:0] _th_myfunc_6_tid_32;
  reg _tmp_12;
  reg signed [32-1:0] _th_myfunc_6_lock_33;
  reg signed [32-1:0] _th_myfunc_6_waitcount_34;
  reg _tmp_13;
  reg signed [32-1:0] _th_myfunc_6_i_35;
  reg _th_myfunc_7_called;
  reg signed [32-1:0] _th_myfunc_7_tid_36;
  reg signed [32-1:0] _th_myfunc_7_tid_37;
  reg _tmp_14;
  reg signed [32-1:0] _th_myfunc_7_lock_38;
  reg signed [32-1:0] _th_myfunc_7_waitcount_39;
  reg _tmp_15;
  reg signed [32-1:0] _th_myfunc_7_i_40;

  always @(posedge CLK) begin
    if(RST) begin
      _mymutex_lock_reg <= 0;
      _mymutex_lock_id <= 0;
    end else begin
      if((th_myfunc_0 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 19) && (_mymutex_lock_id == 0)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_1 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 19) && (_mymutex_lock_id == 1)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_2 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 19) && (_mymutex_lock_id == 2)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_3 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 19) && (_mymutex_lock_id == 3)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_4 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 19) && (_mymutex_lock_id == 4)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_5 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 19) && (_mymutex_lock_id == 5)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_6 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 19) && (_mymutex_lock_id == 6)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_7 == 3) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 10) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 19) && (_mymutex_lock_id == 7)) begin
        _mymutex_lock_reg <= 0;
      end 
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
          if((_th_blink_tid_0 == 0)? th_myfunc_0 == 21 : 
          (_th_blink_tid_0 == 1)? th_myfunc_1 == 21 : 
          (_th_blink_tid_0 == 2)? th_myfunc_2 == 21 : 
          (_th_blink_tid_0 == 3)? th_myfunc_3 == 21 : 
          (_th_blink_tid_0 == 4)? th_myfunc_4 == 21 : 
          (_th_blink_tid_0 == 5)? th_myfunc_5 == 21 : 
          (_th_blink_tid_0 == 6)? th_myfunc_6 == 21 : 
          (_th_blink_tid_0 == 7)? th_myfunc_7 == 21 : 0) begin
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
  localparam th_myfunc_0_15 = 15;
  localparam th_myfunc_0_16 = 16;
  localparam th_myfunc_0_17 = 17;
  localparam th_myfunc_0_18 = 18;
  localparam th_myfunc_0_19 = 19;
  localparam th_myfunc_0_20 = 20;
  localparam th_myfunc_0_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_0 <= th_myfunc_0_init;
      _th_myfunc_0_called <= 0;
      _th_myfunc_0_tid_1 <= 0;
      _th_myfunc_0_tid_2 <= 0;
      _tmp_0 <= 0;
      _th_myfunc_0_lock_3 <= 0;
      _th_myfunc_0_waitcount_4 <= 0;
      _tmp_1 <= 0;
      _th_myfunc_0_i_5 <= 0;
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
          $display("-- Thread %d TryLock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_3;
        end
        th_myfunc_0_3: begin
          th_myfunc_0 <= th_myfunc_0_4;
        end
        th_myfunc_0_4: begin
          _tmp_0 <= _mymutex_lock_reg & (_mymutex_lock_id == 0);
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_5: begin
          _th_myfunc_0_lock_3 <= _tmp_0;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_6: begin
          _th_myfunc_0_waitcount_4 <= 0;
          th_myfunc_0 <= th_myfunc_0_7;
        end
        th_myfunc_0_7: begin
          if(!_th_myfunc_0_lock_3) begin
            th_myfunc_0 <= th_myfunc_0_8;
          end else begin
            th_myfunc_0 <= th_myfunc_0_14;
          end
        end
        th_myfunc_0_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_9;
        end
        th_myfunc_0_9: begin
          _th_myfunc_0_waitcount_4 <= _th_myfunc_0_waitcount_4 + 1;
          th_myfunc_0 <= th_myfunc_0_10;
        end
        th_myfunc_0_10: begin
          th_myfunc_0 <= th_myfunc_0_11;
        end
        th_myfunc_0_11: begin
          _tmp_1 <= _mymutex_lock_reg & (_mymutex_lock_id == 0);
          th_myfunc_0 <= th_myfunc_0_12;
        end
        th_myfunc_0_12: begin
          _th_myfunc_0_lock_3 <= _tmp_1;
          th_myfunc_0 <= th_myfunc_0_13;
        end
        th_myfunc_0_13: begin
          th_myfunc_0 <= th_myfunc_0_7;
        end
        th_myfunc_0_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_0_tid_2, _th_myfunc_0_waitcount_4);
          th_myfunc_0 <= th_myfunc_0_15;
        end
        th_myfunc_0_15: begin
          _th_myfunc_0_i_5 <= 0;
          th_myfunc_0 <= th_myfunc_0_16;
        end
        th_myfunc_0_16: begin
          if(_th_myfunc_0_i_5 < 20) begin
            th_myfunc_0 <= th_myfunc_0_17;
          end else begin
            th_myfunc_0 <= th_myfunc_0_18;
          end
        end
        th_myfunc_0_17: begin
          _th_myfunc_0_i_5 <= _th_myfunc_0_i_5 + 1;
          th_myfunc_0 <= th_myfunc_0_16;
        end
        th_myfunc_0_18: begin
          $display("Thread %d Hello", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_19;
        end
        th_myfunc_0_19: begin
          th_myfunc_0 <= th_myfunc_0_20;
        end
        th_myfunc_0_20: begin
          $display("Thread %d Unlock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_21;
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
  localparam th_myfunc_1_15 = 15;
  localparam th_myfunc_1_16 = 16;
  localparam th_myfunc_1_17 = 17;
  localparam th_myfunc_1_18 = 18;
  localparam th_myfunc_1_19 = 19;
  localparam th_myfunc_1_20 = 20;
  localparam th_myfunc_1_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_1 <= th_myfunc_1_init;
      _th_myfunc_1_called <= 0;
      _th_myfunc_1_tid_6 <= 0;
      _th_myfunc_1_tid_7 <= 0;
      _tmp_2 <= 0;
      _th_myfunc_1_lock_8 <= 0;
      _th_myfunc_1_waitcount_9 <= 0;
      _tmp_3 <= 0;
      _th_myfunc_1_i_10 <= 0;
    end else begin
      case(th_myfunc_1)
        th_myfunc_1_init: begin
          if(_th_myfunc_start[1] && (th_blink == 4)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(_th_myfunc_start[1] && (th_blink == 4)) begin
            _th_myfunc_1_tid_6 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_7 <= _th_myfunc_1_tid_6;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_1_tid_7);
          th_myfunc_1 <= th_myfunc_1_3;
        end
        th_myfunc_1_3: begin
          th_myfunc_1 <= th_myfunc_1_4;
        end
        th_myfunc_1_4: begin
          _tmp_2 <= _mymutex_lock_reg & (_mymutex_lock_id == 1);
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_5: begin
          _th_myfunc_1_lock_8 <= _tmp_2;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_6: begin
          _th_myfunc_1_waitcount_9 <= 0;
          th_myfunc_1 <= th_myfunc_1_7;
        end
        th_myfunc_1_7: begin
          if(!_th_myfunc_1_lock_8) begin
            th_myfunc_1 <= th_myfunc_1_8;
          end else begin
            th_myfunc_1 <= th_myfunc_1_14;
          end
        end
        th_myfunc_1_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_1_tid_7);
          th_myfunc_1 <= th_myfunc_1_9;
        end
        th_myfunc_1_9: begin
          _th_myfunc_1_waitcount_9 <= _th_myfunc_1_waitcount_9 + 1;
          th_myfunc_1 <= th_myfunc_1_10;
        end
        th_myfunc_1_10: begin
          th_myfunc_1 <= th_myfunc_1_11;
        end
        th_myfunc_1_11: begin
          _tmp_3 <= _mymutex_lock_reg & (_mymutex_lock_id == 1);
          th_myfunc_1 <= th_myfunc_1_12;
        end
        th_myfunc_1_12: begin
          _th_myfunc_1_lock_8 <= _tmp_3;
          th_myfunc_1 <= th_myfunc_1_13;
        end
        th_myfunc_1_13: begin
          th_myfunc_1 <= th_myfunc_1_7;
        end
        th_myfunc_1_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_1_tid_7, _th_myfunc_1_waitcount_9);
          th_myfunc_1 <= th_myfunc_1_15;
        end
        th_myfunc_1_15: begin
          _th_myfunc_1_i_10 <= 0;
          th_myfunc_1 <= th_myfunc_1_16;
        end
        th_myfunc_1_16: begin
          if(_th_myfunc_1_i_10 < 20) begin
            th_myfunc_1 <= th_myfunc_1_17;
          end else begin
            th_myfunc_1 <= th_myfunc_1_18;
          end
        end
        th_myfunc_1_17: begin
          _th_myfunc_1_i_10 <= _th_myfunc_1_i_10 + 1;
          th_myfunc_1 <= th_myfunc_1_16;
        end
        th_myfunc_1_18: begin
          $display("Thread %d Hello", _th_myfunc_1_tid_7);
          th_myfunc_1 <= th_myfunc_1_19;
        end
        th_myfunc_1_19: begin
          th_myfunc_1 <= th_myfunc_1_20;
        end
        th_myfunc_1_20: begin
          $display("Thread %d Unlock", _th_myfunc_1_tid_7);
          th_myfunc_1 <= th_myfunc_1_21;
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
  localparam th_myfunc_2_15 = 15;
  localparam th_myfunc_2_16 = 16;
  localparam th_myfunc_2_17 = 17;
  localparam th_myfunc_2_18 = 18;
  localparam th_myfunc_2_19 = 19;
  localparam th_myfunc_2_20 = 20;
  localparam th_myfunc_2_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_2 <= th_myfunc_2_init;
      _th_myfunc_2_called <= 0;
      _th_myfunc_2_tid_11 <= 0;
      _th_myfunc_2_tid_12 <= 0;
      _tmp_4 <= 0;
      _th_myfunc_2_lock_13 <= 0;
      _th_myfunc_2_waitcount_14 <= 0;
      _tmp_5 <= 0;
      _th_myfunc_2_i_15 <= 0;
    end else begin
      case(th_myfunc_2)
        th_myfunc_2_init: begin
          if(_th_myfunc_start[2] && (th_blink == 4)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(_th_myfunc_start[2] && (th_blink == 4)) begin
            _th_myfunc_2_tid_11 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_12 <= _th_myfunc_2_tid_11;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_2_tid_12);
          th_myfunc_2 <= th_myfunc_2_3;
        end
        th_myfunc_2_3: begin
          th_myfunc_2 <= th_myfunc_2_4;
        end
        th_myfunc_2_4: begin
          _tmp_4 <= _mymutex_lock_reg & (_mymutex_lock_id == 2);
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_5: begin
          _th_myfunc_2_lock_13 <= _tmp_4;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_6: begin
          _th_myfunc_2_waitcount_14 <= 0;
          th_myfunc_2 <= th_myfunc_2_7;
        end
        th_myfunc_2_7: begin
          if(!_th_myfunc_2_lock_13) begin
            th_myfunc_2 <= th_myfunc_2_8;
          end else begin
            th_myfunc_2 <= th_myfunc_2_14;
          end
        end
        th_myfunc_2_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_2_tid_12);
          th_myfunc_2 <= th_myfunc_2_9;
        end
        th_myfunc_2_9: begin
          _th_myfunc_2_waitcount_14 <= _th_myfunc_2_waitcount_14 + 1;
          th_myfunc_2 <= th_myfunc_2_10;
        end
        th_myfunc_2_10: begin
          th_myfunc_2 <= th_myfunc_2_11;
        end
        th_myfunc_2_11: begin
          _tmp_5 <= _mymutex_lock_reg & (_mymutex_lock_id == 2);
          th_myfunc_2 <= th_myfunc_2_12;
        end
        th_myfunc_2_12: begin
          _th_myfunc_2_lock_13 <= _tmp_5;
          th_myfunc_2 <= th_myfunc_2_13;
        end
        th_myfunc_2_13: begin
          th_myfunc_2 <= th_myfunc_2_7;
        end
        th_myfunc_2_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_2_tid_12, _th_myfunc_2_waitcount_14);
          th_myfunc_2 <= th_myfunc_2_15;
        end
        th_myfunc_2_15: begin
          _th_myfunc_2_i_15 <= 0;
          th_myfunc_2 <= th_myfunc_2_16;
        end
        th_myfunc_2_16: begin
          if(_th_myfunc_2_i_15 < 20) begin
            th_myfunc_2 <= th_myfunc_2_17;
          end else begin
            th_myfunc_2 <= th_myfunc_2_18;
          end
        end
        th_myfunc_2_17: begin
          _th_myfunc_2_i_15 <= _th_myfunc_2_i_15 + 1;
          th_myfunc_2 <= th_myfunc_2_16;
        end
        th_myfunc_2_18: begin
          $display("Thread %d Hello", _th_myfunc_2_tid_12);
          th_myfunc_2 <= th_myfunc_2_19;
        end
        th_myfunc_2_19: begin
          th_myfunc_2 <= th_myfunc_2_20;
        end
        th_myfunc_2_20: begin
          $display("Thread %d Unlock", _th_myfunc_2_tid_12);
          th_myfunc_2 <= th_myfunc_2_21;
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
  localparam th_myfunc_3_15 = 15;
  localparam th_myfunc_3_16 = 16;
  localparam th_myfunc_3_17 = 17;
  localparam th_myfunc_3_18 = 18;
  localparam th_myfunc_3_19 = 19;
  localparam th_myfunc_3_20 = 20;
  localparam th_myfunc_3_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_3 <= th_myfunc_3_init;
      _th_myfunc_3_called <= 0;
      _th_myfunc_3_tid_16 <= 0;
      _th_myfunc_3_tid_17 <= 0;
      _tmp_6 <= 0;
      _th_myfunc_3_lock_18 <= 0;
      _th_myfunc_3_waitcount_19 <= 0;
      _tmp_7 <= 0;
      _th_myfunc_3_i_20 <= 0;
    end else begin
      case(th_myfunc_3)
        th_myfunc_3_init: begin
          if(_th_myfunc_start[3] && (th_blink == 4)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(_th_myfunc_start[3] && (th_blink == 4)) begin
            _th_myfunc_3_tid_16 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_17 <= _th_myfunc_3_tid_16;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_3_tid_17);
          th_myfunc_3 <= th_myfunc_3_3;
        end
        th_myfunc_3_3: begin
          th_myfunc_3 <= th_myfunc_3_4;
        end
        th_myfunc_3_4: begin
          _tmp_6 <= _mymutex_lock_reg & (_mymutex_lock_id == 3);
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_5: begin
          _th_myfunc_3_lock_18 <= _tmp_6;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_6: begin
          _th_myfunc_3_waitcount_19 <= 0;
          th_myfunc_3 <= th_myfunc_3_7;
        end
        th_myfunc_3_7: begin
          if(!_th_myfunc_3_lock_18) begin
            th_myfunc_3 <= th_myfunc_3_8;
          end else begin
            th_myfunc_3 <= th_myfunc_3_14;
          end
        end
        th_myfunc_3_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_3_tid_17);
          th_myfunc_3 <= th_myfunc_3_9;
        end
        th_myfunc_3_9: begin
          _th_myfunc_3_waitcount_19 <= _th_myfunc_3_waitcount_19 + 1;
          th_myfunc_3 <= th_myfunc_3_10;
        end
        th_myfunc_3_10: begin
          th_myfunc_3 <= th_myfunc_3_11;
        end
        th_myfunc_3_11: begin
          _tmp_7 <= _mymutex_lock_reg & (_mymutex_lock_id == 3);
          th_myfunc_3 <= th_myfunc_3_12;
        end
        th_myfunc_3_12: begin
          _th_myfunc_3_lock_18 <= _tmp_7;
          th_myfunc_3 <= th_myfunc_3_13;
        end
        th_myfunc_3_13: begin
          th_myfunc_3 <= th_myfunc_3_7;
        end
        th_myfunc_3_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_3_tid_17, _th_myfunc_3_waitcount_19);
          th_myfunc_3 <= th_myfunc_3_15;
        end
        th_myfunc_3_15: begin
          _th_myfunc_3_i_20 <= 0;
          th_myfunc_3 <= th_myfunc_3_16;
        end
        th_myfunc_3_16: begin
          if(_th_myfunc_3_i_20 < 20) begin
            th_myfunc_3 <= th_myfunc_3_17;
          end else begin
            th_myfunc_3 <= th_myfunc_3_18;
          end
        end
        th_myfunc_3_17: begin
          _th_myfunc_3_i_20 <= _th_myfunc_3_i_20 + 1;
          th_myfunc_3 <= th_myfunc_3_16;
        end
        th_myfunc_3_18: begin
          $display("Thread %d Hello", _th_myfunc_3_tid_17);
          th_myfunc_3 <= th_myfunc_3_19;
        end
        th_myfunc_3_19: begin
          th_myfunc_3 <= th_myfunc_3_20;
        end
        th_myfunc_3_20: begin
          $display("Thread %d Unlock", _th_myfunc_3_tid_17);
          th_myfunc_3 <= th_myfunc_3_21;
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
  localparam th_myfunc_4_15 = 15;
  localparam th_myfunc_4_16 = 16;
  localparam th_myfunc_4_17 = 17;
  localparam th_myfunc_4_18 = 18;
  localparam th_myfunc_4_19 = 19;
  localparam th_myfunc_4_20 = 20;
  localparam th_myfunc_4_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_4 <= th_myfunc_4_init;
      _th_myfunc_4_called <= 0;
      _th_myfunc_4_tid_21 <= 0;
      _th_myfunc_4_tid_22 <= 0;
      _tmp_8 <= 0;
      _th_myfunc_4_lock_23 <= 0;
      _th_myfunc_4_waitcount_24 <= 0;
      _tmp_9 <= 0;
      _th_myfunc_4_i_25 <= 0;
    end else begin
      case(th_myfunc_4)
        th_myfunc_4_init: begin
          if(_th_myfunc_start[4] && (th_blink == 4)) begin
            _th_myfunc_4_called <= 1;
          end 
          if(_th_myfunc_start[4] && (th_blink == 4)) begin
            _th_myfunc_4_tid_21 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[4]) begin
            th_myfunc_4 <= th_myfunc_4_1;
          end 
        end
        th_myfunc_4_1: begin
          _th_myfunc_4_tid_22 <= _th_myfunc_4_tid_21;
          th_myfunc_4 <= th_myfunc_4_2;
        end
        th_myfunc_4_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_4_tid_22);
          th_myfunc_4 <= th_myfunc_4_3;
        end
        th_myfunc_4_3: begin
          th_myfunc_4 <= th_myfunc_4_4;
        end
        th_myfunc_4_4: begin
          _tmp_8 <= _mymutex_lock_reg & (_mymutex_lock_id == 4);
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_5: begin
          _th_myfunc_4_lock_23 <= _tmp_8;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_6: begin
          _th_myfunc_4_waitcount_24 <= 0;
          th_myfunc_4 <= th_myfunc_4_7;
        end
        th_myfunc_4_7: begin
          if(!_th_myfunc_4_lock_23) begin
            th_myfunc_4 <= th_myfunc_4_8;
          end else begin
            th_myfunc_4 <= th_myfunc_4_14;
          end
        end
        th_myfunc_4_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_4_tid_22);
          th_myfunc_4 <= th_myfunc_4_9;
        end
        th_myfunc_4_9: begin
          _th_myfunc_4_waitcount_24 <= _th_myfunc_4_waitcount_24 + 1;
          th_myfunc_4 <= th_myfunc_4_10;
        end
        th_myfunc_4_10: begin
          th_myfunc_4 <= th_myfunc_4_11;
        end
        th_myfunc_4_11: begin
          _tmp_9 <= _mymutex_lock_reg & (_mymutex_lock_id == 4);
          th_myfunc_4 <= th_myfunc_4_12;
        end
        th_myfunc_4_12: begin
          _th_myfunc_4_lock_23 <= _tmp_9;
          th_myfunc_4 <= th_myfunc_4_13;
        end
        th_myfunc_4_13: begin
          th_myfunc_4 <= th_myfunc_4_7;
        end
        th_myfunc_4_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_4_tid_22, _th_myfunc_4_waitcount_24);
          th_myfunc_4 <= th_myfunc_4_15;
        end
        th_myfunc_4_15: begin
          _th_myfunc_4_i_25 <= 0;
          th_myfunc_4 <= th_myfunc_4_16;
        end
        th_myfunc_4_16: begin
          if(_th_myfunc_4_i_25 < 20) begin
            th_myfunc_4 <= th_myfunc_4_17;
          end else begin
            th_myfunc_4 <= th_myfunc_4_18;
          end
        end
        th_myfunc_4_17: begin
          _th_myfunc_4_i_25 <= _th_myfunc_4_i_25 + 1;
          th_myfunc_4 <= th_myfunc_4_16;
        end
        th_myfunc_4_18: begin
          $display("Thread %d Hello", _th_myfunc_4_tid_22);
          th_myfunc_4 <= th_myfunc_4_19;
        end
        th_myfunc_4_19: begin
          th_myfunc_4 <= th_myfunc_4_20;
        end
        th_myfunc_4_20: begin
          $display("Thread %d Unlock", _th_myfunc_4_tid_22);
          th_myfunc_4 <= th_myfunc_4_21;
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
  localparam th_myfunc_5_15 = 15;
  localparam th_myfunc_5_16 = 16;
  localparam th_myfunc_5_17 = 17;
  localparam th_myfunc_5_18 = 18;
  localparam th_myfunc_5_19 = 19;
  localparam th_myfunc_5_20 = 20;
  localparam th_myfunc_5_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_5 <= th_myfunc_5_init;
      _th_myfunc_5_called <= 0;
      _th_myfunc_5_tid_26 <= 0;
      _th_myfunc_5_tid_27 <= 0;
      _tmp_10 <= 0;
      _th_myfunc_5_lock_28 <= 0;
      _th_myfunc_5_waitcount_29 <= 0;
      _tmp_11 <= 0;
      _th_myfunc_5_i_30 <= 0;
    end else begin
      case(th_myfunc_5)
        th_myfunc_5_init: begin
          if(_th_myfunc_start[5] && (th_blink == 4)) begin
            _th_myfunc_5_called <= 1;
          end 
          if(_th_myfunc_start[5] && (th_blink == 4)) begin
            _th_myfunc_5_tid_26 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[5]) begin
            th_myfunc_5 <= th_myfunc_5_1;
          end 
        end
        th_myfunc_5_1: begin
          _th_myfunc_5_tid_27 <= _th_myfunc_5_tid_26;
          th_myfunc_5 <= th_myfunc_5_2;
        end
        th_myfunc_5_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_5_tid_27);
          th_myfunc_5 <= th_myfunc_5_3;
        end
        th_myfunc_5_3: begin
          th_myfunc_5 <= th_myfunc_5_4;
        end
        th_myfunc_5_4: begin
          _tmp_10 <= _mymutex_lock_reg & (_mymutex_lock_id == 5);
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_5: begin
          _th_myfunc_5_lock_28 <= _tmp_10;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_6: begin
          _th_myfunc_5_waitcount_29 <= 0;
          th_myfunc_5 <= th_myfunc_5_7;
        end
        th_myfunc_5_7: begin
          if(!_th_myfunc_5_lock_28) begin
            th_myfunc_5 <= th_myfunc_5_8;
          end else begin
            th_myfunc_5 <= th_myfunc_5_14;
          end
        end
        th_myfunc_5_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_5_tid_27);
          th_myfunc_5 <= th_myfunc_5_9;
        end
        th_myfunc_5_9: begin
          _th_myfunc_5_waitcount_29 <= _th_myfunc_5_waitcount_29 + 1;
          th_myfunc_5 <= th_myfunc_5_10;
        end
        th_myfunc_5_10: begin
          th_myfunc_5 <= th_myfunc_5_11;
        end
        th_myfunc_5_11: begin
          _tmp_11 <= _mymutex_lock_reg & (_mymutex_lock_id == 5);
          th_myfunc_5 <= th_myfunc_5_12;
        end
        th_myfunc_5_12: begin
          _th_myfunc_5_lock_28 <= _tmp_11;
          th_myfunc_5 <= th_myfunc_5_13;
        end
        th_myfunc_5_13: begin
          th_myfunc_5 <= th_myfunc_5_7;
        end
        th_myfunc_5_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_5_tid_27, _th_myfunc_5_waitcount_29);
          th_myfunc_5 <= th_myfunc_5_15;
        end
        th_myfunc_5_15: begin
          _th_myfunc_5_i_30 <= 0;
          th_myfunc_5 <= th_myfunc_5_16;
        end
        th_myfunc_5_16: begin
          if(_th_myfunc_5_i_30 < 20) begin
            th_myfunc_5 <= th_myfunc_5_17;
          end else begin
            th_myfunc_5 <= th_myfunc_5_18;
          end
        end
        th_myfunc_5_17: begin
          _th_myfunc_5_i_30 <= _th_myfunc_5_i_30 + 1;
          th_myfunc_5 <= th_myfunc_5_16;
        end
        th_myfunc_5_18: begin
          $display("Thread %d Hello", _th_myfunc_5_tid_27);
          th_myfunc_5 <= th_myfunc_5_19;
        end
        th_myfunc_5_19: begin
          th_myfunc_5 <= th_myfunc_5_20;
        end
        th_myfunc_5_20: begin
          $display("Thread %d Unlock", _th_myfunc_5_tid_27);
          th_myfunc_5 <= th_myfunc_5_21;
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
  localparam th_myfunc_6_15 = 15;
  localparam th_myfunc_6_16 = 16;
  localparam th_myfunc_6_17 = 17;
  localparam th_myfunc_6_18 = 18;
  localparam th_myfunc_6_19 = 19;
  localparam th_myfunc_6_20 = 20;
  localparam th_myfunc_6_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_6 <= th_myfunc_6_init;
      _th_myfunc_6_called <= 0;
      _th_myfunc_6_tid_31 <= 0;
      _th_myfunc_6_tid_32 <= 0;
      _tmp_12 <= 0;
      _th_myfunc_6_lock_33 <= 0;
      _th_myfunc_6_waitcount_34 <= 0;
      _tmp_13 <= 0;
      _th_myfunc_6_i_35 <= 0;
    end else begin
      case(th_myfunc_6)
        th_myfunc_6_init: begin
          if(_th_myfunc_start[6] && (th_blink == 4)) begin
            _th_myfunc_6_called <= 1;
          end 
          if(_th_myfunc_start[6] && (th_blink == 4)) begin
            _th_myfunc_6_tid_31 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[6]) begin
            th_myfunc_6 <= th_myfunc_6_1;
          end 
        end
        th_myfunc_6_1: begin
          _th_myfunc_6_tid_32 <= _th_myfunc_6_tid_31;
          th_myfunc_6 <= th_myfunc_6_2;
        end
        th_myfunc_6_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_6_tid_32);
          th_myfunc_6 <= th_myfunc_6_3;
        end
        th_myfunc_6_3: begin
          th_myfunc_6 <= th_myfunc_6_4;
        end
        th_myfunc_6_4: begin
          _tmp_12 <= _mymutex_lock_reg & (_mymutex_lock_id == 6);
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_5: begin
          _th_myfunc_6_lock_33 <= _tmp_12;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_6: begin
          _th_myfunc_6_waitcount_34 <= 0;
          th_myfunc_6 <= th_myfunc_6_7;
        end
        th_myfunc_6_7: begin
          if(!_th_myfunc_6_lock_33) begin
            th_myfunc_6 <= th_myfunc_6_8;
          end else begin
            th_myfunc_6 <= th_myfunc_6_14;
          end
        end
        th_myfunc_6_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_6_tid_32);
          th_myfunc_6 <= th_myfunc_6_9;
        end
        th_myfunc_6_9: begin
          _th_myfunc_6_waitcount_34 <= _th_myfunc_6_waitcount_34 + 1;
          th_myfunc_6 <= th_myfunc_6_10;
        end
        th_myfunc_6_10: begin
          th_myfunc_6 <= th_myfunc_6_11;
        end
        th_myfunc_6_11: begin
          _tmp_13 <= _mymutex_lock_reg & (_mymutex_lock_id == 6);
          th_myfunc_6 <= th_myfunc_6_12;
        end
        th_myfunc_6_12: begin
          _th_myfunc_6_lock_33 <= _tmp_13;
          th_myfunc_6 <= th_myfunc_6_13;
        end
        th_myfunc_6_13: begin
          th_myfunc_6 <= th_myfunc_6_7;
        end
        th_myfunc_6_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_6_tid_32, _th_myfunc_6_waitcount_34);
          th_myfunc_6 <= th_myfunc_6_15;
        end
        th_myfunc_6_15: begin
          _th_myfunc_6_i_35 <= 0;
          th_myfunc_6 <= th_myfunc_6_16;
        end
        th_myfunc_6_16: begin
          if(_th_myfunc_6_i_35 < 20) begin
            th_myfunc_6 <= th_myfunc_6_17;
          end else begin
            th_myfunc_6 <= th_myfunc_6_18;
          end
        end
        th_myfunc_6_17: begin
          _th_myfunc_6_i_35 <= _th_myfunc_6_i_35 + 1;
          th_myfunc_6 <= th_myfunc_6_16;
        end
        th_myfunc_6_18: begin
          $display("Thread %d Hello", _th_myfunc_6_tid_32);
          th_myfunc_6 <= th_myfunc_6_19;
        end
        th_myfunc_6_19: begin
          th_myfunc_6 <= th_myfunc_6_20;
        end
        th_myfunc_6_20: begin
          $display("Thread %d Unlock", _th_myfunc_6_tid_32);
          th_myfunc_6 <= th_myfunc_6_21;
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
  localparam th_myfunc_7_15 = 15;
  localparam th_myfunc_7_16 = 16;
  localparam th_myfunc_7_17 = 17;
  localparam th_myfunc_7_18 = 18;
  localparam th_myfunc_7_19 = 19;
  localparam th_myfunc_7_20 = 20;
  localparam th_myfunc_7_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_7 <= th_myfunc_7_init;
      _th_myfunc_7_called <= 0;
      _th_myfunc_7_tid_36 <= 0;
      _th_myfunc_7_tid_37 <= 0;
      _tmp_14 <= 0;
      _th_myfunc_7_lock_38 <= 0;
      _th_myfunc_7_waitcount_39 <= 0;
      _tmp_15 <= 0;
      _th_myfunc_7_i_40 <= 0;
    end else begin
      case(th_myfunc_7)
        th_myfunc_7_init: begin
          if(_th_myfunc_start[7] && (th_blink == 4)) begin
            _th_myfunc_7_called <= 1;
          end 
          if(_th_myfunc_start[7] && (th_blink == 4)) begin
            _th_myfunc_7_tid_36 <= _th_blink_tid_0;
          end 
          if((th_blink == 4) && _th_myfunc_start[7]) begin
            th_myfunc_7 <= th_myfunc_7_1;
          end 
        end
        th_myfunc_7_1: begin
          _th_myfunc_7_tid_37 <= _th_myfunc_7_tid_36;
          th_myfunc_7 <= th_myfunc_7_2;
        end
        th_myfunc_7_2: begin
          $display("-- Thread %d TryLock", _th_myfunc_7_tid_37);
          th_myfunc_7 <= th_myfunc_7_3;
        end
        th_myfunc_7_3: begin
          th_myfunc_7 <= th_myfunc_7_4;
        end
        th_myfunc_7_4: begin
          _tmp_14 <= _mymutex_lock_reg & (_mymutex_lock_id == 7);
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_5: begin
          _th_myfunc_7_lock_38 <= _tmp_14;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_6: begin
          _th_myfunc_7_waitcount_39 <= 0;
          th_myfunc_7 <= th_myfunc_7_7;
        end
        th_myfunc_7_7: begin
          if(!_th_myfunc_7_lock_38) begin
            th_myfunc_7 <= th_myfunc_7_8;
          end else begin
            th_myfunc_7 <= th_myfunc_7_14;
          end
        end
        th_myfunc_7_8: begin
          $display("-- Thread %d TryLock", _th_myfunc_7_tid_37);
          th_myfunc_7 <= th_myfunc_7_9;
        end
        th_myfunc_7_9: begin
          _th_myfunc_7_waitcount_39 <= _th_myfunc_7_waitcount_39 + 1;
          th_myfunc_7 <= th_myfunc_7_10;
        end
        th_myfunc_7_10: begin
          th_myfunc_7 <= th_myfunc_7_11;
        end
        th_myfunc_7_11: begin
          _tmp_15 <= _mymutex_lock_reg & (_mymutex_lock_id == 7);
          th_myfunc_7 <= th_myfunc_7_12;
        end
        th_myfunc_7_12: begin
          _th_myfunc_7_lock_38 <= _tmp_15;
          th_myfunc_7 <= th_myfunc_7_13;
        end
        th_myfunc_7_13: begin
          th_myfunc_7 <= th_myfunc_7_7;
        end
        th_myfunc_7_14: begin
          $display("Thread %d Lock: waitcount=%d", _th_myfunc_7_tid_37, _th_myfunc_7_waitcount_39);
          th_myfunc_7 <= th_myfunc_7_15;
        end
        th_myfunc_7_15: begin
          _th_myfunc_7_i_40 <= 0;
          th_myfunc_7 <= th_myfunc_7_16;
        end
        th_myfunc_7_16: begin
          if(_th_myfunc_7_i_40 < 20) begin
            th_myfunc_7 <= th_myfunc_7_17;
          end else begin
            th_myfunc_7 <= th_myfunc_7_18;
          end
        end
        th_myfunc_7_17: begin
          _th_myfunc_7_i_40 <= _th_myfunc_7_i_40 + 1;
          th_myfunc_7 <= th_myfunc_7_16;
        end
        th_myfunc_7_18: begin
          $display("Thread %d Hello", _th_myfunc_7_tid_37);
          th_myfunc_7 <= th_myfunc_7_19;
        end
        th_myfunc_7_19: begin
          th_myfunc_7 <= th_myfunc_7_20;
        end
        th_myfunc_7_20: begin
          $display("Thread %d Unlock", _th_myfunc_7_tid_37);
          th_myfunc_7 <= th_myfunc_7_21;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_mutex_try_lock.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
