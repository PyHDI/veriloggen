from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_stream_axi_stream_fifo


expected_verilog = """
module blinkled
(
  input CLK,
  input RST,
  output reg [32-1:0] maxi_awaddr,
  output reg [8-1:0] maxi_awlen,
  output [3-1:0] maxi_awsize,
  output [2-1:0] maxi_awburst,
  output [1-1:0] maxi_awlock,
  output [4-1:0] maxi_awcache,
  output [3-1:0] maxi_awprot,
  output [4-1:0] maxi_awqos,
  output [2-1:0] maxi_awuser,
  output reg maxi_awvalid,
  input maxi_awready,
  output reg [32-1:0] maxi_wdata,
  output reg [4-1:0] maxi_wstrb,
  output reg maxi_wlast,
  output reg maxi_wvalid,
  input maxi_wready,
  input [2-1:0] maxi_bresp,
  input maxi_bvalid,
  output maxi_bready,
  output reg [32-1:0] maxi_araddr,
  output reg [8-1:0] maxi_arlen,
  output [3-1:0] maxi_arsize,
  output [2-1:0] maxi_arburst,
  output [1-1:0] maxi_arlock,
  output [4-1:0] maxi_arcache,
  output [3-1:0] maxi_arprot,
  output [4-1:0] maxi_arqos,
  output [2-1:0] maxi_aruser,
  output reg maxi_arvalid,
  input maxi_arready,
  input [32-1:0] maxi_rdata,
  input [2-1:0] maxi_rresp,
  input maxi_rlast,
  input maxi_rvalid,
  output maxi_rready,
  input [32-1:0] saxi_awaddr,
  input [4-1:0] saxi_awcache,
  input [3-1:0] saxi_awprot,
  input saxi_awvalid,
  output saxi_awready,
  input [32-1:0] saxi_wdata,
  input [4-1:0] saxi_wstrb,
  input saxi_wvalid,
  output saxi_wready,
  output [2-1:0] saxi_bresp,
  output reg saxi_bvalid,
  input saxi_bready,
  input [32-1:0] saxi_araddr,
  input [4-1:0] saxi_arcache,
  input [3-1:0] saxi_arprot,
  input saxi_arvalid,
  output saxi_arready,
  output reg [32-1:0] saxi_rdata,
  output [2-1:0] saxi_rresp,
  output reg saxi_rvalid,
  input saxi_rready,
  input [32-1:0] axi_in_tdata,
  input axi_in_tvalid,
  output axi_in_tready,
  input axi_in_tlast,
  output reg [32-1:0] axi_out_tdata,
  output reg axi_out_tvalid,
  input axi_out_tready,
  output reg axi_out_tlast
);

  assign maxi_awsize = 2;
  assign maxi_awburst = 1;
  assign maxi_awlock = 0;
  assign maxi_awcache = 3;
  assign maxi_awprot = 0;
  assign maxi_awqos = 0;
  assign maxi_awuser = 0;
  assign maxi_bready = 1;
  assign maxi_arsize = 2;
  assign maxi_arburst = 1;
  assign maxi_arlock = 0;
  assign maxi_arcache = 3;
  assign maxi_arprot = 0;
  assign maxi_arqos = 0;
  assign maxi_aruser = 0;
  reg _maxi_read_start;
  reg [8-1:0] _maxi_read_op_sel;
  reg [32-1:0] _maxi_read_local_addr;
  reg [32-1:0] _maxi_read_global_addr;
  reg [33-1:0] _maxi_read_size;
  reg [32-1:0] _maxi_read_local_stride;
  reg _maxi_read_idle;
  reg _maxi_write_start;
  reg [8-1:0] _maxi_write_op_sel;
  reg [32-1:0] _maxi_write_local_addr;
  reg [32-1:0] _maxi_write_global_addr;
  reg [33-1:0] _maxi_write_size;
  reg [32-1:0] _maxi_write_local_stride;
  reg _maxi_write_idle;
  wire _maxi_write_data_done;
  assign saxi_bresp = 0;
  assign saxi_rresp = 0;
  reg signed [32-1:0] _saxi_register_0;
  reg signed [32-1:0] _saxi_register_1;
  reg signed [32-1:0] _saxi_register_2;
  reg signed [32-1:0] _saxi_register_3;
  reg signed [32-1:0] _saxi_register_4;
  reg signed [32-1:0] _saxi_register_5;
  reg signed [32-1:0] _saxi_register_6;
  reg signed [32-1:0] _saxi_register_7;
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg _saxi_flag_4;
  reg _saxi_flag_5;
  reg _saxi_flag_6;
  reg _saxi_flag_7;
  reg signed [32-1:0] _saxi_resetval_0;
  reg signed [32-1:0] _saxi_resetval_1;
  reg signed [32-1:0] _saxi_resetval_2;
  reg signed [32-1:0] _saxi_resetval_3;
  reg signed [32-1:0] _saxi_resetval_4;
  reg signed [32-1:0] _saxi_resetval_5;
  reg signed [32-1:0] _saxi_resetval_6;
  reg signed [32-1:0] _saxi_resetval_7;
  localparam _saxi_maskwidth = 3;
  localparam _saxi_mask = { _saxi_maskwidth{ 1'd1 } };
  localparam _saxi_shift = 2;
  reg [32-1:0] _saxi_register_fsm;
  localparam _saxi_register_fsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg _tmp_1;
  reg _tmp_2;
  reg _tmp_3;
  reg _tmp_4;
  assign saxi_awready = (_saxi_register_fsm == 0) && !_tmp_1 && !_tmp_2 && !saxi_bvalid && _tmp_3;
  assign saxi_arready = (_saxi_register_fsm == 0) && !_tmp_2 && !_tmp_1 && _tmp_4;
  reg [_saxi_maskwidth-1:0] _tmp_5;
  wire signed [32-1:0] _tmp_6;
  assign _tmp_6 = (_tmp_5 == 0)? _saxi_register_0 : 
                  (_tmp_5 == 1)? _saxi_register_1 : 
                  (_tmp_5 == 2)? _saxi_register_2 : 
                  (_tmp_5 == 3)? _saxi_register_3 : 
                  (_tmp_5 == 4)? _saxi_register_4 : 
                  (_tmp_5 == 5)? _saxi_register_5 : 
                  (_tmp_5 == 6)? _saxi_register_6 : 
                  (_tmp_5 == 7)? _saxi_register_7 : 'hx;
  wire _tmp_7;
  assign _tmp_7 = (_tmp_5 == 0)? _saxi_flag_0 : 
                  (_tmp_5 == 1)? _saxi_flag_1 : 
                  (_tmp_5 == 2)? _saxi_flag_2 : 
                  (_tmp_5 == 3)? _saxi_flag_3 : 
                  (_tmp_5 == 4)? _saxi_flag_4 : 
                  (_tmp_5 == 5)? _saxi_flag_5 : 
                  (_tmp_5 == 6)? _saxi_flag_6 : 
                  (_tmp_5 == 7)? _saxi_flag_7 : 'hx;
  wire signed [32-1:0] _tmp_8;
  assign _tmp_8 = (_tmp_5 == 0)? _saxi_resetval_0 : 
                  (_tmp_5 == 1)? _saxi_resetval_1 : 
                  (_tmp_5 == 2)? _saxi_resetval_2 : 
                  (_tmp_5 == 3)? _saxi_resetval_3 : 
                  (_tmp_5 == 4)? _saxi_resetval_4 : 
                  (_tmp_5 == 5)? _saxi_resetval_5 : 
                  (_tmp_5 == 6)? _saxi_resetval_6 : 
                  (_tmp_5 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg _axi_in_read_start;
  reg [8-1:0] _axi_in_read_op_sel;
  reg [32-1:0] _axi_in_read_local_addr;
  reg [33-1:0] _axi_in_read_size;
  reg [32-1:0] _axi_in_read_local_stride;
  reg _axi_in_read_idle;
  reg _axi_out_write_start;
  reg [8-1:0] _axi_out_write_op_sel;
  reg [32-1:0] _axi_out_write_local_addr;
  reg [33-1:0] _axi_out_write_size;
  reg [32-1:0] _axi_out_write_local_stride;
  reg _axi_out_write_idle;
  wire fifo_a_enq;
  wire [32-1:0] fifo_a_wdata;
  wire fifo_a_full;
  wire fifo_a_almost_full;
  wire fifo_a_deq;
  wire [32-1:0] fifo_a_rdata;
  wire fifo_a_empty;
  wire fifo_a_almost_empty;

  fifo_a
  inst_fifo_a
  (
    .CLK(CLK),
    .RST(RST),
    .fifo_a_enq(fifo_a_enq),
    .fifo_a_wdata(fifo_a_wdata),
    .fifo_a_full(fifo_a_full),
    .fifo_a_almost_full(fifo_a_almost_full),
    .fifo_a_deq(fifo_a_deq),
    .fifo_a_rdata(fifo_a_rdata),
    .fifo_a_empty(fifo_a_empty),
    .fifo_a_almost_empty(fifo_a_almost_empty)
  );

  reg [9-1:0] count_fifo_a;
  wire fifo_b_enq;
  wire [32-1:0] fifo_b_wdata;
  wire fifo_b_full;
  wire fifo_b_almost_full;
  wire fifo_b_deq;
  wire [32-1:0] fifo_b_rdata;
  wire fifo_b_empty;
  wire fifo_b_almost_empty;

  fifo_b
  inst_fifo_b
  (
    .CLK(CLK),
    .RST(RST),
    .fifo_b_enq(fifo_b_enq),
    .fifo_b_wdata(fifo_b_wdata),
    .fifo_b_full(fifo_b_full),
    .fifo_b_almost_full(fifo_b_almost_full),
    .fifo_b_deq(fifo_b_deq),
    .fifo_b_rdata(fifo_b_rdata),
    .fifo_b_empty(fifo_b_empty),
    .fifo_b_almost_empty(fifo_b_almost_empty)
  );

  reg [9-1:0] count_fifo_b;
  wire fifo_c_enq;
  wire [32-1:0] fifo_c_wdata;
  wire fifo_c_full;
  wire fifo_c_almost_full;
  wire fifo_c_deq;
  wire [32-1:0] fifo_c_rdata;
  wire fifo_c_empty;
  wire fifo_c_almost_empty;

  fifo_c
  inst_fifo_c
  (
    .CLK(CLK),
    .RST(RST),
    .fifo_c_enq(fifo_c_enq),
    .fifo_c_wdata(fifo_c_wdata),
    .fifo_c_full(fifo_c_full),
    .fifo_c_almost_full(fifo_c_almost_full),
    .fifo_c_deq(fifo_c_deq),
    .fifo_c_rdata(fifo_c_rdata),
    .fifo_c_empty(fifo_c_empty),
    .fifo_c_almost_empty(fifo_c_almost_empty)
  );

  reg [9-1:0] count_fifo_c;
  wire [10-1:0] ram_b_0_addr;
  wire [32-1:0] ram_b_0_rdata;
  wire [32-1:0] ram_b_0_wdata;
  wire ram_b_0_wenable;
  wire ram_b_0_enable;

  ram_b
  inst_ram_b
  (
    .CLK(CLK),
    .ram_b_0_addr(ram_b_0_addr),
    .ram_b_0_rdata(ram_b_0_rdata),
    .ram_b_0_wdata(ram_b_0_wdata),
    .ram_b_0_wenable(ram_b_0_wenable),
    .ram_b_0_enable(ram_b_0_enable)
  );

  reg _mystream_reduce_stream_ivalid;
  wire _mystream_reduce_stream_oready;
  reg [32-1:0] _mystream_reduce_fsm;
  localparam _mystream_reduce_fsm_init = 0;
  wire _mystream_reduce_run_flag;
  reg _mystream_reduce_source_start;
  reg _mystream_reduce_source_stop;
  reg _mystream_reduce_source_busy;
  wire _mystream_reduce_sink_start;
  wire _mystream_reduce_sink_stop;
  wire _mystream_reduce_sink_busy;
  wire _mystream_reduce_busy;
  reg _mystream_reduce_busy_buf;
  wire _mystream_reduce_is_root;
  assign _mystream_reduce_is_root = 1;
  reg _mystream_reduce_a_idle;
  reg [33-1:0] _mystream_reduce_a_source_count;
  reg [4-1:0] _mystream_reduce_a_source_mode;
  reg [4-1:0] _mystream_reduce_a_source_mode_buf;
  reg [32-1:0] _mystream_reduce_a_source_offset;
  reg [33-1:0] _mystream_reduce_a_source_size;
  reg [32-1:0] _mystream_reduce_a_source_stride;
  reg [32-1:0] _mystream_reduce_a_source_offset_buf;
  reg [33-1:0] _mystream_reduce_a_source_size_buf;
  reg [32-1:0] _mystream_reduce_a_source_stride_buf;
  reg [8-1:0] _mystream_reduce_a_source_sel;
  reg [32-1:0] _mystream_reduce_a_source_ram_raddr;
  reg _mystream_reduce_a_source_ram_renable;
  wire [32-1:0] _mystream_reduce_a_source_ram_rdata;
  reg _mystream_reduce_a_source_fifo_deq;
  wire [32-1:0] _mystream_reduce_a_source_fifo_rdata;
  reg [32-1:0] _mystream_reduce_a_source_empty_data;
  reg [32-1:0] _mystream_reduce_reduce_size_next_constant_data;
  reg _mystream_reduce_reduce_reset;
  reg [33-1:0] _mystream_reduce_sum_sink_count;
  reg [4-1:0] _mystream_reduce_sum_sink_mode;
  reg [4-1:0] _mystream_reduce_sum_sink_mode_buf;
  reg [32-1:0] _mystream_reduce_sum_sink_offset;
  reg [33-1:0] _mystream_reduce_sum_sink_size;
  reg [32-1:0] _mystream_reduce_sum_sink_stride;
  reg [32-1:0] _mystream_reduce_sum_sink_offset_buf;
  reg [33-1:0] _mystream_reduce_sum_sink_size_buf;
  reg [32-1:0] _mystream_reduce_sum_sink_stride_buf;
  reg [8-1:0] _mystream_reduce_sum_sink_sel;
  reg [32-1:0] _mystream_reduce_sum_sink_waddr;
  reg _mystream_reduce_sum_sink_wenable;
  reg [32-1:0] _mystream_reduce_sum_sink_wdata;
  reg _mystream_reduce_sum_sink_fifo_enq;
  reg [32-1:0] _mystream_reduce_sum_sink_fifo_wdata;
  reg [32-1:0] _mystream_reduce_sum_sink_immediate;
  reg [33-1:0] _mystream_reduce_sum_valid_sink_count;
  reg [4-1:0] _mystream_reduce_sum_valid_sink_mode;
  reg [4-1:0] _mystream_reduce_sum_valid_sink_mode_buf;
  reg [32-1:0] _mystream_reduce_sum_valid_sink_offset;
  reg [33-1:0] _mystream_reduce_sum_valid_sink_size;
  reg [32-1:0] _mystream_reduce_sum_valid_sink_stride;
  reg [32-1:0] _mystream_reduce_sum_valid_sink_offset_buf;
  reg [33-1:0] _mystream_reduce_sum_valid_sink_size_buf;
  reg [32-1:0] _mystream_reduce_sum_valid_sink_stride_buf;
  reg [8-1:0] _mystream_reduce_sum_valid_sink_sel;
  reg [32-1:0] _mystream_reduce_sum_valid_sink_waddr;
  reg _mystream_reduce_sum_valid_sink_wenable;
  reg [1-1:0] _mystream_reduce_sum_valid_sink_wdata;
  reg _mystream_reduce_sum_valid_sink_fifo_enq;
  reg [1-1:0] _mystream_reduce_sum_valid_sink_fifo_wdata;
  reg [1-1:0] _mystream_reduce_sum_valid_sink_immediate;
  reg _mystream_bias_stream_ivalid;
  wire _mystream_bias_stream_oready;
  reg [32-1:0] _mystream_bias_fsm;
  localparam _mystream_bias_fsm_init = 0;
  wire _mystream_bias_run_flag;
  reg _mystream_bias_source_start;
  reg _mystream_bias_source_stop;
  reg _mystream_bias_source_busy;
  wire _mystream_bias_sink_start;
  wire _mystream_bias_sink_stop;
  wire _mystream_bias_sink_busy;
  wire _mystream_bias_busy;
  reg _mystream_bias_busy_buf;
  wire _mystream_bias_is_root;
  assign _mystream_bias_is_root = 1;
  reg _mystream_bias_x_idle;
  reg [33-1:0] _mystream_bias_x_source_count;
  reg [4-1:0] _mystream_bias_x_source_mode;
  reg [4-1:0] _mystream_bias_x_source_mode_buf;
  reg [32-1:0] _mystream_bias_x_source_offset;
  reg [33-1:0] _mystream_bias_x_source_size;
  reg [32-1:0] _mystream_bias_x_source_stride;
  reg [32-1:0] _mystream_bias_x_source_offset_buf;
  reg [33-1:0] _mystream_bias_x_source_size_buf;
  reg [32-1:0] _mystream_bias_x_source_stride_buf;
  reg [8-1:0] _mystream_bias_x_source_sel;
  reg [32-1:0] _mystream_bias_x_source_ram_raddr;
  reg _mystream_bias_x_source_ram_renable;
  wire [32-1:0] _mystream_bias_x_source_ram_rdata;
  reg _mystream_bias_x_source_fifo_deq;
  wire [32-1:0] _mystream_bias_x_source_fifo_rdata;
  reg [32-1:0] _mystream_bias_x_source_empty_data;
  reg _mystream_bias_y_idle;
  reg [33-1:0] _mystream_bias_y_source_count;
  reg [4-1:0] _mystream_bias_y_source_mode;
  reg [4-1:0] _mystream_bias_y_source_mode_buf;
  reg [32-1:0] _mystream_bias_y_source_offset;
  reg [33-1:0] _mystream_bias_y_source_size;
  reg [32-1:0] _mystream_bias_y_source_stride;
  reg [32-1:0] _mystream_bias_y_source_offset_buf;
  reg [33-1:0] _mystream_bias_y_source_size_buf;
  reg [32-1:0] _mystream_bias_y_source_stride_buf;
  reg [8-1:0] _mystream_bias_y_source_sel;
  reg [32-1:0] _mystream_bias_y_source_ram_raddr;
  reg _mystream_bias_y_source_ram_renable;
  wire [32-1:0] _mystream_bias_y_source_ram_rdata;
  reg _mystream_bias_y_source_fifo_deq;
  wire [32-1:0] _mystream_bias_y_source_fifo_rdata;
  reg [32-1:0] _mystream_bias_y_source_empty_data;
  reg [33-1:0] _mystream_bias_z_sink_count;
  reg [4-1:0] _mystream_bias_z_sink_mode;
  reg [4-1:0] _mystream_bias_z_sink_mode_buf;
  reg [32-1:0] _mystream_bias_z_sink_offset;
  reg [33-1:0] _mystream_bias_z_sink_size;
  reg [32-1:0] _mystream_bias_z_sink_stride;
  reg [32-1:0] _mystream_bias_z_sink_offset_buf;
  reg [33-1:0] _mystream_bias_z_sink_size_buf;
  reg [32-1:0] _mystream_bias_z_sink_stride_buf;
  reg [8-1:0] _mystream_bias_z_sink_sel;
  reg [32-1:0] _mystream_bias_z_sink_waddr;
  reg _mystream_bias_z_sink_wenable;
  reg [32-1:0] _mystream_bias_z_sink_wdata;
  reg _mystream_bias_z_sink_fifo_enq;
  reg [32-1:0] _mystream_bias_z_sink_fifo_wdata;
  reg [32-1:0] _mystream_bias_z_sink_immediate;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_read_size_0;
  reg signed [32-1:0] _th_comp_write_size_1;
  reg signed [32-1:0] _th_comp_reduce_size_2;
  reg signed [32-1:0] _th_comp_bias_addr_3;
  reg axim_flag_9;
  reg [32-1:0] _d1_th_comp;
  reg _th_comp_cond_14_0_1;
  reg _maxi_ram_b_0_read_start;
  reg [8-1:0] _maxi_ram_b_0_read_op_sel;
  reg [32-1:0] _maxi_ram_b_0_read_local_addr;
  reg [32-1:0] _maxi_ram_b_0_read_global_addr;
  reg [33-1:0] _maxi_ram_b_0_read_size;
  reg [32-1:0] _maxi_ram_b_0_read_local_stride;
  reg [32-1:0] _maxi_read_fsm;
  localparam _maxi_read_fsm_init = 0;
  reg [32-1:0] _maxi_read_cur_global_addr;
  reg [33-1:0] _maxi_read_cur_size;
  reg [33-1:0] _maxi_read_rest_size;
  reg [32-1:0] _wdata_10;
  reg _wvalid_11;
  reg [33-1:0] _tmp_12;
  reg _tmp_13;
  wire [32-1:0] _dataflow__variable_odata_0;
  wire _dataflow__variable_ovalid_0;
  wire _dataflow__variable_oready_0;
  assign _dataflow__variable_oready_0 = (_tmp_12 > 0) && !_tmp_13;
  reg [10-1:0] _tmp_14;
  reg [32-1:0] _tmp_15;
  reg _tmp_16;
  assign ram_b_0_wdata = (_tmp_16)? _tmp_15 : 'hx;
  assign ram_b_0_wenable = (_tmp_16)? 1'd1 : 0;
  reg _ram_b_cond_0_1;
  reg [9-1:0] _tmp_17;
  reg _maxi_cond_0_1;
  assign maxi_rready = _maxi_read_fsm == 3;
  reg [32-1:0] _d1__maxi_read_fsm;
  reg __maxi_read_fsm_cond_3_0_1;
  reg axim_flag_18;
  reg __maxi_read_fsm_cond_4_1_1;
  reg axistreamin_flag_19;
  reg _th_comp_cond_19_1_1;
  reg _axi_in_fifo_a_read_start;
  reg [8-1:0] _axi_in_fifo_a_read_op_sel;
  reg [33-1:0] _axi_in_fifo_a_read_size;
  reg [32-1:0] _axi_in_read_fsm;
  localparam _axi_in_read_fsm_init = 0;
  reg [33-1:0] _axi_in_read_rest_size;
  assign axi_in_tready = (_axi_in_read_fsm == 1) && !fifo_a_almost_full;
  assign fifo_a_wdata = (axi_in_tready && axi_in_tvalid && (_axi_in_read_op_sel == 1))? axi_in_tdata : 'hx;
  assign fifo_a_enq = (axi_in_tready && axi_in_tvalid && (_axi_in_read_op_sel == 1))? axi_in_tready && axi_in_tvalid && (_axi_in_read_op_sel == 1) && !fifo_a_almost_full : 0;
  localparam _tmp_20 = 1;
  wire [_tmp_20-1:0] _tmp_21;
  assign _tmp_21 = !fifo_a_almost_full;
  reg [_tmp_20-1:0] __tmp_21_1;
  reg axistreamin_flag_22;
  reg [32-1:0] _d1__axi_in_read_fsm;
  reg __axi_in_read_fsm_cond_2_0_1;
  reg axistreamout_flag_23;
  reg _th_comp_cond_22_2_1;
  reg _axi_out_fifo_c_write_start;
  reg [8-1:0] _axi_out_fifo_c_write_op_sel;
  reg [33-1:0] _axi_out_fifo_c_write_size;
  reg [32-1:0] _axi_out_write_fsm;
  localparam _axi_out_write_fsm_init = 0;
  reg [33-1:0] _axi_out_write_counter;
  reg [33-1:0] _axi_out_write_fifo_counter_24;
  assign fifo_c_deq = ((_axi_out_write_fsm == 1) && (_axi_out_write_op_sel == 1) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty && (_axi_out_write_fifo_counter_24 > 0) && !fifo_c_empty)? 1 : 0;
  localparam _tmp_25 = 1;
  wire [_tmp_25-1:0] _tmp_26;
  assign _tmp_26 = (_axi_out_write_fsm == 1) && (_axi_out_write_op_sel == 1) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty && (_axi_out_write_fifo_counter_24 > 0) && !fifo_c_empty;
  reg [_tmp_25-1:0] __tmp_26_1;
  reg rlast_27;
  reg repeat_rvalid_28;
  reg _axi_out_cond_0_1;
  reg axistreamout_flag_29;
  reg [32-1:0] _d1__axi_out_write_fsm;
  reg __axi_out_write_fsm_cond_2_0_1;
  wire signed [32-1:0] mystream_reduce_a_data;
  wire signed [32-1:0] mystream_reduce_reduce_size_data;
  reg __mystream_reduce_stream_ivalid_1;
  reg __mystream_reduce_stream_ivalid_2;
  reg __mystream_reduce_stream_ivalid_3;
  reg __mystream_reduce_stream_ivalid_4;
  reg __mystream_reduce_stream_ivalid_5;
  reg __mystream_reduce_stream_ivalid_6;
  reg __mystream_reduce_stream_ivalid_7;
  reg __mystream_reduce_stream_ivalid_8;
  wire signed [64-1:0] _times_mul_odata_2;
  reg signed [64-1:0] _times_mul_odata_reg_2;
  wire signed [32-1:0] _times_data_2;
  assign _times_data_2 = _times_mul_odata_reg_2;
  wire _times_mul_update_2;
  assign _times_mul_update_2 = _mystream_reduce_stream_oready;

  multiplier_0
  _times_mul_2
  (
    .CLK(CLK),
    .update(_times_mul_update_2),
    .a(mystream_reduce_a_data),
    .b(mystream_reduce_a_data),
    .c(_times_mul_odata_2)
  );

  reg signed [32-1:0] __delay_data_11__variable_1;
  reg signed [1-1:0] __delay_data_18__variable_3;
  reg signed [32-1:0] __delay_data_12__delay_11__variable_1;
  reg signed [1-1:0] __delay_data_19__delay_18__variable_3;
  reg signed [32-1:0] __delay_data_13__delay_12__delay_11__variable_1;
  reg signed [1-1:0] __delay_data_20__delay_19__delay_18__variable_3;
  reg signed [32-1:0] __delay_data_14__delay_13__delay_12__delay_11__variable_1;
  reg signed [1-1:0] __delay_data_21__delay_20__delay_19__delay_18__variable_3;
  reg signed [32-1:0] __delay_data_15__delay_14__delay_13__delay_12____variable_1;
  reg signed [1-1:0] __delay_data_22__delay_21__delay_20__delay_19____variable_3;
  reg signed [32-1:0] __delay_data_16__delay_15__delay_14__delay_13____variable_1;
  reg signed [1-1:0] __delay_data_23__delay_22__delay_21__delay_20____variable_3;
  reg signed [32-1:0] __delay_data_17__delay_16__delay_15__delay_14____variable_1;
  reg signed [1-1:0] __delay_data_24__delay_23__delay_22__delay_21____variable_3;
  reg signed [32-1:0] _reduceadd_data_4;
  reg [33-1:0] _reduceadd_count_4;
  reg _reduceadd_prev_count_max_4;
  wire _reduceadd_reset_cond_4;
  assign _reduceadd_reset_cond_4 = __delay_data_24__delay_23__delay_22__delay_21____variable_3 || _reduceadd_prev_count_max_4;
  wire [33-1:0] _reduceadd_current_count_4;
  assign _reduceadd_current_count_4 = (_reduceadd_reset_cond_4)? 0 : _reduceadd_count_4;
  wire signed [32-1:0] _reduceadd_current_data_4;
  assign _reduceadd_current_data_4 = (_reduceadd_reset_cond_4)? 1'sd0 : _reduceadd_data_4;
  reg [1-1:0] _pulse_data_6;
  reg [33-1:0] _pulse_count_6;
  reg _pulse_prev_count_max_6;
  wire _pulse_reset_cond_6;
  assign _pulse_reset_cond_6 = __delay_data_24__delay_23__delay_22__delay_21____variable_3 || _pulse_prev_count_max_6;
  wire [33-1:0] _pulse_current_count_6;
  assign _pulse_current_count_6 = (_pulse_reset_cond_6)? 0 : _pulse_count_6;
  wire [1-1:0] _pulse_current_data_6;
  assign _pulse_current_data_6 = (_pulse_reset_cond_6)? 1'sd0 : _pulse_data_6;
  wire signed [32-1:0] mystream_reduce_sum_data;
  assign mystream_reduce_sum_data = _reduceadd_data_4;
  wire [1-1:0] mystream_reduce_sum_valid_data;
  assign mystream_reduce_sum_valid_data = _pulse_data_6;
  wire _set_flag_30;
  assign _set_flag_30 = th_comp == 25;
  assign fifo_a_deq = (_mystream_reduce_stream_oready && _mystream_reduce_a_source_fifo_deq && (_mystream_reduce_a_source_sel == 1) && !fifo_a_empty)? 1 : 0;
  localparam _tmp_31 = 1;
  wire [_tmp_31-1:0] _tmp_32;
  assign _tmp_32 = _mystream_reduce_stream_oready && _mystream_reduce_a_source_fifo_deq && (_mystream_reduce_a_source_sel == 1) && !fifo_a_empty;
  reg [_tmp_31-1:0] __tmp_32_1;
  assign _mystream_reduce_a_source_fifo_rdata = (_mystream_reduce_a_source_sel == 1)? fifo_a_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_reduce_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_reduce_a_source_fsm_0;
  localparam _mystream_reduce_a_source_fsm_0_init = 0;
  wire _set_flag_33;
  assign _set_flag_33 = th_comp == 26;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_reduce_reduce_size_data = __variable_wdata_1;
  wire _set_flag_34;
  assign _set_flag_34 = th_comp == 27;
  reg _tmp_35;
  reg _tmp_36;
  reg _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  reg _tmp_40;
  reg _tmp_41;
  reg _tmp_42;
  reg _tmp_43;
  reg _tmp_44;
  reg signed [32-1:0] _tmp_45;
  reg signed [32-1:0] _tmp_46;
  reg signed [32-1:0] _tmp_47;
  reg signed [32-1:0] _tmp_48;
  reg signed [32-1:0] _tmp_49;
  reg signed [32-1:0] _tmp_50;
  reg signed [32-1:0] _tmp_51;
  reg signed [32-1:0] _tmp_52;
  reg signed [32-1:0] _tmp_53;
  reg signed [32-1:0] _tmp_54;
  assign fifo_b_wdata = (_mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2))? _mystream_reduce_sum_sink_fifo_wdata : 'hx;
  assign fifo_b_enq = (_mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2))? _mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2) && !fifo_b_almost_full : 0;
  localparam _tmp_55 = 1;
  wire [_tmp_55-1:0] _tmp_56;
  assign _tmp_56 = !fifo_b_almost_full;
  reg [_tmp_55-1:0] __tmp_56_1;
  assign _mystream_reduce_stream_oready = ((_mystream_reduce_sink_busy && (_mystream_reduce_sum_sink_sel == 2))? !fifo_b_almost_full : 1) && (((_mystream_reduce_source_busy && (_mystream_reduce_a_source_sel == 1))? !fifo_a_empty || _mystream_reduce_a_idle : 1) && 1);
  reg [32-1:0] _mystream_reduce_sum_sink_fsm_1;
  localparam _mystream_reduce_sum_sink_fsm_1_init = 0;
  wire signed [32-1:0] mystream_bias_x_data;
  wire signed [32-1:0] mystream_bias_y_data;
  reg __mystream_bias_stream_ivalid_1;
  reg signed [32-1:0] _plus_data_10;
  wire signed [32-1:0] mystream_bias_z_data;
  assign mystream_bias_z_data = _plus_data_10;
  wire _set_flag_57;
  assign _set_flag_57 = th_comp == 28;
  assign fifo_b_deq = (_mystream_bias_stream_oready && _mystream_bias_x_source_fifo_deq && (_mystream_bias_x_source_sel == 1) && !fifo_b_empty)? 1 : 0;
  localparam _tmp_58 = 1;
  wire [_tmp_58-1:0] _tmp_59;
  assign _tmp_59 = _mystream_bias_stream_oready && _mystream_bias_x_source_fifo_deq && (_mystream_bias_x_source_sel == 1) && !fifo_b_empty;
  reg [_tmp_58-1:0] __tmp_59_1;
  assign _mystream_bias_x_source_fifo_rdata = (_mystream_bias_x_source_sel == 1)? fifo_b_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_8;
  assign mystream_bias_x_data = __variable_wdata_8;
  reg [32-1:0] _mystream_bias_x_source_fsm_0;
  localparam _mystream_bias_x_source_fsm_0_init = 0;
  wire _set_flag_60;
  assign _set_flag_60 = th_comp == 29;
  assign ram_b_0_addr = (_mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2))? _mystream_bias_y_source_ram_raddr : 
                        (_tmp_16)? _tmp_14 : 'hx;
  assign ram_b_0_enable = (_mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2))? 1'd1 : 
                          (_tmp_16)? 1'd1 : 0;
  localparam _tmp_61 = 1;
  wire [_tmp_61-1:0] _tmp_62;
  assign _tmp_62 = _mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2);
  reg [_tmp_61-1:0] __tmp_62_1;
  assign _mystream_bias_y_source_ram_rdata = (_mystream_bias_y_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_9;
  assign mystream_bias_y_data = __variable_wdata_9;
  reg [32-1:0] _mystream_bias_y_source_fsm_1;
  localparam _mystream_bias_y_source_fsm_1_init = 0;
  wire _set_flag_63;
  assign _set_flag_63 = th_comp == 30;
  reg _tmp_64;
  reg _tmp_65;
  reg _tmp_66;
  reg signed [32-1:0] _tmp_67;
  reg signed [32-1:0] _tmp_68;
  reg signed [32-1:0] _tmp_69;
  assign fifo_c_wdata = (_mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3))? _mystream_bias_z_sink_fifo_wdata : 'hx;
  assign fifo_c_enq = (_mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3))? _mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3) && !fifo_c_almost_full : 0;
  localparam _tmp_70 = 1;
  wire [_tmp_70-1:0] _tmp_71;
  assign _tmp_71 = !fifo_c_almost_full;
  reg [_tmp_70-1:0] __tmp_71_1;
  assign _mystream_bias_stream_oready = ((_mystream_bias_sink_busy && (_mystream_bias_z_sink_sel == 3))? !fifo_c_almost_full : 1) && (((_mystream_bias_source_busy && (_mystream_bias_x_source_sel == 1))? !fifo_b_empty || _mystream_bias_x_idle : 1) && 1);
  reg [32-1:0] _mystream_bias_z_sink_fsm_2;
  localparam _mystream_bias_z_sink_fsm_2_init = 0;
  wire _set_flag_72;
  assign _set_flag_72 = th_comp == 31;
  assign _mystream_reduce_run_flag = (_set_flag_72)? 1 : 0;
  reg _tmp_73;
  reg _tmp_74;
  reg _tmp_75;
  reg _tmp_76;
  reg _tmp_77;
  reg _tmp_78;
  reg _tmp_79;
  localparam _tmp_80 = 1;
  wire [_tmp_80-1:0] _tmp_81;
  assign _tmp_81 = _mystream_reduce_a_idle && (_mystream_reduce_fsm == 3);
  reg [_tmp_80-1:0] _tmp_82;
  localparam _tmp_83 = 1;
  wire [_tmp_83-1:0] _tmp_84;
  assign _tmp_84 = _mystream_reduce_a_idle && (_mystream_reduce_fsm == 3);
  reg [_tmp_83-1:0] _tmp_85;
  reg _tmp_86;
  reg _tmp_87;
  reg _tmp_88;
  reg _tmp_89;
  reg _tmp_90;
  reg _tmp_91;
  reg _tmp_92;
  reg _tmp_93;
  reg _tmp_94;
  reg _tmp_95;
  assign _mystream_reduce_sink_start = _tmp_95;
  reg _tmp_96;
  reg _tmp_97;
  reg _tmp_98;
  reg _tmp_99;
  reg _tmp_100;
  reg _tmp_101;
  reg _tmp_102;
  reg _tmp_103;
  assign _mystream_reduce_sink_stop = _tmp_103;
  reg _tmp_104;
  reg _tmp_105;
  reg _tmp_106;
  reg _tmp_107;
  reg _tmp_108;
  reg _tmp_109;
  reg _tmp_110;
  reg _tmp_111;
  reg _tmp_112;
  reg _tmp_113;
  assign _mystream_reduce_sink_busy = _tmp_113;
  reg __mystream_reduce_sink_busy_1;
  assign _mystream_reduce_busy = _mystream_reduce_source_busy || _mystream_reduce_sink_busy || _mystream_reduce_busy_buf;
  wire _set_flag_114;
  assign _set_flag_114 = th_comp == 33;
  assign _mystream_bias_run_flag = (_set_flag_114)? 1 : 0;
  reg _tmp_115;
  reg _tmp_116;
  reg _tmp_117;
  localparam _tmp_118 = 1;
  wire [_tmp_118-1:0] _tmp_119;
  assign _tmp_119 = _mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3);
  reg [_tmp_118-1:0] _tmp_120;
  reg _tmp_121;
  reg _tmp_122;
  reg _tmp_123;
  assign _mystream_bias_sink_start = _tmp_123;
  reg _tmp_124;
  assign _mystream_bias_sink_stop = _tmp_124;
  reg _tmp_125;
  reg _tmp_126;
  reg _tmp_127;
  assign _mystream_bias_sink_busy = _tmp_127;
  reg __mystream_bias_sink_busy_1;
  assign _mystream_bias_busy = _mystream_bias_source_busy || _mystream_bias_sink_busy || _mystream_bias_busy_buf;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      maxi_wdata <= 0;
      maxi_wstrb <= 0;
      maxi_wlast <= 0;
      maxi_wvalid <= 0;
      _maxi_ram_b_0_read_start <= 0;
      _maxi_ram_b_0_read_op_sel <= 0;
      _maxi_ram_b_0_read_local_addr <= 0;
      _maxi_ram_b_0_read_global_addr <= 0;
      _maxi_ram_b_0_read_size <= 0;
      _maxi_ram_b_0_read_local_stride <= 0;
      _maxi_read_idle <= 1;
      _maxi_read_op_sel <= 0;
      _maxi_read_local_addr <= 0;
      _maxi_read_global_addr <= 0;
      _maxi_read_size <= 0;
      _maxi_read_local_stride <= 0;
      maxi_araddr <= 0;
      maxi_arlen <= 0;
      maxi_arvalid <= 0;
      _tmp_17 <= 0;
      _maxi_cond_0_1 <= 0;
    end else begin
      if(_maxi_cond_0_1) begin
        maxi_arvalid <= 0;
      end 
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      maxi_wdata <= 0;
      maxi_wstrb <= 0;
      maxi_wlast <= 0;
      maxi_wvalid <= 0;
      _maxi_ram_b_0_read_start <= 0;
      if(axim_flag_9) begin
        _maxi_ram_b_0_read_start <= 1;
        _maxi_ram_b_0_read_op_sel <= 1;
        _maxi_ram_b_0_read_local_addr <= 0;
        _maxi_ram_b_0_read_global_addr <= _th_comp_bias_addr_3;
        _maxi_ram_b_0_read_size <= _th_comp_write_size_1;
        _maxi_ram_b_0_read_local_stride <= 1;
      end 
      if(_maxi_ram_b_0_read_start) begin
        _maxi_read_idle <= 0;
      end 
      if(_maxi_ram_b_0_read_start) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= _maxi_ram_b_0_read_op_sel;
        _maxi_read_local_addr <= _maxi_ram_b_0_read_local_addr;
        _maxi_read_global_addr <= _maxi_ram_b_0_read_global_addr;
        _maxi_read_size <= _maxi_ram_b_0_read_size;
        _maxi_read_local_stride <= _maxi_ram_b_0_read_local_stride;
      end 
      if((_maxi_read_fsm == 2) && ((maxi_arready || !maxi_arvalid) && (_tmp_17 == 0))) begin
        maxi_araddr <= _maxi_read_cur_global_addr;
        maxi_arlen <= _maxi_read_cur_size - 1;
        maxi_arvalid <= 1;
        _tmp_17 <= _maxi_read_cur_size;
      end 
      _maxi_cond_0_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
      if(maxi_rready && maxi_rvalid && (_tmp_17 > 0)) begin
        _tmp_17 <= _tmp_17 - 1;
      end 
      if(axim_flag_18) begin
        _maxi_read_idle <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_0 = _wdata_10;
  assign _dataflow__variable_ovalid_0 = _wvalid_11;

  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_0 <= 0;
      saxi_rdata <= 0;
      saxi_rvalid <= 0;
      _saxi_cond_0_1 <= 0;
      _saxi_register_0 <= 0;
      _saxi_flag_0 <= 0;
      _saxi_register_1 <= 0;
      _saxi_flag_1 <= 0;
      _saxi_register_2 <= 0;
      _saxi_flag_2 <= 0;
      _saxi_register_3 <= 0;
      _saxi_flag_3 <= 0;
      _saxi_register_4 <= 0;
      _saxi_flag_4 <= 0;
      _saxi_register_5 <= 0;
      _saxi_flag_5 <= 0;
      _saxi_register_6 <= 0;
      _saxi_flag_6 <= 0;
      _saxi_register_7 <= 0;
      _saxi_flag_7 <= 0;
    end else begin
      if(_saxi_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      if(saxi_bvalid && saxi_bready) begin
        saxi_bvalid <= 0;
      end 
      if(saxi_wvalid && saxi_wready) begin
        saxi_bvalid <= 1;
      end 
      _tmp_3 <= saxi_awvalid;
      _tmp_4 <= saxi_arvalid;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        _tmp_0 <= saxi_awaddr;
        _tmp_1 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        _tmp_0 <= saxi_araddr;
        _tmp_2 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= _tmp_6;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 0)) begin
        _saxi_register_0 <= _tmp_8;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 1)) begin
        _saxi_register_1 <= _tmp_8;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 2)) begin
        _saxi_register_2 <= _tmp_8;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 3)) begin
        _saxi_register_3 <= _tmp_8;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 4)) begin
        _saxi_register_4 <= _tmp_8;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 5)) begin
        _saxi_register_5 <= _tmp_8;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 6)) begin
        _saxi_register_6 <= _tmp_8;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 7)) begin
        _saxi_register_7 <= _tmp_8;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 7)) begin
        _saxi_register_7 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_4 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_5 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_6 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_comp == 2) && 0) begin
        _saxi_register_7 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 3) && 1) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_4 <= 1;
        _saxi_flag_4 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_5 <= 1;
        _saxi_flag_5 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_6 <= 1;
        _saxi_flag_6 <= 0;
      end 
      if((th_comp == 3) && 0) begin
        _saxi_register_7 <= 1;
        _saxi_flag_7 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 37) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_4 <= 0;
        _saxi_flag_4 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_5 <= 0;
        _saxi_flag_5 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_6 <= 0;
        _saxi_flag_6 <= 0;
      end 
      if((th_comp == 37) && 0) begin
        _saxi_register_7 <= 0;
        _saxi_flag_7 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(_tmp_2 || _tmp_1) begin
            _tmp_5 <= (_tmp_0 >> _saxi_shift) & _saxi_mask;
          end 
          if(_tmp_2) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(_tmp_1) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_2: begin
          _saxi_register_fsm <= _saxi_register_fsm_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_in_read_start <= 0;
      _axi_in_fifo_a_read_start <= 0;
      _axi_in_fifo_a_read_op_sel <= 0;
      _axi_in_fifo_a_read_size <= 0;
      _axi_in_read_idle <= 1;
      _axi_in_read_op_sel <= 0;
      _axi_in_read_size <= 0;
    end else begin
      _axi_in_read_start <= 0;
      _axi_in_fifo_a_read_start <= 0;
      if(axistreamin_flag_19) begin
        _axi_in_fifo_a_read_start <= 1;
        _axi_in_fifo_a_read_op_sel <= 1;
        _axi_in_fifo_a_read_size <= _th_comp_read_size_0;
      end 
      if(_axi_in_fifo_a_read_start) begin
        _axi_in_read_idle <= 0;
      end 
      if(_axi_in_fifo_a_read_start) begin
        _axi_in_read_start <= 1;
        _axi_in_read_op_sel <= _axi_in_fifo_a_read_op_sel;
        _axi_in_read_size <= _axi_in_fifo_a_read_size;
      end 
      if(axistreamin_flag_22) begin
        _axi_in_read_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_out_write_start <= 0;
      _axi_out_fifo_c_write_start <= 0;
      _axi_out_fifo_c_write_op_sel <= 0;
      _axi_out_fifo_c_write_size <= 0;
      _axi_out_write_idle <= 1;
      _axi_out_write_op_sel <= 0;
      _axi_out_write_size <= 0;
      rlast_27 <= 0;
      repeat_rvalid_28 <= 0;
      axi_out_tdata <= 0;
      axi_out_tvalid <= 0;
      axi_out_tlast <= 0;
      _axi_out_cond_0_1 <= 0;
    end else begin
      if(_axi_out_cond_0_1) begin
        axi_out_tvalid <= 0;
        axi_out_tlast <= 0;
      end 
      _axi_out_write_start <= 0;
      _axi_out_fifo_c_write_start <= 0;
      if(axistreamout_flag_23) begin
        _axi_out_fifo_c_write_start <= 1;
        _axi_out_fifo_c_write_op_sel <= 1;
        _axi_out_fifo_c_write_size <= _th_comp_write_size_1;
      end 
      if(_axi_out_fifo_c_write_start) begin
        _axi_out_write_idle <= 0;
      end 
      if(_axi_out_fifo_c_write_start) begin
        _axi_out_write_start <= 1;
        _axi_out_write_op_sel <= _axi_out_fifo_c_write_op_sel;
        _axi_out_write_size <= _axi_out_fifo_c_write_size;
      end 
      if((_axi_out_write_fsm == 1) && (_axi_out_write_op_sel == 1) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty && (_axi_out_write_fifo_counter_24 > 0)) begin
        rlast_27 <= _axi_out_write_fifo_counter_24 <= 1;
      end 
      repeat_rvalid_28 <= 0;
      if(__tmp_26_1 && !(axi_out_tready || !axi_out_tvalid)) begin
        repeat_rvalid_28 <= 1;
      end 
      if(repeat_rvalid_28 && !(axi_out_tready || !axi_out_tvalid)) begin
        repeat_rvalid_28 <= 1;
      end 
      if((__tmp_26_1 || repeat_rvalid_28) && (axi_out_tready || !axi_out_tvalid)) begin
        axi_out_tdata <= fifo_c_rdata;
        axi_out_tvalid <= 1;
        axi_out_tlast <= rlast_27;
      end 
      _axi_out_cond_0_1 <= 1;
      if(axi_out_tvalid && !axi_out_tready) begin
        axi_out_tvalid <= axi_out_tvalid;
        axi_out_tlast <= axi_out_tlast;
      end 
      if(axistreamout_flag_29) begin
        _axi_out_write_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_a <= 0;
      __tmp_21_1 <= 0;
      __tmp_32_1 <= 0;
    end else begin
      if(fifo_a_enq && !fifo_a_full && (fifo_a_deq && !fifo_a_empty)) begin
        count_fifo_a <= count_fifo_a;
      end else if(fifo_a_enq && !fifo_a_full) begin
        count_fifo_a <= count_fifo_a + 1;
      end else if(fifo_a_deq && !fifo_a_empty) begin
        count_fifo_a <= count_fifo_a - 1;
      end 
      __tmp_21_1 <= _tmp_21;
      __tmp_32_1 <= _tmp_32;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_b <= 0;
      __tmp_56_1 <= 0;
      __tmp_59_1 <= 0;
    end else begin
      if(fifo_b_enq && !fifo_b_full && (fifo_b_deq && !fifo_b_empty)) begin
        count_fifo_b <= count_fifo_b;
      end else if(fifo_b_enq && !fifo_b_full) begin
        count_fifo_b <= count_fifo_b + 1;
      end else if(fifo_b_deq && !fifo_b_empty) begin
        count_fifo_b <= count_fifo_b - 1;
      end 
      __tmp_56_1 <= _tmp_56;
      __tmp_59_1 <= _tmp_59;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_c <= 0;
      __tmp_26_1 <= 0;
      __tmp_71_1 <= 0;
    end else begin
      if(fifo_c_enq && !fifo_c_full && (fifo_c_deq && !fifo_c_empty)) begin
        count_fifo_c <= count_fifo_c;
      end else if(fifo_c_enq && !fifo_c_full) begin
        count_fifo_c <= count_fifo_c + 1;
      end else if(fifo_c_deq && !fifo_c_empty) begin
        count_fifo_c <= count_fifo_c - 1;
      end 
      __tmp_26_1 <= _tmp_26;
      __tmp_71_1 <= _tmp_71;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_14 <= 0;
      _tmp_12 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_13 <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_62_1 <= 0;
    end else begin
      if(_ram_b_cond_0_1) begin
        _tmp_16 <= 0;
        _tmp_13 <= 0;
      end 
      if(_maxi_read_start && (_maxi_read_op_sel == 1) && (_tmp_12 == 0)) begin
        _tmp_14 <= _maxi_read_local_addr - _maxi_read_local_stride;
        _tmp_12 <= _maxi_read_size;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 > 0)) begin
        _tmp_14 <= _tmp_14 + _maxi_read_local_stride;
        _tmp_15 <= _dataflow__variable_odata_0;
        _tmp_16 <= 1;
        _tmp_12 <= _tmp_12 - 1;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 == 1)) begin
        _tmp_13 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      __tmp_62_1 <= _tmp_62;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _mystream_reduce_a_source_ram_renable <= 0;
      _mystream_reduce_a_source_fifo_deq <= 0;
      _mystream_reduce_a_idle <= 1;
      _mystream_reduce_sum_sink_wenable <= 0;
      _mystream_reduce_sum_sink_fifo_enq <= 0;
      _mystream_reduce_sum_valid_sink_wenable <= 0;
      _mystream_reduce_sum_valid_sink_fifo_enq <= 0;
      __mystream_reduce_stream_ivalid_1 <= 0;
      __mystream_reduce_stream_ivalid_2 <= 0;
      __mystream_reduce_stream_ivalid_3 <= 0;
      __mystream_reduce_stream_ivalid_4 <= 0;
      __mystream_reduce_stream_ivalid_5 <= 0;
      __mystream_reduce_stream_ivalid_6 <= 0;
      __mystream_reduce_stream_ivalid_7 <= 0;
      __mystream_reduce_stream_ivalid_8 <= 0;
      _times_mul_odata_reg_2 <= 0;
      __delay_data_11__variable_1 <= 0;
      __delay_data_18__variable_3 <= 0;
      __delay_data_12__delay_11__variable_1 <= 0;
      __delay_data_19__delay_18__variable_3 <= 0;
      __delay_data_13__delay_12__delay_11__variable_1 <= 0;
      __delay_data_20__delay_19__delay_18__variable_3 <= 0;
      __delay_data_14__delay_13__delay_12__delay_11__variable_1 <= 0;
      __delay_data_21__delay_20__delay_19__delay_18__variable_3 <= 0;
      __delay_data_15__delay_14__delay_13__delay_12____variable_1 <= 0;
      __delay_data_22__delay_21__delay_20__delay_19____variable_3 <= 0;
      __delay_data_16__delay_15__delay_14__delay_13____variable_1 <= 0;
      __delay_data_23__delay_22__delay_21__delay_20____variable_3 <= 0;
      __delay_data_17__delay_16__delay_15__delay_14____variable_1 <= 0;
      __delay_data_24__delay_23__delay_22__delay_21____variable_3 <= 0;
      _reduceadd_data_4 <= 1'sd0;
      _reduceadd_count_4 <= 0;
      _reduceadd_prev_count_max_4 <= 0;
      _pulse_data_6 <= 1'sd0;
      _pulse_count_6 <= 0;
      _pulse_prev_count_max_6 <= 0;
      _mystream_reduce_a_source_mode <= 4'b0;
      _mystream_reduce_a_source_size <= 0;
      _mystream_reduce_a_source_sel <= 0;
      _mystream_reduce_a_source_size_buf <= 0;
      __variable_wdata_0 <= 0;
      _mystream_reduce_a_source_count <= 0;
      _mystream_reduce_reduce_size_next_constant_data <= 0;
      __variable_wdata_1 <= 0;
      _tmp_35 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
      _tmp_42 <= 0;
      _tmp_43 <= 0;
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_48 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _mystream_reduce_sum_sink_mode <= 4'b0;
      _mystream_reduce_sum_sink_size <= 0;
      _mystream_reduce_sum_sink_sel <= 0;
      _mystream_reduce_sum_sink_size_buf <= 0;
      _mystream_reduce_sum_sink_count <= 0;
      _mystream_reduce_sum_sink_fifo_wdata <= 0;
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_78 <= 0;
      _tmp_79 <= 0;
      _tmp_82 <= 0;
      _tmp_85 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _tmp_90 <= 0;
      _tmp_91 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _tmp_99 <= 0;
      _tmp_100 <= 0;
      _tmp_101 <= 0;
      _tmp_102 <= 0;
      _tmp_103 <= 0;
      _tmp_104 <= 0;
      _tmp_105 <= 0;
      _tmp_106 <= 0;
      _tmp_107 <= 0;
      _tmp_108 <= 0;
      _tmp_109 <= 0;
      _tmp_110 <= 0;
      _tmp_111 <= 0;
      _tmp_112 <= 0;
      _tmp_113 <= 0;
      __mystream_reduce_sink_busy_1 <= 0;
      _mystream_reduce_busy_buf <= 0;
    end else begin
      if(_mystream_reduce_stream_oready) begin
        _mystream_reduce_a_source_ram_renable <= 0;
        _mystream_reduce_a_source_fifo_deq <= 0;
      end 
      _mystream_reduce_a_idle <= _mystream_reduce_a_idle;
      if(_mystream_reduce_stream_oready) begin
        _mystream_reduce_sum_sink_wenable <= 0;
        _mystream_reduce_sum_sink_fifo_enq <= 0;
      end 
      if(_mystream_reduce_stream_oready) begin
        _mystream_reduce_sum_valid_sink_wenable <= 0;
        _mystream_reduce_sum_valid_sink_fifo_enq <= 0;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_1 <= _mystream_reduce_stream_ivalid;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_2 <= __mystream_reduce_stream_ivalid_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_3 <= __mystream_reduce_stream_ivalid_2;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_4 <= __mystream_reduce_stream_ivalid_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_5 <= __mystream_reduce_stream_ivalid_4;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_6 <= __mystream_reduce_stream_ivalid_5;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_7 <= __mystream_reduce_stream_ivalid_6;
      end 
      if(_mystream_reduce_stream_oready) begin
        __mystream_reduce_stream_ivalid_8 <= __mystream_reduce_stream_ivalid_7;
      end 
      if(_mystream_reduce_stream_oready) begin
        _times_mul_odata_reg_2 <= _times_mul_odata_2;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_11__variable_1 <= mystream_reduce_reduce_size_data;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_18__variable_3 <= _mystream_reduce_reduce_reset;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_12__delay_11__variable_1 <= __delay_data_11__variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_19__delay_18__variable_3 <= __delay_data_18__variable_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_13__delay_12__delay_11__variable_1 <= __delay_data_12__delay_11__variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_20__delay_19__delay_18__variable_3 <= __delay_data_19__delay_18__variable_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_14__delay_13__delay_12__delay_11__variable_1 <= __delay_data_13__delay_12__delay_11__variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_21__delay_20__delay_19__delay_18__variable_3 <= __delay_data_20__delay_19__delay_18__variable_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_15__delay_14__delay_13__delay_12____variable_1 <= __delay_data_14__delay_13__delay_12__delay_11__variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_22__delay_21__delay_20__delay_19____variable_3 <= __delay_data_21__delay_20__delay_19__delay_18__variable_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_16__delay_15__delay_14__delay_13____variable_1 <= __delay_data_15__delay_14__delay_13__delay_12____variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_23__delay_22__delay_21__delay_20____variable_3 <= __delay_data_22__delay_21__delay_20__delay_19____variable_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_17__delay_16__delay_15__delay_14____variable_1 <= __delay_data_16__delay_15__delay_14__delay_13____variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_24__delay_23__delay_22__delay_21____variable_3 <= __delay_data_23__delay_22__delay_21__delay_20____variable_3;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready && _reduceadd_reset_cond_4) begin
        _reduceadd_data_4 <= 1'sd0;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready) begin
        _reduceadd_data_4 <= _reduceadd_current_data_4 + _times_data_2;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready) begin
        _reduceadd_count_4 <= (_reduceadd_current_count_4 >= __delay_data_17__delay_16__delay_15__delay_14____variable_1 - 1)? 0 : _reduceadd_current_count_4 + 1;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready) begin
        _reduceadd_prev_count_max_4 <= _reduceadd_current_count_4 >= __delay_data_17__delay_16__delay_15__delay_14____variable_1 - 1;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready && _pulse_reset_cond_6) begin
        _pulse_data_6 <= 1'sd0;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready) begin
        _pulse_data_6 <= _pulse_current_count_6 >= __delay_data_17__delay_16__delay_15__delay_14____variable_1 - 1;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready) begin
        _pulse_count_6 <= (_pulse_current_count_6 >= __delay_data_17__delay_16__delay_15__delay_14____variable_1 - 1)? 0 : _pulse_current_count_6 + 1;
      end 
      if(__mystream_reduce_stream_ivalid_7 && _mystream_reduce_stream_oready) begin
        _pulse_prev_count_max_6 <= _pulse_current_count_6 >= __delay_data_17__delay_16__delay_15__delay_14____variable_1 - 1;
      end 
      if(_set_flag_30) begin
        _mystream_reduce_a_source_mode <= 4'b1000;
        _mystream_reduce_a_source_size <= _th_comp_read_size_0;
      end 
      if(_set_flag_30) begin
        _mystream_reduce_a_source_sel <= 1;
      end 
      if(_mystream_reduce_source_start && _mystream_reduce_a_source_mode & 4'b1000 && _mystream_reduce_stream_oready) begin
        _mystream_reduce_a_idle <= 0;
        _mystream_reduce_a_source_size_buf <= _mystream_reduce_a_source_size;
      end 
      if(_mystream_reduce_stream_oready && _mystream_reduce_source_busy && _mystream_reduce_is_root) begin
        __variable_wdata_0 <= _mystream_reduce_a_source_fifo_rdata;
      end 
      if((_mystream_reduce_a_source_fsm_0 == 1) && _mystream_reduce_stream_oready) begin
        _mystream_reduce_a_source_fifo_deq <= 1;
        _mystream_reduce_a_source_count <= _mystream_reduce_a_source_size_buf;
      end 
      if((_mystream_reduce_a_source_fsm_0 == 2) && _mystream_reduce_stream_oready) begin
        _mystream_reduce_a_source_fifo_deq <= 1;
        _mystream_reduce_a_source_count <= _mystream_reduce_a_source_count - 1;
      end 
      if((_mystream_reduce_a_source_fsm_0 == 2) && (_mystream_reduce_a_source_count == 1) && _mystream_reduce_stream_oready) begin
        _mystream_reduce_a_source_fifo_deq <= 0;
        _mystream_reduce_a_idle <= 1;
      end 
      if(_set_flag_33) begin
        _mystream_reduce_reduce_size_next_constant_data <= _th_comp_reduce_size_2;
      end 
      if(_mystream_reduce_source_start) begin
        __variable_wdata_1 <= _mystream_reduce_reduce_size_next_constant_data;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_35 <= _set_flag_34;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_36 <= _tmp_35;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_37 <= _tmp_36;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_38 <= _tmp_37;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_39 <= _tmp_38;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_40 <= _tmp_39;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_41 <= _tmp_40;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_42 <= _tmp_41;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_43 <= _tmp_42;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_44 <= _tmp_43;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_45 <= _th_comp_write_size_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_46 <= _tmp_45;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_47 <= _tmp_46;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_48 <= _tmp_47;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_49 <= _tmp_48;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_50 <= _tmp_49;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_51 <= _tmp_50;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_52 <= _tmp_51;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_53 <= _tmp_52;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_54 <= _tmp_53;
      end 
      if(_tmp_44) begin
        _mystream_reduce_sum_sink_mode <= 4'b1000;
        _mystream_reduce_sum_sink_size <= _tmp_54;
      end 
      if(_tmp_44) begin
        _mystream_reduce_sum_sink_sel <= 2;
      end 
      if(_mystream_reduce_sink_start && _mystream_reduce_sum_sink_mode & 4'b1000 && _mystream_reduce_stream_oready) begin
        _mystream_reduce_sum_sink_size_buf <= _mystream_reduce_sum_sink_size;
      end 
      if((_mystream_reduce_sum_sink_fsm_1 == 1) && _mystream_reduce_stream_oready) begin
        _mystream_reduce_sum_sink_count <= _mystream_reduce_sum_sink_size;
        _mystream_reduce_sum_sink_size_buf <= _mystream_reduce_sum_sink_size;
      end 
      if((_mystream_reduce_sum_sink_fsm_1 == 2) && mystream_reduce_sum_valid_data && _mystream_reduce_stream_oready) begin
        _mystream_reduce_sum_sink_fifo_wdata <= mystream_reduce_sum_data;
        _mystream_reduce_sum_sink_fifo_enq <= 1;
        _mystream_reduce_sum_sink_count <= _mystream_reduce_sum_sink_count - 1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_73 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_74 <= _tmp_73;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_75 <= _tmp_74;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_76 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_77 <= _tmp_76;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_78 <= _tmp_77;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_79 <= _tmp_78;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_82 <= _tmp_81;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_85 <= _tmp_84;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_86 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_87 <= _tmp_86;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_88 <= _tmp_87;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_89 <= _tmp_88;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_90 <= _tmp_89;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_91 <= _tmp_90;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_92 <= _tmp_91;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_93 <= _tmp_92;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_94 <= _tmp_93;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_95 <= _tmp_94;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_96 <= _mystream_reduce_source_stop;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_97 <= _tmp_96;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_98 <= _tmp_97;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_99 <= _tmp_98;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_100 <= _tmp_99;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_101 <= _tmp_100;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_102 <= _tmp_101;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_103 <= _tmp_102;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_104 <= _mystream_reduce_source_busy;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_105 <= _tmp_104;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_106 <= _tmp_105;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_107 <= _tmp_106;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_108 <= _tmp_107;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_109 <= _tmp_108;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_110 <= _tmp_109;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_111 <= _tmp_110;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_112 <= _tmp_111;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_113 <= _tmp_112;
      end 
      __mystream_reduce_sink_busy_1 <= _mystream_reduce_sink_busy;
      if(!_mystream_reduce_sink_busy && __mystream_reduce_sink_busy_1) begin
        _mystream_reduce_busy_buf <= 0;
      end 
      if(_mystream_reduce_source_busy) begin
        _mystream_reduce_busy_buf <= 1;
      end 
    end
  end

  localparam _mystream_reduce_fsm_1 = 1;
  localparam _mystream_reduce_fsm_2 = 2;
  localparam _mystream_reduce_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_reduce_fsm <= _mystream_reduce_fsm_init;
      _mystream_reduce_source_start <= 0;
      _mystream_reduce_source_busy <= 0;
      _mystream_reduce_source_stop <= 0;
      _mystream_reduce_stream_ivalid <= 0;
      _mystream_reduce_reduce_reset <= 1;
    end else begin
      if(_tmp_75 && _mystream_reduce_stream_oready) begin
        _mystream_reduce_stream_ivalid <= 1;
      end 
      if(_tmp_79 && _mystream_reduce_stream_oready) begin
        _mystream_reduce_reduce_reset <= 0;
      end 
      if(_mystream_reduce_stream_oready) begin
        _mystream_reduce_source_stop <= 0;
      end 
      if(_tmp_82 && _mystream_reduce_stream_oready) begin
        _mystream_reduce_stream_ivalid <= 0;
      end 
      if(_tmp_85 && _mystream_reduce_stream_oready) begin
        _mystream_reduce_reduce_reset <= 1;
      end 
      case(_mystream_reduce_fsm)
        _mystream_reduce_fsm_init: begin
          if(_mystream_reduce_run_flag) begin
            _mystream_reduce_source_start <= 1;
          end 
          if(_mystream_reduce_run_flag) begin
            _mystream_reduce_fsm <= _mystream_reduce_fsm_1;
          end 
        end
        _mystream_reduce_fsm_1: begin
          if(_mystream_reduce_source_start && _mystream_reduce_stream_oready) begin
            _mystream_reduce_source_start <= 0;
            _mystream_reduce_source_busy <= 1;
          end 
          if(_mystream_reduce_source_start && _mystream_reduce_stream_oready) begin
            _mystream_reduce_fsm <= _mystream_reduce_fsm_2;
          end 
        end
        _mystream_reduce_fsm_2: begin
          if(_mystream_reduce_stream_oready) begin
            _mystream_reduce_fsm <= _mystream_reduce_fsm_3;
          end 
        end
        _mystream_reduce_fsm_3: begin
          if(_mystream_reduce_stream_oready && (_mystream_reduce_a_idle && (_mystream_reduce_fsm == 3))) begin
            _mystream_reduce_source_stop <= 1;
            _mystream_reduce_source_busy <= 0;
          end 
          if(_mystream_reduce_stream_oready && (_mystream_reduce_a_idle && (_mystream_reduce_fsm == 3)) && _mystream_reduce_run_flag) begin
            _mystream_reduce_source_start <= 1;
          end 
          if(_mystream_reduce_stream_oready && (_mystream_reduce_a_idle && (_mystream_reduce_fsm == 3))) begin
            _mystream_reduce_fsm <= _mystream_reduce_fsm_init;
          end 
          if(_mystream_reduce_stream_oready && (_mystream_reduce_a_idle && (_mystream_reduce_fsm == 3)) && _mystream_reduce_run_flag) begin
            _mystream_reduce_fsm <= _mystream_reduce_fsm_1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _mystream_bias_x_source_ram_renable <= 0;
      _mystream_bias_x_source_fifo_deq <= 0;
      _mystream_bias_x_idle <= 1;
      _mystream_bias_y_source_ram_renable <= 0;
      _mystream_bias_y_source_fifo_deq <= 0;
      _mystream_bias_y_idle <= 1;
      _mystream_bias_z_sink_wenable <= 0;
      _mystream_bias_z_sink_fifo_enq <= 0;
      __mystream_bias_stream_ivalid_1 <= 0;
      _plus_data_10 <= 0;
      _mystream_bias_x_source_mode <= 4'b0;
      _mystream_bias_x_source_size <= 0;
      _mystream_bias_x_source_sel <= 0;
      _mystream_bias_x_source_size_buf <= 0;
      __variable_wdata_8 <= 0;
      _mystream_bias_x_source_count <= 0;
      _mystream_bias_y_source_mode <= 4'b0;
      _mystream_bias_y_source_offset <= 0;
      _mystream_bias_y_source_size <= 0;
      _mystream_bias_y_source_stride <= 0;
      _mystream_bias_y_source_sel <= 0;
      _mystream_bias_y_source_offset_buf <= 0;
      _mystream_bias_y_source_size_buf <= 0;
      _mystream_bias_y_source_stride_buf <= 0;
      __variable_wdata_9 <= 0;
      _mystream_bias_y_source_ram_raddr <= 0;
      _mystream_bias_y_source_count <= 0;
      _tmp_64 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _tmp_69 <= 0;
      _mystream_bias_z_sink_mode <= 4'b0;
      _mystream_bias_z_sink_size <= 0;
      _mystream_bias_z_sink_sel <= 0;
      _mystream_bias_z_sink_size_buf <= 0;
      _mystream_bias_z_sink_count <= 0;
      _mystream_bias_z_sink_fifo_wdata <= 0;
      _tmp_115 <= 0;
      _tmp_116 <= 0;
      _tmp_117 <= 0;
      _tmp_120 <= 0;
      _tmp_121 <= 0;
      _tmp_122 <= 0;
      _tmp_123 <= 0;
      _tmp_124 <= 0;
      _tmp_125 <= 0;
      _tmp_126 <= 0;
      _tmp_127 <= 0;
      __mystream_bias_sink_busy_1 <= 0;
      _mystream_bias_busy_buf <= 0;
    end else begin
      if(_mystream_bias_stream_oready) begin
        _mystream_bias_x_source_ram_renable <= 0;
        _mystream_bias_x_source_fifo_deq <= 0;
      end 
      _mystream_bias_x_idle <= _mystream_bias_x_idle;
      if(_mystream_bias_stream_oready) begin
        _mystream_bias_y_source_ram_renable <= 0;
        _mystream_bias_y_source_fifo_deq <= 0;
      end 
      _mystream_bias_y_idle <= _mystream_bias_y_idle;
      if(_mystream_bias_stream_oready) begin
        _mystream_bias_z_sink_wenable <= 0;
        _mystream_bias_z_sink_fifo_enq <= 0;
      end 
      if(_mystream_bias_stream_oready) begin
        __mystream_bias_stream_ivalid_1 <= _mystream_bias_stream_ivalid;
      end 
      if(_mystream_bias_stream_oready) begin
        _plus_data_10 <= mystream_bias_x_data + mystream_bias_y_data;
      end 
      if(_set_flag_57) begin
        _mystream_bias_x_source_mode <= 4'b1000;
        _mystream_bias_x_source_size <= _th_comp_write_size_1;
      end 
      if(_set_flag_57) begin
        _mystream_bias_x_source_sel <= 1;
      end 
      if(_mystream_bias_source_start && _mystream_bias_x_source_mode & 4'b1000 && _mystream_bias_stream_oready) begin
        _mystream_bias_x_idle <= 0;
        _mystream_bias_x_source_size_buf <= _mystream_bias_x_source_size;
      end 
      if(_mystream_bias_stream_oready && _mystream_bias_source_busy && _mystream_bias_is_root) begin
        __variable_wdata_8 <= _mystream_bias_x_source_fifo_rdata;
      end 
      if((_mystream_bias_x_source_fsm_0 == 1) && _mystream_bias_stream_oready) begin
        _mystream_bias_x_source_fifo_deq <= 1;
        _mystream_bias_x_source_count <= _mystream_bias_x_source_size_buf;
      end 
      if((_mystream_bias_x_source_fsm_0 == 2) && _mystream_bias_stream_oready) begin
        _mystream_bias_x_source_fifo_deq <= 1;
        _mystream_bias_x_source_count <= _mystream_bias_x_source_count - 1;
      end 
      if((_mystream_bias_x_source_fsm_0 == 2) && (_mystream_bias_x_source_count == 1) && _mystream_bias_stream_oready) begin
        _mystream_bias_x_source_fifo_deq <= 0;
        _mystream_bias_x_idle <= 1;
      end 
      if(_set_flag_60) begin
        _mystream_bias_y_source_mode <= 4'b1;
        _mystream_bias_y_source_offset <= 0;
        _mystream_bias_y_source_size <= _th_comp_write_size_1;
        _mystream_bias_y_source_stride <= 1;
      end 
      if(_set_flag_60) begin
        _mystream_bias_y_source_sel <= 2;
      end 
      if(_mystream_bias_source_start && _mystream_bias_y_source_mode & 4'b1 && _mystream_bias_stream_oready) begin
        _mystream_bias_y_source_offset_buf <= _mystream_bias_y_source_offset;
        _mystream_bias_y_source_size_buf <= _mystream_bias_y_source_size;
        _mystream_bias_y_source_stride_buf <= _mystream_bias_y_source_stride;
      end 
      if(_mystream_bias_stream_oready && _mystream_bias_source_busy && _mystream_bias_is_root) begin
        __variable_wdata_9 <= _mystream_bias_y_source_ram_rdata;
      end 
      if((_mystream_bias_y_source_fsm_1 == 1) && _mystream_bias_stream_oready) begin
        _mystream_bias_y_idle <= 0;
        _mystream_bias_y_source_ram_raddr <= _mystream_bias_y_source_offset_buf;
        _mystream_bias_y_source_ram_renable <= 1;
        _mystream_bias_y_source_count <= _mystream_bias_y_source_size_buf;
      end 
      if((_mystream_bias_y_source_fsm_1 == 2) && _mystream_bias_stream_oready) begin
        _mystream_bias_y_source_ram_raddr <= _mystream_bias_y_source_ram_raddr + _mystream_bias_y_source_stride_buf;
        _mystream_bias_y_source_ram_renable <= 1;
        _mystream_bias_y_source_count <= _mystream_bias_y_source_count - 1;
      end 
      if((_mystream_bias_y_source_fsm_1 == 2) && (_mystream_bias_y_source_count == 1) && _mystream_bias_stream_oready) begin
        _mystream_bias_y_source_ram_renable <= 0;
        _mystream_bias_y_idle <= 1;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_64 <= _set_flag_63;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_65 <= _tmp_64;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_66 <= _tmp_65;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_67 <= _th_comp_write_size_1;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_68 <= _tmp_67;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_69 <= _tmp_68;
      end 
      if(_tmp_66) begin
        _mystream_bias_z_sink_mode <= 4'b1000;
        _mystream_bias_z_sink_size <= _tmp_69;
      end 
      if(_tmp_66) begin
        _mystream_bias_z_sink_sel <= 3;
      end 
      if(_mystream_bias_sink_start && _mystream_bias_z_sink_mode & 4'b1000 && _mystream_bias_stream_oready) begin
        _mystream_bias_z_sink_size_buf <= _mystream_bias_z_sink_size;
      end 
      if((_mystream_bias_z_sink_fsm_2 == 1) && _mystream_bias_stream_oready) begin
        _mystream_bias_z_sink_count <= _mystream_bias_z_sink_size;
        _mystream_bias_z_sink_size_buf <= _mystream_bias_z_sink_size;
      end 
      if((_mystream_bias_z_sink_fsm_2 == 2) && _mystream_bias_stream_oready) begin
        _mystream_bias_z_sink_fifo_wdata <= mystream_bias_z_data;
        _mystream_bias_z_sink_fifo_enq <= 1;
        _mystream_bias_z_sink_count <= _mystream_bias_z_sink_count - 1;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_115 <= _mystream_bias_source_start;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_116 <= _tmp_115;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_117 <= _tmp_116;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_120 <= _tmp_119;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_121 <= _mystream_bias_source_start;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_122 <= _tmp_121;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_123 <= _tmp_122;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_124 <= _mystream_bias_source_stop;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_125 <= _mystream_bias_source_busy;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_126 <= _tmp_125;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_127 <= _tmp_126;
      end 
      __mystream_bias_sink_busy_1 <= _mystream_bias_sink_busy;
      if(!_mystream_bias_sink_busy && __mystream_bias_sink_busy_1) begin
        _mystream_bias_busy_buf <= 0;
      end 
      if(_mystream_bias_source_busy) begin
        _mystream_bias_busy_buf <= 1;
      end 
    end
  end

  localparam _mystream_bias_fsm_1 = 1;
  localparam _mystream_bias_fsm_2 = 2;
  localparam _mystream_bias_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_bias_fsm <= _mystream_bias_fsm_init;
      _mystream_bias_source_start <= 0;
      _mystream_bias_source_busy <= 0;
      _mystream_bias_source_stop <= 0;
      _mystream_bias_stream_ivalid <= 0;
    end else begin
      if(_tmp_117 && _mystream_bias_stream_oready) begin
        _mystream_bias_stream_ivalid <= 1;
      end 
      if(_mystream_bias_stream_oready) begin
        _mystream_bias_source_stop <= 0;
      end 
      if(_tmp_120 && _mystream_bias_stream_oready) begin
        _mystream_bias_stream_ivalid <= 0;
      end 
      case(_mystream_bias_fsm)
        _mystream_bias_fsm_init: begin
          if(_mystream_bias_run_flag) begin
            _mystream_bias_source_start <= 1;
          end 
          if(_mystream_bias_run_flag) begin
            _mystream_bias_fsm <= _mystream_bias_fsm_1;
          end 
        end
        _mystream_bias_fsm_1: begin
          if(_mystream_bias_source_start && _mystream_bias_stream_oready) begin
            _mystream_bias_source_start <= 0;
            _mystream_bias_source_busy <= 1;
          end 
          if(_mystream_bias_source_start && _mystream_bias_stream_oready) begin
            _mystream_bias_fsm <= _mystream_bias_fsm_2;
          end 
        end
        _mystream_bias_fsm_2: begin
          if(_mystream_bias_stream_oready) begin
            _mystream_bias_fsm <= _mystream_bias_fsm_3;
          end 
        end
        _mystream_bias_fsm_3: begin
          if(_mystream_bias_stream_oready && (_mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3))) begin
            _mystream_bias_source_stop <= 1;
            _mystream_bias_source_busy <= 0;
          end 
          if(_mystream_bias_stream_oready && (_mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3)) && _mystream_bias_run_flag) begin
            _mystream_bias_source_start <= 1;
          end 
          if(_mystream_bias_stream_oready && (_mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3))) begin
            _mystream_bias_fsm <= _mystream_bias_fsm_init;
          end 
          if(_mystream_bias_stream_oready && (_mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3)) && _mystream_bias_run_flag) begin
            _mystream_bias_fsm <= _mystream_bias_fsm_1;
          end 
        end
      endcase
    end
  end

  localparam th_comp_1 = 1;
  localparam th_comp_2 = 2;
  localparam th_comp_3 = 3;
  localparam th_comp_4 = 4;
  localparam th_comp_5 = 5;
  localparam th_comp_6 = 6;
  localparam th_comp_7 = 7;
  localparam th_comp_8 = 8;
  localparam th_comp_9 = 9;
  localparam th_comp_10 = 10;
  localparam th_comp_11 = 11;
  localparam th_comp_12 = 12;
  localparam th_comp_13 = 13;
  localparam th_comp_14 = 14;
  localparam th_comp_15 = 15;
  localparam th_comp_16 = 16;
  localparam th_comp_17 = 17;
  localparam th_comp_18 = 18;
  localparam th_comp_19 = 19;
  localparam th_comp_20 = 20;
  localparam th_comp_21 = 21;
  localparam th_comp_22 = 22;
  localparam th_comp_23 = 23;
  localparam th_comp_24 = 24;
  localparam th_comp_25 = 25;
  localparam th_comp_26 = 26;
  localparam th_comp_27 = 27;
  localparam th_comp_28 = 28;
  localparam th_comp_29 = 29;
  localparam th_comp_30 = 30;
  localparam th_comp_31 = 31;
  localparam th_comp_32 = 32;
  localparam th_comp_33 = 33;
  localparam th_comp_34 = 34;
  localparam th_comp_35 = 35;
  localparam th_comp_36 = 36;
  localparam th_comp_37 = 37;
  localparam th_comp_38 = 38;
  localparam th_comp_39 = 39;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _d1_th_comp <= th_comp_init;
      _th_comp_read_size_0 <= 0;
      _th_comp_write_size_1 <= 0;
      _th_comp_reduce_size_2 <= 0;
      _th_comp_bias_addr_3 <= 0;
      axim_flag_9 <= 0;
      _th_comp_cond_14_0_1 <= 0;
      axistreamin_flag_19 <= 0;
      _th_comp_cond_19_1_1 <= 0;
      axistreamout_flag_23 <= 0;
      _th_comp_cond_22_2_1 <= 0;
    end else begin
      _d1_th_comp <= th_comp;
      case(_d1_th_comp)
        th_comp_14: begin
          if(_th_comp_cond_14_0_1) begin
            axim_flag_9 <= 0;
          end 
        end
        th_comp_19: begin
          if(_th_comp_cond_19_1_1) begin
            axistreamin_flag_19 <= 0;
          end 
        end
        th_comp_22: begin
          if(_th_comp_cond_22_2_1) begin
            axistreamout_flag_23 <= 0;
          end 
        end
      endcase
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          if(1) begin
            th_comp <= th_comp_2;
          end else begin
            th_comp <= th_comp_39;
          end
        end
        th_comp_2: begin
          if(_saxi_register_0 == 1) begin
            th_comp <= th_comp_3;
          end 
        end
        th_comp_3: begin
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          _th_comp_read_size_0 <= _saxi_register_2;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          _th_comp_write_size_1 <= _saxi_register_3;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          _th_comp_reduce_size_2 <= _saxi_register_4;
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          _th_comp_bias_addr_3 <= _saxi_register_5;
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if((_th_comp_read_size_0 < 0) || (_th_comp_read_size_0 == 0)) begin
            th_comp <= th_comp_9;
          end else begin
            th_comp <= th_comp_10;
          end
        end
        th_comp_9: begin
          _th_comp_read_size_0 <= 1;
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if((_th_comp_write_size_1 < 0) || (_th_comp_write_size_1 == 0)) begin
            th_comp <= th_comp_11;
          end else begin
            th_comp <= th_comp_12;
          end
        end
        th_comp_11: begin
          _th_comp_write_size_1 <= 1;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if((_th_comp_reduce_size_2 < 0) || (_th_comp_reduce_size_2 == 0)) begin
            th_comp <= th_comp_13;
          end else begin
            th_comp <= th_comp_14;
          end
        end
        th_comp_13: begin
          _th_comp_reduce_size_2 <= 1;
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          axim_flag_9 <= 1;
          _th_comp_cond_14_0_1 <= 1;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          if(_maxi_read_idle) begin
            th_comp <= th_comp_18;
          end 
        end
        th_comp_18: begin
          if(_axi_in_read_idle) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          axistreamin_flag_19 <= 1;
          _th_comp_cond_19_1_1 <= 1;
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          if(_axi_out_write_idle) begin
            th_comp <= th_comp_22;
          end 
        end
        th_comp_22: begin
          axistreamout_flag_23 <= 1;
          _th_comp_cond_22_2_1 <= 1;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          if(_mystream_reduce_stream_oready) begin
            th_comp <= th_comp_28;
          end 
        end
        th_comp_28: begin
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          if(_mystream_bias_stream_oready) begin
            th_comp <= th_comp_31;
          end 
        end
        th_comp_31: begin
          th_comp <= th_comp_32;
        end
        th_comp_32: begin
          if(_mystream_reduce_busy) begin
            th_comp <= th_comp_33;
          end 
        end
        th_comp_33: begin
          th_comp <= th_comp_34;
        end
        th_comp_34: begin
          if(_mystream_bias_busy) begin
            th_comp <= th_comp_35;
          end 
        end
        th_comp_35: begin
          if(!_mystream_reduce_busy) begin
            th_comp <= th_comp_36;
          end 
        end
        th_comp_36: begin
          if(!_mystream_bias_busy) begin
            th_comp <= th_comp_37;
          end 
        end
        th_comp_37: begin
          th_comp <= th_comp_38;
        end
        th_comp_38: begin
          th_comp <= th_comp_1;
        end
      endcase
    end
  end

  localparam _maxi_read_fsm_1 = 1;
  localparam _maxi_read_fsm_2 = 2;
  localparam _maxi_read_fsm_3 = 3;
  localparam _maxi_read_fsm_4 = 4;
  localparam _maxi_read_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_fsm <= _maxi_read_fsm_init;
      _d1__maxi_read_fsm <= _maxi_read_fsm_init;
      _maxi_read_cur_global_addr <= 0;
      _maxi_read_rest_size <= 0;
      _maxi_read_cur_size <= 0;
      __maxi_read_fsm_cond_3_0_1 <= 0;
      _wvalid_11 <= 0;
      _wdata_10 <= 0;
      axim_flag_18 <= 0;
      __maxi_read_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__maxi_read_fsm <= _maxi_read_fsm;
      case(_d1__maxi_read_fsm)
        _maxi_read_fsm_3: begin
          if(__maxi_read_fsm_cond_3_0_1) begin
            _wvalid_11 <= 0;
          end 
        end
        _maxi_read_fsm_4: begin
          if(__maxi_read_fsm_cond_4_1_1) begin
            axim_flag_18 <= 0;
          end 
        end
      endcase
      case(_maxi_read_fsm)
        _maxi_read_fsm_init: begin
          if(_maxi_read_start) begin
            _maxi_read_cur_global_addr <= (_maxi_read_global_addr >> 2) << 2;
            _maxi_read_rest_size <= _maxi_read_size;
          end 
          if(_maxi_read_start && (_maxi_read_op_sel == 1)) begin
            _maxi_read_fsm <= _maxi_read_fsm_1;
          end 
        end
        _maxi_read_fsm_1: begin
          if((_maxi_read_rest_size <= 256) && ((_maxi_read_cur_global_addr & 4095) + (_maxi_read_rest_size << 2) >= 4096)) begin
            _maxi_read_cur_size <= 4096 - (_maxi_read_cur_global_addr & 4095) >> 2;
            _maxi_read_rest_size <= _maxi_read_rest_size - (4096 - (_maxi_read_cur_global_addr & 4095) >> 2);
          end else if(_maxi_read_rest_size <= 256) begin
            _maxi_read_cur_size <= _maxi_read_rest_size;
            _maxi_read_rest_size <= 0;
          end else if((_maxi_read_cur_global_addr & 4095) + 1024 >= 4096) begin
            _maxi_read_cur_size <= 4096 - (_maxi_read_cur_global_addr & 4095) >> 2;
            _maxi_read_rest_size <= _maxi_read_rest_size - (4096 - (_maxi_read_cur_global_addr & 4095) >> 2);
          end else begin
            _maxi_read_cur_size <= 256;
            _maxi_read_rest_size <= _maxi_read_rest_size - 256;
          end
          _maxi_read_fsm <= _maxi_read_fsm_2;
        end
        _maxi_read_fsm_2: begin
          if(maxi_arready || !maxi_arvalid) begin
            _maxi_read_fsm <= _maxi_read_fsm_3;
          end 
        end
        _maxi_read_fsm_3: begin
          __maxi_read_fsm_cond_3_0_1 <= 1;
          if(maxi_rready && maxi_rvalid && (_maxi_read_op_sel == 1)) begin
            _wdata_10 <= maxi_rdata;
            _wvalid_11 <= 1;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast) begin
            _maxi_read_cur_global_addr <= _maxi_read_cur_global_addr + (_maxi_read_cur_size << 2);
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_maxi_read_rest_size > 0)) begin
            _maxi_read_fsm <= _maxi_read_fsm_1;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_maxi_read_rest_size == 0)) begin
            _maxi_read_fsm <= _maxi_read_fsm_4;
          end 
        end
        _maxi_read_fsm_4: begin
          axim_flag_18 <= 1;
          __maxi_read_fsm_cond_4_1_1 <= 1;
          _maxi_read_fsm <= _maxi_read_fsm_5;
        end
        _maxi_read_fsm_5: begin
          _maxi_read_fsm <= _maxi_read_fsm_init;
        end
      endcase
    end
  end

  localparam _axi_in_read_fsm_1 = 1;
  localparam _axi_in_read_fsm_2 = 2;
  localparam _axi_in_read_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_in_read_fsm <= _axi_in_read_fsm_init;
      _d1__axi_in_read_fsm <= _axi_in_read_fsm_init;
      _axi_in_read_rest_size <= 0;
      axistreamin_flag_22 <= 0;
      __axi_in_read_fsm_cond_2_0_1 <= 0;
    end else begin
      _d1__axi_in_read_fsm <= _axi_in_read_fsm;
      case(_d1__axi_in_read_fsm)
        _axi_in_read_fsm_2: begin
          if(__axi_in_read_fsm_cond_2_0_1) begin
            axistreamin_flag_22 <= 0;
          end 
        end
      endcase
      case(_axi_in_read_fsm)
        _axi_in_read_fsm_init: begin
          if(_axi_in_read_start) begin
            _axi_in_read_rest_size <= _axi_in_read_size;
          end 
          if(_axi_in_read_start && (_axi_in_read_op_sel == 1)) begin
            _axi_in_read_fsm <= _axi_in_read_fsm_1;
          end 
        end
        _axi_in_read_fsm_1: begin
          if(axi_in_tready && axi_in_tvalid && (_axi_in_read_op_sel == 1)) begin
            _axi_in_read_rest_size <= _axi_in_read_rest_size - 1;
          end 
          if(axi_in_tready && axi_in_tvalid && (_axi_in_read_rest_size <= 1)) begin
            _axi_in_read_fsm <= _axi_in_read_fsm_2;
          end 
        end
        _axi_in_read_fsm_2: begin
          axistreamin_flag_22 <= 1;
          __axi_in_read_fsm_cond_2_0_1 <= 1;
          _axi_in_read_fsm <= _axi_in_read_fsm_3;
        end
        _axi_in_read_fsm_3: begin
          _axi_in_read_fsm <= _axi_in_read_fsm_init;
        end
      endcase
    end
  end

  localparam _axi_out_write_fsm_1 = 1;
  localparam _axi_out_write_fsm_2 = 2;
  localparam _axi_out_write_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_out_write_fsm <= _axi_out_write_fsm_init;
      _d1__axi_out_write_fsm <= _axi_out_write_fsm_init;
      _axi_out_write_counter <= 0;
      _axi_out_write_fifo_counter_24 <= 0;
      axistreamout_flag_29 <= 0;
      __axi_out_write_fsm_cond_2_0_1 <= 0;
    end else begin
      _d1__axi_out_write_fsm <= _axi_out_write_fsm;
      case(_d1__axi_out_write_fsm)
        _axi_out_write_fsm_2: begin
          if(__axi_out_write_fsm_cond_2_0_1) begin
            axistreamout_flag_29 <= 0;
          end 
        end
      endcase
      case(_axi_out_write_fsm)
        _axi_out_write_fsm_init: begin
          if(_axi_out_write_start) begin
            _axi_out_write_counter <= _axi_out_write_size;
          end 
          if(_axi_out_write_start) begin
            _axi_out_write_fifo_counter_24 <= _axi_out_write_size;
          end 
          if(_axi_out_write_start && (_axi_out_write_op_sel == 1)) begin
            _axi_out_write_fsm <= _axi_out_write_fsm_1;
          end 
        end
        _axi_out_write_fsm_1: begin
          if((_axi_out_write_fsm == 1) && (_axi_out_write_op_sel == 1) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty && (_axi_out_write_fifo_counter_24 > 0)) begin
            _axi_out_write_fifo_counter_24 <= _axi_out_write_fifo_counter_24 - 1;
          end 
          if(axi_out_tvalid && axi_out_tready) begin
            _axi_out_write_counter <= _axi_out_write_counter - 1;
          end 
          if(_axi_out_write_counter == 0) begin
            _axi_out_write_fsm <= _axi_out_write_fsm_2;
          end 
        end
        _axi_out_write_fsm_2: begin
          axistreamout_flag_29 <= 1;
          __axi_out_write_fsm_cond_2_0_1 <= 1;
          _axi_out_write_fsm <= _axi_out_write_fsm_3;
        end
        _axi_out_write_fsm_3: begin
          _axi_out_write_fsm <= _axi_out_write_fsm_init;
        end
      endcase
    end
  end

  localparam _mystream_reduce_a_source_fsm_0_1 = 1;
  localparam _mystream_reduce_a_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_reduce_a_source_fsm_0 <= _mystream_reduce_a_source_fsm_0_init;
    end else begin
      case(_mystream_reduce_a_source_fsm_0)
        _mystream_reduce_a_source_fsm_0_init: begin
          if(_mystream_reduce_source_start && _mystream_reduce_a_source_mode & 4'b1000 && _mystream_reduce_stream_oready) begin
            _mystream_reduce_a_source_fsm_0 <= _mystream_reduce_a_source_fsm_0_1;
          end 
        end
        _mystream_reduce_a_source_fsm_0_1: begin
          if(_mystream_reduce_stream_oready) begin
            _mystream_reduce_a_source_fsm_0 <= _mystream_reduce_a_source_fsm_0_2;
          end 
        end
        _mystream_reduce_a_source_fsm_0_2: begin
          if((_mystream_reduce_a_source_count == 1) && _mystream_reduce_stream_oready) begin
            _mystream_reduce_a_source_fsm_0 <= _mystream_reduce_a_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_reduce_sum_sink_fsm_1_1 = 1;
  localparam _mystream_reduce_sum_sink_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_reduce_sum_sink_fsm_1 <= _mystream_reduce_sum_sink_fsm_1_init;
    end else begin
      case(_mystream_reduce_sum_sink_fsm_1)
        _mystream_reduce_sum_sink_fsm_1_init: begin
          if(_mystream_reduce_sink_start && _mystream_reduce_sum_sink_mode & 4'b1000 && _mystream_reduce_stream_oready) begin
            _mystream_reduce_sum_sink_fsm_1 <= _mystream_reduce_sum_sink_fsm_1_1;
          end 
        end
        _mystream_reduce_sum_sink_fsm_1_1: begin
          if(_mystream_reduce_stream_oready) begin
            _mystream_reduce_sum_sink_fsm_1 <= _mystream_reduce_sum_sink_fsm_1_2;
          end 
        end
        _mystream_reduce_sum_sink_fsm_1_2: begin
          if(mystream_reduce_sum_valid_data && (_mystream_reduce_sum_sink_count == 1) && _mystream_reduce_stream_oready) begin
            _mystream_reduce_sum_sink_fsm_1 <= _mystream_reduce_sum_sink_fsm_1_init;
          end 
          if(_mystream_reduce_sink_stop && _mystream_reduce_stream_oready) begin
            _mystream_reduce_sum_sink_fsm_1 <= _mystream_reduce_sum_sink_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_bias_x_source_fsm_0_1 = 1;
  localparam _mystream_bias_x_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_bias_x_source_fsm_0 <= _mystream_bias_x_source_fsm_0_init;
    end else begin
      case(_mystream_bias_x_source_fsm_0)
        _mystream_bias_x_source_fsm_0_init: begin
          if(_mystream_bias_source_start && _mystream_bias_x_source_mode & 4'b1000 && _mystream_bias_stream_oready) begin
            _mystream_bias_x_source_fsm_0 <= _mystream_bias_x_source_fsm_0_1;
          end 
        end
        _mystream_bias_x_source_fsm_0_1: begin
          if(_mystream_bias_stream_oready) begin
            _mystream_bias_x_source_fsm_0 <= _mystream_bias_x_source_fsm_0_2;
          end 
        end
        _mystream_bias_x_source_fsm_0_2: begin
          if((_mystream_bias_x_source_count == 1) && _mystream_bias_stream_oready) begin
            _mystream_bias_x_source_fsm_0 <= _mystream_bias_x_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_bias_y_source_fsm_1_1 = 1;
  localparam _mystream_bias_y_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_bias_y_source_fsm_1 <= _mystream_bias_y_source_fsm_1_init;
    end else begin
      case(_mystream_bias_y_source_fsm_1)
        _mystream_bias_y_source_fsm_1_init: begin
          if(_mystream_bias_source_start && _mystream_bias_y_source_mode & 4'b1 && _mystream_bias_stream_oready) begin
            _mystream_bias_y_source_fsm_1 <= _mystream_bias_y_source_fsm_1_1;
          end 
        end
        _mystream_bias_y_source_fsm_1_1: begin
          if(_mystream_bias_stream_oready) begin
            _mystream_bias_y_source_fsm_1 <= _mystream_bias_y_source_fsm_1_2;
          end 
        end
        _mystream_bias_y_source_fsm_1_2: begin
          if((_mystream_bias_y_source_count == 1) && _mystream_bias_stream_oready) begin
            _mystream_bias_y_source_fsm_1 <= _mystream_bias_y_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_bias_z_sink_fsm_2_1 = 1;
  localparam _mystream_bias_z_sink_fsm_2_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_bias_z_sink_fsm_2 <= _mystream_bias_z_sink_fsm_2_init;
    end else begin
      case(_mystream_bias_z_sink_fsm_2)
        _mystream_bias_z_sink_fsm_2_init: begin
          if(_mystream_bias_sink_start && _mystream_bias_z_sink_mode & 4'b1000 && _mystream_bias_stream_oready) begin
            _mystream_bias_z_sink_fsm_2 <= _mystream_bias_z_sink_fsm_2_1;
          end 
        end
        _mystream_bias_z_sink_fsm_2_1: begin
          if(_mystream_bias_stream_oready) begin
            _mystream_bias_z_sink_fsm_2 <= _mystream_bias_z_sink_fsm_2_2;
          end 
        end
        _mystream_bias_z_sink_fsm_2_2: begin
          if((_mystream_bias_z_sink_count == 1) && _mystream_bias_stream_oready) begin
            _mystream_bias_z_sink_fsm_2 <= _mystream_bias_z_sink_fsm_2_init;
          end 
          if(_mystream_bias_sink_stop && _mystream_bias_stream_oready) begin
            _mystream_bias_z_sink_fsm_2 <= _mystream_bias_z_sink_fsm_2_init;
          end 
        end
      endcase
    end
  end


endmodule



module fifo_a
(
  input CLK,
  input RST,
  input fifo_a_enq,
  input [32-1:0] fifo_a_wdata,
  output fifo_a_full,
  output fifo_a_almost_full,
  input fifo_a_deq,
  output [32-1:0] fifo_a_rdata,
  output fifo_a_empty,
  output fifo_a_almost_empty
);

  reg [32-1:0] mem [0:256-1];
  reg [8-1:0] head;
  reg [8-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 255);
  assign is_full = (head + 1 & 255) == tail;
  assign is_almost_full = (head + 2 & 255) == tail;
  reg [32-1:0] rdata_reg;
  assign fifo_a_full = is_full;
  assign fifo_a_almost_full = is_almost_full || is_full;
  assign fifo_a_empty = is_empty;
  assign fifo_a_almost_empty = is_almost_empty || is_empty;
  assign fifo_a_rdata = rdata_reg;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      rdata_reg <= 0;
      tail <= 0;
    end else begin
      if(fifo_a_enq && !is_full) begin
        mem[head] <= fifo_a_wdata;
        head <= head + 1;
      end 
      if(fifo_a_deq && !is_empty) begin
        rdata_reg <= mem[tail];
        tail <= tail + 1;
      end 
    end
  end


endmodule



module fifo_b
(
  input CLK,
  input RST,
  input fifo_b_enq,
  input [32-1:0] fifo_b_wdata,
  output fifo_b_full,
  output fifo_b_almost_full,
  input fifo_b_deq,
  output [32-1:0] fifo_b_rdata,
  output fifo_b_empty,
  output fifo_b_almost_empty
);

  reg [32-1:0] mem [0:256-1];
  reg [8-1:0] head;
  reg [8-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 255);
  assign is_full = (head + 1 & 255) == tail;
  assign is_almost_full = (head + 2 & 255) == tail;
  reg [32-1:0] rdata_reg;
  assign fifo_b_full = is_full;
  assign fifo_b_almost_full = is_almost_full || is_full;
  assign fifo_b_empty = is_empty;
  assign fifo_b_almost_empty = is_almost_empty || is_empty;
  assign fifo_b_rdata = rdata_reg;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      rdata_reg <= 0;
      tail <= 0;
    end else begin
      if(fifo_b_enq && !is_full) begin
        mem[head] <= fifo_b_wdata;
        head <= head + 1;
      end 
      if(fifo_b_deq && !is_empty) begin
        rdata_reg <= mem[tail];
        tail <= tail + 1;
      end 
    end
  end


endmodule



module fifo_c
(
  input CLK,
  input RST,
  input fifo_c_enq,
  input [32-1:0] fifo_c_wdata,
  output fifo_c_full,
  output fifo_c_almost_full,
  input fifo_c_deq,
  output [32-1:0] fifo_c_rdata,
  output fifo_c_empty,
  output fifo_c_almost_empty
);

  reg [32-1:0] mem [0:256-1];
  reg [8-1:0] head;
  reg [8-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 255);
  assign is_full = (head + 1 & 255) == tail;
  assign is_almost_full = (head + 2 & 255) == tail;
  reg [32-1:0] rdata_reg;
  assign fifo_c_full = is_full;
  assign fifo_c_almost_full = is_almost_full || is_full;
  assign fifo_c_empty = is_empty;
  assign fifo_c_almost_empty = is_almost_empty || is_empty;
  assign fifo_c_rdata = rdata_reg;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      rdata_reg <= 0;
      tail <= 0;
    end else begin
      if(fifo_c_enq && !is_full) begin
        mem[head] <= fifo_c_wdata;
        head <= head + 1;
      end 
      if(fifo_c_deq && !is_empty) begin
        rdata_reg <= mem[tail];
        tail <= tail + 1;
      end 
    end
  end


endmodule



module ram_b
(
  input CLK,
  input [10-1:0] ram_b_0_addr,
  output [32-1:0] ram_b_0_rdata,
  input [32-1:0] ram_b_0_wdata,
  input ram_b_0_wenable,
  input ram_b_0_enable
);

  reg [32-1:0] ram_b_0_rdata_out;
  assign ram_b_0_rdata = ram_b_0_rdata_out;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_0_enable) begin
      if(ram_b_0_wenable) begin
        mem[ram_b_0_addr] <= ram_b_0_wdata;
        ram_b_0_rdata_out <= ram_b_0_wdata;
      end else begin
        ram_b_0_rdata_out <= mem[ram_b_0_addr];
      end
    end 
  end


endmodule



module multiplier_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);


  multiplier_core_0
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule
"""


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    code = thread_stream_axi_stream_fifo.run(filename=None, simtype=simtype,
                                             outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
