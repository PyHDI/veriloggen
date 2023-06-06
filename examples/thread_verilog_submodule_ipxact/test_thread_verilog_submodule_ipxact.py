from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_verilog_submodule_ipxact

expected_verilog = """
module test;

  reg uut_CLK;
  reg uut_RST;
  wire [8-1:0] uut_led;
  wire [32-1:0] uut_maxi_awaddr;
  wire [8-1:0] uut_maxi_awlen;
  wire [3-1:0] uut_maxi_awsize;
  wire [2-1:0] uut_maxi_awburst;
  wire [1-1:0] uut_maxi_awlock;
  wire [4-1:0] uut_maxi_awcache;
  wire [3-1:0] uut_maxi_awprot;
  wire [4-1:0] uut_maxi_awqos;
  wire [2-1:0] uut_maxi_awuser;
  wire uut_maxi_awvalid;
  reg uut_maxi_awready;
  wire [32-1:0] uut_maxi_wdata;
  wire [4-1:0] uut_maxi_wstrb;
  wire uut_maxi_wlast;
  wire uut_maxi_wvalid;
  reg uut_maxi_wready;
  reg [2-1:0] uut_maxi_bresp;
  reg uut_maxi_bvalid;
  wire uut_maxi_bready;
  wire [32-1:0] uut_maxi_araddr;
  wire [8-1:0] uut_maxi_arlen;
  wire [3-1:0] uut_maxi_arsize;
  wire [2-1:0] uut_maxi_arburst;
  wire [1-1:0] uut_maxi_arlock;
  wire [4-1:0] uut_maxi_arcache;
  wire [3-1:0] uut_maxi_arprot;
  wire [4-1:0] uut_maxi_arqos;
  wire [2-1:0] uut_maxi_aruser;
  wire uut_maxi_arvalid;
  reg uut_maxi_arready;
  reg [32-1:0] uut_maxi_rdata;
  reg [2-1:0] uut_maxi_rresp;
  reg uut_maxi_rlast;
  reg uut_maxi_rvalid;
  wire uut_maxi_rready;
  reg [32-1:0] uut_saxi_awaddr;
  reg [4-1:0] uut_saxi_awcache;
  reg [3-1:0] uut_saxi_awprot;
  reg uut_saxi_awvalid;
  wire uut_saxi_awready;
  reg [32-1:0] uut_saxi_wdata;
  reg [4-1:0] uut_saxi_wstrb;
  reg uut_saxi_wvalid;
  wire uut_saxi_wready;
  wire [2-1:0] uut_saxi_bresp;
  wire uut_saxi_bvalid;
  reg uut_saxi_bready;
  reg [32-1:0] uut_saxi_araddr;
  reg [4-1:0] uut_saxi_arcache;
  reg [3-1:0] uut_saxi_arprot;
  reg uut_saxi_arvalid;
  wire uut_saxi_arready;
  wire [32-1:0] uut_saxi_rdata;
  wire [2-1:0] uut_saxi_rresp;
  wire uut_saxi_rvalid;
  reg uut_saxi_rready;

  blinkled
  uut
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .led(uut_led),
    .maxi_awaddr(uut_maxi_awaddr),
    .maxi_awlen(uut_maxi_awlen),
    .maxi_awsize(uut_maxi_awsize),
    .maxi_awburst(uut_maxi_awburst),
    .maxi_awlock(uut_maxi_awlock),
    .maxi_awcache(uut_maxi_awcache),
    .maxi_awprot(uut_maxi_awprot),
    .maxi_awqos(uut_maxi_awqos),
    .maxi_awuser(uut_maxi_awuser),
    .maxi_awvalid(uut_maxi_awvalid),
    .maxi_awready(uut_maxi_awready),
    .maxi_wdata(uut_maxi_wdata),
    .maxi_wstrb(uut_maxi_wstrb),
    .maxi_wlast(uut_maxi_wlast),
    .maxi_wvalid(uut_maxi_wvalid),
    .maxi_wready(uut_maxi_wready),
    .maxi_bresp(uut_maxi_bresp),
    .maxi_bvalid(uut_maxi_bvalid),
    .maxi_bready(uut_maxi_bready),
    .maxi_araddr(uut_maxi_araddr),
    .maxi_arlen(uut_maxi_arlen),
    .maxi_arsize(uut_maxi_arsize),
    .maxi_arburst(uut_maxi_arburst),
    .maxi_arlock(uut_maxi_arlock),
    .maxi_arcache(uut_maxi_arcache),
    .maxi_arprot(uut_maxi_arprot),
    .maxi_arqos(uut_maxi_arqos),
    .maxi_aruser(uut_maxi_aruser),
    .maxi_arvalid(uut_maxi_arvalid),
    .maxi_arready(uut_maxi_arready),
    .maxi_rdata(uut_maxi_rdata),
    .maxi_rresp(uut_maxi_rresp),
    .maxi_rlast(uut_maxi_rlast),
    .maxi_rvalid(uut_maxi_rvalid),
    .maxi_rready(uut_maxi_rready),
    .saxi_awaddr(uut_saxi_awaddr),
    .saxi_awcache(uut_saxi_awcache),
    .saxi_awprot(uut_saxi_awprot),
    .saxi_awvalid(uut_saxi_awvalid),
    .saxi_awready(uut_saxi_awready),
    .saxi_wdata(uut_saxi_wdata),
    .saxi_wstrb(uut_saxi_wstrb),
    .saxi_wvalid(uut_saxi_wvalid),
    .saxi_wready(uut_saxi_wready),
    .saxi_bresp(uut_saxi_bresp),
    .saxi_bvalid(uut_saxi_bvalid),
    .saxi_bready(uut_saxi_bready),
    .saxi_araddr(uut_saxi_araddr),
    .saxi_arcache(uut_saxi_arcache),
    .saxi_arprot(uut_saxi_arprot),
    .saxi_arvalid(uut_saxi_arvalid),
    .saxi_arready(uut_saxi_arready),
    .saxi_rdata(uut_saxi_rdata),
    .saxi_rresp(uut_saxi_rresp),
    .saxi_rvalid(uut_saxi_rvalid),
    .saxi_rready(uut_saxi_rready)
  );

  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire [3-1:0] memory_awsize;
  wire [2-1:0] memory_awburst;
  wire [1-1:0] memory_awlock;
  wire [4-1:0] memory_awcache;
  wire [3-1:0] memory_awprot;
  wire [4-1:0] memory_awqos;
  wire [2-1:0] memory_awuser;
  wire memory_awvalid;
  reg memory_awready;
  wire [32-1:0] memory_wdata;
  wire [4-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  wire memory_wready;
  wire [2-1:0] memory_bresp;
  reg memory_bvalid;
  wire memory_bready;
  assign memory_bresp = 0;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire [3-1:0] memory_arsize;
  wire [2-1:0] memory_arburst;
  wire [1-1:0] memory_arlock;
  wire [4-1:0] memory_arcache;
  wire [3-1:0] memory_arprot;
  wire [4-1:0] memory_arqos;
  wire [2-1:0] memory_aruser;
  wire memory_arvalid;
  reg memory_arready;
  reg [32-1:0] memory_rdata;
  wire [2-1:0] memory_rresp;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  assign memory_rresp = 0;
  reg [32-1:0] _memory_waddr_fsm;
  localparam _memory_waddr_fsm_init = 0;
  reg [32-1:0] _memory_wdata_fsm;
  localparam _memory_wdata_fsm_init = 0;
  reg [32-1:0] _memory_raddr_fsm;
  localparam _memory_raddr_fsm_init = 0;
  reg [32-1:0] _memory_rdata_fsm;
  localparam _memory_rdata_fsm_init = 0;
  wire _memory_wreq_fifo_enq;
  wire [41-1:0] _memory_wreq_fifo_wdata;
  wire _memory_wreq_fifo_full;
  wire _memory_wreq_fifo_almost_full;
  wire _memory_wreq_fifo_deq;
  wire [41-1:0] _memory_wreq_fifo_rdata;
  wire _memory_wreq_fifo_empty;
  wire _memory_wreq_fifo_almost_empty;

  _memory_wreq_fifo
  inst__memory_wreq_fifo
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    ._memory_wreq_fifo_enq(_memory_wreq_fifo_enq),
    ._memory_wreq_fifo_wdata(_memory_wreq_fifo_wdata),
    ._memory_wreq_fifo_full(_memory_wreq_fifo_full),
    ._memory_wreq_fifo_almost_full(_memory_wreq_fifo_almost_full),
    ._memory_wreq_fifo_deq(_memory_wreq_fifo_deq),
    ._memory_wreq_fifo_rdata(_memory_wreq_fifo_rdata),
    ._memory_wreq_fifo_empty(_memory_wreq_fifo_empty),
    ._memory_wreq_fifo_almost_empty(_memory_wreq_fifo_almost_empty)
  );

  reg [4-1:0] count__memory_wreq_fifo;
  wire _memory_rreq_fifo_enq;
  wire [41-1:0] _memory_rreq_fifo_wdata;
  wire _memory_rreq_fifo_full;
  wire _memory_rreq_fifo_almost_full;
  wire _memory_rreq_fifo_deq;
  wire [41-1:0] _memory_rreq_fifo_rdata;
  wire _memory_rreq_fifo_empty;
  wire _memory_rreq_fifo_almost_empty;

  _memory_rreq_fifo
  inst__memory_rreq_fifo
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    ._memory_rreq_fifo_enq(_memory_rreq_fifo_enq),
    ._memory_rreq_fifo_wdata(_memory_rreq_fifo_wdata),
    ._memory_rreq_fifo_full(_memory_rreq_fifo_full),
    ._memory_rreq_fifo_almost_full(_memory_rreq_fifo_almost_full),
    ._memory_rreq_fifo_deq(_memory_rreq_fifo_deq),
    ._memory_rreq_fifo_rdata(_memory_rreq_fifo_rdata),
    ._memory_rreq_fifo_empty(_memory_rreq_fifo_empty),
    ._memory_rreq_fifo_almost_empty(_memory_rreq_fifo_almost_empty)
  );

  reg [4-1:0] count__memory_rreq_fifo;
  wire _memory_wdata_fifo_enq;
  wire [37-1:0] _memory_wdata_fifo_wdata;
  wire _memory_wdata_fifo_full;
  wire _memory_wdata_fifo_almost_full;
  wire _memory_wdata_fifo_deq;
  wire [37-1:0] _memory_wdata_fifo_rdata;
  wire _memory_wdata_fifo_empty;
  wire _memory_wdata_fifo_almost_empty;

  _memory_wdata_fifo
  inst__memory_wdata_fifo
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    ._memory_wdata_fifo_enq(_memory_wdata_fifo_enq),
    ._memory_wdata_fifo_wdata(_memory_wdata_fifo_wdata),
    ._memory_wdata_fifo_full(_memory_wdata_fifo_full),
    ._memory_wdata_fifo_almost_full(_memory_wdata_fifo_almost_full),
    ._memory_wdata_fifo_deq(_memory_wdata_fifo_deq),
    ._memory_wdata_fifo_rdata(_memory_wdata_fifo_rdata),
    ._memory_wdata_fifo_empty(_memory_wdata_fifo_empty),
    ._memory_wdata_fifo_almost_empty(_memory_wdata_fifo_almost_empty)
  );

  reg [4-1:0] count__memory_wdata_fifo;
  assign memory_wready = !_memory_wdata_fifo_almost_full;
  wire [32-1:0] pack_write_data_wdata_0;
  wire [4-1:0] pack_write_data_wstrb_1;
  wire [1-1:0] pack_write_data_wlast_2;
  assign pack_write_data_wdata_0 = memory_wdata;
  assign pack_write_data_wstrb_1 = memory_wstrb;
  assign pack_write_data_wlast_2 = memory_wlast;
  wire [37-1:0] pack_write_data_packed_3;
  assign pack_write_data_packed_3 = { pack_write_data_wlast_2, pack_write_data_wstrb_1, pack_write_data_wdata_0 };
  assign _memory_wdata_fifo_wdata = (memory_wvalid && memory_wready)? pack_write_data_packed_3 : 'hx;
  assign _memory_wdata_fifo_enq = (memory_wvalid && memory_wready)? memory_wvalid && memory_wready && !_memory_wdata_fifo_almost_full : 0;
  localparam _tmp_4 = 1;
  wire [_tmp_4-1:0] _tmp_5;
  assign _tmp_5 = !_memory_wdata_fifo_almost_full;
  reg [_tmp_4-1:0] __tmp_5_1;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("memimg_thread_verilog_submodule_ipxact.out", _memory_mem);
  end

  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_interval_count;
  reg [33-1:0] _keep_sleep_count;
  wire [32-1:0] pack_write_req_global_addr_6;
  wire [9-1:0] pack_write_req_size_7;
  assign pack_write_req_global_addr_6 = memory_awaddr;
  assign pack_write_req_size_7 = memory_awlen + 1;
  wire [41-1:0] pack_write_req_packed_8;
  assign pack_write_req_packed_8 = { pack_write_req_global_addr_6, pack_write_req_size_7 };
  assign _memory_wreq_fifo_wdata = ((_memory_waddr_fsm == 11) && memory_awvalid && memory_awready)? pack_write_req_packed_8 : 'hx;
  assign _memory_wreq_fifo_enq = ((_memory_waddr_fsm == 11) && memory_awvalid && memory_awready)? (_memory_waddr_fsm == 11) && memory_awvalid && memory_awready && !_memory_wreq_fifo_almost_full : 0;
  localparam _tmp_9 = 1;
  wire [_tmp_9-1:0] _tmp_10;
  assign _tmp_10 = !_memory_wreq_fifo_almost_full;
  reg [_tmp_9-1:0] __tmp_10_1;
  wire [32-1:0] unpack_write_req_global_addr_11;
  wire [9-1:0] unpack_write_req_size_12;
  assign unpack_write_req_global_addr_11 = _memory_wreq_fifo_rdata[40:9];
  assign unpack_write_req_size_12 = _memory_wreq_fifo_rdata[8:0];
  assign _memory_wreq_fifo_deq = ((_memory_wdata_fsm == 0) && !_memory_wreq_fifo_empty && !_memory_wreq_fifo_empty)? 1 : 0;
  wire [32-1:0] pack_write_data_wdata_13;
  wire [4-1:0] pack_write_data_wstrb_14;
  wire [1-1:0] pack_write_data_wlast_15;
  assign pack_write_data_wdata_13 = _memory_wdata_fifo_rdata[31:0];
  assign pack_write_data_wstrb_14 = _memory_wdata_fifo_rdata[35:32];
  assign pack_write_data_wlast_15 = _memory_wdata_fifo_rdata[36];
  wire write_data_wvalid_16;
  assign write_data_wvalid_16 = !_memory_wdata_fifo_empty;
  wire write_data_wready_17;
  assign write_data_wready_17 = (_memory_wdata_fsm == 1) && (_sleep_interval_count != 15);
  assign _memory_wdata_fifo_deq = (write_data_wready_17 && !_memory_wdata_fifo_empty && !_memory_wdata_fifo_empty)? 1 : 0;
  wire [32-1:0] pack_read_req_global_addr_18;
  wire [9-1:0] pack_read_req_size_19;
  assign pack_read_req_global_addr_18 = memory_araddr;
  assign pack_read_req_size_19 = memory_arlen + 1;
  wire [41-1:0] pack_read_req_packed_20;
  assign pack_read_req_packed_20 = { pack_read_req_global_addr_18, pack_read_req_size_19 };
  assign _memory_rreq_fifo_wdata = ((_memory_raddr_fsm == 1) && memory_arvalid && memory_arready)? pack_read_req_packed_20 : 'hx;
  assign _memory_rreq_fifo_enq = ((_memory_raddr_fsm == 1) && memory_arvalid && memory_arready)? (_memory_raddr_fsm == 1) && memory_arvalid && memory_arready && !_memory_rreq_fifo_almost_full : 0;
  localparam _tmp_21 = 1;
  wire [_tmp_21-1:0] _tmp_22;
  assign _tmp_22 = !_memory_rreq_fifo_almost_full;
  reg [_tmp_21-1:0] __tmp_22_1;
  wire [32-1:0] unpack_read_req_global_addr_23;
  wire [9-1:0] unpack_read_req_size_24;
  assign unpack_read_req_global_addr_23 = _memory_rreq_fifo_rdata[40:9];
  assign unpack_read_req_size_24 = _memory_rreq_fifo_rdata[8:0];
  assign _memory_rreq_fifo_deq = ((_memory_rdata_fsm == 0) && !_memory_rreq_fifo_empty && !_memory_rreq_fifo_empty)? 1 : 0;
  reg [32-1:0] _d1__memory_rdata_fsm;
  reg __memory_rdata_fsm_cond_11_0_1;
  assign memory_awaddr = uut_maxi_awaddr;
  assign memory_awlen = uut_maxi_awlen;
  assign memory_awsize = uut_maxi_awsize;
  assign memory_awburst = uut_maxi_awburst;
  assign memory_awlock = uut_maxi_awlock;
  assign memory_awcache = uut_maxi_awcache;
  assign memory_awprot = uut_maxi_awprot;
  assign memory_awqos = uut_maxi_awqos;
  assign memory_awuser = uut_maxi_awuser;
  assign memory_awvalid = uut_maxi_awvalid;
  wire _tmp_25;
  assign _tmp_25 = memory_awready;

  always @(*) begin
    uut_maxi_awready = _tmp_25;
  end

  assign memory_wdata = uut_maxi_wdata;
  assign memory_wstrb = uut_maxi_wstrb;
  assign memory_wlast = uut_maxi_wlast;
  assign memory_wvalid = uut_maxi_wvalid;
  wire _tmp_26;
  assign _tmp_26 = memory_wready;

  always @(*) begin
    uut_maxi_wready = _tmp_26;
  end

  wire [2-1:0] _tmp_27;
  assign _tmp_27 = memory_bresp;

  always @(*) begin
    uut_maxi_bresp = _tmp_27;
  end

  wire _tmp_28;
  assign _tmp_28 = memory_bvalid;

  always @(*) begin
    uut_maxi_bvalid = _tmp_28;
  end

  assign memory_bready = uut_maxi_bready;
  assign memory_araddr = uut_maxi_araddr;
  assign memory_arlen = uut_maxi_arlen;
  assign memory_arsize = uut_maxi_arsize;
  assign memory_arburst = uut_maxi_arburst;
  assign memory_arlock = uut_maxi_arlock;
  assign memory_arcache = uut_maxi_arcache;
  assign memory_arprot = uut_maxi_arprot;
  assign memory_arqos = uut_maxi_arqos;
  assign memory_aruser = uut_maxi_aruser;
  assign memory_arvalid = uut_maxi_arvalid;
  wire _tmp_29;
  assign _tmp_29 = memory_arready;

  always @(*) begin
    uut_maxi_arready = _tmp_29;
  end

  wire [32-1:0] _tmp_30;
  assign _tmp_30 = memory_rdata;

  always @(*) begin
    uut_maxi_rdata = _tmp_30;
  end

  wire [2-1:0] _tmp_31;
  assign _tmp_31 = memory_rresp;

  always @(*) begin
    uut_maxi_rresp = _tmp_31;
  end

  wire _tmp_32;
  assign _tmp_32 = memory_rlast;

  always @(*) begin
    uut_maxi_rlast = _tmp_32;
  end

  wire _tmp_33;
  assign _tmp_33 = memory_rvalid;

  always @(*) begin
    uut_maxi_rvalid = _tmp_33;
  end

  assign memory_rready = uut_maxi_rready;
  reg [32-1:0] _saxi_awaddr;
  wire [4-1:0] _saxi_awcache;
  wire [3-1:0] _saxi_awprot;
  reg _saxi_awvalid;
  wire _saxi_awready;
  assign _saxi_awcache = 3;
  assign _saxi_awprot = 0;
  wire [32-1:0] _saxi_wdata;
  wire [4-1:0] _saxi_wstrb;
  wire _saxi_wvalid;
  wire _saxi_wready;
  reg [32-1:0] __saxi_wdata_sb_0;
  reg [4-1:0] __saxi_wstrb_sb_0;
  reg __saxi_wvalid_sb_0;
  wire __saxi_wready_sb_0;
  wire [4-1:0] _sb__saxi_writedata_s_value_34;
  assign _sb__saxi_writedata_s_value_34 = __saxi_wstrb_sb_0;
  wire [32-1:0] _sb__saxi_writedata_s_value_35;
  assign _sb__saxi_writedata_s_value_35 = __saxi_wdata_sb_0;
  wire [36-1:0] _sb__saxi_writedata_s_data_36;
  assign _sb__saxi_writedata_s_data_36 = { _sb__saxi_writedata_s_value_34, _sb__saxi_writedata_s_value_35 };
  wire _sb__saxi_writedata_s_valid_37;
  assign _sb__saxi_writedata_s_valid_37 = __saxi_wvalid_sb_0;
  wire _sb__saxi_writedata_m_ready_38;
  assign _sb__saxi_writedata_m_ready_38 = _saxi_wready;
  reg [36-1:0] _sb__saxi_writedata_data_39;
  reg _sb__saxi_writedata_valid_40;
  wire _sb__saxi_writedata_ready_41;
  reg [36-1:0] _sb__saxi_writedata_tmp_data_42;
  reg _sb__saxi_writedata_tmp_valid_43;
  wire [36-1:0] _sb__saxi_writedata_next_data_44;
  wire _sb__saxi_writedata_next_valid_45;
  assign _sb__saxi_writedata_ready_41 = !_sb__saxi_writedata_tmp_valid_43;
  assign _sb__saxi_writedata_next_data_44 = (_sb__saxi_writedata_tmp_valid_43)? _sb__saxi_writedata_tmp_data_42 : _sb__saxi_writedata_s_data_36;
  assign _sb__saxi_writedata_next_valid_45 = _sb__saxi_writedata_tmp_valid_43 || _sb__saxi_writedata_s_valid_37;
  wire [4-1:0] _sb__saxi_writedata_m_value_46;
  assign _sb__saxi_writedata_m_value_46 = _sb__saxi_writedata_data_39[35:32];
  wire [32-1:0] _sb__saxi_writedata_m_value_47;
  assign _sb__saxi_writedata_m_value_47 = _sb__saxi_writedata_data_39[31:0];
  assign __saxi_wready_sb_0 = _sb__saxi_writedata_ready_41;
  assign _saxi_wdata = _sb__saxi_writedata_m_value_47;
  assign _saxi_wstrb = _sb__saxi_writedata_m_value_46;
  assign _saxi_wvalid = _sb__saxi_writedata_valid_40;
  wire [2-1:0] _saxi_bresp;
  wire _saxi_bvalid;
  wire _saxi_bready;
  assign _saxi_bready = 1;
  reg [32-1:0] _saxi_araddr;
  wire [4-1:0] _saxi_arcache;
  wire [3-1:0] _saxi_arprot;
  reg _saxi_arvalid;
  wire _saxi_arready;
  assign _saxi_arcache = 3;
  assign _saxi_arprot = 0;
  wire [32-1:0] _saxi_rdata;
  wire [2-1:0] _saxi_rresp;
  wire _saxi_rvalid;
  wire _saxi_rready;
  wire [32-1:0] __saxi_rdata_sb_0;
  wire __saxi_rvalid_sb_0;
  wire __saxi_rready_sb_0;
  wire [32-1:0] _sb__saxi_readdata_s_value_48;
  assign _sb__saxi_readdata_s_value_48 = _saxi_rdata;
  wire [32-1:0] _sb__saxi_readdata_s_data_49;
  assign _sb__saxi_readdata_s_data_49 = { _sb__saxi_readdata_s_value_48 };
  wire _sb__saxi_readdata_s_valid_50;
  assign _sb__saxi_readdata_s_valid_50 = _saxi_rvalid;
  wire _sb__saxi_readdata_m_ready_51;
  assign _sb__saxi_readdata_m_ready_51 = __saxi_rready_sb_0;
  reg [32-1:0] _sb__saxi_readdata_data_52;
  reg _sb__saxi_readdata_valid_53;
  wire _sb__saxi_readdata_ready_54;
  reg [32-1:0] _sb__saxi_readdata_tmp_data_55;
  reg _sb__saxi_readdata_tmp_valid_56;
  wire [32-1:0] _sb__saxi_readdata_next_data_57;
  wire _sb__saxi_readdata_next_valid_58;
  assign _sb__saxi_readdata_ready_54 = !_sb__saxi_readdata_tmp_valid_56;
  assign _sb__saxi_readdata_next_data_57 = (_sb__saxi_readdata_tmp_valid_56)? _sb__saxi_readdata_tmp_data_55 : _sb__saxi_readdata_s_data_49;
  assign _sb__saxi_readdata_next_valid_58 = _sb__saxi_readdata_tmp_valid_56 || _sb__saxi_readdata_s_valid_50;
  wire [32-1:0] _sb__saxi_readdata_m_value_59;
  assign _sb__saxi_readdata_m_value_59 = _sb__saxi_readdata_data_52[31:0];
  assign __saxi_rdata_sb_0 = _sb__saxi_readdata_m_value_59;
  assign __saxi_rvalid_sb_0 = _sb__saxi_readdata_valid_53;
  assign _saxi_rready = _sb__saxi_readdata_ready_54;
  reg [3-1:0] __saxi_outstanding_wcount;
  wire __saxi_has_outstanding_write;
  assign __saxi_has_outstanding_write = (__saxi_outstanding_wcount > 0) || _saxi_awvalid;
  wire [32-1:0] _tmp_60;
  assign _tmp_60 = _saxi_awaddr;

  always @(*) begin
    uut_saxi_awaddr = _tmp_60;
  end

  wire [4-1:0] _tmp_61;
  assign _tmp_61 = _saxi_awcache;

  always @(*) begin
    uut_saxi_awcache = _tmp_61;
  end

  wire [3-1:0] _tmp_62;
  assign _tmp_62 = _saxi_awprot;

  always @(*) begin
    uut_saxi_awprot = _tmp_62;
  end

  wire _tmp_63;
  assign _tmp_63 = _saxi_awvalid;

  always @(*) begin
    uut_saxi_awvalid = _tmp_63;
  end

  assign _saxi_awready = uut_saxi_awready;
  wire [32-1:0] _tmp_64;
  assign _tmp_64 = _saxi_wdata;

  always @(*) begin
    uut_saxi_wdata = _tmp_64;
  end

  wire [4-1:0] _tmp_65;
  assign _tmp_65 = _saxi_wstrb;

  always @(*) begin
    uut_saxi_wstrb = _tmp_65;
  end

  wire _tmp_66;
  assign _tmp_66 = _saxi_wvalid;

  always @(*) begin
    uut_saxi_wvalid = _tmp_66;
  end

  assign _saxi_wready = uut_saxi_wready;
  assign _saxi_bresp = uut_saxi_bresp;
  assign _saxi_bvalid = uut_saxi_bvalid;
  wire _tmp_67;
  assign _tmp_67 = _saxi_bready;

  always @(*) begin
    uut_saxi_bready = _tmp_67;
  end

  wire [32-1:0] _tmp_68;
  assign _tmp_68 = _saxi_araddr;

  always @(*) begin
    uut_saxi_araddr = _tmp_68;
  end

  wire [4-1:0] _tmp_69;
  assign _tmp_69 = _saxi_arcache;

  always @(*) begin
    uut_saxi_arcache = _tmp_69;
  end

  wire [3-1:0] _tmp_70;
  assign _tmp_70 = _saxi_arprot;

  always @(*) begin
    uut_saxi_arprot = _tmp_70;
  end

  wire _tmp_71;
  assign _tmp_71 = _saxi_arvalid;

  always @(*) begin
    uut_saxi_arvalid = _tmp_71;
  end

  assign _saxi_arready = uut_saxi_arready;
  assign _saxi_rdata = uut_saxi_rdata;
  assign _saxi_rresp = uut_saxi_rresp;
  assign _saxi_rvalid = uut_saxi_rvalid;
  wire _tmp_72;
  assign _tmp_72 = _saxi_rready;

  always @(*) begin
    uut_saxi_rready = _tmp_72;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_12;
  reg signed [32-1:0] _th_ctrl_awaddr_13;
  reg __saxi_waddr_cond_0_1;
  reg __saxi_wdata_cond_0_1;
  reg signed [32-1:0] _th_ctrl_src_offset_14;
  reg __saxi_waddr_cond_1_1;
  reg __saxi_wdata_cond_1_1;
  reg signed [32-1:0] _th_ctrl_dst_offset_15;
  reg __saxi_waddr_cond_2_1;
  reg __saxi_wdata_cond_2_1;
  reg signed [32-1:0] _th_ctrl_start_time_16;
  reg __saxi_waddr_cond_3_1;
  reg __saxi_wdata_cond_3_1;
  reg signed [32-1:0] _th_ctrl_araddr_17;
  reg __saxi_raddr_cond_0_1;
  reg signed [32-1:0] axim_rdata_73;
  assign __saxi_rready_sb_0 = th_ctrl == 39;
  reg signed [32-1:0] _th_ctrl_busy_18;
  reg signed [32-1:0] _th_ctrl_end_time_19;
  reg signed [32-1:0] _th_ctrl_time_20;

  initial begin
    $dumpfile("thread_verilog_submodule_ipxact.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    uut_CLK = 0;
    forever begin
      #5 uut_CLK = !uut_CLK;
    end
  end


  initial begin
    uut_RST = 0;
    memory_awready = 0;
    memory_bvalid = 0;
    memory_arready = 0;
    memory_rdata = 0;
    memory_rlast = 0;
    memory_rvalid = 0;
    _memory_waddr_fsm = _memory_waddr_fsm_init;
    _memory_wdata_fsm = _memory_wdata_fsm_init;
    _memory_raddr_fsm = _memory_raddr_fsm_init;
    _memory_rdata_fsm = _memory_rdata_fsm_init;
    count__memory_wreq_fifo = 0;
    count__memory_rreq_fifo = 0;
    count__memory_wdata_fifo = 0;
    __tmp_5_1 = 0;
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_interval_count = 0;
    _keep_sleep_count = 0;
    __tmp_10_1 = 0;
    __tmp_22_1 = 0;
    _d1__memory_rdata_fsm = _memory_rdata_fsm_init;
    __memory_rdata_fsm_cond_11_0_1 = 0;
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    __saxi_wdata_sb_0 = 0;
    __saxi_wstrb_sb_0 = 0;
    __saxi_wvalid_sb_0 = 0;
    _sb__saxi_writedata_data_39 = 0;
    _sb__saxi_writedata_valid_40 = 0;
    _sb__saxi_writedata_tmp_data_42 = 0;
    _sb__saxi_writedata_tmp_valid_43 = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    _sb__saxi_readdata_data_52 = 0;
    _sb__saxi_readdata_valid_53 = 0;
    _sb__saxi_readdata_tmp_data_55 = 0;
    _sb__saxi_readdata_tmp_valid_56 = 0;
    __saxi_outstanding_wcount = 0;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_12 = 0;
    _th_ctrl_awaddr_13 = 0;
    __saxi_waddr_cond_0_1 = 0;
    __saxi_wdata_cond_0_1 = 0;
    _th_ctrl_src_offset_14 = 0;
    __saxi_waddr_cond_1_1 = 0;
    __saxi_wdata_cond_1_1 = 0;
    _th_ctrl_dst_offset_15 = 0;
    __saxi_waddr_cond_2_1 = 0;
    __saxi_wdata_cond_2_1 = 0;
    _th_ctrl_start_time_16 = 0;
    __saxi_waddr_cond_3_1 = 0;
    __saxi_wdata_cond_3_1 = 0;
    _th_ctrl_araddr_17 = 0;
    __saxi_raddr_cond_0_1 = 0;
    axim_rdata_73 = 0;
    _th_ctrl_busy_18 = 0;
    _th_ctrl_end_time_19 = 0;
    _th_ctrl_time_20 = 0;
    #100;
    uut_RST = 1;
    #100;
    uut_RST = 0;
    #1000000;
    $finish;
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _keep_sleep_count <= 0;
      _sleep_interval_count <= 0;
    end else begin
      if(_sleep_interval_count == 15) begin
        _keep_sleep_count <= _keep_sleep_count + 1;
      end 
      if((_sleep_interval_count == 15) && (_keep_sleep_count == 3)) begin
        _keep_sleep_count <= 0;
      end 
      if(_sleep_interval_count < 15) begin
        _sleep_interval_count <= _sleep_interval_count + 1;
      end 
      if((_keep_sleep_count == 3) && (_sleep_interval_count == 15)) begin
        _sleep_interval_count <= 0;
      end 
      if((_memory_wdata_fsm == 1) && write_data_wvalid_16 && write_data_wready_17 && pack_write_data_wstrb_14[0]) begin
        _memory_mem[_write_addr + 0] <= pack_write_data_wdata_13[7:0];
      end 
      if((_memory_wdata_fsm == 1) && write_data_wvalid_16 && write_data_wready_17 && pack_write_data_wstrb_14[1]) begin
        _memory_mem[_write_addr + 1] <= pack_write_data_wdata_13[15:8];
      end 
      if((_memory_wdata_fsm == 1) && write_data_wvalid_16 && write_data_wready_17 && pack_write_data_wstrb_14[2]) begin
        _memory_mem[_write_addr + 2] <= pack_write_data_wdata_13[23:16];
      end 
      if((_memory_wdata_fsm == 1) && write_data_wvalid_16 && write_data_wready_17 && pack_write_data_wstrb_14[3]) begin
        _memory_mem[_write_addr + 3] <= pack_write_data_wdata_13[31:24];
      end 
    end
  end

  localparam _memory_waddr_fsm_1 = 1;
  localparam _memory_waddr_fsm_2 = 2;
  localparam _memory_waddr_fsm_3 = 3;
  localparam _memory_waddr_fsm_4 = 4;
  localparam _memory_waddr_fsm_5 = 5;
  localparam _memory_waddr_fsm_6 = 6;
  localparam _memory_waddr_fsm_7 = 7;
  localparam _memory_waddr_fsm_8 = 8;
  localparam _memory_waddr_fsm_9 = 9;
  localparam _memory_waddr_fsm_10 = 10;
  localparam _memory_waddr_fsm_11 = 11;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _memory_waddr_fsm <= _memory_waddr_fsm_init;
      memory_awready <= 0;
    end else begin
      case(_memory_waddr_fsm)
        _memory_waddr_fsm_init: begin
          memory_awready <= 0;
          if(memory_awvalid) begin
            _memory_waddr_fsm <= _memory_waddr_fsm_1;
          end 
        end
        _memory_waddr_fsm_1: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_2;
        end
        _memory_waddr_fsm_2: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_3;
        end
        _memory_waddr_fsm_3: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_4;
        end
        _memory_waddr_fsm_4: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_5;
        end
        _memory_waddr_fsm_5: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_6;
        end
        _memory_waddr_fsm_6: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_7;
        end
        _memory_waddr_fsm_7: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_8;
        end
        _memory_waddr_fsm_8: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_9;
        end
        _memory_waddr_fsm_9: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_10;
        end
        _memory_waddr_fsm_10: begin
          _memory_waddr_fsm <= _memory_waddr_fsm_11;
        end
        _memory_waddr_fsm_11: begin
          if(!_memory_wreq_fifo_almost_full) begin
            memory_awready <= 1;
          end 
          if(memory_awvalid && memory_awready) begin
            memory_awready <= 0;
          end 
          if(!memory_awvalid) begin
            _memory_waddr_fsm <= _memory_waddr_fsm_init;
          end 
          if(memory_awvalid && memory_awready) begin
            _memory_waddr_fsm <= _memory_waddr_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _memory_wdata_fsm_1 = 1;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _memory_wdata_fsm <= _memory_wdata_fsm_init;
      memory_bvalid <= 0;
      _write_addr <= 0;
      _write_count <= 0;
    end else begin
      case(_memory_wdata_fsm)
        _memory_wdata_fsm_init: begin
          memory_bvalid <= 0;
          if(!_memory_wreq_fifo_empty) begin
            _write_addr <= unpack_write_req_global_addr_11;
            _write_count <= unpack_write_req_size_12;
          end 
          if(!_memory_wreq_fifo_empty) begin
            _memory_wdata_fsm <= _memory_wdata_fsm_1;
          end 
        end
        _memory_wdata_fsm_1: begin
          if(write_data_wvalid_16 && write_data_wready_17) begin
            _write_addr <= _write_addr + 4;
            _write_count <= _write_count - 1;
          end 
          if(write_data_wvalid_16 && write_data_wready_17 && (_write_count == 1)) begin
            memory_bvalid <= 1;
          end 
          if(write_data_wvalid_16 && write_data_wready_17 && pack_write_data_wlast_15) begin
            memory_bvalid <= 1;
          end 
          if(write_data_wvalid_16 && write_data_wready_17 && (_write_count == 1)) begin
            _memory_wdata_fsm <= _memory_wdata_fsm_init;
          end 
          if(write_data_wvalid_16 && write_data_wready_17 && pack_write_data_wlast_15) begin
            _memory_wdata_fsm <= _memory_wdata_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _memory_raddr_fsm_1 = 1;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _memory_raddr_fsm <= _memory_raddr_fsm_init;
      memory_arready <= 0;
    end else begin
      case(_memory_raddr_fsm)
        _memory_raddr_fsm_init: begin
          memory_arready <= 0;
          if(memory_arvalid) begin
            _memory_raddr_fsm <= _memory_raddr_fsm_1;
          end 
        end
        _memory_raddr_fsm_1: begin
          if(!_memory_rreq_fifo_almost_full) begin
            memory_arready <= 1;
          end 
          if(memory_arvalid && memory_arready) begin
            memory_arready <= 0;
          end 
          if(!memory_arvalid) begin
            _memory_raddr_fsm <= _memory_raddr_fsm_init;
          end 
          if(memory_arvalid && memory_arready) begin
            _memory_raddr_fsm <= _memory_raddr_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _memory_rdata_fsm_1 = 1;
  localparam _memory_rdata_fsm_2 = 2;
  localparam _memory_rdata_fsm_3 = 3;
  localparam _memory_rdata_fsm_4 = 4;
  localparam _memory_rdata_fsm_5 = 5;
  localparam _memory_rdata_fsm_6 = 6;
  localparam _memory_rdata_fsm_7 = 7;
  localparam _memory_rdata_fsm_8 = 8;
  localparam _memory_rdata_fsm_9 = 9;
  localparam _memory_rdata_fsm_10 = 10;
  localparam _memory_rdata_fsm_11 = 11;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _memory_rdata_fsm <= _memory_rdata_fsm_init;
      _d1__memory_rdata_fsm <= _memory_rdata_fsm_init;
      _read_addr <= 0;
      _read_count <= 0;
      memory_rdata[7:0] <= (0 >> 0) & { 8{ 1'd1 } };
      memory_rdata[15:8] <= (0 >> 8) & { 8{ 1'd1 } };
      memory_rdata[23:16] <= (0 >> 16) & { 8{ 1'd1 } };
      memory_rdata[31:24] <= (0 >> 24) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_rdata_fsm_cond_11_0_1 <= 0;
      memory_rdata <= 0;
    end else begin
      _d1__memory_rdata_fsm <= _memory_rdata_fsm;
      case(_d1__memory_rdata_fsm)
        _memory_rdata_fsm_11: begin
          if(__memory_rdata_fsm_cond_11_0_1) begin
            memory_rvalid <= 0;
            memory_rlast <= 0;
          end 
        end
      endcase
      case(_memory_rdata_fsm)
        _memory_rdata_fsm_init: begin
          if(!_memory_rreq_fifo_empty) begin
            _read_addr <= unpack_read_req_global_addr_23;
            _read_count <= unpack_read_req_size_24;
          end 
          if(!_memory_rreq_fifo_empty) begin
            _memory_rdata_fsm <= _memory_rdata_fsm_1;
          end 
        end
        _memory_rdata_fsm_1: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_2;
        end
        _memory_rdata_fsm_2: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_3;
        end
        _memory_rdata_fsm_3: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_4;
        end
        _memory_rdata_fsm_4: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_5;
        end
        _memory_rdata_fsm_5: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_6;
        end
        _memory_rdata_fsm_6: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_7;
        end
        _memory_rdata_fsm_7: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_8;
        end
        _memory_rdata_fsm_8: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_9;
        end
        _memory_rdata_fsm_9: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_10;
        end
        _memory_rdata_fsm_10: begin
          _memory_rdata_fsm <= _memory_rdata_fsm_11;
        end
        _memory_rdata_fsm_11: begin
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[7:0] <= _memory_mem[_read_addr + 0];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[15:8] <= _memory_mem[_read_addr + 1];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[23:16] <= _memory_mem[_read_addr + 2];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[31:24] <= _memory_mem[_read_addr + 3];
          end 
          if((_sleep_interval_count < 15) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 4;
            _read_count <= _read_count - 1;
          end 
          if((_sleep_interval_count < 15) && (_read_count == 1) && memory_rready | !memory_rvalid) begin
            memory_rlast <= 1;
          end 
          __memory_rdata_fsm_cond_11_0_1 <= 1;
          if(memory_rvalid && !memory_rready) begin
            memory_rvalid <= memory_rvalid;
            memory_rdata <= memory_rdata;
            memory_rlast <= memory_rlast;
          end 
          if(memory_rvalid && memory_rready && (_read_count == 0)) begin
            _memory_rdata_fsm <= _memory_rdata_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      count__memory_wreq_fifo <= 0;
      __tmp_10_1 <= 0;
    end else begin
      if(_memory_wreq_fifo_enq && !_memory_wreq_fifo_full && (_memory_wreq_fifo_deq && !_memory_wreq_fifo_empty)) begin
        count__memory_wreq_fifo <= count__memory_wreq_fifo;
      end else if(_memory_wreq_fifo_enq && !_memory_wreq_fifo_full) begin
        count__memory_wreq_fifo <= count__memory_wreq_fifo + 1;
      end else if(_memory_wreq_fifo_deq && !_memory_wreq_fifo_empty) begin
        count__memory_wreq_fifo <= count__memory_wreq_fifo - 1;
      end 
      __tmp_10_1 <= _tmp_10;
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      count__memory_rreq_fifo <= 0;
      __tmp_22_1 <= 0;
    end else begin
      if(_memory_rreq_fifo_enq && !_memory_rreq_fifo_full && (_memory_rreq_fifo_deq && !_memory_rreq_fifo_empty)) begin
        count__memory_rreq_fifo <= count__memory_rreq_fifo;
      end else if(_memory_rreq_fifo_enq && !_memory_rreq_fifo_full) begin
        count__memory_rreq_fifo <= count__memory_rreq_fifo + 1;
      end else if(_memory_rreq_fifo_deq && !_memory_rreq_fifo_empty) begin
        count__memory_rreq_fifo <= count__memory_rreq_fifo - 1;
      end 
      __tmp_22_1 <= _tmp_22;
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      count__memory_wdata_fifo <= 0;
      __tmp_5_1 <= 0;
    end else begin
      if(_memory_wdata_fifo_enq && !_memory_wdata_fifo_full && (_memory_wdata_fifo_deq && !_memory_wdata_fifo_empty)) begin
        count__memory_wdata_fifo <= count__memory_wdata_fifo;
      end else if(_memory_wdata_fifo_enq && !_memory_wdata_fifo_full) begin
        count__memory_wdata_fifo <= count__memory_wdata_fifo + 1;
      end else if(_memory_wdata_fifo_deq && !_memory_wdata_fifo_empty) begin
        count__memory_wdata_fifo <= count__memory_wdata_fifo - 1;
      end 
      __tmp_5_1 <= _tmp_5;
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _saxi_awaddr <= 0;
      _saxi_awvalid <= 0;
      __saxi_waddr_cond_0_1 <= 0;
      __saxi_waddr_cond_1_1 <= 0;
      __saxi_waddr_cond_2_1 <= 0;
      __saxi_waddr_cond_3_1 <= 0;
    end else begin
      if(__saxi_waddr_cond_0_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_waddr_cond_1_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_waddr_cond_2_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_waddr_cond_3_1) begin
        _saxi_awvalid <= 0;
      end 
      if((th_ctrl == 6) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_13;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 14) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_13;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_1_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 22) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_13;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 30) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_13;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_3_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      __saxi_wdata_sb_0 <= 0;
      __saxi_wvalid_sb_0 <= 0;
      __saxi_wstrb_sb_0 <= 0;
      __saxi_wdata_cond_0_1 <= 0;
      __saxi_wdata_cond_1_1 <= 0;
      __saxi_wdata_cond_2_1 <= 0;
      __saxi_wdata_cond_3_1 <= 0;
    end else begin
      if(__saxi_wdata_cond_0_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if(__saxi_wdata_cond_1_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if(__saxi_wdata_cond_2_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if(__saxi_wdata_cond_3_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if((th_ctrl == 8) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= 4096;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_0_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
      if((th_ctrl == 16) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= _th_ctrl_src_offset_14;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_1_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
      if((th_ctrl == 24) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= _th_ctrl_dst_offset_15;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_2_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
      if((th_ctrl == 32) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= 1;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_3_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _sb__saxi_writedata_data_39 <= 0;
      _sb__saxi_writedata_valid_40 <= 0;
      _sb__saxi_writedata_tmp_data_42 <= 0;
      _sb__saxi_writedata_tmp_valid_43 <= 0;
    end else begin
      if(_sb__saxi_writedata_m_ready_38 || !_sb__saxi_writedata_valid_40) begin
        _sb__saxi_writedata_data_39 <= _sb__saxi_writedata_next_data_44;
        _sb__saxi_writedata_valid_40 <= _sb__saxi_writedata_next_valid_45;
      end 
      if(!_sb__saxi_writedata_tmp_valid_43 && _sb__saxi_writedata_valid_40 && !_sb__saxi_writedata_m_ready_38) begin
        _sb__saxi_writedata_tmp_data_42 <= _sb__saxi_writedata_s_data_36;
        _sb__saxi_writedata_tmp_valid_43 <= _sb__saxi_writedata_s_valid_37;
      end 
      if(_sb__saxi_writedata_tmp_valid_43 && _sb__saxi_writedata_m_ready_38) begin
        _sb__saxi_writedata_tmp_valid_43 <= 0;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_raddr_cond_0_1 <= 0;
    end else begin
      if(__saxi_raddr_cond_0_1) begin
        _saxi_arvalid <= 0;
      end 
      if((th_ctrl == 37) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_17;
        _saxi_arvalid <= 1;
      end 
      __saxi_raddr_cond_0_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      _sb__saxi_readdata_data_52 <= 0;
      _sb__saxi_readdata_valid_53 <= 0;
      _sb__saxi_readdata_tmp_data_55 <= 0;
      _sb__saxi_readdata_tmp_valid_56 <= 0;
    end else begin
      if(_sb__saxi_readdata_m_ready_51 || !_sb__saxi_readdata_valid_53) begin
        _sb__saxi_readdata_data_52 <= _sb__saxi_readdata_next_data_57;
        _sb__saxi_readdata_valid_53 <= _sb__saxi_readdata_next_valid_58;
      end 
      if(!_sb__saxi_readdata_tmp_valid_56 && _sb__saxi_readdata_valid_53 && !_sb__saxi_readdata_m_ready_51) begin
        _sb__saxi_readdata_tmp_data_55 <= _sb__saxi_readdata_s_data_49;
        _sb__saxi_readdata_tmp_valid_56 <= _sb__saxi_readdata_s_valid_50;
      end 
      if(_sb__saxi_readdata_tmp_valid_56 && _sb__saxi_readdata_m_ready_51) begin
        _sb__saxi_readdata_tmp_valid_56 <= 0;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      __saxi_outstanding_wcount <= 0;
    end else begin
      if(_saxi_awvalid && _saxi_awready && !(_saxi_bvalid && _saxi_bready) && (__saxi_outstanding_wcount < 7)) begin
        __saxi_outstanding_wcount <= __saxi_outstanding_wcount + 1;
      end 
      if(!(_saxi_awvalid && _saxi_awready) && (_saxi_bvalid && _saxi_bready) && (__saxi_outstanding_wcount > 0)) begin
        __saxi_outstanding_wcount <= __saxi_outstanding_wcount - 1;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      counter <= 0;
    end else begin
      counter <= counter + 1;
    end
  end

  localparam th_ctrl_1 = 1;
  localparam th_ctrl_2 = 2;
  localparam th_ctrl_3 = 3;
  localparam th_ctrl_4 = 4;
  localparam th_ctrl_5 = 5;
  localparam th_ctrl_6 = 6;
  localparam th_ctrl_7 = 7;
  localparam th_ctrl_8 = 8;
  localparam th_ctrl_9 = 9;
  localparam th_ctrl_10 = 10;
  localparam th_ctrl_11 = 11;
  localparam th_ctrl_12 = 12;
  localparam th_ctrl_13 = 13;
  localparam th_ctrl_14 = 14;
  localparam th_ctrl_15 = 15;
  localparam th_ctrl_16 = 16;
  localparam th_ctrl_17 = 17;
  localparam th_ctrl_18 = 18;
  localparam th_ctrl_19 = 19;
  localparam th_ctrl_20 = 20;
  localparam th_ctrl_21 = 21;
  localparam th_ctrl_22 = 22;
  localparam th_ctrl_23 = 23;
  localparam th_ctrl_24 = 24;
  localparam th_ctrl_25 = 25;
  localparam th_ctrl_26 = 26;
  localparam th_ctrl_27 = 27;
  localparam th_ctrl_28 = 28;
  localparam th_ctrl_29 = 29;
  localparam th_ctrl_30 = 30;
  localparam th_ctrl_31 = 31;
  localparam th_ctrl_32 = 32;
  localparam th_ctrl_33 = 33;
  localparam th_ctrl_34 = 34;
  localparam th_ctrl_35 = 35;
  localparam th_ctrl_36 = 36;
  localparam th_ctrl_37 = 37;
  localparam th_ctrl_38 = 38;
  localparam th_ctrl_39 = 39;
  localparam th_ctrl_40 = 40;
  localparam th_ctrl_41 = 41;
  localparam th_ctrl_42 = 42;
  localparam th_ctrl_43 = 43;
  localparam th_ctrl_44 = 44;
  localparam th_ctrl_45 = 45;
  localparam th_ctrl_46 = 46;
  localparam th_ctrl_47 = 47;
  localparam th_ctrl_48 = 48;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_12 <= 0;
      _th_ctrl_awaddr_13 <= 0;
      _th_ctrl_src_offset_14 <= 0;
      _th_ctrl_dst_offset_15 <= 0;
      _th_ctrl_start_time_16 <= 0;
      _th_ctrl_araddr_17 <= 0;
      axim_rdata_73 <= 0;
      _th_ctrl_busy_18 <= 0;
      _th_ctrl_end_time_19 <= 0;
      _th_ctrl_time_20 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_12 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_12 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_12 <= _th_ctrl_i_12 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_13 <= 8;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          $display("# copy_bytes = %d", 4096);
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_7;
          end 
        end
        th_ctrl_7: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_8;
          end 
        end
        th_ctrl_8: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_10;
          end 
        end
        th_ctrl_10: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_11;
          end 
        end
        th_ctrl_11: begin
          _th_ctrl_awaddr_13 <= 12;
          th_ctrl <= th_ctrl_12;
        end
        th_ctrl_12: begin
          _th_ctrl_src_offset_14 <= 0;
          th_ctrl <= th_ctrl_13;
        end
        th_ctrl_13: begin
          $display("# src_offset = %d", _th_ctrl_src_offset_14);
          th_ctrl <= th_ctrl_14;
        end
        th_ctrl_14: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_15;
          end 
        end
        th_ctrl_15: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_16;
          end 
        end
        th_ctrl_16: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_17;
          end 
        end
        th_ctrl_17: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_18;
          end 
        end
        th_ctrl_18: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          _th_ctrl_awaddr_13 <= 16;
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          _th_ctrl_dst_offset_15 <= 8192;
          th_ctrl <= th_ctrl_21;
        end
        th_ctrl_21: begin
          $display("# dst_offset = %d", _th_ctrl_dst_offset_15);
          th_ctrl <= th_ctrl_22;
        end
        th_ctrl_22: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_23;
          end 
        end
        th_ctrl_23: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_24;
          end 
        end
        th_ctrl_24: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_25;
          end 
        end
        th_ctrl_25: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_26;
          end 
        end
        th_ctrl_26: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_27;
          end 
        end
        th_ctrl_27: begin
          _th_ctrl_awaddr_13 <= 0;
          th_ctrl <= th_ctrl_28;
        end
        th_ctrl_28: begin
          _th_ctrl_start_time_16 <= counter;
          th_ctrl <= th_ctrl_29;
        end
        th_ctrl_29: begin
          $display("# start time = %d", _th_ctrl_start_time_16);
          th_ctrl <= th_ctrl_30;
        end
        th_ctrl_30: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_31;
          end 
        end
        th_ctrl_31: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_32;
          end 
        end
        th_ctrl_32: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_33;
          end 
        end
        th_ctrl_33: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_34;
          end 
        end
        th_ctrl_34: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_35;
          end 
        end
        th_ctrl_35: begin
          _th_ctrl_araddr_17 <= 4;
          th_ctrl <= th_ctrl_36;
        end
        th_ctrl_36: begin
          if(1) begin
            th_ctrl <= th_ctrl_37;
          end else begin
            th_ctrl <= th_ctrl_44;
          end
        end
        th_ctrl_37: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_38;
          end 
        end
        th_ctrl_38: begin
          if(_saxi_arvalid && _saxi_arready) begin
            th_ctrl <= th_ctrl_39;
          end 
        end
        th_ctrl_39: begin
          if(__saxi_rvalid_sb_0) begin
            axim_rdata_73 <= __saxi_rdata_sb_0;
          end 
          if(__saxi_rvalid_sb_0) begin
            th_ctrl <= th_ctrl_40;
          end 
        end
        th_ctrl_40: begin
          _th_ctrl_busy_18 <= axim_rdata_73;
          th_ctrl <= th_ctrl_41;
        end
        th_ctrl_41: begin
          if(!_th_ctrl_busy_18) begin
            th_ctrl <= th_ctrl_42;
          end else begin
            th_ctrl <= th_ctrl_43;
          end
        end
        th_ctrl_42: begin
          th_ctrl <= th_ctrl_44;
        end
        th_ctrl_43: begin
          th_ctrl <= th_ctrl_36;
        end
        th_ctrl_44: begin
          _th_ctrl_end_time_19 <= counter;
          th_ctrl <= th_ctrl_45;
        end
        th_ctrl_45: begin
          $display("# end time = %d", _th_ctrl_end_time_19);
          th_ctrl <= th_ctrl_46;
        end
        th_ctrl_46: begin
          _th_ctrl_time_20 <= _th_ctrl_end_time_19 - _th_ctrl_start_time_16;
          th_ctrl <= th_ctrl_47;
        end
        th_ctrl_47: begin
          $display("# exec time = %d", _th_ctrl_time_20);
          th_ctrl <= th_ctrl_48;
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] led,
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
  input saxi_rready
);

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
  reg start;
  wire busy;
  reg [10-1:0] size;
  localparam pe_ADDR_WIDTH = 10;
  localparam pe_DATA_WIDTH = 32;
  wire [pe_ADDR_WIDTH-1+1-1:0] pe_addr;
  wire [pe_DATA_WIDTH-1+1-1:0] pe_rdata;
  wire [pe_DATA_WIDTH-1+1-1:0] pe_wdata;
  wire pe_wenable;

  processing_unit
  #(
    .ADDR_WIDTH(pe_ADDR_WIDTH),
    .DATA_WIDTH(pe_DATA_WIDTH)
  )
  inst_pe
  (
    .CLK(CLK),
    .RST(RST),
    .start(start),
    .busy(busy),
    .size(size),
    .addr(pe_addr),
    .rdata(pe_rdata),
    .wdata(pe_wdata),
    .wenable(pe_wenable)
  );

  assign ram_a_1_addr = pe_addr;
  assign ram_a_1_wdata = pe_wdata;
  assign ram_a_1_wenable = pe_wenable;
  assign pe_rdata = ram_a_1_rdata;
  assign ram_a_1_enable = 1;
  reg [32-1:0] th_memcpy;
  localparam th_memcpy_init = 0;
  reg signed [32-1:0] _th_memcpy_copy_bytes_0;
  reg signed [32-1:0] _th_memcpy_src_offset_1;
  reg signed [32-1:0] _th_memcpy_dst_offset_2;
  reg signed [32-1:0] _th_memcpy_copy_bytes_3;
  reg signed [32-1:0] _th_memcpy_src_offset_4;
  reg signed [32-1:0] _th_memcpy_dst_offset_5;
  reg signed [32-1:0] _th_memcpy_rest_words_6;
  reg signed [32-1:0] _th_memcpy_src_global_addr_7;
  reg signed [32-1:0] _th_memcpy_dst_global_addr_8;
  reg signed [32-1:0] _th_memcpy_local_addr_9;
  reg signed [32-1:0] _th_memcpy_dma_size_10;
  wire [32-1:0] mask_addr_shifted_49;
  assign mask_addr_shifted_49 = _th_memcpy_src_global_addr_7 >> 2;
  wire [32-1:0] mask_addr_masked_50;
  assign mask_addr_masked_50 = mask_addr_shifted_49 << 2;
  reg [32-1:0] _maxi_read_req_fsm;
  localparam _maxi_read_req_fsm_init = 0;
  reg [33-1:0] _maxi_read_cur_global_size;
  reg _maxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_51;
  wire [32-1:0] pack_read_req_local_addr_52;
  wire [32-1:0] pack_read_req_local_stride_53;
  wire [33-1:0] pack_read_req_local_size_54;
  wire [32-1:0] pack_read_req_local_blocksize_55;
  assign pack_read_req_op_sel_51 = _maxi_read_op_sel;
  assign pack_read_req_local_addr_52 = _maxi_read_local_addr;
  assign pack_read_req_local_stride_53 = _maxi_read_local_stride;
  assign pack_read_req_local_size_54 = _maxi_read_local_size;
  assign pack_read_req_local_blocksize_55 = _maxi_read_local_blocksize;
  wire [137-1:0] pack_read_req_packed_56;
  assign pack_read_req_packed_56 = { pack_read_req_op_sel_51, pack_read_req_local_addr_52, pack_read_req_local_stride_53, pack_read_req_local_size_54, pack_read_req_local_blocksize_55 };
  assign _maxi_read_req_fifo_wdata = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? pack_read_req_packed_56 : 'hx;
  assign _maxi_read_req_fifo_enq = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? (_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full && !_maxi_read_req_fifo_almost_full : 0;
  localparam _tmp_57 = 1;
  wire [_tmp_57-1:0] _tmp_58;
  assign _tmp_58 = !_maxi_read_req_fifo_almost_full;
  reg [_tmp_57-1:0] __tmp_58_1;
  wire [32-1:0] mask_addr_shifted_59;
  assign mask_addr_shifted_59 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_60;
  assign mask_addr_masked_60 = mask_addr_shifted_59 << 2;
  wire [32-1:0] mask_addr_shifted_61;
  assign mask_addr_shifted_61 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_62;
  assign mask_addr_masked_62 = mask_addr_shifted_61 << 2;
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
  reg _maxi_raddr_cond_0_1;
  reg [32-1:0] _maxi_read_data_fsm;
  localparam _maxi_read_data_fsm_init = 0;
  assign _maxi_read_req_fifo_deq = ((_maxi_read_data_fsm == 0) && (!_maxi_read_data_busy && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) && !_maxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_71;
  reg [10-1:0] write_burst_stride_72;
  reg [33-1:0] write_burst_length_73;
  reg write_burst_done_74;
  assign ram_a_0_wdata = ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? _maxi_rdata_sb_0 : 'hx;
  assign ram_a_0_wenable = ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? 1'd1 : 0;
  assign _maxi_rready_sb_0 = _maxi_read_data_fsm == 2;
  reg signed [32-1:0] _th_memcpy_v_11;
  wire [32-1:0] mask_addr_shifted_75;
  assign mask_addr_shifted_75 = _th_memcpy_dst_global_addr_8 >> 2;
  wire [32-1:0] mask_addr_masked_76;
  assign mask_addr_masked_76 = mask_addr_shifted_75 << 2;
  reg [32-1:0] _maxi_write_req_fsm;
  localparam _maxi_write_req_fsm_init = 0;
  reg [33-1:0] _maxi_write_cur_global_size;
  reg _maxi_write_cont;
  wire [8-1:0] pack_write_req_op_sel_77;
  wire [32-1:0] pack_write_req_local_addr_78;
  wire [32-1:0] pack_write_req_local_stride_79;
  wire [33-1:0] pack_write_req_size_80;
  wire [32-1:0] pack_write_req_local_blocksize_81;
  assign pack_write_req_op_sel_77 = _maxi_write_op_sel;
  assign pack_write_req_local_addr_78 = _maxi_write_local_addr;
  assign pack_write_req_local_stride_79 = _maxi_write_local_stride;
  assign pack_write_req_size_80 = _maxi_write_local_size;
  assign pack_write_req_local_blocksize_81 = _maxi_write_local_blocksize;
  wire [137-1:0] pack_write_req_packed_82;
  assign pack_write_req_packed_82 = { pack_write_req_op_sel_77, pack_write_req_local_addr_78, pack_write_req_local_stride_79, pack_write_req_size_80, pack_write_req_local_blocksize_81 };
  localparam _tmp_83 = 1;
  wire [_tmp_83-1:0] _tmp_84;
  assign _tmp_84 = !_maxi_write_req_fifo_almost_full;
  reg [_tmp_83-1:0] __tmp_84_1;
  wire [32-1:0] mask_addr_shifted_85;
  assign mask_addr_shifted_85 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_86;
  assign mask_addr_masked_86 = mask_addr_shifted_85 << 2;
  wire [32-1:0] mask_addr_shifted_87;
  assign mask_addr_shifted_87 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_88;
  assign mask_addr_masked_88 = mask_addr_shifted_87 << 2;
  wire [32-1:0] mask_addr_shifted_89;
  assign mask_addr_shifted_89 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_90;
  assign mask_addr_masked_90 = mask_addr_shifted_89 << 2;
  wire [32-1:0] mask_addr_shifted_91;
  assign mask_addr_shifted_91 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_92;
  assign mask_addr_masked_92 = mask_addr_shifted_91 << 2;
  wire [32-1:0] mask_addr_shifted_93;
  assign mask_addr_shifted_93 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_94;
  assign mask_addr_masked_94 = mask_addr_shifted_93 << 2;
  wire [32-1:0] mask_addr_shifted_95;
  assign mask_addr_shifted_95 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_96;
  assign mask_addr_masked_96 = mask_addr_shifted_95 << 2;
  wire [8-1:0] pack_write_req_op_sel_97;
  wire [32-1:0] pack_write_req_local_addr_98;
  wire [32-1:0] pack_write_req_local_stride_99;
  wire [33-1:0] pack_write_req_size_100;
  wire [32-1:0] pack_write_req_local_blocksize_101;
  assign pack_write_req_op_sel_97 = _maxi_write_op_sel;
  assign pack_write_req_local_addr_98 = _maxi_write_local_addr;
  assign pack_write_req_local_stride_99 = _maxi_write_local_stride;
  assign pack_write_req_size_100 = _maxi_write_cur_global_size;
  assign pack_write_req_local_blocksize_101 = _maxi_write_local_blocksize;
  wire [137-1:0] pack_write_req_packed_102;
  assign pack_write_req_packed_102 = { pack_write_req_op_sel_97, pack_write_req_local_addr_98, pack_write_req_local_stride_99, pack_write_req_size_100, pack_write_req_local_blocksize_101 };
  assign _maxi_write_req_fifo_wdata = ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6))? pack_write_req_packed_102 : 
                                      ((_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full)? pack_write_req_packed_82 : 'hx;
  assign _maxi_write_req_fifo_enq = ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6))? (_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6) && !_maxi_write_req_fifo_almost_full : 
                                    ((_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full)? (_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full && !_maxi_write_req_fifo_almost_full : 0;
  localparam _tmp_103 = 1;
  wire [_tmp_103-1:0] _tmp_104;
  assign _tmp_104 = !_maxi_write_req_fifo_almost_full;
  reg [_tmp_103-1:0] __tmp_104_1;
  reg _maxi_waddr_cond_0_1;
  reg [32-1:0] _maxi_write_data_fsm;
  localparam _maxi_write_data_fsm_init = 0;
  reg [32-1:0] read_burst_fsm_1;
  localparam read_burst_fsm_1_init = 0;
  reg [10-1:0] read_burst_addr_105;
  reg [10-1:0] read_burst_stride_106;
  reg [33-1:0] read_burst_length_107;
  reg read_burst_rvalid_108;
  reg read_burst_rlast_109;
  assign ram_a_0_addr = ((read_burst_fsm_1 == 1) && (!read_burst_rvalid_108 || (_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0)))? read_burst_addr_105 : 
                        ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? write_burst_addr_71 : 'hx;
  assign ram_a_0_enable = ((read_burst_fsm_1 == 1) && (!read_burst_rvalid_108 || (_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0)))? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && _maxi_rvalid_sb_0)? 1'd1 : 0;
  localparam _tmp_110 = 1;
  wire [_tmp_110-1:0] _tmp_111;
  assign _tmp_111 = (read_burst_fsm_1 == 1) && (!read_burst_rvalid_108 || (_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0));
  reg [_tmp_110-1:0] __tmp_111_1;
  wire [32-1:0] read_burst_rdata_112;
  assign read_burst_rdata_112 = ram_a_0_rdata;
  assign _maxi_write_req_fifo_deq = ((_maxi_write_data_fsm == 2) && (!_maxi_write_req_fifo_empty && (_maxi_write_size_buf == 0)) && !_maxi_write_req_fifo_empty)? 1 : 
                                    ((_maxi_write_data_fsm == 0) && (!_maxi_write_data_busy && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1)) && !_maxi_write_req_fifo_empty)? 1 : 0;
  reg _maxi_wdata_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_111_1 <= 0;
    end else begin
      __tmp_111_1 <= _tmp_111;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      _maxi_waddr_cond_0_1 <= 0;
    end else begin
      if(_maxi_waddr_cond_0_1) begin
        maxi_awvalid <= 0;
      end 
      if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (_maxi_outstanding_wcount < 6) && ((_maxi_outstanding_wcount < 6) && (maxi_awready || !maxi_awvalid))) begin
        maxi_awaddr <= _maxi_write_global_addr;
        maxi_awlen <= _maxi_write_cur_global_size - 1;
        maxi_awvalid <= 1;
      end 
      if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (_maxi_outstanding_wcount < 6) && ((_maxi_outstanding_wcount < 6) && (maxi_awready || !maxi_awvalid)) && (_maxi_write_cur_global_size == 0)) begin
        maxi_awvalid <= 0;
      end 
      _maxi_waddr_cond_0_1 <= 1;
      if(maxi_awvalid && !maxi_awready) begin
        maxi_awvalid <= maxi_awvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _maxi_wdata_sb_0 <= 0;
      _maxi_wvalid_sb_0 <= 0;
      _maxi_wlast_sb_0 <= 0;
      _maxi_wstrb_sb_0 <= 0;
      _maxi_wdata_cond_0_1 <= 0;
    end else begin
      if(_maxi_wdata_cond_0_1) begin
        _maxi_wvalid_sb_0 <= 0;
        _maxi_wlast_sb_0 <= 0;
      end 
      if((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_108 && ((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0)) && (_maxi_wready_sb_0 || !_maxi_wvalid_sb_0)) begin
        _maxi_wdata_sb_0 <= read_burst_rdata_112;
        _maxi_wvalid_sb_0 <= 1;
        _maxi_wlast_sb_0 <= read_burst_rlast_109 || (_maxi_write_size_buf == 1);
        _maxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      _maxi_wdata_cond_0_1 <= 1;
      if(_maxi_wvalid_sb_0 && !_maxi_wready_sb_0) begin
        _maxi_wvalid_sb_0 <= _maxi_wvalid_sb_0;
        _maxi_wlast_sb_0 <= _maxi_wlast_sb_0;
      end 
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
      _maxi_write_op_sel <= 0;
      _maxi_write_global_addr <= 0;
      _maxi_write_global_size <= 0;
      _maxi_write_local_addr <= 0;
      _maxi_write_local_stride <= 0;
      _maxi_write_local_size <= 0;
      _maxi_write_local_blocksize <= 0;
      _maxi_write_req_busy <= 0;
      _maxi_write_cur_global_size <= 0;
      _maxi_write_data_busy <= 0;
      _maxi_write_op_sel_buf <= 0;
      _maxi_write_local_addr_buf <= 0;
      _maxi_write_local_stride_buf <= 0;
      _maxi_write_size_buf <= 0;
      _maxi_write_local_blocksize_buf <= 0;
    end else begin
      if(maxi_awvalid && maxi_awready && !(maxi_bvalid && maxi_bready) && (_maxi_outstanding_wcount < 7)) begin
        _maxi_outstanding_wcount <= _maxi_outstanding_wcount + 1;
      end 
      if(!(maxi_awvalid && maxi_awready) && (maxi_bvalid && maxi_bready) && (_maxi_outstanding_wcount > 0)) begin
        _maxi_outstanding_wcount <= _maxi_outstanding_wcount - 1;
      end 
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      if((th_memcpy == 17) && _maxi_read_req_idle) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= 1;
        _maxi_read_global_addr <= mask_addr_masked_50;
        _maxi_read_global_size <= _th_memcpy_dma_size_10;
        _maxi_read_local_addr <= _th_memcpy_local_addr_9;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_memcpy_dma_size_10;
        _maxi_read_local_blocksize <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && _maxi_read_start) begin
        _maxi_read_req_busy <= 1;
      end 
      if(_maxi_read_start && _maxi_read_req_fifo_almost_full) begin
        _maxi_read_start <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256) && ((mask_addr_masked_60 & 4095) + (_maxi_read_global_size << 2) >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_62 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_64 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256)) begin
        _maxi_read_cur_global_size <= _maxi_read_global_size;
        _maxi_read_global_size <= 0;
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && ((mask_addr_masked_66 & 4095) + 1024 >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_68 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_70 & 4095) >> 2);
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
      if((th_memcpy == 25) && _maxi_write_req_idle) begin
        _maxi_write_start <= 1;
        _maxi_write_op_sel <= 1;
        _maxi_write_global_addr <= mask_addr_masked_76;
        _maxi_write_global_size <= _th_memcpy_dma_size_10;
        _maxi_write_local_addr <= _th_memcpy_local_addr_9;
        _maxi_write_local_stride <= 1;
        _maxi_write_local_size <= _th_memcpy_dma_size_10;
        _maxi_write_local_blocksize <= 1;
      end 
      if((_maxi_write_req_fsm == 0) && _maxi_write_start) begin
        _maxi_write_req_busy <= 1;
      end 
      if(_maxi_write_start && _maxi_write_req_fifo_almost_full) begin
        _maxi_write_start <= 1;
      end 
      if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && (_maxi_write_global_size <= 256) && ((mask_addr_masked_86 & 4095) + (_maxi_write_global_size << 2) >= 4096)) begin
        _maxi_write_cur_global_size <= 4096 - (mask_addr_masked_88 & 4095) >> 2;
        _maxi_write_global_size <= _maxi_write_global_size - (4096 - (mask_addr_masked_90 & 4095) >> 2);
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && (_maxi_write_global_size <= 256)) begin
        _maxi_write_cur_global_size <= _maxi_write_global_size;
        _maxi_write_global_size <= 0;
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && ((mask_addr_masked_92 & 4095) + 1024 >= 4096)) begin
        _maxi_write_cur_global_size <= 4096 - (mask_addr_masked_94 & 4095) >> 2;
        _maxi_write_global_size <= _maxi_write_global_size - (4096 - (mask_addr_masked_96 & 4095) >> 2);
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full) begin
        _maxi_write_cur_global_size <= 256;
        _maxi_write_global_size <= _maxi_write_global_size - 256;
      end 
      if((_maxi_write_req_fsm == 1) && ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6))) begin
        _maxi_write_global_addr <= _maxi_write_global_addr + (_maxi_write_cur_global_size << 2);
      end 
      if((_maxi_write_req_fsm == 1) && ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6)) && (_maxi_write_global_size == 0)) begin
        _maxi_write_req_busy <= 0;
      end 
      if((_maxi_write_data_fsm == 0) && (!_maxi_write_data_busy && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1))) begin
        _maxi_write_data_busy <= 1;
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
      if((_maxi_write_data_fsm == 2) && read_burst_rvalid_108 && ((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0))) begin
        _maxi_write_size_buf <= _maxi_write_size_buf - 1;
      end 
      if((_maxi_write_data_fsm == 2) && ((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_108 && ((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0))) && read_burst_rlast_109) begin
        _maxi_write_data_busy <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_read_req_fifo <= 0;
      __tmp_58_1 <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full && (_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty)) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo;
      end else if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo + 1;
      end else if(_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo - 1;
      end 
      __tmp_58_1 <= _tmp_58;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_write_req_fifo <= 0;
      __tmp_84_1 <= 0;
      __tmp_104_1 <= 0;
    end else begin
      if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full && (_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty)) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo;
      end else if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo + 1;
      end else if(_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo - 1;
      end 
      __tmp_84_1 <= _tmp_84;
      __tmp_104_1 <= _tmp_104;
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
      if((th_memcpy == 31) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_memcpy == 31) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_memcpy == 31) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_memcpy == 31) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_memcpy == 31) && 0) begin
        _saxi_register_4 <= 0;
        _saxi_flag_4 <= 0;
      end 
      if((th_memcpy == 31) && 0) begin
        _saxi_register_5 <= 0;
        _saxi_flag_5 <= 0;
      end 
      if((th_memcpy == 31) && 0) begin
        _saxi_register_6 <= 0;
        _saxi_flag_6 <= 0;
      end 
      if((th_memcpy == 31) && 0) begin
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
  localparam th_memcpy_28 = 28;
  localparam th_memcpy_29 = 29;
  localparam th_memcpy_30 = 30;
  localparam th_memcpy_31 = 31;
  localparam th_memcpy_32 = 32;
  localparam th_memcpy_33 = 33;

  always @(posedge CLK) begin
    if(RST) begin
      th_memcpy <= th_memcpy_init;
      _th_memcpy_copy_bytes_0 <= 0;
      _th_memcpy_src_offset_1 <= 0;
      _th_memcpy_dst_offset_2 <= 0;
      _th_memcpy_copy_bytes_3 <= 0;
      _th_memcpy_src_offset_4 <= 0;
      _th_memcpy_dst_offset_5 <= 0;
      _th_memcpy_rest_words_6 <= 0;
      _th_memcpy_src_global_addr_7 <= 0;
      _th_memcpy_dst_global_addr_8 <= 0;
      _th_memcpy_local_addr_9 <= 0;
      _th_memcpy_dma_size_10 <= 0;
      _th_memcpy_v_11 <= 0;
      size <= 0;
      start <= 0;
    end else begin
      case(th_memcpy)
        th_memcpy_init: begin
          th_memcpy <= th_memcpy_1;
        end
        th_memcpy_1: begin
          if(1) begin
            th_memcpy <= th_memcpy_2;
          end else begin
            th_memcpy <= th_memcpy_33;
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
          _th_memcpy_copy_bytes_0 <= _saxi_register_2;
          th_memcpy <= th_memcpy_5;
        end
        th_memcpy_5: begin
          _th_memcpy_src_offset_1 <= _saxi_register_3;
          th_memcpy <= th_memcpy_6;
        end
        th_memcpy_6: begin
          _th_memcpy_dst_offset_2 <= _saxi_register_4;
          th_memcpy <= th_memcpy_7;
        end
        th_memcpy_7: begin
          _th_memcpy_copy_bytes_3 <= _th_memcpy_copy_bytes_0;
          _th_memcpy_src_offset_4 <= _th_memcpy_src_offset_1;
          _th_memcpy_dst_offset_5 <= _th_memcpy_dst_offset_2;
          th_memcpy <= th_memcpy_8;
        end
        th_memcpy_8: begin
          _th_memcpy_rest_words_6 <= _th_memcpy_copy_bytes_3 >>> 2;
          th_memcpy <= th_memcpy_9;
        end
        th_memcpy_9: begin
          _th_memcpy_src_global_addr_7 <= _th_memcpy_src_offset_4;
          th_memcpy <= th_memcpy_10;
        end
        th_memcpy_10: begin
          _th_memcpy_dst_global_addr_8 <= _th_memcpy_dst_offset_5;
          th_memcpy <= th_memcpy_11;
        end
        th_memcpy_11: begin
          _th_memcpy_local_addr_9 <= 0;
          th_memcpy <= th_memcpy_12;
        end
        th_memcpy_12: begin
          if(_th_memcpy_rest_words_6 > 0) begin
            th_memcpy <= th_memcpy_13;
          end else begin
            th_memcpy <= th_memcpy_31;
          end
        end
        th_memcpy_13: begin
          if(_th_memcpy_rest_words_6 > 256) begin
            th_memcpy <= th_memcpy_14;
          end else begin
            th_memcpy <= th_memcpy_16;
          end
        end
        th_memcpy_14: begin
          _th_memcpy_dma_size_10 <= 256;
          th_memcpy <= th_memcpy_15;
        end
        th_memcpy_15: begin
          th_memcpy <= th_memcpy_17;
        end
        th_memcpy_16: begin
          _th_memcpy_dma_size_10 <= _th_memcpy_rest_words_6;
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
          _th_memcpy_v_11 <= _th_memcpy_dma_size_10;
          th_memcpy <= th_memcpy_20;
        end
        th_memcpy_20: begin
          size <= _th_memcpy_v_11;
          th_memcpy <= th_memcpy_21;
        end
        th_memcpy_21: begin
          start <= 1;
          th_memcpy <= th_memcpy_22;
        end
        th_memcpy_22: begin
          start <= 0;
          th_memcpy <= th_memcpy_23;
        end
        th_memcpy_23: begin
          if(busy) begin
            th_memcpy <= th_memcpy_24;
          end else begin
            th_memcpy <= th_memcpy_25;
          end
        end
        th_memcpy_24: begin
          th_memcpy <= th_memcpy_23;
        end
        th_memcpy_25: begin
          if(_maxi_write_req_idle) begin
            th_memcpy <= th_memcpy_26;
          end 
        end
        th_memcpy_26: begin
          if(_maxi_write_idle && !_maxi_has_outstanding_write) begin
            th_memcpy <= th_memcpy_27;
          end 
        end
        th_memcpy_27: begin
          _th_memcpy_src_global_addr_7 <= _th_memcpy_src_global_addr_7 + (_th_memcpy_dma_size_10 << 2);
          th_memcpy <= th_memcpy_28;
        end
        th_memcpy_28: begin
          _th_memcpy_dst_global_addr_8 <= _th_memcpy_dst_global_addr_8 + (_th_memcpy_dma_size_10 << 2);
          th_memcpy <= th_memcpy_29;
        end
        th_memcpy_29: begin
          _th_memcpy_rest_words_6 <= _th_memcpy_rest_words_6 - _th_memcpy_dma_size_10;
          th_memcpy <= th_memcpy_30;
        end
        th_memcpy_30: begin
          th_memcpy <= th_memcpy_12;
        end
        th_memcpy_31: begin
          th_memcpy <= th_memcpy_32;
        end
        th_memcpy_32: begin
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
      write_burst_addr_71 <= 0;
      write_burst_stride_72 <= 0;
      write_burst_length_73 <= 0;
      write_burst_done_74 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_71 <= _maxi_read_local_addr_buf;
          write_burst_stride_72 <= _maxi_read_local_stride_buf;
          write_burst_length_73 <= _maxi_read_local_size_buf;
          write_burst_done_74 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 1) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(_maxi_rvalid_sb_0) begin
            write_burst_addr_71 <= write_burst_addr_71 + write_burst_stride_72;
            write_burst_length_73 <= write_burst_length_73 - 1;
            write_burst_done_74 <= 0;
          end 
          if(_maxi_rvalid_sb_0 && (write_burst_length_73 <= 1)) begin
            write_burst_done_74 <= 1;
          end 
          if(_maxi_rvalid_sb_0 && 0) begin
            write_burst_done_74 <= 1;
          end 
          if(_maxi_rvalid_sb_0 && (write_burst_length_73 <= 1)) begin
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
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6)) begin
            _maxi_write_cont <= 1;
          end 
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6) && (_maxi_write_global_size == 0)) begin
            _maxi_write_cont <= 0;
          end 
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (_maxi_outstanding_wcount < 6)) begin
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
          if(!_maxi_write_data_busy && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1)) begin
            _maxi_write_data_fsm <= _maxi_write_data_fsm_1;
          end 
        end
        _maxi_write_data_fsm_1: begin
          _maxi_write_data_fsm <= _maxi_write_data_fsm_2;
        end
        _maxi_write_data_fsm_2: begin
          if((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_108 && ((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0)) && read_burst_rlast_109) begin
            _maxi_write_data_fsm <= _maxi_write_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam read_burst_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      read_burst_fsm_1 <= read_burst_fsm_1_init;
      read_burst_addr_105 <= 0;
      read_burst_stride_106 <= 0;
      read_burst_length_107 <= 0;
      read_burst_rvalid_108 <= 0;
      read_burst_rlast_109 <= 0;
    end else begin
      case(read_burst_fsm_1)
        read_burst_fsm_1_init: begin
          read_burst_addr_105 <= _maxi_write_local_addr_buf;
          read_burst_stride_106 <= _maxi_write_local_stride_buf;
          read_burst_length_107 <= _maxi_write_size_buf;
          read_burst_rvalid_108 <= 0;
          read_burst_rlast_109 <= 0;
          if((_maxi_write_data_fsm == 1) && (_maxi_write_op_sel_buf == 1) && (_maxi_write_size_buf > 0)) begin
            read_burst_fsm_1 <= read_burst_fsm_1_1;
          end 
        end
        read_burst_fsm_1_1: begin
          if((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0) && (read_burst_length_107 > 0)) begin
            read_burst_addr_105 <= read_burst_addr_105 + read_burst_stride_106;
            read_burst_length_107 <= read_burst_length_107 - 1;
            read_burst_rvalid_108 <= 1;
          end 
          if((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0) && (read_burst_length_107 <= 1)) begin
            read_burst_rlast_109 <= 1;
          end 
          if(read_burst_rlast_109 && read_burst_rvalid_108 && ((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0))) begin
            read_burst_rvalid_108 <= 0;
            read_burst_rlast_109 <= 0;
          end 
          if(0) begin
            read_burst_rvalid_108 <= 0;
            read_burst_rlast_109 <= 0;
          end 
          if(read_burst_rlast_109 && read_burst_rvalid_108 && ((_maxi_wready_sb_0 || !_maxi_wvalid_sb_0) && (_maxi_write_size_buf > 0))) begin
            read_burst_fsm_1 <= read_burst_fsm_1_init;
          end 
          if(0) begin
            read_burst_fsm_1 <= read_burst_fsm_1_init;
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



module processing_unit #
(
  parameter ADDR_WIDTH = 10,
  parameter DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  input start,
  output reg busy,
  input [ADDR_WIDTH-1:0] size,
  output reg [ADDR_WIDTH-1:0] addr,
  input [DATA_WIDTH-1:0] rdata,
  output reg [DATA_WIDTH-1:0] wdata,
  output reg wenable
);

  localparam INCR = 100;
  reg [ADDR_WIDTH-1:0] count;
  reg [DATA_WIDTH-1:0] rdata_buf;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      addr <= 0;
      count <= 0;
      busy <= 0;
      rdata_buf <= 0;
      wdata <= 0;
      wenable <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(start) begin
            addr <= 0;
            count <= size;
            busy <= 1;
          end 
          if(start) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          rdata_buf <= rdata;
          fsm <= fsm_3;
        end
        fsm_3: begin
          wdata <= rdata_buf + INCR;
          wenable <= 1;
          fsm <= fsm_4;
        end
        fsm_4: begin
          wenable <= 0;
          addr <= addr + 1;
          count <= count - 1;
          if(count > 1) begin
            fsm <= fsm_1;
          end 
          if(count <= 1) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          busy <= 0;
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule



module _memory_wreq_fifo
(
  input CLK,
  input RST,
  input _memory_wreq_fifo_enq,
  input [41-1:0] _memory_wreq_fifo_wdata,
  output _memory_wreq_fifo_full,
  output _memory_wreq_fifo_almost_full,
  input _memory_wreq_fifo_deq,
  output [41-1:0] _memory_wreq_fifo_rdata,
  output _memory_wreq_fifo_empty,
  output _memory_wreq_fifo_almost_empty
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
  assign _memory_wreq_fifo_full = is_full;
  assign _memory_wreq_fifo_almost_full = is_almost_full || is_full;
  assign _memory_wreq_fifo_empty = is_empty;
  assign _memory_wreq_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _memory_wreq_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_memory_wreq_fifo_enq && !is_full) begin
        mem[head] <= _memory_wreq_fifo_wdata;
        head <= head + 1;
      end 
      if(_memory_wreq_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _memory_rreq_fifo
(
  input CLK,
  input RST,
  input _memory_rreq_fifo_enq,
  input [41-1:0] _memory_rreq_fifo_wdata,
  output _memory_rreq_fifo_full,
  output _memory_rreq_fifo_almost_full,
  input _memory_rreq_fifo_deq,
  output [41-1:0] _memory_rreq_fifo_rdata,
  output _memory_rreq_fifo_empty,
  output _memory_rreq_fifo_almost_empty
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
  assign _memory_rreq_fifo_full = is_full;
  assign _memory_rreq_fifo_almost_full = is_almost_full || is_full;
  assign _memory_rreq_fifo_empty = is_empty;
  assign _memory_rreq_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _memory_rreq_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_memory_rreq_fifo_enq && !is_full) begin
        mem[head] <= _memory_rreq_fifo_wdata;
        head <= head + 1;
      end 
      if(_memory_rreq_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _memory_wdata_fifo
(
  input CLK,
  input RST,
  input _memory_wdata_fifo_enq,
  input [37-1:0] _memory_wdata_fifo_wdata,
  output _memory_wdata_fifo_full,
  output _memory_wdata_fifo_almost_full,
  input _memory_wdata_fifo_deq,
  output [37-1:0] _memory_wdata_fifo_rdata,
  output _memory_wdata_fifo_empty,
  output _memory_wdata_fifo_almost_empty
);

  reg [37-1:0] mem [0:8-1];
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
  wire [37-1:0] rdata;
  assign _memory_wdata_fifo_full = is_full;
  assign _memory_wdata_fifo_almost_full = is_almost_full || is_full;
  assign _memory_wdata_fifo_empty = is_empty;
  assign _memory_wdata_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _memory_wdata_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_memory_wdata_fifo_enq && !is_full) begin
        mem[head] <= _memory_wdata_fifo_wdata;
        head <= head + 1;
      end 
      if(_memory_wdata_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()

    memimg_name = 'memimg_thread_verilog_submodule_ipxact.out'

    test_module = thread_verilog_submodule_ipxact.mkTest(memimg_name=memimg_name)
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
