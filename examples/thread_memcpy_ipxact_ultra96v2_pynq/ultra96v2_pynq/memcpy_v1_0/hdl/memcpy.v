

module memcpy
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
  input saxi_rready
);

  wire [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  wire [32-1:0] ram_a_0_wdata;
  wire ram_a_0_wenable;
  wire ram_a_0_enable;

  ram_a
  inst_ram_a
  (
    .CLK(CLK),
    .ram_a_0_addr(ram_a_0_addr),
    .ram_a_0_rdata(ram_a_0_rdata),
    .ram_a_0_wdata(ram_a_0_wdata),
    .ram_a_0_wenable(ram_a_0_wenable),
    .ram_a_0_enable(ram_a_0_enable)
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
  reg [3-1:0] outstanding_wcount_0;
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
  wire [8-1:0] unpack_read_req_op_sel_1;
  wire [32-1:0] unpack_read_req_local_addr_2;
  wire [32-1:0] unpack_read_req_local_stride_3;
  wire [33-1:0] unpack_read_req_local_size_4;
  wire [32-1:0] unpack_read_req_local_blocksize_5;
  assign unpack_read_req_op_sel_1 = _maxi_read_req_fifo_rdata[136:129];
  assign unpack_read_req_local_addr_2 = _maxi_read_req_fifo_rdata[128:97];
  assign unpack_read_req_local_stride_3 = _maxi_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_size_4 = _maxi_read_req_fifo_rdata[64:32];
  assign unpack_read_req_local_blocksize_5 = _maxi_read_req_fifo_rdata[31:0];
  assign _maxi_read_op_sel_fifo = unpack_read_req_op_sel_1;
  assign _maxi_read_local_addr_fifo = unpack_read_req_local_addr_2;
  assign _maxi_read_local_stride_fifo = unpack_read_req_local_stride_3;
  assign _maxi_read_local_size_fifo = unpack_read_req_local_size_4;
  assign _maxi_read_local_blocksize_fifo = unpack_read_req_local_blocksize_5;
  reg [8-1:0] _maxi_read_op_sel_buf;
  reg [32-1:0] _maxi_read_local_addr_buf;
  reg [32-1:0] _maxi_read_local_stride_buf;
  reg [33-1:0] _maxi_read_local_size_buf;
  reg [32-1:0] _maxi_read_local_blocksize_buf;
  reg _maxi_read_req_idle;
  reg _maxi_read_data_idle;
  wire _maxi_read_idle;
  assign _maxi_read_idle = !_maxi_read_start && _maxi_read_req_idle && _maxi_read_req_fifo_empty && _maxi_read_data_idle;
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
  wire [8-1:0] unpack_write_req_op_sel_6;
  wire [32-1:0] unpack_write_req_local_addr_7;
  wire [32-1:0] unpack_write_req_local_stride_8;
  wire [33-1:0] unpack_write_req_size_9;
  wire [32-1:0] unpack_write_req_local_blocksize_10;
  assign unpack_write_req_op_sel_6 = _maxi_write_req_fifo_rdata[136:129];
  assign unpack_write_req_local_addr_7 = _maxi_write_req_fifo_rdata[128:97];
  assign unpack_write_req_local_stride_8 = _maxi_write_req_fifo_rdata[96:65];
  assign unpack_write_req_size_9 = _maxi_write_req_fifo_rdata[64:32];
  assign unpack_write_req_local_blocksize_10 = _maxi_write_req_fifo_rdata[31:0];
  assign _maxi_write_op_sel_fifo = unpack_write_req_op_sel_6;
  assign _maxi_write_local_addr_fifo = unpack_write_req_local_addr_7;
  assign _maxi_write_local_stride_fifo = unpack_write_req_local_stride_8;
  assign _maxi_write_size_fifo = unpack_write_req_size_9;
  assign _maxi_write_local_blocksize_fifo = unpack_write_req_local_blocksize_10;
  reg [8-1:0] _maxi_write_op_sel_buf;
  reg [32-1:0] _maxi_write_local_addr_buf;
  reg [32-1:0] _maxi_write_local_stride_buf;
  reg [33-1:0] _maxi_write_size_buf;
  reg [32-1:0] _maxi_write_local_blocksize_buf;
  reg _maxi_write_req_idle;
  reg _maxi_write_data_idle;
  wire _maxi_write_idle;
  assign _maxi_write_idle = !_maxi_write_start && _maxi_write_req_idle && _maxi_write_req_fifo_empty && _maxi_write_data_idle;
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
  reg [32-1:0] addr_11;
  reg writevalid_12;
  reg readvalid_13;
  reg prev_awvalid_14;
  reg prev_arvalid_15;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_12 && !readvalid_13 && !saxi_bvalid && prev_awvalid_14);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_13 && !writevalid_12 && prev_arvalid_15 && !prev_awvalid_14);
  reg [_saxi_maskwidth-1:0] axis_maskaddr_16;
  wire signed [32-1:0] axislite_rdata_17;
  assign axislite_rdata_17 = (axis_maskaddr_16 == 0)? _saxi_register_0 : 
                             (axis_maskaddr_16 == 1)? _saxi_register_1 : 
                             (axis_maskaddr_16 == 2)? _saxi_register_2 : 
                             (axis_maskaddr_16 == 3)? _saxi_register_3 : 
                             (axis_maskaddr_16 == 4)? _saxi_register_4 : 
                             (axis_maskaddr_16 == 5)? _saxi_register_5 : 
                             (axis_maskaddr_16 == 6)? _saxi_register_6 : 
                             (axis_maskaddr_16 == 7)? _saxi_register_7 : 'hx;
  wire axislite_flag_18;
  assign axislite_flag_18 = (axis_maskaddr_16 == 0)? _saxi_flag_0 : 
                            (axis_maskaddr_16 == 1)? _saxi_flag_1 : 
                            (axis_maskaddr_16 == 2)? _saxi_flag_2 : 
                            (axis_maskaddr_16 == 3)? _saxi_flag_3 : 
                            (axis_maskaddr_16 == 4)? _saxi_flag_4 : 
                            (axis_maskaddr_16 == 5)? _saxi_flag_5 : 
                            (axis_maskaddr_16 == 6)? _saxi_flag_6 : 
                            (axis_maskaddr_16 == 7)? _saxi_flag_7 : 'hx;
  wire signed [32-1:0] axislite_resetval_19;
  assign axislite_resetval_19 = (axis_maskaddr_16 == 0)? _saxi_resetval_0 : 
                                (axis_maskaddr_16 == 1)? _saxi_resetval_1 : 
                                (axis_maskaddr_16 == 2)? _saxi_resetval_2 : 
                                (axis_maskaddr_16 == 3)? _saxi_resetval_3 : 
                                (axis_maskaddr_16 == 4)? _saxi_resetval_4 : 
                                (axis_maskaddr_16 == 5)? _saxi_resetval_5 : 
                                (axis_maskaddr_16 == 6)? _saxi_resetval_6 : 
                                (axis_maskaddr_16 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg [32-1:0] th_memcpy;
  localparam th_memcpy_init = 0;
  reg signed [32-1:0] _th_memcpy_copy_bytes_20;
  reg signed [32-1:0] _th_memcpy_src_offset_21;
  reg signed [32-1:0] _th_memcpy_dst_offset_22;
  reg signed [32-1:0] _th_memcpy_copy_bytes_23;
  reg signed [32-1:0] _th_memcpy_src_offset_24;
  reg signed [32-1:0] _th_memcpy_dst_offset_25;
  reg signed [32-1:0] _th_memcpy_rest_words_26;
  reg signed [32-1:0] _th_memcpy_src_global_addr_27;
  reg signed [32-1:0] _th_memcpy_dst_global_addr_28;
  reg signed [32-1:0] _th_memcpy_local_addr_29;
  reg signed [32-1:0] _th_memcpy_dma_size_30;
  wire [32-1:0] mask_addr_shifted_20;
  assign mask_addr_shifted_20 = _th_memcpy_src_global_addr_27 >> 2;
  wire [32-1:0] mask_addr_masked_21;
  assign mask_addr_masked_21 = mask_addr_shifted_20 << 2;
  reg [32-1:0] _maxi_read_req_fsm;
  localparam _maxi_read_req_fsm_init = 0;
  reg [33-1:0] _maxi_read_cur_global_size;
  reg _maxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_22;
  wire [32-1:0] pack_read_req_local_addr_23;
  wire [32-1:0] pack_read_req_local_stride_24;
  wire [33-1:0] pack_read_req_local_size_25;
  wire [32-1:0] pack_read_req_local_blocksize_26;
  assign pack_read_req_op_sel_22 = _maxi_read_op_sel;
  assign pack_read_req_local_addr_23 = _maxi_read_local_addr;
  assign pack_read_req_local_stride_24 = _maxi_read_local_stride;
  assign pack_read_req_local_size_25 = _maxi_read_local_size;
  assign pack_read_req_local_blocksize_26 = _maxi_read_local_blocksize;
  wire [137-1:0] pack_read_req_packed_27;
  assign pack_read_req_packed_27 = { pack_read_req_op_sel_22, pack_read_req_local_addr_23, pack_read_req_local_stride_24, pack_read_req_local_size_25, pack_read_req_local_blocksize_26 };
  assign _maxi_read_req_fifo_wdata = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? pack_read_req_packed_27 : 'hx;
  assign _maxi_read_req_fifo_enq = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? (_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full && !_maxi_read_req_fifo_almost_full : 0;
  localparam _tmp_28 = 1;
  wire [_tmp_28-1:0] _tmp_29;
  assign _tmp_29 = !_maxi_read_req_fifo_almost_full;
  reg [_tmp_28-1:0] __tmp_29_1;
  wire [32-1:0] mask_addr_shifted_30;
  assign mask_addr_shifted_30 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_31;
  assign mask_addr_masked_31 = mask_addr_shifted_30 << 2;
  wire [32-1:0] mask_addr_shifted_32;
  assign mask_addr_shifted_32 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_33;
  assign mask_addr_masked_33 = mask_addr_shifted_32 << 2;
  wire [32-1:0] mask_addr_shifted_34;
  assign mask_addr_shifted_34 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_35;
  assign mask_addr_masked_35 = mask_addr_shifted_34 << 2;
  wire [32-1:0] mask_addr_shifted_36;
  assign mask_addr_shifted_36 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_37;
  assign mask_addr_masked_37 = mask_addr_shifted_36 << 2;
  wire [32-1:0] mask_addr_shifted_38;
  assign mask_addr_shifted_38 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_39;
  assign mask_addr_masked_39 = mask_addr_shifted_38 << 2;
  wire [32-1:0] mask_addr_shifted_40;
  assign mask_addr_shifted_40 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_41;
  assign mask_addr_masked_41 = mask_addr_shifted_40 << 2;
  reg _maxi_cond_0_1;
  reg [32-1:0] _maxi_read_data_fsm;
  localparam _maxi_read_data_fsm_init = 0;
  assign _maxi_read_req_fifo_deq = ((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) && !_maxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_2;
  localparam write_burst_fsm_2_init = 0;
  reg [10-1:0] write_burst_addr_42;
  reg [10-1:0] write_burst_stride_43;
  reg [33-1:0] write_burst_length_44;
  reg write_burst_done_45;
  assign ram_a_0_wdata = ((write_burst_fsm_2 == 1) && maxi_rvalid)? maxi_rdata : 'hx;
  assign ram_a_0_wenable = ((write_burst_fsm_2 == 1) && maxi_rvalid)? 1'd1 : 0;
  assign maxi_rready = _maxi_read_data_fsm == 2;
  wire [32-1:0] mask_addr_shifted_46;
  assign mask_addr_shifted_46 = _th_memcpy_dst_global_addr_28 >> 2;
  wire [32-1:0] mask_addr_masked_47;
  assign mask_addr_masked_47 = mask_addr_shifted_46 << 2;
  reg [32-1:0] _maxi_write_req_fsm;
  localparam _maxi_write_req_fsm_init = 0;
  reg [33-1:0] _maxi_write_cur_global_size;
  reg _maxi_write_cont;
  wire [8-1:0] pack_write_req_op_sel_48;
  wire [32-1:0] pack_write_req_local_addr_49;
  wire [32-1:0] pack_write_req_local_stride_50;
  wire [33-1:0] pack_write_req_size_51;
  wire [32-1:0] pack_write_req_local_blocksize_52;
  assign pack_write_req_op_sel_48 = _maxi_write_op_sel;
  assign pack_write_req_local_addr_49 = _maxi_write_local_addr;
  assign pack_write_req_local_stride_50 = _maxi_write_local_stride;
  assign pack_write_req_size_51 = _maxi_write_local_size;
  assign pack_write_req_local_blocksize_52 = _maxi_write_local_blocksize;
  wire [137-1:0] pack_write_req_packed_53;
  assign pack_write_req_packed_53 = { pack_write_req_op_sel_48, pack_write_req_local_addr_49, pack_write_req_local_stride_50, pack_write_req_size_51, pack_write_req_local_blocksize_52 };
  localparam _tmp_54 = 1;
  wire [_tmp_54-1:0] _tmp_55;
  assign _tmp_55 = !_maxi_write_req_fifo_almost_full;
  reg [_tmp_54-1:0] __tmp_55_1;
  wire [32-1:0] mask_addr_shifted_56;
  assign mask_addr_shifted_56 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_57;
  assign mask_addr_masked_57 = mask_addr_shifted_56 << 2;
  wire [32-1:0] mask_addr_shifted_58;
  assign mask_addr_shifted_58 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_59;
  assign mask_addr_masked_59 = mask_addr_shifted_58 << 2;
  wire [32-1:0] mask_addr_shifted_60;
  assign mask_addr_shifted_60 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_61;
  assign mask_addr_masked_61 = mask_addr_shifted_60 << 2;
  wire [32-1:0] mask_addr_shifted_62;
  assign mask_addr_shifted_62 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_63;
  assign mask_addr_masked_63 = mask_addr_shifted_62 << 2;
  wire [32-1:0] mask_addr_shifted_64;
  assign mask_addr_shifted_64 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_65;
  assign mask_addr_masked_65 = mask_addr_shifted_64 << 2;
  wire [32-1:0] mask_addr_shifted_66;
  assign mask_addr_shifted_66 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_67;
  assign mask_addr_masked_67 = mask_addr_shifted_66 << 2;
  wire [8-1:0] pack_write_req_op_sel_68;
  wire [32-1:0] pack_write_req_local_addr_69;
  wire [32-1:0] pack_write_req_local_stride_70;
  wire [33-1:0] pack_write_req_size_71;
  wire [32-1:0] pack_write_req_local_blocksize_72;
  assign pack_write_req_op_sel_68 = _maxi_write_op_sel;
  assign pack_write_req_local_addr_69 = _maxi_write_local_addr;
  assign pack_write_req_local_stride_70 = _maxi_write_local_stride;
  assign pack_write_req_size_71 = _maxi_write_cur_global_size;
  assign pack_write_req_local_blocksize_72 = _maxi_write_local_blocksize;
  wire [137-1:0] pack_write_req_packed_73;
  assign pack_write_req_packed_73 = { pack_write_req_op_sel_68, pack_write_req_local_addr_69, pack_write_req_local_stride_70, pack_write_req_size_71, pack_write_req_local_blocksize_72 };
  assign _maxi_write_req_fifo_wdata = ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6))? pack_write_req_packed_73 : 
                                      ((_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full)? pack_write_req_packed_53 : 'hx;
  assign _maxi_write_req_fifo_enq = ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6))? (_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6) && !_maxi_write_req_fifo_almost_full : 
                                    ((_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full)? (_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full && !_maxi_write_req_fifo_almost_full : 0;
  localparam _tmp_74 = 1;
  wire [_tmp_74-1:0] _tmp_75;
  assign _tmp_75 = !_maxi_write_req_fifo_almost_full;
  reg [_tmp_74-1:0] __tmp_75_1;
  reg _maxi_cond_1_1;
  reg [32-1:0] _maxi_write_data_fsm;
  localparam _maxi_write_data_fsm_init = 0;
  reg [32-1:0] read_burst_fsm_3;
  localparam read_burst_fsm_3_init = 0;
  reg [10-1:0] read_burst_addr_76;
  reg [10-1:0] read_burst_stride_77;
  reg [33-1:0] read_burst_length_78;
  reg read_burst_rvalid_79;
  reg read_burst_rlast_80;
  assign ram_a_0_addr = ((read_burst_fsm_3 == 1) && (!read_burst_rvalid_79 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)))? read_burst_addr_76 : 
                        ((write_burst_fsm_2 == 1) && maxi_rvalid)? write_burst_addr_42 : 'hx;
  assign ram_a_0_enable = ((read_burst_fsm_3 == 1) && (!read_burst_rvalid_79 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)))? 1'd1 : 
                          ((write_burst_fsm_2 == 1) && maxi_rvalid)? 1'd1 : 0;
  localparam _tmp_81 = 1;
  wire [_tmp_81-1:0] _tmp_82;
  assign _tmp_82 = (read_burst_fsm_3 == 1) && (!read_burst_rvalid_79 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0));
  reg [_tmp_81-1:0] __tmp_82_1;
  wire [32-1:0] read_burst_rdata_83;
  assign read_burst_rdata_83 = ram_a_0_rdata;
  assign _maxi_write_req_fifo_deq = ((_maxi_write_data_fsm == 2) && (!_maxi_write_req_fifo_empty && (_maxi_write_size_buf == 0)) && !_maxi_write_req_fifo_empty)? 1 : 
                                    ((_maxi_write_data_fsm == 0) && (_maxi_write_data_idle && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1)) && !_maxi_write_req_fifo_empty)? 1 : 0;
  reg _maxi_cond_2_1;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_82_1 <= 0;
    end else begin
      __tmp_82_1 <= _tmp_82;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wcount_0 <= 0;
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      _maxi_read_op_sel <= 0;
      _maxi_read_global_addr <= 0;
      _maxi_read_global_size <= 0;
      _maxi_read_local_addr <= 0;
      _maxi_read_local_stride <= 0;
      _maxi_read_local_size <= 0;
      _maxi_read_local_blocksize <= 0;
      _maxi_read_req_idle <= 1;
      _maxi_read_cur_global_size <= 0;
      maxi_araddr <= 0;
      maxi_arlen <= 0;
      maxi_arvalid <= 0;
      _maxi_cond_0_1 <= 0;
      _maxi_read_data_idle <= 1;
      _maxi_read_op_sel_buf <= 0;
      _maxi_read_local_addr_buf <= 0;
      _maxi_read_local_stride_buf <= 0;
      _maxi_read_local_size_buf <= 0;
      _maxi_read_local_blocksize_buf <= 0;
      _maxi_write_op_sel <= 0;
      _maxi_write_global_addr <= 0;
      _maxi_write_global_size <= 0;
      _maxi_write_local_addr <= 0;
      _maxi_write_local_stride <= 0;
      _maxi_write_local_size <= 0;
      _maxi_write_local_blocksize <= 0;
      _maxi_write_req_idle <= 1;
      _maxi_write_cur_global_size <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      _maxi_cond_1_1 <= 0;
      _maxi_write_data_idle <= 1;
      _maxi_write_op_sel_buf <= 0;
      _maxi_write_local_addr_buf <= 0;
      _maxi_write_local_stride_buf <= 0;
      _maxi_write_size_buf <= 0;
      _maxi_write_local_blocksize_buf <= 0;
      maxi_wdata <= 0;
      maxi_wvalid <= 0;
      maxi_wlast <= 0;
      maxi_wstrb <= 0;
      _maxi_cond_2_1 <= 0;
    end else begin
      if(_maxi_cond_0_1) begin
        maxi_arvalid <= 0;
      end 
      if(_maxi_cond_1_1) begin
        maxi_awvalid <= 0;
      end 
      if(_maxi_cond_2_1) begin
        maxi_wvalid <= 0;
        maxi_wlast <= 0;
      end 
      if(maxi_awvalid && maxi_awready && !(maxi_bvalid && maxi_bready) && (outstanding_wcount_0 < 7)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 + 1;
      end 
      if(!(maxi_awvalid && maxi_awready) && (maxi_bvalid && maxi_bready) && (outstanding_wcount_0 > 0)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 - 1;
      end 
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      if((th_memcpy == 17) && _maxi_read_req_idle) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= 1;
        _maxi_read_global_addr <= mask_addr_masked_21;
        _maxi_read_global_size <= _th_memcpy_dma_size_30;
        _maxi_read_local_addr <= _th_memcpy_local_addr_29;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_memcpy_dma_size_30;
        _maxi_read_local_blocksize <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && _maxi_read_start) begin
        _maxi_read_req_idle <= 0;
      end 
      if(_maxi_read_start && _maxi_read_req_fifo_almost_full) begin
        _maxi_read_start <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256) && ((mask_addr_masked_31 & 4095) + (_maxi_read_global_size << 2) >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_33 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_35 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256)) begin
        _maxi_read_cur_global_size <= _maxi_read_global_size;
        _maxi_read_global_size <= 0;
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && ((mask_addr_masked_37 & 4095) + 1024 >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_39 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_41 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full) begin
        _maxi_read_cur_global_size <= 256;
        _maxi_read_global_size <= _maxi_read_global_size - 256;
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid)) begin
        maxi_araddr <= _maxi_read_global_addr;
        maxi_arlen <= _maxi_read_cur_global_size - 1;
        maxi_arvalid <= 1;
      end 
      _maxi_cond_0_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid)) begin
        _maxi_read_global_addr <= _maxi_read_global_addr + (_maxi_read_cur_global_size << 2);
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid) && (_maxi_read_global_size == 0)) begin
        _maxi_read_req_idle <= 1;
      end 
      if((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1))) begin
        _maxi_read_data_idle <= 0;
        _maxi_read_op_sel_buf <= _maxi_read_op_sel_fifo;
        _maxi_read_local_addr_buf <= _maxi_read_local_addr_fifo;
        _maxi_read_local_stride_buf <= _maxi_read_local_stride_fifo;
        _maxi_read_local_size_buf <= _maxi_read_local_size_fifo;
        _maxi_read_local_blocksize_buf <= _maxi_read_local_blocksize_fifo;
      end 
      if((_maxi_read_data_fsm == 2) && maxi_rvalid) begin
        _maxi_read_local_size_buf <= _maxi_read_local_size_buf - 1;
      end 
      if((_maxi_read_data_fsm == 2) && maxi_rvalid && (_maxi_read_local_size_buf <= 1)) begin
        _maxi_read_data_idle <= 1;
      end 
      if((th_memcpy == 19) && _maxi_write_req_idle) begin
        _maxi_write_start <= 1;
        _maxi_write_op_sel <= 1;
        _maxi_write_global_addr <= mask_addr_masked_47;
        _maxi_write_global_size <= _th_memcpy_dma_size_30;
        _maxi_write_local_addr <= _th_memcpy_local_addr_29;
        _maxi_write_local_stride <= 1;
        _maxi_write_local_size <= _th_memcpy_dma_size_30;
        _maxi_write_local_blocksize <= 1;
      end 
      if((_maxi_write_req_fsm == 0) && _maxi_write_start) begin
        _maxi_write_req_idle <= 0;
      end 
      if(_maxi_write_start && _maxi_write_req_fifo_almost_full) begin
        _maxi_write_start <= 1;
      end 
      if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && (_maxi_write_global_size <= 256) && ((mask_addr_masked_57 & 4095) + (_maxi_write_global_size << 2) >= 4096)) begin
        _maxi_write_cur_global_size <= 4096 - (mask_addr_masked_59 & 4095) >> 2;
        _maxi_write_global_size <= _maxi_write_global_size - (4096 - (mask_addr_masked_61 & 4095) >> 2);
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && (_maxi_write_global_size <= 256)) begin
        _maxi_write_cur_global_size <= _maxi_write_global_size;
        _maxi_write_global_size <= 0;
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && ((mask_addr_masked_63 & 4095) + 1024 >= 4096)) begin
        _maxi_write_cur_global_size <= 4096 - (mask_addr_masked_65 & 4095) >> 2;
        _maxi_write_global_size <= _maxi_write_global_size - (4096 - (mask_addr_masked_67 & 4095) >> 2);
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full) begin
        _maxi_write_cur_global_size <= 256;
        _maxi_write_global_size <= _maxi_write_global_size - 256;
      end 
      if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (outstanding_wcount_0 < 6) && ((outstanding_wcount_0 < 6) && (maxi_awready || !maxi_awvalid))) begin
        maxi_awaddr <= _maxi_write_global_addr;
        maxi_awlen <= _maxi_write_cur_global_size - 1;
        maxi_awvalid <= 1;
      end 
      if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (outstanding_wcount_0 < 6) && ((outstanding_wcount_0 < 6) && (maxi_awready || !maxi_awvalid)) && (_maxi_write_cur_global_size == 0)) begin
        maxi_awvalid <= 0;
      end 
      _maxi_cond_1_1 <= 1;
      if(maxi_awvalid && !maxi_awready) begin
        maxi_awvalid <= maxi_awvalid;
      end 
      if((_maxi_write_req_fsm == 1) && ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6))) begin
        _maxi_write_global_addr <= _maxi_write_global_addr + (_maxi_write_cur_global_size << 2);
      end 
      if((_maxi_write_req_fsm == 1) && ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6)) && (_maxi_write_global_size == 0)) begin
        _maxi_write_req_idle <= 1;
      end 
      if((_maxi_write_data_fsm == 0) && (_maxi_write_data_idle && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1))) begin
        _maxi_write_data_idle <= 0;
        _maxi_write_op_sel_buf <= _maxi_write_op_sel_fifo;
        _maxi_write_local_addr_buf <= _maxi_write_local_addr_fifo;
        _maxi_write_local_stride_buf <= _maxi_write_local_stride_fifo;
        _maxi_write_size_buf <= _maxi_write_size_fifo;
        _maxi_write_local_blocksize_buf <= _maxi_write_local_blocksize_fifo;
      end 
      if(_maxi_write_data_fsm == 1) begin
        _maxi_write_size_buf <= 0;
      end 
      if((_maxi_write_data_fsm == 2) && (!_maxi_write_req_fifo_empty && (_maxi_write_size_buf == 0))) begin
        _maxi_write_size_buf <= _maxi_write_size_fifo;
      end 
      if((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_79 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)) && (maxi_wready || !maxi_wvalid)) begin
        maxi_wdata <= read_burst_rdata_83;
        maxi_wvalid <= 1;
        maxi_wlast <= read_burst_rlast_80 || (_maxi_write_size_buf == 1);
        maxi_wstrb <= { 4{ 1'd1 } };
      end 
      _maxi_cond_2_1 <= 1;
      if(maxi_wvalid && !maxi_wready) begin
        maxi_wvalid <= maxi_wvalid;
        maxi_wlast <= maxi_wlast;
      end 
      if((_maxi_write_data_fsm == 2) && read_burst_rvalid_79 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) begin
        _maxi_write_size_buf <= _maxi_write_size_buf - 1;
      end 
      if((_maxi_write_data_fsm == 2) && ((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_79 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) && read_burst_rlast_80) begin
        _maxi_write_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_read_req_fifo <= 0;
      __tmp_29_1 <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full && (_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty)) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo;
      end else if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo + 1;
      end else if(_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo - 1;
      end 
      __tmp_29_1 <= _tmp_29;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_write_req_fifo <= 0;
      __tmp_55_1 <= 0;
      __tmp_75_1 <= 0;
    end else begin
      if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full && (_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty)) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo;
      end else if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo + 1;
      end else if(_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo - 1;
      end 
      __tmp_55_1 <= _tmp_55;
      __tmp_75_1 <= _tmp_75;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_14 <= 0;
      prev_arvalid_15 <= 0;
      writevalid_12 <= 0;
      readvalid_13 <= 0;
      addr_11 <= 0;
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
      prev_awvalid_14 <= saxi_awvalid;
      prev_arvalid_15 <= saxi_arvalid;
      writevalid_12 <= 0;
      readvalid_13 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_11 <= saxi_awaddr;
        writevalid_12 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_11 <= saxi_araddr;
        readvalid_13 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_17;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 0)) begin
        _saxi_register_0 <= axislite_resetval_19;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 1)) begin
        _saxi_register_1 <= axislite_resetval_19;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 2)) begin
        _saxi_register_2 <= axislite_resetval_19;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 3)) begin
        _saxi_register_3 <= axislite_resetval_19;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 4)) begin
        _saxi_register_4 <= axislite_resetval_19;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 5)) begin
        _saxi_register_5 <= axislite_resetval_19;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 6)) begin
        _saxi_register_6 <= axislite_resetval_19;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_18 && (axis_maskaddr_16 == 7)) begin
        _saxi_register_7 <= axislite_resetval_19;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_16 == 7)) begin
        _saxi_register_7 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_4 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_5 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_6 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_7 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 0;
      end 
      if((th_memcpy == 3) && 1) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_4 <= 1;
        _saxi_flag_4 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_5 <= 1;
        _saxi_flag_5 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_6 <= 1;
        _saxi_flag_6 <= 0;
      end 
      if((th_memcpy == 3) && 0) begin
        _saxi_register_7 <= 1;
        _saxi_flag_7 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_memcpy == 25) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
        _saxi_register_4 <= 0;
        _saxi_flag_4 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
        _saxi_register_5 <= 0;
        _saxi_flag_5 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
        _saxi_register_6 <= 0;
        _saxi_flag_6 <= 0;
      end 
      if((th_memcpy == 25) && 0) begin
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
      axis_maskaddr_16 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_13 || writevalid_12) begin
            axis_maskaddr_16 <= (addr_11 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_13) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_12) begin
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

  localparam th_memcpy_1 = 1;
  localparam th_memcpy_2 = 2;
  localparam th_memcpy_3 = 3;
  localparam th_memcpy_4 = 4;
  localparam th_memcpy_5 = 5;
  localparam th_memcpy_6 = 6;
  localparam th_memcpy_7 = 7;
  localparam th_memcpy_8 = 8;
  localparam th_memcpy_9 = 9;
  localparam th_memcpy_10 = 10;
  localparam th_memcpy_11 = 11;
  localparam th_memcpy_12 = 12;
  localparam th_memcpy_13 = 13;
  localparam th_memcpy_14 = 14;
  localparam th_memcpy_15 = 15;
  localparam th_memcpy_16 = 16;
  localparam th_memcpy_17 = 17;
  localparam th_memcpy_18 = 18;
  localparam th_memcpy_19 = 19;
  localparam th_memcpy_20 = 20;
  localparam th_memcpy_21 = 21;
  localparam th_memcpy_22 = 22;
  localparam th_memcpy_23 = 23;
  localparam th_memcpy_24 = 24;
  localparam th_memcpy_25 = 25;
  localparam th_memcpy_26 = 26;
  localparam th_memcpy_27 = 27;

  always @(posedge CLK) begin
    if(RST) begin
      th_memcpy <= th_memcpy_init;
      _th_memcpy_copy_bytes_20 <= 0;
      _th_memcpy_src_offset_21 <= 0;
      _th_memcpy_dst_offset_22 <= 0;
      _th_memcpy_copy_bytes_23 <= 0;
      _th_memcpy_src_offset_24 <= 0;
      _th_memcpy_dst_offset_25 <= 0;
      _th_memcpy_rest_words_26 <= 0;
      _th_memcpy_src_global_addr_27 <= 0;
      _th_memcpy_dst_global_addr_28 <= 0;
      _th_memcpy_local_addr_29 <= 0;
      _th_memcpy_dma_size_30 <= 0;
    end else begin
      case(th_memcpy)
        th_memcpy_init: begin
          th_memcpy <= th_memcpy_1;
        end
        th_memcpy_1: begin
          if(1) begin
            th_memcpy <= th_memcpy_2;
          end else begin
            th_memcpy <= th_memcpy_27;
          end
        end
        th_memcpy_2: begin
          if(_saxi_register_0 == 1) begin
            th_memcpy <= th_memcpy_3;
          end 
        end
        th_memcpy_3: begin
          th_memcpy <= th_memcpy_4;
        end
        th_memcpy_4: begin
          _th_memcpy_copy_bytes_20 <= _saxi_register_2;
          th_memcpy <= th_memcpy_5;
        end
        th_memcpy_5: begin
          _th_memcpy_src_offset_21 <= _saxi_register_3;
          th_memcpy <= th_memcpy_6;
        end
        th_memcpy_6: begin
          _th_memcpy_dst_offset_22 <= _saxi_register_4;
          th_memcpy <= th_memcpy_7;
        end
        th_memcpy_7: begin
          _th_memcpy_copy_bytes_23 <= _th_memcpy_copy_bytes_20;
          _th_memcpy_src_offset_24 <= _th_memcpy_src_offset_21;
          _th_memcpy_dst_offset_25 <= _th_memcpy_dst_offset_22;
          th_memcpy <= th_memcpy_8;
        end
        th_memcpy_8: begin
          _th_memcpy_rest_words_26 <= _th_memcpy_copy_bytes_23 >>> 2;
          th_memcpy <= th_memcpy_9;
        end
        th_memcpy_9: begin
          _th_memcpy_src_global_addr_27 <= _th_memcpy_src_offset_24;
          th_memcpy <= th_memcpy_10;
        end
        th_memcpy_10: begin
          _th_memcpy_dst_global_addr_28 <= _th_memcpy_dst_offset_25;
          th_memcpy <= th_memcpy_11;
        end
        th_memcpy_11: begin
          _th_memcpy_local_addr_29 <= 0;
          th_memcpy <= th_memcpy_12;
        end
        th_memcpy_12: begin
          if(_th_memcpy_rest_words_26 > 0) begin
            th_memcpy <= th_memcpy_13;
          end else begin
            th_memcpy <= th_memcpy_25;
          end
        end
        th_memcpy_13: begin
          if(_th_memcpy_rest_words_26 > 256) begin
            th_memcpy <= th_memcpy_14;
          end else begin
            th_memcpy <= th_memcpy_16;
          end
        end
        th_memcpy_14: begin
          _th_memcpy_dma_size_30 <= 256;
          th_memcpy <= th_memcpy_15;
        end
        th_memcpy_15: begin
          th_memcpy <= th_memcpy_17;
        end
        th_memcpy_16: begin
          _th_memcpy_dma_size_30 <= _th_memcpy_rest_words_26;
          th_memcpy <= th_memcpy_17;
        end
        th_memcpy_17: begin
          if(_maxi_read_req_idle) begin
            th_memcpy <= th_memcpy_18;
          end 
        end
        th_memcpy_18: begin
          if(_maxi_read_idle) begin
            th_memcpy <= th_memcpy_19;
          end 
        end
        th_memcpy_19: begin
          if(_maxi_write_req_idle) begin
            th_memcpy <= th_memcpy_20;
          end 
        end
        th_memcpy_20: begin
          if(_maxi_write_idle && (outstanding_wcount_0 == 0)) begin
            th_memcpy <= th_memcpy_21;
          end 
        end
        th_memcpy_21: begin
          _th_memcpy_src_global_addr_27 <= _th_memcpy_src_global_addr_27 + (_th_memcpy_dma_size_30 << 2);
          th_memcpy <= th_memcpy_22;
        end
        th_memcpy_22: begin
          _th_memcpy_dst_global_addr_28 <= _th_memcpy_dst_global_addr_28 + (_th_memcpy_dma_size_30 << 2);
          th_memcpy <= th_memcpy_23;
        end
        th_memcpy_23: begin
          _th_memcpy_rest_words_26 <= _th_memcpy_rest_words_26 - _th_memcpy_dma_size_30;
          th_memcpy <= th_memcpy_24;
        end
        th_memcpy_24: begin
          th_memcpy <= th_memcpy_12;
        end
        th_memcpy_25: begin
          th_memcpy <= th_memcpy_26;
        end
        th_memcpy_26: begin
          th_memcpy <= th_memcpy_1;
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
          if(_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_1;
          end 
        end
        _maxi_read_data_fsm_1: begin
          _maxi_read_data_fsm <= _maxi_read_data_fsm_2;
        end
        _maxi_read_data_fsm_2: begin
          if(maxi_rvalid && (_maxi_read_local_size_buf <= 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_2_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_2 <= write_burst_fsm_2_init;
      write_burst_addr_42 <= 0;
      write_burst_stride_43 <= 0;
      write_burst_length_44 <= 0;
      write_burst_done_45 <= 0;
    end else begin
      case(write_burst_fsm_2)
        write_burst_fsm_2_init: begin
          write_burst_addr_42 <= _maxi_read_local_addr_buf;
          write_burst_stride_43 <= _maxi_read_local_stride_buf;
          write_burst_length_44 <= _maxi_read_local_size_buf;
          write_burst_done_45 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 1) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_2 <= write_burst_fsm_2_1;
          end 
        end
        write_burst_fsm_2_1: begin
          if(maxi_rvalid) begin
            write_burst_addr_42 <= write_burst_addr_42 + write_burst_stride_43;
            write_burst_length_44 <= write_burst_length_44 - 1;
            write_burst_done_45 <= 0;
          end 
          if(maxi_rvalid && (write_burst_length_44 <= 1)) begin
            write_burst_done_45 <= 1;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_done_45 <= 1;
          end 
          if(maxi_rvalid && (write_burst_length_44 <= 1)) begin
            write_burst_fsm_2 <= write_burst_fsm_2_init;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_fsm_2 <= write_burst_fsm_2_init;
          end 
          if(0) begin
            write_burst_fsm_2 <= write_burst_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _maxi_write_req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_write_req_fsm <= _maxi_write_req_fsm_init;
      _maxi_write_cont <= 0;
    end else begin
      case(_maxi_write_req_fsm)
        _maxi_write_req_fsm_init: begin
          if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full) begin
            _maxi_write_req_fsm <= _maxi_write_req_fsm_1;
          end 
        end
        _maxi_write_req_fsm_1: begin
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6)) begin
            _maxi_write_cont <= 1;
          end 
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6) && (_maxi_write_global_size == 0)) begin
            _maxi_write_cont <= 0;
          end 
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6)) begin
            _maxi_write_req_fsm <= _maxi_write_req_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _maxi_write_data_fsm_1 = 1;
  localparam _maxi_write_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_write_data_fsm <= _maxi_write_data_fsm_init;
    end else begin
      case(_maxi_write_data_fsm)
        _maxi_write_data_fsm_init: begin
          if(_maxi_write_data_idle && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1)) begin
            _maxi_write_data_fsm <= _maxi_write_data_fsm_1;
          end 
        end
        _maxi_write_data_fsm_1: begin
          _maxi_write_data_fsm <= _maxi_write_data_fsm_2;
        end
        _maxi_write_data_fsm_2: begin
          if((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_79 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)) && read_burst_rlast_80) begin
            _maxi_write_data_fsm <= _maxi_write_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam read_burst_fsm_3_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      read_burst_fsm_3 <= read_burst_fsm_3_init;
      read_burst_addr_76 <= 0;
      read_burst_stride_77 <= 0;
      read_burst_length_78 <= 0;
      read_burst_rvalid_79 <= 0;
      read_burst_rlast_80 <= 0;
    end else begin
      case(read_burst_fsm_3)
        read_burst_fsm_3_init: begin
          read_burst_addr_76 <= _maxi_write_local_addr_buf;
          read_burst_stride_77 <= _maxi_write_local_stride_buf;
          read_burst_length_78 <= _maxi_write_size_buf;
          read_burst_rvalid_79 <= 0;
          read_burst_rlast_80 <= 0;
          if((_maxi_write_data_fsm == 1) && (_maxi_write_op_sel_buf == 1) && (_maxi_write_size_buf > 0)) begin
            read_burst_fsm_3 <= read_burst_fsm_3_1;
          end 
        end
        read_burst_fsm_3_1: begin
          if((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0) && (read_burst_length_78 > 0)) begin
            read_burst_addr_76 <= read_burst_addr_76 + read_burst_stride_77;
            read_burst_length_78 <= read_burst_length_78 - 1;
            read_burst_rvalid_79 <= 1;
          end 
          if((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0) && (read_burst_length_78 <= 1)) begin
            read_burst_rlast_80 <= 1;
          end 
          if(read_burst_rlast_80 && read_burst_rvalid_79 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) begin
            read_burst_rvalid_79 <= 0;
            read_burst_rlast_80 <= 0;
          end 
          if(0) begin
            read_burst_rvalid_79 <= 0;
            read_burst_rlast_80 <= 0;
          end 
          if(read_burst_rlast_80 && read_burst_rvalid_79 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) begin
            read_burst_fsm_3 <= read_burst_fsm_3_init;
          end 
          if(0) begin
            read_burst_fsm_3 <= read_burst_fsm_3_init;
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
  input ram_a_0_enable
);

  reg [32-1:0] ram_a_0_rdata_out;
  assign ram_a_0_rdata = ram_a_0_rdata_out;
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

