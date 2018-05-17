from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_multibank_nested_ram_dma

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
    #200000;
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
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_offset_2;
  reg signed [32-1:0] _th_blink_size_3;
  reg signed [32-1:0] _th_blink_offset_4;
  reg signed [32-1:0] _th_blink_bank_5;
  reg signed [32-1:0] _th_blink_i_6;
  reg signed [32-1:0] _th_blink_wdata_7;
  reg _myram0_0_cond_0_1;
  reg _myram0_1_cond_0_1;
  reg _myram0_2_cond_0_1;
  reg _myram0_3_cond_0_1;
  reg _myram1_0_cond_0_1;
  reg _myram1_1_cond_0_1;
  reg _myram1_2_cond_0_1;
  reg _myram1_3_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_8;
  reg signed [32-1:0] _th_blink_gaddr_9;
  reg axim_flag_1;
  reg [32-1:0] _d1_th_blink;
  reg _th_blink_cond_18_0_1;
  reg _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start;
  reg [8-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_op_sel;
  reg [32-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_addr;
  reg [32-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_global_addr;
  reg [33-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_size;
  reg [32-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_stride;
  reg [32-1:0] _myaxi_write_narrow_2_fsm;
  localparam _myaxi_write_narrow_2_fsm_init = 0;
  reg [32-1:0] _myaxi_write_narrow_2_cur_global_addr;
  reg [33-1:0] _myaxi_write_narrow_2_cur_size;
  reg [33-1:0] _myaxi_write_narrow_2_rest_size;
  reg _tmp_2;
  reg _tmp_3;
  wire _tmp_4;
  wire _tmp_5;
  assign _tmp_5 = 1;
  localparam _tmp_6 = 1;
  wire [_tmp_6-1:0] _tmp_7;
  assign _tmp_7 = (_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3);
  reg [_tmp_6-1:0] __tmp_7_1;
  wire signed [32-1:0] _tmp_8;
  reg signed [32-1:0] __tmp_8_1;
  assign _tmp_8 = (__tmp_7_1)? myram0_0_0_rdata : __tmp_8_1;
  reg _tmp_9;
  reg _tmp_10;
  reg _tmp_11;
  reg _tmp_12;
  reg [34-1:0] _tmp_13;
  reg _tmp_14;
  reg _tmp_15;
  wire _tmp_16;
  wire _tmp_17;
  assign _tmp_17 = 1;
  localparam _tmp_18 = 1;
  wire [_tmp_18-1:0] _tmp_19;
  assign _tmp_19 = (_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15);
  reg [_tmp_18-1:0] __tmp_19_1;
  wire signed [32-1:0] _tmp_20;
  reg signed [32-1:0] __tmp_20_1;
  assign _tmp_20 = (__tmp_19_1)? myram0_1_0_rdata : __tmp_20_1;
  reg _tmp_21;
  reg _tmp_22;
  reg _tmp_23;
  reg _tmp_24;
  reg [34-1:0] _tmp_25;
  reg _tmp_26;
  reg _tmp_27;
  wire _tmp_28;
  wire _tmp_29;
  assign _tmp_29 = 1;
  localparam _tmp_30 = 1;
  wire [_tmp_30-1:0] _tmp_31;
  assign _tmp_31 = (_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27);
  reg [_tmp_30-1:0] __tmp_31_1;
  wire signed [32-1:0] _tmp_32;
  reg signed [32-1:0] __tmp_32_1;
  assign _tmp_32 = (__tmp_31_1)? myram0_2_0_rdata : __tmp_32_1;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg [34-1:0] _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  wire _tmp_40;
  wire _tmp_41;
  assign _tmp_41 = 1;
  localparam _tmp_42 = 1;
  wire [_tmp_42-1:0] _tmp_43;
  assign _tmp_43 = (_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39);
  reg [_tmp_42-1:0] __tmp_43_1;
  wire signed [32-1:0] _tmp_44;
  reg signed [32-1:0] __tmp_44_1;
  assign _tmp_44 = (__tmp_43_1)? myram0_3_0_rdata : __tmp_44_1;
  reg _tmp_45;
  reg _tmp_46;
  reg _tmp_47;
  reg _tmp_48;
  reg [34-1:0] _tmp_49;
  reg _tmp_50;
  reg _tmp_51;
  wire _tmp_52;
  wire _tmp_53;
  assign _tmp_53 = 1;
  localparam _tmp_54 = 1;
  wire [_tmp_54-1:0] _tmp_55;
  assign _tmp_55 = (_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51);
  reg [_tmp_54-1:0] __tmp_55_1;
  wire signed [32-1:0] _tmp_56;
  reg signed [32-1:0] __tmp_56_1;
  assign _tmp_56 = (__tmp_55_1)? myram1_0_0_rdata : __tmp_56_1;
  reg _tmp_57;
  reg _tmp_58;
  reg _tmp_59;
  reg _tmp_60;
  reg [34-1:0] _tmp_61;
  reg _tmp_62;
  reg _tmp_63;
  wire _tmp_64;
  wire _tmp_65;
  assign _tmp_65 = 1;
  localparam _tmp_66 = 1;
  wire [_tmp_66-1:0] _tmp_67;
  assign _tmp_67 = (_tmp_64 || !_tmp_62) && (_tmp_65 || !_tmp_63);
  reg [_tmp_66-1:0] __tmp_67_1;
  wire signed [32-1:0] _tmp_68;
  reg signed [32-1:0] __tmp_68_1;
  assign _tmp_68 = (__tmp_67_1)? myram1_1_0_rdata : __tmp_68_1;
  reg _tmp_69;
  reg _tmp_70;
  reg _tmp_71;
  reg _tmp_72;
  reg [34-1:0] _tmp_73;
  reg _tmp_74;
  reg _tmp_75;
  wire _tmp_76;
  wire _tmp_77;
  assign _tmp_77 = 1;
  localparam _tmp_78 = 1;
  wire [_tmp_78-1:0] _tmp_79;
  assign _tmp_79 = (_tmp_76 || !_tmp_74) && (_tmp_77 || !_tmp_75);
  reg [_tmp_78-1:0] __tmp_79_1;
  wire signed [32-1:0] _tmp_80;
  reg signed [32-1:0] __tmp_80_1;
  assign _tmp_80 = (__tmp_79_1)? myram1_2_0_rdata : __tmp_80_1;
  reg _tmp_81;
  reg _tmp_82;
  reg _tmp_83;
  reg _tmp_84;
  reg [34-1:0] _tmp_85;
  reg _tmp_86;
  reg _tmp_87;
  wire _tmp_88;
  wire _tmp_89;
  assign _tmp_89 = 1;
  localparam _tmp_90 = 1;
  wire [_tmp_90-1:0] _tmp_91;
  assign _tmp_91 = (_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87);
  reg [_tmp_90-1:0] __tmp_91_1;
  wire signed [32-1:0] _tmp_92;
  reg signed [32-1:0] __tmp_92_1;
  assign _tmp_92 = (__tmp_91_1)? myram1_3_0_rdata : __tmp_92_1;
  reg _tmp_93;
  reg _tmp_94;
  reg _tmp_95;
  reg _tmp_96;
  reg [34-1:0] _tmp_97;
  reg [9-1:0] _tmp_98;
  reg _myaxi_cond_0_1;
  reg [256-1:0] _myaxi_write_narrow_2_wdata;
  reg _myaxi_write_narrow_2_wvalid;
  wire _myaxi_write_narrow_2_wready;
  reg [1-1:0] _myaxi_write_narrow_2_pack_count;
  wire [256-1:0] _cat_data_99;
  wire _cat_valid_99;
  wire _cat_ready_99;
  assign _cat_ready_99 = (_myaxi_write_narrow_2_fsm == 3) && (_myaxi_write_narrow_2_wready || !_myaxi_write_narrow_2_wvalid) && (_myaxi_write_narrow_2_pack_count == 0) && (_myaxi_write_op_sel == 1);
  reg _tmp_100;
  wire [128-1:0] __variable_data_101;
  wire __variable_valid_101;
  wire __variable_ready_101;
  assign __variable_ready_101 = (_myaxi_write_narrow_2_fsm == 3) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  reg axim_flag_102;
  reg [32-1:0] _d1__myaxi_write_narrow_2_fsm;
  reg __myaxi_write_narrow_2_fsm_cond_4_0_1;
  reg _myram0_0_cond_1_1;
  reg _myram0_1_cond_1_1;
  reg _myram0_2_cond_1_1;
  reg _myram0_3_cond_1_1;
  reg _myram1_0_cond_1_1;
  reg _myram1_1_cond_1_1;
  reg _myram1_2_cond_1_1;
  reg _myram1_3_cond_1_1;
  reg axim_flag_103;
  reg _th_blink_cond_34_1_1;
  reg axim_flag_104;
  reg _th_blink_cond_41_2_1;
  reg _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start;
  reg [8-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_op_sel;
  reg [32-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_addr;
  reg [32-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_global_addr;
  reg [33-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_size;
  reg [32-1:0] _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_stride;
  reg [32-1:0] _myaxi_read_narrow_2_fsm;
  localparam _myaxi_read_narrow_2_fsm_init = 0;
  reg [32-1:0] _myaxi_read_narrow_2_cur_global_addr;
  reg [33-1:0] _myaxi_read_narrow_2_cur_size;
  reg [33-1:0] _myaxi_read_narrow_2_rest_size;
  reg [256-1:0] _wdata_105;
  reg _wvalid_106;
  reg [34-1:0] _tmp_107;
  reg _tmp_108;
  wire [32-1:0] _slice_data_109;
  wire _slice_valid_109;
  wire _slice_ready_109;
  assign _slice_ready_109 = (_tmp_107 > 0) && !_tmp_108;
  reg _myram0_0_cond_2_1;
  reg [34-1:0] _tmp_110;
  reg _tmp_111;
  wire [32-1:0] _slice_data_112;
  wire _slice_valid_112;
  wire _slice_ready_112;
  assign _slice_ready_112 = (_tmp_110 > 0) && !_tmp_111;
  reg _myram0_1_cond_2_1;
  reg [34-1:0] _tmp_113;
  reg _tmp_114;
  wire [32-1:0] _slice_data_115;
  wire _slice_valid_115;
  wire _slice_ready_115;
  assign _slice_ready_115 = (_tmp_113 > 0) && !_tmp_114;
  reg _myram0_2_cond_2_1;
  reg [34-1:0] _tmp_116;
  reg _tmp_117;
  wire [32-1:0] _slice_data_118;
  wire _slice_valid_118;
  wire _slice_ready_118;
  assign _slice_ready_118 = (_tmp_116 > 0) && !_tmp_117;
  reg _myram0_3_cond_2_1;
  reg [34-1:0] _tmp_119;
  reg _tmp_120;
  wire [32-1:0] _slice_data_121;
  wire _slice_valid_121;
  wire _slice_ready_121;
  assign _slice_ready_121 = (_tmp_119 > 0) && !_tmp_120;
  reg _myram1_0_cond_2_1;
  reg [34-1:0] _tmp_122;
  reg _tmp_123;
  wire [32-1:0] _slice_data_124;
  wire _slice_valid_124;
  wire _slice_ready_124;
  assign _slice_ready_124 = (_tmp_122 > 0) && !_tmp_123;
  reg _myram1_1_cond_2_1;
  reg [34-1:0] _tmp_125;
  reg _tmp_126;
  wire [32-1:0] _slice_data_127;
  wire _slice_valid_127;
  wire _slice_ready_127;
  assign _slice_ready_127 = (_tmp_125 > 0) && !_tmp_126;
  reg _myram1_2_cond_2_1;
  reg [34-1:0] _tmp_128;
  reg _tmp_129;
  wire [32-1:0] _slice_data_130;
  wire _slice_valid_130;
  wire _slice_ready_130;
  assign _slice_ready_130 = (_tmp_128 > 0) && !_tmp_129;
  reg _myram1_3_cond_2_1;
  reg [9-1:0] _tmp_131;
  reg _myaxi_cond_2_1;
  reg [1-1:0] _myaxi_read_narrow_2_pack_count;
  assign myaxi_rready = _myaxi_read_narrow_2_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_narrow_2_fsm;
  reg __myaxi_read_narrow_2_fsm_cond_3_0_1;
  reg axim_flag_132;
  reg __myaxi_read_narrow_2_fsm_cond_4_1_1;
  reg _tmp_133;
  reg _myram0_0_cond_3_1;
  reg _myram0_0_cond_4_1;
  reg _myram0_0_cond_4_2;
  reg _tmp_134;
  reg _myram0_1_cond_3_1;
  reg _myram0_1_cond_4_1;
  reg _myram0_1_cond_4_2;
  reg _tmp_135;
  reg _myram0_2_cond_3_1;
  reg _myram0_2_cond_4_1;
  reg _myram0_2_cond_4_2;
  reg _tmp_136;
  reg _myram0_3_cond_3_1;
  reg _myram0_3_cond_4_1;
  reg _myram0_3_cond_4_2;
  reg signed [32-1:0] _tmp_137;
  reg signed [32-1:0] _th_blink_rdata_10;
  reg _tmp_138;
  reg _myram1_0_cond_3_1;
  reg _myram1_0_cond_4_1;
  reg _myram1_0_cond_4_2;
  reg _tmp_139;
  reg _myram1_1_cond_3_1;
  reg _myram1_1_cond_4_1;
  reg _myram1_1_cond_4_2;
  reg _tmp_140;
  reg _myram1_2_cond_3_1;
  reg _myram1_2_cond_4_1;
  reg _myram1_2_cond_4_2;
  reg _tmp_141;
  reg _myram1_3_cond_3_1;
  reg _myram1_3_cond_4_1;
  reg _myram1_3_cond_4_2;
  reg signed [32-1:0] _tmp_142;
  reg axim_flag_143;
  reg _th_blink_cond_64_3_1;
  reg _tmp_144;
  reg _myram0_0_cond_5_1;
  reg _myram0_0_cond_6_1;
  reg _myram0_0_cond_6_2;
  reg _tmp_145;
  reg _myram0_1_cond_5_1;
  reg _myram0_1_cond_6_1;
  reg _myram0_1_cond_6_2;
  reg _tmp_146;
  reg _myram0_2_cond_5_1;
  reg _myram0_2_cond_6_1;
  reg _myram0_2_cond_6_2;
  reg _tmp_147;
  reg _myram0_3_cond_5_1;
  reg _myram0_3_cond_6_1;
  reg _myram0_3_cond_6_2;
  reg signed [32-1:0] _tmp_148;
  reg _tmp_149;
  reg _myram1_0_cond_5_1;
  reg _myram1_0_cond_6_1;
  reg _myram1_0_cond_6_2;
  reg _tmp_150;
  reg _myram1_1_cond_5_1;
  reg _myram1_1_cond_6_1;
  reg _myram1_1_cond_6_2;
  reg _tmp_151;
  reg _myram1_2_cond_5_1;
  reg _myram1_2_cond_6_1;
  reg _myram1_2_cond_6_2;
  reg _tmp_152;
  reg _myram1_3_cond_5_1;
  reg _myram1_3_cond_6_1;
  reg _myram1_3_cond_6_2;
  reg signed [32-1:0] _tmp_153;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_op_sel <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_addr <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_global_addr <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_size <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_stride <= 0;
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
      _myaxi_write_narrow_2_wvalid <= 0;
      _myaxi_write_narrow_2_wdata <= 0;
      _myaxi_write_narrow_2_pack_count <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_100 <= 0;
      _myaxi_cond_1_1 <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_op_sel <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_addr <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_global_addr <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_size <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_131 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_100 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_arvalid <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start <= 0;
      if(axim_flag_1) begin
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_op_sel <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_addr <= _th_blink_laddr_8;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_size <= _th_blink_size_3;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_stride <= 1;
      end 
      if(_myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_global_addr;
        _myaxi_write_size <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_size;
        _myaxi_write_local_stride <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_stride;
      end 
      if((_myaxi_write_narrow_2_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_98 == 0))) begin
        myaxi_awaddr <= _myaxi_write_narrow_2_cur_global_addr;
        myaxi_awlen <= _myaxi_write_narrow_2_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_98 <= _myaxi_write_narrow_2_cur_size;
      end 
      if((_myaxi_write_narrow_2_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_98 == 0)) && (_myaxi_write_narrow_2_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_myaxi_write_narrow_2_wready || !_myaxi_write_narrow_2_wvalid) begin
        _myaxi_write_narrow_2_wvalid <= 0;
      end 
      if(_cat_valid_99 && ((_myaxi_write_narrow_2_fsm == 3) && (_myaxi_write_narrow_2_wready || !_myaxi_write_narrow_2_wvalid) && (_myaxi_write_narrow_2_pack_count == 0) && (_myaxi_write_op_sel == 1)) && (_myaxi_write_op_sel == 1)) begin
        _myaxi_write_narrow_2_wdata <= _cat_data_99;
        _myaxi_write_narrow_2_wvalid <= 1;
        _myaxi_write_narrow_2_pack_count <= _myaxi_write_narrow_2_pack_count + 1;
      end 
      if((_myaxi_write_narrow_2_wready || !_myaxi_write_narrow_2_wvalid) && (_myaxi_write_narrow_2_pack_count > 0) && (_myaxi_write_op_sel == 1)) begin
        _myaxi_write_narrow_2_wdata <= _myaxi_write_narrow_2_wdata >> 128;
        _myaxi_write_narrow_2_wvalid <= 1;
        _myaxi_write_narrow_2_pack_count <= _myaxi_write_narrow_2_pack_count + 1;
      end 
      if((_myaxi_write_narrow_2_wready || !_myaxi_write_narrow_2_wvalid) && (_myaxi_write_narrow_2_pack_count == 1) && (_myaxi_write_op_sel == 1)) begin
        _myaxi_write_narrow_2_wdata <= _myaxi_write_narrow_2_wdata >> 128;
        _myaxi_write_narrow_2_wvalid <= 1;
        _myaxi_write_narrow_2_pack_count <= 0;
      end 
      if(__variable_valid_101 && ((_myaxi_write_narrow_2_fsm == 3) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_98 > 0))) begin
        myaxi_wdata <= __variable_data_101;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 16{ 1'd1 } };
        _tmp_98 <= _tmp_98 - 1;
      end 
      if(__variable_valid_101 && ((_myaxi_write_narrow_2_fsm == 3) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_98 > 0)) && (_tmp_98 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_100 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_100 <= _tmp_100;
      end 
      if(axim_flag_102) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_103) begin
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_start <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_op_sel <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_addr <= _th_blink_laddr_8;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_size <= _th_blink_size_3;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_write_local_stride <= 1;
      end 
      _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start <= 0;
      if(axim_flag_104) begin
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_op_sel <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_addr <= _th_blink_laddr_8;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_size <= _th_blink_size_3;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_stride <= 1;
      end 
      if(_myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_global_addr;
        _myaxi_read_size <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_size;
        _myaxi_read_local_stride <= _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_stride;
      end 
      if((_myaxi_read_narrow_2_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_131 == 0))) begin
        myaxi_araddr <= _myaxi_read_narrow_2_cur_global_addr;
        myaxi_arlen <= _myaxi_read_narrow_2_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_131 <= _myaxi_read_narrow_2_cur_size;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_131 > 0)) begin
        _tmp_131 <= _tmp_131 - 1;
      end 
      if(axim_flag_132) begin
        _myaxi_read_idle <= 1;
      end 
      if(axim_flag_143) begin
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_start <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_op_sel <= 1;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_addr <= _th_blink_laddr_8;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_size <= _th_blink_size_3;
        _myaxi_myram0_0_myram0_1_myram0_2_myram0_3_myram1_0_myram1_1_myram1_2_myram1_3_0_read_local_stride <= 1;
      end 
    end
  end

  reg [32-1:0] _slice_data_154;
  reg _slice_valid_154;
  wire _slice_ready_154;
  reg [32-1:0] _slice_data_155;
  reg _slice_valid_155;
  wire _slice_ready_155;
  reg [32-1:0] _slice_data_156;
  reg _slice_valid_156;
  wire _slice_ready_156;
  reg [32-1:0] _slice_data_157;
  reg _slice_valid_157;
  wire _slice_ready_157;
  reg [32-1:0] _slice_data_158;
  reg _slice_valid_158;
  wire _slice_ready_158;
  reg [32-1:0] _slice_data_159;
  reg _slice_valid_159;
  wire _slice_ready_159;
  reg [32-1:0] _slice_data_160;
  reg _slice_valid_160;
  wire _slice_ready_160;
  reg [32-1:0] _slice_data_161;
  reg _slice_valid_161;
  wire _slice_ready_161;
  reg [128-1:0] __delay_data_162;
  reg __delay_valid_162;
  wire __delay_ready_162;
  assign _myaxi_write_narrow_2_wready = (__delay_ready_162 || !__delay_valid_162) && _myaxi_write_narrow_2_wvalid;
  assign _slice_data_109 = _slice_data_154;
  assign _slice_valid_109 = _slice_valid_154;
  assign _slice_ready_154 = _slice_ready_109;
  assign _slice_data_112 = _slice_data_155;
  assign _slice_valid_112 = _slice_valid_155;
  assign _slice_ready_155 = _slice_ready_112;
  assign _slice_data_115 = _slice_data_156;
  assign _slice_valid_115 = _slice_valid_156;
  assign _slice_ready_156 = _slice_ready_115;
  assign _slice_data_118 = _slice_data_157;
  assign _slice_valid_118 = _slice_valid_157;
  assign _slice_ready_157 = _slice_ready_118;
  assign _slice_data_121 = _slice_data_158;
  assign _slice_valid_121 = _slice_valid_158;
  assign _slice_ready_158 = _slice_ready_121;
  assign _slice_data_124 = _slice_data_159;
  assign _slice_valid_124 = _slice_valid_159;
  assign _slice_ready_159 = _slice_ready_124;
  assign _slice_data_127 = _slice_data_160;
  assign _slice_valid_127 = _slice_valid_160;
  assign _slice_ready_160 = _slice_ready_127;
  assign _slice_data_130 = _slice_data_161;
  assign _slice_valid_130 = _slice_valid_161;
  assign _slice_ready_161 = _slice_ready_130;
  assign __variable_data_101 = __delay_data_162;
  assign __variable_valid_101 = __delay_valid_162;
  assign __delay_ready_162 = __variable_ready_101;

  always @(posedge CLK) begin
    if(RST) begin
      _slice_data_154 <= 0;
      _slice_valid_154 <= 0;
      _slice_data_155 <= 0;
      _slice_valid_155 <= 0;
      _slice_data_156 <= 0;
      _slice_valid_156 <= 0;
      _slice_data_157 <= 0;
      _slice_valid_157 <= 0;
      _slice_data_158 <= 0;
      _slice_valid_158 <= 0;
      _slice_data_159 <= 0;
      _slice_valid_159 <= 0;
      _slice_data_160 <= 0;
      _slice_valid_160 <= 0;
      _slice_data_161 <= 0;
      _slice_valid_161 <= 0;
      __delay_data_162 <= 0;
      __delay_valid_162 <= 0;
    end else begin
      if((_slice_ready_154 || !_slice_valid_154) && 1 && _wvalid_106) begin
        _slice_data_154 <= _wdata_105[6'd31:1'd0];
      end 
      if(_slice_valid_154 && _slice_ready_154) begin
        _slice_valid_154 <= 0;
      end 
      if((_slice_ready_154 || !_slice_valid_154) && 1) begin
        _slice_valid_154 <= _wvalid_106;
      end 
      if((_slice_ready_155 || !_slice_valid_155) && 1 && _wvalid_106) begin
        _slice_data_155 <= _wdata_105[7'd63:7'd32];
      end 
      if(_slice_valid_155 && _slice_ready_155) begin
        _slice_valid_155 <= 0;
      end 
      if((_slice_ready_155 || !_slice_valid_155) && 1) begin
        _slice_valid_155 <= _wvalid_106;
      end 
      if((_slice_ready_156 || !_slice_valid_156) && 1 && _wvalid_106) begin
        _slice_data_156 <= _wdata_105[8'd95:8'd64];
      end 
      if(_slice_valid_156 && _slice_ready_156) begin
        _slice_valid_156 <= 0;
      end 
      if((_slice_ready_156 || !_slice_valid_156) && 1) begin
        _slice_valid_156 <= _wvalid_106;
      end 
      if((_slice_ready_157 || !_slice_valid_157) && 1 && _wvalid_106) begin
        _slice_data_157 <= _wdata_105[8'd127:8'd96];
      end 
      if(_slice_valid_157 && _slice_ready_157) begin
        _slice_valid_157 <= 0;
      end 
      if((_slice_ready_157 || !_slice_valid_157) && 1) begin
        _slice_valid_157 <= _wvalid_106;
      end 
      if((_slice_ready_158 || !_slice_valid_158) && 1 && _wvalid_106) begin
        _slice_data_158 <= _wdata_105[9'd159:9'd128];
      end 
      if(_slice_valid_158 && _slice_ready_158) begin
        _slice_valid_158 <= 0;
      end 
      if((_slice_ready_158 || !_slice_valid_158) && 1) begin
        _slice_valid_158 <= _wvalid_106;
      end 
      if((_slice_ready_159 || !_slice_valid_159) && 1 && _wvalid_106) begin
        _slice_data_159 <= _wdata_105[9'd191:9'd160];
      end 
      if(_slice_valid_159 && _slice_ready_159) begin
        _slice_valid_159 <= 0;
      end 
      if((_slice_ready_159 || !_slice_valid_159) && 1) begin
        _slice_valid_159 <= _wvalid_106;
      end 
      if((_slice_ready_160 || !_slice_valid_160) && 1 && _wvalid_106) begin
        _slice_data_160 <= _wdata_105[9'd223:9'd192];
      end 
      if(_slice_valid_160 && _slice_ready_160) begin
        _slice_valid_160 <= 0;
      end 
      if((_slice_ready_160 || !_slice_valid_160) && 1) begin
        _slice_valid_160 <= _wvalid_106;
      end 
      if((_slice_ready_161 || !_slice_valid_161) && 1 && _wvalid_106) begin
        _slice_data_161 <= _wdata_105[9'd255:9'd224];
      end 
      if(_slice_valid_161 && _slice_ready_161) begin
        _slice_valid_161 <= 0;
      end 
      if((_slice_ready_161 || !_slice_valid_161) && 1) begin
        _slice_valid_161 <= _wvalid_106;
      end 
      if((__delay_ready_162 || !__delay_valid_162) && _myaxi_write_narrow_2_wready && _myaxi_write_narrow_2_wvalid) begin
        __delay_data_162 <= _myaxi_write_narrow_2_wdata;
      end 
      if(__delay_valid_162 && __delay_ready_162) begin
        __delay_valid_162 <= 0;
      end 
      if((__delay_ready_162 || !__delay_valid_162) && _myaxi_write_narrow_2_wready) begin
        __delay_valid_162 <= _myaxi_write_narrow_2_wvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_0_0_addr <= 0;
      myram0_0_0_wdata <= 0;
      myram0_0_0_wenable <= 0;
      _myram0_0_cond_0_1 <= 0;
      __tmp_7_1 <= 0;
      __tmp_8_1 <= 0;
      _tmp_12 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_9 <= 0;
      _tmp_13 <= 0;
      _myram0_0_cond_1_1 <= 0;
      _tmp_107 <= 0;
      _tmp_108 <= 0;
      _myram0_0_cond_2_1 <= 0;
      _myram0_0_cond_3_1 <= 0;
      _tmp_133 <= 0;
      _myram0_0_cond_4_1 <= 0;
      _myram0_0_cond_4_2 <= 0;
      _myram0_0_cond_5_1 <= 0;
      _tmp_144 <= 0;
      _myram0_0_cond_6_1 <= 0;
      _myram0_0_cond_6_2 <= 0;
    end else begin
      if(_myram0_0_cond_4_2) begin
        _tmp_133 <= 0;
      end 
      if(_myram0_0_cond_6_2) begin
        _tmp_144 <= 0;
      end 
      if(_myram0_0_cond_0_1) begin
        myram0_0_0_wenable <= 0;
      end 
      if(_myram0_0_cond_1_1) begin
        myram0_0_0_wenable <= 0;
      end 
      if(_myram0_0_cond_2_1) begin
        myram0_0_0_wenable <= 0;
        _tmp_108 <= 0;
      end 
      if(_myram0_0_cond_3_1) begin
        _tmp_133 <= 1;
      end 
      _myram0_0_cond_4_2 <= _myram0_0_cond_4_1;
      if(_myram0_0_cond_5_1) begin
        _tmp_144 <= 1;
      end 
      _myram0_0_cond_6_2 <= _myram0_0_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 0)) begin
        myram0_0_0_addr <= _th_blink_i_6;
        myram0_0_0_wdata <= _th_blink_wdata_7;
        myram0_0_0_wenable <= 1;
      end 
      _myram0_0_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 0);
      __tmp_7_1 <= _tmp_7;
      __tmp_8_1 <= _tmp_8;
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && _tmp_10) begin
        _tmp_12 <= 0;
        _tmp_2 <= 0;
        _tmp_3 <= 0;
        _tmp_10 <= 0;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && _tmp_9) begin
        _tmp_2 <= 1;
        _tmp_3 <= 1;
        _tmp_12 <= _tmp_11;
        _tmp_11 <= 0;
        _tmp_9 <= 0;
        _tmp_10 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_13 == 0) && !_tmp_11 && !_tmp_12) begin
        myram0_0_0_addr <= _myaxi_write_local_addr;
        _tmp_13 <= _myaxi_write_size - 1;
        _tmp_9 <= 1;
        _tmp_11 <= _myaxi_write_size == 1;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && (_tmp_13 > 0)) begin
        myram0_0_0_addr <= myram0_0_0_addr + _myaxi_write_local_stride;
        _tmp_13 <= _tmp_13 - 1;
        _tmp_9 <= 1;
        _tmp_11 <= 0;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && (_tmp_13 == 1)) begin
        _tmp_11 <= 1;
      end 
      if((th_blink == 28) && (_th_blink_bank_5 == 0)) begin
        myram0_0_0_addr <= _th_blink_i_6;
        myram0_0_0_wdata <= _th_blink_wdata_7;
        myram0_0_0_wenable <= 1;
      end 
      _myram0_0_cond_1_1 <= (th_blink == 28) && (_th_blink_bank_5 == 0);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_107 == 0)) begin
        myram0_0_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_107 <= _myaxi_read_size;
      end 
      if(_slice_valid_109 && ((_tmp_107 > 0) && !_tmp_108) && (_tmp_107 > 0)) begin
        myram0_0_0_addr <= myram0_0_0_addr + _myaxi_read_local_stride;
        myram0_0_0_wdata <= _slice_data_109;
        myram0_0_0_wenable <= 1;
        _tmp_107 <= _tmp_107 - 1;
      end 
      if(_slice_valid_109 && ((_tmp_107 > 0) && !_tmp_108) && (_tmp_107 == 1)) begin
        _tmp_108 <= 1;
      end 
      _myram0_0_cond_2_1 <= 1;
      if(th_blink == 50) begin
        myram0_0_0_addr <= _th_blink_i_6;
      end 
      _myram0_0_cond_3_1 <= th_blink == 50;
      _myram0_0_cond_4_1 <= th_blink == 50;
      if(th_blink == 73) begin
        myram0_0_0_addr <= _th_blink_i_6;
      end 
      _myram0_0_cond_5_1 <= th_blink == 73;
      _myram0_0_cond_6_1 <= th_blink == 73;
    end
  end

  reg [256-1:0] _cat_data_163;
  reg _cat_valid_163;
  wire _cat_ready_163;
  assign _tmp_88 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_76 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_64 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_52 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_40 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_28 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_16 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_4 = 1 && ((_cat_ready_163 || !_cat_valid_163) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _cat_data_99 = _cat_data_163;
  assign _cat_valid_99 = _cat_valid_163;
  assign _cat_ready_163 = _cat_ready_99;

  always @(posedge CLK) begin
    if(RST) begin
      _cat_data_163 <= 0;
      _cat_valid_163 <= 0;
    end else begin
      if((_cat_ready_163 || !_cat_valid_163) && (_tmp_88 && _tmp_76 && _tmp_64 && _tmp_52 && _tmp_40 && _tmp_28 && _tmp_16 && _tmp_4) && (_tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2)) begin
        _cat_data_163 <= { _tmp_92, _tmp_80, _tmp_68, _tmp_56, _tmp_44, _tmp_32, _tmp_20, _tmp_8 };
      end 
      if(_cat_valid_163 && _cat_ready_163) begin
        _cat_valid_163 <= 0;
      end 
      if((_cat_ready_163 || !_cat_valid_163) && (_tmp_88 && _tmp_76 && _tmp_64 && _tmp_52 && _tmp_40 && _tmp_28 && _tmp_16 && _tmp_4)) begin
        _cat_valid_163 <= _tmp_86 && _tmp_74 && _tmp_62 && _tmp_50 && _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_1_0_addr <= 0;
      myram0_1_0_wdata <= 0;
      myram0_1_0_wenable <= 0;
      _myram0_1_cond_0_1 <= 0;
      __tmp_19_1 <= 0;
      __tmp_20_1 <= 0;
      _tmp_24 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_22 <= 0;
      _tmp_23 <= 0;
      _tmp_21 <= 0;
      _tmp_25 <= 0;
      _myram0_1_cond_1_1 <= 0;
      _tmp_110 <= 0;
      _tmp_111 <= 0;
      _myram0_1_cond_2_1 <= 0;
      _myram0_1_cond_3_1 <= 0;
      _tmp_134 <= 0;
      _myram0_1_cond_4_1 <= 0;
      _myram0_1_cond_4_2 <= 0;
      _myram0_1_cond_5_1 <= 0;
      _tmp_145 <= 0;
      _myram0_1_cond_6_1 <= 0;
      _myram0_1_cond_6_2 <= 0;
    end else begin
      if(_myram0_1_cond_4_2) begin
        _tmp_134 <= 0;
      end 
      if(_myram0_1_cond_6_2) begin
        _tmp_145 <= 0;
      end 
      if(_myram0_1_cond_0_1) begin
        myram0_1_0_wenable <= 0;
      end 
      if(_myram0_1_cond_1_1) begin
        myram0_1_0_wenable <= 0;
      end 
      if(_myram0_1_cond_2_1) begin
        myram0_1_0_wenable <= 0;
        _tmp_111 <= 0;
      end 
      if(_myram0_1_cond_3_1) begin
        _tmp_134 <= 1;
      end 
      _myram0_1_cond_4_2 <= _myram0_1_cond_4_1;
      if(_myram0_1_cond_5_1) begin
        _tmp_145 <= 1;
      end 
      _myram0_1_cond_6_2 <= _myram0_1_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 1)) begin
        myram0_1_0_addr <= _th_blink_i_6;
        myram0_1_0_wdata <= _th_blink_wdata_7;
        myram0_1_0_wenable <= 1;
      end 
      _myram0_1_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 1);
      __tmp_19_1 <= _tmp_19;
      __tmp_20_1 <= _tmp_20;
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && _tmp_22) begin
        _tmp_24 <= 0;
        _tmp_14 <= 0;
        _tmp_15 <= 0;
        _tmp_22 <= 0;
      end 
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && _tmp_21) begin
        _tmp_14 <= 1;
        _tmp_15 <= 1;
        _tmp_24 <= _tmp_23;
        _tmp_23 <= 0;
        _tmp_21 <= 0;
        _tmp_22 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_25 == 0) && !_tmp_23 && !_tmp_24) begin
        myram0_1_0_addr <= _myaxi_write_local_addr;
        _tmp_25 <= _myaxi_write_size - 1;
        _tmp_21 <= 1;
        _tmp_23 <= _myaxi_write_size == 1;
      end 
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && (_tmp_25 > 0)) begin
        myram0_1_0_addr <= myram0_1_0_addr + _myaxi_write_local_stride;
        _tmp_25 <= _tmp_25 - 1;
        _tmp_21 <= 1;
        _tmp_23 <= 0;
      end 
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && (_tmp_25 == 1)) begin
        _tmp_23 <= 1;
      end 
      if((th_blink == 28) && (_th_blink_bank_5 == 1)) begin
        myram0_1_0_addr <= _th_blink_i_6;
        myram0_1_0_wdata <= _th_blink_wdata_7;
        myram0_1_0_wenable <= 1;
      end 
      _myram0_1_cond_1_1 <= (th_blink == 28) && (_th_blink_bank_5 == 1);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_110 == 0)) begin
        myram0_1_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_110 <= _myaxi_read_size;
      end 
      if(_slice_valid_112 && ((_tmp_110 > 0) && !_tmp_111) && (_tmp_110 > 0)) begin
        myram0_1_0_addr <= myram0_1_0_addr + _myaxi_read_local_stride;
        myram0_1_0_wdata <= _slice_data_112;
        myram0_1_0_wenable <= 1;
        _tmp_110 <= _tmp_110 - 1;
      end 
      if(_slice_valid_112 && ((_tmp_110 > 0) && !_tmp_111) && (_tmp_110 == 1)) begin
        _tmp_111 <= 1;
      end 
      _myram0_1_cond_2_1 <= 1;
      if(th_blink == 50) begin
        myram0_1_0_addr <= _th_blink_i_6;
      end 
      _myram0_1_cond_3_1 <= th_blink == 50;
      _myram0_1_cond_4_1 <= th_blink == 50;
      if(th_blink == 73) begin
        myram0_1_0_addr <= _th_blink_i_6;
      end 
      _myram0_1_cond_5_1 <= th_blink == 73;
      _myram0_1_cond_6_1 <= th_blink == 73;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_2_0_addr <= 0;
      myram0_2_0_wdata <= 0;
      myram0_2_0_wenable <= 0;
      _myram0_2_cond_0_1 <= 0;
      __tmp_31_1 <= 0;
      __tmp_32_1 <= 0;
      _tmp_36 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_33 <= 0;
      _tmp_37 <= 0;
      _myram0_2_cond_1_1 <= 0;
      _tmp_113 <= 0;
      _tmp_114 <= 0;
      _myram0_2_cond_2_1 <= 0;
      _myram0_2_cond_3_1 <= 0;
      _tmp_135 <= 0;
      _myram0_2_cond_4_1 <= 0;
      _myram0_2_cond_4_2 <= 0;
      _myram0_2_cond_5_1 <= 0;
      _tmp_146 <= 0;
      _myram0_2_cond_6_1 <= 0;
      _myram0_2_cond_6_2 <= 0;
    end else begin
      if(_myram0_2_cond_4_2) begin
        _tmp_135 <= 0;
      end 
      if(_myram0_2_cond_6_2) begin
        _tmp_146 <= 0;
      end 
      if(_myram0_2_cond_0_1) begin
        myram0_2_0_wenable <= 0;
      end 
      if(_myram0_2_cond_1_1) begin
        myram0_2_0_wenable <= 0;
      end 
      if(_myram0_2_cond_2_1) begin
        myram0_2_0_wenable <= 0;
        _tmp_114 <= 0;
      end 
      if(_myram0_2_cond_3_1) begin
        _tmp_135 <= 1;
      end 
      _myram0_2_cond_4_2 <= _myram0_2_cond_4_1;
      if(_myram0_2_cond_5_1) begin
        _tmp_146 <= 1;
      end 
      _myram0_2_cond_6_2 <= _myram0_2_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 2)) begin
        myram0_2_0_addr <= _th_blink_i_6;
        myram0_2_0_wdata <= _th_blink_wdata_7;
        myram0_2_0_wenable <= 1;
      end 
      _myram0_2_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 2);
      __tmp_31_1 <= _tmp_31;
      __tmp_32_1 <= _tmp_32;
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_34) begin
        _tmp_36 <= 0;
        _tmp_26 <= 0;
        _tmp_27 <= 0;
        _tmp_34 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_33) begin
        _tmp_26 <= 1;
        _tmp_27 <= 1;
        _tmp_36 <= _tmp_35;
        _tmp_35 <= 0;
        _tmp_33 <= 0;
        _tmp_34 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_37 == 0) && !_tmp_35 && !_tmp_36) begin
        myram0_2_0_addr <= _myaxi_write_local_addr;
        _tmp_37 <= _myaxi_write_size - 1;
        _tmp_33 <= 1;
        _tmp_35 <= _myaxi_write_size == 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 > 0)) begin
        myram0_2_0_addr <= myram0_2_0_addr + _myaxi_write_local_stride;
        _tmp_37 <= _tmp_37 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 == 1)) begin
        _tmp_35 <= 1;
      end 
      if((th_blink == 28) && (_th_blink_bank_5 == 2)) begin
        myram0_2_0_addr <= _th_blink_i_6;
        myram0_2_0_wdata <= _th_blink_wdata_7;
        myram0_2_0_wenable <= 1;
      end 
      _myram0_2_cond_1_1 <= (th_blink == 28) && (_th_blink_bank_5 == 2);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_113 == 0)) begin
        myram0_2_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_113 <= _myaxi_read_size;
      end 
      if(_slice_valid_115 && ((_tmp_113 > 0) && !_tmp_114) && (_tmp_113 > 0)) begin
        myram0_2_0_addr <= myram0_2_0_addr + _myaxi_read_local_stride;
        myram0_2_0_wdata <= _slice_data_115;
        myram0_2_0_wenable <= 1;
        _tmp_113 <= _tmp_113 - 1;
      end 
      if(_slice_valid_115 && ((_tmp_113 > 0) && !_tmp_114) && (_tmp_113 == 1)) begin
        _tmp_114 <= 1;
      end 
      _myram0_2_cond_2_1 <= 1;
      if(th_blink == 50) begin
        myram0_2_0_addr <= _th_blink_i_6;
      end 
      _myram0_2_cond_3_1 <= th_blink == 50;
      _myram0_2_cond_4_1 <= th_blink == 50;
      if(th_blink == 73) begin
        myram0_2_0_addr <= _th_blink_i_6;
      end 
      _myram0_2_cond_5_1 <= th_blink == 73;
      _myram0_2_cond_6_1 <= th_blink == 73;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram0_3_0_addr <= 0;
      myram0_3_0_wdata <= 0;
      myram0_3_0_wenable <= 0;
      _myram0_3_cond_0_1 <= 0;
      __tmp_43_1 <= 0;
      __tmp_44_1 <= 0;
      _tmp_48 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_45 <= 0;
      _tmp_49 <= 0;
      _myram0_3_cond_1_1 <= 0;
      _tmp_116 <= 0;
      _tmp_117 <= 0;
      _myram0_3_cond_2_1 <= 0;
      _myram0_3_cond_3_1 <= 0;
      _tmp_136 <= 0;
      _myram0_3_cond_4_1 <= 0;
      _myram0_3_cond_4_2 <= 0;
      _myram0_3_cond_5_1 <= 0;
      _tmp_147 <= 0;
      _myram0_3_cond_6_1 <= 0;
      _myram0_3_cond_6_2 <= 0;
    end else begin
      if(_myram0_3_cond_4_2) begin
        _tmp_136 <= 0;
      end 
      if(_myram0_3_cond_6_2) begin
        _tmp_147 <= 0;
      end 
      if(_myram0_3_cond_0_1) begin
        myram0_3_0_wenable <= 0;
      end 
      if(_myram0_3_cond_1_1) begin
        myram0_3_0_wenable <= 0;
      end 
      if(_myram0_3_cond_2_1) begin
        myram0_3_0_wenable <= 0;
        _tmp_117 <= 0;
      end 
      if(_myram0_3_cond_3_1) begin
        _tmp_136 <= 1;
      end 
      _myram0_3_cond_4_2 <= _myram0_3_cond_4_1;
      if(_myram0_3_cond_5_1) begin
        _tmp_147 <= 1;
      end 
      _myram0_3_cond_6_2 <= _myram0_3_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 3)) begin
        myram0_3_0_addr <= _th_blink_i_6;
        myram0_3_0_wdata <= _th_blink_wdata_7;
        myram0_3_0_wenable <= 1;
      end 
      _myram0_3_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 3);
      __tmp_43_1 <= _tmp_43;
      __tmp_44_1 <= _tmp_44;
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && _tmp_46) begin
        _tmp_48 <= 0;
        _tmp_38 <= 0;
        _tmp_39 <= 0;
        _tmp_46 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && _tmp_45) begin
        _tmp_38 <= 1;
        _tmp_39 <= 1;
        _tmp_48 <= _tmp_47;
        _tmp_47 <= 0;
        _tmp_45 <= 0;
        _tmp_46 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_49 == 0) && !_tmp_47 && !_tmp_48) begin
        myram0_3_0_addr <= _myaxi_write_local_addr;
        _tmp_49 <= _myaxi_write_size - 1;
        _tmp_45 <= 1;
        _tmp_47 <= _myaxi_write_size == 1;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 > 0)) begin
        myram0_3_0_addr <= myram0_3_0_addr + _myaxi_write_local_stride;
        _tmp_49 <= _tmp_49 - 1;
        _tmp_45 <= 1;
        _tmp_47 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 == 1)) begin
        _tmp_47 <= 1;
      end 
      if((th_blink == 28) && (_th_blink_bank_5 == 3)) begin
        myram0_3_0_addr <= _th_blink_i_6;
        myram0_3_0_wdata <= _th_blink_wdata_7;
        myram0_3_0_wenable <= 1;
      end 
      _myram0_3_cond_1_1 <= (th_blink == 28) && (_th_blink_bank_5 == 3);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_116 == 0)) begin
        myram0_3_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_116 <= _myaxi_read_size;
      end 
      if(_slice_valid_118 && ((_tmp_116 > 0) && !_tmp_117) && (_tmp_116 > 0)) begin
        myram0_3_0_addr <= myram0_3_0_addr + _myaxi_read_local_stride;
        myram0_3_0_wdata <= _slice_data_118;
        myram0_3_0_wenable <= 1;
        _tmp_116 <= _tmp_116 - 1;
      end 
      if(_slice_valid_118 && ((_tmp_116 > 0) && !_tmp_117) && (_tmp_116 == 1)) begin
        _tmp_117 <= 1;
      end 
      _myram0_3_cond_2_1 <= 1;
      if(th_blink == 50) begin
        myram0_3_0_addr <= _th_blink_i_6;
      end 
      _myram0_3_cond_3_1 <= th_blink == 50;
      _myram0_3_cond_4_1 <= th_blink == 50;
      if(th_blink == 73) begin
        myram0_3_0_addr <= _th_blink_i_6;
      end 
      _myram0_3_cond_5_1 <= th_blink == 73;
      _myram0_3_cond_6_1 <= th_blink == 73;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_0_0_addr <= 0;
      myram1_0_0_wdata <= 0;
      myram1_0_0_wenable <= 0;
      _myram1_0_cond_0_1 <= 0;
      __tmp_55_1 <= 0;
      __tmp_56_1 <= 0;
      _tmp_60 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _tmp_57 <= 0;
      _tmp_61 <= 0;
      _myram1_0_cond_1_1 <= 0;
      _tmp_119 <= 0;
      _tmp_120 <= 0;
      _myram1_0_cond_2_1 <= 0;
      _myram1_0_cond_3_1 <= 0;
      _tmp_138 <= 0;
      _myram1_0_cond_4_1 <= 0;
      _myram1_0_cond_4_2 <= 0;
      _myram1_0_cond_5_1 <= 0;
      _tmp_149 <= 0;
      _myram1_0_cond_6_1 <= 0;
      _myram1_0_cond_6_2 <= 0;
    end else begin
      if(_myram1_0_cond_4_2) begin
        _tmp_138 <= 0;
      end 
      if(_myram1_0_cond_6_2) begin
        _tmp_149 <= 0;
      end 
      if(_myram1_0_cond_0_1) begin
        myram1_0_0_wenable <= 0;
      end 
      if(_myram1_0_cond_1_1) begin
        myram1_0_0_wenable <= 0;
      end 
      if(_myram1_0_cond_2_1) begin
        myram1_0_0_wenable <= 0;
        _tmp_120 <= 0;
      end 
      if(_myram1_0_cond_3_1) begin
        _tmp_138 <= 1;
      end 
      _myram1_0_cond_4_2 <= _myram1_0_cond_4_1;
      if(_myram1_0_cond_5_1) begin
        _tmp_149 <= 1;
      end 
      _myram1_0_cond_6_2 <= _myram1_0_cond_6_1;
      if((th_blink == 13) && (_th_blink_bank_5 == 0)) begin
        myram1_0_0_addr <= _th_blink_i_6;
        myram1_0_0_wdata <= _th_blink_wdata_7 + 10;
        myram1_0_0_wenable <= 1;
      end 
      _myram1_0_cond_0_1 <= (th_blink == 13) && (_th_blink_bank_5 == 0);
      __tmp_55_1 <= _tmp_55;
      __tmp_56_1 <= _tmp_56;
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && _tmp_58) begin
        _tmp_60 <= 0;
        _tmp_50 <= 0;
        _tmp_51 <= 0;
        _tmp_58 <= 0;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && _tmp_57) begin
        _tmp_50 <= 1;
        _tmp_51 <= 1;
        _tmp_60 <= _tmp_59;
        _tmp_59 <= 0;
        _tmp_57 <= 0;
        _tmp_58 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_61 == 0) && !_tmp_59 && !_tmp_60) begin
        myram1_0_0_addr <= _myaxi_write_local_addr;
        _tmp_61 <= _myaxi_write_size - 1;
        _tmp_57 <= 1;
        _tmp_59 <= _myaxi_write_size == 1;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_61 > 0)) begin
        myram1_0_0_addr <= myram1_0_0_addr + _myaxi_write_local_stride;
        _tmp_61 <= _tmp_61 - 1;
        _tmp_57 <= 1;
        _tmp_59 <= 0;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_61 == 1)) begin
        _tmp_59 <= 1;
      end 
      if((th_blink == 29) && (_th_blink_bank_5 == 0)) begin
        myram1_0_0_addr <= _th_blink_i_6;
        myram1_0_0_wdata <= _th_blink_wdata_7 + 20;
        myram1_0_0_wenable <= 1;
      end 
      _myram1_0_cond_1_1 <= (th_blink == 29) && (_th_blink_bank_5 == 0);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_119 == 0)) begin
        myram1_0_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_119 <= _myaxi_read_size;
      end 
      if(_slice_valid_121 && ((_tmp_119 > 0) && !_tmp_120) && (_tmp_119 > 0)) begin
        myram1_0_0_addr <= myram1_0_0_addr + _myaxi_read_local_stride;
        myram1_0_0_wdata <= _slice_data_121;
        myram1_0_0_wenable <= 1;
        _tmp_119 <= _tmp_119 - 1;
      end 
      if(_slice_valid_121 && ((_tmp_119 > 0) && !_tmp_120) && (_tmp_119 == 1)) begin
        _tmp_120 <= 1;
      end 
      _myram1_0_cond_2_1 <= 1;
      if(th_blink == 55) begin
        myram1_0_0_addr <= _th_blink_i_6;
      end 
      _myram1_0_cond_3_1 <= th_blink == 55;
      _myram1_0_cond_4_1 <= th_blink == 55;
      if(th_blink == 78) begin
        myram1_0_0_addr <= _th_blink_i_6;
      end 
      _myram1_0_cond_5_1 <= th_blink == 78;
      _myram1_0_cond_6_1 <= th_blink == 78;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_1_0_addr <= 0;
      myram1_1_0_wdata <= 0;
      myram1_1_0_wenable <= 0;
      _myram1_1_cond_0_1 <= 0;
      __tmp_67_1 <= 0;
      __tmp_68_1 <= 0;
      _tmp_72 <= 0;
      _tmp_62 <= 0;
      _tmp_63 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_69 <= 0;
      _tmp_73 <= 0;
      _myram1_1_cond_1_1 <= 0;
      _tmp_122 <= 0;
      _tmp_123 <= 0;
      _myram1_1_cond_2_1 <= 0;
      _myram1_1_cond_3_1 <= 0;
      _tmp_139 <= 0;
      _myram1_1_cond_4_1 <= 0;
      _myram1_1_cond_4_2 <= 0;
      _myram1_1_cond_5_1 <= 0;
      _tmp_150 <= 0;
      _myram1_1_cond_6_1 <= 0;
      _myram1_1_cond_6_2 <= 0;
    end else begin
      if(_myram1_1_cond_4_2) begin
        _tmp_139 <= 0;
      end 
      if(_myram1_1_cond_6_2) begin
        _tmp_150 <= 0;
      end 
      if(_myram1_1_cond_0_1) begin
        myram1_1_0_wenable <= 0;
      end 
      if(_myram1_1_cond_1_1) begin
        myram1_1_0_wenable <= 0;
      end 
      if(_myram1_1_cond_2_1) begin
        myram1_1_0_wenable <= 0;
        _tmp_123 <= 0;
      end 
      if(_myram1_1_cond_3_1) begin
        _tmp_139 <= 1;
      end 
      _myram1_1_cond_4_2 <= _myram1_1_cond_4_1;
      if(_myram1_1_cond_5_1) begin
        _tmp_150 <= 1;
      end 
      _myram1_1_cond_6_2 <= _myram1_1_cond_6_1;
      if((th_blink == 13) && (_th_blink_bank_5 == 1)) begin
        myram1_1_0_addr <= _th_blink_i_6;
        myram1_1_0_wdata <= _th_blink_wdata_7 + 10;
        myram1_1_0_wenable <= 1;
      end 
      _myram1_1_cond_0_1 <= (th_blink == 13) && (_th_blink_bank_5 == 1);
      __tmp_67_1 <= _tmp_67;
      __tmp_68_1 <= _tmp_68;
      if((_tmp_64 || !_tmp_62) && (_tmp_65 || !_tmp_63) && _tmp_70) begin
        _tmp_72 <= 0;
        _tmp_62 <= 0;
        _tmp_63 <= 0;
        _tmp_70 <= 0;
      end 
      if((_tmp_64 || !_tmp_62) && (_tmp_65 || !_tmp_63) && _tmp_69) begin
        _tmp_62 <= 1;
        _tmp_63 <= 1;
        _tmp_72 <= _tmp_71;
        _tmp_71 <= 0;
        _tmp_69 <= 0;
        _tmp_70 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_73 == 0) && !_tmp_71 && !_tmp_72) begin
        myram1_1_0_addr <= _myaxi_write_local_addr;
        _tmp_73 <= _myaxi_write_size - 1;
        _tmp_69 <= 1;
        _tmp_71 <= _myaxi_write_size == 1;
      end 
      if((_tmp_64 || !_tmp_62) && (_tmp_65 || !_tmp_63) && (_tmp_73 > 0)) begin
        myram1_1_0_addr <= myram1_1_0_addr + _myaxi_write_local_stride;
        _tmp_73 <= _tmp_73 - 1;
        _tmp_69 <= 1;
        _tmp_71 <= 0;
      end 
      if((_tmp_64 || !_tmp_62) && (_tmp_65 || !_tmp_63) && (_tmp_73 == 1)) begin
        _tmp_71 <= 1;
      end 
      if((th_blink == 29) && (_th_blink_bank_5 == 1)) begin
        myram1_1_0_addr <= _th_blink_i_6;
        myram1_1_0_wdata <= _th_blink_wdata_7 + 20;
        myram1_1_0_wenable <= 1;
      end 
      _myram1_1_cond_1_1 <= (th_blink == 29) && (_th_blink_bank_5 == 1);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_122 == 0)) begin
        myram1_1_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_122 <= _myaxi_read_size;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 > 0)) begin
        myram1_1_0_addr <= myram1_1_0_addr + _myaxi_read_local_stride;
        myram1_1_0_wdata <= _slice_data_124;
        myram1_1_0_wenable <= 1;
        _tmp_122 <= _tmp_122 - 1;
      end 
      if(_slice_valid_124 && ((_tmp_122 > 0) && !_tmp_123) && (_tmp_122 == 1)) begin
        _tmp_123 <= 1;
      end 
      _myram1_1_cond_2_1 <= 1;
      if(th_blink == 55) begin
        myram1_1_0_addr <= _th_blink_i_6;
      end 
      _myram1_1_cond_3_1 <= th_blink == 55;
      _myram1_1_cond_4_1 <= th_blink == 55;
      if(th_blink == 78) begin
        myram1_1_0_addr <= _th_blink_i_6;
      end 
      _myram1_1_cond_5_1 <= th_blink == 78;
      _myram1_1_cond_6_1 <= th_blink == 78;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_2_0_addr <= 0;
      myram1_2_0_wdata <= 0;
      myram1_2_0_wenable <= 0;
      _myram1_2_cond_0_1 <= 0;
      __tmp_79_1 <= 0;
      __tmp_80_1 <= 0;
      _tmp_84 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      _tmp_82 <= 0;
      _tmp_83 <= 0;
      _tmp_81 <= 0;
      _tmp_85 <= 0;
      _myram1_2_cond_1_1 <= 0;
      _tmp_125 <= 0;
      _tmp_126 <= 0;
      _myram1_2_cond_2_1 <= 0;
      _myram1_2_cond_3_1 <= 0;
      _tmp_140 <= 0;
      _myram1_2_cond_4_1 <= 0;
      _myram1_2_cond_4_2 <= 0;
      _myram1_2_cond_5_1 <= 0;
      _tmp_151 <= 0;
      _myram1_2_cond_6_1 <= 0;
      _myram1_2_cond_6_2 <= 0;
    end else begin
      if(_myram1_2_cond_4_2) begin
        _tmp_140 <= 0;
      end 
      if(_myram1_2_cond_6_2) begin
        _tmp_151 <= 0;
      end 
      if(_myram1_2_cond_0_1) begin
        myram1_2_0_wenable <= 0;
      end 
      if(_myram1_2_cond_1_1) begin
        myram1_2_0_wenable <= 0;
      end 
      if(_myram1_2_cond_2_1) begin
        myram1_2_0_wenable <= 0;
        _tmp_126 <= 0;
      end 
      if(_myram1_2_cond_3_1) begin
        _tmp_140 <= 1;
      end 
      _myram1_2_cond_4_2 <= _myram1_2_cond_4_1;
      if(_myram1_2_cond_5_1) begin
        _tmp_151 <= 1;
      end 
      _myram1_2_cond_6_2 <= _myram1_2_cond_6_1;
      if((th_blink == 13) && (_th_blink_bank_5 == 2)) begin
        myram1_2_0_addr <= _th_blink_i_6;
        myram1_2_0_wdata <= _th_blink_wdata_7 + 10;
        myram1_2_0_wenable <= 1;
      end 
      _myram1_2_cond_0_1 <= (th_blink == 13) && (_th_blink_bank_5 == 2);
      __tmp_79_1 <= _tmp_79;
      __tmp_80_1 <= _tmp_80;
      if((_tmp_76 || !_tmp_74) && (_tmp_77 || !_tmp_75) && _tmp_82) begin
        _tmp_84 <= 0;
        _tmp_74 <= 0;
        _tmp_75 <= 0;
        _tmp_82 <= 0;
      end 
      if((_tmp_76 || !_tmp_74) && (_tmp_77 || !_tmp_75) && _tmp_81) begin
        _tmp_74 <= 1;
        _tmp_75 <= 1;
        _tmp_84 <= _tmp_83;
        _tmp_83 <= 0;
        _tmp_81 <= 0;
        _tmp_82 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_85 == 0) && !_tmp_83 && !_tmp_84) begin
        myram1_2_0_addr <= _myaxi_write_local_addr;
        _tmp_85 <= _myaxi_write_size - 1;
        _tmp_81 <= 1;
        _tmp_83 <= _myaxi_write_size == 1;
      end 
      if((_tmp_76 || !_tmp_74) && (_tmp_77 || !_tmp_75) && (_tmp_85 > 0)) begin
        myram1_2_0_addr <= myram1_2_0_addr + _myaxi_write_local_stride;
        _tmp_85 <= _tmp_85 - 1;
        _tmp_81 <= 1;
        _tmp_83 <= 0;
      end 
      if((_tmp_76 || !_tmp_74) && (_tmp_77 || !_tmp_75) && (_tmp_85 == 1)) begin
        _tmp_83 <= 1;
      end 
      if((th_blink == 29) && (_th_blink_bank_5 == 2)) begin
        myram1_2_0_addr <= _th_blink_i_6;
        myram1_2_0_wdata <= _th_blink_wdata_7 + 20;
        myram1_2_0_wenable <= 1;
      end 
      _myram1_2_cond_1_1 <= (th_blink == 29) && (_th_blink_bank_5 == 2);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_125 == 0)) begin
        myram1_2_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_125 <= _myaxi_read_size;
      end 
      if(_slice_valid_127 && ((_tmp_125 > 0) && !_tmp_126) && (_tmp_125 > 0)) begin
        myram1_2_0_addr <= myram1_2_0_addr + _myaxi_read_local_stride;
        myram1_2_0_wdata <= _slice_data_127;
        myram1_2_0_wenable <= 1;
        _tmp_125 <= _tmp_125 - 1;
      end 
      if(_slice_valid_127 && ((_tmp_125 > 0) && !_tmp_126) && (_tmp_125 == 1)) begin
        _tmp_126 <= 1;
      end 
      _myram1_2_cond_2_1 <= 1;
      if(th_blink == 55) begin
        myram1_2_0_addr <= _th_blink_i_6;
      end 
      _myram1_2_cond_3_1 <= th_blink == 55;
      _myram1_2_cond_4_1 <= th_blink == 55;
      if(th_blink == 78) begin
        myram1_2_0_addr <= _th_blink_i_6;
      end 
      _myram1_2_cond_5_1 <= th_blink == 78;
      _myram1_2_cond_6_1 <= th_blink == 78;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram1_3_0_addr <= 0;
      myram1_3_0_wdata <= 0;
      myram1_3_0_wenable <= 0;
      _myram1_3_cond_0_1 <= 0;
      __tmp_91_1 <= 0;
      __tmp_92_1 <= 0;
      _tmp_96 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_93 <= 0;
      _tmp_97 <= 0;
      _myram1_3_cond_1_1 <= 0;
      _tmp_128 <= 0;
      _tmp_129 <= 0;
      _myram1_3_cond_2_1 <= 0;
      _myram1_3_cond_3_1 <= 0;
      _tmp_141 <= 0;
      _myram1_3_cond_4_1 <= 0;
      _myram1_3_cond_4_2 <= 0;
      _myram1_3_cond_5_1 <= 0;
      _tmp_152 <= 0;
      _myram1_3_cond_6_1 <= 0;
      _myram1_3_cond_6_2 <= 0;
    end else begin
      if(_myram1_3_cond_4_2) begin
        _tmp_141 <= 0;
      end 
      if(_myram1_3_cond_6_2) begin
        _tmp_152 <= 0;
      end 
      if(_myram1_3_cond_0_1) begin
        myram1_3_0_wenable <= 0;
      end 
      if(_myram1_3_cond_1_1) begin
        myram1_3_0_wenable <= 0;
      end 
      if(_myram1_3_cond_2_1) begin
        myram1_3_0_wenable <= 0;
        _tmp_129 <= 0;
      end 
      if(_myram1_3_cond_3_1) begin
        _tmp_141 <= 1;
      end 
      _myram1_3_cond_4_2 <= _myram1_3_cond_4_1;
      if(_myram1_3_cond_5_1) begin
        _tmp_152 <= 1;
      end 
      _myram1_3_cond_6_2 <= _myram1_3_cond_6_1;
      if((th_blink == 13) && (_th_blink_bank_5 == 3)) begin
        myram1_3_0_addr <= _th_blink_i_6;
        myram1_3_0_wdata <= _th_blink_wdata_7 + 10;
        myram1_3_0_wenable <= 1;
      end 
      _myram1_3_cond_0_1 <= (th_blink == 13) && (_th_blink_bank_5 == 3);
      __tmp_91_1 <= _tmp_91;
      __tmp_92_1 <= _tmp_92;
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && _tmp_94) begin
        _tmp_96 <= 0;
        _tmp_86 <= 0;
        _tmp_87 <= 0;
        _tmp_94 <= 0;
      end 
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && _tmp_93) begin
        _tmp_86 <= 1;
        _tmp_87 <= 1;
        _tmp_96 <= _tmp_95;
        _tmp_95 <= 0;
        _tmp_93 <= 0;
        _tmp_94 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_97 == 0) && !_tmp_95 && !_tmp_96) begin
        myram1_3_0_addr <= _myaxi_write_local_addr;
        _tmp_97 <= _myaxi_write_size - 1;
        _tmp_93 <= 1;
        _tmp_95 <= _myaxi_write_size == 1;
      end 
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && (_tmp_97 > 0)) begin
        myram1_3_0_addr <= myram1_3_0_addr + _myaxi_write_local_stride;
        _tmp_97 <= _tmp_97 - 1;
        _tmp_93 <= 1;
        _tmp_95 <= 0;
      end 
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && (_tmp_97 == 1)) begin
        _tmp_95 <= 1;
      end 
      if((th_blink == 29) && (_th_blink_bank_5 == 3)) begin
        myram1_3_0_addr <= _th_blink_i_6;
        myram1_3_0_wdata <= _th_blink_wdata_7 + 20;
        myram1_3_0_wenable <= 1;
      end 
      _myram1_3_cond_1_1 <= (th_blink == 29) && (_th_blink_bank_5 == 3);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_128 == 0)) begin
        myram1_3_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_128 <= _myaxi_read_size;
      end 
      if(_slice_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0)) begin
        myram1_3_0_addr <= myram1_3_0_addr + _myaxi_read_local_stride;
        myram1_3_0_wdata <= _slice_data_130;
        myram1_3_0_wenable <= 1;
        _tmp_128 <= _tmp_128 - 1;
      end 
      if(_slice_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 == 1)) begin
        _tmp_129 <= 1;
      end 
      _myram1_3_cond_2_1 <= 1;
      if(th_blink == 55) begin
        myram1_3_0_addr <= _th_blink_i_6;
      end 
      _myram1_3_cond_3_1 <= th_blink == 55;
      _myram1_3_cond_4_1 <= th_blink == 55;
      if(th_blink == 78) begin
        myram1_3_0_addr <= _th_blink_i_6;
      end 
      _myram1_3_cond_5_1 <= th_blink == 78;
      _myram1_3_cond_6_1 <= th_blink == 78;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _d1_th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_offset_2 <= 0;
      _th_blink_size_3 <= 0;
      _th_blink_offset_4 <= 0;
      _th_blink_bank_5 <= 0;
      _th_blink_i_6 <= 0;
      _th_blink_wdata_7 <= 0;
      _th_blink_laddr_8 <= 0;
      _th_blink_gaddr_9 <= 0;
      axim_flag_1 <= 0;
      _th_blink_cond_18_0_1 <= 0;
      axim_flag_103 <= 0;
      _th_blink_cond_34_1_1 <= 0;
      axim_flag_104 <= 0;
      _th_blink_cond_41_2_1 <= 0;
      _tmp_137 <= 0;
      _th_blink_rdata_10 <= 0;
      _tmp_142 <= 0;
      axim_flag_143 <= 0;
      _th_blink_cond_64_3_1 <= 0;
      _tmp_148 <= 0;
      _tmp_153 <= 0;
    end else begin
      _d1_th_blink <= th_blink;
      case(_d1_th_blink)
        th_blink_18: begin
          if(_th_blink_cond_18_0_1) begin
            axim_flag_1 <= 0;
          end 
        end
        th_blink_34: begin
          if(_th_blink_cond_34_1_1) begin
            axim_flag_103 <= 0;
          end 
        end
        th_blink_41: begin
          if(_th_blink_cond_41_2_1) begin
            axim_flag_104 <= 0;
          end 
        end
        th_blink_64: begin
          if(_th_blink_cond_64_3_1) begin
            axim_flag_143 <= 0;
          end 
        end
      endcase
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 16;
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
            th_blink <= th_blink_87;
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
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_16;
          end
        end
        th_blink_9: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_11;
          end else begin
            th_blink <= th_blink_15;
          end
        end
        th_blink_11: begin
          _th_blink_wdata_7 <= _th_blink_i_6 + 100 + _th_blink_bank_5;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_10;
        end
        th_blink_15: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_8;
        end
        th_blink_16: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          _th_blink_gaddr_9 <= _th_blink_offset_4;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          axim_flag_1 <= 1;
          _th_blink_cond_18_0_1 <= 1;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_22;
          end 
        end
        th_blink_22: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_25;
          end else begin
            th_blink <= th_blink_32;
          end
        end
        th_blink_25: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_27;
          end else begin
            th_blink <= th_blink_31;
          end
        end
        th_blink_27: begin
          _th_blink_wdata_7 <= _th_blink_i_6 + 1000 + _th_blink_bank_5;
          th_blink <= th_blink_28;
        end
        th_blink_28: begin
          th_blink <= th_blink_29;
        end
        th_blink_29: begin
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_26;
        end
        th_blink_31: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_24;
        end
        th_blink_32: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          _th_blink_gaddr_9 <= 512 + _th_blink_offset_4;
          th_blink <= th_blink_34;
        end
        th_blink_34: begin
          axim_flag_103 <= 1;
          _th_blink_cond_34_1_1 <= 1;
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          th_blink <= th_blink_36;
        end
        th_blink_36: begin
          th_blink <= th_blink_37;
        end
        th_blink_37: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_38;
          end 
        end
        th_blink_38: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_40;
        end
        th_blink_40: begin
          _th_blink_gaddr_9 <= _th_blink_offset_4;
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          axim_flag_104 <= 1;
          _th_blink_cond_41_2_1 <= 1;
          th_blink <= th_blink_42;
        end
        th_blink_42: begin
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          th_blink <= th_blink_44;
        end
        th_blink_44: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_45;
          end 
        end
        th_blink_45: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_46;
        end
        th_blink_46: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_47;
        end
        th_blink_47: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_48;
          end else begin
            th_blink <= th_blink_62;
          end
        end
        th_blink_48: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_49;
        end
        th_blink_49: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_50;
          end else begin
            th_blink <= th_blink_61;
          end
        end
        th_blink_50: begin
          if(_tmp_133 && (_th_blink_bank_5 == 0)) begin
            _tmp_137 <= myram0_0_0_rdata;
          end 
          if(_tmp_134 && (_th_blink_bank_5 == 1)) begin
            _tmp_137 <= myram0_1_0_rdata;
          end 
          if(_tmp_135 && (_th_blink_bank_5 == 2)) begin
            _tmp_137 <= myram0_2_0_rdata;
          end 
          if(_tmp_136 && (_th_blink_bank_5 == 3)) begin
            _tmp_137 <= myram0_3_0_rdata;
          end 
          if(_tmp_133) begin
            th_blink <= th_blink_51;
          end 
        end
        th_blink_51: begin
          _th_blink_rdata_10 <= _tmp_137;
          th_blink <= th_blink_52;
        end
        th_blink_52: begin
          if(_th_blink_rdata_10 !== _th_blink_i_6 + 100 + _th_blink_bank_5) begin
            th_blink <= th_blink_53;
          end else begin
            th_blink <= th_blink_55;
          end
        end
        th_blink_53: begin
          $display("myram0 rdata[%d] = %d", _th_blink_i_6, _th_blink_rdata_10);
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_55;
        end
        th_blink_55: begin
          if(_tmp_138 && (_th_blink_bank_5 == 0)) begin
            _tmp_142 <= myram1_0_0_rdata;
          end 
          if(_tmp_139 && (_th_blink_bank_5 == 1)) begin
            _tmp_142 <= myram1_1_0_rdata;
          end 
          if(_tmp_140 && (_th_blink_bank_5 == 2)) begin
            _tmp_142 <= myram1_2_0_rdata;
          end 
          if(_tmp_141 && (_th_blink_bank_5 == 3)) begin
            _tmp_142 <= myram1_3_0_rdata;
          end 
          if(_tmp_138) begin
            th_blink <= th_blink_56;
          end 
        end
        th_blink_56: begin
          _th_blink_rdata_10 <= _tmp_142;
          th_blink <= th_blink_57;
        end
        th_blink_57: begin
          if(_th_blink_rdata_10 !== _th_blink_i_6 + 100 + 10 + _th_blink_bank_5) begin
            th_blink <= th_blink_58;
          end else begin
            th_blink <= th_blink_60;
          end
        end
        th_blink_58: begin
          $display("myram1 rdata[%d] = %d", _th_blink_i_6, _th_blink_rdata_10);
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_60;
        end
        th_blink_60: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_49;
        end
        th_blink_61: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_47;
        end
        th_blink_62: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_63;
        end
        th_blink_63: begin
          _th_blink_gaddr_9 <= 512 + _th_blink_offset_4;
          th_blink <= th_blink_64;
        end
        th_blink_64: begin
          axim_flag_143 <= 1;
          _th_blink_cond_64_3_1 <= 1;
          th_blink <= th_blink_65;
        end
        th_blink_65: begin
          th_blink <= th_blink_66;
        end
        th_blink_66: begin
          th_blink <= th_blink_67;
        end
        th_blink_67: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_68;
          end 
        end
        th_blink_68: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_69;
        end
        th_blink_69: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_70;
        end
        th_blink_70: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_71;
          end else begin
            th_blink <= th_blink_85;
          end
        end
        th_blink_71: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_72;
        end
        th_blink_72: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_73;
          end else begin
            th_blink <= th_blink_84;
          end
        end
        th_blink_73: begin
          if(_tmp_144 && (_th_blink_bank_5 == 0)) begin
            _tmp_148 <= myram0_0_0_rdata;
          end 
          if(_tmp_145 && (_th_blink_bank_5 == 1)) begin
            _tmp_148 <= myram0_1_0_rdata;
          end 
          if(_tmp_146 && (_th_blink_bank_5 == 2)) begin
            _tmp_148 <= myram0_2_0_rdata;
          end 
          if(_tmp_147 && (_th_blink_bank_5 == 3)) begin
            _tmp_148 <= myram0_3_0_rdata;
          end 
          if(_tmp_144) begin
            th_blink <= th_blink_74;
          end 
        end
        th_blink_74: begin
          _th_blink_rdata_10 <= _tmp_148;
          th_blink <= th_blink_75;
        end
        th_blink_75: begin
          if(_th_blink_rdata_10 !== _th_blink_i_6 + 1000 + _th_blink_bank_5) begin
            th_blink <= th_blink_76;
          end else begin
            th_blink <= th_blink_78;
          end
        end
        th_blink_76: begin
          $display("myram0 rdata[%d] = %d", _th_blink_i_6, _th_blink_rdata_10);
          th_blink <= th_blink_77;
        end
        th_blink_77: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_78;
        end
        th_blink_78: begin
          if(_tmp_149 && (_th_blink_bank_5 == 0)) begin
            _tmp_153 <= myram1_0_0_rdata;
          end 
          if(_tmp_150 && (_th_blink_bank_5 == 1)) begin
            _tmp_153 <= myram1_1_0_rdata;
          end 
          if(_tmp_151 && (_th_blink_bank_5 == 2)) begin
            _tmp_153 <= myram1_2_0_rdata;
          end 
          if(_tmp_152 && (_th_blink_bank_5 == 3)) begin
            _tmp_153 <= myram1_3_0_rdata;
          end 
          if(_tmp_149) begin
            th_blink <= th_blink_79;
          end 
        end
        th_blink_79: begin
          _th_blink_rdata_10 <= _tmp_153;
          th_blink <= th_blink_80;
        end
        th_blink_80: begin
          if(_th_blink_rdata_10 !== _th_blink_i_6 + 1000 + 20 + _th_blink_bank_5) begin
            th_blink <= th_blink_81;
          end else begin
            th_blink <= th_blink_83;
          end
        end
        th_blink_81: begin
          $display("myram1 rdata[%d] = %d", _th_blink_i_6, _th_blink_rdata_10);
          th_blink <= th_blink_82;
        end
        th_blink_82: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_83;
        end
        th_blink_83: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_72;
        end
        th_blink_84: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_70;
        end
        th_blink_85: begin
          $display("# iter %d end", _th_blink_i_1);
          th_blink <= th_blink_86;
        end
        th_blink_86: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_87: begin
          if(_tmp_0) begin
            th_blink <= th_blink_88;
          end else begin
            th_blink <= th_blink_89;
          end
        end
        th_blink_88: begin
          $display("ALL OK");
          th_blink <= th_blink_89;
        end
      endcase
    end
  end

  localparam _myaxi_write_narrow_2_fsm_1 = 1;
  localparam _myaxi_write_narrow_2_fsm_2 = 2;
  localparam _myaxi_write_narrow_2_fsm_3 = 3;
  localparam _myaxi_write_narrow_2_fsm_4 = 4;
  localparam _myaxi_write_narrow_2_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_init;
      _d1__myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_init;
      _myaxi_write_narrow_2_cur_global_addr <= 0;
      _myaxi_write_narrow_2_rest_size <= 0;
      _myaxi_write_narrow_2_cur_size <= 0;
      axim_flag_102 <= 0;
      __myaxi_write_narrow_2_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm;
      case(_d1__myaxi_write_narrow_2_fsm)
        _myaxi_write_narrow_2_fsm_4: begin
          if(__myaxi_write_narrow_2_fsm_cond_4_0_1) begin
            axim_flag_102 <= 0;
          end 
        end
      endcase
      case(_myaxi_write_narrow_2_fsm)
        _myaxi_write_narrow_2_fsm_init: begin
          if(_myaxi_write_start) begin
            _myaxi_write_narrow_2_cur_global_addr <= (_myaxi_write_global_addr >> 4) << 4;
            _myaxi_write_narrow_2_rest_size <= _myaxi_write_size << 1;
          end 
          if(_myaxi_write_start && (_myaxi_write_op_sel == 1)) begin
            _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_1;
          end 
        end
        _myaxi_write_narrow_2_fsm_1: begin
          if((_myaxi_write_narrow_2_rest_size <= 256) && ((_myaxi_write_narrow_2_cur_global_addr & 4095) + (_myaxi_write_narrow_2_rest_size << 4) >= 4096)) begin
            _myaxi_write_narrow_2_cur_size <= 4096 - (_myaxi_write_narrow_2_cur_global_addr & 4095) >> 4;
            _myaxi_write_narrow_2_rest_size <= _myaxi_write_narrow_2_rest_size - (4096 - (_myaxi_write_narrow_2_cur_global_addr & 4095) >> 4);
          end else if(_myaxi_write_narrow_2_rest_size <= 256) begin
            _myaxi_write_narrow_2_cur_size <= _myaxi_write_narrow_2_rest_size;
            _myaxi_write_narrow_2_rest_size <= 0;
          end else if((_myaxi_write_narrow_2_cur_global_addr & 4095) + 4096 >= 4096) begin
            _myaxi_write_narrow_2_cur_size <= 4096 - (_myaxi_write_narrow_2_cur_global_addr & 4095) >> 4;
            _myaxi_write_narrow_2_rest_size <= _myaxi_write_narrow_2_rest_size - (4096 - (_myaxi_write_narrow_2_cur_global_addr & 4095) >> 4);
          end else begin
            _myaxi_write_narrow_2_cur_size <= 256;
            _myaxi_write_narrow_2_rest_size <= _myaxi_write_narrow_2_rest_size - 256;
          end
          _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_2;
        end
        _myaxi_write_narrow_2_fsm_2: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_3;
          end 
        end
        _myaxi_write_narrow_2_fsm_3: begin
          if(_tmp_100 && myaxi_wvalid && myaxi_wready) begin
            _myaxi_write_narrow_2_cur_global_addr <= _myaxi_write_narrow_2_cur_global_addr + (_myaxi_write_narrow_2_cur_size << 4);
          end 
          if(_tmp_100 && myaxi_wvalid && myaxi_wready && (_myaxi_write_narrow_2_rest_size > 0)) begin
            _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_1;
          end 
          if(_tmp_100 && myaxi_wvalid && myaxi_wready && (_myaxi_write_narrow_2_rest_size == 0)) begin
            _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_4;
          end 
        end
        _myaxi_write_narrow_2_fsm_4: begin
          axim_flag_102 <= 1;
          __myaxi_write_narrow_2_fsm_cond_4_0_1 <= 1;
          _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_5;
        end
        _myaxi_write_narrow_2_fsm_5: begin
          _myaxi_write_narrow_2_fsm <= _myaxi_write_narrow_2_fsm_init;
        end
      endcase
    end
  end

  localparam _myaxi_read_narrow_2_fsm_1 = 1;
  localparam _myaxi_read_narrow_2_fsm_2 = 2;
  localparam _myaxi_read_narrow_2_fsm_3 = 3;
  localparam _myaxi_read_narrow_2_fsm_4 = 4;
  localparam _myaxi_read_narrow_2_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_init;
      _d1__myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_init;
      _myaxi_read_narrow_2_cur_global_addr <= 0;
      _myaxi_read_narrow_2_rest_size <= 0;
      _myaxi_read_narrow_2_cur_size <= 0;
      __myaxi_read_narrow_2_fsm_cond_3_0_1 <= 0;
      _wvalid_106 <= 0;
      _wdata_105 <= 0;
      _myaxi_read_narrow_2_pack_count <= 0;
      axim_flag_132 <= 0;
      __myaxi_read_narrow_2_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm;
      case(_d1__myaxi_read_narrow_2_fsm)
        _myaxi_read_narrow_2_fsm_3: begin
          if(__myaxi_read_narrow_2_fsm_cond_3_0_1) begin
            _wvalid_106 <= 0;
          end 
        end
        _myaxi_read_narrow_2_fsm_4: begin
          if(__myaxi_read_narrow_2_fsm_cond_4_1_1) begin
            axim_flag_132 <= 0;
          end 
        end
      endcase
      case(_myaxi_read_narrow_2_fsm)
        _myaxi_read_narrow_2_fsm_init: begin
          if(_myaxi_read_start) begin
            _myaxi_read_narrow_2_cur_global_addr <= (_myaxi_read_global_addr >> 4) << 4;
            _myaxi_read_narrow_2_rest_size <= _myaxi_read_size << 1;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 1)) begin
            _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_1;
          end 
        end
        _myaxi_read_narrow_2_fsm_1: begin
          if((_myaxi_read_narrow_2_rest_size <= 256) && ((_myaxi_read_narrow_2_cur_global_addr & 4095) + (_myaxi_read_narrow_2_rest_size << 4) >= 4096)) begin
            _myaxi_read_narrow_2_cur_size <= 4096 - (_myaxi_read_narrow_2_cur_global_addr & 4095) >> 4;
            _myaxi_read_narrow_2_rest_size <= _myaxi_read_narrow_2_rest_size - (4096 - (_myaxi_read_narrow_2_cur_global_addr & 4095) >> 4);
          end else if(_myaxi_read_narrow_2_rest_size <= 256) begin
            _myaxi_read_narrow_2_cur_size <= _myaxi_read_narrow_2_rest_size;
            _myaxi_read_narrow_2_rest_size <= 0;
          end else if((_myaxi_read_narrow_2_cur_global_addr & 4095) + 4096 >= 4096) begin
            _myaxi_read_narrow_2_cur_size <= 4096 - (_myaxi_read_narrow_2_cur_global_addr & 4095) >> 4;
            _myaxi_read_narrow_2_rest_size <= _myaxi_read_narrow_2_rest_size - (4096 - (_myaxi_read_narrow_2_cur_global_addr & 4095) >> 4);
          end else begin
            _myaxi_read_narrow_2_cur_size <= 256;
            _myaxi_read_narrow_2_rest_size <= _myaxi_read_narrow_2_rest_size - 256;
          end
          _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_2;
        end
        _myaxi_read_narrow_2_fsm_2: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_3;
          end 
        end
        _myaxi_read_narrow_2_fsm_3: begin
          __myaxi_read_narrow_2_fsm_cond_3_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 1)) begin
            _wdata_105 <= { myaxi_rdata, _wdata_105[255:128] };
            _wvalid_106 <= 0;
            _myaxi_read_narrow_2_pack_count <= _myaxi_read_narrow_2_pack_count + 1;
          end 
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 1) && (_myaxi_read_narrow_2_pack_count == 1)) begin
            _wdata_105 <= { myaxi_rdata, _wdata_105[255:128] };
            _wvalid_106 <= 1;
            _myaxi_read_narrow_2_pack_count <= 0;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_narrow_2_cur_global_addr <= _myaxi_read_narrow_2_cur_global_addr + (_myaxi_read_narrow_2_cur_size << 4);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_narrow_2_rest_size > 0)) begin
            _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_narrow_2_rest_size == 0)) begin
            _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_4;
          end 
        end
        _myaxi_read_narrow_2_fsm_4: begin
          axim_flag_132 <= 1;
          __myaxi_read_narrow_2_fsm_cond_4_1_1 <= 1;
          _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_5;
        end
        _myaxi_read_narrow_2_fsm_5: begin
          _myaxi_read_narrow_2_fsm <= _myaxi_read_narrow_2_fsm_init;
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
    test_module = thread_multibank_nested_ram_dma.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
