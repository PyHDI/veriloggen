from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_embedded_verilog_ipxact

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
  reg memory_wready;
  wire [2-1:0] memory_bresp;
  reg memory_bvalid;
  wire memory_bready;
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
  assign memory_bresp = 0;
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
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("_memory_memimg_.out", _memory_mem);
  end

  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_interval_count;
  reg [33-1:0] _keep_sleep_count;
  wire [32-1:0] pack_write_req_global_addr_0;
  wire [9-1:0] pack_write_req_size_1;
  assign pack_write_req_global_addr_0 = memory_awaddr;
  assign pack_write_req_size_1 = memory_awlen + 1;
  wire [41-1:0] pack_write_req_packed_2;
  assign pack_write_req_packed_2 = { pack_write_req_global_addr_0, pack_write_req_size_1 };
  assign _memory_wreq_fifo_wdata = ((_memory_waddr_fsm == 11) && memory_awvalid && memory_awready)? pack_write_req_packed_2 : 'hx;
  assign _memory_wreq_fifo_enq = ((_memory_waddr_fsm == 11) && memory_awvalid && memory_awready)? (_memory_waddr_fsm == 11) && memory_awvalid && memory_awready && !_memory_wreq_fifo_almost_full : 0;
  localparam _tmp_3 = 1;
  wire [_tmp_3-1:0] _tmp_4;
  assign _tmp_4 = !_memory_wreq_fifo_almost_full;
  reg [_tmp_3-1:0] __tmp_4_1;
  wire [32-1:0] unpack_write_req_global_addr_5;
  wire [9-1:0] unpack_write_req_size_6;
  assign unpack_write_req_global_addr_5 = _memory_wreq_fifo_rdata[40:9];
  assign unpack_write_req_size_6 = _memory_wreq_fifo_rdata[8:0];
  assign _memory_wreq_fifo_deq = ((_memory_wdata_fsm == 0) && !_memory_wreq_fifo_empty && !_memory_wreq_fifo_empty)? 1 : 0;
  wire [32-1:0] pack_read_req_global_addr_7;
  wire [9-1:0] pack_read_req_size_8;
  assign pack_read_req_global_addr_7 = memory_araddr;
  assign pack_read_req_size_8 = memory_arlen + 1;
  wire [41-1:0] pack_read_req_packed_9;
  assign pack_read_req_packed_9 = { pack_read_req_global_addr_7, pack_read_req_size_8 };
  assign _memory_rreq_fifo_wdata = ((_memory_raddr_fsm == 1) && memory_arvalid && memory_arready)? pack_read_req_packed_9 : 'hx;
  assign _memory_rreq_fifo_enq = ((_memory_raddr_fsm == 1) && memory_arvalid && memory_arready)? (_memory_raddr_fsm == 1) && memory_arvalid && memory_arready && !_memory_rreq_fifo_almost_full : 0;
  localparam _tmp_10 = 1;
  wire [_tmp_10-1:0] _tmp_11;
  assign _tmp_11 = !_memory_rreq_fifo_almost_full;
  reg [_tmp_10-1:0] __tmp_11_1;
  wire [32-1:0] unpack_read_req_global_addr_12;
  wire [9-1:0] unpack_read_req_size_13;
  assign unpack_read_req_global_addr_12 = _memory_rreq_fifo_rdata[40:9];
  assign unpack_read_req_size_13 = _memory_rreq_fifo_rdata[8:0];
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
  wire _tmp_14;
  assign _tmp_14 = memory_awready;

  always @(*) begin
    uut_maxi_awready = _tmp_14;
  end

  assign memory_wdata = uut_maxi_wdata;
  assign memory_wstrb = uut_maxi_wstrb;
  assign memory_wlast = uut_maxi_wlast;
  assign memory_wvalid = uut_maxi_wvalid;
  wire _tmp_15;
  assign _tmp_15 = memory_wready;

  always @(*) begin
    uut_maxi_wready = _tmp_15;
  end

  wire [2-1:0] _tmp_16;
  assign _tmp_16 = memory_bresp;

  always @(*) begin
    uut_maxi_bresp = _tmp_16;
  end

  wire _tmp_17;
  assign _tmp_17 = memory_bvalid;

  always @(*) begin
    uut_maxi_bvalid = _tmp_17;
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
  wire _tmp_18;
  assign _tmp_18 = memory_arready;

  always @(*) begin
    uut_maxi_arready = _tmp_18;
  end

  wire [32-1:0] _tmp_19;
  assign _tmp_19 = memory_rdata;

  always @(*) begin
    uut_maxi_rdata = _tmp_19;
  end

  wire [2-1:0] _tmp_20;
  assign _tmp_20 = memory_rresp;

  always @(*) begin
    uut_maxi_rresp = _tmp_20;
  end

  wire _tmp_21;
  assign _tmp_21 = memory_rlast;

  always @(*) begin
    uut_maxi_rlast = _tmp_21;
  end

  wire _tmp_22;
  assign _tmp_22 = memory_rvalid;

  always @(*) begin
    uut_maxi_rvalid = _tmp_22;
  end

  assign memory_rready = uut_maxi_rready;
  reg [32-1:0] _saxi_awaddr;
  wire [4-1:0] _saxi_awcache;
  wire [3-1:0] _saxi_awprot;
  reg _saxi_awvalid;
  wire _saxi_awready;
  reg [32-1:0] _saxi_wdata;
  reg [4-1:0] _saxi_wstrb;
  reg _saxi_wvalid;
  wire _saxi_wready;
  wire [2-1:0] _saxi_bresp;
  wire _saxi_bvalid;
  wire _saxi_bready;
  reg [32-1:0] _saxi_araddr;
  wire [4-1:0] _saxi_arcache;
  wire [3-1:0] _saxi_arprot;
  reg _saxi_arvalid;
  wire _saxi_arready;
  wire [32-1:0] _saxi_rdata;
  wire [2-1:0] _saxi_rresp;
  wire _saxi_rvalid;
  wire _saxi_rready;
  assign _saxi_awcache = 3;
  assign _saxi_awprot = 0;
  assign _saxi_bready = 1;
  assign _saxi_arcache = 3;
  assign _saxi_arprot = 0;
  reg [3-1:0] outstanding_wcount_23;
  wire [32-1:0] _tmp_24;
  assign _tmp_24 = _saxi_awaddr;

  always @(*) begin
    uut_saxi_awaddr = _tmp_24;
  end

  wire [4-1:0] _tmp_25;
  assign _tmp_25 = _saxi_awcache;

  always @(*) begin
    uut_saxi_awcache = _tmp_25;
  end

  wire [3-1:0] _tmp_26;
  assign _tmp_26 = _saxi_awprot;

  always @(*) begin
    uut_saxi_awprot = _tmp_26;
  end

  wire _tmp_27;
  assign _tmp_27 = _saxi_awvalid;

  always @(*) begin
    uut_saxi_awvalid = _tmp_27;
  end

  assign _saxi_awready = uut_saxi_awready;
  wire [32-1:0] _tmp_28;
  assign _tmp_28 = _saxi_wdata;

  always @(*) begin
    uut_saxi_wdata = _tmp_28;
  end

  wire [4-1:0] _tmp_29;
  assign _tmp_29 = _saxi_wstrb;

  always @(*) begin
    uut_saxi_wstrb = _tmp_29;
  end

  wire _tmp_30;
  assign _tmp_30 = _saxi_wvalid;

  always @(*) begin
    uut_saxi_wvalid = _tmp_30;
  end

  assign _saxi_wready = uut_saxi_wready;
  assign _saxi_bresp = uut_saxi_bresp;
  assign _saxi_bvalid = uut_saxi_bvalid;
  wire _tmp_31;
  assign _tmp_31 = _saxi_bready;

  always @(*) begin
    uut_saxi_bready = _tmp_31;
  end

  wire [32-1:0] _tmp_32;
  assign _tmp_32 = _saxi_araddr;

  always @(*) begin
    uut_saxi_araddr = _tmp_32;
  end

  wire [4-1:0] _tmp_33;
  assign _tmp_33 = _saxi_arcache;

  always @(*) begin
    uut_saxi_arcache = _tmp_33;
  end

  wire [3-1:0] _tmp_34;
  assign _tmp_34 = _saxi_arprot;

  always @(*) begin
    uut_saxi_arprot = _tmp_34;
  end

  wire _tmp_35;
  assign _tmp_35 = _saxi_arvalid;

  always @(*) begin
    uut_saxi_arvalid = _tmp_35;
  end

  assign _saxi_arready = uut_saxi_arready;
  assign _saxi_rdata = uut_saxi_rdata;
  assign _saxi_rresp = uut_saxi_rresp;
  assign _saxi_rvalid = uut_saxi_rvalid;
  wire _tmp_36;
  assign _tmp_36 = _saxi_rready;

  always @(*) begin
    uut_saxi_rready = _tmp_36;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_11;
  reg signed [32-1:0] _th_ctrl_awaddr_12;
  reg __saxi_cond_0_1;
  reg __saxi_cond_1_1;
  reg signed [32-1:0] _th_ctrl_src_offset_13;
  reg __saxi_cond_2_1;
  reg __saxi_cond_3_1;
  reg signed [32-1:0] _th_ctrl_dst_offset_14;
  reg __saxi_cond_4_1;
  reg __saxi_cond_5_1;
  reg signed [32-1:0] _th_ctrl_start_time_15;
  reg __saxi_cond_6_1;
  reg __saxi_cond_7_1;
  reg signed [32-1:0] _th_ctrl_araddr_16;
  reg __saxi_cond_8_1;
  reg signed [32-1:0] axim_rdata_37;
  assign _saxi_rready = th_ctrl == 31;
  reg signed [32-1:0] _th_ctrl_busy_17;
  reg signed [32-1:0] _th_ctrl_end_time_18;
  reg signed [32-1:0] _th_ctrl_time_19;

  initial begin
    $dumpfile("uut.vcd");
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
    memory_wready = 0;
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
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_interval_count = 0;
    _keep_sleep_count = 0;
    __tmp_4_1 = 0;
    __tmp_11_1 = 0;
    _d1__memory_rdata_fsm = _memory_rdata_fsm_init;
    __memory_rdata_fsm_cond_11_0_1 = 0;
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    _saxi_wdata = 0;
    _saxi_wstrb = 0;
    _saxi_wvalid = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    outstanding_wcount_23 = 0;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_11 = 0;
    _th_ctrl_awaddr_12 = 0;
    __saxi_cond_0_1 = 0;
    __saxi_cond_1_1 = 0;
    _th_ctrl_src_offset_13 = 0;
    __saxi_cond_2_1 = 0;
    __saxi_cond_3_1 = 0;
    _th_ctrl_dst_offset_14 = 0;
    __saxi_cond_4_1 = 0;
    __saxi_cond_5_1 = 0;
    _th_ctrl_start_time_15 = 0;
    __saxi_cond_6_1 = 0;
    __saxi_cond_7_1 = 0;
    _th_ctrl_araddr_16 = 0;
    __saxi_cond_8_1 = 0;
    axim_rdata_37 = 0;
    _th_ctrl_busy_17 = 0;
    _th_ctrl_end_time_18 = 0;
    _th_ctrl_time_19 = 0;
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
      if((_memory_wdata_fsm == 1) && memory_wvalid && memory_wready && memory_wstrb[0]) begin
        _memory_mem[_write_addr + 0] <= memory_wdata[7:0];
      end 
      if((_memory_wdata_fsm == 1) && memory_wvalid && memory_wready && memory_wstrb[1]) begin
        _memory_mem[_write_addr + 1] <= memory_wdata[15:8];
      end 
      if((_memory_wdata_fsm == 1) && memory_wvalid && memory_wready && memory_wstrb[2]) begin
        _memory_mem[_write_addr + 2] <= memory_wdata[23:16];
      end 
      if((_memory_wdata_fsm == 1) && memory_wvalid && memory_wready && memory_wstrb[3]) begin
        _memory_mem[_write_addr + 3] <= memory_wdata[31:24];
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
      memory_wready <= 0;
    end else begin
      case(_memory_wdata_fsm)
        _memory_wdata_fsm_init: begin
          memory_bvalid <= 0;
          if(!_memory_wreq_fifo_empty) begin
            _write_addr <= unpack_write_req_global_addr_5;
            _write_count <= unpack_write_req_size_6;
            memory_wready <= 1;
          end 
          if(!_memory_wreq_fifo_empty) begin
            _memory_wdata_fsm <= _memory_wdata_fsm_1;
          end 
        end
        _memory_wdata_fsm_1: begin
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 4;
            _write_count <= _write_count - 1;
          end 
          if(_sleep_interval_count == 15) begin
            memory_wready <= 0;
          end else begin
            memory_wready <= 1;
          end
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            memory_wready <= 0;
            memory_bvalid <= 1;
          end 
          if(memory_wvalid && memory_wready && memory_wlast) begin
            memory_wready <= 0;
            memory_bvalid <= 1;
          end 
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            _memory_wdata_fsm <= _memory_wdata_fsm_init;
          end 
          if(memory_wvalid && memory_wready && memory_wlast) begin
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
            _read_addr <= unpack_read_req_global_addr_12;
            _read_count <= unpack_read_req_size_13;
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
      __tmp_4_1 <= 0;
    end else begin
      if(_memory_wreq_fifo_enq && !_memory_wreq_fifo_full && (_memory_wreq_fifo_deq && !_memory_wreq_fifo_empty)) begin
        count__memory_wreq_fifo <= count__memory_wreq_fifo;
      end else if(_memory_wreq_fifo_enq && !_memory_wreq_fifo_full) begin
        count__memory_wreq_fifo <= count__memory_wreq_fifo + 1;
      end else if(_memory_wreq_fifo_deq && !_memory_wreq_fifo_empty) begin
        count__memory_wreq_fifo <= count__memory_wreq_fifo - 1;
      end 
      __tmp_4_1 <= _tmp_4;
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      count__memory_rreq_fifo <= 0;
      __tmp_11_1 <= 0;
    end else begin
      if(_memory_rreq_fifo_enq && !_memory_rreq_fifo_full && (_memory_rreq_fifo_deq && !_memory_rreq_fifo_empty)) begin
        count__memory_rreq_fifo <= count__memory_rreq_fifo;
      end else if(_memory_rreq_fifo_enq && !_memory_rreq_fifo_full) begin
        count__memory_rreq_fifo <= count__memory_rreq_fifo + 1;
      end else if(_memory_rreq_fifo_deq && !_memory_rreq_fifo_empty) begin
        count__memory_rreq_fifo <= count__memory_rreq_fifo - 1;
      end 
      __tmp_11_1 <= _tmp_11;
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      outstanding_wcount_23 <= 0;
      _saxi_awaddr <= 0;
      _saxi_awvalid <= 0;
      __saxi_cond_0_1 <= 0;
      _saxi_wdata <= 0;
      _saxi_wvalid <= 0;
      _saxi_wstrb <= 0;
      __saxi_cond_1_1 <= 0;
      __saxi_cond_2_1 <= 0;
      __saxi_cond_3_1 <= 0;
      __saxi_cond_4_1 <= 0;
      __saxi_cond_5_1 <= 0;
      __saxi_cond_6_1 <= 0;
      __saxi_cond_7_1 <= 0;
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_8_1 <= 0;
    end else begin
      if(__saxi_cond_0_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_1_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_2_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_3_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_4_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_5_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_6_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_7_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_8_1) begin
        _saxi_arvalid <= 0;
      end 
      if(_saxi_wvalid && _saxi_wready && !(_saxi_bvalid && _saxi_bready) && (outstanding_wcount_23 < 7)) begin
        outstanding_wcount_23 <= outstanding_wcount_23 + 1;
      end 
      if(!(_saxi_wvalid && _saxi_wready) && (_saxi_bvalid && _saxi_bready) && (outstanding_wcount_23 > 0)) begin
        outstanding_wcount_23 <= outstanding_wcount_23 - 1;
      end 
      if((th_ctrl == 6) && ((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 8) && ((outstanding_wcount_23 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 4096;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 12) && ((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 14) && ((outstanding_wcount_23 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= _th_ctrl_src_offset_13;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 18) && ((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 20) && ((outstanding_wcount_23 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= _th_ctrl_dst_offset_14;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_5_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 24) && ((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_6_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 26) && ((outstanding_wcount_23 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_7_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 29) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_16;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_8_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
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

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_11 <= 0;
      _th_ctrl_awaddr_12 <= 0;
      _th_ctrl_src_offset_13 <= 0;
      _th_ctrl_dst_offset_14 <= 0;
      _th_ctrl_start_time_15 <= 0;
      _th_ctrl_araddr_16 <= 0;
      axim_rdata_37 <= 0;
      _th_ctrl_busy_17 <= 0;
      _th_ctrl_end_time_18 <= 0;
      _th_ctrl_time_19 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_11 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_11 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_11 <= _th_ctrl_i_11 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_12 <= 8;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          $display("# copy_bytes = %d", 4096);
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          if((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_7;
          end 
        end
        th_ctrl_7: begin
          th_ctrl <= th_ctrl_8;
        end
        th_ctrl_8: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          _th_ctrl_awaddr_12 <= 12;
          th_ctrl <= th_ctrl_10;
        end
        th_ctrl_10: begin
          _th_ctrl_src_offset_13 <= 0;
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          $display("# src_offset = %d", _th_ctrl_src_offset_13);
          th_ctrl <= th_ctrl_12;
        end
        th_ctrl_12: begin
          if((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_13;
          end 
        end
        th_ctrl_13: begin
          th_ctrl <= th_ctrl_14;
        end
        th_ctrl_14: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_15;
          end 
        end
        th_ctrl_15: begin
          _th_ctrl_awaddr_12 <= 16;
          th_ctrl <= th_ctrl_16;
        end
        th_ctrl_16: begin
          _th_ctrl_dst_offset_14 <= 8192;
          th_ctrl <= th_ctrl_17;
        end
        th_ctrl_17: begin
          $display("# dst_offset = %d", _th_ctrl_dst_offset_14);
          th_ctrl <= th_ctrl_18;
        end
        th_ctrl_18: begin
          if((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_21;
          end 
        end
        th_ctrl_21: begin
          _th_ctrl_awaddr_12 <= 0;
          th_ctrl <= th_ctrl_22;
        end
        th_ctrl_22: begin
          _th_ctrl_start_time_15 <= counter;
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_23: begin
          $display("# start time = %d", _th_ctrl_start_time_15);
          th_ctrl <= th_ctrl_24;
        end
        th_ctrl_24: begin
          if((outstanding_wcount_23 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_25;
          end 
        end
        th_ctrl_25: begin
          th_ctrl <= th_ctrl_26;
        end
        th_ctrl_26: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_27;
          end 
        end
        th_ctrl_27: begin
          _th_ctrl_araddr_16 <= 4;
          th_ctrl <= th_ctrl_28;
        end
        th_ctrl_28: begin
          if(1) begin
            th_ctrl <= th_ctrl_29;
          end else begin
            th_ctrl <= th_ctrl_36;
          end
        end
        th_ctrl_29: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_30;
          end 
        end
        th_ctrl_30: begin
          th_ctrl <= th_ctrl_31;
        end
        th_ctrl_31: begin
          if(_saxi_rvalid) begin
            axim_rdata_37 <= _saxi_rdata;
          end 
          if(_saxi_rvalid) begin
            th_ctrl <= th_ctrl_32;
          end 
        end
        th_ctrl_32: begin
          _th_ctrl_busy_17 <= axim_rdata_37;
          th_ctrl <= th_ctrl_33;
        end
        th_ctrl_33: begin
          if(!_th_ctrl_busy_17) begin
            th_ctrl <= th_ctrl_34;
          end else begin
            th_ctrl <= th_ctrl_35;
          end
        end
        th_ctrl_34: begin
          th_ctrl <= th_ctrl_36;
        end
        th_ctrl_35: begin
          th_ctrl <= th_ctrl_28;
        end
        th_ctrl_36: begin
          _th_ctrl_end_time_18 <= counter;
          th_ctrl <= th_ctrl_37;
        end
        th_ctrl_37: begin
          $display("# end time = %d", _th_ctrl_end_time_18);
          th_ctrl <= th_ctrl_38;
        end
        th_ctrl_38: begin
          _th_ctrl_time_19 <= _th_ctrl_end_time_18 - _th_ctrl_start_time_15;
          th_ctrl <= th_ctrl_39;
        end
        th_ctrl_39: begin
          $display("# exec time = %d", _th_ctrl_time_19);
          th_ctrl <= th_ctrl_40;
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

  reg [31:0] sum;
  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      led <= 0;
    end else begin
      if(ram_a_0_wenable) begin
        sum <= sum + ram_a_0_wdata;
      end
      led <= sum;
    end 
  end

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
  wire [32-1:0] mask_addr_shifted_20;
  assign mask_addr_shifted_20 = _th_memcpy_src_global_addr_7 >> 2;
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
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_42;
  reg [10-1:0] write_burst_stride_43;
  reg [33-1:0] write_burst_length_44;
  reg write_burst_done_45;
  assign ram_a_0_wdata = ((write_burst_fsm_0 == 1) && maxi_rvalid)? maxi_rdata : 'hx;
  assign ram_a_0_wenable = ((write_burst_fsm_0 == 1) && maxi_rvalid)? 1'd1 : 0;
  assign maxi_rready = _maxi_read_data_fsm == 2;
  wire [32-1:0] mask_addr_shifted_46;
  assign mask_addr_shifted_46 = _th_memcpy_dst_global_addr_8 >> 2;
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
  reg [32-1:0] read_burst_fsm_1;
  localparam read_burst_fsm_1_init = 0;
  reg [10-1:0] read_burst_addr_76;
  reg [10-1:0] read_burst_stride_77;
  reg [33-1:0] read_burst_length_78;
  reg read_burst_rvalid_79;
  reg read_burst_rlast_80;
  assign ram_a_0_addr = ((read_burst_fsm_1 == 1) && (!read_burst_rvalid_79 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)))? read_burst_addr_76 : 
                        ((write_burst_fsm_0 == 1) && maxi_rvalid)? write_burst_addr_42 : 'hx;
  assign ram_a_0_enable = ((read_burst_fsm_1 == 1) && (!read_burst_rvalid_79 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)))? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && maxi_rvalid)? 1'd1 : 0;
  localparam _tmp_81 = 1;
  wire [_tmp_81-1:0] _tmp_82;
  assign _tmp_82 = (read_burst_fsm_1 == 1) && (!read_burst_rvalid_79 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0));
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
        _maxi_read_global_size <= _th_memcpy_dma_size_10;
        _maxi_read_local_addr <= _th_memcpy_local_addr_9;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_memcpy_dma_size_10;
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
        _maxi_write_global_size <= _th_memcpy_dma_size_10;
        _maxi_write_local_addr <= _th_memcpy_local_addr_9;
        _maxi_write_local_stride <= 1;
        _maxi_write_local_size <= _th_memcpy_dma_size_10;
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
            th_memcpy <= th_memcpy_25;
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
          _th_memcpy_src_global_addr_7 <= _th_memcpy_src_global_addr_7 + (_th_memcpy_dma_size_10 << 2);
          th_memcpy <= th_memcpy_22;
        end
        th_memcpy_22: begin
          _th_memcpy_dst_global_addr_8 <= _th_memcpy_dst_global_addr_8 + (_th_memcpy_dma_size_10 << 2);
          th_memcpy <= th_memcpy_23;
        end
        th_memcpy_23: begin
          _th_memcpy_rest_words_6 <= _th_memcpy_rest_words_6 - _th_memcpy_dma_size_10;
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

  localparam write_burst_fsm_0_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_0 <= write_burst_fsm_0_init;
      write_burst_addr_42 <= 0;
      write_burst_stride_43 <= 0;
      write_burst_length_44 <= 0;
      write_burst_done_45 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_42 <= _maxi_read_local_addr_buf;
          write_burst_stride_43 <= _maxi_read_local_stride_buf;
          write_burst_length_44 <= _maxi_read_local_size_buf;
          write_burst_done_45 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 1) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
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

  localparam read_burst_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      read_burst_fsm_1 <= read_burst_fsm_1_init;
      read_burst_addr_76 <= 0;
      read_burst_stride_77 <= 0;
      read_burst_length_78 <= 0;
      read_burst_rvalid_79 <= 0;
      read_burst_rlast_80 <= 0;
    end else begin
      case(read_burst_fsm_1)
        read_burst_fsm_1_init: begin
          read_burst_addr_76 <= _maxi_write_local_addr_buf;
          read_burst_stride_77 <= _maxi_write_local_stride_buf;
          read_burst_length_78 <= _maxi_write_size_buf;
          read_burst_rvalid_79 <= 0;
          read_burst_rlast_80 <= 0;
          if((_maxi_write_data_fsm == 1) && (_maxi_write_op_sel_buf == 1) && (_maxi_write_size_buf > 0)) begin
            read_burst_fsm_1 <= read_burst_fsm_1_1;
          end 
        end
        read_burst_fsm_1_1: begin
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
"""


def test():
    veriloggen.reset()
    test_module = thread_embedded_verilog_ipxact.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    # reformat due to embedded codes
    code_ast = parser.parse(code)
    code = codegen.visit(code_ast)

    assert(expected_code == code)
