from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_multibank

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
    myaxi_rdata = memory_rdata;
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
  reg [10-1:0] ram_a_0_0_addr;
  wire [32-1:0] ram_a_0_0_rdata;
  reg [32-1:0] ram_a_0_0_wdata;
  reg ram_a_0_0_wenable;

  ram_a_0
  inst_ram_a_0
  (
    .CLK(CLK),
    .ram_a_0_0_addr(ram_a_0_0_addr),
    .ram_a_0_0_rdata(ram_a_0_0_rdata),
    .ram_a_0_0_wdata(ram_a_0_0_wdata),
    .ram_a_0_0_wenable(ram_a_0_0_wenable)
  );

  reg [10-1:0] ram_a_1_0_addr;
  wire [32-1:0] ram_a_1_0_rdata;
  reg [32-1:0] ram_a_1_0_wdata;
  reg ram_a_1_0_wenable;

  ram_a_1
  inst_ram_a_1
  (
    .CLK(CLK),
    .ram_a_1_0_addr(ram_a_1_0_addr),
    .ram_a_1_0_rdata(ram_a_1_0_rdata),
    .ram_a_1_0_wdata(ram_a_1_0_wdata),
    .ram_a_1_0_wenable(ram_a_1_0_wenable)
  );

  reg [10-1:0] ram_a_2_0_addr;
  wire [32-1:0] ram_a_2_0_rdata;
  reg [32-1:0] ram_a_2_0_wdata;
  reg ram_a_2_0_wenable;

  ram_a_2
  inst_ram_a_2
  (
    .CLK(CLK),
    .ram_a_2_0_addr(ram_a_2_0_addr),
    .ram_a_2_0_rdata(ram_a_2_0_rdata),
    .ram_a_2_0_wdata(ram_a_2_0_wdata),
    .ram_a_2_0_wenable(ram_a_2_0_wenable)
  );

  reg [10-1:0] ram_a_3_0_addr;
  wire [32-1:0] ram_a_3_0_rdata;
  reg [32-1:0] ram_a_3_0_wdata;
  reg ram_a_3_0_wenable;

  ram_a_3
  inst_ram_a_3
  (
    .CLK(CLK),
    .ram_a_3_0_addr(ram_a_3_0_addr),
    .ram_a_3_0_rdata(ram_a_3_0_rdata),
    .ram_a_3_0_wdata(ram_a_3_0_wdata),
    .ram_a_3_0_wenable(ram_a_3_0_wenable)
  );

  reg [10-1:0] ram_b_0_0_addr;
  wire [32-1:0] ram_b_0_0_rdata;
  reg [32-1:0] ram_b_0_0_wdata;
  reg ram_b_0_0_wenable;

  ram_b_0
  inst_ram_b_0
  (
    .CLK(CLK),
    .ram_b_0_0_addr(ram_b_0_0_addr),
    .ram_b_0_0_rdata(ram_b_0_0_rdata),
    .ram_b_0_0_wdata(ram_b_0_0_wdata),
    .ram_b_0_0_wenable(ram_b_0_0_wenable)
  );

  reg [10-1:0] ram_b_1_0_addr;
  wire [32-1:0] ram_b_1_0_rdata;
  reg [32-1:0] ram_b_1_0_wdata;
  reg ram_b_1_0_wenable;

  ram_b_1
  inst_ram_b_1
  (
    .CLK(CLK),
    .ram_b_1_0_addr(ram_b_1_0_addr),
    .ram_b_1_0_rdata(ram_b_1_0_rdata),
    .ram_b_1_0_wdata(ram_b_1_0_wdata),
    .ram_b_1_0_wenable(ram_b_1_0_wenable)
  );

  reg [10-1:0] ram_b_2_0_addr;
  wire [32-1:0] ram_b_2_0_rdata;
  reg [32-1:0] ram_b_2_0_wdata;
  reg ram_b_2_0_wenable;

  ram_b_2
  inst_ram_b_2
  (
    .CLK(CLK),
    .ram_b_2_0_addr(ram_b_2_0_addr),
    .ram_b_2_0_rdata(ram_b_2_0_rdata),
    .ram_b_2_0_wdata(ram_b_2_0_wdata),
    .ram_b_2_0_wenable(ram_b_2_0_wenable)
  );

  reg [10-1:0] ram_b_3_0_addr;
  wire [32-1:0] ram_b_3_0_rdata;
  reg [32-1:0] ram_b_3_0_wdata;
  reg ram_b_3_0_wenable;

  ram_b_3
  inst_ram_b_3
  (
    .CLK(CLK),
    .ram_b_3_0_addr(ram_b_3_0_addr),
    .ram_b_3_0_rdata(ram_b_3_0_rdata),
    .ram_b_3_0_wdata(ram_b_3_0_wdata),
    .ram_b_3_0_wenable(ram_b_3_0_wenable)
  );

  reg [10-1:0] ram_c_0_0_addr;
  wire [32-1:0] ram_c_0_0_rdata;
  reg [32-1:0] ram_c_0_0_wdata;
  reg ram_c_0_0_wenable;

  ram_c_0
  inst_ram_c_0
  (
    .CLK(CLK),
    .ram_c_0_0_addr(ram_c_0_0_addr),
    .ram_c_0_0_rdata(ram_c_0_0_rdata),
    .ram_c_0_0_wdata(ram_c_0_0_wdata),
    .ram_c_0_0_wenable(ram_c_0_0_wenable)
  );

  reg [10-1:0] ram_c_1_0_addr;
  wire [32-1:0] ram_c_1_0_rdata;
  reg [32-1:0] ram_c_1_0_wdata;
  reg ram_c_1_0_wenable;

  ram_c_1
  inst_ram_c_1
  (
    .CLK(CLK),
    .ram_c_1_0_addr(ram_c_1_0_addr),
    .ram_c_1_0_rdata(ram_c_1_0_rdata),
    .ram_c_1_0_wdata(ram_c_1_0_wdata),
    .ram_c_1_0_wenable(ram_c_1_0_wenable)
  );

  reg [10-1:0] ram_c_2_0_addr;
  wire [32-1:0] ram_c_2_0_rdata;
  reg [32-1:0] ram_c_2_0_wdata;
  reg ram_c_2_0_wenable;

  ram_c_2
  inst_ram_c_2
  (
    .CLK(CLK),
    .ram_c_2_0_addr(ram_c_2_0_addr),
    .ram_c_2_0_rdata(ram_c_2_0_rdata),
    .ram_c_2_0_wdata(ram_c_2_0_wdata),
    .ram_c_2_0_wenable(ram_c_2_0_wenable)
  );

  reg [10-1:0] ram_c_3_0_addr;
  wire [32-1:0] ram_c_3_0_rdata;
  reg [32-1:0] ram_c_3_0_wdata;
  reg ram_c_3_0_wenable;

  ram_c_3
  inst_ram_c_3
  (
    .CLK(CLK),
    .ram_c_3_0_addr(ram_c_3_0_addr),
    .ram_c_3_0_rdata(ram_c_3_0_rdata),
    .ram_c_3_0_wdata(ram_c_3_0_wdata),
    .ram_c_3_0_wenable(ram_c_3_0_wenable)
  );

  reg [32-1:0] _mystream_fsm;
  localparam _mystream_fsm_init = 0;
  wire _mystream_start_flag;
  reg _mystream_start;
  reg _mystream_busy;
  reg _mystream_a_idle;
  reg [3-1:0] _mystream_a_source_mode;
  reg [32-1:0] _mystream_a_source_offset;
  reg [33-1:0] _mystream_a_source_size;
  reg [32-1:0] _mystream_a_source_stride;
  reg [33-1:0] _mystream_a_source_count;
  reg [8-1:0] _mystream_a_source_ram_sel;
  reg [32-1:0] _mystream_a_source_ram_raddr;
  reg _mystream_a_source_ram_renable;
  wire [32-1:0] _mystream_a_source_ram_rdata;
  reg _mystream_a_source_ram_rvalid;
  reg _mystream_b_idle;
  reg [3-1:0] _mystream_b_source_mode;
  reg [32-1:0] _mystream_b_source_offset;
  reg [33-1:0] _mystream_b_source_size;
  reg [32-1:0] _mystream_b_source_stride;
  reg [33-1:0] _mystream_b_source_count;
  reg [8-1:0] _mystream_b_source_ram_sel;
  reg [32-1:0] _mystream_b_source_ram_raddr;
  reg _mystream_b_source_ram_renable;
  wire [32-1:0] _mystream_b_source_ram_rdata;
  reg _mystream_b_source_ram_rvalid;
  reg [3-1:0] _mystream_c_sink_mode;
  reg [32-1:0] _mystream_c_sink_offset;
  reg [33-1:0] _mystream_c_sink_size;
  reg [32-1:0] _mystream_c_sink_stride;
  reg [33-1:0] _mystream_c_sink_count;
  reg [8-1:0] _mystream_c_sink_ram_sel;
  reg [32-1:0] _mystream_c_sink_waddr;
  reg _mystream_c_sink_wenable;
  reg [32-1:0] _mystream_c_sink_wdata;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_0;
  reg signed [32-1:0] _th_comp_dma_size_1;
  reg signed [32-1:0] _th_comp_comp_size_2;
  reg signed [32-1:0] _th_comp_dma_offset_3;
  reg signed [32-1:0] _th_comp_comp_offset_4;
  reg axim_flag_0;
  reg [32-1:0] _d1_th_comp;
  reg _th_comp_cond_5_0_1;
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
  reg [128-1:0] _wdata_1;
  reg _wvalid_2;
  reg [34-1:0] _tmp_3;
  reg _tmp_4;
  wire [32-1:0] _slice_data_5;
  wire _slice_valid_5;
  wire _slice_ready_5;
  assign _slice_ready_5 = (_tmp_3 > 0) && !_tmp_4;
  reg _ram_a_0_cond_0_1;
  reg [34-1:0] _tmp_6;
  reg _tmp_7;
  wire [32-1:0] _slice_data_8;
  wire _slice_valid_8;
  wire _slice_ready_8;
  assign _slice_ready_8 = (_tmp_6 > 0) && !_tmp_7;
  reg _ram_a_1_cond_0_1;
  reg [34-1:0] _tmp_9;
  reg _tmp_10;
  wire [32-1:0] _slice_data_11;
  wire _slice_valid_11;
  wire _slice_ready_11;
  assign _slice_ready_11 = (_tmp_9 > 0) && !_tmp_10;
  reg _ram_a_2_cond_0_1;
  reg [34-1:0] _tmp_12;
  reg _tmp_13;
  wire [32-1:0] _slice_data_14;
  wire _slice_valid_14;
  wire _slice_ready_14;
  assign _slice_ready_14 = (_tmp_12 > 0) && !_tmp_13;
  reg _ram_a_3_cond_0_1;
  reg [9-1:0] _tmp_15;
  reg _myaxi_cond_0_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_16;
  reg __myaxi_read_fsm_cond_4_1_1;
  reg axim_flag_17;
  reg _th_comp_cond_9_1_1;
  reg _myaxi_ram_b_0_read_start;
  reg [8-1:0] _myaxi_ram_b_0_read_op_sel;
  reg [32-1:0] _myaxi_ram_b_0_read_local_addr;
  reg [32-1:0] _myaxi_ram_b_0_read_global_addr;
  reg [33-1:0] _myaxi_ram_b_0_read_size;
  reg [32-1:0] _myaxi_ram_b_0_read_local_stride;
  reg [128-1:0] _wdata_18;
  reg _wvalid_19;
  reg [34-1:0] _tmp_20;
  reg _tmp_21;
  wire [32-1:0] _slice_data_22;
  wire _slice_valid_22;
  wire _slice_ready_22;
  assign _slice_ready_22 = (_tmp_20 > 0) && !_tmp_21;
  reg _ram_b_0_cond_0_1;
  reg [34-1:0] _tmp_23;
  reg _tmp_24;
  wire [32-1:0] _slice_data_25;
  wire _slice_valid_25;
  wire _slice_ready_25;
  assign _slice_ready_25 = (_tmp_23 > 0) && !_tmp_24;
  reg _ram_b_1_cond_0_1;
  reg [34-1:0] _tmp_26;
  reg _tmp_27;
  wire [32-1:0] _slice_data_28;
  wire _slice_valid_28;
  wire _slice_ready_28;
  assign _slice_ready_28 = (_tmp_26 > 0) && !_tmp_27;
  reg _ram_b_2_cond_0_1;
  reg [34-1:0] _tmp_29;
  reg _tmp_30;
  wire [32-1:0] _slice_data_31;
  wire _slice_valid_31;
  wire _slice_ready_31;
  assign _slice_ready_31 = (_tmp_29 > 0) && !_tmp_30;
  reg _ram_b_3_cond_0_1;
  reg __myaxi_read_fsm_cond_3_2_1;
  reg signed [32-1:0] _th_comp_size_5;
  reg signed [32-1:0] _th_comp_offset_6;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  reg signed [32-1:0] _plus_data_2;
  wire signed [32-1:0] mystream_c_data;
  assign mystream_c_data = _plus_data_2;
  reg _set_flag_32;
  wire [2-1:0] _tmp_33;
  assign _tmp_33 = _mystream_a_source_ram_raddr;
  reg [2-1:0] __tmp_33_1;
  reg [2-1:0] __tmp_33_2;
  reg _tmp_34;
  reg _ram_a_0_cond_1_1;
  reg _ram_a_0_cond_2_1;
  reg _ram_a_0_cond_2_2;
  reg _tmp_35;
  reg _ram_a_1_cond_1_1;
  reg _ram_a_1_cond_2_1;
  reg _ram_a_1_cond_2_2;
  reg _tmp_36;
  reg _ram_a_2_cond_1_1;
  reg _ram_a_2_cond_2_1;
  reg _ram_a_2_cond_2_2;
  reg _tmp_37;
  reg _ram_a_3_cond_1_1;
  reg _ram_a_3_cond_2_1;
  reg _ram_a_3_cond_2_2;
  wire signed [32-1:0] _tmp_38;
  wire _tmp_39;
  assign _tmp_38 = (__tmp_33_2 == 0)? ram_a_0_0_rdata : 
                   (__tmp_33_2 == 1)? ram_a_1_0_rdata : 
                   (__tmp_33_2 == 2)? ram_a_2_0_rdata : 
                   (__tmp_33_2 == 3)? ram_a_3_0_rdata : 0;
  assign _tmp_39 = _tmp_34;
  assign _mystream_a_source_ram_rdata = (_mystream_a_source_ram_sel == 1)? _tmp_38 : 0;
  localparam _tmp_40 = 1;
  wire [_tmp_40-1:0] _tmp_41;
  assign _tmp_41 = _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
  reg [_tmp_40-1:0] __tmp_41_1;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_a_source_fsm_0;
  localparam _mystream_a_source_fsm_0_init = 0;
  reg _set_flag_42;
  wire [2-1:0] _tmp_43;
  assign _tmp_43 = _mystream_b_source_ram_raddr;
  reg [2-1:0] __tmp_43_1;
  reg [2-1:0] __tmp_43_2;
  reg _tmp_44;
  reg _ram_b_0_cond_1_1;
  reg _ram_b_0_cond_2_1;
  reg _ram_b_0_cond_2_2;
  reg _tmp_45;
  reg _ram_b_1_cond_1_1;
  reg _ram_b_1_cond_2_1;
  reg _ram_b_1_cond_2_2;
  reg _tmp_46;
  reg _ram_b_2_cond_1_1;
  reg _ram_b_2_cond_2_1;
  reg _ram_b_2_cond_2_2;
  reg _tmp_47;
  reg _ram_b_3_cond_1_1;
  reg _ram_b_3_cond_2_1;
  reg _ram_b_3_cond_2_2;
  wire signed [32-1:0] _tmp_48;
  wire _tmp_49;
  assign _tmp_48 = (__tmp_43_2 == 0)? ram_b_0_0_rdata : 
                   (__tmp_43_2 == 1)? ram_b_1_0_rdata : 
                   (__tmp_43_2 == 2)? ram_b_2_0_rdata : 
                   (__tmp_43_2 == 3)? ram_b_3_0_rdata : 0;
  assign _tmp_49 = _tmp_44;
  assign _mystream_b_source_ram_rdata = (_mystream_b_source_ram_sel == 2)? _tmp_48 : 0;
  localparam _tmp_50 = 1;
  wire [_tmp_50-1:0] _tmp_51;
  assign _tmp_51 = _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
  reg [_tmp_50-1:0] __tmp_51_1;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_b_data = __variable_wdata_1;
  reg [32-1:0] _mystream_b_source_fsm_1;
  localparam _mystream_b_source_fsm_1_init = 0;
  reg _set_flag_52;
  wire [2-1:0] _tmp_53;
  assign _tmp_53 = _mystream_c_sink_waddr;
  reg _ram_c_0_cond_0_1;
  reg _ram_c_1_cond_0_1;
  reg _ram_c_2_cond_0_1;
  reg _ram_c_3_cond_0_1;
  reg [32-1:0] _mystream_c_sink_fsm_2;
  localparam _mystream_c_sink_fsm_2_init = 0;
  reg _set_flag_54;
  assign _mystream_start_flag = (_set_flag_54)? 1 : 0;
  wire _mystream_done;
  assign _mystream_done = _mystream_a_idle && _mystream_b_idle;
  reg axim_flag_55;
  reg _th_comp_cond_20_2_1;
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
  reg _tmp_56;
  reg _tmp_57;
  wire _tmp_58;
  wire _tmp_59;
  assign _tmp_59 = 1;
  localparam _tmp_60 = 1;
  wire [_tmp_60-1:0] _tmp_61;
  assign _tmp_61 = (_tmp_58 || !_tmp_56) && (_tmp_59 || !_tmp_57);
  reg [_tmp_60-1:0] __tmp_61_1;
  wire signed [32-1:0] _tmp_62;
  reg signed [32-1:0] __tmp_62_1;
  assign _tmp_62 = (__tmp_61_1)? ram_c_0_0_rdata : __tmp_62_1;
  reg _tmp_63;
  reg _tmp_64;
  reg _tmp_65;
  reg _tmp_66;
  reg [34-1:0] _tmp_67;
  reg _tmp_68;
  reg _tmp_69;
  wire _tmp_70;
  wire _tmp_71;
  assign _tmp_71 = 1;
  localparam _tmp_72 = 1;
  wire [_tmp_72-1:0] _tmp_73;
  assign _tmp_73 = (_tmp_70 || !_tmp_68) && (_tmp_71 || !_tmp_69);
  reg [_tmp_72-1:0] __tmp_73_1;
  wire signed [32-1:0] _tmp_74;
  reg signed [32-1:0] __tmp_74_1;
  assign _tmp_74 = (__tmp_73_1)? ram_c_1_0_rdata : __tmp_74_1;
  reg _tmp_75;
  reg _tmp_76;
  reg _tmp_77;
  reg _tmp_78;
  reg [34-1:0] _tmp_79;
  reg _tmp_80;
  reg _tmp_81;
  wire _tmp_82;
  wire _tmp_83;
  assign _tmp_83 = 1;
  localparam _tmp_84 = 1;
  wire [_tmp_84-1:0] _tmp_85;
  assign _tmp_85 = (_tmp_82 || !_tmp_80) && (_tmp_83 || !_tmp_81);
  reg [_tmp_84-1:0] __tmp_85_1;
  wire signed [32-1:0] _tmp_86;
  reg signed [32-1:0] __tmp_86_1;
  assign _tmp_86 = (__tmp_85_1)? ram_c_2_0_rdata : __tmp_86_1;
  reg _tmp_87;
  reg _tmp_88;
  reg _tmp_89;
  reg _tmp_90;
  reg [34-1:0] _tmp_91;
  reg _tmp_92;
  reg _tmp_93;
  wire _tmp_94;
  wire _tmp_95;
  assign _tmp_95 = 1;
  localparam _tmp_96 = 1;
  wire [_tmp_96-1:0] _tmp_97;
  assign _tmp_97 = (_tmp_94 || !_tmp_92) && (_tmp_95 || !_tmp_93);
  reg [_tmp_96-1:0] __tmp_97_1;
  wire signed [32-1:0] _tmp_98;
  reg signed [32-1:0] __tmp_98_1;
  assign _tmp_98 = (__tmp_97_1)? ram_c_3_0_rdata : __tmp_98_1;
  reg _tmp_99;
  reg _tmp_100;
  reg _tmp_101;
  reg _tmp_102;
  reg [34-1:0] _tmp_103;
  reg [9-1:0] _tmp_104;
  reg _myaxi_cond_1_1;
  reg _tmp_105;
  wire [128-1:0] _cat_data_106;
  wire _cat_valid_106;
  wire _cat_ready_106;
  assign _cat_ready_106 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_104 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  assign _myaxi_write_data_done = (_tmp_105 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_107;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg axim_flag_108;
  reg _th_comp_cond_26_3_1;
  reg axim_flag_109;
  reg _th_comp_cond_30_4_1;
  reg signed [32-1:0] _th_comp_size_7;
  reg signed [32-1:0] _th_comp_offset_8;
  reg signed [32-1:0] _th_comp_sum_9;
  reg signed [32-1:0] _th_comp_i_10;
  wire [2-1:0] _tmp_110;
  assign _tmp_110 = _th_comp_i_10 + _th_comp_offset_8;
  reg _tmp_111;
  reg _ram_a_0_cond_3_1;
  reg _ram_a_0_cond_4_1;
  reg _ram_a_0_cond_4_2;
  reg _tmp_112;
  reg _ram_a_1_cond_3_1;
  reg _ram_a_1_cond_4_1;
  reg _ram_a_1_cond_4_2;
  reg _tmp_113;
  reg _ram_a_2_cond_3_1;
  reg _ram_a_2_cond_4_1;
  reg _ram_a_2_cond_4_2;
  reg _tmp_114;
  reg _ram_a_3_cond_3_1;
  reg _ram_a_3_cond_4_1;
  reg _ram_a_3_cond_4_2;
  reg signed [32-1:0] _tmp_115;
  reg signed [32-1:0] _th_comp_a_11;
  wire [2-1:0] _tmp_116;
  assign _tmp_116 = _th_comp_i_10 + _th_comp_offset_8;
  reg _tmp_117;
  reg _ram_b_0_cond_3_1;
  reg _ram_b_0_cond_4_1;
  reg _ram_b_0_cond_4_2;
  reg _tmp_118;
  reg _ram_b_1_cond_3_1;
  reg _ram_b_1_cond_4_1;
  reg _ram_b_1_cond_4_2;
  reg _tmp_119;
  reg _ram_b_2_cond_3_1;
  reg _ram_b_2_cond_4_1;
  reg _ram_b_2_cond_4_2;
  reg _tmp_120;
  reg _ram_b_3_cond_3_1;
  reg _ram_b_3_cond_4_1;
  reg _ram_b_3_cond_4_2;
  reg signed [32-1:0] _tmp_121;
  reg signed [32-1:0] _th_comp_b_12;
  wire [2-1:0] _tmp_122;
  assign _tmp_122 = _th_comp_i_10 + _th_comp_offset_8;
  reg _ram_c_0_cond_1_1;
  reg _ram_c_1_cond_1_1;
  reg _ram_c_2_cond_1_1;
  reg _ram_c_3_cond_1_1;
  reg axim_flag_123;
  reg _th_comp_cond_45_5_1;
  reg signed [32-1:0] _th_comp_size_13;
  reg signed [32-1:0] _th_comp_offset_stream_14;
  reg signed [32-1:0] _th_comp_offset_seq_15;
  reg signed [32-1:0] _th_comp_all_ok_16;
  reg signed [32-1:0] _th_comp_i_17;
  wire [2-1:0] _tmp_124;
  assign _tmp_124 = _th_comp_i_17 + _th_comp_offset_stream_14;
  reg _tmp_125;
  reg _ram_c_0_cond_2_1;
  reg _ram_c_0_cond_3_1;
  reg _ram_c_0_cond_3_2;
  reg _tmp_126;
  reg _ram_c_1_cond_2_1;
  reg _ram_c_1_cond_3_1;
  reg _ram_c_1_cond_3_2;
  reg _tmp_127;
  reg _ram_c_2_cond_2_1;
  reg _ram_c_2_cond_3_1;
  reg _ram_c_2_cond_3_2;
  reg _tmp_128;
  reg _ram_c_3_cond_2_1;
  reg _ram_c_3_cond_3_1;
  reg _ram_c_3_cond_3_2;
  reg signed [32-1:0] _tmp_129;
  reg signed [32-1:0] _th_comp_st_18;
  wire [2-1:0] _tmp_130;
  assign _tmp_130 = _th_comp_i_17 + _th_comp_offset_seq_15;
  reg _tmp_131;
  reg _ram_c_0_cond_4_1;
  reg _ram_c_0_cond_5_1;
  reg _ram_c_0_cond_5_2;
  reg _tmp_132;
  reg _ram_c_1_cond_4_1;
  reg _ram_c_1_cond_5_1;
  reg _ram_c_1_cond_5_2;
  reg _tmp_133;
  reg _ram_c_2_cond_4_1;
  reg _ram_c_2_cond_5_1;
  reg _ram_c_2_cond_5_2;
  reg _tmp_134;
  reg _ram_c_3_cond_4_1;
  reg _ram_c_3_cond_5_1;
  reg _ram_c_3_cond_5_2;
  reg signed [32-1:0] _tmp_135;
  reg signed [32-1:0] _th_comp_sq_19;

  always @(posedge CLK) begin
    if(RST) begin
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
      _tmp_15 <= 0;
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
      _tmp_104 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_105 <= 0;
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
        _tmp_105 <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_ram_a_0_read_start <= 0;
      if(axim_flag_0) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_dma_offset_3;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_dma_size_1;
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
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_15 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_15 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_15 > 0)) begin
        _tmp_15 <= _tmp_15 - 1;
      end 
      if(axim_flag_16) begin
        _myaxi_read_idle <= 1;
      end 
      _myaxi_ram_b_0_read_start <= 0;
      if(axim_flag_17) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_dma_offset_3;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_dma_size_1;
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
      if(axim_flag_55) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_dma_offset_3;
        _myaxi_ram_c_0_write_global_addr <= 1024;
        _myaxi_ram_c_0_write_size <= _th_comp_dma_size_1;
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
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_104 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_104 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_104 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_cat_valid_106 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_104 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_104 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_104 > 0))) begin
        myaxi_wdata <= _cat_data_106;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 16{ 1'd1 } };
        _tmp_104 <= _tmp_104 - 1;
      end 
      if(_cat_valid_106 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_104 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_104 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_104 > 0)) && (_tmp_104 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_105 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_105 <= _tmp_105;
      end 
      if(axim_flag_107) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_108) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_dma_offset_3;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_dma_size_1;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_109) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_dma_offset_3;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_dma_size_1;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_123) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_dma_offset_3;
        _myaxi_ram_c_0_write_global_addr <= 2048;
        _myaxi_ram_c_0_write_size <= _th_comp_dma_size_1;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
    end
  end

  reg [32-1:0] _slice_data_136;
  reg _slice_valid_136;
  wire _slice_ready_136;
  reg [32-1:0] _slice_data_137;
  reg _slice_valid_137;
  wire _slice_ready_137;
  reg [32-1:0] _slice_data_138;
  reg _slice_valid_138;
  wire _slice_ready_138;
  reg [32-1:0] _slice_data_139;
  reg _slice_valid_139;
  wire _slice_ready_139;
  reg [32-1:0] _slice_data_140;
  reg _slice_valid_140;
  wire _slice_ready_140;
  reg [32-1:0] _slice_data_141;
  reg _slice_valid_141;
  wire _slice_ready_141;
  reg [32-1:0] _slice_data_142;
  reg _slice_valid_142;
  wire _slice_ready_142;
  reg [32-1:0] _slice_data_143;
  reg _slice_valid_143;
  wire _slice_ready_143;
  assign _slice_data_5 = _slice_data_136;
  assign _slice_valid_5 = _slice_valid_136;
  assign _slice_ready_136 = _slice_ready_5;
  assign _slice_data_8 = _slice_data_137;
  assign _slice_valid_8 = _slice_valid_137;
  assign _slice_ready_137 = _slice_ready_8;
  assign _slice_data_11 = _slice_data_138;
  assign _slice_valid_11 = _slice_valid_138;
  assign _slice_ready_138 = _slice_ready_11;
  assign _slice_data_14 = _slice_data_139;
  assign _slice_valid_14 = _slice_valid_139;
  assign _slice_ready_139 = _slice_ready_14;
  assign _slice_data_22 = _slice_data_140;
  assign _slice_valid_22 = _slice_valid_140;
  assign _slice_ready_140 = _slice_ready_22;
  assign _slice_data_25 = _slice_data_141;
  assign _slice_valid_25 = _slice_valid_141;
  assign _slice_ready_141 = _slice_ready_25;
  assign _slice_data_28 = _slice_data_142;
  assign _slice_valid_28 = _slice_valid_142;
  assign _slice_ready_142 = _slice_ready_28;
  assign _slice_data_31 = _slice_data_143;
  assign _slice_valid_31 = _slice_valid_143;
  assign _slice_ready_143 = _slice_ready_31;

  always @(posedge CLK) begin
    if(RST) begin
      _slice_data_136 <= 0;
      _slice_valid_136 <= 0;
      _slice_data_137 <= 0;
      _slice_valid_137 <= 0;
      _slice_data_138 <= 0;
      _slice_valid_138 <= 0;
      _slice_data_139 <= 0;
      _slice_valid_139 <= 0;
      _slice_data_140 <= 0;
      _slice_valid_140 <= 0;
      _slice_data_141 <= 0;
      _slice_valid_141 <= 0;
      _slice_data_142 <= 0;
      _slice_valid_142 <= 0;
      _slice_data_143 <= 0;
      _slice_valid_143 <= 0;
    end else begin
      if((_slice_ready_136 || !_slice_valid_136) && 1 && _wvalid_2) begin
        _slice_data_136 <= _wdata_1[6'd31:1'd0];
      end 
      if(_slice_valid_136 && _slice_ready_136) begin
        _slice_valid_136 <= 0;
      end 
      if((_slice_ready_136 || !_slice_valid_136) && 1) begin
        _slice_valid_136 <= _wvalid_2;
      end 
      if((_slice_ready_137 || !_slice_valid_137) && 1 && _wvalid_2) begin
        _slice_data_137 <= _wdata_1[7'd63:7'd32];
      end 
      if(_slice_valid_137 && _slice_ready_137) begin
        _slice_valid_137 <= 0;
      end 
      if((_slice_ready_137 || !_slice_valid_137) && 1) begin
        _slice_valid_137 <= _wvalid_2;
      end 
      if((_slice_ready_138 || !_slice_valid_138) && 1 && _wvalid_2) begin
        _slice_data_138 <= _wdata_1[8'd95:8'd64];
      end 
      if(_slice_valid_138 && _slice_ready_138) begin
        _slice_valid_138 <= 0;
      end 
      if((_slice_ready_138 || !_slice_valid_138) && 1) begin
        _slice_valid_138 <= _wvalid_2;
      end 
      if((_slice_ready_139 || !_slice_valid_139) && 1 && _wvalid_2) begin
        _slice_data_139 <= _wdata_1[8'd127:8'd96];
      end 
      if(_slice_valid_139 && _slice_ready_139) begin
        _slice_valid_139 <= 0;
      end 
      if((_slice_ready_139 || !_slice_valid_139) && 1) begin
        _slice_valid_139 <= _wvalid_2;
      end 
      if((_slice_ready_140 || !_slice_valid_140) && 1 && _wvalid_19) begin
        _slice_data_140 <= _wdata_18[6'd31:1'd0];
      end 
      if(_slice_valid_140 && _slice_ready_140) begin
        _slice_valid_140 <= 0;
      end 
      if((_slice_ready_140 || !_slice_valid_140) && 1) begin
        _slice_valid_140 <= _wvalid_19;
      end 
      if((_slice_ready_141 || !_slice_valid_141) && 1 && _wvalid_19) begin
        _slice_data_141 <= _wdata_18[7'd63:7'd32];
      end 
      if(_slice_valid_141 && _slice_ready_141) begin
        _slice_valid_141 <= 0;
      end 
      if((_slice_ready_141 || !_slice_valid_141) && 1) begin
        _slice_valid_141 <= _wvalid_19;
      end 
      if((_slice_ready_142 || !_slice_valid_142) && 1 && _wvalid_19) begin
        _slice_data_142 <= _wdata_18[8'd95:8'd64];
      end 
      if(_slice_valid_142 && _slice_ready_142) begin
        _slice_valid_142 <= 0;
      end 
      if((_slice_ready_142 || !_slice_valid_142) && 1) begin
        _slice_valid_142 <= _wvalid_19;
      end 
      if((_slice_ready_143 || !_slice_valid_143) && 1 && _wvalid_19) begin
        _slice_data_143 <= _wdata_18[8'd127:8'd96];
      end 
      if(_slice_valid_143 && _slice_ready_143) begin
        _slice_valid_143 <= 0;
      end 
      if((_slice_ready_143 || !_slice_valid_143) && 1) begin
        _slice_valid_143 <= _wvalid_19;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_0_addr <= 0;
      _tmp_3 <= 0;
      ram_a_0_0_wdata <= 0;
      ram_a_0_0_wenable <= 0;
      _tmp_4 <= 0;
      _ram_a_0_cond_0_1 <= 0;
      _ram_a_0_cond_1_1 <= 0;
      _tmp_34 <= 0;
      _ram_a_0_cond_2_1 <= 0;
      _ram_a_0_cond_2_2 <= 0;
      _ram_a_0_cond_3_1 <= 0;
      _tmp_111 <= 0;
      _ram_a_0_cond_4_1 <= 0;
      _ram_a_0_cond_4_2 <= 0;
    end else begin
      if(_ram_a_0_cond_2_2) begin
        _tmp_34 <= 0;
      end 
      if(_ram_a_0_cond_4_2) begin
        _tmp_111 <= 0;
      end 
      if(_ram_a_0_cond_0_1) begin
        ram_a_0_0_wenable <= 0;
        _tmp_4 <= 0;
      end 
      if(_ram_a_0_cond_1_1) begin
        _tmp_34 <= 1;
      end 
      _ram_a_0_cond_2_2 <= _ram_a_0_cond_2_1;
      if(_ram_a_0_cond_3_1) begin
        _tmp_111 <= 1;
      end 
      _ram_a_0_cond_4_2 <= _ram_a_0_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_3 == 0)) begin
        ram_a_0_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_3 <= _myaxi_read_size;
      end 
      if(_slice_valid_5 && ((_tmp_3 > 0) && !_tmp_4) && (_tmp_3 > 0)) begin
        ram_a_0_0_addr <= ram_a_0_0_addr + _myaxi_read_local_stride;
        ram_a_0_0_wdata <= _slice_data_5;
        ram_a_0_0_wenable <= 1;
        _tmp_3 <= _tmp_3 - 1;
      end 
      if(_slice_valid_5 && ((_tmp_3 > 0) && !_tmp_4) && (_tmp_3 == 1)) begin
        _tmp_4 <= 1;
      end 
      _ram_a_0_cond_0_1 <= 1;
      if(_mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1)) begin
        ram_a_0_0_addr <= _mystream_a_source_ram_raddr >> 2;
      end 
      _ram_a_0_cond_1_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      _ram_a_0_cond_2_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      if(th_comp == 38) begin
        ram_a_0_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_a_0_cond_3_1 <= th_comp == 38;
      _ram_a_0_cond_4_1 <= th_comp == 38;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_a_1_0_addr <= 0;
      _tmp_6 <= 0;
      ram_a_1_0_wdata <= 0;
      ram_a_1_0_wenable <= 0;
      _tmp_7 <= 0;
      _ram_a_1_cond_0_1 <= 0;
      _ram_a_1_cond_1_1 <= 0;
      _tmp_35 <= 0;
      _ram_a_1_cond_2_1 <= 0;
      _ram_a_1_cond_2_2 <= 0;
      _ram_a_1_cond_3_1 <= 0;
      _tmp_112 <= 0;
      _ram_a_1_cond_4_1 <= 0;
      _ram_a_1_cond_4_2 <= 0;
    end else begin
      if(_ram_a_1_cond_2_2) begin
        _tmp_35 <= 0;
      end 
      if(_ram_a_1_cond_4_2) begin
        _tmp_112 <= 0;
      end 
      if(_ram_a_1_cond_0_1) begin
        ram_a_1_0_wenable <= 0;
        _tmp_7 <= 0;
      end 
      if(_ram_a_1_cond_1_1) begin
        _tmp_35 <= 1;
      end 
      _ram_a_1_cond_2_2 <= _ram_a_1_cond_2_1;
      if(_ram_a_1_cond_3_1) begin
        _tmp_112 <= 1;
      end 
      _ram_a_1_cond_4_2 <= _ram_a_1_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_6 == 0)) begin
        ram_a_1_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_6 <= _myaxi_read_size;
      end 
      if(_slice_valid_8 && ((_tmp_6 > 0) && !_tmp_7) && (_tmp_6 > 0)) begin
        ram_a_1_0_addr <= ram_a_1_0_addr + _myaxi_read_local_stride;
        ram_a_1_0_wdata <= _slice_data_8;
        ram_a_1_0_wenable <= 1;
        _tmp_6 <= _tmp_6 - 1;
      end 
      if(_slice_valid_8 && ((_tmp_6 > 0) && !_tmp_7) && (_tmp_6 == 1)) begin
        _tmp_7 <= 1;
      end 
      _ram_a_1_cond_0_1 <= 1;
      if(_mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1)) begin
        ram_a_1_0_addr <= _mystream_a_source_ram_raddr >> 2;
      end 
      _ram_a_1_cond_1_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      _ram_a_1_cond_2_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      if(th_comp == 38) begin
        ram_a_1_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_a_1_cond_3_1 <= th_comp == 38;
      _ram_a_1_cond_4_1 <= th_comp == 38;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_a_2_0_addr <= 0;
      _tmp_9 <= 0;
      ram_a_2_0_wdata <= 0;
      ram_a_2_0_wenable <= 0;
      _tmp_10 <= 0;
      _ram_a_2_cond_0_1 <= 0;
      _ram_a_2_cond_1_1 <= 0;
      _tmp_36 <= 0;
      _ram_a_2_cond_2_1 <= 0;
      _ram_a_2_cond_2_2 <= 0;
      _ram_a_2_cond_3_1 <= 0;
      _tmp_113 <= 0;
      _ram_a_2_cond_4_1 <= 0;
      _ram_a_2_cond_4_2 <= 0;
    end else begin
      if(_ram_a_2_cond_2_2) begin
        _tmp_36 <= 0;
      end 
      if(_ram_a_2_cond_4_2) begin
        _tmp_113 <= 0;
      end 
      if(_ram_a_2_cond_0_1) begin
        ram_a_2_0_wenable <= 0;
        _tmp_10 <= 0;
      end 
      if(_ram_a_2_cond_1_1) begin
        _tmp_36 <= 1;
      end 
      _ram_a_2_cond_2_2 <= _ram_a_2_cond_2_1;
      if(_ram_a_2_cond_3_1) begin
        _tmp_113 <= 1;
      end 
      _ram_a_2_cond_4_2 <= _ram_a_2_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_9 == 0)) begin
        ram_a_2_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_9 <= _myaxi_read_size;
      end 
      if(_slice_valid_11 && ((_tmp_9 > 0) && !_tmp_10) && (_tmp_9 > 0)) begin
        ram_a_2_0_addr <= ram_a_2_0_addr + _myaxi_read_local_stride;
        ram_a_2_0_wdata <= _slice_data_11;
        ram_a_2_0_wenable <= 1;
        _tmp_9 <= _tmp_9 - 1;
      end 
      if(_slice_valid_11 && ((_tmp_9 > 0) && !_tmp_10) && (_tmp_9 == 1)) begin
        _tmp_10 <= 1;
      end 
      _ram_a_2_cond_0_1 <= 1;
      if(_mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1)) begin
        ram_a_2_0_addr <= _mystream_a_source_ram_raddr >> 2;
      end 
      _ram_a_2_cond_1_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      _ram_a_2_cond_2_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      if(th_comp == 38) begin
        ram_a_2_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_a_2_cond_3_1 <= th_comp == 38;
      _ram_a_2_cond_4_1 <= th_comp == 38;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_a_3_0_addr <= 0;
      _tmp_12 <= 0;
      ram_a_3_0_wdata <= 0;
      ram_a_3_0_wenable <= 0;
      _tmp_13 <= 0;
      _ram_a_3_cond_0_1 <= 0;
      _ram_a_3_cond_1_1 <= 0;
      _tmp_37 <= 0;
      _ram_a_3_cond_2_1 <= 0;
      _ram_a_3_cond_2_2 <= 0;
      _ram_a_3_cond_3_1 <= 0;
      _tmp_114 <= 0;
      _ram_a_3_cond_4_1 <= 0;
      _ram_a_3_cond_4_2 <= 0;
    end else begin
      if(_ram_a_3_cond_2_2) begin
        _tmp_37 <= 0;
      end 
      if(_ram_a_3_cond_4_2) begin
        _tmp_114 <= 0;
      end 
      if(_ram_a_3_cond_0_1) begin
        ram_a_3_0_wenable <= 0;
        _tmp_13 <= 0;
      end 
      if(_ram_a_3_cond_1_1) begin
        _tmp_37 <= 1;
      end 
      _ram_a_3_cond_2_2 <= _ram_a_3_cond_2_1;
      if(_ram_a_3_cond_3_1) begin
        _tmp_114 <= 1;
      end 
      _ram_a_3_cond_4_2 <= _ram_a_3_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_12 == 0)) begin
        ram_a_3_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_12 <= _myaxi_read_size;
      end 
      if(_slice_valid_14 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 > 0)) begin
        ram_a_3_0_addr <= ram_a_3_0_addr + _myaxi_read_local_stride;
        ram_a_3_0_wdata <= _slice_data_14;
        ram_a_3_0_wenable <= 1;
        _tmp_12 <= _tmp_12 - 1;
      end 
      if(_slice_valid_14 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 == 1)) begin
        _tmp_13 <= 1;
      end 
      _ram_a_3_cond_0_1 <= 1;
      if(_mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1)) begin
        ram_a_3_0_addr <= _mystream_a_source_ram_raddr >> 2;
      end 
      _ram_a_3_cond_1_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      _ram_a_3_cond_2_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      if(th_comp == 38) begin
        ram_a_3_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_a_3_cond_3_1 <= th_comp == 38;
      _ram_a_3_cond_4_1 <= th_comp == 38;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_0_addr <= 0;
      _tmp_20 <= 0;
      ram_b_0_0_wdata <= 0;
      ram_b_0_0_wenable <= 0;
      _tmp_21 <= 0;
      _ram_b_0_cond_0_1 <= 0;
      _ram_b_0_cond_1_1 <= 0;
      _tmp_44 <= 0;
      _ram_b_0_cond_2_1 <= 0;
      _ram_b_0_cond_2_2 <= 0;
      _ram_b_0_cond_3_1 <= 0;
      _tmp_117 <= 0;
      _ram_b_0_cond_4_1 <= 0;
      _ram_b_0_cond_4_2 <= 0;
    end else begin
      if(_ram_b_0_cond_2_2) begin
        _tmp_44 <= 0;
      end 
      if(_ram_b_0_cond_4_2) begin
        _tmp_117 <= 0;
      end 
      if(_ram_b_0_cond_0_1) begin
        ram_b_0_0_wenable <= 0;
        _tmp_21 <= 0;
      end 
      if(_ram_b_0_cond_1_1) begin
        _tmp_44 <= 1;
      end 
      _ram_b_0_cond_2_2 <= _ram_b_0_cond_2_1;
      if(_ram_b_0_cond_3_1) begin
        _tmp_117 <= 1;
      end 
      _ram_b_0_cond_4_2 <= _ram_b_0_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 2) && (_tmp_20 == 0)) begin
        ram_b_0_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_20 <= _myaxi_read_size;
      end 
      if(_slice_valid_22 && ((_tmp_20 > 0) && !_tmp_21) && (_tmp_20 > 0)) begin
        ram_b_0_0_addr <= ram_b_0_0_addr + _myaxi_read_local_stride;
        ram_b_0_0_wdata <= _slice_data_22;
        ram_b_0_0_wenable <= 1;
        _tmp_20 <= _tmp_20 - 1;
      end 
      if(_slice_valid_22 && ((_tmp_20 > 0) && !_tmp_21) && (_tmp_20 == 1)) begin
        _tmp_21 <= 1;
      end 
      _ram_b_0_cond_0_1 <= 1;
      if(_mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2)) begin
        ram_b_0_0_addr <= _mystream_b_source_ram_raddr >> 2;
      end 
      _ram_b_0_cond_1_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      _ram_b_0_cond_2_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      if(th_comp == 40) begin
        ram_b_0_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_b_0_cond_3_1 <= th_comp == 40;
      _ram_b_0_cond_4_1 <= th_comp == 40;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_1_0_addr <= 0;
      _tmp_23 <= 0;
      ram_b_1_0_wdata <= 0;
      ram_b_1_0_wenable <= 0;
      _tmp_24 <= 0;
      _ram_b_1_cond_0_1 <= 0;
      _ram_b_1_cond_1_1 <= 0;
      _tmp_45 <= 0;
      _ram_b_1_cond_2_1 <= 0;
      _ram_b_1_cond_2_2 <= 0;
      _ram_b_1_cond_3_1 <= 0;
      _tmp_118 <= 0;
      _ram_b_1_cond_4_1 <= 0;
      _ram_b_1_cond_4_2 <= 0;
    end else begin
      if(_ram_b_1_cond_2_2) begin
        _tmp_45 <= 0;
      end 
      if(_ram_b_1_cond_4_2) begin
        _tmp_118 <= 0;
      end 
      if(_ram_b_1_cond_0_1) begin
        ram_b_1_0_wenable <= 0;
        _tmp_24 <= 0;
      end 
      if(_ram_b_1_cond_1_1) begin
        _tmp_45 <= 1;
      end 
      _ram_b_1_cond_2_2 <= _ram_b_1_cond_2_1;
      if(_ram_b_1_cond_3_1) begin
        _tmp_118 <= 1;
      end 
      _ram_b_1_cond_4_2 <= _ram_b_1_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 2) && (_tmp_23 == 0)) begin
        ram_b_1_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_23 <= _myaxi_read_size;
      end 
      if(_slice_valid_25 && ((_tmp_23 > 0) && !_tmp_24) && (_tmp_23 > 0)) begin
        ram_b_1_0_addr <= ram_b_1_0_addr + _myaxi_read_local_stride;
        ram_b_1_0_wdata <= _slice_data_25;
        ram_b_1_0_wenable <= 1;
        _tmp_23 <= _tmp_23 - 1;
      end 
      if(_slice_valid_25 && ((_tmp_23 > 0) && !_tmp_24) && (_tmp_23 == 1)) begin
        _tmp_24 <= 1;
      end 
      _ram_b_1_cond_0_1 <= 1;
      if(_mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2)) begin
        ram_b_1_0_addr <= _mystream_b_source_ram_raddr >> 2;
      end 
      _ram_b_1_cond_1_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      _ram_b_1_cond_2_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      if(th_comp == 40) begin
        ram_b_1_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_b_1_cond_3_1 <= th_comp == 40;
      _ram_b_1_cond_4_1 <= th_comp == 40;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_2_0_addr <= 0;
      _tmp_26 <= 0;
      ram_b_2_0_wdata <= 0;
      ram_b_2_0_wenable <= 0;
      _tmp_27 <= 0;
      _ram_b_2_cond_0_1 <= 0;
      _ram_b_2_cond_1_1 <= 0;
      _tmp_46 <= 0;
      _ram_b_2_cond_2_1 <= 0;
      _ram_b_2_cond_2_2 <= 0;
      _ram_b_2_cond_3_1 <= 0;
      _tmp_119 <= 0;
      _ram_b_2_cond_4_1 <= 0;
      _ram_b_2_cond_4_2 <= 0;
    end else begin
      if(_ram_b_2_cond_2_2) begin
        _tmp_46 <= 0;
      end 
      if(_ram_b_2_cond_4_2) begin
        _tmp_119 <= 0;
      end 
      if(_ram_b_2_cond_0_1) begin
        ram_b_2_0_wenable <= 0;
        _tmp_27 <= 0;
      end 
      if(_ram_b_2_cond_1_1) begin
        _tmp_46 <= 1;
      end 
      _ram_b_2_cond_2_2 <= _ram_b_2_cond_2_1;
      if(_ram_b_2_cond_3_1) begin
        _tmp_119 <= 1;
      end 
      _ram_b_2_cond_4_2 <= _ram_b_2_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 2) && (_tmp_26 == 0)) begin
        ram_b_2_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_26 <= _myaxi_read_size;
      end 
      if(_slice_valid_28 && ((_tmp_26 > 0) && !_tmp_27) && (_tmp_26 > 0)) begin
        ram_b_2_0_addr <= ram_b_2_0_addr + _myaxi_read_local_stride;
        ram_b_2_0_wdata <= _slice_data_28;
        ram_b_2_0_wenable <= 1;
        _tmp_26 <= _tmp_26 - 1;
      end 
      if(_slice_valid_28 && ((_tmp_26 > 0) && !_tmp_27) && (_tmp_26 == 1)) begin
        _tmp_27 <= 1;
      end 
      _ram_b_2_cond_0_1 <= 1;
      if(_mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2)) begin
        ram_b_2_0_addr <= _mystream_b_source_ram_raddr >> 2;
      end 
      _ram_b_2_cond_1_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      _ram_b_2_cond_2_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      if(th_comp == 40) begin
        ram_b_2_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_b_2_cond_3_1 <= th_comp == 40;
      _ram_b_2_cond_4_1 <= th_comp == 40;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_3_0_addr <= 0;
      _tmp_29 <= 0;
      ram_b_3_0_wdata <= 0;
      ram_b_3_0_wenable <= 0;
      _tmp_30 <= 0;
      _ram_b_3_cond_0_1 <= 0;
      _ram_b_3_cond_1_1 <= 0;
      _tmp_47 <= 0;
      _ram_b_3_cond_2_1 <= 0;
      _ram_b_3_cond_2_2 <= 0;
      _ram_b_3_cond_3_1 <= 0;
      _tmp_120 <= 0;
      _ram_b_3_cond_4_1 <= 0;
      _ram_b_3_cond_4_2 <= 0;
    end else begin
      if(_ram_b_3_cond_2_2) begin
        _tmp_47 <= 0;
      end 
      if(_ram_b_3_cond_4_2) begin
        _tmp_120 <= 0;
      end 
      if(_ram_b_3_cond_0_1) begin
        ram_b_3_0_wenable <= 0;
        _tmp_30 <= 0;
      end 
      if(_ram_b_3_cond_1_1) begin
        _tmp_47 <= 1;
      end 
      _ram_b_3_cond_2_2 <= _ram_b_3_cond_2_1;
      if(_ram_b_3_cond_3_1) begin
        _tmp_120 <= 1;
      end 
      _ram_b_3_cond_4_2 <= _ram_b_3_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 2) && (_tmp_29 == 0)) begin
        ram_b_3_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_29 <= _myaxi_read_size;
      end 
      if(_slice_valid_31 && ((_tmp_29 > 0) && !_tmp_30) && (_tmp_29 > 0)) begin
        ram_b_3_0_addr <= ram_b_3_0_addr + _myaxi_read_local_stride;
        ram_b_3_0_wdata <= _slice_data_31;
        ram_b_3_0_wenable <= 1;
        _tmp_29 <= _tmp_29 - 1;
      end 
      if(_slice_valid_31 && ((_tmp_29 > 0) && !_tmp_30) && (_tmp_29 == 1)) begin
        _tmp_30 <= 1;
      end 
      _ram_b_3_cond_0_1 <= 1;
      if(_mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2)) begin
        ram_b_3_0_addr <= _mystream_b_source_ram_raddr >> 2;
      end 
      _ram_b_3_cond_1_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      _ram_b_3_cond_2_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      if(th_comp == 40) begin
        ram_b_3_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
      end 
      _ram_b_3_cond_3_1 <= th_comp == 40;
      _ram_b_3_cond_4_1 <= th_comp == 40;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_0_addr <= 0;
      ram_c_0_0_wdata <= 0;
      ram_c_0_0_wenable <= 0;
      _ram_c_0_cond_0_1 <= 0;
      __tmp_61_1 <= 0;
      __tmp_62_1 <= 0;
      _tmp_66 <= 0;
      _tmp_56 <= 0;
      _tmp_57 <= 0;
      _tmp_64 <= 0;
      _tmp_65 <= 0;
      _tmp_63 <= 0;
      _tmp_67 <= 0;
      _ram_c_0_cond_1_1 <= 0;
      _ram_c_0_cond_2_1 <= 0;
      _tmp_125 <= 0;
      _ram_c_0_cond_3_1 <= 0;
      _ram_c_0_cond_3_2 <= 0;
      _ram_c_0_cond_4_1 <= 0;
      _tmp_131 <= 0;
      _ram_c_0_cond_5_1 <= 0;
      _ram_c_0_cond_5_2 <= 0;
    end else begin
      if(_ram_c_0_cond_3_2) begin
        _tmp_125 <= 0;
      end 
      if(_ram_c_0_cond_5_2) begin
        _tmp_131 <= 0;
      end 
      if(_ram_c_0_cond_0_1) begin
        ram_c_0_0_wenable <= 0;
      end 
      if(_ram_c_0_cond_1_1) begin
        ram_c_0_0_wenable <= 0;
      end 
      if(_ram_c_0_cond_2_1) begin
        _tmp_125 <= 1;
      end 
      _ram_c_0_cond_3_2 <= _ram_c_0_cond_3_1;
      if(_ram_c_0_cond_4_1) begin
        _tmp_131 <= 1;
      end 
      _ram_c_0_cond_5_2 <= _ram_c_0_cond_5_1;
      if(_mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 0)) begin
        ram_c_0_0_addr <= _mystream_c_sink_waddr >> 2;
        ram_c_0_0_wdata <= _mystream_c_sink_wdata;
        ram_c_0_0_wenable <= 1;
      end 
      _ram_c_0_cond_0_1 <= _mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 0);
      __tmp_61_1 <= _tmp_61;
      __tmp_62_1 <= _tmp_62;
      if((_tmp_58 || !_tmp_56) && (_tmp_59 || !_tmp_57) && _tmp_64) begin
        _tmp_66 <= 0;
        _tmp_56 <= 0;
        _tmp_57 <= 0;
        _tmp_64 <= 0;
      end 
      if((_tmp_58 || !_tmp_56) && (_tmp_59 || !_tmp_57) && _tmp_63) begin
        _tmp_56 <= 1;
        _tmp_57 <= 1;
        _tmp_66 <= _tmp_65;
        _tmp_65 <= 0;
        _tmp_63 <= 0;
        _tmp_64 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_67 == 0) && !_tmp_65 && !_tmp_66) begin
        ram_c_0_0_addr <= _myaxi_write_local_addr;
        _tmp_67 <= _myaxi_write_size - 1;
        _tmp_63 <= 1;
        _tmp_65 <= _myaxi_write_size == 1;
      end 
      if((_tmp_58 || !_tmp_56) && (_tmp_59 || !_tmp_57) && (_tmp_67 > 0)) begin
        ram_c_0_0_addr <= ram_c_0_0_addr + _myaxi_write_local_stride;
        _tmp_67 <= _tmp_67 - 1;
        _tmp_63 <= 1;
        _tmp_65 <= 0;
      end 
      if((_tmp_58 || !_tmp_56) && (_tmp_59 || !_tmp_57) && (_tmp_67 == 1)) begin
        _tmp_65 <= 1;
      end 
      if((th_comp == 43) && (_tmp_122 == 0)) begin
        ram_c_0_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
        ram_c_0_0_wdata <= _th_comp_sum_9;
        ram_c_0_0_wenable <= 1;
      end 
      _ram_c_0_cond_1_1 <= (th_comp == 43) && (_tmp_122 == 0);
      if(th_comp == 53) begin
        ram_c_0_0_addr <= _th_comp_i_17 + _th_comp_offset_stream_14 >> 2;
      end 
      _ram_c_0_cond_2_1 <= th_comp == 53;
      _ram_c_0_cond_3_1 <= th_comp == 53;
      if(th_comp == 55) begin
        ram_c_0_0_addr <= _th_comp_i_17 + _th_comp_offset_seq_15 >> 2;
      end 
      _ram_c_0_cond_4_1 <= th_comp == 55;
      _ram_c_0_cond_5_1 <= th_comp == 55;
    end
  end

  reg [128-1:0] _cat_data_144;
  reg _cat_valid_144;
  wire _cat_ready_144;
  assign _tmp_94 = 1 && ((_cat_ready_144 || !_cat_valid_144) && (_tmp_92 && _tmp_80 && _tmp_68 && _tmp_56));
  assign _tmp_82 = 1 && ((_cat_ready_144 || !_cat_valid_144) && (_tmp_92 && _tmp_80 && _tmp_68 && _tmp_56));
  assign _tmp_70 = 1 && ((_cat_ready_144 || !_cat_valid_144) && (_tmp_92 && _tmp_80 && _tmp_68 && _tmp_56));
  assign _tmp_58 = 1 && ((_cat_ready_144 || !_cat_valid_144) && (_tmp_92 && _tmp_80 && _tmp_68 && _tmp_56));
  assign _cat_data_106 = _cat_data_144;
  assign _cat_valid_106 = _cat_valid_144;
  assign _cat_ready_144 = _cat_ready_106;

  always @(posedge CLK) begin
    if(RST) begin
      _cat_data_144 <= 0;
      _cat_valid_144 <= 0;
    end else begin
      if((_cat_ready_144 || !_cat_valid_144) && (_tmp_94 && _tmp_82 && _tmp_70 && _tmp_58) && (_tmp_92 && _tmp_80 && _tmp_68 && _tmp_56)) begin
        _cat_data_144 <= { _tmp_98, _tmp_86, _tmp_74, _tmp_62 };
      end 
      if(_cat_valid_144 && _cat_ready_144) begin
        _cat_valid_144 <= 0;
      end 
      if((_cat_ready_144 || !_cat_valid_144) && (_tmp_94 && _tmp_82 && _tmp_70 && _tmp_58)) begin
        _cat_valid_144 <= _tmp_92 && _tmp_80 && _tmp_68 && _tmp_56;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_1_0_addr <= 0;
      ram_c_1_0_wdata <= 0;
      ram_c_1_0_wenable <= 0;
      _ram_c_1_cond_0_1 <= 0;
      __tmp_73_1 <= 0;
      __tmp_74_1 <= 0;
      _tmp_78 <= 0;
      _tmp_68 <= 0;
      _tmp_69 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_75 <= 0;
      _tmp_79 <= 0;
      _ram_c_1_cond_1_1 <= 0;
      _ram_c_1_cond_2_1 <= 0;
      _tmp_126 <= 0;
      _ram_c_1_cond_3_1 <= 0;
      _ram_c_1_cond_3_2 <= 0;
      _ram_c_1_cond_4_1 <= 0;
      _tmp_132 <= 0;
      _ram_c_1_cond_5_1 <= 0;
      _ram_c_1_cond_5_2 <= 0;
    end else begin
      if(_ram_c_1_cond_3_2) begin
        _tmp_126 <= 0;
      end 
      if(_ram_c_1_cond_5_2) begin
        _tmp_132 <= 0;
      end 
      if(_ram_c_1_cond_0_1) begin
        ram_c_1_0_wenable <= 0;
      end 
      if(_ram_c_1_cond_1_1) begin
        ram_c_1_0_wenable <= 0;
      end 
      if(_ram_c_1_cond_2_1) begin
        _tmp_126 <= 1;
      end 
      _ram_c_1_cond_3_2 <= _ram_c_1_cond_3_1;
      if(_ram_c_1_cond_4_1) begin
        _tmp_132 <= 1;
      end 
      _ram_c_1_cond_5_2 <= _ram_c_1_cond_5_1;
      if(_mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 1)) begin
        ram_c_1_0_addr <= _mystream_c_sink_waddr >> 2;
        ram_c_1_0_wdata <= _mystream_c_sink_wdata;
        ram_c_1_0_wenable <= 1;
      end 
      _ram_c_1_cond_0_1 <= _mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 1);
      __tmp_73_1 <= _tmp_73;
      __tmp_74_1 <= _tmp_74;
      if((_tmp_70 || !_tmp_68) && (_tmp_71 || !_tmp_69) && _tmp_76) begin
        _tmp_78 <= 0;
        _tmp_68 <= 0;
        _tmp_69 <= 0;
        _tmp_76 <= 0;
      end 
      if((_tmp_70 || !_tmp_68) && (_tmp_71 || !_tmp_69) && _tmp_75) begin
        _tmp_68 <= 1;
        _tmp_69 <= 1;
        _tmp_78 <= _tmp_77;
        _tmp_77 <= 0;
        _tmp_75 <= 0;
        _tmp_76 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_79 == 0) && !_tmp_77 && !_tmp_78) begin
        ram_c_1_0_addr <= _myaxi_write_local_addr;
        _tmp_79 <= _myaxi_write_size - 1;
        _tmp_75 <= 1;
        _tmp_77 <= _myaxi_write_size == 1;
      end 
      if((_tmp_70 || !_tmp_68) && (_tmp_71 || !_tmp_69) && (_tmp_79 > 0)) begin
        ram_c_1_0_addr <= ram_c_1_0_addr + _myaxi_write_local_stride;
        _tmp_79 <= _tmp_79 - 1;
        _tmp_75 <= 1;
        _tmp_77 <= 0;
      end 
      if((_tmp_70 || !_tmp_68) && (_tmp_71 || !_tmp_69) && (_tmp_79 == 1)) begin
        _tmp_77 <= 1;
      end 
      if((th_comp == 43) && (_tmp_122 == 1)) begin
        ram_c_1_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
        ram_c_1_0_wdata <= _th_comp_sum_9;
        ram_c_1_0_wenable <= 1;
      end 
      _ram_c_1_cond_1_1 <= (th_comp == 43) && (_tmp_122 == 1);
      if(th_comp == 53) begin
        ram_c_1_0_addr <= _th_comp_i_17 + _th_comp_offset_stream_14 >> 2;
      end 
      _ram_c_1_cond_2_1 <= th_comp == 53;
      _ram_c_1_cond_3_1 <= th_comp == 53;
      if(th_comp == 55) begin
        ram_c_1_0_addr <= _th_comp_i_17 + _th_comp_offset_seq_15 >> 2;
      end 
      _ram_c_1_cond_4_1 <= th_comp == 55;
      _ram_c_1_cond_5_1 <= th_comp == 55;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_2_0_addr <= 0;
      ram_c_2_0_wdata <= 0;
      ram_c_2_0_wenable <= 0;
      _ram_c_2_cond_0_1 <= 0;
      __tmp_85_1 <= 0;
      __tmp_86_1 <= 0;
      _tmp_90 <= 0;
      _tmp_80 <= 0;
      _tmp_81 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _tmp_87 <= 0;
      _tmp_91 <= 0;
      _ram_c_2_cond_1_1 <= 0;
      _ram_c_2_cond_2_1 <= 0;
      _tmp_127 <= 0;
      _ram_c_2_cond_3_1 <= 0;
      _ram_c_2_cond_3_2 <= 0;
      _ram_c_2_cond_4_1 <= 0;
      _tmp_133 <= 0;
      _ram_c_2_cond_5_1 <= 0;
      _ram_c_2_cond_5_2 <= 0;
    end else begin
      if(_ram_c_2_cond_3_2) begin
        _tmp_127 <= 0;
      end 
      if(_ram_c_2_cond_5_2) begin
        _tmp_133 <= 0;
      end 
      if(_ram_c_2_cond_0_1) begin
        ram_c_2_0_wenable <= 0;
      end 
      if(_ram_c_2_cond_1_1) begin
        ram_c_2_0_wenable <= 0;
      end 
      if(_ram_c_2_cond_2_1) begin
        _tmp_127 <= 1;
      end 
      _ram_c_2_cond_3_2 <= _ram_c_2_cond_3_1;
      if(_ram_c_2_cond_4_1) begin
        _tmp_133 <= 1;
      end 
      _ram_c_2_cond_5_2 <= _ram_c_2_cond_5_1;
      if(_mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 2)) begin
        ram_c_2_0_addr <= _mystream_c_sink_waddr >> 2;
        ram_c_2_0_wdata <= _mystream_c_sink_wdata;
        ram_c_2_0_wenable <= 1;
      end 
      _ram_c_2_cond_0_1 <= _mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 2);
      __tmp_85_1 <= _tmp_85;
      __tmp_86_1 <= _tmp_86;
      if((_tmp_82 || !_tmp_80) && (_tmp_83 || !_tmp_81) && _tmp_88) begin
        _tmp_90 <= 0;
        _tmp_80 <= 0;
        _tmp_81 <= 0;
        _tmp_88 <= 0;
      end 
      if((_tmp_82 || !_tmp_80) && (_tmp_83 || !_tmp_81) && _tmp_87) begin
        _tmp_80 <= 1;
        _tmp_81 <= 1;
        _tmp_90 <= _tmp_89;
        _tmp_89 <= 0;
        _tmp_87 <= 0;
        _tmp_88 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_91 == 0) && !_tmp_89 && !_tmp_90) begin
        ram_c_2_0_addr <= _myaxi_write_local_addr;
        _tmp_91 <= _myaxi_write_size - 1;
        _tmp_87 <= 1;
        _tmp_89 <= _myaxi_write_size == 1;
      end 
      if((_tmp_82 || !_tmp_80) && (_tmp_83 || !_tmp_81) && (_tmp_91 > 0)) begin
        ram_c_2_0_addr <= ram_c_2_0_addr + _myaxi_write_local_stride;
        _tmp_91 <= _tmp_91 - 1;
        _tmp_87 <= 1;
        _tmp_89 <= 0;
      end 
      if((_tmp_82 || !_tmp_80) && (_tmp_83 || !_tmp_81) && (_tmp_91 == 1)) begin
        _tmp_89 <= 1;
      end 
      if((th_comp == 43) && (_tmp_122 == 2)) begin
        ram_c_2_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
        ram_c_2_0_wdata <= _th_comp_sum_9;
        ram_c_2_0_wenable <= 1;
      end 
      _ram_c_2_cond_1_1 <= (th_comp == 43) && (_tmp_122 == 2);
      if(th_comp == 53) begin
        ram_c_2_0_addr <= _th_comp_i_17 + _th_comp_offset_stream_14 >> 2;
      end 
      _ram_c_2_cond_2_1 <= th_comp == 53;
      _ram_c_2_cond_3_1 <= th_comp == 53;
      if(th_comp == 55) begin
        ram_c_2_0_addr <= _th_comp_i_17 + _th_comp_offset_seq_15 >> 2;
      end 
      _ram_c_2_cond_4_1 <= th_comp == 55;
      _ram_c_2_cond_5_1 <= th_comp == 55;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_3_0_addr <= 0;
      ram_c_3_0_wdata <= 0;
      ram_c_3_0_wenable <= 0;
      _ram_c_3_cond_0_1 <= 0;
      __tmp_97_1 <= 0;
      __tmp_98_1 <= 0;
      _tmp_102 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 0;
      _tmp_100 <= 0;
      _tmp_101 <= 0;
      _tmp_99 <= 0;
      _tmp_103 <= 0;
      _ram_c_3_cond_1_1 <= 0;
      _ram_c_3_cond_2_1 <= 0;
      _tmp_128 <= 0;
      _ram_c_3_cond_3_1 <= 0;
      _ram_c_3_cond_3_2 <= 0;
      _ram_c_3_cond_4_1 <= 0;
      _tmp_134 <= 0;
      _ram_c_3_cond_5_1 <= 0;
      _ram_c_3_cond_5_2 <= 0;
    end else begin
      if(_ram_c_3_cond_3_2) begin
        _tmp_128 <= 0;
      end 
      if(_ram_c_3_cond_5_2) begin
        _tmp_134 <= 0;
      end 
      if(_ram_c_3_cond_0_1) begin
        ram_c_3_0_wenable <= 0;
      end 
      if(_ram_c_3_cond_1_1) begin
        ram_c_3_0_wenable <= 0;
      end 
      if(_ram_c_3_cond_2_1) begin
        _tmp_128 <= 1;
      end 
      _ram_c_3_cond_3_2 <= _ram_c_3_cond_3_1;
      if(_ram_c_3_cond_4_1) begin
        _tmp_134 <= 1;
      end 
      _ram_c_3_cond_5_2 <= _ram_c_3_cond_5_1;
      if(_mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 3)) begin
        ram_c_3_0_addr <= _mystream_c_sink_waddr >> 2;
        ram_c_3_0_wdata <= _mystream_c_sink_wdata;
        ram_c_3_0_wenable <= 1;
      end 
      _ram_c_3_cond_0_1 <= _mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3) && (_tmp_53 == 3);
      __tmp_97_1 <= _tmp_97;
      __tmp_98_1 <= _tmp_98;
      if((_tmp_94 || !_tmp_92) && (_tmp_95 || !_tmp_93) && _tmp_100) begin
        _tmp_102 <= 0;
        _tmp_92 <= 0;
        _tmp_93 <= 0;
        _tmp_100 <= 0;
      end 
      if((_tmp_94 || !_tmp_92) && (_tmp_95 || !_tmp_93) && _tmp_99) begin
        _tmp_92 <= 1;
        _tmp_93 <= 1;
        _tmp_102 <= _tmp_101;
        _tmp_101 <= 0;
        _tmp_99 <= 0;
        _tmp_100 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_103 == 0) && !_tmp_101 && !_tmp_102) begin
        ram_c_3_0_addr <= _myaxi_write_local_addr;
        _tmp_103 <= _myaxi_write_size - 1;
        _tmp_99 <= 1;
        _tmp_101 <= _myaxi_write_size == 1;
      end 
      if((_tmp_94 || !_tmp_92) && (_tmp_95 || !_tmp_93) && (_tmp_103 > 0)) begin
        ram_c_3_0_addr <= ram_c_3_0_addr + _myaxi_write_local_stride;
        _tmp_103 <= _tmp_103 - 1;
        _tmp_99 <= 1;
        _tmp_101 <= 0;
      end 
      if((_tmp_94 || !_tmp_92) && (_tmp_95 || !_tmp_93) && (_tmp_103 == 1)) begin
        _tmp_101 <= 1;
      end 
      if((th_comp == 43) && (_tmp_122 == 3)) begin
        ram_c_3_0_addr <= _th_comp_i_10 + _th_comp_offset_8 >> 2;
        ram_c_3_0_wdata <= _th_comp_sum_9;
        ram_c_3_0_wenable <= 1;
      end 
      _ram_c_3_cond_1_1 <= (th_comp == 43) && (_tmp_122 == 3);
      if(th_comp == 53) begin
        ram_c_3_0_addr <= _th_comp_i_17 + _th_comp_offset_stream_14 >> 2;
      end 
      _ram_c_3_cond_2_1 <= th_comp == 53;
      _ram_c_3_cond_3_1 <= th_comp == 53;
      if(th_comp == 55) begin
        ram_c_3_0_addr <= _th_comp_i_17 + _th_comp_offset_seq_15 >> 2;
      end 
      _ram_c_3_cond_4_1 <= th_comp == 55;
      _ram_c_3_cond_5_1 <= th_comp == 55;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_2 <= 0;
      _set_flag_32 <= 0;
      _mystream_a_source_mode <= 3'b0;
      _mystream_a_source_offset <= 0;
      _mystream_a_source_size <= 0;
      _mystream_a_source_stride <= 0;
      _mystream_a_source_ram_sel <= 0;
      __tmp_41_1 <= 0;
      _mystream_a_source_ram_rvalid <= 0;
      __variable_wdata_0 <= 0;
      _mystream_a_idle <= 1;
      _mystream_a_source_ram_raddr <= 0;
      _mystream_a_source_ram_renable <= 0;
      _mystream_a_source_count <= 0;
      _set_flag_42 <= 0;
      _mystream_b_source_mode <= 3'b0;
      _mystream_b_source_offset <= 0;
      _mystream_b_source_size <= 0;
      _mystream_b_source_stride <= 0;
      _mystream_b_source_ram_sel <= 0;
      __tmp_51_1 <= 0;
      _mystream_b_source_ram_rvalid <= 0;
      __variable_wdata_1 <= 0;
      _mystream_b_idle <= 1;
      _mystream_b_source_ram_raddr <= 0;
      _mystream_b_source_ram_renable <= 0;
      _mystream_b_source_count <= 0;
      _set_flag_52 <= 0;
      _mystream_c_sink_mode <= 3'b0;
      _mystream_c_sink_offset <= 0;
      _mystream_c_sink_size <= 0;
      _mystream_c_sink_stride <= 0;
      _mystream_c_sink_ram_sel <= 0;
      _mystream_c_sink_wenable <= 0;
      _mystream_c_sink_waddr <= 0;
      _mystream_c_sink_count <= 0;
      _mystream_c_sink_wdata <= 0;
      _set_flag_54 <= 0;
    end else begin
      _plus_data_2 <= mystream_a_data + mystream_b_data;
      _set_flag_32 <= 0;
      if(th_comp == 14) begin
        _set_flag_32 <= 1;
      end 
      if(_set_flag_32) begin
        _mystream_a_source_mode <= 3'b1;
        _mystream_a_source_offset <= _th_comp_offset_6;
        _mystream_a_source_size <= _th_comp_size_5;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_32) begin
        _mystream_a_source_ram_sel <= 1;
      end 
      __tmp_41_1 <= _tmp_41;
      _mystream_a_source_ram_rvalid <= __tmp_41_1;
      if(_mystream_a_source_ram_rvalid) begin
        __variable_wdata_0 <= _mystream_a_source_ram_rdata;
      end 
      if(_mystream_start && _mystream_a_source_mode & 3'b1) begin
        _mystream_a_idle <= 0;
      end 
      if(_mystream_a_source_fsm_0 == 1) begin
        _mystream_a_source_ram_raddr <= _mystream_a_source_offset;
        _mystream_a_source_ram_renable <= 1;
        _mystream_a_source_count <= _mystream_a_source_size;
      end 
      if(_mystream_a_source_fsm_0 == 2) begin
        _mystream_a_source_ram_raddr <= _mystream_a_source_ram_raddr + _mystream_a_source_stride;
        _mystream_a_source_ram_renable <= 1;
        _mystream_a_source_count <= _mystream_a_source_count - 1;
      end 
      if((_mystream_a_source_fsm_0 == 2) && (_mystream_a_source_count == 1)) begin
        _mystream_a_source_ram_renable <= 0;
        _mystream_a_idle <= 1;
      end 
      _set_flag_42 <= 0;
      if(th_comp == 15) begin
        _set_flag_42 <= 1;
      end 
      if(_set_flag_42) begin
        _mystream_b_source_mode <= 3'b1;
        _mystream_b_source_offset <= _th_comp_offset_6;
        _mystream_b_source_size <= _th_comp_size_5;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_42) begin
        _mystream_b_source_ram_sel <= 2;
      end 
      __tmp_51_1 <= _tmp_51;
      _mystream_b_source_ram_rvalid <= __tmp_51_1;
      if(_mystream_b_source_ram_rvalid) begin
        __variable_wdata_1 <= _mystream_b_source_ram_rdata;
      end 
      if(_mystream_start && _mystream_b_source_mode & 3'b1) begin
        _mystream_b_idle <= 0;
      end 
      if(_mystream_b_source_fsm_1 == 1) begin
        _mystream_b_source_ram_raddr <= _mystream_b_source_offset;
        _mystream_b_source_ram_renable <= 1;
        _mystream_b_source_count <= _mystream_b_source_size;
      end 
      if(_mystream_b_source_fsm_1 == 2) begin
        _mystream_b_source_ram_raddr <= _mystream_b_source_ram_raddr + _mystream_b_source_stride;
        _mystream_b_source_ram_renable <= 1;
        _mystream_b_source_count <= _mystream_b_source_count - 1;
      end 
      if((_mystream_b_source_fsm_1 == 2) && (_mystream_b_source_count == 1)) begin
        _mystream_b_source_ram_renable <= 0;
        _mystream_b_idle <= 1;
      end 
      _set_flag_52 <= 0;
      if(th_comp == 16) begin
        _set_flag_52 <= 1;
      end 
      if(_set_flag_52) begin
        _mystream_c_sink_mode <= 3'b1;
        _mystream_c_sink_offset <= _th_comp_offset_6;
        _mystream_c_sink_size <= _th_comp_size_5;
        _mystream_c_sink_stride <= 1;
      end 
      if(_set_flag_52) begin
        _mystream_c_sink_ram_sel <= 3;
      end 
      if(_mystream_c_sink_fsm_2 == 0) begin
        _mystream_c_sink_wenable <= 0;
      end 
      if(_mystream_c_sink_fsm_2 == 1) begin
        _mystream_c_sink_waddr <= _mystream_c_sink_offset - _mystream_c_sink_stride;
        _mystream_c_sink_count <= _mystream_c_sink_size;
      end 
      if(_mystream_c_sink_fsm_2 == 6) begin
        _mystream_c_sink_wenable <= 0;
      end 
      if(_mystream_c_sink_fsm_2 == 6) begin
        _mystream_c_sink_waddr <= _mystream_c_sink_waddr + _mystream_c_sink_stride;
        _mystream_c_sink_wdata <= mystream_c_data;
        _mystream_c_sink_wenable <= 1;
        _mystream_c_sink_count <= _mystream_c_sink_count - 1;
      end 
      _set_flag_54 <= 0;
      if(th_comp == 17) begin
        _set_flag_54 <= 1;
      end 
    end
  end

  localparam _mystream_fsm_1 = 1;
  localparam _mystream_fsm_2 = 2;
  localparam _mystream_fsm_3 = 3;
  localparam _mystream_fsm_4 = 4;
  localparam _mystream_fsm_5 = 5;
  localparam _mystream_fsm_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm <= _mystream_fsm_init;
      _mystream_start <= 0;
      _mystream_busy <= 0;
    end else begin
      case(_mystream_fsm)
        _mystream_fsm_init: begin
          if(_mystream_start_flag) begin
            _mystream_start <= 1;
            _mystream_busy <= 1;
          end 
          if(_mystream_start_flag) begin
            _mystream_fsm <= _mystream_fsm_1;
          end 
        end
        _mystream_fsm_1: begin
          _mystream_start <= 0;
          _mystream_fsm <= _mystream_fsm_2;
        end
        _mystream_fsm_2: begin
          if(_mystream_done) begin
            _mystream_fsm <= _mystream_fsm_3;
          end 
        end
        _mystream_fsm_3: begin
          _mystream_fsm <= _mystream_fsm_4;
        end
        _mystream_fsm_4: begin
          _mystream_fsm <= _mystream_fsm_5;
        end
        _mystream_fsm_5: begin
          _mystream_fsm <= _mystream_fsm_6;
        end
        _mystream_fsm_6: begin
          _mystream_busy <= 0;
          _mystream_fsm <= _mystream_fsm_init;
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
  localparam th_comp_33 = 33;
  localparam th_comp_34 = 34;
  localparam th_comp_35 = 35;
  localparam th_comp_36 = 36;
  localparam th_comp_37 = 37;
  localparam th_comp_38 = 38;
  localparam th_comp_39 = 39;
  localparam th_comp_40 = 40;
  localparam th_comp_41 = 41;
  localparam th_comp_42 = 42;
  localparam th_comp_43 = 43;
  localparam th_comp_44 = 44;
  localparam th_comp_45 = 45;
  localparam th_comp_46 = 46;
  localparam th_comp_47 = 47;
  localparam th_comp_48 = 48;
  localparam th_comp_49 = 49;
  localparam th_comp_50 = 50;
  localparam th_comp_51 = 51;
  localparam th_comp_52 = 52;
  localparam th_comp_53 = 53;
  localparam th_comp_54 = 54;
  localparam th_comp_55 = 55;
  localparam th_comp_56 = 56;
  localparam th_comp_57 = 57;
  localparam th_comp_58 = 58;
  localparam th_comp_59 = 59;
  localparam th_comp_60 = 60;
  localparam th_comp_61 = 61;
  localparam th_comp_62 = 62;
  localparam th_comp_63 = 63;
  localparam th_comp_64 = 64;
  localparam th_comp_65 = 65;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _d1_th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_dma_size_1 <= 0;
      _th_comp_comp_size_2 <= 0;
      _th_comp_dma_offset_3 <= 0;
      _th_comp_comp_offset_4 <= 0;
      axim_flag_0 <= 0;
      _th_comp_cond_5_0_1 <= 0;
      axim_flag_17 <= 0;
      _th_comp_cond_9_1_1 <= 0;
      _th_comp_size_5 <= 0;
      _th_comp_offset_6 <= 0;
      axim_flag_55 <= 0;
      _th_comp_cond_20_2_1 <= 0;
      axim_flag_108 <= 0;
      _th_comp_cond_26_3_1 <= 0;
      axim_flag_109 <= 0;
      _th_comp_cond_30_4_1 <= 0;
      _th_comp_size_7 <= 0;
      _th_comp_offset_8 <= 0;
      _th_comp_sum_9 <= 0;
      _th_comp_i_10 <= 0;
      _tmp_115 <= 0;
      _th_comp_a_11 <= 0;
      _tmp_121 <= 0;
      _th_comp_b_12 <= 0;
      axim_flag_123 <= 0;
      _th_comp_cond_45_5_1 <= 0;
      _th_comp_size_13 <= 0;
      _th_comp_offset_stream_14 <= 0;
      _th_comp_offset_seq_15 <= 0;
      _th_comp_all_ok_16 <= 0;
      _th_comp_i_17 <= 0;
      _tmp_129 <= 0;
      _th_comp_st_18 <= 0;
      _tmp_135 <= 0;
      _th_comp_sq_19 <= 0;
    end else begin
      _d1_th_comp <= th_comp;
      case(_d1_th_comp)
        th_comp_5: begin
          if(_th_comp_cond_5_0_1) begin
            axim_flag_0 <= 0;
          end 
        end
        th_comp_9: begin
          if(_th_comp_cond_9_1_1) begin
            axim_flag_17 <= 0;
          end 
        end
        th_comp_20: begin
          if(_th_comp_cond_20_2_1) begin
            axim_flag_55 <= 0;
          end 
        end
        th_comp_26: begin
          if(_th_comp_cond_26_3_1) begin
            axim_flag_108 <= 0;
          end 
        end
        th_comp_30: begin
          if(_th_comp_cond_30_4_1) begin
            axim_flag_109 <= 0;
          end 
        end
        th_comp_45: begin
          if(_th_comp_cond_45_5_1) begin
            axim_flag_123 <= 0;
          end 
        end
      endcase
      case(th_comp)
        th_comp_init: begin
          _th_comp_size_0 <= 32;
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_dma_size_1 <= _th_comp_size_0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          _th_comp_comp_size_2 <= _th_comp_size_0 << 2;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          _th_comp_dma_offset_3 <= 0;
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          _th_comp_comp_offset_4 <= 0;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          axim_flag_0 <= 1;
          _th_comp_cond_5_0_1 <= 1;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          axim_flag_17 <= 1;
          _th_comp_cond_9_1_1 <= 1;
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_13;
          end 
        end
        th_comp_13: begin
          _th_comp_size_5 <= _th_comp_size_0;
          _th_comp_offset_6 <= _th_comp_comp_offset_4;
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_20;
          end 
        end
        th_comp_20: begin
          axim_flag_55 <= 1;
          _th_comp_cond_20_2_1 <= 1;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_24;
          end 
        end
        th_comp_24: begin
          _th_comp_dma_offset_3 <= _th_comp_size_0;
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          _th_comp_comp_offset_4 <= _th_comp_comp_size_2;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          axim_flag_108 <= 1;
          _th_comp_cond_26_3_1 <= 1;
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_30;
          end 
        end
        th_comp_30: begin
          axim_flag_109 <= 1;
          _th_comp_cond_30_4_1 <= 1;
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          th_comp <= th_comp_32;
        end
        th_comp_32: begin
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_34;
          end 
        end
        th_comp_34: begin
          _th_comp_size_7 <= _th_comp_size_0;
          _th_comp_offset_8 <= _th_comp_comp_offset_4;
          th_comp <= th_comp_35;
        end
        th_comp_35: begin
          _th_comp_sum_9 <= 0;
          th_comp <= th_comp_36;
        end
        th_comp_36: begin
          _th_comp_i_10 <= 0;
          th_comp <= th_comp_37;
        end
        th_comp_37: begin
          if(_th_comp_i_10 < _th_comp_size_7) begin
            th_comp <= th_comp_38;
          end else begin
            th_comp <= th_comp_45;
          end
        end
        th_comp_38: begin
          if(_tmp_111 && (_tmp_110 == 0)) begin
            _tmp_115 <= ram_a_0_0_rdata;
          end 
          if(_tmp_112 && (_tmp_110 == 1)) begin
            _tmp_115 <= ram_a_1_0_rdata;
          end 
          if(_tmp_113 && (_tmp_110 == 2)) begin
            _tmp_115 <= ram_a_2_0_rdata;
          end 
          if(_tmp_114 && (_tmp_110 == 3)) begin
            _tmp_115 <= ram_a_3_0_rdata;
          end 
          if(_tmp_111) begin
            th_comp <= th_comp_39;
          end 
        end
        th_comp_39: begin
          _th_comp_a_11 <= _tmp_115;
          th_comp <= th_comp_40;
        end
        th_comp_40: begin
          if(_tmp_117 && (_tmp_116 == 0)) begin
            _tmp_121 <= ram_b_0_0_rdata;
          end 
          if(_tmp_118 && (_tmp_116 == 1)) begin
            _tmp_121 <= ram_b_1_0_rdata;
          end 
          if(_tmp_119 && (_tmp_116 == 2)) begin
            _tmp_121 <= ram_b_2_0_rdata;
          end 
          if(_tmp_120 && (_tmp_116 == 3)) begin
            _tmp_121 <= ram_b_3_0_rdata;
          end 
          if(_tmp_117) begin
            th_comp <= th_comp_41;
          end 
        end
        th_comp_41: begin
          _th_comp_b_12 <= _tmp_121;
          th_comp <= th_comp_42;
        end
        th_comp_42: begin
          _th_comp_sum_9 <= _th_comp_a_11 + _th_comp_b_12;
          th_comp <= th_comp_43;
        end
        th_comp_43: begin
          th_comp <= th_comp_44;
        end
        th_comp_44: begin
          _th_comp_i_10 <= _th_comp_i_10 + 1;
          th_comp <= th_comp_37;
        end
        th_comp_45: begin
          axim_flag_123 <= 1;
          _th_comp_cond_45_5_1 <= 1;
          th_comp <= th_comp_46;
        end
        th_comp_46: begin
          th_comp <= th_comp_47;
        end
        th_comp_47: begin
          th_comp <= th_comp_48;
        end
        th_comp_48: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_49;
          end 
        end
        th_comp_49: begin
          _th_comp_size_13 <= _th_comp_comp_size_2;
          _th_comp_offset_stream_14 <= 0;
          _th_comp_offset_seq_15 <= _th_comp_comp_offset_4;
          th_comp <= th_comp_50;
        end
        th_comp_50: begin
          _th_comp_all_ok_16 <= 1;
          th_comp <= th_comp_51;
        end
        th_comp_51: begin
          _th_comp_i_17 <= 0;
          th_comp <= th_comp_52;
        end
        th_comp_52: begin
          if(_th_comp_i_17 < _th_comp_size_13) begin
            th_comp <= th_comp_53;
          end else begin
            th_comp <= th_comp_61;
          end
        end
        th_comp_53: begin
          if(_tmp_125 && (_tmp_124 == 0)) begin
            _tmp_129 <= ram_c_0_0_rdata;
          end 
          if(_tmp_126 && (_tmp_124 == 1)) begin
            _tmp_129 <= ram_c_1_0_rdata;
          end 
          if(_tmp_127 && (_tmp_124 == 2)) begin
            _tmp_129 <= ram_c_2_0_rdata;
          end 
          if(_tmp_128 && (_tmp_124 == 3)) begin
            _tmp_129 <= ram_c_3_0_rdata;
          end 
          if(_tmp_125) begin
            th_comp <= th_comp_54;
          end 
        end
        th_comp_54: begin
          _th_comp_st_18 <= _tmp_129;
          th_comp <= th_comp_55;
        end
        th_comp_55: begin
          if(_tmp_131 && (_tmp_130 == 0)) begin
            _tmp_135 <= ram_c_0_0_rdata;
          end 
          if(_tmp_132 && (_tmp_130 == 1)) begin
            _tmp_135 <= ram_c_1_0_rdata;
          end 
          if(_tmp_133 && (_tmp_130 == 2)) begin
            _tmp_135 <= ram_c_2_0_rdata;
          end 
          if(_tmp_134 && (_tmp_130 == 3)) begin
            _tmp_135 <= ram_c_3_0_rdata;
          end 
          if(_tmp_131) begin
            th_comp <= th_comp_56;
          end 
        end
        th_comp_56: begin
          _th_comp_sq_19 <= _tmp_135;
          th_comp <= th_comp_57;
        end
        th_comp_57: begin
          if(_th_comp_st_18 !== _th_comp_sq_19) begin
            th_comp <= th_comp_58;
          end else begin
            th_comp <= th_comp_60;
          end
        end
        th_comp_58: begin
          _th_comp_all_ok_16 <= 0;
          th_comp <= th_comp_59;
        end
        th_comp_59: begin
          $display("%d %d %d", _th_comp_i_17, _th_comp_st_18, _th_comp_sq_19);
          th_comp <= th_comp_60;
        end
        th_comp_60: begin
          _th_comp_i_17 <= _th_comp_i_17 + 1;
          th_comp <= th_comp_52;
        end
        th_comp_61: begin
          if(_th_comp_all_ok_16) begin
            th_comp <= th_comp_62;
          end else begin
            th_comp <= th_comp_64;
          end
        end
        th_comp_62: begin
          $display("OK");
          th_comp <= th_comp_63;
        end
        th_comp_63: begin
          th_comp <= th_comp_65;
        end
        th_comp_64: begin
          $display("NG");
          th_comp <= th_comp_65;
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
      _wvalid_2 <= 0;
      _wdata_1 <= 0;
      axim_flag_16 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
      __myaxi_read_fsm_cond_3_2_1 <= 0;
      _wvalid_19 <= 0;
      _wdata_18 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_2 <= 0;
          end 
          if(__myaxi_read_fsm_cond_3_2_1) begin
            _wvalid_19 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_16 <= 0;
          end 
        end
      endcase
      case(_myaxi_read_fsm)
        _myaxi_read_fsm_init: begin
          if(_myaxi_read_start) begin
            _myaxi_read_cur_global_addr <= (_myaxi_read_global_addr >> 4) << 4;
            _myaxi_read_rest_size <= _myaxi_read_size;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 1)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 2)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
        end
        _myaxi_read_fsm_1: begin
          if((_myaxi_read_rest_size <= 256) && ((_myaxi_read_cur_global_addr & 4095) + (_myaxi_read_rest_size << 4) >= 4096)) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 4;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 4);
          end else if(_myaxi_read_rest_size <= 256) begin
            _myaxi_read_cur_size <= _myaxi_read_rest_size;
            _myaxi_read_rest_size <= 0;
          end else if((_myaxi_read_cur_global_addr & 4095) + 4096 >= 4096) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 4;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 4);
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
            _wdata_1 <= myaxi_rdata;
            _wvalid_2 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 4);
          end 
          __myaxi_read_fsm_cond_3_2_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 2)) begin
            _wdata_18 <= myaxi_rdata;
            _wvalid_19 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_16 <= 1;
          __myaxi_read_fsm_cond_4_1_1 <= 1;
          _myaxi_read_fsm <= _myaxi_read_fsm_5;
        end
        _myaxi_read_fsm_5: begin
          _myaxi_read_fsm <= _myaxi_read_fsm_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_33_1 <= 0;
      __tmp_33_2 <= 0;
    end else begin
      __tmp_33_1 <= _tmp_33;
      __tmp_33_2 <= __tmp_33_1;
    end
  end

  localparam _mystream_a_source_fsm_0_1 = 1;
  localparam _mystream_a_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
    end else begin
      case(_mystream_a_source_fsm_0)
        _mystream_a_source_fsm_0_init: begin
          if(_mystream_start && _mystream_a_source_mode & 3'b1) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_1;
          end 
        end
        _mystream_a_source_fsm_0_1: begin
          _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_2;
        end
        _mystream_a_source_fsm_0_2: begin
          if(_mystream_a_source_count == 1) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_43_1 <= 0;
      __tmp_43_2 <= 0;
    end else begin
      __tmp_43_1 <= _tmp_43;
      __tmp_43_2 <= __tmp_43_1;
    end
  end

  localparam _mystream_b_source_fsm_1_1 = 1;
  localparam _mystream_b_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
    end else begin
      case(_mystream_b_source_fsm_1)
        _mystream_b_source_fsm_1_init: begin
          if(_mystream_start && _mystream_b_source_mode & 3'b1) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_1;
          end 
        end
        _mystream_b_source_fsm_1_1: begin
          _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_2;
        end
        _mystream_b_source_fsm_1_2: begin
          if(_mystream_b_source_count == 1) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_c_sink_fsm_2_1 = 1;
  localparam _mystream_c_sink_fsm_2_2 = 2;
  localparam _mystream_c_sink_fsm_2_3 = 3;
  localparam _mystream_c_sink_fsm_2_4 = 4;
  localparam _mystream_c_sink_fsm_2_5 = 5;
  localparam _mystream_c_sink_fsm_2_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
    end else begin
      case(_mystream_c_sink_fsm_2)
        _mystream_c_sink_fsm_2_init: begin
          if(_mystream_start && _mystream_c_sink_mode & 3'b1) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_1;
          end 
        end
        _mystream_c_sink_fsm_2_1: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_2;
        end
        _mystream_c_sink_fsm_2_2: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_3;
        end
        _mystream_c_sink_fsm_2_3: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_4;
        end
        _mystream_c_sink_fsm_2_4: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_5;
        end
        _mystream_c_sink_fsm_2_5: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_6;
        end
        _mystream_c_sink_fsm_2_6: begin
          if(_mystream_c_sink_count == 1) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
          end 
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
      axim_flag_107 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_107 <= 0;
          end 
        end
      endcase
      case(_myaxi_write_fsm)
        _myaxi_write_fsm_init: begin
          if(_myaxi_write_start) begin
            _myaxi_write_cur_global_addr <= (_myaxi_write_global_addr >> 4) << 4;
            _myaxi_write_rest_size <= _myaxi_write_size;
          end 
          if(_myaxi_write_start && (_myaxi_write_op_sel == 1)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
        end
        _myaxi_write_fsm_1: begin
          if((_myaxi_write_rest_size <= 256) && ((_myaxi_write_cur_global_addr & 4095) + (_myaxi_write_rest_size << 4) >= 4096)) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 4;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 4);
          end else if(_myaxi_write_rest_size <= 256) begin
            _myaxi_write_cur_size <= _myaxi_write_rest_size;
            _myaxi_write_rest_size <= 0;
          end else if((_myaxi_write_cur_global_addr & 4095) + 4096 >= 4096) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 4;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 4);
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
            _myaxi_write_cur_global_addr <= _myaxi_write_cur_global_addr + (_myaxi_write_cur_size << 4);
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size > 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size == 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_4;
          end 
        end
        _myaxi_write_fsm_4: begin
          axim_flag_107 <= 1;
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



module ram_a_0
(
  input CLK,
  input [10-1:0] ram_a_0_0_addr,
  output [32-1:0] ram_a_0_0_rdata,
  input [32-1:0] ram_a_0_0_wdata,
  input ram_a_0_0_wenable
);

  reg [10-1:0] ram_a_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_0_0_wenable) begin
      mem[ram_a_0_0_addr] <= ram_a_0_0_wdata;
    end 
    ram_a_0_0_daddr <= ram_a_0_0_addr;
  end

  assign ram_a_0_0_rdata = mem[ram_a_0_0_daddr];

endmodule



module ram_a_1
(
  input CLK,
  input [10-1:0] ram_a_1_0_addr,
  output [32-1:0] ram_a_1_0_rdata,
  input [32-1:0] ram_a_1_0_wdata,
  input ram_a_1_0_wenable
);

  reg [10-1:0] ram_a_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_1_0_wenable) begin
      mem[ram_a_1_0_addr] <= ram_a_1_0_wdata;
    end 
    ram_a_1_0_daddr <= ram_a_1_0_addr;
  end

  assign ram_a_1_0_rdata = mem[ram_a_1_0_daddr];

endmodule



module ram_a_2
(
  input CLK,
  input [10-1:0] ram_a_2_0_addr,
  output [32-1:0] ram_a_2_0_rdata,
  input [32-1:0] ram_a_2_0_wdata,
  input ram_a_2_0_wenable
);

  reg [10-1:0] ram_a_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_2_0_wenable) begin
      mem[ram_a_2_0_addr] <= ram_a_2_0_wdata;
    end 
    ram_a_2_0_daddr <= ram_a_2_0_addr;
  end

  assign ram_a_2_0_rdata = mem[ram_a_2_0_daddr];

endmodule



module ram_a_3
(
  input CLK,
  input [10-1:0] ram_a_3_0_addr,
  output [32-1:0] ram_a_3_0_rdata,
  input [32-1:0] ram_a_3_0_wdata,
  input ram_a_3_0_wenable
);

  reg [10-1:0] ram_a_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_3_0_wenable) begin
      mem[ram_a_3_0_addr] <= ram_a_3_0_wdata;
    end 
    ram_a_3_0_daddr <= ram_a_3_0_addr;
  end

  assign ram_a_3_0_rdata = mem[ram_a_3_0_daddr];

endmodule



module ram_b_0
(
  input CLK,
  input [10-1:0] ram_b_0_0_addr,
  output [32-1:0] ram_b_0_0_rdata,
  input [32-1:0] ram_b_0_0_wdata,
  input ram_b_0_0_wenable
);

  reg [10-1:0] ram_b_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_0_0_wenable) begin
      mem[ram_b_0_0_addr] <= ram_b_0_0_wdata;
    end 
    ram_b_0_0_daddr <= ram_b_0_0_addr;
  end

  assign ram_b_0_0_rdata = mem[ram_b_0_0_daddr];

endmodule



module ram_b_1
(
  input CLK,
  input [10-1:0] ram_b_1_0_addr,
  output [32-1:0] ram_b_1_0_rdata,
  input [32-1:0] ram_b_1_0_wdata,
  input ram_b_1_0_wenable
);

  reg [10-1:0] ram_b_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_1_0_wenable) begin
      mem[ram_b_1_0_addr] <= ram_b_1_0_wdata;
    end 
    ram_b_1_0_daddr <= ram_b_1_0_addr;
  end

  assign ram_b_1_0_rdata = mem[ram_b_1_0_daddr];

endmodule



module ram_b_2
(
  input CLK,
  input [10-1:0] ram_b_2_0_addr,
  output [32-1:0] ram_b_2_0_rdata,
  input [32-1:0] ram_b_2_0_wdata,
  input ram_b_2_0_wenable
);

  reg [10-1:0] ram_b_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_2_0_wenable) begin
      mem[ram_b_2_0_addr] <= ram_b_2_0_wdata;
    end 
    ram_b_2_0_daddr <= ram_b_2_0_addr;
  end

  assign ram_b_2_0_rdata = mem[ram_b_2_0_daddr];

endmodule



module ram_b_3
(
  input CLK,
  input [10-1:0] ram_b_3_0_addr,
  output [32-1:0] ram_b_3_0_rdata,
  input [32-1:0] ram_b_3_0_wdata,
  input ram_b_3_0_wenable
);

  reg [10-1:0] ram_b_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_3_0_wenable) begin
      mem[ram_b_3_0_addr] <= ram_b_3_0_wdata;
    end 
    ram_b_3_0_daddr <= ram_b_3_0_addr;
  end

  assign ram_b_3_0_rdata = mem[ram_b_3_0_daddr];

endmodule



module ram_c_0
(
  input CLK,
  input [10-1:0] ram_c_0_0_addr,
  output [32-1:0] ram_c_0_0_rdata,
  input [32-1:0] ram_c_0_0_wdata,
  input ram_c_0_0_wenable
);

  reg [10-1:0] ram_c_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_0_0_wenable) begin
      mem[ram_c_0_0_addr] <= ram_c_0_0_wdata;
    end 
    ram_c_0_0_daddr <= ram_c_0_0_addr;
  end

  assign ram_c_0_0_rdata = mem[ram_c_0_0_daddr];

endmodule



module ram_c_1
(
  input CLK,
  input [10-1:0] ram_c_1_0_addr,
  output [32-1:0] ram_c_1_0_rdata,
  input [32-1:0] ram_c_1_0_wdata,
  input ram_c_1_0_wenable
);

  reg [10-1:0] ram_c_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_1_0_wenable) begin
      mem[ram_c_1_0_addr] <= ram_c_1_0_wdata;
    end 
    ram_c_1_0_daddr <= ram_c_1_0_addr;
  end

  assign ram_c_1_0_rdata = mem[ram_c_1_0_daddr];

endmodule



module ram_c_2
(
  input CLK,
  input [10-1:0] ram_c_2_0_addr,
  output [32-1:0] ram_c_2_0_rdata,
  input [32-1:0] ram_c_2_0_wdata,
  input ram_c_2_0_wenable
);

  reg [10-1:0] ram_c_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_2_0_wenable) begin
      mem[ram_c_2_0_addr] <= ram_c_2_0_wdata;
    end 
    ram_c_2_0_daddr <= ram_c_2_0_addr;
  end

  assign ram_c_2_0_rdata = mem[ram_c_2_0_daddr];

endmodule



module ram_c_3
(
  input CLK,
  input [10-1:0] ram_c_3_0_addr,
  output [32-1:0] ram_c_3_0_rdata,
  input [32-1:0] ram_c_3_0_wdata,
  input ram_c_3_0_wenable
);

  reg [10-1:0] ram_c_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_3_0_wenable) begin
      mem[ram_c_3_0_addr] <= ram_c_3_0_wdata;
    end 
    ram_c_3_0_daddr <= ram_c_3_0_addr;
  end

  assign ram_c_3_0_rdata = mem[ram_c_3_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_stream_multibank.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
