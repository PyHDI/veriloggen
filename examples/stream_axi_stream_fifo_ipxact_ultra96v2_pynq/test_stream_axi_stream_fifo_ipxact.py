from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import stream_axi_stream_fifo_ipxact


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
  output [32-1:0] maxi_wdata,
  output [4-1:0] maxi_wstrb,
  output maxi_wlast,
  output maxi_wvalid,
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
  reg [32-1:0] _maxi_wdata_sb_0;
  reg [4-1:0] _maxi_wstrb_sb_0;
  reg _maxi_wlast_sb_0;
  reg _maxi_wvalid_sb_0;
  wire _maxi_wready_sb_0;
  wire _sb_maxi_writedata_s_value_0;
  assign _sb_maxi_writedata_s_value_0 = _maxi_wlast_sb_0;
  wire [4-1:0] _sb_maxi_writedata_s_value_1;
  assign _sb_maxi_writedata_s_value_1 = _maxi_wstrb_sb_0;
  wire [32-1:0] _sb_maxi_writedata_s_value_2;
  assign _sb_maxi_writedata_s_value_2 = _maxi_wdata_sb_0;
  wire [37-1:0] _sb_maxi_writedata_s_data_3;
  assign _sb_maxi_writedata_s_data_3 = { _sb_maxi_writedata_s_value_0, _sb_maxi_writedata_s_value_1, _sb_maxi_writedata_s_value_2 };
  wire _sb_maxi_writedata_s_valid_4;
  assign _sb_maxi_writedata_s_valid_4 = _maxi_wvalid_sb_0;
  wire _sb_maxi_writedata_m_ready_5;
  assign _sb_maxi_writedata_m_ready_5 = maxi_wready;
  reg [37-1:0] _sb_maxi_writedata_data_6;
  reg _sb_maxi_writedata_valid_7;
  wire _sb_maxi_writedata_ready_8;
  reg [37-1:0] _sb_maxi_writedata_tmp_data_9;
  reg _sb_maxi_writedata_tmp_valid_10;
  wire [37-1:0] _sb_maxi_writedata_next_data_11;
  wire _sb_maxi_writedata_next_valid_12;
  assign _sb_maxi_writedata_ready_8 = !_sb_maxi_writedata_tmp_valid_10;
  assign _sb_maxi_writedata_next_data_11 = (_sb_maxi_writedata_tmp_valid_10)? _sb_maxi_writedata_tmp_data_9 : _sb_maxi_writedata_s_data_3;
  assign _sb_maxi_writedata_next_valid_12 = _sb_maxi_writedata_tmp_valid_10 || _sb_maxi_writedata_s_valid_4;
  wire _sb_maxi_writedata_m_value_13;
  assign _sb_maxi_writedata_m_value_13 = _sb_maxi_writedata_data_6[36:36];
  wire [4-1:0] _sb_maxi_writedata_m_value_14;
  assign _sb_maxi_writedata_m_value_14 = _sb_maxi_writedata_data_6[35:32];
  wire [32-1:0] _sb_maxi_writedata_m_value_15;
  assign _sb_maxi_writedata_m_value_15 = _sb_maxi_writedata_data_6[31:0];
  assign _maxi_wready_sb_0 = _sb_maxi_writedata_ready_8;
  assign maxi_wdata = _sb_maxi_writedata_m_value_15;
  assign maxi_wstrb = _sb_maxi_writedata_m_value_14;
  assign maxi_wlast = _sb_maxi_writedata_m_value_13;
  assign maxi_wvalid = _sb_maxi_writedata_valid_7;
  assign maxi_bready = 1;
  assign maxi_arsize = 2;
  assign maxi_arburst = 1;
  assign maxi_arlock = 0;
  assign maxi_arcache = 3;
  assign maxi_arprot = 0;
  assign maxi_arqos = 0;
  assign maxi_aruser = 0;
  wire [32-1:0] _maxi_rdata_sb_0;
  wire _maxi_rlast_sb_0;
  wire _maxi_rvalid_sb_0;
  wire _maxi_rready_sb_0;
  wire _sb_maxi_readdata_s_value_16;
  assign _sb_maxi_readdata_s_value_16 = maxi_rlast;
  wire [32-1:0] _sb_maxi_readdata_s_value_17;
  assign _sb_maxi_readdata_s_value_17 = maxi_rdata;
  wire [33-1:0] _sb_maxi_readdata_s_data_18;
  assign _sb_maxi_readdata_s_data_18 = { _sb_maxi_readdata_s_value_16, _sb_maxi_readdata_s_value_17 };
  wire _sb_maxi_readdata_s_valid_19;
  assign _sb_maxi_readdata_s_valid_19 = maxi_rvalid;
  wire _sb_maxi_readdata_m_ready_20;
  assign _sb_maxi_readdata_m_ready_20 = _maxi_rready_sb_0;
  reg [33-1:0] _sb_maxi_readdata_data_21;
  reg _sb_maxi_readdata_valid_22;
  wire _sb_maxi_readdata_ready_23;
  reg [33-1:0] _sb_maxi_readdata_tmp_data_24;
  reg _sb_maxi_readdata_tmp_valid_25;
  wire [33-1:0] _sb_maxi_readdata_next_data_26;
  wire _sb_maxi_readdata_next_valid_27;
  assign _sb_maxi_readdata_ready_23 = !_sb_maxi_readdata_tmp_valid_25;
  assign _sb_maxi_readdata_next_data_26 = (_sb_maxi_readdata_tmp_valid_25)? _sb_maxi_readdata_tmp_data_24 : _sb_maxi_readdata_s_data_18;
  assign _sb_maxi_readdata_next_valid_27 = _sb_maxi_readdata_tmp_valid_25 || _sb_maxi_readdata_s_valid_19;
  wire _sb_maxi_readdata_m_value_28;
  assign _sb_maxi_readdata_m_value_28 = _sb_maxi_readdata_data_21[32:32];
  wire [32-1:0] _sb_maxi_readdata_m_value_29;
  assign _sb_maxi_readdata_m_value_29 = _sb_maxi_readdata_data_21[31:0];
  assign _maxi_rdata_sb_0 = _sb_maxi_readdata_m_value_29;
  assign _maxi_rlast_sb_0 = _sb_maxi_readdata_m_value_28;
  assign _maxi_rvalid_sb_0 = _sb_maxi_readdata_valid_22;
  assign maxi_rready = _sb_maxi_readdata_ready_23;
  reg [3-1:0] _maxi_outstanding_wcount;
  wire _maxi_has_outstanding_write;
  assign _maxi_has_outstanding_write = (_maxi_outstanding_wcount > 0) || maxi_awvalid;
  reg _maxi_read_start;
  reg [8-1:0] _maxi_read_op_sel;
  reg [32-1:0] _maxi_read_global_addr;
  reg [33-1:0] _maxi_read_global_size;
  reg [32-1:0] _maxi_read_local_addr;
  reg [32-1:0] _maxi_read_local_stride;
  reg [33-1:0] _maxi_read_local_size;
  reg [32-1:0] _maxi_read_local_blocksize;
  wire _maxi_read_req_fifo_enq;
  wire [137-1:0] _maxi_read_req_fifo_wdata;
  wire _maxi_read_req_fifo_full;
  wire _maxi_read_req_fifo_almost_full;
  wire _maxi_read_req_fifo_deq;
  wire [137-1:0] _maxi_read_req_fifo_rdata;
  wire _maxi_read_req_fifo_empty;
  wire _maxi_read_req_fifo_almost_empty;

  _maxi_read_req_fifo
  inst__maxi_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._maxi_read_req_fifo_enq(_maxi_read_req_fifo_enq),
    ._maxi_read_req_fifo_wdata(_maxi_read_req_fifo_wdata),
    ._maxi_read_req_fifo_full(_maxi_read_req_fifo_full),
    ._maxi_read_req_fifo_almost_full(_maxi_read_req_fifo_almost_full),
    ._maxi_read_req_fifo_deq(_maxi_read_req_fifo_deq),
    ._maxi_read_req_fifo_rdata(_maxi_read_req_fifo_rdata),
    ._maxi_read_req_fifo_empty(_maxi_read_req_fifo_empty),
    ._maxi_read_req_fifo_almost_empty(_maxi_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__maxi_read_req_fifo;
  wire [8-1:0] _maxi_read_op_sel_fifo;
  wire [32-1:0] _maxi_read_local_addr_fifo;
  wire [32-1:0] _maxi_read_local_stride_fifo;
  wire [33-1:0] _maxi_read_local_size_fifo;
  wire [32-1:0] _maxi_read_local_blocksize_fifo;
  wire [8-1:0] unpack_read_req_op_sel_30;
  wire [32-1:0] unpack_read_req_local_addr_31;
  wire [32-1:0] unpack_read_req_local_stride_32;
  wire [33-1:0] unpack_read_req_local_size_33;
  wire [32-1:0] unpack_read_req_local_blocksize_34;
  assign unpack_read_req_op_sel_30 = _maxi_read_req_fifo_rdata[136:129];
  assign unpack_read_req_local_addr_31 = _maxi_read_req_fifo_rdata[128:97];
  assign unpack_read_req_local_stride_32 = _maxi_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_size_33 = _maxi_read_req_fifo_rdata[64:32];
  assign unpack_read_req_local_blocksize_34 = _maxi_read_req_fifo_rdata[31:0];
  assign _maxi_read_op_sel_fifo = unpack_read_req_op_sel_30;
  assign _maxi_read_local_addr_fifo = unpack_read_req_local_addr_31;
  assign _maxi_read_local_stride_fifo = unpack_read_req_local_stride_32;
  assign _maxi_read_local_size_fifo = unpack_read_req_local_size_33;
  assign _maxi_read_local_blocksize_fifo = unpack_read_req_local_blocksize_34;
  reg [8-1:0] _maxi_read_op_sel_buf;
  reg [32-1:0] _maxi_read_local_addr_buf;
  reg [32-1:0] _maxi_read_local_stride_buf;
  reg [33-1:0] _maxi_read_local_size_buf;
  reg [32-1:0] _maxi_read_local_blocksize_buf;
  reg _maxi_read_req_busy;
  reg _maxi_read_data_busy;
  wire _maxi_read_req_idle;
  wire _maxi_read_data_idle;
  wire _maxi_read_idle;
  assign _maxi_read_req_idle = !_maxi_read_start && !_maxi_read_req_busy;
  assign _maxi_read_data_idle = _maxi_read_req_fifo_empty && !_maxi_read_data_busy;
  assign _maxi_read_idle = _maxi_read_req_idle && _maxi_read_data_idle;
  reg _maxi_write_start;
  reg [8-1:0] _maxi_write_op_sel;
  reg [32-1:0] _maxi_write_global_addr;
  reg [33-1:0] _maxi_write_global_size;
  reg [32-1:0] _maxi_write_local_addr;
  reg [32-1:0] _maxi_write_local_stride;
  reg [33-1:0] _maxi_write_local_size;
  reg [32-1:0] _maxi_write_local_blocksize;
  wire _maxi_write_req_fifo_enq;
  wire [137-1:0] _maxi_write_req_fifo_wdata;
  wire _maxi_write_req_fifo_full;
  wire _maxi_write_req_fifo_almost_full;
  wire _maxi_write_req_fifo_deq;
  wire [137-1:0] _maxi_write_req_fifo_rdata;
  wire _maxi_write_req_fifo_empty;
  wire _maxi_write_req_fifo_almost_empty;
  assign _maxi_write_req_fifo_enq = 0;
  assign _maxi_write_req_fifo_wdata = 'hx;
  assign _maxi_write_req_fifo_deq = 0;

  _maxi_write_req_fifo
  inst__maxi_write_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._maxi_write_req_fifo_enq(_maxi_write_req_fifo_enq),
    ._maxi_write_req_fifo_wdata(_maxi_write_req_fifo_wdata),
    ._maxi_write_req_fifo_full(_maxi_write_req_fifo_full),
    ._maxi_write_req_fifo_almost_full(_maxi_write_req_fifo_almost_full),
    ._maxi_write_req_fifo_deq(_maxi_write_req_fifo_deq),
    ._maxi_write_req_fifo_rdata(_maxi_write_req_fifo_rdata),
    ._maxi_write_req_fifo_empty(_maxi_write_req_fifo_empty),
    ._maxi_write_req_fifo_almost_empty(_maxi_write_req_fifo_almost_empty)
  );

  reg [4-1:0] count__maxi_write_req_fifo;
  wire [8-1:0] _maxi_write_op_sel_fifo;
  wire [32-1:0] _maxi_write_local_addr_fifo;
  wire [32-1:0] _maxi_write_local_stride_fifo;
  wire [33-1:0] _maxi_write_size_fifo;
  wire [32-1:0] _maxi_write_local_blocksize_fifo;
  wire [8-1:0] unpack_write_req_op_sel_35;
  wire [32-1:0] unpack_write_req_local_addr_36;
  wire [32-1:0] unpack_write_req_local_stride_37;
  wire [33-1:0] unpack_write_req_size_38;
  wire [32-1:0] unpack_write_req_local_blocksize_39;
  assign unpack_write_req_op_sel_35 = _maxi_write_req_fifo_rdata[136:129];
  assign unpack_write_req_local_addr_36 = _maxi_write_req_fifo_rdata[128:97];
  assign unpack_write_req_local_stride_37 = _maxi_write_req_fifo_rdata[96:65];
  assign unpack_write_req_size_38 = _maxi_write_req_fifo_rdata[64:32];
  assign unpack_write_req_local_blocksize_39 = _maxi_write_req_fifo_rdata[31:0];
  assign _maxi_write_op_sel_fifo = unpack_write_req_op_sel_35;
  assign _maxi_write_local_addr_fifo = unpack_write_req_local_addr_36;
  assign _maxi_write_local_stride_fifo = unpack_write_req_local_stride_37;
  assign _maxi_write_size_fifo = unpack_write_req_size_38;
  assign _maxi_write_local_blocksize_fifo = unpack_write_req_local_blocksize_39;
  reg [8-1:0] _maxi_write_op_sel_buf;
  reg [32-1:0] _maxi_write_local_addr_buf;
  reg [32-1:0] _maxi_write_local_stride_buf;
  reg [33-1:0] _maxi_write_size_buf;
  reg [32-1:0] _maxi_write_local_blocksize_buf;
  reg _maxi_write_req_busy;
  reg _maxi_write_data_busy;
  wire _maxi_write_req_idle;
  wire _maxi_write_data_idle;
  wire _maxi_write_idle;
  assign _maxi_write_req_idle = !_maxi_write_start && !_maxi_write_req_busy;
  assign _maxi_write_data_idle = _maxi_write_req_fifo_empty && !_maxi_write_data_busy;
  assign _maxi_write_idle = _maxi_write_req_idle && _maxi_write_data_idle;
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
  reg [32-1:0] addr_40;
  reg writevalid_41;
  reg readvalid_42;
  reg prev_awvalid_43;
  reg prev_arvalid_44;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_41 && !readvalid_42 && !saxi_bvalid && prev_awvalid_43);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_42 && !writevalid_41 && prev_arvalid_44 && !prev_awvalid_43);
  reg [_saxi_maskwidth-1:0] axis_maskaddr_45;
  wire signed [32-1:0] axislite_rdata_46;
  assign axislite_rdata_46 = (axis_maskaddr_45 == 0)? _saxi_register_0 : 
                             (axis_maskaddr_45 == 1)? _saxi_register_1 : 
                             (axis_maskaddr_45 == 2)? _saxi_register_2 : 
                             (axis_maskaddr_45 == 3)? _saxi_register_3 : 
                             (axis_maskaddr_45 == 4)? _saxi_register_4 : 
                             (axis_maskaddr_45 == 5)? _saxi_register_5 : 
                             (axis_maskaddr_45 == 6)? _saxi_register_6 : 
                             (axis_maskaddr_45 == 7)? _saxi_register_7 : 'hx;
  wire axislite_flag_47;
  assign axislite_flag_47 = (axis_maskaddr_45 == 0)? _saxi_flag_0 : 
                            (axis_maskaddr_45 == 1)? _saxi_flag_1 : 
                            (axis_maskaddr_45 == 2)? _saxi_flag_2 : 
                            (axis_maskaddr_45 == 3)? _saxi_flag_3 : 
                            (axis_maskaddr_45 == 4)? _saxi_flag_4 : 
                            (axis_maskaddr_45 == 5)? _saxi_flag_5 : 
                            (axis_maskaddr_45 == 6)? _saxi_flag_6 : 
                            (axis_maskaddr_45 == 7)? _saxi_flag_7 : 'hx;
  wire signed [32-1:0] axislite_resetval_48;
  assign axislite_resetval_48 = (axis_maskaddr_45 == 0)? _saxi_resetval_0 : 
                                (axis_maskaddr_45 == 1)? _saxi_resetval_1 : 
                                (axis_maskaddr_45 == 2)? _saxi_resetval_2 : 
                                (axis_maskaddr_45 == 3)? _saxi_resetval_3 : 
                                (axis_maskaddr_45 == 4)? _saxi_resetval_4 : 
                                (axis_maskaddr_45 == 5)? _saxi_resetval_5 : 
                                (axis_maskaddr_45 == 6)? _saxi_resetval_6 : 
                                (axis_maskaddr_45 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_rdata_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 3;
  wire _axi_in_read_req_fifo_enq;
  wire [41-1:0] _axi_in_read_req_fifo_wdata;
  wire _axi_in_read_req_fifo_full;
  wire _axi_in_read_req_fifo_almost_full;
  wire _axi_in_read_req_fifo_deq;
  wire [41-1:0] _axi_in_read_req_fifo_rdata;
  wire _axi_in_read_req_fifo_empty;
  wire _axi_in_read_req_fifo_almost_empty;

  _axi_in_read_req_fifo
  inst__axi_in_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_in_read_req_fifo_enq(_axi_in_read_req_fifo_enq),
    ._axi_in_read_req_fifo_wdata(_axi_in_read_req_fifo_wdata),
    ._axi_in_read_req_fifo_full(_axi_in_read_req_fifo_full),
    ._axi_in_read_req_fifo_almost_full(_axi_in_read_req_fifo_almost_full),
    ._axi_in_read_req_fifo_deq(_axi_in_read_req_fifo_deq),
    ._axi_in_read_req_fifo_rdata(_axi_in_read_req_fifo_rdata),
    ._axi_in_read_req_fifo_empty(_axi_in_read_req_fifo_empty),
    ._axi_in_read_req_fifo_almost_empty(_axi_in_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_in_read_req_fifo;
  wire [8-1:0] _axi_in_read_op_sel_fifo;
  wire [33-1:0] _axi_in_read_local_size_fifo;
  wire [8-1:0] unpack_read_req_op_sel_49;
  wire [33-1:0] unpack_read_req_local_size_50;
  assign unpack_read_req_op_sel_49 = _axi_in_read_req_fifo_rdata[40:33];
  assign unpack_read_req_local_size_50 = _axi_in_read_req_fifo_rdata[32:0];
  assign _axi_in_read_op_sel_fifo = unpack_read_req_op_sel_49;
  assign _axi_in_read_local_size_fifo = unpack_read_req_local_size_50;
  reg [8-1:0] _axi_in_read_op_sel_buf;
  reg [33-1:0] _axi_in_read_local_size_buf;
  reg _axi_in_read_data_busy;
  wire _axi_in_read_data_idle;
  wire _axi_in_read_idle;
  assign _axi_in_read_data_idle = _axi_in_read_req_fifo_empty && !_axi_in_read_data_busy;
  assign _axi_in_read_idle = _axi_in_read_data_idle;
  wire _axi_out_write_req_fifo_enq;
  wire [41-1:0] _axi_out_write_req_fifo_wdata;
  wire _axi_out_write_req_fifo_full;
  wire _axi_out_write_req_fifo_almost_full;
  wire _axi_out_write_req_fifo_deq;
  wire [41-1:0] _axi_out_write_req_fifo_rdata;
  wire _axi_out_write_req_fifo_empty;
  wire _axi_out_write_req_fifo_almost_empty;

  _axi_out_write_req_fifo
  inst__axi_out_write_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._axi_out_write_req_fifo_enq(_axi_out_write_req_fifo_enq),
    ._axi_out_write_req_fifo_wdata(_axi_out_write_req_fifo_wdata),
    ._axi_out_write_req_fifo_full(_axi_out_write_req_fifo_full),
    ._axi_out_write_req_fifo_almost_full(_axi_out_write_req_fifo_almost_full),
    ._axi_out_write_req_fifo_deq(_axi_out_write_req_fifo_deq),
    ._axi_out_write_req_fifo_rdata(_axi_out_write_req_fifo_rdata),
    ._axi_out_write_req_fifo_empty(_axi_out_write_req_fifo_empty),
    ._axi_out_write_req_fifo_almost_empty(_axi_out_write_req_fifo_almost_empty)
  );

  reg [4-1:0] count__axi_out_write_req_fifo;
  wire [8-1:0] _axi_out_write_op_sel_fifo;
  wire [33-1:0] _axi_out_write_size_fifo;
  wire [8-1:0] unpack_write_req_op_sel_51;
  wire [33-1:0] unpack_write_req_local_size_52;
  assign unpack_write_req_op_sel_51 = _axi_out_write_req_fifo_rdata[40:33];
  assign unpack_write_req_local_size_52 = _axi_out_write_req_fifo_rdata[32:0];
  assign _axi_out_write_op_sel_fifo = unpack_write_req_op_sel_51;
  assign _axi_out_write_size_fifo = unpack_write_req_local_size_52;
  reg [8-1:0] _axi_out_write_op_sel_buf;
  reg [33-1:0] _axi_out_write_size_buf;
  reg _axi_out_write_data_busy;
  wire _axi_out_write_data_idle;
  wire _axi_out_write_idle;
  assign _axi_out_write_data_idle = _axi_out_write_req_fifo_empty && !_axi_out_write_data_busy;
  assign _axi_out_write_idle = _axi_out_write_data_idle;
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
  wire _mystream_reduce_stream_internal_oready;
  assign _mystream_reduce_stream_internal_oready = 1;
  reg [32-1:0] _mystream_reduce_fsm;
  localparam _mystream_reduce_fsm_init = 0;
  wire _mystream_reduce_run_flag;
  reg _mystream_reduce_source_start;
  wire _mystream_reduce_source_stop;
  reg _mystream_reduce_source_busy;
  wire _mystream_reduce_sink_start;
  wire _mystream_reduce_sink_stop;
  wire _mystream_reduce_sink_busy;
  wire _mystream_reduce_busy;
  reg _mystream_reduce_busy_reg;
  wire _mystream_reduce_is_root;
  assign _mystream_reduce_is_root = 1;
  reg _mystream_reduce_a_idle;
  reg [33-1:0] _mystream_reduce_a_source_count;
  reg [5-1:0] _mystream_reduce_a_source_mode;
  reg [16-1:0] _mystream_reduce_a_source_generator_id;
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
  reg [32-1:0] _mystream_reduce_reduce_size_next_parameter_data;
  reg [33-1:0] _mystream_reduce_sum_sink_count;
  reg [5-1:0] _mystream_reduce_sum_sink_mode;
  reg [16-1:0] _mystream_reduce_sum_sink_generator_id;
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
  reg [5-1:0] _mystream_reduce_sum_valid_sink_mode;
  reg [16-1:0] _mystream_reduce_sum_valid_sink_generator_id;
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
  wire _mystream_bias_stream_internal_oready;
  assign _mystream_bias_stream_internal_oready = 1;
  reg [32-1:0] _mystream_bias_fsm;
  localparam _mystream_bias_fsm_init = 0;
  wire _mystream_bias_run_flag;
  reg _mystream_bias_source_start;
  wire _mystream_bias_source_stop;
  reg _mystream_bias_source_busy;
  wire _mystream_bias_sink_start;
  wire _mystream_bias_sink_stop;
  wire _mystream_bias_sink_busy;
  wire _mystream_bias_busy;
  reg _mystream_bias_busy_reg;
  wire _mystream_bias_is_root;
  assign _mystream_bias_is_root = 1;
  reg _mystream_bias_x_idle;
  reg [33-1:0] _mystream_bias_x_source_count;
  reg [5-1:0] _mystream_bias_x_source_mode;
  reg [16-1:0] _mystream_bias_x_source_generator_id;
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
  reg [5-1:0] _mystream_bias_y_source_mode;
  reg [16-1:0] _mystream_bias_y_source_generator_id;
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
  reg [5-1:0] _mystream_bias_z_sink_mode;
  reg [16-1:0] _mystream_bias_z_sink_generator_id;
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
  wire [32-1:0] mask_addr_shifted_53;
  assign mask_addr_shifted_53 = _th_comp_bias_addr_3 >> 2;
  wire [32-1:0] mask_addr_masked_54;
  assign mask_addr_masked_54 = mask_addr_shifted_53 << 2;
  reg [32-1:0] _maxi_read_req_fsm;
  localparam _maxi_read_req_fsm_init = 0;
  reg [33-1:0] _maxi_read_cur_global_size;
  reg _maxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_55;
  wire [32-1:0] pack_read_req_local_addr_56;
  wire [32-1:0] pack_read_req_local_stride_57;
  wire [33-1:0] pack_read_req_local_size_58;
  wire [32-1:0] pack_read_req_local_blocksize_59;
  assign pack_read_req_op_sel_55 = _maxi_read_op_sel;
  assign pack_read_req_local_addr_56 = _maxi_read_local_addr;
  assign pack_read_req_local_stride_57 = _maxi_read_local_stride;
  assign pack_read_req_local_size_58 = _maxi_read_local_size;
  assign pack_read_req_local_blocksize_59 = _maxi_read_local_blocksize;
  wire [137-1:0] pack_read_req_packed_60;
  assign pack_read_req_packed_60 = { pack_read_req_op_sel_55, pack_read_req_local_addr_56, pack_read_req_local_stride_57, pack_read_req_local_size_58, pack_read_req_local_blocksize_59 };
  assign _maxi_read_req_fifo_wdata = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? pack_read_req_packed_60 : 'hx;
  assign _maxi_read_req_fifo_enq = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? (_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full && !_maxi_read_req_fifo_almost_full : 0;
  localparam _tmp_61 = 1;
  wire [_tmp_61-1:0] _tmp_62;
  assign _tmp_62 = !_maxi_read_req_fifo_almost_full;
  reg [_tmp_61-1:0] __tmp_62_1;
  wire [32-1:0] mask_addr_shifted_63;
  assign mask_addr_shifted_63 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_64;
  assign mask_addr_masked_64 = mask_addr_shifted_63 << 2;
  wire [32-1:0] mask_addr_shifted_65;
  assign mask_addr_shifted_65 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_66;
  assign mask_addr_masked_66 = mask_addr_shifted_65 << 2;
  wire [32-1:0] mask_addr_shifted_67;
  assign mask_addr_shifted_67 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_68;
  assign mask_addr_masked_68 = mask_addr_shifted_67 << 2;
  wire [32-1:0] mask_addr_shifted_69;
  assign mask_addr_shifted_69 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_70;
  assign mask_addr_masked_70 = mask_addr_shifted_69 << 2;
  wire [32-1:0] mask_addr_shifted_71;
  assign mask_addr_shifted_71 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_72;
  assign mask_addr_masked_72 = mask_addr_shifted_71 << 2;
  wire [32-1:0] mask_addr_shifted_73;
  assign mask_addr_shifted_73 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_74;
  assign mask_addr_masked_74 = mask_addr_shifted_73 << 2;
  reg _maxi_raddr_cond_0_1;
  reg [32-1:0] _maxi_read_data_fsm;
  localparam _maxi_read_data_fsm_init = 0;
  assign _maxi_read_req_fifo_deq = ((_maxi_read_data_fsm == 0) && (!_maxi_read_data_busy && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) && !_maxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_75;
  reg [10-1:0] write_burst_stride_76;
  reg [33-1:0] write_burst_length_77;
  reg write_burst_done_78;
  assign ram_b_0_wdata = ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? _maxi_rdata_sb_0 : 'hx;
  assign ram_b_0_wenable = ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? 1'd1 : 0;
  assign _maxi_rready_sb_0 = _maxi_read_data_fsm == 2;
  wire [8-1:0] pack_read_req_op_sel_79;
  wire [33-1:0] pack_read_req_local_size_80;
  assign pack_read_req_op_sel_79 = 1;
  assign pack_read_req_local_size_80 = _th_comp_read_size_0;
  wire [41-1:0] pack_read_req_packed_81;
  assign pack_read_req_packed_81 = { pack_read_req_op_sel_79, pack_read_req_local_size_80 };
  assign _axi_in_read_req_fifo_wdata = ((th_comp == 16) && !_axi_in_read_req_fifo_almost_full)? pack_read_req_packed_81 : 'hx;
  assign _axi_in_read_req_fifo_enq = ((th_comp == 16) && !_axi_in_read_req_fifo_almost_full)? (th_comp == 16) && !_axi_in_read_req_fifo_almost_full && !_axi_in_read_req_fifo_almost_full : 0;
  localparam _tmp_82 = 1;
  wire [_tmp_82-1:0] _tmp_83;
  assign _tmp_83 = !_axi_in_read_req_fifo_almost_full;
  reg [_tmp_82-1:0] __tmp_83_1;
  reg [32-1:0] _axi_in_read_data_fsm;
  localparam _axi_in_read_data_fsm_init = 0;
  assign _axi_in_read_req_fifo_deq = ((_axi_in_read_data_fsm == 0) && (!_axi_in_read_data_busy && !_axi_in_read_req_fifo_empty && (_axi_in_read_op_sel_fifo == 1)) && !_axi_in_read_req_fifo_empty)? 1 : 0;
  assign axi_in_tready = (_axi_in_read_data_fsm == 1) && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1);
  assign fifo_a_wdata = ((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1))? axi_in_tdata : 'hx;
  assign fifo_a_enq = ((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1))? (_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1) && !fifo_a_almost_full : 0;
  localparam _tmp_84 = 1;
  wire [_tmp_84-1:0] _tmp_85;
  assign _tmp_85 = !fifo_a_almost_full;
  reg [_tmp_84-1:0] __tmp_85_1;
  wire axistreamout_flag_86;
  assign axistreamout_flag_86 = th_comp == 17;
  wire [8-1:0] pack_write_req_op_sel_87;
  wire [33-1:0] pack_write_req_local_size_88;
  assign pack_write_req_op_sel_87 = 1;
  assign pack_write_req_local_size_88 = _th_comp_write_size_1;
  wire [41-1:0] pack_write_req_packed_89;
  assign pack_write_req_packed_89 = { pack_write_req_op_sel_87, pack_write_req_local_size_88 };
  assign _axi_out_write_req_fifo_wdata = (axistreamout_flag_86 && !_axi_out_write_req_fifo_almost_full)? pack_write_req_packed_89 : 'hx;
  assign _axi_out_write_req_fifo_enq = (axistreamout_flag_86 && !_axi_out_write_req_fifo_almost_full)? axistreamout_flag_86 && !_axi_out_write_req_fifo_almost_full && !_axi_out_write_req_fifo_almost_full : 0;
  localparam _tmp_90 = 1;
  wire [_tmp_90-1:0] _tmp_91;
  assign _tmp_91 = !_axi_out_write_req_fifo_almost_full;
  reg [_tmp_90-1:0] __tmp_91_1;
  reg [32-1:0] _axi_out_write_data_fsm;
  localparam _axi_out_write_data_fsm_init = 0;
  assign _axi_out_write_req_fifo_deq = ((_axi_out_write_data_fsm == 0) && (!_axi_out_write_data_busy && !_axi_out_write_req_fifo_empty && (_axi_out_write_op_sel_fifo == 1)) && !_axi_out_write_req_fifo_empty)? 1 : 0;
  reg rlast_92;
  wire cur_rvalid_93;
  assign fifo_c_deq = ((_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty)? 1 : 0;
  localparam _tmp_94 = 1;
  wire [_tmp_94-1:0] _tmp_95;
  assign _tmp_95 = (_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty;
  reg [_tmp_94-1:0] __tmp_95_1;
  reg repeat_rvalid_96;
  assign cur_rvalid_93 = __tmp_95_1 || repeat_rvalid_96;
  reg _axi_out_cond_0_1;
  wire signed [32-1:0] mystream_reduce_a_data;
  wire signed [32-1:0] mystream_reduce_reduce_size_data;
  wire [1-1:0] mystream_reduce__reduce_reset_data;
  reg __mystream_reduce_stream_ivalid_1;
  reg __mystream_reduce_stream_ivalid_2;
  reg __mystream_reduce_stream_ivalid_3;
  reg __mystream_reduce_stream_ivalid_4;
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
  reg [1-1:0] __delay_data_14__variable_3;
  reg signed [32-1:0] __delay_data_12__delay_11__variable_1;
  reg [1-1:0] __delay_data_15__delay_14__variable_3;
  reg signed [32-1:0] __delay_data_13__delay_12__delay_11__variable_1;
  reg [1-1:0] __delay_data_16__delay_15__delay_14__variable_3;
  reg signed [32-1:0] _reduceadd_data_4;
  reg [33-1:0] _reduceadd_count_4;
  reg _reduceadd_prev_count_max_4;
  wire _reduceadd_reset_cond_4;
  assign _reduceadd_reset_cond_4 = __delay_data_16__delay_15__delay_14__variable_3 || _reduceadd_prev_count_max_4;
  wire [33-1:0] _reduceadd_current_count_4;
  assign _reduceadd_current_count_4 = (_reduceadd_reset_cond_4)? 0 : _reduceadd_count_4;
  wire signed [32-1:0] _reduceadd_current_data_4;
  assign _reduceadd_current_data_4 = (_reduceadd_reset_cond_4)? 1'sd0 : _reduceadd_data_4;
  reg [1-1:0] _pulse_data_6;
  reg [33-1:0] _pulse_count_6;
  reg _pulse_prev_count_max_6;
  wire _pulse_reset_cond_6;
  assign _pulse_reset_cond_6 = __delay_data_16__delay_15__delay_14__variable_3 || _pulse_prev_count_max_6;
  wire [33-1:0] _pulse_current_count_6;
  assign _pulse_current_count_6 = (_pulse_reset_cond_6)? 0 : _pulse_count_6;
  wire [1-1:0] _pulse_current_data_6;
  assign _pulse_current_data_6 = (_pulse_reset_cond_6)? 1'sd0 : _pulse_data_6;
  wire signed [32-1:0] mystream_reduce_sum_data;
  assign mystream_reduce_sum_data = _reduceadd_data_4;
  wire [1-1:0] mystream_reduce_sum_valid_data;
  assign mystream_reduce_sum_valid_data = _pulse_data_6;
  wire _set_flag_97;
  assign _set_flag_97 = th_comp == 18;
  assign fifo_a_deq = (_mystream_reduce_stream_oready && _mystream_reduce_a_source_fifo_deq && (_mystream_reduce_a_source_sel == 1) && !fifo_a_empty)? 1 : 0;
  localparam _tmp_98 = 1;
  wire [_tmp_98-1:0] _tmp_99;
  assign _tmp_99 = _mystream_reduce_stream_oready && _mystream_reduce_a_source_fifo_deq && (_mystream_reduce_a_source_sel == 1) && !fifo_a_empty;
  reg [_tmp_98-1:0] __tmp_99_1;
  assign _mystream_reduce_a_source_fifo_rdata = (_mystream_reduce_a_source_sel == 1)? fifo_a_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_reduce_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_reduce_a_source_fsm_0;
  localparam _mystream_reduce_a_source_fsm_0_init = 0;
  wire _set_flag_100;
  assign _set_flag_100 = th_comp == 19;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_reduce_reduce_size_data = __variable_wdata_1;
  wire _set_flag_101;
  assign _set_flag_101 = th_comp == 20;
  reg _tmp_102;
  reg _tmp_103;
  reg _tmp_104;
  reg _tmp_105;
  reg _tmp_106;
  reg _tmp_107;
  reg signed [32-1:0] _tmp_108;
  reg signed [32-1:0] _tmp_109;
  reg signed [32-1:0] _tmp_110;
  reg signed [32-1:0] _tmp_111;
  reg signed [32-1:0] _tmp_112;
  reg signed [32-1:0] _tmp_113;
  assign fifo_b_wdata = (_mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2))? _mystream_reduce_sum_sink_fifo_wdata : 'hx;
  assign fifo_b_enq = (_mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2))? _mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2) && !fifo_b_almost_full : 0;
  localparam _tmp_114 = 1;
  wire [_tmp_114-1:0] _tmp_115;
  assign _tmp_115 = !fifo_b_almost_full;
  reg [_tmp_114-1:0] __tmp_115_1;
  assign _mystream_reduce_stream_oready = ((_mystream_reduce_sink_busy && (_mystream_reduce_sum_sink_sel == 2))? !fifo_b_almost_full : 1) && (((_mystream_reduce_source_busy && (_mystream_reduce_a_source_sel == 1))? !fifo_a_empty || _mystream_reduce_a_idle : 1) && _mystream_reduce_stream_internal_oready);
  reg [32-1:0] _mystream_reduce_sum_sink_fsm_1;
  localparam _mystream_reduce_sum_sink_fsm_1_init = 0;
  wire signed [32-1:0] mystream_bias_x_data;
  wire signed [32-1:0] mystream_bias_y_data;
  reg __mystream_bias_stream_ivalid_1;
  reg signed [32-1:0] _plus_data_10;
  wire signed [32-1:0] mystream_bias_z_data;
  assign mystream_bias_z_data = _plus_data_10;
  wire _set_flag_116;
  assign _set_flag_116 = th_comp == 21;
  assign fifo_b_deq = (_mystream_bias_stream_oready && _mystream_bias_x_source_fifo_deq && (_mystream_bias_x_source_sel == 1) && !fifo_b_empty)? 1 : 0;
  localparam _tmp_117 = 1;
  wire [_tmp_117-1:0] _tmp_118;
  assign _tmp_118 = _mystream_bias_stream_oready && _mystream_bias_x_source_fifo_deq && (_mystream_bias_x_source_sel == 1) && !fifo_b_empty;
  reg [_tmp_117-1:0] __tmp_118_1;
  assign _mystream_bias_x_source_fifo_rdata = (_mystream_bias_x_source_sel == 1)? fifo_b_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_8;
  assign mystream_bias_x_data = __variable_wdata_8;
  reg [32-1:0] _mystream_bias_x_source_fsm_0;
  localparam _mystream_bias_x_source_fsm_0_init = 0;
  wire _set_flag_119;
  assign _set_flag_119 = th_comp == 22;
  assign ram_b_0_addr = (_mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2))? _mystream_bias_y_source_ram_raddr : 
                        ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? write_burst_addr_75 : 'hx;
  assign ram_b_0_enable = (_mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2))? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? 1'd1 : 0;
  localparam _tmp_120 = 1;
  wire [_tmp_120-1:0] _tmp_121;
  assign _tmp_121 = _mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2);
  reg [_tmp_120-1:0] __tmp_121_1;
  assign _mystream_bias_y_source_ram_rdata = (_mystream_bias_y_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_9;
  assign mystream_bias_y_data = __variable_wdata_9;
  reg [32-1:0] _mystream_bias_y_source_fsm_1;
  localparam _mystream_bias_y_source_fsm_1_init = 0;
  wire _set_flag_122;
  assign _set_flag_122 = th_comp == 23;
  reg _tmp_123;
  reg _tmp_124;
  reg _tmp_125;
  reg signed [32-1:0] _tmp_126;
  reg signed [32-1:0] _tmp_127;
  reg signed [32-1:0] _tmp_128;
  assign fifo_c_wdata = (_mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3))? _mystream_bias_z_sink_fifo_wdata : 'hx;
  assign fifo_c_enq = (_mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3))? _mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3) && !fifo_c_almost_full : 0;
  localparam _tmp_129 = 1;
  wire [_tmp_129-1:0] _tmp_130;
  assign _tmp_130 = !fifo_c_almost_full;
  reg [_tmp_129-1:0] __tmp_130_1;
  assign _mystream_bias_stream_oready = ((_mystream_bias_sink_busy && (_mystream_bias_z_sink_sel == 3))? !fifo_c_almost_full : 1) && (((_mystream_bias_source_busy && (_mystream_bias_x_source_sel == 1))? !fifo_b_empty || _mystream_bias_x_idle : 1) && _mystream_bias_stream_internal_oready);
  reg [32-1:0] _mystream_bias_z_sink_fsm_2;
  localparam _mystream_bias_z_sink_fsm_2_init = 0;
  wire _set_flag_131;
  assign _set_flag_131 = th_comp == 24;
  assign _mystream_reduce_run_flag = (_set_flag_131)? 1 : 0;
  reg _tmp_132;
  reg _tmp_133;
  reg _tmp_134;
  reg _tmp_135;
  reg _tmp_136;
  reg _tmp_137;
  reg [1-1:0] __variable_wdata_3;
  assign mystream_reduce__reduce_reset_data = __variable_wdata_3;
  reg _tmp_138;
  reg _tmp_139;
  reg _tmp_140;
  reg _tmp_141;
  assign _mystream_reduce_source_stop = _mystream_reduce_stream_oready && (_mystream_reduce_a_idle && (_mystream_reduce_fsm == 3));
  localparam _tmp_142 = 1;
  wire [_tmp_142-1:0] _tmp_143;
  assign _tmp_143 = _mystream_reduce_a_idle && (_mystream_reduce_fsm == 3);
  reg [_tmp_142-1:0] _tmp_144;
  localparam _tmp_145 = 1;
  wire [_tmp_145-1:0] _tmp_146;
  assign _tmp_146 = _mystream_reduce_a_idle && (_mystream_reduce_fsm == 3);
  reg [_tmp_145-1:0] _tmp_147;
  reg _tmp_148;
  reg _tmp_149;
  reg _tmp_150;
  reg _tmp_151;
  reg _tmp_152;
  reg _tmp_153;
  assign _mystream_reduce_sink_start = _tmp_153;
  reg _tmp_154;
  reg _tmp_155;
  reg _tmp_156;
  reg _tmp_157;
  reg _tmp_158;
  reg _tmp_159;
  assign _mystream_reduce_sink_stop = _tmp_159;
  reg _tmp_160;
  reg _tmp_161;
  reg _tmp_162;
  reg _tmp_163;
  reg _tmp_164;
  reg _tmp_165;
  assign _mystream_reduce_sink_busy = _tmp_165;
  reg _tmp_166;
  assign _mystream_reduce_busy = _mystream_reduce_source_busy || _mystream_reduce_sink_busy || _mystream_reduce_busy_reg;
  wire _set_flag_167;
  assign _set_flag_167 = th_comp == 26;
  assign _mystream_bias_run_flag = (_set_flag_167)? 1 : 0;
  reg _tmp_168;
  reg _tmp_169;
  reg _tmp_170;
  assign _mystream_bias_source_stop = _mystream_bias_stream_oready && (_mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3));
  localparam _tmp_171 = 1;
  wire [_tmp_171-1:0] _tmp_172;
  assign _tmp_172 = _mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3);
  reg [_tmp_171-1:0] _tmp_173;
  reg _tmp_174;
  reg _tmp_175;
  reg _tmp_176;
  assign _mystream_bias_sink_start = _tmp_176;
  reg _tmp_177;
  reg _tmp_178;
  reg _tmp_179;
  assign _mystream_bias_sink_stop = _tmp_179;
  reg _tmp_180;
  reg _tmp_181;
  reg _tmp_182;
  assign _mystream_bias_sink_busy = _tmp_182;
  reg _tmp_183;
  assign _mystream_bias_busy = _mystream_bias_source_busy || _mystream_bias_sink_busy || _mystream_bias_busy_reg;

  always @(posedge CLK) begin
    if(RST) begin
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
    end else begin
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _maxi_wdata_sb_0 <= 0;
      _maxi_wstrb_sb_0 <= 0;
      _maxi_wlast_sb_0 <= 0;
      _maxi_wvalid_sb_0 <= 0;
    end else begin
      _maxi_wdata_sb_0 <= 0;
      _maxi_wstrb_sb_0 <= 0;
      _maxi_wlast_sb_0 <= 0;
      _maxi_wvalid_sb_0 <= 0;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb_maxi_writedata_data_6 <= 0;
      _sb_maxi_writedata_valid_7 <= 0;
      _sb_maxi_writedata_tmp_data_9 <= 0;
      _sb_maxi_writedata_tmp_valid_10 <= 0;
    end else begin
      if(_sb_maxi_writedata_m_ready_5 || !_sb_maxi_writedata_valid_7) begin
        _sb_maxi_writedata_data_6 <= _sb_maxi_writedata_next_data_11;
        _sb_maxi_writedata_valid_7 <= _sb_maxi_writedata_next_valid_12;
      end 
      if(!_sb_maxi_writedata_tmp_valid_10 && _sb_maxi_writedata_valid_7 && !_sb_maxi_writedata_m_ready_5) begin
        _sb_maxi_writedata_tmp_data_9 <= _sb_maxi_writedata_s_data_3;
        _sb_maxi_writedata_tmp_valid_10 <= _sb_maxi_writedata_s_valid_4;
      end 
      if(_sb_maxi_writedata_tmp_valid_10 && _sb_maxi_writedata_m_ready_5) begin
        _sb_maxi_writedata_tmp_valid_10 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      maxi_araddr <= 0;
      maxi_arlen <= 0;
      maxi_arvalid <= 0;
      _maxi_raddr_cond_0_1 <= 0;
    end else begin
      if(_maxi_raddr_cond_0_1) begin
        maxi_arvalid <= 0;
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid)) begin
        maxi_araddr <= _maxi_read_global_addr;
        maxi_arlen <= _maxi_read_cur_global_size - 1;
        maxi_arvalid <= 1;
      end 
      _maxi_raddr_cond_0_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb_maxi_readdata_data_21 <= 0;
      _sb_maxi_readdata_valid_22 <= 0;
      _sb_maxi_readdata_tmp_data_24 <= 0;
      _sb_maxi_readdata_tmp_valid_25 <= 0;
    end else begin
      if(_sb_maxi_readdata_m_ready_20 || !_sb_maxi_readdata_valid_22) begin
        _sb_maxi_readdata_data_21 <= _sb_maxi_readdata_next_data_26;
        _sb_maxi_readdata_valid_22 <= _sb_maxi_readdata_next_valid_27;
      end 
      if(!_sb_maxi_readdata_tmp_valid_25 && _sb_maxi_readdata_valid_22 && !_sb_maxi_readdata_m_ready_20) begin
        _sb_maxi_readdata_tmp_data_24 <= _sb_maxi_readdata_s_data_18;
        _sb_maxi_readdata_tmp_valid_25 <= _sb_maxi_readdata_s_valid_19;
      end 
      if(_sb_maxi_readdata_tmp_valid_25 && _sb_maxi_readdata_m_ready_20) begin
        _sb_maxi_readdata_tmp_valid_25 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _maxi_outstanding_wcount <= 0;
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      _maxi_read_op_sel <= 0;
      _maxi_read_global_addr <= 0;
      _maxi_read_global_size <= 0;
      _maxi_read_local_addr <= 0;
      _maxi_read_local_stride <= 0;
      _maxi_read_local_size <= 0;
      _maxi_read_local_blocksize <= 0;
      _maxi_read_req_busy <= 0;
      _maxi_read_cur_global_size <= 0;
      _maxi_read_data_busy <= 0;
      _maxi_read_op_sel_buf <= 0;
      _maxi_read_local_addr_buf <= 0;
      _maxi_read_local_stride_buf <= 0;
      _maxi_read_local_size_buf <= 0;
      _maxi_read_local_blocksize_buf <= 0;
    end else begin
      if(maxi_awvalid && maxi_awready && !(maxi_bvalid && maxi_bready) && (_maxi_outstanding_wcount < 7)) begin
        _maxi_outstanding_wcount <= _maxi_outstanding_wcount + 1;
      end 
      if(!(maxi_awvalid && maxi_awready) && (maxi_bvalid && maxi_bready) && (_maxi_outstanding_wcount > 0)) begin
        _maxi_outstanding_wcount <= _maxi_outstanding_wcount - 1;
      end 
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      if((th_comp == 14) && _maxi_read_req_idle) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= 1;
        _maxi_read_global_addr <= mask_addr_masked_54;
        _maxi_read_global_size <= _th_comp_write_size_1;
        _maxi_read_local_addr <= 0;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_comp_write_size_1;
        _maxi_read_local_blocksize <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && _maxi_read_start) begin
        _maxi_read_req_busy <= 1;
      end 
      if(_maxi_read_start && _maxi_read_req_fifo_almost_full) begin
        _maxi_read_start <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256) && ((mask_addr_masked_64 & 4095) + (_maxi_read_global_size << 2) >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_66 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_68 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256)) begin
        _maxi_read_cur_global_size <= _maxi_read_global_size;
        _maxi_read_global_size <= 0;
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && ((mask_addr_masked_70 & 4095) + 1024 >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_72 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_74 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full) begin
        _maxi_read_cur_global_size <= 256;
        _maxi_read_global_size <= _maxi_read_global_size - 256;
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid)) begin
        _maxi_read_global_addr <= _maxi_read_global_addr + (_maxi_read_cur_global_size << 2);
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid) && (_maxi_read_global_size == 0)) begin
        _maxi_read_req_busy <= 0;
      end 
      if((_maxi_read_data_fsm == 0) && (!_maxi_read_data_busy && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1))) begin
        _maxi_read_data_busy <= 1;
        _maxi_read_op_sel_buf <= _maxi_read_op_sel_fifo;
        _maxi_read_local_addr_buf <= _maxi_read_local_addr_fifo;
        _maxi_read_local_stride_buf <= _maxi_read_local_stride_fifo;
        _maxi_read_local_size_buf <= _maxi_read_local_size_fifo;
        _maxi_read_local_blocksize_buf <= _maxi_read_local_blocksize_fifo;
      end 
      if((_maxi_read_data_fsm == 2) && _maxi_rvalid_sb_0) begin
        _maxi_read_local_size_buf <= _maxi_read_local_size_buf - 1;
      end 
      if((_maxi_read_data_fsm == 2) && _maxi_rvalid_sb_0 && (_maxi_read_local_size_buf <= 1)) begin
        _maxi_read_data_busy <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_read_req_fifo <= 0;
      __tmp_62_1 <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full && (_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty)) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo;
      end else if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo + 1;
      end else if(_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo - 1;
      end 
      __tmp_62_1 <= _tmp_62;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_write_req_fifo <= 0;
    end else begin
      if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full && (_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty)) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo;
      end else if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo + 1;
      end else if(_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo - 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_rdata <= 0;
      saxi_rvalid <= 0;
      _saxi_rdata_cond_0_1 <= 0;
    end else begin
      if(_saxi_rdata_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_46;
        saxi_rvalid <= 1;
      end 
      _saxi_rdata_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_43 <= 0;
      prev_arvalid_44 <= 0;
      writevalid_41 <= 0;
      readvalid_42 <= 0;
      addr_40 <= 0;
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
      if(saxi_bvalid && saxi_bready) begin
        saxi_bvalid <= 0;
      end 
      if(saxi_wvalid && saxi_wready) begin
        saxi_bvalid <= 1;
      end 
      prev_awvalid_43 <= saxi_awvalid;
      prev_arvalid_44 <= saxi_arvalid;
      writevalid_41 <= 0;
      readvalid_42 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_40 <= saxi_awaddr;
        writevalid_41 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_40 <= saxi_araddr;
        readvalid_42 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 0)) begin
        _saxi_register_0 <= axislite_resetval_48;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 1)) begin
        _saxi_register_1 <= axislite_resetval_48;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 2)) begin
        _saxi_register_2 <= axislite_resetval_48;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 3)) begin
        _saxi_register_3 <= axislite_resetval_48;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 4)) begin
        _saxi_register_4 <= axislite_resetval_48;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 5)) begin
        _saxi_register_5 <= axislite_resetval_48;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 6)) begin
        _saxi_register_6 <= axislite_resetval_48;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_47 && (axis_maskaddr_45 == 7)) begin
        _saxi_register_7 <= axislite_resetval_48;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_45 == 7)) begin
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
      if((th_comp == 30) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 30) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 30) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 30) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_comp == 30) && 0) begin
        _saxi_register_4 <= 0;
        _saxi_flag_4 <= 0;
      end 
      if((th_comp == 30) && 0) begin
        _saxi_register_5 <= 0;
        _saxi_flag_5 <= 0;
      end 
      if((th_comp == 30) && 0) begin
        _saxi_register_6 <= 0;
        _saxi_flag_6 <= 0;
      end 
      if((th_comp == 30) && 0) begin
        _saxi_register_7 <= 0;
        _saxi_flag_7 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;
  localparam _saxi_register_fsm_3 = 3;
  localparam _saxi_register_fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
      axis_maskaddr_45 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_42 || writevalid_41) begin
            axis_maskaddr_45 <= (addr_40 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_42) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_41) begin
            _saxi_register_fsm <= _saxi_register_fsm_3;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_2: begin
          if(saxi_rready && saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_3: begin
          if(saxi_wvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_4;
          end 
        end
        _saxi_register_fsm_4: begin
          if(saxi_bready && saxi_bvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_in_read_data_busy <= 0;
      _axi_in_read_op_sel_buf <= 0;
      _axi_in_read_local_size_buf <= 0;
    end else begin
      if((_axi_in_read_data_fsm == 0) && (!_axi_in_read_data_busy && !_axi_in_read_req_fifo_empty && (_axi_in_read_op_sel_fifo == 1))) begin
        _axi_in_read_data_busy <= 1;
        _axi_in_read_op_sel_buf <= _axi_in_read_op_sel_fifo;
        _axi_in_read_local_size_buf <= _axi_in_read_local_size_fifo;
      end 
      if((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full) begin
        _axi_in_read_local_size_buf <= _axi_in_read_local_size_buf - 1;
      end 
      if((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_local_size_buf <= 1)) begin
        _axi_in_read_data_busy <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_in_read_req_fifo <= 0;
      __tmp_83_1 <= 0;
    end else begin
      if(_axi_in_read_req_fifo_enq && !_axi_in_read_req_fifo_full && (_axi_in_read_req_fifo_deq && !_axi_in_read_req_fifo_empty)) begin
        count__axi_in_read_req_fifo <= count__axi_in_read_req_fifo;
      end else if(_axi_in_read_req_fifo_enq && !_axi_in_read_req_fifo_full) begin
        count__axi_in_read_req_fifo <= count__axi_in_read_req_fifo + 1;
      end else if(_axi_in_read_req_fifo_deq && !_axi_in_read_req_fifo_empty) begin
        count__axi_in_read_req_fifo <= count__axi_in_read_req_fifo - 1;
      end 
      __tmp_83_1 <= _tmp_83;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      axi_out_tdata <= 0;
      axi_out_tvalid <= 0;
      axi_out_tlast <= 0;
      _axi_out_cond_0_1 <= 0;
    end else begin
      if(_axi_out_cond_0_1) begin
        axi_out_tvalid <= 0;
        axi_out_tlast <= 0;
      end 
      if((_axi_out_write_op_sel_buf == 1) && cur_rvalid_93 && (axi_out_tready || !axi_out_tvalid) && (axi_out_tready || !axi_out_tvalid)) begin
        axi_out_tdata <= fifo_c_rdata;
        axi_out_tvalid <= 1;
        axi_out_tlast <= rlast_92;
      end 
      _axi_out_cond_0_1 <= 1;
      if(axi_out_tvalid && !axi_out_tready) begin
        axi_out_tvalid <= axi_out_tvalid;
        axi_out_tlast <= axi_out_tlast;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_out_write_data_busy <= 0;
      _axi_out_write_op_sel_buf <= 0;
      _axi_out_write_size_buf <= 0;
      repeat_rvalid_96 <= 0;
    end else begin
      if((_axi_out_write_data_fsm == 0) && (!_axi_out_write_data_busy && !_axi_out_write_req_fifo_empty && (_axi_out_write_op_sel_fifo == 1))) begin
        _axi_out_write_data_busy <= 1;
        _axi_out_write_op_sel_buf <= _axi_out_write_op_sel_fifo;
        _axi_out_write_size_buf <= _axi_out_write_size_fifo;
      end 
      repeat_rvalid_96 <= 0;
      if(__tmp_95_1 && !(axi_out_tready || !axi_out_tvalid)) begin
        repeat_rvalid_96 <= 1;
      end 
      if(repeat_rvalid_96 && !(axi_out_tready || !axi_out_tvalid)) begin
        repeat_rvalid_96 <= 1;
      end 
      if((_axi_out_write_data_fsm == 1) && ((_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid))) begin
        _axi_out_write_size_buf <= _axi_out_write_size_buf - 1;
      end 
      if((_axi_out_write_data_fsm == 1) && ((_axi_out_write_op_sel_buf == 1) && cur_rvalid_93 && (axi_out_tready || !axi_out_tvalid)) && rlast_92) begin
        _axi_out_write_data_busy <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_out_write_req_fifo <= 0;
      __tmp_91_1 <= 0;
    end else begin
      if(_axi_out_write_req_fifo_enq && !_axi_out_write_req_fifo_full && (_axi_out_write_req_fifo_deq && !_axi_out_write_req_fifo_empty)) begin
        count__axi_out_write_req_fifo <= count__axi_out_write_req_fifo;
      end else if(_axi_out_write_req_fifo_enq && !_axi_out_write_req_fifo_full) begin
        count__axi_out_write_req_fifo <= count__axi_out_write_req_fifo + 1;
      end else if(_axi_out_write_req_fifo_deq && !_axi_out_write_req_fifo_empty) begin
        count__axi_out_write_req_fifo <= count__axi_out_write_req_fifo - 1;
      end 
      __tmp_91_1 <= _tmp_91;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_a <= 0;
      __tmp_85_1 <= 0;
      __tmp_99_1 <= 0;
    end else begin
      if(fifo_a_enq && !fifo_a_full && (fifo_a_deq && !fifo_a_empty)) begin
        count_fifo_a <= count_fifo_a;
      end else if(fifo_a_enq && !fifo_a_full) begin
        count_fifo_a <= count_fifo_a + 1;
      end else if(fifo_a_deq && !fifo_a_empty) begin
        count_fifo_a <= count_fifo_a - 1;
      end 
      __tmp_85_1 <= _tmp_85;
      __tmp_99_1 <= _tmp_99;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_b <= 0;
      __tmp_115_1 <= 0;
      __tmp_118_1 <= 0;
    end else begin
      if(fifo_b_enq && !fifo_b_full && (fifo_b_deq && !fifo_b_empty)) begin
        count_fifo_b <= count_fifo_b;
      end else if(fifo_b_enq && !fifo_b_full) begin
        count_fifo_b <= count_fifo_b + 1;
      end else if(fifo_b_deq && !fifo_b_empty) begin
        count_fifo_b <= count_fifo_b - 1;
      end 
      __tmp_115_1 <= _tmp_115;
      __tmp_118_1 <= _tmp_118;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_c <= 0;
      __tmp_95_1 <= 0;
      __tmp_130_1 <= 0;
    end else begin
      if(fifo_c_enq && !fifo_c_full && (fifo_c_deq && !fifo_c_empty)) begin
        count_fifo_c <= count_fifo_c;
      end else if(fifo_c_enq && !fifo_c_full) begin
        count_fifo_c <= count_fifo_c + 1;
      end else if(fifo_c_deq && !fifo_c_empty) begin
        count_fifo_c <= count_fifo_c - 1;
      end 
      __tmp_95_1 <= _tmp_95;
      __tmp_130_1 <= _tmp_130;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_121_1 <= 0;
    end else begin
      __tmp_121_1 <= _tmp_121;
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
      _times_mul_odata_reg_2 <= 0;
      __delay_data_11__variable_1 <= 0;
      __delay_data_14__variable_3 <= 0;
      __delay_data_12__delay_11__variable_1 <= 0;
      __delay_data_15__delay_14__variable_3 <= 0;
      __delay_data_13__delay_12__delay_11__variable_1 <= 0;
      __delay_data_16__delay_15__delay_14__variable_3 <= 0;
      _reduceadd_data_4 <= 1'sd0;
      _reduceadd_count_4 <= 0;
      _reduceadd_prev_count_max_4 <= 0;
      _pulse_data_6 <= 1'sd0;
      _pulse_count_6 <= 0;
      _pulse_prev_count_max_6 <= 0;
      _mystream_reduce_a_source_mode <= 5'b0;
      _mystream_reduce_a_source_size <= 0;
      _mystream_reduce_a_source_sel <= 0;
      _mystream_reduce_a_source_size_buf <= 0;
      __variable_wdata_0 <= 0;
      _mystream_reduce_a_source_count <= 0;
      _mystream_reduce_reduce_size_next_parameter_data <= 0;
      __variable_wdata_1 <= 0;
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
      _mystream_reduce_sum_sink_mode <= 5'b0;
      _mystream_reduce_sum_sink_size <= 0;
      _mystream_reduce_sum_sink_sel <= 0;
      _mystream_reduce_sum_sink_size_buf <= 0;
      _mystream_reduce_sum_sink_count <= 0;
      _mystream_reduce_sum_sink_fifo_wdata <= 0;
      _tmp_132 <= 0;
      _tmp_133 <= 0;
      _tmp_134 <= 0;
      _tmp_135 <= 0;
      _tmp_136 <= 0;
      _tmp_137 <= 0;
      __variable_wdata_3 <= 0;
      _tmp_138 <= 0;
      _tmp_139 <= 0;
      _tmp_140 <= 0;
      _tmp_141 <= 0;
      _tmp_144 <= 0;
      _tmp_147 <= 0;
      _tmp_148 <= 0;
      _tmp_149 <= 0;
      _tmp_150 <= 0;
      _tmp_151 <= 0;
      _tmp_152 <= 0;
      _tmp_153 <= 0;
      _tmp_154 <= 0;
      _tmp_155 <= 0;
      _tmp_156 <= 0;
      _tmp_157 <= 0;
      _tmp_158 <= 0;
      _tmp_159 <= 0;
      _tmp_160 <= 0;
      _tmp_161 <= 0;
      _tmp_162 <= 0;
      _tmp_163 <= 0;
      _tmp_164 <= 0;
      _tmp_165 <= 0;
      _tmp_166 <= 0;
      _mystream_reduce_busy_reg <= 0;
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
        _times_mul_odata_reg_2 <= _times_mul_odata_2;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_11__variable_1 <= mystream_reduce_reduce_size_data;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_14__variable_3 <= mystream_reduce__reduce_reset_data;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_12__delay_11__variable_1 <= __delay_data_11__variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_15__delay_14__variable_3 <= __delay_data_14__variable_3;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_13__delay_12__delay_11__variable_1 <= __delay_data_12__delay_11__variable_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        __delay_data_16__delay_15__delay_14__variable_3 <= __delay_data_15__delay_14__variable_3;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready && _reduceadd_reset_cond_4) begin
        _reduceadd_data_4 <= 1'sd0;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready) begin
        _reduceadd_count_4 <= (_reduceadd_current_count_4 >= __delay_data_13__delay_12__delay_11__variable_1 - 1)? 0 : _reduceadd_current_count_4 + 1;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready) begin
        _reduceadd_prev_count_max_4 <= _reduceadd_current_count_4 >= __delay_data_13__delay_12__delay_11__variable_1 - 1;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready) begin
        _reduceadd_data_4 <= _reduceadd_current_data_4 + _times_data_2;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready && _pulse_reset_cond_6) begin
        _pulse_data_6 <= 1'sd0;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready) begin
        _pulse_count_6 <= (_pulse_current_count_6 >= __delay_data_13__delay_12__delay_11__variable_1 - 1)? 0 : _pulse_current_count_6 + 1;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready) begin
        _pulse_prev_count_max_6 <= _pulse_current_count_6 >= __delay_data_13__delay_12__delay_11__variable_1 - 1;
      end 
      if(__mystream_reduce_stream_ivalid_3 && _mystream_reduce_stream_oready) begin
        _pulse_data_6 <= _pulse_current_count_6 >= __delay_data_13__delay_12__delay_11__variable_1 - 1;
      end 
      if(_set_flag_97) begin
        _mystream_reduce_a_source_mode <= 5'b10000;
        _mystream_reduce_a_source_size <= _th_comp_read_size_0;
      end 
      if(_set_flag_97) begin
        _mystream_reduce_a_source_sel <= 1;
      end 
      if(_mystream_reduce_source_start && _mystream_reduce_a_source_mode & 5'b10000 && _mystream_reduce_stream_oready) begin
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
      if((_mystream_reduce_a_source_fsm_0 == 2) && _mystream_reduce_source_stop && _mystream_reduce_stream_oready) begin
        _mystream_reduce_a_source_fifo_deq <= 0;
        _mystream_reduce_a_idle <= 1;
      end 
      if(_set_flag_100) begin
        _mystream_reduce_reduce_size_next_parameter_data <= _th_comp_reduce_size_2;
      end 
      if(_mystream_reduce_source_start) begin
        __variable_wdata_1 <= _mystream_reduce_reduce_size_next_parameter_data;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_102 <= _set_flag_101;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_103 <= _tmp_102;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_104 <= _tmp_103;
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
        _tmp_108 <= _th_comp_write_size_1;
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
      if(_tmp_107) begin
        _mystream_reduce_sum_sink_mode <= 5'b10000;
        _mystream_reduce_sum_sink_size <= _tmp_113;
      end 
      if(_tmp_107) begin
        _mystream_reduce_sum_sink_sel <= 2;
      end 
      if(_mystream_reduce_sink_start && _mystream_reduce_sum_sink_mode & 5'b10000 && _mystream_reduce_stream_oready) begin
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
        _tmp_132 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_133 <= _tmp_132;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_134 <= _tmp_133;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_135 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_136 <= _tmp_135;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_137 <= _tmp_136;
      end 
      if(_mystream_reduce_stream_oready && _tmp_137) begin
        __variable_wdata_3 <= 1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_138 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_139 <= _tmp_138;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_140 <= _tmp_139;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_141 <= _tmp_140;
      end 
      if(_mystream_reduce_stream_oready && _tmp_141) begin
        __variable_wdata_3 <= 0;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_144 <= _tmp_143;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_147 <= _tmp_146;
      end 
      if(_mystream_reduce_stream_oready && _tmp_147) begin
        __variable_wdata_3 <= 1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_148 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_149 <= _tmp_148;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_150 <= _tmp_149;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_151 <= _tmp_150;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_152 <= _tmp_151;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_153 <= _tmp_152;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_154 <= _mystream_reduce_source_stop;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_155 <= _tmp_154;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_156 <= _tmp_155;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_157 <= _tmp_156;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_158 <= _tmp_157;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_159 <= _tmp_158;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_160 <= _mystream_reduce_source_busy;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_161 <= _tmp_160;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_162 <= _tmp_161;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_163 <= _tmp_162;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_164 <= _tmp_163;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_165 <= _tmp_164;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_166 <= _mystream_reduce_sink_busy;
      end 
      if(!_mystream_reduce_sink_busy && _tmp_166) begin
        _mystream_reduce_busy_reg <= 0;
      end 
      if(_mystream_reduce_source_busy) begin
        _mystream_reduce_busy_reg <= 1;
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
      _mystream_reduce_stream_ivalid <= 0;
    end else begin
      if(_mystream_reduce_stream_oready && _tmp_134) begin
        _mystream_reduce_stream_ivalid <= 1;
      end 
      if(_mystream_reduce_stream_oready && _tmp_144) begin
        _mystream_reduce_stream_ivalid <= 0;
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
      _mystream_bias_x_source_mode <= 5'b0;
      _mystream_bias_x_source_size <= 0;
      _mystream_bias_x_source_sel <= 0;
      _mystream_bias_x_source_size_buf <= 0;
      __variable_wdata_8 <= 0;
      _mystream_bias_x_source_count <= 0;
      _mystream_bias_y_source_mode <= 5'b0;
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
      _tmp_123 <= 0;
      _tmp_124 <= 0;
      _tmp_125 <= 0;
      _tmp_126 <= 0;
      _tmp_127 <= 0;
      _tmp_128 <= 0;
      _mystream_bias_z_sink_mode <= 5'b0;
      _mystream_bias_z_sink_size <= 0;
      _mystream_bias_z_sink_sel <= 0;
      _mystream_bias_z_sink_size_buf <= 0;
      _mystream_bias_z_sink_count <= 0;
      _mystream_bias_z_sink_fifo_wdata <= 0;
      _tmp_168 <= 0;
      _tmp_169 <= 0;
      _tmp_170 <= 0;
      _tmp_173 <= 0;
      _tmp_174 <= 0;
      _tmp_175 <= 0;
      _tmp_176 <= 0;
      _tmp_177 <= 0;
      _tmp_178 <= 0;
      _tmp_179 <= 0;
      _tmp_180 <= 0;
      _tmp_181 <= 0;
      _tmp_182 <= 0;
      _tmp_183 <= 0;
      _mystream_bias_busy_reg <= 0;
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
      if(_set_flag_116) begin
        _mystream_bias_x_source_mode <= 5'b10000;
        _mystream_bias_x_source_size <= _th_comp_write_size_1;
      end 
      if(_set_flag_116) begin
        _mystream_bias_x_source_sel <= 1;
      end 
      if(_mystream_bias_source_start && _mystream_bias_x_source_mode & 5'b10000 && _mystream_bias_stream_oready) begin
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
      if((_mystream_bias_x_source_fsm_0 == 2) && _mystream_bias_source_stop && _mystream_bias_stream_oready) begin
        _mystream_bias_x_source_fifo_deq <= 0;
        _mystream_bias_x_idle <= 1;
      end 
      if(_set_flag_119) begin
        _mystream_bias_y_source_mode <= 5'b1;
        _mystream_bias_y_source_offset <= 0;
        _mystream_bias_y_source_size <= _th_comp_write_size_1;
        _mystream_bias_y_source_stride <= 1;
      end 
      if(_set_flag_119) begin
        _mystream_bias_y_source_sel <= 2;
      end 
      if(_mystream_bias_source_start && _mystream_bias_y_source_mode & 5'b1 && _mystream_bias_stream_oready) begin
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
      if((_mystream_bias_y_source_fsm_1 == 2) && _mystream_bias_source_stop && _mystream_bias_stream_oready) begin
        _mystream_bias_y_source_ram_renable <= 0;
        _mystream_bias_y_idle <= 1;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_123 <= _set_flag_122;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_124 <= _tmp_123;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_125 <= _tmp_124;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_126 <= _th_comp_write_size_1;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_127 <= _tmp_126;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_128 <= _tmp_127;
      end 
      if(_tmp_125) begin
        _mystream_bias_z_sink_mode <= 5'b10000;
        _mystream_bias_z_sink_size <= _tmp_128;
      end 
      if(_tmp_125) begin
        _mystream_bias_z_sink_sel <= 3;
      end 
      if(_mystream_bias_sink_start && _mystream_bias_z_sink_mode & 5'b10000 && _mystream_bias_stream_oready) begin
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
        _tmp_168 <= _mystream_bias_source_start;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_169 <= _tmp_168;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_170 <= _tmp_169;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_173 <= _tmp_172;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_174 <= _mystream_bias_source_start;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_175 <= _tmp_174;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_176 <= _tmp_175;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_177 <= _mystream_bias_source_stop;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_178 <= _tmp_177;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_179 <= _tmp_178;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_180 <= _mystream_bias_source_busy;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_181 <= _tmp_180;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_182 <= _tmp_181;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_183 <= _mystream_bias_sink_busy;
      end 
      if(!_mystream_bias_sink_busy && _tmp_183) begin
        _mystream_bias_busy_reg <= 0;
      end 
      if(_mystream_bias_source_busy) begin
        _mystream_bias_busy_reg <= 1;
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
      _mystream_bias_stream_ivalid <= 0;
    end else begin
      if(_mystream_bias_stream_oready && _tmp_170) begin
        _mystream_bias_stream_ivalid <= 1;
      end 
      if(_mystream_bias_stream_oready && _tmp_173) begin
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_read_size_0 <= 0;
      _th_comp_write_size_1 <= 0;
      _th_comp_reduce_size_2 <= 0;
      _th_comp_bias_addr_3 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          if(1) begin
            th_comp <= th_comp_2;
          end else begin
            th_comp <= th_comp_32;
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
          if(_maxi_read_req_idle) begin
            th_comp <= th_comp_15;
          end 
        end
        th_comp_15: begin
          if(_maxi_read_idle) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          if(!_axi_in_read_req_fifo_almost_full) begin
            th_comp <= th_comp_17;
          end 
        end
        th_comp_17: begin
          if(!_axi_out_write_req_fifo_almost_full) begin
            th_comp <= th_comp_18;
          end 
        end
        th_comp_18: begin
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          if(_mystream_reduce_stream_oready) begin
            th_comp <= th_comp_21;
          end 
        end
        th_comp_21: begin
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          if(_mystream_bias_stream_oready) begin
            th_comp <= th_comp_24;
          end 
        end
        th_comp_24: begin
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          if(_mystream_reduce_busy) begin
            th_comp <= th_comp_26;
          end 
        end
        th_comp_26: begin
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          if(_mystream_bias_busy) begin
            th_comp <= th_comp_28;
          end 
        end
        th_comp_28: begin
          if(!_mystream_reduce_busy) begin
            th_comp <= th_comp_29;
          end 
        end
        th_comp_29: begin
          if(!_mystream_bias_busy) begin
            th_comp <= th_comp_30;
          end 
        end
        th_comp_30: begin
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          th_comp <= th_comp_1;
        end
      endcase
    end
  end

  localparam _maxi_read_req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_req_fsm <= _maxi_read_req_fsm_init;
      _maxi_read_cont <= 0;
    end else begin
      case(_maxi_read_req_fsm)
        _maxi_read_req_fsm_init: begin
          if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full) begin
            _maxi_read_req_fsm <= _maxi_read_req_fsm_1;
          end 
        end
        _maxi_read_req_fsm_1: begin
          if(maxi_arready || !maxi_arvalid) begin
            _maxi_read_cont <= 1;
          end 
          if((maxi_arready || !maxi_arvalid) && (_maxi_read_global_size == 0)) begin
            _maxi_read_cont <= 0;
          end 
          if(maxi_arready || !maxi_arvalid) begin
            _maxi_read_req_fsm <= _maxi_read_req_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _maxi_read_data_fsm_1 = 1;
  localparam _maxi_read_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_data_fsm <= _maxi_read_data_fsm_init;
    end else begin
      case(_maxi_read_data_fsm)
        _maxi_read_data_fsm_init: begin
          if(!_maxi_read_data_busy && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_1;
          end 
        end
        _maxi_read_data_fsm_1: begin
          _maxi_read_data_fsm <= _maxi_read_data_fsm_2;
        end
        _maxi_read_data_fsm_2: begin
          if(_maxi_rvalid_sb_0 && (_maxi_read_local_size_buf <= 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_0_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_0 <= write_burst_fsm_0_init;
      write_burst_addr_75 <= 0;
      write_burst_stride_76 <= 0;
      write_burst_length_77 <= 0;
      write_burst_done_78 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_75 <= _maxi_read_local_addr_buf;
          write_burst_stride_76 <= _maxi_read_local_stride_buf;
          write_burst_length_77 <= _maxi_read_local_size_buf;
          write_burst_done_78 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 1) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(_maxi_rvalid_sb_0) begin
            write_burst_addr_75 <= write_burst_addr_75 + write_burst_stride_76;
            write_burst_length_77 <= write_burst_length_77 - 1;
            write_burst_done_78 <= 0;
          end 
          if(_maxi_rvalid_sb_0 && (write_burst_length_77 <= 1)) begin
            write_burst_done_78 <= 1;
          end 
          if(_maxi_rvalid_sb_0 && 0) begin
            write_burst_done_78 <= 1;
          end 
          if(_maxi_rvalid_sb_0 && (write_burst_length_77 <= 1)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(_maxi_rvalid_sb_0 && 0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _axi_in_read_data_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_in_read_data_fsm <= _axi_in_read_data_fsm_init;
    end else begin
      case(_axi_in_read_data_fsm)
        _axi_in_read_data_fsm_init: begin
          if(!_axi_in_read_data_busy && !_axi_in_read_req_fifo_empty && (_axi_in_read_op_sel_fifo == 1)) begin
            _axi_in_read_data_fsm <= _axi_in_read_data_fsm_1;
          end 
        end
        _axi_in_read_data_fsm_1: begin
          if(axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_local_size_buf <= 1)) begin
            _axi_in_read_data_fsm <= _axi_in_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _axi_out_write_data_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_out_write_data_fsm <= _axi_out_write_data_fsm_init;
      rlast_92 <= 0;
    end else begin
      case(_axi_out_write_data_fsm)
        _axi_out_write_data_fsm_init: begin
          rlast_92 <= 0;
          if(!_axi_out_write_data_busy && !_axi_out_write_req_fifo_empty && (_axi_out_write_op_sel_fifo == 1)) begin
            _axi_out_write_data_fsm <= _axi_out_write_data_fsm_1;
          end 
        end
        _axi_out_write_data_fsm_1: begin
          if((_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid)) begin
            rlast_92 <= _axi_out_write_size_buf <= 1;
          end 
          if((_axi_out_write_op_sel_buf == 1) && cur_rvalid_93 && (axi_out_tready || !axi_out_tvalid) && rlast_92) begin
            _axi_out_write_data_fsm <= _axi_out_write_data_fsm_init;
          end 
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
          if(_mystream_reduce_source_start && _mystream_reduce_a_source_mode & 5'b10000 && _mystream_reduce_stream_oready) begin
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
          if(_mystream_reduce_source_stop && _mystream_reduce_stream_oready) begin
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
          if(_mystream_reduce_sink_start && _mystream_reduce_sum_sink_mode & 5'b10000 && _mystream_reduce_stream_oready) begin
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
          if(_mystream_bias_source_start && _mystream_bias_x_source_mode & 5'b10000 && _mystream_bias_stream_oready) begin
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
          if(_mystream_bias_source_stop && _mystream_bias_stream_oready) begin
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
          if(_mystream_bias_source_start && _mystream_bias_y_source_mode & 5'b1 && _mystream_bias_stream_oready) begin
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
          if(_mystream_bias_source_stop && _mystream_bias_stream_oready) begin
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
          if(_mystream_bias_sink_start && _mystream_bias_z_sink_mode & 5'b10000 && _mystream_bias_stream_oready) begin
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



module _maxi_read_req_fifo
(
  input CLK,
  input RST,
  input _maxi_read_req_fifo_enq,
  input [137-1:0] _maxi_read_req_fifo_wdata,
  output _maxi_read_req_fifo_full,
  output _maxi_read_req_fifo_almost_full,
  input _maxi_read_req_fifo_deq,
  output [137-1:0] _maxi_read_req_fifo_rdata,
  output _maxi_read_req_fifo_empty,
  output _maxi_read_req_fifo_almost_empty
);

  reg [137-1:0] mem [0:8-1];
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
  wire [137-1:0] rdata;
  assign _maxi_read_req_fifo_full = is_full;
  assign _maxi_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _maxi_read_req_fifo_empty = is_empty;
  assign _maxi_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _maxi_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !is_full) begin
        mem[head] <= _maxi_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_maxi_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _maxi_write_req_fifo
(
  input CLK,
  input RST,
  input _maxi_write_req_fifo_enq,
  input [137-1:0] _maxi_write_req_fifo_wdata,
  output _maxi_write_req_fifo_full,
  output _maxi_write_req_fifo_almost_full,
  input _maxi_write_req_fifo_deq,
  output [137-1:0] _maxi_write_req_fifo_rdata,
  output _maxi_write_req_fifo_empty,
  output _maxi_write_req_fifo_almost_empty
);

  reg [137-1:0] mem [0:8-1];
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
  wire [137-1:0] rdata;
  assign _maxi_write_req_fifo_full = is_full;
  assign _maxi_write_req_fifo_almost_full = is_almost_full || is_full;
  assign _maxi_write_req_fifo_empty = is_empty;
  assign _maxi_write_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _maxi_write_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_maxi_write_req_fifo_enq && !is_full) begin
        mem[head] <= _maxi_write_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_maxi_write_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _axi_in_read_req_fifo
(
  input CLK,
  input RST,
  input _axi_in_read_req_fifo_enq,
  input [41-1:0] _axi_in_read_req_fifo_wdata,
  output _axi_in_read_req_fifo_full,
  output _axi_in_read_req_fifo_almost_full,
  input _axi_in_read_req_fifo_deq,
  output [41-1:0] _axi_in_read_req_fifo_rdata,
  output _axi_in_read_req_fifo_empty,
  output _axi_in_read_req_fifo_almost_empty
);

  reg [41-1:0] mem [0:8-1];
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
  wire [41-1:0] rdata;
  assign _axi_in_read_req_fifo_full = is_full;
  assign _axi_in_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_in_read_req_fifo_empty = is_empty;
  assign _axi_in_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_in_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_in_read_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_in_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_in_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _axi_out_write_req_fifo
(
  input CLK,
  input RST,
  input _axi_out_write_req_fifo_enq,
  input [41-1:0] _axi_out_write_req_fifo_wdata,
  output _axi_out_write_req_fifo_full,
  output _axi_out_write_req_fifo_almost_full,
  input _axi_out_write_req_fifo_deq,
  output [41-1:0] _axi_out_write_req_fifo_rdata,
  output _axi_out_write_req_fifo_empty,
  output _axi_out_write_req_fifo_almost_empty
);

  reg [41-1:0] mem [0:8-1];
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
  wire [41-1:0] rdata;
  assign _axi_out_write_req_fifo_full = is_full;
  assign _axi_out_write_req_fifo_almost_full = is_almost_full || is_full;
  assign _axi_out_write_req_fifo_empty = is_empty;
  assign _axi_out_write_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _axi_out_write_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_axi_out_write_req_fifo_enq && !is_full) begin
        mem[head] <= _axi_out_write_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_axi_out_write_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
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
  assign _mul = _a * _b;
  assign c = _pipe_mul0;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
    end 
  end


endmodule
"""


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    code = stream_axi_stream_fifo_ipxact.run(filename=None, simtype=simtype,
                                             outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
