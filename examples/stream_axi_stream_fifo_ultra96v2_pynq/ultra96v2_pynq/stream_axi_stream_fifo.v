

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
  wire [8-1:0] unpack_read_req_op_sel_20;
  wire [33-1:0] unpack_read_req_local_size_21;
  assign unpack_read_req_op_sel_20 = _axi_in_read_req_fifo_rdata[40:33];
  assign unpack_read_req_local_size_21 = _axi_in_read_req_fifo_rdata[32:0];
  assign _axi_in_read_op_sel_fifo = unpack_read_req_op_sel_20;
  assign _axi_in_read_local_size_fifo = unpack_read_req_local_size_21;
  reg [8-1:0] _axi_in_read_op_sel_buf;
  reg [33-1:0] _axi_in_read_local_size_buf;
  reg _axi_in_read_data_idle;
  wire _axi_in_read_idle;
  assign _axi_in_read_idle = _axi_in_read_req_fifo_empty && _axi_in_read_data_idle;
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
  wire [8-1:0] unpack_write_req_op_sel_22;
  wire [33-1:0] unpack_write_req_local_size_23;
  assign unpack_write_req_op_sel_22 = _axi_out_write_req_fifo_rdata[40:33];
  assign unpack_write_req_local_size_23 = _axi_out_write_req_fifo_rdata[32:0];
  assign _axi_out_write_op_sel_fifo = unpack_write_req_op_sel_22;
  assign _axi_out_write_size_fifo = unpack_write_req_local_size_23;
  reg [8-1:0] _axi_out_write_op_sel_buf;
  reg [33-1:0] _axi_out_write_size_buf;
  reg _axi_out_write_data_idle;
  wire _axi_out_write_idle;
  assign _axi_out_write_idle = _axi_out_write_req_fifo_empty && _axi_out_write_data_idle;
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
  wire [32-1:0] mask_addr_shifted_24;
  assign mask_addr_shifted_24 = _th_comp_bias_addr_3 >> 2;
  wire [32-1:0] mask_addr_masked_25;
  assign mask_addr_masked_25 = mask_addr_shifted_24 << 2;
  reg [32-1:0] _maxi_read_req_fsm;
  localparam _maxi_read_req_fsm_init = 0;
  reg [33-1:0] _maxi_read_cur_global_size;
  reg _maxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_26;
  wire [32-1:0] pack_read_req_local_addr_27;
  wire [32-1:0] pack_read_req_local_stride_28;
  wire [33-1:0] pack_read_req_local_size_29;
  wire [32-1:0] pack_read_req_local_blocksize_30;
  assign pack_read_req_op_sel_26 = _maxi_read_op_sel;
  assign pack_read_req_local_addr_27 = _maxi_read_local_addr;
  assign pack_read_req_local_stride_28 = _maxi_read_local_stride;
  assign pack_read_req_local_size_29 = _maxi_read_local_size;
  assign pack_read_req_local_blocksize_30 = _maxi_read_local_blocksize;
  wire [137-1:0] pack_read_req_packed_31;
  assign pack_read_req_packed_31 = { pack_read_req_op_sel_26, pack_read_req_local_addr_27, pack_read_req_local_stride_28, pack_read_req_local_size_29, pack_read_req_local_blocksize_30 };
  assign _maxi_read_req_fifo_wdata = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? pack_read_req_packed_31 : 'hx;
  assign _maxi_read_req_fifo_enq = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? (_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full && !_maxi_read_req_fifo_almost_full : 0;
  localparam _tmp_32 = 1;
  wire [_tmp_32-1:0] _tmp_33;
  assign _tmp_33 = !_maxi_read_req_fifo_almost_full;
  reg [_tmp_32-1:0] __tmp_33_1;
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
  wire [32-1:0] mask_addr_shifted_42;
  assign mask_addr_shifted_42 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_43;
  assign mask_addr_masked_43 = mask_addr_shifted_42 << 2;
  wire [32-1:0] mask_addr_shifted_44;
  assign mask_addr_shifted_44 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_45;
  assign mask_addr_masked_45 = mask_addr_shifted_44 << 2;
  reg _maxi_cond_0_1;
  reg [32-1:0] _maxi_read_data_fsm;
  localparam _maxi_read_data_fsm_init = 0;
  assign _maxi_read_req_fifo_deq = ((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) && !_maxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_46;
  reg [10-1:0] write_burst_stride_47;
  reg [33-1:0] write_burst_length_48;
  reg write_burst_done_49;
  assign ram_b_0_wdata = ((write_burst_fsm_0 == 1) && maxi_rvalid)? maxi_rdata : 'hx;
  assign ram_b_0_wenable = ((write_burst_fsm_0 == 1) && maxi_rvalid)? 1'd1 : 0;
  assign maxi_rready = _maxi_read_data_fsm == 2;
  wire [8-1:0] pack_read_req_op_sel_50;
  wire [33-1:0] pack_read_req_local_size_51;
  assign pack_read_req_op_sel_50 = 1;
  assign pack_read_req_local_size_51 = _th_comp_read_size_0;
  wire [41-1:0] pack_read_req_packed_52;
  assign pack_read_req_packed_52 = { pack_read_req_op_sel_50, pack_read_req_local_size_51 };
  assign _axi_in_read_req_fifo_wdata = ((th_comp == 16) && !_axi_in_read_req_fifo_almost_full)? pack_read_req_packed_52 : 'hx;
  assign _axi_in_read_req_fifo_enq = ((th_comp == 16) && !_axi_in_read_req_fifo_almost_full)? (th_comp == 16) && !_axi_in_read_req_fifo_almost_full && !_axi_in_read_req_fifo_almost_full : 0;
  localparam _tmp_53 = 1;
  wire [_tmp_53-1:0] _tmp_54;
  assign _tmp_54 = !_axi_in_read_req_fifo_almost_full;
  reg [_tmp_53-1:0] __tmp_54_1;
  reg [32-1:0] _axi_in_read_data_fsm;
  localparam _axi_in_read_data_fsm_init = 0;
  assign _axi_in_read_req_fifo_deq = ((_axi_in_read_data_fsm == 0) && (_axi_in_read_data_idle && !_axi_in_read_req_fifo_empty && (_axi_in_read_op_sel_fifo == 1)) && !_axi_in_read_req_fifo_empty)? 1 : 0;
  assign axi_in_tready = (_axi_in_read_data_fsm == 1) && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1);
  assign fifo_a_wdata = ((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1))? axi_in_tdata : 'hx;
  assign fifo_a_enq = ((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1))? (_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_op_sel_buf == 1) && !fifo_a_almost_full : 0;
  localparam _tmp_55 = 1;
  wire [_tmp_55-1:0] _tmp_56;
  assign _tmp_56 = !fifo_a_almost_full;
  reg [_tmp_55-1:0] __tmp_56_1;
  wire axistreamout_flag_57;
  assign axistreamout_flag_57 = th_comp == 17;
  wire [8-1:0] pack_write_req_op_sel_58;
  wire [33-1:0] pack_write_req_local_size_59;
  assign pack_write_req_op_sel_58 = 1;
  assign pack_write_req_local_size_59 = _th_comp_write_size_1;
  wire [41-1:0] pack_write_req_packed_60;
  assign pack_write_req_packed_60 = { pack_write_req_op_sel_58, pack_write_req_local_size_59 };
  assign _axi_out_write_req_fifo_wdata = (axistreamout_flag_57 && !_axi_out_write_req_fifo_almost_full)? pack_write_req_packed_60 : 'hx;
  assign _axi_out_write_req_fifo_enq = (axistreamout_flag_57 && !_axi_out_write_req_fifo_almost_full)? axistreamout_flag_57 && !_axi_out_write_req_fifo_almost_full && !_axi_out_write_req_fifo_almost_full : 0;
  localparam _tmp_61 = 1;
  wire [_tmp_61-1:0] _tmp_62;
  assign _tmp_62 = !_axi_out_write_req_fifo_almost_full;
  reg [_tmp_61-1:0] __tmp_62_1;
  reg [32-1:0] _axi_out_write_data_fsm;
  localparam _axi_out_write_data_fsm_init = 0;
  assign _axi_out_write_req_fifo_deq = ((_axi_out_write_data_fsm == 0) && (_axi_out_write_data_idle && !_axi_out_write_req_fifo_empty && (_axi_out_write_op_sel_fifo == 1)) && !_axi_out_write_req_fifo_empty)? 1 : 0;
  reg rlast_63;
  wire cur_rvalid_64;
  assign fifo_c_deq = ((_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty)? 1 : 0;
  localparam _tmp_65 = 1;
  wire [_tmp_65-1:0] _tmp_66;
  assign _tmp_66 = (_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid) && !fifo_c_empty;
  reg [_tmp_65-1:0] __tmp_66_1;
  reg repeat_rvalid_67;
  assign cur_rvalid_64 = __tmp_66_1 || repeat_rvalid_67;
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
  wire _set_flag_68;
  assign _set_flag_68 = th_comp == 18;
  assign fifo_a_deq = (_mystream_reduce_stream_oready && _mystream_reduce_a_source_fifo_deq && (_mystream_reduce_a_source_sel == 1) && !fifo_a_empty)? 1 : 0;
  localparam _tmp_69 = 1;
  wire [_tmp_69-1:0] _tmp_70;
  assign _tmp_70 = _mystream_reduce_stream_oready && _mystream_reduce_a_source_fifo_deq && (_mystream_reduce_a_source_sel == 1) && !fifo_a_empty;
  reg [_tmp_69-1:0] __tmp_70_1;
  assign _mystream_reduce_a_source_fifo_rdata = (_mystream_reduce_a_source_sel == 1)? fifo_a_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_reduce_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_reduce_a_source_fsm_0;
  localparam _mystream_reduce_a_source_fsm_0_init = 0;
  wire _set_flag_71;
  assign _set_flag_71 = th_comp == 19;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_reduce_reduce_size_data = __variable_wdata_1;
  wire _set_flag_72;
  assign _set_flag_72 = th_comp == 20;
  reg _tmp_73;
  reg _tmp_74;
  reg _tmp_75;
  reg _tmp_76;
  reg _tmp_77;
  reg _tmp_78;
  reg signed [32-1:0] _tmp_79;
  reg signed [32-1:0] _tmp_80;
  reg signed [32-1:0] _tmp_81;
  reg signed [32-1:0] _tmp_82;
  reg signed [32-1:0] _tmp_83;
  reg signed [32-1:0] _tmp_84;
  assign fifo_b_wdata = (_mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2))? _mystream_reduce_sum_sink_fifo_wdata : 'hx;
  assign fifo_b_enq = (_mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2))? _mystream_reduce_stream_oready && _mystream_reduce_sum_sink_fifo_enq && (_mystream_reduce_sum_sink_sel == 2) && !fifo_b_almost_full : 0;
  localparam _tmp_85 = 1;
  wire [_tmp_85-1:0] _tmp_86;
  assign _tmp_86 = !fifo_b_almost_full;
  reg [_tmp_85-1:0] __tmp_86_1;
  assign _mystream_reduce_stream_oready = ((_mystream_reduce_sink_busy && (_mystream_reduce_sum_sink_sel == 2))? !fifo_b_almost_full : 1) && (((_mystream_reduce_source_busy && (_mystream_reduce_a_source_sel == 1))? !fifo_a_empty || _mystream_reduce_a_idle : 1) && _mystream_reduce_stream_internal_oready);
  reg [32-1:0] _mystream_reduce_sum_sink_fsm_1;
  localparam _mystream_reduce_sum_sink_fsm_1_init = 0;
  wire signed [32-1:0] mystream_bias_x_data;
  wire signed [32-1:0] mystream_bias_y_data;
  reg __mystream_bias_stream_ivalid_1;
  reg signed [32-1:0] _plus_data_10;
  wire signed [32-1:0] mystream_bias_z_data;
  assign mystream_bias_z_data = _plus_data_10;
  wire _set_flag_87;
  assign _set_flag_87 = th_comp == 21;
  assign fifo_b_deq = (_mystream_bias_stream_oready && _mystream_bias_x_source_fifo_deq && (_mystream_bias_x_source_sel == 1) && !fifo_b_empty)? 1 : 0;
  localparam _tmp_88 = 1;
  wire [_tmp_88-1:0] _tmp_89;
  assign _tmp_89 = _mystream_bias_stream_oready && _mystream_bias_x_source_fifo_deq && (_mystream_bias_x_source_sel == 1) && !fifo_b_empty;
  reg [_tmp_88-1:0] __tmp_89_1;
  assign _mystream_bias_x_source_fifo_rdata = (_mystream_bias_x_source_sel == 1)? fifo_b_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_8;
  assign mystream_bias_x_data = __variable_wdata_8;
  reg [32-1:0] _mystream_bias_x_source_fsm_0;
  localparam _mystream_bias_x_source_fsm_0_init = 0;
  wire _set_flag_90;
  assign _set_flag_90 = th_comp == 22;
  assign ram_b_0_addr = (_mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2))? _mystream_bias_y_source_ram_raddr : 
                        ((write_burst_fsm_0 == 1) && maxi_rvalid)? write_burst_addr_46 : 'hx;
  assign ram_b_0_enable = (_mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2))? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && maxi_rvalid)? 1'd1 : 0;
  localparam _tmp_91 = 1;
  wire [_tmp_91-1:0] _tmp_92;
  assign _tmp_92 = _mystream_bias_stream_oready && _mystream_bias_y_source_ram_renable && (_mystream_bias_y_source_sel == 2);
  reg [_tmp_91-1:0] __tmp_92_1;
  assign _mystream_bias_y_source_ram_rdata = (_mystream_bias_y_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_9;
  assign mystream_bias_y_data = __variable_wdata_9;
  reg [32-1:0] _mystream_bias_y_source_fsm_1;
  localparam _mystream_bias_y_source_fsm_1_init = 0;
  wire _set_flag_93;
  assign _set_flag_93 = th_comp == 23;
  reg _tmp_94;
  reg _tmp_95;
  reg _tmp_96;
  reg signed [32-1:0] _tmp_97;
  reg signed [32-1:0] _tmp_98;
  reg signed [32-1:0] _tmp_99;
  assign fifo_c_wdata = (_mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3))? _mystream_bias_z_sink_fifo_wdata : 'hx;
  assign fifo_c_enq = (_mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3))? _mystream_bias_stream_oready && _mystream_bias_z_sink_fifo_enq && (_mystream_bias_z_sink_sel == 3) && !fifo_c_almost_full : 0;
  localparam _tmp_100 = 1;
  wire [_tmp_100-1:0] _tmp_101;
  assign _tmp_101 = !fifo_c_almost_full;
  reg [_tmp_100-1:0] __tmp_101_1;
  assign _mystream_bias_stream_oready = ((_mystream_bias_sink_busy && (_mystream_bias_z_sink_sel == 3))? !fifo_c_almost_full : 1) && (((_mystream_bias_source_busy && (_mystream_bias_x_source_sel == 1))? !fifo_b_empty || _mystream_bias_x_idle : 1) && _mystream_bias_stream_internal_oready);
  reg [32-1:0] _mystream_bias_z_sink_fsm_2;
  localparam _mystream_bias_z_sink_fsm_2_init = 0;
  wire _set_flag_102;
  assign _set_flag_102 = th_comp == 24;
  assign _mystream_reduce_run_flag = (_set_flag_102)? 1 : 0;
  reg _tmp_103;
  reg _tmp_104;
  reg _tmp_105;
  reg _tmp_106;
  reg _tmp_107;
  reg _tmp_108;
  reg [1-1:0] __variable_wdata_3;
  assign mystream_reduce__reduce_reset_data = __variable_wdata_3;
  reg _tmp_109;
  reg _tmp_110;
  reg _tmp_111;
  reg _tmp_112;
  assign _mystream_reduce_source_stop = _mystream_reduce_stream_oready && (_mystream_reduce_a_idle && (_mystream_reduce_fsm == 3));
  localparam _tmp_113 = 1;
  wire [_tmp_113-1:0] _tmp_114;
  assign _tmp_114 = _mystream_reduce_a_idle && (_mystream_reduce_fsm == 3);
  reg [_tmp_113-1:0] _tmp_115;
  localparam _tmp_116 = 1;
  wire [_tmp_116-1:0] _tmp_117;
  assign _tmp_117 = _mystream_reduce_a_idle && (_mystream_reduce_fsm == 3);
  reg [_tmp_116-1:0] _tmp_118;
  reg _tmp_119;
  reg _tmp_120;
  reg _tmp_121;
  reg _tmp_122;
  reg _tmp_123;
  reg _tmp_124;
  assign _mystream_reduce_sink_start = _tmp_124;
  reg _tmp_125;
  reg _tmp_126;
  reg _tmp_127;
  reg _tmp_128;
  reg _tmp_129;
  reg _tmp_130;
  assign _mystream_reduce_sink_stop = _tmp_130;
  reg _tmp_131;
  reg _tmp_132;
  reg _tmp_133;
  reg _tmp_134;
  reg _tmp_135;
  reg _tmp_136;
  assign _mystream_reduce_sink_busy = _tmp_136;
  reg _tmp_137;
  assign _mystream_reduce_busy = _mystream_reduce_source_busy || _mystream_reduce_sink_busy || _mystream_reduce_busy_reg;
  wire _set_flag_138;
  assign _set_flag_138 = th_comp == 26;
  assign _mystream_bias_run_flag = (_set_flag_138)? 1 : 0;
  reg _tmp_139;
  reg _tmp_140;
  reg _tmp_141;
  assign _mystream_bias_source_stop = _mystream_bias_stream_oready && (_mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3));
  localparam _tmp_142 = 1;
  wire [_tmp_142-1:0] _tmp_143;
  assign _tmp_143 = _mystream_bias_x_idle && _mystream_bias_y_idle && (_mystream_bias_fsm == 3);
  reg [_tmp_142-1:0] _tmp_144;
  reg _tmp_145;
  reg _tmp_146;
  reg _tmp_147;
  assign _mystream_bias_sink_start = _tmp_147;
  reg _tmp_148;
  reg _tmp_149;
  reg _tmp_150;
  assign _mystream_bias_sink_stop = _tmp_150;
  reg _tmp_151;
  reg _tmp_152;
  reg _tmp_153;
  assign _mystream_bias_sink_busy = _tmp_153;
  reg _tmp_154;
  assign _mystream_bias_busy = _mystream_bias_source_busy || _mystream_bias_sink_busy || _mystream_bias_busy_reg;

  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wcount_0 <= 0;
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      maxi_wdata <= 0;
      maxi_wstrb <= 0;
      maxi_wlast <= 0;
      maxi_wvalid <= 0;
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
    end else begin
      if(_maxi_cond_0_1) begin
        maxi_arvalid <= 0;
      end 
      if(maxi_awvalid && maxi_awready && !(maxi_bvalid && maxi_bready) && (outstanding_wcount_0 < 7)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 + 1;
      end 
      if(!(maxi_awvalid && maxi_awready) && (maxi_bvalid && maxi_bready) && (outstanding_wcount_0 > 0)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 - 1;
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
      if((th_comp == 14) && _maxi_read_req_idle) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= 1;
        _maxi_read_global_addr <= mask_addr_masked_25;
        _maxi_read_global_size <= _th_comp_write_size_1;
        _maxi_read_local_addr <= 0;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_comp_write_size_1;
        _maxi_read_local_blocksize <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && _maxi_read_start) begin
        _maxi_read_req_idle <= 0;
      end 
      if(_maxi_read_start && _maxi_read_req_fifo_almost_full) begin
        _maxi_read_start <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256) && ((mask_addr_masked_35 & 4095) + (_maxi_read_global_size << 2) >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_37 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_39 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256)) begin
        _maxi_read_cur_global_size <= _maxi_read_global_size;
        _maxi_read_global_size <= 0;
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && ((mask_addr_masked_41 & 4095) + 1024 >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_43 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_45 & 4095) >> 2);
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
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_read_req_fifo <= 0;
      __tmp_33_1 <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full && (_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty)) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo;
      end else if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo + 1;
      end else if(_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo - 1;
      end 
      __tmp_33_1 <= _tmp_33;
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


  always @(posedge CLK) begin
    if(RST) begin
      _axi_in_read_data_idle <= 1;
      _axi_in_read_op_sel_buf <= 0;
      _axi_in_read_local_size_buf <= 0;
    end else begin
      if((_axi_in_read_data_fsm == 0) && (_axi_in_read_data_idle && !_axi_in_read_req_fifo_empty && (_axi_in_read_op_sel_fifo == 1))) begin
        _axi_in_read_data_idle <= 0;
        _axi_in_read_op_sel_buf <= _axi_in_read_op_sel_fifo;
        _axi_in_read_local_size_buf <= _axi_in_read_local_size_fifo;
      end 
      if((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full) begin
        _axi_in_read_local_size_buf <= _axi_in_read_local_size_buf - 1;
      end 
      if((_axi_in_read_data_fsm == 1) && axi_in_tvalid && !fifo_a_almost_full && (_axi_in_read_local_size_buf <= 1)) begin
        _axi_in_read_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_in_read_req_fifo <= 0;
      __tmp_54_1 <= 0;
    end else begin
      if(_axi_in_read_req_fifo_enq && !_axi_in_read_req_fifo_full && (_axi_in_read_req_fifo_deq && !_axi_in_read_req_fifo_empty)) begin
        count__axi_in_read_req_fifo <= count__axi_in_read_req_fifo;
      end else if(_axi_in_read_req_fifo_enq && !_axi_in_read_req_fifo_full) begin
        count__axi_in_read_req_fifo <= count__axi_in_read_req_fifo + 1;
      end else if(_axi_in_read_req_fifo_deq && !_axi_in_read_req_fifo_empty) begin
        count__axi_in_read_req_fifo <= count__axi_in_read_req_fifo - 1;
      end 
      __tmp_54_1 <= _tmp_54;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_out_write_data_idle <= 1;
      _axi_out_write_op_sel_buf <= 0;
      _axi_out_write_size_buf <= 0;
      repeat_rvalid_67 <= 0;
      axi_out_tdata <= 0;
      axi_out_tvalid <= 0;
      axi_out_tlast <= 0;
      _axi_out_cond_0_1 <= 0;
    end else begin
      if(_axi_out_cond_0_1) begin
        axi_out_tvalid <= 0;
        axi_out_tlast <= 0;
      end 
      if((_axi_out_write_data_fsm == 0) && (_axi_out_write_data_idle && !_axi_out_write_req_fifo_empty && (_axi_out_write_op_sel_fifo == 1))) begin
        _axi_out_write_data_idle <= 0;
        _axi_out_write_op_sel_buf <= _axi_out_write_op_sel_fifo;
        _axi_out_write_size_buf <= _axi_out_write_size_fifo;
      end 
      repeat_rvalid_67 <= 0;
      if(__tmp_66_1 && !(axi_out_tready || !axi_out_tvalid)) begin
        repeat_rvalid_67 <= 1;
      end 
      if(repeat_rvalid_67 && !(axi_out_tready || !axi_out_tvalid)) begin
        repeat_rvalid_67 <= 1;
      end 
      if((_axi_out_write_data_fsm == 1) && ((_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid))) begin
        _axi_out_write_size_buf <= _axi_out_write_size_buf - 1;
      end 
      if((_axi_out_write_op_sel_buf == 1) && cur_rvalid_64 && (axi_out_tready || !axi_out_tvalid) && (axi_out_tready || !axi_out_tvalid)) begin
        axi_out_tdata <= fifo_c_rdata;
        axi_out_tvalid <= 1;
        axi_out_tlast <= rlast_63;
      end 
      _axi_out_cond_0_1 <= 1;
      if(axi_out_tvalid && !axi_out_tready) begin
        axi_out_tvalid <= axi_out_tvalid;
        axi_out_tlast <= axi_out_tlast;
      end 
      if((_axi_out_write_data_fsm == 1) && ((_axi_out_write_op_sel_buf == 1) && cur_rvalid_64 && (axi_out_tready || !axi_out_tvalid)) && rlast_63) begin
        _axi_out_write_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__axi_out_write_req_fifo <= 0;
      __tmp_62_1 <= 0;
    end else begin
      if(_axi_out_write_req_fifo_enq && !_axi_out_write_req_fifo_full && (_axi_out_write_req_fifo_deq && !_axi_out_write_req_fifo_empty)) begin
        count__axi_out_write_req_fifo <= count__axi_out_write_req_fifo;
      end else if(_axi_out_write_req_fifo_enq && !_axi_out_write_req_fifo_full) begin
        count__axi_out_write_req_fifo <= count__axi_out_write_req_fifo + 1;
      end else if(_axi_out_write_req_fifo_deq && !_axi_out_write_req_fifo_empty) begin
        count__axi_out_write_req_fifo <= count__axi_out_write_req_fifo - 1;
      end 
      __tmp_62_1 <= _tmp_62;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_a <= 0;
      __tmp_56_1 <= 0;
      __tmp_70_1 <= 0;
    end else begin
      if(fifo_a_enq && !fifo_a_full && (fifo_a_deq && !fifo_a_empty)) begin
        count_fifo_a <= count_fifo_a;
      end else if(fifo_a_enq && !fifo_a_full) begin
        count_fifo_a <= count_fifo_a + 1;
      end else if(fifo_a_deq && !fifo_a_empty) begin
        count_fifo_a <= count_fifo_a - 1;
      end 
      __tmp_56_1 <= _tmp_56;
      __tmp_70_1 <= _tmp_70;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_b <= 0;
      __tmp_86_1 <= 0;
      __tmp_89_1 <= 0;
    end else begin
      if(fifo_b_enq && !fifo_b_full && (fifo_b_deq && !fifo_b_empty)) begin
        count_fifo_b <= count_fifo_b;
      end else if(fifo_b_enq && !fifo_b_full) begin
        count_fifo_b <= count_fifo_b + 1;
      end else if(fifo_b_deq && !fifo_b_empty) begin
        count_fifo_b <= count_fifo_b - 1;
      end 
      __tmp_86_1 <= _tmp_86;
      __tmp_89_1 <= _tmp_89;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_fifo_c <= 0;
      __tmp_66_1 <= 0;
      __tmp_101_1 <= 0;
    end else begin
      if(fifo_c_enq && !fifo_c_full && (fifo_c_deq && !fifo_c_empty)) begin
        count_fifo_c <= count_fifo_c;
      end else if(fifo_c_enq && !fifo_c_full) begin
        count_fifo_c <= count_fifo_c + 1;
      end else if(fifo_c_deq && !fifo_c_empty) begin
        count_fifo_c <= count_fifo_c - 1;
      end 
      __tmp_66_1 <= _tmp_66;
      __tmp_101_1 <= _tmp_101;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_92_1 <= 0;
    end else begin
      __tmp_92_1 <= _tmp_92;
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
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_78 <= 0;
      _tmp_79 <= 0;
      _tmp_80 <= 0;
      _tmp_81 <= 0;
      _tmp_82 <= 0;
      _tmp_83 <= 0;
      _tmp_84 <= 0;
      _mystream_reduce_sum_sink_mode <= 5'b0;
      _mystream_reduce_sum_sink_size <= 0;
      _mystream_reduce_sum_sink_sel <= 0;
      _mystream_reduce_sum_sink_size_buf <= 0;
      _mystream_reduce_sum_sink_count <= 0;
      _mystream_reduce_sum_sink_fifo_wdata <= 0;
      _tmp_103 <= 0;
      _tmp_104 <= 0;
      _tmp_105 <= 0;
      _tmp_106 <= 0;
      _tmp_107 <= 0;
      _tmp_108 <= 0;
      __variable_wdata_3 <= 0;
      _tmp_109 <= 0;
      _tmp_110 <= 0;
      _tmp_111 <= 0;
      _tmp_112 <= 0;
      _tmp_115 <= 0;
      _tmp_118 <= 0;
      _tmp_119 <= 0;
      _tmp_120 <= 0;
      _tmp_121 <= 0;
      _tmp_122 <= 0;
      _tmp_123 <= 0;
      _tmp_124 <= 0;
      _tmp_125 <= 0;
      _tmp_126 <= 0;
      _tmp_127 <= 0;
      _tmp_128 <= 0;
      _tmp_129 <= 0;
      _tmp_130 <= 0;
      _tmp_131 <= 0;
      _tmp_132 <= 0;
      _tmp_133 <= 0;
      _tmp_134 <= 0;
      _tmp_135 <= 0;
      _tmp_136 <= 0;
      _tmp_137 <= 0;
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
      if(_set_flag_68) begin
        _mystream_reduce_a_source_mode <= 5'b10000;
        _mystream_reduce_a_source_size <= _th_comp_read_size_0;
      end 
      if(_set_flag_68) begin
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
      if(_set_flag_71) begin
        _mystream_reduce_reduce_size_next_parameter_data <= _th_comp_reduce_size_2;
      end 
      if(_mystream_reduce_source_start) begin
        __variable_wdata_1 <= _mystream_reduce_reduce_size_next_parameter_data;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_73 <= _set_flag_72;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_74 <= _tmp_73;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_75 <= _tmp_74;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_76 <= _tmp_75;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_77 <= _tmp_76;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_78 <= _tmp_77;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_79 <= _th_comp_write_size_1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_80 <= _tmp_79;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_81 <= _tmp_80;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_82 <= _tmp_81;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_83 <= _tmp_82;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_84 <= _tmp_83;
      end 
      if(_tmp_78) begin
        _mystream_reduce_sum_sink_mode <= 5'b10000;
        _mystream_reduce_sum_sink_size <= _tmp_84;
      end 
      if(_tmp_78) begin
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
        _tmp_103 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_104 <= _tmp_103;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_105 <= _tmp_104;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_106 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_107 <= _tmp_106;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_108 <= _tmp_107;
      end 
      if(_mystream_reduce_stream_oready && _tmp_108) begin
        __variable_wdata_3 <= 1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_109 <= _mystream_reduce_source_start;
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
      if(_mystream_reduce_stream_oready && _tmp_112) begin
        __variable_wdata_3 <= 0;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_115 <= _tmp_114;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_118 <= _tmp_117;
      end 
      if(_mystream_reduce_stream_oready && _tmp_118) begin
        __variable_wdata_3 <= 1;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_119 <= _mystream_reduce_source_start;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_120 <= _tmp_119;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_121 <= _tmp_120;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_122 <= _tmp_121;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_123 <= _tmp_122;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_124 <= _tmp_123;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_125 <= _mystream_reduce_source_stop;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_126 <= _tmp_125;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_127 <= _tmp_126;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_128 <= _tmp_127;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_129 <= _tmp_128;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_130 <= _tmp_129;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_131 <= _mystream_reduce_source_busy;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_132 <= _tmp_131;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_133 <= _tmp_132;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_134 <= _tmp_133;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_135 <= _tmp_134;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_136 <= _tmp_135;
      end 
      if(_mystream_reduce_stream_oready) begin
        _tmp_137 <= _mystream_reduce_sink_busy;
      end 
      if(!_mystream_reduce_sink_busy && _tmp_137) begin
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
      if(_mystream_reduce_stream_oready && _tmp_105) begin
        _mystream_reduce_stream_ivalid <= 1;
      end 
      if(_mystream_reduce_stream_oready && _tmp_115) begin
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
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _tmp_99 <= 0;
      _mystream_bias_z_sink_mode <= 5'b0;
      _mystream_bias_z_sink_size <= 0;
      _mystream_bias_z_sink_sel <= 0;
      _mystream_bias_z_sink_size_buf <= 0;
      _mystream_bias_z_sink_count <= 0;
      _mystream_bias_z_sink_fifo_wdata <= 0;
      _tmp_139 <= 0;
      _tmp_140 <= 0;
      _tmp_141 <= 0;
      _tmp_144 <= 0;
      _tmp_145 <= 0;
      _tmp_146 <= 0;
      _tmp_147 <= 0;
      _tmp_148 <= 0;
      _tmp_149 <= 0;
      _tmp_150 <= 0;
      _tmp_151 <= 0;
      _tmp_152 <= 0;
      _tmp_153 <= 0;
      _tmp_154 <= 0;
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
      if(_set_flag_87) begin
        _mystream_bias_x_source_mode <= 5'b10000;
        _mystream_bias_x_source_size <= _th_comp_write_size_1;
      end 
      if(_set_flag_87) begin
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
      if(_set_flag_90) begin
        _mystream_bias_y_source_mode <= 5'b1;
        _mystream_bias_y_source_offset <= 0;
        _mystream_bias_y_source_size <= _th_comp_write_size_1;
        _mystream_bias_y_source_stride <= 1;
      end 
      if(_set_flag_90) begin
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
        _tmp_94 <= _set_flag_93;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_95 <= _tmp_94;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_96 <= _tmp_95;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_97 <= _th_comp_write_size_1;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_98 <= _tmp_97;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_99 <= _tmp_98;
      end 
      if(_tmp_96) begin
        _mystream_bias_z_sink_mode <= 5'b10000;
        _mystream_bias_z_sink_size <= _tmp_99;
      end 
      if(_tmp_96) begin
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
        _tmp_139 <= _mystream_bias_source_start;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_140 <= _tmp_139;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_141 <= _tmp_140;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_144 <= _tmp_143;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_145 <= _mystream_bias_source_start;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_146 <= _tmp_145;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_147 <= _tmp_146;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_148 <= _mystream_bias_source_stop;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_149 <= _tmp_148;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_150 <= _tmp_149;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_151 <= _mystream_bias_source_busy;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_152 <= _tmp_151;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_153 <= _tmp_152;
      end 
      if(_mystream_bias_stream_oready) begin
        _tmp_154 <= _mystream_bias_sink_busy;
      end 
      if(!_mystream_bias_sink_busy && _tmp_154) begin
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
      if(_mystream_bias_stream_oready && _tmp_141) begin
        _mystream_bias_stream_ivalid <= 1;
      end 
      if(_mystream_bias_stream_oready && _tmp_144) begin
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

  localparam write_burst_fsm_0_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_0 <= write_burst_fsm_0_init;
      write_burst_addr_46 <= 0;
      write_burst_stride_47 <= 0;
      write_burst_length_48 <= 0;
      write_burst_done_49 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_46 <= _maxi_read_local_addr_buf;
          write_burst_stride_47 <= _maxi_read_local_stride_buf;
          write_burst_length_48 <= _maxi_read_local_size_buf;
          write_burst_done_49 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 1) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(maxi_rvalid) begin
            write_burst_addr_46 <= write_burst_addr_46 + write_burst_stride_47;
            write_burst_length_48 <= write_burst_length_48 - 1;
            write_burst_done_49 <= 0;
          end 
          if(maxi_rvalid && (write_burst_length_48 <= 1)) begin
            write_burst_done_49 <= 1;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_done_49 <= 1;
          end 
          if(maxi_rvalid && (write_burst_length_48 <= 1)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(maxi_rvalid && 0) begin
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
          if(_axi_in_read_data_idle && !_axi_in_read_req_fifo_empty && (_axi_in_read_op_sel_fifo == 1)) begin
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
      rlast_63 <= 0;
    end else begin
      case(_axi_out_write_data_fsm)
        _axi_out_write_data_fsm_init: begin
          rlast_63 <= 0;
          if(_axi_out_write_data_idle && !_axi_out_write_req_fifo_empty && (_axi_out_write_op_sel_fifo == 1)) begin
            _axi_out_write_data_fsm <= _axi_out_write_data_fsm_1;
          end 
        end
        _axi_out_write_data_fsm_1: begin
          if((_axi_out_write_data_fsm == 1) && !fifo_c_empty && (_axi_out_write_op_sel_buf == 1) && (_axi_out_write_size_buf > 0) && (axi_out_tready || !axi_out_tvalid)) begin
            rlast_63 <= _axi_out_write_size_buf <= 1;
          end 
          if((_axi_out_write_op_sel_buf == 1) && cur_rvalid_64 && (axi_out_tready || !axi_out_tvalid) && rlast_63) begin
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

