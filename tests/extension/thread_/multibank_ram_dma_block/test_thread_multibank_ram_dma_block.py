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
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [32-1:0] myaxi_rdata;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire memory_awvalid;
  reg memory_awready;
  wire [32-1:0] memory_wdata;
  wire [4-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire memory_arvalid;
  reg memory_arready;
  reg [32-1:0] memory_rdata;
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
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [32-1:0] myaxi_rdata,
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
  reg _myram_0_cond_0_1;
  reg _myram_1_cond_0_1;
  reg _myram_2_cond_0_1;
  reg _myram_3_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_11;
  reg signed [32-1:0] _th_blink_gaddr_12;
  reg [10-1:0] req_block_size_1;
  reg set_req_2;
  reg [32-1:0] _d1_th_blink;
  reg _th_blink_cond_29_0_1;
  reg axim_flag_3;
  reg _th_blink_cond_30_1_1;
  reg _myaxi_myram_0_write_start;
  reg [8-1:0] _myaxi_myram_0_write_op_sel;
  reg [32-1:0] _myaxi_myram_0_write_local_addr;
  reg [32-1:0] _myaxi_myram_0_write_global_addr;
  reg [33-1:0] _myaxi_myram_0_write_size;
  reg [32-1:0] _myaxi_myram_0_write_local_stride;
  reg [32-1:0] _myaxi_write_fsm;
  localparam _myaxi_write_fsm_init = 0;
  reg [32-1:0] _myaxi_write_cur_global_addr;
  reg [33-1:0] _myaxi_write_cur_size;
  reg [33-1:0] _myaxi_write_rest_size;
  reg _tmp_4;
  reg _tmp_5;
  wire _tmp_6;
  wire _tmp_7;
  assign _tmp_7 = 1;
  localparam _tmp_8 = 1;
  wire [_tmp_8-1:0] _tmp_9;
  assign _tmp_9 = (_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5);
  reg [_tmp_8-1:0] __tmp_9_1;
  wire signed [32-1:0] _tmp_10;
  wire signed [32-1:0] _tmp_11;
  wire signed [32-1:0] _tmp_12;
  wire signed [32-1:0] _tmp_13;
  reg signed [32-1:0] __tmp_10_1;
  reg signed [32-1:0] __tmp_11_1;
  reg signed [32-1:0] __tmp_12_1;
  reg signed [32-1:0] __tmp_13_1;
  assign _tmp_10 = (__tmp_9_1)? myram_0_0_rdata : __tmp_10_1;
  assign _tmp_11 = (__tmp_9_1)? myram_1_0_rdata : __tmp_11_1;
  assign _tmp_12 = (__tmp_9_1)? myram_2_0_rdata : __tmp_12_1;
  assign _tmp_13 = (__tmp_9_1)? myram_3_0_rdata : __tmp_13_1;
  reg [10-1:0] _tmp_14;
  reg [10-1:0] _tmp_15;
  reg [10-1:0] _tmp_16;
  reg [10-1:0] _tmp_17;
  wire [10-1:0] _tmp_18;
  wire [10-1:0] _tmp_19;
  wire [10-1:0] _tmp_20;
  wire [10-1:0] _tmp_21;
  assign _tmp_18 = _tmp_14 + _myaxi_write_local_stride;
  assign _tmp_19 = _tmp_15 + _myaxi_write_local_stride;
  assign _tmp_20 = _tmp_16 + _myaxi_write_local_stride;
  assign _tmp_21 = _tmp_17 + _myaxi_write_local_stride;
  wire [10-1:0] _tmp_22;
  wire [10-1:0] _tmp_23;
  wire [10-1:0] _tmp_24;
  wire [10-1:0] _tmp_25;
  assign _tmp_22 = _tmp_18;
  assign _tmp_23 = _tmp_19;
  assign _tmp_24 = _tmp_20;
  assign _tmp_25 = _tmp_21;
  reg [2-1:0] _tmp_26;
  reg [2-1:0] _tmp_27;
  reg [2-1:0] __tmp_27_1;
  wire signed [32-1:0] _tmp_28;
  assign _tmp_28 = (__tmp_9_1)? (_tmp_27 == 0)? _tmp_10 : 
                   (_tmp_27 == 1)? _tmp_11 : 
                   (_tmp_27 == 2)? _tmp_12 : 
                   (_tmp_27 == 3)? _tmp_13 : 0 : 
                   (__tmp_27_1 == 0)? __tmp_10_1 : 
                   (__tmp_27_1 == 1)? __tmp_11_1 : 
                   (__tmp_27_1 == 2)? __tmp_12_1 : 
                   (__tmp_27_1 == 3)? __tmp_13_1 : 0;
  reg _tmp_29;
  reg _tmp_30;
  reg _tmp_31;
  reg _tmp_32;
  reg [11-1:0] _tmp_33;
  reg [34-1:0] _tmp_34;
  reg [9-1:0] _tmp_35;
  reg _myaxi_cond_0_1;
  reg _tmp_36;
  wire [32-1:0] __variable_data_37;
  wire __variable_valid_37;
  wire __variable_ready_37;
  assign __variable_ready_37 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_35 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  assign _myaxi_write_data_done = (_tmp_36 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_38;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg _myram_0_cond_1_1;
  reg _myram_1_cond_1_1;
  reg _myram_2_cond_1_1;
  reg _myram_3_cond_1_1;
  reg set_req_39;
  reg _th_blink_cond_59_2_1;
  reg axim_flag_40;
  reg _th_blink_cond_60_3_1;
  reg set_req_41;
  reg _th_blink_cond_67_4_1;
  reg axim_flag_42;
  reg _th_blink_cond_68_5_1;
  reg _myaxi_myram_0_read_start;
  reg [8-1:0] _myaxi_myram_0_read_op_sel;
  reg [32-1:0] _myaxi_myram_0_read_local_addr;
  reg [32-1:0] _myaxi_myram_0_read_global_addr;
  reg [33-1:0] _myaxi_myram_0_read_size;
  reg [32-1:0] _myaxi_myram_0_read_local_stride;
  reg [32-1:0] _myaxi_read_fsm;
  localparam _myaxi_read_fsm_init = 0;
  reg [32-1:0] _myaxi_read_cur_global_addr;
  reg [33-1:0] _myaxi_read_cur_size;
  reg [33-1:0] _myaxi_read_rest_size;
  reg [32-1:0] _wdata_43;
  reg _wvalid_44;
  reg [11-1:0] _tmp_45;
  reg [34-1:0] _tmp_46;
  reg _tmp_47;
  wire [32-1:0] __variable_data_48;
  wire __variable_valid_48;
  wire __variable_ready_48;
  assign __variable_ready_48 = (_tmp_46 > 0) && !_tmp_47;
  reg [10-1:0] _tmp_49;
  reg [10-1:0] _tmp_50;
  reg [10-1:0] _tmp_51;
  reg [10-1:0] _tmp_52;
  wire [10-1:0] _tmp_53;
  wire [10-1:0] _tmp_54;
  wire [10-1:0] _tmp_55;
  wire [10-1:0] _tmp_56;
  assign _tmp_53 = _tmp_49 + _myaxi_read_local_stride;
  assign _tmp_54 = _tmp_50 + _myaxi_read_local_stride;
  assign _tmp_55 = _tmp_51 + _myaxi_read_local_stride;
  assign _tmp_56 = _tmp_52 + _myaxi_read_local_stride;
  wire [10-1:0] _tmp_57;
  wire [10-1:0] _tmp_58;
  wire [10-1:0] _tmp_59;
  wire [10-1:0] _tmp_60;
  assign _tmp_57 = _tmp_53;
  assign _tmp_58 = _tmp_54;
  assign _tmp_59 = _tmp_55;
  assign _tmp_60 = _tmp_56;
  reg [2-1:0] _tmp_61;
  reg _myram_cond_0_1;
  reg _myram_0_cond_2_1;
  reg _myram_1_cond_2_1;
  reg _myram_2_cond_2_1;
  reg _myram_3_cond_2_1;
  reg [9-1:0] _tmp_62;
  reg _myaxi_cond_2_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_63;
  reg __myaxi_read_fsm_cond_4_1_1;
  reg _tmp_64;
  reg _myram_0_cond_3_1;
  reg _myram_0_cond_4_1;
  reg _myram_0_cond_4_2;
  reg _tmp_65;
  reg _myram_1_cond_3_1;
  reg _myram_1_cond_4_1;
  reg _myram_1_cond_4_2;
  reg _tmp_66;
  reg _myram_2_cond_3_1;
  reg _myram_2_cond_4_1;
  reg _myram_2_cond_4_2;
  reg _tmp_67;
  reg _myram_3_cond_3_1;
  reg _myram_3_cond_4_1;
  reg _myram_3_cond_4_2;
  reg signed [32-1:0] _tmp_68;
  reg signed [32-1:0] _th_blink_rdata_13;
  reg signed [32-1:0] _th_blink_exp_14;
  reg set_req_69;
  reg _th_blink_cond_101_6_1;
  reg axim_flag_70;
  reg _th_blink_cond_102_7_1;
  reg _tmp_71;
  reg _myram_0_cond_5_1;
  reg _myram_0_cond_6_1;
  reg _myram_0_cond_6_2;
  reg _tmp_72;
  reg _myram_1_cond_5_1;
  reg _myram_1_cond_6_1;
  reg _myram_1_cond_6_2;
  reg _tmp_73;
  reg _myram_2_cond_5_1;
  reg _myram_2_cond_6_1;
  reg _myram_2_cond_6_2;
  reg _tmp_74;
  reg _myram_3_cond_5_1;
  reg _myram_3_cond_6_1;
  reg _myram_3_cond_6_2;
  reg signed [32-1:0] _tmp_75;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram_0_write_start <= 0;
      _myaxi_myram_0_write_op_sel <= 0;
      _myaxi_myram_0_write_local_addr <= 0;
      _myaxi_myram_0_write_global_addr <= 0;
      _myaxi_myram_0_write_size <= 0;
      _myaxi_myram_0_write_local_stride <= 0;
      _myaxi_write_idle <= 1;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_size <= 0;
      _myaxi_write_local_stride <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_35 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_36 <= 0;
      _myaxi_cond_1_1 <= 0;
      _myaxi_myram_0_read_start <= 0;
      _myaxi_myram_0_read_op_sel <= 0;
      _myaxi_myram_0_read_local_addr <= 0;
      _myaxi_myram_0_read_global_addr <= 0;
      _myaxi_myram_0_read_size <= 0;
      _myaxi_myram_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_62 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_36 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_arvalid <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram_0_write_start <= 0;
      if(axim_flag_3) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_11;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram_0_write_size <= _th_blink_size_2;
        _myaxi_myram_0_write_local_stride <= 1;
      end 
      if(_myaxi_myram_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_myram_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_myram_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_myram_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_myram_0_write_global_addr;
        _myaxi_write_size <= _myaxi_myram_0_write_size;
        _myaxi_write_local_stride <= _myaxi_myram_0_write_local_stride;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_35 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_35 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_35 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_37 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_35 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_35 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_35 > 0))) begin
        myaxi_wdata <= __variable_data_37;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_35 <= _tmp_35 - 1;
      end 
      if(__variable_valid_37 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_35 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_35 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_35 > 0)) && (_tmp_35 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_36 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_36 <= _tmp_36;
      end 
      if(axim_flag_38) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_40) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_11;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram_0_write_size <= _th_blink_size_2;
        _myaxi_myram_0_write_local_stride <= 1;
      end 
      _myaxi_myram_0_read_start <= 0;
      if(axim_flag_42) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_11;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram_0_read_size <= _th_blink_size_2;
        _myaxi_myram_0_read_local_stride <= 1;
      end 
      if(_myaxi_myram_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_myram_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_myram_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_myram_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_myram_0_read_global_addr;
        _myaxi_read_size <= _myaxi_myram_0_read_size;
        _myaxi_read_local_stride <= _myaxi_myram_0_read_local_stride;
      end 
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_62 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_62 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_62 > 0)) begin
        _tmp_62 <= _tmp_62 - 1;
      end 
      if(axim_flag_63) begin
        _myaxi_read_idle <= 1;
      end 
      if(axim_flag_70) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_11;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_12;
        _myaxi_myram_0_read_size <= _th_blink_size_2;
        _myaxi_myram_0_read_local_stride <= 1;
      end 
    end
  end

  assign __variable_data_48 = _wdata_43;
  assign __variable_valid_48 = _wvalid_44;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_0_addr <= 0;
      myram_0_0_wdata <= 0;
      myram_0_0_wenable <= 0;
      _myram_0_cond_0_1 <= 0;
      _myram_0_cond_1_1 <= 0;
      _myram_0_cond_2_1 <= 0;
      _myram_0_cond_3_1 <= 0;
      _tmp_64 <= 0;
      _myram_0_cond_4_1 <= 0;
      _myram_0_cond_4_2 <= 0;
      _myram_0_cond_5_1 <= 0;
      _tmp_71 <= 0;
      _myram_0_cond_6_1 <= 0;
      _myram_0_cond_6_2 <= 0;
    end else begin
      if(_myram_0_cond_4_2) begin
        _tmp_64 <= 0;
      end 
      if(_myram_0_cond_6_2) begin
        _tmp_71 <= 0;
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
        _tmp_64 <= 1;
      end 
      _myram_0_cond_4_2 <= _myram_0_cond_4_1;
      if(_myram_0_cond_5_1) begin
        _tmp_71 <= 1;
      end 
      _myram_0_cond_6_2 <= _myram_0_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 0)) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_0_0_wdata <= _th_blink_wdata_10;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 0);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        myram_0_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 0)) begin
        myram_0_0_addr <= _tmp_22;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 0)) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_0_0_wdata <= _th_blink_wdata_10;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 0);
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0)) begin
        myram_0_0_addr <= _tmp_57;
        myram_0_0_wdata <= __variable_data_48;
        myram_0_0_wenable <= _tmp_61 == 0;
      end 
      _myram_0_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_0_cond_3_1 <= th_blink == 82;
      _myram_0_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_0_cond_5_1 <= th_blink == 116;
      _myram_0_cond_6_1 <= th_blink == 116;
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
      _tmp_65 <= 0;
      _myram_1_cond_4_1 <= 0;
      _myram_1_cond_4_2 <= 0;
      _myram_1_cond_5_1 <= 0;
      _tmp_72 <= 0;
      _myram_1_cond_6_1 <= 0;
      _myram_1_cond_6_2 <= 0;
    end else begin
      if(_myram_1_cond_4_2) begin
        _tmp_65 <= 0;
      end 
      if(_myram_1_cond_6_2) begin
        _tmp_72 <= 0;
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
        _tmp_65 <= 1;
      end 
      _myram_1_cond_4_2 <= _myram_1_cond_4_1;
      if(_myram_1_cond_5_1) begin
        _tmp_72 <= 1;
      end 
      _myram_1_cond_6_2 <= _myram_1_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 1)) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_1_0_wdata <= _th_blink_wdata_10;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 1);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        myram_1_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 1)) begin
        myram_1_0_addr <= _tmp_23;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 1)) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_1_0_wdata <= _th_blink_wdata_10;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 1);
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0)) begin
        myram_1_0_addr <= _tmp_58;
        myram_1_0_wdata <= __variable_data_48;
        myram_1_0_wenable <= _tmp_61 == 1;
      end 
      _myram_1_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_1_cond_3_1 <= th_blink == 82;
      _myram_1_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_1_cond_5_1 <= th_blink == 116;
      _myram_1_cond_6_1 <= th_blink == 116;
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
      _tmp_66 <= 0;
      _myram_2_cond_4_1 <= 0;
      _myram_2_cond_4_2 <= 0;
      _myram_2_cond_5_1 <= 0;
      _tmp_73 <= 0;
      _myram_2_cond_6_1 <= 0;
      _myram_2_cond_6_2 <= 0;
    end else begin
      if(_myram_2_cond_4_2) begin
        _tmp_66 <= 0;
      end 
      if(_myram_2_cond_6_2) begin
        _tmp_73 <= 0;
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
        _tmp_66 <= 1;
      end 
      _myram_2_cond_4_2 <= _myram_2_cond_4_1;
      if(_myram_2_cond_5_1) begin
        _tmp_73 <= 1;
      end 
      _myram_2_cond_6_2 <= _myram_2_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 2)) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_2_0_wdata <= _th_blink_wdata_10;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 2);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        myram_2_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 2)) begin
        myram_2_0_addr <= _tmp_24;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 2)) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_2_0_wdata <= _th_blink_wdata_10;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 2);
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0)) begin
        myram_2_0_addr <= _tmp_59;
        myram_2_0_wdata <= __variable_data_48;
        myram_2_0_wenable <= _tmp_61 == 2;
      end 
      _myram_2_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_2_cond_3_1 <= th_blink == 82;
      _myram_2_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_2_cond_5_1 <= th_blink == 116;
      _myram_2_cond_6_1 <= th_blink == 116;
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
      _tmp_67 <= 0;
      _myram_3_cond_4_1 <= 0;
      _myram_3_cond_4_2 <= 0;
      _myram_3_cond_5_1 <= 0;
      _tmp_74 <= 0;
      _myram_3_cond_6_1 <= 0;
      _myram_3_cond_6_2 <= 0;
    end else begin
      if(_myram_3_cond_4_2) begin
        _tmp_67 <= 0;
      end 
      if(_myram_3_cond_6_2) begin
        _tmp_74 <= 0;
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
        _tmp_67 <= 1;
      end 
      _myram_3_cond_4_2 <= _myram_3_cond_4_1;
      if(_myram_3_cond_5_1) begin
        _tmp_74 <= 1;
      end 
      _myram_3_cond_6_2 <= _myram_3_cond_6_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 3)) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_3_0_wdata <= _th_blink_wdata_10;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 3);
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        myram_3_0_addr <= _myaxi_write_local_addr;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 3)) begin
        myram_3_0_addr <= _tmp_25;
      end 
      if((th_blink == 45) && (_th_blink_bank_8 == 3)) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_3_0_wdata <= _th_blink_wdata_10;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_1_1 <= (th_blink == 45) && (_th_blink_bank_8 == 3);
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0)) begin
        myram_3_0_addr <= _tmp_60;
        myram_3_0_wdata <= __variable_data_48;
        myram_3_0_wenable <= _tmp_61 == 3;
      end 
      _myram_3_cond_2_1 <= 1;
      if(th_blink == 82) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_3_cond_3_1 <= th_blink == 82;
      _myram_3_cond_4_1 <= th_blink == 82;
      if(th_blink == 116) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_3_cond_5_1 <= th_blink == 116;
      _myram_3_cond_6_1 <= th_blink == 116;
    end
  end

  assign __variable_data_37 = _tmp_28;
  assign __variable_valid_37 = _tmp_4;
  assign _tmp_6 = 1 && __variable_ready_37;
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
      set_req_2 <= 0;
      _th_blink_cond_29_0_1 <= 0;
      axim_flag_3 <= 0;
      _th_blink_cond_30_1_1 <= 0;
      set_req_39 <= 0;
      _th_blink_cond_59_2_1 <= 0;
      axim_flag_40 <= 0;
      _th_blink_cond_60_3_1 <= 0;
      set_req_41 <= 0;
      _th_blink_cond_67_4_1 <= 0;
      axim_flag_42 <= 0;
      _th_blink_cond_68_5_1 <= 0;
      _tmp_68 <= 0;
      _th_blink_rdata_13 <= 0;
      _th_blink_exp_14 <= 0;
      set_req_69 <= 0;
      _th_blink_cond_101_6_1 <= 0;
      axim_flag_70 <= 0;
      _th_blink_cond_102_7_1 <= 0;
      _tmp_75 <= 0;
    end else begin
      _d1_th_blink <= th_blink;
      case(_d1_th_blink)
        th_blink_29: begin
          if(_th_blink_cond_29_0_1) begin
            set_req_2 <= 0;
          end 
        end
        th_blink_30: begin
          if(_th_blink_cond_30_1_1) begin
            axim_flag_3 <= 0;
          end 
        end
        th_blink_59: begin
          if(_th_blink_cond_59_2_1) begin
            set_req_39 <= 0;
          end 
        end
        th_blink_60: begin
          if(_th_blink_cond_60_3_1) begin
            axim_flag_40 <= 0;
          end 
        end
        th_blink_67: begin
          if(_th_blink_cond_67_4_1) begin
            set_req_41 <= 0;
          end 
        end
        th_blink_68: begin
          if(_th_blink_cond_68_5_1) begin
            axim_flag_42 <= 0;
          end 
        end
        th_blink_101: begin
          if(_th_blink_cond_101_6_1) begin
            set_req_69 <= 0;
          end 
        end
        th_blink_102: begin
          if(_th_blink_cond_102_7_1) begin
            axim_flag_70 <= 0;
          end 
        end
      endcase
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
          $display("# start");
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _th_blink_offset_1 <= 16384;
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
          if(_th_blink_bank_8 < 4) begin
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
          if(_th_blink_i_9 < 3) begin
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
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_11;
        end
        th_blink_25: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
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
          set_req_2 <= 1;
          _th_blink_cond_29_0_1 <= 1;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          axim_flag_3 <= 1;
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
          if(_th_blink_bank_8 < 4) begin
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
          if(_th_blink_i_9 < 3) begin
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
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_41;
        end
        th_blink_55: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
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
          _th_blink_gaddr_12 <= 1024 + _th_blink_offset_3;
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          set_req_39 <= 1;
          _th_blink_cond_59_2_1 <= 1;
          th_blink <= th_blink_60;
        end
        th_blink_60: begin
          axim_flag_40 <= 1;
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
          set_req_41 <= 1;
          _th_blink_cond_67_4_1 <= 1;
          th_blink <= th_blink_68;
        end
        th_blink_68: begin
          axim_flag_42 <= 1;
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
          if(_th_blink_bank_8 < 4) begin
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
          if(_th_blink_i_9 < 3) begin
            th_blink <= th_blink_82;
          end else begin
            th_blink <= th_blink_93;
          end
        end
        th_blink_82: begin
          if(_tmp_64 && (_th_blink_bank_8 == 0)) begin
            _tmp_68 <= myram_0_0_rdata;
          end 
          if(_tmp_65 && (_th_blink_bank_8 == 1)) begin
            _tmp_68 <= myram_1_0_rdata;
          end 
          if(_tmp_66 && (_th_blink_bank_8 == 2)) begin
            _tmp_68 <= myram_2_0_rdata;
          end 
          if(_tmp_67 && (_th_blink_bank_8 == 3)) begin
            _tmp_68 <= myram_3_0_rdata;
          end 
          if(_tmp_64) begin
            th_blink <= th_blink_83;
          end 
        end
        th_blink_83: begin
          _th_blink_rdata_13 <= _tmp_68;
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
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_96;
        end
        th_blink_96: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_79;
        end
        th_blink_97: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
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
          _th_blink_gaddr_12 <= 1024 + _th_blink_offset_3;
          th_blink <= th_blink_101;
        end
        th_blink_101: begin
          set_req_69 <= 1;
          _th_blink_cond_101_6_1 <= 1;
          th_blink <= th_blink_102;
        end
        th_blink_102: begin
          axim_flag_70 <= 1;
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
          if(_th_blink_bank_8 < 4) begin
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
          if(_th_blink_i_9 < 3) begin
            th_blink <= th_blink_116;
          end else begin
            th_blink <= th_blink_127;
          end
        end
        th_blink_116: begin
          if(_tmp_71 && (_th_blink_bank_8 == 0)) begin
            _tmp_75 <= myram_0_0_rdata;
          end 
          if(_tmp_72 && (_th_blink_bank_8 == 1)) begin
            _tmp_75 <= myram_1_0_rdata;
          end 
          if(_tmp_73 && (_th_blink_bank_8 == 2)) begin
            _tmp_75 <= myram_2_0_rdata;
          end 
          if(_tmp_74 && (_th_blink_bank_8 == 3)) begin
            _tmp_75 <= myram_3_0_rdata;
          end 
          if(_tmp_71) begin
            th_blink <= th_blink_117;
          end 
        end
        th_blink_117: begin
          _th_blink_rdata_13 <= _tmp_75;
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
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_130;
        end
        th_blink_130: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_113;
        end
        th_blink_131: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
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
      req_block_size_1 <= 0;
    end else begin
      if(set_req_2) begin
        req_block_size_1 <= 3;
      end 
      if(set_req_39) begin
        req_block_size_1 <= 3;
      end 
      if(set_req_41) begin
        req_block_size_1 <= 3;
      end 
      if(set_req_69) begin
        req_block_size_1 <= 3;
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
      axim_flag_38 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_38 <= 0;
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
          axim_flag_38 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_9_1 <= 0;
      __tmp_10_1 <= 0;
      __tmp_11_1 <= 0;
      __tmp_12_1 <= 0;
      __tmp_13_1 <= 0;
      __tmp_27_1 <= 0;
      _tmp_27 <= 0;
      _tmp_32 <= 0;
      _tmp_4 <= 0;
      _tmp_5 <= 0;
      _tmp_30 <= 0;
      _tmp_31 <= 0;
      _tmp_29 <= 0;
      _tmp_26 <= 0;
      _tmp_33 <= 0;
      _tmp_34 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_17 <= 0;
      _tmp_61 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_47 <= 0;
      _myram_cond_0_1 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        _tmp_47 <= 0;
      end 
      __tmp_9_1 <= _tmp_9;
      __tmp_10_1 <= _tmp_10;
      __tmp_11_1 <= _tmp_11;
      __tmp_12_1 <= _tmp_12;
      __tmp_13_1 <= _tmp_13;
      __tmp_27_1 <= _tmp_27;
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5)) begin
        _tmp_27 <= _tmp_26;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && _tmp_30) begin
        _tmp_32 <= 0;
        _tmp_4 <= 0;
        _tmp_5 <= 0;
        _tmp_30 <= 0;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && _tmp_29) begin
        _tmp_4 <= 1;
        _tmp_5 <= 1;
        _tmp_32 <= _tmp_31;
        _tmp_31 <= 0;
        _tmp_29 <= 0;
        _tmp_30 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        _tmp_26 <= 0;
        _tmp_27 <= 0;
        _tmp_33 <= req_block_size_1 - 1;
        _tmp_34 <= _myaxi_write_size - 1;
        _tmp_29 <= 1;
        _tmp_31 <= _myaxi_write_size == 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        _tmp_14 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        _tmp_15 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        _tmp_16 <= _myaxi_write_local_addr;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_34 == 0) && !_tmp_31 && !_tmp_32) begin
        _tmp_17 <= _myaxi_write_local_addr;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0)) begin
        _tmp_33 <= _tmp_33 - 1;
        _tmp_34 <= _tmp_34 - 1;
        _tmp_29 <= 1;
        _tmp_31 <= 0;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_33 == 0)) begin
        _tmp_33 <= req_block_size_1 - 1;
        _tmp_26 <= _tmp_26 + 1;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_33 == 0) && (_tmp_26 == 3)) begin
        _tmp_26 <= 0;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 0)) begin
        _tmp_14 <= _tmp_18;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 1)) begin
        _tmp_15 <= _tmp_19;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 2)) begin
        _tmp_16 <= _tmp_20;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 > 0) && (_tmp_26 == 3)) begin
        _tmp_17 <= _tmp_21;
      end 
      if((_tmp_6 || !_tmp_4) && (_tmp_7 || !_tmp_5) && (_tmp_34 == 1)) begin
        _tmp_31 <= 1;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_46 == 0)) begin
        _tmp_61 <= 0;
        _tmp_45 <= req_block_size_1 - 1;
        _tmp_46 <= _myaxi_read_size;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_46 == 0)) begin
        _tmp_49 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_46 == 0)) begin
        _tmp_50 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_46 == 0)) begin
        _tmp_51 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_46 == 0)) begin
        _tmp_52 <= _myaxi_read_local_addr - _myaxi_read_local_stride;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0)) begin
        _tmp_45 <= _tmp_45 - 1;
        _tmp_46 <= _tmp_46 - 1;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0) && (_tmp_45 == 0)) begin
        _tmp_45 <= req_block_size_1 - 1;
        _tmp_61 <= _tmp_61 + 1;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0) && (_tmp_45 == 0) && (_tmp_61 == 3)) begin
        _tmp_61 <= 0;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0) && (_tmp_61 == 0)) begin
        _tmp_49 <= _tmp_53;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0) && (_tmp_61 == 1)) begin
        _tmp_50 <= _tmp_54;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0) && (_tmp_61 == 2)) begin
        _tmp_51 <= _tmp_55;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 > 0) && (_tmp_61 == 3)) begin
        _tmp_52 <= _tmp_56;
      end 
      if(__variable_valid_48 && ((_tmp_46 > 0) && !_tmp_47) && (_tmp_46 == 1)) begin
        _tmp_47 <= 1;
      end 
      _myram_cond_0_1 <= 1;
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
      _wvalid_44 <= 0;
      _wdata_43 <= 0;
      axim_flag_63 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_44 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_63 <= 0;
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
            _wdata_43 <= myaxi_rdata;
            _wvalid_44 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_63 <= 1;
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
