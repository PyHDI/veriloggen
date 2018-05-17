from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_multibank_nested_ram_dma_block

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
  reg [10-1:0] myram0_0_0_addr;
  wire [32-1:0] myram0_0_0_rdata;
  reg [32-1:0] myram0_0_0_wdata;
  reg myram0_0_0_wenable;

  myram0_0
  inst_myram0_0
  (
    .CLK(CLK),
    .myram0_0_0_addr(myram0_0_0_addr),
    .myram0_0_0_rdata(myram0_0_0_rdata),
    .myram0_0_0_wdata(myram0_0_0_wdata),
    .myram0_0_0_wenable(myram0_0_0_wenable)
  );

  reg [10-1:0] myram0_1_0_addr;
  wire [32-1:0] myram0_1_0_rdata;
  reg [32-1:0] myram0_1_0_wdata;
  reg myram0_1_0_wenable;

  myram0_1
  inst_myram0_1
  (
    .CLK(CLK),
    .myram0_1_0_addr(myram0_1_0_addr),
    .myram0_1_0_rdata(myram0_1_0_rdata),
    .myram0_1_0_wdata(myram0_1_0_wdata),
    .myram0_1_0_wenable(myram0_1_0_wenable)
  );

  reg [10-1:0] myram0_2_0_addr;
  wire [32-1:0] myram0_2_0_rdata;
  reg [32-1:0] myram0_2_0_wdata;
  reg myram0_2_0_wenable;

  myram0_2
  inst_myram0_2
  (
    .CLK(CLK),
    .myram0_2_0_addr(myram0_2_0_addr),
    .myram0_2_0_rdata(myram0_2_0_rdata),
    .myram0_2_0_wdata(myram0_2_0_wdata),
    .myram0_2_0_wenable(myram0_2_0_wenable)
  );

  reg [10-1:0] myram0_3_0_addr;
  wire [32-1:0] myram0_3_0_rdata;
  reg [32-1:0] myram0_3_0_wdata;
  reg myram0_3_0_wenable;

  myram0_3
  inst_myram0_3
  (
    .CLK(CLK),
    .myram0_3_0_addr(myram0_3_0_addr),
    .myram0_3_0_rdata(myram0_3_0_rdata),
    .myram0_3_0_wdata(myram0_3_0_wdata),
    .myram0_3_0_wenable(myram0_3_0_wenable)
  );

  reg [10-1:0] myram1_0_0_addr;
  wire [32-1:0] myram1_0_0_rdata;
  reg [32-1:0] myram1_0_0_wdata;
  reg myram1_0_0_wenable;

  myram1_0
  inst_myram1_0
  (
    .CLK(CLK),
    .myram1_0_0_addr(myram1_0_0_addr),
    .myram1_0_0_rdata(myram1_0_0_rdata),
    .myram1_0_0_wdata(myram1_0_0_wdata),
    .myram1_0_0_wenable(myram1_0_0_wenable)
  );

  reg [10-1:0] myram1_1_0_addr;
  wire [32-1:0] myram1_1_0_rdata;
  reg [32-1:0] myram1_1_0_wdata;
  reg myram1_1_0_wenable;

  myram1_1
  inst_myram1_1
  (
    .CLK(CLK),
    .myram1_1_0_addr(myram1_1_0_addr),
    .myram1_1_0_rdata(myram1_1_0_rdata),
    .myram1_1_0_wdata(myram1_1_0_wdata),
    .myram1_1_0_wenable(myram1_1_0_wenable)
  );

  reg [10-1:0] myram1_2_0_addr;
  wire [32-1:0] myram1_2_0_rdata;
  reg [32-1:0] myram1_2_0_wdata;
  reg myram1_2_0_wenable;

  myram1_2
  inst_myram1_2
  (
    .CLK(CLK),
    .myram1_2_0_addr(myram1_2_0_addr),
    .myram1_2_0_rdata(myram1_2_0_rdata),
    .myram1_2_0_wdata(myram1_2_0_wdata),
    .myram1_2_0_wenable(myram1_2_0_wenable)
  );

  reg [10-1:0] myram1_3_0_addr;
  wire [32-1:0] myram1_3_0_rdata;
  reg [32-1:0] myram1_3_0_wdata;
  reg myram1_3_0_wenable;

  myram1_3
  inst_myram1_3
  (
    .CLK(CLK),
    .myram1_3_0_addr(myram1_3_0_addr),
    .myram1_3_0_rdata(myram1_3_0_rdata),
    .myram1_3_0_wdata(myram1_3_0_wdata),
    .myram1_3_0_wenable(myram1_3_0_wenable)
  );

  reg _tmp_0;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_offset_1;
  reg signed [32-1:0] _th_blink_size_2;
  reg signed [32-1:0] _th_blink_offset_3;
  reg signed [32-1:0] _th_blink_count_4;
  reg signed [32-1:0] _th_blink_blk_offset_5;
  reg signed [32-1:0] _th_blink_bias_6;
  reg signed [32-1:0] _th_blink_done_7;
  reg signed [32-1:0] _th_blink_bank_8;
  reg signed [32-1:0] _th_blink_i_9;
  reg signed [32-1:0] _th_blink_wdata_10;
  wire [2-1:0] _tmp_1;
  assign _tmp_1 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _myram0_0_cond_0_1;
  reg _myram0_1_cond_0_1;
  reg _myram0_2_cond_0_1;
  reg _myram0_3_cond_0_1;
  wire [2-1:0] _tmp_2;
  assign _tmp_2 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _myram1_0_cond_0_1;
  reg _myram1_1_cond_0_1;
  reg _myram1_2_cond_0_1;
  reg _myram1_3_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_11;
  reg signed [32-1:0] _th_blink_gaddr_12;
  reg [10-1:0] req_block_size_3;
  reg set_req_4;
  reg [32-1:0] _d1_th_blink;
  reg _th_blink_cond_29_0_1;
  reg axim_flag_5;
  reg _th_blink_cond_30_1_1;
  reg _myaxi_myram0_myram1_0_write_start;
  reg [8-1:0] _myaxi_myram0_myram1_0_write_op_sel;
  reg [32-1:0] _myaxi_myram0_myram1_0_write_local_addr;
  reg [32-1:0] _myaxi_myram0_myram1_0_write_global_addr;
  reg [33-1:0] _myaxi_myram0_myram1_0_write_size;
  reg [32-1:0] _myaxi_myram0_myram1_0_write_local_stride;
  reg [32-1:0] _myaxi_write_fsm;
  localparam _myaxi_write_fsm_init = 0;
  reg [32-1:0] _myaxi_write_cur_global_addr;
  reg [33-1:0] _myaxi_write_cur_size;
  reg [33-1:0] _myaxi_write_rest_size;
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
  wire signed [32-1:0] _tmp_13;
  reg signed [32-1:0] __tmp_12_1;
  reg signed [32-1:0] __tmp_13_1;
  assign _tmp_12 = (__tmp_11_1)? myram0_0_0_rdata : __tmp_12_1;
  assign _tmp_13 = (__tmp_11_1)? myram1_0_0_rdata : __tmp_13_1;
  reg [10-1:0] _tmp_14;
  reg [10-1:0] _tmp_15;
  wire [10-1:0] _tmp_16;
  wire [10-1:0] _tmp_17;
  assign _tmp_16 = _tmp_14 + _myaxi_write_local_stride;
  assign _tmp_17 = _tmp_15 + _myaxi_write_local_stride;
  wire [10-1:0] _tmp_18;
  wire [10-1:0] _tmp_19;
  assign _tmp_18 = _tmp_16;
  assign _tmp_19 = _tmp_17;
  reg [1-1:0] _tmp_20;
  reg [1-1:0] _tmp_21;
  reg [1-1:0] __tmp_21_1;
  wire signed [32-1:0] _tmp_22;
  assign _tmp_22 = (__tmp_11_1)? (_tmp_21 == 0)? _tmp_12 : 
                   (_tmp_21 == 1)? _tmp_13 : 0 : 
                   (__tmp_21_1 == 0)? __tmp_12_1 : 
                   (__tmp_21_1 == 1)? __tmp_13_1 : 0;
  reg _tmp_23;
  reg _tmp_24;
  reg _tmp_25;
  reg _tmp_26;
  reg [11-1:0] _tmp_27;
  reg [34-1:0] _tmp_28;
  reg _tmp_29;
  reg _tmp_30;
  wire _tmp_31;
  wire _tmp_32;
  assign _tmp_32 = 1;
  localparam _tmp_33 = 1;
  wire [_tmp_33-1:0] _tmp_34;
  assign _tmp_34 = (_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30);
  reg [_tmp_33-1:0] __tmp_34_1;
  wire signed [32-1:0] _tmp_35;
  wire signed [32-1:0] _tmp_36;
  reg signed [32-1:0] __tmp_35_1;
  reg signed [32-1:0] __tmp_36_1;
  assign _tmp_35 = (__tmp_34_1)? myram0_1_0_rdata : __tmp_35_1;
  assign _tmp_36 = (__tmp_34_1)? myram1_1_0_rdata : __tmp_36_1;
  reg [10-1:0] _tmp_37;
  reg [10-1:0] _tmp_38;
  wire [10-1:0] _tmp_39;
  wire [10-1:0] _tmp_40;
  assign _tmp_39 = _tmp_37 + _myaxi_write_local_stride;
  assign _tmp_40 = _tmp_38 + _myaxi_write_local_stride;
  wire [10-1:0] _tmp_41;
  wire [10-1:0] _tmp_42;
  assign _tmp_41 = _tmp_39;
  assign _tmp_42 = _tmp_40;
  reg [1-1:0] _tmp_43;
  reg [1-1:0] _tmp_44;
  reg [1-1:0] __tmp_44_1;
  wire signed [32-1:0] _tmp_45;
  assign _tmp_45 = (__tmp_34_1)? (_tmp_44 == 0)? _tmp_35 : 
                   (_tmp_44 == 1)? _tmp_36 : 0 : 
                   (__tmp_44_1 == 0)? __tmp_35_1 : 
                   (__tmp_44_1 == 1)? __tmp_36_1 : 0;
  reg _tmp_46;
  reg _tmp_47;
  reg _tmp_48;
  reg _tmp_49;
  reg [11-1:0] _tmp_50;
  reg [34-1:0] _tmp_51;
  reg _tmp_52;
  reg _tmp_53;
  wire _tmp_54;
  wire _tmp_55;
  assign _tmp_55 = 1;
  localparam _tmp_56 = 1;
  wire [_tmp_56-1:0] _tmp_57;
  assign _tmp_57 = (_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53);
  reg [_tmp_56-1:0] __tmp_57_1;
  wire signed [32-1:0] _tmp_58;
  wire signed [32-1:0] _tmp_59;
  reg signed [32-1:0] __tmp_58_1;
  reg signed [32-1:0] __tmp_59_1;
  assign _tmp_58 = (__tmp_57_1)? myram0_2_0_rdata : __tmp_58_1;
  assign _tmp_59 = (__tmp_57_1)? myram1_2_0_rdata : __tmp_59_1;
  reg [10-1:0] _tmp_60;
  reg [10-1:0] _tmp_61;
  wire [10-1:0] _tmp_62;
  wire [10-1:0] _tmp_63;
  assign _tmp_62 = _tmp_60 + _myaxi_write_local_stride;
  assign _tmp_63 = _tmp_61 + _myaxi_write_local_stride;
  wire [10-1:0] _tmp_64;
  wire [10-1:0] _tmp_65;
  assign _tmp_64 = _tmp_62;
  assign _tmp_65 = _tmp_63;
  reg [1-1:0] _tmp_66;
  reg [1-1:0] _tmp_67;
  reg [1-1:0] __tmp_67_1;
  wire signed [32-1:0] _tmp_68;
  assign _tmp_68 = (__tmp_57_1)? (_tmp_67 == 0)? _tmp_58 : 
                   (_tmp_67 == 1)? _tmp_59 : 0 : 
                   (__tmp_67_1 == 0)? __tmp_58_1 : 
                   (__tmp_67_1 == 1)? __tmp_59_1 : 0;
  reg _tmp_69;
  reg _tmp_70;
  reg _tmp_71;
  reg _tmp_72;
  reg [11-1:0] _tmp_73;
  reg [34-1:0] _tmp_74;
  reg _tmp_75;
  reg _tmp_76;
  wire _tmp_77;
  wire _tmp_78;
  assign _tmp_78 = 1;
  localparam _tmp_79 = 1;
  wire [_tmp_79-1:0] _tmp_80;
  assign _tmp_80 = (_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76);
  reg [_tmp_79-1:0] __tmp_80_1;
  wire signed [32-1:0] _tmp_81;
  wire signed [32-1:0] _tmp_82;
  reg signed [32-1:0] __tmp_81_1;
  reg signed [32-1:0] __tmp_82_1;
  assign _tmp_81 = (__tmp_80_1)? myram0_3_0_rdata : __tmp_81_1;
  assign _tmp_82 = (__tmp_80_1)? myram1_3_0_rdata : __tmp_82_1;
  reg [10-1:0] _tmp_83;
  reg [10-1:0] _tmp_84;
  wire [10-1:0] _tmp_85;
  wire [10-1:0] _tmp_86;
  assign _tmp_85 = _tmp_83 + _myaxi_write_local_stride;
  assign _tmp_86 = _tmp_84 + _myaxi_write_local_stride;
  wire [10-1:0] _tmp_87;
  wire [10-1:0] _tmp_88;
  assign _tmp_87 = _tmp_85;
  assign _tmp_88 = _tmp_86;
  reg [1-1:0] _tmp_89;
  reg [1-1:0] _tmp_90;
  reg [1-1:0] __tmp_90_1;
  wire signed [32-1:0] _tmp_91;
  assign _tmp_91 = (__tmp_80_1)? (_tmp_90 == 0)? _tmp_81 : 
                   (_tmp_90 == 1)? _tmp_82 : 0 : 
                   (__tmp_90_1 == 0)? __tmp_81_1 : 
                   (__tmp_90_1 == 1)? __tmp_82_1 : 0;
  reg _tmp_92;
  reg _tmp_93;
  reg _tmp_94;
  reg _tmp_95;
  reg [11-1:0] _tmp_96;
  reg [34-1:0] _tmp_97;
  reg [9-1:0] _tmp_98;
  reg _myaxi_cond_0_1;
  reg _tmp_99;
  wire [128-1:0] _cat_data_100;
  wire _cat_valid_100;
  wire _cat_ready_100;
  assign _cat_ready_100 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  assign _myaxi_write_data_done = (_tmp_99 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_101;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  wire [2-1:0] _tmp_102;
  assign _tmp_102 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _myram0_0_cond_1_1;
  reg _myram0_1_cond_1_1;
  reg _myram0_2_cond_1_1;
  reg _myram0_3_cond_1_1;
  wire [2-1:0] _tmp_103;
  assign _tmp_103 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _myram1_0_cond_1_1;
  reg _myram1_1_cond_1_1;
  reg _myram1_2_cond_1_1;
  reg _myram1_3_cond_1_1;
  reg set_req_104;
  reg _th_blink_cond_59_2_1;
  reg axim_flag_105;
  reg _th_blink_cond_60_3_1;
  reg set_req_106;
  reg _th_blink_cond_67_4_1;
  reg axim_flag_107;
  reg _th_blink_cond_68_5_1;
  reg _myaxi_myram0_myram1_0_read_start;
  reg [8-1:0] _myaxi_myram0_myram1_0_read_op_sel;
  reg [32-1:0] _myaxi_myram0_myram1_0_read_local_addr;
  reg [32-1:0] _myaxi_myram0_myram1_0_read_global_addr;
  reg [33-1:0] _myaxi_myram0_myram1_0_read_size;
  reg [32-1:0] _myaxi_myram0_myram1_0_read_local_stride;
  reg [32-1:0] _myaxi_read_fsm;
  localparam _myaxi_read_fsm_init = 0;
  reg [32-1:0] _myaxi_read_cur_global_addr;
  reg [33-1:0] _myaxi_read_cur_size;
  reg [33-1:0] _myaxi_read_rest_size;
  reg [128-1:0] _wdata_108;
  reg _wvalid_109;
  reg [11-1:0] _tmp_110;
  reg [34-1:0] _tmp_111;
  reg _tmp_112;
  wire [32-1:0] _slice_data_113;
  wire _slice_valid_113;
  wire _slice_ready_113;
  assign _slice_ready_113 = (_tmp_111 > 0) && !_tmp_112;
  reg [10-1:0] _tmp_114;
  reg [10-1:0] _tmp_115;
  wire [10-1:0] _tmp_116;
  wire [10-1:0] _tmp_117;
  assign _tmp_116 = _tmp_114 + _myaxi_read_local_stride;
  assign _tmp_117 = _tmp_115 + _myaxi_read_local_stride;
  wire [10-1:0] _tmp_118;
  wire [10-1:0] _tmp_119;
  assign _tmp_118 = _tmp_116;
  assign _tmp_119 = _tmp_117;
  reg [1-1:0] _tmp_120;
  reg _myram0_0_cond_2_1;
  reg _myram0_0_cond_3_1;
  reg _myram1_0_cond_2_1;
  reg [11-1:0] _tmp_121;
  reg [34-1:0] _tmp_122;
  reg _tmp_123;
  wire [32-1:0] _slice_data_124;
  wire _slice_valid_124;
  wire _slice_ready_124;
  assign _slice_ready_124 = (_tmp_122 > 0) && !_tmp_123;
  reg [10-1:0] _tmp_125;
  reg [10-1:0] _tmp_126;
  wire [10-1:0] _tmp_127;
  wire [10-1:0] _tmp_128;
  assign _tmp_127 = _tmp_125 + _myaxi_read_local_stride;
  assign _tmp_128 = _tmp_126 + _myaxi_read_local_stride;
  wire [10-1:0] _tmp_129;
  wire [10-1:0] _tmp_130;
  assign _tmp_129 = _tmp_127;
  assign _tmp_130 = _tmp_128;
  reg [1-1:0] _tmp_131;
  reg _myram0_1_cond_2_1;
  reg _myram0_1_cond_3_1;
  reg _myram1_1_cond_2_1;
  reg [11-1:0] _tmp_132;
  reg [34-1:0] _tmp_133;
  reg _tmp_134;
  wire [32-1:0] _slice_data_135;
  wire _slice_valid_135;
  wire _slice_ready_135;
  assign _slice_ready_135 = (_tmp_133 > 0) && !_tmp_134;
  reg [10-1:0] _tmp_136;
  reg [10-1:0] _tmp_137;
  wire [10-1:0] _tmp_138;
  wire [10-1:0] _tmp_139;
  assign _tmp_138 = _tmp_136 + _myaxi_read_local_stride;
  assign _tmp_139 = _tmp_137 + _myaxi_read_local_stride;
  wire [10-1:0] _tmp_140;
  wire [10-1:0] _tmp_141;
  assign _tmp_140 = _tmp_138;
  assign _tmp_141 = _tmp_139;
  reg [1-1:0] _tmp_142;
  reg _myram0_2_cond_2_1;
  reg _myram0_2_cond_3_1;
  reg _myram1_2_cond_2_1;
  reg [11-1:0] _tmp_143;
  reg [34-1:0] _tmp_144;
  reg _tmp_145;
  wire [32-1:0] _slice_data_146;
  wire _slice_valid_146;
  wire _slice_ready_146;
  assign _slice_ready_146 = (_tmp_144 > 0) && !_tmp_145;
  reg [10-1:0] _tmp_147;
  reg [10-1:0] _tmp_148;
  wire [10-1:0] _tmp_149;
  wire [10-1:0] _tmp_150;
  assign _tmp_149 = _tmp_147 + _myaxi_read_local_stride;
  assign _tmp_150 = _tmp_148 + _myaxi_read_local_stride;
  wire [10-1:0] _tmp_151;
  wire [10-1:0] _tmp_152;
  assign _tmp_151 = _tmp_149;
  assign _tmp_152 = _tmp_150;
  reg [1-1:0] _tmp_153;
  reg _myram0_3_cond_2_1;
  reg _myram0_3_cond_3_1;
  reg _myram1_3_cond_2_1;
  reg [9-1:0] _tmp_154;
  reg _myaxi_cond_2_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_155;
  reg __myaxi_read_fsm_cond_4_1_1;
  wire [2-1:0] _tmp_156;
  assign _tmp_156 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _tmp_157;
  reg _myram0_0_cond_4_1;
  reg _myram0_0_cond_5_1;
  reg _myram0_0_cond_5_2;
  reg _tmp_158;
  reg _myram0_1_cond_4_1;
  reg _myram0_1_cond_5_1;
  reg _myram0_1_cond_5_2;
  reg _tmp_159;
  reg _myram0_2_cond_4_1;
  reg _myram0_2_cond_5_1;
  reg _myram0_2_cond_5_2;
  reg _tmp_160;
  reg _myram0_3_cond_4_1;
  reg _myram0_3_cond_5_1;
  reg _myram0_3_cond_5_2;
  wire signed [32-1:0] _tmp_161;
  assign _tmp_161 = (_tmp_156 == 0)? myram0_0_0_rdata : 
                    (_tmp_156 == 1)? myram0_1_0_rdata : 
                    (_tmp_156 == 2)? myram0_2_0_rdata : 
                    (_tmp_156 == 3)? myram0_3_0_rdata : 0;
  wire [2-1:0] _tmp_162;
  assign _tmp_162 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _tmp_163;
  reg _myram1_0_cond_3_1;
  reg _myram1_0_cond_4_1;
  reg _myram1_0_cond_4_2;
  reg _tmp_164;
  reg _myram1_1_cond_3_1;
  reg _myram1_1_cond_4_1;
  reg _myram1_1_cond_4_2;
  reg _tmp_165;
  reg _myram1_2_cond_3_1;
  reg _myram1_2_cond_4_1;
  reg _myram1_2_cond_4_2;
  reg _tmp_166;
  reg _myram1_3_cond_3_1;
  reg _myram1_3_cond_4_1;
  reg _myram1_3_cond_4_2;
  wire signed [32-1:0] _tmp_167;
  assign _tmp_167 = (_tmp_162 == 0)? myram1_0_0_rdata : 
                    (_tmp_162 == 1)? myram1_1_0_rdata : 
                    (_tmp_162 == 2)? myram1_2_0_rdata : 
                    (_tmp_162 == 3)? myram1_3_0_rdata : 0;
  reg signed [128-1:0] _tmp_168;
  reg signed [32-1:0] _th_blink_rdata_13;
  reg signed [32-1:0] _th_blink_exp_14;
  reg set_req_169;
  reg _th_blink_cond_101_6_1;
  reg axim_flag_170;
  reg _th_blink_cond_102_7_1;
  wire [2-1:0] _tmp_171;
  assign _tmp_171 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _tmp_172;
  reg _myram0_0_cond_6_1;
  reg _myram0_0_cond_7_1;
  reg _myram0_0_cond_7_2;
  reg _tmp_173;
  reg _myram0_1_cond_6_1;
  reg _myram0_1_cond_7_1;
  reg _myram0_1_cond_7_2;
  reg _tmp_174;
  reg _myram0_2_cond_6_1;
  reg _myram0_2_cond_7_1;
  reg _myram0_2_cond_7_2;
  reg _tmp_175;
  reg _myram0_3_cond_6_1;
  reg _myram0_3_cond_7_1;
  reg _myram0_3_cond_7_2;
  wire signed [32-1:0] _tmp_176;
  assign _tmp_176 = (_tmp_171 == 0)? myram0_0_0_rdata : 
                    (_tmp_171 == 1)? myram0_1_0_rdata : 
                    (_tmp_171 == 2)? myram0_2_0_rdata : 
                    (_tmp_171 == 3)? myram0_3_0_rdata : 0;
  wire [2-1:0] _tmp_177;
  assign _tmp_177 = _th_blink_blk_offset_5 + _th_blink_i_9;
  reg _tmp_178;
  reg _myram1_0_cond_5_1;
  reg _myram1_0_cond_6_1;
  reg _myram1_0_cond_6_2;
  reg _tmp_179;
  reg _myram1_1_cond_5_1;
  reg _myram1_1_cond_6_1;
  reg _myram1_1_cond_6_2;
  reg _tmp_180;
  reg _myram1_2_cond_5_1;
  reg _myram1_2_cond_6_1;
  reg _myram1_2_cond_6_2;
  reg _tmp_181;
  reg _myram1_3_cond_5_1;
  reg _myram1_3_cond_6_1;
  reg _myram1_3_cond_6_2;
  wire signed [32-1:0] _tmp_182;
  assign _tmp_182 = (_tmp_177 == 0)? myram1_0_0_rdata : 
                    (_tmp_177 == 1)? myram1_1_0_rdata : 
                    (_tmp_177 == 2)? myram1_2_0_rdata : 
                    (_tmp_177 == 3)? myram1_3_0_rdata : 0;
  reg signed [128-1:0] _tmp_183;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram0_myram1_0_write_start <= 0;
      _myaxi_myram0_myram1_0_write_op_sel <= 0;
      _myaxi_myram0_myram1_0_write_local_addr <= 0;
      _myaxi_myram0_myram1_0_write_global_addr <= 0;
      _myaxi_myram0_myram1_0_write_size <= 0;
      _myaxi_myram0_myram1_0_write_local_stride <= 0;
      _myaxi_write_idle <= 1;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_size <= 0;
      _myaxi_write_local_stride <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_98 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_99 <= 0;
      _myaxi_cond_1_1 <= 0;
      _myaxi_myram0_myram1_0_read_start <= 0;
      _myaxi_myram0_myram1_0_read_op_sel <= 0;
      _myaxi_myram0_myram1_0_read_local_addr <= 0;
      _myaxi_myram0_myram1_0_read_global_addr <= 0;
      _myaxi_myram0_myram1_0_read_size <= 0;
      _myaxi_myram0_myram1_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_154 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_99 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_arvalid <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram0_myram1_0_write_start <= 0;
      if(axim_flag_5) begin
        _myaxi_myram0_myram1_0_write_start <= 1;
        _myaxi_myram0_myram1_0_write_op_sel <= 1;
        _myaxi_myram0_myram1_0_write_local_addr <= _th_blink_laddr_11;
        _myaxi_myram0_myram1_0_write_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram0_myram1_0_write_size <= _th_blink_size_2 >>> 2;
        _myaxi_myram0_myram1_0_write_local_stride <= 1;
      end 
      if(_myaxi_myram0_myram1_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_myram0_myram1_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_myram0_myram1_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_myram0_myram1_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_myram0_myram1_0_write_global_addr;
        _myaxi_write_size <= _myaxi_myram0_myram1_0_write_size;
        _myaxi_write_local_stride <= _myaxi_myram0_myram1_0_write_local_stride;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_98 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_98 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_98 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_cat_valid_100 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_98 > 0))) begin
        myaxi_wdata <= _cat_data_100;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 16{ 1'd1 } };
        _tmp_98 <= _tmp_98 - 1;
      end 
      if(_cat_valid_100 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_98 > 0)) && (_tmp_98 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_99 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_99 <= _tmp_99;
      end 
      if(axim_flag_101) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_105) begin
        _myaxi_myram0_myram1_0_write_start <= 1;
        _myaxi_myram0_myram1_0_write_op_sel <= 1;
        _myaxi_myram0_myram1_0_write_local_addr <= _th_blink_laddr_11;
        _myaxi_myram0_myram1_0_write_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram0_myram1_0_write_size <= _th_blink_size_2 >>> 2;
        _myaxi_myram0_myram1_0_write_local_stride <= 1;
      end 
      _myaxi_myram0_myram1_0_read_start <= 0;
      if(axim_flag_107) begin
        _myaxi_myram0_myram1_0_read_start <= 1;
        _myaxi_myram0_myram1_0_read_op_sel <= 1;
        _myaxi_myram0_myram1_0_read_local_addr <= _th_blink_laddr_11;
        _myaxi_myram0_myram1_0_read_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram0_myram1_0_read_size <= _th_blink_size_2 >>> 2;
        _myaxi_myram0_myram1_0_read_local_stride <= 1;
      end 
      if(_myaxi_myram0_myram1_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_myram0_myram1_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_myram0_myram1_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_myram0_myram1_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_myram0_myram1_0_read_global_addr;
        _myaxi_read_size <= _myaxi_myram0_myram1_0_read_size;
        _myaxi_read_local_stride <= _myaxi_myram0_myram1_0_read_local_stride;
      end 
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_154 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_154 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_154 > 0)) begin
        _tmp_154 <= _tmp_154 - 1;
      end 
      if(axim_flag_155) begin
        _myaxi_read_idle <= 1;
      end 
      if(axim_flag_170) begin
        _myaxi_myram0_myram1_0_read_start <= 1;
        _myaxi_myram0_myram1_0_read_op_sel <= 1;
        _myaxi_myram0_myram1_0_read_local_addr <= _th_blink_laddr_11;
        _myaxi_myram0_myram1_0_read_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram0_myram1_0_read_size <= _th_blink_size_2 >>> 2;
        _myaxi_myram0_myram1_0_read_local_stride <= 1;
      end 
    end
  end

  reg [32-1:0] _slice_data_184;
  reg _slice_valid_184;
  wire _slice_ready_184;
  reg [32-1:0] _slice_data_185;
  reg _slice_valid_185;
  wire _slice_ready_185;
  reg [32-1:0] _slice_data_186;
  reg _slice_valid_186;
  wire _slice_ready_186;
  reg [32-1:0] _slice_data_187;
  reg _slice_valid_187;
  wire _slice_ready_187;
  assign _slice_data_113 = _slice_data_184;
  assign _slice_valid_113 = _slice_valid_184;
  assign _slice_ready_184 = _slice_ready_113;
  assign _slice_data_124 = _slice_data_185;
  assign _slice_valid_124 = _slice_valid_185;
  assign _slice_ready_185 = _slice_ready_124;
  assign _slice_data_135 = _slice_data_186;
  assign _slice_valid_135 = _slice_valid_186;
  assign _slice_ready_186 = _slice_ready_135;
  assign _slice_data_146 = _slice_data_187;
  assign _slice_valid_146 = _slice_valid_187;
  assign _slice_ready_187 = _slice_ready_146;

  always @(posedge CLK) begin
    if(RST) begin
      _slice_data_184 <= 0;
      _slice_valid_184 <= 0;
      _slice_data_185 <= 0;
      _slice_valid_185 <= 0;
      _slice_data_186 <= 0;
      _slice_valid_186 <= 0;
      _slice_data_187 <= 0;
      _slice_valid_187 <= 0;
    end else begin
      if((_slice_ready_184 || !_slice_valid_184) && 1 && _wvalid_109) begin
        _slice_data_184 <= _wdata_108[6'd31:1'd0];
      end 
      if(_slice_valid_184 && _slice_ready_184) begin
        _slice_valid_184 <= 0;
      end 
      if((_slice_ready_184 || !_slice_valid_184) && 1) begin
        _slice_valid_184 <= _wvalid_109;
      end 
      if((_slice_ready_185 || !_slice_valid_185) && 1 && _wvalid_109) begin
        _slice_data_185 <= _wdata_108[7'd63:7'd32];
      end 
      if(_slice_valid_185 && _slice_ready_185) begin
        _slice_valid_185 <= 0;
      end 
      if((_slice_ready_185 || !_slice_valid_185) && 1) begin
        _slice_valid_185 <= _wvalid_109;
      end 
      if((_slice_ready_186 || !_slice_valid_186) && 1 && _wvalid_109) begin
        _slice_data_186 <= _wdata_108[8'd95:8'd64];
      end 
      if(_slice_valid_186 && _slice_ready_186) begin
        _slice_valid_186 <= 0;
      end 
      if((_slice_ready_186 || !_slice_valid_186) && 1) begin
        _slice_valid_186 <= _wvalid_109;
      end 
      if((_slice_ready_187 || !_slice_valid_187) && 1 && _wvalid_109) begin
        _slice_data_187 <= _wdata_108[8'd127:8'd96];
      end 
      if(_slice_valid_187 && _slice_ready_187) begin
        _slice_valid_187 <= 0;
      end 
      if((_slice_ready_187 || !_slice_valid_187) && 1) begin
        _slice_valid_187 <= _wvalid_109;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_0_0_addr <= 0;
      myram0_0_0_wdata <= 0;
      myram0_0_0_wenable <= 0;
      _myram0_0_cond_0_1 <= 0;
      __tmp_11_1 <= 0;
      __tmp_12_1 <= 0;
      __tmp_13_1 <= 0;
      __tmp_21_1 <= 0;
      _tmp_21 <= 0;
      _tmp_26 <= 0;
      _tmp_6 <= 0;
      _tmp_7 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_23 <= 0;
      _tmp_20 <= 0;
      _tmp_27 <= 0;
      _tmp_28 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _myram0_0_cond_1_1 <= 0;
      _tmp_120 <= 0;
      _tmp_110 <= 0;
      _tmp_111 <= 0;
      _tmp_114 <= 0;
      _tmp_115 <= 0;
      _tmp_112 <= 0;
      _myram0_0_cond_2_1 <= 0;
      _myram0_0_cond_3_1 <= 0;
      _myram0_0_cond_4_1 <= 0;
      _tmp_157 <= 0;
      _myram0_0_cond_5_1 <= 0;
      _myram0_0_cond_5_2 <= 0;
      _myram0_0_cond_6_1 <= 0;
      _tmp_172 <= 0;
      _myram0_0_cond_7_1 <= 0;
      _myram0_0_cond_7_2 <= 0;
    end else begin
      if(_myram0_0_cond_5_2) begin
        _tmp_157 <= 0;
      end 
      if(_myram0_0_cond_7_2) begin
        _tmp_172 <= 0;
      end 
      if(_myram0_0_cond_0_1) begin
        myram0_0_0_wenable <= 0;
      end 
      if(_myram0_0_cond_1_1) begin
        myram0_0_0_wenable <= 0;
      end 
      if(_myram0_0_cond_2_1) begin
        _tmp_112 <= 0;
      end 
      if(_myram0_0_cond_3_1) begin
        myram0_0_0_wenable <= 0;
      end 
      if(_myram0_0_cond_4_1) begin
        _tmp_157 <= 1;
      end 
      _myram0_0_cond_5_2 <= _myram0_0_cond_5_1;
      if(_myram0_0_cond_6_1) begin
        _tmp_172 <= 1;
      end 
      _myram0_0_cond_7_2 <= _myram0_0_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 0)) begin
        myram0_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_0_0_wdata <= _th_blink_wdata_10;
        myram0_0_0_wenable <= 1;
      end 
      _myram0_0_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 0);
      __tmp_11_1 <= _tmp_11;
      __tmp_12_1 <= _tmp_12;
      __tmp_13_1 <= _tmp_13;
      __tmp_21_1 <= _tmp_21;
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7)) begin
        _tmp_21 <= _tmp_20;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && _tmp_24) begin
        _tmp_26 <= 0;
        _tmp_6 <= 0;
        _tmp_7 <= 0;
        _tmp_24 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && _tmp_23) begin
        _tmp_6 <= 1;
        _tmp_7 <= 1;
        _tmp_26 <= _tmp_25;
        _tmp_25 <= 0;
        _tmp_23 <= 0;
        _tmp_24 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_28 == 0) && !_tmp_25 && !_tmp_26) begin
        _tmp_20 <= 0;
        _tmp_21 <= 0;
        _tmp_27 <= req_block_size_3 - 1;
        _tmp_28 <= _myaxi_write_size - 1;
        _tmp_23 <= 1;
        _tmp_25 <= _myaxi_write_size == 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_28 == 0) && !_tmp_25 && !_tmp_26) begin
        _tmp_14 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_28 == 0) && !_tmp_25 && !_tmp_26) begin
        _tmp_15 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_28 == 0) && !_tmp_25 && !_tmp_26) begin
        myram0_0_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0)) begin
        _tmp_27 <= _tmp_27 - 1;
        _tmp_28 <= _tmp_28 - 1;
        _tmp_23 <= 1;
        _tmp_25 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0) && (_tmp_27 == 0)) begin
        _tmp_27 <= req_block_size_3 - 1;
        _tmp_20 <= _tmp_20 + 1;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0) && (_tmp_27 == 0) && (_tmp_20 == 1)) begin
        _tmp_20 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0) && (_tmp_20 == 0)) begin
        _tmp_14 <= _tmp_16;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0) && (_tmp_20 == 1)) begin
        _tmp_15 <= _tmp_17;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0) && (_tmp_20 == 0)) begin
        myram0_0_0_addr <= _tmp_18;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 == 1)) begin
        _tmp_25 <= 1;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 0)) begin
        myram0_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_0_0_wdata <= _th_blink_wdata_10;
        myram0_0_0_wenable <= 1;
      end 
      _myram0_0_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 0);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_111 == 0)) begin
        _tmp_120 <= 0;
        _tmp_110 <= req_block_size_3 - 1;
        _tmp_111 <= _myaxi_read_size;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_111 == 0)) begin
        _tmp_114 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_111 == 0)) begin
        _tmp_115 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0)) begin
        _tmp_110 <= _tmp_110 - 1;
        _tmp_111 <= _tmp_111 - 1;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0) && (_tmp_110 == 0)) begin
        _tmp_110 <= req_block_size_3 - 1;
        _tmp_120 <= _tmp_120 + 1;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0) && (_tmp_110 == 0) && (_tmp_120 == 1)) begin
        _tmp_120 <= 0;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0) && (_tmp_120 == 0)) begin
        _tmp_114 <= _tmp_116;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0) && (_tmp_120 == 1)) begin
        _tmp_115 <= _tmp_117;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0)) begin
        myram0_0_0_addr <= _tmp_118;
        myram0_0_0_wdata <= _slice_data_113;
        myram0_0_0_wenable <= _tmp_120 == 0;
      end 
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 == 1)) begin
        _tmp_112 <= 1;
      end 
      _myram0_0_cond_2_1 <= 1;
      _myram0_0_cond_3_1 <= 1;
      if(th_blink == 82) begin
        myram0_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_0_cond_4_1 <= th_blink == 82;
      _myram0_0_cond_5_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram0_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_0_cond_6_1 <= th_blink == 116;
      _myram0_0_cond_7_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_1_0_addr <= 0;
      myram0_1_0_wdata <= 0;
      myram0_1_0_wenable <= 0;
      _myram0_1_cond_0_1 <= 0;
      __tmp_34_1 <= 0;
      __tmp_35_1 <= 0;
      __tmp_36_1 <= 0;
      __tmp_44_1 <= 0;
      _tmp_44 <= 0;
      _tmp_49 <= 0;
      _tmp_29 <= 0;
      _tmp_30 <= 0;
      _tmp_47 <= 0;
      _tmp_48 <= 0;
      _tmp_46 <= 0;
      _tmp_43 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _myram0_1_cond_1_1 <= 0;
      _tmp_131 <= 0;
      _tmp_121 <= 0;
      _tmp_122 <= 0;
      _tmp_125 <= 0;
      _tmp_126 <= 0;
      _tmp_123 <= 0;
      _myram0_1_cond_2_1 <= 0;
      _myram0_1_cond_3_1 <= 0;
      _myram0_1_cond_4_1 <= 0;
      _tmp_158 <= 0;
      _myram0_1_cond_5_1 <= 0;
      _myram0_1_cond_5_2 <= 0;
      _myram0_1_cond_6_1 <= 0;
      _tmp_173 <= 0;
      _myram0_1_cond_7_1 <= 0;
      _myram0_1_cond_7_2 <= 0;
    end else begin
      if(_myram0_1_cond_5_2) begin
        _tmp_158 <= 0;
      end 
      if(_myram0_1_cond_7_2) begin
        _tmp_173 <= 0;
      end 
      if(_myram0_1_cond_0_1) begin
        myram0_1_0_wenable <= 0;
      end 
      if(_myram0_1_cond_1_1) begin
        myram0_1_0_wenable <= 0;
      end 
      if(_myram0_1_cond_2_1) begin
        _tmp_123 <= 0;
      end 
      if(_myram0_1_cond_3_1) begin
        myram0_1_0_wenable <= 0;
      end 
      if(_myram0_1_cond_4_1) begin
        _tmp_158 <= 1;
      end 
      _myram0_1_cond_5_2 <= _myram0_1_cond_5_1;
      if(_myram0_1_cond_6_1) begin
        _tmp_173 <= 1;
      end 
      _myram0_1_cond_7_2 <= _myram0_1_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 1)) begin
        myram0_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_1_0_wdata <= _th_blink_wdata_10;
        myram0_1_0_wenable <= 1;
      end 
      _myram0_1_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 1);
      __tmp_34_1 <= _tmp_34;
      __tmp_35_1 <= _tmp_35;
      __tmp_36_1 <= _tmp_36;
      __tmp_44_1 <= _tmp_44;
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30)) begin
        _tmp_44 <= _tmp_43;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && _tmp_47) begin
        _tmp_49 <= 0;
        _tmp_29 <= 0;
        _tmp_30 <= 0;
        _tmp_47 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && _tmp_46) begin
        _tmp_29 <= 1;
        _tmp_30 <= 1;
        _tmp_49 <= _tmp_48;
        _tmp_48 <= 0;
        _tmp_46 <= 0;
        _tmp_47 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_51 == 0) && !_tmp_48 && !_tmp_49) begin
        _tmp_43 <= 0;
        _tmp_44 <= 0;
        _tmp_50 <= req_block_size_3 - 1;
        _tmp_51 <= _myaxi_write_size - 1;
        _tmp_46 <= 1;
        _tmp_48 <= _myaxi_write_size == 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_51 == 0) && !_tmp_48 && !_tmp_49) begin
        _tmp_37 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_51 == 0) && !_tmp_48 && !_tmp_49) begin
        _tmp_38 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_51 == 0) && !_tmp_48 && !_tmp_49) begin
        myram0_1_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0)) begin
        _tmp_50 <= _tmp_50 - 1;
        _tmp_51 <= _tmp_51 - 1;
        _tmp_46 <= 1;
        _tmp_48 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0) && (_tmp_50 == 0)) begin
        _tmp_50 <= req_block_size_3 - 1;
        _tmp_43 <= _tmp_43 + 1;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0) && (_tmp_50 == 0) && (_tmp_43 == 1)) begin
        _tmp_43 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0) && (_tmp_43 == 0)) begin
        _tmp_37 <= _tmp_39;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0) && (_tmp_43 == 1)) begin
        _tmp_38 <= _tmp_40;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0) && (_tmp_43 == 0)) begin
        myram0_1_0_addr <= _tmp_41;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 == 1)) begin
        _tmp_48 <= 1;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 1)) begin
        myram0_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_1_0_wdata <= _th_blink_wdata_10;
        myram0_1_0_wenable <= 1;
      end 
      _myram0_1_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 1);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_122 == 0)) begin
        _tmp_131 <= 0;
        _tmp_121 <= req_block_size_3 - 1;
        _tmp_122 <= _myaxi_read_size;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_122 == 0)) begin
        _tmp_125 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_122 == 0)) begin
        _tmp_126 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0)) begin
        _tmp_121 <= _tmp_121 - 1;
        _tmp_122 <= _tmp_122 - 1;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0) && (_tmp_121 == 0)) begin
        _tmp_121 <= req_block_size_3 - 1;
        _tmp_131 <= _tmp_131 + 1;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0) && (_tmp_121 == 0) && (_tmp_131 == 1)) begin
        _tmp_131 <= 0;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0) && (_tmp_131 == 0)) begin
        _tmp_125 <= _tmp_127;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0) && (_tmp_131 == 1)) begin
        _tmp_126 <= _tmp_128;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0)) begin
        myram0_1_0_addr <= _tmp_129;
        myram0_1_0_wdata <= _slice_data_124;
        myram0_1_0_wenable <= _tmp_131 == 0;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 == 1)) begin
        _tmp_123 <= 1;
      end 
      _myram0_1_cond_2_1 <= 1;
      _myram0_1_cond_3_1 <= 1;
      if(th_blink == 82) begin
        myram0_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_1_cond_4_1 <= th_blink == 82;
      _myram0_1_cond_5_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram0_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_1_cond_6_1 <= th_blink == 116;
      _myram0_1_cond_7_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_2_0_addr <= 0;
      myram0_2_0_wdata <= 0;
      myram0_2_0_wenable <= 0;
      _myram0_2_cond_0_1 <= 0;
      __tmp_57_1 <= 0;
      __tmp_58_1 <= 0;
      __tmp_59_1 <= 0;
      __tmp_67_1 <= 0;
      _tmp_67 <= 0;
      _tmp_72 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_69 <= 0;
      _tmp_66 <= 0;
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _myram0_2_cond_1_1 <= 0;
      _tmp_142 <= 0;
      _tmp_132 <= 0;
      _tmp_133 <= 0;
      _tmp_136 <= 0;
      _tmp_137 <= 0;
      _tmp_134 <= 0;
      _myram0_2_cond_2_1 <= 0;
      _myram0_2_cond_3_1 <= 0;
      _myram0_2_cond_4_1 <= 0;
      _tmp_159 <= 0;
      _myram0_2_cond_5_1 <= 0;
      _myram0_2_cond_5_2 <= 0;
      _myram0_2_cond_6_1 <= 0;
      _tmp_174 <= 0;
      _myram0_2_cond_7_1 <= 0;
      _myram0_2_cond_7_2 <= 0;
    end else begin
      if(_myram0_2_cond_5_2) begin
        _tmp_159 <= 0;
      end 
      if(_myram0_2_cond_7_2) begin
        _tmp_174 <= 0;
      end 
      if(_myram0_2_cond_0_1) begin
        myram0_2_0_wenable <= 0;
      end 
      if(_myram0_2_cond_1_1) begin
        myram0_2_0_wenable <= 0;
      end 
      if(_myram0_2_cond_2_1) begin
        _tmp_134 <= 0;
      end 
      if(_myram0_2_cond_3_1) begin
        myram0_2_0_wenable <= 0;
      end 
      if(_myram0_2_cond_4_1) begin
        _tmp_159 <= 1;
      end 
      _myram0_2_cond_5_2 <= _myram0_2_cond_5_1;
      if(_myram0_2_cond_6_1) begin
        _tmp_174 <= 1;
      end 
      _myram0_2_cond_7_2 <= _myram0_2_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 2)) begin
        myram0_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_2_0_wdata <= _th_blink_wdata_10;
        myram0_2_0_wenable <= 1;
      end 
      _myram0_2_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 2);
      __tmp_57_1 <= _tmp_57;
      __tmp_58_1 <= _tmp_58;
      __tmp_59_1 <= _tmp_59;
      __tmp_67_1 <= _tmp_67;
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53)) begin
        _tmp_67 <= _tmp_66;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && _tmp_70) begin
        _tmp_72 <= 0;
        _tmp_52 <= 0;
        _tmp_53 <= 0;
        _tmp_70 <= 0;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && _tmp_69) begin
        _tmp_52 <= 1;
        _tmp_53 <= 1;
        _tmp_72 <= _tmp_71;
        _tmp_71 <= 0;
        _tmp_69 <= 0;
        _tmp_70 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_74 == 0) && !_tmp_71 && !_tmp_72) begin
        _tmp_66 <= 0;
        _tmp_67 <= 0;
        _tmp_73 <= req_block_size_3 - 1;
        _tmp_74 <= _myaxi_write_size - 1;
        _tmp_69 <= 1;
        _tmp_71 <= _myaxi_write_size == 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_74 == 0) && !_tmp_71 && !_tmp_72) begin
        _tmp_60 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_74 == 0) && !_tmp_71 && !_tmp_72) begin
        _tmp_61 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_74 == 0) && !_tmp_71 && !_tmp_72) begin
        myram0_2_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0)) begin
        _tmp_73 <= _tmp_73 - 1;
        _tmp_74 <= _tmp_74 - 1;
        _tmp_69 <= 1;
        _tmp_71 <= 0;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0) && (_tmp_73 == 0)) begin
        _tmp_73 <= req_block_size_3 - 1;
        _tmp_66 <= _tmp_66 + 1;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0) && (_tmp_73 == 0) && (_tmp_66 == 1)) begin
        _tmp_66 <= 0;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0) && (_tmp_66 == 0)) begin
        _tmp_60 <= _tmp_62;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0) && (_tmp_66 == 1)) begin
        _tmp_61 <= _tmp_63;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0) && (_tmp_66 == 0)) begin
        myram0_2_0_addr <= _tmp_64;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 == 1)) begin
        _tmp_71 <= 1;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 2)) begin
        myram0_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_2_0_wdata <= _th_blink_wdata_10;
        myram0_2_0_wenable <= 1;
      end 
      _myram0_2_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 2);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_133 == 0)) begin
        _tmp_142 <= 0;
        _tmp_132 <= req_block_size_3 - 1;
        _tmp_133 <= _myaxi_read_size;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_133 == 0)) begin
        _tmp_136 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_133 == 0)) begin
        _tmp_137 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0)) begin
        _tmp_132 <= _tmp_132 - 1;
        _tmp_133 <= _tmp_133 - 1;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0) && (_tmp_132 == 0)) begin
        _tmp_132 <= req_block_size_3 - 1;
        _tmp_142 <= _tmp_142 + 1;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0) && (_tmp_132 == 0) && (_tmp_142 == 1)) begin
        _tmp_142 <= 0;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0) && (_tmp_142 == 0)) begin
        _tmp_136 <= _tmp_138;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0) && (_tmp_142 == 1)) begin
        _tmp_137 <= _tmp_139;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0)) begin
        myram0_2_0_addr <= _tmp_140;
        myram0_2_0_wdata <= _slice_data_135;
        myram0_2_0_wenable <= _tmp_142 == 0;
      end 
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 == 1)) begin
        _tmp_134 <= 1;
      end 
      _myram0_2_cond_2_1 <= 1;
      _myram0_2_cond_3_1 <= 1;
      if(th_blink == 82) begin
        myram0_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_2_cond_4_1 <= th_blink == 82;
      _myram0_2_cond_5_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram0_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_2_cond_6_1 <= th_blink == 116;
      _myram0_2_cond_7_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_3_0_addr <= 0;
      myram0_3_0_wdata <= 0;
      myram0_3_0_wenable <= 0;
      _myram0_3_cond_0_1 <= 0;
      __tmp_80_1 <= 0;
      __tmp_81_1 <= 0;
      __tmp_82_1 <= 0;
      __tmp_90_1 <= 0;
      _tmp_90 <= 0;
      _tmp_95 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_93 <= 0;
      _tmp_94 <= 0;
      _tmp_92 <= 0;
      _tmp_89 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _tmp_83 <= 0;
      _tmp_84 <= 0;
      _myram0_3_cond_1_1 <= 0;
      _tmp_153 <= 0;
      _tmp_143 <= 0;
      _tmp_144 <= 0;
      _tmp_147 <= 0;
      _tmp_148 <= 0;
      _tmp_145 <= 0;
      _myram0_3_cond_2_1 <= 0;
      _myram0_3_cond_3_1 <= 0;
      _myram0_3_cond_4_1 <= 0;
      _tmp_160 <= 0;
      _myram0_3_cond_5_1 <= 0;
      _myram0_3_cond_5_2 <= 0;
      _myram0_3_cond_6_1 <= 0;
      _tmp_175 <= 0;
      _myram0_3_cond_7_1 <= 0;
      _myram0_3_cond_7_2 <= 0;
    end else begin
      if(_myram0_3_cond_5_2) begin
        _tmp_160 <= 0;
      end 
      if(_myram0_3_cond_7_2) begin
        _tmp_175 <= 0;
      end 
      if(_myram0_3_cond_0_1) begin
        myram0_3_0_wenable <= 0;
      end 
      if(_myram0_3_cond_1_1) begin
        myram0_3_0_wenable <= 0;
      end 
      if(_myram0_3_cond_2_1) begin
        _tmp_145 <= 0;
      end 
      if(_myram0_3_cond_3_1) begin
        myram0_3_0_wenable <= 0;
      end 
      if(_myram0_3_cond_4_1) begin
        _tmp_160 <= 1;
      end 
      _myram0_3_cond_5_2 <= _myram0_3_cond_5_1;
      if(_myram0_3_cond_6_1) begin
        _tmp_175 <= 1;
      end 
      _myram0_3_cond_7_2 <= _myram0_3_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 3)) begin
        myram0_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_3_0_wdata <= _th_blink_wdata_10;
        myram0_3_0_wenable <= 1;
      end 
      _myram0_3_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 0) && (_tmp_1 == 3);
      __tmp_80_1 <= _tmp_80;
      __tmp_81_1 <= _tmp_81;
      __tmp_82_1 <= _tmp_82;
      __tmp_90_1 <= _tmp_90;
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76)) begin
        _tmp_90 <= _tmp_89;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && _tmp_93) begin
        _tmp_95 <= 0;
        _tmp_75 <= 0;
        _tmp_76 <= 0;
        _tmp_93 <= 0;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && _tmp_92) begin
        _tmp_75 <= 1;
        _tmp_76 <= 1;
        _tmp_95 <= _tmp_94;
        _tmp_94 <= 0;
        _tmp_92 <= 0;
        _tmp_93 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_97 == 0) && !_tmp_94 && !_tmp_95) begin
        _tmp_89 <= 0;
        _tmp_90 <= 0;
        _tmp_96 <= req_block_size_3 - 1;
        _tmp_97 <= _myaxi_write_size - 1;
        _tmp_92 <= 1;
        _tmp_94 <= _myaxi_write_size == 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_97 == 0) && !_tmp_94 && !_tmp_95) begin
        _tmp_83 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_97 == 0) && !_tmp_94 && !_tmp_95) begin
        _tmp_84 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_97 == 0) && !_tmp_94 && !_tmp_95) begin
        myram0_3_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0)) begin
        _tmp_96 <= _tmp_96 - 1;
        _tmp_97 <= _tmp_97 - 1;
        _tmp_92 <= 1;
        _tmp_94 <= 0;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0) && (_tmp_96 == 0)) begin
        _tmp_96 <= req_block_size_3 - 1;
        _tmp_89 <= _tmp_89 + 1;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0) && (_tmp_96 == 0) && (_tmp_89 == 1)) begin
        _tmp_89 <= 0;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0) && (_tmp_89 == 0)) begin
        _tmp_83 <= _tmp_85;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0) && (_tmp_89 == 1)) begin
        _tmp_84 <= _tmp_86;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0) && (_tmp_89 == 0)) begin
        myram0_3_0_addr <= _tmp_87;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 == 1)) begin
        _tmp_94 <= 1;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 3)) begin
        myram0_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram0_3_0_wdata <= _th_blink_wdata_10;
        myram0_3_0_wenable <= 1;
      end 
      _myram0_3_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 0) && (_tmp_102 == 3);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_144 == 0)) begin
        _tmp_153 <= 0;
        _tmp_143 <= req_block_size_3 - 1;
        _tmp_144 <= _myaxi_read_size;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_144 == 0)) begin
        _tmp_147 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_144 == 0)) begin
        _tmp_148 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0)) begin
        _tmp_143 <= _tmp_143 - 1;
        _tmp_144 <= _tmp_144 - 1;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0) && (_tmp_143 == 0)) begin
        _tmp_143 <= req_block_size_3 - 1;
        _tmp_153 <= _tmp_153 + 1;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0) && (_tmp_143 == 0) && (_tmp_153 == 1)) begin
        _tmp_153 <= 0;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0) && (_tmp_153 == 0)) begin
        _tmp_147 <= _tmp_149;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0) && (_tmp_153 == 1)) begin
        _tmp_148 <= _tmp_150;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0)) begin
        myram0_3_0_addr <= _tmp_151;
        myram0_3_0_wdata <= _slice_data_146;
        myram0_3_0_wenable <= _tmp_153 == 0;
      end 
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 == 1)) begin
        _tmp_145 <= 1;
      end 
      _myram0_3_cond_2_1 <= 1;
      _myram0_3_cond_3_1 <= 1;
      if(th_blink == 82) begin
        myram0_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_3_cond_4_1 <= th_blink == 82;
      _myram0_3_cond_5_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram0_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram0_3_cond_6_1 <= th_blink == 116;
      _myram0_3_cond_7_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_0_0_addr <= 0;
      myram1_0_0_wdata <= 0;
      myram1_0_0_wenable <= 0;
      _myram1_0_cond_0_1 <= 0;
      _myram1_0_cond_1_1 <= 0;
      _myram1_0_cond_2_1 <= 0;
      _myram1_0_cond_3_1 <= 0;
      _tmp_163 <= 0;
      _myram1_0_cond_4_1 <= 0;
      _myram1_0_cond_4_2 <= 0;
      _myram1_0_cond_5_1 <= 0;
      _tmp_178 <= 0;
      _myram1_0_cond_6_1 <= 0;
      _myram1_0_cond_6_2 <= 0;
    end else begin
      if(_myram1_0_cond_4_2) begin
        _tmp_163 <= 0;
      end 
      if(_myram1_0_cond_6_2) begin
        _tmp_178 <= 0;
      end 
      if(_myram1_0_cond_0_1) begin
        myram1_0_0_wenable <= 0;
      end 
      if(_myram1_0_cond_1_1) begin
        myram1_0_0_wenable <= 0;
      end 
      if(_myram1_0_cond_2_1) begin
        myram1_0_0_wenable <= 0;
      end 
      if(_myram1_0_cond_3_1) begin
        _tmp_163 <= 1;
      end 
      _myram1_0_cond_4_2 <= _myram1_0_cond_4_1;
      if(_myram1_0_cond_5_1) begin
        _tmp_178 <= 1;
      end 
      _myram1_0_cond_6_2 <= _myram1_0_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 0)) begin
        myram1_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_0_0_wdata <= _th_blink_wdata_10;
        myram1_0_0_wenable <= 1;
      end 
      _myram1_0_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 0);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_28 == 0) && !_tmp_25 && !_tmp_26) begin
        myram1_0_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_28 > 0) && (_tmp_20 == 1)) begin
        myram1_0_0_addr <= _tmp_19;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 0)) begin
        myram1_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_0_0_wdata <= _th_blink_wdata_10;
        myram1_0_0_wenable <= 1;
      end 
      _myram1_0_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 0);
      if(_slice_valid_113 && ((_tmp_111 > 0) && !_tmp_112) && (_tmp_111 > 0)) begin
        myram1_0_0_addr <= _tmp_119;
        myram1_0_0_wdata <= _slice_data_113;
        myram1_0_0_wenable <= _tmp_120 == 1;
      end 
      _myram1_0_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram1_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_0_cond_3_1 <= th_blink == 82;
      _myram1_0_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram1_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_0_cond_5_1 <= th_blink == 116;
      _myram1_0_cond_6_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_1_0_addr <= 0;
      myram1_1_0_wdata <= 0;
      myram1_1_0_wenable <= 0;
      _myram1_1_cond_0_1 <= 0;
      _myram1_1_cond_1_1 <= 0;
      _myram1_1_cond_2_1 <= 0;
      _myram1_1_cond_3_1 <= 0;
      _tmp_164 <= 0;
      _myram1_1_cond_4_1 <= 0;
      _myram1_1_cond_4_2 <= 0;
      _myram1_1_cond_5_1 <= 0;
      _tmp_179 <= 0;
      _myram1_1_cond_6_1 <= 0;
      _myram1_1_cond_6_2 <= 0;
    end else begin
      if(_myram1_1_cond_4_2) begin
        _tmp_164 <= 0;
      end 
      if(_myram1_1_cond_6_2) begin
        _tmp_179 <= 0;
      end 
      if(_myram1_1_cond_0_1) begin
        myram1_1_0_wenable <= 0;
      end 
      if(_myram1_1_cond_1_1) begin
        myram1_1_0_wenable <= 0;
      end 
      if(_myram1_1_cond_2_1) begin
        myram1_1_0_wenable <= 0;
      end 
      if(_myram1_1_cond_3_1) begin
        _tmp_164 <= 1;
      end 
      _myram1_1_cond_4_2 <= _myram1_1_cond_4_1;
      if(_myram1_1_cond_5_1) begin
        _tmp_179 <= 1;
      end 
      _myram1_1_cond_6_2 <= _myram1_1_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 1)) begin
        myram1_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_1_0_wdata <= _th_blink_wdata_10;
        myram1_1_0_wenable <= 1;
      end 
      _myram1_1_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 1);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_51 == 0) && !_tmp_48 && !_tmp_49) begin
        myram1_1_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_51 > 0) && (_tmp_43 == 1)) begin
        myram1_1_0_addr <= _tmp_42;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 1)) begin
        myram1_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_1_0_wdata <= _th_blink_wdata_10;
        myram1_1_0_wenable <= 1;
      end 
      _myram1_1_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 1);
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0)) begin
        myram1_1_0_addr <= _tmp_130;
        myram1_1_0_wdata <= _slice_data_124;
        myram1_1_0_wenable <= _tmp_131 == 1;
      end 
      _myram1_1_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram1_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_1_cond_3_1 <= th_blink == 82;
      _myram1_1_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram1_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_1_cond_5_1 <= th_blink == 116;
      _myram1_1_cond_6_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_2_0_addr <= 0;
      myram1_2_0_wdata <= 0;
      myram1_2_0_wenable <= 0;
      _myram1_2_cond_0_1 <= 0;
      _myram1_2_cond_1_1 <= 0;
      _myram1_2_cond_2_1 <= 0;
      _myram1_2_cond_3_1 <= 0;
      _tmp_165 <= 0;
      _myram1_2_cond_4_1 <= 0;
      _myram1_2_cond_4_2 <= 0;
      _myram1_2_cond_5_1 <= 0;
      _tmp_180 <= 0;
      _myram1_2_cond_6_1 <= 0;
      _myram1_2_cond_6_2 <= 0;
    end else begin
      if(_myram1_2_cond_4_2) begin
        _tmp_165 <= 0;
      end 
      if(_myram1_2_cond_6_2) begin
        _tmp_180 <= 0;
      end 
      if(_myram1_2_cond_0_1) begin
        myram1_2_0_wenable <= 0;
      end 
      if(_myram1_2_cond_1_1) begin
        myram1_2_0_wenable <= 0;
      end 
      if(_myram1_2_cond_2_1) begin
        myram1_2_0_wenable <= 0;
      end 
      if(_myram1_2_cond_3_1) begin
        _tmp_165 <= 1;
      end 
      _myram1_2_cond_4_2 <= _myram1_2_cond_4_1;
      if(_myram1_2_cond_5_1) begin
        _tmp_180 <= 1;
      end 
      _myram1_2_cond_6_2 <= _myram1_2_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 2)) begin
        myram1_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_2_0_wdata <= _th_blink_wdata_10;
        myram1_2_0_wenable <= 1;
      end 
      _myram1_2_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 2);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_74 == 0) && !_tmp_71 && !_tmp_72) begin
        myram1_2_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_54 || !_tmp_52) && (_tmp_55 || !_tmp_53) && (_tmp_74 > 0) && (_tmp_66 == 1)) begin
        myram1_2_0_addr <= _tmp_65;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 2)) begin
        myram1_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_2_0_wdata <= _th_blink_wdata_10;
        myram1_2_0_wenable <= 1;
      end 
      _myram1_2_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 2);
      if(_slice_valid_135 && ((_tmp_133 > 0) && !_tmp_134) && (_tmp_133 > 0)) begin
        myram1_2_0_addr <= _tmp_141;
        myram1_2_0_wdata <= _slice_data_135;
        myram1_2_0_wenable <= _tmp_142 == 1;
      end 
      _myram1_2_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram1_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_2_cond_3_1 <= th_blink == 82;
      _myram1_2_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram1_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_2_cond_5_1 <= th_blink == 116;
      _myram1_2_cond_6_1 <= th_blink == 116;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_3_0_addr <= 0;
      myram1_3_0_wdata <= 0;
      myram1_3_0_wenable <= 0;
      _myram1_3_cond_0_1 <= 0;
      _myram1_3_cond_1_1 <= 0;
      _myram1_3_cond_2_1 <= 0;
      _myram1_3_cond_3_1 <= 0;
      _tmp_166 <= 0;
      _myram1_3_cond_4_1 <= 0;
      _myram1_3_cond_4_2 <= 0;
      _myram1_3_cond_5_1 <= 0;
      _tmp_181 <= 0;
      _myram1_3_cond_6_1 <= 0;
      _myram1_3_cond_6_2 <= 0;
    end else begin
      if(_myram1_3_cond_4_2) begin
        _tmp_166 <= 0;
      end 
      if(_myram1_3_cond_6_2) begin
        _tmp_181 <= 0;
      end 
      if(_myram1_3_cond_0_1) begin
        myram1_3_0_wenable <= 0;
      end 
      if(_myram1_3_cond_1_1) begin
        myram1_3_0_wenable <= 0;
      end 
      if(_myram1_3_cond_2_1) begin
        myram1_3_0_wenable <= 0;
      end 
      if(_myram1_3_cond_3_1) begin
        _tmp_166 <= 1;
      end 
      _myram1_3_cond_4_2 <= _myram1_3_cond_4_1;
      if(_myram1_3_cond_5_1) begin
        _tmp_181 <= 1;
      end 
      _myram1_3_cond_6_2 <= _myram1_3_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 3)) begin
        myram1_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_3_0_wdata <= _th_blink_wdata_10;
        myram1_3_0_wenable <= 1;
      end 
      _myram1_3_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 1) && (_tmp_2 == 3);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_97 == 0) && !_tmp_94 && !_tmp_95) begin
        myram1_3_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_97 > 0) && (_tmp_89 == 1)) begin
        myram1_3_0_addr <= _tmp_88;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 3)) begin
        myram1_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
        myram1_3_0_wdata <= _th_blink_wdata_10;
        myram1_3_0_wenable <= 1;
      end 
      _myram1_3_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 1) && (_tmp_103 == 3);
      if(_slice_valid_146 && ((_tmp_144 > 0) && !_tmp_145) && (_tmp_144 > 0)) begin
        myram1_3_0_addr <= _tmp_152;
        myram1_3_0_wdata <= _slice_data_146;
        myram1_3_0_wenable <= _tmp_153 == 1;
      end 
      _myram1_3_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram1_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_3_cond_3_1 <= th_blink == 82;
      _myram1_3_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram1_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9 >> 2;
      end 
      _myram1_3_cond_5_1 <= th_blink == 116;
      _myram1_3_cond_6_1 <= th_blink == 116;
    end
  end

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
  localparam th_blink_102 = 102;
  localparam th_blink_103 = 103;
  localparam th_blink_104 = 104;
  localparam th_blink_105 = 105;
  localparam th_blink_106 = 106;
  localparam th_blink_107 = 107;
  localparam th_blink_108 = 108;
  localparam th_blink_109 = 109;
  localparam th_blink_110 = 110;
  localparam th_blink_111 = 111;
  localparam th_blink_112 = 112;
  localparam th_blink_113 = 113;
  localparam th_blink_114 = 114;
  localparam th_blink_115 = 115;
  localparam th_blink_116 = 116;
  localparam th_blink_117 = 117;
  localparam th_blink_118 = 118;
  localparam th_blink_119 = 119;
  localparam th_blink_120 = 120;
  localparam th_blink_121 = 121;
  localparam th_blink_122 = 122;
  localparam th_blink_123 = 123;
  localparam th_blink_124 = 124;
  localparam th_blink_125 = 125;
  localparam th_blink_126 = 126;
  localparam th_blink_127 = 127;
  localparam th_blink_128 = 128;
  localparam th_blink_129 = 129;
  localparam th_blink_130 = 130;
  localparam th_blink_131 = 131;
  localparam th_blink_132 = 132;
  localparam th_blink_133 = 133;
  localparam th_blink_134 = 134;
  localparam th_blink_135 = 135;
  localparam th_blink_136 = 136;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _d1_th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_offset_1 <= 0;
      _th_blink_size_2 <= 0;
      _th_blink_offset_3 <= 0;
      _th_blink_count_4 <= 0;
      _th_blink_blk_offset_5 <= 0;
      _th_blink_bias_6 <= 0;
      _th_blink_done_7 <= 0;
      _th_blink_bank_8 <= 0;
      _th_blink_i_9 <= 0;
      _th_blink_wdata_10 <= 0;
      _th_blink_laddr_11 <= 0;
      _th_blink_gaddr_12 <= 0;
      set_req_4 <= 0;
      _th_blink_cond_29_0_1 <= 0;
      axim_flag_5 <= 0;
      _th_blink_cond_30_1_1 <= 0;
      set_req_104 <= 0;
      _th_blink_cond_59_2_1 <= 0;
      axim_flag_105 <= 0;
      _th_blink_cond_60_3_1 <= 0;
      set_req_106 <= 0;
      _th_blink_cond_67_4_1 <= 0;
      axim_flag_107 <= 0;
      _th_blink_cond_68_5_1 <= 0;
      _tmp_168 <= 0;
      _th_blink_rdata_13 <= 0;
      _th_blink_exp_14 <= 0;
      set_req_169 <= 0;
      _th_blink_cond_101_6_1 <= 0;
      axim_flag_170 <= 0;
      _th_blink_cond_102_7_1 <= 0;
      _tmp_183 <= 0;
    end else begin
      _d1_th_blink <= th_blink;
      case(_d1_th_blink)
        th_blink_29: begin
          if(_th_blink_cond_29_0_1) begin
            set_req_4 <= 0;
          end 
        end
        th_blink_30: begin
          if(_th_blink_cond_30_1_1) begin
            axim_flag_5 <= 0;
          end 
        end
        th_blink_59: begin
          if(_th_blink_cond_59_2_1) begin
            set_req_104 <= 0;
          end 
        end
        th_blink_60: begin
          if(_th_blink_cond_60_3_1) begin
            axim_flag_105 <= 0;
          end 
        end
        th_blink_67: begin
          if(_th_blink_cond_67_4_1) begin
            set_req_106 <= 0;
          end 
        end
        th_blink_68: begin
          if(_th_blink_cond_68_5_1) begin
            axim_flag_107 <= 0;
          end 
        end
        th_blink_101: begin
          if(_th_blink_cond_101_6_1) begin
            set_req_169 <= 0;
          end 
        end
        th_blink_102: begin
          if(_th_blink_cond_102_7_1) begin
            axim_flag_170 <= 0;
          end 
        end
      endcase
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 128;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _tmp_0 <= 1;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          $display("# start");
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _th_blink_offset_1 <= 20476;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _th_blink_size_2 <= _th_blink_size_0;
          _th_blink_offset_3 <= _th_blink_offset_1;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_10;
          end else begin
            th_blink <= th_blink_27;
          end
        end
        th_blink_10: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          if(_th_blink_bank_8 < 2) begin
            th_blink <= th_blink_12;
          end else begin
            th_blink <= th_blink_25;
          end
        end
        th_blink_12: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          if(_th_blink_i_9 < 8) begin
            th_blink <= th_blink_14;
          end else begin
            th_blink <= th_blink_21;
          end
        end
        th_blink_14: begin
          _th_blink_wdata_10 <= _th_blink_bias_6 + _th_blink_i_9 + 512;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_18;
          end else begin
            th_blink <= th_blink_20;
          end
        end
        th_blink_18: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          th_blink <= th_blink_21;
        end
        th_blink_20: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_13;
        end
        th_blink_21: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_22;
          end else begin
            th_blink <= th_blink_23;
          end
        end
        th_blink_22: begin
          th_blink <= th_blink_25;
        end
        th_blink_23: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 8;
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_11;
        end
        th_blink_25: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 8;
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          th_blink <= th_blink_9;
        end
        th_blink_27: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_28;
        end
        th_blink_28: begin
          _th_blink_gaddr_12 <= _th_blink_offset_3;
          th_blink <= th_blink_29;
        end
        th_blink_29: begin
          set_req_4 <= 1;
          _th_blink_cond_29_0_1 <= 1;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          axim_flag_5 <= 1;
          _th_blink_cond_30_1_1 <= 1;
          th_blink <= th_blink_31;
        end
        th_blink_31: begin
          th_blink <= th_blink_32;
        end
        th_blink_32: begin
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_34;
          end 
        end
        th_blink_34: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_36;
        end
        th_blink_36: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_37;
        end
        th_blink_37: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_40;
          end else begin
            th_blink <= th_blink_57;
          end
        end
        th_blink_40: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          if(_th_blink_bank_8 < 2) begin
            th_blink <= th_blink_42;
          end else begin
            th_blink <= th_blink_55;
          end
        end
        th_blink_42: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          if(_th_blink_i_9 < 8) begin
            th_blink <= th_blink_44;
          end else begin
            th_blink <= th_blink_51;
          end
        end
        th_blink_44: begin
          _th_blink_wdata_10 <= _th_blink_bias_6 + _th_blink_i_9 + 1024;
          th_blink <= th_blink_45;
        end
        th_blink_45: begin
          th_blink <= th_blink_46;
        end
        th_blink_46: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_47;
        end
        th_blink_47: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_48;
          end else begin
            th_blink <= th_blink_50;
          end
        end
        th_blink_48: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_49;
        end
        th_blink_49: begin
          th_blink <= th_blink_51;
        end
        th_blink_50: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_43;
        end
        th_blink_51: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_52;
          end else begin
            th_blink <= th_blink_53;
          end
        end
        th_blink_52: begin
          th_blink <= th_blink_55;
        end
        th_blink_53: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 8;
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_41;
        end
        th_blink_55: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 8;
          th_blink <= th_blink_56;
        end
        th_blink_56: begin
          th_blink <= th_blink_39;
        end
        th_blink_57: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_58;
        end
        th_blink_58: begin
          _th_blink_gaddr_12 <= 2048 + _th_blink_offset_3;
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          set_req_104 <= 1;
          _th_blink_cond_59_2_1 <= 1;
          th_blink <= th_blink_60;
        end
        th_blink_60: begin
          axim_flag_105 <= 1;
          _th_blink_cond_60_3_1 <= 1;
          th_blink <= th_blink_61;
        end
        th_blink_61: begin
          th_blink <= th_blink_62;
        end
        th_blink_62: begin
          th_blink <= th_blink_63;
        end
        th_blink_63: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_64;
          end 
        end
        th_blink_64: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_65;
        end
        th_blink_65: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_66;
        end
        th_blink_66: begin
          _th_blink_gaddr_12 <= _th_blink_offset_3;
          th_blink <= th_blink_67;
        end
        th_blink_67: begin
          set_req_106 <= 1;
          _th_blink_cond_67_4_1 <= 1;
          th_blink <= th_blink_68;
        end
        th_blink_68: begin
          axim_flag_107 <= 1;
          _th_blink_cond_68_5_1 <= 1;
          th_blink <= th_blink_69;
        end
        th_blink_69: begin
          th_blink <= th_blink_70;
        end
        th_blink_70: begin
          th_blink <= th_blink_71;
        end
        th_blink_71: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_72;
          end 
        end
        th_blink_72: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_73;
        end
        th_blink_73: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_74;
        end
        th_blink_74: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_75;
        end
        th_blink_75: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_76;
        end
        th_blink_76: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_77;
        end
        th_blink_77: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_78;
          end else begin
            th_blink <= th_blink_99;
          end
        end
        th_blink_78: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_79;
        end
        th_blink_79: begin
          if(_th_blink_bank_8 < 2) begin
            th_blink <= th_blink_80;
          end else begin
            th_blink <= th_blink_97;
          end
        end
        th_blink_80: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_81;
        end
        th_blink_81: begin
          if(_th_blink_i_9 < 8) begin
            th_blink <= th_blink_82;
          end else begin
            th_blink <= th_blink_93;
          end
        end
        th_blink_82: begin
          if(_tmp_157 && (_th_blink_bank_8 == 0)) begin
            _tmp_168 <= _tmp_161;
          end 
          if(_tmp_163 && (_th_blink_bank_8 == 1)) begin
            _tmp_168 <= _tmp_167;
          end 
          if(_tmp_157) begin
            th_blink <= th_blink_83;
          end 
        end
        th_blink_83: begin
          _th_blink_rdata_13 <= _tmp_168;
          th_blink <= th_blink_84;
        end
        th_blink_84: begin
          _th_blink_exp_14 <= _th_blink_bias_6 + _th_blink_i_9 + 512;
          th_blink <= th_blink_85;
        end
        th_blink_85: begin
          if(_th_blink_rdata_13 !== _th_blink_exp_14) begin
            th_blink <= th_blink_86;
          end else begin
            th_blink <= th_blink_88;
          end
        end
        th_blink_86: begin
          $display("rdata[%d:%d] = %d:%d", _th_blink_bank_8, _th_blink_i_9, _th_blink_rdata_13, _th_blink_exp_14);
          th_blink <= th_blink_87;
        end
        th_blink_87: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_88;
        end
        th_blink_88: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_89;
        end
        th_blink_89: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_90;
          end else begin
            th_blink <= th_blink_92;
          end
        end
        th_blink_90: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_91;
        end
        th_blink_91: begin
          th_blink <= th_blink_93;
        end
        th_blink_92: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_81;
        end
        th_blink_93: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_94;
          end else begin
            th_blink <= th_blink_95;
          end
        end
        th_blink_94: begin
          th_blink <= th_blink_97;
        end
        th_blink_95: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 8;
          th_blink <= th_blink_96;
        end
        th_blink_96: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_79;
        end
        th_blink_97: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 8;
          th_blink <= th_blink_98;
        end
        th_blink_98: begin
          th_blink <= th_blink_77;
        end
        th_blink_99: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_100;
        end
        th_blink_100: begin
          _th_blink_gaddr_12 <= 2048 + _th_blink_offset_3;
          th_blink <= th_blink_101;
        end
        th_blink_101: begin
          set_req_169 <= 1;
          _th_blink_cond_101_6_1 <= 1;
          th_blink <= th_blink_102;
        end
        th_blink_102: begin
          axim_flag_170 <= 1;
          _th_blink_cond_102_7_1 <= 1;
          th_blink <= th_blink_103;
        end
        th_blink_103: begin
          th_blink <= th_blink_104;
        end
        th_blink_104: begin
          th_blink <= th_blink_105;
        end
        th_blink_105: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_106;
          end 
        end
        th_blink_106: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_107;
        end
        th_blink_107: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_108;
        end
        th_blink_108: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_109;
        end
        th_blink_109: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_110;
        end
        th_blink_110: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_111;
        end
        th_blink_111: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_112;
          end else begin
            th_blink <= th_blink_133;
          end
        end
        th_blink_112: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_113;
        end
        th_blink_113: begin
          if(_th_blink_bank_8 < 2) begin
            th_blink <= th_blink_114;
          end else begin
            th_blink <= th_blink_131;
          end
        end
        th_blink_114: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_115;
        end
        th_blink_115: begin
          if(_th_blink_i_9 < 8) begin
            th_blink <= th_blink_116;
          end else begin
            th_blink <= th_blink_127;
          end
        end
        th_blink_116: begin
          if(_tmp_172 && (_th_blink_bank_8 == 0)) begin
            _tmp_183 <= _tmp_176;
          end 
          if(_tmp_178 && (_th_blink_bank_8 == 1)) begin
            _tmp_183 <= _tmp_182;
          end 
          if(_tmp_172) begin
            th_blink <= th_blink_117;
          end 
        end
        th_blink_117: begin
          _th_blink_rdata_13 <= _tmp_183;
          th_blink <= th_blink_118;
        end
        th_blink_118: begin
          _th_blink_exp_14 <= _th_blink_bias_6 + _th_blink_i_9 + 1024;
          th_blink <= th_blink_119;
        end
        th_blink_119: begin
          if(_th_blink_rdata_13 !== _th_blink_exp_14) begin
            th_blink <= th_blink_120;
          end else begin
            th_blink <= th_blink_122;
          end
        end
        th_blink_120: begin
          $display("rdata[%d:%d] = %d:%d", _th_blink_bank_8, _th_blink_i_9, _th_blink_rdata_13, _th_blink_exp_14);
          th_blink <= th_blink_121;
        end
        th_blink_121: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_122;
        end
        th_blink_122: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_123;
        end
        th_blink_123: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_124;
          end else begin
            th_blink <= th_blink_126;
          end
        end
        th_blink_124: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_125;
        end
        th_blink_125: begin
          th_blink <= th_blink_127;
        end
        th_blink_126: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_115;
        end
        th_blink_127: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_128;
          end else begin
            th_blink <= th_blink_129;
          end
        end
        th_blink_128: begin
          th_blink <= th_blink_131;
        end
        th_blink_129: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 8;
          th_blink <= th_blink_130;
        end
        th_blink_130: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_113;
        end
        th_blink_131: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 8;
          th_blink <= th_blink_132;
        end
        th_blink_132: begin
          th_blink <= th_blink_111;
        end
        th_blink_133: begin
          $display("# end");
          th_blink <= th_blink_134;
        end
        th_blink_134: begin
          if(_tmp_0) begin
            th_blink <= th_blink_135;
          end else begin
            th_blink <= th_blink_136;
          end
        end
        th_blink_135: begin
          $display("ALL OK");
          th_blink <= th_blink_136;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      req_block_size_3 <= 0;
    end else begin
      if(set_req_4) begin
        req_block_size_3 <= 2.0;
      end 
      if(set_req_104) begin
        req_block_size_3 <= 2.0;
      end 
      if(set_req_106) begin
        req_block_size_3 <= 2.0;
      end 
      if(set_req_169) begin
        req_block_size_3 <= 2.0;
      end 
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
      axim_flag_101 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_101 <= 0;
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
          axim_flag_101 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
        end
      endcase
    end
  end

  reg [128-1:0] _cat_data_188;
  reg _cat_valid_188;
  wire _cat_ready_188;
  assign _tmp_77 = 1 && ((_cat_ready_188 || !_cat_valid_188) && (_tmp_75 && _tmp_52 && _tmp_29 && _tmp_6));
  assign _tmp_54 = 1 && ((_cat_ready_188 || !_cat_valid_188) && (_tmp_75 && _tmp_52 && _tmp_29 && _tmp_6));
  assign _tmp_31 = 1 && ((_cat_ready_188 || !_cat_valid_188) && (_tmp_75 && _tmp_52 && _tmp_29 && _tmp_6));
  assign _tmp_8 = 1 && ((_cat_ready_188 || !_cat_valid_188) && (_tmp_75 && _tmp_52 && _tmp_29 && _tmp_6));
  assign _cat_data_100 = _cat_data_188;
  assign _cat_valid_100 = _cat_valid_188;
  assign _cat_ready_188 = _cat_ready_100;

  always @(posedge CLK) begin
    if(RST) begin
      _cat_data_188 <= 0;
      _cat_valid_188 <= 0;
    end else begin
      if((_cat_ready_188 || !_cat_valid_188) && (_tmp_77 && _tmp_54 && _tmp_31 && _tmp_8) && (_tmp_75 && _tmp_52 && _tmp_29 && _tmp_6)) begin
        _cat_data_188 <= { _tmp_91, _tmp_68, _tmp_45, _tmp_22 };
      end 
      if(_cat_valid_188 && _cat_ready_188) begin
        _cat_valid_188 <= 0;
      end 
      if((_cat_ready_188 || !_cat_valid_188) && (_tmp_77 && _tmp_54 && _tmp_31 && _tmp_8)) begin
        _cat_valid_188 <= _tmp_75 && _tmp_52 && _tmp_29 && _tmp_6;
      end 
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
      _wvalid_109 <= 0;
      _wdata_108 <= 0;
      axim_flag_155 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_109 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_155 <= 0;
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
            _wdata_108 <= myaxi_rdata;
            _wvalid_109 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 4);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_155 <= 1;
          __myaxi_read_fsm_cond_4_1_1 <= 1;
          _myaxi_read_fsm <= _myaxi_read_fsm_5;
        end
        _myaxi_read_fsm_5: begin
          _myaxi_read_fsm <= _myaxi_read_fsm_init;
        end
      endcase
    end
  end


endmodule



module myram0_0
(
  input CLK,
  input [10-1:0] myram0_0_0_addr,
  output [32-1:0] myram0_0_0_rdata,
  input [32-1:0] myram0_0_0_wdata,
  input myram0_0_0_wenable
);

  reg [10-1:0] myram0_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram0_0_0_wenable) begin
      mem[myram0_0_0_addr] <= myram0_0_0_wdata;
    end 
    myram0_0_0_daddr <= myram0_0_0_addr;
  end

  assign myram0_0_0_rdata = mem[myram0_0_0_daddr];

endmodule



module myram0_1
(
  input CLK,
  input [10-1:0] myram0_1_0_addr,
  output [32-1:0] myram0_1_0_rdata,
  input [32-1:0] myram0_1_0_wdata,
  input myram0_1_0_wenable
);

  reg [10-1:0] myram0_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram0_1_0_wenable) begin
      mem[myram0_1_0_addr] <= myram0_1_0_wdata;
    end 
    myram0_1_0_daddr <= myram0_1_0_addr;
  end

  assign myram0_1_0_rdata = mem[myram0_1_0_daddr];

endmodule



module myram0_2
(
  input CLK,
  input [10-1:0] myram0_2_0_addr,
  output [32-1:0] myram0_2_0_rdata,
  input [32-1:0] myram0_2_0_wdata,
  input myram0_2_0_wenable
);

  reg [10-1:0] myram0_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram0_2_0_wenable) begin
      mem[myram0_2_0_addr] <= myram0_2_0_wdata;
    end 
    myram0_2_0_daddr <= myram0_2_0_addr;
  end

  assign myram0_2_0_rdata = mem[myram0_2_0_daddr];

endmodule



module myram0_3
(
  input CLK,
  input [10-1:0] myram0_3_0_addr,
  output [32-1:0] myram0_3_0_rdata,
  input [32-1:0] myram0_3_0_wdata,
  input myram0_3_0_wenable
);

  reg [10-1:0] myram0_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram0_3_0_wenable) begin
      mem[myram0_3_0_addr] <= myram0_3_0_wdata;
    end 
    myram0_3_0_daddr <= myram0_3_0_addr;
  end

  assign myram0_3_0_rdata = mem[myram0_3_0_daddr];

endmodule



module myram1_0
(
  input CLK,
  input [10-1:0] myram1_0_0_addr,
  output [32-1:0] myram1_0_0_rdata,
  input [32-1:0] myram1_0_0_wdata,
  input myram1_0_0_wenable
);

  reg [10-1:0] myram1_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram1_0_0_wenable) begin
      mem[myram1_0_0_addr] <= myram1_0_0_wdata;
    end 
    myram1_0_0_daddr <= myram1_0_0_addr;
  end

  assign myram1_0_0_rdata = mem[myram1_0_0_daddr];

endmodule



module myram1_1
(
  input CLK,
  input [10-1:0] myram1_1_0_addr,
  output [32-1:0] myram1_1_0_rdata,
  input [32-1:0] myram1_1_0_wdata,
  input myram1_1_0_wenable
);

  reg [10-1:0] myram1_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram1_1_0_wenable) begin
      mem[myram1_1_0_addr] <= myram1_1_0_wdata;
    end 
    myram1_1_0_daddr <= myram1_1_0_addr;
  end

  assign myram1_1_0_rdata = mem[myram1_1_0_daddr];

endmodule



module myram1_2
(
  input CLK,
  input [10-1:0] myram1_2_0_addr,
  output [32-1:0] myram1_2_0_rdata,
  input [32-1:0] myram1_2_0_wdata,
  input myram1_2_0_wenable
);

  reg [10-1:0] myram1_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram1_2_0_wenable) begin
      mem[myram1_2_0_addr] <= myram1_2_0_wdata;
    end 
    myram1_2_0_daddr <= myram1_2_0_addr;
  end

  assign myram1_2_0_rdata = mem[myram1_2_0_daddr];

endmodule



module myram1_3
(
  input CLK,
  input [10-1:0] myram1_3_0_addr,
  output [32-1:0] myram1_3_0_rdata,
  input [32-1:0] myram1_3_0_wdata,
  input myram1_3_0_wenable
);

  reg [10-1:0] myram1_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram1_3_0_wenable) begin
      mem[myram1_3_0_addr] <= myram1_3_0_wdata;
    end 
    myram1_3_0_daddr <= myram1_3_0_addr;
  end

  assign myram1_3_0_rdata = mem[myram1_3_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_multibank_nested_ram_dma_block.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
