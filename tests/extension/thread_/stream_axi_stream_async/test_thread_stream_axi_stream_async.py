from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_stream_axi_stream_async


expected_verilog = """
module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] axi_a_tdata,
  input axi_a_tvalid,
  output axi_a_tready,
  input axi_a_tlast,
  input [32-1:0] axi_b_tdata,
  input axi_b_tvalid,
  output axi_b_tready,
  input axi_b_tlast,
  output reg [32-1:0] axi_c_tdata,
  output reg axi_c_tvalid,
  input axi_c_tready,
  output reg axi_c_tlast,
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
  input saxi_rready
);

  wire _axi_a_read_req_fifo_enq;
  wire [105-1:0] _axi_a_read_req_fifo_wdata;
  wire _axi_a_read_req_fifo_full;
  wire _axi_a_read_req_fifo_almost_full;
  wire _axi_a_read_req_fifo_deq;
  wire [105-1:0] _axi_a_read_req_fifo_rdata;
  wire _axi_a_read_req_fifo_empty;
  wire _axi_a_read_req_fifo_almost_empty;

  _axi_a_read_req_fifo
  inst__axi_a_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_a_read_req_fifo_enq(_axi_a_read_req_fifo_enq),
    ._axi_a_read_req_fifo_wdata(_axi_a_read_req_fifo_wdata),
    ._axi_a_read_req_fifo_full(_axi_a_read_req_fifo_full),
    ._axi_a_read_req_fifo_almost_full(_axi_a_read_req_fifo_almost_full),
    ._axi_a_read_req_fifo_deq(_axi_a_read_req_fifo_deq),
    ._axi_a_read_req_fifo_rdata(_axi_a_read_req_fifo_rdata),
    ._axi_a_read_req_fifo_empty(_axi_a_read_req_fifo_empty),
    ._axi_a_read_req_fifo_almost_empty(_axi_a_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_a_read_req_fifo;
  wire [8-1:0] _axi_a_read_op_sel_fifo;
  wire [32-1:0] _axi_a_read_local_addr_fifo;
  wire [32-1:0] _axi_a_read_local_stride_fifo;
  wire [33-1:0] _axi_a_read_local_size_fifo;
  wire [8-1:0] unpack_read_req_op_sel_0;
  wire [32-1:0] unpack_read_req_local_addr_1;
  wire [32-1:0] unpack_read_req_local_stride_2;
  wire [33-1:0] unpack_read_req_local_size_3;
  assign unpack_read_req_op_sel_0 = _axi_a_read_req_fifo_rdata[104:97];
  assign unpack_read_req_local_addr_1 = _axi_a_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_stride_2 = _axi_a_read_req_fifo_rdata[64:33];
  assign unpack_read_req_local_size_3 = _axi_a_read_req_fifo_rdata[32:0];
  assign _axi_a_read_op_sel_fifo = unpack_read_req_op_sel_0;
  assign _axi_a_read_local_addr_fifo = unpack_read_req_local_addr_1;
  assign _axi_a_read_local_stride_fifo = unpack_read_req_local_stride_2;
  assign _axi_a_read_local_size_fifo = unpack_read_req_local_size_3;
  reg [8-1:0] _axi_a_read_op_sel_buf;
  reg [32-1:0] _axi_a_read_local_addr_buf;
  reg [32-1:0] _axi_a_read_local_stride_buf;
  reg [33-1:0] _axi_a_read_local_size_buf;
  reg _axi_a_read_data_idle;
  wire _axi_a_read_idle;
  assign _axi_a_read_idle = _axi_a_read_req_fifo_empty && _axi_a_read_data_idle;
  wire _axi_b_read_req_fifo_enq;
  wire [105-1:0] _axi_b_read_req_fifo_wdata;
  wire _axi_b_read_req_fifo_full;
  wire _axi_b_read_req_fifo_almost_full;
  wire _axi_b_read_req_fifo_deq;
  wire [105-1:0] _axi_b_read_req_fifo_rdata;
  wire _axi_b_read_req_fifo_empty;
  wire _axi_b_read_req_fifo_almost_empty;

  _axi_b_read_req_fifo
  inst__axi_b_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_b_read_req_fifo_enq(_axi_b_read_req_fifo_enq),
    ._axi_b_read_req_fifo_wdata(_axi_b_read_req_fifo_wdata),
    ._axi_b_read_req_fifo_full(_axi_b_read_req_fifo_full),
    ._axi_b_read_req_fifo_almost_full(_axi_b_read_req_fifo_almost_full),
    ._axi_b_read_req_fifo_deq(_axi_b_read_req_fifo_deq),
    ._axi_b_read_req_fifo_rdata(_axi_b_read_req_fifo_rdata),
    ._axi_b_read_req_fifo_empty(_axi_b_read_req_fifo_empty),
    ._axi_b_read_req_fifo_almost_empty(_axi_b_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_b_read_req_fifo;
  wire [8-1:0] _axi_b_read_op_sel_fifo;
  wire [32-1:0] _axi_b_read_local_addr_fifo;
  wire [32-1:0] _axi_b_read_local_stride_fifo;
  wire [33-1:0] _axi_b_read_local_size_fifo;
  wire [8-1:0] unpack_read_req_op_sel_4;
  wire [32-1:0] unpack_read_req_local_addr_5;
  wire [32-1:0] unpack_read_req_local_stride_6;
  wire [33-1:0] unpack_read_req_local_size_7;
  assign unpack_read_req_op_sel_4 = _axi_b_read_req_fifo_rdata[104:97];
  assign unpack_read_req_local_addr_5 = _axi_b_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_stride_6 = _axi_b_read_req_fifo_rdata[64:33];
  assign unpack_read_req_local_size_7 = _axi_b_read_req_fifo_rdata[32:0];
  assign _axi_b_read_op_sel_fifo = unpack_read_req_op_sel_4;
  assign _axi_b_read_local_addr_fifo = unpack_read_req_local_addr_5;
  assign _axi_b_read_local_stride_fifo = unpack_read_req_local_stride_6;
  assign _axi_b_read_local_size_fifo = unpack_read_req_local_size_7;
  reg [8-1:0] _axi_b_read_op_sel_buf;
  reg [32-1:0] _axi_b_read_local_addr_buf;
  reg [32-1:0] _axi_b_read_local_stride_buf;
  reg [33-1:0] _axi_b_read_local_size_buf;
  reg _axi_b_read_data_idle;
  wire _axi_b_read_idle;
  assign _axi_b_read_idle = _axi_b_read_req_fifo_empty && _axi_b_read_data_idle;
  wire _axi_c_write_req_fifo_enq;
  wire [105-1:0] _axi_c_write_req_fifo_wdata;
  wire _axi_c_write_req_fifo_full;
  wire _axi_c_write_req_fifo_almost_full;
  wire _axi_c_write_req_fifo_deq;
  wire [105-1:0] _axi_c_write_req_fifo_rdata;
  wire _axi_c_write_req_fifo_empty;
  wire _axi_c_write_req_fifo_almost_empty;

  _axi_c_write_req_fifo
  inst__axi_c_write_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_c_write_req_fifo_enq(_axi_c_write_req_fifo_enq),
    ._axi_c_write_req_fifo_wdata(_axi_c_write_req_fifo_wdata),
    ._axi_c_write_req_fifo_full(_axi_c_write_req_fifo_full),
    ._axi_c_write_req_fifo_almost_full(_axi_c_write_req_fifo_almost_full),
    ._axi_c_write_req_fifo_deq(_axi_c_write_req_fifo_deq),
    ._axi_c_write_req_fifo_rdata(_axi_c_write_req_fifo_rdata),
    ._axi_c_write_req_fifo_empty(_axi_c_write_req_fifo_empty),
    ._axi_c_write_req_fifo_almost_empty(_axi_c_write_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_c_write_req_fifo;
  wire [8-1:0] _axi_c_write_op_sel_fifo;
  wire [32-1:0] _axi_c_write_local_addr_fifo;
  wire [32-1:0] _axi_c_write_local_stride_fifo;
  wire [33-1:0] _axi_c_write_size_fifo;
  wire [8-1:0] unpack_write_req_op_sel_8;
  wire [32-1:0] unpack_write_req_local_addr_9;
  wire [32-1:0] unpack_write_req_local_stride_10;
  wire [33-1:0] unpack_write_req_local_size_11;
  assign unpack_write_req_op_sel_8 = _axi_c_write_req_fifo_rdata[104:97];
  assign unpack_write_req_local_addr_9 = _axi_c_write_req_fifo_rdata[96:65];
  assign unpack_write_req_local_stride_10 = _axi_c_write_req_fifo_rdata[64:33];
  assign unpack_write_req_local_size_11 = _axi_c_write_req_fifo_rdata[32:0];
  assign _axi_c_write_op_sel_fifo = unpack_write_req_op_sel_8;
  assign _axi_c_write_local_addr_fifo = unpack_write_req_local_addr_9;
  assign _axi_c_write_local_stride_fifo = unpack_write_req_local_stride_10;
  assign _axi_c_write_size_fifo = unpack_write_req_local_size_11;
  reg [8-1:0] _axi_c_write_op_sel_buf;
  reg [32-1:0] _axi_c_write_local_addr_buf;
  reg [32-1:0] _axi_c_write_local_stride_buf;
  reg [33-1:0] _axi_c_write_size_buf;
  reg _axi_c_write_data_idle;
  wire _axi_c_write_idle;
  assign _axi_c_write_idle = _axi_c_write_req_fifo_empty && _axi_c_write_data_idle;
  assign saxi_bresp = 0;
  assign saxi_rresp = 0;
  reg signed [32-1:0] _saxi_register_0;
  reg signed [32-1:0] _saxi_register_1;
  reg signed [32-1:0] _saxi_register_2;
  reg signed [32-1:0] _saxi_register_3;
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg signed [32-1:0] _saxi_resetval_0;
  reg signed [32-1:0] _saxi_resetval_1;
  reg signed [32-1:0] _saxi_resetval_2;
  reg signed [32-1:0] _saxi_resetval_3;
  localparam _saxi_maskwidth = 2;
  localparam _saxi_mask = { _saxi_maskwidth{ 1'd1 } };
  localparam _saxi_shift = 2;
  reg [32-1:0] _saxi_register_fsm;
  localparam _saxi_register_fsm_init = 0;
  reg [32-1:0] addr_12;
  reg writevalid_13;
  reg readvalid_14;
  reg prev_awvalid_15;
  reg prev_arvalid_16;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_13 && !readvalid_14 && !saxi_bvalid && prev_awvalid_15);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_14 && !writevalid_13 && prev_arvalid_16 && !prev_awvalid_15);
  reg [_saxi_maskwidth-1:0] axis_maskaddr_17;
  wire signed [32-1:0] axislite_rdata_18;
  assign axislite_rdata_18 = (axis_maskaddr_17 == 0)? _saxi_register_0 : 
                             (axis_maskaddr_17 == 1)? _saxi_register_1 : 
                             (axis_maskaddr_17 == 2)? _saxi_register_2 : 
                             (axis_maskaddr_17 == 3)? _saxi_register_3 : 'hx;
  wire axislite_flag_19;
  assign axislite_flag_19 = (axis_maskaddr_17 == 0)? _saxi_flag_0 : 
                            (axis_maskaddr_17 == 1)? _saxi_flag_1 : 
                            (axis_maskaddr_17 == 2)? _saxi_flag_2 : 
                            (axis_maskaddr_17 == 3)? _saxi_flag_3 : 'hx;
  wire signed [32-1:0] axislite_resetval_20;
  assign axislite_resetval_20 = (axis_maskaddr_17 == 0)? _saxi_resetval_0 : 
                                (axis_maskaddr_17 == 1)? _saxi_resetval_1 : 
                                (axis_maskaddr_17 == 2)? _saxi_resetval_2 : 
                                (axis_maskaddr_17 == 3)? _saxi_resetval_3 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  wire [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  wire [32-1:0] ram_a_0_wdata;
  wire ram_a_0_wenable;
  wire ram_a_0_enable;
  wire [10-1:0] ram_a_1_addr;
  wire [32-1:0] ram_a_1_rdata;
  wire [32-1:0] ram_a_1_wdata;
  wire ram_a_1_wenable;
  wire ram_a_1_enable;
  assign ram_a_0_wdata = 'hx;
  assign ram_a_0_wenable = 0;

  ram_a
  inst_ram_a
  (
    .CLK(CLK),
    .ram_a_0_addr(ram_a_0_addr),
    .ram_a_0_rdata(ram_a_0_rdata),
    .ram_a_0_wdata(ram_a_0_wdata),
    .ram_a_0_wenable(ram_a_0_wenable),
    .ram_a_0_enable(ram_a_0_enable),
    .ram_a_1_addr(ram_a_1_addr),
    .ram_a_1_rdata(ram_a_1_rdata),
    .ram_a_1_wdata(ram_a_1_wdata),
    .ram_a_1_wenable(ram_a_1_wenable),
    .ram_a_1_enable(ram_a_1_enable)
  );

  wire [10-1:0] ram_b_0_addr;
  wire [32-1:0] ram_b_0_rdata;
  wire [32-1:0] ram_b_0_wdata;
  wire ram_b_0_wenable;
  wire ram_b_0_enable;
  wire [10-1:0] ram_b_1_addr;
  wire [32-1:0] ram_b_1_rdata;
  wire [32-1:0] ram_b_1_wdata;
  wire ram_b_1_wenable;
  wire ram_b_1_enable;
  assign ram_b_0_wdata = 'hx;
  assign ram_b_0_wenable = 0;

  ram_b
  inst_ram_b
  (
    .CLK(CLK),
    .ram_b_0_addr(ram_b_0_addr),
    .ram_b_0_rdata(ram_b_0_rdata),
    .ram_b_0_wdata(ram_b_0_wdata),
    .ram_b_0_wenable(ram_b_0_wenable),
    .ram_b_0_enable(ram_b_0_enable),
    .ram_b_1_addr(ram_b_1_addr),
    .ram_b_1_rdata(ram_b_1_rdata),
    .ram_b_1_wdata(ram_b_1_wdata),
    .ram_b_1_wenable(ram_b_1_wenable),
    .ram_b_1_enable(ram_b_1_enable)
  );

  wire [10-1:0] ram_c_0_addr;
  wire [32-1:0] ram_c_0_rdata;
  wire [32-1:0] ram_c_0_wdata;
  wire ram_c_0_wenable;
  wire ram_c_0_enable;
  wire [10-1:0] ram_c_1_addr;
  wire [32-1:0] ram_c_1_rdata;
  wire [32-1:0] ram_c_1_wdata;
  wire ram_c_1_wenable;
  wire ram_c_1_enable;
  assign ram_c_1_wdata = 'hx;
  assign ram_c_1_wenable = 0;

  ram_c
  inst_ram_c
  (
    .CLK(CLK),
    .ram_c_0_addr(ram_c_0_addr),
    .ram_c_0_rdata(ram_c_0_rdata),
    .ram_c_0_wdata(ram_c_0_wdata),
    .ram_c_0_wenable(ram_c_0_wenable),
    .ram_c_0_enable(ram_c_0_enable),
    .ram_c_1_addr(ram_c_1_addr),
    .ram_c_1_rdata(ram_c_1_rdata),
    .ram_c_1_wdata(ram_c_1_wdata),
    .ram_c_1_wenable(ram_c_1_wenable),
    .ram_c_1_enable(ram_c_1_enable)
  );

  reg _mystream_stream_ivalid;
  wire _mystream_stream_oready;
  wire _mystream_stream_internal_oready;
  assign _mystream_stream_internal_oready = 1;
  assign _mystream_stream_oready = _mystream_stream_internal_oready;
  reg [32-1:0] _mystream_fsm;
  localparam _mystream_fsm_init = 0;
  wire _mystream_run_flag;
  reg _mystream_source_start;
  wire _mystream_source_stop;
  reg _mystream_source_busy;
  wire _mystream_sink_start;
  wire _mystream_sink_stop;
  wire _mystream_sink_busy;
  wire _mystream_busy;
  reg _mystream_busy_reg;
  wire _mystream_is_root;
  assign _mystream_is_root = 1;
  reg _mystream_a_idle;
  reg [33-1:0] _mystream_a_source_count;
  reg [5-1:0] _mystream_a_source_mode;
  reg [16-1:0] _mystream_a_source_generator_id;
  reg [32-1:0] _mystream_a_source_offset;
  reg [33-1:0] _mystream_a_source_size;
  reg [32-1:0] _mystream_a_source_stride;
  reg [32-1:0] _mystream_a_source_offset_buf;
  reg [33-1:0] _mystream_a_source_size_buf;
  reg [32-1:0] _mystream_a_source_stride_buf;
  reg [8-1:0] _mystream_a_source_sel;
  reg [32-1:0] _mystream_a_source_ram_raddr;
  reg _mystream_a_source_ram_renable;
  wire [32-1:0] _mystream_a_source_ram_rdata;
  reg _mystream_a_source_fifo_deq;
  wire [32-1:0] _mystream_a_source_fifo_rdata;
  reg [32-1:0] _mystream_a_source_empty_data;
  reg _mystream_b_idle;
  reg [33-1:0] _mystream_b_source_count;
  reg [5-1:0] _mystream_b_source_mode;
  reg [16-1:0] _mystream_b_source_generator_id;
  reg [32-1:0] _mystream_b_source_offset;
  reg [33-1:0] _mystream_b_source_size;
  reg [32-1:0] _mystream_b_source_stride;
  reg [32-1:0] _mystream_b_source_offset_buf;
  reg [33-1:0] _mystream_b_source_size_buf;
  reg [32-1:0] _mystream_b_source_stride_buf;
  reg [8-1:0] _mystream_b_source_sel;
  reg [32-1:0] _mystream_b_source_ram_raddr;
  reg _mystream_b_source_ram_renable;
  wire [32-1:0] _mystream_b_source_ram_rdata;
  reg _mystream_b_source_fifo_deq;
  wire [32-1:0] _mystream_b_source_fifo_rdata;
  reg [32-1:0] _mystream_b_source_empty_data;
  reg [33-1:0] _mystream_c_sink_count;
  reg [5-1:0] _mystream_c_sink_mode;
  reg [16-1:0] _mystream_c_sink_generator_id;
  reg [32-1:0] _mystream_c_sink_offset;
  reg [33-1:0] _mystream_c_sink_size;
  reg [32-1:0] _mystream_c_sink_stride;
  reg [32-1:0] _mystream_c_sink_offset_buf;
  reg [33-1:0] _mystream_c_sink_size_buf;
  reg [32-1:0] _mystream_c_sink_stride_buf;
  reg [8-1:0] _mystream_c_sink_sel;
  reg [32-1:0] _mystream_c_sink_waddr;
  reg _mystream_c_sink_wenable;
  reg [32-1:0] _mystream_c_sink_wdata;
  reg _mystream_c_sink_fifo_enq;
  reg [32-1:0] _mystream_c_sink_fifo_wdata;
  reg [32-1:0] _mystream_c_sink_immediate;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_0;
  reg signed [32-1:0] _th_comp_offset_1;
  wire [8-1:0] pack_read_req_op_sel_21;
  wire [32-1:0] pack_read_req_local_addr_22;
  wire [32-1:0] pack_read_req_local_stride_23;
  wire [33-1:0] pack_read_req_local_size_24;
  assign pack_read_req_op_sel_21 = 1;
  assign pack_read_req_local_addr_22 = _th_comp_offset_1;
  assign pack_read_req_local_stride_23 = 1;
  assign pack_read_req_local_size_24 = _th_comp_size_0;
  wire [105-1:0] pack_read_req_packed_25;
  assign pack_read_req_packed_25 = { pack_read_req_op_sel_21, pack_read_req_local_addr_22, pack_read_req_local_stride_23, pack_read_req_local_size_24 };
  assign _axi_a_read_req_fifo_wdata = ((th_comp == 6) && !_axi_a_read_req_fifo_almost_full)? pack_read_req_packed_25 : 'hx;
  assign _axi_a_read_req_fifo_enq = ((th_comp == 6) && !_axi_a_read_req_fifo_almost_full)? (th_comp == 6) && !_axi_a_read_req_fifo_almost_full && !_axi_a_read_req_fifo_almost_full : 0;
  localparam _tmp_26 = 1;
  wire [_tmp_26-1:0] _tmp_27;
  assign _tmp_27 = !_axi_a_read_req_fifo_almost_full;
  reg [_tmp_26-1:0] __tmp_27_1;
  reg [32-1:0] _axi_a_read_data_fsm;
  localparam _axi_a_read_data_fsm_init = 0;
  assign _axi_a_read_req_fifo_deq = ((_axi_a_read_data_fsm == 0) && (_axi_a_read_data_idle && !_axi_a_read_req_fifo_empty && (_axi_a_read_op_sel_fifo == 1)) && !_axi_a_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_28;
  reg [10-1:0] write_burst_stride_29;
  reg [33-1:0] write_burst_length_30;
  reg write_burst_done_31;
  assign ram_a_1_addr = ((write_burst_fsm_0 == 1) && axi_a_tvalid)? write_burst_addr_28 : 'hx;
  assign ram_a_1_wdata = ((write_burst_fsm_0 == 1) && axi_a_tvalid)? axi_a_tdata : 'hx;
  assign ram_a_1_wenable = ((write_burst_fsm_0 == 1) && axi_a_tvalid)? 1'd1 : 0;
  assign ram_a_1_enable = ((write_burst_fsm_0 == 1) && axi_a_tvalid)? 1'd1 : 0;
  assign axi_a_tready = _axi_a_read_data_fsm == 2;
  wire [8-1:0] pack_read_req_op_sel_32;
  wire [32-1:0] pack_read_req_local_addr_33;
  wire [32-1:0] pack_read_req_local_stride_34;
  wire [33-1:0] pack_read_req_local_size_35;
  assign pack_read_req_op_sel_32 = 1;
  assign pack_read_req_local_addr_33 = _th_comp_offset_1;
  assign pack_read_req_local_stride_34 = 1;
  assign pack_read_req_local_size_35 = _th_comp_size_0;
  wire [105-1:0] pack_read_req_packed_36;
  assign pack_read_req_packed_36 = { pack_read_req_op_sel_32, pack_read_req_local_addr_33, pack_read_req_local_stride_34, pack_read_req_local_size_35 };
  assign _axi_b_read_req_fifo_wdata = ((th_comp == 7) && !_axi_b_read_req_fifo_almost_full)? pack_read_req_packed_36 : 'hx;
  assign _axi_b_read_req_fifo_enq = ((th_comp == 7) && !_axi_b_read_req_fifo_almost_full)? (th_comp == 7) && !_axi_b_read_req_fifo_almost_full && !_axi_b_read_req_fifo_almost_full : 0;
  localparam _tmp_37 = 1;
  wire [_tmp_37-1:0] _tmp_38;
  assign _tmp_38 = !_axi_b_read_req_fifo_almost_full;
  reg [_tmp_37-1:0] __tmp_38_1;
  reg [32-1:0] _axi_b_read_data_fsm;
  localparam _axi_b_read_data_fsm_init = 0;
  assign _axi_b_read_req_fifo_deq = ((_axi_b_read_data_fsm == 0) && (_axi_b_read_data_idle && !_axi_b_read_req_fifo_empty && (_axi_b_read_op_sel_fifo == 1)) && !_axi_b_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_1;
  localparam write_burst_fsm_1_init = 0;
  reg [10-1:0] write_burst_addr_39;
  reg [10-1:0] write_burst_stride_40;
  reg [33-1:0] write_burst_length_41;
  reg write_burst_done_42;
  assign ram_b_1_addr = ((write_burst_fsm_1 == 1) && axi_b_tvalid)? write_burst_addr_39 : 'hx;
  assign ram_b_1_wdata = ((write_burst_fsm_1 == 1) && axi_b_tvalid)? axi_b_tdata : 'hx;
  assign ram_b_1_wenable = ((write_burst_fsm_1 == 1) && axi_b_tvalid)? 1'd1 : 0;
  assign ram_b_1_enable = ((write_burst_fsm_1 == 1) && axi_b_tvalid)? 1'd1 : 0;
  assign axi_b_tready = _axi_b_read_data_fsm == 2;
  reg signed [32-1:0] _th_comp_size_2;
  reg signed [32-1:0] _th_comp_offset_3;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  reg __mystream_stream_ivalid_1;
  reg signed [32-1:0] _plus_data_2;
  wire signed [32-1:0] mystream_c_data;
  assign mystream_c_data = _plus_data_2;
  wire _set_flag_43;
  assign _set_flag_43 = th_comp == 11;
  assign ram_a_0_addr = (_mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1))? _mystream_a_source_ram_raddr : 'hx;
  assign ram_a_0_enable = (_mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1))? 1'd1 : 0;
  localparam _tmp_44 = 1;
  wire [_tmp_44-1:0] _tmp_45;
  assign _tmp_45 = _mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1);
  reg [_tmp_44-1:0] __tmp_45_1;
  assign _mystream_a_source_ram_rdata = (_mystream_a_source_sel == 1)? ram_a_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_a_source_fsm_0;
  localparam _mystream_a_source_fsm_0_init = 0;
  wire _set_flag_46;
  assign _set_flag_46 = th_comp == 12;
  assign ram_b_0_addr = (_mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2))? _mystream_b_source_ram_raddr : 'hx;
  assign ram_b_0_enable = (_mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2))? 1'd1 : 0;
  localparam _tmp_47 = 1;
  wire [_tmp_47-1:0] _tmp_48;
  assign _tmp_48 = _mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2);
  reg [_tmp_47-1:0] __tmp_48_1;
  assign _mystream_b_source_ram_rdata = (_mystream_b_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_b_data = __variable_wdata_1;
  reg [32-1:0] _mystream_b_source_fsm_1;
  localparam _mystream_b_source_fsm_1_init = 0;
  wire _set_flag_49;
  assign _set_flag_49 = th_comp == 13;
  reg _tmp_50;
  reg _tmp_51;
  reg _tmp_52;
  reg signed [32-1:0] _tmp_53;
  reg signed [32-1:0] _tmp_54;
  reg signed [32-1:0] _tmp_55;
  reg signed [32-1:0] _tmp_56;
  reg signed [32-1:0] _tmp_57;
  reg signed [32-1:0] _tmp_58;
  assign ram_c_0_addr = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? _mystream_c_sink_waddr : 'hx;
  assign ram_c_0_wdata = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? _mystream_c_sink_wdata : 'hx;
  assign ram_c_0_wenable = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? 1'd1 : 0;
  assign ram_c_0_enable = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? 1'd1 : 0;
  reg [32-1:0] _mystream_c_sink_fsm_2;
  localparam _mystream_c_sink_fsm_2_init = 0;
  wire _set_flag_59;
  assign _set_flag_59 = th_comp == 14;
  assign _mystream_run_flag = (_set_flag_59)? 1 : 0;
  reg _tmp_60;
  reg _tmp_61;
  reg _tmp_62;
  assign _mystream_source_stop = _mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3));
  localparam _tmp_63 = 1;
  wire [_tmp_63-1:0] _tmp_64;
  assign _tmp_64 = _mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3);
  reg [_tmp_63-1:0] _tmp_65;
  reg _tmp_66;
  reg _tmp_67;
  reg _tmp_68;
  assign _mystream_sink_start = _tmp_68;
  reg _tmp_69;
  reg _tmp_70;
  reg _tmp_71;
  assign _mystream_sink_stop = _tmp_71;
  reg _tmp_72;
  reg _tmp_73;
  reg _tmp_74;
  assign _mystream_sink_busy = _tmp_74;
  reg _tmp_75;
  assign _mystream_busy = _mystream_source_busy || _mystream_sink_busy || _mystream_busy_reg;
  wire [8-1:0] pack_write_req_op_sel_76;
  wire [32-1:0] pack_write_req_local_addr_77;
  wire [32-1:0] pack_write_req_local_stride_78;
  wire [33-1:0] pack_write_req_local_size_79;
  assign pack_write_req_op_sel_76 = 1;
  assign pack_write_req_local_addr_77 = _th_comp_offset_1;
  assign pack_write_req_local_stride_78 = 1;
  assign pack_write_req_local_size_79 = _th_comp_size_0;
  wire [105-1:0] pack_write_req_packed_80;
  assign pack_write_req_packed_80 = { pack_write_req_op_sel_76, pack_write_req_local_addr_77, pack_write_req_local_stride_78, pack_write_req_local_size_79 };
  assign _axi_c_write_req_fifo_wdata = ((th_comp == 17) && !_axi_c_write_req_fifo_almost_full)? pack_write_req_packed_80 : 'hx;
  assign _axi_c_write_req_fifo_enq = ((th_comp == 17) && !_axi_c_write_req_fifo_almost_full)? (th_comp == 17) && !_axi_c_write_req_fifo_almost_full && !_axi_c_write_req_fifo_almost_full : 0;
  localparam _tmp_81 = 1;
  wire [_tmp_81-1:0] _tmp_82;
  assign _tmp_82 = !_axi_c_write_req_fifo_almost_full;
  reg [_tmp_81-1:0] __tmp_82_1;
  reg [32-1:0] _axi_c_write_data_fsm;
  localparam _axi_c_write_data_fsm_init = 0;
  assign _axi_c_write_req_fifo_deq = ((_axi_c_write_data_fsm == 0) && (_axi_c_write_data_idle && !_axi_c_write_req_fifo_empty && (_axi_c_write_op_sel_fifo == 1)) && !_axi_c_write_req_fifo_empty)? 1 : 0;
  reg [32-1:0] read_burst_fsm_2;
  localparam read_burst_fsm_2_init = 0;
  reg [10-1:0] read_burst_addr_83;
  reg [10-1:0] read_burst_stride_84;
  reg [33-1:0] read_burst_length_85;
  reg read_burst_rvalid_86;
  reg read_burst_rlast_87;
  assign ram_c_1_addr = ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_86 || (axi_c_tready || !axi_c_tvalid)))? read_burst_addr_83 : 'hx;
  assign ram_c_1_enable = ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_86 || (axi_c_tready || !axi_c_tvalid)))? 1'd1 : 0;
  localparam _tmp_88 = 1;
  wire [_tmp_88-1:0] _tmp_89;
  assign _tmp_89 = (read_burst_fsm_2 == 1) && (!read_burst_rvalid_86 || (axi_c_tready || !axi_c_tvalid));
  reg [_tmp_88-1:0] __tmp_89_1;
  wire [32-1:0] read_burst_rdata_90;
  assign read_burst_rdata_90 = ram_c_1_rdata;
  reg _axi_c_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_a_read_data_idle <= 1;
      _axi_a_read_op_sel_buf <= 0;
      _axi_a_read_local_addr_buf <= 0;
      _axi_a_read_local_stride_buf <= 0;
      _axi_a_read_local_size_buf <= 0;
    end else begin
      if((_axi_a_read_data_fsm == 0) && (_axi_a_read_data_idle && !_axi_a_read_req_fifo_empty && (_axi_a_read_op_sel_fifo == 1))) begin
        _axi_a_read_data_idle <= 0;
        _axi_a_read_op_sel_buf <= _axi_a_read_op_sel_fifo;
        _axi_a_read_local_addr_buf <= _axi_a_read_local_addr_fifo;
        _axi_a_read_local_stride_buf <= _axi_a_read_local_stride_fifo;
        _axi_a_read_local_size_buf <= _axi_a_read_local_size_fifo;
      end 
      if((_axi_a_read_data_fsm == 2) && axi_a_tvalid) begin
        _axi_a_read_local_size_buf <= _axi_a_read_local_size_buf - 1;
      end 
      if((_axi_a_read_data_fsm == 2) && axi_a_tvalid && (_axi_a_read_local_size_buf <= 1)) begin
        _axi_a_read_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_a_read_req_fifo <= 0;
      __tmp_27_1 <= 0;
    end else begin
      if(_axi_a_read_req_fifo_enq && !_axi_a_read_req_fifo_full && (_axi_a_read_req_fifo_deq && !_axi_a_read_req_fifo_empty)) begin
        count__axi_a_read_req_fifo <= count__axi_a_read_req_fifo;
      end else if(_axi_a_read_req_fifo_enq && !_axi_a_read_req_fifo_full) begin
        count__axi_a_read_req_fifo <= count__axi_a_read_req_fifo + 1;
      end else if(_axi_a_read_req_fifo_deq && !_axi_a_read_req_fifo_empty) begin
        count__axi_a_read_req_fifo <= count__axi_a_read_req_fifo - 1;
      end 
      __tmp_27_1 <= _tmp_27;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_b_read_data_idle <= 1;
      _axi_b_read_op_sel_buf <= 0;
      _axi_b_read_local_addr_buf <= 0;
      _axi_b_read_local_stride_buf <= 0;
      _axi_b_read_local_size_buf <= 0;
    end else begin
      if((_axi_b_read_data_fsm == 0) && (_axi_b_read_data_idle && !_axi_b_read_req_fifo_empty && (_axi_b_read_op_sel_fifo == 1))) begin
        _axi_b_read_data_idle <= 0;
        _axi_b_read_op_sel_buf <= _axi_b_read_op_sel_fifo;
        _axi_b_read_local_addr_buf <= _axi_b_read_local_addr_fifo;
        _axi_b_read_local_stride_buf <= _axi_b_read_local_stride_fifo;
        _axi_b_read_local_size_buf <= _axi_b_read_local_size_fifo;
      end 
      if((_axi_b_read_data_fsm == 2) && axi_b_tvalid) begin
        _axi_b_read_local_size_buf <= _axi_b_read_local_size_buf - 1;
      end 
      if((_axi_b_read_data_fsm == 2) && axi_b_tvalid && (_axi_b_read_local_size_buf <= 1)) begin
        _axi_b_read_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_b_read_req_fifo <= 0;
      __tmp_38_1 <= 0;
    end else begin
      if(_axi_b_read_req_fifo_enq && !_axi_b_read_req_fifo_full && (_axi_b_read_req_fifo_deq && !_axi_b_read_req_fifo_empty)) begin
        count__axi_b_read_req_fifo <= count__axi_b_read_req_fifo;
      end else if(_axi_b_read_req_fifo_enq && !_axi_b_read_req_fifo_full) begin
        count__axi_b_read_req_fifo <= count__axi_b_read_req_fifo + 1;
      end else if(_axi_b_read_req_fifo_deq && !_axi_b_read_req_fifo_empty) begin
        count__axi_b_read_req_fifo <= count__axi_b_read_req_fifo - 1;
      end 
      __tmp_38_1 <= _tmp_38;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_c_write_data_idle <= 1;
      _axi_c_write_op_sel_buf <= 0;
      _axi_c_write_local_addr_buf <= 0;
      _axi_c_write_local_stride_buf <= 0;
      _axi_c_write_size_buf <= 0;
      axi_c_tdata <= 0;
      axi_c_tvalid <= 0;
      axi_c_tlast <= 0;
      _axi_c_cond_0_1 <= 0;
    end else begin
      if(_axi_c_cond_0_1) begin
        axi_c_tvalid <= 0;
        axi_c_tlast <= 0;
      end 
      if((_axi_c_write_data_fsm == 0) && (_axi_c_write_data_idle && !_axi_c_write_req_fifo_empty && (_axi_c_write_op_sel_fifo == 1))) begin
        _axi_c_write_data_idle <= 0;
        _axi_c_write_op_sel_buf <= _axi_c_write_op_sel_fifo;
        _axi_c_write_local_addr_buf <= _axi_c_write_local_addr_fifo;
        _axi_c_write_local_stride_buf <= _axi_c_write_local_stride_fifo;
        _axi_c_write_size_buf <= _axi_c_write_size_fifo;
      end 
      if((_axi_c_write_op_sel_buf == 1) && read_burst_rvalid_86 && (axi_c_tready || !axi_c_tvalid) && (axi_c_tready || !axi_c_tvalid)) begin
        axi_c_tdata <= read_burst_rdata_90;
        axi_c_tvalid <= 1;
        axi_c_tlast <= read_burst_rlast_87;
      end 
      _axi_c_cond_0_1 <= 1;
      if(axi_c_tvalid && !axi_c_tready) begin
        axi_c_tvalid <= axi_c_tvalid;
        axi_c_tlast <= axi_c_tlast;
      end 
      if((_axi_c_write_data_fsm == 2) && ((_axi_c_write_op_sel_buf == 1) && read_burst_rvalid_86 && (axi_c_tready || !axi_c_tvalid))) begin
        _axi_c_write_size_buf <= _axi_c_write_size_buf - 1;
      end 
      if((_axi_c_write_data_fsm == 2) && ((_axi_c_write_op_sel_buf == 1) && read_burst_rvalid_86 && (axi_c_tready || !axi_c_tvalid)) && read_burst_rlast_87) begin
        _axi_c_write_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_c_write_req_fifo <= 0;
      __tmp_82_1 <= 0;
    end else begin
      if(_axi_c_write_req_fifo_enq && !_axi_c_write_req_fifo_full && (_axi_c_write_req_fifo_deq && !_axi_c_write_req_fifo_empty)) begin
        count__axi_c_write_req_fifo <= count__axi_c_write_req_fifo;
      end else if(_axi_c_write_req_fifo_enq && !_axi_c_write_req_fifo_full) begin
        count__axi_c_write_req_fifo <= count__axi_c_write_req_fifo + 1;
      end else if(_axi_c_write_req_fifo_deq && !_axi_c_write_req_fifo_empty) begin
        count__axi_c_write_req_fifo <= count__axi_c_write_req_fifo - 1;
      end 
      __tmp_82_1 <= _tmp_82;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_15 <= 0;
      prev_arvalid_16 <= 0;
      writevalid_13 <= 0;
      readvalid_14 <= 0;
      addr_12 <= 0;
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
      prev_awvalid_15 <= saxi_awvalid;
      prev_arvalid_16 <= saxi_arvalid;
      writevalid_13 <= 0;
      readvalid_14 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_12 <= saxi_awaddr;
        writevalid_13 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_12 <= saxi_araddr;
        readvalid_14 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_18;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_19 && (axis_maskaddr_17 == 0)) begin
        _saxi_register_0 <= axislite_resetval_20;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_19 && (axis_maskaddr_17 == 1)) begin
        _saxi_register_1 <= axislite_resetval_20;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_19 && (axis_maskaddr_17 == 2)) begin
        _saxi_register_2 <= axislite_resetval_20;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_19 && (axis_maskaddr_17 == 3)) begin
        _saxi_register_3 <= axislite_resetval_20;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_17 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_17 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_17 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_17 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
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
      if((th_comp == 19) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 19) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 19) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 19) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
      axis_maskaddr_17 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_14 || writevalid_13) begin
            axis_maskaddr_17 <= (addr_12 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_14) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_13) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_2: begin
          if(saxi_wvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_45_1 <= 0;
    end else begin
      __tmp_45_1 <= _tmp_45;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_48_1 <= 0;
    end else begin
      __tmp_48_1 <= _tmp_48;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_89_1 <= 0;
    end else begin
      __tmp_89_1 <= _tmp_89;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_source_ram_renable <= 0;
      _mystream_a_source_fifo_deq <= 0;
      _mystream_a_idle <= 1;
      _mystream_b_source_ram_renable <= 0;
      _mystream_b_source_fifo_deq <= 0;
      _mystream_b_idle <= 1;
      _mystream_c_sink_wenable <= 0;
      _mystream_c_sink_fifo_enq <= 0;
      __mystream_stream_ivalid_1 <= 0;
      _plus_data_2 <= 0;
      _mystream_a_source_mode <= 5'b0;
      _mystream_a_source_offset <= 0;
      _mystream_a_source_size <= 0;
      _mystream_a_source_stride <= 0;
      _mystream_a_source_sel <= 0;
      _mystream_a_source_offset_buf <= 0;
      _mystream_a_source_size_buf <= 0;
      _mystream_a_source_stride_buf <= 0;
      __variable_wdata_0 <= 0;
      _mystream_a_source_ram_raddr <= 0;
      _mystream_a_source_count <= 0;
      _mystream_b_source_mode <= 5'b0;
      _mystream_b_source_offset <= 0;
      _mystream_b_source_size <= 0;
      _mystream_b_source_stride <= 0;
      _mystream_b_source_sel <= 0;
      _mystream_b_source_offset_buf <= 0;
      _mystream_b_source_size_buf <= 0;
      _mystream_b_source_stride_buf <= 0;
      __variable_wdata_1 <= 0;
      _mystream_b_source_ram_raddr <= 0;
      _mystream_b_source_count <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_55 <= 0;
      _tmp_56 <= 0;
      _tmp_57 <= 0;
      _tmp_58 <= 0;
      _mystream_c_sink_mode <= 5'b0;
      _mystream_c_sink_offset <= 0;
      _mystream_c_sink_size <= 0;
      _mystream_c_sink_stride <= 0;
      _mystream_c_sink_sel <= 0;
      _mystream_c_sink_offset_buf <= 0;
      _mystream_c_sink_size_buf <= 0;
      _mystream_c_sink_stride_buf <= 0;
      _mystream_c_sink_waddr <= 0;
      _mystream_c_sink_count <= 0;
      _mystream_c_sink_wdata <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _tmp_69 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_72 <= 0;
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      _mystream_busy_reg <= 0;
    end else begin
      if(_mystream_stream_oready) begin
        _mystream_a_source_ram_renable <= 0;
        _mystream_a_source_fifo_deq <= 0;
      end 
      _mystream_a_idle <= _mystream_a_idle;
      if(_mystream_stream_oready) begin
        _mystream_b_source_ram_renable <= 0;
        _mystream_b_source_fifo_deq <= 0;
      end 
      _mystream_b_idle <= _mystream_b_idle;
      if(_mystream_stream_oready) begin
        _mystream_c_sink_wenable <= 0;
        _mystream_c_sink_fifo_enq <= 0;
      end 
      if(_mystream_stream_oready) begin
        __mystream_stream_ivalid_1 <= _mystream_stream_ivalid;
      end 
      if(_mystream_stream_oready) begin
        _plus_data_2 <= mystream_a_data + mystream_b_data;
      end 
      if(_set_flag_43) begin
        _mystream_a_source_mode <= 5'b1;
        _mystream_a_source_offset <= _th_comp_offset_3;
        _mystream_a_source_size <= _th_comp_size_2;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_43) begin
        _mystream_a_source_sel <= 1;
      end 
      if(_mystream_source_start && _mystream_a_source_mode & 5'b1 && _mystream_stream_oready) begin
        _mystream_a_source_offset_buf <= _mystream_a_source_offset;
        _mystream_a_source_size_buf <= _mystream_a_source_size;
        _mystream_a_source_stride_buf <= _mystream_a_source_stride;
      end 
      if(_mystream_stream_oready && _mystream_source_busy && _mystream_is_root) begin
        __variable_wdata_0 <= _mystream_a_source_ram_rdata;
      end 
      if((_mystream_a_source_fsm_0 == 1) && _mystream_stream_oready) begin
        _mystream_a_idle <= 0;
        _mystream_a_source_ram_raddr <= _mystream_a_source_offset_buf;
        _mystream_a_source_ram_renable <= 1;
        _mystream_a_source_count <= _mystream_a_source_size_buf;
      end 
      if((_mystream_a_source_fsm_0 == 2) && _mystream_stream_oready) begin
        _mystream_a_source_ram_raddr <= _mystream_a_source_ram_raddr + _mystream_a_source_stride_buf;
        _mystream_a_source_ram_renable <= 1;
        _mystream_a_source_count <= _mystream_a_source_count - 1;
      end 
      if((_mystream_a_source_fsm_0 == 2) && (_mystream_a_source_count == 1) && _mystream_stream_oready) begin
        _mystream_a_source_ram_renable <= 0;
        _mystream_a_idle <= 1;
      end 
      if((_mystream_a_source_fsm_0 == 2) && _mystream_source_stop && _mystream_stream_oready) begin
        _mystream_a_source_ram_renable <= 0;
        _mystream_a_idle <= 1;
      end 
      if(_set_flag_46) begin
        _mystream_b_source_mode <= 5'b1;
        _mystream_b_source_offset <= _th_comp_offset_3;
        _mystream_b_source_size <= _th_comp_size_2;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_46) begin
        _mystream_b_source_sel <= 2;
      end 
      if(_mystream_source_start && _mystream_b_source_mode & 5'b1 && _mystream_stream_oready) begin
        _mystream_b_source_offset_buf <= _mystream_b_source_offset;
        _mystream_b_source_size_buf <= _mystream_b_source_size;
        _mystream_b_source_stride_buf <= _mystream_b_source_stride;
      end 
      if(_mystream_stream_oready && _mystream_source_busy && _mystream_is_root) begin
        __variable_wdata_1 <= _mystream_b_source_ram_rdata;
      end 
      if((_mystream_b_source_fsm_1 == 1) && _mystream_stream_oready) begin
        _mystream_b_idle <= 0;
        _mystream_b_source_ram_raddr <= _mystream_b_source_offset_buf;
        _mystream_b_source_ram_renable <= 1;
        _mystream_b_source_count <= _mystream_b_source_size_buf;
      end 
      if((_mystream_b_source_fsm_1 == 2) && _mystream_stream_oready) begin
        _mystream_b_source_ram_raddr <= _mystream_b_source_ram_raddr + _mystream_b_source_stride_buf;
        _mystream_b_source_ram_renable <= 1;
        _mystream_b_source_count <= _mystream_b_source_count - 1;
      end 
      if((_mystream_b_source_fsm_1 == 2) && (_mystream_b_source_count == 1) && _mystream_stream_oready) begin
        _mystream_b_source_ram_renable <= 0;
        _mystream_b_idle <= 1;
      end 
      if((_mystream_b_source_fsm_1 == 2) && _mystream_source_stop && _mystream_stream_oready) begin
        _mystream_b_source_ram_renable <= 0;
        _mystream_b_idle <= 1;
      end 
      if(_mystream_stream_oready) begin
        _tmp_50 <= _set_flag_49;
      end 
      if(_mystream_stream_oready) begin
        _tmp_51 <= _tmp_50;
      end 
      if(_mystream_stream_oready) begin
        _tmp_52 <= _tmp_51;
      end 
      if(_mystream_stream_oready) begin
        _tmp_53 <= _th_comp_offset_3;
      end 
      if(_mystream_stream_oready) begin
        _tmp_54 <= _tmp_53;
      end 
      if(_mystream_stream_oready) begin
        _tmp_55 <= _tmp_54;
      end 
      if(_mystream_stream_oready) begin
        _tmp_56 <= _th_comp_size_2;
      end 
      if(_mystream_stream_oready) begin
        _tmp_57 <= _tmp_56;
      end 
      if(_mystream_stream_oready) begin
        _tmp_58 <= _tmp_57;
      end 
      if(_tmp_52) begin
        _mystream_c_sink_mode <= 5'b1;
        _mystream_c_sink_offset <= _tmp_55;
        _mystream_c_sink_size <= _tmp_58;
        _mystream_c_sink_stride <= 1;
      end 
      if(_tmp_52) begin
        _mystream_c_sink_sel <= 3;
      end 
      if(_mystream_sink_start && _mystream_c_sink_mode & 5'b1 && _mystream_stream_oready) begin
        _mystream_c_sink_offset_buf <= _mystream_c_sink_offset;
        _mystream_c_sink_size_buf <= _mystream_c_sink_size;
        _mystream_c_sink_stride_buf <= _mystream_c_sink_stride;
      end 
      if((_mystream_c_sink_fsm_2 == 1) && _mystream_stream_oready) begin
        _mystream_c_sink_waddr <= _mystream_c_sink_offset_buf - _mystream_c_sink_stride_buf;
        _mystream_c_sink_count <= _mystream_c_sink_size_buf;
      end 
      if((_mystream_c_sink_fsm_2 == 2) && _mystream_stream_oready) begin
        _mystream_c_sink_waddr <= _mystream_c_sink_waddr + _mystream_c_sink_stride_buf;
        _mystream_c_sink_wdata <= mystream_c_data;
        _mystream_c_sink_wenable <= 1;
        _mystream_c_sink_count <= _mystream_c_sink_count - 1;
      end 
      if(_mystream_stream_oready) begin
        _tmp_60 <= _mystream_source_start;
      end 
      if(_mystream_stream_oready) begin
        _tmp_61 <= _tmp_60;
      end 
      if(_mystream_stream_oready) begin
        _tmp_62 <= _tmp_61;
      end 
      if(_mystream_stream_oready) begin
        _tmp_65 <= _tmp_64;
      end 
      if(_mystream_stream_oready) begin
        _tmp_66 <= _mystream_source_start;
      end 
      if(_mystream_stream_oready) begin
        _tmp_67 <= _tmp_66;
      end 
      if(_mystream_stream_oready) begin
        _tmp_68 <= _tmp_67;
      end 
      if(_mystream_stream_oready) begin
        _tmp_69 <= _mystream_source_stop;
      end 
      if(_mystream_stream_oready) begin
        _tmp_70 <= _tmp_69;
      end 
      if(_mystream_stream_oready) begin
        _tmp_71 <= _tmp_70;
      end 
      if(_mystream_stream_oready) begin
        _tmp_72 <= _mystream_source_busy;
      end 
      if(_mystream_stream_oready) begin
        _tmp_73 <= _tmp_72;
      end 
      if(_mystream_stream_oready) begin
        _tmp_74 <= _tmp_73;
      end 
      if(_mystream_stream_oready) begin
        _tmp_75 <= _mystream_sink_busy;
      end 
      if(!_mystream_sink_busy && _tmp_75) begin
        _mystream_busy_reg <= 0;
      end 
      if(_mystream_source_busy) begin
        _mystream_busy_reg <= 1;
      end 
    end
  end

  localparam _mystream_fsm_1 = 1;
  localparam _mystream_fsm_2 = 2;
  localparam _mystream_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm <= _mystream_fsm_init;
      _mystream_source_start <= 0;
      _mystream_source_busy <= 0;
      _mystream_stream_ivalid <= 0;
    end else begin
      if(_mystream_stream_oready && _tmp_62) begin
        _mystream_stream_ivalid <= 1;
      end 
      if(_mystream_stream_oready && _tmp_65) begin
        _mystream_stream_ivalid <= 0;
      end 
      case(_mystream_fsm)
        _mystream_fsm_init: begin
          if(_mystream_run_flag) begin
            _mystream_source_start <= 1;
          end 
          if(_mystream_run_flag) begin
            _mystream_fsm <= _mystream_fsm_1;
          end 
        end
        _mystream_fsm_1: begin
          if(_mystream_source_start && _mystream_stream_oready) begin
            _mystream_source_start <= 0;
            _mystream_source_busy <= 1;
          end 
          if(_mystream_source_start && _mystream_stream_oready) begin
            _mystream_fsm <= _mystream_fsm_2;
          end 
        end
        _mystream_fsm_2: begin
          if(_mystream_stream_oready) begin
            _mystream_fsm <= _mystream_fsm_3;
          end 
        end
        _mystream_fsm_3: begin
          if(_mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3))) begin
            _mystream_source_busy <= 0;
          end 
          if(_mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3)) && _mystream_run_flag) begin
            _mystream_source_start <= 1;
          end 
          if(_mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3))) begin
            _mystream_fsm <= _mystream_fsm_init;
          end 
          if(_mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3)) && _mystream_run_flag) begin
            _mystream_fsm <= _mystream_fsm_1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_offset_1 <= 0;
      _th_comp_size_2 <= 0;
      _th_comp_offset_3 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          if(1) begin
            th_comp <= th_comp_2;
          end else begin
            th_comp <= th_comp_21;
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
          _th_comp_size_0 <= _saxi_register_2;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          _th_comp_offset_1 <= 0;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          if(!_axi_a_read_req_fifo_almost_full) begin
            th_comp <= th_comp_7;
          end 
        end
        th_comp_7: begin
          if(!_axi_b_read_req_fifo_almost_full) begin
            th_comp <= th_comp_8;
          end 
        end
        th_comp_8: begin
          if(_axi_a_read_idle) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          if(_axi_b_read_idle) begin
            th_comp <= th_comp_10;
          end 
        end
        th_comp_10: begin
          _th_comp_size_2 <= _th_comp_size_0;
          _th_comp_offset_3 <= _th_comp_offset_1;
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          if(_mystream_stream_oready) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(_mystream_busy) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_17;
          end 
        end
        th_comp_17: begin
          if(!_axi_c_write_req_fifo_almost_full) begin
            th_comp <= th_comp_18;
          end 
        end
        th_comp_18: begin
          if(_axi_c_write_idle) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          th_comp <= th_comp_1;
        end
        th_comp_21: begin
          $finish;
          th_comp <= th_comp_22;
        end
      endcase
    end
  end

  localparam _axi_a_read_data_fsm_1 = 1;
  localparam _axi_a_read_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_a_read_data_fsm <= _axi_a_read_data_fsm_init;
    end else begin
      case(_axi_a_read_data_fsm)
        _axi_a_read_data_fsm_init: begin
          if(_axi_a_read_data_idle && !_axi_a_read_req_fifo_empty && (_axi_a_read_op_sel_fifo == 1)) begin
            _axi_a_read_data_fsm <= _axi_a_read_data_fsm_1;
          end 
        end
        _axi_a_read_data_fsm_1: begin
          _axi_a_read_data_fsm <= _axi_a_read_data_fsm_2;
        end
        _axi_a_read_data_fsm_2: begin
          if(axi_a_tvalid && (_axi_a_read_local_size_buf <= 1)) begin
            _axi_a_read_data_fsm <= _axi_a_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_0_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_0 <= write_burst_fsm_0_init;
      write_burst_addr_28 <= 0;
      write_burst_stride_29 <= 0;
      write_burst_length_30 <= 0;
      write_burst_done_31 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_28 <= _axi_a_read_local_addr_buf;
          write_burst_stride_29 <= _axi_a_read_local_stride_buf;
          write_burst_length_30 <= _axi_a_read_local_size_buf;
          write_burst_done_31 <= 0;
          if((_axi_a_read_data_fsm == 1) && (_axi_a_read_op_sel_buf == 1) && (_axi_a_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(axi_a_tvalid) begin
            write_burst_addr_28 <= write_burst_addr_28 + write_burst_stride_29;
            write_burst_length_30 <= write_burst_length_30 - 1;
            write_burst_done_31 <= 0;
          end 
          if(axi_a_tvalid && (write_burst_length_30 <= 1)) begin
            write_burst_done_31 <= 1;
          end 
          if(axi_a_tvalid && 0) begin
            write_burst_done_31 <= 1;
          end 
          if(axi_a_tvalid && (write_burst_length_30 <= 1)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(axi_a_tvalid && 0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _axi_b_read_data_fsm_1 = 1;
  localparam _axi_b_read_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_b_read_data_fsm <= _axi_b_read_data_fsm_init;
    end else begin
      case(_axi_b_read_data_fsm)
        _axi_b_read_data_fsm_init: begin
          if(_axi_b_read_data_idle && !_axi_b_read_req_fifo_empty && (_axi_b_read_op_sel_fifo == 1)) begin
            _axi_b_read_data_fsm <= _axi_b_read_data_fsm_1;
          end 
        end
        _axi_b_read_data_fsm_1: begin
          _axi_b_read_data_fsm <= _axi_b_read_data_fsm_2;
        end
        _axi_b_read_data_fsm_2: begin
          if(axi_b_tvalid && (_axi_b_read_local_size_buf <= 1)) begin
            _axi_b_read_data_fsm <= _axi_b_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_1 <= write_burst_fsm_1_init;
      write_burst_addr_39 <= 0;
      write_burst_stride_40 <= 0;
      write_burst_length_41 <= 0;
      write_burst_done_42 <= 0;
    end else begin
      case(write_burst_fsm_1)
        write_burst_fsm_1_init: begin
          write_burst_addr_39 <= _axi_b_read_local_addr_buf;
          write_burst_stride_40 <= _axi_b_read_local_stride_buf;
          write_burst_length_41 <= _axi_b_read_local_size_buf;
          write_burst_done_42 <= 0;
          if((_axi_b_read_data_fsm == 1) && (_axi_b_read_op_sel_buf == 1) && (_axi_b_read_local_size_buf > 0)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_1;
          end 
        end
        write_burst_fsm_1_1: begin
          if(axi_b_tvalid) begin
            write_burst_addr_39 <= write_burst_addr_39 + write_burst_stride_40;
            write_burst_length_41 <= write_burst_length_41 - 1;
            write_burst_done_42 <= 0;
          end 
          if(axi_b_tvalid && (write_burst_length_41 <= 1)) begin
            write_burst_done_42 <= 1;
          end 
          if(axi_b_tvalid && 0) begin
            write_burst_done_42 <= 1;
          end 
          if(axi_b_tvalid && (write_burst_length_41 <= 1)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(axi_b_tvalid && 0) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(0) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_a_source_fsm_0_1 = 1;
  localparam _mystream_a_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
    end else begin
      case(_mystream_a_source_fsm_0)
        _mystream_a_source_fsm_0_init: begin
          if(_mystream_source_start && _mystream_a_source_mode & 5'b1 && _mystream_stream_oready) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_1;
          end 
        end
        _mystream_a_source_fsm_0_1: begin
          if(_mystream_stream_oready) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_2;
          end 
        end
        _mystream_a_source_fsm_0_2: begin
          if((_mystream_a_source_count == 1) && _mystream_stream_oready) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
          end 
          if(_mystream_source_stop && _mystream_stream_oready) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_b_source_fsm_1_1 = 1;
  localparam _mystream_b_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
    end else begin
      case(_mystream_b_source_fsm_1)
        _mystream_b_source_fsm_1_init: begin
          if(_mystream_source_start && _mystream_b_source_mode & 5'b1 && _mystream_stream_oready) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_1;
          end 
        end
        _mystream_b_source_fsm_1_1: begin
          if(_mystream_stream_oready) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_2;
          end 
        end
        _mystream_b_source_fsm_1_2: begin
          if((_mystream_b_source_count == 1) && _mystream_stream_oready) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
          end 
          if(_mystream_source_stop && _mystream_stream_oready) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_c_sink_fsm_2_1 = 1;
  localparam _mystream_c_sink_fsm_2_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
    end else begin
      case(_mystream_c_sink_fsm_2)
        _mystream_c_sink_fsm_2_init: begin
          if(_mystream_sink_start && _mystream_c_sink_mode & 5'b1 && _mystream_stream_oready) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_1;
          end 
        end
        _mystream_c_sink_fsm_2_1: begin
          if(_mystream_stream_oready) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_2;
          end 
        end
        _mystream_c_sink_fsm_2_2: begin
          if((_mystream_c_sink_count == 1) && _mystream_stream_oready) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
          end 
          if(_mystream_sink_stop && _mystream_stream_oready) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _axi_c_write_data_fsm_1 = 1;
  localparam _axi_c_write_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_c_write_data_fsm <= _axi_c_write_data_fsm_init;
    end else begin
      case(_axi_c_write_data_fsm)
        _axi_c_write_data_fsm_init: begin
          if(_axi_c_write_data_idle && !_axi_c_write_req_fifo_empty && (_axi_c_write_op_sel_fifo == 1)) begin
            _axi_c_write_data_fsm <= _axi_c_write_data_fsm_1;
          end 
        end
        _axi_c_write_data_fsm_1: begin
          _axi_c_write_data_fsm <= _axi_c_write_data_fsm_2;
        end
        _axi_c_write_data_fsm_2: begin
          if((_axi_c_write_op_sel_buf == 1) && read_burst_rvalid_86 && (axi_c_tready || !axi_c_tvalid) && read_burst_rlast_87) begin
            _axi_c_write_data_fsm <= _axi_c_write_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam read_burst_fsm_2_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      read_burst_fsm_2 <= read_burst_fsm_2_init;
      read_burst_addr_83 <= 0;
      read_burst_stride_84 <= 0;
      read_burst_length_85 <= 0;
      read_burst_rvalid_86 <= 0;
      read_burst_rlast_87 <= 0;
    end else begin
      case(read_burst_fsm_2)
        read_burst_fsm_2_init: begin
          read_burst_addr_83 <= _axi_c_write_local_addr_buf;
          read_burst_stride_84 <= _axi_c_write_local_stride_buf;
          read_burst_length_85 <= _axi_c_write_size_buf;
          read_burst_rvalid_86 <= 0;
          read_burst_rlast_87 <= 0;
          if((_axi_c_write_data_fsm == 1) && (_axi_c_write_op_sel_buf == 1) && (_axi_c_write_size_buf > 0)) begin
            read_burst_fsm_2 <= read_burst_fsm_2_1;
          end 
        end
        read_burst_fsm_2_1: begin
          if((axi_c_tready || !axi_c_tvalid) && (read_burst_length_85 > 0)) begin
            read_burst_addr_83 <= read_burst_addr_83 + read_burst_stride_84;
            read_burst_length_85 <= read_burst_length_85 - 1;
            read_burst_rvalid_86 <= 1;
          end 
          if((axi_c_tready || !axi_c_tvalid) && (read_burst_length_85 <= 1)) begin
            read_burst_rlast_87 <= 1;
          end 
          if(read_burst_rlast_87 && read_burst_rvalid_86 && (axi_c_tready || !axi_c_tvalid)) begin
            read_burst_rvalid_86 <= 0;
            read_burst_rlast_87 <= 0;
          end 
          if(0) begin
            read_burst_rvalid_86 <= 0;
            read_burst_rlast_87 <= 0;
          end 
          if(read_burst_rlast_87 && read_burst_rvalid_86 && (axi_c_tready || !axi_c_tvalid)) begin
            read_burst_fsm_2 <= read_burst_fsm_2_init;
          end 
          if(0) begin
            read_burst_fsm_2 <= read_burst_fsm_2_init;
          end 
        end
      endcase
    end
  end


endmodule



module _axi_a_read_req_fifo
(
  input CLK,
  input RST,
  input _axi_a_read_req_fifo_enq,
  input [105-1:0] _axi_a_read_req_fifo_wdata,
  output _axi_a_read_req_fifo_full,
  output _axi_a_read_req_fifo_almost_full,
  input _axi_a_read_req_fifo_deq,
  output [105-1:0] _axi_a_read_req_fifo_rdata,
  output _axi_a_read_req_fifo_empty,
  output _axi_a_read_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _axi_a_read_req_fifo_full = is_full;
  assign _axi_a_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_a_read_req_fifo_empty = is_empty;
  assign _axi_a_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_a_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_a_read_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_a_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_a_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _axi_b_read_req_fifo
(
  input CLK,
  input RST,
  input _axi_b_read_req_fifo_enq,
  input [105-1:0] _axi_b_read_req_fifo_wdata,
  output _axi_b_read_req_fifo_full,
  output _axi_b_read_req_fifo_almost_full,
  input _axi_b_read_req_fifo_deq,
  output [105-1:0] _axi_b_read_req_fifo_rdata,
  output _axi_b_read_req_fifo_empty,
  output _axi_b_read_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _axi_b_read_req_fifo_full = is_full;
  assign _axi_b_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_b_read_req_fifo_empty = is_empty;
  assign _axi_b_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_b_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_b_read_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_b_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_b_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _axi_c_write_req_fifo
(
  input CLK,
  input RST,
  input _axi_c_write_req_fifo_enq,
  input [105-1:0] _axi_c_write_req_fifo_wdata,
  output _axi_c_write_req_fifo_full,
  output _axi_c_write_req_fifo_almost_full,
  input _axi_c_write_req_fifo_deq,
  output [105-1:0] _axi_c_write_req_fifo_rdata,
  output _axi_c_write_req_fifo_empty,
  output _axi_c_write_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _axi_c_write_req_fifo_full = is_full;
  assign _axi_c_write_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_c_write_req_fifo_empty = is_empty;
  assign _axi_c_write_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_c_write_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_c_write_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_c_write_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_c_write_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module ram_a
(
  input CLK,
  input [10-1:0] ram_a_0_addr,
  output [32-1:0] ram_a_0_rdata,
  input [32-1:0] ram_a_0_wdata,
  input ram_a_0_wenable,
  input ram_a_0_enable,
  input [10-1:0] ram_a_1_addr,
  output [32-1:0] ram_a_1_rdata,
  input [32-1:0] ram_a_1_wdata,
  input ram_a_1_wenable,
  input ram_a_1_enable
);

  reg [32-1:0] ram_a_0_rdata_out;
  assign ram_a_0_rdata = ram_a_0_rdata_out;
  reg [32-1:0] ram_a_1_rdata_out;
  assign ram_a_1_rdata = ram_a_1_rdata_out;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_0_enable) begin
      if(ram_a_0_wenable) begin
        mem[ram_a_0_addr] <= ram_a_0_wdata;
        ram_a_0_rdata_out <= ram_a_0_wdata;
      end else begin
        ram_a_0_rdata_out <= mem[ram_a_0_addr];
      end
    end 
  end


  always @(posedge CLK) begin
    if(ram_a_1_enable) begin
      if(ram_a_1_wenable) begin
        mem[ram_a_1_addr] <= ram_a_1_wdata;
        ram_a_1_rdata_out <= ram_a_1_wdata;
      end else begin
        ram_a_1_rdata_out <= mem[ram_a_1_addr];
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
  input ram_b_0_enable,
  input [10-1:0] ram_b_1_addr,
  output [32-1:0] ram_b_1_rdata,
  input [32-1:0] ram_b_1_wdata,
  input ram_b_1_wenable,
  input ram_b_1_enable
);

  reg [32-1:0] ram_b_0_rdata_out;
  assign ram_b_0_rdata = ram_b_0_rdata_out;
  reg [32-1:0] ram_b_1_rdata_out;
  assign ram_b_1_rdata = ram_b_1_rdata_out;
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


  always @(posedge CLK) begin
    if(ram_b_1_enable) begin
      if(ram_b_1_wenable) begin
        mem[ram_b_1_addr] <= ram_b_1_wdata;
        ram_b_1_rdata_out <= ram_b_1_wdata;
      end else begin
        ram_b_1_rdata_out <= mem[ram_b_1_addr];
      end
    end 
  end


endmodule



module ram_c
(
  input CLK,
  input [10-1:0] ram_c_0_addr,
  output [32-1:0] ram_c_0_rdata,
  input [32-1:0] ram_c_0_wdata,
  input ram_c_0_wenable,
  input ram_c_0_enable,
  input [10-1:0] ram_c_1_addr,
  output [32-1:0] ram_c_1_rdata,
  input [32-1:0] ram_c_1_wdata,
  input ram_c_1_wenable,
  input ram_c_1_enable
);

  reg [32-1:0] ram_c_0_rdata_out;
  assign ram_c_0_rdata = ram_c_0_rdata_out;
  reg [32-1:0] ram_c_1_rdata_out;
  assign ram_c_1_rdata = ram_c_1_rdata_out;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_0_enable) begin
      if(ram_c_0_wenable) begin
        mem[ram_c_0_addr] <= ram_c_0_wdata;
        ram_c_0_rdata_out <= ram_c_0_wdata;
      end else begin
        ram_c_0_rdata_out <= mem[ram_c_0_addr];
      end
    end 
  end


  always @(posedge CLK) begin
    if(ram_c_1_enable) begin
      if(ram_c_1_wenable) begin
        mem[ram_c_1_addr] <= ram_c_1_wdata;
        ram_c_1_rdata_out <= ram_c_1_wdata;
      end else begin
        ram_c_1_rdata_out <= mem[ram_c_1_addr];
      end
    end 
  end


endmodule
"""


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    code = thread_stream_axi_stream_async.run(filename=None, simtype=simtype,
                                              outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
