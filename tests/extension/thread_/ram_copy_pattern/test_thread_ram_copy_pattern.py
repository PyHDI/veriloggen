from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_copy_pattern

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

  reg [10-1:0] ram0_0_addr;
  wire [32-1:0] ram0_0_rdata;
  reg [32-1:0] ram0_0_wdata;
  reg ram0_0_wenable;

  ram0
  inst_ram0
  (
    .CLK(CLK),
    .ram0_0_addr(ram0_0_addr),
    .ram0_0_rdata(ram0_0_rdata),
    .ram0_0_wdata(ram0_0_wdata),
    .ram0_0_wenable(ram0_0_wenable)
  );

  reg [10-1:0] ram1_0_addr;
  wire [32-1:0] ram1_0_rdata;
  reg [32-1:0] ram1_0_wdata;
  reg ram1_0_wenable;

  ram1
  inst_ram1
  (
    .CLK(CLK),
    .ram1_0_addr(ram1_0_addr),
    .ram1_0_rdata(ram1_0_rdata),
    .ram1_0_wdata(ram1_0_wdata),
    .ram1_0_wenable(ram1_0_wenable)
  );

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_wdata_2;
  reg _ram0_cond_0_1;
  reg [32-1:0] _copy_ram0_ram1_fsm;
  localparam _copy_ram0_ram1_fsm_init = 0;
  wire _copy_ram0_ram1_start_flag;
  reg _copy_ram0_ram1_start;
  reg _copy_ram0_ram1_end_flag;
  reg _copy_ram0_ram1_term_sink;
  reg _copy_ram0_ram1_source_busy;
  reg _copy_ram0_ram1_sink_busy;
  reg _copy_ram0_ram1_src_idle;
  reg [3-1:0] _copy_ram0_ram1_src_source_mode;
  reg [32-1:0] _copy_ram0_ram1_src_source_offset;
  reg [33-1:0] _copy_ram0_ram1_src_source_size;
  reg [32-1:0] _copy_ram0_ram1_src_source_stride;
  reg [33-1:0] _copy_ram0_ram1_src_source_count;
  reg [32-1:0] _copy_ram0_ram1_src_source_offset_buf;
  reg [32-1:0] _copy_ram0_ram1_src_source_stride_buf;
  reg [8-1:0] _copy_ram0_ram1_src_source_ram_sel;
  reg [32-1:0] _copy_ram0_ram1_src_source_ram_raddr;
  reg _copy_ram0_ram1_src_source_ram_renable;
  wire [32-1:0] _copy_ram0_ram1_src_source_ram_rdata;
  reg _copy_ram0_ram1_src_source_ram_rvalid;
  reg [32-1:0] _copy_ram0_ram1_src_source_empty_data;
  reg [3-1:0] _copy_ram0_ram1_dst_sink_mode;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_offset;
  reg [33-1:0] _copy_ram0_ram1_dst_sink_size;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_stride;
  reg [33-1:0] _copy_ram0_ram1_dst_sink_count;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_offset_buf;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_stride_buf;
  reg [8-1:0] _copy_ram0_ram1_dst_sink_ram_sel;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_waddr;
  reg _copy_ram0_ram1_dst_sink_wenable;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_wdata;
  wire signed [32-1:0] copy_ram0_ram1_src_data;
  wire signed [32-1:0] copy_ram0_ram1_dst_data;
  assign copy_ram0_ram1_dst_data = copy_ram0_ram1_src_data;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_cur_offset_0;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_cur_offset_1;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_cur_offset_2;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_cur_offset_3;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_0;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_1;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_2;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_3;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_0;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_1;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_2;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_3;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_count_0;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_count_1;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_count_2;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_count_3;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_buf_0;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_buf_1;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_buf_2;
  reg [33-1:0] _source_copy_ram0_ram1_src_pat_size_buf_3;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_buf_0;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_buf_1;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_buf_2;
  reg [32-1:0] _source_copy_ram0_ram1_src_pat_stride_buf_3;
  reg _set_flag_0;
  reg _tmp_1;
  reg _ram0_cond_1_1;
  reg _ram0_cond_2_1;
  reg _ram0_cond_2_2;
  assign _copy_ram0_ram1_src_source_ram_rdata = (_copy_ram0_ram1_src_source_ram_sel == 1)? ram0_0_rdata : 0;
  localparam _tmp_2 = 1;
  wire [_tmp_2-1:0] _tmp_3;
  assign _tmp_3 = _copy_ram0_ram1_src_source_ram_renable && (_copy_ram0_ram1_src_source_ram_sel == 1);
  reg [_tmp_2-1:0] __tmp_3_1;
  reg signed [32-1:0] __variable_wdata_0;
  assign copy_ram0_ram1_src_data = __variable_wdata_0;
  reg [32-1:0] _copy_ram0_ram1_src_source_pat_fsm_0;
  localparam _copy_ram0_ram1_src_source_pat_fsm_0_init = 0;
  wire [32-1:0] _copy_ram0_ram1_src_source_pat_all_offset;
  assign _copy_ram0_ram1_src_source_pat_all_offset = _copy_ram0_ram1_src_source_offset_buf + _source_copy_ram0_ram1_src_pat_cur_offset_0 + _source_copy_ram0_ram1_src_pat_cur_offset_1 + _source_copy_ram0_ram1_src_pat_cur_offset_2 + _source_copy_ram0_ram1_src_pat_cur_offset_3;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_cur_offset_0;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_cur_offset_1;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_cur_offset_2;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_cur_offset_3;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_0;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_1;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_2;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_3;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_0;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_1;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_2;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_3;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_count_0;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_count_1;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_count_2;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_count_3;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_buf_0;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_buf_1;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_buf_2;
  reg [33-1:0] _sink_copy_ram0_ram1_dst_pat_size_buf_3;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_buf_0;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_buf_1;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_buf_2;
  reg [32-1:0] _sink_copy_ram0_ram1_dst_pat_stride_buf_3;
  reg _set_flag_4;
  reg [32-1:0] __copy_ram0_ram1_dst_sink_offset_0_1;
  reg [32-1:0] __copy_ram0_ram1_dst_sink_offset_0_2;
  reg [32-1:0] __copy_ram0_ram1_dst_sink_offset_0_3;
  reg __stream_seq_0_cond_1_1;
  reg __stream_seq_0_cond_1_2;
  reg __stream_seq_0_cond_1_3;
  reg [33-1:0] __sink_copy_ram0_ram1_dst_pat_size_0_2_1;
  reg [33-1:0] __sink_copy_ram0_ram1_dst_pat_size_0_2_2;
  reg [33-1:0] __sink_copy_ram0_ram1_dst_pat_size_0_2_3;
  reg __stream_seq_0_cond_3_1;
  reg __stream_seq_0_cond_3_2;
  reg __stream_seq_0_cond_3_3;
  reg __stream_seq_0_cond_4_1;
  reg __stream_seq_0_cond_4_2;
  reg __stream_seq_0_cond_4_3;
  reg __stream_seq_0_cond_5_1;
  reg __stream_seq_0_cond_5_2;
  reg __stream_seq_0_cond_5_3;
  reg __stream_seq_0_cond_6_1;
  reg __stream_seq_0_cond_6_2;
  reg __stream_seq_0_cond_6_3;
  reg __set_flag_4_1;
  reg __set_flag_4_2;
  reg __set_flag_4_3;
  reg _ram1_cond_0_1;
  reg __copy_ram0_ram1_start_1;
  reg __copy_ram0_ram1_start_2;
  reg __copy_ram0_ram1_start_3;
  reg __copy_ram0_ram1_start_4;
  reg [32-1:0] _copy_ram0_ram1_dst_sink_pat_fsm_1;
  localparam _copy_ram0_ram1_dst_sink_pat_fsm_1_init = 0;
  wire [32-1:0] _copy_ram0_ram1_dst_sink_pat_all_offset;
  assign _copy_ram0_ram1_dst_sink_pat_all_offset = _copy_ram0_ram1_dst_sink_offset_buf + _sink_copy_ram0_ram1_dst_pat_cur_offset_0 + _sink_copy_ram0_ram1_dst_pat_cur_offset_1 + _sink_copy_ram0_ram1_dst_pat_cur_offset_2 + _sink_copy_ram0_ram1_dst_pat_cur_offset_3;
  reg _set_flag_5;
  assign _copy_ram0_ram1_start_flag = (_set_flag_5)? 1 : 0;
  wire _copy_ram0_ram1_done;
  assign _copy_ram0_ram1_done = _copy_ram0_ram1_src_idle;
  reg [2-1:0] _copy_ram0_ram1_sink_wait_count;
  localparam _tmp_6 = 1;
  wire [_tmp_6-1:0] _tmp_7;
  assign _tmp_7 = _copy_ram0_ram1_fsm == 3;
  reg [_tmp_6-1:0] __tmp_7_1;
  reg [_tmp_6-1:0] __tmp_7_2;
  reg [_tmp_6-1:0] __tmp_7_3;
  reg [_tmp_6-1:0] __tmp_7_4;
  localparam _tmp_8 = 1;
  wire [_tmp_8-1:0] _tmp_9;
  assign _tmp_9 = _copy_ram0_ram1_fsm == 3;
  reg [_tmp_8-1:0] __tmp_9_1;
  reg [_tmp_8-1:0] __tmp_9_2;
  reg [_tmp_8-1:0] __tmp_9_3;
  reg [_tmp_8-1:0] __tmp_9_4;
  localparam _tmp_10 = 1;
  wire [_tmp_10-1:0] _tmp_11;
  assign _tmp_11 = _copy_ram0_ram1_fsm == 3;
  reg [_tmp_10-1:0] __tmp_11_1;
  reg [_tmp_10-1:0] __tmp_11_2;
  reg [_tmp_10-1:0] __tmp_11_3;
  reg [_tmp_10-1:0] __tmp_11_4;
  localparam _tmp_12 = 1;
  wire [_tmp_12-1:0] _tmp_13;
  assign _tmp_13 = _copy_ram0_ram1_fsm == 3;
  reg [_tmp_12-1:0] __tmp_13_1;
  reg [_tmp_12-1:0] __tmp_13_2;
  reg [_tmp_12-1:0] __tmp_13_3;
  reg [_tmp_12-1:0] __tmp_13_4;
  reg signed [32-1:0] _th_blink_sum_3;
  reg _tmp_14;
  reg _ram1_cond_1_1;
  reg _ram1_cond_2_1;
  reg _ram1_cond_2_2;
  reg signed [32-1:0] _tmp_15;
  reg signed [32-1:0] _th_blink_rdata_4;

  always @(posedge CLK) begin
    if(RST) begin
      ram0_0_addr <= 0;
      ram0_0_wdata <= 0;
      ram0_0_wenable <= 0;
      _ram0_cond_0_1 <= 0;
      _ram0_cond_1_1 <= 0;
      _tmp_1 <= 0;
      _ram0_cond_2_1 <= 0;
      _ram0_cond_2_2 <= 0;
    end else begin
      if(_ram0_cond_2_2) begin
        _tmp_1 <= 0;
      end 
      if(_ram0_cond_0_1) begin
        ram0_0_wenable <= 0;
      end 
      if(_ram0_cond_1_1) begin
        _tmp_1 <= 1;
      end 
      _ram0_cond_2_2 <= _ram0_cond_2_1;
      if(th_blink == 4) begin
        ram0_0_addr <= _th_blink_i_1;
        ram0_0_wdata <= _th_blink_wdata_2;
        ram0_0_wenable <= 1;
      end 
      _ram0_cond_0_1 <= th_blink == 4;
      if(_copy_ram0_ram1_src_source_ram_renable && (_copy_ram0_ram1_src_source_ram_sel == 1)) begin
        ram0_0_addr <= _copy_ram0_ram1_src_source_ram_raddr;
      end 
      _ram0_cond_1_1 <= _copy_ram0_ram1_src_source_ram_renable && (_copy_ram0_ram1_src_source_ram_sel == 1);
      _ram0_cond_2_1 <= _copy_ram0_ram1_src_source_ram_renable && (_copy_ram0_ram1_src_source_ram_sel == 1);
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram1_0_addr <= 0;
      ram1_0_wdata <= 0;
      ram1_0_wenable <= 0;
      _ram1_cond_0_1 <= 0;
      _ram1_cond_1_1 <= 0;
      _tmp_14 <= 0;
      _ram1_cond_2_1 <= 0;
      _ram1_cond_2_2 <= 0;
    end else begin
      if(_ram1_cond_2_2) begin
        _tmp_14 <= 0;
      end 
      if(_ram1_cond_0_1) begin
        ram1_0_wenable <= 0;
      end 
      if(_ram1_cond_1_1) begin
        _tmp_14 <= 1;
      end 
      _ram1_cond_2_2 <= _ram1_cond_2_1;
      if(_copy_ram0_ram1_dst_sink_wenable && (_copy_ram0_ram1_dst_sink_ram_sel == 2)) begin
        ram1_0_addr <= _copy_ram0_ram1_dst_sink_waddr;
        ram1_0_wdata <= _copy_ram0_ram1_dst_sink_wdata;
        ram1_0_wenable <= 1;
      end 
      _ram1_cond_0_1 <= _copy_ram0_ram1_dst_sink_wenable && (_copy_ram0_ram1_dst_sink_ram_sel == 2);
      if(th_blink == 15) begin
        ram1_0_addr <= _th_blink_i_1;
      end 
      _ram1_cond_1_1 <= th_blink == 15;
      _ram1_cond_2_1 <= th_blink == 15;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_wdata_2 <= 0;
      _th_blink_sum_3 <= 0;
      _tmp_15 <= 0;
      _th_blink_rdata_4 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
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
            th_blink <= th_blink_7;
          end
        end
        th_blink_3: begin
          _th_blink_wdata_2 <= _th_blink_i_1;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          $display("wdata = %d", _th_blink_wdata_2);
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_7: begin
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          if(!_copy_ram0_ram1_source_busy && !_copy_ram0_ram1_sink_busy) begin
            th_blink <= th_blink_12;
          end 
        end
        th_blink_12: begin
          _th_blink_sum_3 <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_15;
          end else begin
            th_blink <= th_blink_20;
          end
        end
        th_blink_15: begin
          if(_tmp_14) begin
            _tmp_15 <= ram1_0_rdata;
          end 
          if(_tmp_14) begin
            th_blink <= th_blink_16;
          end 
        end
        th_blink_16: begin
          _th_blink_rdata_4 <= _tmp_15;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          _th_blink_sum_3 <= _th_blink_sum_3 + _th_blink_rdata_4;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          $display("rdata = %d", _th_blink_rdata_4);
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_14;
        end
        th_blink_20: begin
          $display("sum = %d", _th_blink_sum_3);
          th_blink <= th_blink_21;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _copy_ram0_ram1_src_idle <= 1;
      _copy_ram0_ram1_src_source_ram_rvalid <= 0;
      _copy_ram0_ram1_dst_sink_wenable <= 0;
      _set_flag_0 <= 0;
      _copy_ram0_ram1_src_source_mode <= 3'b0;
      _copy_ram0_ram1_src_source_offset <= 0;
      _source_copy_ram0_ram1_src_pat_size_0 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_0 <= 0;
      _source_copy_ram0_ram1_src_pat_size_1 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_1 <= 0;
      _source_copy_ram0_ram1_src_pat_size_2 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_2 <= 0;
      _source_copy_ram0_ram1_src_pat_size_3 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_3 <= 0;
      _copy_ram0_ram1_src_source_ram_sel <= 0;
      __tmp_3_1 <= 0;
      __variable_wdata_0 <= 0;
      _copy_ram0_ram1_src_source_offset_buf <= 0;
      _source_copy_ram0_ram1_src_pat_cur_offset_0 <= 0;
      _source_copy_ram0_ram1_src_pat_cur_offset_1 <= 0;
      _source_copy_ram0_ram1_src_pat_cur_offset_2 <= 0;
      _source_copy_ram0_ram1_src_pat_cur_offset_3 <= 0;
      _source_copy_ram0_ram1_src_pat_count_0 <= 0;
      _source_copy_ram0_ram1_src_pat_count_1 <= 0;
      _source_copy_ram0_ram1_src_pat_count_2 <= 0;
      _source_copy_ram0_ram1_src_pat_count_3 <= 0;
      _source_copy_ram0_ram1_src_pat_size_buf_0 <= 0;
      _source_copy_ram0_ram1_src_pat_size_buf_1 <= 0;
      _source_copy_ram0_ram1_src_pat_size_buf_2 <= 0;
      _source_copy_ram0_ram1_src_pat_size_buf_3 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_buf_0 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_buf_1 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_buf_2 <= 0;
      _source_copy_ram0_ram1_src_pat_stride_buf_3 <= 0;
      _copy_ram0_ram1_src_source_ram_raddr <= 0;
      _copy_ram0_ram1_src_source_ram_renable <= 0;
      _set_flag_4 <= 0;
      __copy_ram0_ram1_dst_sink_offset_0_1 <= 0;
      __copy_ram0_ram1_dst_sink_offset_0_2 <= 0;
      __copy_ram0_ram1_dst_sink_offset_0_3 <= 0;
      __stream_seq_0_cond_1_1 <= 0;
      __stream_seq_0_cond_1_2 <= 0;
      __stream_seq_0_cond_1_3 <= 0;
      _copy_ram0_ram1_dst_sink_mode <= 3'b0;
      _copy_ram0_ram1_dst_sink_offset <= 0;
      __sink_copy_ram0_ram1_dst_pat_size_0_2_1 <= 0;
      __sink_copy_ram0_ram1_dst_pat_size_0_2_2 <= 0;
      __sink_copy_ram0_ram1_dst_pat_size_0_2_3 <= 0;
      __stream_seq_0_cond_3_1 <= 0;
      __stream_seq_0_cond_3_2 <= 0;
      __stream_seq_0_cond_3_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_0 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_0 <= 0;
      __stream_seq_0_cond_4_1 <= 0;
      __stream_seq_0_cond_4_2 <= 0;
      __stream_seq_0_cond_4_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_1 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_1 <= 0;
      __stream_seq_0_cond_5_1 <= 0;
      __stream_seq_0_cond_5_2 <= 0;
      __stream_seq_0_cond_5_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_2 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_2 <= 0;
      __stream_seq_0_cond_6_1 <= 0;
      __stream_seq_0_cond_6_2 <= 0;
      __stream_seq_0_cond_6_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_3 <= 0;
      __set_flag_4_1 <= 0;
      __set_flag_4_2 <= 0;
      __set_flag_4_3 <= 0;
      _copy_ram0_ram1_dst_sink_ram_sel <= 0;
      __copy_ram0_ram1_start_1 <= 0;
      __copy_ram0_ram1_start_2 <= 0;
      __copy_ram0_ram1_start_3 <= 0;
      __copy_ram0_ram1_start_4 <= 0;
      _copy_ram0_ram1_dst_sink_offset_buf <= 0;
      _sink_copy_ram0_ram1_dst_pat_cur_offset_0 <= 0;
      _sink_copy_ram0_ram1_dst_pat_cur_offset_1 <= 0;
      _sink_copy_ram0_ram1_dst_pat_cur_offset_2 <= 0;
      _sink_copy_ram0_ram1_dst_pat_cur_offset_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_count_0 <= 0;
      _sink_copy_ram0_ram1_dst_pat_count_1 <= 0;
      _sink_copy_ram0_ram1_dst_pat_count_2 <= 0;
      _sink_copy_ram0_ram1_dst_pat_count_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_buf_0 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_buf_1 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_buf_2 <= 0;
      _sink_copy_ram0_ram1_dst_pat_size_buf_3 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_buf_0 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_buf_1 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_buf_2 <= 0;
      _sink_copy_ram0_ram1_dst_pat_stride_buf_3 <= 0;
      _copy_ram0_ram1_dst_sink_waddr <= 0;
      _copy_ram0_ram1_dst_sink_wdata <= 0;
      _set_flag_5 <= 0;
      __tmp_7_1 <= 0;
      __tmp_7_2 <= 0;
      __tmp_7_3 <= 0;
      __tmp_7_4 <= 0;
      __tmp_9_1 <= 0;
      __tmp_9_2 <= 0;
      __tmp_9_3 <= 0;
      __tmp_9_4 <= 0;
      __tmp_11_1 <= 0;
      __tmp_11_2 <= 0;
      __tmp_11_3 <= 0;
      __tmp_11_4 <= 0;
      __tmp_13_1 <= 0;
      __tmp_13_2 <= 0;
      __tmp_13_3 <= 0;
      __tmp_13_4 <= 0;
    end else begin
      if(__stream_seq_0_cond_1_3) begin
        _copy_ram0_ram1_dst_sink_mode <= 3'b10;
        _copy_ram0_ram1_dst_sink_offset <= __copy_ram0_ram1_dst_sink_offset_0_3;
      end 
      if(__stream_seq_0_cond_3_3) begin
        _sink_copy_ram0_ram1_dst_pat_size_0 <= __sink_copy_ram0_ram1_dst_pat_size_0_2_3;
        _sink_copy_ram0_ram1_dst_pat_stride_0 <= -'sd1;
      end 
      if(__stream_seq_0_cond_4_3) begin
        _sink_copy_ram0_ram1_dst_pat_size_1 <= 1;
        _sink_copy_ram0_ram1_dst_pat_stride_1 <= 0;
      end 
      if(__stream_seq_0_cond_5_3) begin
        _sink_copy_ram0_ram1_dst_pat_size_2 <= 1;
        _sink_copy_ram0_ram1_dst_pat_stride_2 <= 0;
      end 
      if(__stream_seq_0_cond_6_3) begin
        _sink_copy_ram0_ram1_dst_pat_size_3 <= 1;
        _sink_copy_ram0_ram1_dst_pat_stride_3 <= 0;
      end 
      __copy_ram0_ram1_dst_sink_offset_0_3 <= __copy_ram0_ram1_dst_sink_offset_0_2;
      __stream_seq_0_cond_1_3 <= __stream_seq_0_cond_1_2;
      __sink_copy_ram0_ram1_dst_pat_size_0_2_3 <= __sink_copy_ram0_ram1_dst_pat_size_0_2_2;
      __stream_seq_0_cond_3_3 <= __stream_seq_0_cond_3_2;
      __stream_seq_0_cond_4_3 <= __stream_seq_0_cond_4_2;
      __stream_seq_0_cond_5_3 <= __stream_seq_0_cond_5_2;
      __stream_seq_0_cond_6_3 <= __stream_seq_0_cond_6_2;
      __copy_ram0_ram1_dst_sink_offset_0_2 <= __copy_ram0_ram1_dst_sink_offset_0_1;
      __stream_seq_0_cond_1_2 <= __stream_seq_0_cond_1_1;
      __sink_copy_ram0_ram1_dst_pat_size_0_2_2 <= __sink_copy_ram0_ram1_dst_pat_size_0_2_1;
      __stream_seq_0_cond_3_2 <= __stream_seq_0_cond_3_1;
      __stream_seq_0_cond_4_2 <= __stream_seq_0_cond_4_1;
      __stream_seq_0_cond_5_2 <= __stream_seq_0_cond_5_1;
      __stream_seq_0_cond_6_2 <= __stream_seq_0_cond_6_1;
      _copy_ram0_ram1_src_idle <= _copy_ram0_ram1_src_idle;
      _copy_ram0_ram1_src_source_ram_rvalid <= 0;
      _copy_ram0_ram1_dst_sink_wenable <= 0;
      _set_flag_0 <= 0;
      if(th_blink == 7) begin
        _set_flag_0 <= 1;
      end 
      if(_set_flag_0) begin
        _copy_ram0_ram1_src_source_mode <= 3'b10;
        _copy_ram0_ram1_src_source_offset <= 0;
      end 
      if(_set_flag_0) begin
        _source_copy_ram0_ram1_src_pat_size_0 <= _th_blink_times_0;
        _source_copy_ram0_ram1_src_pat_stride_0 <= 1;
      end 
      if(_set_flag_0) begin
        _source_copy_ram0_ram1_src_pat_size_1 <= 1;
        _source_copy_ram0_ram1_src_pat_stride_1 <= 0;
      end 
      if(_set_flag_0) begin
        _source_copy_ram0_ram1_src_pat_size_2 <= 1;
        _source_copy_ram0_ram1_src_pat_stride_2 <= 0;
      end 
      if(_set_flag_0) begin
        _source_copy_ram0_ram1_src_pat_size_3 <= 1;
        _source_copy_ram0_ram1_src_pat_stride_3 <= 0;
      end 
      if(_set_flag_0) begin
        _copy_ram0_ram1_src_source_ram_sel <= 1;
      end 
      __tmp_3_1 <= _tmp_3;
      if(__tmp_3_1) begin
        _copy_ram0_ram1_src_source_ram_rvalid <= 1;
      end 
      if(_copy_ram0_ram1_src_source_ram_rvalid) begin
        __variable_wdata_0 <= _copy_ram0_ram1_src_source_ram_rdata;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _copy_ram0_ram1_src_idle <= 0;
        _copy_ram0_ram1_src_source_offset_buf <= _copy_ram0_ram1_src_source_offset;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_0 <= 0;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_1 <= 0;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_2 <= 0;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_3 <= 0;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_count_0 <= _source_copy_ram0_ram1_src_pat_size_0 - 1;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_count_1 <= _source_copy_ram0_ram1_src_pat_size_1 - 1;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_count_2 <= _source_copy_ram0_ram1_src_pat_size_2 - 1;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_count_3 <= _source_copy_ram0_ram1_src_pat_size_3 - 1;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_size_buf_0 <= _source_copy_ram0_ram1_src_pat_size_0;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_size_buf_1 <= _source_copy_ram0_ram1_src_pat_size_1;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_size_buf_2 <= _source_copy_ram0_ram1_src_pat_size_2;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_size_buf_3 <= _source_copy_ram0_ram1_src_pat_size_3;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_stride_buf_0 <= _source_copy_ram0_ram1_src_pat_stride_0;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_stride_buf_1 <= _source_copy_ram0_ram1_src_pat_stride_1;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_stride_buf_2 <= _source_copy_ram0_ram1_src_pat_stride_2;
      end 
      if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
        _source_copy_ram0_ram1_src_pat_stride_buf_3 <= _source_copy_ram0_ram1_src_pat_stride_3;
      end 
      if(_copy_ram0_ram1_src_source_pat_fsm_0 == 1) begin
        _copy_ram0_ram1_src_source_ram_raddr <= _copy_ram0_ram1_src_source_pat_all_offset;
        _copy_ram0_ram1_src_source_ram_renable <= 1;
      end 
      if(_copy_ram0_ram1_src_source_pat_fsm_0 == 1) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_0 <= _source_copy_ram0_ram1_src_pat_cur_offset_0 + _source_copy_ram0_ram1_src_pat_stride_buf_0;
        _source_copy_ram0_ram1_src_pat_count_0 <= _source_copy_ram0_ram1_src_pat_count_0 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && (_source_copy_ram0_ram1_src_pat_count_0 == 0)) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_0 <= 0;
        _source_copy_ram0_ram1_src_pat_count_0 <= _source_copy_ram0_ram1_src_pat_size_buf_0 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && (_source_copy_ram0_ram1_src_pat_count_0 == 0)) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_1 <= _source_copy_ram0_ram1_src_pat_cur_offset_1 + _source_copy_ram0_ram1_src_pat_stride_buf_1;
        _source_copy_ram0_ram1_src_pat_count_1 <= _source_copy_ram0_ram1_src_pat_count_1 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && (_source_copy_ram0_ram1_src_pat_count_0 == 0) && (_source_copy_ram0_ram1_src_pat_count_1 == 0)) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_1 <= 0;
        _source_copy_ram0_ram1_src_pat_count_1 <= _source_copy_ram0_ram1_src_pat_size_buf_1 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && ((_source_copy_ram0_ram1_src_pat_count_0 == 0) && (_source_copy_ram0_ram1_src_pat_count_1 == 0))) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_2 <= _source_copy_ram0_ram1_src_pat_cur_offset_2 + _source_copy_ram0_ram1_src_pat_stride_buf_2;
        _source_copy_ram0_ram1_src_pat_count_2 <= _source_copy_ram0_ram1_src_pat_count_2 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && ((_source_copy_ram0_ram1_src_pat_count_0 == 0) && (_source_copy_ram0_ram1_src_pat_count_1 == 0)) && (_source_copy_ram0_ram1_src_pat_count_2 == 0)) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_2 <= 0;
        _source_copy_ram0_ram1_src_pat_count_2 <= _source_copy_ram0_ram1_src_pat_size_buf_2 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && ((_source_copy_ram0_ram1_src_pat_count_0 == 0) && (_source_copy_ram0_ram1_src_pat_count_1 == 0) && (_source_copy_ram0_ram1_src_pat_count_2 == 0))) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_3 <= _source_copy_ram0_ram1_src_pat_cur_offset_3 + _source_copy_ram0_ram1_src_pat_stride_buf_3;
        _source_copy_ram0_ram1_src_pat_count_3 <= _source_copy_ram0_ram1_src_pat_count_3 - 1;
      end 
      if((_copy_ram0_ram1_src_source_pat_fsm_0 == 1) && ((_source_copy_ram0_ram1_src_pat_count_0 == 0) && (_source_copy_ram0_ram1_src_pat_count_1 == 0) && (_source_copy_ram0_ram1_src_pat_count_2 == 0)) && (_source_copy_ram0_ram1_src_pat_count_3 == 0)) begin
        _source_copy_ram0_ram1_src_pat_cur_offset_3 <= 0;
        _source_copy_ram0_ram1_src_pat_count_3 <= _source_copy_ram0_ram1_src_pat_size_buf_3 - 1;
      end 
      if(_copy_ram0_ram1_src_source_pat_fsm_0 == 2) begin
        _copy_ram0_ram1_src_source_ram_renable <= 0;
        _copy_ram0_ram1_src_idle <= 1;
      end 
      _set_flag_4 <= 0;
      if(th_blink == 8) begin
        _set_flag_4 <= 1;
      end 
      __copy_ram0_ram1_dst_sink_offset_0_1 <= _th_blink_times_0 - 1;
      __stream_seq_0_cond_1_1 <= _set_flag_4;
      __sink_copy_ram0_ram1_dst_pat_size_0_2_1 <= _th_blink_times_0;
      __stream_seq_0_cond_3_1 <= _set_flag_4;
      __stream_seq_0_cond_4_1 <= _set_flag_4;
      __stream_seq_0_cond_5_1 <= _set_flag_4;
      __stream_seq_0_cond_6_1 <= _set_flag_4;
      __set_flag_4_1 <= _set_flag_4;
      __set_flag_4_2 <= __set_flag_4_1;
      __set_flag_4_3 <= __set_flag_4_2;
      if(__set_flag_4_3) begin
        _copy_ram0_ram1_dst_sink_ram_sel <= 2;
      end 
      __copy_ram0_ram1_start_1 <= _copy_ram0_ram1_start;
      __copy_ram0_ram1_start_2 <= __copy_ram0_ram1_start_1;
      __copy_ram0_ram1_start_3 <= __copy_ram0_ram1_start_2;
      __copy_ram0_ram1_start_4 <= __copy_ram0_ram1_start_3;
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _copy_ram0_ram1_dst_sink_offset_buf <= _copy_ram0_ram1_dst_sink_offset;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_0 <= 0;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_1 <= 0;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_2 <= 0;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_3 <= 0;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_count_0 <= _sink_copy_ram0_ram1_dst_pat_size_0 - 1;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_count_1 <= _sink_copy_ram0_ram1_dst_pat_size_1 - 1;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_count_2 <= _sink_copy_ram0_ram1_dst_pat_size_2 - 1;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_count_3 <= _sink_copy_ram0_ram1_dst_pat_size_3 - 1;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_size_buf_0 <= _sink_copy_ram0_ram1_dst_pat_size_0;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_size_buf_1 <= _sink_copy_ram0_ram1_dst_pat_size_1;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_size_buf_2 <= _sink_copy_ram0_ram1_dst_pat_size_2;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_size_buf_3 <= _sink_copy_ram0_ram1_dst_pat_size_3;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_stride_buf_0 <= _sink_copy_ram0_ram1_dst_pat_stride_0;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_stride_buf_1 <= _sink_copy_ram0_ram1_dst_pat_stride_1;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_stride_buf_2 <= _sink_copy_ram0_ram1_dst_pat_stride_2;
      end 
      if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
        _sink_copy_ram0_ram1_dst_pat_stride_buf_3 <= _sink_copy_ram0_ram1_dst_pat_stride_3;
      end 
      if(_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) begin
        _copy_ram0_ram1_dst_sink_waddr <= _copy_ram0_ram1_dst_sink_pat_all_offset;
        _copy_ram0_ram1_dst_sink_wdata <= copy_ram0_ram1_dst_data;
        _copy_ram0_ram1_dst_sink_wenable <= 1;
      end 
      if(_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_0 <= _sink_copy_ram0_ram1_dst_pat_cur_offset_0 + _sink_copy_ram0_ram1_dst_pat_stride_buf_0;
        _sink_copy_ram0_ram1_dst_pat_count_0 <= _sink_copy_ram0_ram1_dst_pat_count_0 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && (_sink_copy_ram0_ram1_dst_pat_count_0 == 0)) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_0 <= 0;
        _sink_copy_ram0_ram1_dst_pat_count_0 <= _sink_copy_ram0_ram1_dst_pat_size_buf_0 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && (_sink_copy_ram0_ram1_dst_pat_count_0 == 0)) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_1 <= _sink_copy_ram0_ram1_dst_pat_cur_offset_1 + _sink_copy_ram0_ram1_dst_pat_stride_buf_1;
        _sink_copy_ram0_ram1_dst_pat_count_1 <= _sink_copy_ram0_ram1_dst_pat_count_1 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && (_sink_copy_ram0_ram1_dst_pat_count_0 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_1 == 0)) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_1 <= 0;
        _sink_copy_ram0_ram1_dst_pat_count_1 <= _sink_copy_ram0_ram1_dst_pat_size_buf_1 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && ((_sink_copy_ram0_ram1_dst_pat_count_0 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_1 == 0))) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_2 <= _sink_copy_ram0_ram1_dst_pat_cur_offset_2 + _sink_copy_ram0_ram1_dst_pat_stride_buf_2;
        _sink_copy_ram0_ram1_dst_pat_count_2 <= _sink_copy_ram0_ram1_dst_pat_count_2 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && ((_sink_copy_ram0_ram1_dst_pat_count_0 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_1 == 0)) && (_sink_copy_ram0_ram1_dst_pat_count_2 == 0)) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_2 <= 0;
        _sink_copy_ram0_ram1_dst_pat_count_2 <= _sink_copy_ram0_ram1_dst_pat_size_buf_2 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && ((_sink_copy_ram0_ram1_dst_pat_count_0 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_1 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_2 == 0))) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_3 <= _sink_copy_ram0_ram1_dst_pat_cur_offset_3 + _sink_copy_ram0_ram1_dst_pat_stride_buf_3;
        _sink_copy_ram0_ram1_dst_pat_count_3 <= _sink_copy_ram0_ram1_dst_pat_count_3 - 1;
      end 
      if((_copy_ram0_ram1_dst_sink_pat_fsm_1 == 1) && ((_sink_copy_ram0_ram1_dst_pat_count_0 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_1 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_2 == 0)) && (_sink_copy_ram0_ram1_dst_pat_count_3 == 0)) begin
        _sink_copy_ram0_ram1_dst_pat_cur_offset_3 <= 0;
        _sink_copy_ram0_ram1_dst_pat_count_3 <= _sink_copy_ram0_ram1_dst_pat_size_buf_3 - 1;
      end 
      _set_flag_5 <= 0;
      if(th_blink == 9) begin
        _set_flag_5 <= 1;
      end 
      __tmp_7_1 <= _tmp_7;
      __tmp_7_2 <= __tmp_7_1;
      __tmp_7_3 <= __tmp_7_2;
      __tmp_7_4 <= __tmp_7_3;
      __tmp_9_1 <= _tmp_9;
      __tmp_9_2 <= __tmp_9_1;
      __tmp_9_3 <= __tmp_9_2;
      __tmp_9_4 <= __tmp_9_3;
      __tmp_11_1 <= _tmp_11;
      __tmp_11_2 <= __tmp_11_1;
      __tmp_11_3 <= __tmp_11_2;
      __tmp_11_4 <= __tmp_11_3;
      __tmp_13_1 <= _tmp_13;
      __tmp_13_2 <= __tmp_13_1;
      __tmp_13_3 <= __tmp_13_2;
      __tmp_13_4 <= __tmp_13_3;
    end
  end

  localparam _copy_ram0_ram1_fsm_1 = 1;
  localparam _copy_ram0_ram1_fsm_2 = 2;
  localparam _copy_ram0_ram1_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _copy_ram0_ram1_fsm <= _copy_ram0_ram1_fsm_init;
      _copy_ram0_ram1_start <= 0;
      _copy_ram0_ram1_source_busy <= 0;
      _copy_ram0_ram1_sink_busy <= 0;
      _copy_ram0_ram1_sink_wait_count <= 0;
      _copy_ram0_ram1_end_flag <= 0;
      _copy_ram0_ram1_term_sink <= 0;
    end else begin
      _copy_ram0_ram1_start <= 0;
      if((_copy_ram0_ram1_sink_wait_count == 1) && !((_copy_ram0_ram1_fsm == 0) && _copy_ram0_ram1_start_flag) && __tmp_7_4) begin
        _copy_ram0_ram1_sink_busy <= 0;
      end 
      if((_copy_ram0_ram1_fsm == 0) && _copy_ram0_ram1_start_flag) begin
        _copy_ram0_ram1_sink_busy <= 1;
      end 
      if(!((_copy_ram0_ram1_fsm == 0) && _copy_ram0_ram1_start_flag) && __tmp_9_4) begin
        _copy_ram0_ram1_sink_wait_count <= _copy_ram0_ram1_sink_wait_count - 1;
      end 
      if((_copy_ram0_ram1_fsm == 0) && _copy_ram0_ram1_start_flag && !__tmp_11_4) begin
        _copy_ram0_ram1_sink_wait_count <= _copy_ram0_ram1_sink_wait_count + 1;
      end 
      _copy_ram0_ram1_end_flag <= 0;
      if(__tmp_13_4) begin
        _copy_ram0_ram1_end_flag <= 1;
      end 
      _copy_ram0_ram1_term_sink <= 0;
      if(_copy_ram0_ram1_fsm == 3) begin
        _copy_ram0_ram1_term_sink <= 1;
      end 
      case(_copy_ram0_ram1_fsm)
        _copy_ram0_ram1_fsm_init: begin
          if(_copy_ram0_ram1_start_flag) begin
            _copy_ram0_ram1_start <= 1;
            _copy_ram0_ram1_source_busy <= 1;
          end 
          if(_copy_ram0_ram1_start_flag) begin
            _copy_ram0_ram1_fsm <= _copy_ram0_ram1_fsm_1;
          end 
        end
        _copy_ram0_ram1_fsm_1: begin
          _copy_ram0_ram1_fsm <= _copy_ram0_ram1_fsm_2;
        end
        _copy_ram0_ram1_fsm_2: begin
          if(_copy_ram0_ram1_done) begin
            _copy_ram0_ram1_fsm <= _copy_ram0_ram1_fsm_3;
          end 
        end
        _copy_ram0_ram1_fsm_3: begin
          _copy_ram0_ram1_source_busy <= 0;
          _copy_ram0_ram1_fsm <= _copy_ram0_ram1_fsm_init;
        end
      endcase
    end
  end

  localparam _copy_ram0_ram1_src_source_pat_fsm_0_1 = 1;
  localparam _copy_ram0_ram1_src_source_pat_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _copy_ram0_ram1_src_source_pat_fsm_0 <= _copy_ram0_ram1_src_source_pat_fsm_0_init;
    end else begin
      case(_copy_ram0_ram1_src_source_pat_fsm_0)
        _copy_ram0_ram1_src_source_pat_fsm_0_init: begin
          if(_copy_ram0_ram1_start && _copy_ram0_ram1_src_source_mode & 3'b10) begin
            _copy_ram0_ram1_src_source_pat_fsm_0 <= _copy_ram0_ram1_src_source_pat_fsm_0_1;
          end 
        end
        _copy_ram0_ram1_src_source_pat_fsm_0_1: begin
          if((_source_copy_ram0_ram1_src_pat_count_0 == 0) && (_source_copy_ram0_ram1_src_pat_count_1 == 0) && (_source_copy_ram0_ram1_src_pat_count_2 == 0) && (_source_copy_ram0_ram1_src_pat_count_3 == 0)) begin
            _copy_ram0_ram1_src_source_pat_fsm_0 <= _copy_ram0_ram1_src_source_pat_fsm_0_2;
          end 
        end
        _copy_ram0_ram1_src_source_pat_fsm_0_2: begin
          _copy_ram0_ram1_src_source_pat_fsm_0 <= _copy_ram0_ram1_src_source_pat_fsm_0_init;
        end
      endcase
    end
  end

  localparam _copy_ram0_ram1_dst_sink_pat_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _copy_ram0_ram1_dst_sink_pat_fsm_1 <= _copy_ram0_ram1_dst_sink_pat_fsm_1_init;
    end else begin
      case(_copy_ram0_ram1_dst_sink_pat_fsm_1)
        _copy_ram0_ram1_dst_sink_pat_fsm_1_init: begin
          if(__copy_ram0_ram1_start_4 && _copy_ram0_ram1_dst_sink_mode & 3'b10) begin
            _copy_ram0_ram1_dst_sink_pat_fsm_1 <= _copy_ram0_ram1_dst_sink_pat_fsm_1_1;
          end 
        end
        _copy_ram0_ram1_dst_sink_pat_fsm_1_1: begin
          if((_sink_copy_ram0_ram1_dst_pat_count_0 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_1 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_2 == 0) && (_sink_copy_ram0_ram1_dst_pat_count_3 == 0)) begin
            _copy_ram0_ram1_dst_sink_pat_fsm_1 <= _copy_ram0_ram1_dst_sink_pat_fsm_1_init;
          end 
          if(_copy_ram0_ram1_term_sink) begin
            _copy_ram0_ram1_dst_sink_pat_fsm_1 <= _copy_ram0_ram1_dst_sink_pat_fsm_1_init;
          end 
        end
      endcase
    end
  end


endmodule



module ram0
(
  input CLK,
  input [10-1:0] ram0_0_addr,
  output [32-1:0] ram0_0_rdata,
  input [32-1:0] ram0_0_wdata,
  input ram0_0_wenable
);

  reg [10-1:0] ram0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram0_0_wenable) begin
      mem[ram0_0_addr] <= ram0_0_wdata;
    end 
    ram0_0_daddr <= ram0_0_addr;
  end

  assign ram0_0_rdata = mem[ram0_0_daddr];

endmodule



module ram1
(
  input CLK,
  input [10-1:0] ram1_0_addr,
  output [32-1:0] ram1_0_rdata,
  input [32-1:0] ram1_0_wdata,
  input ram1_0_wenable
);

  reg [10-1:0] ram1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram1_0_wenable) begin
      mem[ram1_0_addr] <= ram1_0_wdata;
    end 
    ram1_0_daddr <= ram1_0_addr;
  end

  assign ram1_0_rdata = mem[ram1_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_ram_copy_pattern.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
