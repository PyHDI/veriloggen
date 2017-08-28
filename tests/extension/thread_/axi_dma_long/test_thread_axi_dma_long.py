from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_axi_dma_long

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
    #1000000;
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

  reg _tmp_0;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_offset_1;
  reg signed [32-1:0] _th_blink_size_2;
  reg signed [32-1:0] _th_blink_offset_3;
  reg signed [32-1:0] _th_blink_i_4;
  reg signed [32-1:0] _th_blink_wdata_5;
  reg _myram_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_6;
  reg signed [32-1:0] _th_blink_gaddr_7;
  reg [10-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _tmp_4;
  reg [33-1:0] _tmp_5;
  reg [33-1:0] _tmp_6;
  reg _tmp_7;
  reg _tmp_8;
  wire _tmp_9;
  wire _tmp_10;
  assign _tmp_10 = 1;
  localparam _tmp_11 = 1;
  wire [_tmp_11-1:0] _tmp_12;
  assign _tmp_12 = (_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8);
  reg [_tmp_11-1:0] __tmp_12_1;
  wire [32-1:0] _tmp_13;
  reg [32-1:0] __tmp_13_1;
  assign _tmp_13 = (__tmp_12_1)? myram_0_rdata : __tmp_13_1;
  reg _tmp_14;
  reg _tmp_15;
  reg _tmp_16;
  reg _tmp_17;
  reg [33-1:0] _tmp_18;
  reg [9-1:0] _tmp_19;
  reg _myaxi_cond_0_1;
  reg _tmp_20;
  wire [32-1:0] _tmp_data_21;
  wire _tmp_valid_21;
  wire _tmp_ready_21;
  assign _tmp_ready_21 = (_tmp_fsm_0 == 4) && ((_tmp_19 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  reg _tmp_22;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_5_0_1;
  reg _myram_cond_1_1;
  reg [10-1:0] _tmp_23;
  reg [32-1:0] _tmp_24;
  reg [32-1:0] _tmp_25;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_26;
  reg [33-1:0] _tmp_27;
  reg [33-1:0] _tmp_28;
  reg _tmp_29;
  reg _tmp_30;
  wire _tmp_31;
  wire _tmp_32;
  assign _tmp_32 = 1;
  localparam _tmp_33 = 1;
  wire [_tmp_33-1:0] _tmp_34;
  assign _tmp_34 = (_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30);
  reg [_tmp_33-1:0] __tmp_34_1;
  wire [32-1:0] _tmp_35;
  reg [32-1:0] __tmp_35_1;
  assign _tmp_35 = (__tmp_34_1)? myram_0_rdata : __tmp_35_1;
  reg _tmp_36;
  reg _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  reg [33-1:0] _tmp_40;
  reg [9-1:0] _tmp_41;
  reg _myaxi_cond_2_1;
  reg _tmp_42;
  wire [32-1:0] _tmp_data_43;
  wire _tmp_valid_43;
  wire _tmp_ready_43;
  assign _tmp_ready_43 = (_tmp_fsm_1 == 4) && ((_tmp_41 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_44;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_5_0_1;
  reg [10-1:0] _tmp_45;
  reg [32-1:0] _tmp_46;
  reg [32-1:0] _tmp_47;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_48;
  reg [33-1:0] _tmp_49;
  reg [33-1:0] _tmp_50;
  reg [32-1:0] _tmp_51;
  reg _tmp_52;
  reg [33-1:0] _tmp_53;
  reg _tmp_54;
  wire [32-1:0] _tmp_data_55;
  wire _tmp_valid_55;
  wire _tmp_ready_55;
  assign _tmp_ready_55 = (_tmp_53 > 0) && !_tmp_54;
  reg _myram_cond_2_1;
  reg [9-1:0] _tmp_56;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_4_0_1;
  reg _tmp_57;
  reg __tmp_fsm_2_cond_5_1_1;
  reg _tmp_58;
  reg _myram_cond_3_1;
  reg _myram_cond_4_1;
  reg _myram_cond_4_2;
  reg signed [32-1:0] _tmp_59;
  reg signed [32-1:0] _th_blink_rdata_8;
  reg [10-1:0] _tmp_60;
  reg [32-1:0] _tmp_61;
  reg [32-1:0] _tmp_62;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_63;
  reg [33-1:0] _tmp_64;
  reg [33-1:0] _tmp_65;
  reg [32-1:0] _tmp_66;
  reg _tmp_67;
  reg [33-1:0] _tmp_68;
  reg _tmp_69;
  wire [32-1:0] _tmp_data_70;
  wire _tmp_valid_70;
  wire _tmp_ready_70;
  assign _tmp_ready_70 = (_tmp_68 > 0) && !_tmp_69;
  reg _myram_cond_5_1;
  reg [9-1:0] _tmp_71;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_2 == 4) || (_tmp_fsm_3 == 4);
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_72;
  reg __tmp_fsm_3_cond_5_1_1;
  reg _tmp_73;
  reg _myram_cond_6_1;
  reg _myram_cond_7_1;
  reg _myram_cond_7_2;
  reg signed [32-1:0] _tmp_74;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_19 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_20 <= 0;
      _myaxi_cond_1_1 <= 0;
      _tmp_41 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_42 <= 0;
      _myaxi_cond_3_1 <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_56 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_71 <= 0;
      _myaxi_cond_5_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_20 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_42 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_5_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_19 == 0))) begin
        myaxi_awaddr <= _tmp_4;
        myaxi_awlen <= _tmp_5 - 1;
        myaxi_awvalid <= 1;
        _tmp_19 <= _tmp_5;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_19 == 0)) && (_tmp_5 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_21 && ((_tmp_fsm_0 == 4) && ((_tmp_19 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_19 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_19 > 0))) begin
        myaxi_wdata <= _tmp_data_21;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_19 <= _tmp_19 - 1;
      end 
      if(_tmp_valid_21 && ((_tmp_fsm_0 == 4) && ((_tmp_19 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_19 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_19 > 0)) && (_tmp_19 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_20 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_20 <= _tmp_20;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_41 == 0))) begin
        myaxi_awaddr <= _tmp_26;
        myaxi_awlen <= _tmp_27 - 1;
        myaxi_awvalid <= 1;
        _tmp_41 <= _tmp_27;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_41 == 0)) && (_tmp_27 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_43 && ((_tmp_fsm_1 == 4) && ((_tmp_41 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_41 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_41 > 0))) begin
        myaxi_wdata <= _tmp_data_43;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_41 <= _tmp_41 - 1;
      end 
      if(_tmp_valid_43 && ((_tmp_fsm_1 == 4) && ((_tmp_41 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_41 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_41 > 0)) && (_tmp_41 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_42 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_42 <= _tmp_42;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_56 == 0))) begin
        myaxi_araddr <= _tmp_48;
        myaxi_arlen <= _tmp_49 - 1;
        myaxi_arvalid <= 1;
        _tmp_56 <= _tmp_49;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_56 > 0)) begin
        _tmp_56 <= _tmp_56 - 1;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_71 == 0))) begin
        myaxi_araddr <= _tmp_63;
        myaxi_arlen <= _tmp_64 - 1;
        myaxi_arvalid <= 1;
        _tmp_71 <= _tmp_64;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_71 > 0)) begin
        _tmp_71 <= _tmp_71 - 1;
      end 
    end
  end

  assign _tmp_data_55 = _tmp_51;
  assign _tmp_valid_55 = _tmp_52;
  assign _tmp_data_70 = _tmp_66;
  assign _tmp_valid_70 = _tmp_67;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
      __tmp_12_1 <= 0;
      __tmp_13_1 <= 0;
      _tmp_17 <= 0;
      _tmp_7 <= 0;
      _tmp_8 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_14 <= 0;
      _tmp_18 <= 0;
      _myram_cond_1_1 <= 0;
      __tmp_34_1 <= 0;
      __tmp_35_1 <= 0;
      _tmp_39 <= 0;
      _tmp_29 <= 0;
      _tmp_30 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _tmp_36 <= 0;
      _tmp_40 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _myram_cond_2_1 <= 0;
      _myram_cond_3_1 <= 0;
      _tmp_58 <= 0;
      _myram_cond_4_1 <= 0;
      _myram_cond_4_2 <= 0;
      _tmp_68 <= 0;
      _tmp_69 <= 0;
      _myram_cond_5_1 <= 0;
      _myram_cond_6_1 <= 0;
      _tmp_73 <= 0;
      _myram_cond_7_1 <= 0;
      _myram_cond_7_2 <= 0;
    end else begin
      if(_myram_cond_4_2) begin
        _tmp_58 <= 0;
      end 
      if(_myram_cond_7_2) begin
        _tmp_73 <= 0;
      end 
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_1_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_2_1) begin
        myram_0_wenable <= 0;
        _tmp_54 <= 0;
      end 
      if(_myram_cond_3_1) begin
        _tmp_58 <= 1;
      end 
      _myram_cond_4_2 <= _myram_cond_4_1;
      if(_myram_cond_5_1) begin
        myram_0_wenable <= 0;
        _tmp_69 <= 0;
      end 
      if(_myram_cond_6_1) begin
        _tmp_73 <= 1;
      end 
      _myram_cond_7_2 <= _myram_cond_7_1;
      if(th_blink == 7) begin
        myram_0_addr <= _th_blink_i_4;
        myram_0_wdata <= _th_blink_wdata_5;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= th_blink == 7;
      __tmp_12_1 <= _tmp_12;
      __tmp_13_1 <= _tmp_13;
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && _tmp_15) begin
        _tmp_17 <= 0;
        _tmp_7 <= 0;
        _tmp_8 <= 0;
        _tmp_15 <= 0;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && _tmp_14) begin
        _tmp_7 <= 1;
        _tmp_8 <= 1;
        _tmp_17 <= _tmp_16;
        _tmp_16 <= 0;
        _tmp_14 <= 0;
        _tmp_15 <= 1;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_18 == 0) && !_tmp_16 && !_tmp_17) begin
        myram_0_addr <= _tmp_1;
        _tmp_18 <= _tmp_3 - 1;
        _tmp_14 <= 1;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && (_tmp_18 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        _tmp_18 <= _tmp_18 - 1;
        _tmp_14 <= 1;
        _tmp_16 <= 0;
      end 
      if((_tmp_9 || !_tmp_7) && (_tmp_10 || !_tmp_8) && (_tmp_18 == 1)) begin
        _tmp_16 <= 1;
      end 
      if(th_blink == 17) begin
        myram_0_addr <= _th_blink_i_4;
        myram_0_wdata <= _th_blink_wdata_5;
        myram_0_wenable <= 1;
      end 
      _myram_cond_1_1 <= th_blink == 17;
      __tmp_34_1 <= _tmp_34;
      __tmp_35_1 <= _tmp_35;
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && _tmp_37) begin
        _tmp_39 <= 0;
        _tmp_29 <= 0;
        _tmp_30 <= 0;
        _tmp_37 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && _tmp_36) begin
        _tmp_29 <= 1;
        _tmp_30 <= 1;
        _tmp_39 <= _tmp_38;
        _tmp_38 <= 0;
        _tmp_36 <= 0;
        _tmp_37 <= 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_40 == 0) && !_tmp_38 && !_tmp_39) begin
        myram_0_addr <= _tmp_23;
        _tmp_40 <= _tmp_25 - 1;
        _tmp_36 <= 1;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_40 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        _tmp_40 <= _tmp_40 - 1;
        _tmp_36 <= 1;
        _tmp_38 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_40 == 1)) begin
        _tmp_38 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_53 == 0)) begin
        myram_0_addr <= _tmp_45 - 1;
        _tmp_53 <= _tmp_47;
      end 
      if(_tmp_valid_55 && ((_tmp_53 > 0) && !_tmp_54) && (_tmp_53 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _tmp_data_55;
        myram_0_wenable <= 1;
        _tmp_53 <= _tmp_53 - 1;
      end 
      if(_tmp_valid_55 && ((_tmp_53 > 0) && !_tmp_54) && (_tmp_53 == 1)) begin
        _tmp_54 <= 1;
      end 
      _myram_cond_2_1 <= 1;
      if(th_blink == 31) begin
        myram_0_addr <= _th_blink_i_4;
      end 
      _myram_cond_3_1 <= th_blink == 31;
      _myram_cond_4_1 <= th_blink == 31;
      if((_tmp_fsm_3 == 1) && (_tmp_68 == 0)) begin
        myram_0_addr <= _tmp_60 - 1;
        _tmp_68 <= _tmp_62;
      end 
      if(_tmp_valid_70 && ((_tmp_68 > 0) && !_tmp_69) && (_tmp_68 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _tmp_data_70;
        myram_0_wenable <= 1;
        _tmp_68 <= _tmp_68 - 1;
      end 
      if(_tmp_valid_70 && ((_tmp_68 > 0) && !_tmp_69) && (_tmp_68 == 1)) begin
        _tmp_69 <= 1;
      end 
      _myram_cond_5_1 <= 1;
      if(th_blink == 44) begin
        myram_0_addr <= _th_blink_i_4;
      end 
      _myram_cond_6_1 <= th_blink == 44;
      _myram_cond_7_1 <= th_blink == 44;
    end
  end

  assign _tmp_data_21 = _tmp_13;
  assign _tmp_valid_21 = _tmp_7;
  assign _tmp_9 = 1 && _tmp_ready_21;
  assign _tmp_data_43 = _tmp_35;
  assign _tmp_valid_43 = _tmp_29;
  assign _tmp_31 = 1 && _tmp_ready_43;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_offset_1 <= 0;
      _th_blink_size_2 <= 0;
      _th_blink_offset_3 <= 0;
      _th_blink_i_4 <= 0;
      _th_blink_wdata_5 <= 0;
      _th_blink_laddr_6 <= 0;
      _th_blink_gaddr_7 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_23 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_59 <= 0;
      _th_blink_rdata_8 <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_74 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 576;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _tmp_0 <= 1;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_offset_1 <= 4092;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _th_blink_size_2 <= _th_blink_size_0;
          _th_blink_offset_3 <= _th_blink_offset_1;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _th_blink_i_4 <= 0;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          if(_th_blink_i_4 < _th_blink_size_2) begin
            th_blink <= th_blink_6;
          end else begin
            th_blink <= th_blink_9;
          end
        end
        th_blink_6: begin
          _th_blink_wdata_5 <= _th_blink_i_4 + 100;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_i_4 <= _th_blink_i_4 + 1;
          th_blink <= th_blink_5;
        end
        th_blink_9: begin
          _th_blink_laddr_6 <= 0;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          _th_blink_gaddr_7 <= _th_blink_offset_3;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _tmp_1 <= _th_blink_laddr_6;
          _tmp_2 <= _th_blink_gaddr_7;
          _tmp_3 <= _th_blink_size_2;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          if(_tmp_22) begin
            th_blink <= th_blink_13;
          end 
        end
        th_blink_13: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_6, _th_blink_gaddr_7);
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          _th_blink_i_4 <= 0;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          if(_th_blink_i_4 < _th_blink_size_2) begin
            th_blink <= th_blink_16;
          end else begin
            th_blink <= th_blink_19;
          end
        end
        th_blink_16: begin
          _th_blink_wdata_5 <= _th_blink_i_4 + 1000;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          _th_blink_i_4 <= _th_blink_i_4 + 1;
          th_blink <= th_blink_15;
        end
        th_blink_19: begin
          _th_blink_laddr_6 <= 0;
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          _th_blink_gaddr_7 <= _th_blink_offset_3 + 4096;
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          _tmp_23 <= _th_blink_laddr_6;
          _tmp_24 <= _th_blink_gaddr_7;
          _tmp_25 <= _th_blink_size_2;
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          if(_tmp_44) begin
            th_blink <= th_blink_23;
          end 
        end
        th_blink_23: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_6, _th_blink_gaddr_7);
          th_blink <= th_blink_24;
        end
        th_blink_24: begin
          _th_blink_laddr_6 <= 0;
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          _th_blink_gaddr_7 <= _th_blink_offset_3;
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          _tmp_45 <= _th_blink_laddr_6;
          _tmp_46 <= _th_blink_gaddr_7;
          _tmp_47 <= _th_blink_size_2;
          th_blink <= th_blink_27;
        end
        th_blink_27: begin
          if(_tmp_57) begin
            th_blink <= th_blink_28;
          end 
        end
        th_blink_28: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_6, _th_blink_gaddr_7);
          th_blink <= th_blink_29;
        end
        th_blink_29: begin
          _th_blink_i_4 <= 0;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          if(_th_blink_i_4 < _th_blink_size_2) begin
            th_blink <= th_blink_31;
          end else begin
            th_blink <= th_blink_37;
          end
        end
        th_blink_31: begin
          if(_tmp_58) begin
            _tmp_59 <= myram_0_rdata;
          end 
          if(_tmp_58) begin
            th_blink <= th_blink_32;
          end 
        end
        th_blink_32: begin
          _th_blink_rdata_8 <= _tmp_59;
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          if(_th_blink_rdata_8 !== _th_blink_i_4 + 100) begin
            th_blink <= th_blink_34;
          end else begin
            th_blink <= th_blink_36;
          end
        end
        th_blink_34: begin
          $display("rdata[%d] = %d", _th_blink_i_4, _th_blink_rdata_8);
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_36;
        end
        th_blink_36: begin
          _th_blink_i_4 <= _th_blink_i_4 + 1;
          th_blink <= th_blink_30;
        end
        th_blink_37: begin
          _th_blink_laddr_6 <= 0;
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          _th_blink_gaddr_7 <= _th_blink_offset_3 + 4096;
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          _tmp_60 <= _th_blink_laddr_6;
          _tmp_61 <= _th_blink_gaddr_7;
          _tmp_62 <= _th_blink_size_2;
          th_blink <= th_blink_40;
        end
        th_blink_40: begin
          if(_tmp_72) begin
            th_blink <= th_blink_41;
          end 
        end
        th_blink_41: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_6, _th_blink_gaddr_7);
          th_blink <= th_blink_42;
        end
        th_blink_42: begin
          _th_blink_i_4 <= 0;
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          if(_th_blink_i_4 < _th_blink_size_2) begin
            th_blink <= th_blink_44;
          end else begin
            th_blink <= th_blink_50;
          end
        end
        th_blink_44: begin
          if(_tmp_73) begin
            _tmp_74 <= myram_0_rdata;
          end 
          if(_tmp_73) begin
            th_blink <= th_blink_45;
          end 
        end
        th_blink_45: begin
          _th_blink_rdata_8 <= _tmp_74;
          th_blink <= th_blink_46;
        end
        th_blink_46: begin
          if(_th_blink_rdata_8 !== _th_blink_i_4 + 1000) begin
            th_blink <= th_blink_47;
          end else begin
            th_blink <= th_blink_49;
          end
        end
        th_blink_47: begin
          $display("rdata[%d] = %d", _th_blink_i_4, _th_blink_rdata_8);
          th_blink <= th_blink_48;
        end
        th_blink_48: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_49;
        end
        th_blink_49: begin
          _th_blink_i_4 <= _th_blink_i_4 + 1;
          th_blink <= th_blink_43;
        end
        th_blink_50: begin
          if(_tmp_0) begin
            th_blink <= th_blink_51;
          end else begin
            th_blink <= th_blink_52;
          end
        end
        th_blink_51: begin
          $display("ALL OK");
          th_blink <= th_blink_52;
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
      _tmp_4 <= 0;
      _tmp_6 <= 0;
      _tmp_5 <= 0;
      _tmp_22 <= 0;
      __tmp_fsm_0_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_0_1) begin
            _tmp_22 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_blink == 12) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          _tmp_4 <= (_tmp_2 >> 2) << 2;
          _tmp_6 <= _tmp_3;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          if((_tmp_6 <= 256) && ((_tmp_4 & 4095) + (_tmp_6 << 2) >= 4096)) begin
            _tmp_5 <= 4096 - (_tmp_4 & 4095) >> 2;
            _tmp_6 <= _tmp_6 - (4096 - (_tmp_4 & 4095) >> 2);
          end else if(_tmp_6 <= 256) begin
            _tmp_5 <= _tmp_6;
            _tmp_6 <= 0;
          end else if((_tmp_4 & 4095) + 1024 >= 4096) begin
            _tmp_5 <= 4096 - (_tmp_4 & 4095) >> 2;
            _tmp_6 <= _tmp_6 - (4096 - (_tmp_4 & 4095) >> 2);
          end else begin
            _tmp_5 <= 256;
            _tmp_6 <= _tmp_6 - 256;
          end
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_4;
          end 
        end
        _tmp_fsm_0_4: begin
          if(_tmp_20 && myaxi_wvalid && myaxi_wready) begin
            _tmp_4 <= _tmp_4 + (_tmp_5 << 2);
          end 
          if(_tmp_20 && myaxi_wvalid && myaxi_wready && (_tmp_6 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(_tmp_20 && myaxi_wvalid && myaxi_wready && (_tmp_6 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_22 <= 1;
          __tmp_fsm_0_cond_5_0_1 <= 1;
          _tmp_fsm_0 <= _tmp_fsm_0_6;
        end
        _tmp_fsm_0_6: begin
          _tmp_fsm_0 <= _tmp_fsm_0_init;
        end
      endcase
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
      _tmp_26 <= 0;
      _tmp_28 <= 0;
      _tmp_27 <= 0;
      _tmp_44 <= 0;
      __tmp_fsm_1_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_0_1) begin
            _tmp_44 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_blink == 22) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_26 <= (_tmp_24 >> 2) << 2;
          _tmp_28 <= _tmp_25;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_28 <= 256) && ((_tmp_26 & 4095) + (_tmp_28 << 2) >= 4096)) begin
            _tmp_27 <= 4096 - (_tmp_26 & 4095) >> 2;
            _tmp_28 <= _tmp_28 - (4096 - (_tmp_26 & 4095) >> 2);
          end else if(_tmp_28 <= 256) begin
            _tmp_27 <= _tmp_28;
            _tmp_28 <= 0;
          end else if((_tmp_26 & 4095) + 1024 >= 4096) begin
            _tmp_27 <= 4096 - (_tmp_26 & 4095) >> 2;
            _tmp_28 <= _tmp_28 - (4096 - (_tmp_26 & 4095) >> 2);
          end else begin
            _tmp_27 <= 256;
            _tmp_28 <= _tmp_28 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          if(_tmp_42 && myaxi_wvalid && myaxi_wready) begin
            _tmp_26 <= _tmp_26 + (_tmp_27 << 2);
          end 
          if(_tmp_42 && myaxi_wvalid && myaxi_wready && (_tmp_28 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(_tmp_42 && myaxi_wvalid && myaxi_wready && (_tmp_28 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_44 <= 1;
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
      _tmp_48 <= 0;
      _tmp_50 <= 0;
      _tmp_49 <= 0;
      __tmp_fsm_2_cond_4_0_1 <= 0;
      _tmp_52 <= 0;
      _tmp_51 <= 0;
      _tmp_57 <= 0;
      __tmp_fsm_2_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_0_1) begin
            _tmp_52 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_1_1) begin
            _tmp_57 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_blink == 27) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_48 <= (_tmp_46 >> 2) << 2;
          _tmp_50 <= _tmp_47;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_50 <= 256) && ((_tmp_48 & 4095) + (_tmp_50 << 2) >= 4096)) begin
            _tmp_49 <= 4096 - (_tmp_48 & 4095) >> 2;
            _tmp_50 <= _tmp_50 - (4096 - (_tmp_48 & 4095) >> 2);
          end else if(_tmp_50 <= 256) begin
            _tmp_49 <= _tmp_50;
            _tmp_50 <= 0;
          end else if((_tmp_48 & 4095) + 1024 >= 4096) begin
            _tmp_49 <= 4096 - (_tmp_48 & 4095) >> 2;
            _tmp_50 <= _tmp_50 - (4096 - (_tmp_48 & 4095) >> 2);
          end else begin
            _tmp_49 <= 256;
            _tmp_50 <= _tmp_50 - 256;
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
            _tmp_51 <= myaxi_rdata;
            _tmp_52 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_48 <= _tmp_48 + (_tmp_49 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_50 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_50 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_57 <= 1;
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
      _tmp_63 <= 0;
      _tmp_65 <= 0;
      _tmp_64 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_67 <= 0;
      _tmp_66 <= 0;
      _tmp_72 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_67 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_72 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_blink == 40) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_63 <= (_tmp_61 >> 2) << 2;
          _tmp_65 <= _tmp_62;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_65 <= 256) && ((_tmp_63 & 4095) + (_tmp_65 << 2) >= 4096)) begin
            _tmp_64 <= 4096 - (_tmp_63 & 4095) >> 2;
            _tmp_65 <= _tmp_65 - (4096 - (_tmp_63 & 4095) >> 2);
          end else if(_tmp_65 <= 256) begin
            _tmp_64 <= _tmp_65;
            _tmp_65 <= 0;
          end else if((_tmp_63 & 4095) + 1024 >= 4096) begin
            _tmp_64 <= 4096 - (_tmp_63 & 4095) >> 2;
            _tmp_65 <= _tmp_65 - (4096 - (_tmp_63 & 4095) >> 2);
          end else begin
            _tmp_64 <= 256;
            _tmp_65 <= _tmp_65 - 256;
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
            _tmp_66 <= myaxi_rdata;
            _tmp_67 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_63 <= _tmp_63 + (_tmp_64 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_65 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_65 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_72 <= 1;
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
    test_module = thread_axi_dma_long.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
