from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_mutex_shared_own

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

  reg [32-1:0] count;
  assign LED = count;
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
  reg __count_mutex_lock_reg;
  reg [32-1:0] __count_mutex_lock_id;
  reg signed [32-1:0] _th_myfunc_0_i_3;
  reg _th_myfunc_1_called;
  reg signed [32-1:0] _th_myfunc_1_tid_4;
  reg signed [32-1:0] _th_myfunc_1_tid_5;
  reg signed [32-1:0] _th_myfunc_1_i_6;
  reg _th_myfunc_2_called;
  reg signed [32-1:0] _th_myfunc_2_tid_7;
  reg signed [32-1:0] _th_myfunc_2_tid_8;
  reg signed [32-1:0] _th_myfunc_2_i_9;
  reg _th_myfunc_3_called;
  reg signed [32-1:0] _th_myfunc_3_tid_10;
  reg signed [32-1:0] _th_myfunc_3_tid_11;
  reg signed [32-1:0] _th_myfunc_3_i_12;
  reg _th_myfunc_4_called;
  reg signed [32-1:0] _th_myfunc_4_tid_13;
  reg signed [32-1:0] _th_myfunc_4_tid_14;
  reg signed [32-1:0] _th_myfunc_4_i_15;
  reg _th_myfunc_5_called;
  reg signed [32-1:0] _th_myfunc_5_tid_16;
  reg signed [32-1:0] _th_myfunc_5_tid_17;
  reg signed [32-1:0] _th_myfunc_5_i_18;
  reg _th_myfunc_6_called;
  reg signed [32-1:0] _th_myfunc_6_tid_19;
  reg signed [32-1:0] _th_myfunc_6_tid_20;
  reg signed [32-1:0] _th_myfunc_6_i_21;
  reg _th_myfunc_7_called;
  reg signed [32-1:0] _th_myfunc_7_tid_22;
  reg signed [32-1:0] _th_myfunc_7_tid_23;
  reg signed [32-1:0] _th_myfunc_7_i_24;

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
      _th_blink_tid_0 <= 0;
      _th_myfunc_start[_th_blink_tid_0] <= (0 >> _th_blink_tid_0) & 1'd1;
    end else begin
      case(th_blink)
        th_blink_init: begin
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_tid_0 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_tid_0 < 8) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_8;
          end
        end
        th_blink_4: begin
          _th_myfunc_start[_th_blink_tid_0] <= 1;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_myfunc_start[_th_blink_tid_0] <= 0;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_tid_0 <= _th_blink_tid_0 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_8: begin
          _th_blink_tid_0 <= 0;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          if(_th_blink_tid_0 < 8) begin
            th_blink <= th_blink_10;
          end else begin
            th_blink <= th_blink_12;
          end
        end
        th_blink_10: begin
          if((_th_blink_tid_0 == 0)? th_myfunc_0 == 12 : 
          (_th_blink_tid_0 == 1)? th_myfunc_1 == 12 : 
          (_th_blink_tid_0 == 2)? th_myfunc_2 == 12 : 
          (_th_blink_tid_0 == 3)? th_myfunc_3 == 12 : 
          (_th_blink_tid_0 == 4)? th_myfunc_4 == 12 : 
          (_th_blink_tid_0 == 5)? th_myfunc_5 == 12 : 
          (_th_blink_tid_0 == 6)? th_myfunc_6 == 12 : 
          (_th_blink_tid_0 == 7)? th_myfunc_7 == 12 : 0) begin
            th_blink <= th_blink_11;
          end 
        end
        th_blink_11: begin
          _th_blink_tid_0 <= _th_blink_tid_0 + 1;
          th_blink <= th_blink_9;
        end
        th_blink_12: begin
          $display("result count = %d", count);
          th_blink <= th_blink_13;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(th_blink == 1) begin
        count <= 0;
      end 
      if(th_myfunc_0 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_1 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_2 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_3 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_4 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_5 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_6 == 8) begin
        count <= count + 1;
      end 
      if(th_myfunc_7 == 8) begin
        count <= count + 1;
      end 
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_0 <= th_myfunc_0_init;
      _th_myfunc_0_called <= 0;
      _th_myfunc_0_tid_1 <= 0;
      _th_myfunc_0_tid_2 <= 0;
      _th_myfunc_0_i_3 <= 0;
    end else begin
      case(th_myfunc_0)
        th_myfunc_0_init: begin
          if(_th_myfunc_start[0] && (th_blink == 5)) begin
            _th_myfunc_0_called <= 1;
          end 
          if(_th_myfunc_start[0] && (th_blink == 5)) begin
            _th_myfunc_0_tid_1 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[0]) begin
            th_myfunc_0 <= th_myfunc_0_1;
          end 
        end
        th_myfunc_0_1: begin
          _th_myfunc_0_tid_2 <= _th_myfunc_0_tid_1;
          th_myfunc_0 <= th_myfunc_0_2;
        end
        th_myfunc_0_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_3;
          end 
        end
        th_myfunc_0_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 0))) begin
            th_myfunc_0 <= th_myfunc_0_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_4;
          end 
        end
        th_myfunc_0_4: begin
          $display("Thread %d Lock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_5: begin
          _th_myfunc_0_i_3 <= 0;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_6: begin
          if(_th_myfunc_0_i_3 < 20) begin
            th_myfunc_0 <= th_myfunc_0_7;
          end else begin
            th_myfunc_0 <= th_myfunc_0_8;
          end
        end
        th_myfunc_0_7: begin
          _th_myfunc_0_i_3 <= _th_myfunc_0_i_3 + 1;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_8: begin
          th_myfunc_0 <= th_myfunc_0_9;
        end
        th_myfunc_0_9: begin
          $display("Thread %d count = %d", _th_myfunc_0_tid_2, count);
          th_myfunc_0 <= th_myfunc_0_10;
        end
        th_myfunc_0_10: begin
          th_myfunc_0 <= th_myfunc_0_11;
        end
        th_myfunc_0_11: begin
          $display("Thread %d Unlock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_1 <= th_myfunc_1_init;
      _th_myfunc_1_called <= 0;
      _th_myfunc_1_tid_4 <= 0;
      _th_myfunc_1_tid_5 <= 0;
      _th_myfunc_1_i_6 <= 0;
    end else begin
      case(th_myfunc_1)
        th_myfunc_1_init: begin
          if(_th_myfunc_start[1] && (th_blink == 5)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(_th_myfunc_start[1] && (th_blink == 5)) begin
            _th_myfunc_1_tid_4 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_5 <= _th_myfunc_1_tid_4;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_3;
          end 
        end
        th_myfunc_1_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 1))) begin
            th_myfunc_1 <= th_myfunc_1_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_4;
          end 
        end
        th_myfunc_1_4: begin
          $display("Thread %d Lock", _th_myfunc_1_tid_5);
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_5: begin
          _th_myfunc_1_i_6 <= 0;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_6: begin
          if(_th_myfunc_1_i_6 < 20) begin
            th_myfunc_1 <= th_myfunc_1_7;
          end else begin
            th_myfunc_1 <= th_myfunc_1_8;
          end
        end
        th_myfunc_1_7: begin
          _th_myfunc_1_i_6 <= _th_myfunc_1_i_6 + 1;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_8: begin
          th_myfunc_1 <= th_myfunc_1_9;
        end
        th_myfunc_1_9: begin
          $display("Thread %d count = %d", _th_myfunc_1_tid_5, count);
          th_myfunc_1 <= th_myfunc_1_10;
        end
        th_myfunc_1_10: begin
          th_myfunc_1 <= th_myfunc_1_11;
        end
        th_myfunc_1_11: begin
          $display("Thread %d Unlock", _th_myfunc_1_tid_5);
          th_myfunc_1 <= th_myfunc_1_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_2 <= th_myfunc_2_init;
      _th_myfunc_2_called <= 0;
      _th_myfunc_2_tid_7 <= 0;
      _th_myfunc_2_tid_8 <= 0;
      _th_myfunc_2_i_9 <= 0;
    end else begin
      case(th_myfunc_2)
        th_myfunc_2_init: begin
          if(_th_myfunc_start[2] && (th_blink == 5)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(_th_myfunc_start[2] && (th_blink == 5)) begin
            _th_myfunc_2_tid_7 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_8 <= _th_myfunc_2_tid_7;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_3;
          end 
        end
        th_myfunc_2_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 2))) begin
            th_myfunc_2 <= th_myfunc_2_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_4;
          end 
        end
        th_myfunc_2_4: begin
          $display("Thread %d Lock", _th_myfunc_2_tid_8);
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_5: begin
          _th_myfunc_2_i_9 <= 0;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_6: begin
          if(_th_myfunc_2_i_9 < 20) begin
            th_myfunc_2 <= th_myfunc_2_7;
          end else begin
            th_myfunc_2 <= th_myfunc_2_8;
          end
        end
        th_myfunc_2_7: begin
          _th_myfunc_2_i_9 <= _th_myfunc_2_i_9 + 1;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_8: begin
          th_myfunc_2 <= th_myfunc_2_9;
        end
        th_myfunc_2_9: begin
          $display("Thread %d count = %d", _th_myfunc_2_tid_8, count);
          th_myfunc_2 <= th_myfunc_2_10;
        end
        th_myfunc_2_10: begin
          th_myfunc_2 <= th_myfunc_2_11;
        end
        th_myfunc_2_11: begin
          $display("Thread %d Unlock", _th_myfunc_2_tid_8);
          th_myfunc_2 <= th_myfunc_2_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_3 <= th_myfunc_3_init;
      _th_myfunc_3_called <= 0;
      _th_myfunc_3_tid_10 <= 0;
      _th_myfunc_3_tid_11 <= 0;
      _th_myfunc_3_i_12 <= 0;
    end else begin
      case(th_myfunc_3)
        th_myfunc_3_init: begin
          if(_th_myfunc_start[3] && (th_blink == 5)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(_th_myfunc_start[3] && (th_blink == 5)) begin
            _th_myfunc_3_tid_10 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_11 <= _th_myfunc_3_tid_10;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_3;
          end 
        end
        th_myfunc_3_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 3))) begin
            th_myfunc_3 <= th_myfunc_3_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_4;
          end 
        end
        th_myfunc_3_4: begin
          $display("Thread %d Lock", _th_myfunc_3_tid_11);
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_5: begin
          _th_myfunc_3_i_12 <= 0;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_6: begin
          if(_th_myfunc_3_i_12 < 20) begin
            th_myfunc_3 <= th_myfunc_3_7;
          end else begin
            th_myfunc_3 <= th_myfunc_3_8;
          end
        end
        th_myfunc_3_7: begin
          _th_myfunc_3_i_12 <= _th_myfunc_3_i_12 + 1;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_8: begin
          th_myfunc_3 <= th_myfunc_3_9;
        end
        th_myfunc_3_9: begin
          $display("Thread %d count = %d", _th_myfunc_3_tid_11, count);
          th_myfunc_3 <= th_myfunc_3_10;
        end
        th_myfunc_3_10: begin
          th_myfunc_3 <= th_myfunc_3_11;
        end
        th_myfunc_3_11: begin
          $display("Thread %d Unlock", _th_myfunc_3_tid_11);
          th_myfunc_3 <= th_myfunc_3_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_4 <= th_myfunc_4_init;
      _th_myfunc_4_called <= 0;
      _th_myfunc_4_tid_13 <= 0;
      _th_myfunc_4_tid_14 <= 0;
      _th_myfunc_4_i_15 <= 0;
    end else begin
      case(th_myfunc_4)
        th_myfunc_4_init: begin
          if(_th_myfunc_start[4] && (th_blink == 5)) begin
            _th_myfunc_4_called <= 1;
          end 
          if(_th_myfunc_start[4] && (th_blink == 5)) begin
            _th_myfunc_4_tid_13 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[4]) begin
            th_myfunc_4 <= th_myfunc_4_1;
          end 
        end
        th_myfunc_4_1: begin
          _th_myfunc_4_tid_14 <= _th_myfunc_4_tid_13;
          th_myfunc_4 <= th_myfunc_4_2;
        end
        th_myfunc_4_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_3;
          end 
        end
        th_myfunc_4_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 4))) begin
            th_myfunc_4 <= th_myfunc_4_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_4;
          end 
        end
        th_myfunc_4_4: begin
          $display("Thread %d Lock", _th_myfunc_4_tid_14);
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_5: begin
          _th_myfunc_4_i_15 <= 0;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_6: begin
          if(_th_myfunc_4_i_15 < 20) begin
            th_myfunc_4 <= th_myfunc_4_7;
          end else begin
            th_myfunc_4 <= th_myfunc_4_8;
          end
        end
        th_myfunc_4_7: begin
          _th_myfunc_4_i_15 <= _th_myfunc_4_i_15 + 1;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_8: begin
          th_myfunc_4 <= th_myfunc_4_9;
        end
        th_myfunc_4_9: begin
          $display("Thread %d count = %d", _th_myfunc_4_tid_14, count);
          th_myfunc_4 <= th_myfunc_4_10;
        end
        th_myfunc_4_10: begin
          th_myfunc_4 <= th_myfunc_4_11;
        end
        th_myfunc_4_11: begin
          $display("Thread %d Unlock", _th_myfunc_4_tid_14);
          th_myfunc_4 <= th_myfunc_4_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_5 <= th_myfunc_5_init;
      _th_myfunc_5_called <= 0;
      _th_myfunc_5_tid_16 <= 0;
      _th_myfunc_5_tid_17 <= 0;
      _th_myfunc_5_i_18 <= 0;
    end else begin
      case(th_myfunc_5)
        th_myfunc_5_init: begin
          if(_th_myfunc_start[5] && (th_blink == 5)) begin
            _th_myfunc_5_called <= 1;
          end 
          if(_th_myfunc_start[5] && (th_blink == 5)) begin
            _th_myfunc_5_tid_16 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[5]) begin
            th_myfunc_5 <= th_myfunc_5_1;
          end 
        end
        th_myfunc_5_1: begin
          _th_myfunc_5_tid_17 <= _th_myfunc_5_tid_16;
          th_myfunc_5 <= th_myfunc_5_2;
        end
        th_myfunc_5_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_3;
          end 
        end
        th_myfunc_5_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 5))) begin
            th_myfunc_5 <= th_myfunc_5_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_4;
          end 
        end
        th_myfunc_5_4: begin
          $display("Thread %d Lock", _th_myfunc_5_tid_17);
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_5: begin
          _th_myfunc_5_i_18 <= 0;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_6: begin
          if(_th_myfunc_5_i_18 < 20) begin
            th_myfunc_5 <= th_myfunc_5_7;
          end else begin
            th_myfunc_5 <= th_myfunc_5_8;
          end
        end
        th_myfunc_5_7: begin
          _th_myfunc_5_i_18 <= _th_myfunc_5_i_18 + 1;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_8: begin
          th_myfunc_5 <= th_myfunc_5_9;
        end
        th_myfunc_5_9: begin
          $display("Thread %d count = %d", _th_myfunc_5_tid_17, count);
          th_myfunc_5 <= th_myfunc_5_10;
        end
        th_myfunc_5_10: begin
          th_myfunc_5 <= th_myfunc_5_11;
        end
        th_myfunc_5_11: begin
          $display("Thread %d Unlock", _th_myfunc_5_tid_17);
          th_myfunc_5 <= th_myfunc_5_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_6 <= th_myfunc_6_init;
      _th_myfunc_6_called <= 0;
      _th_myfunc_6_tid_19 <= 0;
      _th_myfunc_6_tid_20 <= 0;
      _th_myfunc_6_i_21 <= 0;
    end else begin
      case(th_myfunc_6)
        th_myfunc_6_init: begin
          if(_th_myfunc_start[6] && (th_blink == 5)) begin
            _th_myfunc_6_called <= 1;
          end 
          if(_th_myfunc_start[6] && (th_blink == 5)) begin
            _th_myfunc_6_tid_19 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[6]) begin
            th_myfunc_6 <= th_myfunc_6_1;
          end 
        end
        th_myfunc_6_1: begin
          _th_myfunc_6_tid_20 <= _th_myfunc_6_tid_19;
          th_myfunc_6 <= th_myfunc_6_2;
        end
        th_myfunc_6_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_3;
          end 
        end
        th_myfunc_6_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 6))) begin
            th_myfunc_6 <= th_myfunc_6_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_4;
          end 
        end
        th_myfunc_6_4: begin
          $display("Thread %d Lock", _th_myfunc_6_tid_20);
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_5: begin
          _th_myfunc_6_i_21 <= 0;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_6: begin
          if(_th_myfunc_6_i_21 < 20) begin
            th_myfunc_6 <= th_myfunc_6_7;
          end else begin
            th_myfunc_6 <= th_myfunc_6_8;
          end
        end
        th_myfunc_6_7: begin
          _th_myfunc_6_i_21 <= _th_myfunc_6_i_21 + 1;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_8: begin
          th_myfunc_6 <= th_myfunc_6_9;
        end
        th_myfunc_6_9: begin
          $display("Thread %d count = %d", _th_myfunc_6_tid_20, count);
          th_myfunc_6 <= th_myfunc_6_10;
        end
        th_myfunc_6_10: begin
          th_myfunc_6 <= th_myfunc_6_11;
        end
        th_myfunc_6_11: begin
          $display("Thread %d Unlock", _th_myfunc_6_tid_20);
          th_myfunc_6 <= th_myfunc_6_12;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_7 <= th_myfunc_7_init;
      _th_myfunc_7_called <= 0;
      _th_myfunc_7_tid_22 <= 0;
      _th_myfunc_7_tid_23 <= 0;
      _th_myfunc_7_i_24 <= 0;
    end else begin
      case(th_myfunc_7)
        th_myfunc_7_init: begin
          if(_th_myfunc_start[7] && (th_blink == 5)) begin
            _th_myfunc_7_called <= 1;
          end 
          if(_th_myfunc_start[7] && (th_blink == 5)) begin
            _th_myfunc_7_tid_22 <= _th_blink_tid_0;
          end 
          if((th_blink == 5) && _th_myfunc_start[7]) begin
            th_myfunc_7 <= th_myfunc_7_1;
          end 
        end
        th_myfunc_7_1: begin
          _th_myfunc_7_tid_23 <= _th_myfunc_7_tid_22;
          th_myfunc_7 <= th_myfunc_7_2;
        end
        th_myfunc_7_2: begin
          if(!__count_mutex_lock_reg || (__count_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_3;
          end 
        end
        th_myfunc_7_3: begin
          if(!(__count_mutex_lock_reg && (__count_mutex_lock_id == 7))) begin
            th_myfunc_7 <= th_myfunc_7_2;
          end 
          if(__count_mutex_lock_reg && (__count_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_4;
          end 
        end
        th_myfunc_7_4: begin
          $display("Thread %d Lock", _th_myfunc_7_tid_23);
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_5: begin
          _th_myfunc_7_i_24 <= 0;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_6: begin
          if(_th_myfunc_7_i_24 < 20) begin
            th_myfunc_7 <= th_myfunc_7_7;
          end else begin
            th_myfunc_7 <= th_myfunc_7_8;
          end
        end
        th_myfunc_7_7: begin
          _th_myfunc_7_i_24 <= _th_myfunc_7_i_24 + 1;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_8: begin
          th_myfunc_7 <= th_myfunc_7_9;
        end
        th_myfunc_7_9: begin
          $display("Thread %d count = %d", _th_myfunc_7_tid_23, count);
          th_myfunc_7 <= th_myfunc_7_10;
        end
        th_myfunc_7_10: begin
          th_myfunc_7 <= th_myfunc_7_11;
        end
        th_myfunc_7_11: begin
          $display("Thread %d Unlock", _th_myfunc_7_tid_23);
          th_myfunc_7 <= th_myfunc_7_12;
        end
      endcase
    end
  end

  always @(posedge CLK) begin
    if(RST) begin
      __count_mutex_lock_reg <= 0;
      __count_mutex_lock_id <= 0;
    end else begin
      if((th_myfunc_0 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 10) && (__count_mutex_lock_id == 0)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_1 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 10) && (__count_mutex_lock_id == 1)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_2 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 10) && (__count_mutex_lock_id == 2)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_3 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 10) && (__count_mutex_lock_id == 3)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_4 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 10) && (__count_mutex_lock_id == 4)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_5 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 10) && (__count_mutex_lock_id == 5)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_6 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 10) && (__count_mutex_lock_id == 6)) begin
        __count_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_7 == 2) && !__count_mutex_lock_reg) begin
        __count_mutex_lock_reg <= 1;
        __count_mutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 10) && (__count_mutex_lock_id == 7)) begin
        __count_mutex_lock_reg <= 0;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_mutex_shared_own.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
