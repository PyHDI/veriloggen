from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_slave_write

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] sum;
  reg [1-1:0] myaxi_awid;
  reg [32-1:0] myaxi_awaddr;
  reg [8-1:0] myaxi_awlen;
  reg [3-1:0] myaxi_awsize;
  reg [2-1:0] myaxi_awburst;
  reg [2-1:0] myaxi_awlock;
  reg [4-1:0] myaxi_awcache;
  reg [3-1:0] myaxi_awprot;
  reg [4-1:0] myaxi_awqos;
  reg [1-1:0] myaxi_awuser;
  reg myaxi_awvalid;
  wire myaxi_awready;
  reg [32-1:0] myaxi_wdata;
  reg [4-1:0] myaxi_wstrb;
  reg myaxi_wlast;
  reg [1-1:0] myaxi_wuser;
  reg myaxi_wvalid;
  wire myaxi_wready;
  wire [1-1:0] myaxi_bid;
  wire [2-1:0] myaxi_bresp;
  wire [1-1:0] myaxi_buser;
  wire myaxi_bvalid;
  reg myaxi_bready;
  reg [1-1:0] myaxi_arid;
  reg [32-1:0] myaxi_araddr;
  reg [8-1:0] myaxi_arlen;
  reg [3-1:0] myaxi_arsize;
  reg [2-1:0] myaxi_arburst;
  reg [2-1:0] myaxi_arlock;
  reg [4-1:0] myaxi_arcache;
  reg [3-1:0] myaxi_arprot;
  reg [4-1:0] myaxi_arqos;
  reg [1-1:0] myaxi_aruser;
  reg myaxi_arvalid;
  wire myaxi_arready;
  wire [1-1:0] myaxi_rid;
  wire [32-1:0] myaxi_rdata;
  wire [2-1:0] myaxi_rresp;
  wire myaxi_rlast;
  wire [1-1:0] myaxi_ruser;
  wire myaxi_rvalid;
  reg myaxi_rready;
  reg [1-1:0] _axi_awid;
  reg [32-1:0] _axi_awaddr;
  reg [8-1:0] _axi_awlen;
  wire [3-1:0] _axi_awsize;
  wire [2-1:0] _axi_awburst;
  wire [2-1:0] _axi_awlock;
  wire [4-1:0] _axi_awcache;
  wire [3-1:0] _axi_awprot;
  wire [4-1:0] _axi_awqos;
  wire [1-1:0] _axi_awuser;
  reg _axi_awvalid;
  wire _axi_awready;
  reg [32-1:0] _axi_wdata;
  reg [4-1:0] _axi_wstrb;
  reg _axi_wlast;
  wire [1-1:0] _axi_wuser;
  reg _axi_wvalid;
  wire _axi_wready;
  wire [1-1:0] _axi_bid;
  wire [2-1:0] _axi_bresp;
  wire [1-1:0] _axi_buser;
  wire _axi_bvalid;
  wire _axi_bready;
  reg [1-1:0] _axi_arid;
  reg [32-1:0] _axi_araddr;
  reg [8-1:0] _axi_arlen;
  wire [3-1:0] _axi_arsize;
  wire [2-1:0] _axi_arburst;
  wire [2-1:0] _axi_arlock;
  wire [4-1:0] _axi_arcache;
  wire [3-1:0] _axi_arprot;
  wire [4-1:0] _axi_arqos;
  wire [1-1:0] _axi_aruser;
  reg _axi_arvalid;
  wire _axi_arready;
  wire [1-1:0] _axi_rid;
  wire [32-1:0] _axi_rdata;
  wire [2-1:0] _axi_rresp;
  wire _axi_rlast;
  wire [1-1:0] _axi_ruser;
  wire _axi_rvalid;
  wire _axi_rready;
  assign _axi_awsize = 2;
  assign _axi_awburst = 1;
  assign _axi_awlock = 0;
  assign _axi_awcache = 3;
  assign _axi_awprot = 0;
  assign _axi_awqos = 0;
  assign _axi_awuser = 1;
  assign _axi_wuser = 1;
  assign _axi_bready = 1;
  assign _axi_arsize = 2;
  assign _axi_arburst = 1;
  assign _axi_arlock = 0;
  assign _axi_arcache = 3;
  assign _axi_arprot = 0;
  assign _axi_arqos = 0;
  assign _axi_aruser = 1;
  assign _axi_rready = 0;
  wire [1-1:0] _tmp_0;
  assign _tmp_0 = _axi_awid;

  always @(*) begin
    myaxi_awid = _tmp_0;
  end

  wire [32-1:0] _tmp_1;
  assign _tmp_1 = _axi_awaddr;

  always @(*) begin
    myaxi_awaddr = _tmp_1;
  end

  wire [8-1:0] _tmp_2;
  assign _tmp_2 = _axi_awlen;

  always @(*) begin
    myaxi_awlen = _tmp_2;
  end

  wire [3-1:0] _tmp_3;
  assign _tmp_3 = _axi_awsize;

  always @(*) begin
    myaxi_awsize = _tmp_3;
  end

  wire [2-1:0] _tmp_4;
  assign _tmp_4 = _axi_awburst;

  always @(*) begin
    myaxi_awburst = _tmp_4;
  end

  wire [2-1:0] _tmp_5;
  assign _tmp_5 = _axi_awlock;

  always @(*) begin
    myaxi_awlock = _tmp_5;
  end

  wire [4-1:0] _tmp_6;
  assign _tmp_6 = _axi_awcache;

  always @(*) begin
    myaxi_awcache = _tmp_6;
  end

  wire [3-1:0] _tmp_7;
  assign _tmp_7 = _axi_awprot;

  always @(*) begin
    myaxi_awprot = _tmp_7;
  end

  wire [4-1:0] _tmp_8;
  assign _tmp_8 = _axi_awqos;

  always @(*) begin
    myaxi_awqos = _tmp_8;
  end

  wire [1-1:0] _tmp_9;
  assign _tmp_9 = _axi_awuser;

  always @(*) begin
    myaxi_awuser = _tmp_9;
  end

  wire _tmp_10;
  assign _tmp_10 = _axi_awvalid;

  always @(*) begin
    myaxi_awvalid = _tmp_10;
  end

  assign _axi_awready = myaxi_awready;
  wire [32-1:0] _tmp_11;
  assign _tmp_11 = _axi_wdata;

  always @(*) begin
    myaxi_wdata = _tmp_11;
  end

  wire [4-1:0] _tmp_12;
  assign _tmp_12 = _axi_wstrb;

  always @(*) begin
    myaxi_wstrb = _tmp_12;
  end

  wire _tmp_13;
  assign _tmp_13 = _axi_wlast;

  always @(*) begin
    myaxi_wlast = _tmp_13;
  end

  wire [1-1:0] _tmp_14;
  assign _tmp_14 = _axi_wuser;

  always @(*) begin
    myaxi_wuser = _tmp_14;
  end

  wire _tmp_15;
  assign _tmp_15 = _axi_wvalid;

  always @(*) begin
    myaxi_wvalid = _tmp_15;
  end

  assign _axi_wready = myaxi_wready;
  assign _axi_bid = myaxi_bid;
  assign _axi_bresp = myaxi_bresp;
  assign _axi_buser = myaxi_buser;
  assign _axi_bvalid = myaxi_bvalid;
  wire _tmp_16;
  assign _tmp_16 = _axi_bready;

  always @(*) begin
    myaxi_bready = _tmp_16;
  end

  wire [1-1:0] _tmp_17;
  assign _tmp_17 = _axi_arid;

  always @(*) begin
    myaxi_arid = _tmp_17;
  end

  wire [32-1:0] _tmp_18;
  assign _tmp_18 = _axi_araddr;

  always @(*) begin
    myaxi_araddr = _tmp_18;
  end

  wire [8-1:0] _tmp_19;
  assign _tmp_19 = _axi_arlen;

  always @(*) begin
    myaxi_arlen = _tmp_19;
  end

  wire [3-1:0] _tmp_20;
  assign _tmp_20 = _axi_arsize;

  always @(*) begin
    myaxi_arsize = _tmp_20;
  end

  wire [2-1:0] _tmp_21;
  assign _tmp_21 = _axi_arburst;

  always @(*) begin
    myaxi_arburst = _tmp_21;
  end

  wire [2-1:0] _tmp_22;
  assign _tmp_22 = _axi_arlock;

  always @(*) begin
    myaxi_arlock = _tmp_22;
  end

  wire [4-1:0] _tmp_23;
  assign _tmp_23 = _axi_arcache;

  always @(*) begin
    myaxi_arcache = _tmp_23;
  end

  wire [3-1:0] _tmp_24;
  assign _tmp_24 = _axi_arprot;

  always @(*) begin
    myaxi_arprot = _tmp_24;
  end

  wire [4-1:0] _tmp_25;
  assign _tmp_25 = _axi_arqos;

  always @(*) begin
    myaxi_arqos = _tmp_25;
  end

  wire [1-1:0] _tmp_26;
  assign _tmp_26 = _axi_aruser;

  always @(*) begin
    myaxi_aruser = _tmp_26;
  end

  wire _tmp_27;
  assign _tmp_27 = _axi_arvalid;

  always @(*) begin
    myaxi_arvalid = _tmp_27;
  end

  assign _axi_arready = myaxi_arready;
  assign _axi_rid = myaxi_rid;
  assign _axi_rdata = myaxi_rdata;
  assign _axi_rresp = myaxi_rresp;
  assign _axi_rlast = myaxi_rlast;
  assign _axi_ruser = myaxi_ruser;
  assign _axi_rvalid = myaxi_rvalid;
  wire _tmp_28;
  assign _tmp_28 = _axi_rready;

  always @(*) begin
    myaxi_rready = _tmp_28;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_29;
  reg __axi_cond_0_1;
  reg [32-1:0] wdata;
  reg _tmp_30;
  reg __axi_cond_1_1;
  reg [9-1:0] _tmp_31;
  reg __axi_cond_2_1;
  reg _tmp_32;
  reg __axi_cond_3_1;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .sum(sum),
    .myaxi_awid(myaxi_awid),
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
    .myaxi_wuser(myaxi_wuser),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_bid(myaxi_bid),
    .myaxi_bresp(myaxi_bresp),
    .myaxi_buser(myaxi_buser),
    .myaxi_bvalid(myaxi_bvalid),
    .myaxi_bready(myaxi_bready),
    .myaxi_arid(myaxi_arid),
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
    .myaxi_rid(myaxi_rid),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rresp(myaxi_rresp),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_ruser(myaxi_ruser),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, sum, myaxi_awid, myaxi_awaddr, myaxi_awlen, myaxi_awsize, myaxi_awburst, myaxi_awlock, myaxi_awcache, myaxi_awprot, myaxi_awqos, myaxi_awuser, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wuser, myaxi_wvalid, myaxi_wready, myaxi_bid, myaxi_bresp, myaxi_buser, myaxi_bvalid, myaxi_bready, myaxi_arid, myaxi_araddr, myaxi_arlen, myaxi_arsize, myaxi_arburst, myaxi_arlock, myaxi_arcache, myaxi_arprot, myaxi_arqos, myaxi_aruser, myaxi_arvalid, myaxi_arready, myaxi_rid, myaxi_rdata, myaxi_rresp, myaxi_rlast, myaxi_ruser, myaxi_rvalid, myaxi_rready, _axi_awid, _axi_awaddr, _axi_awlen, _axi_awsize, _axi_awburst, _axi_awlock, _axi_awcache, _axi_awprot, _axi_awqos, _axi_awuser, _axi_awvalid, _axi_awready, _axi_wdata, _axi_wstrb, _axi_wlast, _axi_wuser, _axi_wvalid, _axi_wready, _axi_bid, _axi_bresp, _axi_buser, _axi_bvalid, _axi_bready, _axi_arid, _axi_araddr, _axi_arlen, _axi_arsize, _axi_arburst, _axi_arlock, _axi_arcache, _axi_arprot, _axi_arqos, _axi_aruser, _axi_arvalid, _axi_arready, _axi_rid, _axi_rdata, _axi_rresp, _axi_rlast, _axi_ruser, _axi_rvalid, _axi_rready, _tmp_0, _tmp_1, _tmp_2, _tmp_3, _tmp_4, _tmp_5, _tmp_6, _tmp_7, _tmp_8, _tmp_9, _tmp_10, _tmp_11, _tmp_12, _tmp_13, _tmp_14, _tmp_15, _tmp_16, _tmp_17, _tmp_18, _tmp_19, _tmp_20, _tmp_21, _tmp_22, _tmp_23, _tmp_24, _tmp_25, _tmp_26, _tmp_27, _tmp_28, fsm, _tmp_29, __axi_cond_0_1, wdata, _tmp_30, __axi_cond_1_1, _tmp_31, __axi_cond_2_1, _tmp_32, __axi_cond_3_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    _axi_awid = 0;
    _axi_awaddr = 0;
    _axi_awlen = 0;
    _axi_awvalid = 0;
    _axi_wdata = 0;
    _axi_wstrb = 0;
    _axi_wlast = 0;
    _axi_wvalid = 0;
    _axi_arid = 0;
    _axi_araddr = 0;
    _axi_arlen = 0;
    _axi_arvalid = 0;
    fsm = fsm_init;
    _tmp_29 = 0;
    __axi_cond_0_1 = 0;
    wdata = 0;
    _tmp_30 = 0;
    __axi_cond_1_1 = 0;
    _tmp_31 = 0;
    __axi_cond_2_1 = 0;
    _tmp_32 = 0;
    __axi_cond_3_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      _axi_arid <= 0;
      _axi_araddr <= 0;
      _axi_arlen <= 0;
      _axi_arvalid <= 0;
      _axi_awid <= 0;
      _axi_awaddr <= 0;
      _axi_awlen <= 0;
      _axi_awvalid <= 0;
      _tmp_29 <= 0;
      __axi_cond_0_1 <= 0;
      _axi_wdata <= 0;
      _axi_wvalid <= 0;
      _axi_wlast <= 0;
      _axi_wstrb <= 0;
      _tmp_30 <= 0;
      __axi_cond_1_1 <= 0;
      _tmp_31 <= 0;
      __axi_cond_2_1 <= 0;
      _tmp_32 <= 0;
      __axi_cond_3_1 <= 0;
    end else begin
      if(__axi_cond_0_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_1_1) begin
        _axi_wvalid <= 0;
        _axi_wlast <= 0;
        _tmp_30 <= 0;
      end 
      if(__axi_cond_2_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_3_1) begin
        _axi_wvalid <= 0;
        _axi_wlast <= 0;
        _tmp_32 <= 0;
      end 
      _axi_arid <= 0;
      _axi_araddr <= 0;
      _axi_arlen <= 0;
      _axi_arvalid <= 0;
      if((fsm == 0) && ((_axi_awready || !_axi_awvalid) && (_tmp_29 == 0))) begin
        _axi_awid <= 0;
        _axi_awaddr <= 1024;
        _axi_awlen <= 63;
        _axi_awvalid <= 1;
        _tmp_29 <= 64;
      end 
      if((fsm == 0) && ((_axi_awready || !_axi_awvalid) && (_tmp_29 == 0)) && 0) begin
        _axi_awvalid <= 0;
      end 
      __axi_cond_0_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 1) && ((_tmp_29 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_29 > 0))) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wlast <= 0;
        _axi_wstrb <= { 4{ 1'd1 } };
        _tmp_29 <= _tmp_29 - 1;
      end 
      if((fsm == 1) && ((_tmp_29 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_29 > 0)) && (_tmp_29 == 1)) begin
        _axi_wlast <= 1;
        _tmp_30 <= 1;
      end 
      __axi_cond_1_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
        _axi_wlast <= _axi_wlast;
        _tmp_30 <= _tmp_30;
      end 
      if((fsm == 2) && ((_axi_awready || !_axi_awvalid) && (_tmp_31 == 0))) begin
        _axi_awid <= 0;
        _axi_awaddr <= 1024;
        _axi_awlen <= 127;
        _axi_awvalid <= 1;
        _tmp_31 <= 128;
      end 
      if((fsm == 2) && ((_axi_awready || !_axi_awvalid) && (_tmp_31 == 0)) && 0) begin
        _axi_awvalid <= 0;
      end 
      __axi_cond_2_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 3) && ((_tmp_31 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_31 > 0))) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wlast <= 0;
        _axi_wstrb <= { 4{ 1'd1 } };
        _tmp_31 <= _tmp_31 - 1;
      end 
      if((fsm == 3) && ((_tmp_31 > 0) && (_axi_wready || !_axi_wvalid) && (_tmp_31 > 0)) && (_tmp_31 == 1)) begin
        _axi_wlast <= 1;
        _tmp_32 <= 1;
      end 
      __axi_cond_3_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
        _axi_wlast <= _axi_wlast;
        _tmp_32 <= _tmp_32;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      wdata <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if((_tmp_29 > 0) && (_axi_wready || !_axi_wvalid)) begin
            wdata <= wdata + 1;
          end 
          if(_tmp_30) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if((_tmp_31 > 0) && (_axi_wready || !_axi_wvalid)) begin
            wdata <= wdata + 1;
          end 
          if(_tmp_32) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          $display("sum=%d expected_sum=%d", sum, 18336);
          fsm <= fsm_5;
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output reg [32-1:0] sum,
  input [1-1:0] myaxi_awid,
  input [32-1:0] myaxi_awaddr,
  input [8-1:0] myaxi_awlen,
  input [3-1:0] myaxi_awsize,
  input [2-1:0] myaxi_awburst,
  input [2-1:0] myaxi_awlock,
  input [4-1:0] myaxi_awcache,
  input [3-1:0] myaxi_awprot,
  input [4-1:0] myaxi_awqos,
  input [1-1:0] myaxi_awuser,
  input myaxi_awvalid,
  output myaxi_awready,
  input [32-1:0] myaxi_wdata,
  input [4-1:0] myaxi_wstrb,
  input myaxi_wlast,
  input [1-1:0] myaxi_wuser,
  input myaxi_wvalid,
  output myaxi_wready,
  output reg [1-1:0] myaxi_bid,
  output [2-1:0] myaxi_bresp,
  output [1-1:0] myaxi_buser,
  output reg myaxi_bvalid,
  input myaxi_bready,
  input [1-1:0] myaxi_arid,
  input [32-1:0] myaxi_araddr,
  input [8-1:0] myaxi_arlen,
  input [3-1:0] myaxi_arsize,
  input [2-1:0] myaxi_arburst,
  input [2-1:0] myaxi_arlock,
  input [4-1:0] myaxi_arcache,
  input [3-1:0] myaxi_arprot,
  input [4-1:0] myaxi_arqos,
  input [1-1:0] myaxi_aruser,
  input myaxi_arvalid,
  output myaxi_arready,
  output reg [1-1:0] myaxi_rid,
  output reg [32-1:0] myaxi_rdata,
  output [2-1:0] myaxi_rresp,
  output reg myaxi_rlast,
  output [1-1:0] myaxi_ruser,
  output reg myaxi_rvalid,
  input myaxi_rready
);

  assign myaxi_bresp = 0;
  assign myaxi_buser = 1;
  assign myaxi_rresp = 0;
  assign myaxi_ruser = 1;
  assign myaxi_arready = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg _tmp_2;
  reg _tmp_3;
  assign myaxi_awready = (fsm == 0) && !_tmp_2 && !myaxi_bvalid && _tmp_3;
  assign myaxi_wready = fsm == 1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_bid <= 0;
      myaxi_rid <= 0;
      myaxi_bvalid <= 0;
      myaxi_rvalid <= 0;
      myaxi_rlast <= 0;
      _tmp_3 <= 0;
      _tmp_1 <= 0;
      _tmp_0 <= 0;
      _tmp_2 <= 0;
    end else begin
      if(myaxi_awvalid && myaxi_awready && !myaxi_bvalid) begin
        myaxi_bid <= myaxi_awid;
      end 
      if(myaxi_arvalid && myaxi_arready) begin
        myaxi_rid <= myaxi_arid;
      end 
      if(myaxi_bvalid && myaxi_bready) begin
        myaxi_bvalid <= 0;
      end 
      if(myaxi_wvalid && myaxi_wready && myaxi_wlast) begin
        myaxi_bvalid <= 1;
      end 
      myaxi_rvalid <= 0;
      myaxi_rlast <= 0;
      _tmp_3 <= myaxi_awvalid;
      if(myaxi_awready && myaxi_awvalid && !myaxi_bvalid) begin
        _tmp_1 <= myaxi_awaddr;
        _tmp_0 <= myaxi_awlen + 1;
      end 
      _tmp_2 <= myaxi_awready && myaxi_awvalid && !myaxi_bvalid;
      if(myaxi_wready && myaxi_wvalid && (_tmp_0 > 0)) begin
        _tmp_0 <= _tmp_0 - 1;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_tmp_2) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(myaxi_wready && myaxi_wvalid) begin
            sum <= sum + myaxi_wdata;
          end 
          if(myaxi_wready && myaxi_wvalid && myaxi_wlast) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_slave_write.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
