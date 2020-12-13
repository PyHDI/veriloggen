from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_fsm_as_module_mutex

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

  always @(posedge CLK) begin
    if(RST) begin
      _mymutex_lock_reg <= 0;
      _mymutex_lock_id <= 0;
    end else begin
      if((th_myfunc_0 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 9) && (_mymutex_lock_id == 0)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_1 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 9) && (_mymutex_lock_id == 1)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_2 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 9) && (_mymutex_lock_id == 2)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_3 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 9) && (_mymutex_lock_id == 3)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_4 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 9) && (_mymutex_lock_id == 4)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_5 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 9) && (_mymutex_lock_id == 5)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_6 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 9) && (_mymutex_lock_id == 6)) begin
        _mymutex_lock_reg <= 0;
      end 
      if((th_myfunc_7 == 2) && !_mymutex_lock_reg) begin
        _mymutex_lock_reg <= 1;
        _mymutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 9) && (_mymutex_lock_id == 7)) begin
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
          if((_th_blink_tid_0 == 0)? th_myfunc_0 == 11 : 
          (_th_blink_tid_0 == 1)? th_myfunc_1 == 11 : 
          (_th_blink_tid_0 == 2)? th_myfunc_2 == 11 : 
          (_th_blink_tid_0 == 3)? th_myfunc_3 == 11 : 
          (_th_blink_tid_0 == 4)? th_myfunc_4 == 11 : 
          (_th_blink_tid_0 == 5)? th_myfunc_5 == 11 : 
          (_th_blink_tid_0 == 6)? th_myfunc_6 == 11 : 
          (_th_blink_tid_0 == 7)? th_myfunc_7 == 11 : 0) begin
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
  wire [32-1:0] _th_myfunc_0_out_0;

  always @(*) begin
    th_myfunc_0 = _th_myfunc_0_out_0;
  end

  wire _th_myfunc_0__th_myfunc_0_called_1;

  always @(*) begin
    _th_myfunc_0_called = _th_myfunc_0__th_myfunc_0_called_1;
  end

  wire signed [32-1:0] _th_myfunc_0__th_myfunc_0_tid_1_2;

  always @(*) begin
    _th_myfunc_0_tid_1 = _th_myfunc_0__th_myfunc_0_tid_1_2;
  end

  wire signed [32-1:0] _th_myfunc_0__th_myfunc_0_tid_2_3;

  always @(*) begin
    _th_myfunc_0_tid_2 = _th_myfunc_0__th_myfunc_0_tid_2_3;
  end

  wire signed [32-1:0] _th_myfunc_0__th_myfunc_0_i_3_4;

  always @(*) begin
    _th_myfunc_0_i_3 = _th_myfunc_0__th_myfunc_0_i_3_4;
  end

  localparam _th_myfunc_0_th_blink_init = th_blink_init;

  sub_th_myfunc_0
  #(
    .th_blink_init(_th_myfunc_0_th_blink_init)
  )
  inst_sub_th_myfunc_0
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_0(_th_myfunc_0_out_0),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_0_tid_1(_th_myfunc_0_tid_1),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_0_tid_2(_th_myfunc_0_tid_2),
    .i__th_myfunc_0_i_3(_th_myfunc_0_i_3),
    ._th_myfunc_0_called(_th_myfunc_0__th_myfunc_0_called_1),
    ._th_myfunc_0_tid_1(_th_myfunc_0__th_myfunc_0_tid_1_2),
    ._th_myfunc_0_tid_2(_th_myfunc_0__th_myfunc_0_tid_2_3),
    ._th_myfunc_0_i_3(_th_myfunc_0__th_myfunc_0_i_3_4)
  );

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
  wire [32-1:0] _th_myfunc_1_out_5;

  always @(*) begin
    th_myfunc_1 = _th_myfunc_1_out_5;
  end

  wire _th_myfunc_1__th_myfunc_1_called_6;

  always @(*) begin
    _th_myfunc_1_called = _th_myfunc_1__th_myfunc_1_called_6;
  end

  wire signed [32-1:0] _th_myfunc_1__th_myfunc_1_tid_4_7;

  always @(*) begin
    _th_myfunc_1_tid_4 = _th_myfunc_1__th_myfunc_1_tid_4_7;
  end

  wire signed [32-1:0] _th_myfunc_1__th_myfunc_1_tid_5_8;

  always @(*) begin
    _th_myfunc_1_tid_5 = _th_myfunc_1__th_myfunc_1_tid_5_8;
  end

  wire signed [32-1:0] _th_myfunc_1__th_myfunc_1_i_6_9;

  always @(*) begin
    _th_myfunc_1_i_6 = _th_myfunc_1__th_myfunc_1_i_6_9;
  end

  localparam _th_myfunc_1_th_blink_init = th_blink_init;

  sub_th_myfunc_1
  #(
    .th_blink_init(_th_myfunc_1_th_blink_init)
  )
  inst_sub_th_myfunc_1
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_1(_th_myfunc_1_out_5),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_1_tid_4(_th_myfunc_1_tid_4),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_1_tid_5(_th_myfunc_1_tid_5),
    .i__th_myfunc_1_i_6(_th_myfunc_1_i_6),
    ._th_myfunc_1_called(_th_myfunc_1__th_myfunc_1_called_6),
    ._th_myfunc_1_tid_4(_th_myfunc_1__th_myfunc_1_tid_4_7),
    ._th_myfunc_1_tid_5(_th_myfunc_1__th_myfunc_1_tid_5_8),
    ._th_myfunc_1_i_6(_th_myfunc_1__th_myfunc_1_i_6_9)
  );

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
  wire [32-1:0] _th_myfunc_2_out_10;

  always @(*) begin
    th_myfunc_2 = _th_myfunc_2_out_10;
  end

  wire _th_myfunc_2__th_myfunc_2_called_11;

  always @(*) begin
    _th_myfunc_2_called = _th_myfunc_2__th_myfunc_2_called_11;
  end

  wire signed [32-1:0] _th_myfunc_2__th_myfunc_2_tid_7_12;

  always @(*) begin
    _th_myfunc_2_tid_7 = _th_myfunc_2__th_myfunc_2_tid_7_12;
  end

  wire signed [32-1:0] _th_myfunc_2__th_myfunc_2_tid_8_13;

  always @(*) begin
    _th_myfunc_2_tid_8 = _th_myfunc_2__th_myfunc_2_tid_8_13;
  end

  wire signed [32-1:0] _th_myfunc_2__th_myfunc_2_i_9_14;

  always @(*) begin
    _th_myfunc_2_i_9 = _th_myfunc_2__th_myfunc_2_i_9_14;
  end

  localparam _th_myfunc_2_th_blink_init = th_blink_init;

  sub_th_myfunc_2
  #(
    .th_blink_init(_th_myfunc_2_th_blink_init)
  )
  inst_sub_th_myfunc_2
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_2(_th_myfunc_2_out_10),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_2_tid_7(_th_myfunc_2_tid_7),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_2_tid_8(_th_myfunc_2_tid_8),
    .i__th_myfunc_2_i_9(_th_myfunc_2_i_9),
    ._th_myfunc_2_called(_th_myfunc_2__th_myfunc_2_called_11),
    ._th_myfunc_2_tid_7(_th_myfunc_2__th_myfunc_2_tid_7_12),
    ._th_myfunc_2_tid_8(_th_myfunc_2__th_myfunc_2_tid_8_13),
    ._th_myfunc_2_i_9(_th_myfunc_2__th_myfunc_2_i_9_14)
  );

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
  wire [32-1:0] _th_myfunc_3_out_15;

  always @(*) begin
    th_myfunc_3 = _th_myfunc_3_out_15;
  end

  wire _th_myfunc_3__th_myfunc_3_called_16;

  always @(*) begin
    _th_myfunc_3_called = _th_myfunc_3__th_myfunc_3_called_16;
  end

  wire signed [32-1:0] _th_myfunc_3__th_myfunc_3_tid_10_17;

  always @(*) begin
    _th_myfunc_3_tid_10 = _th_myfunc_3__th_myfunc_3_tid_10_17;
  end

  wire signed [32-1:0] _th_myfunc_3__th_myfunc_3_tid_11_18;

  always @(*) begin
    _th_myfunc_3_tid_11 = _th_myfunc_3__th_myfunc_3_tid_11_18;
  end

  wire signed [32-1:0] _th_myfunc_3__th_myfunc_3_i_12_19;

  always @(*) begin
    _th_myfunc_3_i_12 = _th_myfunc_3__th_myfunc_3_i_12_19;
  end

  localparam _th_myfunc_3_th_blink_init = th_blink_init;

  sub_th_myfunc_3
  #(
    .th_blink_init(_th_myfunc_3_th_blink_init)
  )
  inst_sub_th_myfunc_3
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_3(_th_myfunc_3_out_15),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_3_tid_10(_th_myfunc_3_tid_10),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_3_tid_11(_th_myfunc_3_tid_11),
    .i__th_myfunc_3_i_12(_th_myfunc_3_i_12),
    ._th_myfunc_3_called(_th_myfunc_3__th_myfunc_3_called_16),
    ._th_myfunc_3_tid_10(_th_myfunc_3__th_myfunc_3_tid_10_17),
    ._th_myfunc_3_tid_11(_th_myfunc_3__th_myfunc_3_tid_11_18),
    ._th_myfunc_3_i_12(_th_myfunc_3__th_myfunc_3_i_12_19)
  );

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
  wire [32-1:0] _th_myfunc_4_out_20;

  always @(*) begin
    th_myfunc_4 = _th_myfunc_4_out_20;
  end

  wire _th_myfunc_4__th_myfunc_4_called_21;

  always @(*) begin
    _th_myfunc_4_called = _th_myfunc_4__th_myfunc_4_called_21;
  end

  wire signed [32-1:0] _th_myfunc_4__th_myfunc_4_tid_13_22;

  always @(*) begin
    _th_myfunc_4_tid_13 = _th_myfunc_4__th_myfunc_4_tid_13_22;
  end

  wire signed [32-1:0] _th_myfunc_4__th_myfunc_4_tid_14_23;

  always @(*) begin
    _th_myfunc_4_tid_14 = _th_myfunc_4__th_myfunc_4_tid_14_23;
  end

  wire signed [32-1:0] _th_myfunc_4__th_myfunc_4_i_15_24;

  always @(*) begin
    _th_myfunc_4_i_15 = _th_myfunc_4__th_myfunc_4_i_15_24;
  end

  localparam _th_myfunc_4_th_blink_init = th_blink_init;

  sub_th_myfunc_4
  #(
    .th_blink_init(_th_myfunc_4_th_blink_init)
  )
  inst_sub_th_myfunc_4
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_4(_th_myfunc_4_out_20),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_4_tid_13(_th_myfunc_4_tid_13),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_4_tid_14(_th_myfunc_4_tid_14),
    .i__th_myfunc_4_i_15(_th_myfunc_4_i_15),
    ._th_myfunc_4_called(_th_myfunc_4__th_myfunc_4_called_21),
    ._th_myfunc_4_tid_13(_th_myfunc_4__th_myfunc_4_tid_13_22),
    ._th_myfunc_4_tid_14(_th_myfunc_4__th_myfunc_4_tid_14_23),
    ._th_myfunc_4_i_15(_th_myfunc_4__th_myfunc_4_i_15_24)
  );

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
  wire [32-1:0] _th_myfunc_5_out_25;

  always @(*) begin
    th_myfunc_5 = _th_myfunc_5_out_25;
  end

  wire _th_myfunc_5__th_myfunc_5_called_26;

  always @(*) begin
    _th_myfunc_5_called = _th_myfunc_5__th_myfunc_5_called_26;
  end

  wire signed [32-1:0] _th_myfunc_5__th_myfunc_5_tid_16_27;

  always @(*) begin
    _th_myfunc_5_tid_16 = _th_myfunc_5__th_myfunc_5_tid_16_27;
  end

  wire signed [32-1:0] _th_myfunc_5__th_myfunc_5_tid_17_28;

  always @(*) begin
    _th_myfunc_5_tid_17 = _th_myfunc_5__th_myfunc_5_tid_17_28;
  end

  wire signed [32-1:0] _th_myfunc_5__th_myfunc_5_i_18_29;

  always @(*) begin
    _th_myfunc_5_i_18 = _th_myfunc_5__th_myfunc_5_i_18_29;
  end

  localparam _th_myfunc_5_th_blink_init = th_blink_init;

  sub_th_myfunc_5
  #(
    .th_blink_init(_th_myfunc_5_th_blink_init)
  )
  inst_sub_th_myfunc_5
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_5(_th_myfunc_5_out_25),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_5_tid_16(_th_myfunc_5_tid_16),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_5_tid_17(_th_myfunc_5_tid_17),
    .i__th_myfunc_5_i_18(_th_myfunc_5_i_18),
    ._th_myfunc_5_called(_th_myfunc_5__th_myfunc_5_called_26),
    ._th_myfunc_5_tid_16(_th_myfunc_5__th_myfunc_5_tid_16_27),
    ._th_myfunc_5_tid_17(_th_myfunc_5__th_myfunc_5_tid_17_28),
    ._th_myfunc_5_i_18(_th_myfunc_5__th_myfunc_5_i_18_29)
  );

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
  wire [32-1:0] _th_myfunc_6_out_30;

  always @(*) begin
    th_myfunc_6 = _th_myfunc_6_out_30;
  end

  wire _th_myfunc_6__th_myfunc_6_called_31;

  always @(*) begin
    _th_myfunc_6_called = _th_myfunc_6__th_myfunc_6_called_31;
  end

  wire signed [32-1:0] _th_myfunc_6__th_myfunc_6_tid_19_32;

  always @(*) begin
    _th_myfunc_6_tid_19 = _th_myfunc_6__th_myfunc_6_tid_19_32;
  end

  wire signed [32-1:0] _th_myfunc_6__th_myfunc_6_tid_20_33;

  always @(*) begin
    _th_myfunc_6_tid_20 = _th_myfunc_6__th_myfunc_6_tid_20_33;
  end

  wire signed [32-1:0] _th_myfunc_6__th_myfunc_6_i_21_34;

  always @(*) begin
    _th_myfunc_6_i_21 = _th_myfunc_6__th_myfunc_6_i_21_34;
  end

  localparam _th_myfunc_6_th_blink_init = th_blink_init;

  sub_th_myfunc_6
  #(
    .th_blink_init(_th_myfunc_6_th_blink_init)
  )
  inst_sub_th_myfunc_6
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_6(_th_myfunc_6_out_30),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_6_tid_19(_th_myfunc_6_tid_19),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_6_tid_20(_th_myfunc_6_tid_20),
    .i__th_myfunc_6_i_21(_th_myfunc_6_i_21),
    ._th_myfunc_6_called(_th_myfunc_6__th_myfunc_6_called_31),
    ._th_myfunc_6_tid_19(_th_myfunc_6__th_myfunc_6_tid_19_32),
    ._th_myfunc_6_tid_20(_th_myfunc_6__th_myfunc_6_tid_20_33),
    ._th_myfunc_6_i_21(_th_myfunc_6__th_myfunc_6_i_21_34)
  );

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
  wire [32-1:0] _th_myfunc_7_out_35;

  always @(*) begin
    th_myfunc_7 = _th_myfunc_7_out_35;
  end

  wire _th_myfunc_7__th_myfunc_7_called_36;

  always @(*) begin
    _th_myfunc_7_called = _th_myfunc_7__th_myfunc_7_called_36;
  end

  wire signed [32-1:0] _th_myfunc_7__th_myfunc_7_tid_22_37;

  always @(*) begin
    _th_myfunc_7_tid_22 = _th_myfunc_7__th_myfunc_7_tid_22_37;
  end

  wire signed [32-1:0] _th_myfunc_7__th_myfunc_7_tid_23_38;

  always @(*) begin
    _th_myfunc_7_tid_23 = _th_myfunc_7__th_myfunc_7_tid_23_38;
  end

  wire signed [32-1:0] _th_myfunc_7__th_myfunc_7_i_24_39;

  always @(*) begin
    _th_myfunc_7_i_24 = _th_myfunc_7__th_myfunc_7_i_24_39;
  end

  localparam _th_myfunc_7_th_blink_init = th_blink_init;

  sub_th_myfunc_7
  #(
    .th_blink_init(_th_myfunc_7_th_blink_init)
  )
  inst_sub_th_myfunc_7
  (
    .CLK(CLK),
    .RST(RST),
    .th_myfunc_7(_th_myfunc_7_out_35),
    .i__th_myfunc_start(_th_myfunc_start),
    .i_th_blink(th_blink),
    .i__th_blink_tid_0(_th_blink_tid_0),
    .i__th_myfunc_7_tid_22(_th_myfunc_7_tid_22),
    .i__mymutex_lock_reg(_mymutex_lock_reg),
    .i__mymutex_lock_id(_mymutex_lock_id),
    .i__th_myfunc_7_tid_23(_th_myfunc_7_tid_23),
    .i__th_myfunc_7_i_24(_th_myfunc_7_i_24),
    ._th_myfunc_7_called(_th_myfunc_7__th_myfunc_7_called_36),
    ._th_myfunc_7_tid_22(_th_myfunc_7__th_myfunc_7_tid_22_37),
    ._th_myfunc_7_tid_23(_th_myfunc_7__th_myfunc_7_tid_23_38),
    ._th_myfunc_7_i_24(_th_myfunc_7__th_myfunc_7_i_24_39)
  );


endmodule



module sub_th_myfunc_0 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_0,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_0_tid_1,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_0_tid_2,
  input signed [32-1:0] i__th_myfunc_0_i_3,
  output reg _th_myfunc_0_called,
  output reg signed [32-1:0] _th_myfunc_0_tid_1,
  output reg signed [32-1:0] _th_myfunc_0_tid_2,
  output reg signed [32-1:0] _th_myfunc_0_i_3
);

  localparam th_myfunc_0_init = 0;
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
          if(i__th_myfunc_start[0] && (i_th_blink == 4)) begin
            _th_myfunc_0_called <= 1;
          end 
          if(i__th_myfunc_start[0] && (i_th_blink == 4)) begin
            _th_myfunc_0_tid_1 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[0]) begin
            th_myfunc_0 <= th_myfunc_0_1;
          end 
        end
        th_myfunc_0_1: begin
          _th_myfunc_0_tid_2 <= i__th_myfunc_0_tid_1;
          th_myfunc_0 <= th_myfunc_0_2;
        end
        th_myfunc_0_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_3;
          end 
        end
        th_myfunc_0_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 0))) begin
            th_myfunc_0 <= th_myfunc_0_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_4;
          end 
        end
        th_myfunc_0_4: begin
          $display("Thread %d Lock", i__th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_5: begin
          _th_myfunc_0_i_3 <= 0;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_6: begin
          if(i__th_myfunc_0_i_3 < 20) begin
            th_myfunc_0 <= th_myfunc_0_7;
          end else begin
            th_myfunc_0 <= th_myfunc_0_8;
          end
        end
        th_myfunc_0_7: begin
          _th_myfunc_0_i_3 <= i__th_myfunc_0_i_3 + 1;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_8: begin
          $display("Thread %d Hello", i__th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_9;
        end
        th_myfunc_0_9: begin
          th_myfunc_0 <= th_myfunc_0_10;
        end
        th_myfunc_0_10: begin
          $display("Thread %d Unlock", i__th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_1 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_1,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_1_tid_4,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_1_tid_5,
  input signed [32-1:0] i__th_myfunc_1_i_6,
  output reg _th_myfunc_1_called,
  output reg signed [32-1:0] _th_myfunc_1_tid_4,
  output reg signed [32-1:0] _th_myfunc_1_tid_5,
  output reg signed [32-1:0] _th_myfunc_1_i_6
);

  localparam th_myfunc_1_init = 0;
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
          if(i__th_myfunc_start[1] && (i_th_blink == 4)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(i__th_myfunc_start[1] && (i_th_blink == 4)) begin
            _th_myfunc_1_tid_4 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_5 <= i__th_myfunc_1_tid_4;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_3;
          end 
        end
        th_myfunc_1_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 1))) begin
            th_myfunc_1 <= th_myfunc_1_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_4;
          end 
        end
        th_myfunc_1_4: begin
          $display("Thread %d Lock", i__th_myfunc_1_tid_5);
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_5: begin
          _th_myfunc_1_i_6 <= 0;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_6: begin
          if(i__th_myfunc_1_i_6 < 20) begin
            th_myfunc_1 <= th_myfunc_1_7;
          end else begin
            th_myfunc_1 <= th_myfunc_1_8;
          end
        end
        th_myfunc_1_7: begin
          _th_myfunc_1_i_6 <= i__th_myfunc_1_i_6 + 1;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_8: begin
          $display("Thread %d Hello", i__th_myfunc_1_tid_5);
          th_myfunc_1 <= th_myfunc_1_9;
        end
        th_myfunc_1_9: begin
          th_myfunc_1 <= th_myfunc_1_10;
        end
        th_myfunc_1_10: begin
          $display("Thread %d Unlock", i__th_myfunc_1_tid_5);
          th_myfunc_1 <= th_myfunc_1_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_2 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_2,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_2_tid_7,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_2_tid_8,
  input signed [32-1:0] i__th_myfunc_2_i_9,
  output reg _th_myfunc_2_called,
  output reg signed [32-1:0] _th_myfunc_2_tid_7,
  output reg signed [32-1:0] _th_myfunc_2_tid_8,
  output reg signed [32-1:0] _th_myfunc_2_i_9
);

  localparam th_myfunc_2_init = 0;
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
          if(i__th_myfunc_start[2] && (i_th_blink == 4)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(i__th_myfunc_start[2] && (i_th_blink == 4)) begin
            _th_myfunc_2_tid_7 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_8 <= i__th_myfunc_2_tid_7;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_3;
          end 
        end
        th_myfunc_2_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 2))) begin
            th_myfunc_2 <= th_myfunc_2_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_4;
          end 
        end
        th_myfunc_2_4: begin
          $display("Thread %d Lock", i__th_myfunc_2_tid_8);
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_5: begin
          _th_myfunc_2_i_9 <= 0;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_6: begin
          if(i__th_myfunc_2_i_9 < 20) begin
            th_myfunc_2 <= th_myfunc_2_7;
          end else begin
            th_myfunc_2 <= th_myfunc_2_8;
          end
        end
        th_myfunc_2_7: begin
          _th_myfunc_2_i_9 <= i__th_myfunc_2_i_9 + 1;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_8: begin
          $display("Thread %d Hello", i__th_myfunc_2_tid_8);
          th_myfunc_2 <= th_myfunc_2_9;
        end
        th_myfunc_2_9: begin
          th_myfunc_2 <= th_myfunc_2_10;
        end
        th_myfunc_2_10: begin
          $display("Thread %d Unlock", i__th_myfunc_2_tid_8);
          th_myfunc_2 <= th_myfunc_2_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_3 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_3,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_3_tid_10,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_3_tid_11,
  input signed [32-1:0] i__th_myfunc_3_i_12,
  output reg _th_myfunc_3_called,
  output reg signed [32-1:0] _th_myfunc_3_tid_10,
  output reg signed [32-1:0] _th_myfunc_3_tid_11,
  output reg signed [32-1:0] _th_myfunc_3_i_12
);

  localparam th_myfunc_3_init = 0;
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
          if(i__th_myfunc_start[3] && (i_th_blink == 4)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(i__th_myfunc_start[3] && (i_th_blink == 4)) begin
            _th_myfunc_3_tid_10 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_11 <= i__th_myfunc_3_tid_10;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_3;
          end 
        end
        th_myfunc_3_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 3))) begin
            th_myfunc_3 <= th_myfunc_3_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_4;
          end 
        end
        th_myfunc_3_4: begin
          $display("Thread %d Lock", i__th_myfunc_3_tid_11);
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_5: begin
          _th_myfunc_3_i_12 <= 0;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_6: begin
          if(i__th_myfunc_3_i_12 < 20) begin
            th_myfunc_3 <= th_myfunc_3_7;
          end else begin
            th_myfunc_3 <= th_myfunc_3_8;
          end
        end
        th_myfunc_3_7: begin
          _th_myfunc_3_i_12 <= i__th_myfunc_3_i_12 + 1;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_8: begin
          $display("Thread %d Hello", i__th_myfunc_3_tid_11);
          th_myfunc_3 <= th_myfunc_3_9;
        end
        th_myfunc_3_9: begin
          th_myfunc_3 <= th_myfunc_3_10;
        end
        th_myfunc_3_10: begin
          $display("Thread %d Unlock", i__th_myfunc_3_tid_11);
          th_myfunc_3 <= th_myfunc_3_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_4 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_4,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_4_tid_13,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_4_tid_14,
  input signed [32-1:0] i__th_myfunc_4_i_15,
  output reg _th_myfunc_4_called,
  output reg signed [32-1:0] _th_myfunc_4_tid_13,
  output reg signed [32-1:0] _th_myfunc_4_tid_14,
  output reg signed [32-1:0] _th_myfunc_4_i_15
);

  localparam th_myfunc_4_init = 0;
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
          if(i__th_myfunc_start[4] && (i_th_blink == 4)) begin
            _th_myfunc_4_called <= 1;
          end 
          if(i__th_myfunc_start[4] && (i_th_blink == 4)) begin
            _th_myfunc_4_tid_13 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[4]) begin
            th_myfunc_4 <= th_myfunc_4_1;
          end 
        end
        th_myfunc_4_1: begin
          _th_myfunc_4_tid_14 <= i__th_myfunc_4_tid_13;
          th_myfunc_4 <= th_myfunc_4_2;
        end
        th_myfunc_4_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_3;
          end 
        end
        th_myfunc_4_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 4))) begin
            th_myfunc_4 <= th_myfunc_4_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_4;
          end 
        end
        th_myfunc_4_4: begin
          $display("Thread %d Lock", i__th_myfunc_4_tid_14);
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_5: begin
          _th_myfunc_4_i_15 <= 0;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_6: begin
          if(i__th_myfunc_4_i_15 < 20) begin
            th_myfunc_4 <= th_myfunc_4_7;
          end else begin
            th_myfunc_4 <= th_myfunc_4_8;
          end
        end
        th_myfunc_4_7: begin
          _th_myfunc_4_i_15 <= i__th_myfunc_4_i_15 + 1;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_8: begin
          $display("Thread %d Hello", i__th_myfunc_4_tid_14);
          th_myfunc_4 <= th_myfunc_4_9;
        end
        th_myfunc_4_9: begin
          th_myfunc_4 <= th_myfunc_4_10;
        end
        th_myfunc_4_10: begin
          $display("Thread %d Unlock", i__th_myfunc_4_tid_14);
          th_myfunc_4 <= th_myfunc_4_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_5 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_5,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_5_tid_16,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_5_tid_17,
  input signed [32-1:0] i__th_myfunc_5_i_18,
  output reg _th_myfunc_5_called,
  output reg signed [32-1:0] _th_myfunc_5_tid_16,
  output reg signed [32-1:0] _th_myfunc_5_tid_17,
  output reg signed [32-1:0] _th_myfunc_5_i_18
);

  localparam th_myfunc_5_init = 0;
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
          if(i__th_myfunc_start[5] && (i_th_blink == 4)) begin
            _th_myfunc_5_called <= 1;
          end 
          if(i__th_myfunc_start[5] && (i_th_blink == 4)) begin
            _th_myfunc_5_tid_16 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[5]) begin
            th_myfunc_5 <= th_myfunc_5_1;
          end 
        end
        th_myfunc_5_1: begin
          _th_myfunc_5_tid_17 <= i__th_myfunc_5_tid_16;
          th_myfunc_5 <= th_myfunc_5_2;
        end
        th_myfunc_5_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_3;
          end 
        end
        th_myfunc_5_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 5))) begin
            th_myfunc_5 <= th_myfunc_5_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_4;
          end 
        end
        th_myfunc_5_4: begin
          $display("Thread %d Lock", i__th_myfunc_5_tid_17);
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_5: begin
          _th_myfunc_5_i_18 <= 0;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_6: begin
          if(i__th_myfunc_5_i_18 < 20) begin
            th_myfunc_5 <= th_myfunc_5_7;
          end else begin
            th_myfunc_5 <= th_myfunc_5_8;
          end
        end
        th_myfunc_5_7: begin
          _th_myfunc_5_i_18 <= i__th_myfunc_5_i_18 + 1;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_8: begin
          $display("Thread %d Hello", i__th_myfunc_5_tid_17);
          th_myfunc_5 <= th_myfunc_5_9;
        end
        th_myfunc_5_9: begin
          th_myfunc_5 <= th_myfunc_5_10;
        end
        th_myfunc_5_10: begin
          $display("Thread %d Unlock", i__th_myfunc_5_tid_17);
          th_myfunc_5 <= th_myfunc_5_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_6 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_6,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_6_tid_19,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_6_tid_20,
  input signed [32-1:0] i__th_myfunc_6_i_21,
  output reg _th_myfunc_6_called,
  output reg signed [32-1:0] _th_myfunc_6_tid_19,
  output reg signed [32-1:0] _th_myfunc_6_tid_20,
  output reg signed [32-1:0] _th_myfunc_6_i_21
);

  localparam th_myfunc_6_init = 0;
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
          if(i__th_myfunc_start[6] && (i_th_blink == 4)) begin
            _th_myfunc_6_called <= 1;
          end 
          if(i__th_myfunc_start[6] && (i_th_blink == 4)) begin
            _th_myfunc_6_tid_19 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[6]) begin
            th_myfunc_6 <= th_myfunc_6_1;
          end 
        end
        th_myfunc_6_1: begin
          _th_myfunc_6_tid_20 <= i__th_myfunc_6_tid_19;
          th_myfunc_6 <= th_myfunc_6_2;
        end
        th_myfunc_6_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_3;
          end 
        end
        th_myfunc_6_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 6))) begin
            th_myfunc_6 <= th_myfunc_6_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_4;
          end 
        end
        th_myfunc_6_4: begin
          $display("Thread %d Lock", i__th_myfunc_6_tid_20);
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_5: begin
          _th_myfunc_6_i_21 <= 0;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_6: begin
          if(i__th_myfunc_6_i_21 < 20) begin
            th_myfunc_6 <= th_myfunc_6_7;
          end else begin
            th_myfunc_6 <= th_myfunc_6_8;
          end
        end
        th_myfunc_6_7: begin
          _th_myfunc_6_i_21 <= i__th_myfunc_6_i_21 + 1;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_8: begin
          $display("Thread %d Hello", i__th_myfunc_6_tid_20);
          th_myfunc_6 <= th_myfunc_6_9;
        end
        th_myfunc_6_9: begin
          th_myfunc_6 <= th_myfunc_6_10;
        end
        th_myfunc_6_10: begin
          $display("Thread %d Unlock", i__th_myfunc_6_tid_20);
          th_myfunc_6 <= th_myfunc_6_11;
        end
      endcase
    end
  end


endmodule



module sub_th_myfunc_7 #
(
  parameter th_blink_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] th_myfunc_7,
  input [8-1:0] i__th_myfunc_start,
  input [32-1:0] i_th_blink,
  input signed [32-1:0] i__th_blink_tid_0,
  input signed [32-1:0] i__th_myfunc_7_tid_22,
  input i__mymutex_lock_reg,
  input [32-1:0] i__mymutex_lock_id,
  input signed [32-1:0] i__th_myfunc_7_tid_23,
  input signed [32-1:0] i__th_myfunc_7_i_24,
  output reg _th_myfunc_7_called,
  output reg signed [32-1:0] _th_myfunc_7_tid_22,
  output reg signed [32-1:0] _th_myfunc_7_tid_23,
  output reg signed [32-1:0] _th_myfunc_7_i_24
);

  localparam th_myfunc_7_init = 0;
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
          if(i__th_myfunc_start[7] && (i_th_blink == 4)) begin
            _th_myfunc_7_called <= 1;
          end 
          if(i__th_myfunc_start[7] && (i_th_blink == 4)) begin
            _th_myfunc_7_tid_22 <= i__th_blink_tid_0;
          end 
          if((i_th_blink == 4) && i__th_myfunc_start[7]) begin
            th_myfunc_7 <= th_myfunc_7_1;
          end 
        end
        th_myfunc_7_1: begin
          _th_myfunc_7_tid_23 <= i__th_myfunc_7_tid_22;
          th_myfunc_7 <= th_myfunc_7_2;
        end
        th_myfunc_7_2: begin
          if(!i__mymutex_lock_reg || (i__mymutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_3;
          end 
        end
        th_myfunc_7_3: begin
          if(!(i__mymutex_lock_reg && (i__mymutex_lock_id == 7))) begin
            th_myfunc_7 <= th_myfunc_7_2;
          end 
          if(i__mymutex_lock_reg && (i__mymutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_4;
          end 
        end
        th_myfunc_7_4: begin
          $display("Thread %d Lock", i__th_myfunc_7_tid_23);
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_5: begin
          _th_myfunc_7_i_24 <= 0;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_6: begin
          if(i__th_myfunc_7_i_24 < 20) begin
            th_myfunc_7 <= th_myfunc_7_7;
          end else begin
            th_myfunc_7 <= th_myfunc_7_8;
          end
        end
        th_myfunc_7_7: begin
          _th_myfunc_7_i_24 <= i__th_myfunc_7_i_24 + 1;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_8: begin
          $display("Thread %d Hello", i__th_myfunc_7_tid_23);
          th_myfunc_7 <= th_myfunc_7_9;
        end
        th_myfunc_7_9: begin
          th_myfunc_7 <= th_myfunc_7_10;
        end
        th_myfunc_7_10: begin
          $display("Thread %d Unlock", i__th_myfunc_7_tid_23);
          th_myfunc_7 <= th_myfunc_7_11;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_fsm_as_module_mutex.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
