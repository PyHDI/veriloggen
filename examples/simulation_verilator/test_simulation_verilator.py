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
      _sleep_count <= 0;
    end else begin
      if(memory_bvalid && memory_bready) begin
        memory_bvalid <= 0;
      end 
      if(memory_wvalid && memory_wready && memory_wlast) begin
        memory_bvalid <= 1;
      end 
      _sleep_count <= _sleep_count + 1;
      if(_sleep_count == 3) begin
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
  reg [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  reg [32-1:0] ram_a_0_wdata;
  reg ram_a_0_wenable;

  ram_a
  inst_ram_a
  (
    .CLK(CLK),
    .ram_a_0_addr(ram_a_0_addr),
    .ram_a_0_rdata(ram_a_0_rdata),
    .ram_a_0_wdata(ram_a_0_wdata),
    .ram_a_0_wenable(ram_a_0_wenable)
  );

  reg [10-1:0] ram_b_0_addr;
  wire [32-1:0] ram_b_0_rdata;
  reg [32-1:0] ram_b_0_wdata;
  reg ram_b_0_wenable;

  ram_b
  inst_ram_b
  (
    .CLK(CLK),
    .ram_b_0_addr(ram_b_0_addr),
    .ram_b_0_rdata(ram_b_0_rdata),
    .ram_b_0_wdata(ram_b_0_wdata),
    .ram_b_0_wenable(ram_b_0_wenable)
  );

  reg [10-1:0] ram_c_0_addr;
  wire [32-1:0] ram_c_0_rdata;
  reg [32-1:0] ram_c_0_wdata;
  reg ram_c_0_wenable;

  ram_c
  inst_ram_c
  (
    .CLK(CLK),
    .ram_c_0_addr(ram_c_0_addr),
    .ram_c_0_rdata(ram_c_0_rdata),
    .ram_c_0_wdata(ram_c_0_wdata),
    .ram_c_0_wenable(ram_c_0_wenable)
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
  reg [32-1:0] outstanding_wreq_count_0;
  reg _myaxi_read_start;
  reg [8-1:0] _myaxi_read_op_sel;
  reg [32-1:0] _myaxi_read_local_addr;
  reg [32-1:0] _myaxi_read_global_addr;
  reg [33-1:0] _myaxi_read_size;
  reg [32-1:0] _myaxi_read_local_stride;
  reg _myaxi_read_idle;
  reg _myaxi_write_start;
  reg [8-1:0] _myaxi_write_op_sel;
  reg [32-1:0] _myaxi_write_local_addr;
  reg [32-1:0] _myaxi_write_global_addr;
  reg [33-1:0] _myaxi_write_size;
  reg [32-1:0] _myaxi_write_local_stride;
  reg _myaxi_write_idle;
  wire _myaxi_write_data_done;
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
  reg axim_flag_1;
  reg [32-1:0] _d1_th_matmul;
  reg _th_matmul_cond_6_0_1;
  reg _myaxi_ram_a_0_read_start;
  reg [8-1:0] _myaxi_ram_a_0_read_op_sel;
  reg [32-1:0] _myaxi_ram_a_0_read_local_addr;
  reg [32-1:0] _myaxi_ram_a_0_read_global_addr;
  reg [33-1:0] _myaxi_ram_a_0_read_size;
  reg [32-1:0] _myaxi_ram_a_0_read_local_stride;
  reg [32-1:0] _myaxi_read_fsm;
  localparam _myaxi_read_fsm_init = 0;
  reg [32-1:0] _myaxi_read_cur_global_addr;
  reg [33-1:0] _myaxi_read_cur_size;
  reg [33-1:0] _myaxi_read_rest_size;
  reg [32-1:0] _wdata_2;
  reg _wvalid_3;
  reg [34-1:0] _tmp_4;
  reg _tmp_5;
  wire [32-1:0] _dataflow__variable_odata_0;
  wire _dataflow__variable_ovalid_0;
  wire _dataflow__variable_oready_0;
  assign _dataflow__variable_oready_0 = (_tmp_4 > 0) && !_tmp_5;
  reg _ram_a_cond_0_1;
  reg [9-1:0] counter_6;
  reg _myaxi_cond_0_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_7;
  reg __myaxi_read_fsm_cond_4_1_1;
  reg signed [32-1:0] _th_matmul_b_addr_12;
  reg signed [32-1:0] _th_matmul_j_13;
  reg axim_flag_8;
  reg _th_matmul_cond_13_1_1;
  reg _myaxi_ram_b_0_read_start;
  reg [8-1:0] _myaxi_ram_b_0_read_op_sel;
  reg [32-1:0] _myaxi_ram_b_0_read_local_addr;
  reg [32-1:0] _myaxi_ram_b_0_read_global_addr;
  reg [33-1:0] _myaxi_ram_b_0_read_size;
  reg [32-1:0] _myaxi_ram_b_0_read_local_stride;
  reg [32-1:0] _wdata_9;
  reg _wvalid_10;
  reg [34-1:0] _tmp_11;
  reg _tmp_12;
  wire [32-1:0] _dataflow__variable_odata_1;
  wire _dataflow__variable_ovalid_1;
  wire _dataflow__variable_oready_1;
  assign _dataflow__variable_oready_1 = (_tmp_11 > 0) && !_tmp_12;
  reg _ram_b_cond_0_1;
  reg __myaxi_read_fsm_cond_3_2_1;
  reg signed [32-1:0] _th_matmul_sum_14;
  reg signed [32-1:0] _th_matmul_k_15;
  reg _tmp_13;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  reg signed [32-1:0] _tmp_14;
  reg signed [32-1:0] _th_matmul_x_16;
  reg _tmp_15;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  reg signed [32-1:0] _tmp_16;
  reg signed [32-1:0] _th_matmul_y_17;
  reg _ram_c_cond_0_1;
  reg axim_flag_17;
  reg _th_matmul_cond_29_2_1;
  reg _myaxi_ram_c_0_write_start;
  reg [8-1:0] _myaxi_ram_c_0_write_op_sel;
  reg [32-1:0] _myaxi_ram_c_0_write_local_addr;
  reg [32-1:0] _myaxi_ram_c_0_write_global_addr;
  reg [33-1:0] _myaxi_ram_c_0_write_size;
  reg [32-1:0] _myaxi_ram_c_0_write_local_stride;
  reg [32-1:0] _myaxi_write_fsm;
  localparam _myaxi_write_fsm_init = 0;
  reg [32-1:0] _myaxi_write_cur_global_addr;
  reg [33-1:0] _myaxi_write_cur_size;
  reg [33-1:0] _myaxi_write_rest_size;
  reg _tmp_18;
  reg _tmp_19;
  wire _tmp_20;
  wire _tmp_21;
  assign _tmp_21 = 1;
  localparam _tmp_22 = 1;
  wire [_tmp_22-1:0] _tmp_23;
  assign _tmp_23 = (_tmp_20 || !_tmp_18) && (_tmp_21 || !_tmp_19);
  reg [_tmp_22-1:0] __tmp_23_1;
  wire signed [32-1:0] _tmp_24;
  reg signed [32-1:0] __tmp_24_1;
  assign _tmp_24 = (__tmp_23_1)? ram_c_0_rdata : __tmp_24_1;
  reg _tmp_25;
  reg _tmp_26;
  reg _tmp_27;
  reg _tmp_28;
  reg [34-1:0] _tmp_29;
  reg [9-1:0] counter_30;
  reg _myaxi_cond_1_1;
  reg last_31;
  wire [32-1:0] _dataflow__variable_odata_2;
  wire _dataflow__variable_ovalid_2;
  wire _dataflow__variable_oready_2;
  assign _dataflow__variable_oready_2 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((counter_30 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  assign _myaxi_write_data_done = (last_31 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_32;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg signed [32-1:0] _th_matmul_end_time_18;
  reg signed [32-1:0] _th_matmul_time_19;
  reg signed [32-1:0] _th_matmul_matrix_size_20;
  reg signed [32-1:0] _th_matmul_a_offset_21;
  reg signed [32-1:0] _th_matmul_b_offset_22;
  reg signed [32-1:0] _th_matmul_c_offset_23;
  reg signed [32-1:0] _th_matmul_all_ok_24;
  reg signed [32-1:0] _th_matmul_c_addr_25;
  reg signed [32-1:0] _th_matmul_i_26;
  reg axim_flag_33;
  reg _th_matmul_cond_44_3_1;
  reg _myaxi_ram_c_0_read_start;
  reg [8-1:0] _myaxi_ram_c_0_read_op_sel;
  reg [32-1:0] _myaxi_ram_c_0_read_local_addr;
  reg [32-1:0] _myaxi_ram_c_0_read_global_addr;
  reg [33-1:0] _myaxi_ram_c_0_read_size;
  reg [32-1:0] _myaxi_ram_c_0_read_local_stride;
  reg [32-1:0] _wdata_34;
  reg _wvalid_35;
  reg [34-1:0] _tmp_36;
  reg _tmp_37;
  wire [32-1:0] _dataflow__variable_odata_4;
  wire _dataflow__variable_ovalid_4;
  wire _dataflow__variable_oready_4;
  assign _dataflow__variable_oready_4 = (_tmp_36 > 0) && !_tmp_37;
  reg _ram_c_cond_1_1;
  reg __myaxi_read_fsm_cond_3_3_1;
  reg signed [32-1:0] _th_matmul_j_27;
  reg _tmp_38;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_39;
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
      ram_a_0_addr <= 0;
      _tmp_4 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_5 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_13 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_13 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_5 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_13 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_4 == 0)) begin
        ram_a_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_4 <= _myaxi_read_size;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_4 > 0) && !_tmp_5) && (_tmp_4 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _myaxi_read_local_stride;
        ram_a_0_wdata <= _dataflow__variable_odata_0;
        ram_a_0_wenable <= 1;
        _tmp_4 <= _tmp_4 - 1;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_4 > 0) && !_tmp_5) && (_tmp_4 == 1)) begin
        _tmp_5 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      if(th_matmul == 20) begin
        ram_a_0_addr <= _th_matmul_k_15;
      end 
      _ram_a_cond_1_1 <= th_matmul == 20;
      _ram_a_cond_2_1 <= th_matmul == 20;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_11 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_12 <= 0;
      _ram_b_cond_0_1 <= 0;
      _ram_b_cond_1_1 <= 0;
      _tmp_15 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_15 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_12 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_15 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 2) && (_tmp_11 == 0)) begin
        ram_b_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_11 <= _myaxi_read_size;
      end 
      if(_dataflow__variable_ovalid_1 && ((_tmp_11 > 0) && !_tmp_12) && (_tmp_11 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + _myaxi_read_local_stride;
        ram_b_0_wdata <= _dataflow__variable_odata_1;
        ram_b_0_wenable <= 1;
        _tmp_11 <= _tmp_11 - 1;
      end 
      if(_dataflow__variable_ovalid_1 && ((_tmp_11 > 0) && !_tmp_12) && (_tmp_11 == 1)) begin
        _tmp_12 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      if(th_matmul == 22) begin
        ram_b_0_addr <= _th_matmul_k_15;
      end 
      _ram_b_cond_1_1 <= th_matmul == 22;
      _ram_b_cond_2_1 <= th_matmul == 22;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_23_1 <= 0;
      __tmp_24_1 <= 0;
      _tmp_28 <= 0;
      _tmp_18 <= 0;
      _tmp_19 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_25 <= 0;
      _tmp_29 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _ram_c_cond_1_1 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_38 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_38 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
        _tmp_37 <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_38 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(th_matmul == 26) begin
        ram_c_0_addr <= _th_matmul_j_13;
        ram_c_0_wdata <= _th_matmul_sum_14;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= th_matmul == 26;
      __tmp_23_1 <= _tmp_23;
      __tmp_24_1 <= _tmp_24;
      if((_tmp_20 || !_tmp_18) && (_tmp_21 || !_tmp_19) && _tmp_26) begin
        _tmp_28 <= 0;
        _tmp_18 <= 0;
        _tmp_19 <= 0;
        _tmp_26 <= 0;
      end 
      if((_tmp_20 || !_tmp_18) && (_tmp_21 || !_tmp_19) && _tmp_25) begin
        _tmp_18 <= 1;
        _tmp_19 <= 1;
        _tmp_28 <= _tmp_27;
        _tmp_27 <= 0;
        _tmp_25 <= 0;
        _tmp_26 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_29 == 0) && !_tmp_27 && !_tmp_28) begin
        ram_c_0_addr <= _myaxi_write_local_addr;
        _tmp_29 <= _myaxi_write_size - 1;
        _tmp_25 <= 1;
        _tmp_27 <= _myaxi_write_size == 1;
      end 
      if((_tmp_20 || !_tmp_18) && (_tmp_21 || !_tmp_19) && (_tmp_29 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + _myaxi_write_local_stride;
        _tmp_29 <= _tmp_29 - 1;
        _tmp_25 <= 1;
        _tmp_27 <= 0;
      end 
      if((_tmp_20 || !_tmp_18) && (_tmp_21 || !_tmp_19) && (_tmp_29 == 1)) begin
        _tmp_27 <= 1;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 3) && (_tmp_36 == 0)) begin
        ram_c_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_36 <= _myaxi_read_size;
      end 
      if(_dataflow__variable_ovalid_4 && ((_tmp_36 > 0) && !_tmp_37) && (_tmp_36 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + _myaxi_read_local_stride;
        ram_c_0_wdata <= _dataflow__variable_odata_4;
        ram_c_0_wenable <= 1;
        _tmp_36 <= _tmp_36 - 1;
      end 
      if(_dataflow__variable_ovalid_4 && ((_tmp_36 > 0) && !_tmp_37) && (_tmp_36 == 1)) begin
        _tmp_37 <= 1;
      end 
      _ram_c_cond_1_1 <= 1;
      if(th_matmul == 50) begin
        ram_c_0_addr <= _th_matmul_j_27;
      end 
      _ram_c_cond_2_1 <= th_matmul == 50;
      _ram_c_cond_3_1 <= th_matmul == 50;
    end
  end

  assign _dataflow__variable_odata_2 = _tmp_24;
  assign _dataflow__variable_ovalid_2 = _tmp_18;
  assign _tmp_20 = 1 && _dataflow__variable_oready_2;

  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wreq_count_0 <= 0;
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_ram_a_0_read_start <= 0;
      _myaxi_ram_a_0_read_op_sel <= 0;
      _myaxi_ram_a_0_read_local_addr <= 0;
      _myaxi_ram_a_0_read_global_addr <= 0;
      _myaxi_ram_a_0_read_size <= 0;
      _myaxi_ram_a_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      counter_6 <= 0;
      _myaxi_cond_0_1 <= 0;
      _myaxi_ram_b_0_read_start <= 0;
      _myaxi_ram_b_0_read_op_sel <= 0;
      _myaxi_ram_b_0_read_local_addr <= 0;
      _myaxi_ram_b_0_read_global_addr <= 0;
      _myaxi_ram_b_0_read_size <= 0;
      _myaxi_ram_b_0_read_local_stride <= 0;
      _myaxi_ram_c_0_write_start <= 0;
      _myaxi_ram_c_0_write_op_sel <= 0;
      _myaxi_ram_c_0_write_local_addr <= 0;
      _myaxi_ram_c_0_write_global_addr <= 0;
      _myaxi_ram_c_0_write_size <= 0;
      _myaxi_ram_c_0_write_local_stride <= 0;
      _myaxi_write_idle <= 1;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_size <= 0;
      _myaxi_write_local_stride <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      counter_30 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      last_31 <= 0;
      _myaxi_cond_2_1 <= 0;
      _myaxi_ram_c_0_read_start <= 0;
      _myaxi_ram_c_0_read_op_sel <= 0;
      _myaxi_ram_c_0_read_local_addr <= 0;
      _myaxi_ram_c_0_read_global_addr <= 0;
      _myaxi_ram_c_0_read_size <= 0;
      _myaxi_ram_c_0_read_local_stride <= 0;
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
        last_31 <= 0;
      end 
      if(myaxi_awvalid && myaxi_awready && !(myaxi_bvalid && myaxi_bready)) begin
        outstanding_wreq_count_0 <= outstanding_wreq_count_0 + 1;
      end 
      if(!(myaxi_awvalid && myaxi_awready) && (myaxi_bvalid && myaxi_bready) && (outstanding_wreq_count_0 > 0)) begin
        outstanding_wreq_count_0 <= outstanding_wreq_count_0 - 1;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_ram_a_0_read_start <= 0;
      if(axim_flag_1) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= 0;
        _myaxi_ram_a_0_read_global_addr <= _th_matmul_a_addr_9;
        _myaxi_ram_a_0_read_size <= _th_matmul_matrix_size_5;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(_myaxi_ram_a_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_ram_a_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_ram_a_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_ram_a_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_ram_a_0_read_global_addr;
        _myaxi_read_size <= _myaxi_ram_a_0_read_size;
        _myaxi_read_local_stride <= _myaxi_ram_a_0_read_local_stride;
      end 
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (counter_6 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        counter_6 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (counter_6 > 0)) begin
        counter_6 <= counter_6 - 1;
      end 
      if(axim_flag_7) begin
        _myaxi_read_idle <= 1;
      end 
      _myaxi_ram_b_0_read_start <= 0;
      if(axim_flag_8) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= 0;
        _myaxi_ram_b_0_read_global_addr <= _th_matmul_b_addr_12;
        _myaxi_ram_b_0_read_size <= _th_matmul_matrix_size_5;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(_myaxi_ram_b_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_ram_b_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_ram_b_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_ram_b_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_ram_b_0_read_global_addr;
        _myaxi_read_size <= _myaxi_ram_b_0_read_size;
        _myaxi_read_local_stride <= _myaxi_ram_b_0_read_local_stride;
      end 
      _myaxi_ram_c_0_write_start <= 0;
      if(axim_flag_17) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= 0;
        _myaxi_ram_c_0_write_global_addr <= _th_matmul_c_addr_10;
        _myaxi_ram_c_0_write_size <= _th_matmul_matrix_size_5;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
      if(_myaxi_ram_c_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_ram_c_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_ram_c_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_ram_c_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_ram_c_0_write_global_addr;
        _myaxi_write_size <= _myaxi_ram_c_0_write_size;
        _myaxi_write_local_stride <= _myaxi_ram_c_0_write_local_stride;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (counter_30 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        counter_30 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (counter_30 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_dataflow__variable_ovalid_2 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((counter_30 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((counter_30 > 0) && (myaxi_wready || !myaxi_wvalid) && (counter_30 > 0))) begin
        myaxi_wdata <= _dataflow__variable_odata_2;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        counter_30 <= counter_30 - 1;
      end 
      if(_dataflow__variable_ovalid_2 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((counter_30 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((counter_30 > 0) && (myaxi_wready || !myaxi_wvalid) && (counter_30 > 0)) && (counter_30 == 1)) begin
        myaxi_wlast <= 1;
        last_31 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        last_31 <= last_31;
      end 
      if(axim_flag_32) begin
        _myaxi_write_idle <= 1;
      end 
      _myaxi_ram_c_0_read_start <= 0;
      if(axim_flag_33) begin
        _myaxi_ram_c_0_read_start <= 1;
        _myaxi_ram_c_0_read_op_sel <= 3;
        _myaxi_ram_c_0_read_local_addr <= 0;
        _myaxi_ram_c_0_read_global_addr <= _th_matmul_c_addr_25;
        _myaxi_ram_c_0_read_size <= _th_matmul_matrix_size_20;
        _myaxi_ram_c_0_read_local_stride <= 1;
      end 
      if(_myaxi_ram_c_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_ram_c_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_ram_c_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_ram_c_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_ram_c_0_read_global_addr;
        _myaxi_read_size <= _myaxi_ram_c_0_read_size;
        _myaxi_read_local_stride <= _myaxi_ram_c_0_read_local_stride;
      end 
    end
  end

  assign _dataflow__variable_odata_0 = _wdata_2;
  assign _dataflow__variable_ovalid_0 = _wvalid_3;
  assign _dataflow__variable_odata_1 = _wdata_9;
  assign _dataflow__variable_ovalid_1 = _wvalid_10;
  assign _dataflow__variable_odata_4 = _wdata_34;
  assign _dataflow__variable_ovalid_4 = _wvalid_35;
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
  localparam th_matmul_59 = 59;
  localparam th_matmul_60 = 60;
  localparam th_matmul_61 = 61;
  localparam th_matmul_62 = 62;
  localparam th_matmul_63 = 63;
  localparam th_matmul_64 = 64;
  localparam th_matmul_65 = 65;
  localparam th_matmul_66 = 66;

  always @(posedge CLK) begin
    if(RST) begin
      th_matmul <= th_matmul_init;
      _d1_th_matmul <= th_matmul_init;
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
      axim_flag_1 <= 0;
      _th_matmul_cond_6_0_1 <= 0;
      _th_matmul_b_addr_12 <= 0;
      _th_matmul_j_13 <= 0;
      axim_flag_8 <= 0;
      _th_matmul_cond_13_1_1 <= 0;
      _th_matmul_sum_14 <= 0;
      _th_matmul_k_15 <= 0;
      _tmp_14 <= 0;
      _th_matmul_x_16 <= 0;
      _tmp_16 <= 0;
      _th_matmul_y_17 <= 0;
      axim_flag_17 <= 0;
      _th_matmul_cond_29_2_1 <= 0;
      _th_matmul_end_time_18 <= 0;
      _th_matmul_time_19 <= 0;
      _th_matmul_matrix_size_20 <= 0;
      _th_matmul_a_offset_21 <= 0;
      _th_matmul_b_offset_22 <= 0;
      _th_matmul_c_offset_23 <= 0;
      _th_matmul_all_ok_24 <= 0;
      _th_matmul_c_addr_25 <= 0;
      _th_matmul_i_26 <= 0;
      axim_flag_33 <= 0;
      _th_matmul_cond_44_3_1 <= 0;
      _th_matmul_j_27 <= 0;
      _tmp_39 <= 0;
      _th_matmul_v_28 <= 0;
    end else begin
      _d1_th_matmul <= th_matmul;
      case(_d1_th_matmul)
        th_matmul_6: begin
          if(_th_matmul_cond_6_0_1) begin
            axim_flag_1 <= 0;
          end 
        end
        th_matmul_13: begin
          if(_th_matmul_cond_13_1_1) begin
            axim_flag_8 <= 0;
          end 
        end
        th_matmul_29: begin
          if(_th_matmul_cond_29_2_1) begin
            axim_flag_17 <= 0;
          end 
        end
        th_matmul_44: begin
          if(_th_matmul_cond_44_3_1) begin
            axim_flag_33 <= 0;
          end 
        end
      endcase
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
            th_matmul <= th_matmul_36;
          end
        end
        th_matmul_6: begin
          axim_flag_1 <= 1;
          _th_matmul_cond_6_0_1 <= 1;
          th_matmul <= th_matmul_7;
        end
        th_matmul_7: begin
          th_matmul <= th_matmul_8;
        end
        th_matmul_8: begin
          th_matmul <= th_matmul_9;
        end
        th_matmul_9: begin
          if(_myaxi_read_idle) begin
            th_matmul <= th_matmul_10;
          end 
        end
        th_matmul_10: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_offset_7;
          th_matmul <= th_matmul_11;
        end
        th_matmul_11: begin
          _th_matmul_j_13 <= 0;
          th_matmul <= th_matmul_12;
        end
        th_matmul_12: begin
          if(_th_matmul_j_13 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_13;
          end else begin
            th_matmul <= th_matmul_29;
          end
        end
        th_matmul_13: begin
          axim_flag_8 <= 1;
          _th_matmul_cond_13_1_1 <= 1;
          th_matmul <= th_matmul_14;
        end
        th_matmul_14: begin
          th_matmul <= th_matmul_15;
        end
        th_matmul_15: begin
          th_matmul <= th_matmul_16;
        end
        th_matmul_16: begin
          if(_myaxi_read_idle) begin
            th_matmul <= th_matmul_17;
          end 
        end
        th_matmul_17: begin
          _th_matmul_sum_14 <= 0;
          th_matmul <= th_matmul_18;
        end
        th_matmul_18: begin
          _th_matmul_k_15 <= 0;
          th_matmul <= th_matmul_19;
        end
        th_matmul_19: begin
          if(_th_matmul_k_15 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_20;
          end else begin
            th_matmul <= th_matmul_26;
          end
        end
        th_matmul_20: begin
          if(_tmp_13) begin
            _tmp_14 <= ram_a_0_rdata;
          end 
          if(_tmp_13) begin
            th_matmul <= th_matmul_21;
          end 
        end
        th_matmul_21: begin
          _th_matmul_x_16 <= _tmp_14;
          th_matmul <= th_matmul_22;
        end
        th_matmul_22: begin
          if(_tmp_15) begin
            _tmp_16 <= ram_b_0_rdata;
          end 
          if(_tmp_15) begin
            th_matmul <= th_matmul_23;
          end 
        end
        th_matmul_23: begin
          _th_matmul_y_17 <= _tmp_16;
          th_matmul <= th_matmul_24;
        end
        th_matmul_24: begin
          _th_matmul_sum_14 <= _th_matmul_sum_14 + _th_matmul_x_16 * _th_matmul_y_17;
          th_matmul <= th_matmul_25;
        end
        th_matmul_25: begin
          _th_matmul_k_15 <= _th_matmul_k_15 + 1;
          th_matmul <= th_matmul_19;
        end
        th_matmul_26: begin
          th_matmul <= th_matmul_27;
        end
        th_matmul_27: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_addr_12 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_28;
        end
        th_matmul_28: begin
          _th_matmul_j_13 <= _th_matmul_j_13 + 1;
          th_matmul <= th_matmul_12;
        end
        th_matmul_29: begin
          axim_flag_17 <= 1;
          _th_matmul_cond_29_2_1 <= 1;
          th_matmul <= th_matmul_30;
        end
        th_matmul_30: begin
          th_matmul <= th_matmul_31;
        end
        th_matmul_31: begin
          th_matmul <= th_matmul_32;
        end
        th_matmul_32: begin
          if(_myaxi_write_idle && (outstanding_wreq_count_0 == 0)) begin
            th_matmul <= th_matmul_33;
          end 
        end
        th_matmul_33: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_addr_9 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_34;
        end
        th_matmul_34: begin
          _th_matmul_c_addr_10 <= _th_matmul_c_addr_10 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_35;
        end
        th_matmul_35: begin
          _th_matmul_i_11 <= _th_matmul_i_11 + 1;
          th_matmul <= th_matmul_5;
        end
        th_matmul_36: begin
          _th_matmul_end_time_18 <= timer;
          th_matmul <= th_matmul_37;
        end
        th_matmul_37: begin
          _th_matmul_time_19 <= _th_matmul_end_time_18 - _th_matmul_start_time_4;
          th_matmul <= th_matmul_38;
        end
        th_matmul_38: begin
          $display("Time (cycles): %d", _th_matmul_time_19);
          th_matmul <= th_matmul_39;
        end
        th_matmul_39: begin
          _th_matmul_matrix_size_20 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_21 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_22 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_23 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_40;
        end
        th_matmul_40: begin
          _th_matmul_all_ok_24 <= 1;
          th_matmul <= th_matmul_41;
        end
        th_matmul_41: begin
          _th_matmul_c_addr_25 <= _th_matmul_c_offset_23;
          th_matmul <= th_matmul_42;
        end
        th_matmul_42: begin
          _th_matmul_i_26 <= 0;
          th_matmul <= th_matmul_43;
        end
        th_matmul_43: begin
          if(_th_matmul_i_26 < _th_matmul_matrix_size_20) begin
            th_matmul <= th_matmul_44;
          end else begin
            th_matmul <= th_matmul_61;
          end
        end
        th_matmul_44: begin
          axim_flag_33 <= 1;
          _th_matmul_cond_44_3_1 <= 1;
          th_matmul <= th_matmul_45;
        end
        th_matmul_45: begin
          th_matmul <= th_matmul_46;
        end
        th_matmul_46: begin
          th_matmul <= th_matmul_47;
        end
        th_matmul_47: begin
          if(_myaxi_read_idle) begin
            th_matmul <= th_matmul_48;
          end 
        end
        th_matmul_48: begin
          _th_matmul_j_27 <= 0;
          th_matmul <= th_matmul_49;
        end
        th_matmul_49: begin
          if(_th_matmul_j_27 < _th_matmul_matrix_size_20) begin
            th_matmul <= th_matmul_50;
          end else begin
            th_matmul <= th_matmul_59;
          end
        end
        th_matmul_50: begin
          if(_tmp_38) begin
            _tmp_39 <= ram_c_0_rdata;
          end 
          if(_tmp_38) begin
            th_matmul <= th_matmul_51;
          end 
        end
        th_matmul_51: begin
          _th_matmul_v_28 <= _tmp_39;
          th_matmul <= th_matmul_52;
        end
        th_matmul_52: begin
          if((_th_matmul_i_26 == _th_matmul_j_27) && (_th_matmul_v_28 !== (_th_matmul_i_26 + 1 << 1))) begin
            th_matmul <= th_matmul_53;
          end else begin
            th_matmul <= th_matmul_55;
          end
        end
        th_matmul_53: begin
          _th_matmul_all_ok_24 <= 0;
          th_matmul <= th_matmul_54;
        end
        th_matmul_54: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_26, _th_matmul_j_27, _th_matmul_v_28);
          th_matmul <= th_matmul_55;
        end
        th_matmul_55: begin
          if((_th_matmul_i_26 != _th_matmul_j_27) && (_th_matmul_v_28 !== 0)) begin
            th_matmul <= th_matmul_56;
          end else begin
            th_matmul <= th_matmul_58;
          end
        end
        th_matmul_56: begin
          _th_matmul_all_ok_24 <= 0;
          th_matmul <= th_matmul_57;
        end
        th_matmul_57: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_26, _th_matmul_j_27, _th_matmul_v_28);
          th_matmul <= th_matmul_58;
        end
        th_matmul_58: begin
          _th_matmul_j_27 <= _th_matmul_j_27 + 1;
          th_matmul <= th_matmul_49;
        end
        th_matmul_59: begin
          _th_matmul_c_addr_25 <= _th_matmul_c_addr_25 + (_th_matmul_matrix_size_20 << 2);
          th_matmul <= th_matmul_60;
        end
        th_matmul_60: begin
          _th_matmul_i_26 <= _th_matmul_i_26 + 1;
          th_matmul <= th_matmul_43;
        end
        th_matmul_61: begin
          if(_th_matmul_all_ok_24) begin
            th_matmul <= th_matmul_62;
          end else begin
            th_matmul <= th_matmul_64;
          end
        end
        th_matmul_62: begin
          $display("# verify: PASSED");
          th_matmul <= th_matmul_63;
        end
        th_matmul_63: begin
          th_matmul <= th_matmul_65;
        end
        th_matmul_64: begin
          $display("# verify: FAILED");
          th_matmul <= th_matmul_65;
        end
        th_matmul_65: begin
          $finish;
          th_matmul <= th_matmul_66;
        end
      endcase
    end
  end

  localparam _myaxi_read_fsm_1 = 1;
  localparam _myaxi_read_fsm_2 = 2;
  localparam _myaxi_read_fsm_3 = 3;
  localparam _myaxi_read_fsm_4 = 4;
  localparam _myaxi_read_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_fsm <= _myaxi_read_fsm_init;
      _d1__myaxi_read_fsm <= _myaxi_read_fsm_init;
      _myaxi_read_cur_global_addr <= 0;
      _myaxi_read_rest_size <= 0;
      _myaxi_read_cur_size <= 0;
      __myaxi_read_fsm_cond_3_0_1 <= 0;
      _wvalid_3 <= 0;
      _wdata_2 <= 0;
      axim_flag_7 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
      __myaxi_read_fsm_cond_3_2_1 <= 0;
      _wvalid_10 <= 0;
      _wdata_9 <= 0;
      __myaxi_read_fsm_cond_3_3_1 <= 0;
      _wvalid_35 <= 0;
      _wdata_34 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_3 <= 0;
          end 
          if(__myaxi_read_fsm_cond_3_2_1) begin
            _wvalid_10 <= 0;
          end 
          if(__myaxi_read_fsm_cond_3_3_1) begin
            _wvalid_35 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_7 <= 0;
          end 
        end
      endcase
      case(_myaxi_read_fsm)
        _myaxi_read_fsm_init: begin
          if(_myaxi_read_start) begin
            _myaxi_read_cur_global_addr <= (_myaxi_read_global_addr >> 2) << 2;
            _myaxi_read_rest_size <= _myaxi_read_size;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 1)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 2)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 3)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
        end
        _myaxi_read_fsm_1: begin
          if((_myaxi_read_rest_size <= 256) && ((_myaxi_read_cur_global_addr & 4095) + (_myaxi_read_rest_size << 2) >= 4096)) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 2;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 2);
          end else if(_myaxi_read_rest_size <= 256) begin
            _myaxi_read_cur_size <= _myaxi_read_rest_size;
            _myaxi_read_rest_size <= 0;
          end else if((_myaxi_read_cur_global_addr & 4095) + 1024 >= 4096) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 2;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 2);
          end else begin
            _myaxi_read_cur_size <= 256;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - 256;
          end
          _myaxi_read_fsm <= _myaxi_read_fsm_2;
        end
        _myaxi_read_fsm_2: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_3;
          end 
        end
        _myaxi_read_fsm_3: begin
          __myaxi_read_fsm_cond_3_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 1)) begin
            _wdata_2 <= myaxi_rdata;
            _wvalid_3 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 2);
          end 
          __myaxi_read_fsm_cond_3_2_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 2)) begin
            _wdata_9 <= myaxi_rdata;
            _wvalid_10 <= 1;
          end 
          __myaxi_read_fsm_cond_3_3_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 3)) begin
            _wdata_34 <= myaxi_rdata;
            _wvalid_35 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_7 <= 1;
          __myaxi_read_fsm_cond_4_1_1 <= 1;
          _myaxi_read_fsm <= _myaxi_read_fsm_5;
        end
        _myaxi_read_fsm_5: begin
          _myaxi_read_fsm <= _myaxi_read_fsm_init;
        end
      endcase
    end
  end

  localparam _myaxi_write_fsm_1 = 1;
  localparam _myaxi_write_fsm_2 = 2;
  localparam _myaxi_write_fsm_3 = 3;
  localparam _myaxi_write_fsm_4 = 4;
  localparam _myaxi_write_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_fsm <= _myaxi_write_fsm_init;
      _d1__myaxi_write_fsm <= _myaxi_write_fsm_init;
      _myaxi_write_cur_global_addr <= 0;
      _myaxi_write_rest_size <= 0;
      _myaxi_write_cur_size <= 0;
      axim_flag_32 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_32 <= 0;
          end 
        end
      endcase
      case(_myaxi_write_fsm)
        _myaxi_write_fsm_init: begin
          if(_myaxi_write_start) begin
            _myaxi_write_cur_global_addr <= (_myaxi_write_global_addr >> 2) << 2;
            _myaxi_write_rest_size <= _myaxi_write_size;
          end 
          if(_myaxi_write_start && (_myaxi_write_op_sel == 1)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
        end
        _myaxi_write_fsm_1: begin
          if((_myaxi_write_rest_size <= 256) && ((_myaxi_write_cur_global_addr & 4095) + (_myaxi_write_rest_size << 2) >= 4096)) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 2;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 2);
          end else if(_myaxi_write_rest_size <= 256) begin
            _myaxi_write_cur_size <= _myaxi_write_rest_size;
            _myaxi_write_rest_size <= 0;
          end else if((_myaxi_write_cur_global_addr & 4095) + 1024 >= 4096) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 2;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 2);
          end else begin
            _myaxi_write_cur_size <= 256;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - 256;
          end
          _myaxi_write_fsm <= _myaxi_write_fsm_2;
        end
        _myaxi_write_fsm_2: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_3;
          end 
        end
        _myaxi_write_fsm_3: begin
          if(_myaxi_write_data_done) begin
            _myaxi_write_cur_global_addr <= _myaxi_write_cur_global_addr + (_myaxi_write_cur_size << 2);
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size > 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size == 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_4;
          end 
        end
        _myaxi_write_fsm_4: begin
          axim_flag_32 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
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
  input ram_a_0_wenable
);

  reg [10-1:0] ram_a_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_0_wenable) begin
      mem[ram_a_0_addr] <= ram_a_0_wdata;
    end 
    ram_a_0_daddr <= ram_a_0_addr;
  end

  assign ram_a_0_rdata = mem[ram_a_0_daddr];

endmodule



module ram_b
(
  input CLK,
  input [10-1:0] ram_b_0_addr,
  output [32-1:0] ram_b_0_rdata,
  input [32-1:0] ram_b_0_wdata,
  input ram_b_0_wenable
);

  reg [10-1:0] ram_b_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_0_wenable) begin
      mem[ram_b_0_addr] <= ram_b_0_wdata;
    end 
    ram_b_0_daddr <= ram_b_0_addr;
  end

  assign ram_b_0_rdata = mem[ram_b_0_daddr];

endmodule



module ram_c
(
  input CLK,
  input [10-1:0] ram_c_0_addr,
  output [32-1:0] ram_c_0_rdata,
  input [32-1:0] ram_c_0_wdata,
  input ram_c_0_wenable
);

  reg [10-1:0] ram_c_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_0_wenable) begin
      mem[ram_c_0_addr] <= ram_c_0_wdata;
    end 
    ram_c_0_daddr <= ram_c_0_addr;
  end

  assign ram_c_0_rdata = mem[ram_c_0_daddr];

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
