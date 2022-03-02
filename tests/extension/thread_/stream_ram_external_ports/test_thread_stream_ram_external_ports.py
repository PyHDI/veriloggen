from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_stream_ram_external_ports


expected_verilog = """
module blinkled
(
  input CLK,
  input RST,
  input [10-1:0] ram_a_1_addr,
  output [32-1:0] ram_a_1_rdata,
  input [32-1:0] ram_a_1_wdata,
  input ram_a_1_wenable,
  input ram_a_1_enable,
  input [10-1:0] ram_b_1_addr,
  output [32-1:0] ram_b_1_rdata,
  input [32-1:0] ram_b_1_wdata,
  input ram_b_1_wenable,
  input ram_b_1_enable,
  input [10-1:0] ram_c_1_addr,
  output [32-1:0] ram_c_1_rdata,
  input [32-1:0] ram_c_1_wdata,
  input ram_c_1_wenable,
  input ram_c_1_enable,
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

  wire [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  wire [32-1:0] ram_a_0_wdata;
  wire ram_a_0_wenable;
  wire ram_a_0_enable;
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
  reg [_saxi_maskwidth-1:0] axis_maskaddr_5;
  wire signed [32-1:0] axislite_rdata_6;
  assign axislite_rdata_6 = (axis_maskaddr_5 == 0)? _saxi_register_0 : 
                            (axis_maskaddr_5 == 1)? _saxi_register_1 : 
                            (axis_maskaddr_5 == 2)? _saxi_register_2 : 
                            (axis_maskaddr_5 == 3)? _saxi_register_3 : 'hx;
  wire axislite_flag_7;
  assign axislite_flag_7 = (axis_maskaddr_5 == 0)? _saxi_flag_0 : 
                           (axis_maskaddr_5 == 1)? _saxi_flag_1 : 
                           (axis_maskaddr_5 == 2)? _saxi_flag_2 : 
                           (axis_maskaddr_5 == 3)? _saxi_flag_3 : 'hx;
  wire signed [32-1:0] axislite_resetval_8;
  assign axislite_resetval_8 = (axis_maskaddr_5 == 0)? _saxi_resetval_0 : 
                               (axis_maskaddr_5 == 1)? _saxi_resetval_1 : 
                               (axis_maskaddr_5 == 2)? _saxi_resetval_2 : 
                               (axis_maskaddr_5 == 3)? _saxi_resetval_3 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
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
  reg signed [32-1:0] _th_comp_size_2;
  reg signed [32-1:0] _th_comp_offset_3;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  reg __mystream_stream_ivalid_1;
  reg signed [32-1:0] _plus_data_2;
  wire signed [32-1:0] mystream_c_data;
  assign mystream_c_data = _plus_data_2;
  wire _set_flag_9;
  assign _set_flag_9 = th_comp == 7;
  assign ram_a_0_addr = (_mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1))? _mystream_a_source_ram_raddr : 'hx;
  assign ram_a_0_enable = (_mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1))? 1'd1 : 0;
  localparam _tmp_10 = 1;
  wire [_tmp_10-1:0] _tmp_11;
  assign _tmp_11 = _mystream_stream_oready && _mystream_a_source_ram_renable && (_mystream_a_source_sel == 1);
  reg [_tmp_10-1:0] __tmp_11_1;
  assign _mystream_a_source_ram_rdata = (_mystream_a_source_sel == 1)? ram_a_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_a_source_fsm_0;
  localparam _mystream_a_source_fsm_0_init = 0;
  wire _set_flag_12;
  assign _set_flag_12 = th_comp == 8;
  assign ram_b_0_addr = (_mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2))? _mystream_b_source_ram_raddr : 'hx;
  assign ram_b_0_enable = (_mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2))? 1'd1 : 0;
  localparam _tmp_13 = 1;
  wire [_tmp_13-1:0] _tmp_14;
  assign _tmp_14 = _mystream_stream_oready && _mystream_b_source_ram_renable && (_mystream_b_source_sel == 2);
  reg [_tmp_13-1:0] __tmp_14_1;
  assign _mystream_b_source_ram_rdata = (_mystream_b_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_b_data = __variable_wdata_1;
  reg [32-1:0] _mystream_b_source_fsm_1;
  localparam _mystream_b_source_fsm_1_init = 0;
  wire _set_flag_15;
  assign _set_flag_15 = th_comp == 9;
  reg _tmp_16;
  reg _tmp_17;
  reg _tmp_18;
  reg signed [32-1:0] _tmp_19;
  reg signed [32-1:0] _tmp_20;
  reg signed [32-1:0] _tmp_21;
  reg signed [32-1:0] _tmp_22;
  reg signed [32-1:0] _tmp_23;
  reg signed [32-1:0] _tmp_24;
  assign ram_c_0_addr = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? _mystream_c_sink_waddr : 'hx;
  assign ram_c_0_wdata = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? _mystream_c_sink_wdata : 'hx;
  assign ram_c_0_wenable = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? 1'd1 : 0;
  assign ram_c_0_enable = (_mystream_stream_oready && _mystream_c_sink_wenable && (_mystream_c_sink_sel == 3))? 1'd1 : 0;
  reg [32-1:0] _mystream_c_sink_fsm_2;
  localparam _mystream_c_sink_fsm_2_init = 0;
  wire _set_flag_25;
  assign _set_flag_25 = th_comp == 10;
  assign _mystream_run_flag = (_set_flag_25)? 1 : 0;
  reg _tmp_26;
  reg _tmp_27;
  reg _tmp_28;
  assign _mystream_source_stop = _mystream_stream_oready && (_mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3));
  localparam _tmp_29 = 1;
  wire [_tmp_29-1:0] _tmp_30;
  assign _tmp_30 = _mystream_a_idle && _mystream_b_idle && (_mystream_fsm == 3);
  reg [_tmp_29-1:0] _tmp_31;
  reg _tmp_32;
  reg _tmp_33;
  reg _tmp_34;
  assign _mystream_sink_start = _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg _tmp_37;
  assign _mystream_sink_stop = _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  reg _tmp_40;
  assign _mystream_sink_busy = _tmp_40;
  reg _tmp_41;
  assign _mystream_busy = _mystream_source_busy || _mystream_sink_busy || _mystream_busy_reg;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_11_1 <= 0;
    end else begin
      __tmp_11_1 <= _tmp_11;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_14_1 <= 0;
    end else begin
      __tmp_14_1 <= _tmp_14;
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
        saxi_rdata <= axislite_rdata_6;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 0)) begin
        _saxi_register_0 <= axislite_resetval_8;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 1)) begin
        _saxi_register_1 <= axislite_resetval_8;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 2)) begin
        _saxi_register_2 <= axislite_resetval_8;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 3)) begin
        _saxi_register_3 <= axislite_resetval_8;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 3)) begin
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
      if((th_comp == 13) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_comp == 13) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_comp == 13) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_comp == 13) && 0) begin
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
      axis_maskaddr_5 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_2 || writevalid_1) begin
            axis_maskaddr_5 <= (addr_0 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_2) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_1) begin
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
      _tmp_16 <= 0;
      _tmp_17 <= 0;
      _tmp_18 <= 0;
      _tmp_19 <= 0;
      _tmp_20 <= 0;
      _tmp_21 <= 0;
      _tmp_22 <= 0;
      _tmp_23 <= 0;
      _tmp_24 <= 0;
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
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_28 <= 0;
      _tmp_31 <= 0;
      _tmp_32 <= 0;
      _tmp_33 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
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
      if(_set_flag_9) begin
        _mystream_a_source_mode <= 5'b1;
        _mystream_a_source_offset <= _th_comp_offset_3;
        _mystream_a_source_size <= _th_comp_size_2;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_9) begin
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
      if(_set_flag_12) begin
        _mystream_b_source_mode <= 5'b1;
        _mystream_b_source_offset <= _th_comp_offset_3;
        _mystream_b_source_size <= _th_comp_size_2;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_12) begin
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
        _tmp_16 <= _set_flag_15;
      end 
      if(_mystream_stream_oready) begin
        _tmp_17 <= _tmp_16;
      end 
      if(_mystream_stream_oready) begin
        _tmp_18 <= _tmp_17;
      end 
      if(_mystream_stream_oready) begin
        _tmp_19 <= _th_comp_offset_3;
      end 
      if(_mystream_stream_oready) begin
        _tmp_20 <= _tmp_19;
      end 
      if(_mystream_stream_oready) begin
        _tmp_21 <= _tmp_20;
      end 
      if(_mystream_stream_oready) begin
        _tmp_22 <= _th_comp_size_2;
      end 
      if(_mystream_stream_oready) begin
        _tmp_23 <= _tmp_22;
      end 
      if(_mystream_stream_oready) begin
        _tmp_24 <= _tmp_23;
      end 
      if(_tmp_18) begin
        _mystream_c_sink_mode <= 5'b1;
        _mystream_c_sink_offset <= _tmp_21;
        _mystream_c_sink_size <= _tmp_24;
        _mystream_c_sink_stride <= 1;
      end 
      if(_tmp_18) begin
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
        _tmp_26 <= _mystream_source_start;
      end 
      if(_mystream_stream_oready) begin
        _tmp_27 <= _tmp_26;
      end 
      if(_mystream_stream_oready) begin
        _tmp_28 <= _tmp_27;
      end 
      if(_mystream_stream_oready) begin
        _tmp_31 <= _tmp_30;
      end 
      if(_mystream_stream_oready) begin
        _tmp_32 <= _mystream_source_start;
      end 
      if(_mystream_stream_oready) begin
        _tmp_33 <= _tmp_32;
      end 
      if(_mystream_stream_oready) begin
        _tmp_34 <= _tmp_33;
      end 
      if(_mystream_stream_oready) begin
        _tmp_35 <= _mystream_source_stop;
      end 
      if(_mystream_stream_oready) begin
        _tmp_36 <= _tmp_35;
      end 
      if(_mystream_stream_oready) begin
        _tmp_37 <= _tmp_36;
      end 
      if(_mystream_stream_oready) begin
        _tmp_38 <= _mystream_source_busy;
      end 
      if(_mystream_stream_oready) begin
        _tmp_39 <= _tmp_38;
      end 
      if(_mystream_stream_oready) begin
        _tmp_40 <= _tmp_39;
      end 
      if(_mystream_stream_oready) begin
        _tmp_41 <= _mystream_sink_busy;
      end 
      if(!_mystream_sink_busy && _tmp_41) begin
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
      if(_mystream_stream_oready && _tmp_28) begin
        _mystream_stream_ivalid <= 1;
      end 
      if(_mystream_stream_oready && _tmp_31) begin
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
            th_comp <= th_comp_15;
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
          _th_comp_offset_1 <= _saxi_register_3;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          _th_comp_size_2 <= _th_comp_size_0;
          _th_comp_offset_3 <= _th_comp_offset_1;
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          if(_mystream_stream_oready) begin
            th_comp <= th_comp_10;
          end 
        end
        th_comp_10: begin
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          if(_mystream_busy) begin
            th_comp <= th_comp_12;
          end 
        end
        th_comp_12: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_13;
          end 
        end
        th_comp_13: begin
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          th_comp <= th_comp_1;
        end
        th_comp_15: begin
          $finish;
          th_comp <= th_comp_16;
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

    code = thread_stream_ram_external_ports.run(filename=None, simtype=simtype,
                                                outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
