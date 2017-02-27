from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_fifo_multithread

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
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


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

  reg myfifo_enq;
  reg [32-1:0] myfifo_wdata;
  wire myfifo_full;
  wire myfifo_almost_full;
  reg myfifo_deq;
  wire [32-1:0] myfifo_rdata;
  wire myfifo_empty;
  wire myfifo_almost_empty;

  myfifo
  inst_myfifo
  (
    .CLK(CLK),
    .RST(RST),
    .myfifo_enq(myfifo_enq),
    .myfifo_wdata(myfifo_wdata),
    .myfifo_full(myfifo_full),
    .myfifo_almost_full(myfifo_almost_full),
    .myfifo_deq(myfifo_deq),
    .myfifo_rdata(myfifo_rdata),
    .myfifo_empty(myfifo_empty),
    .myfifo_almost_empty(myfifo_almost_empty)
  );

  reg [5-1:0] count_myfifo;
  reg [8-1:0] _th_myfunc_start;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg _myfifo_cond_0_1;
  reg _myfifo_cond_1_1;
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
  reg __myfifo_mutex_lock_reg;
  reg [32-1:0] __myfifo_mutex_lock_id;
  reg _tmp_0;
  reg _myfifo_cond_2_1;
  reg _myfifo_cond_3_1;
  reg _myfifo_cond_4_1;
  reg _myfifo_cond_4_2;
  reg signed [32-1:0] _tmp_1;
  reg signed [32-1:0] _th_myfunc_0_read_data_3;
  reg signed [32-1:0] _th_myfunc_0_write_data_4;
  reg _myfifo_cond_5_1;
  reg _tmp_2;
  reg _myfifo_cond_6_1;
  reg _myfifo_cond_7_1;
  reg _myfifo_cond_8_1;
  reg _myfifo_cond_8_2;
  reg signed [32-1:0] _tmp_3;
  reg _myfifo_cond_9_1;
  reg _th_myfunc_1_called;
  reg signed [32-1:0] _th_myfunc_1_tid_5;
  reg signed [32-1:0] _th_myfunc_1_tid_6;
  reg _tmp_4;
  reg _myfifo_cond_10_1;
  reg _myfifo_cond_11_1;
  reg _myfifo_cond_12_1;
  reg _myfifo_cond_12_2;
  reg signed [32-1:0] _tmp_5;
  reg signed [32-1:0] _th_myfunc_1_read_data_7;
  reg signed [32-1:0] _th_myfunc_1_write_data_8;
  reg _myfifo_cond_13_1;
  reg _tmp_6;
  reg _myfifo_cond_14_1;
  reg _myfifo_cond_15_1;
  reg _myfifo_cond_16_1;
  reg _myfifo_cond_16_2;
  reg signed [32-1:0] _tmp_7;
  reg _myfifo_cond_17_1;
  reg _th_myfunc_2_called;
  reg signed [32-1:0] _th_myfunc_2_tid_9;
  reg signed [32-1:0] _th_myfunc_2_tid_10;
  reg _tmp_8;
  reg _myfifo_cond_18_1;
  reg _myfifo_cond_19_1;
  reg _myfifo_cond_20_1;
  reg _myfifo_cond_20_2;
  reg signed [32-1:0] _tmp_9;
  reg signed [32-1:0] _th_myfunc_2_read_data_11;
  reg signed [32-1:0] _th_myfunc_2_write_data_12;
  reg _myfifo_cond_21_1;
  reg _tmp_10;
  reg _myfifo_cond_22_1;
  reg _myfifo_cond_23_1;
  reg _myfifo_cond_24_1;
  reg _myfifo_cond_24_2;
  reg signed [32-1:0] _tmp_11;
  reg _myfifo_cond_25_1;
  reg _th_myfunc_3_called;
  reg signed [32-1:0] _th_myfunc_3_tid_13;
  reg signed [32-1:0] _th_myfunc_3_tid_14;
  reg _tmp_12;
  reg _myfifo_cond_26_1;
  reg _myfifo_cond_27_1;
  reg _myfifo_cond_28_1;
  reg _myfifo_cond_28_2;
  reg signed [32-1:0] _tmp_13;
  reg signed [32-1:0] _th_myfunc_3_read_data_15;
  reg signed [32-1:0] _th_myfunc_3_write_data_16;
  reg _myfifo_cond_29_1;
  reg _tmp_14;
  reg _myfifo_cond_30_1;
  reg _myfifo_cond_31_1;
  reg _myfifo_cond_32_1;
  reg _myfifo_cond_32_2;
  reg signed [32-1:0] _tmp_15;
  reg _myfifo_cond_33_1;
  reg _th_myfunc_4_called;
  reg signed [32-1:0] _th_myfunc_4_tid_17;
  reg signed [32-1:0] _th_myfunc_4_tid_18;
  reg _tmp_16;
  reg _myfifo_cond_34_1;
  reg _myfifo_cond_35_1;
  reg _myfifo_cond_36_1;
  reg _myfifo_cond_36_2;
  reg signed [32-1:0] _tmp_17;
  reg signed [32-1:0] _th_myfunc_4_read_data_19;
  reg signed [32-1:0] _th_myfunc_4_write_data_20;
  reg _myfifo_cond_37_1;
  reg _tmp_18;
  reg _myfifo_cond_38_1;
  reg _myfifo_cond_39_1;
  reg _myfifo_cond_40_1;
  reg _myfifo_cond_40_2;
  reg signed [32-1:0] _tmp_19;
  reg _myfifo_cond_41_1;
  reg _th_myfunc_5_called;
  reg signed [32-1:0] _th_myfunc_5_tid_21;
  reg signed [32-1:0] _th_myfunc_5_tid_22;
  reg _tmp_20;
  reg _myfifo_cond_42_1;
  reg _myfifo_cond_43_1;
  reg _myfifo_cond_44_1;
  reg _myfifo_cond_44_2;
  reg signed [32-1:0] _tmp_21;
  reg signed [32-1:0] _th_myfunc_5_read_data_23;
  reg signed [32-1:0] _th_myfunc_5_write_data_24;
  reg _myfifo_cond_45_1;
  reg _tmp_22;
  reg _myfifo_cond_46_1;
  reg _myfifo_cond_47_1;
  reg _myfifo_cond_48_1;
  reg _myfifo_cond_48_2;
  reg signed [32-1:0] _tmp_23;
  reg _myfifo_cond_49_1;
  reg _th_myfunc_6_called;
  reg signed [32-1:0] _th_myfunc_6_tid_25;
  reg signed [32-1:0] _th_myfunc_6_tid_26;
  reg _tmp_24;
  reg _myfifo_cond_50_1;
  reg _myfifo_cond_51_1;
  reg _myfifo_cond_52_1;
  reg _myfifo_cond_52_2;
  reg signed [32-1:0] _tmp_25;
  reg signed [32-1:0] _th_myfunc_6_read_data_27;
  reg signed [32-1:0] _th_myfunc_6_write_data_28;
  reg _myfifo_cond_53_1;
  reg _tmp_26;
  reg _myfifo_cond_54_1;
  reg _myfifo_cond_55_1;
  reg _myfifo_cond_56_1;
  reg _myfifo_cond_56_2;
  reg signed [32-1:0] _tmp_27;
  reg _myfifo_cond_57_1;
  reg _th_myfunc_7_called;
  reg signed [32-1:0] _th_myfunc_7_tid_29;
  reg signed [32-1:0] _th_myfunc_7_tid_30;
  reg _tmp_28;
  reg _myfifo_cond_58_1;
  reg _myfifo_cond_59_1;
  reg _myfifo_cond_60_1;
  reg _myfifo_cond_60_2;
  reg signed [32-1:0] _tmp_29;
  reg signed [32-1:0] _th_myfunc_7_read_data_31;
  reg signed [32-1:0] _th_myfunc_7_write_data_32;
  reg _myfifo_cond_61_1;
  reg _tmp_30;
  reg _myfifo_cond_62_1;
  reg _myfifo_cond_63_1;
  reg _myfifo_cond_64_1;
  reg _myfifo_cond_64_2;
  reg signed [32-1:0] _tmp_31;
  reg _myfifo_cond_65_1;
  reg _tmp_32;
  reg _myfifo_cond_66_1;
  reg _myfifo_cond_67_1;
  reg _myfifo_cond_68_1;
  reg _myfifo_cond_68_2;
  reg signed [32-1:0] _tmp_33;
  reg signed [32-1:0] _th_blink_read_data_33;
  reg _tmp_34;
  reg _myfifo_cond_69_1;
  reg _myfifo_cond_70_1;
  reg _myfifo_cond_71_1;
  reg _myfifo_cond_71_2;
  reg signed [32-1:0] _tmp_35;

  always @(posedge CLK) begin
    if(RST) begin
      count_myfifo <= 0;
      myfifo_wdata <= 0;
      myfifo_enq <= 0;
      _myfifo_cond_0_1 <= 0;
      _myfifo_cond_1_1 <= 0;
      myfifo_deq <= 0;
      _myfifo_cond_2_1 <= 0;
      _tmp_0 <= 0;
      _myfifo_cond_3_1 <= 0;
      _myfifo_cond_4_1 <= 0;
      _myfifo_cond_4_2 <= 0;
      _myfifo_cond_5_1 <= 0;
      _myfifo_cond_6_1 <= 0;
      _tmp_2 <= 0;
      _myfifo_cond_7_1 <= 0;
      _myfifo_cond_8_1 <= 0;
      _myfifo_cond_8_2 <= 0;
      _myfifo_cond_9_1 <= 0;
      _myfifo_cond_10_1 <= 0;
      _tmp_4 <= 0;
      _myfifo_cond_11_1 <= 0;
      _myfifo_cond_12_1 <= 0;
      _myfifo_cond_12_2 <= 0;
      _myfifo_cond_13_1 <= 0;
      _myfifo_cond_14_1 <= 0;
      _tmp_6 <= 0;
      _myfifo_cond_15_1 <= 0;
      _myfifo_cond_16_1 <= 0;
      _myfifo_cond_16_2 <= 0;
      _myfifo_cond_17_1 <= 0;
      _myfifo_cond_18_1 <= 0;
      _tmp_8 <= 0;
      _myfifo_cond_19_1 <= 0;
      _myfifo_cond_20_1 <= 0;
      _myfifo_cond_20_2 <= 0;
      _myfifo_cond_21_1 <= 0;
      _myfifo_cond_22_1 <= 0;
      _tmp_10 <= 0;
      _myfifo_cond_23_1 <= 0;
      _myfifo_cond_24_1 <= 0;
      _myfifo_cond_24_2 <= 0;
      _myfifo_cond_25_1 <= 0;
      _myfifo_cond_26_1 <= 0;
      _tmp_12 <= 0;
      _myfifo_cond_27_1 <= 0;
      _myfifo_cond_28_1 <= 0;
      _myfifo_cond_28_2 <= 0;
      _myfifo_cond_29_1 <= 0;
      _myfifo_cond_30_1 <= 0;
      _tmp_14 <= 0;
      _myfifo_cond_31_1 <= 0;
      _myfifo_cond_32_1 <= 0;
      _myfifo_cond_32_2 <= 0;
      _myfifo_cond_33_1 <= 0;
      _myfifo_cond_34_1 <= 0;
      _tmp_16 <= 0;
      _myfifo_cond_35_1 <= 0;
      _myfifo_cond_36_1 <= 0;
      _myfifo_cond_36_2 <= 0;
      _myfifo_cond_37_1 <= 0;
      _myfifo_cond_38_1 <= 0;
      _tmp_18 <= 0;
      _myfifo_cond_39_1 <= 0;
      _myfifo_cond_40_1 <= 0;
      _myfifo_cond_40_2 <= 0;
      _myfifo_cond_41_1 <= 0;
      _myfifo_cond_42_1 <= 0;
      _tmp_20 <= 0;
      _myfifo_cond_43_1 <= 0;
      _myfifo_cond_44_1 <= 0;
      _myfifo_cond_44_2 <= 0;
      _myfifo_cond_45_1 <= 0;
      _myfifo_cond_46_1 <= 0;
      _tmp_22 <= 0;
      _myfifo_cond_47_1 <= 0;
      _myfifo_cond_48_1 <= 0;
      _myfifo_cond_48_2 <= 0;
      _myfifo_cond_49_1 <= 0;
      _myfifo_cond_50_1 <= 0;
      _tmp_24 <= 0;
      _myfifo_cond_51_1 <= 0;
      _myfifo_cond_52_1 <= 0;
      _myfifo_cond_52_2 <= 0;
      _myfifo_cond_53_1 <= 0;
      _myfifo_cond_54_1 <= 0;
      _tmp_26 <= 0;
      _myfifo_cond_55_1 <= 0;
      _myfifo_cond_56_1 <= 0;
      _myfifo_cond_56_2 <= 0;
      _myfifo_cond_57_1 <= 0;
      _myfifo_cond_58_1 <= 0;
      _tmp_28 <= 0;
      _myfifo_cond_59_1 <= 0;
      _myfifo_cond_60_1 <= 0;
      _myfifo_cond_60_2 <= 0;
      _myfifo_cond_61_1 <= 0;
      _myfifo_cond_62_1 <= 0;
      _tmp_30 <= 0;
      _myfifo_cond_63_1 <= 0;
      _myfifo_cond_64_1 <= 0;
      _myfifo_cond_64_2 <= 0;
      _myfifo_cond_65_1 <= 0;
      _myfifo_cond_66_1 <= 0;
      _tmp_32 <= 0;
      _myfifo_cond_67_1 <= 0;
      _myfifo_cond_68_1 <= 0;
      _myfifo_cond_68_2 <= 0;
      _myfifo_cond_69_1 <= 0;
      _tmp_34 <= 0;
      _myfifo_cond_70_1 <= 0;
      _myfifo_cond_71_1 <= 0;
      _myfifo_cond_71_2 <= 0;
    end else begin
      if(_myfifo_cond_4_2) begin
        _tmp_0 <= 0;
      end 
      if(_myfifo_cond_8_2) begin
        _tmp_2 <= 0;
      end 
      if(_myfifo_cond_12_2) begin
        _tmp_4 <= 0;
      end 
      if(_myfifo_cond_16_2) begin
        _tmp_6 <= 0;
      end 
      if(_myfifo_cond_20_2) begin
        _tmp_8 <= 0;
      end 
      if(_myfifo_cond_24_2) begin
        _tmp_10 <= 0;
      end 
      if(_myfifo_cond_28_2) begin
        _tmp_12 <= 0;
      end 
      if(_myfifo_cond_32_2) begin
        _tmp_14 <= 0;
      end 
      if(_myfifo_cond_36_2) begin
        _tmp_16 <= 0;
      end 
      if(_myfifo_cond_40_2) begin
        _tmp_18 <= 0;
      end 
      if(_myfifo_cond_44_2) begin
        _tmp_20 <= 0;
      end 
      if(_myfifo_cond_48_2) begin
        _tmp_22 <= 0;
      end 
      if(_myfifo_cond_52_2) begin
        _tmp_24 <= 0;
      end 
      if(_myfifo_cond_56_2) begin
        _tmp_26 <= 0;
      end 
      if(_myfifo_cond_60_2) begin
        _tmp_28 <= 0;
      end 
      if(_myfifo_cond_64_2) begin
        _tmp_30 <= 0;
      end 
      if(_myfifo_cond_68_2) begin
        _tmp_32 <= 0;
      end 
      if(_myfifo_cond_71_2) begin
        _tmp_34 <= 0;
      end 
      if(_myfifo_cond_0_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_1_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_2_1) begin
        _tmp_0 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_3_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_4_2 <= _myfifo_cond_4_1;
      if(_myfifo_cond_5_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_6_1) begin
        _tmp_2 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_7_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_8_2 <= _myfifo_cond_8_1;
      if(_myfifo_cond_9_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_10_1) begin
        _tmp_4 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_11_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_12_2 <= _myfifo_cond_12_1;
      if(_myfifo_cond_13_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_14_1) begin
        _tmp_6 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_15_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_16_2 <= _myfifo_cond_16_1;
      if(_myfifo_cond_17_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_18_1) begin
        _tmp_8 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_19_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_20_2 <= _myfifo_cond_20_1;
      if(_myfifo_cond_21_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_22_1) begin
        _tmp_10 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_23_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_24_2 <= _myfifo_cond_24_1;
      if(_myfifo_cond_25_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_26_1) begin
        _tmp_12 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_27_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_28_2 <= _myfifo_cond_28_1;
      if(_myfifo_cond_29_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_30_1) begin
        _tmp_14 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_31_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_32_2 <= _myfifo_cond_32_1;
      if(_myfifo_cond_33_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_34_1) begin
        _tmp_16 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_35_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_36_2 <= _myfifo_cond_36_1;
      if(_myfifo_cond_37_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_38_1) begin
        _tmp_18 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_39_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_40_2 <= _myfifo_cond_40_1;
      if(_myfifo_cond_41_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_42_1) begin
        _tmp_20 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_43_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_44_2 <= _myfifo_cond_44_1;
      if(_myfifo_cond_45_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_46_1) begin
        _tmp_22 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_47_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_48_2 <= _myfifo_cond_48_1;
      if(_myfifo_cond_49_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_50_1) begin
        _tmp_24 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_51_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_52_2 <= _myfifo_cond_52_1;
      if(_myfifo_cond_53_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_54_1) begin
        _tmp_26 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_55_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_56_2 <= _myfifo_cond_56_1;
      if(_myfifo_cond_57_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_58_1) begin
        _tmp_28 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_59_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_60_2 <= _myfifo_cond_60_1;
      if(_myfifo_cond_61_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_62_1) begin
        _tmp_30 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_63_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_64_2 <= _myfifo_cond_64_1;
      if(_myfifo_cond_65_1) begin
        myfifo_enq <= 0;
      end 
      if(_myfifo_cond_66_1) begin
        _tmp_32 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_67_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_68_2 <= _myfifo_cond_68_1;
      if(_myfifo_cond_69_1) begin
        _tmp_34 <= !myfifo_empty && myfifo_deq;
      end 
      if(_myfifo_cond_70_1) begin
        myfifo_deq <= 0;
      end 
      _myfifo_cond_71_2 <= _myfifo_cond_71_1;
      if(myfifo_enq && !myfifo_full && (myfifo_deq && !myfifo_empty)) begin
        count_myfifo <= count_myfifo;
      end else if(myfifo_enq && !myfifo_full) begin
        count_myfifo <= count_myfifo + 1;
      end else if(myfifo_deq && !myfifo_empty) begin
        count_myfifo <= count_myfifo - 1;
      end 
      if((th_blink == 1) && !myfifo_full) begin
        myfifo_wdata <= 100;
      end 
      if((th_blink == 1) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_0_1 <= 1;
      if((th_blink == 2) && !myfifo_full) begin
        myfifo_wdata <= 200;
      end 
      if((th_blink == 2) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_1_1 <= 1;
      if(th_myfunc_0 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_2_1 <= th_myfunc_0 == 5;
      _myfifo_cond_3_1 <= 1;
      _myfifo_cond_4_1 <= 1;
      if((th_myfunc_0 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_0_write_data_4;
      end 
      if((th_myfunc_0 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_5_1 <= 1;
      if(th_myfunc_0 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_6_1 <= th_myfunc_0 == 13;
      _myfifo_cond_7_1 <= 1;
      _myfifo_cond_8_1 <= 1;
      if((th_myfunc_0 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_0_write_data_4;
      end 
      if((th_myfunc_0 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_9_1 <= 1;
      if(th_myfunc_1 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_10_1 <= th_myfunc_1 == 5;
      _myfifo_cond_11_1 <= 1;
      _myfifo_cond_12_1 <= 1;
      if((th_myfunc_1 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_1_write_data_8;
      end 
      if((th_myfunc_1 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_13_1 <= 1;
      if(th_myfunc_1 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_14_1 <= th_myfunc_1 == 13;
      _myfifo_cond_15_1 <= 1;
      _myfifo_cond_16_1 <= 1;
      if((th_myfunc_1 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_1_write_data_8;
      end 
      if((th_myfunc_1 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_17_1 <= 1;
      if(th_myfunc_2 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_18_1 <= th_myfunc_2 == 5;
      _myfifo_cond_19_1 <= 1;
      _myfifo_cond_20_1 <= 1;
      if((th_myfunc_2 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_2_write_data_12;
      end 
      if((th_myfunc_2 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_21_1 <= 1;
      if(th_myfunc_2 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_22_1 <= th_myfunc_2 == 13;
      _myfifo_cond_23_1 <= 1;
      _myfifo_cond_24_1 <= 1;
      if((th_myfunc_2 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_2_write_data_12;
      end 
      if((th_myfunc_2 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_25_1 <= 1;
      if(th_myfunc_3 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_26_1 <= th_myfunc_3 == 5;
      _myfifo_cond_27_1 <= 1;
      _myfifo_cond_28_1 <= 1;
      if((th_myfunc_3 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_3_write_data_16;
      end 
      if((th_myfunc_3 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_29_1 <= 1;
      if(th_myfunc_3 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_30_1 <= th_myfunc_3 == 13;
      _myfifo_cond_31_1 <= 1;
      _myfifo_cond_32_1 <= 1;
      if((th_myfunc_3 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_3_write_data_16;
      end 
      if((th_myfunc_3 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_33_1 <= 1;
      if(th_myfunc_4 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_34_1 <= th_myfunc_4 == 5;
      _myfifo_cond_35_1 <= 1;
      _myfifo_cond_36_1 <= 1;
      if((th_myfunc_4 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_4_write_data_20;
      end 
      if((th_myfunc_4 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_37_1 <= 1;
      if(th_myfunc_4 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_38_1 <= th_myfunc_4 == 13;
      _myfifo_cond_39_1 <= 1;
      _myfifo_cond_40_1 <= 1;
      if((th_myfunc_4 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_4_write_data_20;
      end 
      if((th_myfunc_4 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_41_1 <= 1;
      if(th_myfunc_5 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_42_1 <= th_myfunc_5 == 5;
      _myfifo_cond_43_1 <= 1;
      _myfifo_cond_44_1 <= 1;
      if((th_myfunc_5 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_5_write_data_24;
      end 
      if((th_myfunc_5 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_45_1 <= 1;
      if(th_myfunc_5 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_46_1 <= th_myfunc_5 == 13;
      _myfifo_cond_47_1 <= 1;
      _myfifo_cond_48_1 <= 1;
      if((th_myfunc_5 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_5_write_data_24;
      end 
      if((th_myfunc_5 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_49_1 <= 1;
      if(th_myfunc_6 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_50_1 <= th_myfunc_6 == 5;
      _myfifo_cond_51_1 <= 1;
      _myfifo_cond_52_1 <= 1;
      if((th_myfunc_6 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_6_write_data_28;
      end 
      if((th_myfunc_6 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_53_1 <= 1;
      if(th_myfunc_6 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_54_1 <= th_myfunc_6 == 13;
      _myfifo_cond_55_1 <= 1;
      _myfifo_cond_56_1 <= 1;
      if((th_myfunc_6 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_6_write_data_28;
      end 
      if((th_myfunc_6 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_57_1 <= 1;
      if(th_myfunc_7 == 5) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_58_1 <= th_myfunc_7 == 5;
      _myfifo_cond_59_1 <= 1;
      _myfifo_cond_60_1 <= 1;
      if((th_myfunc_7 == 11) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_7_write_data_32;
      end 
      if((th_myfunc_7 == 11) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_61_1 <= 1;
      if(th_myfunc_7 == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_62_1 <= th_myfunc_7 == 13;
      _myfifo_cond_63_1 <= 1;
      _myfifo_cond_64_1 <= 1;
      if((th_myfunc_7 == 19) && !myfifo_full) begin
        myfifo_wdata <= _th_myfunc_7_write_data_32;
      end 
      if((th_myfunc_7 == 19) && !myfifo_full) begin
        myfifo_enq <= 1;
      end 
      _myfifo_cond_65_1 <= 1;
      if(th_blink == 13) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_66_1 <= th_blink == 13;
      _myfifo_cond_67_1 <= 1;
      _myfifo_cond_68_1 <= 1;
      if(th_blink == 19) begin
        myfifo_deq <= 1;
      end 
      _myfifo_cond_69_1 <= th_blink == 19;
      _myfifo_cond_70_1 <= 1;
      _myfifo_cond_71_1 <= 1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_tid_0 <= 0;
      _th_myfunc_start[_th_blink_tid_0] <= (0 >> _th_blink_tid_0) & 1'd1;
      _tmp_33 <= 0;
      _th_blink_read_data_33 <= 0;
      _tmp_35 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          if(!myfifo_almost_full) begin
            th_blink <= th_blink_2;
          end 
        end
        th_blink_2: begin
          if(!myfifo_almost_full) begin
            th_blink <= th_blink_3;
          end 
        end
        th_blink_3: begin
          _th_blink_tid_0 <= 0;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          if(_th_blink_tid_0 < 8) begin
            th_blink <= th_blink_5;
          end else begin
            th_blink <= th_blink_9;
          end
        end
        th_blink_5: begin
          _th_myfunc_start[_th_blink_tid_0] <= 1;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_myfunc_start[_th_blink_tid_0] <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_tid_0 <= _th_blink_tid_0 + 1;
          th_blink <= th_blink_4;
        end
        th_blink_9: begin
          _th_blink_tid_0 <= 0;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          if(_th_blink_tid_0 < 8) begin
            th_blink <= th_blink_11;
          end else begin
            th_blink <= th_blink_13;
          end
        end
        th_blink_11: begin
          if((_th_blink_tid_0 == 0)? th_myfunc_0 == 23 : 
          (_th_blink_tid_0 == 1)? th_myfunc_1 == 23 : 
          (_th_blink_tid_0 == 2)? th_myfunc_2 == 23 : 
          (_th_blink_tid_0 == 3)? th_myfunc_3 == 23 : 
          (_th_blink_tid_0 == 4)? th_myfunc_4 == 23 : 
          (_th_blink_tid_0 == 5)? th_myfunc_5 == 23 : 
          (_th_blink_tid_0 == 6)? th_myfunc_6 == 23 : 
          (_th_blink_tid_0 == 7)? th_myfunc_7 == 23 : 0) begin
            th_blink <= th_blink_12;
          end 
        end
        th_blink_12: begin
          _th_blink_tid_0 <= _th_blink_tid_0 + 1;
          th_blink <= th_blink_10;
        end
        th_blink_13: begin
          if(!myfifo_empty) begin
            th_blink <= th_blink_14;
          end 
        end
        th_blink_14: begin
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          if(_tmp_32) begin
            _tmp_33 <= myfifo_rdata;
          end 
          if(_tmp_32) begin
            th_blink <= th_blink_16;
          end 
        end
        th_blink_16: begin
          _th_blink_read_data_33 <= _tmp_33;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          LED <= _th_blink_read_data_33;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          $display("result fifo.out = %d", _th_blink_read_data_33);
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          if(!myfifo_empty) begin
            th_blink <= th_blink_20;
          end 
        end
        th_blink_20: begin
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          if(_tmp_34) begin
            _tmp_35 <= myfifo_rdata;
          end 
          if(_tmp_34) begin
            th_blink <= th_blink_22;
          end 
        end
        th_blink_22: begin
          _th_blink_read_data_33 <= _tmp_35;
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          LED <= _th_blink_read_data_33;
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          $display("result fifo.out = %d", _th_blink_read_data_33);
          th_blink <= th_blink_25;
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
  localparam th_myfunc_0_22 = 22;
  localparam th_myfunc_0_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_0 <= th_myfunc_0_init;
      _th_myfunc_0_called <= 0;
      _th_myfunc_0_tid_1 <= 0;
      _th_myfunc_0_tid_2 <= 0;
      _tmp_1 <= 0;
      _th_myfunc_0_read_data_3 <= 0;
      _th_myfunc_0_write_data_4 <= 0;
      _tmp_3 <= 0;
    end else begin
      case(th_myfunc_0)
        th_myfunc_0_init: begin
          if(_th_myfunc_start[0] && (th_blink == 6)) begin
            _th_myfunc_0_called <= 1;
          end 
          if(_th_myfunc_start[0] && (th_blink == 6)) begin
            _th_myfunc_0_tid_1 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[0]) begin
            th_myfunc_0 <= th_myfunc_0_1;
          end 
        end
        th_myfunc_0_1: begin
          _th_myfunc_0_tid_2 <= _th_myfunc_0_tid_1;
          th_myfunc_0 <= th_myfunc_0_2;
        end
        th_myfunc_0_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_3;
          end 
        end
        th_myfunc_0_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 0))) begin
            th_myfunc_0 <= th_myfunc_0_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_4;
          end 
        end
        th_myfunc_0_4: begin
          $display("Thread %d Lock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_5: begin
          if(!myfifo_empty) begin
            th_myfunc_0 <= th_myfunc_0_6;
          end 
        end
        th_myfunc_0_6: begin
          th_myfunc_0 <= th_myfunc_0_7;
        end
        th_myfunc_0_7: begin
          if(_tmp_0) begin
            _tmp_1 <= myfifo_rdata;
          end 
          if(_tmp_0) begin
            th_myfunc_0 <= th_myfunc_0_8;
          end 
        end
        th_myfunc_0_8: begin
          _th_myfunc_0_read_data_3 <= _tmp_1;
          th_myfunc_0 <= th_myfunc_0_9;
        end
        th_myfunc_0_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_0_tid_2, _th_myfunc_0_read_data_3);
          th_myfunc_0 <= th_myfunc_0_10;
        end
        th_myfunc_0_10: begin
          _th_myfunc_0_write_data_4 <= _th_myfunc_0_read_data_3 + 1;
          th_myfunc_0 <= th_myfunc_0_11;
        end
        th_myfunc_0_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_0 <= th_myfunc_0_12;
          end 
        end
        th_myfunc_0_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_0_tid_2, _th_myfunc_0_write_data_4);
          th_myfunc_0 <= th_myfunc_0_13;
        end
        th_myfunc_0_13: begin
          if(!myfifo_empty) begin
            th_myfunc_0 <= th_myfunc_0_14;
          end 
        end
        th_myfunc_0_14: begin
          th_myfunc_0 <= th_myfunc_0_15;
        end
        th_myfunc_0_15: begin
          if(_tmp_2) begin
            _tmp_3 <= myfifo_rdata;
          end 
          if(_tmp_2) begin
            th_myfunc_0 <= th_myfunc_0_16;
          end 
        end
        th_myfunc_0_16: begin
          _th_myfunc_0_read_data_3 <= _tmp_3;
          th_myfunc_0 <= th_myfunc_0_17;
        end
        th_myfunc_0_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_0_tid_2, _th_myfunc_0_read_data_3);
          th_myfunc_0 <= th_myfunc_0_18;
        end
        th_myfunc_0_18: begin
          _th_myfunc_0_write_data_4 <= _th_myfunc_0_read_data_3 + 1;
          th_myfunc_0 <= th_myfunc_0_19;
        end
        th_myfunc_0_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_0 <= th_myfunc_0_20;
          end 
        end
        th_myfunc_0_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_0_tid_2, _th_myfunc_0_write_data_4);
          th_myfunc_0 <= th_myfunc_0_21;
        end
        th_myfunc_0_21: begin
          th_myfunc_0 <= th_myfunc_0_22;
        end
        th_myfunc_0_22: begin
          $display("Thread %d Unlock", _th_myfunc_0_tid_2);
          th_myfunc_0 <= th_myfunc_0_23;
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
  localparam th_myfunc_1_22 = 22;
  localparam th_myfunc_1_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_1 <= th_myfunc_1_init;
      _th_myfunc_1_called <= 0;
      _th_myfunc_1_tid_5 <= 0;
      _th_myfunc_1_tid_6 <= 0;
      _tmp_5 <= 0;
      _th_myfunc_1_read_data_7 <= 0;
      _th_myfunc_1_write_data_8 <= 0;
      _tmp_7 <= 0;
    end else begin
      case(th_myfunc_1)
        th_myfunc_1_init: begin
          if(_th_myfunc_start[1] && (th_blink == 6)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(_th_myfunc_start[1] && (th_blink == 6)) begin
            _th_myfunc_1_tid_5 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_6 <= _th_myfunc_1_tid_5;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_3;
          end 
        end
        th_myfunc_1_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 1))) begin
            th_myfunc_1 <= th_myfunc_1_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_4;
          end 
        end
        th_myfunc_1_4: begin
          $display("Thread %d Lock", _th_myfunc_1_tid_6);
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_5: begin
          if(!myfifo_empty) begin
            th_myfunc_1 <= th_myfunc_1_6;
          end 
        end
        th_myfunc_1_6: begin
          th_myfunc_1 <= th_myfunc_1_7;
        end
        th_myfunc_1_7: begin
          if(_tmp_4) begin
            _tmp_5 <= myfifo_rdata;
          end 
          if(_tmp_4) begin
            th_myfunc_1 <= th_myfunc_1_8;
          end 
        end
        th_myfunc_1_8: begin
          _th_myfunc_1_read_data_7 <= _tmp_5;
          th_myfunc_1 <= th_myfunc_1_9;
        end
        th_myfunc_1_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_1_tid_6, _th_myfunc_1_read_data_7);
          th_myfunc_1 <= th_myfunc_1_10;
        end
        th_myfunc_1_10: begin
          _th_myfunc_1_write_data_8 <= _th_myfunc_1_read_data_7 + 1;
          th_myfunc_1 <= th_myfunc_1_11;
        end
        th_myfunc_1_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_1 <= th_myfunc_1_12;
          end 
        end
        th_myfunc_1_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_1_tid_6, _th_myfunc_1_write_data_8);
          th_myfunc_1 <= th_myfunc_1_13;
        end
        th_myfunc_1_13: begin
          if(!myfifo_empty) begin
            th_myfunc_1 <= th_myfunc_1_14;
          end 
        end
        th_myfunc_1_14: begin
          th_myfunc_1 <= th_myfunc_1_15;
        end
        th_myfunc_1_15: begin
          if(_tmp_6) begin
            _tmp_7 <= myfifo_rdata;
          end 
          if(_tmp_6) begin
            th_myfunc_1 <= th_myfunc_1_16;
          end 
        end
        th_myfunc_1_16: begin
          _th_myfunc_1_read_data_7 <= _tmp_7;
          th_myfunc_1 <= th_myfunc_1_17;
        end
        th_myfunc_1_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_1_tid_6, _th_myfunc_1_read_data_7);
          th_myfunc_1 <= th_myfunc_1_18;
        end
        th_myfunc_1_18: begin
          _th_myfunc_1_write_data_8 <= _th_myfunc_1_read_data_7 + 1;
          th_myfunc_1 <= th_myfunc_1_19;
        end
        th_myfunc_1_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_1 <= th_myfunc_1_20;
          end 
        end
        th_myfunc_1_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_1_tid_6, _th_myfunc_1_write_data_8);
          th_myfunc_1 <= th_myfunc_1_21;
        end
        th_myfunc_1_21: begin
          th_myfunc_1 <= th_myfunc_1_22;
        end
        th_myfunc_1_22: begin
          $display("Thread %d Unlock", _th_myfunc_1_tid_6);
          th_myfunc_1 <= th_myfunc_1_23;
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
  localparam th_myfunc_2_22 = 22;
  localparam th_myfunc_2_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_2 <= th_myfunc_2_init;
      _th_myfunc_2_called <= 0;
      _th_myfunc_2_tid_9 <= 0;
      _th_myfunc_2_tid_10 <= 0;
      _tmp_9 <= 0;
      _th_myfunc_2_read_data_11 <= 0;
      _th_myfunc_2_write_data_12 <= 0;
      _tmp_11 <= 0;
    end else begin
      case(th_myfunc_2)
        th_myfunc_2_init: begin
          if(_th_myfunc_start[2] && (th_blink == 6)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(_th_myfunc_start[2] && (th_blink == 6)) begin
            _th_myfunc_2_tid_9 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_10 <= _th_myfunc_2_tid_9;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_3;
          end 
        end
        th_myfunc_2_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 2))) begin
            th_myfunc_2 <= th_myfunc_2_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_4;
          end 
        end
        th_myfunc_2_4: begin
          $display("Thread %d Lock", _th_myfunc_2_tid_10);
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_5: begin
          if(!myfifo_empty) begin
            th_myfunc_2 <= th_myfunc_2_6;
          end 
        end
        th_myfunc_2_6: begin
          th_myfunc_2 <= th_myfunc_2_7;
        end
        th_myfunc_2_7: begin
          if(_tmp_8) begin
            _tmp_9 <= myfifo_rdata;
          end 
          if(_tmp_8) begin
            th_myfunc_2 <= th_myfunc_2_8;
          end 
        end
        th_myfunc_2_8: begin
          _th_myfunc_2_read_data_11 <= _tmp_9;
          th_myfunc_2 <= th_myfunc_2_9;
        end
        th_myfunc_2_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_2_tid_10, _th_myfunc_2_read_data_11);
          th_myfunc_2 <= th_myfunc_2_10;
        end
        th_myfunc_2_10: begin
          _th_myfunc_2_write_data_12 <= _th_myfunc_2_read_data_11 + 1;
          th_myfunc_2 <= th_myfunc_2_11;
        end
        th_myfunc_2_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_2 <= th_myfunc_2_12;
          end 
        end
        th_myfunc_2_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_2_tid_10, _th_myfunc_2_write_data_12);
          th_myfunc_2 <= th_myfunc_2_13;
        end
        th_myfunc_2_13: begin
          if(!myfifo_empty) begin
            th_myfunc_2 <= th_myfunc_2_14;
          end 
        end
        th_myfunc_2_14: begin
          th_myfunc_2 <= th_myfunc_2_15;
        end
        th_myfunc_2_15: begin
          if(_tmp_10) begin
            _tmp_11 <= myfifo_rdata;
          end 
          if(_tmp_10) begin
            th_myfunc_2 <= th_myfunc_2_16;
          end 
        end
        th_myfunc_2_16: begin
          _th_myfunc_2_read_data_11 <= _tmp_11;
          th_myfunc_2 <= th_myfunc_2_17;
        end
        th_myfunc_2_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_2_tid_10, _th_myfunc_2_read_data_11);
          th_myfunc_2 <= th_myfunc_2_18;
        end
        th_myfunc_2_18: begin
          _th_myfunc_2_write_data_12 <= _th_myfunc_2_read_data_11 + 1;
          th_myfunc_2 <= th_myfunc_2_19;
        end
        th_myfunc_2_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_2 <= th_myfunc_2_20;
          end 
        end
        th_myfunc_2_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_2_tid_10, _th_myfunc_2_write_data_12);
          th_myfunc_2 <= th_myfunc_2_21;
        end
        th_myfunc_2_21: begin
          th_myfunc_2 <= th_myfunc_2_22;
        end
        th_myfunc_2_22: begin
          $display("Thread %d Unlock", _th_myfunc_2_tid_10);
          th_myfunc_2 <= th_myfunc_2_23;
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
  localparam th_myfunc_3_22 = 22;
  localparam th_myfunc_3_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_3 <= th_myfunc_3_init;
      _th_myfunc_3_called <= 0;
      _th_myfunc_3_tid_13 <= 0;
      _th_myfunc_3_tid_14 <= 0;
      _tmp_13 <= 0;
      _th_myfunc_3_read_data_15 <= 0;
      _th_myfunc_3_write_data_16 <= 0;
      _tmp_15 <= 0;
    end else begin
      case(th_myfunc_3)
        th_myfunc_3_init: begin
          if(_th_myfunc_start[3] && (th_blink == 6)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(_th_myfunc_start[3] && (th_blink == 6)) begin
            _th_myfunc_3_tid_13 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_14 <= _th_myfunc_3_tid_13;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_3;
          end 
        end
        th_myfunc_3_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 3))) begin
            th_myfunc_3 <= th_myfunc_3_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_4;
          end 
        end
        th_myfunc_3_4: begin
          $display("Thread %d Lock", _th_myfunc_3_tid_14);
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_5: begin
          if(!myfifo_empty) begin
            th_myfunc_3 <= th_myfunc_3_6;
          end 
        end
        th_myfunc_3_6: begin
          th_myfunc_3 <= th_myfunc_3_7;
        end
        th_myfunc_3_7: begin
          if(_tmp_12) begin
            _tmp_13 <= myfifo_rdata;
          end 
          if(_tmp_12) begin
            th_myfunc_3 <= th_myfunc_3_8;
          end 
        end
        th_myfunc_3_8: begin
          _th_myfunc_3_read_data_15 <= _tmp_13;
          th_myfunc_3 <= th_myfunc_3_9;
        end
        th_myfunc_3_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_3_tid_14, _th_myfunc_3_read_data_15);
          th_myfunc_3 <= th_myfunc_3_10;
        end
        th_myfunc_3_10: begin
          _th_myfunc_3_write_data_16 <= _th_myfunc_3_read_data_15 + 1;
          th_myfunc_3 <= th_myfunc_3_11;
        end
        th_myfunc_3_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_3 <= th_myfunc_3_12;
          end 
        end
        th_myfunc_3_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_3_tid_14, _th_myfunc_3_write_data_16);
          th_myfunc_3 <= th_myfunc_3_13;
        end
        th_myfunc_3_13: begin
          if(!myfifo_empty) begin
            th_myfunc_3 <= th_myfunc_3_14;
          end 
        end
        th_myfunc_3_14: begin
          th_myfunc_3 <= th_myfunc_3_15;
        end
        th_myfunc_3_15: begin
          if(_tmp_14) begin
            _tmp_15 <= myfifo_rdata;
          end 
          if(_tmp_14) begin
            th_myfunc_3 <= th_myfunc_3_16;
          end 
        end
        th_myfunc_3_16: begin
          _th_myfunc_3_read_data_15 <= _tmp_15;
          th_myfunc_3 <= th_myfunc_3_17;
        end
        th_myfunc_3_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_3_tid_14, _th_myfunc_3_read_data_15);
          th_myfunc_3 <= th_myfunc_3_18;
        end
        th_myfunc_3_18: begin
          _th_myfunc_3_write_data_16 <= _th_myfunc_3_read_data_15 + 1;
          th_myfunc_3 <= th_myfunc_3_19;
        end
        th_myfunc_3_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_3 <= th_myfunc_3_20;
          end 
        end
        th_myfunc_3_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_3_tid_14, _th_myfunc_3_write_data_16);
          th_myfunc_3 <= th_myfunc_3_21;
        end
        th_myfunc_3_21: begin
          th_myfunc_3 <= th_myfunc_3_22;
        end
        th_myfunc_3_22: begin
          $display("Thread %d Unlock", _th_myfunc_3_tid_14);
          th_myfunc_3 <= th_myfunc_3_23;
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
  localparam th_myfunc_4_22 = 22;
  localparam th_myfunc_4_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_4 <= th_myfunc_4_init;
      _th_myfunc_4_called <= 0;
      _th_myfunc_4_tid_17 <= 0;
      _th_myfunc_4_tid_18 <= 0;
      _tmp_17 <= 0;
      _th_myfunc_4_read_data_19 <= 0;
      _th_myfunc_4_write_data_20 <= 0;
      _tmp_19 <= 0;
    end else begin
      case(th_myfunc_4)
        th_myfunc_4_init: begin
          if(_th_myfunc_start[4] && (th_blink == 6)) begin
            _th_myfunc_4_called <= 1;
          end 
          if(_th_myfunc_start[4] && (th_blink == 6)) begin
            _th_myfunc_4_tid_17 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[4]) begin
            th_myfunc_4 <= th_myfunc_4_1;
          end 
        end
        th_myfunc_4_1: begin
          _th_myfunc_4_tid_18 <= _th_myfunc_4_tid_17;
          th_myfunc_4 <= th_myfunc_4_2;
        end
        th_myfunc_4_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_3;
          end 
        end
        th_myfunc_4_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 4))) begin
            th_myfunc_4 <= th_myfunc_4_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_4;
          end 
        end
        th_myfunc_4_4: begin
          $display("Thread %d Lock", _th_myfunc_4_tid_18);
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_5: begin
          if(!myfifo_empty) begin
            th_myfunc_4 <= th_myfunc_4_6;
          end 
        end
        th_myfunc_4_6: begin
          th_myfunc_4 <= th_myfunc_4_7;
        end
        th_myfunc_4_7: begin
          if(_tmp_16) begin
            _tmp_17 <= myfifo_rdata;
          end 
          if(_tmp_16) begin
            th_myfunc_4 <= th_myfunc_4_8;
          end 
        end
        th_myfunc_4_8: begin
          _th_myfunc_4_read_data_19 <= _tmp_17;
          th_myfunc_4 <= th_myfunc_4_9;
        end
        th_myfunc_4_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_4_tid_18, _th_myfunc_4_read_data_19);
          th_myfunc_4 <= th_myfunc_4_10;
        end
        th_myfunc_4_10: begin
          _th_myfunc_4_write_data_20 <= _th_myfunc_4_read_data_19 + 1;
          th_myfunc_4 <= th_myfunc_4_11;
        end
        th_myfunc_4_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_4 <= th_myfunc_4_12;
          end 
        end
        th_myfunc_4_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_4_tid_18, _th_myfunc_4_write_data_20);
          th_myfunc_4 <= th_myfunc_4_13;
        end
        th_myfunc_4_13: begin
          if(!myfifo_empty) begin
            th_myfunc_4 <= th_myfunc_4_14;
          end 
        end
        th_myfunc_4_14: begin
          th_myfunc_4 <= th_myfunc_4_15;
        end
        th_myfunc_4_15: begin
          if(_tmp_18) begin
            _tmp_19 <= myfifo_rdata;
          end 
          if(_tmp_18) begin
            th_myfunc_4 <= th_myfunc_4_16;
          end 
        end
        th_myfunc_4_16: begin
          _th_myfunc_4_read_data_19 <= _tmp_19;
          th_myfunc_4 <= th_myfunc_4_17;
        end
        th_myfunc_4_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_4_tid_18, _th_myfunc_4_read_data_19);
          th_myfunc_4 <= th_myfunc_4_18;
        end
        th_myfunc_4_18: begin
          _th_myfunc_4_write_data_20 <= _th_myfunc_4_read_data_19 + 1;
          th_myfunc_4 <= th_myfunc_4_19;
        end
        th_myfunc_4_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_4 <= th_myfunc_4_20;
          end 
        end
        th_myfunc_4_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_4_tid_18, _th_myfunc_4_write_data_20);
          th_myfunc_4 <= th_myfunc_4_21;
        end
        th_myfunc_4_21: begin
          th_myfunc_4 <= th_myfunc_4_22;
        end
        th_myfunc_4_22: begin
          $display("Thread %d Unlock", _th_myfunc_4_tid_18);
          th_myfunc_4 <= th_myfunc_4_23;
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
  localparam th_myfunc_5_22 = 22;
  localparam th_myfunc_5_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_5 <= th_myfunc_5_init;
      _th_myfunc_5_called <= 0;
      _th_myfunc_5_tid_21 <= 0;
      _th_myfunc_5_tid_22 <= 0;
      _tmp_21 <= 0;
      _th_myfunc_5_read_data_23 <= 0;
      _th_myfunc_5_write_data_24 <= 0;
      _tmp_23 <= 0;
    end else begin
      case(th_myfunc_5)
        th_myfunc_5_init: begin
          if(_th_myfunc_start[5] && (th_blink == 6)) begin
            _th_myfunc_5_called <= 1;
          end 
          if(_th_myfunc_start[5] && (th_blink == 6)) begin
            _th_myfunc_5_tid_21 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[5]) begin
            th_myfunc_5 <= th_myfunc_5_1;
          end 
        end
        th_myfunc_5_1: begin
          _th_myfunc_5_tid_22 <= _th_myfunc_5_tid_21;
          th_myfunc_5 <= th_myfunc_5_2;
        end
        th_myfunc_5_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_3;
          end 
        end
        th_myfunc_5_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 5))) begin
            th_myfunc_5 <= th_myfunc_5_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_4;
          end 
        end
        th_myfunc_5_4: begin
          $display("Thread %d Lock", _th_myfunc_5_tid_22);
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_5: begin
          if(!myfifo_empty) begin
            th_myfunc_5 <= th_myfunc_5_6;
          end 
        end
        th_myfunc_5_6: begin
          th_myfunc_5 <= th_myfunc_5_7;
        end
        th_myfunc_5_7: begin
          if(_tmp_20) begin
            _tmp_21 <= myfifo_rdata;
          end 
          if(_tmp_20) begin
            th_myfunc_5 <= th_myfunc_5_8;
          end 
        end
        th_myfunc_5_8: begin
          _th_myfunc_5_read_data_23 <= _tmp_21;
          th_myfunc_5 <= th_myfunc_5_9;
        end
        th_myfunc_5_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_5_tid_22, _th_myfunc_5_read_data_23);
          th_myfunc_5 <= th_myfunc_5_10;
        end
        th_myfunc_5_10: begin
          _th_myfunc_5_write_data_24 <= _th_myfunc_5_read_data_23 + 1;
          th_myfunc_5 <= th_myfunc_5_11;
        end
        th_myfunc_5_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_5 <= th_myfunc_5_12;
          end 
        end
        th_myfunc_5_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_5_tid_22, _th_myfunc_5_write_data_24);
          th_myfunc_5 <= th_myfunc_5_13;
        end
        th_myfunc_5_13: begin
          if(!myfifo_empty) begin
            th_myfunc_5 <= th_myfunc_5_14;
          end 
        end
        th_myfunc_5_14: begin
          th_myfunc_5 <= th_myfunc_5_15;
        end
        th_myfunc_5_15: begin
          if(_tmp_22) begin
            _tmp_23 <= myfifo_rdata;
          end 
          if(_tmp_22) begin
            th_myfunc_5 <= th_myfunc_5_16;
          end 
        end
        th_myfunc_5_16: begin
          _th_myfunc_5_read_data_23 <= _tmp_23;
          th_myfunc_5 <= th_myfunc_5_17;
        end
        th_myfunc_5_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_5_tid_22, _th_myfunc_5_read_data_23);
          th_myfunc_5 <= th_myfunc_5_18;
        end
        th_myfunc_5_18: begin
          _th_myfunc_5_write_data_24 <= _th_myfunc_5_read_data_23 + 1;
          th_myfunc_5 <= th_myfunc_5_19;
        end
        th_myfunc_5_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_5 <= th_myfunc_5_20;
          end 
        end
        th_myfunc_5_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_5_tid_22, _th_myfunc_5_write_data_24);
          th_myfunc_5 <= th_myfunc_5_21;
        end
        th_myfunc_5_21: begin
          th_myfunc_5 <= th_myfunc_5_22;
        end
        th_myfunc_5_22: begin
          $display("Thread %d Unlock", _th_myfunc_5_tid_22);
          th_myfunc_5 <= th_myfunc_5_23;
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
  localparam th_myfunc_6_22 = 22;
  localparam th_myfunc_6_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_6 <= th_myfunc_6_init;
      _th_myfunc_6_called <= 0;
      _th_myfunc_6_tid_25 <= 0;
      _th_myfunc_6_tid_26 <= 0;
      _tmp_25 <= 0;
      _th_myfunc_6_read_data_27 <= 0;
      _th_myfunc_6_write_data_28 <= 0;
      _tmp_27 <= 0;
    end else begin
      case(th_myfunc_6)
        th_myfunc_6_init: begin
          if(_th_myfunc_start[6] && (th_blink == 6)) begin
            _th_myfunc_6_called <= 1;
          end 
          if(_th_myfunc_start[6] && (th_blink == 6)) begin
            _th_myfunc_6_tid_25 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[6]) begin
            th_myfunc_6 <= th_myfunc_6_1;
          end 
        end
        th_myfunc_6_1: begin
          _th_myfunc_6_tid_26 <= _th_myfunc_6_tid_25;
          th_myfunc_6 <= th_myfunc_6_2;
        end
        th_myfunc_6_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_3;
          end 
        end
        th_myfunc_6_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 6))) begin
            th_myfunc_6 <= th_myfunc_6_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_4;
          end 
        end
        th_myfunc_6_4: begin
          $display("Thread %d Lock", _th_myfunc_6_tid_26);
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_5: begin
          if(!myfifo_empty) begin
            th_myfunc_6 <= th_myfunc_6_6;
          end 
        end
        th_myfunc_6_6: begin
          th_myfunc_6 <= th_myfunc_6_7;
        end
        th_myfunc_6_7: begin
          if(_tmp_24) begin
            _tmp_25 <= myfifo_rdata;
          end 
          if(_tmp_24) begin
            th_myfunc_6 <= th_myfunc_6_8;
          end 
        end
        th_myfunc_6_8: begin
          _th_myfunc_6_read_data_27 <= _tmp_25;
          th_myfunc_6 <= th_myfunc_6_9;
        end
        th_myfunc_6_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_6_tid_26, _th_myfunc_6_read_data_27);
          th_myfunc_6 <= th_myfunc_6_10;
        end
        th_myfunc_6_10: begin
          _th_myfunc_6_write_data_28 <= _th_myfunc_6_read_data_27 + 1;
          th_myfunc_6 <= th_myfunc_6_11;
        end
        th_myfunc_6_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_6 <= th_myfunc_6_12;
          end 
        end
        th_myfunc_6_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_6_tid_26, _th_myfunc_6_write_data_28);
          th_myfunc_6 <= th_myfunc_6_13;
        end
        th_myfunc_6_13: begin
          if(!myfifo_empty) begin
            th_myfunc_6 <= th_myfunc_6_14;
          end 
        end
        th_myfunc_6_14: begin
          th_myfunc_6 <= th_myfunc_6_15;
        end
        th_myfunc_6_15: begin
          if(_tmp_26) begin
            _tmp_27 <= myfifo_rdata;
          end 
          if(_tmp_26) begin
            th_myfunc_6 <= th_myfunc_6_16;
          end 
        end
        th_myfunc_6_16: begin
          _th_myfunc_6_read_data_27 <= _tmp_27;
          th_myfunc_6 <= th_myfunc_6_17;
        end
        th_myfunc_6_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_6_tid_26, _th_myfunc_6_read_data_27);
          th_myfunc_6 <= th_myfunc_6_18;
        end
        th_myfunc_6_18: begin
          _th_myfunc_6_write_data_28 <= _th_myfunc_6_read_data_27 + 1;
          th_myfunc_6 <= th_myfunc_6_19;
        end
        th_myfunc_6_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_6 <= th_myfunc_6_20;
          end 
        end
        th_myfunc_6_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_6_tid_26, _th_myfunc_6_write_data_28);
          th_myfunc_6 <= th_myfunc_6_21;
        end
        th_myfunc_6_21: begin
          th_myfunc_6 <= th_myfunc_6_22;
        end
        th_myfunc_6_22: begin
          $display("Thread %d Unlock", _th_myfunc_6_tid_26);
          th_myfunc_6 <= th_myfunc_6_23;
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
  localparam th_myfunc_7_22 = 22;
  localparam th_myfunc_7_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_7 <= th_myfunc_7_init;
      _th_myfunc_7_called <= 0;
      _th_myfunc_7_tid_29 <= 0;
      _th_myfunc_7_tid_30 <= 0;
      _tmp_29 <= 0;
      _th_myfunc_7_read_data_31 <= 0;
      _th_myfunc_7_write_data_32 <= 0;
      _tmp_31 <= 0;
    end else begin
      case(th_myfunc_7)
        th_myfunc_7_init: begin
          if(_th_myfunc_start[7] && (th_blink == 6)) begin
            _th_myfunc_7_called <= 1;
          end 
          if(_th_myfunc_start[7] && (th_blink == 6)) begin
            _th_myfunc_7_tid_29 <= _th_blink_tid_0;
          end 
          if((th_blink == 6) && _th_myfunc_start[7]) begin
            th_myfunc_7 <= th_myfunc_7_1;
          end 
        end
        th_myfunc_7_1: begin
          _th_myfunc_7_tid_30 <= _th_myfunc_7_tid_29;
          th_myfunc_7 <= th_myfunc_7_2;
        end
        th_myfunc_7_2: begin
          if(!__myfifo_mutex_lock_reg || (__myfifo_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_3;
          end 
        end
        th_myfunc_7_3: begin
          if(!(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 7))) begin
            th_myfunc_7 <= th_myfunc_7_2;
          end 
          if(__myfifo_mutex_lock_reg && (__myfifo_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_4;
          end 
        end
        th_myfunc_7_4: begin
          $display("Thread %d Lock", _th_myfunc_7_tid_30);
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_5: begin
          if(!myfifo_empty) begin
            th_myfunc_7 <= th_myfunc_7_6;
          end 
        end
        th_myfunc_7_6: begin
          th_myfunc_7 <= th_myfunc_7_7;
        end
        th_myfunc_7_7: begin
          if(_tmp_28) begin
            _tmp_29 <= myfifo_rdata;
          end 
          if(_tmp_28) begin
            th_myfunc_7 <= th_myfunc_7_8;
          end 
        end
        th_myfunc_7_8: begin
          _th_myfunc_7_read_data_31 <= _tmp_29;
          th_myfunc_7 <= th_myfunc_7_9;
        end
        th_myfunc_7_9: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_7_tid_30, _th_myfunc_7_read_data_31);
          th_myfunc_7 <= th_myfunc_7_10;
        end
        th_myfunc_7_10: begin
          _th_myfunc_7_write_data_32 <= _th_myfunc_7_read_data_31 + 1;
          th_myfunc_7 <= th_myfunc_7_11;
        end
        th_myfunc_7_11: begin
          if(!myfifo_almost_full) begin
            th_myfunc_7 <= th_myfunc_7_12;
          end 
        end
        th_myfunc_7_12: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_7_tid_30, _th_myfunc_7_write_data_32);
          th_myfunc_7 <= th_myfunc_7_13;
        end
        th_myfunc_7_13: begin
          if(!myfifo_empty) begin
            th_myfunc_7 <= th_myfunc_7_14;
          end 
        end
        th_myfunc_7_14: begin
          th_myfunc_7 <= th_myfunc_7_15;
        end
        th_myfunc_7_15: begin
          if(_tmp_30) begin
            _tmp_31 <= myfifo_rdata;
          end 
          if(_tmp_30) begin
            th_myfunc_7 <= th_myfunc_7_16;
          end 
        end
        th_myfunc_7_16: begin
          _th_myfunc_7_read_data_31 <= _tmp_31;
          th_myfunc_7 <= th_myfunc_7_17;
        end
        th_myfunc_7_17: begin
          $display("Thread %d fifo.out = %d", _th_myfunc_7_tid_30, _th_myfunc_7_read_data_31);
          th_myfunc_7 <= th_myfunc_7_18;
        end
        th_myfunc_7_18: begin
          _th_myfunc_7_write_data_32 <= _th_myfunc_7_read_data_31 + 1;
          th_myfunc_7 <= th_myfunc_7_19;
        end
        th_myfunc_7_19: begin
          if(!myfifo_almost_full) begin
            th_myfunc_7 <= th_myfunc_7_20;
          end 
        end
        th_myfunc_7_20: begin
          $display("Thread %d fifo.in <- %d", _th_myfunc_7_tid_30, _th_myfunc_7_write_data_32);
          th_myfunc_7 <= th_myfunc_7_21;
        end
        th_myfunc_7_21: begin
          th_myfunc_7 <= th_myfunc_7_22;
        end
        th_myfunc_7_22: begin
          $display("Thread %d Unlock", _th_myfunc_7_tid_30);
          th_myfunc_7 <= th_myfunc_7_23;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __myfifo_mutex_lock_reg <= 0;
      __myfifo_mutex_lock_id <= 0;
    end else begin
      if((th_myfunc_0 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 21) && (__myfifo_mutex_lock_id == 0)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_1 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 21) && (__myfifo_mutex_lock_id == 1)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_2 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 21) && (__myfifo_mutex_lock_id == 2)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_3 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 21) && (__myfifo_mutex_lock_id == 3)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_4 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 21) && (__myfifo_mutex_lock_id == 4)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_5 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 21) && (__myfifo_mutex_lock_id == 5)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_6 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 21) && (__myfifo_mutex_lock_id == 6)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_7 == 2) && !__myfifo_mutex_lock_reg) begin
        __myfifo_mutex_lock_reg <= 1;
        __myfifo_mutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 21) && (__myfifo_mutex_lock_id == 7)) begin
        __myfifo_mutex_lock_reg <= 0;
      end 
    end
  end


endmodule



module myfifo
(
  input CLK,
  input RST,
  input myfifo_enq,
  input [32-1:0] myfifo_wdata,
  output myfifo_full,
  output myfifo_almost_full,
  input myfifo_deq,
  output [32-1:0] myfifo_rdata,
  output myfifo_empty,
  output myfifo_almost_empty
);

  reg [32-1:0] mem [0:16-1];
  reg [4-1:0] head;
  reg [4-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 15);
  assign is_full = (head + 1 & 15) == tail;
  assign is_almost_full = (head + 2 & 15) == tail;
  reg [32-1:0] rdata_reg;
  assign myfifo_full = is_full;
  assign myfifo_almost_full = is_almost_full || is_full;
  assign myfifo_empty = is_empty;
  assign myfifo_almost_empty = is_almost_empty || is_empty;
  assign myfifo_rdata = rdata_reg;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      rdata_reg <= 0;
      tail <= 0;
    end else begin
      if(myfifo_enq && !is_full) begin
        mem[head] <= myfifo_wdata;
        head <= head + 1;
      end 
      if(myfifo_deq && !is_empty) begin
        rdata_reg <= mem[tail];
        tail <= tail + 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_fifo_multithread.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
