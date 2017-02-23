from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_own_mutex

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
    #100000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] LED
);

  reg [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg [8-1:0] _th_myfunc_start;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg [32-1:0] _th_blink_size_0;
  reg [32-1:0] _th_blink_i_1;
  reg _myram_cond_0_1;
  reg [32-1:0] _th_blink_tid_2;
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
  reg [32-1:0] _th_myfunc_0_tid_3;
  reg [32-1:0] _th_myfunc_0_size_4;
  reg [32-1:0] _th_myfunc_0_tid_5;
  reg [32-1:0] _th_myfunc_0_size_6;
  reg __myram_mutex_lock_reg;
  reg [32-1:0] __myram_mutex_lock_id;
  reg [32-1:0] _th_myfunc_0_i_7;
  reg _tmp_0;
  reg _myram_cond_1_1;
  reg _myram_cond_2_1;
  reg _myram_cond_2_2;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _th_myfunc_0_read_data_8;
  reg [32-1:0] _th_myfunc_0_write_data_9;
  reg _myram_cond_3_1;
  reg _th_myfunc_1_called;
  reg [32-1:0] _th_myfunc_1_tid_10;
  reg [32-1:0] _th_myfunc_1_size_11;
  reg [32-1:0] _th_myfunc_1_tid_12;
  reg [32-1:0] _th_myfunc_1_size_13;
  reg [32-1:0] _th_myfunc_1_i_14;
  reg _tmp_2;
  reg _myram_cond_4_1;
  reg _myram_cond_5_1;
  reg _myram_cond_5_2;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _th_myfunc_1_read_data_15;
  reg [32-1:0] _th_myfunc_1_write_data_16;
  reg _myram_cond_6_1;
  reg _th_myfunc_2_called;
  reg [32-1:0] _th_myfunc_2_tid_17;
  reg [32-1:0] _th_myfunc_2_size_18;
  reg [32-1:0] _th_myfunc_2_tid_19;
  reg [32-1:0] _th_myfunc_2_size_20;
  reg [32-1:0] _th_myfunc_2_i_21;
  reg _tmp_4;
  reg _myram_cond_7_1;
  reg _myram_cond_8_1;
  reg _myram_cond_8_2;
  reg [32-1:0] _tmp_5;
  reg [32-1:0] _th_myfunc_2_read_data_22;
  reg [32-1:0] _th_myfunc_2_write_data_23;
  reg _myram_cond_9_1;
  reg _th_myfunc_3_called;
  reg [32-1:0] _th_myfunc_3_tid_24;
  reg [32-1:0] _th_myfunc_3_size_25;
  reg [32-1:0] _th_myfunc_3_tid_26;
  reg [32-1:0] _th_myfunc_3_size_27;
  reg [32-1:0] _th_myfunc_3_i_28;
  reg _tmp_6;
  reg _myram_cond_10_1;
  reg _myram_cond_11_1;
  reg _myram_cond_11_2;
  reg [32-1:0] _tmp_7;
  reg [32-1:0] _th_myfunc_3_read_data_29;
  reg [32-1:0] _th_myfunc_3_write_data_30;
  reg _myram_cond_12_1;
  reg _th_myfunc_4_called;
  reg [32-1:0] _th_myfunc_4_tid_31;
  reg [32-1:0] _th_myfunc_4_size_32;
  reg [32-1:0] _th_myfunc_4_tid_33;
  reg [32-1:0] _th_myfunc_4_size_34;
  reg [32-1:0] _th_myfunc_4_i_35;
  reg _tmp_8;
  reg _myram_cond_13_1;
  reg _myram_cond_14_1;
  reg _myram_cond_14_2;
  reg [32-1:0] _tmp_9;
  reg [32-1:0] _th_myfunc_4_read_data_36;
  reg [32-1:0] _th_myfunc_4_write_data_37;
  reg _myram_cond_15_1;
  reg _th_myfunc_5_called;
  reg [32-1:0] _th_myfunc_5_tid_38;
  reg [32-1:0] _th_myfunc_5_size_39;
  reg [32-1:0] _th_myfunc_5_tid_40;
  reg [32-1:0] _th_myfunc_5_size_41;
  reg [32-1:0] _th_myfunc_5_i_42;
  reg _tmp_10;
  reg _myram_cond_16_1;
  reg _myram_cond_17_1;
  reg _myram_cond_17_2;
  reg [32-1:0] _tmp_11;
  reg [32-1:0] _th_myfunc_5_read_data_43;
  reg [32-1:0] _th_myfunc_5_write_data_44;
  reg _myram_cond_18_1;
  reg _th_myfunc_6_called;
  reg [32-1:0] _th_myfunc_6_tid_45;
  reg [32-1:0] _th_myfunc_6_size_46;
  reg [32-1:0] _th_myfunc_6_tid_47;
  reg [32-1:0] _th_myfunc_6_size_48;
  reg [32-1:0] _th_myfunc_6_i_49;
  reg _tmp_12;
  reg _myram_cond_19_1;
  reg _myram_cond_20_1;
  reg _myram_cond_20_2;
  reg [32-1:0] _tmp_13;
  reg [32-1:0] _th_myfunc_6_read_data_50;
  reg [32-1:0] _th_myfunc_6_write_data_51;
  reg _myram_cond_21_1;
  reg _th_myfunc_7_called;
  reg [32-1:0] _th_myfunc_7_tid_52;
  reg [32-1:0] _th_myfunc_7_size_53;
  reg [32-1:0] _th_myfunc_7_tid_54;
  reg [32-1:0] _th_myfunc_7_size_55;
  reg [32-1:0] _th_myfunc_7_i_56;
  reg _tmp_14;
  reg _myram_cond_22_1;
  reg _myram_cond_23_1;
  reg _myram_cond_23_2;
  reg [32-1:0] _tmp_15;
  reg [32-1:0] _th_myfunc_7_read_data_57;
  reg [32-1:0] _th_myfunc_7_write_data_58;
  reg _myram_cond_24_1;
  reg _tmp_16;
  reg _myram_cond_25_1;
  reg _myram_cond_26_1;
  reg _myram_cond_26_2;
  reg [32-1:0] _tmp_17;
  reg [32-1:0] _th_blink_read_data_59;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
      _myram_cond_1_1 <= 0;
      _tmp_0 <= 0;
      _myram_cond_2_1 <= 0;
      _myram_cond_2_2 <= 0;
      _myram_cond_3_1 <= 0;
      _myram_cond_4_1 <= 0;
      _tmp_2 <= 0;
      _myram_cond_5_1 <= 0;
      _myram_cond_5_2 <= 0;
      _myram_cond_6_1 <= 0;
      _myram_cond_7_1 <= 0;
      _tmp_4 <= 0;
      _myram_cond_8_1 <= 0;
      _myram_cond_8_2 <= 0;
      _myram_cond_9_1 <= 0;
      _myram_cond_10_1 <= 0;
      _tmp_6 <= 0;
      _myram_cond_11_1 <= 0;
      _myram_cond_11_2 <= 0;
      _myram_cond_12_1 <= 0;
      _myram_cond_13_1 <= 0;
      _tmp_8 <= 0;
      _myram_cond_14_1 <= 0;
      _myram_cond_14_2 <= 0;
      _myram_cond_15_1 <= 0;
      _myram_cond_16_1 <= 0;
      _tmp_10 <= 0;
      _myram_cond_17_1 <= 0;
      _myram_cond_17_2 <= 0;
      _myram_cond_18_1 <= 0;
      _myram_cond_19_1 <= 0;
      _tmp_12 <= 0;
      _myram_cond_20_1 <= 0;
      _myram_cond_20_2 <= 0;
      _myram_cond_21_1 <= 0;
      _myram_cond_22_1 <= 0;
      _tmp_14 <= 0;
      _myram_cond_23_1 <= 0;
      _myram_cond_23_2 <= 0;
      _myram_cond_24_1 <= 0;
      _myram_cond_25_1 <= 0;
      _tmp_16 <= 0;
      _myram_cond_26_1 <= 0;
      _myram_cond_26_2 <= 0;
    end else begin
      if(_myram_cond_2_2) begin
        _tmp_0 <= 0;
      end 
      if(_myram_cond_5_2) begin
        _tmp_2 <= 0;
      end 
      if(_myram_cond_8_2) begin
        _tmp_4 <= 0;
      end 
      if(_myram_cond_11_2) begin
        _tmp_6 <= 0;
      end 
      if(_myram_cond_14_2) begin
        _tmp_8 <= 0;
      end 
      if(_myram_cond_17_2) begin
        _tmp_10 <= 0;
      end 
      if(_myram_cond_20_2) begin
        _tmp_12 <= 0;
      end 
      if(_myram_cond_23_2) begin
        _tmp_14 <= 0;
      end 
      if(_myram_cond_26_2) begin
        _tmp_16 <= 0;
      end 
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_1_1) begin
        _tmp_0 <= 1;
      end 
      _myram_cond_2_2 <= _myram_cond_2_1;
      if(_myram_cond_3_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_4_1) begin
        _tmp_2 <= 1;
      end 
      _myram_cond_5_2 <= _myram_cond_5_1;
      if(_myram_cond_6_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_7_1) begin
        _tmp_4 <= 1;
      end 
      _myram_cond_8_2 <= _myram_cond_8_1;
      if(_myram_cond_9_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_10_1) begin
        _tmp_6 <= 1;
      end 
      _myram_cond_11_2 <= _myram_cond_11_1;
      if(_myram_cond_12_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_13_1) begin
        _tmp_8 <= 1;
      end 
      _myram_cond_14_2 <= _myram_cond_14_1;
      if(_myram_cond_15_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_16_1) begin
        _tmp_10 <= 1;
      end 
      _myram_cond_17_2 <= _myram_cond_17_1;
      if(_myram_cond_18_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_19_1) begin
        _tmp_12 <= 1;
      end 
      _myram_cond_20_2 <= _myram_cond_20_1;
      if(_myram_cond_21_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_22_1) begin
        _tmp_14 <= 1;
      end 
      _myram_cond_23_2 <= _myram_cond_23_1;
      if(_myram_cond_24_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_25_1) begin
        _tmp_16 <= 1;
      end 
      _myram_cond_26_2 <= _myram_cond_26_1;
      if(th_blink == 4) begin
        myram_0_addr <= _th_blink_i_1;
        myram_0_wdata <= 0;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= th_blink == 4;
      if(th_myfunc_0 == 7) begin
        myram_0_addr <= _th_myfunc_0_i_7;
      end 
      _myram_cond_1_1 <= th_myfunc_0 == 7;
      _myram_cond_2_1 <= th_myfunc_0 == 7;
      if(th_myfunc_0 == 10) begin
        myram_0_addr <= _th_myfunc_0_i_7;
        myram_0_wdata <= _th_myfunc_0_write_data_9;
        myram_0_wenable <= 1;
      end 
      _myram_cond_3_1 <= th_myfunc_0 == 10;
      if(th_myfunc_1 == 7) begin
        myram_0_addr <= _th_myfunc_1_i_14;
      end 
      _myram_cond_4_1 <= th_myfunc_1 == 7;
      _myram_cond_5_1 <= th_myfunc_1 == 7;
      if(th_myfunc_1 == 10) begin
        myram_0_addr <= _th_myfunc_1_i_14;
        myram_0_wdata <= _th_myfunc_1_write_data_16;
        myram_0_wenable <= 1;
      end 
      _myram_cond_6_1 <= th_myfunc_1 == 10;
      if(th_myfunc_2 == 7) begin
        myram_0_addr <= _th_myfunc_2_i_21;
      end 
      _myram_cond_7_1 <= th_myfunc_2 == 7;
      _myram_cond_8_1 <= th_myfunc_2 == 7;
      if(th_myfunc_2 == 10) begin
        myram_0_addr <= _th_myfunc_2_i_21;
        myram_0_wdata <= _th_myfunc_2_write_data_23;
        myram_0_wenable <= 1;
      end 
      _myram_cond_9_1 <= th_myfunc_2 == 10;
      if(th_myfunc_3 == 7) begin
        myram_0_addr <= _th_myfunc_3_i_28;
      end 
      _myram_cond_10_1 <= th_myfunc_3 == 7;
      _myram_cond_11_1 <= th_myfunc_3 == 7;
      if(th_myfunc_3 == 10) begin
        myram_0_addr <= _th_myfunc_3_i_28;
        myram_0_wdata <= _th_myfunc_3_write_data_30;
        myram_0_wenable <= 1;
      end 
      _myram_cond_12_1 <= th_myfunc_3 == 10;
      if(th_myfunc_4 == 7) begin
        myram_0_addr <= _th_myfunc_4_i_35;
      end 
      _myram_cond_13_1 <= th_myfunc_4 == 7;
      _myram_cond_14_1 <= th_myfunc_4 == 7;
      if(th_myfunc_4 == 10) begin
        myram_0_addr <= _th_myfunc_4_i_35;
        myram_0_wdata <= _th_myfunc_4_write_data_37;
        myram_0_wenable <= 1;
      end 
      _myram_cond_15_1 <= th_myfunc_4 == 10;
      if(th_myfunc_5 == 7) begin
        myram_0_addr <= _th_myfunc_5_i_42;
      end 
      _myram_cond_16_1 <= th_myfunc_5 == 7;
      _myram_cond_17_1 <= th_myfunc_5 == 7;
      if(th_myfunc_5 == 10) begin
        myram_0_addr <= _th_myfunc_5_i_42;
        myram_0_wdata <= _th_myfunc_5_write_data_44;
        myram_0_wenable <= 1;
      end 
      _myram_cond_18_1 <= th_myfunc_5 == 10;
      if(th_myfunc_6 == 7) begin
        myram_0_addr <= _th_myfunc_6_i_49;
      end 
      _myram_cond_19_1 <= th_myfunc_6 == 7;
      _myram_cond_20_1 <= th_myfunc_6 == 7;
      if(th_myfunc_6 == 10) begin
        myram_0_addr <= _th_myfunc_6_i_49;
        myram_0_wdata <= _th_myfunc_6_write_data_51;
        myram_0_wenable <= 1;
      end 
      _myram_cond_21_1 <= th_myfunc_6 == 10;
      if(th_myfunc_7 == 7) begin
        myram_0_addr <= _th_myfunc_7_i_56;
      end 
      _myram_cond_22_1 <= th_myfunc_7 == 7;
      _myram_cond_23_1 <= th_myfunc_7 == 7;
      if(th_myfunc_7 == 10) begin
        myram_0_addr <= _th_myfunc_7_i_56;
        myram_0_wdata <= _th_myfunc_7_write_data_58;
        myram_0_wenable <= 1;
      end 
      _myram_cond_24_1 <= th_myfunc_7 == 10;
      if(th_blink == 18) begin
        myram_0_addr <= _th_blink_i_1;
      end 
      _myram_cond_25_1 <= th_blink == 18;
      _myram_cond_26_1 <= th_blink == 18;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_tid_2 <= 0;
      _th_myfunc_start[_th_blink_tid_2] <= (0 >> _th_blink_tid_2) & 1'd1;
      _tmp_17 <= 0;
      _th_blink_read_data_59 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_size_0 <= 16;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_i_1 < _th_blink_size_0) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_6;
          end
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_6: begin
          _th_blink_tid_2 <= 0;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          if(_th_blink_tid_2 < 8) begin
            th_blink <= th_blink_8;
          end else begin
            th_blink <= th_blink_12;
          end
        end
        th_blink_8: begin
          _th_myfunc_start[_th_blink_tid_2] <= 1;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          _th_myfunc_start[_th_blink_tid_2] <= 0;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_tid_2 <= _th_blink_tid_2 + 1;
          th_blink <= th_blink_7;
        end
        th_blink_12: begin
          _th_blink_tid_2 <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          if(_th_blink_tid_2 < 8) begin
            th_blink <= th_blink_14;
          end else begin
            th_blink <= th_blink_16;
          end
        end
        th_blink_14: begin
          if((_th_blink_tid_2 == 0)? th_myfunc_0 == 15 : 
          (_th_blink_tid_2 == 1)? th_myfunc_1 == 15 : 
          (_th_blink_tid_2 == 2)? th_myfunc_2 == 15 : 
          (_th_blink_tid_2 == 3)? th_myfunc_3 == 15 : 
          (_th_blink_tid_2 == 4)? th_myfunc_4 == 15 : 
          (_th_blink_tid_2 == 5)? th_myfunc_5 == 15 : 
          (_th_blink_tid_2 == 6)? th_myfunc_6 == 15 : 
          (_th_blink_tid_2 == 7)? th_myfunc_7 == 15 : 0) begin
            th_blink <= th_blink_15;
          end 
        end
        th_blink_15: begin
          _th_blink_tid_2 <= _th_blink_tid_2 + 1;
          th_blink <= th_blink_13;
        end
        th_blink_16: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          if(_th_blink_i_1 < _th_blink_size_0) begin
            th_blink <= th_blink_18;
          end else begin
            th_blink <= th_blink_23;
          end
        end
        th_blink_18: begin
          if(_tmp_16) begin
            _tmp_17 <= myram_0_rdata;
          end 
          if(_tmp_16) begin
            th_blink <= th_blink_19;
          end 
        end
        th_blink_19: begin
          _th_blink_read_data_59 <= _tmp_17;
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          LED <= _th_blink_read_data_59;
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          $display("result ram[%d] = %d", _th_blink_i_1, _th_blink_read_data_59);
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_17;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_0 <= th_myfunc_0_init;
      _th_myfunc_0_called <= 0;
      _th_myfunc_0_tid_3 <= 0;
      _th_myfunc_0_size_4 <= 0;
      _th_myfunc_0_tid_5 <= 0;
      _th_myfunc_0_size_6 <= 0;
      _th_myfunc_0_i_7 <= 0;
      _tmp_1 <= 0;
      _th_myfunc_0_read_data_8 <= 0;
      _th_myfunc_0_write_data_9 <= 0;
    end else begin
      case(th_myfunc_0)
        th_myfunc_0_init: begin
          if(_th_myfunc_start[0] && (th_blink == 9)) begin
            _th_myfunc_0_called <= 1;
          end 
          if(_th_myfunc_start[0] && (th_blink == 9)) begin
            _th_myfunc_0_tid_3 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[0] && (th_blink == 9)) begin
            _th_myfunc_0_size_4 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[0]) begin
            th_myfunc_0 <= th_myfunc_0_1;
          end 
        end
        th_myfunc_0_1: begin
          _th_myfunc_0_tid_5 <= _th_myfunc_0_tid_3;
          _th_myfunc_0_size_6 <= _th_myfunc_0_size_4;
          th_myfunc_0 <= th_myfunc_0_2;
        end
        th_myfunc_0_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_3;
          end 
        end
        th_myfunc_0_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 0))) begin
            th_myfunc_0 <= th_myfunc_0_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 0)) begin
            th_myfunc_0 <= th_myfunc_0_4;
          end 
        end
        th_myfunc_0_4: begin
          $display("Thread %d Lock", _th_myfunc_0_tid_5);
          th_myfunc_0 <= th_myfunc_0_5;
        end
        th_myfunc_0_5: begin
          _th_myfunc_0_i_7 <= 0;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_6: begin
          if(_th_myfunc_0_i_7 < _th_myfunc_0_size_6) begin
            th_myfunc_0 <= th_myfunc_0_7;
          end else begin
            th_myfunc_0 <= th_myfunc_0_13;
          end
        end
        th_myfunc_0_7: begin
          if(_tmp_0) begin
            _tmp_1 <= myram_0_rdata;
          end 
          if(_tmp_0) begin
            th_myfunc_0 <= th_myfunc_0_8;
          end 
        end
        th_myfunc_0_8: begin
          _th_myfunc_0_read_data_8 <= _tmp_1;
          th_myfunc_0 <= th_myfunc_0_9;
        end
        th_myfunc_0_9: begin
          _th_myfunc_0_write_data_9 <= _th_myfunc_0_read_data_8 + _th_myfunc_0_tid_5 + _th_myfunc_0_i_7;
          th_myfunc_0 <= th_myfunc_0_10;
        end
        th_myfunc_0_10: begin
          th_myfunc_0 <= th_myfunc_0_11;
        end
        th_myfunc_0_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_0_tid_5, _th_myfunc_0_i_7, _th_myfunc_0_write_data_9);
          th_myfunc_0 <= th_myfunc_0_12;
        end
        th_myfunc_0_12: begin
          _th_myfunc_0_i_7 <= _th_myfunc_0_i_7 + 1;
          th_myfunc_0 <= th_myfunc_0_6;
        end
        th_myfunc_0_13: begin
          th_myfunc_0 <= th_myfunc_0_14;
        end
        th_myfunc_0_14: begin
          $display("Thread %d Unlock", _th_myfunc_0_tid_5);
          th_myfunc_0 <= th_myfunc_0_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_1 <= th_myfunc_1_init;
      _th_myfunc_1_called <= 0;
      _th_myfunc_1_tid_10 <= 0;
      _th_myfunc_1_size_11 <= 0;
      _th_myfunc_1_tid_12 <= 0;
      _th_myfunc_1_size_13 <= 0;
      _th_myfunc_1_i_14 <= 0;
      _tmp_3 <= 0;
      _th_myfunc_1_read_data_15 <= 0;
      _th_myfunc_1_write_data_16 <= 0;
    end else begin
      case(th_myfunc_1)
        th_myfunc_1_init: begin
          if(_th_myfunc_start[1] && (th_blink == 9)) begin
            _th_myfunc_1_called <= 1;
          end 
          if(_th_myfunc_start[1] && (th_blink == 9)) begin
            _th_myfunc_1_tid_10 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[1] && (th_blink == 9)) begin
            _th_myfunc_1_size_11 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[1]) begin
            th_myfunc_1 <= th_myfunc_1_1;
          end 
        end
        th_myfunc_1_1: begin
          _th_myfunc_1_tid_12 <= _th_myfunc_1_tid_10;
          _th_myfunc_1_size_13 <= _th_myfunc_1_size_11;
          th_myfunc_1 <= th_myfunc_1_2;
        end
        th_myfunc_1_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_3;
          end 
        end
        th_myfunc_1_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 1))) begin
            th_myfunc_1 <= th_myfunc_1_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 1)) begin
            th_myfunc_1 <= th_myfunc_1_4;
          end 
        end
        th_myfunc_1_4: begin
          $display("Thread %d Lock", _th_myfunc_1_tid_12);
          th_myfunc_1 <= th_myfunc_1_5;
        end
        th_myfunc_1_5: begin
          _th_myfunc_1_i_14 <= 0;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_6: begin
          if(_th_myfunc_1_i_14 < _th_myfunc_1_size_13) begin
            th_myfunc_1 <= th_myfunc_1_7;
          end else begin
            th_myfunc_1 <= th_myfunc_1_13;
          end
        end
        th_myfunc_1_7: begin
          if(_tmp_2) begin
            _tmp_3 <= myram_0_rdata;
          end 
          if(_tmp_2) begin
            th_myfunc_1 <= th_myfunc_1_8;
          end 
        end
        th_myfunc_1_8: begin
          _th_myfunc_1_read_data_15 <= _tmp_3;
          th_myfunc_1 <= th_myfunc_1_9;
        end
        th_myfunc_1_9: begin
          _th_myfunc_1_write_data_16 <= _th_myfunc_1_read_data_15 + _th_myfunc_1_tid_12 + _th_myfunc_1_i_14;
          th_myfunc_1 <= th_myfunc_1_10;
        end
        th_myfunc_1_10: begin
          th_myfunc_1 <= th_myfunc_1_11;
        end
        th_myfunc_1_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_1_tid_12, _th_myfunc_1_i_14, _th_myfunc_1_write_data_16);
          th_myfunc_1 <= th_myfunc_1_12;
        end
        th_myfunc_1_12: begin
          _th_myfunc_1_i_14 <= _th_myfunc_1_i_14 + 1;
          th_myfunc_1 <= th_myfunc_1_6;
        end
        th_myfunc_1_13: begin
          th_myfunc_1 <= th_myfunc_1_14;
        end
        th_myfunc_1_14: begin
          $display("Thread %d Unlock", _th_myfunc_1_tid_12);
          th_myfunc_1 <= th_myfunc_1_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_2 <= th_myfunc_2_init;
      _th_myfunc_2_called <= 0;
      _th_myfunc_2_tid_17 <= 0;
      _th_myfunc_2_size_18 <= 0;
      _th_myfunc_2_tid_19 <= 0;
      _th_myfunc_2_size_20 <= 0;
      _th_myfunc_2_i_21 <= 0;
      _tmp_5 <= 0;
      _th_myfunc_2_read_data_22 <= 0;
      _th_myfunc_2_write_data_23 <= 0;
    end else begin
      case(th_myfunc_2)
        th_myfunc_2_init: begin
          if(_th_myfunc_start[2] && (th_blink == 9)) begin
            _th_myfunc_2_called <= 1;
          end 
          if(_th_myfunc_start[2] && (th_blink == 9)) begin
            _th_myfunc_2_tid_17 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[2] && (th_blink == 9)) begin
            _th_myfunc_2_size_18 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[2]) begin
            th_myfunc_2 <= th_myfunc_2_1;
          end 
        end
        th_myfunc_2_1: begin
          _th_myfunc_2_tid_19 <= _th_myfunc_2_tid_17;
          _th_myfunc_2_size_20 <= _th_myfunc_2_size_18;
          th_myfunc_2 <= th_myfunc_2_2;
        end
        th_myfunc_2_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_3;
          end 
        end
        th_myfunc_2_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 2))) begin
            th_myfunc_2 <= th_myfunc_2_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 2)) begin
            th_myfunc_2 <= th_myfunc_2_4;
          end 
        end
        th_myfunc_2_4: begin
          $display("Thread %d Lock", _th_myfunc_2_tid_19);
          th_myfunc_2 <= th_myfunc_2_5;
        end
        th_myfunc_2_5: begin
          _th_myfunc_2_i_21 <= 0;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_6: begin
          if(_th_myfunc_2_i_21 < _th_myfunc_2_size_20) begin
            th_myfunc_2 <= th_myfunc_2_7;
          end else begin
            th_myfunc_2 <= th_myfunc_2_13;
          end
        end
        th_myfunc_2_7: begin
          if(_tmp_4) begin
            _tmp_5 <= myram_0_rdata;
          end 
          if(_tmp_4) begin
            th_myfunc_2 <= th_myfunc_2_8;
          end 
        end
        th_myfunc_2_8: begin
          _th_myfunc_2_read_data_22 <= _tmp_5;
          th_myfunc_2 <= th_myfunc_2_9;
        end
        th_myfunc_2_9: begin
          _th_myfunc_2_write_data_23 <= _th_myfunc_2_read_data_22 + _th_myfunc_2_tid_19 + _th_myfunc_2_i_21;
          th_myfunc_2 <= th_myfunc_2_10;
        end
        th_myfunc_2_10: begin
          th_myfunc_2 <= th_myfunc_2_11;
        end
        th_myfunc_2_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_2_tid_19, _th_myfunc_2_i_21, _th_myfunc_2_write_data_23);
          th_myfunc_2 <= th_myfunc_2_12;
        end
        th_myfunc_2_12: begin
          _th_myfunc_2_i_21 <= _th_myfunc_2_i_21 + 1;
          th_myfunc_2 <= th_myfunc_2_6;
        end
        th_myfunc_2_13: begin
          th_myfunc_2 <= th_myfunc_2_14;
        end
        th_myfunc_2_14: begin
          $display("Thread %d Unlock", _th_myfunc_2_tid_19);
          th_myfunc_2 <= th_myfunc_2_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_3 <= th_myfunc_3_init;
      _th_myfunc_3_called <= 0;
      _th_myfunc_3_tid_24 <= 0;
      _th_myfunc_3_size_25 <= 0;
      _th_myfunc_3_tid_26 <= 0;
      _th_myfunc_3_size_27 <= 0;
      _th_myfunc_3_i_28 <= 0;
      _tmp_7 <= 0;
      _th_myfunc_3_read_data_29 <= 0;
      _th_myfunc_3_write_data_30 <= 0;
    end else begin
      case(th_myfunc_3)
        th_myfunc_3_init: begin
          if(_th_myfunc_start[3] && (th_blink == 9)) begin
            _th_myfunc_3_called <= 1;
          end 
          if(_th_myfunc_start[3] && (th_blink == 9)) begin
            _th_myfunc_3_tid_24 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[3] && (th_blink == 9)) begin
            _th_myfunc_3_size_25 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[3]) begin
            th_myfunc_3 <= th_myfunc_3_1;
          end 
        end
        th_myfunc_3_1: begin
          _th_myfunc_3_tid_26 <= _th_myfunc_3_tid_24;
          _th_myfunc_3_size_27 <= _th_myfunc_3_size_25;
          th_myfunc_3 <= th_myfunc_3_2;
        end
        th_myfunc_3_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_3;
          end 
        end
        th_myfunc_3_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 3))) begin
            th_myfunc_3 <= th_myfunc_3_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 3)) begin
            th_myfunc_3 <= th_myfunc_3_4;
          end 
        end
        th_myfunc_3_4: begin
          $display("Thread %d Lock", _th_myfunc_3_tid_26);
          th_myfunc_3 <= th_myfunc_3_5;
        end
        th_myfunc_3_5: begin
          _th_myfunc_3_i_28 <= 0;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_6: begin
          if(_th_myfunc_3_i_28 < _th_myfunc_3_size_27) begin
            th_myfunc_3 <= th_myfunc_3_7;
          end else begin
            th_myfunc_3 <= th_myfunc_3_13;
          end
        end
        th_myfunc_3_7: begin
          if(_tmp_6) begin
            _tmp_7 <= myram_0_rdata;
          end 
          if(_tmp_6) begin
            th_myfunc_3 <= th_myfunc_3_8;
          end 
        end
        th_myfunc_3_8: begin
          _th_myfunc_3_read_data_29 <= _tmp_7;
          th_myfunc_3 <= th_myfunc_3_9;
        end
        th_myfunc_3_9: begin
          _th_myfunc_3_write_data_30 <= _th_myfunc_3_read_data_29 + _th_myfunc_3_tid_26 + _th_myfunc_3_i_28;
          th_myfunc_3 <= th_myfunc_3_10;
        end
        th_myfunc_3_10: begin
          th_myfunc_3 <= th_myfunc_3_11;
        end
        th_myfunc_3_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_3_tid_26, _th_myfunc_3_i_28, _th_myfunc_3_write_data_30);
          th_myfunc_3 <= th_myfunc_3_12;
        end
        th_myfunc_3_12: begin
          _th_myfunc_3_i_28 <= _th_myfunc_3_i_28 + 1;
          th_myfunc_3 <= th_myfunc_3_6;
        end
        th_myfunc_3_13: begin
          th_myfunc_3 <= th_myfunc_3_14;
        end
        th_myfunc_3_14: begin
          $display("Thread %d Unlock", _th_myfunc_3_tid_26);
          th_myfunc_3 <= th_myfunc_3_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_4 <= th_myfunc_4_init;
      _th_myfunc_4_called <= 0;
      _th_myfunc_4_tid_31 <= 0;
      _th_myfunc_4_size_32 <= 0;
      _th_myfunc_4_tid_33 <= 0;
      _th_myfunc_4_size_34 <= 0;
      _th_myfunc_4_i_35 <= 0;
      _tmp_9 <= 0;
      _th_myfunc_4_read_data_36 <= 0;
      _th_myfunc_4_write_data_37 <= 0;
    end else begin
      case(th_myfunc_4)
        th_myfunc_4_init: begin
          if(_th_myfunc_start[4] && (th_blink == 9)) begin
            _th_myfunc_4_called <= 1;
          end 
          if(_th_myfunc_start[4] && (th_blink == 9)) begin
            _th_myfunc_4_tid_31 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[4] && (th_blink == 9)) begin
            _th_myfunc_4_size_32 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[4]) begin
            th_myfunc_4 <= th_myfunc_4_1;
          end 
        end
        th_myfunc_4_1: begin
          _th_myfunc_4_tid_33 <= _th_myfunc_4_tid_31;
          _th_myfunc_4_size_34 <= _th_myfunc_4_size_32;
          th_myfunc_4 <= th_myfunc_4_2;
        end
        th_myfunc_4_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_3;
          end 
        end
        th_myfunc_4_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 4))) begin
            th_myfunc_4 <= th_myfunc_4_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 4)) begin
            th_myfunc_4 <= th_myfunc_4_4;
          end 
        end
        th_myfunc_4_4: begin
          $display("Thread %d Lock", _th_myfunc_4_tid_33);
          th_myfunc_4 <= th_myfunc_4_5;
        end
        th_myfunc_4_5: begin
          _th_myfunc_4_i_35 <= 0;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_6: begin
          if(_th_myfunc_4_i_35 < _th_myfunc_4_size_34) begin
            th_myfunc_4 <= th_myfunc_4_7;
          end else begin
            th_myfunc_4 <= th_myfunc_4_13;
          end
        end
        th_myfunc_4_7: begin
          if(_tmp_8) begin
            _tmp_9 <= myram_0_rdata;
          end 
          if(_tmp_8) begin
            th_myfunc_4 <= th_myfunc_4_8;
          end 
        end
        th_myfunc_4_8: begin
          _th_myfunc_4_read_data_36 <= _tmp_9;
          th_myfunc_4 <= th_myfunc_4_9;
        end
        th_myfunc_4_9: begin
          _th_myfunc_4_write_data_37 <= _th_myfunc_4_read_data_36 + _th_myfunc_4_tid_33 + _th_myfunc_4_i_35;
          th_myfunc_4 <= th_myfunc_4_10;
        end
        th_myfunc_4_10: begin
          th_myfunc_4 <= th_myfunc_4_11;
        end
        th_myfunc_4_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_4_tid_33, _th_myfunc_4_i_35, _th_myfunc_4_write_data_37);
          th_myfunc_4 <= th_myfunc_4_12;
        end
        th_myfunc_4_12: begin
          _th_myfunc_4_i_35 <= _th_myfunc_4_i_35 + 1;
          th_myfunc_4 <= th_myfunc_4_6;
        end
        th_myfunc_4_13: begin
          th_myfunc_4 <= th_myfunc_4_14;
        end
        th_myfunc_4_14: begin
          $display("Thread %d Unlock", _th_myfunc_4_tid_33);
          th_myfunc_4 <= th_myfunc_4_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_5 <= th_myfunc_5_init;
      _th_myfunc_5_called <= 0;
      _th_myfunc_5_tid_38 <= 0;
      _th_myfunc_5_size_39 <= 0;
      _th_myfunc_5_tid_40 <= 0;
      _th_myfunc_5_size_41 <= 0;
      _th_myfunc_5_i_42 <= 0;
      _tmp_11 <= 0;
      _th_myfunc_5_read_data_43 <= 0;
      _th_myfunc_5_write_data_44 <= 0;
    end else begin
      case(th_myfunc_5)
        th_myfunc_5_init: begin
          if(_th_myfunc_start[5] && (th_blink == 9)) begin
            _th_myfunc_5_called <= 1;
          end 
          if(_th_myfunc_start[5] && (th_blink == 9)) begin
            _th_myfunc_5_tid_38 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[5] && (th_blink == 9)) begin
            _th_myfunc_5_size_39 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[5]) begin
            th_myfunc_5 <= th_myfunc_5_1;
          end 
        end
        th_myfunc_5_1: begin
          _th_myfunc_5_tid_40 <= _th_myfunc_5_tid_38;
          _th_myfunc_5_size_41 <= _th_myfunc_5_size_39;
          th_myfunc_5 <= th_myfunc_5_2;
        end
        th_myfunc_5_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_3;
          end 
        end
        th_myfunc_5_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 5))) begin
            th_myfunc_5 <= th_myfunc_5_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 5)) begin
            th_myfunc_5 <= th_myfunc_5_4;
          end 
        end
        th_myfunc_5_4: begin
          $display("Thread %d Lock", _th_myfunc_5_tid_40);
          th_myfunc_5 <= th_myfunc_5_5;
        end
        th_myfunc_5_5: begin
          _th_myfunc_5_i_42 <= 0;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_6: begin
          if(_th_myfunc_5_i_42 < _th_myfunc_5_size_41) begin
            th_myfunc_5 <= th_myfunc_5_7;
          end else begin
            th_myfunc_5 <= th_myfunc_5_13;
          end
        end
        th_myfunc_5_7: begin
          if(_tmp_10) begin
            _tmp_11 <= myram_0_rdata;
          end 
          if(_tmp_10) begin
            th_myfunc_5 <= th_myfunc_5_8;
          end 
        end
        th_myfunc_5_8: begin
          _th_myfunc_5_read_data_43 <= _tmp_11;
          th_myfunc_5 <= th_myfunc_5_9;
        end
        th_myfunc_5_9: begin
          _th_myfunc_5_write_data_44 <= _th_myfunc_5_read_data_43 + _th_myfunc_5_tid_40 + _th_myfunc_5_i_42;
          th_myfunc_5 <= th_myfunc_5_10;
        end
        th_myfunc_5_10: begin
          th_myfunc_5 <= th_myfunc_5_11;
        end
        th_myfunc_5_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_5_tid_40, _th_myfunc_5_i_42, _th_myfunc_5_write_data_44);
          th_myfunc_5 <= th_myfunc_5_12;
        end
        th_myfunc_5_12: begin
          _th_myfunc_5_i_42 <= _th_myfunc_5_i_42 + 1;
          th_myfunc_5 <= th_myfunc_5_6;
        end
        th_myfunc_5_13: begin
          th_myfunc_5 <= th_myfunc_5_14;
        end
        th_myfunc_5_14: begin
          $display("Thread %d Unlock", _th_myfunc_5_tid_40);
          th_myfunc_5 <= th_myfunc_5_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_6 <= th_myfunc_6_init;
      _th_myfunc_6_called <= 0;
      _th_myfunc_6_tid_45 <= 0;
      _th_myfunc_6_size_46 <= 0;
      _th_myfunc_6_tid_47 <= 0;
      _th_myfunc_6_size_48 <= 0;
      _th_myfunc_6_i_49 <= 0;
      _tmp_13 <= 0;
      _th_myfunc_6_read_data_50 <= 0;
      _th_myfunc_6_write_data_51 <= 0;
    end else begin
      case(th_myfunc_6)
        th_myfunc_6_init: begin
          if(_th_myfunc_start[6] && (th_blink == 9)) begin
            _th_myfunc_6_called <= 1;
          end 
          if(_th_myfunc_start[6] && (th_blink == 9)) begin
            _th_myfunc_6_tid_45 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[6] && (th_blink == 9)) begin
            _th_myfunc_6_size_46 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[6]) begin
            th_myfunc_6 <= th_myfunc_6_1;
          end 
        end
        th_myfunc_6_1: begin
          _th_myfunc_6_tid_47 <= _th_myfunc_6_tid_45;
          _th_myfunc_6_size_48 <= _th_myfunc_6_size_46;
          th_myfunc_6 <= th_myfunc_6_2;
        end
        th_myfunc_6_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_3;
          end 
        end
        th_myfunc_6_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 6))) begin
            th_myfunc_6 <= th_myfunc_6_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 6)) begin
            th_myfunc_6 <= th_myfunc_6_4;
          end 
        end
        th_myfunc_6_4: begin
          $display("Thread %d Lock", _th_myfunc_6_tid_47);
          th_myfunc_6 <= th_myfunc_6_5;
        end
        th_myfunc_6_5: begin
          _th_myfunc_6_i_49 <= 0;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_6: begin
          if(_th_myfunc_6_i_49 < _th_myfunc_6_size_48) begin
            th_myfunc_6 <= th_myfunc_6_7;
          end else begin
            th_myfunc_6 <= th_myfunc_6_13;
          end
        end
        th_myfunc_6_7: begin
          if(_tmp_12) begin
            _tmp_13 <= myram_0_rdata;
          end 
          if(_tmp_12) begin
            th_myfunc_6 <= th_myfunc_6_8;
          end 
        end
        th_myfunc_6_8: begin
          _th_myfunc_6_read_data_50 <= _tmp_13;
          th_myfunc_6 <= th_myfunc_6_9;
        end
        th_myfunc_6_9: begin
          _th_myfunc_6_write_data_51 <= _th_myfunc_6_read_data_50 + _th_myfunc_6_tid_47 + _th_myfunc_6_i_49;
          th_myfunc_6 <= th_myfunc_6_10;
        end
        th_myfunc_6_10: begin
          th_myfunc_6 <= th_myfunc_6_11;
        end
        th_myfunc_6_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_6_tid_47, _th_myfunc_6_i_49, _th_myfunc_6_write_data_51);
          th_myfunc_6 <= th_myfunc_6_12;
        end
        th_myfunc_6_12: begin
          _th_myfunc_6_i_49 <= _th_myfunc_6_i_49 + 1;
          th_myfunc_6 <= th_myfunc_6_6;
        end
        th_myfunc_6_13: begin
          th_myfunc_6 <= th_myfunc_6_14;
        end
        th_myfunc_6_14: begin
          $display("Thread %d Unlock", _th_myfunc_6_tid_47);
          th_myfunc_6 <= th_myfunc_6_15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_myfunc_7 <= th_myfunc_7_init;
      _th_myfunc_7_called <= 0;
      _th_myfunc_7_tid_52 <= 0;
      _th_myfunc_7_size_53 <= 0;
      _th_myfunc_7_tid_54 <= 0;
      _th_myfunc_7_size_55 <= 0;
      _th_myfunc_7_i_56 <= 0;
      _tmp_15 <= 0;
      _th_myfunc_7_read_data_57 <= 0;
      _th_myfunc_7_write_data_58 <= 0;
    end else begin
      case(th_myfunc_7)
        th_myfunc_7_init: begin
          if(_th_myfunc_start[7] && (th_blink == 9)) begin
            _th_myfunc_7_called <= 1;
          end 
          if(_th_myfunc_start[7] && (th_blink == 9)) begin
            _th_myfunc_7_tid_52 <= _th_blink_tid_2;
          end 
          if(_th_myfunc_start[7] && (th_blink == 9)) begin
            _th_myfunc_7_size_53 <= _th_blink_size_0;
          end 
          if((th_blink == 9) && _th_myfunc_start[7]) begin
            th_myfunc_7 <= th_myfunc_7_1;
          end 
        end
        th_myfunc_7_1: begin
          _th_myfunc_7_tid_54 <= _th_myfunc_7_tid_52;
          _th_myfunc_7_size_55 <= _th_myfunc_7_size_53;
          th_myfunc_7 <= th_myfunc_7_2;
        end
        th_myfunc_7_2: begin
          if(!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_3;
          end 
        end
        th_myfunc_7_3: begin
          if(!(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 7))) begin
            th_myfunc_7 <= th_myfunc_7_2;
          end 
          if(__myram_mutex_lock_reg && (__myram_mutex_lock_id == 7)) begin
            th_myfunc_7 <= th_myfunc_7_4;
          end 
        end
        th_myfunc_7_4: begin
          $display("Thread %d Lock", _th_myfunc_7_tid_54);
          th_myfunc_7 <= th_myfunc_7_5;
        end
        th_myfunc_7_5: begin
          _th_myfunc_7_i_56 <= 0;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_6: begin
          if(_th_myfunc_7_i_56 < _th_myfunc_7_size_55) begin
            th_myfunc_7 <= th_myfunc_7_7;
          end else begin
            th_myfunc_7 <= th_myfunc_7_13;
          end
        end
        th_myfunc_7_7: begin
          if(_tmp_14) begin
            _tmp_15 <= myram_0_rdata;
          end 
          if(_tmp_14) begin
            th_myfunc_7 <= th_myfunc_7_8;
          end 
        end
        th_myfunc_7_8: begin
          _th_myfunc_7_read_data_57 <= _tmp_15;
          th_myfunc_7 <= th_myfunc_7_9;
        end
        th_myfunc_7_9: begin
          _th_myfunc_7_write_data_58 <= _th_myfunc_7_read_data_57 + _th_myfunc_7_tid_54 + _th_myfunc_7_i_56;
          th_myfunc_7 <= th_myfunc_7_10;
        end
        th_myfunc_7_10: begin
          th_myfunc_7 <= th_myfunc_7_11;
        end
        th_myfunc_7_11: begin
          $display("Thread %d ram[%d] <- %d", _th_myfunc_7_tid_54, _th_myfunc_7_i_56, _th_myfunc_7_write_data_58);
          th_myfunc_7 <= th_myfunc_7_12;
        end
        th_myfunc_7_12: begin
          _th_myfunc_7_i_56 <= _th_myfunc_7_i_56 + 1;
          th_myfunc_7 <= th_myfunc_7_6;
        end
        th_myfunc_7_13: begin
          th_myfunc_7 <= th_myfunc_7_14;
        end
        th_myfunc_7_14: begin
          $display("Thread %d Unlock", _th_myfunc_7_tid_54);
          th_myfunc_7 <= th_myfunc_7_15;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __myram_mutex_lock_reg <= 0;
      __myram_mutex_lock_id <= 0;
    end else begin
      if((th_myfunc_0 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 0))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 0;
      end 
      if((th_myfunc_0 == 13) && (__myram_mutex_lock_id == 0)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_1 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 1))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 1;
      end 
      if((th_myfunc_1 == 13) && (__myram_mutex_lock_id == 1)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_2 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 2))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 2;
      end 
      if((th_myfunc_2 == 13) && (__myram_mutex_lock_id == 2)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_3 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 3))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 3;
      end 
      if((th_myfunc_3 == 13) && (__myram_mutex_lock_id == 3)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_4 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 4))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 4;
      end 
      if((th_myfunc_4 == 13) && (__myram_mutex_lock_id == 4)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_5 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 5))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 5;
      end 
      if((th_myfunc_5 == 13) && (__myram_mutex_lock_id == 5)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_6 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 6))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 6;
      end 
      if((th_myfunc_6 == 13) && (__myram_mutex_lock_id == 6)) begin
        __myram_mutex_lock_reg <= 0;
      end 
      if((th_myfunc_7 == 2) && (!__myram_mutex_lock_reg || (__myram_mutex_lock_id == 7))) begin
        __myram_mutex_lock_reg <= 1;
        __myram_mutex_lock_id <= 7;
      end 
      if((th_myfunc_7 == 13) && (__myram_mutex_lock_id == 7)) begin
        __myram_mutex_lock_reg <= 0;
      end 
    end
  end


endmodule



module myram
(
  input CLK,
  input [10-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_ram_own_mutex.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
