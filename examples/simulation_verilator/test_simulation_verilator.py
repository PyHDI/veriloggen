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
  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("memimg_test_simulation_verilator.out", _memory_mem);
  end

  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_count;
  reg [33-1:0] _sub_sleep_count;
  reg [32-1:0] _d1__memory_fsm;
  reg __memory_fsm_cond_100_0_1;
  reg __memory_fsm_cond_200_1_1;
  reg __memory_fsm_cond_211_2_1;
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
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    myaxi_awready = _tmp_0;
  end

  assign memory_wdata = myaxi_wdata;
  assign memory_wstrb = myaxi_wstrb;
  assign memory_wlast = myaxi_wlast;
  assign memory_wvalid = myaxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    myaxi_wready = _tmp_1;
  end

  wire [2-1:0] _tmp_2;
  assign _tmp_2 = memory_bresp;

  always @(*) begin
    myaxi_bresp = _tmp_2;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_bvalid;

  always @(*) begin
    myaxi_bvalid = _tmp_3;
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
  wire _tmp_4;
  assign _tmp_4 = memory_arready;

  always @(*) begin
    myaxi_arready = _tmp_4;
  end

  wire [32-1:0] _tmp_5;
  assign _tmp_5 = memory_rdata;

  always @(*) begin
    myaxi_rdata = _tmp_5;
  end

  wire [2-1:0] _tmp_6;
  assign _tmp_6 = memory_rresp;

  always @(*) begin
    myaxi_rresp = _tmp_6;
  end

  wire _tmp_7;
  assign _tmp_7 = memory_rlast;

  always @(*) begin
    myaxi_rlast = _tmp_7;
  end

  wire _tmp_8;
  assign _tmp_8 = memory_rvalid;

  always @(*) begin
    myaxi_rvalid = _tmp_8;
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
    memory_wready = 0;
    memory_bvalid = 0;
    memory_arready = 0;
    memory_rdata = 0;
    memory_rlast = 0;
    memory_rvalid = 0;
    _memory_fsm = _memory_fsm_init;
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_count = 0;
    _sub_sleep_count = 0;
    _d1__memory_fsm = _memory_fsm_init;
    __memory_fsm_cond_100_0_1 = 0;
    __memory_fsm_cond_200_1_1 = 0;
    __memory_fsm_cond_211_2_1 = 0;
    $write("");
    RST = 1;
    $write("");
    RST = 0;
    $write("");
    $write("");
  end

  wire _tmp_9;
  assign _tmp_9 = io_CLK;

  always @(*) begin
    CLK = _tmp_9;
  end

  wire _tmp_10;
  assign _tmp_10 = io_RST;

  always @(*) begin
    RST = _tmp_10;
  end

  localparam _memory_fsm_200 = 200;
  localparam _memory_fsm_201 = 201;
  localparam _memory_fsm_202 = 202;
  localparam _memory_fsm_203 = 203;
  localparam _memory_fsm_204 = 204;
  localparam _memory_fsm_205 = 205;
  localparam _memory_fsm_206 = 206;
  localparam _memory_fsm_207 = 207;
  localparam _memory_fsm_208 = 208;
  localparam _memory_fsm_209 = 209;
  localparam _memory_fsm_210 = 210;
  localparam _memory_fsm_211 = 211;
  localparam _memory_fsm_100 = 100;
  localparam _memory_fsm_101 = 101;
  localparam _memory_fsm_102 = 102;
  localparam _memory_fsm_103 = 103;
  localparam _memory_fsm_104 = 104;
  localparam _memory_fsm_105 = 105;
  localparam _memory_fsm_106 = 106;
  localparam _memory_fsm_107 = 107;
  localparam _memory_fsm_108 = 108;
  localparam _memory_fsm_109 = 109;
  localparam _memory_fsm_110 = 110;
  localparam _memory_fsm_111 = 111;
  localparam _memory_fsm_112 = 112;

  always @(posedge CLK) begin
    if(RST) begin
      _memory_fsm <= _memory_fsm_init;
      _d1__memory_fsm <= _memory_fsm_init;
      memory_awready <= 0;
      _write_addr <= 0;
      _write_count <= 0;
      __memory_fsm_cond_100_0_1 <= 0;
      memory_wready <= 0;
      memory_arready <= 0;
      _read_addr <= 0;
      _read_count <= 0;
      __memory_fsm_cond_200_1_1 <= 0;
      memory_rdata[7:0] <= (0 >> 0) & { 8{ 1'd1 } };
      memory_rdata[15:8] <= (0 >> 8) & { 8{ 1'd1 } };
      memory_rdata[23:16] <= (0 >> 16) & { 8{ 1'd1 } };
      memory_rdata[31:24] <= (0 >> 24) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_fsm_cond_211_2_1 <= 0;
      memory_rdata <= 0;
      memory_bvalid <= 0;
      _sub_sleep_count <= 0;
      _sleep_count <= 0;
    end else begin
      if(memory_bvalid && memory_bready) begin
        memory_bvalid <= 0;
      end 
      if(memory_wvalid && memory_wready && memory_wlast) begin
        memory_bvalid <= 1;
      end 
      if(_sleep_count == 3) begin
        _sub_sleep_count <= _sub_sleep_count + 1;
      end 
      if((_sleep_count == 3) && (_sub_sleep_count == 3)) begin
        _sub_sleep_count <= 0;
      end 
      if(_sleep_count < 3) begin
        _sleep_count <= _sleep_count + 1;
      end 
      if((_sub_sleep_count == 3) && (_sleep_count == 3)) begin
        _sleep_count <= 0;
      end 
      _d1__memory_fsm <= _memory_fsm;
      case(_d1__memory_fsm)
        _memory_fsm_100: begin
          if(__memory_fsm_cond_100_0_1) begin
            memory_awready <= 0;
          end 
        end
        _memory_fsm_200: begin
          if(__memory_fsm_cond_200_1_1) begin
            memory_arready <= 0;
          end 
        end
        _memory_fsm_211: begin
          if(__memory_fsm_cond_211_2_1) begin
            memory_rvalid <= 0;
            memory_rlast <= 0;
          end 
        end
      endcase
      case(_memory_fsm)
        _memory_fsm_init: begin
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_100;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_200;
          end 
        end
        _memory_fsm_100: begin
          if(memory_awvalid && !memory_bvalid) begin
            memory_awready <= 1;
            _write_addr <= memory_awaddr;
            _write_count <= memory_awlen + 1;
          end 
          __memory_fsm_cond_100_0_1 <= 1;
          if(!memory_awvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_101;
          end 
        end
        _memory_fsm_101: begin
          _memory_fsm <= _memory_fsm_102;
        end
        _memory_fsm_102: begin
          _memory_fsm <= _memory_fsm_103;
        end
        _memory_fsm_103: begin
          _memory_fsm <= _memory_fsm_104;
        end
        _memory_fsm_104: begin
          _memory_fsm <= _memory_fsm_105;
        end
        _memory_fsm_105: begin
          _memory_fsm <= _memory_fsm_106;
        end
        _memory_fsm_106: begin
          _memory_fsm <= _memory_fsm_107;
        end
        _memory_fsm_107: begin
          _memory_fsm <= _memory_fsm_108;
        end
        _memory_fsm_108: begin
          _memory_fsm <= _memory_fsm_109;
        end
        _memory_fsm_109: begin
          _memory_fsm <= _memory_fsm_110;
        end
        _memory_fsm_110: begin
          _memory_fsm <= _memory_fsm_111;
        end
        _memory_fsm_111: begin
          memory_wready <= 1;
          _memory_fsm <= _memory_fsm_112;
        end
        _memory_fsm_112: begin
          if(memory_wvalid && memory_wstrb[0]) begin
            _memory_mem[_write_addr + 0] <= memory_wdata[7:0];
          end 
          if(memory_wvalid && memory_wstrb[1]) begin
            _memory_mem[_write_addr + 1] <= memory_wdata[15:8];
          end 
          if(memory_wvalid && memory_wstrb[2]) begin
            _memory_mem[_write_addr + 2] <= memory_wdata[23:16];
          end 
          if(memory_wvalid && memory_wstrb[3]) begin
            _memory_mem[_write_addr + 3] <= memory_wdata[31:24];
          end 
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 4;
            _write_count <= _write_count - 1;
          end 
          if(_sleep_count == 3) begin
            memory_wready <= 0;
          end else begin
            memory_wready <= 1;
          end
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            memory_wready <= 0;
          end 
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
        _memory_fsm_200: begin
          if(memory_arvalid) begin
            memory_arready <= 1;
            _read_addr <= memory_araddr;
            _read_count <= memory_arlen + 1;
          end 
          __memory_fsm_cond_200_1_1 <= 1;
          if(!memory_arvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_201;
          end 
        end
        _memory_fsm_201: begin
          _memory_fsm <= _memory_fsm_202;
        end
        _memory_fsm_202: begin
          _memory_fsm <= _memory_fsm_203;
        end
        _memory_fsm_203: begin
          _memory_fsm <= _memory_fsm_204;
        end
        _memory_fsm_204: begin
          _memory_fsm <= _memory_fsm_205;
        end
        _memory_fsm_205: begin
          _memory_fsm <= _memory_fsm_206;
        end
        _memory_fsm_206: begin
          _memory_fsm <= _memory_fsm_207;
        end
        _memory_fsm_207: begin
          _memory_fsm <= _memory_fsm_208;
        end
        _memory_fsm_208: begin
          _memory_fsm <= _memory_fsm_209;
        end
        _memory_fsm_209: begin
          _memory_fsm <= _memory_fsm_210;
        end
        _memory_fsm_210: begin
          _memory_fsm <= _memory_fsm_211;
        end
        _memory_fsm_211: begin
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
          if((_sleep_count < 3) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 4;
            _read_count <= _read_count - 1;
          end 
          if((_sleep_count < 3) && (_read_count == 1) && memory_rready | !memory_rvalid) begin
            memory_rlast <= 1;
          end 
          __memory_fsm_cond_211_2_1 <= 1;
          if(memory_rvalid && !memory_rready) begin
            memory_rvalid <= memory_rvalid;
            memory_rdata <= memory_rdata;
            memory_rlast <= memory_rlast;
          end 
          if(memory_rvalid && memory_rready && (_read_count == 0)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
      endcase
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
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
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
  assign myaxi_bready = 1;
  assign myaxi_arsize = 2;
  assign myaxi_arburst = 1;
  assign myaxi_arlock = 0;
  assign myaxi_arcache = 3;
  assign myaxi_arprot = 0;
  assign myaxi_arqos = 0;
  assign myaxi_aruser = 0;
  reg [3-1:0] outstanding_wcount_0;
  reg _myaxi_read_start;
  reg [8-1:0] _myaxi_read_op_sel;
  reg [32-1:0] _myaxi_read_global_addr;
  reg [33-1:0] _myaxi_read_global_size;
  reg [32-1:0] _myaxi_read_local_addr;
  reg [32-1:0] _myaxi_read_local_stride;
  reg [33-1:0] _myaxi_read_local_size;
  wire _myaxi_read_req_fifo_enq;
  wire [105-1:0] _myaxi_read_req_fifo_wdata;
  wire _myaxi_read_req_fifo_full;
  wire _myaxi_read_req_fifo_almost_full;
  wire _myaxi_read_req_fifo_deq;
  wire [105-1:0] _myaxi_read_req_fifo_rdata;
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
  wire [8-1:0] unpack_read_req_op_sel_1;
  wire [32-1:0] unpack_read_req_local_addr_2;
  wire [32-1:0] unpack_read_req_local_stride_3;
  wire [33-1:0] unpack_read_req_local_size_4;
  assign unpack_read_req_op_sel_1 = _myaxi_read_req_fifo_rdata[104:97];
  assign unpack_read_req_local_addr_2 = _myaxi_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_stride_3 = _myaxi_read_req_fifo_rdata[64:33];
  assign unpack_read_req_local_size_4 = _myaxi_read_req_fifo_rdata[32:0];
  assign _myaxi_read_op_sel_fifo = unpack_read_req_op_sel_1;
  assign _myaxi_read_local_addr_fifo = unpack_read_req_local_addr_2;
  assign _myaxi_read_local_stride_fifo = unpack_read_req_local_stride_3;
  assign _myaxi_read_local_size_fifo = unpack_read_req_local_size_4;
  reg [8-1:0] _myaxi_read_op_sel_buf;
  reg [32-1:0] _myaxi_read_local_addr_buf;
  reg [32-1:0] _myaxi_read_local_stride_buf;
  reg [33-1:0] _myaxi_read_local_size_buf;
  reg _myaxi_read_req_idle;
  reg _myaxi_read_data_idle;
  wire _myaxi_read_idle;
  assign _myaxi_read_idle = !_myaxi_read_start && _myaxi_read_req_idle && _myaxi_read_req_fifo_empty && _myaxi_read_data_idle;
  reg _myaxi_write_start;
  reg [8-1:0] _myaxi_write_op_sel;
  reg [32-1:0] _myaxi_write_global_addr;
  reg [33-1:0] _myaxi_write_global_size;
  reg [32-1:0] _myaxi_write_local_addr;
  reg [32-1:0] _myaxi_write_local_stride;
  reg [33-1:0] _myaxi_write_local_size;
  wire _myaxi_write_req_fifo_enq;
  wire [105-1:0] _myaxi_write_req_fifo_wdata;
  wire _myaxi_write_req_fifo_full;
  wire _myaxi_write_req_fifo_almost_full;
  wire _myaxi_write_req_fifo_deq;
  wire [105-1:0] _myaxi_write_req_fifo_rdata;
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
  wire [8-1:0] unpack_write_req_op_sel_5;
  wire [32-1:0] unpack_write_req_local_addr_6;
  wire [32-1:0] unpack_write_req_local_stride_7;
  wire [33-1:0] unpack_write_req_size_8;
  assign unpack_write_req_op_sel_5 = _myaxi_write_req_fifo_rdata[104:97];
  assign unpack_write_req_local_addr_6 = _myaxi_write_req_fifo_rdata[96:65];
  assign unpack_write_req_local_stride_7 = _myaxi_write_req_fifo_rdata[64:33];
  assign unpack_write_req_size_8 = _myaxi_write_req_fifo_rdata[32:0];
  assign _myaxi_write_op_sel_fifo = unpack_write_req_op_sel_5;
  assign _myaxi_write_local_addr_fifo = unpack_write_req_local_addr_6;
  assign _myaxi_write_local_stride_fifo = unpack_write_req_local_stride_7;
  assign _myaxi_write_size_fifo = unpack_write_req_size_8;
  reg [8-1:0] _myaxi_write_op_sel_buf;
  reg [32-1:0] _myaxi_write_local_addr_buf;
  reg [32-1:0] _myaxi_write_local_stride_buf;
  reg [33-1:0] _myaxi_write_size_buf;
  reg _myaxi_write_req_idle;
  reg _myaxi_write_data_idle;
  wire _myaxi_write_idle;
  assign _myaxi_write_idle = !_myaxi_write_start && _myaxi_write_req_idle && _myaxi_write_req_fifo_empty && _myaxi_write_data_idle;
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
  wire [32-1:0] mask_addr_shifted_9;
  assign mask_addr_shifted_9 = _th_matmul_a_addr_9 >> 2;
  wire [32-1:0] mask_addr_masked_10;
  assign mask_addr_masked_10 = mask_addr_shifted_9 << 2;
  reg [32-1:0] _myaxi_read_req_fsm;
  localparam _myaxi_read_req_fsm_init = 0;
  reg [33-1:0] _myaxi_read_cur_global_size;
  reg _myaxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_11;
  wire [32-1:0] pack_read_req_local_addr_12;
  wire [32-1:0] pack_read_req_local_stride_13;
  wire [33-1:0] pack_read_req_local_size_14;
  assign pack_read_req_op_sel_11 = _myaxi_read_op_sel;
  assign pack_read_req_local_addr_12 = _myaxi_read_local_addr;
  assign pack_read_req_local_stride_13 = _myaxi_read_local_stride;
  assign pack_read_req_local_size_14 = _myaxi_read_local_size;
  wire [105-1:0] pack_read_req_packed_15;
  assign pack_read_req_packed_15 = { pack_read_req_op_sel_11, pack_read_req_local_addr_12, pack_read_req_local_stride_13, pack_read_req_local_size_14 };
  assign _myaxi_read_req_fifo_wdata = ((_myaxi_read_req_fsm == 0) && _myaxi_read_start && !_myaxi_read_req_fifo_almost_full)? pack_read_req_packed_15 : 'hx;
  assign _myaxi_read_req_fifo_enq = ((_myaxi_read_req_fsm == 0) && _myaxi_read_start && !_myaxi_read_req_fifo_almost_full)? (_myaxi_read_req_fsm == 0) && _myaxi_read_start && !_myaxi_read_req_fifo_almost_full && !_myaxi_read_req_fifo_almost_full : 0;
  localparam _tmp_16 = 1;
  wire [_tmp_16-1:0] _tmp_17;
  assign _tmp_17 = !_myaxi_read_req_fifo_almost_full;
  reg [_tmp_16-1:0] __tmp_17_1;
  wire [32-1:0] mask_addr_shifted_18;
  assign mask_addr_shifted_18 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_19;
  assign mask_addr_masked_19 = mask_addr_shifted_18 << 2;
  wire [32-1:0] mask_addr_shifted_20;
  assign mask_addr_shifted_20 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_21;
  assign mask_addr_masked_21 = mask_addr_shifted_20 << 2;
  wire [32-1:0] mask_addr_shifted_22;
  assign mask_addr_shifted_22 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_23;
  assign mask_addr_masked_23 = mask_addr_shifted_22 << 2;
  wire [32-1:0] mask_addr_shifted_24;
  assign mask_addr_shifted_24 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_25;
  assign mask_addr_masked_25 = mask_addr_shifted_24 << 2;
  wire [32-1:0] mask_addr_shifted_26;
  assign mask_addr_shifted_26 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_27;
  assign mask_addr_masked_27 = mask_addr_shifted_26 << 2;
  wire [32-1:0] mask_addr_shifted_28;
  assign mask_addr_shifted_28 = _myaxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_29;
  assign mask_addr_masked_29 = mask_addr_shifted_28 << 2;
  reg _myaxi_cond_0_1;
  reg [32-1:0] _myaxi_read_data_fsm;
  localparam _myaxi_read_data_fsm_init = 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_30;
  reg [10-1:0] write_burst_stride_31;
  reg [11-1:0] write_burst_length_32;
  reg write_burst_done_33;
  assign ram_a_0_wdata = ((write_burst_fsm_0 == 1) && myaxi_rvalid)? myaxi_rdata : 'hx;
  assign ram_a_0_wenable = ((write_burst_fsm_0 == 1) && myaxi_rvalid)? 1'd1 : 0;
  reg signed [32-1:0] _th_matmul_b_addr_12;
  reg signed [32-1:0] _th_matmul_j_13;
  wire [32-1:0] mask_addr_shifted_34;
  assign mask_addr_shifted_34 = _th_matmul_b_addr_12 >> 2;
  wire [32-1:0] mask_addr_masked_35;
  assign mask_addr_masked_35 = mask_addr_shifted_34 << 2;
  reg [32-1:0] write_burst_fsm_1;
  localparam write_burst_fsm_1_init = 0;
  reg [10-1:0] write_burst_addr_36;
  reg [10-1:0] write_burst_stride_37;
  reg [11-1:0] write_burst_length_38;
  reg write_burst_done_39;
  assign ram_b_0_wdata = ((write_burst_fsm_1 == 1) && myaxi_rvalid)? myaxi_rdata : 'hx;
  assign ram_b_0_wenable = ((write_burst_fsm_1 == 1) && myaxi_rvalid)? 1'd1 : 0;
  reg signed [32-1:0] _th_matmul_sum_14;
  reg signed [32-1:0] _th_matmul_k_15;
  assign ram_a_0_addr = (th_matmul == 16)? _th_matmul_k_15 : 
                        ((write_burst_fsm_0 == 1) && myaxi_rvalid)? write_burst_addr_30 : 'hx;
  assign ram_a_0_enable = (th_matmul == 16)? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && myaxi_rvalid)? 1'd1 : 0;
  localparam _tmp_40 = 1;
  wire [_tmp_40-1:0] _tmp_41;
  assign _tmp_41 = th_matmul == 16;
  reg [_tmp_40-1:0] __tmp_41_1;
  reg signed [32-1:0] _tmp_42;
  reg signed [32-1:0] _th_matmul_x_16;
  assign ram_b_0_addr = (th_matmul == 18)? _th_matmul_k_15 : 
                        ((write_burst_fsm_1 == 1) && myaxi_rvalid)? write_burst_addr_36 : 'hx;
  assign ram_b_0_enable = (th_matmul == 18)? 1'd1 : 
                          ((write_burst_fsm_1 == 1) && myaxi_rvalid)? 1'd1 : 0;
  localparam _tmp_43 = 1;
  wire [_tmp_43-1:0] _tmp_44;
  assign _tmp_44 = th_matmul == 18;
  reg [_tmp_43-1:0] __tmp_44_1;
  reg signed [32-1:0] _tmp_45;
  reg signed [32-1:0] _th_matmul_y_17;
  wire [32-1:0] mask_addr_shifted_46;
  assign mask_addr_shifted_46 = _th_matmul_c_addr_10 >> 2;
  wire [32-1:0] mask_addr_masked_47;
  assign mask_addr_masked_47 = mask_addr_shifted_46 << 2;
  reg [32-1:0] _myaxi_write_req_fsm;
  localparam _myaxi_write_req_fsm_init = 0;
  reg [33-1:0] _myaxi_write_cur_global_size;
  reg _myaxi_write_cont;
  wire [8-1:0] pack_write_req_op_sel_48;
  wire [32-1:0] pack_write_req_local_addr_49;
  wire [32-1:0] pack_write_req_local_stride_50;
  wire [33-1:0] pack_write_req_size_51;
  assign pack_write_req_op_sel_48 = _myaxi_write_op_sel;
  assign pack_write_req_local_addr_49 = _myaxi_write_local_addr;
  assign pack_write_req_local_stride_50 = _myaxi_write_local_stride;
  assign pack_write_req_size_51 = _myaxi_write_local_size;
  wire [105-1:0] pack_write_req_packed_52;
  assign pack_write_req_packed_52 = { pack_write_req_op_sel_48, pack_write_req_local_addr_49, pack_write_req_local_stride_50, pack_write_req_size_51 };
  localparam _tmp_53 = 1;
  wire [_tmp_53-1:0] _tmp_54;
  assign _tmp_54 = !_myaxi_write_req_fifo_almost_full;
  reg [_tmp_53-1:0] __tmp_54_1;
  wire [32-1:0] mask_addr_shifted_55;
  assign mask_addr_shifted_55 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_56;
  assign mask_addr_masked_56 = mask_addr_shifted_55 << 2;
  wire [32-1:0] mask_addr_shifted_57;
  assign mask_addr_shifted_57 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_58;
  assign mask_addr_masked_58 = mask_addr_shifted_57 << 2;
  wire [32-1:0] mask_addr_shifted_59;
  assign mask_addr_shifted_59 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_60;
  assign mask_addr_masked_60 = mask_addr_shifted_59 << 2;
  wire [32-1:0] mask_addr_shifted_61;
  assign mask_addr_shifted_61 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_62;
  assign mask_addr_masked_62 = mask_addr_shifted_61 << 2;
  wire [32-1:0] mask_addr_shifted_63;
  assign mask_addr_shifted_63 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_64;
  assign mask_addr_masked_64 = mask_addr_shifted_63 << 2;
  wire [32-1:0] mask_addr_shifted_65;
  assign mask_addr_shifted_65 = _myaxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_66;
  assign mask_addr_masked_66 = mask_addr_shifted_65 << 2;
  wire [8-1:0] pack_write_req_op_sel_67;
  wire [32-1:0] pack_write_req_local_addr_68;
  wire [32-1:0] pack_write_req_local_stride_69;
  wire [33-1:0] pack_write_req_size_70;
  assign pack_write_req_op_sel_67 = _myaxi_write_op_sel;
  assign pack_write_req_local_addr_68 = _myaxi_write_local_addr;
  assign pack_write_req_local_stride_69 = _myaxi_write_local_stride;
  assign pack_write_req_size_70 = _myaxi_write_cur_global_size;
  wire [105-1:0] pack_write_req_packed_71;
  assign pack_write_req_packed_71 = { pack_write_req_op_sel_67, pack_write_req_local_addr_68, pack_write_req_local_stride_69, pack_write_req_size_70 };
  assign _myaxi_write_req_fifo_wdata = ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6))? pack_write_req_packed_71 : 
                                       ((_myaxi_write_req_fsm == 0) && _myaxi_write_start && !_myaxi_write_req_fifo_almost_full)? pack_write_req_packed_52 : 'hx;
  assign _myaxi_write_req_fifo_enq = ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6))? (_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6) && !_myaxi_write_req_fifo_almost_full : 
                                     ((_myaxi_write_req_fsm == 0) && _myaxi_write_start && !_myaxi_write_req_fifo_almost_full)? (_myaxi_write_req_fsm == 0) && _myaxi_write_start && !_myaxi_write_req_fifo_almost_full && !_myaxi_write_req_fifo_almost_full : 0;
  localparam _tmp_72 = 1;
  wire [_tmp_72-1:0] _tmp_73;
  assign _tmp_73 = !_myaxi_write_req_fifo_almost_full;
  reg [_tmp_72-1:0] __tmp_73_1;
  reg _myaxi_cond_1_1;
  reg [32-1:0] _myaxi_write_data_fsm;
  localparam _myaxi_write_data_fsm_init = 0;
  reg [32-1:0] read_burst_fsm_2;
  localparam read_burst_fsm_2_init = 0;
  reg [10-1:0] read_burst_addr_74;
  reg [10-1:0] read_burst_stride_75;
  reg [11-1:0] read_burst_length_76;
  reg read_burst_rvalid_77;
  reg read_burst_rlast_78;
  localparam _tmp_79 = 1;
  wire [_tmp_79-1:0] _tmp_80;
  assign _tmp_80 = (read_burst_fsm_2 == 1) && (!read_burst_rvalid_77 || (myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0));
  reg [_tmp_79-1:0] __tmp_80_1;
  wire [32-1:0] read_burst_rdata_81;
  assign read_burst_rdata_81 = ram_c_0_rdata;
  assign _myaxi_write_req_fifo_deq = ((_myaxi_write_data_fsm == 2) && (!_myaxi_write_req_fifo_empty && (_myaxi_write_size_buf == 0)) && !_myaxi_write_req_fifo_empty)? 1 : 
                                     ((_myaxi_write_data_fsm == 0) && (_myaxi_write_data_idle && !_myaxi_write_req_fifo_empty && (_myaxi_write_op_sel_fifo == 1)) && !_myaxi_write_req_fifo_empty)? 1 : 0;
  reg _myaxi_cond_2_1;
  reg signed [32-1:0] _th_matmul_end_time_18;
  reg signed [32-1:0] _th_matmul_time_19;
  reg signed [32-1:0] _th_matmul_matrix_size_20;
  reg signed [32-1:0] _th_matmul_a_offset_21;
  reg signed [32-1:0] _th_matmul_b_offset_22;
  reg signed [32-1:0] _th_matmul_c_offset_23;
  reg signed [32-1:0] _th_matmul_all_ok_24;
  reg signed [32-1:0] _th_matmul_c_addr_25;
  reg signed [32-1:0] _th_matmul_i_26;
  wire [32-1:0] mask_addr_shifted_82;
  assign mask_addr_shifted_82 = _th_matmul_c_addr_25 >> 2;
  wire [32-1:0] mask_addr_masked_83;
  assign mask_addr_masked_83 = mask_addr_shifted_82 << 2;
  assign _myaxi_read_req_fifo_deq = ((_myaxi_read_data_fsm == 0) && (_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 3)) && !_myaxi_read_req_fifo_empty)? 1 : 
                                    ((_myaxi_read_data_fsm == 0) && (_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 2)) && !_myaxi_read_req_fifo_empty)? 1 : 
                                    ((_myaxi_read_data_fsm == 0) && (_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 1)) && !_myaxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_3;
  localparam write_burst_fsm_3_init = 0;
  reg [10-1:0] write_burst_addr_84;
  reg [10-1:0] write_burst_stride_85;
  reg [11-1:0] write_burst_length_86;
  reg write_burst_done_87;
  assign ram_c_0_wdata = ((write_burst_fsm_3 == 1) && myaxi_rvalid)? myaxi_rdata : 
                         (th_matmul == 22)? _th_matmul_sum_14 : 'hx;
  assign ram_c_0_wenable = ((write_burst_fsm_3 == 1) && myaxi_rvalid)? 1'd1 : 
                           (th_matmul == 22)? 1'd1 : 0;
  assign myaxi_rready = (_myaxi_read_data_fsm == 2) || (_myaxi_read_data_fsm == 2) || (_myaxi_read_data_fsm == 2);
  reg signed [32-1:0] _th_matmul_j_27;
  assign ram_c_0_addr = (th_matmul == 42)? _th_matmul_j_27 : 
                        ((write_burst_fsm_3 == 1) && myaxi_rvalid)? write_burst_addr_84 : 
                        ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_77 || (myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0)))? read_burst_addr_74 : 
                        (th_matmul == 22)? _th_matmul_j_13 : 'hx;
  assign ram_c_0_enable = (th_matmul == 42)? 1'd1 : 
                          ((write_burst_fsm_3 == 1) && myaxi_rvalid)? 1'd1 : 
                          ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_77 || (myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0)))? 1'd1 : 
                          (th_matmul == 22)? 1'd1 : 0;
  localparam _tmp_88 = 1;
  wire [_tmp_88-1:0] _tmp_89;
  assign _tmp_89 = th_matmul == 42;
  reg [_tmp_88-1:0] __tmp_89_1;
  reg signed [32-1:0] _tmp_90;
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
      __tmp_41_1 <= 0;
    end else begin
      __tmp_41_1 <= _tmp_41;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_44_1 <= 0;
    end else begin
      __tmp_44_1 <= _tmp_44;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_80_1 <= 0;
      __tmp_89_1 <= 0;
    end else begin
      __tmp_80_1 <= _tmp_80;
      __tmp_89_1 <= _tmp_89;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wcount_0 <= 0;
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_global_size <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_local_stride <= 0;
      _myaxi_read_local_size <= 0;
      _myaxi_read_req_idle <= 1;
      _myaxi_read_cur_global_size <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _myaxi_cond_0_1 <= 0;
      _myaxi_read_data_idle <= 1;
      _myaxi_read_op_sel_buf <= 0;
      _myaxi_read_local_addr_buf <= 0;
      _myaxi_read_local_stride_buf <= 0;
      _myaxi_read_local_size_buf <= 0;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_global_size <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_local_stride <= 0;
      _myaxi_write_local_size <= 0;
      _myaxi_write_req_idle <= 1;
      _myaxi_write_cur_global_size <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _myaxi_cond_1_1 <= 0;
      _myaxi_write_data_idle <= 1;
      _myaxi_write_op_sel_buf <= 0;
      _myaxi_write_local_addr_buf <= 0;
      _myaxi_write_local_stride_buf <= 0;
      _myaxi_write_size_buf <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
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
      end 
      if(myaxi_awvalid && myaxi_awready && !(myaxi_bvalid && myaxi_bready) && (outstanding_wcount_0 < 7)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 + 1;
      end 
      if(!(myaxi_awvalid && myaxi_awready) && (myaxi_bvalid && myaxi_bready) && (outstanding_wcount_0 > 0)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 - 1;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      if((th_matmul == 6) && _myaxi_read_req_idle) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= 1;
        _myaxi_read_global_addr <= mask_addr_masked_10;
        _myaxi_read_global_size <= _th_matmul_matrix_size_5;
        _myaxi_read_local_addr <= 0;
        _myaxi_read_local_stride <= 1;
        _myaxi_read_local_size <= _th_matmul_matrix_size_5;
      end 
      if((_myaxi_read_req_fsm == 0) && _myaxi_read_start) begin
        _myaxi_read_req_idle <= 0;
      end 
      if(_myaxi_read_start && _myaxi_read_req_fifo_almost_full) begin
        _myaxi_read_start <= 1;
      end 
      if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full && (_myaxi_read_global_size <= 256) && ((mask_addr_masked_19 & 4095) + (_myaxi_read_global_size << 2) >= 4096)) begin
        _myaxi_read_cur_global_size <= 4096 - (mask_addr_masked_21 & 4095) >> 2;
        _myaxi_read_global_size <= _myaxi_read_global_size - (4096 - (mask_addr_masked_23 & 4095) >> 2);
      end else if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full && (_myaxi_read_global_size <= 256)) begin
        _myaxi_read_cur_global_size <= _myaxi_read_global_size;
        _myaxi_read_global_size <= 0;
      end else if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full && ((mask_addr_masked_25 & 4095) + 1024 >= 4096)) begin
        _myaxi_read_cur_global_size <= 4096 - (mask_addr_masked_27 & 4095) >> 2;
        _myaxi_read_global_size <= _myaxi_read_global_size - (4096 - (mask_addr_masked_29 & 4095) >> 2);
      end else if((_myaxi_read_req_fsm == 0) && (_myaxi_read_start || _myaxi_read_cont) && !_myaxi_read_req_fifo_almost_full) begin
        _myaxi_read_cur_global_size <= 256;
        _myaxi_read_global_size <= _myaxi_read_global_size - 256;
      end 
      if((_myaxi_read_req_fsm == 1) && (myaxi_arready || !myaxi_arvalid)) begin
        myaxi_araddr <= _myaxi_read_global_addr;
        myaxi_arlen <= _myaxi_read_cur_global_size - 1;
        myaxi_arvalid <= 1;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if((_myaxi_read_req_fsm == 1) && (myaxi_arready || !myaxi_arvalid) && (_myaxi_read_global_size == 0)) begin
        _myaxi_read_req_idle <= 1;
      end 
      if((_myaxi_read_data_fsm == 0) && (_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 1))) begin
        _myaxi_read_data_idle <= 0;
        _myaxi_read_op_sel_buf <= _myaxi_read_op_sel_fifo;
        _myaxi_read_local_addr_buf <= _myaxi_read_local_addr_fifo;
        _myaxi_read_local_stride_buf <= _myaxi_read_local_stride_fifo;
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_fifo;
      end 
      if((_myaxi_read_data_fsm == 2) && myaxi_rvalid) begin
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_buf - 1;
      end 
      if((_myaxi_read_data_fsm == 2) && myaxi_rvalid && (_myaxi_read_local_size_buf <= 1)) begin
        _myaxi_read_data_idle <= 1;
      end 
      if((th_matmul == 11) && _myaxi_read_req_idle) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= 2;
        _myaxi_read_global_addr <= mask_addr_masked_35;
        _myaxi_read_global_size <= _th_matmul_matrix_size_5;
        _myaxi_read_local_addr <= 0;
        _myaxi_read_local_stride <= 1;
        _myaxi_read_local_size <= _th_matmul_matrix_size_5;
      end 
      if((_myaxi_read_data_fsm == 0) && (_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 2))) begin
        _myaxi_read_data_idle <= 0;
        _myaxi_read_op_sel_buf <= _myaxi_read_op_sel_fifo;
        _myaxi_read_local_addr_buf <= _myaxi_read_local_addr_fifo;
        _myaxi_read_local_stride_buf <= _myaxi_read_local_stride_fifo;
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_fifo;
      end 
      if((_myaxi_read_data_fsm == 2) && myaxi_rvalid) begin
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_buf - 1;
      end 
      if((_myaxi_read_data_fsm == 2) && myaxi_rvalid && (_myaxi_read_local_size_buf <= 1)) begin
        _myaxi_read_data_idle <= 1;
      end 
      if((th_matmul == 25) && _myaxi_write_req_idle) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= 1;
        _myaxi_write_global_addr <= mask_addr_masked_47;
        _myaxi_write_global_size <= _th_matmul_matrix_size_5;
        _myaxi_write_local_addr <= 0;
        _myaxi_write_local_stride <= 1;
        _myaxi_write_local_size <= _th_matmul_matrix_size_5;
      end 
      if((_myaxi_write_req_fsm == 0) && _myaxi_write_start) begin
        _myaxi_write_req_idle <= 0;
      end 
      if(_myaxi_write_start && _myaxi_write_req_fifo_almost_full) begin
        _myaxi_write_start <= 1;
      end 
      if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full && (_myaxi_write_global_size <= 256) && ((mask_addr_masked_56 & 4095) + (_myaxi_write_global_size << 2) >= 4096)) begin
        _myaxi_write_cur_global_size <= 4096 - (mask_addr_masked_58 & 4095) >> 2;
        _myaxi_write_global_size <= _myaxi_write_global_size - (4096 - (mask_addr_masked_60 & 4095) >> 2);
      end else if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full && (_myaxi_write_global_size <= 256)) begin
        _myaxi_write_cur_global_size <= _myaxi_write_global_size;
        _myaxi_write_global_size <= 0;
      end else if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full && ((mask_addr_masked_62 & 4095) + 1024 >= 4096)) begin
        _myaxi_write_cur_global_size <= 4096 - (mask_addr_masked_64 & 4095) >> 2;
        _myaxi_write_global_size <= _myaxi_write_global_size - (4096 - (mask_addr_masked_66 & 4095) >> 2);
      end else if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full) begin
        _myaxi_write_cur_global_size <= 256;
        _myaxi_write_global_size <= _myaxi_write_global_size - 256;
      end 
      if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (outstanding_wcount_0 < 6) && ((outstanding_wcount_0 < 6) && (myaxi_awready || !myaxi_awvalid))) begin
        myaxi_awaddr <= _myaxi_write_global_addr;
        myaxi_awlen <= _myaxi_write_cur_global_size - 1;
        myaxi_awvalid <= 1;
      end 
      if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (outstanding_wcount_0 < 6) && ((outstanding_wcount_0 < 6) && (myaxi_awready || !myaxi_awvalid)) && (_myaxi_write_cur_global_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if((_myaxi_write_req_fsm == 1) && ((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6)) && (_myaxi_write_global_size == 0)) begin
        _myaxi_write_req_idle <= 1;
      end 
      if((_myaxi_write_data_fsm == 0) && (_myaxi_write_data_idle && !_myaxi_write_req_fifo_empty && (_myaxi_write_op_sel_fifo == 1))) begin
        _myaxi_write_data_idle <= 0;
        _myaxi_write_op_sel_buf <= _myaxi_write_op_sel_fifo;
        _myaxi_write_local_addr_buf <= _myaxi_write_local_addr_fifo;
        _myaxi_write_local_stride_buf <= _myaxi_write_local_stride_fifo;
        _myaxi_write_size_buf <= _myaxi_write_size_fifo;
      end 
      if(_myaxi_write_data_fsm == 1) begin
        _myaxi_write_size_buf <= 0;
      end 
      if((_myaxi_write_data_fsm == 2) && (!_myaxi_write_req_fifo_empty && (_myaxi_write_size_buf == 0))) begin
        _myaxi_write_size_buf <= _myaxi_write_size_fifo;
      end 
      if((_myaxi_write_op_sel_buf == 1) && read_burst_rvalid_77 && ((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0)) && ((outstanding_wcount_0 < 6) && (myaxi_wready || !myaxi_wvalid))) begin
        myaxi_wdata <= read_burst_rdata_81;
        myaxi_wvalid <= 1;
        myaxi_wlast <= read_burst_rlast_78 || (_myaxi_write_size_buf == 1);
        myaxi_wstrb <= { 4{ 1'd1 } };
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
      end 
      if((_myaxi_write_data_fsm == 2) && read_burst_rvalid_77 && ((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0))) begin
        _myaxi_write_size_buf <= _myaxi_write_size_buf - 1;
      end 
      if((_myaxi_write_data_fsm == 2) && ((_myaxi_write_op_sel_buf == 1) && read_burst_rvalid_77 && ((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0))) && read_burst_rlast_78) begin
        _myaxi_write_data_idle <= 1;
      end 
      if((th_matmul == 38) && _myaxi_read_req_idle) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= 3;
        _myaxi_read_global_addr <= mask_addr_masked_83;
        _myaxi_read_global_size <= _th_matmul_matrix_size_20;
        _myaxi_read_local_addr <= 0;
        _myaxi_read_local_stride <= 1;
        _myaxi_read_local_size <= _th_matmul_matrix_size_20;
      end 
      if((_myaxi_read_data_fsm == 0) && (_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 3))) begin
        _myaxi_read_data_idle <= 0;
        _myaxi_read_op_sel_buf <= _myaxi_read_op_sel_fifo;
        _myaxi_read_local_addr_buf <= _myaxi_read_local_addr_fifo;
        _myaxi_read_local_stride_buf <= _myaxi_read_local_stride_fifo;
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_fifo;
      end 
      if((_myaxi_read_data_fsm == 2) && myaxi_rvalid) begin
        _myaxi_read_local_size_buf <= _myaxi_read_local_size_buf - 1;
      end 
      if((_myaxi_read_data_fsm == 2) && myaxi_rvalid && (_myaxi_read_local_size_buf <= 1)) begin
        _myaxi_read_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__myaxi_read_req_fifo <= 0;
      __tmp_17_1 <= 0;
    end else begin
      if(_myaxi_read_req_fifo_enq && !_myaxi_read_req_fifo_full && (_myaxi_read_req_fifo_deq && !_myaxi_read_req_fifo_empty)) begin
        count__myaxi_read_req_fifo <= count__myaxi_read_req_fifo;
      end else if(_myaxi_read_req_fifo_enq && !_myaxi_read_req_fifo_full) begin
        count__myaxi_read_req_fifo <= count__myaxi_read_req_fifo + 1;
      end else if(_myaxi_read_req_fifo_deq && !_myaxi_read_req_fifo_empty) begin
        count__myaxi_read_req_fifo <= count__myaxi_read_req_fifo - 1;
      end 
      __tmp_17_1 <= _tmp_17;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__myaxi_write_req_fifo <= 0;
      __tmp_54_1 <= 0;
      __tmp_73_1 <= 0;
    end else begin
      if(_myaxi_write_req_fifo_enq && !_myaxi_write_req_fifo_full && (_myaxi_write_req_fifo_deq && !_myaxi_write_req_fifo_empty)) begin
        count__myaxi_write_req_fifo <= count__myaxi_write_req_fifo;
      end else if(_myaxi_write_req_fifo_enq && !_myaxi_write_req_fifo_full) begin
        count__myaxi_write_req_fifo <= count__myaxi_write_req_fifo + 1;
      end else if(_myaxi_write_req_fifo_deq && !_myaxi_write_req_fifo_empty) begin
        count__myaxi_write_req_fifo <= count__myaxi_write_req_fifo - 1;
      end 
      __tmp_54_1 <= _tmp_54;
      __tmp_73_1 <= _tmp_73;
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
      _tmp_42 <= 0;
      _th_matmul_x_16 <= 0;
      _tmp_45 <= 0;
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
      _tmp_90 <= 0;
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
          if(__tmp_41_1) begin
            _tmp_42 <= ram_a_0_rdata;
          end 
          if(__tmp_41_1) begin
            th_matmul <= th_matmul_17;
          end 
        end
        th_matmul_17: begin
          _th_matmul_x_16 <= _tmp_42;
          th_matmul <= th_matmul_18;
        end
        th_matmul_18: begin
          if(__tmp_44_1) begin
            _tmp_45 <= ram_b_0_rdata;
          end 
          if(__tmp_44_1) begin
            th_matmul <= th_matmul_19;
          end 
        end
        th_matmul_19: begin
          _th_matmul_y_17 <= _tmp_45;
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
          if(_myaxi_write_idle && (outstanding_wcount_0 == 0)) begin
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
          if(__tmp_89_1) begin
            _tmp_90 <= ram_c_0_rdata;
          end 
          if(__tmp_89_1) begin
            th_matmul <= th_matmul_43;
          end 
        end
        th_matmul_43: begin
          _th_matmul_v_28 <= _tmp_90;
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
      _myaxi_read_global_addr <= 0;
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
            _myaxi_read_global_addr <= _myaxi_read_global_addr + (_myaxi_read_cur_global_size << 2);
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
          if(_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_1;
          end 
          if(_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 2)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_1;
          end 
          if(_myaxi_read_data_idle && !_myaxi_read_req_fifo_empty && (_myaxi_read_op_sel_fifo == 3)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_1;
          end 
        end
        _myaxi_read_data_fsm_1: begin
          _myaxi_read_data_fsm <= _myaxi_read_data_fsm_2;
          _myaxi_read_data_fsm <= _myaxi_read_data_fsm_2;
          _myaxi_read_data_fsm <= _myaxi_read_data_fsm_2;
        end
        _myaxi_read_data_fsm_2: begin
          if(myaxi_rvalid && (_myaxi_read_local_size_buf <= 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_init;
          end 
          if(myaxi_rvalid && (_myaxi_read_local_size_buf <= 1)) begin
            _myaxi_read_data_fsm <= _myaxi_read_data_fsm_init;
          end 
          if(myaxi_rvalid && (_myaxi_read_local_size_buf <= 1)) begin
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
      write_burst_addr_30 <= 0;
      write_burst_stride_31 <= 0;
      write_burst_length_32 <= 0;
      write_burst_done_33 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_30 <= _myaxi_read_local_addr_buf;
          write_burst_stride_31 <= _myaxi_read_local_stride_buf;
          write_burst_length_32 <= _myaxi_read_local_size_buf;
          write_burst_done_33 <= 0;
          if((_myaxi_read_data_fsm == 1) && (_myaxi_read_op_sel_buf == 1) && (_myaxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(myaxi_rvalid) begin
            write_burst_addr_30 <= write_burst_addr_30 + write_burst_stride_31;
            write_burst_length_32 <= write_burst_length_32 - 1;
            write_burst_done_33 <= 0;
          end 
          if(myaxi_rvalid && (write_burst_length_32 <= 1)) begin
            write_burst_done_33 <= 1;
          end 
          if(myaxi_rvalid && 0) begin
            write_burst_done_33 <= 1;
          end 
          if(myaxi_rvalid && (write_burst_length_32 <= 1)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(myaxi_rvalid && 0) begin
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
      write_burst_addr_36 <= 0;
      write_burst_stride_37 <= 0;
      write_burst_length_38 <= 0;
      write_burst_done_39 <= 0;
    end else begin
      case(write_burst_fsm_1)
        write_burst_fsm_1_init: begin
          write_burst_addr_36 <= _myaxi_read_local_addr_buf;
          write_burst_stride_37 <= _myaxi_read_local_stride_buf;
          write_burst_length_38 <= _myaxi_read_local_size_buf;
          write_burst_done_39 <= 0;
          if((_myaxi_read_data_fsm == 1) && (_myaxi_read_op_sel_buf == 2) && (_myaxi_read_local_size_buf > 0)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_1;
          end 
        end
        write_burst_fsm_1_1: begin
          if(myaxi_rvalid) begin
            write_burst_addr_36 <= write_burst_addr_36 + write_burst_stride_37;
            write_burst_length_38 <= write_burst_length_38 - 1;
            write_burst_done_39 <= 0;
          end 
          if(myaxi_rvalid && (write_burst_length_38 <= 1)) begin
            write_burst_done_39 <= 1;
          end 
          if(myaxi_rvalid && 0) begin
            write_burst_done_39 <= 1;
          end 
          if(myaxi_rvalid && (write_burst_length_38 <= 1)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(myaxi_rvalid && 0) begin
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
      _myaxi_write_global_addr <= 0;
      _myaxi_write_cont <= 0;
    end else begin
      case(_myaxi_write_req_fsm)
        _myaxi_write_req_fsm_init: begin
          if((_myaxi_write_req_fsm == 0) && (_myaxi_write_start || _myaxi_write_cont) && !_myaxi_write_req_fifo_almost_full) begin
            _myaxi_write_req_fsm <= _myaxi_write_req_fsm_1;
          end 
        end
        _myaxi_write_req_fsm_1: begin
          if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6)) begin
            _myaxi_write_global_addr <= _myaxi_write_global_addr + (_myaxi_write_cur_global_size << 2);
            _myaxi_write_cont <= 1;
          end 
          if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6) && (_myaxi_write_global_size == 0)) begin
            _myaxi_write_cont <= 0;
          end 
          if((_myaxi_write_req_fsm == 1) && !_myaxi_write_req_fifo_almost_full && (myaxi_awready || !myaxi_awvalid) && (outstanding_wcount_0 < 6)) begin
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
          if(_myaxi_write_data_idle && !_myaxi_write_req_fifo_empty && (_myaxi_write_op_sel_fifo == 1)) begin
            _myaxi_write_data_fsm <= _myaxi_write_data_fsm_1;
          end 
        end
        _myaxi_write_data_fsm_1: begin
          _myaxi_write_data_fsm <= _myaxi_write_data_fsm_2;
        end
        _myaxi_write_data_fsm_2: begin
          if((_myaxi_write_op_sel_buf == 1) && read_burst_rvalid_77 && ((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0)) && read_burst_rlast_78) begin
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
      read_burst_addr_74 <= 0;
      read_burst_stride_75 <= 0;
      read_burst_length_76 <= 0;
      read_burst_rvalid_77 <= 0;
      read_burst_rlast_78 <= 0;
    end else begin
      case(read_burst_fsm_2)
        read_burst_fsm_2_init: begin
          read_burst_addr_74 <= _myaxi_write_local_addr_buf;
          read_burst_stride_75 <= _myaxi_write_local_stride_buf;
          read_burst_length_76 <= _myaxi_write_size_buf;
          read_burst_rvalid_77 <= 0;
          read_burst_rlast_78 <= 0;
          if((_myaxi_write_data_fsm == 1) && (_myaxi_write_op_sel_buf == 1) && (_myaxi_write_size_buf > 0)) begin
            read_burst_fsm_2 <= read_burst_fsm_2_1;
          end 
        end
        read_burst_fsm_2_1: begin
          if((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0) && (read_burst_length_76 > 0)) begin
            read_burst_addr_74 <= read_burst_addr_74 + read_burst_stride_75;
            read_burst_length_76 <= read_burst_length_76 - 1;
            read_burst_rvalid_77 <= 1;
          end 
          if((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0) && (read_burst_length_76 <= 1)) begin
            read_burst_rlast_78 <= 1;
          end 
          if(read_burst_rlast_78 && read_burst_rvalid_77 && ((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0))) begin
            read_burst_rvalid_77 <= 0;
            read_burst_rlast_78 <= 0;
          end 
          if(0) begin
            read_burst_rvalid_77 <= 0;
            read_burst_rlast_78 <= 0;
          end 
          if(read_burst_rlast_78 && read_burst_rvalid_77 && ((myaxi_wready || !myaxi_wvalid) && (_myaxi_write_size_buf > 0))) begin
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
      write_burst_addr_84 <= 0;
      write_burst_stride_85 <= 0;
      write_burst_length_86 <= 0;
      write_burst_done_87 <= 0;
    end else begin
      case(write_burst_fsm_3)
        write_burst_fsm_3_init: begin
          write_burst_addr_84 <= _myaxi_read_local_addr_buf;
          write_burst_stride_85 <= _myaxi_read_local_stride_buf;
          write_burst_length_86 <= _myaxi_read_local_size_buf;
          write_burst_done_87 <= 0;
          if((_myaxi_read_data_fsm == 1) && (_myaxi_read_op_sel_buf == 3) && (_myaxi_read_local_size_buf > 0)) begin
            write_burst_fsm_3 <= write_burst_fsm_3_1;
          end 
        end
        write_burst_fsm_3_1: begin
          if(myaxi_rvalid) begin
            write_burst_addr_84 <= write_burst_addr_84 + write_burst_stride_85;
            write_burst_length_86 <= write_burst_length_86 - 1;
            write_burst_done_87 <= 0;
          end 
          if(myaxi_rvalid && (write_burst_length_86 <= 1)) begin
            write_burst_done_87 <= 1;
          end 
          if(myaxi_rvalid && 0) begin
            write_burst_done_87 <= 1;
          end 
          if(myaxi_rvalid && (write_burst_length_86 <= 1)) begin
            write_burst_fsm_3 <= write_burst_fsm_3_init;
          end 
          if(myaxi_rvalid && 0) begin
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
  input [105-1:0] _myaxi_read_req_fifo_wdata,
  output _myaxi_read_req_fifo_full,
  output _myaxi_read_req_fifo_almost_full,
  input _myaxi_read_req_fifo_deq,
  output [105-1:0] _myaxi_read_req_fifo_rdata,
  output _myaxi_read_req_fifo_empty,
  output _myaxi_read_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
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
  wire [105-1:0] rdata;
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
  input [105-1:0] _myaxi_write_req_fifo_wdata,
  output _myaxi_write_req_fifo_full,
  output _myaxi_write_req_fifo_almost_full,
  input _myaxi_write_req_fifo_deq,
  output [105-1:0] _myaxi_write_req_fifo_rdata,
  output _myaxi_write_req_fifo_empty,
  output _myaxi_write_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
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
  wire [105-1:0] rdata;
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
  tfp->open("uut.vcd");
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
