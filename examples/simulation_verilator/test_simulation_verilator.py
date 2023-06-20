from __future__ import absolute_import
from __future__ import print_function
import os
import veriloggen
import simulation_verilator

expected_verilog = """

module test
(
  input io_CLK,
  input io_RST
);

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire [3-1:0] myaxi_awsize;
  wire [2-1:0] myaxi_awburst;
  wire [1-1:0] myaxi_awlock;
  wire [4-1:0] myaxi_awcache;
  wire [3-1:0] myaxi_awprot;
  wire [4-1:0] myaxi_awqos;
  wire [2-1:0] myaxi_awuser;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  reg [2-1:0] myaxi_bresp;
  reg myaxi_bvalid;
  wire myaxi_bready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire [3-1:0] myaxi_arsize;
  wire [2-1:0] myaxi_arburst;
  wire [1-1:0] myaxi_arlock;
  wire [4-1:0] myaxi_arcache;
  wire [3-1:0] myaxi_arprot;
  wire [4-1:0] myaxi_arqos;
  wire [2-1:0] myaxi_aruser;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [32-1:0] myaxi_rdata;
  reg [2-1:0] myaxi_rresp;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
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
    .CLK(CLK),
    .RST(RST),
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
    .CLK(CLK),
    .RST(RST),
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
    .CLK(CLK),
    .RST(RST),
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
    $readmemh("memimg_test_simulation_verilator.out", _memory_mem);
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
  assign memory_awaddr = myaxi_awaddr;
  assign memory_awlen = myaxi_awlen;
  assign memory_awsize = myaxi_awsize;
  assign memory_awburst = myaxi_awburst;
  assign memory_awlock = myaxi_awlock;
  assign memory_awcache = myaxi_awcache;
  assign memory_awprot = myaxi_awprot;
  assign memory_awqos = myaxi_awqos;
  assign memory_awuser = myaxi_awuser;
  assign memory_awvalid = myaxi_awvalid;
  wire _tmp_25;
  assign _tmp_25 = memory_awready;

  always @(*) begin
    myaxi_awready = _tmp_25;
  end

  assign memory_wdata = myaxi_wdata;
  assign memory_wstrb = myaxi_wstrb;
  assign memory_wlast = myaxi_wlast;
  assign memory_wvalid = myaxi_wvalid;
  wire _tmp_26;
  assign _tmp_26 = memory_wready;

  always @(*) begin
    myaxi_wready = _tmp_26;
  end

  wire [2-1:0] _tmp_27;
  assign _tmp_27 = memory_bresp;

  always @(*) begin
    myaxi_bresp = _tmp_27;
  end

  wire _tmp_28;
  assign _tmp_28 = memory_bvalid;

  always @(*) begin
    myaxi_bvalid = _tmp_28;
  end

  assign memory_bready = myaxi_bready;
  assign memory_araddr = myaxi_araddr;
  assign memory_arlen = myaxi_arlen;
  assign memory_arsize = myaxi_arsize;
  assign memory_arburst = myaxi_arburst;
  assign memory_arlock = myaxi_arlock;
  assign memory_arcache = myaxi_arcache;
  assign memory_arprot = myaxi_arprot;
  assign memory_arqos = myaxi_arqos;
  assign memory_aruser = myaxi_aruser;
  assign memory_arvalid = myaxi_arvalid;
  wire _tmp_29;
  assign _tmp_29 = memory_arready;

  always @(*) begin
    myaxi_arready = _tmp_29;
  end

  wire [32-1:0] _tmp_30;
  assign _tmp_30 = memory_rdata;

  always @(*) begin
    myaxi_rdata = _tmp_30;
  end

  wire [2-1:0] _tmp_31;
  assign _tmp_31 = memory_rresp;

  always @(*) begin
    myaxi_rresp = _tmp_31;
  end

  wire _tmp_32;
  assign _tmp_32 = memory_rlast;

  always @(*) begin
    myaxi_rlast = _tmp_32;
  end

  wire _tmp_33;
  assign _tmp_33 = memory_rvalid;

  always @(*) begin
    myaxi_rvalid = _tmp_33;
  end

  assign memory_rready = myaxi_rready;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awsize(myaxi_awsize),
    .myaxi_awburst(myaxi_awburst),
    .myaxi_awlock(myaxi_awlock),
    .myaxi_awcache(myaxi_awcache),
    .myaxi_awprot(myaxi_awprot),
    .myaxi_awqos(myaxi_awqos),
    .myaxi_awuser(myaxi_awuser),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_bresp(myaxi_bresp),
    .myaxi_bvalid(myaxi_bvalid),
    .myaxi_bready(myaxi_bready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arsize(myaxi_arsize),
    .myaxi_arburst(myaxi_arburst),
    .myaxi_arlock(myaxi_arlock),
    .myaxi_arcache(myaxi_arcache),
    .myaxi_arprot(myaxi_arprot),
    .myaxi_arqos(myaxi_arqos),
    .myaxi_aruser(myaxi_aruser),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rresp(myaxi_rresp),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $write("");
    $write("");
  end


  initial begin
    CLK = 0;
    $write("");
  end


  initial begin
    RST = 0;
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
    $write("");
    RST = 1;
    $write("");
    RST = 0;
    $write("");
    $write("");
  end

  wire _tmp_34;
  assign _tmp_34 = io_CLK;

  always @(*) begin
    CLK = _tmp_34;
  end

  wire _tmp_35;
  assign _tmp_35 = io_RST;

  always @(*) begin
    RST = _tmp_35;
  end


  always @(posedge CLK) begin
    if(RST) begin
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

  always @(posedge CLK) begin
    if(RST) begin
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

  always @(posedge CLK) begin
    if(RST) begin
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

  always @(posedge CLK) begin
    if(RST) begin
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

  always @(posedge CLK) begin
    if(RST) begin
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


  always @(posedge CLK) begin
    if(RST) begin
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


  always @(posedge CLK) begin
    if(RST) begin
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


  always @(posedge CLK) begin
    if(RST) begin
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



module blinkled
(
  input CLK,
  input RST,
  output reg [32-1:0] myaxi_awaddr,
  output reg [8-1:0] myaxi_awlen,
  output [3-1:0] myaxi_awsize,
  output [2-1:0] myaxi_awburst,
  output [1-1:0] myaxi_awlock,
  output [4-1:0] myaxi_awcache,
  output [3-1:0] myaxi_awprot,
  output [4-1:0] myaxi_awqos,
  output [2-1:0] myaxi_awuser,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output [32-1:0] myaxi_wdata,
  output [4-1:0] myaxi_wstrb,
  output myaxi_wlast,
  output myaxi_wvalid,
  input myaxi_wready,
  input [2-1:0] myaxi_bresp,
  input myaxi_bvalid,
  output myaxi_bready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output [3-1:0] myaxi_arsize,
  output [2-1:0] myaxi_arburst,
  output [1-1:0] myaxi_arlock,
  output [4-1:0] myaxi_arcache,
  output [3-1:0] myaxi_arprot,
  output [4-1:0] myaxi_arqos,
  output [2-1:0] myaxi_aruser,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [32-1:0] myaxi_rdata,
  input [2-1:0] myaxi_rresp,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  reg [32-1:0] timer;
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
    .ram_c_0_enable(ram_c_0_enable)
  );

  assign myaxi_awsize = 2;
  assign myaxi_awburst = 1;
  assign myaxi_awlock = 0;
  assign myaxi_awcache = 3;
  assign myaxi_awprot = 0;
  assign myaxi_awqos = 0;
  assign myaxi_awuser = 0;
  reg [32-1:0] _myaxi_wdata_sb_0;
  reg [4-1:0] _myaxi_wstrb_sb_0;
  reg _myaxi_wlast_sb_0;
  reg _myaxi_wvalid_sb_0;
  wire _myaxi_wready_sb_0;
  wire _sb_myaxi_writedata_s_value_0;
  assign _sb_myaxi_writedata_s_value_0 = _myaxi_wlast_sb_0;
  wire [4-1:0] _sb_myaxi_writedata_s_value_1;
  assign _sb_myaxi_writedata_s_value_1 = _myaxi_wstrb_sb_0;
  wire [32-1:0] _sb_myaxi_writedata_s_value_2;
  assign _sb_myaxi_writedata_s_value_2 = _myaxi_wdata_sb_0;
  wire [37-1:0] _sb_myaxi_writedata_s_data_3;
  assign _sb_myaxi_writedata_s_data_3 = { _sb_myaxi_writedata_s_value_0, _sb_myaxi_writedata_s_value_1, _sb_myaxi_writedata_s_value_2 };
  wire _sb_myaxi_writedata_s_valid_4;
  assign _sb_myaxi_writedata_s_valid_4 = _myaxi_wvalid_sb_0;
  wire _sb_myaxi_writedata_m_ready_5;
  assign _sb_myaxi_writedata_m_ready_5 = myaxi_wready;
  reg [37-1:0] _sb_myaxi_writedata_data_6;
  reg _sb_myaxi_writedata_valid_7;
  wire _sb_myaxi_writedata_ready_8;
  reg [37-1:0] _sb_myaxi_writedata_tmp_data_9;
  reg _sb_myaxi_writedata_tmp_valid_10;
  wire [37-1:0] _sb_myaxi_writedata_next_data_11;
  wire _sb_myaxi_writedata_next_valid_12;
  assign _sb_myaxi_writedata_ready_8 = !_sb_myaxi_writedata_tmp_valid_10;
  assign _sb_myaxi_writedata_next_data_11 = (_sb_myaxi_writedata_tmp_valid_10)? _sb_myaxi_writedata_tmp_data_9 : _sb_myaxi_writedata_s_data_3;
  assign _sb_myaxi_writedata_next_valid_12 = _sb_myaxi_writedata_tmp_valid_10 || _sb_myaxi_writedata_s_valid_4;
  wire _sb_myaxi_writedata_m_value_13;
  assign _sb_myaxi_writedata_m_value_13 = _sb_myaxi_writedata_data_6[36:36];
  wire [4-1:0] _sb_myaxi_writedata_m_value_14;
  assign _sb_myaxi_writedata_m_value_14 = _sb_myaxi_writedata_data_6[35:32];
  wire [32-1:0] _sb_myaxi_writedata_m_value_15;
  assign _sb_myaxi_writedata_m_value_15 = _sb_myaxi_writedata_data_6[31:0];
  assign _myaxi_wready_sb_0 = _sb_myaxi_writedata_ready_8;
  assign myaxi_wdata = _sb_myaxi_writedata_m_value_15;
  assign myaxi_wstrb = _sb_myaxi_writedata_m_value_14;
  assign myaxi_wlast = _sb_myaxi_writedata_m_value_13;
  assign myaxi_wvalid = _sb_myaxi_writedata_valid_7;
  assign myaxi_bready = 1;
  assign myaxi_arsize = 2;
  assign myaxi_arburst = 1;
  assign myaxi_arlock = 0;
  assign myaxi_arcache = 3;
  assign myaxi_arprot = 0;
  assign myaxi_arqos = 0;
  assign myaxi_aruser = 0;
  wire [32-1:0] _myaxi_rdata_sb_0;
  wire _myaxi_rlast_sb_0;
  wire _myaxi_rvalid_sb_0;
  wire _myaxi_rready_sb_0;
  wire _sb_myaxi_readdata_s_value_16;
  assign _sb_myaxi_readdata_s_value_16 = myaxi_rlast;
  wire [32-1:0] _sb_myaxi_readdata_s_value_17;
  assign _sb_myaxi_readdata_s_value_17 = myaxi_rdata;
  wire [33-1:0] _sb_myaxi_readdata_s_data_18;
  assign _sb_myaxi_readdata_s_data_18 = { _sb_myaxi_readdata_s_value_16, _sb_myaxi_readdata_s_value_17 };
  wire _sb_myaxi_readdata_s_valid_19;
  assign _sb_myaxi_readdata_s_valid_19 = myaxi_rvalid;
  wire _sb_myaxi_readdata_m_ready_20;
  assign _sb_myaxi_readdata_m_ready_20 = _myaxi_rready_sb_0;
  reg [33-1:0] _sb_myaxi_readdata_data_21;
  reg _sb_myaxi_readdata_valid_22;
  wire _sb_myaxi_readdata_ready_23;
  reg [33-1:0] _sb_myaxi_readdata_tmp_data_24;
  reg _sb_myaxi_readdata_tmp_valid_25;
  wire [33-1:0] _sb_myaxi_readdata_next_data_26;
  wire _sb_myaxi_readdata_next_valid_27;
  assign _sb_myaxi_readdata_ready_23 = !_sb_myaxi_readdata_tmp_valid_25;
  assign _sb_myaxi_readdata_next_data_26 = (_sb_myaxi_readdata_tmp_valid_25)? _sb_myaxi_readdata_tmp_data_24 : _sb_myaxi_readdata_s_data_18;
  assign _sb_myaxi_readdata_next_valid_27 = _sb_myaxi_readdata_tmp_valid_25 || _sb_myaxi_readdata_s_valid_19;
  wire _sb_myaxi_readdata_m_value_28;
  assign _sb_myaxi_readdata_m_value_28 = _sb_myaxi_readdata_data_21[32:32];
  wire [32-1:0] _sb_myaxi_readdata_m_value_29;
  assign _sb_myaxi_readdata_m_value_29 = _sb_myaxi_readdata_data_21[31:0];
  assign _myaxi_rdata_sb_0 = _sb_myaxi_readdata_m_value_29;
  assign _myaxi_rlast_sb_0 = _sb_myaxi_readdata_m_value_28;
  assign _myaxi_rvalid_sb_0 = _sb_myaxi_readdata_valid_22;
  assign myaxi_rready = _sb_myaxi_readdata_ready_23;
  reg [3-1:0] _myaxi_outstanding_wcount;
  wire _myaxi_has_outstanding_write;
  assign _myaxi_has_outstanding_write = (_myaxi_outstanding_wcount > 0) || myaxi_awvalid;
  reg _myaxi_read_start;
  reg [8-1:0] _myaxi_read_op_sel;
  reg [32-1:0] _myaxi_read_global_addr;
  reg [33-1:0] _myaxi_read_global_size;
  reg [32-1:0] _myaxi_read_local_addr;
  reg [32-1:0] _myaxi_read_local_stride;
  reg [33-1:0] _myaxi_read_local_size;
  reg [32-1:0] _myaxi_read_local_blocksize;
  wire _myaxi_read_req_fifo_enq;
  wire [137-1:0] _myaxi_read_req_fifo_wdata;
  wire _myaxi_read_req_fifo_full;
  wire _myaxi_read_req_fifo_almost_full;
  wire _myaxi_read_req_fifo_deq;
  wire [137-1:0] _myaxi_read_req_fifo_rdata;
  wire _myaxi_read_req_fifo_empty;
  wire _myaxi_read_req_fifo_almost_empty;

  _myaxi_read_req_fifo
  inst__myaxi_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._myaxi_read_req_fifo_enq(_myaxi_read_req_fifo_enq),
    ._myaxi_read_req_fifo_wdata(_myaxi_read_req_fifo_wdata),
    ._myaxi_read_req_fifo_full(_myaxi_read_req_fifo_full),
    ._myaxi_read_req_fifo_almost_full(_myaxi_read_req_fifo_almost_full),
    ._myaxi_read_req_fifo_deq(_myaxi_read_req_fifo_deq),
    ._myaxi_read_req_fifo_rdata(_myaxi_read_req_fifo_rdata),
    ._myaxi_read_req_fifo_empty(_myaxi_read_req_fifo_empty),
    ._myaxi_read_req_fifo_almost_empty(_myaxi_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__myaxi_read_req_fifo;
  wire [8-1:0] _myaxi_read_op_sel_fifo;
  wire [32-1:0] _myaxi_read_local_addr_fifo;
  wire [32-1:0] _myaxi_read_local_stride_fifo;
  wire [33-1:0] _myaxi_read_local_size_fifo;
  wire [32-1:0] _myaxi_read_local_blocksize_fifo;
  wire [8-1:0] unpack_read_req_op_sel_30;
  wire [32-1:0] unpack_read_req_local_addr_31;
  wire [32-1:0] unpack_read_req_local_stride_32;
  wire [33-1:0] unpack_read_req_local_size_33;
  wire [32-1:0] unpack_read_req_local_blocksize_34;
  assign unpack_read_req_op_sel_30 = _myaxi_read_req_fifo_rdata[136:129];
  assign unpack_read_req_local_addr_31 = _myaxi_read_req_fifo_rdata[128:97];
  assign unpack_read_req_local_stride_32 = _myaxi_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_size_33 = _myaxi_read_req_fifo_rdata[64:32];
  assign unpack_read_req_local_blocksize_34 = _myaxi_read_req_fifo_rdata[31:0];
  assign _myaxi_read_op_sel_fifo = unpack_read_req_op_sel_30;
  assign _myaxi_read_local_addr_fifo = unpack_read_req_local_addr_31;
  assign _myaxi_read_local_stride_fifo = unpack_read_req_local_stride_32;
  assign _myaxi_read_local_size_fifo = unpack_read_req_local_size_33;
  assign _myaxi_read_local_blocksize_fifo = unpack_read_req_local_blocksize_34;
  reg [8-1:0] _myaxi_read_op_sel_buf;
  reg [32-1:0] _myaxi_read_local_addr_buf;
  reg [32-1:0] _myaxi_read_local_stride_buf;
  reg [33-1:0] _myaxi_read_local_size_buf;
  reg [32-1:0] _myaxi_read_local_blocksize_buf;
  reg _myaxi_read_req_busy;
  reg _myaxi_read_data_busy;
  wire _myaxi_read_req_idle;
  wire _myaxi_read_data_idle;
  wire _myaxi_read_idle;
  assign _myaxi_read_req_idle = !_myaxi_read_start && !_myaxi_read_req_busy;
  assign _myaxi_read_data_idle = _myaxi_read_req_fifo_empty && !_myaxi_read_data_busy;
  assign _myaxi_read_idle = _myaxi_read_req_idle && _myaxi_read_data_idle;
  reg _myaxi_write_start;
  reg [8-1:0] _myaxi_write_op_sel;
  reg [32-1:0] _myaxi_write_global_addr;
  reg [33-1:0] _myaxi_write_global_size;
  reg [32-1:0] _myaxi_write_local_addr;
  reg [32-1:0] _myaxi_write_local_stride;
  reg [33-1:0] _myaxi_write_local_size;
  reg [32-1:0] _myaxi_write_local_blocksize;
  wire _myaxi_write_req_fifo_enq;
  wire [137-1:0] _myaxi_write_req_fifo_wdata;
  wire _myaxi_write_req_fifo_full;
  wire _myaxi_write_req_fifo_almost_full;
  wire _myaxi_write_req_fifo_deq;
  wire [137-1:0] _myaxi_write_req_fifo_rdata;
  wire _myaxi_write_req_fifo_empty;
  wire _myaxi_write_req_fifo_almost_empty;

  _myaxi_write_req_fifo
  inst__myaxi_write_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._myaxi_write_req_fifo_enq(_myaxi_write_req_fifo_enq),
    ._myaxi_write_req_fifo_wdata(_myaxi_write_req_fifo_wdata),
    ._myaxi_write_req_fifo_full(_myaxi_write_req_fifo_full),
    ._myaxi_write_req_fifo_almost_full(_myaxi_write_req_fifo_almost_full),
    ._myaxi_write_req_fifo_deq(_myaxi_write_req_fifo_deq),
    ._myaxi_write_req_fifo_rdata(_myaxi_write_req_fifo_rdata),
    ._myaxi_write_req_fifo_empty(_myaxi_write_req_fifo_empty),
    ._myaxi_write_req_fifo_almost_empty(_myaxi_write_req_fifo_almost_empty)
  );

  reg [4-1:0] count__myaxi_write_req_fifo;
  wire [8-1:0] _myaxi_write_op_sel_fifo;
  wire [32-1:0] _myaxi_write_local_addr_fifo;
  wire [32-1:0] _myaxi_write_local_stride_fifo;
  wire [33-1:0] _myaxi_write_size_fifo;
  wire [32-1:0] _myaxi_write_local_blocksize_fifo;
  wire [8-1:0] unpack_write_req_op_sel_35;
  wire [32-1:0] unpack_write_req_local_addr_36;
  wire [32-1:0] unpack_write_req_local_stride_37;
  wire [33-1:0] unpack_write_req_size_38;
  wire [32-1:0] unpack_write_req_local_blocksize_39;
  assign unpack_write_req_op_sel_35 = _myaxi_write_req_fifo_rdata[136:129];
  assign unpack_write_req_local_addr_36 = _myaxi_write_req_fifo_rdata[128:97];
  assign unpack_write_req_local_stride_37 = _myaxi_write_req_fifo_rdata[96:65];
  assign unpack_write_req_size_38 = _myaxi_write_req_fifo_rdata[64:32];
  assign unpack_write_req_local_blocksize_39 = _myaxi_write_req_fifo_rdata[31:0];
  assign _myaxi_write_op_sel_fifo = unpack_write_req_op_sel_35;
  assign _myaxi_write_local_addr_fifo = unpack_write_req_local_addr_36;
  assign _myaxi_write_local_stride_fifo = unpack_write_req_local_stride_37;
  assign _myaxi_write_size_fifo = unpack_write_req_size_38;
  assign _myaxi_write_local_blocksize_fifo = unpack_write_req_local_blocksize_39;
  reg [8-1:0] _myaxi_write_op_sel_buf;
  reg [32-1:0] _myaxi_write_local_addr_buf;
  reg [32-1:0] _myaxi_write_local_stride_buf;
  reg [33-1:0] _myaxi_write_size_buf;
  reg [32-1:0] _myaxi_write_local_blocksize_buf;
  reg _myaxi_write_req_busy;
  reg _myaxi_write_data_busy;
  wire _myaxi_write_req_idle;
  wire _myaxi_write_data_idle;
  wire _myaxi_write_idle;
  assign _myaxi_write_req_idle = !_myaxi_write_start && !_myaxi_write_req_busy;
  assign _myaxi_write_data_idle = _myaxi_write_req_fifo_empty && !_myaxi_write_data_busy;
  assign _myaxi_write_idle = _myaxi_write_req_idle && _myaxi_write_data_idle;
  reg [32-1:0] th_matmul;
  localparam th_matmul_init = 0;
  reg signed [32-1:0] _th_matmul_matrix_size_0;
  reg signed [32-1:0] _th_matmul_a_offset_1;
  reg signed [32-1:0] _th_matmul_b_offset_2;
  reg signed [32-1:0] _th_matmul_c_offset_3;
  reg signed [32-1:0] _th_matmul_start_time_4;
  reg signed [32-1:0] _th_matmul_matrix_size_5;
  reg signed [32-1:0] _th_matmul_a_offset_6;
  reg signed [32-1:0] _th_matmul_b_offset_7;
  reg signed [32-1:0] _th_matmul_c_offset_8;
  reg signed [32-1:0] _th_matmul_a_addr_9;
  reg signed [32-1:0] _th_matmul_c_addr_10;
  reg signed [32-1:0] _th_matmul_i_11;
  wire [32-1:0] mask_addr_shifted_40;
  assign mask_addr_shifted_40 = _th_matmul_a_addr_9 >> 2;
  wire [32-1:0] mask_addr_masked_41;
  assign mask_addr_masked_41 = mask_addr_shifted_40 << 2;
  reg [32-1:0] _myaxi_read_req_fsm;
  localparam _myaxi_read_req_fsm_init = 0;
  reg [33-1:0] _myaxi_read_cur_global_size;
  reg _myaxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_42;
  wire [32-1:0] pack_read_req_local_addr_43;
  wire [32-1:0] pack_read_req_local_stride_44;
  wire [33-1:0] pack_read_req_local_size_45;
  wire [32-1:0] pack_read_req_local_blocksize_46;
  assign pack_read_req_op_sel_42 = _myaxi_read_op_sel;
  assign pack_read_req_local_addr_43 = _myaxi_read_local_addr;
  assign pack_read_req_local_stride_44 = _myaxi_read_local_stride;
  assign pack_read_req_local_size_45 = _myaxi_read_local_size;
  assign pack_read_req_local_blocksize_46 = _myaxi_read_local_blocksize;
  wire [137-1:0] pack_read_req_packed_47;
  assign pack_read_req_packed_47 = { pack_read_req_op_sel_42, pack_read_req_local_addr_43, pack_read_req_local_stride_44, pack_read_req_local_size_45, pack_read_req_local_blocksize_46 };
  assign _myaxi_read_req_fifo_wdata = ((_myaxi_read_req_fsm == 0) && _myaxi_read_start && !_myaxi_read_req_fifo_almost_full)? pack_read_req_packed_47 : 'hx;
  assign _myaxi_read_req_fifo_enq = ((_myaxi_read_req_fsm == 0) && _myaxi_read_start && !_myaxi_read_req_fifo_almost_full)? (_myaxi_read_req_fsm == 0) && _myaxi_read_start && !_myaxi_read_req_fifo_almost_full && !_myaxi_read_req_fifo_almost_full : 0;
  localparam _tmp_48 = 1;
  wire [_tmp_48-1:0] _tmp_49;
  assign _tmp_49 = !_myaxi_read_req_fifo_almost_full;
  reg [_tmp_48-1:0] __tmp_49_1;
  wire [32-1:0] mask_addr_shifted_50;
  assign mask_addr_shifted_50 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_51;
  assign mask_addr_masked_51 = mask_addr_shifted_50 << 2;
  wire [32-1:0] mask_addr_shifted_52;
  assign mask_addr_shifted_52 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_53;
  assign mask_addr_masked_53 = mask_addr_shifted_52 << 2;
  wire [32-1:0] mask_addr_shifted_54;
  assign mask_addr_shifted_54 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_55;
  assign mask_addr_masked_55 = mask_addr_shifted_54 << 2;
  wire [32-1:0] mask_addr_shifted_56;
  assign mask_addr_shifted_56 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_57;
  assign mask_addr_masked_57 = mask_addr_shifted_56 << 2;
  wire [32-1:0] mask_addr_shifted_58;
  assign mask_addr_shifted_58 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_59;
  assign mask_addr_masked_59 = mask_addr_shifted_58 << 2;
  wire [32-1:0] mask_addr_shifted_60;
  assign mask_addr_shifted_60 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_61;
  assign mask_addr_masked_61 = mask_addr_shifted_60 << 2;
  reg _myaxi_raddr_cond_0_1;
  reg [32-1:0] _myaxi_read_data_fsm;
  localparam _myaxi_read_data_fsm_init = 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_62;
  reg [10-1:0] write_burst_stride_63;
  reg [33-1:0] write_burst_length_64;
  reg write_burst_done_65;
  assign ram_a_0_wdata = ((write_burst_fsm_0 == 1) && _myaxi_rvalid_sb_0)? _myaxi_rdata_sb_0 : 'hx;
  assign ram_a_0_wenable = ((write_burst_fsm_0 == 1) && _myaxi_rvalid_sb_0)? 1'd1 : 0;
  reg signed [32-1:0] _th_matmul_b_addr_12;
  reg signed [32-1:0] _th_matmul_j_13;
  wire [32-1:0] mask_addr_shifted_66;
  assign mask_addr_shifted_66 = _th_matmul_b_addr_12 >> 2;
  wire [32-1:0] mask_addr_masked_67;
  assign mask_addr_masked_67 = mask_addr_shifted_66 << 2;
  reg [32-1:0] write_burst_fsm_1;
  localparam write_burst_fsm_1_init = 0;
  reg [10-1:0] write_burst_addr_68;
  reg [10-1:0] write_burst_stride_69;
  reg [33-1:0] write_burst_length_70;
  reg write_burst_done_71;
  assign ram_b_0_wdata = ((write_burst_fsm_1 == 1) && _myaxi_rvalid_sb_0)? _myaxi_rdata_sb_0 : 'hx;
  assign ram_b_0_wenable = ((write_burst_fsm_1 == 1) && _myaxi_rvalid_sb_0)? 1'd1 : 0;
  reg signed [32-1:0] _th_matmul_sum_14;
  reg signed [32-1:0] _th_matmul_k_15;
  assign ram_a_0_addr = (th_matmul == 16)? _th_matmul_k_15 : 
                        ((write_burst_fsm_0 == 1) && _myaxi_rvalid_sb_0)? write_burst_addr_62 : 'hx;
  assign ram_a_0_enable = (th_matmul == 16)? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && _myaxi_rvalid_sb_0)? 1'd1 : 0;
  localparam _tmp_72 = 1;
  wire [_tmp_72-1:0] _tmp_73;
  assign _tmp_73 = th_matmul == 16;
  reg [_tmp_72-1:0] __tmp_73_1;
  reg signed [32-1:0] read_rdata_74;
  reg signed [32-1:0] _th_matmul_x_16;
  assign ram_b_0_addr = (th_matmul == 18)? _th_matmul_k_15 : 
                        ((write_burst_fsm_1 == 1) && _myaxi_rvalid_sb_0)? write_burst_addr_68 : 'hx;
  assign ram_b_0_enable = (th_matmul == 18)? 1'd1 : 
                          ((write_burst_fsm_1 == 1) && _myaxi_rvalid_sb_0)? 1'd1 : 0;
  localparam _tmp_75 = 1;
  wire [_tmp_75-1:0] _tmp_76;
  assign _tmp_76 = th_matmul == 18;
  reg [_tmp_75-1:0] __tmp_76_1;
  reg signed [32-1:0] read_rdata_77;
  reg signed [32-1:0] _th_matmul_y_17;
  wire [32-1:0] mask_addr_shifted_78;
  assign mask_addr_shifted_78 = _th_matmul_c_addr_10 >> 2;
  wire [32-1:0] mask_addr_masked_79;
  assign mask_addr_masked_79 = mask_addr_shifted_78 << 2;
  reg [32-1:0] _myaxi_write_req_fsm;
  localparam _myaxi_write_req_fsm_init = 0;
  reg [33-1:0] _myaxi_write_cur_global_size;
  reg _myaxi_write_cont;
  wire [8-1:0] pack_write_req_op_sel_80;
  wire [32-1:0] pack_write_req_local_addr_81;
  wire [32-1:0] pack_write_req_local_stride_82;
  wire [33-1:0] pack_write_req_size_83;
  wire [32-1:0] pack_write_req_local_blocksize_84;
  assign pack_write_req_op_sel_80 = _myaxi_write_op_sel;
  assign pack_write_req_local_addr_81 = _myaxi_write_local_addr;
  assign pack_write_req_local_stride_82 = _myaxi_write_local_stride;
  assign pack_write_req_size_83 = _myaxi_write_local_size;
  assign pack_write_req_local_blocksize_84 = _myaxi_write_local_blocksize;
  wire [137-1:0] pack_write_req_packed_85;
  assign pack_write_req_packed_85 = { pack_write_req_op_sel_80, pack_write_req_local_addr_81, pack_write_req_local_stride_82, pack_write_req_size_83, pack_write_req_local_blocksize_84 };
  localparam _tmp_86 = 1;
  wire [_tmp_86-1:0] _tmp_87;
  assign _tmp_87 = !_myaxi_write_req_fifo_almost_full;
  reg [_tmp_86-1:0] __tmp_87_1;
  wire [32-1:0] mask_addr_shifted_88;
  assign mask_addr_shifted_88 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_89;
  assign mask_addr_masked_89 = mask_addr_shifted_88 << 2;
  wire [32-1:0] mask_addr_shifted_90;
  assign mask_addr_shifted_90 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_91;
  assign mask_addr_masked_91 = mask_addr_shifted_90 << 2;
  wire [32-1:0] mask_addr_shifted_92;
  assign mask_addr_shifted_92 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_93;
  assign mask_addr_masked_93 = mask_addr_shifted_92 << 2;
  wire [32-1:0] mask_addr_shifted_94;
  assign mask_addr_shifted_94 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_95;
  assign mask_addr_masked_95 = mask_addr_shifted_94 << 2;
  wire [32-1:0] mask_addr_shifted_96;
  assign mask_addr_shifted_96 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_97;
  assign mask_addr_masked_97 = mask_addr_shifted_96 << 2;
  wire [32-1:0] mask_addr_shifted_98;
  assign mask_addr_shifted_98 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_99;
  assign mask_addr_masked_99 = mask_addr_shifted_98 << 2;
  wire [8-1:0] pack_write_req_op_sel_100;
  wire [32-1:0] pack_write_req_local_addr_101;
  wire [32-1:0] pack_write_req_local_stride_102;
  wire [33-1:0] pack_write_req_size_103;
  wire [32-1:0] pack_write_req_local_blocksize_104;
  assign pack_write_req_op_sel_100 = _myaxi_write_op_sel;
  assign pack_write_req_local_addr_101 = _myaxi_write_local_addr;
  assign pack_write_req_local_stride_102 = _myaxi_write_local_stride;
  assign pack_write_req_size_103 = _myaxi_write_cur_global_size;
  assign pack_write_req_local_blocksize_104 = _myaxi_write_local_blocksize;
  wire [137-1:0] pack_write_req_packed_105;
  assign pack_write_req_packed_105 = { pack_write_req_op_sel_100, pack_write_req_local_addr_101, pack_write_req_local_stride_102, pack_write_req_size_103, pack_write_req_local_blocksize_104 };
  assign _myaxi_write_req_fifo_wdata = ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6))? pack_write_req_packed_105 : 
                                       ((_myaxi_write_req_fsm == 0) && _myaxi_write_start && !_myaxi_write_req_fifo_almost_full)? pack_write_req_packed_85 : 'hx;
  assign _myaxi_write_req_fifo_enq = ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6))? (_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6) && !_myaxi_write_req_fifo_almost_full : 
                                     ((_myaxi_write_req_fsm == 0) && _myaxi_write_start && !_myaxi_write_req_fifo_almost_full)? (_myaxi_write_req_fsm == 0) && _myaxi_write_start && !_myaxi_write_req_fifo_almost_full && !_myaxi_write_req_fifo_almost_full : 0;
  localparam _tmp_106 = 1;
  wire [_tmp_106-1:0] _tmp_107;
  assign _tmp_107 = !_myaxi_write_req_fifo_almost_full;
  reg [_tmp_106-1:0] __tmp_107_1;
  reg _myaxi_waddr_cond_0_1;
  reg [32-1:0] _myaxi_write_data_fsm;
  localparam _myaxi_write_data_fsm_init = 0;
  reg [32-1:0] read_burst_fsm_2;
  localparam read_burst_fsm_2_init = 0;
  reg [10-1:0] read_burst_addr_108;
  reg [10-1:0] read_burst_stride_109;
  reg [33-1:0] read_burst_length_110;
  reg read_burst_rvalid_111;
  reg read_burst_rlast_112;
  localparam _tmp_113 = 1;
  wire [_tmp_113-1:0] _tmp_114;
  assign _tmp_114 = (read_burst_fsm_2 == 1) && (!read_burst_rvalid_111 || (_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0));
  reg [_tmp_113-1:0] __tmp_114_1;
  wire [32-1:0] read_burst_rdata_115;
  assign read_burst_rdata_115 = ram_c_0_rdata;
  assign _myaxi_write_req_fifo_deq = ((_myaxi_write_data_fsm == 2) && (!_myaxi_write_req_fifo_empty && (_myaxi_write_size_buf == 0)) && !_myaxi_write_req_fifo_empty)? 1 : 
                                     ((_myaxi_write_data_fsm == 0) && (!_myaxi_write_data_busy && !_myaxi_write_req_fifo_empty && (_myaxi_write_op_sel_fifo == 1)) && !_myaxi_write_req_fifo_empty)? 1 : 0;
  reg _myaxi_wdata_cond_0_1;
  reg signed [32-1:0] _th_matmul_end_time_18;
  reg signed [32-1:0] _th_matmul_time_19;
  reg signed [32-1:0] _th_matmul_matrix_size_20;
  reg signed [32-1:0] _th_matmul_a_offset_21;
  reg signed [32-1:0] _th_matmul_b_offset_22;
  reg signed [32-1:0] _th_matmul_c_offset_23;
  reg signed [32-1:0] _th_matmul_all_ok_24;
  reg signed [32-1:0] _th_matmul_c_addr_25;
  reg signed [32-1:0] _th_matmul_i_26;
  wire [32-1:0] mask_addr_shifted_116;
  assign mask_addr_shifted_116 = _th_matmul_c_addr_25 >> 2;
  wire [32-1:0] mask_addr_masked_117;
  assign mask_addr_masked_117 = mask_addr_shifted_116 << 2;
  assign _myaxi_read_req_fifo_deq = ((_myaxi_read_data_fsm == 0) && (!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 3)) && !_myaxi_read_req_fifo_empty)? 1 : 
                                    ((_myaxi_read_data_fsm == 0) && (!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 2)) && !_myaxi_read_req_fifo_empty)? 1 : 
                                    ((_myaxi_read_data_fsm == 0) && (!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 1)) && !_myaxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_3;
  localparam write_burst_fsm_3_init = 0;
  reg [10-1:0] write_burst_addr_118;
  reg [10-1:0] write_burst_stride_119;
  reg [33-1:0] write_burst_length_120;
  reg write_burst_done_121;
  assign ram_c_0_wdata = ((write_burst_fsm_3 == 1) && _myaxi_rvalid_sb_0)? _myaxi_rdata_sb_0 : 
                         (th_matmul == 22)? _th_matmul_sum_14 : 'hx;
  assign ram_c_0_wenable = ((write_burst_fsm_3 == 1) && _myaxi_rvalid_sb_0)? 1'd1 : 
                           (th_matmul == 22)? 1'd1 : 0;
  assign _myaxi_rready_sb_0 = (_myaxi_read_data_fsm == 2) || (_myaxi_read_data_fsm == 2) || (_myaxi_read_data_fsm == 2);
  reg signed [32-1:0] _th_matmul_j_27;
  assign ram_c_0_addr = (th_matmul == 42)? _th_matmul_j_27 : 
                        ((write_burst_fsm_3 == 1) && _myaxi_rvalid_sb_0)? write_burst_addr_118 : 
                        ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_111 || (_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0)))? read_burst_addr_108 : 
                        (th_matmul == 22)? _th_matmul_j_13 : 'hx;
  assign ram_c_0_enable = (th_matmul == 42)? 1'd1 : 
                          ((write_burst_fsm_3 == 1) && _myaxi_rvalid_sb_0)? 1'd1 : 
                          ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_111 || (_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0)))? 1'd1 : 
                          (th_matmul == 22)? 1'd1 : 0;
  localparam _tmp_122 = 1;
  wire [_tmp_122-1:0] _tmp_123;
  assign _tmp_123 = th_matmul == 42;
  reg [_tmp_122-1:0] __tmp_123_1;
  reg signed [32-1:0] read_rdata_124;
  reg signed [32-1:0] _th_matmul_v_28;

  always @(posedge CLK) begin
    if(RST) begin
      timer <= 0;
    end else begin
      timer <= timer + 1;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_73_1 <= 0;
    end else begin
      __tmp_73_1 <= _tmp_73;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_76_1 <= 0;
    end else begin
      __tmp_76_1 <= _tmp_76;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_114_1 <= 0;
      __tmp_123_1 <= 0;
    end else begin
      __tmp_114_1 <= _tmp_114;
      __tmp_123_1 <= _tmp_123;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _myaxi_waddr_cond_0_1 <= 0;
    end else begin
      if(_myaxi_waddr_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (_myaxi_outstanding_wcount < 6) && ((_myaxi_outstanding_wcount < 6) && (myaxi_awready || !myaxi_awvalid))) begin
        myaxi_awaddr <= _myaxi_write_global_addr;
        myaxi_awlen <= _myaxi_write_cur_global_size - 1;
        myaxi_awvalid <= 1;
      end 
      if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (_myaxi_outstanding_wcount < 6) && ((_myaxi_outstanding_wcount < 6) && (myaxi_awready || !myaxi_awvalid)) && (_myaxi_write_cur_global_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_waddr_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_wdata_sb_0 <= 0;
      _myaxi_wvalid_sb_0 <= 0;
      _myaxi_wlast_sb_0 <= 0;
      _myaxi_wstrb_sb_0 <= 0;
      _myaxi_wdata_cond_0_1 <= 0;
    end else begin
      if(_myaxi_wdata_cond_0_1) begin
        _myaxi_wvalid_sb_0 <= 0;
        _myaxi_wlast_sb_0 <= 0;
      end 
      if((_myaxi_write_op_sel_buf == 1) && read_burst_rvalid_111 && ((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0)) && (_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0)) begin
        _myaxi_wdata_sb_0 <= read_burst_rdata_115;
        _myaxi_wvalid_sb_0 <= 1;
        _myaxi_wlast_sb_0 <= read_burst_rlast_112 || (_myaxi_write_size_buf == 1);
        _myaxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      _myaxi_wdata_cond_0_1 <= 1;
      if(_myaxi_wvalid_sb_0 && !_myaxi_wready_sb_0) begin
        _myaxi_wvalid_sb_0 <= _myaxi_wvalid_sb_0;
        _myaxi_wlast_sb_0 <= _myaxi_wlast_sb_0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb_myaxi_writedata_data_6 <= 0;
      _sb_myaxi_writedata_valid_7 <= 0;
      _sb_myaxi_writedata_tmp_data_9 <= 0;
      _sb_myaxi_writedata_tmp_valid_10 <= 0;
    end else begin
      if(_sb_myaxi_writedata_m_ready_5 || !_sb_myaxi_writedata_valid_7) begin
        _sb_myaxi_writedata_data_6 <= _sb_myaxi_writedata_next_data_11;
        _sb_myaxi_writedata_valid_7 <= _sb_myaxi_writedata_next_valid_12;
      end 
      if(!_sb_myaxi_writedata_tmp_valid_10 && _sb_myaxi_writedata_valid_7 && !_sb_myaxi_writedata_m_ready_5) begin
        _sb_myaxi_writedata_tmp_data_9 <= _sb_myaxi_writedata_s_data_3;
        _sb_myaxi_writedata_tmp_valid_10 <= _sb_myaxi_writedata_s_valid_4;
      end 
      if(_sb_myaxi_writedata_tmp_valid_10 && _sb_myaxi_writedata_m_ready_5) begin
        _sb_myaxi_writedata_tmp_valid_10 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _myaxi_raddr_cond_0_1 <= 0;
    end else begin
      if(_myaxi_raddr_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_myaxi_read_req_fsm == 1) && (myaxi_arready || !myaxi_arvalid)) begin
        myaxi_araddr <= _myaxi_read_global_addr;
        myaxi_arlen <= _myaxi_read_cur_global_size - 1;
        myaxi_arvalid <= 1;
      end 
      _myaxi_raddr_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb_myaxi_readdata_data_21 <= 0;
      _sb_myaxi_readdata_valid_22 <= 0;
      _sb_myaxi_readdata_tmp_data_24 <= 0;
      _sb_myaxi_readdata_tmp_valid_25 <= 0;
    end else begin
      if(_sb_myaxi_readdata_m_ready_20 || !_sb_myaxi_readdata_valid_22) begin
        _sb_myaxi_readdata_data_21 <= _sb_myaxi_readdata_next_data_26;
        _sb_myaxi_readdata_valid_22 <= _sb_myaxi_readdata_next_valid_27;
      end 
      if(!_sb_myaxi_readdata_tmp_valid_25 && _sb_myaxi_readdata_valid_22 && !_sb_myaxi_readdata_m_ready_20) begin
        _sb_myaxi_readdata_tmp_data_24 <= _sb_myaxi_readdata_s_data_18;
        _sb_myaxi_readdata_tmp_valid_25 <= _sb_myaxi_readdata_s_valid_19;
      end 
      if(_sb_myaxi_readdata_tmp_valid_25 && _sb_myaxi_readdata_m_ready_20) begin
        _sb_myaxi_readdata_tmp_valid_25 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_outstanding_wcount <= 0;
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_global_size <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_local_stride <= 0;
      _myaxi_read_local_size <= 0;
      _myaxi_read_local_blocksize <= 0;
      _myaxi_read_req_busy <= 0;
      _myaxi_read_cur_global_size <= 0;
      _myaxi_read_data_busy <= 0;
      _myaxi_read_op_sel_buf <= 0;
      _myaxi_read_local_addr_buf <= 0;
      _myaxi_read_local_stride_buf <= 0;
      _myaxi_read_local_size_buf <= 0;
      _myaxi_read_local_blocksize_buf <= 0;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_global_size <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_local_stride <= 0;
      _myaxi_write_local_size <= 0;
      _myaxi_write_local_blocksize <= 0;
      _myaxi_write_req_busy <= 0;
      _myaxi_write_cur_global_size <= 0;
      _myaxi_write_data_busy <= 0;
      _myaxi_write_op_sel_buf <= 0;
      _myaxi_write_local_addr_buf <= 0;
      _myaxi_write_local_stride_buf <= 0;
      _myaxi_write_size_buf <= 0;
      _myaxi_write_local_blocksize_buf <= 0;
    end else begin
      if(myaxi_awvalid && myaxi_awready && !(myaxi_bvalid && myaxi_bready) && (_myaxi_outstanding_wcount < 7)) begin
        _myaxi_outstanding_wcount <= _myaxi_outstanding_wcount + 1;
      end 
      if(!(myaxi_awvalid && myaxi_awready) && (myaxi_bvalid && myaxi_bready) && (_myaxi_outstanding_wcount > 0)) begin
        _myaxi_outstanding_wcount <= _myaxi_outstanding_wcount - 1;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      if((th_matmul == 6) && _myaxi_read_req_idle) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= 1;
        _myaxi_read_global_addr <= mask_addr_masked_41;
        _myaxi_read_global_size <= _th_matmul_matrix_size_5;
        _myaxi_read_local_addr <= 0;
        _myaxi_read_local_stride <= 1;
        _myaxi_read_local_size <= _th_matmul_matrix_size_5;
        _myaxi_read_local_blocksize <= 1;
      end 
      if((_myaxi_read_req_fsm == 0) && _myaxi_read_start) begin
        _myaxi_read_req_busy <= 1;
      end 
      if(_myaxi_read_start && _myaxi_read_req_fifo_almost_full) begin
        _myaxi_read_start <= 1;
      end 
      if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full && (_myaxi_read_global_size <= 256) && ((mask_addr_masked_51 & 4095) + (_myaxi_read_global_size << 2) >= 4096)) begin
        _myaxi_read_cur_global_size <= 4096 - (mask_addr_masked_53 & 4095) >> 2;
        _myaxi_read_global_size <= _myaxi_read_global_size - (4096 - (mask_addr_masked_55 & 4095) >> 2);
      end else if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full && (_myaxi_read_global_size <= 256)) begin
        _myaxi_read_cur_global_size <= _myaxi_read_global_size;
        _myaxi_read_global_size <= 0;
      end else if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full && ((mask_addr_masked_57 & 4095) + 1024 >= 4096)) begin
        _myaxi_read_cur_global_size <= 4096 - (mask_addr_masked_59 & 4095) >> 2;
        _myaxi_read_global_size <= _myaxi_read_global_size - (4096 - (mask_addr_masked_61 & 4095) >> 2);
      end else if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full) begin
        _myaxi_read_cur_global_size <= 256;
        _myaxi_read_global_size <= _myaxi_read_global_size - 256;
      end 
      if((_myaxi_read_req_fsm == 1) && (myaxi_arready || !myaxi_arvalid)) begin
        _myaxi_read_global_addr <= _myaxi_read_global_addr + (_myaxi_read_cur_global_size << 2);
      end 
      if((_myaxi_read_req_fsm == 1) && (myaxi_arready || !myaxi_arvalid) && (_myaxi_read_global_size == 0)) begin
        _myaxi_read_req_busy <= 0;
      end 
      if((_myaxi_read_data_fsm == 0) && (!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 1))) begin
        _myaxi_read_data_busy <= 1;
        _myaxi_read_op_sel_buf <= _myaxi_read_op_sel_fifo;
        _myaxi_read_local_addr_buf <= _myaxi_read_local_addr_fifo;
        _myaxi_read_local_stride_buf <= _myaxi_read_local_stride_fifo;
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_fifo;
        _myaxi_read_local_blocksize_buf <= _myaxi_read_local_blocksize_fifo;
      end 
      if((_myaxi_read_data_fsm == 2) && _myaxi_rvalid_sb_0) begin
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_buf - 1;
      end 
      if((_myaxi_read_data_fsm == 2) && _myaxi_rvalid_sb_0 && (_myaxi_read_local_size_buf <= 1)) begin
        _myaxi_read_data_busy <= 0;
      end 
      if((th_matmul == 11) && _myaxi_read_req_idle) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= 2;
        _myaxi_read_global_addr <= mask_addr_masked_67;
        _myaxi_read_global_size <= _th_matmul_matrix_size_5;
        _myaxi_read_local_addr <= 0;
        _myaxi_read_local_stride <= 1;
        _myaxi_read_local_size <= _th_matmul_matrix_size_5;
        _myaxi_read_local_blocksize <= 1;
      end 
      if((_myaxi_read_data_fsm == 0) && (!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 2))) begin
        _myaxi_read_data_busy <= 1;
        _myaxi_read_op_sel_buf <= _myaxi_read_op_sel_fifo;
        _myaxi_read_local_addr_buf <= _myaxi_read_local_addr_fifo;
        _myaxi_read_local_stride_buf <= _myaxi_read_local_stride_fifo;
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_fifo;
        _myaxi_read_local_blocksize_buf <= _myaxi_read_local_blocksize_fifo;
      end 
      if((_myaxi_read_data_fsm == 2) && _myaxi_rvalid_sb_0) begin
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_buf - 1;
      end 
      if((_myaxi_read_data_fsm == 2) && _myaxi_rvalid_sb_0 && (_myaxi_read_local_size_buf <= 1)) begin
        _myaxi_read_data_busy <= 0;
      end 
      if((th_matmul == 25) && _myaxi_write_req_idle) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= 1;
        _myaxi_write_global_addr <= mask_addr_masked_79;
        _myaxi_write_global_size <= _th_matmul_matrix_size_5;
        _myaxi_write_local_addr <= 0;
        _myaxi_write_local_stride <= 1;
        _myaxi_write_local_size <= _th_matmul_matrix_size_5;
        _myaxi_write_local_blocksize <= 1;
      end 
      if((_myaxi_write_req_fsm == 0) && _myaxi_write_start) begin
        _myaxi_write_req_busy <= 1;
      end 
      if(_myaxi_write_start && _myaxi_write_req_fifo_almost_full) begin
        _myaxi_write_start <= 1;
      end 
      if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full && (_myaxi_write_global_size <= 256) && ((mask_addr_masked_89 & 4095) + (_myaxi_write_global_size << 2) >= 4096)) begin
        _myaxi_write_cur_global_size <= 4096 - (mask_addr_masked_91 & 4095) >> 2;
        _myaxi_write_global_size <= _myaxi_write_global_size - (4096 - (mask_addr_masked_93 & 4095) >> 2);
      end else if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full && (_myaxi_write_global_size <= 256)) begin
        _myaxi_write_cur_global_size <= _myaxi_write_global_size;
        _myaxi_write_global_size <= 0;
      end else if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full && ((mask_addr_masked_95 & 4095) + 1024 >= 4096)) begin
        _myaxi_write_cur_global_size <= 4096 - (mask_addr_masked_97 & 4095) >> 2;
        _myaxi_write_global_size <= _myaxi_write_global_size - (4096 - (mask_addr_masked_99 & 4095) >> 2);
      end else if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full) begin
        _myaxi_write_cur_global_size <= 256;
        _myaxi_write_global_size <= _myaxi_write_global_size - 256;
      end 
      if((_myaxi_write_req_fsm == 1) && ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6))) begin
        _myaxi_write_global_addr <= _myaxi_write_global_addr + (_myaxi_write_cur_global_size << 2);
      end 
      if((_myaxi_write_req_fsm == 1) && ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6)) && (_myaxi_write_global_size == 0)) begin
        _myaxi_write_req_busy <= 0;
      end 
      if((_myaxi_write_data_fsm == 0) && (!_myaxi_write_data_busy && !_myaxi_write_req_fifo_empty && (_myaxi_write_op_sel_fifo == 1))) begin
        _myaxi_write_data_busy <= 1;
        _myaxi_write_op_sel_buf <= _myaxi_write_op_sel_fifo;
        _myaxi_write_local_addr_buf <= _myaxi_write_local_addr_fifo;
        _myaxi_write_local_stride_buf <= _myaxi_write_local_stride_fifo;
        _myaxi_write_size_buf <= _myaxi_write_size_fifo;
        _myaxi_write_local_blocksize_buf <= _myaxi_write_local_blocksize_fifo;
      end 
      if(_myaxi_write_data_fsm == 1) begin
        _myaxi_write_size_buf <= 0;
      end 
      if((_myaxi_write_data_fsm == 2) && (!_myaxi_write_req_fifo_empty && (_myaxi_write_size_buf == 0))) begin
        _myaxi_write_size_buf <= _myaxi_write_size_fifo;
      end 
      if((_myaxi_write_data_fsm == 2) && read_burst_rvalid_111 && ((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0))) begin
        _myaxi_write_size_buf <= _myaxi_write_size_buf - 1;
      end 
      if((_myaxi_write_data_fsm == 2) && ((_myaxi_write_op_sel_buf == 1) && read_burst_rvalid_111 && ((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0))) && read_burst_rlast_112) begin
        _myaxi_write_data_busy <= 0;
      end 
      if((th_matmul == 38) && _myaxi_read_req_idle) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= 3;
        _myaxi_read_global_addr <= mask_addr_masked_117;
        _myaxi_read_global_size <= _th_matmul_matrix_size_20;
        _myaxi_read_local_addr <= 0;
        _myaxi_read_local_stride <= 1;
        _myaxi_read_local_size <= _th_matmul_matrix_size_20;
        _myaxi_read_local_blocksize <= 1;
      end 
      if((_myaxi_read_data_fsm == 0) && (!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 3))) begin
        _myaxi_read_data_busy <= 1;
        _myaxi_read_op_sel_buf <= _myaxi_read_op_sel_fifo;
        _myaxi_read_local_addr_buf <= _myaxi_read_local_addr_fifo;
        _myaxi_read_local_stride_buf <= _myaxi_read_local_stride_fifo;
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_fifo;
        _myaxi_read_local_blocksize_buf <= _myaxi_read_local_blocksize_fifo;
      end 
      if((_myaxi_read_data_fsm == 2) && _myaxi_rvalid_sb_0) begin
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_buf - 1;
      end 
      if((_myaxi_read_data_fsm == 2) && _myaxi_rvalid_sb_0 && (_myaxi_read_local_size_buf <= 1)) begin
        _myaxi_read_data_busy <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__myaxi_read_req_fifo <= 0;
      __tmp_49_1 <= 0;
    end else begin
      if(_myaxi_read_req_fifo_enq && !_myaxi_read_req_fifo_full && (_myaxi_read_req_fifo_deq && !_myaxi_read_req_fifo_empty)) begin
        count__myaxi_read_req_fifo <= count__myaxi_read_req_fifo;
      end else if(_myaxi_read_req_fifo_enq && !_myaxi_read_req_fifo_full) begin
        count__myaxi_read_req_fifo <= count__myaxi_read_req_fifo + 1;
      end else if(_myaxi_read_req_fifo_deq && !_myaxi_read_req_fifo_empty) begin
        count__myaxi_read_req_fifo <= count__myaxi_read_req_fifo - 1;
      end 
      __tmp_49_1 <= _tmp_49;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__myaxi_write_req_fifo <= 0;
      __tmp_87_1 <= 0;
      __tmp_107_1 <= 0;
    end else begin
      if(_myaxi_write_req_fifo_enq && !_myaxi_write_req_fifo_full && (_myaxi_write_req_fifo_deq && !_myaxi_write_req_fifo_empty)) begin
        count__myaxi_write_req_fifo <= count__myaxi_write_req_fifo;
      end else if(_myaxi_write_req_fifo_enq && !_myaxi_write_req_fifo_full) begin
        count__myaxi_write_req_fifo <= count__myaxi_write_req_fifo + 1;
      end else if(_myaxi_write_req_fifo_deq && !_myaxi_write_req_fifo_empty) begin
        count__myaxi_write_req_fifo <= count__myaxi_write_req_fifo - 1;
      end 
      __tmp_87_1 <= _tmp_87;
      __tmp_107_1 <= _tmp_107;
    end
  end

  localparam th_matmul_1 = 1;
  localparam th_matmul_2 = 2;
  localparam th_matmul_3 = 3;
  localparam th_matmul_4 = 4;
  localparam th_matmul_5 = 5;
  localparam th_matmul_6 = 6;
  localparam th_matmul_7 = 7;
  localparam th_matmul_8 = 8;
  localparam th_matmul_9 = 9;
  localparam th_matmul_10 = 10;
  localparam th_matmul_11 = 11;
  localparam th_matmul_12 = 12;
  localparam th_matmul_13 = 13;
  localparam th_matmul_14 = 14;
  localparam th_matmul_15 = 15;
  localparam th_matmul_16 = 16;
  localparam th_matmul_17 = 17;
  localparam th_matmul_18 = 18;
  localparam th_matmul_19 = 19;
  localparam th_matmul_20 = 20;
  localparam th_matmul_21 = 21;
  localparam th_matmul_22 = 22;
  localparam th_matmul_23 = 23;
  localparam th_matmul_24 = 24;
  localparam th_matmul_25 = 25;
  localparam th_matmul_26 = 26;
  localparam th_matmul_27 = 27;
  localparam th_matmul_28 = 28;
  localparam th_matmul_29 = 29;
  localparam th_matmul_30 = 30;
  localparam th_matmul_31 = 31;
  localparam th_matmul_32 = 32;
  localparam th_matmul_33 = 33;
  localparam th_matmul_34 = 34;
  localparam th_matmul_35 = 35;
  localparam th_matmul_36 = 36;
  localparam th_matmul_37 = 37;
  localparam th_matmul_38 = 38;
  localparam th_matmul_39 = 39;
  localparam th_matmul_40 = 40;
  localparam th_matmul_41 = 41;
  localparam th_matmul_42 = 42;
  localparam th_matmul_43 = 43;
  localparam th_matmul_44 = 44;
  localparam th_matmul_45 = 45;
  localparam th_matmul_46 = 46;
  localparam th_matmul_47 = 47;
  localparam th_matmul_48 = 48;
  localparam th_matmul_49 = 49;
  localparam th_matmul_50 = 50;
  localparam th_matmul_51 = 51;
  localparam th_matmul_52 = 52;
  localparam th_matmul_53 = 53;
  localparam th_matmul_54 = 54;
  localparam th_matmul_55 = 55;
  localparam th_matmul_56 = 56;
  localparam th_matmul_57 = 57;
  localparam th_matmul_58 = 58;

  always @(posedge CLK) begin
    if(RST) begin
      th_matmul <= th_matmul_init;
      _th_matmul_matrix_size_0 <= 0;
      _th_matmul_a_offset_1 <= 0;
      _th_matmul_b_offset_2 <= 0;
      _th_matmul_c_offset_3 <= 0;
      _th_matmul_start_time_4 <= 0;
      _th_matmul_matrix_size_5 <= 0;
      _th_matmul_a_offset_6 <= 0;
      _th_matmul_b_offset_7 <= 0;
      _th_matmul_c_offset_8 <= 0;
      _th_matmul_a_addr_9 <= 0;
      _th_matmul_c_addr_10 <= 0;
      _th_matmul_i_11 <= 0;
      _th_matmul_b_addr_12 <= 0;
      _th_matmul_j_13 <= 0;
      _th_matmul_sum_14 <= 0;
      _th_matmul_k_15 <= 0;
      read_rdata_74 <= 0;
      _th_matmul_x_16 <= 0;
      read_rdata_77 <= 0;
      _th_matmul_y_17 <= 0;
      _th_matmul_end_time_18 <= 0;
      _th_matmul_time_19 <= 0;
      _th_matmul_matrix_size_20 <= 0;
      _th_matmul_a_offset_21 <= 0;
      _th_matmul_b_offset_22 <= 0;
      _th_matmul_c_offset_23 <= 0;
      _th_matmul_all_ok_24 <= 0;
      _th_matmul_c_addr_25 <= 0;
      _th_matmul_i_26 <= 0;
      _th_matmul_j_27 <= 0;
      read_rdata_124 <= 0;
      _th_matmul_v_28 <= 0;
    end else begin
      case(th_matmul)
        th_matmul_init: begin
          _th_matmul_matrix_size_0 <= 16;
          _th_matmul_a_offset_1 <= 0;
          _th_matmul_b_offset_2 <= 1024;
          _th_matmul_c_offset_3 <= 2048;
          th_matmul <= th_matmul_1;
        end
        th_matmul_1: begin
          _th_matmul_start_time_4 <= timer;
          th_matmul <= th_matmul_2;
        end
        th_matmul_2: begin
          _th_matmul_matrix_size_5 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_6 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_7 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_8 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_3;
        end
        th_matmul_3: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_offset_6;
          _th_matmul_c_addr_10 <= _th_matmul_c_offset_8;
          th_matmul <= th_matmul_4;
        end
        th_matmul_4: begin
          _th_matmul_i_11 <= 0;
          th_matmul <= th_matmul_5;
        end
        th_matmul_5: begin
          if(_th_matmul_i_11 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_6;
          end else begin
            th_matmul <= th_matmul_30;
          end
        end
        th_matmul_6: begin
          if(_myaxi_read_req_idle) begin
            th_matmul <= th_matmul_7;
          end 
        end
        th_matmul_7: begin
          if(_myaxi_read_idle) begin
            th_matmul <= th_matmul_8;
          end 
        end
        th_matmul_8: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_offset_7;
          th_matmul <= th_matmul_9;
        end
        th_matmul_9: begin
          _th_matmul_j_13 <= 0;
          th_matmul <= th_matmul_10;
        end
        th_matmul_10: begin
          if(_th_matmul_j_13 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_11;
          end else begin
            th_matmul <= th_matmul_25;
          end
        end
        th_matmul_11: begin
          if(_myaxi_read_req_idle) begin
            th_matmul <= th_matmul_12;
          end 
        end
        th_matmul_12: begin
          if(_myaxi_read_idle) begin
            th_matmul <= th_matmul_13;
          end 
        end
        th_matmul_13: begin
          _th_matmul_sum_14 <= 0;
          th_matmul <= th_matmul_14;
        end
        th_matmul_14: begin
          _th_matmul_k_15 <= 0;
          th_matmul <= th_matmul_15;
        end
        th_matmul_15: begin
          if(_th_matmul_k_15 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_16;
          end else begin
            th_matmul <= th_matmul_22;
          end
        end
        th_matmul_16: begin
          if(__tmp_73_1) begin
            read_rdata_74 <= ram_a_0_rdata;
          end 
          if(__tmp_73_1) begin
            th_matmul <= th_matmul_17;
          end 
        end
        th_matmul_17: begin
          _th_matmul_x_16 <= read_rdata_74;
          th_matmul <= th_matmul_18;
        end
        th_matmul_18: begin
          if(__tmp_76_1) begin
            read_rdata_77 <= ram_b_0_rdata;
          end 
          if(__tmp_76_1) begin
            th_matmul <= th_matmul_19;
          end 
        end
        th_matmul_19: begin
          _th_matmul_y_17 <= read_rdata_77;
          th_matmul <= th_matmul_20;
        end
        th_matmul_20: begin
          _th_matmul_sum_14 <= _th_matmul_sum_14 + _th_matmul_x_16 * _th_matmul_y_17;
          th_matmul <= th_matmul_21;
        end
        th_matmul_21: begin
          _th_matmul_k_15 <= _th_matmul_k_15 + 1;
          th_matmul <= th_matmul_15;
        end
        th_matmul_22: begin
          th_matmul <= th_matmul_23;
        end
        th_matmul_23: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_addr_12 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_24;
        end
        th_matmul_24: begin
          _th_matmul_j_13 <= _th_matmul_j_13 + 1;
          th_matmul <= th_matmul_10;
        end
        th_matmul_25: begin
          if(_myaxi_write_req_idle) begin
            th_matmul <= th_matmul_26;
          end 
        end
        th_matmul_26: begin
          if(_myaxi_write_idle && !_myaxi_has_outstanding_write) begin
            th_matmul <= th_matmul_27;
          end 
        end
        th_matmul_27: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_addr_9 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_28;
        end
        th_matmul_28: begin
          _th_matmul_c_addr_10 <= _th_matmul_c_addr_10 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_29;
        end
        th_matmul_29: begin
          _th_matmul_i_11 <= _th_matmul_i_11 + 1;
          th_matmul <= th_matmul_5;
        end
        th_matmul_30: begin
          _th_matmul_end_time_18 <= timer;
          th_matmul <= th_matmul_31;
        end
        th_matmul_31: begin
          _th_matmul_time_19 <= _th_matmul_end_time_18 - _th_matmul_start_time_4;
          th_matmul <= th_matmul_32;
        end
        th_matmul_32: begin
          $display("Time (cycles): %d", _th_matmul_time_19);
          th_matmul <= th_matmul_33;
        end
        th_matmul_33: begin
          _th_matmul_matrix_size_20 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_21 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_22 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_23 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_34;
        end
        th_matmul_34: begin
          _th_matmul_all_ok_24 <= 1;
          th_matmul <= th_matmul_35;
        end
        th_matmul_35: begin
          _th_matmul_c_addr_25 <= _th_matmul_c_offset_23;
          th_matmul <= th_matmul_36;
        end
        th_matmul_36: begin
          _th_matmul_i_26 <= 0;
          th_matmul <= th_matmul_37;
        end
        th_matmul_37: begin
          if(_th_matmul_i_26 < _th_matmul_matrix_size_20) begin
            th_matmul <= th_matmul_38;
          end else begin
            th_matmul <= th_matmul_53;
          end
        end
        th_matmul_38: begin
          if(_myaxi_read_req_idle) begin
            th_matmul <= th_matmul_39;
          end 
        end
        th_matmul_39: begin
          if(_myaxi_read_idle) begin
            th_matmul <= th_matmul_40;
          end 
        end
        th_matmul_40: begin
          _th_matmul_j_27 <= 0;
          th_matmul <= th_matmul_41;
        end
        th_matmul_41: begin
          if(_th_matmul_j_27 < _th_matmul_matrix_size_20) begin
            th_matmul <= th_matmul_42;
          end else begin
            th_matmul <= th_matmul_51;
          end
        end
        th_matmul_42: begin
          if(__tmp_123_1) begin
            read_rdata_124 <= ram_c_0_rdata;
          end 
          if(__tmp_123_1) begin
            th_matmul <= th_matmul_43;
          end 
        end
        th_matmul_43: begin
          _th_matmul_v_28 <= read_rdata_124;
          th_matmul <= th_matmul_44;
        end
        th_matmul_44: begin
          if((_th_matmul_i_26 == _th_matmul_j_27) && (_th_matmul_v_28 !== (_th_matmul_i_26 + 1 << 1))) begin
            th_matmul <= th_matmul_45;
          end else begin
            th_matmul <= th_matmul_47;
          end
        end
        th_matmul_45: begin
          _th_matmul_all_ok_24 <= 0;
          th_matmul <= th_matmul_46;
        end
        th_matmul_46: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_26, _th_matmul_j_27, _th_matmul_v_28);
          th_matmul <= th_matmul_47;
        end
        th_matmul_47: begin
          if((_th_matmul_i_26 != _th_matmul_j_27) && (_th_matmul_v_28 !== 0)) begin
            th_matmul <= th_matmul_48;
          end else begin
            th_matmul <= th_matmul_50;
          end
        end
        th_matmul_48: begin
          _th_matmul_all_ok_24 <= 0;
          th_matmul <= th_matmul_49;
        end
        th_matmul_49: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_26, _th_matmul_j_27, _th_matmul_v_28);
          th_matmul <= th_matmul_50;
        end
        th_matmul_50: begin
          _th_matmul_j_27 <= _th_matmul_j_27 + 1;
          th_matmul <= th_matmul_41;
        end
        th_matmul_51: begin
          _th_matmul_c_addr_25 <= _th_matmul_c_addr_25 + (_th_matmul_matrix_size_20 << 2);
          th_matmul <= th_matmul_52;
        end
        th_matmul_52: begin
          _th_matmul_i_26 <= _th_matmul_i_26 + 1;
          th_matmul <= th_matmul_37;
        end
        th_matmul_53: begin
          if(_th_matmul_all_ok_24) begin
            th_matmul <= th_matmul_54;
          end else begin
            th_matmul <= th_matmul_56;
          end
        end
        th_matmul_54: begin
          $display("# verify: PASSED");
          th_matmul <= th_matmul_55;
        end
        th_matmul_55: begin
          th_matmul <= th_matmul_57;
        end
        th_matmul_56: begin
          $display("# verify: FAILED");
          th_matmul <= th_matmul_57;
        end
        th_matmul_57: begin
          $finish;
          th_matmul <= th_matmul_58;
        end
      endcase
    end
  end

  localparam _myaxi_read_req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_req_fsm <= _myaxi_read_req_fsm_init;
      _myaxi_read_cont <= 0;
    end else begin
      case(_myaxi_read_req_fsm)
        _myaxi_read_req_fsm_init: begin
          if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full) begin
            _myaxi_read_req_fsm <= _myaxi_read_req_fsm_1;
          end 
        end
        _myaxi_read_req_fsm_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_cont <= 1;
          end 
          if((myaxi_arready || !myaxi_arvalid) && (_myaxi_read_global_size == 0)) begin
            _myaxi_read_cont <= 0;
          end 
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_req_fsm <= _myaxi_read_req_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _myaxi_read_data_fsm_1 = 1;
  localparam _myaxi_read_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_data_fsm <= _myaxi_read_data_fsm_init;
    end else begin
      case(_myaxi_read_data_fsm)
        _myaxi_read_data_fsm_init: begin
          if(!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_1;
          end 
          if(!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 2)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_1;
          end 
          if(!_myaxi_read_data_busy && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 3)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_1;
          end 
        end
        _myaxi_read_data_fsm_1: begin
          _myaxi_read_data_fsm <= _myaxi_read_data_fsm_2;
          _myaxi_read_data_fsm <= _myaxi_read_data_fsm_2;
          _myaxi_read_data_fsm <= _myaxi_read_data_fsm_2;
        end
        _myaxi_read_data_fsm_2: begin
          if(_myaxi_rvalid_sb_0 && (_myaxi_read_local_size_buf <= 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_init;
          end 
          if(_myaxi_rvalid_sb_0 && (_myaxi_read_local_size_buf <= 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_init;
          end 
          if(_myaxi_rvalid_sb_0 && (_myaxi_read_local_size_buf <= 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_0_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_0 <= write_burst_fsm_0_init;
      write_burst_addr_62 <= 0;
      write_burst_stride_63 <= 0;
      write_burst_length_64 <= 0;
      write_burst_done_65 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_62 <= _myaxi_read_local_addr_buf;
          write_burst_stride_63 <= _myaxi_read_local_stride_buf;
          write_burst_length_64 <= _myaxi_read_local_size_buf;
          write_burst_done_65 <= 0;
          if((_myaxi_read_data_fsm == 1) && (_myaxi_read_op_sel_buf == 1) && (_myaxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(_myaxi_rvalid_sb_0) begin
            write_burst_addr_62 <= write_burst_addr_62 + write_burst_stride_63;
            write_burst_length_64 <= write_burst_length_64 - 1;
            write_burst_done_65 <= 0;
          end 
          if(_myaxi_rvalid_sb_0 && (write_burst_length_64 <= 1)) begin
            write_burst_done_65 <= 1;
          end 
          if(_myaxi_rvalid_sb_0 && 0) begin
            write_burst_done_65 <= 1;
          end 
          if(_myaxi_rvalid_sb_0 && (write_burst_length_64 <= 1)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(_myaxi_rvalid_sb_0 && 0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_1 <= write_burst_fsm_1_init;
      write_burst_addr_68 <= 0;
      write_burst_stride_69 <= 0;
      write_burst_length_70 <= 0;
      write_burst_done_71 <= 0;
    end else begin
      case(write_burst_fsm_1)
        write_burst_fsm_1_init: begin
          write_burst_addr_68 <= _myaxi_read_local_addr_buf;
          write_burst_stride_69 <= _myaxi_read_local_stride_buf;
          write_burst_length_70 <= _myaxi_read_local_size_buf;
          write_burst_done_71 <= 0;
          if((_myaxi_read_data_fsm == 1) && (_myaxi_read_op_sel_buf == 2) && (_myaxi_read_local_size_buf > 0)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_1;
          end 
        end
        write_burst_fsm_1_1: begin
          if(_myaxi_rvalid_sb_0) begin
            write_burst_addr_68 <= write_burst_addr_68 + write_burst_stride_69;
            write_burst_length_70 <= write_burst_length_70 - 1;
            write_burst_done_71 <= 0;
          end 
          if(_myaxi_rvalid_sb_0 && (write_burst_length_70 <= 1)) begin
            write_burst_done_71 <= 1;
          end 
          if(_myaxi_rvalid_sb_0 && 0) begin
            write_burst_done_71 <= 1;
          end 
          if(_myaxi_rvalid_sb_0 && (write_burst_length_70 <= 1)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(_myaxi_rvalid_sb_0 && 0) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(0) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _myaxi_write_req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_req_fsm <= _myaxi_write_req_fsm_init;
      _myaxi_write_cont <= 0;
    end else begin
      case(_myaxi_write_req_fsm)
        _myaxi_write_req_fsm_init: begin
          if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full) begin
            _myaxi_write_req_fsm <= _myaxi_write_req_fsm_1;
          end 
        end
        _myaxi_write_req_fsm_1: begin
          if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6)) begin
            _myaxi_write_cont <= 1;
          end 
          if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6) && (_myaxi_write_global_size == 0)) begin
            _myaxi_write_cont <= 0;
          end 
          if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (_myaxi_outstanding_wcount < 6)) begin
            _myaxi_write_req_fsm <= _myaxi_write_req_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _myaxi_write_data_fsm_1 = 1;
  localparam _myaxi_write_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_data_fsm <= _myaxi_write_data_fsm_init;
    end else begin
      case(_myaxi_write_data_fsm)
        _myaxi_write_data_fsm_init: begin
          if(!_myaxi_write_data_busy && !_myaxi_write_req_fifo_empty && (_myaxi_write_op_sel_fifo == 1)) begin
            _myaxi_write_data_fsm <= _myaxi_write_data_fsm_1;
          end 
        end
        _myaxi_write_data_fsm_1: begin
          _myaxi_write_data_fsm <= _myaxi_write_data_fsm_2;
        end
        _myaxi_write_data_fsm_2: begin
          if((_myaxi_write_op_sel_buf == 1) && read_burst_rvalid_111 && ((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0)) && read_burst_rlast_112) begin
            _myaxi_write_data_fsm <= _myaxi_write_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam read_burst_fsm_2_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      read_burst_fsm_2 <= read_burst_fsm_2_init;
      read_burst_addr_108 <= 0;
      read_burst_stride_109 <= 0;
      read_burst_length_110 <= 0;
      read_burst_rvalid_111 <= 0;
      read_burst_rlast_112 <= 0;
    end else begin
      case(read_burst_fsm_2)
        read_burst_fsm_2_init: begin
          read_burst_addr_108 <= _myaxi_write_local_addr_buf;
          read_burst_stride_109 <= _myaxi_write_local_stride_buf;
          read_burst_length_110 <= _myaxi_write_size_buf;
          read_burst_rvalid_111 <= 0;
          read_burst_rlast_112 <= 0;
          if((_myaxi_write_data_fsm == 1) && (_myaxi_write_op_sel_buf == 1) && (_myaxi_write_size_buf > 0)) begin
            read_burst_fsm_2 <= read_burst_fsm_2_1;
          end 
        end
        read_burst_fsm_2_1: begin
          if((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0) && (read_burst_length_110 > 0)) begin
            read_burst_addr_108 <= read_burst_addr_108 + read_burst_stride_109;
            read_burst_length_110 <= read_burst_length_110 - 1;
            read_burst_rvalid_111 <= 1;
          end 
          if((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0) && (read_burst_length_110 <= 1)) begin
            read_burst_rlast_112 <= 1;
          end 
          if(read_burst_rlast_112 && read_burst_rvalid_111 && ((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0))) begin
            read_burst_rvalid_111 <= 0;
            read_burst_rlast_112 <= 0;
          end 
          if(0) begin
            read_burst_rvalid_111 <= 0;
            read_burst_rlast_112 <= 0;
          end 
          if(read_burst_rlast_112 && read_burst_rvalid_111 && ((_myaxi_wready_sb_0 || !_myaxi_wvalid_sb_0) && (_myaxi_write_size_buf > 0))) begin
            read_burst_fsm_2 <= read_burst_fsm_2_init;
          end 
          if(0) begin
            read_burst_fsm_2 <= read_burst_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_3_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_3 <= write_burst_fsm_3_init;
      write_burst_addr_118 <= 0;
      write_burst_stride_119 <= 0;
      write_burst_length_120 <= 0;
      write_burst_done_121 <= 0;
    end else begin
      case(write_burst_fsm_3)
        write_burst_fsm_3_init: begin
          write_burst_addr_118 <= _myaxi_read_local_addr_buf;
          write_burst_stride_119 <= _myaxi_read_local_stride_buf;
          write_burst_length_120 <= _myaxi_read_local_size_buf;
          write_burst_done_121 <= 0;
          if((_myaxi_read_data_fsm == 1) && (_myaxi_read_op_sel_buf == 3) && (_myaxi_read_local_size_buf > 0)) begin
            write_burst_fsm_3 <= write_burst_fsm_3_1;
          end 
        end
        write_burst_fsm_3_1: begin
          if(_myaxi_rvalid_sb_0) begin
            write_burst_addr_118 <= write_burst_addr_118 + write_burst_stride_119;
            write_burst_length_120 <= write_burst_length_120 - 1;
            write_burst_done_121 <= 0;
          end 
          if(_myaxi_rvalid_sb_0 && (write_burst_length_120 <= 1)) begin
            write_burst_done_121 <= 1;
          end 
          if(_myaxi_rvalid_sb_0 && 0) begin
            write_burst_done_121 <= 1;
          end 
          if(_myaxi_rvalid_sb_0 && (write_burst_length_120 <= 1)) begin
            write_burst_fsm_3 <= write_burst_fsm_3_init;
          end 
          if(_myaxi_rvalid_sb_0 && 0) begin
            write_burst_fsm_3 <= write_burst_fsm_3_init;
          end 
          if(0) begin
            write_burst_fsm_3 <= write_burst_fsm_3_init;
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



module ram_c
(
  input CLK,
  input [10-1:0] ram_c_0_addr,
  output [32-1:0] ram_c_0_rdata,
  input [32-1:0] ram_c_0_wdata,
  input ram_c_0_wenable,
  input ram_c_0_enable
);

  reg [32-1:0] ram_c_0_rdata_out;
  assign ram_c_0_rdata = ram_c_0_rdata_out;
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


endmodule



module _myaxi_read_req_fifo
(
  input CLK,
  input RST,
  input _myaxi_read_req_fifo_enq,
  input [137-1:0] _myaxi_read_req_fifo_wdata,
  output _myaxi_read_req_fifo_full,
  output _myaxi_read_req_fifo_almost_full,
  input _myaxi_read_req_fifo_deq,
  output [137-1:0] _myaxi_read_req_fifo_rdata,
  output _myaxi_read_req_fifo_empty,
  output _myaxi_read_req_fifo_almost_empty
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
  assign _myaxi_read_req_fifo_full = is_full;
  assign _myaxi_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _myaxi_read_req_fifo_empty = is_empty;
  assign _myaxi_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _myaxi_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_myaxi_read_req_fifo_enq && !is_full) begin
        mem[head] <= _myaxi_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_myaxi_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _myaxi_write_req_fifo
(
  input CLK,
  input RST,
  input _myaxi_write_req_fifo_enq,
  input [137-1:0] _myaxi_write_req_fifo_wdata,
  output _myaxi_write_req_fifo_full,
  output _myaxi_write_req_fifo_almost_full,
  input _myaxi_write_req_fifo_deq,
  output [137-1:0] _myaxi_write_req_fifo_rdata,
  output _myaxi_write_req_fifo_empty,
  output _myaxi_write_req_fifo_almost_empty
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
  assign _myaxi_write_req_fifo_full = is_full;
  assign _myaxi_write_req_fifo_almost_full = is_almost_full || is_full;
  assign _myaxi_write_req_fifo_empty = is_empty;
  assign _myaxi_write_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _myaxi_write_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_myaxi_write_req_fifo_enq && !is_full) begin
        mem[head] <= _myaxi_write_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_myaxi_write_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule


"""


expected_cpp = """
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>

#include "Vout.h"
#define Top Vout

#define MAX_SIM_TIME (0)
#define TIME_STEP (5)


#define TRACE


vluint64_t main_time = 0;

double sc_time_stamp(){
  return main_time;
}

int main(int argc, char** argv)
{
  Verilated::commandArgs(argc, argv);

  Top *top = new Top();

#ifdef TRACE
  Verilated::traceEverOn(true);
  VerilatedVcdC* tfp = new VerilatedVcdC;
  top->trace(tfp, 99);
  tfp->open("simulation_verilator.vcd");
#endif
  top->io_CLK = 0;
  top->io_RST = 0;

  // input initialization

  while(!Verilated::gotFinish()){
    if(main_time % 5 == 0){
      top->io_CLK = !top->io_CLK;
    }
    if(main_time == 100){
      top->io_RST = 1;
    }
    if(main_time == 100 * 2){
      top->io_RST = 0;
    }

    // update input

    top->eval();

#ifdef TRACE
    tfp->dump(main_time);
#endif

    if(MAX_SIM_TIME > 0 && main_time >= MAX_SIM_TIME){
      //std::cout << "# simulation time: " << main_time << std::endl;
      break;
    }

    main_time += TIME_STEP;
  }

#ifdef TRACE
  tfp->close();
#endif

  top->final();

  return 0;
}
"""


def test():
    veriloggen.reset()
    memimg_name = 'memimg_' + os.path.splitext(os.path.basename(__file__))[0] + '.out'
    test_module = simulation_verilator.mkTest(memimg_name=memimg_name)
    verilog = veriloggen.simulation.to_verilator_code(
        test_module, [test_module])
    cpp = veriloggen.simulation.to_verilator_cpp(test_module, 'out')

    assert(expected_verilog == verilog)
    assert(expected_cpp == cpp)
