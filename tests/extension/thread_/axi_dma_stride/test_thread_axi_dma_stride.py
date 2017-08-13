from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_axi_dma_stride

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
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_offset_2;
  reg signed [32-1:0] _th_blink_size_3;
  reg signed [32-1:0] _th_blink_offset_4;
  reg signed [32-1:0] _th_blink_i_5;
  reg signed [32-1:0] _th_blink_wdata_6;
  reg _myram_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_7;
  reg signed [32-1:0] _th_blink_gaddr_8;
  reg [10-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _tmp_4;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [9-1:0] _tmp_5;
  reg _myaxi_cond_0_1;
  reg _tmp_6;
  reg _tmp_7;
  wire _tmp_8;
  wire _tmp_9;
  assign _tmp_9 = 1;
  localparam _tmp_10 = 1;
  wire [_tmp_10-1:0] _tmp_11;
  assign _tmp_11 = (_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7);
  reg [_tmp_10-1:0] __tmp_11_1;
  wire [32-1:0] _tmp_12;
  reg [32-1:0] __tmp_12_1;
  assign _tmp_12 = (__tmp_11_1)? myram_0_rdata : __tmp_12_1;
  reg _tmp_13;
  reg _tmp_14;
  reg _tmp_15;
  reg _tmp_16;
  reg [33-1:0] _tmp_17;
  reg _tmp_18;
  wire [32-1:0] _tmp_data_19;
  wire _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_fsm_0 == 3) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  reg signed [32-1:0] _th_blink_lstride_9;
  reg [10-1:0] _tmp_20;
  reg [32-1:0] _tmp_21;
  reg [32-1:0] _tmp_22;
  reg [32-1:0] _tmp_23;
  reg [10-1:0] _tmp_24;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [9-1:0] _tmp_25;
  reg _myaxi_cond_2_1;
  reg _tmp_26;
  reg _tmp_27;
  wire _tmp_28;
  wire _tmp_29;
  assign _tmp_29 = 1;
  localparam _tmp_30 = 1;
  wire [_tmp_30-1:0] _tmp_31;
  assign _tmp_31 = (_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27);
  reg [_tmp_30-1:0] __tmp_31_1;
  wire [32-1:0] _tmp_32;
  reg [32-1:0] __tmp_32_1;
  assign _tmp_32 = (__tmp_31_1)? myram_0_rdata : __tmp_32_1;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg [33-1:0] _tmp_37;
  reg _tmp_38;
  wire [32-1:0] _tmp_data_39;
  wire _tmp_valid_39;
  wire _tmp_ready_39;
  assign _tmp_ready_39 = (_tmp_fsm_1 == 3) && ((_tmp_25 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _myram_cond_1_1;
  reg [10-1:0] _tmp_40;
  reg [32-1:0] _tmp_41;
  reg [32-1:0] _tmp_42;
  reg [32-1:0] _tmp_43;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [9-1:0] _tmp_44;
  reg _myaxi_cond_4_1;
  reg _tmp_45;
  reg _tmp_46;
  wire _tmp_47;
  wire _tmp_48;
  assign _tmp_48 = 1;
  localparam _tmp_49 = 1;
  wire [_tmp_49-1:0] _tmp_50;
  assign _tmp_50 = (_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46);
  reg [_tmp_49-1:0] __tmp_50_1;
  wire [32-1:0] _tmp_51;
  reg [32-1:0] __tmp_51_1;
  assign _tmp_51 = (__tmp_50_1)? myram_0_rdata : __tmp_51_1;
  reg _tmp_52;
  reg _tmp_53;
  reg _tmp_54;
  reg _tmp_55;
  reg [33-1:0] _tmp_56;
  reg _tmp_57;
  wire [32-1:0] _tmp_data_58;
  wire _tmp_valid_58;
  wire _tmp_ready_58;
  assign _tmp_ready_58 = (_tmp_fsm_2 == 3) && ((_tmp_44 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_5_1;
  reg [10-1:0] _tmp_59;
  reg [32-1:0] _tmp_60;
  reg [32-1:0] _tmp_61;
  reg [32-1:0] _tmp_62;
  reg [10-1:0] _tmp_63;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [9-1:0] _tmp_64;
  reg _myaxi_cond_6_1;
  reg _tmp_65;
  reg _tmp_66;
  wire _tmp_67;
  wire _tmp_68;
  assign _tmp_68 = 1;
  localparam _tmp_69 = 1;
  wire [_tmp_69-1:0] _tmp_70;
  assign _tmp_70 = (_tmp_67 || !_tmp_65) && (_tmp_68 || !_tmp_66);
  reg [_tmp_69-1:0] __tmp_70_1;
  wire [32-1:0] _tmp_71;
  reg [32-1:0] __tmp_71_1;
  assign _tmp_71 = (__tmp_70_1)? myram_0_rdata : __tmp_71_1;
  reg _tmp_72;
  reg _tmp_73;
  reg _tmp_74;
  reg _tmp_75;
  reg [33-1:0] _tmp_76;
  reg _tmp_77;
  wire [32-1:0] _tmp_data_78;
  wire _tmp_valid_78;
  wire _tmp_ready_78;
  assign _tmp_ready_78 = (_tmp_fsm_3 == 3) && ((_tmp_64 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_7_1;
  reg [10-1:0] _tmp_79;
  reg [32-1:0] _tmp_80;
  reg [32-1:0] _tmp_81;
  reg [32-1:0] _tmp_82;
  reg [32-1:0] _tmp_fsm_4;
  localparam _tmp_fsm_4_init = 0;
  reg [9-1:0] _tmp_83;
  reg _myaxi_cond_8_1;
  reg [32-1:0] _tmp_84;
  reg _tmp_85;
  reg [33-1:0] _tmp_86;
  reg _tmp_87;
  wire [32-1:0] _tmp_data_88;
  wire _tmp_valid_88;
  wire _tmp_ready_88;
  assign _tmp_ready_88 = (_tmp_86 > 0) && !_tmp_87;
  reg _myram_cond_2_1;
  reg [10-1:0] _tmp_89;
  reg [32-1:0] _tmp_90;
  reg [32-1:0] _tmp_91;
  reg [32-1:0] _tmp_92;
  reg [10-1:0] _tmp_93;
  reg [32-1:0] _tmp_fsm_5;
  localparam _tmp_fsm_5_init = 0;
  reg [9-1:0] _tmp_94;
  reg _myaxi_cond_9_1;
  reg [32-1:0] _tmp_95;
  reg _tmp_96;
  reg [33-1:0] _tmp_97;
  reg _tmp_98;
  wire [32-1:0] _tmp_data_99;
  wire _tmp_valid_99;
  wire _tmp_ready_99;
  assign _tmp_ready_99 = (_tmp_97 > 0) && !_tmp_98;
  reg _myram_cond_3_1;
  reg _tmp_100;
  reg _myram_cond_4_1;
  reg _myram_cond_5_1;
  reg _myram_cond_5_2;
  reg signed [32-1:0] _tmp_101;
  reg signed [32-1:0] _th_blink_rdata_10;
  reg [10-1:0] _tmp_102;
  reg [32-1:0] _tmp_103;
  reg [32-1:0] _tmp_104;
  reg [32-1:0] _tmp_105;
  reg [32-1:0] _tmp_fsm_6;
  localparam _tmp_fsm_6_init = 0;
  reg [9-1:0] _tmp_106;
  reg _myaxi_cond_10_1;
  reg [32-1:0] _tmp_107;
  reg _tmp_108;
  reg [33-1:0] _tmp_109;
  reg _tmp_110;
  wire [32-1:0] _tmp_data_111;
  wire _tmp_valid_111;
  wire _tmp_ready_111;
  assign _tmp_ready_111 = (_tmp_109 > 0) && !_tmp_110;
  reg _myram_cond_6_1;
  reg [10-1:0] _tmp_112;
  reg [32-1:0] _tmp_113;
  reg [32-1:0] _tmp_114;
  reg [32-1:0] _tmp_115;
  reg [10-1:0] _tmp_116;
  reg [32-1:0] _tmp_fsm_7;
  localparam _tmp_fsm_7_init = 0;
  reg [9-1:0] _tmp_117;
  reg _myaxi_cond_11_1;
  reg [32-1:0] _tmp_118;
  reg _tmp_119;
  reg [33-1:0] _tmp_120;
  reg _tmp_121;
  wire [32-1:0] _tmp_data_122;
  wire _tmp_valid_122;
  wire _tmp_ready_122;
  assign _tmp_ready_122 = (_tmp_120 > 0) && !_tmp_121;
  reg _myram_cond_7_1;
  assign myaxi_rready = (_tmp_fsm_4 == 3) || (_tmp_fsm_5 == 3) || (_tmp_fsm_6 == 3) || (_tmp_fsm_7 == 3);
  reg _tmp_123;
  reg _myram_cond_8_1;
  reg _myram_cond_9_1;
  reg _myram_cond_9_2;
  reg signed [32-1:0] _tmp_124;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_5 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_18 <= 0;
      _myaxi_cond_1_1 <= 0;
      _tmp_25 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_38 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_44 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_57 <= 0;
      _myaxi_cond_5_1 <= 0;
      _tmp_64 <= 0;
      _myaxi_cond_6_1 <= 0;
      _tmp_77 <= 0;
      _myaxi_cond_7_1 <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_83 <= 0;
      _myaxi_cond_8_1 <= 0;
      _tmp_94 <= 0;
      _myaxi_cond_9_1 <= 0;
      _tmp_106 <= 0;
      _myaxi_cond_10_1 <= 0;
      _tmp_117 <= 0;
      _myaxi_cond_11_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_18 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_38 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_5_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_57 <= 0;
      end 
      if(_myaxi_cond_6_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_7_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_77 <= 0;
      end 
      if(_myaxi_cond_8_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_9_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_10_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_11_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_tmp_fsm_0 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_5 == 0))) begin
        myaxi_awaddr <= _tmp_2;
        myaxi_awlen <= _tmp_3 - 1;
        myaxi_awvalid <= 1;
        _tmp_5 <= _tmp_3;
      end 
      if((_tmp_fsm_0 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_5 == 0)) && (_tmp_3 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_19 && ((_tmp_fsm_0 == 3) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_5 > 0))) begin
        myaxi_wdata <= _tmp_data_19;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_5 <= _tmp_5 - 1;
      end 
      if(_tmp_valid_19 && ((_tmp_fsm_0 == 3) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_5 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_5 > 0)) && (_tmp_5 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_18 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_18 <= _tmp_18;
      end 
      if((_tmp_fsm_1 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_25 == 0))) begin
        myaxi_awaddr <= _tmp_21;
        myaxi_awlen <= _tmp_22 - 1;
        myaxi_awvalid <= 1;
        _tmp_25 <= _tmp_22;
      end 
      if((_tmp_fsm_1 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_25 == 0)) && (_tmp_22 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_39 && ((_tmp_fsm_1 == 3) && ((_tmp_25 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_25 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_25 > 0))) begin
        myaxi_wdata <= _tmp_data_39;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_25 <= _tmp_25 - 1;
      end 
      if(_tmp_valid_39 && ((_tmp_fsm_1 == 3) && ((_tmp_25 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_25 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_25 > 0)) && (_tmp_25 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_38 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_38 <= _tmp_38;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_44 == 0))) begin
        myaxi_awaddr <= _tmp_41;
        myaxi_awlen <= _tmp_42 - 1;
        myaxi_awvalid <= 1;
        _tmp_44 <= _tmp_42;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_44 == 0)) && (_tmp_42 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_58 && ((_tmp_fsm_2 == 3) && ((_tmp_44 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_44 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_44 > 0))) begin
        myaxi_wdata <= _tmp_data_58;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_44 <= _tmp_44 - 1;
      end 
      if(_tmp_valid_58 && ((_tmp_fsm_2 == 3) && ((_tmp_44 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_44 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_44 > 0)) && (_tmp_44 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_57 <= 1;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_57 <= _tmp_57;
      end 
      if((_tmp_fsm_3 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_64 == 0))) begin
        myaxi_awaddr <= _tmp_60;
        myaxi_awlen <= _tmp_61 - 1;
        myaxi_awvalid <= 1;
        _tmp_64 <= _tmp_61;
      end 
      if((_tmp_fsm_3 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_64 == 0)) && (_tmp_61 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_6_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_78 && ((_tmp_fsm_3 == 3) && ((_tmp_64 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_64 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_64 > 0))) begin
        myaxi_wdata <= _tmp_data_78;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_64 <= _tmp_64 - 1;
      end 
      if(_tmp_valid_78 && ((_tmp_fsm_3 == 3) && ((_tmp_64 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_64 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_64 > 0)) && (_tmp_64 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_77 <= 1;
      end 
      _myaxi_cond_7_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_77 <= _tmp_77;
      end 
      if((_tmp_fsm_4 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_83 == 0))) begin
        myaxi_araddr <= _tmp_80;
        myaxi_arlen <= _tmp_81 - 1;
        myaxi_arvalid <= 1;
        _tmp_83 <= _tmp_81;
      end 
      _myaxi_cond_8_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_83 > 0)) begin
        _tmp_83 <= _tmp_83 - 1;
      end 
      if((_tmp_fsm_5 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_94 == 0))) begin
        myaxi_araddr <= _tmp_90;
        myaxi_arlen <= _tmp_91 - 1;
        myaxi_arvalid <= 1;
        _tmp_94 <= _tmp_91;
      end 
      _myaxi_cond_9_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_94 > 0)) begin
        _tmp_94 <= _tmp_94 - 1;
      end 
      if((_tmp_fsm_6 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_106 == 0))) begin
        myaxi_araddr <= _tmp_103;
        myaxi_arlen <= _tmp_104 - 1;
        myaxi_arvalid <= 1;
        _tmp_106 <= _tmp_104;
      end 
      _myaxi_cond_10_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_106 > 0)) begin
        _tmp_106 <= _tmp_106 - 1;
      end 
      if((_tmp_fsm_7 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_117 == 0))) begin
        myaxi_araddr <= _tmp_113;
        myaxi_arlen <= _tmp_114 - 1;
        myaxi_arvalid <= 1;
        _tmp_117 <= _tmp_114;
      end 
      _myaxi_cond_11_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_117 > 0)) begin
        _tmp_117 <= _tmp_117 - 1;
      end 
    end
  end

  assign _tmp_data_88 = _tmp_84;
  assign _tmp_valid_88 = _tmp_85;
  assign _tmp_data_99 = _tmp_95;
  assign _tmp_valid_99 = _tmp_96;
  assign _tmp_data_111 = _tmp_107;
  assign _tmp_valid_111 = _tmp_108;
  assign _tmp_data_122 = _tmp_118;
  assign _tmp_valid_122 = _tmp_119;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
      __tmp_11_1 <= 0;
      __tmp_12_1 <= 0;
      _tmp_16 <= 0;
      _tmp_6 <= 0;
      _tmp_7 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_13 <= 0;
      _tmp_17 <= 0;
      __tmp_31_1 <= 0;
      __tmp_32_1 <= 0;
      _tmp_36 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_33 <= 0;
      _tmp_37 <= 0;
      _myram_cond_1_1 <= 0;
      __tmp_50_1 <= 0;
      __tmp_51_1 <= 0;
      _tmp_55 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_52 <= 0;
      _tmp_56 <= 0;
      __tmp_70_1 <= 0;
      __tmp_71_1 <= 0;
      _tmp_75 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_72 <= 0;
      _tmp_76 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _myram_cond_2_1 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _myram_cond_3_1 <= 0;
      _myram_cond_4_1 <= 0;
      _tmp_100 <= 0;
      _myram_cond_5_1 <= 0;
      _myram_cond_5_2 <= 0;
      _tmp_109 <= 0;
      _tmp_110 <= 0;
      _myram_cond_6_1 <= 0;
      _tmp_120 <= 0;
      _tmp_121 <= 0;
      _myram_cond_7_1 <= 0;
      _myram_cond_8_1 <= 0;
      _tmp_123 <= 0;
      _myram_cond_9_1 <= 0;
      _myram_cond_9_2 <= 0;
    end else begin
      if(_myram_cond_5_2) begin
        _tmp_100 <= 0;
      end 
      if(_myram_cond_9_2) begin
        _tmp_123 <= 0;
      end 
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_1_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_2_1) begin
        myram_0_wenable <= 0;
        _tmp_87 <= 0;
      end 
      if(_myram_cond_3_1) begin
        myram_0_wenable <= 0;
        _tmp_98 <= 0;
      end 
      if(_myram_cond_4_1) begin
        _tmp_100 <= 1;
      end 
      _myram_cond_5_2 <= _myram_cond_5_1;
      if(_myram_cond_6_1) begin
        myram_0_wenable <= 0;
        _tmp_110 <= 0;
      end 
      if(_myram_cond_7_1) begin
        myram_0_wenable <= 0;
        _tmp_121 <= 0;
      end 
      if(_myram_cond_8_1) begin
        _tmp_123 <= 1;
      end 
      _myram_cond_9_2 <= _myram_cond_9_1;
      if(th_blink == 10) begin
        myram_0_addr <= _th_blink_i_5;
        myram_0_wdata <= _th_blink_wdata_6;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= th_blink == 10;
      __tmp_11_1 <= _tmp_11;
      __tmp_12_1 <= _tmp_12;
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && _tmp_14) begin
        _tmp_16 <= 0;
        _tmp_6 <= 0;
        _tmp_7 <= 0;
        _tmp_14 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && _tmp_13) begin
        _tmp_6 <= 1;
        _tmp_7 <= 1;
        _tmp_16 <= _tmp_15;
        _tmp_15 <= 0;
        _tmp_13 <= 0;
        _tmp_14 <= 1;
      end 
      if((_tmp_fsm_0 == 2) && (_tmp_17 == 0) && !_tmp_15 && !_tmp_16) begin
        myram_0_addr <= _tmp_1;
        _tmp_17 <= _tmp_3 - 1;
        _tmp_13 <= 1;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_17 > 0)) begin
        myram_0_addr <= myram_0_addr + 2;
        _tmp_17 <= _tmp_17 - 1;
        _tmp_13 <= 1;
        _tmp_15 <= 0;
      end 
      if((_tmp_8 || !_tmp_6) && (_tmp_9 || !_tmp_7) && (_tmp_17 == 1)) begin
        _tmp_15 <= 1;
      end 
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
      if((_tmp_fsm_1 == 2) && (_tmp_37 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_0_addr <= _tmp_20;
        _tmp_37 <= _tmp_22 - 1;
        _tmp_33 <= 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 > 0)) begin
        myram_0_addr <= myram_0_addr + _tmp_24;
        _tmp_37 <= _tmp_37 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 == 1)) begin
        _tmp_35 <= 1;
      end 
      if(th_blink == 25) begin
        myram_0_addr <= _th_blink_i_5;
        myram_0_wdata <= _th_blink_wdata_6;
        myram_0_wenable <= 1;
      end 
      _myram_cond_1_1 <= th_blink == 25;
      __tmp_50_1 <= _tmp_50;
      __tmp_51_1 <= _tmp_51;
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_53) begin
        _tmp_55 <= 0;
        _tmp_45 <= 0;
        _tmp_46 <= 0;
        _tmp_53 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_52) begin
        _tmp_45 <= 1;
        _tmp_46 <= 1;
        _tmp_55 <= _tmp_54;
        _tmp_54 <= 0;
        _tmp_52 <= 0;
        _tmp_53 <= 1;
      end 
      if((_tmp_fsm_2 == 2) && (_tmp_56 == 0) && !_tmp_54 && !_tmp_55) begin
        myram_0_addr <= _tmp_40;
        _tmp_56 <= _tmp_42 - 1;
        _tmp_52 <= 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && (_tmp_56 > 0)) begin
        myram_0_addr <= myram_0_addr + 2;
        _tmp_56 <= _tmp_56 - 1;
        _tmp_52 <= 1;
        _tmp_54 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && (_tmp_56 == 1)) begin
        _tmp_54 <= 1;
      end 
      __tmp_70_1 <= _tmp_70;
      __tmp_71_1 <= _tmp_71;
      if((_tmp_67 || !_tmp_65) && (_tmp_68 || !_tmp_66) && _tmp_73) begin
        _tmp_75 <= 0;
        _tmp_65 <= 0;
        _tmp_66 <= 0;
        _tmp_73 <= 0;
      end 
      if((_tmp_67 || !_tmp_65) && (_tmp_68 || !_tmp_66) && _tmp_72) begin
        _tmp_65 <= 1;
        _tmp_66 <= 1;
        _tmp_75 <= _tmp_74;
        _tmp_74 <= 0;
        _tmp_72 <= 0;
        _tmp_73 <= 1;
      end 
      if((_tmp_fsm_3 == 2) && (_tmp_76 == 0) && !_tmp_74 && !_tmp_75) begin
        myram_0_addr <= _tmp_59;
        _tmp_76 <= _tmp_61 - 1;
        _tmp_72 <= 1;
      end 
      if((_tmp_67 || !_tmp_65) && (_tmp_68 || !_tmp_66) && (_tmp_76 > 0)) begin
        myram_0_addr <= myram_0_addr + _tmp_63;
        _tmp_76 <= _tmp_76 - 1;
        _tmp_72 <= 1;
        _tmp_74 <= 0;
      end 
      if((_tmp_67 || !_tmp_65) && (_tmp_68 || !_tmp_66) && (_tmp_76 == 1)) begin
        _tmp_74 <= 1;
      end 
      if((_tmp_fsm_4 == 2) && (_tmp_86 == 0)) begin
        myram_0_addr <= _tmp_79 - 2;
        _tmp_86 <= _tmp_81;
      end 
      if(_tmp_valid_88 && ((_tmp_86 > 0) && !_tmp_87) && (_tmp_86 > 0)) begin
        myram_0_addr <= myram_0_addr + 2;
        myram_0_wdata <= _tmp_data_88;
        myram_0_wenable <= 1;
        _tmp_86 <= _tmp_86 - 1;
      end 
      if(_tmp_valid_88 && ((_tmp_86 > 0) && !_tmp_87) && (_tmp_86 == 1)) begin
        _tmp_87 <= 1;
      end 
      _myram_cond_2_1 <= 1;
      if((_tmp_fsm_5 == 2) && (_tmp_97 == 0)) begin
        myram_0_addr <= _tmp_89 - _tmp_93;
        _tmp_97 <= _tmp_91;
      end 
      if(_tmp_valid_99 && ((_tmp_97 > 0) && !_tmp_98) && (_tmp_97 > 0)) begin
        myram_0_addr <= myram_0_addr + _tmp_93;
        myram_0_wdata <= _tmp_data_99;
        myram_0_wenable <= 1;
        _tmp_97 <= _tmp_97 - 1;
      end 
      if(_tmp_valid_99 && ((_tmp_97 > 0) && !_tmp_98) && (_tmp_97 == 1)) begin
        _tmp_98 <= 1;
      end 
      _myram_cond_3_1 <= 1;
      if(th_blink == 49) begin
        myram_0_addr <= _th_blink_i_5;
      end 
      _myram_cond_4_1 <= th_blink == 49;
      _myram_cond_5_1 <= th_blink == 49;
      if((_tmp_fsm_6 == 2) && (_tmp_109 == 0)) begin
        myram_0_addr <= _tmp_102 - 2;
        _tmp_109 <= _tmp_104;
      end 
      if(_tmp_valid_111 && ((_tmp_109 > 0) && !_tmp_110) && (_tmp_109 > 0)) begin
        myram_0_addr <= myram_0_addr + 2;
        myram_0_wdata <= _tmp_data_111;
        myram_0_wenable <= 1;
        _tmp_109 <= _tmp_109 - 1;
      end 
      if(_tmp_valid_111 && ((_tmp_109 > 0) && !_tmp_110) && (_tmp_109 == 1)) begin
        _tmp_110 <= 1;
      end 
      _myram_cond_6_1 <= 1;
      if((_tmp_fsm_7 == 2) && (_tmp_120 == 0)) begin
        myram_0_addr <= _tmp_112 - _tmp_116;
        _tmp_120 <= _tmp_114;
      end 
      if(_tmp_valid_122 && ((_tmp_120 > 0) && !_tmp_121) && (_tmp_120 > 0)) begin
        myram_0_addr <= myram_0_addr + _tmp_116;
        myram_0_wdata <= _tmp_data_122;
        myram_0_wenable <= 1;
        _tmp_120 <= _tmp_120 - 1;
      end 
      if(_tmp_valid_122 && ((_tmp_120 > 0) && !_tmp_121) && (_tmp_120 == 1)) begin
        _tmp_121 <= 1;
      end 
      _myram_cond_7_1 <= 1;
      if(th_blink == 67) begin
        myram_0_addr <= _th_blink_i_5;
      end 
      _myram_cond_8_1 <= th_blink == 67;
      _myram_cond_9_1 <= th_blink == 67;
    end
  end

  assign _tmp_data_19 = _tmp_12;
  assign _tmp_valid_19 = _tmp_6;
  assign _tmp_8 = 1 && _tmp_ready_19;
  assign _tmp_data_39 = _tmp_32;
  assign _tmp_valid_39 = _tmp_26;
  assign _tmp_28 = 1 && _tmp_ready_39;
  assign _tmp_data_58 = _tmp_51;
  assign _tmp_valid_58 = _tmp_45;
  assign _tmp_47 = 1 && _tmp_ready_58;
  assign _tmp_data_78 = _tmp_71;
  assign _tmp_valid_78 = _tmp_65;
  assign _tmp_67 = 1 && _tmp_ready_78;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_offset_2 <= 0;
      _th_blink_size_3 <= 0;
      _th_blink_offset_4 <= 0;
      _th_blink_i_5 <= 0;
      _th_blink_wdata_6 <= 0;
      _th_blink_laddr_7 <= 0;
      _th_blink_gaddr_8 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_4 <= 0;
      _tmp_3 <= 0;
      _th_blink_lstride_9 <= 0;
      _tmp_20 <= 0;
      _tmp_21 <= 0;
      _tmp_23 <= 0;
      _tmp_24 <= 1;
      _tmp_22 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
      _tmp_43 <= 0;
      _tmp_42 <= 0;
      _tmp_59 <= 0;
      _tmp_60 <= 0;
      _tmp_62 <= 0;
      _tmp_63 <= 1;
      _tmp_61 <= 0;
      _tmp_79 <= 0;
      _tmp_80 <= 0;
      _tmp_82 <= 0;
      _tmp_81 <= 0;
      _tmp_89 <= 0;
      _tmp_90 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 1;
      _tmp_91 <= 0;
      _tmp_101 <= 0;
      _th_blink_rdata_10 <= 0;
      _tmp_102 <= 0;
      _tmp_103 <= 0;
      _tmp_105 <= 0;
      _tmp_104 <= 0;
      _tmp_112 <= 0;
      _tmp_113 <= 0;
      _tmp_115 <= 0;
      _tmp_116 <= 1;
      _tmp_114 <= 0;
      _tmp_124 <= 0;
    end else begin
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
            th_blink <= th_blink_75;
          end
        end
        th_blink_4: begin
          $display("# iter %d start", _th_blink_i_1);
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_offset_2 <= (_th_blink_i_1 << 10) << 4;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_size_3 <= _th_blink_size_0;
          _th_blink_offset_4 <= _th_blink_offset_2;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_12;
          end
        end
        th_blink_9: begin
          _th_blink_wdata_6 <= _th_blink_i_5 + 100;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_8;
        end
        th_blink_12: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          _th_blink_gaddr_8 <= _th_blink_offset_4;
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          _tmp_1 <= _th_blink_laddr_7;
          _tmp_2 <= _th_blink_gaddr_8;
          _tmp_4 <= _th_blink_size_3 >>> 1;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          if(_tmp_4 <= 256) begin
            _tmp_3 <= _tmp_4;
            _tmp_4 <= 0;
          end else begin
            _tmp_3 <= 256;
            _tmp_4 <= _tmp_4 - 256;
          end
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          if(_tmp_18) begin
            _tmp_1 <= _tmp_1 + _tmp_3;
            _tmp_2 <= _tmp_2 + (_tmp_3 << 2);
          end 
          if(_tmp_18 && (_tmp_4 > 0)) begin
            th_blink <= th_blink_15;
          end 
          if(_tmp_18 && (_tmp_4 == 0)) begin
            th_blink <= th_blink_17;
          end 
        end
        th_blink_17: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          _tmp_20 <= _th_blink_laddr_7 + 1;
          _tmp_21 <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
          _tmp_23 <= _th_blink_size_3 >>> 1;
          _tmp_24 <= _th_blink_lstride_9;
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          if(_tmp_23 <= 256) begin
            _tmp_22 <= _tmp_23;
            _tmp_23 <= 0;
          end else begin
            _tmp_22 <= 256;
            _tmp_23 <= _tmp_23 - 256;
          end
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          if(_tmp_38) begin
            _tmp_20 <= _tmp_20 + _tmp_22;
            _tmp_21 <= _tmp_21 + (_tmp_22 << 2);
          end 
          if(_tmp_38 && (_tmp_23 > 0)) begin
            th_blink <= th_blink_19;
          end 
          if(_tmp_38 && (_tmp_23 == 0)) begin
            th_blink <= th_blink_21;
          end 
        end
        th_blink_21: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_24;
          end else begin
            th_blink <= th_blink_27;
          end
        end
        th_blink_24: begin
          _th_blink_wdata_6 <= _th_blink_i_5 + 1000;
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_23;
        end
        th_blink_27: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_28;
        end
        th_blink_28: begin
          _th_blink_gaddr_8 <= (_th_blink_size_3 + _th_blink_size_3 << 2) + _th_blink_offset_4;
          th_blink <= th_blink_29;
        end
        th_blink_29: begin
          _tmp_40 <= _th_blink_laddr_7;
          _tmp_41 <= _th_blink_gaddr_8;
          _tmp_43 <= _th_blink_size_3 >>> 1;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          if(_tmp_43 <= 256) begin
            _tmp_42 <= _tmp_43;
            _tmp_43 <= 0;
          end else begin
            _tmp_42 <= 256;
            _tmp_43 <= _tmp_43 - 256;
          end
          th_blink <= th_blink_31;
        end
        th_blink_31: begin
          if(_tmp_57) begin
            _tmp_40 <= _tmp_40 + _tmp_42;
            _tmp_41 <= _tmp_41 + (_tmp_42 << 2);
          end 
          if(_tmp_57 && (_tmp_43 > 0)) begin
            th_blink <= th_blink_30;
          end 
          if(_tmp_57 && (_tmp_43 == 0)) begin
            th_blink <= th_blink_32;
          end 
        end
        th_blink_32: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          _tmp_59 <= _th_blink_laddr_7 + 1;
          _tmp_60 <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
          _tmp_62 <= _th_blink_size_3 >>> 1;
          _tmp_63 <= _th_blink_lstride_9;
          th_blink <= th_blink_34;
        end
        th_blink_34: begin
          if(_tmp_62 <= 256) begin
            _tmp_61 <= _tmp_62;
            _tmp_62 <= 0;
          end else begin
            _tmp_61 <= 256;
            _tmp_62 <= _tmp_62 - 256;
          end
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          if(_tmp_77) begin
            _tmp_59 <= _tmp_59 + _tmp_61;
            _tmp_60 <= _tmp_60 + (_tmp_61 << 2);
          end 
          if(_tmp_77 && (_tmp_62 > 0)) begin
            th_blink <= th_blink_34;
          end 
          if(_tmp_77 && (_tmp_62 == 0)) begin
            th_blink <= th_blink_36;
          end 
        end
        th_blink_36: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_37;
        end
        th_blink_37: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          _th_blink_gaddr_8 <= _th_blink_offset_4;
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          _tmp_79 <= _th_blink_laddr_7;
          _tmp_80 <= _th_blink_gaddr_8;
          _tmp_82 <= _th_blink_size_3 >>> 1;
          th_blink <= th_blink_40;
        end
        th_blink_40: begin
          if(_tmp_82 <= 256) begin
            _tmp_81 <= _tmp_82;
            _tmp_82 <= 0;
          end else begin
            _tmp_81 <= 256;
            _tmp_82 <= _tmp_82 - 256;
          end
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          if(_tmp_87) begin
            _tmp_79 <= _tmp_79 + _tmp_81;
            _tmp_80 <= _tmp_80 + (_tmp_81 << 2);
          end 
          if(_tmp_87 && (_tmp_82 > 0)) begin
            th_blink <= th_blink_40;
          end 
          if(_tmp_87 && (_tmp_82 == 0)) begin
            th_blink <= th_blink_42;
          end 
        end
        th_blink_42: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          _tmp_89 <= _th_blink_laddr_7 + 1;
          _tmp_90 <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
          _tmp_92 <= _th_blink_size_3 >>> 1;
          _tmp_93 <= _th_blink_lstride_9;
          th_blink <= th_blink_44;
        end
        th_blink_44: begin
          if(_tmp_92 <= 256) begin
            _tmp_91 <= _tmp_92;
            _tmp_92 <= 0;
          end else begin
            _tmp_91 <= 256;
            _tmp_92 <= _tmp_92 - 256;
          end
          th_blink <= th_blink_45;
        end
        th_blink_45: begin
          if(_tmp_98) begin
            _tmp_89 <= _tmp_89 + _tmp_91;
            _tmp_90 <= _tmp_90 + (_tmp_91 << 2);
          end 
          if(_tmp_98 && (_tmp_92 > 0)) begin
            th_blink <= th_blink_44;
          end 
          if(_tmp_98 && (_tmp_92 == 0)) begin
            th_blink <= th_blink_46;
          end 
        end
        th_blink_46: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_47;
        end
        th_blink_47: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_48;
        end
        th_blink_48: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_49;
          end else begin
            th_blink <= th_blink_55;
          end
        end
        th_blink_49: begin
          if(_tmp_100) begin
            _tmp_101 <= myram_0_rdata;
          end 
          if(_tmp_100) begin
            th_blink <= th_blink_50;
          end 
        end
        th_blink_50: begin
          _th_blink_rdata_10 <= _tmp_101;
          th_blink <= th_blink_51;
        end
        th_blink_51: begin
          if(_th_blink_rdata_10 !== _th_blink_i_5 + 100) begin
            th_blink <= th_blink_52;
          end else begin
            th_blink <= th_blink_54;
          end
        end
        th_blink_52: begin
          $display("rdata[%d] = %d", _th_blink_i_5, _th_blink_rdata_10);
          th_blink <= th_blink_53;
        end
        th_blink_53: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_48;
        end
        th_blink_55: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_56;
        end
        th_blink_56: begin
          _th_blink_gaddr_8 <= (_th_blink_size_3 + _th_blink_size_3 << 2) + _th_blink_offset_4;
          th_blink <= th_blink_57;
        end
        th_blink_57: begin
          _tmp_102 <= _th_blink_laddr_7;
          _tmp_103 <= _th_blink_gaddr_8;
          _tmp_105 <= _th_blink_size_3 >>> 1;
          th_blink <= th_blink_58;
        end
        th_blink_58: begin
          if(_tmp_105 <= 256) begin
            _tmp_104 <= _tmp_105;
            _tmp_105 <= 0;
          end else begin
            _tmp_104 <= 256;
            _tmp_105 <= _tmp_105 - 256;
          end
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          if(_tmp_110) begin
            _tmp_102 <= _tmp_102 + _tmp_104;
            _tmp_103 <= _tmp_103 + (_tmp_104 << 2);
          end 
          if(_tmp_110 && (_tmp_105 > 0)) begin
            th_blink <= th_blink_58;
          end 
          if(_tmp_110 && (_tmp_105 == 0)) begin
            th_blink <= th_blink_60;
          end 
        end
        th_blink_60: begin
          _th_blink_lstride_9 <= 2;
          th_blink <= th_blink_61;
        end
        th_blink_61: begin
          _tmp_112 <= _th_blink_laddr_7 + 1;
          _tmp_113 <= _th_blink_gaddr_8 + (_th_blink_size_3 << 2);
          _tmp_115 <= _th_blink_size_3 >>> 1;
          _tmp_116 <= _th_blink_lstride_9;
          th_blink <= th_blink_62;
        end
        th_blink_62: begin
          if(_tmp_115 <= 256) begin
            _tmp_114 <= _tmp_115;
            _tmp_115 <= 0;
          end else begin
            _tmp_114 <= 256;
            _tmp_115 <= _tmp_115 - 256;
          end
          th_blink <= th_blink_63;
        end
        th_blink_63: begin
          if(_tmp_121) begin
            _tmp_112 <= _tmp_112 + _tmp_114;
            _tmp_113 <= _tmp_113 + (_tmp_114 << 2);
          end 
          if(_tmp_121 && (_tmp_115 > 0)) begin
            th_blink <= th_blink_62;
          end 
          if(_tmp_121 && (_tmp_115 == 0)) begin
            th_blink <= th_blink_64;
          end 
        end
        th_blink_64: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_65;
        end
        th_blink_65: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_66;
        end
        th_blink_66: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_67;
          end else begin
            th_blink <= th_blink_73;
          end
        end
        th_blink_67: begin
          if(_tmp_123) begin
            _tmp_124 <= myram_0_rdata;
          end 
          if(_tmp_123) begin
            th_blink <= th_blink_68;
          end 
        end
        th_blink_68: begin
          _th_blink_rdata_10 <= _tmp_124;
          th_blink <= th_blink_69;
        end
        th_blink_69: begin
          if(_th_blink_rdata_10 !== _th_blink_i_5 + 1000) begin
            th_blink <= th_blink_70;
          end else begin
            th_blink <= th_blink_72;
          end
        end
        th_blink_70: begin
          $display("rdata[%d] = %d", _th_blink_i_5, _th_blink_rdata_10);
          th_blink <= th_blink_71;
        end
        th_blink_71: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_72;
        end
        th_blink_72: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_66;
        end
        th_blink_73: begin
          $display("# iter %d end", _th_blink_i_1);
          th_blink <= th_blink_74;
        end
        th_blink_74: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_75: begin
          if(_tmp_0) begin
            th_blink <= th_blink_76;
          end else begin
            th_blink <= th_blink_77;
          end
        end
        th_blink_76: begin
          $display("ALL OK");
          th_blink <= th_blink_77;
        end
      endcase
    end
  end

  localparam _tmp_fsm_0_1 = 1;
  localparam _tmp_fsm_0_2 = 2;
  localparam _tmp_fsm_0_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_0 <= _tmp_fsm_0_init;
    end else begin
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_blink == 16) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
        end
        _tmp_fsm_0_2: begin
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          if(_tmp_18) begin
            _tmp_fsm_0 <= _tmp_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_1_1 = 1;
  localparam _tmp_fsm_1_2 = 2;
  localparam _tmp_fsm_1_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_1 <= _tmp_fsm_1_init;
    end else begin
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_blink == 20) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
        end
        _tmp_fsm_1_2: begin
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(_tmp_38) begin
            _tmp_fsm_1 <= _tmp_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_2_1 = 1;
  localparam _tmp_fsm_2_2 = 2;
  localparam _tmp_fsm_2_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_2 <= _tmp_fsm_2_init;
    end else begin
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_blink == 31) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
        end
        _tmp_fsm_2_2: begin
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(_tmp_57) begin
            _tmp_fsm_2 <= _tmp_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_3_1 = 1;
  localparam _tmp_fsm_3_2 = 2;
  localparam _tmp_fsm_3_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_3 <= _tmp_fsm_3_init;
    end else begin
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_blink == 35) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
        end
        _tmp_fsm_3_2: begin
          _tmp_fsm_3 <= _tmp_fsm_3_3;
        end
        _tmp_fsm_3_3: begin
          if(_tmp_77) begin
            _tmp_fsm_3 <= _tmp_fsm_3_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_4_1 = 1;
  localparam _tmp_fsm_4_2 = 2;
  localparam _tmp_fsm_4_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_4 <= _tmp_fsm_4_init;
      _tmp_85 <= 0;
      _tmp_84 <= 0;
    end else begin
      case(_tmp_fsm_4)
        _tmp_fsm_4_init: begin
          if(th_blink == 41) begin
            _tmp_fsm_4 <= _tmp_fsm_4_1;
          end 
        end
        _tmp_fsm_4_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_4 <= _tmp_fsm_4_2;
          end 
        end
        _tmp_fsm_4_2: begin
          _tmp_fsm_4 <= _tmp_fsm_4_3;
        end
        _tmp_fsm_4_3: begin
          _tmp_85 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_84 <= myaxi_rdata;
            _tmp_85 <= 1;
          end 
          if(_tmp_87) begin
            _tmp_fsm_4 <= _tmp_fsm_4_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_5_1 = 1;
  localparam _tmp_fsm_5_2 = 2;
  localparam _tmp_fsm_5_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_5 <= _tmp_fsm_5_init;
      _tmp_96 <= 0;
      _tmp_95 <= 0;
    end else begin
      case(_tmp_fsm_5)
        _tmp_fsm_5_init: begin
          if(th_blink == 45) begin
            _tmp_fsm_5 <= _tmp_fsm_5_1;
          end 
        end
        _tmp_fsm_5_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_5 <= _tmp_fsm_5_2;
          end 
        end
        _tmp_fsm_5_2: begin
          _tmp_fsm_5 <= _tmp_fsm_5_3;
        end
        _tmp_fsm_5_3: begin
          _tmp_96 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_95 <= myaxi_rdata;
            _tmp_96 <= 1;
          end 
          if(_tmp_98) begin
            _tmp_fsm_5 <= _tmp_fsm_5_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_6_1 = 1;
  localparam _tmp_fsm_6_2 = 2;
  localparam _tmp_fsm_6_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_6 <= _tmp_fsm_6_init;
      _tmp_108 <= 0;
      _tmp_107 <= 0;
    end else begin
      case(_tmp_fsm_6)
        _tmp_fsm_6_init: begin
          if(th_blink == 59) begin
            _tmp_fsm_6 <= _tmp_fsm_6_1;
          end 
        end
        _tmp_fsm_6_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_6 <= _tmp_fsm_6_2;
          end 
        end
        _tmp_fsm_6_2: begin
          _tmp_fsm_6 <= _tmp_fsm_6_3;
        end
        _tmp_fsm_6_3: begin
          _tmp_108 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_107 <= myaxi_rdata;
            _tmp_108 <= 1;
          end 
          if(_tmp_110) begin
            _tmp_fsm_6 <= _tmp_fsm_6_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_7_1 = 1;
  localparam _tmp_fsm_7_2 = 2;
  localparam _tmp_fsm_7_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_7 <= _tmp_fsm_7_init;
      _tmp_119 <= 0;
      _tmp_118 <= 0;
    end else begin
      case(_tmp_fsm_7)
        _tmp_fsm_7_init: begin
          if(th_blink == 63) begin
            _tmp_fsm_7 <= _tmp_fsm_7_1;
          end 
        end
        _tmp_fsm_7_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_7 <= _tmp_fsm_7_2;
          end 
        end
        _tmp_fsm_7_2: begin
          _tmp_fsm_7 <= _tmp_fsm_7_3;
        end
        _tmp_fsm_7_3: begin
          _tmp_119 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_118 <= myaxi_rdata;
            _tmp_119 <= 1;
          end 
          if(_tmp_121) begin
            _tmp_fsm_7 <= _tmp_fsm_7_init;
          end 
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
    test_module = thread_axi_dma_stride.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
