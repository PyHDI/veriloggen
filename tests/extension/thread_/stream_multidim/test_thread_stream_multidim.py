from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_multidim

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

  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_offset_0;
  reg [10-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _tmp_3;
  reg [33-1:0] _tmp_4;
  reg [33-1:0] _tmp_5;
  reg [32-1:0] _tmp_6;
  reg _tmp_7;
  reg [33-1:0] _tmp_8;
  reg _tmp_9;
  wire [32-1:0] _tmp_data_10;
  wire _tmp_valid_10;
  wire _tmp_ready_10;
  assign _tmp_ready_10 = (_tmp_8 > 0) && !_tmp_9;
  reg _ram_a_cond_0_1;
  reg [9-1:0] _tmp_11;
  reg _myaxi_cond_0_1;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_4_0_1;
  reg _tmp_12;
  reg __tmp_fsm_0_cond_5_1_1;
  reg [10-1:0] _tmp_13;
  reg [32-1:0] _tmp_14;
  reg [32-1:0] _tmp_15;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_16;
  reg [33-1:0] _tmp_17;
  reg [33-1:0] _tmp_18;
  reg [32-1:0] _tmp_19;
  reg _tmp_20;
  reg [33-1:0] _tmp_21;
  reg _tmp_22;
  wire [32-1:0] _tmp_data_23;
  wire _tmp_valid_23;
  wire _tmp_ready_23;
  assign _tmp_ready_23 = (_tmp_21 > 0) && !_tmp_22;
  reg _ram_b_cond_0_1;
  reg [9-1:0] _tmp_24;
  reg _myaxi_cond_1_1;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_4_0_1;
  reg _tmp_25;
  reg __tmp_fsm_1_cond_5_1_1;
  reg [32-1:0] mystream;
  localparam mystream_init = 0;
  reg _mystream_start_cond;
  reg _mystream_called;
  reg signed [32-1:0] _mystream_offset_1;
  reg _mystream_flag_2;
  reg [32-1:0] _mystream_fsm_3;
  localparam _mystream_fsm_3_init = 0;
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
  assign _tmp_32 = (__tmp_31_1)? ram_a_0_rdata : __tmp_32_1;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg _tmp_37;
  wire [10-1:0] _tmp_38;
  wire [10-1:0] _tmp_39;
  reg [10-1:0] _tmp_40;
  reg [10-1:0] _tmp_41;
  assign _tmp_39 = _tmp_41 + (_tmp_40 + _mystream_offset_1);
  reg [5-1:0] _tmp_42;
  reg [4-1:0] _tmp_43;
  reg [6-1:0] _tmp_44;
  assign _tmp_38 = ((0 && 0)? _tmp_44 == 0 : _tmp_42 == 0)? _tmp_39 : ram_a_0_addr + ((0 && 0)? 1 : 64);
  reg _mystream_flag_4;
  reg [32-1:0] _mystream_fsm_5;
  localparam _mystream_fsm_5_init = 0;
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
  assign _tmp_51 = (__tmp_50_1)? ram_b_0_rdata : __tmp_51_1;
  reg _tmp_52;
  reg _tmp_53;
  reg _tmp_54;
  reg _tmp_55;
  reg _tmp_56;
  wire [10-1:0] _tmp_57;
  wire [10-1:0] _tmp_58;
  reg [10-1:0] _tmp_59;
  reg [10-1:0] _tmp_60;
  assign _tmp_58 = _tmp_60 + (_tmp_59 + _mystream_offset_1);
  reg [5-1:0] _tmp_61;
  reg [4-1:0] _tmp_62;
  reg [6-1:0] _tmp_63;
  assign _tmp_57 = ((0 && 0)? _tmp_63 == 0 : _tmp_61 == 0)? _tmp_58 : ram_b_0_addr + ((0 && 0)? 1 : 64);
  reg _mystream_flag_6;
  reg [32-1:0] _mystream_fsm_7;
  localparam _mystream_fsm_7_init = 0;
  reg [2-1:0] _tmp_64;
  reg _tmp_65;
  wire _tmp_all_valid_66;
  wire [32-1:0] _tmp_data_67;
  wire _tmp_valid_67;
  wire _tmp_ready_67;
  assign _tmp_ready_67 = (_tmp_64 > 0) && !_tmp_65 && _tmp_all_valid_66;
  wire [1-1:0] _tmp_data_68;
  wire _tmp_valid_68;
  wire _tmp_ready_68;
  assign _tmp_ready_68 = (_tmp_64 > 0) && !_tmp_65 && _tmp_all_valid_66;
  assign _tmp_all_valid_66 = _tmp_valid_67 && _tmp_valid_68;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_69;
  reg [32-1:0] _tmp_70;
  reg [32-1:0] _tmp_71;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_72;
  reg [33-1:0] _tmp_73;
  reg [33-1:0] _tmp_74;
  reg _tmp_75;
  reg _tmp_76;
  wire _tmp_77;
  wire _tmp_78;
  assign _tmp_78 = 1;
  localparam _tmp_79 = 1;
  wire [_tmp_79-1:0] _tmp_80;
  assign _tmp_80 = (_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76);
  reg [_tmp_79-1:0] __tmp_80_1;
  wire [32-1:0] _tmp_81;
  reg [32-1:0] __tmp_81_1;
  assign _tmp_81 = (__tmp_80_1)? ram_c_0_rdata : __tmp_81_1;
  reg _tmp_82;
  reg _tmp_83;
  reg _tmp_84;
  reg _tmp_85;
  reg [33-1:0] _tmp_86;
  reg [9-1:0] _tmp_87;
  reg _myaxi_cond_2_1;
  reg _tmp_88;
  wire [32-1:0] _tmp_data_89;
  wire _tmp_valid_89;
  wire _tmp_ready_89;
  assign _tmp_ready_89 = (_tmp_fsm_2 == 4) && ((_tmp_87 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_90;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_5_0_1;
  reg [10-1:0] _tmp_91;
  reg [32-1:0] _tmp_92;
  reg [32-1:0] _tmp_93;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_94;
  reg [33-1:0] _tmp_95;
  reg [33-1:0] _tmp_96;
  reg [32-1:0] _tmp_97;
  reg _tmp_98;
  reg [33-1:0] _tmp_99;
  reg _tmp_100;
  wire [32-1:0] _tmp_data_101;
  wire _tmp_valid_101;
  wire _tmp_ready_101;
  assign _tmp_ready_101 = (_tmp_99 > 0) && !_tmp_100;
  reg _ram_a_cond_1_1;
  reg [9-1:0] _tmp_102;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_103;
  reg __tmp_fsm_3_cond_5_1_1;
  reg [10-1:0] _tmp_104;
  reg [32-1:0] _tmp_105;
  reg [32-1:0] _tmp_106;
  reg [32-1:0] _tmp_fsm_4;
  localparam _tmp_fsm_4_init = 0;
  reg [32-1:0] _tmp_107;
  reg [33-1:0] _tmp_108;
  reg [33-1:0] _tmp_109;
  reg [32-1:0] _tmp_110;
  reg _tmp_111;
  reg [33-1:0] _tmp_112;
  reg _tmp_113;
  wire [32-1:0] _tmp_data_114;
  wire _tmp_valid_114;
  wire _tmp_ready_114;
  assign _tmp_ready_114 = (_tmp_112 > 0) && !_tmp_113;
  reg _ram_b_cond_1_1;
  reg [9-1:0] _tmp_115;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_1 == 4) || (_tmp_fsm_3 == 4) || (_tmp_fsm_4 == 4);
  reg [32-1:0] _d1__tmp_fsm_4;
  reg __tmp_fsm_4_cond_4_0_1;
  reg _tmp_116;
  reg __tmp_fsm_4_cond_5_1_1;
  reg [32-1:0] th_sequential;
  localparam th_sequential_init = 0;
  reg _th_sequential_called;
  reg signed [32-1:0] _th_sequential_offset_8;
  reg signed [32-1:0] _th_sequential_offset_9;
  reg signed [32-1:0] _th_sequential_sum_10;
  reg signed [32-1:0] _th_sequential_i_11;
  reg _tmp_117;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_3_2;
  reg signed [32-1:0] _tmp_118;
  reg signed [32-1:0] _th_sequential_a_12;
  reg _tmp_119;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_3_2;
  reg signed [32-1:0] _tmp_120;
  reg signed [32-1:0] _th_sequential_b_13;
  reg _ram_c_cond_1_1;
  reg [10-1:0] _tmp_121;
  reg [32-1:0] _tmp_122;
  reg [32-1:0] _tmp_123;
  reg [32-1:0] _tmp_fsm_5;
  localparam _tmp_fsm_5_init = 0;
  reg [32-1:0] _tmp_124;
  reg [33-1:0] _tmp_125;
  reg [33-1:0] _tmp_126;
  reg _tmp_127;
  reg _tmp_128;
  wire _tmp_129;
  wire _tmp_130;
  assign _tmp_130 = 1;
  localparam _tmp_131 = 1;
  wire [_tmp_131-1:0] _tmp_132;
  assign _tmp_132 = (_tmp_129 || !_tmp_127) && (_tmp_130 || !_tmp_128);
  reg [_tmp_131-1:0] __tmp_132_1;
  wire [32-1:0] _tmp_133;
  reg [32-1:0] __tmp_133_1;
  assign _tmp_133 = (__tmp_132_1)? ram_c_0_rdata : __tmp_133_1;
  reg _tmp_134;
  reg _tmp_135;
  reg _tmp_136;
  reg _tmp_137;
  reg [33-1:0] _tmp_138;
  reg [9-1:0] _tmp_139;
  reg _myaxi_cond_6_1;
  reg _tmp_140;
  wire [32-1:0] _tmp_data_141;
  wire _tmp_valid_141;
  wire _tmp_ready_141;
  assign _tmp_ready_141 = (_tmp_fsm_5 == 4) && ((_tmp_139 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_7_1;
  reg _tmp_142;
  reg [32-1:0] _d1__tmp_fsm_5;
  reg __tmp_fsm_5_cond_5_0_1;
  reg signed [32-1:0] _th_comp_offset_stream_14;
  reg signed [32-1:0] _th_comp_offset_seq_15;
  reg signed [32-1:0] _th_comp_all_ok_16;
  reg _tmp_143;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_144;
  reg signed [32-1:0] _th_comp_st_17;
  reg _tmp_145;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_146;
  reg signed [32-1:0] _th_comp_sq_18;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_11 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_24 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_87 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_88 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_102 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_115 <= 0;
      _myaxi_cond_5_1 <= 0;
      _tmp_139 <= 0;
      _myaxi_cond_6_1 <= 0;
      _tmp_140 <= 0;
      _myaxi_cond_7_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_88 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_5_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_6_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_7_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_140 <= 0;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_11 == 0))) begin
        myaxi_araddr <= _tmp_3;
        myaxi_arlen <= _tmp_4 - 1;
        myaxi_arvalid <= 1;
        _tmp_11 <= _tmp_4;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_11 > 0)) begin
        _tmp_11 <= _tmp_11 - 1;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_24 == 0))) begin
        myaxi_araddr <= _tmp_16;
        myaxi_arlen <= _tmp_17 - 1;
        myaxi_arvalid <= 1;
        _tmp_24 <= _tmp_17;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_24 > 0)) begin
        _tmp_24 <= _tmp_24 - 1;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_87 == 0))) begin
        myaxi_awaddr <= _tmp_72;
        myaxi_awlen <= _tmp_73 - 1;
        myaxi_awvalid <= 1;
        _tmp_87 <= _tmp_73;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_87 == 0)) && (_tmp_73 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_89 && ((_tmp_fsm_2 == 4) && ((_tmp_87 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_87 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_87 > 0))) begin
        myaxi_wdata <= _tmp_data_89;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_87 <= _tmp_87 - 1;
      end 
      if(_tmp_valid_89 && ((_tmp_fsm_2 == 4) && ((_tmp_87 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_87 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_87 > 0)) && (_tmp_87 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_88 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_88 <= _tmp_88;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_102 == 0))) begin
        myaxi_araddr <= _tmp_94;
        myaxi_arlen <= _tmp_95 - 1;
        myaxi_arvalid <= 1;
        _tmp_102 <= _tmp_95;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_102 > 0)) begin
        _tmp_102 <= _tmp_102 - 1;
      end 
      if((_tmp_fsm_4 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_115 == 0))) begin
        myaxi_araddr <= _tmp_107;
        myaxi_arlen <= _tmp_108 - 1;
        myaxi_arvalid <= 1;
        _tmp_115 <= _tmp_108;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_115 > 0)) begin
        _tmp_115 <= _tmp_115 - 1;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_139 == 0))) begin
        myaxi_awaddr <= _tmp_124;
        myaxi_awlen <= _tmp_125 - 1;
        myaxi_awvalid <= 1;
        _tmp_139 <= _tmp_125;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_139 == 0)) && (_tmp_125 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_6_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_141 && ((_tmp_fsm_5 == 4) && ((_tmp_139 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_139 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_139 > 0))) begin
        myaxi_wdata <= _tmp_data_141;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_139 <= _tmp_139 - 1;
      end 
      if(_tmp_valid_141 && ((_tmp_fsm_5 == 4) && ((_tmp_139 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_139 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_139 > 0)) && (_tmp_139 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_140 <= 1;
      end 
      _myaxi_cond_7_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_140 <= _tmp_140;
      end 
    end
  end

  assign _tmp_data_10 = _tmp_6;
  assign _tmp_valid_10 = _tmp_7;
  assign _tmp_data_23 = _tmp_19;
  assign _tmp_valid_23 = _tmp_20;
  assign _tmp_data_101 = _tmp_97;
  assign _tmp_valid_101 = _tmp_98;
  assign _tmp_data_114 = _tmp_110;
  assign _tmp_valid_114 = _tmp_111;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_8 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_9 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_31_1 <= 0;
      __tmp_32_1 <= 0;
      _tmp_36 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_33 <= 0;
      _tmp_37 <= 0;
      _tmp_42 <= 0;
      _tmp_43 <= 0;
      _tmp_40 <= 0;
      _tmp_44 <= 0;
      _tmp_41 <= 0;
      _tmp_99 <= 0;
      _tmp_100 <= 0;
      _ram_a_cond_1_1 <= 0;
      _ram_a_cond_2_1 <= 0;
      _tmp_117 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_3_2 <= 0;
    end else begin
      if(_ram_a_cond_3_2) begin
        _tmp_117 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_9 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        ram_a_0_wenable <= 0;
        _tmp_100 <= 0;
      end 
      if(_ram_a_cond_2_1) begin
        _tmp_117 <= 1;
      end 
      _ram_a_cond_3_2 <= _ram_a_cond_3_1;
      if((_tmp_fsm_0 == 1) && (_tmp_8 == 0)) begin
        ram_a_0_addr <= _tmp_0 - 1;
        _tmp_8 <= _tmp_2;
      end 
      if(_tmp_valid_10 && ((_tmp_8 > 0) && !_tmp_9) && (_tmp_8 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_10;
        ram_a_0_wenable <= 1;
        _tmp_8 <= _tmp_8 - 1;
      end 
      if(_tmp_valid_10 && ((_tmp_8 > 0) && !_tmp_9) && (_tmp_8 == 1)) begin
        _tmp_9 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
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
      if((_mystream_fsm_3 == 1) && !_tmp_37 && !_tmp_35 && !_tmp_36) begin
        ram_a_0_addr <= _mystream_offset_1;
        _tmp_37 <= 1;
        _tmp_33 <= 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37) begin
        ram_a_0_addr <= _tmp_38;
        _tmp_33 <= 1;
        _tmp_35 <= 0;
      end 
      if((_mystream_fsm_3 == 1) && !_tmp_37 && !_tmp_35 && !_tmp_36) begin
        _tmp_42 <= 7;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37) begin
        _tmp_42 <= _tmp_42 - 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && (_tmp_42 == 0)) begin
        _tmp_42 <= 7;
      end 
      if((_mystream_fsm_3 == 1) && !_tmp_37 && !_tmp_35 && !_tmp_36) begin
        _tmp_43 <= 3;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && (_tmp_42 == 0)) begin
        _tmp_43 <= _tmp_43 - 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && (_tmp_42 == 0) && (_tmp_43 == 0)) begin
        _tmp_43 <= 3;
      end 
      if((_mystream_fsm_3 == 1) && !_tmp_37 && !_tmp_35 && !_tmp_36) begin
        _tmp_40 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && (_tmp_42 == 1) && !0) begin
        _tmp_40 <= _tmp_40 + 16;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && (_tmp_42 == 1) && (_tmp_43 == 0)) begin
        _tmp_40 <= 0;
      end 
      if((_mystream_fsm_3 == 1) && !_tmp_37 && !_tmp_35 && !_tmp_36) begin
        _tmp_44 <= 15;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && ((_tmp_42 == 0) && (_tmp_43 == 0))) begin
        _tmp_44 <= _tmp_44 - 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && ((_tmp_42 == 0) && (_tmp_43 == 0)) && (_tmp_44 == 0)) begin
        _tmp_44 <= 15;
      end 
      if((_mystream_fsm_3 == 1) && !_tmp_37 && !_tmp_35 && !_tmp_36) begin
        _tmp_41 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && ((_tmp_42 == 1) && (_tmp_43 == 0)) && !(0 && 0)) begin
        _tmp_41 <= _tmp_41 + 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && ((_tmp_42 == 1) && (_tmp_43 == 0)) && (_tmp_44 == 0)) begin
        _tmp_41 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_37 && ((_tmp_42 == 0) && (_tmp_43 == 0) && (_tmp_44 == 0))) begin
        _tmp_37 <= 0;
        _tmp_35 <= 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_99 == 0)) begin
        ram_a_0_addr <= _tmp_91 - 1;
        _tmp_99 <= _tmp_93;
      end 
      if(_tmp_valid_101 && ((_tmp_99 > 0) && !_tmp_100) && (_tmp_99 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_101;
        ram_a_0_wenable <= 1;
        _tmp_99 <= _tmp_99 - 1;
      end 
      if(_tmp_valid_101 && ((_tmp_99 > 0) && !_tmp_100) && (_tmp_99 == 1)) begin
        _tmp_100 <= 1;
      end 
      _ram_a_cond_1_1 <= 1;
      if(th_sequential == 5) begin
        ram_a_0_addr <= _th_sequential_i_11 + _th_sequential_offset_9;
      end 
      _ram_a_cond_2_1 <= th_sequential == 5;
      _ram_a_cond_3_1 <= th_sequential == 5;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_21 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_22 <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_50_1 <= 0;
      __tmp_51_1 <= 0;
      _tmp_55 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_52 <= 0;
      _tmp_56 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_59 <= 0;
      _tmp_63 <= 0;
      _tmp_60 <= 0;
      _tmp_112 <= 0;
      _tmp_113 <= 0;
      _ram_b_cond_1_1 <= 0;
      _ram_b_cond_2_1 <= 0;
      _tmp_119 <= 0;
      _ram_b_cond_3_1 <= 0;
      _ram_b_cond_3_2 <= 0;
    end else begin
      if(_ram_b_cond_3_2) begin
        _tmp_119 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_22 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        ram_b_0_wenable <= 0;
        _tmp_113 <= 0;
      end 
      if(_ram_b_cond_2_1) begin
        _tmp_119 <= 1;
      end 
      _ram_b_cond_3_2 <= _ram_b_cond_3_1;
      if((_tmp_fsm_1 == 1) && (_tmp_21 == 0)) begin
        ram_b_0_addr <= _tmp_13 - 1;
        _tmp_21 <= _tmp_15;
      end 
      if(_tmp_valid_23 && ((_tmp_21 > 0) && !_tmp_22) && (_tmp_21 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_23;
        ram_b_0_wenable <= 1;
        _tmp_21 <= _tmp_21 - 1;
      end 
      if(_tmp_valid_23 && ((_tmp_21 > 0) && !_tmp_22) && (_tmp_21 == 1)) begin
        _tmp_22 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
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
      if((_mystream_fsm_5 == 1) && !_tmp_56 && !_tmp_54 && !_tmp_55) begin
        ram_b_0_addr <= _mystream_offset_1;
        _tmp_56 <= 1;
        _tmp_52 <= 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56) begin
        ram_b_0_addr <= _tmp_57;
        _tmp_52 <= 1;
        _tmp_54 <= 0;
      end 
      if((_mystream_fsm_5 == 1) && !_tmp_56 && !_tmp_54 && !_tmp_55) begin
        _tmp_61 <= 7;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56) begin
        _tmp_61 <= _tmp_61 - 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && (_tmp_61 == 0)) begin
        _tmp_61 <= 7;
      end 
      if((_mystream_fsm_5 == 1) && !_tmp_56 && !_tmp_54 && !_tmp_55) begin
        _tmp_62 <= 3;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && (_tmp_61 == 0)) begin
        _tmp_62 <= _tmp_62 - 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && (_tmp_61 == 0) && (_tmp_62 == 0)) begin
        _tmp_62 <= 3;
      end 
      if((_mystream_fsm_5 == 1) && !_tmp_56 && !_tmp_54 && !_tmp_55) begin
        _tmp_59 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && (_tmp_61 == 1) && !0) begin
        _tmp_59 <= _tmp_59 + 16;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && (_tmp_61 == 1) && (_tmp_62 == 0)) begin
        _tmp_59 <= 0;
      end 
      if((_mystream_fsm_5 == 1) && !_tmp_56 && !_tmp_54 && !_tmp_55) begin
        _tmp_63 <= 15;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && ((_tmp_61 == 0) && (_tmp_62 == 0))) begin
        _tmp_63 <= _tmp_63 - 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && ((_tmp_61 == 0) && (_tmp_62 == 0)) && (_tmp_63 == 0)) begin
        _tmp_63 <= 15;
      end 
      if((_mystream_fsm_5 == 1) && !_tmp_56 && !_tmp_54 && !_tmp_55) begin
        _tmp_60 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && ((_tmp_61 == 1) && (_tmp_62 == 0)) && !(0 && 0)) begin
        _tmp_60 <= _tmp_60 + 1;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && ((_tmp_61 == 1) && (_tmp_62 == 0)) && (_tmp_63 == 0)) begin
        _tmp_60 <= 0;
      end 
      if((_tmp_47 || !_tmp_45) && (_tmp_48 || !_tmp_46) && _tmp_56 && ((_tmp_61 == 0) && (_tmp_62 == 0) && (_tmp_63 == 0))) begin
        _tmp_56 <= 0;
        _tmp_54 <= 1;
      end 
      if((_tmp_fsm_4 == 1) && (_tmp_112 == 0)) begin
        ram_b_0_addr <= _tmp_104 - 1;
        _tmp_112 <= _tmp_106;
      end 
      if(_tmp_valid_114 && ((_tmp_112 > 0) && !_tmp_113) && (_tmp_112 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_114;
        ram_b_0_wenable <= 1;
        _tmp_112 <= _tmp_112 - 1;
      end 
      if(_tmp_valid_114 && ((_tmp_112 > 0) && !_tmp_113) && (_tmp_112 == 1)) begin
        _tmp_113 <= 1;
      end 
      _ram_b_cond_1_1 <= 1;
      if(th_sequential == 7) begin
        ram_b_0_addr <= _th_sequential_i_11 + _th_sequential_offset_9;
      end 
      _ram_b_cond_2_1 <= th_sequential == 7;
      _ram_b_cond_3_1 <= th_sequential == 7;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_64 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_65 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_80_1 <= 0;
      __tmp_81_1 <= 0;
      _tmp_85 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_83 <= 0;
      _tmp_84 <= 0;
      _tmp_82 <= 0;
      _tmp_86 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_132_1 <= 0;
      __tmp_133_1 <= 0;
      _tmp_137 <= 0;
      _tmp_127 <= 0;
      _tmp_128 <= 0;
      _tmp_135 <= 0;
      _tmp_136 <= 0;
      _tmp_134 <= 0;
      _tmp_138 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_143 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_145 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_143 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_145 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_65 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_143 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_145 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if((_mystream_fsm_7 == 1) && (_tmp_64 == 0)) begin
        ram_c_0_addr <= _mystream_offset_1 - 1;
        _tmp_64 <= 1;
      end 
      if(_tmp_data_68 && (_tmp_valid_67 && ((_tmp_64 > 0) && !_tmp_65 && _tmp_all_valid_66)) && (_tmp_64 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_67;
        ram_c_0_wenable <= 1;
        _tmp_64 <= _tmp_64 - 1;
      end 
      if(_tmp_data_68 && (_tmp_valid_67 && ((_tmp_64 > 0) && !_tmp_65 && _tmp_all_valid_66)) && (_tmp_64 == 1)) begin
        _tmp_65 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_80_1 <= _tmp_80;
      __tmp_81_1 <= _tmp_81;
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && _tmp_83) begin
        _tmp_85 <= 0;
        _tmp_75 <= 0;
        _tmp_76 <= 0;
        _tmp_83 <= 0;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && _tmp_82) begin
        _tmp_75 <= 1;
        _tmp_76 <= 1;
        _tmp_85 <= _tmp_84;
        _tmp_84 <= 0;
        _tmp_82 <= 0;
        _tmp_83 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_86 == 0) && !_tmp_84 && !_tmp_85) begin
        ram_c_0_addr <= _tmp_69;
        _tmp_86 <= _tmp_71 - 1;
        _tmp_82 <= 1;
        _tmp_84 <= _tmp_71 == 1;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_86 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_86 <= _tmp_86 - 1;
        _tmp_82 <= 1;
        _tmp_84 <= 0;
      end 
      if((_tmp_77 || !_tmp_75) && (_tmp_78 || !_tmp_76) && (_tmp_86 == 1)) begin
        _tmp_84 <= 1;
      end 
      if(th_sequential == 11) begin
        ram_c_0_addr <= _th_sequential_offset_9;
        ram_c_0_wdata <= _th_sequential_sum_10;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_sequential == 11;
      __tmp_132_1 <= _tmp_132;
      __tmp_133_1 <= _tmp_133;
      if((_tmp_129 || !_tmp_127) && (_tmp_130 || !_tmp_128) && _tmp_135) begin
        _tmp_137 <= 0;
        _tmp_127 <= 0;
        _tmp_128 <= 0;
        _tmp_135 <= 0;
      end 
      if((_tmp_129 || !_tmp_127) && (_tmp_130 || !_tmp_128) && _tmp_134) begin
        _tmp_127 <= 1;
        _tmp_128 <= 1;
        _tmp_137 <= _tmp_136;
        _tmp_136 <= 0;
        _tmp_134 <= 0;
        _tmp_135 <= 1;
      end 
      if((_tmp_fsm_5 == 1) && (_tmp_138 == 0) && !_tmp_136 && !_tmp_137) begin
        ram_c_0_addr <= _tmp_121;
        _tmp_138 <= _tmp_123 - 1;
        _tmp_134 <= 1;
        _tmp_136 <= _tmp_123 == 1;
      end 
      if((_tmp_129 || !_tmp_127) && (_tmp_130 || !_tmp_128) && (_tmp_138 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_138 <= _tmp_138 - 1;
        _tmp_134 <= 1;
        _tmp_136 <= 0;
      end 
      if((_tmp_129 || !_tmp_127) && (_tmp_130 || !_tmp_128) && (_tmp_138 == 1)) begin
        _tmp_136 <= 1;
      end 
      if(th_comp == 22) begin
        ram_c_0_addr <= _th_comp_offset_stream_14;
      end 
      _ram_c_cond_2_1 <= th_comp == 22;
      _ram_c_cond_3_1 <= th_comp == 22;
      if(th_comp == 24) begin
        ram_c_0_addr <= _th_comp_offset_seq_15;
      end 
      _ram_c_cond_4_1 <= th_comp == 24;
      _ram_c_cond_5_1 <= th_comp == 24;
    end
  end

  assign _tmp_data_89 = _tmp_81;
  assign _tmp_valid_89 = _tmp_75;
  assign _tmp_77 = 1 && _tmp_ready_89;
  assign _tmp_data_141 = _tmp_133;
  assign _tmp_valid_141 = _tmp_127;
  assign _tmp_129 = 1 && _tmp_ready_141;
  reg [32-1:0] _tmp_data_147;
  reg _tmp_valid_147;
  wire _tmp_ready_147;
  wire [32-1:0] _tmp_data_148;
  wire _tmp_valid_148;
  wire _tmp_ready_148;
  wire [64-1:0] _tmp_odata_148;
  reg [64-1:0] _tmp_data_reg_148;
  assign _tmp_data_148 = _tmp_data_reg_148;
  wire _tmp_ovalid_148;
  reg _tmp_valid_reg_148;
  assign _tmp_valid_148 = _tmp_valid_reg_148;
  wire _tmp_enable_148;
  wire _tmp_update_148;
  assign _tmp_enable_148 = (_tmp_ready_148 || !_tmp_valid_148) && (_tmp_28 && _tmp_47) && (_tmp_26 && _tmp_45);
  assign _tmp_update_148 = _tmp_ready_148 || !_tmp_valid_148;

  multiplier_0
  mul148
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_148),
    .enable(_tmp_enable_148),
    .valid(_tmp_ovalid_148),
    .a(_tmp_32),
    .b(_tmp_51),
    .c(_tmp_odata_148)
  );

  assign _tmp_28 = 1 && ((_tmp_ready_148 || !_tmp_valid_148) && (_tmp_26 && _tmp_45));
  assign _tmp_47 = 1 && ((_tmp_ready_148 || !_tmp_valid_148) && (_tmp_26 && _tmp_45));
  reg [1-1:0] _tmp_data_149;
  reg _tmp_valid_149;
  wire _tmp_ready_149;
  assign _tmp_ready_147 = (_tmp_ready_149 || !_tmp_valid_149) && _tmp_valid_147;
  reg [1-1:0] _tmp_data_150;
  reg [1-1:0] _tmp_data_151;
  reg [1-1:0] _tmp_data_152;
  reg _tmp_valid_152;
  wire _tmp_ready_152;
  reg [1-1:0] _tmp_data_153;
  reg _tmp_valid_153;
  wire _tmp_ready_153;
  assign _tmp_ready_149 = (_tmp_ready_152 || !_tmp_valid_152) && _tmp_valid_149 && ((_tmp_ready_153 || !_tmp_valid_153) && _tmp_valid_149);
  reg [1-1:0] _tmp_data_154;
  reg _tmp_valid_154;
  wire _tmp_ready_154;
  assign _tmp_ready_152 = (_tmp_ready_154 || !_tmp_valid_154) && _tmp_valid_152;
  reg [1-1:0] _tmp_data_155;
  reg _tmp_valid_155;
  wire _tmp_ready_155;
  assign _tmp_ready_153 = (_tmp_ready_155 || !_tmp_valid_155) && _tmp_valid_153;
  reg [1-1:0] _tmp_data_156;
  reg _tmp_valid_156;
  wire _tmp_ready_156;
  assign _tmp_ready_154 = (_tmp_ready_156 || !_tmp_valid_156) && _tmp_valid_154;
  reg [1-1:0] _tmp_data_157;
  reg _tmp_valid_157;
  wire _tmp_ready_157;
  assign _tmp_ready_155 = (_tmp_ready_157 || !_tmp_valid_157) && _tmp_valid_155;
  reg [1-1:0] _tmp_data_158;
  reg _tmp_valid_158;
  wire _tmp_ready_158;
  assign _tmp_ready_156 = (_tmp_ready_158 || !_tmp_valid_158) && _tmp_valid_156;
  reg [1-1:0] _tmp_data_159;
  reg _tmp_valid_159;
  wire _tmp_ready_159;
  assign _tmp_ready_157 = (_tmp_ready_159 || !_tmp_valid_159) && _tmp_valid_157;
  reg [1-1:0] _tmp_data_160;
  reg _tmp_valid_160;
  wire _tmp_ready_160;
  assign _tmp_ready_158 = (_tmp_ready_160 || !_tmp_valid_160) && _tmp_valid_158;
  reg [1-1:0] _tmp_data_161;
  reg _tmp_valid_161;
  wire _tmp_ready_161;
  assign _tmp_ready_159 = (_tmp_ready_161 || !_tmp_valid_161) && _tmp_valid_159;
  reg [1-1:0] _tmp_data_162;
  reg _tmp_valid_162;
  wire _tmp_ready_162;
  assign _tmp_ready_160 = (_tmp_ready_162 || !_tmp_valid_162) && _tmp_valid_160;
  reg [1-1:0] _tmp_data_163;
  reg _tmp_valid_163;
  wire _tmp_ready_163;
  assign _tmp_ready_161 = (_tmp_ready_163 || !_tmp_valid_163) && _tmp_valid_161;
  reg [32-1:0] _tmp_data_164;
  reg _tmp_valid_164;
  wire _tmp_ready_164;
  assign _tmp_ready_148 = (_tmp_ready_164 || !_tmp_valid_164) && (_tmp_valid_148 && _tmp_valid_162);
  assign _tmp_ready_162 = (_tmp_ready_164 || !_tmp_valid_164) && (_tmp_valid_148 && _tmp_valid_162);
  reg [1-1:0] _tmp_data_165;
  reg _tmp_valid_165;
  wire _tmp_ready_165;
  assign _tmp_ready_163 = (_tmp_ready_165 || !_tmp_valid_165) && _tmp_valid_163;
  assign _tmp_data_67 = _tmp_data_164;
  assign _tmp_valid_67 = _tmp_valid_164;
  assign _tmp_ready_164 = _tmp_ready_67;
  assign _tmp_data_68 = _tmp_data_165;
  assign _tmp_valid_68 = _tmp_valid_165;
  assign _tmp_ready_165 = _tmp_ready_68;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_147 <= 1'sd0;
      _tmp_valid_147 <= 0;
      _tmp_data_reg_148 <= 0;
      _tmp_valid_reg_148 <= 0;
      _tmp_data_149 <= 0;
      _tmp_valid_149 <= 0;
      _tmp_data_150 <= 0;
      _tmp_data_151 <= 0;
      _tmp_data_152 <= 0;
      _tmp_valid_152 <= 0;
      _tmp_data_153 <= 0;
      _tmp_valid_153 <= 0;
      _tmp_data_154 <= 0;
      _tmp_valid_154 <= 0;
      _tmp_data_155 <= 0;
      _tmp_valid_155 <= 0;
      _tmp_data_156 <= 0;
      _tmp_valid_156 <= 0;
      _tmp_data_157 <= 0;
      _tmp_valid_157 <= 0;
      _tmp_data_158 <= 0;
      _tmp_valid_158 <= 0;
      _tmp_data_159 <= 0;
      _tmp_valid_159 <= 0;
      _tmp_data_160 <= 0;
      _tmp_valid_160 <= 0;
      _tmp_data_161 <= 0;
      _tmp_valid_161 <= 0;
      _tmp_data_162 <= 0;
      _tmp_valid_162 <= 0;
      _tmp_data_163 <= 0;
      _tmp_valid_163 <= 0;
      _tmp_data_164 <= 1'sd0;
      _tmp_valid_164 <= 0;
      _tmp_data_165 <= 0;
      _tmp_valid_165 <= 0;
    end else begin
      if((_tmp_ready_147 || !_tmp_valid_147) && 1 && 1) begin
        _tmp_data_147 <= (_tmp_data_147 >= 511)? 0 : _tmp_data_147 + 2'sd1;
      end 
      if(_tmp_valid_147 && _tmp_ready_147) begin
        _tmp_valid_147 <= 0;
      end 
      if((_tmp_ready_147 || !_tmp_valid_147) && 1) begin
        _tmp_valid_147 <= 1;
      end 
      if(_tmp_ready_148 || !_tmp_valid_148) begin
        _tmp_data_reg_148 <= _tmp_odata_148;
      end 
      if(_tmp_ready_148 || !_tmp_valid_148) begin
        _tmp_valid_reg_148 <= _tmp_ovalid_148;
      end 
      if((_tmp_ready_149 || !_tmp_valid_149) && _tmp_ready_147 && _tmp_valid_147) begin
        _tmp_data_149 <= _tmp_data_147 == 10'sd511;
      end 
      if(_tmp_valid_149 && _tmp_ready_149) begin
        _tmp_valid_149 <= 0;
      end 
      if((_tmp_ready_149 || !_tmp_valid_149) && _tmp_ready_147) begin
        _tmp_valid_149 <= _tmp_valid_147;
      end 
      if(_tmp_valid_149 && _tmp_ready_149) begin
        _tmp_data_150 <= _tmp_data_149;
      end 
      if(_tmp_valid_149 && _tmp_ready_149) begin
        _tmp_data_151 <= _tmp_data_150;
      end 
      if((_tmp_ready_152 || !_tmp_valid_152) && _tmp_ready_149 && _tmp_valid_149) begin
        _tmp_data_152 <= _tmp_data_151;
      end 
      if(_tmp_valid_152 && _tmp_ready_152) begin
        _tmp_valid_152 <= 0;
      end 
      if((_tmp_ready_152 || !_tmp_valid_152) && _tmp_ready_149) begin
        _tmp_valid_152 <= _tmp_valid_149;
      end 
      if((_tmp_ready_153 || !_tmp_valid_153) && _tmp_ready_149 && _tmp_valid_149) begin
        _tmp_data_153 <= _tmp_data_150;
      end 
      if(_tmp_valid_153 && _tmp_ready_153) begin
        _tmp_valid_153 <= 0;
      end 
      if((_tmp_ready_153 || !_tmp_valid_153) && _tmp_ready_149) begin
        _tmp_valid_153 <= _tmp_valid_149;
      end 
      if((_tmp_ready_154 || !_tmp_valid_154) && _tmp_ready_152 && _tmp_valid_152) begin
        _tmp_data_154 <= _tmp_data_152;
      end 
      if(_tmp_valid_154 && _tmp_ready_154) begin
        _tmp_valid_154 <= 0;
      end 
      if((_tmp_ready_154 || !_tmp_valid_154) && _tmp_ready_152) begin
        _tmp_valid_154 <= _tmp_valid_152;
      end 
      if((_tmp_ready_155 || !_tmp_valid_155) && _tmp_ready_153 && _tmp_valid_153) begin
        _tmp_data_155 <= _tmp_data_153;
      end 
      if(_tmp_valid_155 && _tmp_ready_155) begin
        _tmp_valid_155 <= 0;
      end 
      if((_tmp_ready_155 || !_tmp_valid_155) && _tmp_ready_153) begin
        _tmp_valid_155 <= _tmp_valid_153;
      end 
      if((_tmp_ready_156 || !_tmp_valid_156) && _tmp_ready_154 && _tmp_valid_154) begin
        _tmp_data_156 <= _tmp_data_154;
      end 
      if(_tmp_valid_156 && _tmp_ready_156) begin
        _tmp_valid_156 <= 0;
      end 
      if((_tmp_ready_156 || !_tmp_valid_156) && _tmp_ready_154) begin
        _tmp_valid_156 <= _tmp_valid_154;
      end 
      if((_tmp_ready_157 || !_tmp_valid_157) && _tmp_ready_155 && _tmp_valid_155) begin
        _tmp_data_157 <= _tmp_data_155;
      end 
      if(_tmp_valid_157 && _tmp_ready_157) begin
        _tmp_valid_157 <= 0;
      end 
      if((_tmp_ready_157 || !_tmp_valid_157) && _tmp_ready_155) begin
        _tmp_valid_157 <= _tmp_valid_155;
      end 
      if((_tmp_ready_158 || !_tmp_valid_158) && _tmp_ready_156 && _tmp_valid_156) begin
        _tmp_data_158 <= _tmp_data_156;
      end 
      if(_tmp_valid_158 && _tmp_ready_158) begin
        _tmp_valid_158 <= 0;
      end 
      if((_tmp_ready_158 || !_tmp_valid_158) && _tmp_ready_156) begin
        _tmp_valid_158 <= _tmp_valid_156;
      end 
      if((_tmp_ready_159 || !_tmp_valid_159) && _tmp_ready_157 && _tmp_valid_157) begin
        _tmp_data_159 <= _tmp_data_157;
      end 
      if(_tmp_valid_159 && _tmp_ready_159) begin
        _tmp_valid_159 <= 0;
      end 
      if((_tmp_ready_159 || !_tmp_valid_159) && _tmp_ready_157) begin
        _tmp_valid_159 <= _tmp_valid_157;
      end 
      if((_tmp_ready_160 || !_tmp_valid_160) && _tmp_ready_158 && _tmp_valid_158) begin
        _tmp_data_160 <= _tmp_data_158;
      end 
      if(_tmp_valid_160 && _tmp_ready_160) begin
        _tmp_valid_160 <= 0;
      end 
      if((_tmp_ready_160 || !_tmp_valid_160) && _tmp_ready_158) begin
        _tmp_valid_160 <= _tmp_valid_158;
      end 
      if((_tmp_ready_161 || !_tmp_valid_161) && _tmp_ready_159 && _tmp_valid_159) begin
        _tmp_data_161 <= _tmp_data_159;
      end 
      if(_tmp_valid_161 && _tmp_ready_161) begin
        _tmp_valid_161 <= 0;
      end 
      if((_tmp_ready_161 || !_tmp_valid_161) && _tmp_ready_159) begin
        _tmp_valid_161 <= _tmp_valid_159;
      end 
      if((_tmp_ready_162 || !_tmp_valid_162) && _tmp_ready_160 && _tmp_valid_160) begin
        _tmp_data_162 <= _tmp_data_160;
      end 
      if(_tmp_valid_162 && _tmp_ready_162) begin
        _tmp_valid_162 <= 0;
      end 
      if((_tmp_ready_162 || !_tmp_valid_162) && _tmp_ready_160) begin
        _tmp_valid_162 <= _tmp_valid_160;
      end 
      if((_tmp_ready_163 || !_tmp_valid_163) && _tmp_ready_161 && _tmp_valid_161) begin
        _tmp_data_163 <= _tmp_data_161;
      end 
      if(_tmp_valid_163 && _tmp_ready_163) begin
        _tmp_valid_163 <= 0;
      end 
      if((_tmp_ready_163 || !_tmp_valid_163) && _tmp_ready_161) begin
        _tmp_valid_163 <= _tmp_valid_161;
      end 
      if((_tmp_ready_164 || !_tmp_valid_164) && (_tmp_ready_148 && _tmp_ready_162) && (_tmp_valid_148 && _tmp_valid_162)) begin
        _tmp_data_164 <= _tmp_data_164 + _tmp_data_148;
      end 
      if(_tmp_valid_164 && _tmp_ready_164) begin
        _tmp_valid_164 <= 0;
      end 
      if((_tmp_ready_164 || !_tmp_valid_164) && (_tmp_ready_148 && _tmp_ready_162)) begin
        _tmp_valid_164 <= _tmp_valid_148 && _tmp_valid_162;
      end 
      if((_tmp_ready_164 || !_tmp_valid_164) && (_tmp_ready_148 && _tmp_ready_162) && (_tmp_valid_148 && _tmp_valid_162) && _tmp_data_162) begin
        _tmp_data_164 <= 1'sd0 + _tmp_data_148;
      end 
      if((_tmp_ready_165 || !_tmp_valid_165) && _tmp_ready_163 && _tmp_valid_163) begin
        _tmp_data_165 <= _tmp_data_163;
      end 
      if(_tmp_valid_165 && _tmp_ready_165) begin
        _tmp_valid_165 <= 0;
      end 
      if((_tmp_ready_165 || !_tmp_valid_165) && _tmp_ready_163) begin
        _tmp_valid_165 <= _tmp_valid_163;
      end 
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_offset_0 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_69 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_91 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 0;
      _tmp_104 <= 0;
      _tmp_105 <= 0;
      _tmp_106 <= 0;
      _tmp_121 <= 0;
      _tmp_122 <= 0;
      _tmp_123 <= 0;
      _th_comp_offset_stream_14 <= 0;
      _th_comp_offset_seq_15 <= 0;
      _th_comp_all_ok_16 <= 0;
      _tmp_144 <= 0;
      _th_comp_st_17 <= 0;
      _tmp_146 <= 0;
      _th_comp_sq_18 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_offset_0 <= 0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          _tmp_0 <= _th_comp_offset_0;
          _tmp_1 <= 0;
          _tmp_2 <= 512;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          if(_tmp_12) begin
            th_comp <= th_comp_4;
          end 
        end
        th_comp_4: begin
          _tmp_13 <= _th_comp_offset_0;
          _tmp_14 <= 0;
          _tmp_15 <= 512;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          if(_tmp_25) begin
            th_comp <= th_comp_6;
          end 
        end
        th_comp_6: begin
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if(_mystream_flag_2 && _mystream_flag_4 && _mystream_flag_6) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          _tmp_69 <= _th_comp_offset_0;
          _tmp_70 <= 4096;
          _tmp_71 <= 1;
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if(_tmp_90) begin
            th_comp <= th_comp_11;
          end 
        end
        th_comp_11: begin
          _th_comp_offset_0 <= 512;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          _tmp_91 <= _th_comp_offset_0;
          _tmp_92 <= 0;
          _tmp_93 <= 512;
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          if(_tmp_103) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          _tmp_104 <= _th_comp_offset_0;
          _tmp_105 <= 0;
          _tmp_106 <= 512;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(_tmp_116) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          if(th_sequential == 12) begin
            th_comp <= th_comp_18;
          end 
        end
        th_comp_18: begin
          _tmp_121 <= _th_comp_offset_0;
          _tmp_122 <= 8192;
          _tmp_123 <= 1;
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(_tmp_142) begin
            th_comp <= th_comp_20;
          end 
        end
        th_comp_20: begin
          _th_comp_offset_stream_14 <= 0;
          _th_comp_offset_seq_15 <= _th_comp_offset_0;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          _th_comp_all_ok_16 <= 1;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          if(_tmp_143) begin
            _tmp_144 <= ram_c_0_rdata;
          end 
          if(_tmp_143) begin
            th_comp <= th_comp_23;
          end 
        end
        th_comp_23: begin
          _th_comp_st_17 <= _tmp_144;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          if(_tmp_145) begin
            _tmp_146 <= ram_c_0_rdata;
          end 
          if(_tmp_145) begin
            th_comp <= th_comp_25;
          end 
        end
        th_comp_25: begin
          _th_comp_sq_18 <= _tmp_146;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          if(_th_comp_st_17 !== _th_comp_sq_18) begin
            th_comp <= th_comp_27;
          end else begin
            th_comp <= th_comp_28;
          end
        end
        th_comp_27: begin
          _th_comp_all_ok_16 <= 0;
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          if(_th_comp_all_ok_16) begin
            th_comp <= th_comp_29;
          end else begin
            th_comp <= th_comp_31;
          end
        end
        th_comp_29: begin
          $display("OK");
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          th_comp <= th_comp_32;
        end
        th_comp_31: begin
          $display("NG");
          th_comp <= th_comp_32;
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
      _tmp_3 <= 0;
      _tmp_5 <= 0;
      _tmp_4 <= 0;
      __tmp_fsm_0_cond_4_0_1 <= 0;
      _tmp_7 <= 0;
      _tmp_6 <= 0;
      _tmp_12 <= 0;
      __tmp_fsm_0_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_4: begin
          if(__tmp_fsm_0_cond_4_0_1) begin
            _tmp_7 <= 0;
          end 
        end
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_1_1) begin
            _tmp_12 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_comp == 3) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          _tmp_3 <= (_tmp_1 >> 2) << 2;
          _tmp_5 <= _tmp_2;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          if((_tmp_5 <= 256) && ((_tmp_3 & 4095) + (_tmp_5 << 2) >= 4096)) begin
            _tmp_4 <= 4096 - (_tmp_3 & 4095) >> 2;
            _tmp_5 <= _tmp_5 - (4096 - (_tmp_3 & 4095) >> 2);
          end else if(_tmp_5 <= 256) begin
            _tmp_4 <= _tmp_5;
            _tmp_5 <= 0;
          end else if((_tmp_3 & 4095) + 1024 >= 4096) begin
            _tmp_4 <= 4096 - (_tmp_3 & 4095) >> 2;
            _tmp_5 <= _tmp_5 - (4096 - (_tmp_3 & 4095) >> 2);
          end else begin
            _tmp_4 <= 256;
            _tmp_5 <= _tmp_5 - 256;
          end
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_4;
          end 
        end
        _tmp_fsm_0_4: begin
          __tmp_fsm_0_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_6 <= myaxi_rdata;
            _tmp_7 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_3 <= _tmp_3 + (_tmp_4 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_5 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_5 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_12 <= 1;
          __tmp_fsm_0_cond_5_1_1 <= 1;
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
      _tmp_16 <= 0;
      _tmp_18 <= 0;
      _tmp_17 <= 0;
      __tmp_fsm_1_cond_4_0_1 <= 0;
      _tmp_20 <= 0;
      _tmp_19 <= 0;
      _tmp_25 <= 0;
      __tmp_fsm_1_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_4: begin
          if(__tmp_fsm_1_cond_4_0_1) begin
            _tmp_20 <= 0;
          end 
        end
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_1_1) begin
            _tmp_25 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_comp == 5) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_16 <= (_tmp_14 >> 2) << 2;
          _tmp_18 <= _tmp_15;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_18 <= 256) && ((_tmp_16 & 4095) + (_tmp_18 << 2) >= 4096)) begin
            _tmp_17 <= 4096 - (_tmp_16 & 4095) >> 2;
            _tmp_18 <= _tmp_18 - (4096 - (_tmp_16 & 4095) >> 2);
          end else if(_tmp_18 <= 256) begin
            _tmp_17 <= _tmp_18;
            _tmp_18 <= 0;
          end else if((_tmp_16 & 4095) + 1024 >= 4096) begin
            _tmp_17 <= 4096 - (_tmp_16 & 4095) >> 2;
            _tmp_18 <= _tmp_18 - (4096 - (_tmp_16 & 4095) >> 2);
          end else begin
            _tmp_17 <= 256;
            _tmp_18 <= _tmp_18 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          __tmp_fsm_1_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_19 <= myaxi_rdata;
            _tmp_20 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_16 <= _tmp_16 + (_tmp_17 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_18 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_18 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_25 <= 1;
          __tmp_fsm_1_cond_5_1_1 <= 1;
          _tmp_fsm_1 <= _tmp_fsm_1_6;
        end
        _tmp_fsm_1_6: begin
          _tmp_fsm_1 <= _tmp_fsm_1_init;
        end
      endcase
    end
  end

  localparam mystream_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      mystream <= mystream_init;
      _mystream_start_cond <= 0;
      _mystream_called <= 0;
      _mystream_offset_1 <= 0;
    end else begin
      case(mystream)
        mystream_init: begin
          if(th_comp == 6) begin
            _mystream_start_cond <= 1;
          end 
          if(th_comp == 6) begin
            _mystream_called <= 1;
          end 
          if(th_comp == 6) begin
            _mystream_offset_1 <= _th_comp_offset_0;
          end 
          if(th_comp == 6) begin
            mystream <= mystream_1;
          end 
        end
        mystream_1: begin
          _mystream_start_cond <= 0;
          mystream <= mystream_init;
        end
      endcase
    end
  end

  localparam _mystream_fsm_3_1 = 1;
  localparam _mystream_fsm_3_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_3 <= _mystream_fsm_3_init;
      _mystream_flag_2 <= 0;
    end else begin
      case(_mystream_fsm_3)
        _mystream_fsm_3_init: begin
          if(_mystream_start_cond) begin
            _mystream_flag_2 <= 0;
          end 
          if(_mystream_start_cond) begin
            _mystream_fsm_3 <= _mystream_fsm_3_1;
          end 
        end
        _mystream_fsm_3_1: begin
          _mystream_fsm_3 <= _mystream_fsm_3_2;
        end
        _mystream_fsm_3_2: begin
          if(_tmp_36) begin
            _mystream_flag_2 <= 1;
          end 
          if(_tmp_36) begin
            _mystream_fsm_3 <= _mystream_fsm_3_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_5_1 = 1;
  localparam _mystream_fsm_5_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_5 <= _mystream_fsm_5_init;
      _mystream_flag_4 <= 0;
    end else begin
      case(_mystream_fsm_5)
        _mystream_fsm_5_init: begin
          if(_mystream_start_cond) begin
            _mystream_flag_4 <= 0;
          end 
          if(_mystream_start_cond) begin
            _mystream_fsm_5 <= _mystream_fsm_5_1;
          end 
        end
        _mystream_fsm_5_1: begin
          _mystream_fsm_5 <= _mystream_fsm_5_2;
        end
        _mystream_fsm_5_2: begin
          if(_tmp_55) begin
            _mystream_flag_4 <= 1;
          end 
          if(_tmp_55) begin
            _mystream_fsm_5 <= _mystream_fsm_5_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_7_1 = 1;
  localparam _mystream_fsm_7_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_7 <= _mystream_fsm_7_init;
      _mystream_flag_6 <= 0;
    end else begin
      case(_mystream_fsm_7)
        _mystream_fsm_7_init: begin
          if(_mystream_start_cond) begin
            _mystream_flag_6 <= 0;
          end 
          if(_mystream_start_cond) begin
            _mystream_fsm_7 <= _mystream_fsm_7_1;
          end 
        end
        _mystream_fsm_7_1: begin
          _mystream_fsm_7 <= _mystream_fsm_7_2;
        end
        _mystream_fsm_7_2: begin
          if(_tmp_65) begin
            _mystream_flag_6 <= 1;
          end 
          if(_tmp_65) begin
            _mystream_fsm_7 <= _mystream_fsm_7_init;
          end 
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
      _tmp_72 <= 0;
      _tmp_74 <= 0;
      _tmp_73 <= 0;
      _tmp_90 <= 0;
      __tmp_fsm_2_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_0_1) begin
            _tmp_90 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_comp == 10) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_72 <= (_tmp_70 >> 2) << 2;
          _tmp_74 <= _tmp_71;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_74 <= 256) && ((_tmp_72 & 4095) + (_tmp_74 << 2) >= 4096)) begin
            _tmp_73 <= 4096 - (_tmp_72 & 4095) >> 2;
            _tmp_74 <= _tmp_74 - (4096 - (_tmp_72 & 4095) >> 2);
          end else if(_tmp_74 <= 256) begin
            _tmp_73 <= _tmp_74;
            _tmp_74 <= 0;
          end else if((_tmp_72 & 4095) + 1024 >= 4096) begin
            _tmp_73 <= 4096 - (_tmp_72 & 4095) >> 2;
            _tmp_74 <= _tmp_74 - (4096 - (_tmp_72 & 4095) >> 2);
          end else begin
            _tmp_73 <= 256;
            _tmp_74 <= _tmp_74 - 256;
          end
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_4;
          end 
        end
        _tmp_fsm_2_4: begin
          if(_tmp_88 && myaxi_wvalid && myaxi_wready) begin
            _tmp_72 <= _tmp_72 + (_tmp_73 << 2);
          end 
          if(_tmp_88 && myaxi_wvalid && myaxi_wready && (_tmp_74 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(_tmp_88 && myaxi_wvalid && myaxi_wready && (_tmp_74 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_90 <= 1;
          __tmp_fsm_2_cond_5_0_1 <= 1;
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
      _tmp_94 <= 0;
      _tmp_96 <= 0;
      _tmp_95 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_98 <= 0;
      _tmp_97 <= 0;
      _tmp_103 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_98 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_103 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_comp == 13) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_94 <= (_tmp_92 >> 2) << 2;
          _tmp_96 <= _tmp_93;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_96 <= 256) && ((_tmp_94 & 4095) + (_tmp_96 << 2) >= 4096)) begin
            _tmp_95 <= 4096 - (_tmp_94 & 4095) >> 2;
            _tmp_96 <= _tmp_96 - (4096 - (_tmp_94 & 4095) >> 2);
          end else if(_tmp_96 <= 256) begin
            _tmp_95 <= _tmp_96;
            _tmp_96 <= 0;
          end else if((_tmp_94 & 4095) + 1024 >= 4096) begin
            _tmp_95 <= 4096 - (_tmp_94 & 4095) >> 2;
            _tmp_96 <= _tmp_96 - (4096 - (_tmp_94 & 4095) >> 2);
          end else begin
            _tmp_95 <= 256;
            _tmp_96 <= _tmp_96 - 256;
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
            _tmp_97 <= myaxi_rdata;
            _tmp_98 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_94 <= _tmp_94 + (_tmp_95 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_96 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_96 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_103 <= 1;
          __tmp_fsm_3_cond_5_1_1 <= 1;
          _tmp_fsm_3 <= _tmp_fsm_3_6;
        end
        _tmp_fsm_3_6: begin
          _tmp_fsm_3 <= _tmp_fsm_3_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_4_1 = 1;
  localparam _tmp_fsm_4_2 = 2;
  localparam _tmp_fsm_4_3 = 3;
  localparam _tmp_fsm_4_4 = 4;
  localparam _tmp_fsm_4_5 = 5;
  localparam _tmp_fsm_4_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_4 <= _tmp_fsm_4_init;
      _d1__tmp_fsm_4 <= _tmp_fsm_4_init;
      _tmp_107 <= 0;
      _tmp_109 <= 0;
      _tmp_108 <= 0;
      __tmp_fsm_4_cond_4_0_1 <= 0;
      _tmp_111 <= 0;
      _tmp_110 <= 0;
      _tmp_116 <= 0;
      __tmp_fsm_4_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_4 <= _tmp_fsm_4;
      case(_d1__tmp_fsm_4)
        _tmp_fsm_4_4: begin
          if(__tmp_fsm_4_cond_4_0_1) begin
            _tmp_111 <= 0;
          end 
        end
        _tmp_fsm_4_5: begin
          if(__tmp_fsm_4_cond_5_1_1) begin
            _tmp_116 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_4)
        _tmp_fsm_4_init: begin
          if(th_comp == 15) begin
            _tmp_fsm_4 <= _tmp_fsm_4_1;
          end 
        end
        _tmp_fsm_4_1: begin
          _tmp_107 <= (_tmp_105 >> 2) << 2;
          _tmp_109 <= _tmp_106;
          _tmp_fsm_4 <= _tmp_fsm_4_2;
        end
        _tmp_fsm_4_2: begin
          if((_tmp_109 <= 256) && ((_tmp_107 & 4095) + (_tmp_109 << 2) >= 4096)) begin
            _tmp_108 <= 4096 - (_tmp_107 & 4095) >> 2;
            _tmp_109 <= _tmp_109 - (4096 - (_tmp_107 & 4095) >> 2);
          end else if(_tmp_109 <= 256) begin
            _tmp_108 <= _tmp_109;
            _tmp_109 <= 0;
          end else if((_tmp_107 & 4095) + 1024 >= 4096) begin
            _tmp_108 <= 4096 - (_tmp_107 & 4095) >> 2;
            _tmp_109 <= _tmp_109 - (4096 - (_tmp_107 & 4095) >> 2);
          end else begin
            _tmp_108 <= 256;
            _tmp_109 <= _tmp_109 - 256;
          end
          _tmp_fsm_4 <= _tmp_fsm_4_3;
        end
        _tmp_fsm_4_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_4 <= _tmp_fsm_4_4;
          end 
        end
        _tmp_fsm_4_4: begin
          __tmp_fsm_4_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_110 <= myaxi_rdata;
            _tmp_111 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_107 <= _tmp_107 + (_tmp_108 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_109 > 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_109 == 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_5;
          end 
        end
        _tmp_fsm_4_5: begin
          _tmp_116 <= 1;
          __tmp_fsm_4_cond_5_1_1 <= 1;
          _tmp_fsm_4 <= _tmp_fsm_4_6;
        end
        _tmp_fsm_4_6: begin
          _tmp_fsm_4 <= _tmp_fsm_4_init;
        end
      endcase
    end
  end

  localparam th_sequential_1 = 1;
  localparam th_sequential_2 = 2;
  localparam th_sequential_3 = 3;
  localparam th_sequential_4 = 4;
  localparam th_sequential_5 = 5;
  localparam th_sequential_6 = 6;
  localparam th_sequential_7 = 7;
  localparam th_sequential_8 = 8;
  localparam th_sequential_9 = 9;
  localparam th_sequential_10 = 10;
  localparam th_sequential_11 = 11;
  localparam th_sequential_12 = 12;

  always @(posedge CLK) begin
    if(RST) begin
      th_sequential <= th_sequential_init;
      _th_sequential_called <= 0;
      _th_sequential_offset_8 <= 0;
      _th_sequential_offset_9 <= 0;
      _th_sequential_sum_10 <= 0;
      _th_sequential_i_11 <= 0;
      _tmp_118 <= 0;
      _th_sequential_a_12 <= 0;
      _tmp_120 <= 0;
      _th_sequential_b_13 <= 0;
    end else begin
      case(th_sequential)
        th_sequential_init: begin
          if(th_comp == 16) begin
            _th_sequential_called <= 1;
          end 
          if(th_comp == 16) begin
            _th_sequential_offset_8 <= _th_comp_offset_0;
          end 
          if(th_comp == 16) begin
            th_sequential <= th_sequential_1;
          end 
        end
        th_sequential_1: begin
          _th_sequential_offset_9 <= _th_sequential_offset_8;
          th_sequential <= th_sequential_2;
        end
        th_sequential_2: begin
          _th_sequential_sum_10 <= 0;
          th_sequential <= th_sequential_3;
        end
        th_sequential_3: begin
          _th_sequential_i_11 <= 0;
          th_sequential <= th_sequential_4;
        end
        th_sequential_4: begin
          if(_th_sequential_i_11 < 512) begin
            th_sequential <= th_sequential_5;
          end else begin
            th_sequential <= th_sequential_11;
          end
        end
        th_sequential_5: begin
          if(_tmp_117) begin
            _tmp_118 <= ram_a_0_rdata;
          end 
          if(_tmp_117) begin
            th_sequential <= th_sequential_6;
          end 
        end
        th_sequential_6: begin
          _th_sequential_a_12 <= _tmp_118;
          th_sequential <= th_sequential_7;
        end
        th_sequential_7: begin
          if(_tmp_119) begin
            _tmp_120 <= ram_b_0_rdata;
          end 
          if(_tmp_119) begin
            th_sequential <= th_sequential_8;
          end 
        end
        th_sequential_8: begin
          _th_sequential_b_13 <= _tmp_120;
          th_sequential <= th_sequential_9;
        end
        th_sequential_9: begin
          _th_sequential_sum_10 <= _th_sequential_sum_10 + _th_sequential_a_12 * _th_sequential_b_13;
          th_sequential <= th_sequential_10;
        end
        th_sequential_10: begin
          _th_sequential_i_11 <= _th_sequential_i_11 + 1;
          th_sequential <= th_sequential_4;
        end
        th_sequential_11: begin
          th_sequential <= th_sequential_12;
        end
      endcase
    end
  end

  localparam _tmp_fsm_5_1 = 1;
  localparam _tmp_fsm_5_2 = 2;
  localparam _tmp_fsm_5_3 = 3;
  localparam _tmp_fsm_5_4 = 4;
  localparam _tmp_fsm_5_5 = 5;
  localparam _tmp_fsm_5_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_5 <= _tmp_fsm_5_init;
      _d1__tmp_fsm_5 <= _tmp_fsm_5_init;
      _tmp_124 <= 0;
      _tmp_126 <= 0;
      _tmp_125 <= 0;
      _tmp_142 <= 0;
      __tmp_fsm_5_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_5 <= _tmp_fsm_5;
      case(_d1__tmp_fsm_5)
        _tmp_fsm_5_5: begin
          if(__tmp_fsm_5_cond_5_0_1) begin
            _tmp_142 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_5)
        _tmp_fsm_5_init: begin
          if(th_comp == 19) begin
            _tmp_fsm_5 <= _tmp_fsm_5_1;
          end 
        end
        _tmp_fsm_5_1: begin
          _tmp_124 <= (_tmp_122 >> 2) << 2;
          _tmp_126 <= _tmp_123;
          _tmp_fsm_5 <= _tmp_fsm_5_2;
        end
        _tmp_fsm_5_2: begin
          if((_tmp_126 <= 256) && ((_tmp_124 & 4095) + (_tmp_126 << 2) >= 4096)) begin
            _tmp_125 <= 4096 - (_tmp_124 & 4095) >> 2;
            _tmp_126 <= _tmp_126 - (4096 - (_tmp_124 & 4095) >> 2);
          end else if(_tmp_126 <= 256) begin
            _tmp_125 <= _tmp_126;
            _tmp_126 <= 0;
          end else if((_tmp_124 & 4095) + 1024 >= 4096) begin
            _tmp_125 <= 4096 - (_tmp_124 & 4095) >> 2;
            _tmp_126 <= _tmp_126 - (4096 - (_tmp_124 & 4095) >> 2);
          end else begin
            _tmp_125 <= 256;
            _tmp_126 <= _tmp_126 - 256;
          end
          _tmp_fsm_5 <= _tmp_fsm_5_3;
        end
        _tmp_fsm_5_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_5 <= _tmp_fsm_5_4;
          end 
        end
        _tmp_fsm_5_4: begin
          if(_tmp_140 && myaxi_wvalid && myaxi_wready) begin
            _tmp_124 <= _tmp_124 + (_tmp_125 << 2);
          end 
          if(_tmp_140 && myaxi_wvalid && myaxi_wready && (_tmp_126 > 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_2;
          end 
          if(_tmp_140 && myaxi_wvalid && myaxi_wready && (_tmp_126 == 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_5;
          end 
        end
        _tmp_fsm_5_5: begin
          _tmp_142 <= 1;
          __tmp_fsm_5_cond_5_0_1 <= 1;
          _tmp_fsm_5 <= _tmp_fsm_5_6;
        end
        _tmp_fsm_5_6: begin
          _tmp_fsm_5 <= _tmp_fsm_5_init;
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



module multiplier_0
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_0
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg [32-1:0] _a;
  reg [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
  assign rslt = $signed({ 1'd0, _a }) * $signed({ 1'd0, _b });
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_stream_multidim.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
