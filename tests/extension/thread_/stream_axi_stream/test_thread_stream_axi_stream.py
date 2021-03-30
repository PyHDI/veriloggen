from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_stream_axi_stream


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

  reg _axi_a_read_start;
  reg [8-1:0] _axi_a_read_op_sel;
  reg [32-1:0] _axi_a_read_local_addr;
  reg [33-1:0] _axi_a_read_size;
  reg [32-1:0] _axi_a_read_local_stride;
  reg _axi_a_read_idle;
  reg _axi_b_read_start;
  reg [8-1:0] _axi_b_read_op_sel;
  reg [32-1:0] _axi_b_read_local_addr;
  reg [33-1:0] _axi_b_read_size;
  reg [32-1:0] _axi_b_read_local_stride;
  reg _axi_b_read_idle;
  reg _axi_c_write_start;
  reg [8-1:0] _axi_c_write_op_sel;
  reg [32-1:0] _axi_c_write_local_addr;
  reg [33-1:0] _axi_c_write_size;
  reg [32-1:0] _axi_c_write_local_stride;
  reg _axi_c_write_idle;
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
  reg [32-1:0] addr_0;
  reg writevalid_1;
  reg readvalid_2;
  reg prev_awvalid_3;
  reg prev_arvalid_4;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_1 && !readvalid_2 && !saxi_bvalid && prev_awvalid_3);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_2 && !writevalid_1 && prev_arvalid_4 && !prev_awvalid_3);
  reg [_saxi_maskwidth-1:0] _tmp_5;
  wire signed [32-1:0] _tmp_6;
  assign _tmp_6 = (_tmp_5 == 0)? _saxi_register_0 : 
                  (_tmp_5 == 1)? _saxi_register_1 : 
                  (_tmp_5 == 2)? _saxi_register_2 : 
                  (_tmp_5 == 3)? _saxi_register_3 : 'hx;
  wire _tmp_7;
  assign _tmp_7 = (_tmp_5 == 0)? _saxi_flag_0 : 
                  (_tmp_5 == 1)? _saxi_flag_1 : 
                  (_tmp_5 == 2)? _saxi_flag_2 : 
                  (_tmp_5 == 3)? _saxi_flag_3 : 'hx;
  wire signed [32-1:0] _tmp_8;
  assign _tmp_8 = (_tmp_5 == 0)? _saxi_resetval_0 : 
                  (_tmp_5 == 1)? _saxi_resetval_1 : 
                  (_tmp_5 == 2)? _saxi_resetval_2 : 
                  (_tmp_5 == 3)? _saxi_resetval_3 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 3;
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
  reg axistreamin_flag_9;
  reg [32-1:0] _d1_th_comp;
  reg _th_comp_cond_7_0_1;
  reg _axi_a_ram_a_1_read_start;
  reg [8-1:0] _axi_a_ram_a_1_read_op_sel;
  reg [32-1:0] _axi_a_ram_a_1_read_local_addr;
  reg [33-1:0] _axi_a_ram_a_1_read_size;
  reg [32-1:0] _axi_a_ram_a_1_read_local_stride;
  reg [32-1:0] _axi_a_read_fsm;
  localparam _axi_a_read_fsm_init = 0;
  reg [33-1:0] _axi_a_read_rest_size;
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
  assign ram_a_1_addr = (_tmp_16)? _tmp_14 : 'hx;
  assign ram_a_1_wdata = (_tmp_16)? _tmp_15 : 'hx;
  assign ram_a_1_wenable = (_tmp_16)? 1'd1 : 0;
  assign ram_a_1_enable = (_tmp_16)? 1'd1 : 0;
  reg _ram_a_cond_0_1;
  assign axi_a_tready = _axi_a_read_fsm == 1;
  reg [32-1:0] _d1__axi_a_read_fsm;
  reg __axi_a_read_fsm_cond_1_0_1;
  reg axistreamin_flag_17;
  reg __axi_a_read_fsm_cond_2_1_1;
  reg axistreamin_flag_18;
  reg _th_comp_cond_12_1_1;
  reg _axi_b_ram_b_1_read_start;
  reg [8-1:0] _axi_b_ram_b_1_read_op_sel;
  reg [32-1:0] _axi_b_ram_b_1_read_local_addr;
  reg [33-1:0] _axi_b_ram_b_1_read_size;
  reg [32-1:0] _axi_b_ram_b_1_read_local_stride;
  reg [32-1:0] _axi_b_read_fsm;
  localparam _axi_b_read_fsm_init = 0;
  reg [33-1:0] _axi_b_read_rest_size;
  reg [32-1:0] _wdata_19;
  reg _wvalid_20;
  reg [33-1:0] _tmp_21;
  reg _tmp_22;
  wire [32-1:0] _dataflow__variable_odata_1;
  wire _dataflow__variable_ovalid_1;
  wire _dataflow__variable_oready_1;
  assign _dataflow__variable_oready_1 = (_tmp_21 > 0) && !_tmp_22;
  reg [10-1:0] _tmp_23;
  reg [32-1:0] _tmp_24;
  reg _tmp_25;
  assign ram_b_1_addr = (_tmp_25)? _tmp_23 : 'hx;
  assign ram_b_1_wdata = (_tmp_25)? _tmp_24 : 'hx;
  assign ram_b_1_wenable = (_tmp_25)? 1'd1 : 0;
  assign ram_b_1_enable = (_tmp_25)? 1'd1 : 0;
  reg _ram_b_cond_0_1;
  assign axi_b_tready = _axi_b_read_fsm == 1;
  reg [32-1:0] _d1__axi_b_read_fsm;
  reg __axi_b_read_fsm_cond_1_0_1;
  reg axistreamin_flag_26;
  reg __axi_b_read_fsm_cond_2_1_1;
  reg signed [32-1:0] _th_comp_size_2;
  reg signed [32-1:0] _th_comp_offset_3;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  reg __mystream_stream_ivalid_1;
  reg signed [32-1:0] _plus_data_2;
  wire signed [32-1:0] mystream_c_data;
  assign mystream_c_data = _plus_data_2;
  wire _set_flag_27;
  assign _set_flag_27 = th_comp == 17;
  assign ram_a_0_addr = (_mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1))? _mystream_a_source_ram_raddr : 'hx;
  assign ram_a_0_enable = (_mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1))? 1'd1 : 0;
  localparam _tmp_28 = 1;
  wire [_tmp_28-1:0] _tmp_29;
  assign _tmp_29 = _mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1);
  reg [_tmp_28-1:0] __tmp_29_1;
  assign _mystream_a_source_ram_rdata = (_mystream_a_source_sel == 1)? ram_a_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_a_source_fsm_0;
  localparam _mystream_a_source_fsm_0_init = 0;
  wire _set_flag_30;
  assign _set_flag_30 = th_comp == 18;
  assign ram_b_0_addr = (_mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2))? _mystream_b_source_ram_raddr : 'hx;
  assign ram_b_0_enable = (_mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2))? 1'd1 : 0;
  localparam _tmp_31 = 1;
  wire [_tmp_31-1:0] _tmp_32;
  assign _tmp_32 = _mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2);
  reg [_tmp_31-1:0] __tmp_32_1;
  assign _mystream_b_source_ram_rdata = (_mystream_b_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_b_data = __variable_wdata_1;
  reg [32-1:0] _mystream_b_source_fsm_1;
  localparam _mystream_b_source_fsm_1_init = 0;
  wire _set_flag_33;
  assign _set_flag_33 = th_comp == 19;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg signed [32-1:0] _tmp_37;
  reg signed [32-1:0] _tmp_38;
  reg signed [32-1:0] _tmp_39;
  reg signed [32-1:0] _tmp_40;
  reg signed [32-1:0] _tmp_41;
  reg signed [32-1:0] _tmp_42;
  assign ram_c_0_addr = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? _mystream_c_sink_waddr : 'hx;
  assign ram_c_0_wdata = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? _mystream_c_sink_wdata : 'hx;
  assign ram_c_0_wenable = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? 1'd1 : 0;
  assign ram_c_0_enable = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? 1'd1 : 0;
  reg [32-1:0] _mystream_c_sink_fsm_2;
  localparam _mystream_c_sink_fsm_2_init = 0;
  wire _set_flag_43;
  assign _set_flag_43 = th_comp == 20;
  assign _mystream_run_flag = (_set_flag_43)? 1 : 0;
  reg _tmp_44;
  reg _tmp_45;
  reg _tmp_46;
  assign _mystream_source_stop = _mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3));
  localparam _tmp_47 = 1;
  wire [_tmp_47-1:0] _tmp_48;
  assign _tmp_48 = _mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3);
  reg [_tmp_47-1:0] _tmp_49;
  reg _tmp_50;
  reg _tmp_51;
  reg _tmp_52;
  assign _mystream_sink_start = _tmp_52;
  reg _tmp_53;
  reg _tmp_54;
  reg _tmp_55;
  assign _mystream_sink_stop = _tmp_55;
  reg _tmp_56;
  reg _tmp_57;
  reg _tmp_58;
  assign _mystream_sink_busy = _tmp_58;
  reg _tmp_59;
  assign _mystream_busy = _mystream_source_busy || _mystream_sink_busy || _mystream_busy_reg;
  reg axistreamout_flag_60;
  reg _th_comp_cond_24_2_1;
  reg _axi_c_ram_c_1_write_start;
  reg [8-1:0] _axi_c_ram_c_1_write_op_sel;
  reg [32-1:0] _axi_c_ram_c_1_write_local_addr;
  reg [33-1:0] _axi_c_ram_c_1_write_size;
  reg [32-1:0] _axi_c_ram_c_1_write_local_stride;
  reg [32-1:0] _axi_c_write_fsm;
  localparam _axi_c_write_fsm_init = 0;
  reg _tmp_61;
  reg _tmp_62;
  wire _tmp_63;
  wire _tmp_64;
  wire signed [32-1:0] _tmp_65;
  assign _tmp_65 = ram_c_1_rdata;
  reg _tmp_66;
  reg _tmp_67;
  reg _tmp_68;
  reg _tmp_69;
  reg [33-1:0] _tmp_70;
  reg [10-1:0] _tmp_71;
  assign ram_c_1_addr = (_tmp_66)? _tmp_71 : 'hx;
  assign ram_c_1_enable = ((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && _tmp_66)? 1'd1 : 0;
  reg [33-1:0] _axi_c_write_counter;
  wire [32-1:0] _dataflow__variable_odata_2;
  wire _dataflow__variable_ovalid_2;
  wire _dataflow__variable_oready_2;
  assign _dataflow__variable_oready_2 = (_axi_c_write_fsm == 1) && (_axi_c_write_op_sel == 1) && (axi_c_tready || !axi_c_tvalid);
  wire [1-1:0] _dataflow__variable_odata_3;
  wire _dataflow__variable_ovalid_3;
  wire _dataflow__variable_oready_3;
  assign _dataflow__variable_oready_3 = (_axi_c_write_fsm == 1) && (_axi_c_write_op_sel == 1) && (axi_c_tready || !axi_c_tvalid);
  reg _axi_c_cond_0_1;
  reg axistreamout_flag_72;
  reg [32-1:0] _d1__axi_c_write_fsm;
  reg __axi_c_write_fsm_cond_2_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_a_read_start <= 0;
      _axi_a_ram_a_1_read_start <= 0;
      _axi_a_ram_a_1_read_op_sel <= 0;
      _axi_a_ram_a_1_read_local_addr <= 0;
      _axi_a_ram_a_1_read_size <= 0;
      _axi_a_ram_a_1_read_local_stride <= 0;
      _axi_a_read_idle <= 1;
      _axi_a_read_op_sel <= 0;
      _axi_a_read_local_addr <= 0;
      _axi_a_read_size <= 0;
      _axi_a_read_local_stride <= 0;
    end else begin
      _axi_a_read_start <= 0;
      _axi_a_ram_a_1_read_start <= 0;
      if(axistreamin_flag_9) begin
        _axi_a_ram_a_1_read_start <= 1;
        _axi_a_ram_a_1_read_op_sel <= 1;
        _axi_a_ram_a_1_read_local_addr <= _th_comp_offset_1;
        _axi_a_ram_a_1_read_size <= _th_comp_size_0;
        _axi_a_ram_a_1_read_local_stride <= 1;
      end 
      if(_axi_a_ram_a_1_read_start) begin
        _axi_a_read_idle <= 0;
      end 
      if(_axi_a_ram_a_1_read_start) begin
        _axi_a_read_start <= 1;
        _axi_a_read_op_sel <= _axi_a_ram_a_1_read_op_sel;
        _axi_a_read_local_addr <= _axi_a_ram_a_1_read_local_addr;
        _axi_a_read_size <= _axi_a_ram_a_1_read_size;
        _axi_a_read_local_stride <= _axi_a_ram_a_1_read_local_stride;
      end 
      if(axistreamin_flag_17) begin
        _axi_a_read_idle <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_0 = _wdata_10;
  assign _dataflow__variable_ovalid_0 = _wvalid_11;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_b_read_start <= 0;
      _axi_b_ram_b_1_read_start <= 0;
      _axi_b_ram_b_1_read_op_sel <= 0;
      _axi_b_ram_b_1_read_local_addr <= 0;
      _axi_b_ram_b_1_read_size <= 0;
      _axi_b_ram_b_1_read_local_stride <= 0;
      _axi_b_read_idle <= 1;
      _axi_b_read_op_sel <= 0;
      _axi_b_read_local_addr <= 0;
      _axi_b_read_size <= 0;
      _axi_b_read_local_stride <= 0;
    end else begin
      _axi_b_read_start <= 0;
      _axi_b_ram_b_1_read_start <= 0;
      if(axistreamin_flag_18) begin
        _axi_b_ram_b_1_read_start <= 1;
        _axi_b_ram_b_1_read_op_sel <= 1;
        _axi_b_ram_b_1_read_local_addr <= _th_comp_offset_1;
        _axi_b_ram_b_1_read_size <= _th_comp_size_0;
        _axi_b_ram_b_1_read_local_stride <= 1;
      end 
      if(_axi_b_ram_b_1_read_start) begin
        _axi_b_read_idle <= 0;
      end 
      if(_axi_b_ram_b_1_read_start) begin
        _axi_b_read_start <= 1;
        _axi_b_read_op_sel <= _axi_b_ram_b_1_read_op_sel;
        _axi_b_read_local_addr <= _axi_b_ram_b_1_read_local_addr;
        _axi_b_read_size <= _axi_b_ram_b_1_read_size;
        _axi_b_read_local_stride <= _axi_b_ram_b_1_read_local_stride;
      end 
      if(axistreamin_flag_26) begin
        _axi_b_read_idle <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_1 = _wdata_19;
  assign _dataflow__variable_ovalid_1 = _wvalid_20;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_c_write_start <= 0;
      _axi_c_ram_c_1_write_start <= 0;
      _axi_c_ram_c_1_write_op_sel <= 0;
      _axi_c_ram_c_1_write_local_addr <= 0;
      _axi_c_ram_c_1_write_size <= 0;
      _axi_c_ram_c_1_write_local_stride <= 0;
      _axi_c_write_idle <= 1;
      _axi_c_write_op_sel <= 0;
      _axi_c_write_local_addr <= 0;
      _axi_c_write_size <= 0;
      _axi_c_write_local_stride <= 0;
      axi_c_tdata <= 0;
      axi_c_tvalid <= 0;
      axi_c_tlast <= 0;
      _axi_c_cond_0_1 <= 0;
    end else begin
      if(_axi_c_cond_0_1) begin
        axi_c_tvalid <= 0;
        axi_c_tlast <= 0;
      end 
      _axi_c_write_start <= 0;
      _axi_c_ram_c_1_write_start <= 0;
      if(axistreamout_flag_60) begin
        _axi_c_ram_c_1_write_start <= 1;
        _axi_c_ram_c_1_write_op_sel <= 1;
        _axi_c_ram_c_1_write_local_addr <= _th_comp_offset_1;
        _axi_c_ram_c_1_write_size <= _th_comp_size_0;
        _axi_c_ram_c_1_write_local_stride <= 1;
      end 
      if(_axi_c_ram_c_1_write_start) begin
        _axi_c_write_idle <= 0;
      end 
      if(_axi_c_ram_c_1_write_start) begin
        _axi_c_write_start <= 1;
        _axi_c_write_op_sel <= _axi_c_ram_c_1_write_op_sel;
        _axi_c_write_local_addr <= _axi_c_ram_c_1_write_local_addr;
        _axi_c_write_size <= _axi_c_ram_c_1_write_size;
        _axi_c_write_local_stride <= _axi_c_ram_c_1_write_local_stride;
      end 
      if(_dataflow__variable_ovalid_2 && ((_axi_c_write_fsm == 1) && (_axi_c_write_op_sel == 1) && (axi_c_tready || !axi_c_tvalid)) && (axi_c_tready || !axi_c_tvalid)) begin
        axi_c_tdata <= _dataflow__variable_odata_2;
        axi_c_tvalid <= 1;
        axi_c_tlast <= _dataflow__variable_odata_3;
      end 
      _axi_c_cond_0_1 <= 1;
      if(axi_c_tvalid && !axi_c_tready) begin
        axi_c_tvalid <= axi_c_tvalid;
        axi_c_tlast <= axi_c_tlast;
      end 
      if(axistreamout_flag_72) begin
        _axi_c_write_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_3 <= 0;
      prev_arvalid_4 <= 0;
      writevalid_1 <= 0;
      readvalid_2 <= 0;
      addr_0 <= 0;
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
      prev_awvalid_3 <= saxi_awvalid;
      prev_arvalid_4 <= saxi_arvalid;
      writevalid_1 <= 0;
      readvalid_2 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_0 <= saxi_awaddr;
        writevalid_1 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_0 <= saxi_araddr;
        readvalid_2 <= 1;
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
      if((_saxi_register_fsm == 3) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 3)) begin
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
      if((th_comp == 28) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 28) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 28) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 28) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;
  localparam _saxi_register_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_2 || writevalid_1) begin
            _tmp_5 <= (addr_0 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_2) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_1) begin
            _saxi_register_fsm <= _saxi_register_fsm_3;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready && saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
          if((saxi_rready || !saxi_rvalid) && !(saxi_rready && saxi_rvalid)) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_2: begin
          if(saxi_rready && saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_3: begin
          if(saxi_wready && saxi_wvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_14 <= 0;
      _tmp_12 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_13 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_29_1 <= 0;
    end else begin
      if(_ram_a_cond_0_1) begin
        _tmp_16 <= 0;
        _tmp_13 <= 0;
      end 
      if(_axi_a_read_start && (_axi_a_read_op_sel == 1) && (_tmp_12 == 0)) begin
        _tmp_14 <= _axi_a_read_local_addr - _axi_a_read_local_stride;
        _tmp_12 <= _axi_a_read_size;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 > 0)) begin
        _tmp_14 <= _tmp_14 + _axi_a_read_local_stride;
        _tmp_15 <= _dataflow__variable_odata_0;
        _tmp_16 <= 1;
        _tmp_12 <= _tmp_12 - 1;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 == 1)) begin
        _tmp_13 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      __tmp_29_1 <= _tmp_29;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_23 <= 0;
      _tmp_21 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_22 <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_32_1 <= 0;
    end else begin
      if(_ram_b_cond_0_1) begin
        _tmp_25 <= 0;
        _tmp_22 <= 0;
      end 
      if(_axi_b_read_start && (_axi_b_read_op_sel == 1) && (_tmp_21 == 0)) begin
        _tmp_23 <= _axi_b_read_local_addr - _axi_b_read_local_stride;
        _tmp_21 <= _axi_b_read_size;
      end 
      if(_dataflow__variable_ovalid_1 && ((_tmp_21 > 0) && !_tmp_22) && (_tmp_21 > 0)) begin
        _tmp_23 <= _tmp_23 + _axi_b_read_local_stride;
        _tmp_24 <= _dataflow__variable_odata_1;
        _tmp_25 <= 1;
        _tmp_21 <= _tmp_21 - 1;
      end 
      if(_dataflow__variable_ovalid_1 && ((_tmp_21 > 0) && !_tmp_22) && (_tmp_21 == 1)) begin
        _tmp_22 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      __tmp_32_1 <= _tmp_32;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_69 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _tmp_66 <= 0;
      _tmp_71 <= 0;
      _tmp_70 <= 0;
    end else begin
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && _tmp_67) begin
        _tmp_69 <= 0;
        _tmp_61 <= 0;
        _tmp_62 <= 0;
        _tmp_67 <= 0;
      end 
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && _tmp_66) begin
        _tmp_61 <= 1;
        _tmp_62 <= 1;
        _tmp_69 <= _tmp_68;
        _tmp_68 <= 0;
        _tmp_66 <= 0;
        _tmp_67 <= 1;
      end 
      if(_axi_c_write_start && (_axi_c_write_op_sel == 1) && (_tmp_70 == 0) && !_tmp_68 && !_tmp_69) begin
        _tmp_71 <= _axi_c_write_local_addr;
        _tmp_70 <= _axi_c_write_size - 1;
        _tmp_66 <= 1;
        _tmp_68 <= _axi_c_write_size == 1;
      end 
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && (_tmp_70 > 0)) begin
        _tmp_71 <= _tmp_71 + _axi_c_write_local_stride;
        _tmp_70 <= _tmp_70 - 1;
        _tmp_66 <= 1;
        _tmp_68 <= 0;
      end 
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && (_tmp_70 == 1)) begin
        _tmp_68 <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_2 = _tmp_65;
  assign _dataflow__variable_ovalid_2 = _tmp_61;
  assign _tmp_63 = 1 && _dataflow__variable_oready_2;
  assign _dataflow__variable_odata_3 = _tmp_69;
  assign _dataflow__variable_ovalid_3 = _tmp_62;
  assign _tmp_64 = 1 && _dataflow__variable_oready_3;

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
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
      _tmp_42 <= 0;
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
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_55 <= 0;
      _tmp_56 <= 0;
      _tmp_57 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
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
      if(_set_flag_27) begin
        _mystream_a_source_mode <= 5'b1;
        _mystream_a_source_offset <= _th_comp_offset_3;
        _mystream_a_source_size <= _th_comp_size_2;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_27) begin
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
      if(_set_flag_30) begin
        _mystream_b_source_mode <= 5'b1;
        _mystream_b_source_offset <= _th_comp_offset_3;
        _mystream_b_source_size <= _th_comp_size_2;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_30) begin
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
        _tmp_34 <= _set_flag_33;
      end 
      if(_mystream_stream_oready) begin
        _tmp_35 <= _tmp_34;
      end 
      if(_mystream_stream_oready) begin
        _tmp_36 <= _tmp_35;
      end 
      if(_mystream_stream_oready) begin
        _tmp_37 <= _th_comp_offset_3;
      end 
      if(_mystream_stream_oready) begin
        _tmp_38 <= _tmp_37;
      end 
      if(_mystream_stream_oready) begin
        _tmp_39 <= _tmp_38;
      end 
      if(_mystream_stream_oready) begin
        _tmp_40 <= _th_comp_size_2;
      end 
      if(_mystream_stream_oready) begin
        _tmp_41 <= _tmp_40;
      end 
      if(_mystream_stream_oready) begin
        _tmp_42 <= _tmp_41;
      end 
      if(_tmp_36) begin
        _mystream_c_sink_mode <= 5'b1;
        _mystream_c_sink_offset <= _tmp_39;
        _mystream_c_sink_size <= _tmp_42;
        _mystream_c_sink_stride <= 1;
      end 
      if(_tmp_36) begin
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
        _tmp_44 <= _mystream_source_start;
      end 
      if(_mystream_stream_oready) begin
        _tmp_45 <= _tmp_44;
      end 
      if(_mystream_stream_oready) begin
        _tmp_46 <= _tmp_45;
      end 
      if(_mystream_stream_oready) begin
        _tmp_49 <= _tmp_48;
      end 
      if(_mystream_stream_oready) begin
        _tmp_50 <= _mystream_source_start;
      end 
      if(_mystream_stream_oready) begin
        _tmp_51 <= _tmp_50;
      end 
      if(_mystream_stream_oready) begin
        _tmp_52 <= _tmp_51;
      end 
      if(_mystream_stream_oready) begin
        _tmp_53 <= _mystream_source_stop;
      end 
      if(_mystream_stream_oready) begin
        _tmp_54 <= _tmp_53;
      end 
      if(_mystream_stream_oready) begin
        _tmp_55 <= _tmp_54;
      end 
      if(_mystream_stream_oready) begin
        _tmp_56 <= _mystream_source_busy;
      end 
      if(_mystream_stream_oready) begin
        _tmp_57 <= _tmp_56;
      end 
      if(_mystream_stream_oready) begin
        _tmp_58 <= _tmp_57;
      end 
      if(_mystream_stream_oready) begin
        _tmp_59 <= _mystream_sink_busy;
      end 
      if(!_mystream_sink_busy && _tmp_59) begin
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
      if(_mystream_stream_oready && _tmp_46) begin
        _mystream_stream_ivalid <= 1;
      end 
      if(_mystream_stream_oready && _tmp_49) begin
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
  localparam th_comp_23 = 23;
  localparam th_comp_24 = 24;
  localparam th_comp_25 = 25;
  localparam th_comp_26 = 26;
  localparam th_comp_27 = 27;
  localparam th_comp_28 = 28;
  localparam th_comp_29 = 29;
  localparam th_comp_30 = 30;
  localparam th_comp_31 = 31;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _d1_th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_offset_1 <= 0;
      axistreamin_flag_9 <= 0;
      _th_comp_cond_7_0_1 <= 0;
      axistreamin_flag_18 <= 0;
      _th_comp_cond_12_1_1 <= 0;
      _th_comp_size_2 <= 0;
      _th_comp_offset_3 <= 0;
      axistreamout_flag_60 <= 0;
      _th_comp_cond_24_2_1 <= 0;
    end else begin
      _d1_th_comp <= th_comp;
      case(_d1_th_comp)
        th_comp_7: begin
          if(_th_comp_cond_7_0_1) begin
            axistreamin_flag_9 <= 0;
          end 
        end
        th_comp_12: begin
          if(_th_comp_cond_12_1_1) begin
            axistreamin_flag_18 <= 0;
          end 
        end
        th_comp_24: begin
          if(_th_comp_cond_24_2_1) begin
            axistreamout_flag_60 <= 0;
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
            th_comp <= th_comp_30;
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
          if(_axi_a_read_idle) begin
            th_comp <= th_comp_7;
          end 
        end
        th_comp_7: begin
          axistreamin_flag_9 <= 1;
          _th_comp_cond_7_0_1 <= 1;
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if(_axi_a_read_idle) begin
            th_comp <= th_comp_11;
          end 
        end
        th_comp_11: begin
          if(_axi_b_read_idle) begin
            th_comp <= th_comp_12;
          end 
        end
        th_comp_12: begin
          axistreamin_flag_18 <= 1;
          _th_comp_cond_12_1_1 <= 1;
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(_axi_b_read_idle) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          _th_comp_size_2 <= _th_comp_size_0;
          _th_comp_offset_3 <= _th_comp_offset_1;
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(_mystream_stream_oready) begin
            th_comp <= th_comp_20;
          end 
        end
        th_comp_20: begin
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          if(_mystream_busy) begin
            th_comp <= th_comp_22;
          end 
        end
        th_comp_22: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_23;
          end 
        end
        th_comp_23: begin
          if(_axi_c_write_idle) begin
            th_comp <= th_comp_24;
          end 
        end
        th_comp_24: begin
          axistreamout_flag_60 <= 1;
          _th_comp_cond_24_2_1 <= 1;
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          if(_axi_c_write_idle) begin
            th_comp <= th_comp_28;
          end 
        end
        th_comp_28: begin
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          th_comp <= th_comp_1;
        end
        th_comp_30: begin
          $finish;
          th_comp <= th_comp_31;
        end
      endcase
    end
  end

  localparam _axi_a_read_fsm_1 = 1;
  localparam _axi_a_read_fsm_2 = 2;
  localparam _axi_a_read_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_a_read_fsm <= _axi_a_read_fsm_init;
      _d1__axi_a_read_fsm <= _axi_a_read_fsm_init;
      _axi_a_read_rest_size <= 0;
      __axi_a_read_fsm_cond_1_0_1 <= 0;
      _wvalid_11 <= 0;
      _wdata_10 <= 0;
      axistreamin_flag_17 <= 0;
      __axi_a_read_fsm_cond_2_1_1 <= 0;
    end else begin
      _d1__axi_a_read_fsm <= _axi_a_read_fsm;
      case(_d1__axi_a_read_fsm)
        _axi_a_read_fsm_1: begin
          if(__axi_a_read_fsm_cond_1_0_1) begin
            _wvalid_11 <= 0;
          end 
        end
        _axi_a_read_fsm_2: begin
          if(__axi_a_read_fsm_cond_2_1_1) begin
            axistreamin_flag_17 <= 0;
          end 
        end
      endcase
      case(_axi_a_read_fsm)
        _axi_a_read_fsm_init: begin
          if(_axi_a_read_start) begin
            _axi_a_read_rest_size <= _axi_a_read_size;
          end 
          if(_axi_a_read_start && (_axi_a_read_op_sel == 1)) begin
            _axi_a_read_fsm <= _axi_a_read_fsm_1;
          end 
        end
        _axi_a_read_fsm_1: begin
          __axi_a_read_fsm_cond_1_0_1 <= 1;
          if(axi_a_tready && axi_a_tvalid && (_axi_a_read_op_sel == 1)) begin
            _wdata_10 <= axi_a_tdata;
            _wvalid_11 <= 1;
          end 
          if(axi_a_tready && axi_a_tvalid && (_axi_a_read_op_sel == 1)) begin
            _axi_a_read_rest_size <= _axi_a_read_rest_size - 1;
          end 
          if(axi_a_tready && axi_a_tvalid && (_axi_a_read_rest_size <= 1)) begin
            _axi_a_read_fsm <= _axi_a_read_fsm_2;
          end 
        end
        _axi_a_read_fsm_2: begin
          axistreamin_flag_17 <= 1;
          __axi_a_read_fsm_cond_2_1_1 <= 1;
          _axi_a_read_fsm <= _axi_a_read_fsm_3;
        end
        _axi_a_read_fsm_3: begin
          _axi_a_read_fsm <= _axi_a_read_fsm_init;
        end
      endcase
    end
  end

  localparam _axi_b_read_fsm_1 = 1;
  localparam _axi_b_read_fsm_2 = 2;
  localparam _axi_b_read_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_b_read_fsm <= _axi_b_read_fsm_init;
      _d1__axi_b_read_fsm <= _axi_b_read_fsm_init;
      _axi_b_read_rest_size <= 0;
      __axi_b_read_fsm_cond_1_0_1 <= 0;
      _wvalid_20 <= 0;
      _wdata_19 <= 0;
      axistreamin_flag_26 <= 0;
      __axi_b_read_fsm_cond_2_1_1 <= 0;
    end else begin
      _d1__axi_b_read_fsm <= _axi_b_read_fsm;
      case(_d1__axi_b_read_fsm)
        _axi_b_read_fsm_1: begin
          if(__axi_b_read_fsm_cond_1_0_1) begin
            _wvalid_20 <= 0;
          end 
        end
        _axi_b_read_fsm_2: begin
          if(__axi_b_read_fsm_cond_2_1_1) begin
            axistreamin_flag_26 <= 0;
          end 
        end
      endcase
      case(_axi_b_read_fsm)
        _axi_b_read_fsm_init: begin
          if(_axi_b_read_start) begin
            _axi_b_read_rest_size <= _axi_b_read_size;
          end 
          if(_axi_b_read_start && (_axi_b_read_op_sel == 1)) begin
            _axi_b_read_fsm <= _axi_b_read_fsm_1;
          end 
        end
        _axi_b_read_fsm_1: begin
          __axi_b_read_fsm_cond_1_0_1 <= 1;
          if(axi_b_tready && axi_b_tvalid && (_axi_b_read_op_sel == 1)) begin
            _wdata_19 <= axi_b_tdata;
            _wvalid_20 <= 1;
          end 
          if(axi_b_tready && axi_b_tvalid && (_axi_b_read_op_sel == 1)) begin
            _axi_b_read_rest_size <= _axi_b_read_rest_size - 1;
          end 
          if(axi_b_tready && axi_b_tvalid && (_axi_b_read_rest_size <= 1)) begin
            _axi_b_read_fsm <= _axi_b_read_fsm_2;
          end 
        end
        _axi_b_read_fsm_2: begin
          axistreamin_flag_26 <= 1;
          __axi_b_read_fsm_cond_2_1_1 <= 1;
          _axi_b_read_fsm <= _axi_b_read_fsm_3;
        end
        _axi_b_read_fsm_3: begin
          _axi_b_read_fsm <= _axi_b_read_fsm_init;
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

  localparam _axi_c_write_fsm_1 = 1;
  localparam _axi_c_write_fsm_2 = 2;
  localparam _axi_c_write_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _axi_c_write_fsm <= _axi_c_write_fsm_init;
      _d1__axi_c_write_fsm <= _axi_c_write_fsm_init;
      _axi_c_write_counter <= 0;
      axistreamout_flag_72 <= 0;
      __axi_c_write_fsm_cond_2_0_1 <= 0;
    end else begin
      _d1__axi_c_write_fsm <= _axi_c_write_fsm;
      case(_d1__axi_c_write_fsm)
        _axi_c_write_fsm_2: begin
          if(__axi_c_write_fsm_cond_2_0_1) begin
            axistreamout_flag_72 <= 0;
          end 
        end
      endcase
      case(_axi_c_write_fsm)
        _axi_c_write_fsm_init: begin
          if(_axi_c_write_start) begin
            _axi_c_write_counter <= _axi_c_write_size;
          end 
          if(_axi_c_write_start && (_axi_c_write_op_sel == 1)) begin
            _axi_c_write_fsm <= _axi_c_write_fsm_1;
          end 
        end
        _axi_c_write_fsm_1: begin
          if(axi_c_tvalid && axi_c_tready) begin
            _axi_c_write_counter <= _axi_c_write_counter - 1;
          end 
          if(_axi_c_write_counter == 0) begin
            _axi_c_write_fsm <= _axi_c_write_fsm_2;
          end 
        end
        _axi_c_write_fsm_2: begin
          axistreamout_flag_72 <= 1;
          __axi_c_write_fsm_cond_2_0_1 <= 1;
          _axi_c_write_fsm <= _axi_c_write_fsm_3;
        end
        _axi_c_write_fsm_3: begin
          _axi_c_write_fsm <= _axi_c_write_fsm_init;
        end
      endcase
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

    code = thread_stream_axi_stream.run(filename=None, simtype=simtype,
                                        outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
