from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_ram_to_axi

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [1-1:0] myaxi_awid;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire [3-1:0] myaxi_awsize;
  wire [2-1:0] myaxi_awburst;
  wire [2-1:0] myaxi_awlock;
  wire [4-1:0] myaxi_awcache;
  wire [3-1:0] myaxi_awprot;
  wire [4-1:0] myaxi_awqos;
  wire [1-1:0] myaxi_awuser;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire [1-1:0] myaxi_wuser;
  wire myaxi_wvalid;
  reg myaxi_wready;
  reg [1-1:0] myaxi_bid;
  reg [2-1:0] myaxi_bresp;
  reg [1-1:0] myaxi_buser;
  reg myaxi_bvalid;
  wire myaxi_bready;
  wire [1-1:0] myaxi_arid;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire [3-1:0] myaxi_arsize;
  wire [2-1:0] myaxi_arburst;
  wire [2-1:0] myaxi_arlock;
  wire [4-1:0] myaxi_arcache;
  wire [3-1:0] myaxi_arprot;
  wire [4-1:0] myaxi_arqos;
  wire [1-1:0] myaxi_aruser;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [1-1:0] myaxi_rid;
  reg [32-1:0] myaxi_rdata;
  reg [2-1:0] myaxi_rresp;
  reg myaxi_rlast;
  reg [1-1:0] myaxi_ruser;
  reg myaxi_rvalid;
  wire myaxi_rready;
  reg [32-1:0] waddr;
  localparam waddr_init = 0;
  reg [32-1:0] _awlen;
  reg [32-1:0] raddr;
  localparam raddr_init = 0;
  reg [32-1:0] _arlen;
  reg [32-1:0] _d1_raddr;
  reg _raddr_cond_3_0_1;
  localparam raddr_1 = 1;
  localparam raddr_2 = 2;
  localparam raddr_3 = 3;
  localparam raddr_4 = 4;
  localparam raddr_5 = 5;
  localparam raddr_6 = 6;
  localparam raddr_7 = 7;
  localparam raddr_8 = 8;
  localparam raddr_9 = 9;
  localparam raddr_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      raddr <= raddr_init;
      _d1_raddr <= raddr_init;
      _arlen <= 0;
      _raddr_cond_3_0_1 <= 0;
    end else begin
      _d1_raddr <= raddr;
      case(_d1_raddr)
        raddr_3: begin
          if(_raddr_cond_3_0_1) begin
            myaxi_rvalid <= 0;
            myaxi_rlast <= 0;
          end 
        end
      endcase
      case(raddr)
        raddr_init: begin
          myaxi_arready <= 0;
          myaxi_rdata <= -1;
          myaxi_rvalid <= 0;
          myaxi_rlast <= 0;
          if(myaxi_arvalid) begin
            raddr <= raddr_1;
          end 
        end
        raddr_1: begin
          if(myaxi_arvalid) begin
            myaxi_arready <= 1;
            myaxi_rdata <= myaxi_araddr - 1;
          end 
          raddr <= raddr_2;
        end
        raddr_2: begin
          myaxi_arready <= 0;
          _arlen <= myaxi_arlen;
          raddr <= raddr_3;
        end
        raddr_3: begin
          if((myaxi_rready || !myaxi_rvalid) && !myaxi_rlast) begin
            myaxi_rdata <= myaxi_rdata + 1;
            myaxi_rvalid <= 1;
            myaxi_rlast <= 0;
            _arlen <= _arlen - 1;
          end 
          if((myaxi_rready || !myaxi_rvalid) && !myaxi_rlast && (_arlen == 0)) begin
            myaxi_rlast <= 1;
          end 
          _raddr_cond_3_0_1 <= 1;
          raddr <= raddr_4;
        end
        raddr_4: begin
          if(myaxi_rvalid && !myaxi_rready) begin
            myaxi_rvalid <= myaxi_rvalid;
            myaxi_rlast <= myaxi_rlast;
          end 
          if(myaxi_rvalid && myaxi_rready) begin
            raddr <= raddr_5;
          end 
        end
        raddr_5: begin
          raddr <= raddr_6;
        end
        raddr_6: begin
          raddr <= raddr_7;
        end
        raddr_7: begin
          raddr <= raddr_8;
        end
        raddr_8: begin
          if((_arlen + 1 & 255) != 0) begin
            raddr <= raddr_3;
          end 
          if((_arlen + 1 & 255) == 0) begin
            raddr <= raddr_9;
          end 
        end
        raddr_9: begin
          raddr <= raddr_10;
        end
        raddr_10: begin
          raddr <= raddr_init;
        end
      endcase
    end
  end


  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
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
    $dumpvars(0, uut, CLK, RST, myaxi_awid, myaxi_awaddr, myaxi_awlen, myaxi_awsize, myaxi_awburst, myaxi_awlock, myaxi_awcache, myaxi_awprot, myaxi_awqos, myaxi_awuser, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wuser, myaxi_wvalid, myaxi_wready, myaxi_bid, myaxi_bresp, myaxi_buser, myaxi_bvalid, myaxi_bready, myaxi_arid, myaxi_araddr, myaxi_arlen, myaxi_arsize, myaxi_arburst, myaxi_arlock, myaxi_arcache, myaxi_arprot, myaxi_arqos, myaxi_aruser, myaxi_arvalid, myaxi_arready, myaxi_rid, myaxi_rdata, myaxi_rresp, myaxi_rlast, myaxi_ruser, myaxi_rvalid, myaxi_rready, waddr, _awlen, raddr, _arlen, _d1_raddr, _raddr_cond_3_0_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    waddr = waddr_init;
    _awlen = 0;
    raddr = raddr_init;
    _arlen = 0;
    _d1_raddr = raddr_init;
    _raddr_cond_3_0_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end

  localparam waddr_1 = 1;
  localparam waddr_2 = 2;
  localparam waddr_3 = 3;
  localparam waddr_4 = 4;
  localparam waddr_5 = 5;
  localparam waddr_6 = 6;
  localparam waddr_7 = 7;
  localparam waddr_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      waddr <= waddr_init;
      _awlen <= 0;
    end else begin
      case(waddr)
        waddr_init: begin
          myaxi_awready <= 0;
          myaxi_wready <= 0;
          _awlen <= 0;
          if(myaxi_awvalid) begin
            waddr <= waddr_1;
          end 
        end
        waddr_1: begin
          if(myaxi_awvalid) begin
            myaxi_awready <= 1;
          end 
          waddr <= waddr_2;
        end
        waddr_2: begin
          myaxi_awready <= 0;
          _awlen <= myaxi_awlen;
          waddr <= waddr_3;
        end
        waddr_3: begin
          myaxi_wready <= 0;
          if(myaxi_wvalid) begin
            waddr <= waddr_4;
          end 
        end
        waddr_4: begin
          if(myaxi_wvalid) begin
            myaxi_wready <= 1;
          end 
          waddr <= waddr_5;
        end
        waddr_5: begin
          myaxi_wready <= 0;
          waddr <= waddr_6;
        end
        waddr_6: begin
          waddr <= waddr_7;
        end
        waddr_7: begin
          waddr <= waddr_8;
        end
        waddr_8: begin
          _awlen <= _awlen - 1;
          waddr <= waddr_3;
          if(_awlen == 0) begin
            waddr <= waddr_init;
          end 
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output reg [1-1:0] myaxi_awid,
  output reg [32-1:0] myaxi_awaddr,
  output reg [8-1:0] myaxi_awlen,
  output [3-1:0] myaxi_awsize,
  output [2-1:0] myaxi_awburst,
  output [2-1:0] myaxi_awlock,
  output [4-1:0] myaxi_awcache,
  output [3-1:0] myaxi_awprot,
  output [4-1:0] myaxi_awqos,
  output [1-1:0] myaxi_awuser,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output [1-1:0] myaxi_wuser,
  output reg myaxi_wvalid,
  input myaxi_wready,
  input [1-1:0] myaxi_bid,
  input [2-1:0] myaxi_bresp,
  input [1-1:0] myaxi_buser,
  input myaxi_bvalid,
  output myaxi_bready,
  output reg [1-1:0] myaxi_arid,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output [3-1:0] myaxi_arsize,
  output [2-1:0] myaxi_arburst,
  output [2-1:0] myaxi_arlock,
  output [4-1:0] myaxi_arcache,
  output [3-1:0] myaxi_arprot,
  output [4-1:0] myaxi_arqos,
  output [1-1:0] myaxi_aruser,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [1-1:0] myaxi_rid,
  input [32-1:0] myaxi_rdata,
  input [2-1:0] myaxi_rresp,
  input myaxi_rlast,
  input [1-1:0] myaxi_ruser,
  input myaxi_rvalid,
  output myaxi_rready
);

  assign myaxi_awsize = 2;
  assign myaxi_awburst = 1;
  assign myaxi_awlock = 0;
  assign myaxi_awcache = 3;
  assign myaxi_awprot = 0;
  assign myaxi_awqos = 0;
  assign myaxi_awuser = 1;
  assign myaxi_wuser = 1;
  assign myaxi_bready = 1;
  assign myaxi_arsize = 2;
  assign myaxi_arburst = 1;
  assign myaxi_arlock = 0;
  assign myaxi_arcache = 3;
  assign myaxi_arprot = 0;
  assign myaxi_arqos = 0;
  assign myaxi_aruser = 1;
  reg [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  wire _tmp_1;
  wire _tmp_2;
  assign myaxi_rready = _tmp_1 && _tmp_2;
  reg [8-1:0] _tmp_3;
  reg _tmp_4;
  wire signed [32-1:0] _dataflow_reduceadd_odata_4;
  wire _dataflow_reduceadd_ovalid_4;
  wire _dataflow_reduceadd_oready_4;
  assign _dataflow_reduceadd_oready_4 = (_tmp_3 > 0) && !_tmp_4;
  reg _myram_cond_0_1;
  reg [9-1:0] _tmp_5;
  reg _myaxi_cond_1_1;
  reg _tmp_6;
  reg _tmp_7;
  wire _tmp_8;
  wire _tmp_9;
  assign _tmp_9 = 1;
  localparam _tmp_10 = 1;
  wire [_tmp_10-1:0] _tmp_11;
  assign _tmp_11 = (_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7);
  reg [_tmp_10-1:0] __tmp_11_1;
  wire signed [32-1:0] _tmp_12;
  reg signed [32-1:0] __tmp_12_1;
  assign _tmp_12 = (__tmp_11_1)? myram_0_rdata : __tmp_12_1;
  reg _tmp_13;
  reg _tmp_14;
  reg _tmp_15;
  reg _tmp_16;
  reg [8-1:0] _tmp_17;
  reg _tmp_18;
  wire signed [32-1:0] _dataflow__variable_odata_5;
  wire _dataflow__variable_ovalid_5;
  wire _dataflow__variable_oready_5;
  assign _dataflow__variable_oready_5 = (_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid);
  reg _myaxi_cond_2_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_arid <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_awid <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_5 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_18 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_18 <= 0;
      end 
      if((fsm == 0) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_0 == 0))) begin
        myaxi_arid <= 0;
        myaxi_araddr <= 1024;
        myaxi_arlen <= 63;
        myaxi_arvalid <= 1;
        _tmp_0 <= 64;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_0 > 0)) begin
        _tmp_0 <= _tmp_0 - 1;
      end 
      if((fsm == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_5 == 0))) begin
        myaxi_awid <= 0;
        myaxi_awaddr <= 1024;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_5 <= 64;
      end 
      if((fsm == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_5 == 0)) && 0) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_dataflow__variable_ovalid_5 && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid)) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_5 > 0))) begin
        myaxi_wdata <= _dataflow__variable_odata_5;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_5 <= _tmp_5 - 1;
      end 
      if(_dataflow__variable_ovalid_5 && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid)) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_5 > 0)) && (_tmp_5 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_18 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_18 <= _tmp_18;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      _tmp_3 <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _tmp_4 <= 0;
      _myram_cond_0_1 <= 0;
      __tmp_11_1 <= 0;
      __tmp_12_1 <= 0;
      _tmp_16 <= 0;
      _tmp_6 <= 0;
      _tmp_7 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_13 <= 0;
      _tmp_17 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
        _tmp_4 <= 0;
      end 
      if((fsm == 1) && (_tmp_3 == 0)) begin
        myram_0_addr <= -1;
        _tmp_3 <= 64;
      end 
      if(_dataflow_reduceadd_ovalid_4 && ((_tmp_3 > 0) && !_tmp_4) && (_tmp_3 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _dataflow_reduceadd_odata_4;
        myram_0_wenable <= 1;
        _tmp_3 <= _tmp_3 - 1;
      end 
      if(_dataflow_reduceadd_ovalid_4 && ((_tmp_3 > 0) && !_tmp_4) && (_tmp_3 == 1)) begin
        _tmp_4 <= 1;
      end 
      _myram_cond_0_1 <= 1;
      __tmp_11_1 <= _tmp_11;
      __tmp_12_1 <= _tmp_12;
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && _tmp_14) begin
        _tmp_16 <= 0;
        _tmp_6 <= 0;
        _tmp_7 <= 0;
        _tmp_14 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && _tmp_13) begin
        _tmp_6 <= 1;
        _tmp_7 <= 1;
        _tmp_16 <= _tmp_15;
        _tmp_15 <= 0;
        _tmp_13 <= 0;
        _tmp_14 <= 1;
      end 
      if((fsm == 4) && (_tmp_17 == 0) && !_tmp_15 && !_tmp_16) begin
        myram_0_addr <= 0;
        _tmp_17 <= 63;
        _tmp_13 <= 1;
        _tmp_15 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_17 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        _tmp_17 <= _tmp_17 - 1;
        _tmp_13 <= 1;
        _tmp_15 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_17 == 1)) begin
        _tmp_15 <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_5 = _tmp_12;
  assign _dataflow__variable_ovalid_5 = _tmp_6;
  assign _tmp_8 = 1 && _dataflow__variable_oready_5;
  reg [1-1:0] _dataflow__prev_data_2;
  reg signed [32-1:0] _dataflow_reduceadd_data_4;
  reg _dataflow_reduceadd_valid_4;
  wire _dataflow_reduceadd_ready_4;
  assign _tmp_1 = 1 && ((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (myaxi_rvalid && myaxi_rvalid));
  assign _tmp_2 = 1 && ((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (myaxi_rvalid && myaxi_rvalid));
  assign _dataflow_reduceadd_odata_4 = _dataflow_reduceadd_data_4;
  assign _dataflow_reduceadd_ovalid_4 = _dataflow_reduceadd_valid_4;
  assign _dataflow_reduceadd_ready_4 = _dataflow_reduceadd_oready_4;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow__prev_data_2 <= 0;
      _dataflow_reduceadd_data_4 <= 1'sd0;
      _dataflow_reduceadd_valid_4 <= 0;
    end else begin
      if(myaxi_rvalid && _tmp_2) begin
        _dataflow__prev_data_2 <= myaxi_rlast;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (_tmp_1 && _tmp_2) && (myaxi_rvalid && myaxi_rvalid)) begin
        _dataflow_reduceadd_data_4 <= _dataflow_reduceadd_data_4 + myaxi_rdata;
      end 
      if(_dataflow_reduceadd_valid_4 && _dataflow_reduceadd_ready_4) begin
        _dataflow_reduceadd_valid_4 <= 0;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (_tmp_1 && _tmp_2)) begin
        _dataflow_reduceadd_valid_4 <= myaxi_rvalid && myaxi_rvalid;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (_tmp_1 && _tmp_2) && (myaxi_rvalid && myaxi_rvalid) && _dataflow__prev_data_2) begin
        _dataflow_reduceadd_data_4 <= 1'sd0 + myaxi_rdata;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
    end else begin
      case(fsm)
        fsm_init: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(_tmp_4) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_tmp_18 && myaxi_wvalid && myaxi_wready) begin
            fsm <= fsm_6;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", sum, 2173600);
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        sum <= sum + myaxi_wdata;
      end 
      _seq_cond_0_1 <= myaxi_wvalid && myaxi_wready && myaxi_wlast;
    end
  end


endmodule



module myram
(
  input CLK,
  input [10-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_ram_to_axi.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
