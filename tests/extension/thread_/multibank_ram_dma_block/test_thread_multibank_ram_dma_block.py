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
  reg [10-1:0] _tmp_18;
  reg [10-1:0] _tmp_19;
  reg [10-1:0] _tmp_20;
  reg [10-1:0] _tmp_21;
  wire [10-1:0] _tmp_22;
  wire [10-1:0] _tmp_23;
  wire [10-1:0] _tmp_24;
  wire [10-1:0] _tmp_25;
  assign _tmp_22 = _tmp_18 + 1;
  assign _tmp_23 = _tmp_19 + 1;
  assign _tmp_24 = _tmp_20 + 1;
  assign _tmp_25 = _tmp_21 + 1;
  wire [10-1:0] _tmp_26;
  wire [10-1:0] _tmp_27;
  wire [10-1:0] _tmp_28;
  wire [10-1:0] _tmp_29;
  assign _tmp_26 = _tmp_22;
  assign _tmp_27 = _tmp_23;
  assign _tmp_28 = _tmp_24;
  assign _tmp_29 = _tmp_25;
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
  reg _tmp_40;
  wire [32-1:0] __variable_data_41;
  wire __variable_valid_41;
  wire __variable_ready_41;
  assign __variable_ready_41 = (_tmp_fsm_0 == 4) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  reg _tmp_42;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_5_0_1;
  reg _myram_0_cond_1_1;
  reg _myram_1_cond_1_1;
  reg _myram_2_cond_1_1;
  reg _myram_3_cond_1_1;
  reg [10-1:0] _tmp_43;
  reg [10-1:0] _tmp_44;
  reg [32-1:0] _tmp_45;
  reg [32-1:0] _tmp_46;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_47;
  reg [33-1:0] _tmp_48;
  reg [33-1:0] _tmp_49;
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
  wire signed [32-1:0] _tmp_57;
  wire signed [32-1:0] _tmp_58;
  wire signed [32-1:0] _tmp_59;
  reg signed [32-1:0] __tmp_56_1;
  reg signed [32-1:0] __tmp_57_1;
  reg signed [32-1:0] __tmp_58_1;
  reg signed [32-1:0] __tmp_59_1;
  assign _tmp_56 = (__tmp_55_1)? myram_0_0_rdata : __tmp_56_1;
  assign _tmp_57 = (__tmp_55_1)? myram_1_0_rdata : __tmp_57_1;
  assign _tmp_58 = (__tmp_55_1)? myram_2_0_rdata : __tmp_58_1;
  assign _tmp_59 = (__tmp_55_1)? myram_3_0_rdata : __tmp_59_1;
  reg [10-1:0] _tmp_60;
  reg [10-1:0] _tmp_61;
  reg [10-1:0] _tmp_62;
  reg [10-1:0] _tmp_63;
  wire [10-1:0] _tmp_64;
  wire [10-1:0] _tmp_65;
  wire [10-1:0] _tmp_66;
  wire [10-1:0] _tmp_67;
  assign _tmp_64 = _tmp_60 + 1;
  assign _tmp_65 = _tmp_61 + 1;
  assign _tmp_66 = _tmp_62 + 1;
  assign _tmp_67 = _tmp_63 + 1;
  wire [10-1:0] _tmp_68;
  wire [10-1:0] _tmp_69;
  wire [10-1:0] _tmp_70;
  wire [10-1:0] _tmp_71;
  assign _tmp_68 = _tmp_64;
  assign _tmp_69 = _tmp_65;
  assign _tmp_70 = _tmp_66;
  assign _tmp_71 = _tmp_67;
  reg [2-1:0] _tmp_72;
  reg [2-1:0] _tmp_73;
  reg [2-1:0] __tmp_73_1;
  wire signed [32-1:0] _tmp_74;
  assign _tmp_74 = (__tmp_55_1)? (_tmp_73 == 0)? _tmp_56 : 
                   (_tmp_73 == 1)? _tmp_57 : 
                   (_tmp_73 == 2)? _tmp_58 : 
                   (_tmp_73 == 3)? _tmp_59 : 0 : 
                   (__tmp_73_1 == 0)? __tmp_56_1 : 
                   (__tmp_73_1 == 1)? __tmp_57_1 : 
                   (__tmp_73_1 == 2)? __tmp_58_1 : 
                   (__tmp_73_1 == 3)? __tmp_59_1 : 0;
  reg _tmp_75;
  reg _tmp_76;
  reg _tmp_77;
  reg _tmp_78;
  reg [11-1:0] _tmp_79;
  reg [33-1:0] _tmp_80;
  reg [9-1:0] _tmp_81;
  reg _myaxi_cond_2_1;
  reg _tmp_82;
  wire [32-1:0] __variable_data_83;
  wire __variable_valid_83;
  wire __variable_ready_83;
  assign __variable_ready_83 = (_tmp_fsm_1 == 4) && ((_tmp_81 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_84;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_5_0_1;
  reg [10-1:0] _tmp_85;
  reg [10-1:0] _tmp_86;
  reg [32-1:0] _tmp_87;
  reg [32-1:0] _tmp_88;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_89;
  reg [33-1:0] _tmp_90;
  reg [33-1:0] _tmp_91;
  reg [128-1:0] _tmp_92;
  reg _tmp_93;
  reg [11-1:0] _tmp_94;
  reg [33-1:0] _tmp_95;
  reg _tmp_96;
  wire [128-1:0] __variable_data_97;
  wire __variable_valid_97;
  wire __variable_ready_97;
  assign __variable_ready_97 = (_tmp_95 > 0) && !_tmp_96;
  reg [10-1:0] _tmp_98;
  reg [10-1:0] _tmp_99;
  reg [10-1:0] _tmp_100;
  reg [10-1:0] _tmp_101;
  wire [10-1:0] _tmp_102;
  wire [10-1:0] _tmp_103;
  wire [10-1:0] _tmp_104;
  wire [10-1:0] _tmp_105;
  assign _tmp_102 = _tmp_98 + 1;
  assign _tmp_103 = _tmp_99 + 1;
  assign _tmp_104 = _tmp_100 + 1;
  assign _tmp_105 = _tmp_101 + 1;
  wire [10-1:0] _tmp_106;
  wire [10-1:0] _tmp_107;
  wire [10-1:0] _tmp_108;
  wire [10-1:0] _tmp_109;
  assign _tmp_106 = _tmp_102;
  assign _tmp_107 = _tmp_103;
  assign _tmp_108 = _tmp_104;
  assign _tmp_109 = _tmp_105;
  reg [2-1:0] _tmp_110;
  reg _myram_cond_0_1;
  reg _myram_0_cond_2_1;
  reg _myram_1_cond_2_1;
  reg _myram_2_cond_2_1;
  reg _myram_3_cond_2_1;
  reg [9-1:0] _tmp_111;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_4_0_1;
  reg _tmp_112;
  reg __tmp_fsm_2_cond_5_1_1;
  reg _tmp_113;
  reg _myram_0_cond_3_1;
  reg _myram_0_cond_4_1;
  reg _myram_0_cond_4_2;
  reg _tmp_114;
  reg _myram_1_cond_3_1;
  reg _myram_1_cond_4_1;
  reg _myram_1_cond_4_2;
  reg _tmp_115;
  reg _myram_2_cond_3_1;
  reg _myram_2_cond_4_1;
  reg _myram_2_cond_4_2;
  reg _tmp_116;
  reg _myram_3_cond_3_1;
  reg _myram_3_cond_4_1;
  reg _myram_3_cond_4_2;
  reg signed [32-1:0] _tmp_117;
  reg signed [32-1:0] _th_blink_rdata_13;
  reg signed [32-1:0] _th_blink_exp_14;
  reg [10-1:0] _tmp_118;
  reg [10-1:0] _tmp_119;
  reg [32-1:0] _tmp_120;
  reg [32-1:0] _tmp_121;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_122;
  reg [33-1:0] _tmp_123;
  reg [33-1:0] _tmp_124;
  reg [128-1:0] _tmp_125;
  reg _tmp_126;
  reg [11-1:0] _tmp_127;
  reg [33-1:0] _tmp_128;
  reg _tmp_129;
  wire [128-1:0] __variable_data_130;
  wire __variable_valid_130;
  wire __variable_ready_130;
  assign __variable_ready_130 = (_tmp_128 > 0) && !_tmp_129;
  reg [10-1:0] _tmp_131;
  reg [10-1:0] _tmp_132;
  reg [10-1:0] _tmp_133;
  reg [10-1:0] _tmp_134;
  wire [10-1:0] _tmp_135;
  wire [10-1:0] _tmp_136;
  wire [10-1:0] _tmp_137;
  wire [10-1:0] _tmp_138;
  assign _tmp_135 = _tmp_131 + 1;
  assign _tmp_136 = _tmp_132 + 1;
  assign _tmp_137 = _tmp_133 + 1;
  assign _tmp_138 = _tmp_134 + 1;
  wire [10-1:0] _tmp_139;
  wire [10-1:0] _tmp_140;
  wire [10-1:0] _tmp_141;
  wire [10-1:0] _tmp_142;
  assign _tmp_139 = _tmp_135;
  assign _tmp_140 = _tmp_136;
  assign _tmp_141 = _tmp_137;
  assign _tmp_142 = _tmp_138;
  reg [2-1:0] _tmp_143;
  reg _myram_cond_1_1;
  reg _myram_0_cond_5_1;
  reg _myram_1_cond_5_1;
  reg _myram_2_cond_5_1;
  reg _myram_3_cond_5_1;
  reg [9-1:0] _tmp_144;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_2 == 4) || (_tmp_fsm_3 == 4);
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_145;
  reg __tmp_fsm_3_cond_5_1_1;
  reg _tmp_146;
  reg _myram_0_cond_6_1;
  reg _myram_0_cond_7_1;
  reg _myram_0_cond_7_2;
  reg _tmp_147;
  reg _myram_1_cond_6_1;
  reg _myram_1_cond_7_1;
  reg _myram_1_cond_7_2;
  reg _tmp_148;
  reg _myram_2_cond_6_1;
  reg _myram_2_cond_7_1;
  reg _myram_2_cond_7_2;
  reg _tmp_149;
  reg _myram_3_cond_6_1;
  reg _myram_3_cond_7_1;
  reg _myram_3_cond_7_2;
  reg signed [32-1:0] _tmp_150;

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
      _tmp_40 <= 0;
      _myaxi_cond_1_1 <= 0;
      _tmp_81 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_82 <= 0;
      _myaxi_cond_3_1 <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_111 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_144 <= 0;
      _myaxi_cond_5_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_40 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_82 <= 0;
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
      if(__variable_valid_41 && ((_tmp_fsm_0 == 4) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0))) begin
        myaxi_wdata <= __variable_data_41;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_39 <= _tmp_39 - 1;
      end 
      if(__variable_valid_41 && ((_tmp_fsm_0 == 4) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0)) && (_tmp_39 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_40 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_40 <= _tmp_40;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_81 == 0))) begin
        myaxi_awaddr <= _tmp_47;
        myaxi_awlen <= _tmp_48 - 1;
        myaxi_awvalid <= 1;
        _tmp_81 <= _tmp_48;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_81 == 0)) && (_tmp_48 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_83 && ((_tmp_fsm_1 == 4) && ((_tmp_81 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_81 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_81 > 0))) begin
        myaxi_wdata <= __variable_data_83;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_81 <= _tmp_81 - 1;
      end 
      if(__variable_valid_83 && ((_tmp_fsm_1 == 4) && ((_tmp_81 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_81 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_81 > 0)) && (_tmp_81 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_82 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_82 <= _tmp_82;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_111 == 0))) begin
        myaxi_araddr <= _tmp_89;
        myaxi_arlen <= _tmp_90 - 1;
        myaxi_arvalid <= 1;
        _tmp_111 <= _tmp_90;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_111 > 0)) begin
        _tmp_111 <= _tmp_111 - 1;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_144 == 0))) begin
        myaxi_araddr <= _tmp_122;
        myaxi_arlen <= _tmp_123 - 1;
        myaxi_arvalid <= 1;
        _tmp_144 <= _tmp_123;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_144 > 0)) begin
        _tmp_144 <= _tmp_144 - 1;
      end 
    end
  end

  assign __variable_data_97 = _tmp_92;
  assign __variable_valid_97 = _tmp_93;
  assign __variable_data_130 = _tmp_125;
  assign __variable_valid_130 = _tmp_126;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_0_addr <= 0;
      myram_0_0_wdata <= 0;
      myram_0_0_wenable <= 0;
      _myram_0_cond_0_1 <= 0;
      _myram_0_cond_1_1 <= 0;
      _myram_0_cond_2_1 <= 0;
      _myram_0_cond_3_1 <= 0;
      _tmp_113 <= 0;
      _myram_0_cond_4_1 <= 0;
      _myram_0_cond_4_2 <= 0;
      _myram_0_cond_5_1 <= 0;
      _myram_0_cond_6_1 <= 0;
      _tmp_146 <= 0;
      _myram_0_cond_7_1 <= 0;
      _myram_0_cond_7_2 <= 0;
    end else begin
      if(_myram_0_cond_4_2) begin
        _tmp_113 <= 0;
      end 
      if(_myram_0_cond_7_2) begin
        _tmp_146 <= 0;
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
        _tmp_113 <= 1;
      end 
      _myram_0_cond_4_2 <= _myram_0_cond_4_1;
      if(_myram_0_cond_5_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_6_1) begin
        _tmp_146 <= 1;
      end 
      _myram_0_cond_7_2 <= _myram_0_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 0)) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_0_0_wdata <= _th_blink_wdata_10;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 0);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_0_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 0)) begin
        myram_0_0_addr <= _tmp_26;
      end 
      if((th_blink == 42) && (_th_blink_bank_8 == 0)) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_0_0_wdata <= _th_blink_wdata_10;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_1_1 <= (th_blink == 42) && (_th_blink_bank_8 == 0);
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        myram_0_0_addr <= _tmp_44;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 0)) begin
        myram_0_0_addr <= _tmp_68;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0)) begin
        myram_0_0_addr <= _tmp_106;
        myram_0_0_wdata <= __variable_data_97;
        myram_0_0_wenable <= _tmp_110 == 0;
      end 
      _myram_0_cond_2_1 <= 1;
      if(th_blink == 73) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_0_cond_3_1 <= th_blink == 73;
      _myram_0_cond_4_1 <= th_blink == 73;
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0)) begin
        myram_0_0_addr <= _tmp_139;
        myram_0_0_wdata <= __variable_data_130;
        myram_0_0_wenable <= _tmp_143 == 0;
      end 
      _myram_0_cond_5_1 <= 1;
      if(th_blink == 104) begin
        myram_0_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_0_cond_6_1 <= th_blink == 104;
      _myram_0_cond_7_1 <= th_blink == 104;
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
      _tmp_114 <= 0;
      _myram_1_cond_4_1 <= 0;
      _myram_1_cond_4_2 <= 0;
      _myram_1_cond_5_1 <= 0;
      _myram_1_cond_6_1 <= 0;
      _tmp_147 <= 0;
      _myram_1_cond_7_1 <= 0;
      _myram_1_cond_7_2 <= 0;
    end else begin
      if(_myram_1_cond_4_2) begin
        _tmp_114 <= 0;
      end 
      if(_myram_1_cond_7_2) begin
        _tmp_147 <= 0;
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
        _tmp_114 <= 1;
      end 
      _myram_1_cond_4_2 <= _myram_1_cond_4_1;
      if(_myram_1_cond_5_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_6_1) begin
        _tmp_147 <= 1;
      end 
      _myram_1_cond_7_2 <= _myram_1_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 1)) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_1_0_wdata <= _th_blink_wdata_10;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 1);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_1_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 1)) begin
        myram_1_0_addr <= _tmp_27;
      end 
      if((th_blink == 42) && (_th_blink_bank_8 == 1)) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_1_0_wdata <= _th_blink_wdata_10;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_1_1 <= (th_blink == 42) && (_th_blink_bank_8 == 1);
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        myram_1_0_addr <= _tmp_44;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 1)) begin
        myram_1_0_addr <= _tmp_69;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0)) begin
        myram_1_0_addr <= _tmp_107;
        myram_1_0_wdata <= __variable_data_97;
        myram_1_0_wenable <= _tmp_110 == 1;
      end 
      _myram_1_cond_2_1 <= 1;
      if(th_blink == 73) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_1_cond_3_1 <= th_blink == 73;
      _myram_1_cond_4_1 <= th_blink == 73;
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0)) begin
        myram_1_0_addr <= _tmp_140;
        myram_1_0_wdata <= __variable_data_130;
        myram_1_0_wenable <= _tmp_143 == 1;
      end 
      _myram_1_cond_5_1 <= 1;
      if(th_blink == 104) begin
        myram_1_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_1_cond_6_1 <= th_blink == 104;
      _myram_1_cond_7_1 <= th_blink == 104;
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
      _tmp_115 <= 0;
      _myram_2_cond_4_1 <= 0;
      _myram_2_cond_4_2 <= 0;
      _myram_2_cond_5_1 <= 0;
      _myram_2_cond_6_1 <= 0;
      _tmp_148 <= 0;
      _myram_2_cond_7_1 <= 0;
      _myram_2_cond_7_2 <= 0;
    end else begin
      if(_myram_2_cond_4_2) begin
        _tmp_115 <= 0;
      end 
      if(_myram_2_cond_7_2) begin
        _tmp_148 <= 0;
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
        _tmp_115 <= 1;
      end 
      _myram_2_cond_4_2 <= _myram_2_cond_4_1;
      if(_myram_2_cond_5_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_6_1) begin
        _tmp_148 <= 1;
      end 
      _myram_2_cond_7_2 <= _myram_2_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 2)) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_2_0_wdata <= _th_blink_wdata_10;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 2);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_2_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 2)) begin
        myram_2_0_addr <= _tmp_28;
      end 
      if((th_blink == 42) && (_th_blink_bank_8 == 2)) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_2_0_wdata <= _th_blink_wdata_10;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_1_1 <= (th_blink == 42) && (_th_blink_bank_8 == 2);
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        myram_2_0_addr <= _tmp_44;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 2)) begin
        myram_2_0_addr <= _tmp_70;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0)) begin
        myram_2_0_addr <= _tmp_108;
        myram_2_0_wdata <= __variable_data_97;
        myram_2_0_wenable <= _tmp_110 == 2;
      end 
      _myram_2_cond_2_1 <= 1;
      if(th_blink == 73) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_2_cond_3_1 <= th_blink == 73;
      _myram_2_cond_4_1 <= th_blink == 73;
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0)) begin
        myram_2_0_addr <= _tmp_141;
        myram_2_0_wdata <= __variable_data_130;
        myram_2_0_wenable <= _tmp_143 == 2;
      end 
      _myram_2_cond_5_1 <= 1;
      if(th_blink == 104) begin
        myram_2_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_2_cond_6_1 <= th_blink == 104;
      _myram_2_cond_7_1 <= th_blink == 104;
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
      _tmp_116 <= 0;
      _myram_3_cond_4_1 <= 0;
      _myram_3_cond_4_2 <= 0;
      _myram_3_cond_5_1 <= 0;
      _myram_3_cond_6_1 <= 0;
      _tmp_149 <= 0;
      _myram_3_cond_7_1 <= 0;
      _myram_3_cond_7_2 <= 0;
    end else begin
      if(_myram_3_cond_4_2) begin
        _tmp_116 <= 0;
      end 
      if(_myram_3_cond_7_2) begin
        _tmp_149 <= 0;
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
        _tmp_116 <= 1;
      end 
      _myram_3_cond_4_2 <= _myram_3_cond_4_1;
      if(_myram_3_cond_5_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_6_1) begin
        _tmp_149 <= 1;
      end 
      _myram_3_cond_7_2 <= _myram_3_cond_7_1;
      if((th_blink == 15) && (_th_blink_bank_8 == 3)) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_3_0_wdata <= _th_blink_wdata_10;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_0_1 <= (th_blink == 15) && (_th_blink_bank_8 == 3);
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_3_0_addr <= _tmp_2;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 3)) begin
        myram_3_0_addr <= _tmp_29;
      end 
      if((th_blink == 42) && (_th_blink_bank_8 == 3)) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
        myram_3_0_wdata <= _th_blink_wdata_10;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_1_1 <= (th_blink == 42) && (_th_blink_bank_8 == 3);
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        myram_3_0_addr <= _tmp_44;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 3)) begin
        myram_3_0_addr <= _tmp_71;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0)) begin
        myram_3_0_addr <= _tmp_109;
        myram_3_0_wdata <= __variable_data_97;
        myram_3_0_wenable <= _tmp_110 == 3;
      end 
      _myram_3_cond_2_1 <= 1;
      if(th_blink == 73) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_3_cond_3_1 <= th_blink == 73;
      _myram_3_cond_4_1 <= th_blink == 73;
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0)) begin
        myram_3_0_addr <= _tmp_142;
        myram_3_0_wdata <= __variable_data_130;
        myram_3_0_wenable <= _tmp_143 == 3;
      end 
      _myram_3_cond_5_1 <= 1;
      if(th_blink == 104) begin
        myram_3_0_addr <= _th_blink_blk_offset_5 + _th_blink_i_9;
      end 
      _myram_3_cond_6_1 <= th_blink == 104;
      _myram_3_cond_7_1 <= th_blink == 104;
    end
  end

  assign __variable_data_41 = _tmp_32;
  assign __variable_valid_41 = _tmp_8;
  assign _tmp_10 = 1 && __variable_ready_41;
  assign __variable_data_83 = _tmp_74;
  assign __variable_valid_83 = _tmp_50;
  assign _tmp_52 = 1 && __variable_ready_83;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
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
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_43 <= 0;
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_85 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _tmp_88 <= 0;
      _tmp_117 <= 0;
      _th_blink_rdata_13 <= 0;
      _th_blink_exp_14 <= 0;
      _tmp_118 <= 0;
      _tmp_119 <= 0;
      _tmp_120 <= 0;
      _tmp_121 <= 0;
      _tmp_150 <= 0;
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
          _tmp_1 <= 3;
          _tmp_2 <= _th_blink_laddr_11;
          _tmp_3 <= _th_blink_gaddr_12;
          _tmp_4 <= _th_blink_size_2;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          if(_tmp_42) begin
            th_blink <= th_blink_31;
          end 
        end
        th_blink_31: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_32;
        end
        th_blink_32: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_34;
        end
        th_blink_34: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_36;
        end
        th_blink_36: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_37;
          end else begin
            th_blink <= th_blink_54;
          end
        end
        th_blink_37: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          if(_th_blink_bank_8 < 4) begin
            th_blink <= th_blink_39;
          end else begin
            th_blink <= th_blink_52;
          end
        end
        th_blink_39: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_40;
        end
        th_blink_40: begin
          if(_th_blink_i_9 < 3) begin
            th_blink <= th_blink_41;
          end else begin
            th_blink <= th_blink_48;
          end
        end
        th_blink_41: begin
          _th_blink_wdata_10 <= _th_blink_bias_6 + _th_blink_i_9 + 1024;
          th_blink <= th_blink_42;
        end
        th_blink_42: begin
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_44;
        end
        th_blink_44: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_45;
          end else begin
            th_blink <= th_blink_47;
          end
        end
        th_blink_45: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_46;
        end
        th_blink_46: begin
          th_blink <= th_blink_48;
        end
        th_blink_47: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_40;
        end
        th_blink_48: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_49;
          end else begin
            th_blink <= th_blink_50;
          end
        end
        th_blink_49: begin
          th_blink <= th_blink_52;
        end
        th_blink_50: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_51;
        end
        th_blink_51: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_38;
        end
        th_blink_52: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
          th_blink <= th_blink_53;
        end
        th_blink_53: begin
          th_blink <= th_blink_36;
        end
        th_blink_54: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_55;
        end
        th_blink_55: begin
          _th_blink_gaddr_12 <= 1024 + _th_blink_offset_3;
          th_blink <= th_blink_56;
        end
        th_blink_56: begin
          _tmp_43 <= 3;
          _tmp_44 <= _th_blink_laddr_11;
          _tmp_45 <= _th_blink_gaddr_12;
          _tmp_46 <= _th_blink_size_2;
          th_blink <= th_blink_57;
        end
        th_blink_57: begin
          if(_tmp_84) begin
            th_blink <= th_blink_58;
          end 
        end
        th_blink_58: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_60;
        end
        th_blink_60: begin
          _th_blink_gaddr_12 <= _th_blink_offset_3;
          th_blink <= th_blink_61;
        end
        th_blink_61: begin
          _tmp_85 <= 3;
          _tmp_86 <= _th_blink_laddr_11;
          _tmp_87 <= _th_blink_gaddr_12;
          _tmp_88 <= _th_blink_size_2;
          th_blink <= th_blink_62;
        end
        th_blink_62: begin
          if(_tmp_112) begin
            th_blink <= th_blink_63;
          end 
        end
        th_blink_63: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_64;
        end
        th_blink_64: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_65;
        end
        th_blink_65: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_66;
        end
        th_blink_66: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_67;
        end
        th_blink_67: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_68;
        end
        th_blink_68: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_69;
          end else begin
            th_blink <= th_blink_90;
          end
        end
        th_blink_69: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_70;
        end
        th_blink_70: begin
          if(_th_blink_bank_8 < 4) begin
            th_blink <= th_blink_71;
          end else begin
            th_blink <= th_blink_88;
          end
        end
        th_blink_71: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_72;
        end
        th_blink_72: begin
          if(_th_blink_i_9 < 3) begin
            th_blink <= th_blink_73;
          end else begin
            th_blink <= th_blink_84;
          end
        end
        th_blink_73: begin
          if(_tmp_113 && (_th_blink_bank_8 == 0)) begin
            _tmp_117 <= myram_0_0_rdata;
          end 
          if(_tmp_114 && (_th_blink_bank_8 == 1)) begin
            _tmp_117 <= myram_1_0_rdata;
          end 
          if(_tmp_115 && (_th_blink_bank_8 == 2)) begin
            _tmp_117 <= myram_2_0_rdata;
          end 
          if(_tmp_116 && (_th_blink_bank_8 == 3)) begin
            _tmp_117 <= myram_3_0_rdata;
          end 
          if(_tmp_113) begin
            th_blink <= th_blink_74;
          end 
        end
        th_blink_74: begin
          _th_blink_rdata_13 <= _tmp_117;
          th_blink <= th_blink_75;
        end
        th_blink_75: begin
          _th_blink_exp_14 <= _th_blink_bias_6 + _th_blink_i_9 + 512;
          th_blink <= th_blink_76;
        end
        th_blink_76: begin
          if(_th_blink_rdata_13 !== _th_blink_exp_14) begin
            th_blink <= th_blink_77;
          end else begin
            th_blink <= th_blink_79;
          end
        end
        th_blink_77: begin
          $display("rdata[%d:%d] = %d:%d", _th_blink_bank_8, _th_blink_i_9, _th_blink_rdata_13, _th_blink_exp_14);
          th_blink <= th_blink_78;
        end
        th_blink_78: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_79;
        end
        th_blink_79: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_80;
        end
        th_blink_80: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_81;
          end else begin
            th_blink <= th_blink_83;
          end
        end
        th_blink_81: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_82;
        end
        th_blink_82: begin
          th_blink <= th_blink_84;
        end
        th_blink_83: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_72;
        end
        th_blink_84: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_85;
          end else begin
            th_blink <= th_blink_86;
          end
        end
        th_blink_85: begin
          th_blink <= th_blink_88;
        end
        th_blink_86: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_87;
        end
        th_blink_87: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_70;
        end
        th_blink_88: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
          th_blink <= th_blink_89;
        end
        th_blink_89: begin
          th_blink <= th_blink_68;
        end
        th_blink_90: begin
          _th_blink_laddr_11 <= 0;
          th_blink <= th_blink_91;
        end
        th_blink_91: begin
          _th_blink_gaddr_12 <= 1024 + _th_blink_offset_3;
          th_blink <= th_blink_92;
        end
        th_blink_92: begin
          _tmp_118 <= 3;
          _tmp_119 <= _th_blink_laddr_11;
          _tmp_120 <= _th_blink_gaddr_12;
          _tmp_121 <= _th_blink_size_2;
          th_blink <= th_blink_93;
        end
        th_blink_93: begin
          if(_tmp_145) begin
            th_blink <= th_blink_94;
          end 
        end
        th_blink_94: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_11, _th_blink_gaddr_12);
          th_blink <= th_blink_95;
        end
        th_blink_95: begin
          _th_blink_count_4 <= 0;
          th_blink <= th_blink_96;
        end
        th_blink_96: begin
          _th_blink_blk_offset_5 <= 0;
          th_blink <= th_blink_97;
        end
        th_blink_97: begin
          _th_blink_bias_6 <= 0;
          th_blink <= th_blink_98;
        end
        th_blink_98: begin
          _th_blink_done_7 <= 0;
          th_blink <= th_blink_99;
        end
        th_blink_99: begin
          if(_th_blink_count_4 < _th_blink_size_2) begin
            th_blink <= th_blink_100;
          end else begin
            th_blink <= th_blink_121;
          end
        end
        th_blink_100: begin
          _th_blink_bank_8 <= 0;
          th_blink <= th_blink_101;
        end
        th_blink_101: begin
          if(_th_blink_bank_8 < 4) begin
            th_blink <= th_blink_102;
          end else begin
            th_blink <= th_blink_119;
          end
        end
        th_blink_102: begin
          _th_blink_i_9 <= 0;
          th_blink <= th_blink_103;
        end
        th_blink_103: begin
          if(_th_blink_i_9 < 3) begin
            th_blink <= th_blink_104;
          end else begin
            th_blink <= th_blink_115;
          end
        end
        th_blink_104: begin
          if(_tmp_146 && (_th_blink_bank_8 == 0)) begin
            _tmp_150 <= myram_0_0_rdata;
          end 
          if(_tmp_147 && (_th_blink_bank_8 == 1)) begin
            _tmp_150 <= myram_1_0_rdata;
          end 
          if(_tmp_148 && (_th_blink_bank_8 == 2)) begin
            _tmp_150 <= myram_2_0_rdata;
          end 
          if(_tmp_149 && (_th_blink_bank_8 == 3)) begin
            _tmp_150 <= myram_3_0_rdata;
          end 
          if(_tmp_146) begin
            th_blink <= th_blink_105;
          end 
        end
        th_blink_105: begin
          _th_blink_rdata_13 <= _tmp_150;
          th_blink <= th_blink_106;
        end
        th_blink_106: begin
          _th_blink_exp_14 <= _th_blink_bias_6 + _th_blink_i_9 + 1024;
          th_blink <= th_blink_107;
        end
        th_blink_107: begin
          if(_th_blink_rdata_13 !== _th_blink_exp_14) begin
            th_blink <= th_blink_108;
          end else begin
            th_blink <= th_blink_110;
          end
        end
        th_blink_108: begin
          $display("rdata[%d:%d] = %d:%d", _th_blink_bank_8, _th_blink_i_9, _th_blink_rdata_13, _th_blink_exp_14);
          th_blink <= th_blink_109;
        end
        th_blink_109: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_110;
        end
        th_blink_110: begin
          _th_blink_count_4 <= _th_blink_count_4 + 1;
          th_blink <= th_blink_111;
        end
        th_blink_111: begin
          if((_th_blink_count_4 > _th_blink_size_2) || (_th_blink_count_4 == _th_blink_size_2)) begin
            th_blink <= th_blink_112;
          end else begin
            th_blink <= th_blink_114;
          end
        end
        th_blink_112: begin
          _th_blink_done_7 <= 1;
          th_blink <= th_blink_113;
        end
        th_blink_113: begin
          th_blink <= th_blink_115;
        end
        th_blink_114: begin
          _th_blink_i_9 <= _th_blink_i_9 + 1;
          th_blink <= th_blink_103;
        end
        th_blink_115: begin
          if(_th_blink_done_7) begin
            th_blink <= th_blink_116;
          end else begin
            th_blink <= th_blink_117;
          end
        end
        th_blink_116: begin
          th_blink <= th_blink_119;
        end
        th_blink_117: begin
          _th_blink_bias_6 <= _th_blink_bias_6 + 3;
          th_blink <= th_blink_118;
        end
        th_blink_118: begin
          _th_blink_bank_8 <= _th_blink_bank_8 + 1;
          th_blink <= th_blink_101;
        end
        th_blink_119: begin
          _th_blink_blk_offset_5 <= _th_blink_blk_offset_5 + 3;
          th_blink <= th_blink_120;
        end
        th_blink_120: begin
          th_blink <= th_blink_99;
        end
        th_blink_121: begin
          $display("# end");
          th_blink <= th_blink_122;
        end
        th_blink_122: begin
          if(_tmp_0) begin
            th_blink <= th_blink_123;
          end else begin
            th_blink <= th_blink_124;
          end
        end
        th_blink_123: begin
          $display("ALL OK");
          th_blink <= th_blink_124;
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
      _tmp_42 <= 0;
      __tmp_fsm_0_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_0_1) begin
            _tmp_42 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_blink == 30) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          _tmp_5 <= (_tmp_3 >> 2) << 2;
          _tmp_7 <= _tmp_4;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          if((_tmp_7 <= 256) && ((_tmp_5 & 4095) + (_tmp_7 << 2) >= 4096)) begin
            _tmp_6 <= 4096 - (_tmp_5 & 4095) >> 2;
            _tmp_7 <= _tmp_7 - (4096 - (_tmp_5 & 4095) >> 2);
          end else if(_tmp_7 <= 256) begin
            _tmp_6 <= _tmp_7;
            _tmp_7 <= 0;
          end else if((_tmp_5 & 4095) + 1024 >= 4096) begin
            _tmp_6 <= 4096 - (_tmp_5 & 4095) >> 2;
            _tmp_7 <= _tmp_7 - (4096 - (_tmp_5 & 4095) >> 2);
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
          if(_tmp_40 && myaxi_wvalid && myaxi_wready) begin
            _tmp_5 <= _tmp_5 + (_tmp_6 << 2);
          end 
          if(_tmp_40 && myaxi_wvalid && myaxi_wready && (_tmp_7 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(_tmp_40 && myaxi_wvalid && myaxi_wready && (_tmp_7 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_42 <= 1;
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
      _tmp_18 <= 0;
      _tmp_19 <= 0;
      _tmp_20 <= 0;
      _tmp_21 <= 0;
      __tmp_55_1 <= 0;
      __tmp_56_1 <= 0;
      __tmp_57_1 <= 0;
      __tmp_58_1 <= 0;
      __tmp_59_1 <= 0;
      __tmp_73_1 <= 0;
      _tmp_73 <= 0;
      _tmp_78 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_75 <= 0;
      _tmp_72 <= 0;
      _tmp_79 <= 0;
      _tmp_80 <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_63 <= 0;
      _tmp_110 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_98 <= 0;
      _tmp_99 <= 0;
      _tmp_100 <= 0;
      _tmp_101 <= 0;
      _tmp_96 <= 0;
      _myram_cond_0_1 <= 0;
      _tmp_143 <= 0;
      _tmp_127 <= 0;
      _tmp_128 <= 0;
      _tmp_131 <= 0;
      _tmp_132 <= 0;
      _tmp_133 <= 0;
      _tmp_134 <= 0;
      _tmp_129 <= 0;
      _myram_cond_1_1 <= 0;
    end else begin
      if(_myram_cond_0_1) begin
        _tmp_96 <= 0;
      end 
      if(_myram_cond_1_1) begin
        _tmp_129 <= 0;
      end 
      __tmp_13_1 <= _tmp_13;
      __tmp_14_1 <= _tmp_14;
      __tmp_15_1 <= _tmp_15;
      __tmp_16_1 <= _tmp_16;
      __tmp_17_1 <= _tmp_17;
      __tmp_31_1 <= _tmp_31;
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9)) begin
        _tmp_31 <= _tmp_30;
      end 
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
        _tmp_31 <= 0;
        _tmp_37 <= _tmp_1 - 1;
        _tmp_38 <= _tmp_4 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= _tmp_4 == 1;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        _tmp_18 <= _tmp_2;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        _tmp_19 <= _tmp_2;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        _tmp_20 <= _tmp_2;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_38 == 0) && !_tmp_35 && !_tmp_36) begin
        _tmp_21 <= _tmp_2;
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
        _tmp_18 <= _tmp_22;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 1)) begin
        _tmp_19 <= _tmp_23;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 2)) begin
        _tmp_20 <= _tmp_24;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 > 0) && (_tmp_30 == 3)) begin
        _tmp_21 <= _tmp_25;
      end 
      if((_tmp_10 || !_tmp_8) && (_tmp_11 || !_tmp_9) && (_tmp_38 == 1)) begin
        _tmp_35 <= 1;
      end 
      __tmp_55_1 <= _tmp_55;
      __tmp_56_1 <= _tmp_56;
      __tmp_57_1 <= _tmp_57;
      __tmp_58_1 <= _tmp_58;
      __tmp_59_1 <= _tmp_59;
      __tmp_73_1 <= _tmp_73;
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51)) begin
        _tmp_73 <= _tmp_72;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && _tmp_76) begin
        _tmp_78 <= 0;
        _tmp_50 <= 0;
        _tmp_51 <= 0;
        _tmp_76 <= 0;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && _tmp_75) begin
        _tmp_50 <= 1;
        _tmp_51 <= 1;
        _tmp_78 <= _tmp_77;
        _tmp_77 <= 0;
        _tmp_75 <= 0;
        _tmp_76 <= 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        _tmp_72 <= 0;
        _tmp_73 <= 0;
        _tmp_79 <= _tmp_43 - 1;
        _tmp_80 <= _tmp_46 - 1;
        _tmp_75 <= 1;
        _tmp_77 <= _tmp_46 == 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        _tmp_60 <= _tmp_44;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        _tmp_61 <= _tmp_44;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        _tmp_62 <= _tmp_44;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_80 == 0) && !_tmp_77 && !_tmp_78) begin
        _tmp_63 <= _tmp_44;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0)) begin
        _tmp_79 <= _tmp_79 - 1;
        _tmp_80 <= _tmp_80 - 1;
        _tmp_75 <= 1;
        _tmp_77 <= 0;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_79 == 0)) begin
        _tmp_79 <= _tmp_43 - 1;
        _tmp_72 <= _tmp_72 + 1;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_79 == 0) && (_tmp_72 == 3)) begin
        _tmp_72 <= 0;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 0)) begin
        _tmp_60 <= _tmp_64;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 1)) begin
        _tmp_61 <= _tmp_65;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 2)) begin
        _tmp_62 <= _tmp_66;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 > 0) && (_tmp_72 == 3)) begin
        _tmp_63 <= _tmp_67;
      end 
      if((_tmp_52 || !_tmp_50) && (_tmp_53 || !_tmp_51) && (_tmp_80 == 1)) begin
        _tmp_77 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_95 == 0)) begin
        _tmp_110 <= 0;
        _tmp_94 <= _tmp_85 - 1;
        _tmp_95 <= _tmp_88;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_95 == 0)) begin
        _tmp_98 <= _tmp_86 - 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_95 == 0)) begin
        _tmp_99 <= _tmp_86 - 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_95 == 0)) begin
        _tmp_100 <= _tmp_86 - 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_95 == 0)) begin
        _tmp_101 <= _tmp_86 - 1;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0)) begin
        _tmp_94 <= _tmp_94 - 1;
        _tmp_95 <= _tmp_95 - 1;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0) && (_tmp_94 == 0)) begin
        _tmp_94 <= _tmp_85 - 1;
        _tmp_110 <= _tmp_110 + 1;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0) && (_tmp_94 == 0) && (_tmp_110 == 3)) begin
        _tmp_110 <= 0;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0) && (_tmp_110 == 0)) begin
        _tmp_98 <= _tmp_102;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0) && (_tmp_110 == 1)) begin
        _tmp_99 <= _tmp_103;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0) && (_tmp_110 == 2)) begin
        _tmp_100 <= _tmp_104;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0) && (_tmp_110 == 3)) begin
        _tmp_101 <= _tmp_105;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 == 1)) begin
        _tmp_96 <= 1;
      end 
      _myram_cond_0_1 <= 1;
      if((_tmp_fsm_3 == 1) && (_tmp_128 == 0)) begin
        _tmp_143 <= 0;
        _tmp_127 <= _tmp_118 - 1;
        _tmp_128 <= _tmp_121;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_128 == 0)) begin
        _tmp_131 <= _tmp_119 - 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_128 == 0)) begin
        _tmp_132 <= _tmp_119 - 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_128 == 0)) begin
        _tmp_133 <= _tmp_119 - 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_128 == 0)) begin
        _tmp_134 <= _tmp_119 - 1;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0)) begin
        _tmp_127 <= _tmp_127 - 1;
        _tmp_128 <= _tmp_128 - 1;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0) && (_tmp_127 == 0)) begin
        _tmp_127 <= _tmp_118 - 1;
        _tmp_143 <= _tmp_143 + 1;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0) && (_tmp_127 == 0) && (_tmp_143 == 3)) begin
        _tmp_143 <= 0;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0) && (_tmp_143 == 0)) begin
        _tmp_131 <= _tmp_135;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0) && (_tmp_143 == 1)) begin
        _tmp_132 <= _tmp_136;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0) && (_tmp_143 == 2)) begin
        _tmp_133 <= _tmp_137;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 > 0) && (_tmp_143 == 3)) begin
        _tmp_134 <= _tmp_138;
      end 
      if(__variable_valid_130 && ((_tmp_128 > 0) && !_tmp_129) && (_tmp_128 == 1)) begin
        _tmp_129 <= 1;
      end 
      _myram_cond_1_1 <= 1;
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
      _tmp_47 <= 0;
      _tmp_49 <= 0;
      _tmp_48 <= 0;
      _tmp_84 <= 0;
      __tmp_fsm_1_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_0_1) begin
            _tmp_84 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_blink == 57) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_47 <= (_tmp_45 >> 2) << 2;
          _tmp_49 <= _tmp_46;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_49 <= 256) && ((_tmp_47 & 4095) + (_tmp_49 << 2) >= 4096)) begin
            _tmp_48 <= 4096 - (_tmp_47 & 4095) >> 2;
            _tmp_49 <= _tmp_49 - (4096 - (_tmp_47 & 4095) >> 2);
          end else if(_tmp_49 <= 256) begin
            _tmp_48 <= _tmp_49;
            _tmp_49 <= 0;
          end else if((_tmp_47 & 4095) + 1024 >= 4096) begin
            _tmp_48 <= 4096 - (_tmp_47 & 4095) >> 2;
            _tmp_49 <= _tmp_49 - (4096 - (_tmp_47 & 4095) >> 2);
          end else begin
            _tmp_48 <= 256;
            _tmp_49 <= _tmp_49 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          if(_tmp_82 && myaxi_wvalid && myaxi_wready) begin
            _tmp_47 <= _tmp_47 + (_tmp_48 << 2);
          end 
          if(_tmp_82 && myaxi_wvalid && myaxi_wready && (_tmp_49 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(_tmp_82 && myaxi_wvalid && myaxi_wready && (_tmp_49 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_84 <= 1;
          __tmp_fsm_1_cond_5_0_1 <= 1;
          _tmp_fsm_1 <= _tmp_fsm_1_6;
        end
        _tmp_fsm_1_6: begin
          _tmp_fsm_1 <= _tmp_fsm_1_init;
        end
      endcase
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
      _tmp_89 <= 0;
      _tmp_91 <= 0;
      _tmp_90 <= 0;
      __tmp_fsm_2_cond_4_0_1 <= 0;
      _tmp_93 <= 0;
      _tmp_92 <= 0;
      _tmp_112 <= 0;
      __tmp_fsm_2_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_0_1) begin
            _tmp_93 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_1_1) begin
            _tmp_112 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_blink == 62) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_89 <= (_tmp_87 >> 2) << 2;
          _tmp_91 <= _tmp_88;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_91 <= 256) && ((_tmp_89 & 4095) + (_tmp_91 << 2) >= 4096)) begin
            _tmp_90 <= 4096 - (_tmp_89 & 4095) >> 2;
            _tmp_91 <= _tmp_91 - (4096 - (_tmp_89 & 4095) >> 2);
          end else if(_tmp_91 <= 256) begin
            _tmp_90 <= _tmp_91;
            _tmp_91 <= 0;
          end else if((_tmp_89 & 4095) + 1024 >= 4096) begin
            _tmp_90 <= 4096 - (_tmp_89 & 4095) >> 2;
            _tmp_91 <= _tmp_91 - (4096 - (_tmp_89 & 4095) >> 2);
          end else begin
            _tmp_90 <= 256;
            _tmp_91 <= _tmp_91 - 256;
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
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_92 <= myaxi_rdata;
            _tmp_93 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_89 <= _tmp_89 + (_tmp_90 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_91 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_91 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_112 <= 1;
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
      _tmp_122 <= 0;
      _tmp_124 <= 0;
      _tmp_123 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_126 <= 0;
      _tmp_125 <= 0;
      _tmp_145 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_126 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_145 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_blink == 93) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_122 <= (_tmp_120 >> 2) << 2;
          _tmp_124 <= _tmp_121;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_124 <= 256) && ((_tmp_122 & 4095) + (_tmp_124 << 2) >= 4096)) begin
            _tmp_123 <= 4096 - (_tmp_122 & 4095) >> 2;
            _tmp_124 <= _tmp_124 - (4096 - (_tmp_122 & 4095) >> 2);
          end else if(_tmp_124 <= 256) begin
            _tmp_123 <= _tmp_124;
            _tmp_124 <= 0;
          end else if((_tmp_122 & 4095) + 1024 >= 4096) begin
            _tmp_123 <= 4096 - (_tmp_122 & 4095) >> 2;
            _tmp_124 <= _tmp_124 - (4096 - (_tmp_122 & 4095) >> 2);
          end else begin
            _tmp_123 <= 256;
            _tmp_124 <= _tmp_124 - 256;
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
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_125 <= myaxi_rdata;
            _tmp_126 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_122 <= _tmp_122 + (_tmp_123 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_124 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_124 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_145 <= 1;
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
