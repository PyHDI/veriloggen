from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_multiwrite

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
  wire _tmp_0;
  assign _tmp_0 = 0;

  always @(*) begin
    myaxi_arready <= _tmp_0;
  end

  wire _tmp_1;
  assign _tmp_1 = 0;

  always @(*) begin
    myaxi_rvalid <= _tmp_1;
  end

  wire [32-1:0] _tmp_2;
  assign _tmp_2 = 0;

  always @(*) begin
    myaxi_rdata <= _tmp_2;
  end

  wire _tmp_3;
  assign _tmp_3 = 0;

  always @(*) begin
    myaxi_rlast <= _tmp_3;
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
    $dumpvars(0, uut, CLK, RST, myaxi_awid, myaxi_awaddr, myaxi_awlen, myaxi_awsize, myaxi_awburst, myaxi_awlock, myaxi_awcache, myaxi_awprot, myaxi_awqos, myaxi_awuser, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wuser, myaxi_wvalid, myaxi_wready, myaxi_bid, myaxi_bresp, myaxi_buser, myaxi_bvalid, myaxi_bready, myaxi_arid, myaxi_araddr, myaxi_arlen, myaxi_arsize, myaxi_arburst, myaxi_arlock, myaxi_arcache, myaxi_arprot, myaxi_arqos, myaxi_aruser, myaxi_arvalid, myaxi_arready, myaxi_rid, myaxi_rdata, myaxi_rresp, myaxi_rlast, myaxi_ruser, myaxi_rvalid, myaxi_rready, waddr, _awlen, _tmp_0, _tmp_1, _tmp_2, _tmp_3);
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
  assign myaxi_rready = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  reg [9-1:0] _tmp_1;
  reg _myaxi_cond_1_1;
  reg [32-1:0] wdata;
  reg _tmp_2;
  reg _myaxi_cond_2_1;
  reg _tmp_3;
  reg _myaxi_cond_3_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_arid <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      myaxi_awid <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_1 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_2 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_3 <= 0;
      _myaxi_cond_3_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_2 <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_3 <= 0;
      end 
      myaxi_arid <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      if((fsm == 0) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_0 == 0))) begin
        myaxi_awid <= 0;
        myaxi_awaddr <= 1024;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_0 <= 64;
      end 
      if((fsm == 0) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_0 == 0)) && 0) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if((fsm == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_1 == 0))) begin
        myaxi_awid <= 0;
        myaxi_awaddr <= 2048;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_1 <= 64;
      end 
      if((fsm == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_1 == 0)) && 0) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if((fsm == 2) && ((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_0 > 0))) begin
        myaxi_wdata <= wdata;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_0 <= _tmp_0 - 1;
      end 
      if((fsm == 2) && ((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_0 > 0)) && (_tmp_0 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_2 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_2 <= _tmp_2;
      end 
      if((fsm == 20) && ((_tmp_1 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_1 > 0))) begin
        myaxi_wdata <= wdata;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_1 <= _tmp_1 - 1;
      end 
      if((fsm == 20) && ((_tmp_1 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_1 > 0)) && (_tmp_1 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_3 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_3 <= _tmp_3;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  localparam fsm_16 = 16;
  localparam fsm_17 = 17;
  localparam fsm_18 = 18;
  localparam fsm_19 = 19;
  localparam fsm_20 = 20;
  localparam fsm_21 = 21;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      wdata <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if((_tmp_0 > 0) && (myaxi_wready || !myaxi_wvalid)) begin
            wdata <= wdata + 1;
          end 
          if(_tmp_2) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          wdata <= 1000;
          fsm <= fsm_4;
        end
        fsm_4: begin
          fsm <= fsm_5;
        end
        fsm_5: begin
          fsm <= fsm_6;
        end
        fsm_6: begin
          fsm <= fsm_7;
        end
        fsm_7: begin
          fsm <= fsm_8;
        end
        fsm_8: begin
          fsm <= fsm_9;
        end
        fsm_9: begin
          fsm <= fsm_10;
        end
        fsm_10: begin
          fsm <= fsm_11;
        end
        fsm_11: begin
          fsm <= fsm_12;
        end
        fsm_12: begin
          fsm <= fsm_13;
        end
        fsm_13: begin
          fsm <= fsm_14;
        end
        fsm_14: begin
          fsm <= fsm_15;
        end
        fsm_15: begin
          fsm <= fsm_16;
        end
        fsm_16: begin
          fsm <= fsm_17;
        end
        fsm_17: begin
          fsm <= fsm_18;
        end
        fsm_18: begin
          fsm <= fsm_19;
        end
        fsm_19: begin
          fsm <= fsm_20;
        end
        fsm_20: begin
          if((_tmp_1 > 0) && (myaxi_wready || !myaxi_wvalid)) begin
            wdata <= wdata + 1;
          end 
          if(_tmp_3) begin
            fsm <= fsm_21;
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
        if(fsm < 12) begin
          $display("sum=%d expected_sum=%d", sum, 2016);
        end else begin
          $display("sum=%d expected_sum=%d", sum, 66016);
        end
      end 
      if(fsm == 12) begin
        sum <= 0;
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        sum <= sum + myaxi_wdata;
      end 
      _seq_cond_0_1 <= myaxi_wvalid && myaxi_wready && myaxi_wlast;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_multiwrite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
