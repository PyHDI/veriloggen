from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_multibank_ram_dma_block

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [128-1:0] myaxi_wdata;
  wire [16-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [128-1:0] myaxi_rdata;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire memory_awvalid;
  reg memory_awready;
  wire [128-1:0] memory_wdata;
  wire [16-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire memory_arvalid;
  reg memory_arready;
  reg [128-1:0] memory_rdata;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("_memory_memimg_.out", _memory_mem);
  end

  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
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

  assign memory_araddr = myaxi_araddr;
  assign memory_arlen = myaxi_arlen;
  assign memory_arvalid = myaxi_arvalid;
  wire _tmp_2;
  assign _tmp_2 = memory_arready;

  always @(*) begin
    myaxi_arready = _tmp_2;
  end


  always @(*) begin
    myaxi_rdata <= memory_rdata;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_rlast;

  always @(*) begin
    myaxi_rlast = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = memory_rvalid;

  always @(*) begin
    myaxi_rvalid = _tmp_4;
  end

  assign memory_rready = myaxi_rready;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    memory_awready = 0;
    memory_wready = 0;
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
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
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
      memory_rdata[39:32] <= (0 >> 32) & { 8{ 1'd1 } };
      memory_rdata[47:40] <= (0 >> 40) & { 8{ 1'd1 } };
      memory_rdata[55:48] <= (0 >> 48) & { 8{ 1'd1 } };
      memory_rdata[63:56] <= (0 >> 56) & { 8{ 1'd1 } };
      memory_rdata[71:64] <= (0 >> 64) & { 8{ 1'd1 } };
      memory_rdata[79:72] <= (0 >> 72) & { 8{ 1'd1 } };
      memory_rdata[87:80] <= (0 >> 80) & { 8{ 1'd1 } };
      memory_rdata[95:88] <= (0 >> 88) & { 8{ 1'd1 } };
      memory_rdata[103:96] <= (0 >> 96) & { 8{ 1'd1 } };
      memory_rdata[111:104] <= (0 >> 104) & { 8{ 1'd1 } };
      memory_rdata[119:112] <= (0 >> 112) & { 8{ 1'd1 } };
      memory_rdata[127:120] <= (0 >> 120) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_fsm_cond_211_2_1 <= 0;
      memory_rdata <= 0;
      _sleep_count <= 0;
    end else begin
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
          if(memory_awvalid) begin
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
          if(memory_wvalid && memory_wstrb[4]) begin
            _memory_mem[_write_addr + 4] <= memory_wdata[39:32];
          end 
          if(memory_wvalid && memory_wstrb[5]) begin
            _memory_mem[_write_addr + 5] <= memory_wdata[47:40];
          end 
          if(memory_wvalid && memory_wstrb[6]) begin
            _memory_mem[_write_addr + 6] <= memory_wdata[55:48];
          end 
          if(memory_wvalid && memory_wstrb[7]) begin
            _memory_mem[_write_addr + 7] <= memory_wdata[63:56];
          end 
          if(memory_wvalid && memory_wstrb[8]) begin
            _memory_mem[_write_addr + 8] <= memory_wdata[71:64];
          end 
          if(memory_wvalid && memory_wstrb[9]) begin
            _memory_mem[_write_addr + 9] <= memory_wdata[79:72];
          end 
          if(memory_wvalid && memory_wstrb[10]) begin
            _memory_mem[_write_addr + 10] <= memory_wdata[87:80];
          end 
          if(memory_wvalid && memory_wstrb[11]) begin
            _memory_mem[_write_addr + 11] <= memory_wdata[95:88];
          end 
          if(memory_wvalid && memory_wstrb[12]) begin
            _memory_mem[_write_addr + 12] <= memory_wdata[103:96];
          end 
          if(memory_wvalid && memory_wstrb[13]) begin
            _memory_mem[_write_addr + 13] <= memory_wdata[111:104];
          end 
          if(memory_wvalid && memory_wstrb[14]) begin
            _memory_mem[_write_addr + 14] <= memory_wdata[119:112];
          end 
          if(memory_wvalid && memory_wstrb[15]) begin
            _memory_mem[_write_addr + 15] <= memory_wdata[127:120];
          end 
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 16;
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
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[39:32] <= _memory_mem[_read_addr + 4];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[47:40] <= _memory_mem[_read_addr + 5];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[55:48] <= _memory_mem[_read_addr + 6];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[63:56] <= _memory_mem[_read_addr + 7];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[71:64] <= _memory_mem[_read_addr + 8];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[79:72] <= _memory_mem[_read_addr + 9];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[87:80] <= _memory_mem[_read_addr + 10];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[95:88] <= _memory_mem[_read_addr + 11];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[103:96] <= _memory_mem[_read_addr + 12];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[111:104] <= _memory_mem[_read_addr + 13];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[119:112] <= _memory_mem[_read_addr + 14];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[127:120] <= _memory_mem[_read_addr + 15];
          end 
          if((_sleep_count < 3) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 16;
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
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [128-1:0] myaxi_wdata,
  output reg [16-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [128-1:0] myaxi_rdata,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  reg [10-1:0] myram_0_0_addr;
  wire [32-1:0] myram_0_0_rdata;
  reg [32-1:0] myram_0_0_wdata;
  reg myram_0_0_wenable;

  myram_0
  inst_myram_0
  (
    .CLK(CLK),
    .myram_0_0_addr(myram_0_0_addr),
    .myram_0_0_rdata(myram_0_0_rdata),
    .myram_0_0_wdata(myram_0_0_wdata),
    .myram_0_0_wenable(myram_0_0_wenable)
  );

  reg [10-1:0] myram_1_0_addr;
  wire [32-1:0] myram_1_0_rdata;
  reg [32-1:0] myram_1_0_wdata;
  reg myram_1_0_wenable;

  myram_1
  inst_myram_1
  (
    .CLK(CLK),
    .myram_1_0_addr(myram_1_0_addr),
    .myram_1_0_rdata(myram_1_0_rdata),
    .myram_1_0_wdata(myram_1_0_wdata),
    .myram_1_0_wenable(myram_1_0_wenable)
  );

  reg [10-1:0] myram_2_0_addr;
  wire [32-1:0] myram_2_0_rdata;
  reg [32-1:0] myram_2_0_wdata;
  reg myram_2_0_wenable;

  myram_2
  inst_myram_2
  (
    .CLK(CLK),
    .myram_2_0_addr(myram_2_0_addr),
    .myram_2_0_rdata(myram_2_0_rdata),
    .myram_2_0_wdata(myram_2_0_wdata),
    .myram_2_0_wenable(myram_2_0_wenable)
  );

  reg [10-1:0] myram_3_0_addr;
  wire [32-1:0] myram_3_0_rdata;
  reg [32-1:0] myram_3_0_wdata;
  reg myram_3_0_wenable;

  myram_3
  inst_myram_3
  (
    .CLK(CLK),
    .myram_3_0_addr(myram_3_0_addr),
    .myram_3_0_rdata(myram_3_0_rdata),
    .myram_3_0_wdata(myram_3_0_wdata),
    .myram_3_0_wenable(myram_3_0_wenable)
  );

  reg _tmp_0;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_offset_2;
  reg signed [32-1:0] _th_blink_size_3;
  reg signed [32-1:0] _th_blink_offset_4;
  reg signed [32-1:0] _th_blink_count_5;
  reg signed [32-1:0] _th_blink_bias_6;
  reg signed [32-1:0] _th_blink_bank_7;
  reg signed [32-1:0] _th_blink_i_8;
  reg signed [32-1:0] _th_blink_wdata_9;
  reg _myram_0_cond_0_1;
  reg _myram_1_cond_0_1;
  reg _myram_2_cond_0_1;
  reg _myram_3_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_10;
  reg signed [32-1:0] _th_blink_gaddr_11;
  reg [10-1:0] _tmp_1;
  reg [10-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _tmp_4;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _tmp_5;
  reg [33-1:0] _tmp_6;
  reg [33-1:0] _tmp_7;
  reg _tmp_8;
  reg _tmp_9;
  wire _tmp_10;
  wire _tmp_11;
  assign _tmp_11 = 1;
  localparam _tmp_12 = 1;
  wire [_tmp_12-1:0] _tmp_13;
  assign _tmp_13 = (_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9);
  reg [_tmp_12-1:0] __tmp_13_1;
  wire signed [32-1:0] _tmp_14;
  wire signed [32-1:0] _tmp_15;
  wire signed [32-1:0] _tmp_16;
  wire signed [32-1:0] _tmp_17;
  reg signed [32-1:0] __tmp_14_1;
  reg signed [32-1:0] __tmp_15_1;
  reg signed [32-1:0] __tmp_16_1;
  reg signed [32-1:0] __tmp_17_1;
  assign _tmp_14 = (__tmp_13_1)? myram_0_0_rdata : __tmp_14_1;
  assign _tmp_15 = (__tmp_13_1)? myram_1_0_rdata : __tmp_15_1;
  assign _tmp_16 = (__tmp_13_1)? myram_2_0_rdata : __tmp_16_1;
  assign _tmp_17 = (__tmp_13_1)? myram_3_0_rdata : __tmp_17_1;
  reg [10-1:0] reg_addr_18;
  reg [10-1:0] reg_addr_19;
  reg [10-1:0] reg_addr_20;
  reg [10-1:0] reg_addr_21;
  wire [10-1:0] next_addr_22;
  wire [10-1:0] next_addr_23;
  wire [10-1:0] next_addr_24;
  wire [10-1:0] next_addr_25;
  assign next_addr_22 = reg_addr_18 + 1;
  assign next_addr_23 = reg_addr_19 + 1;
  assign next_addr_24 = reg_addr_20 + 1;
  assign next_addr_25 = reg_addr_21 + 1;
  wire [10-1:0] _tmp_26;
  wire [10-1:0] _tmp_27;
  wire [10-1:0] _tmp_28;
  wire [10-1:0] _tmp_29;
  assign _tmp_26 = next_addr_22;
  assign _tmp_27 = next_addr_23;
  assign _tmp_28 = next_addr_24;
  assign _tmp_29 = next_addr_25;
  reg [2-1:0] _tmp_30;
  reg [2-1:0] _tmp_31;
  reg [2-1:0] __tmp_31_1;
  wire signed [32-1:0] _tmp_32;
  assign _tmp_32 = (__tmp_13_1)? (_tmp_31 == 0)? _tmp_14 : 
                   (_tmp_31 == 1)? _tmp_15 : 
                   (_tmp_31 == 2)? _tmp_16 : 
                   (_tmp_31 == 3)? _tmp_17 : 0 : 
                   (__tmp_31_1 == 0)? __tmp_14_1 : 
                   (__tmp_31_1 == 1)? __tmp_15_1 : 
                   (__tmp_31_1 == 2)? __tmp_16_1 : 
                   (__tmp_31_1 == 3)? __tmp_17_1 : 0;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg [11-1:0] _tmp_37;
  reg [33-1:0] _tmp_38;
  reg [9-1:0] _tmp_39;
  reg _myaxi_cond_0_1;
  reg [128-1:0] _tmp_40;
  reg _tmp_41;
  wire _tmp_42;
  reg [4-1:0] _tmp_43;
  wire [32-1:0] __variable_data_44;
  wire __variable_valid_44;
  wire __variable_ready_44;
  assign __variable_ready_44 = (_tmp_fsm_0 == 4) && (_tmp_42 || !_tmp_41);
  reg _tmp_45;
  wire [128-1:0] __variable_data_46;
  wire __variable_valid_46;
  wire __variable_ready_46;
  assign __variable_ready_46 = (_tmp_fsm_0 == 4) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  reg _tmp_47;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_5_0_1;
  reg _myram_0_cond_1_1;
  reg _myram_1_cond_1_1;
  reg _myram_2_cond_1_1;
  reg _myram_3_cond_1_1;
  reg [10-1:0] _tmp_48;
  reg [10-1:0] _tmp_49;
  reg [32-1:0] _tmp_50;
  reg [32-1:0] _tmp_51;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_52;
  reg [33-1:0] _tmp_53;
  reg [33-1:0] _tmp_54;
  reg _tmp_55;
  reg _tmp_56;
  wire _tmp_57;
  wire _tmp_58;
  assign _tmp_58 = 1;
  localparam _tmp_59 = 1;
  wire [_tmp_59-1:0] _tmp_60;
  assign _tmp_60 = (_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56);
  reg [_tmp_59-1:0] __tmp_60_1;
  wire signed [32-1:0] _tmp_61;
  wire signed [32-1:0] _tmp_62;
  wire signed [32-1:0] _tmp_63;
  wire signed [32-1:0] _tmp_64;
  reg signed [32-1:0] __tmp_61_1;
  reg signed [32-1:0] __tmp_62_1;
  reg signed [32-1:0] __tmp_63_1;
  reg signed [32-1:0] __tmp_64_1;
  assign _tmp_61 = (__tmp_60_1)? myram_0_0_rdata : __tmp_61_1;
  assign _tmp_62 = (__tmp_60_1)? myram_1_0_rdata : __tmp_62_1;
  assign _tmp_63 = (__tmp_60_1)? myram_2_0_rdata : __tmp_63_1;
  assign _tmp_64 = (__tmp_60_1)? myram_3_0_rdata : __tmp_64_1;
  reg [10-1:0] reg_addr_65;
  reg [10-1:0] reg_addr_66;
  reg [10-1:0] reg_addr_67;
  reg [10-1:0] reg_addr_68;
  wire [10-1:0] next_addr_69;
  wire [10-1:0] next_addr_70;
  wire [10-1:0] next_addr_71;
  wire [10-1:0] next_addr_72;
  assign next_addr_69 = reg_addr_65 + 1;
  assign next_addr_70 = reg_addr_66 + 1;
  assign next_addr_71 = reg_addr_67 + 1;
  assign next_addr_72 = reg_addr_68 + 1;
  wire [10-1:0] _tmp_73;
  wire [10-1:0] _tmp_74;
  wire [10-1:0] _tmp_75;
  wire [10-1:0] _tmp_76;
  assign _tmp_73 = next_addr_69;
  assign _tmp_74 = next_addr_70;
  assign _tmp_75 = next_addr_71;
  assign _tmp_76 = next_addr_72;
  reg [2-1:0] _tmp_77;
  reg [2-1:0] _tmp_78;
  reg [2-1:0] __tmp_78_1;
  wire signed [32-1:0] _tmp_79;
  assign _tmp_79 = (__tmp_60_1)? (_tmp_78 == 0)? _tmp_61 : 
                   (_tmp_78 == 1)? _tmp_62 : 
                   (_tmp_78 == 2)? _tmp_63 : 
                   (_tmp_78 == 3)? _tmp_64 : 0 : 
                   (__tmp_78_1 == 0)? __tmp_61_1 : 
                   (__tmp_78_1 == 1)? __tmp_62_1 : 
                   (__tmp_78_1 == 2)? __tmp_63_1 : 
                   (__tmp_78_1 == 3)? __tmp_64_1 : 0;
  reg _tmp_80;
  reg _tmp_81;
  reg _tmp_82;
  reg _tmp_83;
  reg [11-1:0] _tmp_84;
  reg [33-1:0] _tmp_85;
  reg [9-1:0] _tmp_86;
  reg _myaxi_cond_2_1;
  reg [128-1:0] _tmp_87;
  reg _tmp_88;
  wire _tmp_89;
  reg [4-1:0] _tmp_90;
  wire [32-1:0] __variable_data_91;
  wire __variable_valid_91;
  wire __variable_ready_91;
  assign __variable_ready_91 = (_tmp_fsm_1 == 4) && (_tmp_89 || !_tmp_88);
  reg _tmp_92;
  wire [128-1:0] __variable_data_93;
  wire __variable_valid_93;
  wire __variable_ready_93;
  assign __variable_ready_93 = (_tmp_fsm_1 == 4) && ((_tmp_86 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_94;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_5_0_1;
  reg [10-1:0] _tmp_95;
  reg [10-1:0] _tmp_96;
  reg [32-1:0] _tmp_97;
  reg [32-1:0] _tmp_98;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_99;
  reg [33-1:0] _tmp_100;
  reg [33-1:0] _tmp_101;
  reg [128-1:0] _tmp_102;
  wire [32-1:0] _tmp_103;
  assign _tmp_103 = _tmp_102;
  reg _tmp_104;
  reg [11-1:0] block_counter_105;
  reg [33-1:0] _tmp_106;
  reg _tmp_107;
  wire [32-1:0] __variable_data_108;
  wire __variable_valid_108;
  wire __variable_ready_108;
  assign __variable_ready_108 = (_tmp_106 > 0) && !_tmp_107;
  reg [10-1:0] reg_addr_109;
  reg [10-1:0] reg_addr_110;
  reg [10-1:0] reg_addr_111;
  reg [10-1:0] reg_addr_112;
  wire [10-1:0] next_addr_113;
  wire [10-1:0] next_addr_114;
  wire [10-1:0] next_addr_115;
  wire [10-1:0] next_addr_116;
  assign next_addr_113 = reg_addr_109 + 1;
  assign next_addr_114 = reg_addr_110 + 1;
  assign next_addr_115 = reg_addr_111 + 1;
  assign next_addr_116 = reg_addr_112 + 1;
  wire [10-1:0] ram_addr_117;
  wire [10-1:0] ram_addr_118;
  wire [10-1:0] ram_addr_119;
  wire [10-1:0] ram_addr_120;
  assign ram_addr_117 = next_addr_113;
  assign ram_addr_118 = next_addr_114;
  assign ram_addr_119 = next_addr_115;
  assign ram_addr_120 = next_addr_116;
  reg [2-1:0] bank_sel_121;
  reg _myram_cond_0_1;
  reg _myram_0_cond_2_1;
  reg _myram_1_cond_2_1;
  reg _myram_2_cond_2_1;
  reg _myram_3_cond_2_1;
  reg _tmp_122;
  reg [9-1:0] _tmp_123;
  reg _myaxi_cond_4_1;
  reg [4-1:0] _tmp_124;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_4_0_1;
  reg _tmp_125;
  reg __tmp_fsm_2_cond_5_1_1;
  reg _tmp_126;
  reg _myram_0_cond_3_1;
  reg _myram_0_cond_4_1;
  reg _myram_0_cond_4_2;
  reg _tmp_127;
  reg _myram_1_cond_3_1;
  reg _myram_1_cond_4_1;
  reg _myram_1_cond_4_2;
  reg _tmp_128;
  reg _myram_2_cond_3_1;
  reg _myram_2_cond_4_1;
  reg _myram_2_cond_4_2;
  reg _tmp_129;
  reg _myram_3_cond_3_1;
  reg _myram_3_cond_4_1;
  reg _myram_3_cond_4_2;
  reg signed [32-1:0] _tmp_130;
  reg signed [32-1:0] _th_blink_rdata_12;
  reg [10-1:0] _tmp_131;
  reg [10-1:0] _tmp_132;
  reg [32-1:0] _tmp_133;
  reg [32-1:0] _tmp_134;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_135;
  reg [33-1:0] _tmp_136;
  reg [33-1:0] _tmp_137;
  reg [128-1:0] _tmp_138;
  wire [32-1:0] _tmp_139;
  assign _tmp_139 = _tmp_138;
  reg _tmp_140;
  reg [11-1:0] block_counter_141;
  reg [33-1:0] _tmp_142;
  reg _tmp_143;
  wire [32-1:0] __variable_data_144;
  wire __variable_valid_144;
  wire __variable_ready_144;
  assign __variable_ready_144 = (_tmp_142 > 0) && !_tmp_143;
  reg [10-1:0] reg_addr_145;
  reg [10-1:0] reg_addr_146;
  reg [10-1:0] reg_addr_147;
  reg [10-1:0] reg_addr_148;
  wire [10-1:0] next_addr_149;
  wire [10-1:0] next_addr_150;
  wire [10-1:0] next_addr_151;
  wire [10-1:0] next_addr_152;
  assign next_addr_149 = reg_addr_145 + 1;
  assign next_addr_150 = reg_addr_146 + 1;
  assign next_addr_151 = reg_addr_147 + 1;
  assign next_addr_152 = reg_addr_148 + 1;
  wire [10-1:0] ram_addr_153;
  wire [10-1:0] ram_addr_154;
  wire [10-1:0] ram_addr_155;
  wire [10-1:0] ram_addr_156;
  assign ram_addr_153 = next_addr_149;
  assign ram_addr_154 = next_addr_150;
  assign ram_addr_155 = next_addr_151;
  assign ram_addr_156 = next_addr_152;
  reg [2-1:0] bank_sel_157;
  reg _myram_cond_1_1;
  reg _myram_0_cond_5_1;
  reg _myram_1_cond_5_1;
  reg _myram_2_cond_5_1;
  reg _myram_3_cond_5_1;
  reg _tmp_158;
  reg [9-1:0] _tmp_159;
  reg _myaxi_cond_5_1;
  reg [4-1:0] _tmp_160;
  assign myaxi_rready = (_tmp_fsm_2 == 4) && (_tmp_124 == 0) || (_tmp_fsm_3 == 4) && (_tmp_160 == 0);
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_161;
  reg __tmp_fsm_3_cond_5_1_1;
  reg _tmp_162;
  reg _myram_0_cond_6_1;
  reg _myram_0_cond_7_1;
  reg _myram_0_cond_7_2;
  reg _tmp_163;
  reg _myram_1_cond_6_1;
  reg _myram_1_cond_7_1;
  reg _myram_1_cond_7_2;
  reg _tmp_164;
  reg _myram_2_cond_6_1;
  reg _myram_2_cond_7_1;
  reg _myram_2_cond_7_2;
  reg _tmp_165;
  reg _myram_3_cond_6_1;
  reg _myram_3_cond_7_1;
  reg _myram_3_cond_7_2;
  reg signed [32-1:0] _tmp_166;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_39 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_45 <= 0;
      _myaxi_cond_1_1 <= 0;
      _tmp_86 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_92 <= 0;
      _myaxi_cond_3_1 <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_123 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_159 <= 0;
      _myaxi_cond_5_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_45 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_92 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_5_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_39 == 0))) begin
        myaxi_awaddr <= _tmp_5;
        myaxi_awlen <= _tmp_6 - 1;
        myaxi_awvalid <= 1;
        _tmp_39 <= _tmp_6;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_39 == 0)) && (_tmp_6 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_46 && ((_tmp_fsm_0 == 4) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0))) begin
        myaxi_wdata <= __variable_data_46;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 16{ 1'd1 } };
        _tmp_39 <= _tmp_39 - 1;
      end 
      if(__variable_valid_46 && ((_tmp_fsm_0 == 4) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0)) && (_tmp_39 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_45 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_45 <= _tmp_45;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_86 == 0))) begin
        myaxi_awaddr <= _tmp_52;
        myaxi_awlen <= _tmp_53 - 1;
        myaxi_awvalid <= 1;
        _tmp_86 <= _tmp_53;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_86 == 0)) && (_tmp_53 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_93 && ((_tmp_fsm_1 == 4) && ((_tmp_86 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_86 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_86 > 0))) begin
        myaxi_wdata <= __variable_data_93;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 16{ 1'd1 } };
        _tmp_86 <= _tmp_86 - 1;
      end 
      if(__variable_valid_93 && ((_tmp_fsm_1 == 4) && ((_tmp_86 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_86 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_86 > 0)) && (_tmp_86 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_92 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_92 <= _tmp_92;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_123 == 0))) begin
        myaxi_araddr <= _tmp_99;
        myaxi_arlen <= _tmp_100 - 1;
        myaxi_arvalid <= 1;
        _tmp_123 <= _tmp_100;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_123 > 0)) begin
        _tmp_123 <= _tmp_123 - 1;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_159 == 0))) begin
        myaxi_araddr <= _tmp_135;
        myaxi_arlen <= _tmp_136 - 1;
        myaxi_arvalid <= 1;
        _tmp_159 <= _tmp_136;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_159 > 0)) begin
        _tmp_159 <= _tmp_159 - 1;
      end 
    end
  end

  assign __variable_data_46 = _tmp_40;
  assign __variable_valid_46 = _tmp_41;
  assign _tmp_42 = __variable_ready_46;
  assign __variable_data_93 = _tmp_87;
  assign __variable_valid_93 = _tmp_88;
  assign _tmp_89 = __variable_ready_93;
  assign __variable_data_108 = _tmp_103;
  assign __variable_valid_108 = _tmp_104;
  assign __variable_data_144 = _tmp_139;
  assign __variable_valid_144 = _tmp_140;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_0_addr <= 0;
      myram_0_0_wdata <= 0;
      myram_0_0_wenable <= 0;
      _myram_0_cond_0_1 <= 0;
      _myram_0_cond_1_1 <= 0;
      _myram_0_cond_2_1 <= 0;
      _myram_0_cond_3_1 <= 0;
      _tmp_126 <= 0;
      _myram_0_cond_4_1 <= 0;
      _myram_0_cond_4_2 <= 0;
      _myram_0_cond_5_1 <= 0;
      _myram_0_cond_6_1 <= 0;
      _tmp_162 <= 0;
      _myram_0_cond_7_1 <= 0;
      _myram_0_cond_7_2 <= 0;
    end else begin
      if(_myram_0_cond_4_2) begin
        _tmp_126 <= 0;
      end 
      if(_myram_0_cond_7_2) begin
        _tmp_162 <= 0;
      end 
      if(_myram_0_cond_0_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_1_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_2_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_3_1) begin
        _tmp_126 <= 1;
      end 
      _myram_0_cond_4_2 <= _myram_0_cond_4_1;
      if(_myram_0_cond_5_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_6_1) begin
        _tmp_162 <= 1;
      end 
      _myram_0_cond_7_2 <= _myram_0_cond_7_1;
      if((th_blink == 16) && (_th_blink_bank_7 == 0)) begin
        myram_0_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_0_0_wdata <= _th_blink_wdata_9;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_0_1 <= (th_blink == 16) && (_th_blink_bank_7 == 0);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_0_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 0)) begin
        myram_0_0_addr <= _tmp_26;
      end 
      if((th_blink == 37) && (_th_blink_bank_7 == 0)) begin
        myram_0_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_0_0_wdata <= _th_blink_wdata_9;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_1_1 <= (th_blink == 37) && (_th_blink_bank_7 == 0);
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        myram_0_0_addr <= _tmp_49;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 0)) begin
        myram_0_0_addr <= _tmp_73;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0)) begin
        myram_0_0_addr <= ram_addr_117;
        myram_0_0_wdata <= __variable_data_108;
        myram_0_0_wenable <= bank_sel_121 == 0;
      end 
      _myram_0_cond_2_1 <= 1;
      if(th_blink == 62) begin
        myram_0_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_0_cond_3_1 <= th_blink == 62;
      _myram_0_cond_4_1 <= th_blink == 62;
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0)) begin
        myram_0_0_addr <= ram_addr_153;
        myram_0_0_wdata <= __variable_data_144;
        myram_0_0_wenable <= bank_sel_157 == 0;
      end 
      _myram_0_cond_5_1 <= 1;
      if(th_blink == 86) begin
        myram_0_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_0_cond_6_1 <= th_blink == 86;
      _myram_0_cond_7_1 <= th_blink == 86;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_1_0_addr <= 0;
      myram_1_0_wdata <= 0;
      myram_1_0_wenable <= 0;
      _myram_1_cond_0_1 <= 0;
      _myram_1_cond_1_1 <= 0;
      _myram_1_cond_2_1 <= 0;
      _myram_1_cond_3_1 <= 0;
      _tmp_127 <= 0;
      _myram_1_cond_4_1 <= 0;
      _myram_1_cond_4_2 <= 0;
      _myram_1_cond_5_1 <= 0;
      _myram_1_cond_6_1 <= 0;
      _tmp_163 <= 0;
      _myram_1_cond_7_1 <= 0;
      _myram_1_cond_7_2 <= 0;
    end else begin
      if(_myram_1_cond_4_2) begin
        _tmp_127 <= 0;
      end 
      if(_myram_1_cond_7_2) begin
        _tmp_163 <= 0;
      end 
      if(_myram_1_cond_0_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_1_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_2_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_3_1) begin
        _tmp_127 <= 1;
      end 
      _myram_1_cond_4_2 <= _myram_1_cond_4_1;
      if(_myram_1_cond_5_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_6_1) begin
        _tmp_163 <= 1;
      end 
      _myram_1_cond_7_2 <= _myram_1_cond_7_1;
      if((th_blink == 16) && (_th_blink_bank_7 == 1)) begin
        myram_1_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_1_0_wdata <= _th_blink_wdata_9;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_0_1 <= (th_blink == 16) && (_th_blink_bank_7 == 1);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_1_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 1)) begin
        myram_1_0_addr <= _tmp_27;
      end 
      if((th_blink == 37) && (_th_blink_bank_7 == 1)) begin
        myram_1_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_1_0_wdata <= _th_blink_wdata_9;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_1_1 <= (th_blink == 37) && (_th_blink_bank_7 == 1);
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        myram_1_0_addr <= _tmp_49;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 1)) begin
        myram_1_0_addr <= _tmp_74;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0)) begin
        myram_1_0_addr <= ram_addr_118;
        myram_1_0_wdata <= __variable_data_108;
        myram_1_0_wenable <= bank_sel_121 == 1;
      end 
      _myram_1_cond_2_1 <= 1;
      if(th_blink == 62) begin
        myram_1_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_1_cond_3_1 <= th_blink == 62;
      _myram_1_cond_4_1 <= th_blink == 62;
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0)) begin
        myram_1_0_addr <= ram_addr_154;
        myram_1_0_wdata <= __variable_data_144;
        myram_1_0_wenable <= bank_sel_157 == 1;
      end 
      _myram_1_cond_5_1 <= 1;
      if(th_blink == 86) begin
        myram_1_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_1_cond_6_1 <= th_blink == 86;
      _myram_1_cond_7_1 <= th_blink == 86;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_2_0_addr <= 0;
      myram_2_0_wdata <= 0;
      myram_2_0_wenable <= 0;
      _myram_2_cond_0_1 <= 0;
      _myram_2_cond_1_1 <= 0;
      _myram_2_cond_2_1 <= 0;
      _myram_2_cond_3_1 <= 0;
      _tmp_128 <= 0;
      _myram_2_cond_4_1 <= 0;
      _myram_2_cond_4_2 <= 0;
      _myram_2_cond_5_1 <= 0;
      _myram_2_cond_6_1 <= 0;
      _tmp_164 <= 0;
      _myram_2_cond_7_1 <= 0;
      _myram_2_cond_7_2 <= 0;
    end else begin
      if(_myram_2_cond_4_2) begin
        _tmp_128 <= 0;
      end 
      if(_myram_2_cond_7_2) begin
        _tmp_164 <= 0;
      end 
      if(_myram_2_cond_0_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_1_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_2_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_3_1) begin
        _tmp_128 <= 1;
      end 
      _myram_2_cond_4_2 <= _myram_2_cond_4_1;
      if(_myram_2_cond_5_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_6_1) begin
        _tmp_164 <= 1;
      end 
      _myram_2_cond_7_2 <= _myram_2_cond_7_1;
      if((th_blink == 16) && (_th_blink_bank_7 == 2)) begin
        myram_2_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_2_0_wdata <= _th_blink_wdata_9;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_0_1 <= (th_blink == 16) && (_th_blink_bank_7 == 2);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_2_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 2)) begin
        myram_2_0_addr <= _tmp_28;
      end 
      if((th_blink == 37) && (_th_blink_bank_7 == 2)) begin
        myram_2_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_2_0_wdata <= _th_blink_wdata_9;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_1_1 <= (th_blink == 37) && (_th_blink_bank_7 == 2);
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        myram_2_0_addr <= _tmp_49;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 2)) begin
        myram_2_0_addr <= _tmp_75;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0)) begin
        myram_2_0_addr <= ram_addr_119;
        myram_2_0_wdata <= __variable_data_108;
        myram_2_0_wenable <= bank_sel_121 == 2;
      end 
      _myram_2_cond_2_1 <= 1;
      if(th_blink == 62) begin
        myram_2_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_2_cond_3_1 <= th_blink == 62;
      _myram_2_cond_4_1 <= th_blink == 62;
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0)) begin
        myram_2_0_addr <= ram_addr_155;
        myram_2_0_wdata <= __variable_data_144;
        myram_2_0_wenable <= bank_sel_157 == 2;
      end 
      _myram_2_cond_5_1 <= 1;
      if(th_blink == 86) begin
        myram_2_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_2_cond_6_1 <= th_blink == 86;
      _myram_2_cond_7_1 <= th_blink == 86;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_3_0_addr <= 0;
      myram_3_0_wdata <= 0;
      myram_3_0_wenable <= 0;
      _myram_3_cond_0_1 <= 0;
      _myram_3_cond_1_1 <= 0;
      _myram_3_cond_2_1 <= 0;
      _myram_3_cond_3_1 <= 0;
      _tmp_129 <= 0;
      _myram_3_cond_4_1 <= 0;
      _myram_3_cond_4_2 <= 0;
      _myram_3_cond_5_1 <= 0;
      _myram_3_cond_6_1 <= 0;
      _tmp_165 <= 0;
      _myram_3_cond_7_1 <= 0;
      _myram_3_cond_7_2 <= 0;
    end else begin
      if(_myram_3_cond_4_2) begin
        _tmp_129 <= 0;
      end 
      if(_myram_3_cond_7_2) begin
        _tmp_165 <= 0;
      end 
      if(_myram_3_cond_0_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_1_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_2_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_3_1) begin
        _tmp_129 <= 1;
      end 
      _myram_3_cond_4_2 <= _myram_3_cond_4_1;
      if(_myram_3_cond_5_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_6_1) begin
        _tmp_165 <= 1;
      end 
      _myram_3_cond_7_2 <= _myram_3_cond_7_1;
      if((th_blink == 16) && (_th_blink_bank_7 == 3)) begin
        myram_3_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_3_0_wdata <= _th_blink_wdata_9;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_0_1 <= (th_blink == 16) && (_th_blink_bank_7 == 3);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_3_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 3)) begin
        myram_3_0_addr <= _tmp_29;
      end 
      if((th_blink == 37) && (_th_blink_bank_7 == 3)) begin
        myram_3_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
        myram_3_0_wdata <= _th_blink_wdata_9;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_1_1 <= (th_blink == 37) && (_th_blink_bank_7 == 3);
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        myram_3_0_addr <= _tmp_49;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 3)) begin
        myram_3_0_addr <= _tmp_76;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0)) begin
        myram_3_0_addr <= ram_addr_120;
        myram_3_0_wdata <= __variable_data_108;
        myram_3_0_wenable <= bank_sel_121 == 3;
      end 
      _myram_3_cond_2_1 <= 1;
      if(th_blink == 62) begin
        myram_3_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_3_cond_3_1 <= th_blink == 62;
      _myram_3_cond_4_1 <= th_blink == 62;
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0)) begin
        myram_3_0_addr <= ram_addr_156;
        myram_3_0_wdata <= __variable_data_144;
        myram_3_0_wenable <= bank_sel_157 == 3;
      end 
      _myram_3_cond_5_1 <= 1;
      if(th_blink == 86) begin
        myram_3_0_addr <= _th_blink_offset_4 + _th_blink_i_8;
      end 
      _myram_3_cond_6_1 <= th_blink == 86;
      _myram_3_cond_7_1 <= th_blink == 86;
    end
  end

  assign __variable_data_44 = _tmp_32;
  assign __variable_valid_44 = _tmp_8;
  assign _tmp_10 = 1 && __variable_ready_44;
  assign __variable_data_91 = _tmp_79;
  assign __variable_valid_91 = _tmp_55;
  assign _tmp_57 = 1 && __variable_ready_91;
  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;
  localparam th_blink_12 = 12;
  localparam th_blink_13 = 13;
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;
  localparam th_blink_26 = 26;
  localparam th_blink_27 = 27;
  localparam th_blink_28 = 28;
  localparam th_blink_29 = 29;
  localparam th_blink_30 = 30;
  localparam th_blink_31 = 31;
  localparam th_blink_32 = 32;
  localparam th_blink_33 = 33;
  localparam th_blink_34 = 34;
  localparam th_blink_35 = 35;
  localparam th_blink_36 = 36;
  localparam th_blink_37 = 37;
  localparam th_blink_38 = 38;
  localparam th_blink_39 = 39;
  localparam th_blink_40 = 40;
  localparam th_blink_41 = 41;
  localparam th_blink_42 = 42;
  localparam th_blink_43 = 43;
  localparam th_blink_44 = 44;
  localparam th_blink_45 = 45;
  localparam th_blink_46 = 46;
  localparam th_blink_47 = 47;
  localparam th_blink_48 = 48;
  localparam th_blink_49 = 49;
  localparam th_blink_50 = 50;
  localparam th_blink_51 = 51;
  localparam th_blink_52 = 52;
  localparam th_blink_53 = 53;
  localparam th_blink_54 = 54;
  localparam th_blink_55 = 55;
  localparam th_blink_56 = 56;
  localparam th_blink_57 = 57;
  localparam th_blink_58 = 58;
  localparam th_blink_59 = 59;
  localparam th_blink_60 = 60;
  localparam th_blink_61 = 61;
  localparam th_blink_62 = 62;
  localparam th_blink_63 = 63;
  localparam th_blink_64 = 64;
  localparam th_blink_65 = 65;
  localparam th_blink_66 = 66;
  localparam th_blink_67 = 67;
  localparam th_blink_68 = 68;
  localparam th_blink_69 = 69;
  localparam th_blink_70 = 70;
  localparam th_blink_71 = 71;
  localparam th_blink_72 = 72;
  localparam th_blink_73 = 73;
  localparam th_blink_74 = 74;
  localparam th_blink_75 = 75;
  localparam th_blink_76 = 76;
  localparam th_blink_77 = 77;
  localparam th_blink_78 = 78;
  localparam th_blink_79 = 79;
  localparam th_blink_80 = 80;
  localparam th_blink_81 = 81;
  localparam th_blink_82 = 82;
  localparam th_blink_83 = 83;
  localparam th_blink_84 = 84;
  localparam th_blink_85 = 85;
  localparam th_blink_86 = 86;
  localparam th_blink_87 = 87;
  localparam th_blink_88 = 88;
  localparam th_blink_89 = 89;
  localparam th_blink_90 = 90;
  localparam th_blink_91 = 91;
  localparam th_blink_92 = 92;
  localparam th_blink_93 = 93;
  localparam th_blink_94 = 94;
  localparam th_blink_95 = 95;
  localparam th_blink_96 = 96;
  localparam th_blink_97 = 97;
  localparam th_blink_98 = 98;
  localparam th_blink_99 = 99;
  localparam th_blink_100 = 100;
  localparam th_blink_101 = 101;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_offset_2 <= 0;
      _th_blink_size_3 <= 0;
      _th_blink_offset_4 <= 0;
      _th_blink_count_5 <= 0;
      _th_blink_bias_6 <= 0;
      _th_blink_bank_7 <= 0;
      _th_blink_i_8 <= 0;
      _th_blink_wdata_9 <= 0;
      _th_blink_laddr_10 <= 0;
      _th_blink_gaddr_11 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_48 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _tmp_130 <= 0;
      _th_blink_rdata_12 <= 0;
      _tmp_131 <= 0;
      _tmp_132 <= 0;
      _tmp_133 <= 0;
      _tmp_134 <= 0;
      _tmp_166 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 32;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _tmp_0 <= 1;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_i_1 < 4) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_99;
          end
        end
        th_blink_4: begin
          $display("# iter %d start", _th_blink_i_1);
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_offset_2 <= ((_th_blink_i_1 << 10) << 4) + 4092;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_size_3 <= _th_blink_size_0;
          _th_blink_offset_4 <= _th_blink_offset_2;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_count_5 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_offset_4 <= 0;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          if(_th_blink_count_5 < _th_blink_size_3) begin
            th_blink <= th_blink_11;
          end else begin
            th_blink <= th_blink_23;
          end
        end
        th_blink_11: begin
          _th_blink_bank_7 <= 0;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          if(_th_blink_bank_7 < 4) begin
            th_blink <= th_blink_13;
          end else begin
            th_blink <= th_blink_21;
          end
        end
        th_blink_13: begin
          _th_blink_i_8 <= 0;
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          if(_th_blink_i_8 < 4) begin
            th_blink <= th_blink_15;
          end else begin
            th_blink <= th_blink_19;
          end
        end
        th_blink_15: begin
          _th_blink_wdata_9 <= _th_blink_bias_6 + _th_blink_i_8 + 100;
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          _th_blink_count_5 <= _th_blink_count_5 + 1;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          _th_blink_i_8 <= _th_blink_i_8 + 1;
          th_blink <= th_blink_14;
        end
        th_blink_19: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 4;
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          _th_blink_bank_7 <= _th_blink_bank_7 + 1;
          th_blink <= th_blink_12;
        end
        th_blink_21: begin
          _th_blink_offset_4 <= _th_blink_offset_4 + 4;
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          th_blink <= th_blink_10;
        end
        th_blink_23: begin
          _th_blink_laddr_10 <= 0;
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          _th_blink_gaddr_11 <= _th_blink_offset_4;
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          _tmp_1 <= 4;
          _tmp_2 <= _th_blink_laddr_10;
          _tmp_3 <= _th_blink_gaddr_11;
          _tmp_4 <= _th_blink_size_3;
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          if(_tmp_47) begin
            th_blink <= th_blink_27;
          end 
        end
        th_blink_27: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_10, _th_blink_gaddr_11);
          th_blink <= th_blink_28;
        end
        th_blink_28: begin
          _th_blink_count_5 <= 0;
          th_blink <= th_blink_29;
        end
        th_blink_29: begin
          _th_blink_offset_4 <= 0;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_31;
        end
        th_blink_31: begin
          if(_th_blink_count_5 < _th_blink_size_3) begin
            th_blink <= th_blink_32;
          end else begin
            th_blink <= th_blink_44;
          end
        end
        th_blink_32: begin
          _th_blink_bank_7 <= 0;
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          if(_th_blink_bank_7 < 4) begin
            th_blink <= th_blink_34;
          end else begin
            th_blink <= th_blink_42;
          end
        end
        th_blink_34: begin
          _th_blink_i_8 <= 0;
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          if(_th_blink_i_8 < 4) begin
            th_blink <= th_blink_36;
          end else begin
            th_blink <= th_blink_40;
          end
        end
        th_blink_36: begin
          _th_blink_wdata_9 <= _th_blink_bias_6 + _th_blink_i_8 + 1000;
          th_blink <= th_blink_37;
        end
        th_blink_37: begin
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          _th_blink_count_5 <= _th_blink_count_5 + 1;
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          _th_blink_i_8 <= _th_blink_i_8 + 1;
          th_blink <= th_blink_35;
        end
        th_blink_40: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 4;
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          _th_blink_bank_7 <= _th_blink_bank_7 + 1;
          th_blink <= th_blink_33;
        end
        th_blink_42: begin
          _th_blink_offset_4 <= _th_blink_offset_4 + 4;
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          th_blink <= th_blink_31;
        end
        th_blink_44: begin
          _th_blink_laddr_10 <= 0;
          th_blink <= th_blink_45;
        end
        th_blink_45: begin
          _th_blink_gaddr_11 <= 1024 + _th_blink_offset_4;
          th_blink <= th_blink_46;
        end
        th_blink_46: begin
          _tmp_48 <= 4;
          _tmp_49 <= _th_blink_laddr_10;
          _tmp_50 <= _th_blink_gaddr_11;
          _tmp_51 <= _th_blink_size_3;
          th_blink <= th_blink_47;
        end
        th_blink_47: begin
          if(_tmp_94) begin
            th_blink <= th_blink_48;
          end 
        end
        th_blink_48: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_10, _th_blink_gaddr_11);
          th_blink <= th_blink_49;
        end
        th_blink_49: begin
          _th_blink_laddr_10 <= 0;
          th_blink <= th_blink_50;
        end
        th_blink_50: begin
          _th_blink_gaddr_11 <= _th_blink_offset_4;
          th_blink <= th_blink_51;
        end
        th_blink_51: begin
          _tmp_95 <= 4;
          _tmp_96 <= _th_blink_laddr_10;
          _tmp_97 <= _th_blink_gaddr_11;
          _tmp_98 <= _th_blink_size_3;
          th_blink <= th_blink_52;
        end
        th_blink_52: begin
          if(_tmp_125) begin
            th_blink <= th_blink_53;
          end 
        end
        th_blink_53: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_10, _th_blink_gaddr_11);
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          _th_blink_count_5 <= 0;
          th_blink <= th_blink_55;
        end
        th_blink_55: begin
          _th_blink_offset_4 <= 0;
          th_blink <= th_blink_56;
        end
        th_blink_56: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_57;
        end
        th_blink_57: begin
          if(_th_blink_count_5 < _th_blink_size_3) begin
            th_blink <= th_blink_58;
          end else begin
            th_blink <= th_blink_73;
          end
        end
        th_blink_58: begin
          _th_blink_bank_7 <= 0;
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          if(_th_blink_bank_7 < 4) begin
            th_blink <= th_blink_60;
          end else begin
            th_blink <= th_blink_71;
          end
        end
        th_blink_60: begin
          _th_blink_i_8 <= 0;
          th_blink <= th_blink_61;
        end
        th_blink_61: begin
          if(_th_blink_i_8 < 4) begin
            th_blink <= th_blink_62;
          end else begin
            th_blink <= th_blink_69;
          end
        end
        th_blink_62: begin
          if(_tmp_126 && (_th_blink_bank_7 == 0)) begin
            _tmp_130 <= myram_0_0_rdata;
          end 
          if(_tmp_127 && (_th_blink_bank_7 == 1)) begin
            _tmp_130 <= myram_1_0_rdata;
          end 
          if(_tmp_128 && (_th_blink_bank_7 == 2)) begin
            _tmp_130 <= myram_2_0_rdata;
          end 
          if(_tmp_129 && (_th_blink_bank_7 == 3)) begin
            _tmp_130 <= myram_3_0_rdata;
          end 
          if(_tmp_126) begin
            th_blink <= th_blink_63;
          end 
        end
        th_blink_63: begin
          _th_blink_rdata_12 <= _tmp_130;
          th_blink <= th_blink_64;
        end
        th_blink_64: begin
          if(_th_blink_rdata_12 !== _th_blink_bias_6 + _th_blink_i_8 + 100) begin
            th_blink <= th_blink_65;
          end else begin
            th_blink <= th_blink_67;
          end
        end
        th_blink_65: begin
          $display("rdata[%d:%d] = %d", _th_blink_bank_7, _th_blink_i_8, _th_blink_rdata_12);
          th_blink <= th_blink_66;
        end
        th_blink_66: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_67;
        end
        th_blink_67: begin
          _th_blink_count_5 <= _th_blink_count_5 + 1;
          th_blink <= th_blink_68;
        end
        th_blink_68: begin
          _th_blink_i_8 <= _th_blink_i_8 + 1;
          th_blink <= th_blink_61;
        end
        th_blink_69: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 4;
          th_blink <= th_blink_70;
        end
        th_blink_70: begin
          _th_blink_bank_7 <= _th_blink_bank_7 + 1;
          th_blink <= th_blink_59;
        end
        th_blink_71: begin
          _th_blink_offset_4 <= _th_blink_offset_4 + 4;
          th_blink <= th_blink_72;
        end
        th_blink_72: begin
          th_blink <= th_blink_57;
        end
        th_blink_73: begin
          _th_blink_laddr_10 <= 0;
          th_blink <= th_blink_74;
        end
        th_blink_74: begin
          _th_blink_gaddr_11 <= 1024 + _th_blink_offset_4;
          th_blink <= th_blink_75;
        end
        th_blink_75: begin
          _tmp_131 <= 4;
          _tmp_132 <= _th_blink_laddr_10;
          _tmp_133 <= _th_blink_gaddr_11;
          _tmp_134 <= _th_blink_size_3;
          th_blink <= th_blink_76;
        end
        th_blink_76: begin
          if(_tmp_161) begin
            th_blink <= th_blink_77;
          end 
        end
        th_blink_77: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_10, _th_blink_gaddr_11);
          th_blink <= th_blink_78;
        end
        th_blink_78: begin
          _th_blink_count_5 <= 0;
          th_blink <= th_blink_79;
        end
        th_blink_79: begin
          _th_blink_offset_4 <= 0;
          th_blink <= th_blink_80;
        end
        th_blink_80: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_81;
        end
        th_blink_81: begin
          if(_th_blink_count_5 < _th_blink_size_3) begin
            th_blink <= th_blink_82;
          end else begin
            th_blink <= th_blink_97;
          end
        end
        th_blink_82: begin
          _th_blink_bank_7 <= 0;
          th_blink <= th_blink_83;
        end
        th_blink_83: begin
          if(_th_blink_bank_7 < 4) begin
            th_blink <= th_blink_84;
          end else begin
            th_blink <= th_blink_95;
          end
        end
        th_blink_84: begin
          _th_blink_i_8 <= 0;
          th_blink <= th_blink_85;
        end
        th_blink_85: begin
          if(_th_blink_i_8 < 4) begin
            th_blink <= th_blink_86;
          end else begin
            th_blink <= th_blink_93;
          end
        end
        th_blink_86: begin
          if(_tmp_162 && (_th_blink_bank_7 == 0)) begin
            _tmp_166 <= myram_0_0_rdata;
          end 
          if(_tmp_163 && (_th_blink_bank_7 == 1)) begin
            _tmp_166 <= myram_1_0_rdata;
          end 
          if(_tmp_164 && (_th_blink_bank_7 == 2)) begin
            _tmp_166 <= myram_2_0_rdata;
          end 
          if(_tmp_165 && (_th_blink_bank_7 == 3)) begin
            _tmp_166 <= myram_3_0_rdata;
          end 
          if(_tmp_162) begin
            th_blink <= th_blink_87;
          end 
        end
        th_blink_87: begin
          _th_blink_rdata_12 <= _tmp_166;
          th_blink <= th_blink_88;
        end
        th_blink_88: begin
          if(_th_blink_rdata_12 !== _th_blink_bias_6 + _th_blink_i_8 + 1000) begin
            th_blink <= th_blink_89;
          end else begin
            th_blink <= th_blink_91;
          end
        end
        th_blink_89: begin
          $display("rdata[%d:%d] = %d", _th_blink_bank_7, _th_blink_i_8, _th_blink_rdata_12);
          th_blink <= th_blink_90;
        end
        th_blink_90: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_91;
        end
        th_blink_91: begin
          _th_blink_count_5 <= _th_blink_count_5 + 1;
          th_blink <= th_blink_92;
        end
        th_blink_92: begin
          _th_blink_i_8 <= _th_blink_i_8 + 1;
          th_blink <= th_blink_85;
        end
        th_blink_93: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 4;
          th_blink <= th_blink_94;
        end
        th_blink_94: begin
          _th_blink_bank_7 <= _th_blink_bank_7 + 1;
          th_blink <= th_blink_83;
        end
        th_blink_95: begin
          _th_blink_offset_4 <= _th_blink_offset_4 + 4;
          th_blink <= th_blink_96;
        end
        th_blink_96: begin
          th_blink <= th_blink_81;
        end
        th_blink_97: begin
          $display("# iter %d end", _th_blink_i_1);
          th_blink <= th_blink_98;
        end
        th_blink_98: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_99: begin
          if(_tmp_0) begin
            th_blink <= th_blink_100;
          end else begin
            th_blink <= th_blink_101;
          end
        end
        th_blink_100: begin
          $display("ALL OK");
          th_blink <= th_blink_101;
        end
      endcase
    end
  end

  localparam _tmp_fsm_0_1 = 1;
  localparam _tmp_fsm_0_2 = 2;
  localparam _tmp_fsm_0_3 = 3;
  localparam _tmp_fsm_0_4 = 4;
  localparam _tmp_fsm_0_5 = 5;
  localparam _tmp_fsm_0_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_0 <= _tmp_fsm_0_init;
      _d1__tmp_fsm_0 <= _tmp_fsm_0_init;
      _tmp_5 <= 0;
      _tmp_7 <= 0;
      _tmp_6 <= 0;
      _tmp_47 <= 0;
      __tmp_fsm_0_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_0_1) begin
            _tmp_47 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_blink == 26) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          _tmp_5 <= (_tmp_3 >> 4) << 4;
          _tmp_7 <= _tmp_4 >> 2;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          if((_tmp_7 <= 256) && ((_tmp_5 & 4095) + (_tmp_7 << 4) >= 4096)) begin
            _tmp_6 <= 4096 - (_tmp_5 & 4095) >> 4;
            _tmp_7 <= _tmp_7 - (4096 - (_tmp_5 & 4095) >> 4);
          end else if(_tmp_7 <= 256) begin
            _tmp_6 <= _tmp_7;
            _tmp_7 <= 0;
          end else if((_tmp_5 & 4095) + 4096 >= 4096) begin
            _tmp_6 <= 4096 - (_tmp_5 & 4095) >> 4;
            _tmp_7 <= _tmp_7 - (4096 - (_tmp_5 & 4095) >> 4);
          end else begin
            _tmp_6 <= 256;
            _tmp_7 <= _tmp_7 - 256;
          end
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_4;
          end 
        end
        _tmp_fsm_0_4: begin
          if(_tmp_45 && myaxi_wvalid && myaxi_wready) begin
            _tmp_5 <= _tmp_5 + (_tmp_6 << 4);
          end 
          if(_tmp_45 && myaxi_wvalid && myaxi_wready && (_tmp_7 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(_tmp_45 && myaxi_wvalid && myaxi_wready && (_tmp_7 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_47 <= 1;
          __tmp_fsm_0_cond_5_0_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_6;
        end
        _tmp_fsm_0_6: begin
          _tmp_fsm_0 <= _tmp_fsm_0_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_13_1 <= 0;
      __tmp_14_1 <= 0;
      __tmp_15_1 <= 0;
      __tmp_16_1 <= 0;
      __tmp_17_1 <= 0;
      __tmp_31_1 <= 0;
      _tmp_31 <= 0;
      _tmp_36 <= 0;
      _tmp_8 <= 0;
      _tmp_9 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_33 <= 0;
      _tmp_30 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      reg_addr_18 <= 0;
      reg_addr_19 <= 0;
      reg_addr_20 <= 0;
      reg_addr_21 <= 0;
      __tmp_60_1 <= 0;
      __tmp_61_1 <= 0;
      __tmp_62_1 <= 0;
      __tmp_63_1 <= 0;
      __tmp_64_1 <= 0;
      __tmp_78_1 <= 0;
      _tmp_78 <= 0;
      _tmp_83 <= 0;
      _tmp_55 <= 0;
      _tmp_56 <= 0;
      _tmp_81 <= 0;
      _tmp_82 <= 0;
      _tmp_80 <= 0;
      _tmp_77 <= 0;
      _tmp_84 <= 0;
      _tmp_85 <= 0;
      reg_addr_65 <= 0;
      reg_addr_66 <= 0;
      reg_addr_67 <= 0;
      reg_addr_68 <= 0;
      bank_sel_121 <= 0;
      block_counter_105 <= 0;
      _tmp_106 <= 0;
      reg_addr_109 <= 0;
      reg_addr_110 <= 0;
      reg_addr_111 <= 0;
      reg_addr_112 <= 0;
      _tmp_107 <= 0;
      _myram_cond_0_1 <= 0;
      bank_sel_157 <= 0;
      block_counter_141 <= 0;
      _tmp_142 <= 0;
      reg_addr_145 <= 0;
      reg_addr_146 <= 0;
      reg_addr_147 <= 0;
      reg_addr_148 <= 0;
      _tmp_143 <= 0;
      _myram_cond_1_1 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        _tmp_107 <= 0;
      end 
      if(_myram_cond_1_1) begin
        _tmp_143 <= 0;
      end 
      __tmp_13_1 <= _tmp_13;
      __tmp_14_1 <= _tmp_14;
      __tmp_15_1 <= _tmp_15;
      __tmp_16_1 <= _tmp_16;
      __tmp_17_1 <= _tmp_17;
      __tmp_31_1 <= _tmp_31;
      _tmp_31 <= _tmp_30;
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && _tmp_34) begin
        _tmp_36 <= 0;
        _tmp_8 <= 0;
        _tmp_9 <= 0;
        _tmp_34 <= 0;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && _tmp_33) begin
        _tmp_8 <= 1;
        _tmp_9 <= 1;
        _tmp_36 <= _tmp_35;
        _tmp_35 <= 0;
        _tmp_33 <= 0;
        _tmp_34 <= 1;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        _tmp_30 <= 0;
        _tmp_37 <= _tmp_1 - 1;
        _tmp_38 <= _tmp_4 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= _tmp_4 == 1;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        reg_addr_18 <= _tmp_2;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        reg_addr_19 <= _tmp_2;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        reg_addr_20 <= _tmp_2;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        reg_addr_21 <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0)) begin
        _tmp_37 <= _tmp_37 - 1;
        _tmp_38 <= _tmp_38 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= 0;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_37 == 0)) begin
        _tmp_37 <= _tmp_1 - 1;
        _tmp_30 <= _tmp_30 + 1;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_37 == 0) && (_tmp_30 == 3)) begin
        _tmp_30 <= 0;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 0)) begin
        reg_addr_18 <= next_addr_22;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 1)) begin
        reg_addr_19 <= next_addr_23;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 2)) begin
        reg_addr_20 <= next_addr_24;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 3)) begin
        reg_addr_21 <= next_addr_25;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 == 1)) begin
        _tmp_35 <= 1;
      end 
      __tmp_60_1 <= _tmp_60;
      __tmp_61_1 <= _tmp_61;
      __tmp_62_1 <= _tmp_62;
      __tmp_63_1 <= _tmp_63;
      __tmp_64_1 <= _tmp_64;
      __tmp_78_1 <= _tmp_78;
      _tmp_78 <= _tmp_77;
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && _tmp_81) begin
        _tmp_83 <= 0;
        _tmp_55 <= 0;
        _tmp_56 <= 0;
        _tmp_81 <= 0;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && _tmp_80) begin
        _tmp_55 <= 1;
        _tmp_56 <= 1;
        _tmp_83 <= _tmp_82;
        _tmp_82 <= 0;
        _tmp_80 <= 0;
        _tmp_81 <= 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        _tmp_77 <= 0;
        _tmp_84 <= _tmp_48 - 1;
        _tmp_85 <= _tmp_51 - 1;
        _tmp_80 <= 1;
        _tmp_82 <= _tmp_51 == 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        reg_addr_65 <= _tmp_49;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        reg_addr_66 <= _tmp_49;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        reg_addr_67 <= _tmp_49;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_85 == 0) && !_tmp_82 && !_tmp_83) begin
        reg_addr_68 <= _tmp_49;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0)) begin
        _tmp_84 <= _tmp_84 - 1;
        _tmp_85 <= _tmp_85 - 1;
        _tmp_80 <= 1;
        _tmp_82 <= 0;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_84 == 0)) begin
        _tmp_84 <= _tmp_48 - 1;
        _tmp_77 <= _tmp_77 + 1;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_84 == 0) && (_tmp_77 == 3)) begin
        _tmp_77 <= 0;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 0)) begin
        reg_addr_65 <= next_addr_69;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 1)) begin
        reg_addr_66 <= next_addr_70;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 2)) begin
        reg_addr_67 <= next_addr_71;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 > 0) && (_tmp_77 == 3)) begin
        reg_addr_68 <= next_addr_72;
      end 
      if((_tmp_57 || !_tmp_55) && (_tmp_58 || !_tmp_56) && (_tmp_85 == 1)) begin
        _tmp_82 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_106 == 0)) begin
        bank_sel_121 <= 0;
        block_counter_105 <= _tmp_95 - 1;
        _tmp_106 <= _tmp_98;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_106 == 0)) begin
        reg_addr_109 <= _tmp_96 - 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_106 == 0)) begin
        reg_addr_110 <= _tmp_96 - 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_106 == 0)) begin
        reg_addr_111 <= _tmp_96 - 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_106 == 0)) begin
        reg_addr_112 <= _tmp_96 - 1;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0)) begin
        block_counter_105 <= block_counter_105 - 1;
        _tmp_106 <= _tmp_106 - 1;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0) && (block_counter_105 == 0)) begin
        block_counter_105 <= _tmp_95 - 1;
        bank_sel_121 <= bank_sel_121 + 1;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0) && (block_counter_105 == 0) && (bank_sel_121 == 3)) begin
        bank_sel_121 <= 0;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0) && (bank_sel_121 == 0)) begin
        reg_addr_109 <= next_addr_113;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0) && (bank_sel_121 == 1)) begin
        reg_addr_110 <= next_addr_114;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0) && (bank_sel_121 == 2)) begin
        reg_addr_111 <= next_addr_115;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 > 0) && (bank_sel_121 == 3)) begin
        reg_addr_112 <= next_addr_116;
      end 
      if(__variable_valid_108 && ((_tmp_106 > 0) && !_tmp_107) && (_tmp_106 == 1)) begin
        _tmp_107 <= 1;
      end 
      _myram_cond_0_1 <= 1;
      if((_tmp_fsm_3 == 1) && (_tmp_142 == 0)) begin
        bank_sel_157 <= 0;
        block_counter_141 <= _tmp_131 - 1;
        _tmp_142 <= _tmp_134;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_142 == 0)) begin
        reg_addr_145 <= _tmp_132 - 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_142 == 0)) begin
        reg_addr_146 <= _tmp_132 - 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_142 == 0)) begin
        reg_addr_147 <= _tmp_132 - 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_142 == 0)) begin
        reg_addr_148 <= _tmp_132 - 1;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0)) begin
        block_counter_141 <= block_counter_141 - 1;
        _tmp_142 <= _tmp_142 - 1;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0) && (block_counter_141 == 0)) begin
        block_counter_141 <= _tmp_131 - 1;
        bank_sel_157 <= bank_sel_157 + 1;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0) && (block_counter_141 == 0) && (bank_sel_157 == 3)) begin
        bank_sel_157 <= 0;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0) && (bank_sel_157 == 0)) begin
        reg_addr_145 <= next_addr_149;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0) && (bank_sel_157 == 1)) begin
        reg_addr_146 <= next_addr_150;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0) && (bank_sel_157 == 2)) begin
        reg_addr_147 <= next_addr_151;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 > 0) && (bank_sel_157 == 3)) begin
        reg_addr_148 <= next_addr_152;
      end 
      if(__variable_valid_144 && ((_tmp_142 > 0) && !_tmp_143) && (_tmp_142 == 1)) begin
        _tmp_143 <= 1;
      end 
      _myram_cond_1_1 <= 1;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_41 <= 0;
      _tmp_40 <= 0;
      _tmp_43 <= 0;
    end else begin
      if(_tmp_42 || !_tmp_41) begin
        _tmp_41 <= 0;
      end 
      if(__variable_valid_44 && ((_tmp_fsm_0 == 4) && (_tmp_42 || !_tmp_41))) begin
        _tmp_40 <= { __variable_data_44, _tmp_40[127:32] };
        _tmp_41 <= 0;
        _tmp_43 <= _tmp_43 + 1;
      end 
      if(__variable_valid_44 && ((_tmp_fsm_0 == 4) && (_tmp_42 || !_tmp_41)) && (_tmp_43 == 3)) begin
        _tmp_40 <= { __variable_data_44, _tmp_40[127:32] };
        _tmp_41 <= 1;
        _tmp_43 <= 0;
      end 
    end
  end

  localparam _tmp_fsm_1_1 = 1;
  localparam _tmp_fsm_1_2 = 2;
  localparam _tmp_fsm_1_3 = 3;
  localparam _tmp_fsm_1_4 = 4;
  localparam _tmp_fsm_1_5 = 5;
  localparam _tmp_fsm_1_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_1 <= _tmp_fsm_1_init;
      _d1__tmp_fsm_1 <= _tmp_fsm_1_init;
      _tmp_52 <= 0;
      _tmp_54 <= 0;
      _tmp_53 <= 0;
      _tmp_94 <= 0;
      __tmp_fsm_1_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_0_1) begin
            _tmp_94 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_blink == 47) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_52 <= (_tmp_50 >> 4) << 4;
          _tmp_54 <= _tmp_51 >> 2;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_54 <= 256) && ((_tmp_52 & 4095) + (_tmp_54 << 4) >= 4096)) begin
            _tmp_53 <= 4096 - (_tmp_52 & 4095) >> 4;
            _tmp_54 <= _tmp_54 - (4096 - (_tmp_52 & 4095) >> 4);
          end else if(_tmp_54 <= 256) begin
            _tmp_53 <= _tmp_54;
            _tmp_54 <= 0;
          end else if((_tmp_52 & 4095) + 4096 >= 4096) begin
            _tmp_53 <= 4096 - (_tmp_52 & 4095) >> 4;
            _tmp_54 <= _tmp_54 - (4096 - (_tmp_52 & 4095) >> 4);
          end else begin
            _tmp_53 <= 256;
            _tmp_54 <= _tmp_54 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          if(_tmp_92 && myaxi_wvalid && myaxi_wready) begin
            _tmp_52 <= _tmp_52 + (_tmp_53 << 4);
          end 
          if(_tmp_92 && myaxi_wvalid && myaxi_wready && (_tmp_54 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(_tmp_92 && myaxi_wvalid && myaxi_wready && (_tmp_54 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_94 <= 1;
          __tmp_fsm_1_cond_5_0_1 <= 1;
          _tmp_fsm_1 <= _tmp_fsm_1_6;
        end
        _tmp_fsm_1_6: begin
          _tmp_fsm_1 <= _tmp_fsm_1_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_88 <= 0;
      _tmp_87 <= 0;
      _tmp_90 <= 0;
    end else begin
      if(_tmp_89 || !_tmp_88) begin
        _tmp_88 <= 0;
      end 
      if(__variable_valid_91 && ((_tmp_fsm_1 == 4) && (_tmp_89 || !_tmp_88))) begin
        _tmp_87 <= { __variable_data_91, _tmp_87[127:32] };
        _tmp_88 <= 0;
        _tmp_90 <= _tmp_90 + 1;
      end 
      if(__variable_valid_91 && ((_tmp_fsm_1 == 4) && (_tmp_89 || !_tmp_88)) && (_tmp_90 == 3)) begin
        _tmp_87 <= { __variable_data_91, _tmp_87[127:32] };
        _tmp_88 <= 1;
        _tmp_90 <= 0;
      end 
    end
  end

  localparam _tmp_fsm_2_1 = 1;
  localparam _tmp_fsm_2_2 = 2;
  localparam _tmp_fsm_2_3 = 3;
  localparam _tmp_fsm_2_4 = 4;
  localparam _tmp_fsm_2_5 = 5;
  localparam _tmp_fsm_2_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_2 <= _tmp_fsm_2_init;
      _d1__tmp_fsm_2 <= _tmp_fsm_2_init;
      _tmp_99 <= 0;
      _tmp_101 <= 0;
      _tmp_122 <= 0;
      _tmp_100 <= 0;
      __tmp_fsm_2_cond_4_0_1 <= 0;
      _tmp_104 <= 0;
      _tmp_102 <= 0;
      _tmp_124 <= 0;
      _tmp_125 <= 0;
      __tmp_fsm_2_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_0_1) begin
            _tmp_104 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_1_1) begin
            _tmp_125 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_blink == 52) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_99 <= (_tmp_97 >> 4) << 4;
          _tmp_101 <= _tmp_98 >> 2;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          _tmp_122 <= 0;
          if((_tmp_101 <= 256) && ((_tmp_99 & 4095) + (_tmp_101 << 4) >= 4096)) begin
            _tmp_100 <= 4096 - (_tmp_99 & 4095) >> 4;
            _tmp_101 <= _tmp_101 - (4096 - (_tmp_99 & 4095) >> 4);
          end else if(_tmp_101 <= 256) begin
            _tmp_100 <= _tmp_101;
            _tmp_101 <= 0;
          end else if((_tmp_99 & 4095) + 4096 >= 4096) begin
            _tmp_100 <= 4096 - (_tmp_99 & 4095) >> 4;
            _tmp_101 <= _tmp_101 - (4096 - (_tmp_99 & 4095) >> 4);
          end else begin
            _tmp_100 <= 256;
            _tmp_101 <= _tmp_101 - 256;
          end
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_4;
          end 
        end
        _tmp_fsm_2_4: begin
          __tmp_fsm_2_cond_4_0_1 <= 1;
          if((_tmp_124 == 0) && (myaxi_rready && myaxi_rvalid) && myaxi_rlast) begin
            _tmp_122 <= 1;
          end 
          if((_tmp_124 == 0) && (myaxi_rready && myaxi_rvalid)) begin
            _tmp_102 <= myaxi_rdata;
            _tmp_104 <= 1;
            _tmp_124 <= _tmp_124 + 1;
          end 
          if(_tmp_124 > 0) begin
            _tmp_102 <= _tmp_102 >> 32;
            _tmp_104 <= 1;
            _tmp_124 <= _tmp_124 + 1;
          end 
          if(_tmp_124 == 3) begin
            _tmp_124 <= 0;
          end 
          if(_tmp_122 && (_tmp_124 == 3)) begin
            _tmp_99 <= _tmp_99 + (_tmp_100 << 4);
          end 
          if(_tmp_122 && (_tmp_124 == 3) && (_tmp_101 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(_tmp_122 && (_tmp_124 == 3) && (_tmp_101 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_125 <= 1;
          __tmp_fsm_2_cond_5_1_1 <= 1;
          _tmp_fsm_2 <= _tmp_fsm_2_6;
        end
        _tmp_fsm_2_6: begin
          _tmp_fsm_2 <= _tmp_fsm_2_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_3_1 = 1;
  localparam _tmp_fsm_3_2 = 2;
  localparam _tmp_fsm_3_3 = 3;
  localparam _tmp_fsm_3_4 = 4;
  localparam _tmp_fsm_3_5 = 5;
  localparam _tmp_fsm_3_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_3 <= _tmp_fsm_3_init;
      _d1__tmp_fsm_3 <= _tmp_fsm_3_init;
      _tmp_135 <= 0;
      _tmp_137 <= 0;
      _tmp_158 <= 0;
      _tmp_136 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_140 <= 0;
      _tmp_138 <= 0;
      _tmp_160 <= 0;
      _tmp_161 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_140 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_161 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_blink == 76) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_135 <= (_tmp_133 >> 4) << 4;
          _tmp_137 <= _tmp_134 >> 2;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          _tmp_158 <= 0;
          if((_tmp_137 <= 256) && ((_tmp_135 & 4095) + (_tmp_137 << 4) >= 4096)) begin
            _tmp_136 <= 4096 - (_tmp_135 & 4095) >> 4;
            _tmp_137 <= _tmp_137 - (4096 - (_tmp_135 & 4095) >> 4);
          end else if(_tmp_137 <= 256) begin
            _tmp_136 <= _tmp_137;
            _tmp_137 <= 0;
          end else if((_tmp_135 & 4095) + 4096 >= 4096) begin
            _tmp_136 <= 4096 - (_tmp_135 & 4095) >> 4;
            _tmp_137 <= _tmp_137 - (4096 - (_tmp_135 & 4095) >> 4);
          end else begin
            _tmp_136 <= 256;
            _tmp_137 <= _tmp_137 - 256;
          end
          _tmp_fsm_3 <= _tmp_fsm_3_3;
        end
        _tmp_fsm_3_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_3 <= _tmp_fsm_3_4;
          end 
        end
        _tmp_fsm_3_4: begin
          __tmp_fsm_3_cond_4_0_1 <= 1;
          if((_tmp_160 == 0) && (myaxi_rready && myaxi_rvalid) && myaxi_rlast) begin
            _tmp_158 <= 1;
          end 
          if((_tmp_160 == 0) && (myaxi_rready && myaxi_rvalid)) begin
            _tmp_138 <= myaxi_rdata;
            _tmp_140 <= 1;
            _tmp_160 <= _tmp_160 + 1;
          end 
          if(_tmp_160 > 0) begin
            _tmp_138 <= _tmp_138 >> 32;
            _tmp_140 <= 1;
            _tmp_160 <= _tmp_160 + 1;
          end 
          if(_tmp_160 == 3) begin
            _tmp_160 <= 0;
          end 
          if(_tmp_158 && (_tmp_160 == 3)) begin
            _tmp_135 <= _tmp_135 + (_tmp_136 << 4);
          end 
          if(_tmp_158 && (_tmp_160 == 3) && (_tmp_137 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(_tmp_158 && (_tmp_160 == 3) && (_tmp_137 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_161 <= 1;
          __tmp_fsm_3_cond_5_1_1 <= 1;
          _tmp_fsm_3 <= _tmp_fsm_3_6;
        end
        _tmp_fsm_3_6: begin
          _tmp_fsm_3 <= _tmp_fsm_3_init;
        end
      endcase
    end
  end


endmodule



module myram_0
(
  input CLK,
  input [10-1:0] myram_0_0_addr,
  output [32-1:0] myram_0_0_rdata,
  input [32-1:0] myram_0_0_wdata,
  input myram_0_0_wenable
);

  reg [10-1:0] myram_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_0_wenable) begin
      mem[myram_0_0_addr] <= myram_0_0_wdata;
    end 
    myram_0_0_daddr <= myram_0_0_addr;
  end

  assign myram_0_0_rdata = mem[myram_0_0_daddr];

endmodule



module myram_1
(
  input CLK,
  input [10-1:0] myram_1_0_addr,
  output [32-1:0] myram_1_0_rdata,
  input [32-1:0] myram_1_0_wdata,
  input myram_1_0_wenable
);

  reg [10-1:0] myram_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_1_0_wenable) begin
      mem[myram_1_0_addr] <= myram_1_0_wdata;
    end 
    myram_1_0_daddr <= myram_1_0_addr;
  end

  assign myram_1_0_rdata = mem[myram_1_0_daddr];

endmodule



module myram_2
(
  input CLK,
  input [10-1:0] myram_2_0_addr,
  output [32-1:0] myram_2_0_rdata,
  input [32-1:0] myram_2_0_wdata,
  input myram_2_0_wenable
);

  reg [10-1:0] myram_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_2_0_wenable) begin
      mem[myram_2_0_addr] <= myram_2_0_wdata;
    end 
    myram_2_0_daddr <= myram_2_0_addr;
  end

  assign myram_2_0_rdata = mem[myram_2_0_daddr];

endmodule



module myram_3
(
  input CLK,
  input [10-1:0] myram_3_0_addr,
  output [32-1:0] myram_3_0_rdata,
  input [32-1:0] myram_3_0_wdata,
  input myram_3_0_wenable
);

  reg [10-1:0] myram_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_3_0_wenable) begin
      mem[myram_3_0_addr] <= myram_3_0_wdata;
    end 
    myram_3_0_daddr <= myram_3_0_addr;
  end

  assign myram_3_0_rdata = mem[myram_3_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_multibank_ram_dma_block.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
