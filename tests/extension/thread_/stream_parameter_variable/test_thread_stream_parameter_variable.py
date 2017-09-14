from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_parameter_variable

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
  reg signed [32-1:0] _th_comp_size_0;
  reg signed [32-1:0] _th_comp_offset_1;
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
  reg signed [32-1:0] _th_comp_bias_2;
  reg _mystream_flag_3;
  reg [32-1:0] _mystream_fsm_4;
  localparam _mystream_fsm_4_init = 0;
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
  reg [33-1:0] _tmp_37;
  reg _mystream_flag_5;
  reg [32-1:0] _mystream_fsm_6;
  localparam _mystream_fsm_6_init = 0;
  reg _tmp_38;
  reg _tmp_39;
  wire _tmp_40;
  wire _tmp_41;
  assign _tmp_41 = 1;
  localparam _tmp_42 = 1;
  wire [_tmp_42-1:0] _tmp_43;
  assign _tmp_43 = (_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39);
  reg [_tmp_42-1:0] __tmp_43_1;
  wire [32-1:0] _tmp_44;
  reg [32-1:0] __tmp_44_1;
  assign _tmp_44 = (__tmp_43_1)? ram_b_0_rdata : __tmp_44_1;
  reg _tmp_45;
  reg _tmp_46;
  reg _tmp_47;
  reg _tmp_48;
  reg [33-1:0] _tmp_49;
  reg _mystream_flag_7;
  reg [32-1:0] _mystream_fsm_8;
  localparam _mystream_fsm_8_init = 0;
  reg [33-1:0] _tmp_50;
  reg _tmp_51;
  wire [32-1:0] _tmp_data_52;
  wire _tmp_valid_52;
  wire _tmp_ready_52;
  assign _tmp_ready_52 = (_tmp_50 > 0) && !_tmp_51;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_53;
  reg [32-1:0] _tmp_54;
  reg [32-1:0] _tmp_55;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_56;
  reg [33-1:0] _tmp_57;
  reg [33-1:0] _tmp_58;
  reg _tmp_59;
  reg _tmp_60;
  wire _tmp_61;
  wire _tmp_62;
  assign _tmp_62 = 1;
  localparam _tmp_63 = 1;
  wire [_tmp_63-1:0] _tmp_64;
  assign _tmp_64 = (_tmp_61 || !_tmp_59) && (_tmp_62 || !_tmp_60);
  reg [_tmp_63-1:0] __tmp_64_1;
  wire [32-1:0] _tmp_65;
  reg [32-1:0] __tmp_65_1;
  assign _tmp_65 = (__tmp_64_1)? ram_c_0_rdata : __tmp_65_1;
  reg _tmp_66;
  reg _tmp_67;
  reg _tmp_68;
  reg _tmp_69;
  reg [33-1:0] _tmp_70;
  reg [9-1:0] _tmp_71;
  reg _myaxi_cond_2_1;
  reg _tmp_72;
  wire [32-1:0] _tmp_data_73;
  wire _tmp_valid_73;
  wire _tmp_ready_73;
  assign _tmp_ready_73 = (_tmp_fsm_2 == 4) && ((_tmp_71 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_74;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_5_0_1;
  reg [10-1:0] _tmp_75;
  reg [32-1:0] _tmp_76;
  reg [32-1:0] _tmp_77;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_78;
  reg [33-1:0] _tmp_79;
  reg [33-1:0] _tmp_80;
  reg [32-1:0] _tmp_81;
  reg _tmp_82;
  reg [33-1:0] _tmp_83;
  reg _tmp_84;
  wire [32-1:0] _tmp_data_85;
  wire _tmp_valid_85;
  wire _tmp_ready_85;
  assign _tmp_ready_85 = (_tmp_83 > 0) && !_tmp_84;
  reg _ram_a_cond_1_1;
  reg [9-1:0] _tmp_86;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_87;
  reg __tmp_fsm_3_cond_5_1_1;
  reg [10-1:0] _tmp_88;
  reg [32-1:0] _tmp_89;
  reg [32-1:0] _tmp_90;
  reg [32-1:0] _tmp_fsm_4;
  localparam _tmp_fsm_4_init = 0;
  reg [32-1:0] _tmp_91;
  reg [33-1:0] _tmp_92;
  reg [33-1:0] _tmp_93;
  reg [32-1:0] _tmp_94;
  reg _tmp_95;
  reg [33-1:0] _tmp_96;
  reg _tmp_97;
  wire [32-1:0] _tmp_data_98;
  wire _tmp_valid_98;
  wire _tmp_ready_98;
  assign _tmp_ready_98 = (_tmp_96 > 0) && !_tmp_97;
  reg _ram_b_cond_1_1;
  reg [9-1:0] _tmp_99;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_1 == 4) || (_tmp_fsm_3 == 4) || (_tmp_fsm_4 == 4);
  reg [32-1:0] _d1__tmp_fsm_4;
  reg __tmp_fsm_4_cond_4_0_1;
  reg _tmp_100;
  reg __tmp_fsm_4_cond_5_1_1;
  reg [32-1:0] th_sequential;
  localparam th_sequential_init = 0;
  reg _th_sequential_called;
  reg signed [32-1:0] _th_sequential_size_9;
  reg signed [32-1:0] _th_sequential_offset_10;
  reg signed [32-1:0] _th_sequential_bias_11;
  reg signed [32-1:0] _th_sequential_size_12;
  reg signed [32-1:0] _th_sequential_offset_13;
  reg signed [32-1:0] _th_sequential_bias_14;
  reg signed [32-1:0] _th_sequential_sum_15;
  reg signed [32-1:0] _th_sequential_i_16;
  reg _tmp_101;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_3_2;
  reg signed [32-1:0] _tmp_102;
  reg signed [32-1:0] _th_sequential_a_17;
  reg _tmp_103;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_3_2;
  reg signed [32-1:0] _tmp_104;
  reg signed [32-1:0] _th_sequential_b_18;
  reg _ram_c_cond_1_1;
  reg [10-1:0] _tmp_105;
  reg [32-1:0] _tmp_106;
  reg [32-1:0] _tmp_107;
  reg [32-1:0] _tmp_fsm_5;
  localparam _tmp_fsm_5_init = 0;
  reg [32-1:0] _tmp_108;
  reg [33-1:0] _tmp_109;
  reg [33-1:0] _tmp_110;
  reg _tmp_111;
  reg _tmp_112;
  wire _tmp_113;
  wire _tmp_114;
  assign _tmp_114 = 1;
  localparam _tmp_115 = 1;
  wire [_tmp_115-1:0] _tmp_116;
  assign _tmp_116 = (_tmp_113 || !_tmp_111) && (_tmp_114 || !_tmp_112);
  reg [_tmp_115-1:0] __tmp_116_1;
  wire [32-1:0] _tmp_117;
  reg [32-1:0] __tmp_117_1;
  assign _tmp_117 = (__tmp_116_1)? ram_c_0_rdata : __tmp_117_1;
  reg _tmp_118;
  reg _tmp_119;
  reg _tmp_120;
  reg _tmp_121;
  reg [33-1:0] _tmp_122;
  reg [9-1:0] _tmp_123;
  reg _myaxi_cond_6_1;
  reg _tmp_124;
  wire [32-1:0] _tmp_data_125;
  wire _tmp_valid_125;
  wire _tmp_ready_125;
  assign _tmp_ready_125 = (_tmp_fsm_5 == 4) && ((_tmp_123 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_7_1;
  reg _tmp_126;
  reg [32-1:0] _d1__tmp_fsm_5;
  reg __tmp_fsm_5_cond_5_0_1;
  reg signed [32-1:0] _th_comp_size_19;
  reg signed [32-1:0] _th_comp_offset_stream_20;
  reg signed [32-1:0] _th_comp_offset_seq_21;
  reg signed [32-1:0] _th_comp_all_ok_22;
  reg signed [32-1:0] _th_comp_i_23;
  reg _tmp_127;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_128;
  reg signed [32-1:0] _th_comp_st_24;
  reg _tmp_129;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_130;
  reg signed [32-1:0] _th_comp_sq_25;

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
      _tmp_71 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_72 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_86 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_99 <= 0;
      _myaxi_cond_5_1 <= 0;
      _tmp_123 <= 0;
      _myaxi_cond_6_1 <= 0;
      _tmp_124 <= 0;
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
        _tmp_72 <= 0;
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
        _tmp_124 <= 0;
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
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_71 == 0))) begin
        myaxi_awaddr <= _tmp_56;
        myaxi_awlen <= _tmp_57 - 1;
        myaxi_awvalid <= 1;
        _tmp_71 <= _tmp_57;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_71 == 0)) && (_tmp_57 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_73 && ((_tmp_fsm_2 == 4) && ((_tmp_71 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_71 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_71 > 0))) begin
        myaxi_wdata <= _tmp_data_73;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_71 <= _tmp_71 - 1;
      end 
      if(_tmp_valid_73 && ((_tmp_fsm_2 == 4) && ((_tmp_71 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_71 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_71 > 0)) && (_tmp_71 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_72 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_72 <= _tmp_72;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_86 == 0))) begin
        myaxi_araddr <= _tmp_78;
        myaxi_arlen <= _tmp_79 - 1;
        myaxi_arvalid <= 1;
        _tmp_86 <= _tmp_79;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_86 > 0)) begin
        _tmp_86 <= _tmp_86 - 1;
      end 
      if((_tmp_fsm_4 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_99 == 0))) begin
        myaxi_araddr <= _tmp_91;
        myaxi_arlen <= _tmp_92 - 1;
        myaxi_arvalid <= 1;
        _tmp_99 <= _tmp_92;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_99 > 0)) begin
        _tmp_99 <= _tmp_99 - 1;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_123 == 0))) begin
        myaxi_awaddr <= _tmp_108;
        myaxi_awlen <= _tmp_109 - 1;
        myaxi_awvalid <= 1;
        _tmp_123 <= _tmp_109;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_123 == 0)) && (_tmp_109 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_6_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_125 && ((_tmp_fsm_5 == 4) && ((_tmp_123 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_123 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_123 > 0))) begin
        myaxi_wdata <= _tmp_data_125;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_123 <= _tmp_123 - 1;
      end 
      if(_tmp_valid_125 && ((_tmp_fsm_5 == 4) && ((_tmp_123 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_123 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_123 > 0)) && (_tmp_123 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_124 <= 1;
      end 
      _myaxi_cond_7_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_124 <= _tmp_124;
      end 
    end
  end

  assign _tmp_data_10 = _tmp_6;
  assign _tmp_valid_10 = _tmp_7;
  assign _tmp_data_23 = _tmp_19;
  assign _tmp_valid_23 = _tmp_20;
  assign _tmp_data_85 = _tmp_81;
  assign _tmp_valid_85 = _tmp_82;
  assign _tmp_data_98 = _tmp_94;
  assign _tmp_valid_98 = _tmp_95;

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
      _tmp_83 <= 0;
      _tmp_84 <= 0;
      _ram_a_cond_1_1 <= 0;
      _ram_a_cond_2_1 <= 0;
      _tmp_101 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_3_2 <= 0;
    end else begin
      if(_ram_a_cond_3_2) begin
        _tmp_101 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_9 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        ram_a_0_wenable <= 0;
        _tmp_84 <= 0;
      end 
      if(_ram_a_cond_2_1) begin
        _tmp_101 <= 1;
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
      if((_mystream_fsm_4 == 1) && (_tmp_37 == 0) && !_tmp_35 && !_tmp_36) begin
        ram_a_0_addr <= _th_comp_offset_1;
        _tmp_37 <= _th_comp_size_0 - 1;
        _tmp_33 <= 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        _tmp_37 <= _tmp_37 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 == 1)) begin
        _tmp_35 <= 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_83 == 0)) begin
        ram_a_0_addr <= _tmp_75 - 1;
        _tmp_83 <= _tmp_77;
      end 
      if(_tmp_valid_85 && ((_tmp_83 > 0) && !_tmp_84) && (_tmp_83 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_85;
        ram_a_0_wenable <= 1;
        _tmp_83 <= _tmp_83 - 1;
      end 
      if(_tmp_valid_85 && ((_tmp_83 > 0) && !_tmp_84) && (_tmp_83 == 1)) begin
        _tmp_84 <= 1;
      end 
      _ram_a_cond_1_1 <= 1;
      if(th_sequential == 5) begin
        ram_a_0_addr <= _th_sequential_i_16 + _th_sequential_offset_13;
      end 
      _ram_a_cond_2_1 <= th_sequential == 5;
      _ram_a_cond_3_1 <= th_sequential == 5;
    end
  end

  reg [32-1:0] _tmp_data_131;
  reg _tmp_valid_131;
  wire _tmp_ready_131;
  assign _tmp_28 = 1 && ((_tmp_ready_131 || !_tmp_valid_131) && (_tmp_26 && _tmp_38));
  assign _tmp_40 = 1 && ((_tmp_ready_131 || !_tmp_valid_131) && (_tmp_26 && _tmp_38));
  reg [32-1:0] _tmp_data_132;
  reg _tmp_valid_132;
  wire _tmp_ready_132;
  assign _tmp_ready_131 = (_tmp_ready_132 || !_tmp_valid_132) && _tmp_valid_131;
  assign _tmp_data_52 = _tmp_data_132;
  assign _tmp_valid_52 = _tmp_valid_132;
  assign _tmp_ready_132 = _tmp_ready_52;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_131 <= 0;
      _tmp_valid_131 <= 0;
      _tmp_data_132 <= 0;
      _tmp_valid_132 <= 0;
    end else begin
      if((_tmp_ready_131 || !_tmp_valid_131) && (_tmp_28 && _tmp_40) && (_tmp_26 && _tmp_38)) begin
        _tmp_data_131 <= _tmp_32 + _tmp_44;
      end 
      if(_tmp_valid_131 && _tmp_ready_131) begin
        _tmp_valid_131 <= 0;
      end 
      if((_tmp_ready_131 || !_tmp_valid_131) && (_tmp_28 && _tmp_40)) begin
        _tmp_valid_131 <= _tmp_26 && _tmp_38;
      end 
      if((_tmp_ready_132 || !_tmp_valid_132) && _tmp_ready_131 && _tmp_valid_131) begin
        _tmp_data_132 <= _tmp_data_131 + _th_comp_bias_2;
      end 
      if(_tmp_valid_132 && _tmp_ready_132) begin
        _tmp_valid_132 <= 0;
      end 
      if((_tmp_ready_132 || !_tmp_valid_132) && _tmp_ready_131) begin
        _tmp_valid_132 <= _tmp_valid_131;
      end 
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
      __tmp_43_1 <= 0;
      __tmp_44_1 <= 0;
      _tmp_48 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_45 <= 0;
      _tmp_49 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _ram_b_cond_1_1 <= 0;
      _ram_b_cond_2_1 <= 0;
      _tmp_103 <= 0;
      _ram_b_cond_3_1 <= 0;
      _ram_b_cond_3_2 <= 0;
    end else begin
      if(_ram_b_cond_3_2) begin
        _tmp_103 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_22 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        ram_b_0_wenable <= 0;
        _tmp_97 <= 0;
      end 
      if(_ram_b_cond_2_1) begin
        _tmp_103 <= 1;
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
      if((_mystream_fsm_6 == 1) && (_tmp_49 == 0) && !_tmp_47 && !_tmp_48) begin
        ram_b_0_addr <= _th_comp_offset_1;
        _tmp_49 <= _th_comp_size_0 - 1;
        _tmp_45 <= 1;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        _tmp_49 <= _tmp_49 - 1;
        _tmp_45 <= 1;
        _tmp_47 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 == 1)) begin
        _tmp_47 <= 1;
      end 
      if((_tmp_fsm_4 == 1) && (_tmp_96 == 0)) begin
        ram_b_0_addr <= _tmp_88 - 1;
        _tmp_96 <= _tmp_90;
      end 
      if(_tmp_valid_98 && ((_tmp_96 > 0) && !_tmp_97) && (_tmp_96 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_98;
        ram_b_0_wenable <= 1;
        _tmp_96 <= _tmp_96 - 1;
      end 
      if(_tmp_valid_98 && ((_tmp_96 > 0) && !_tmp_97) && (_tmp_96 == 1)) begin
        _tmp_97 <= 1;
      end 
      _ram_b_cond_1_1 <= 1;
      if(th_sequential == 7) begin
        ram_b_0_addr <= _th_sequential_i_16 + _th_sequential_offset_13;
      end 
      _ram_b_cond_2_1 <= th_sequential == 7;
      _ram_b_cond_3_1 <= th_sequential == 7;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_50 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_51 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_64_1 <= 0;
      __tmp_65_1 <= 0;
      _tmp_69 <= 0;
      _tmp_59 <= 0;
      _tmp_60 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _tmp_66 <= 0;
      _tmp_70 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_116_1 <= 0;
      __tmp_117_1 <= 0;
      _tmp_121 <= 0;
      _tmp_111 <= 0;
      _tmp_112 <= 0;
      _tmp_119 <= 0;
      _tmp_120 <= 0;
      _tmp_118 <= 0;
      _tmp_122 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_127 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_129 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_127 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_129 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_51 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_127 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_129 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if((_mystream_fsm_8 == 1) && (_tmp_50 == 0)) begin
        ram_c_0_addr <= _th_comp_offset_1 - 1;
        _tmp_50 <= _th_comp_size_0;
      end 
      if(_tmp_valid_52 && ((_tmp_50 > 0) && !_tmp_51) && (_tmp_50 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_52;
        ram_c_0_wenable <= 1;
        _tmp_50 <= _tmp_50 - 1;
      end 
      if(_tmp_valid_52 && ((_tmp_50 > 0) && !_tmp_51) && (_tmp_50 == 1)) begin
        _tmp_51 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_64_1 <= _tmp_64;
      __tmp_65_1 <= _tmp_65;
      if((_tmp_61 || !_tmp_59) && (_tmp_62 || !_tmp_60) && _tmp_67) begin
        _tmp_69 <= 0;
        _tmp_59 <= 0;
        _tmp_60 <= 0;
        _tmp_67 <= 0;
      end 
      if((_tmp_61 || !_tmp_59) && (_tmp_62 || !_tmp_60) && _tmp_66) begin
        _tmp_59 <= 1;
        _tmp_60 <= 1;
        _tmp_69 <= _tmp_68;
        _tmp_68 <= 0;
        _tmp_66 <= 0;
        _tmp_67 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_70 == 0) && !_tmp_68 && !_tmp_69) begin
        ram_c_0_addr <= _tmp_53;
        _tmp_70 <= _tmp_55 - 1;
        _tmp_66 <= 1;
      end 
      if((_tmp_61 || !_tmp_59) && (_tmp_62 || !_tmp_60) && (_tmp_70 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_70 <= _tmp_70 - 1;
        _tmp_66 <= 1;
        _tmp_68 <= 0;
      end 
      if((_tmp_61 || !_tmp_59) && (_tmp_62 || !_tmp_60) && (_tmp_70 == 1)) begin
        _tmp_68 <= 1;
      end 
      if(th_sequential == 10) begin
        ram_c_0_addr <= _th_sequential_i_16 + _th_sequential_offset_13;
        ram_c_0_wdata <= _th_sequential_sum_15;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_sequential == 10;
      __tmp_116_1 <= _tmp_116;
      __tmp_117_1 <= _tmp_117;
      if((_tmp_113 || !_tmp_111) && (_tmp_114 || !_tmp_112) && _tmp_119) begin
        _tmp_121 <= 0;
        _tmp_111 <= 0;
        _tmp_112 <= 0;
        _tmp_119 <= 0;
      end 
      if((_tmp_113 || !_tmp_111) && (_tmp_114 || !_tmp_112) && _tmp_118) begin
        _tmp_111 <= 1;
        _tmp_112 <= 1;
        _tmp_121 <= _tmp_120;
        _tmp_120 <= 0;
        _tmp_118 <= 0;
        _tmp_119 <= 1;
      end 
      if((_tmp_fsm_5 == 1) && (_tmp_122 == 0) && !_tmp_120 && !_tmp_121) begin
        ram_c_0_addr <= _tmp_105;
        _tmp_122 <= _tmp_107 - 1;
        _tmp_118 <= 1;
      end 
      if((_tmp_113 || !_tmp_111) && (_tmp_114 || !_tmp_112) && (_tmp_122 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_122 <= _tmp_122 - 1;
        _tmp_118 <= 1;
        _tmp_120 <= 0;
      end 
      if((_tmp_113 || !_tmp_111) && (_tmp_114 || !_tmp_112) && (_tmp_122 == 1)) begin
        _tmp_120 <= 1;
      end 
      if(th_comp == 24) begin
        ram_c_0_addr <= _th_comp_i_23 + _th_comp_offset_stream_20;
      end 
      _ram_c_cond_2_1 <= th_comp == 24;
      _ram_c_cond_3_1 <= th_comp == 24;
      if(th_comp == 26) begin
        ram_c_0_addr <= _th_comp_i_23 + _th_comp_offset_seq_21;
      end 
      _ram_c_cond_4_1 <= th_comp == 26;
      _ram_c_cond_5_1 <= th_comp == 26;
    end
  end

  assign _tmp_data_73 = _tmp_65;
  assign _tmp_valid_73 = _tmp_59;
  assign _tmp_61 = 1 && _tmp_ready_73;
  assign _tmp_data_125 = _tmp_117;
  assign _tmp_valid_125 = _tmp_111;
  assign _tmp_113 = 1 && _tmp_ready_125;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_offset_1 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _th_comp_bias_2 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_55 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _tmp_90 <= 0;
      _tmp_105 <= 0;
      _tmp_106 <= 0;
      _tmp_107 <= 0;
      _th_comp_size_19 <= 0;
      _th_comp_offset_stream_20 <= 0;
      _th_comp_offset_seq_21 <= 0;
      _th_comp_all_ok_22 <= 0;
      _th_comp_i_23 <= 0;
      _tmp_128 <= 0;
      _th_comp_st_24 <= 0;
      _tmp_130 <= 0;
      _th_comp_sq_25 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          _th_comp_size_0 <= 32;
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_offset_1 <= 0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          _tmp_0 <= _th_comp_offset_1;
          _tmp_1 <= 0;
          _tmp_2 <= _th_comp_size_0;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          if(_tmp_12) begin
            th_comp <= th_comp_4;
          end 
        end
        th_comp_4: begin
          _tmp_13 <= _th_comp_offset_1;
          _tmp_14 <= 0;
          _tmp_15 <= _th_comp_size_0;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          if(_tmp_25) begin
            th_comp <= th_comp_6;
          end 
        end
        th_comp_6: begin
          _th_comp_bias_2 <= 100;
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if(_mystream_flag_3 && _mystream_flag_5 && _mystream_flag_7) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          _tmp_53 <= _th_comp_offset_1;
          _tmp_54 <= 1024;
          _tmp_55 <= _th_comp_size_0;
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if(_tmp_74) begin
            th_comp <= th_comp_11;
          end 
        end
        th_comp_11: begin
          _th_comp_offset_1 <= _th_comp_size_0;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          _tmp_75 <= _th_comp_offset_1;
          _tmp_76 <= 0;
          _tmp_77 <= _th_comp_size_0;
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          if(_tmp_87) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          _tmp_88 <= _th_comp_offset_1;
          _tmp_89 <= 0;
          _tmp_90 <= _th_comp_size_0;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(_tmp_100) begin
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
          _tmp_105 <= _th_comp_offset_1;
          _tmp_106 <= 2048;
          _tmp_107 <= _th_comp_size_0;
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(_tmp_126) begin
            th_comp <= th_comp_20;
          end 
        end
        th_comp_20: begin
          _th_comp_size_19 <= _th_comp_size_0;
          _th_comp_offset_stream_20 <= 0;
          _th_comp_offset_seq_21 <= _th_comp_offset_1;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          _th_comp_all_ok_22 <= 1;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          _th_comp_i_23 <= 0;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          if(_th_comp_i_23 < _th_comp_size_19) begin
            th_comp <= th_comp_24;
          end else begin
            th_comp <= th_comp_31;
          end
        end
        th_comp_24: begin
          if(_tmp_127) begin
            _tmp_128 <= ram_c_0_rdata;
          end 
          if(_tmp_127) begin
            th_comp <= th_comp_25;
          end 
        end
        th_comp_25: begin
          _th_comp_st_24 <= _tmp_128;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          if(_tmp_129) begin
            _tmp_130 <= ram_c_0_rdata;
          end 
          if(_tmp_129) begin
            th_comp <= th_comp_27;
          end 
        end
        th_comp_27: begin
          _th_comp_sq_25 <= _tmp_130;
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          if(_th_comp_st_24 !== _th_comp_sq_25) begin
            th_comp <= th_comp_29;
          end else begin
            th_comp <= th_comp_30;
          end
        end
        th_comp_29: begin
          _th_comp_all_ok_22 <= 0;
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          _th_comp_i_23 <= _th_comp_i_23 + 1;
          th_comp <= th_comp_23;
        end
        th_comp_31: begin
          if(_th_comp_all_ok_22) begin
            th_comp <= th_comp_32;
          end else begin
            th_comp <= th_comp_34;
          end
        end
        th_comp_32: begin
          $display("OK");
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          th_comp <= th_comp_35;
        end
        th_comp_34: begin
          $display("NG");
          th_comp <= th_comp_35;
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

  localparam _mystream_fsm_4_1 = 1;
  localparam _mystream_fsm_4_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_4 <= _mystream_fsm_4_init;
      _mystream_flag_3 <= 0;
    end else begin
      case(_mystream_fsm_4)
        _mystream_fsm_4_init: begin
          if(th_comp == 7) begin
            _mystream_flag_3 <= 0;
          end 
          if(th_comp == 7) begin
            _mystream_fsm_4 <= _mystream_fsm_4_1;
          end 
        end
        _mystream_fsm_4_1: begin
          _mystream_fsm_4 <= _mystream_fsm_4_2;
        end
        _mystream_fsm_4_2: begin
          if(_tmp_36) begin
            _mystream_flag_3 <= 1;
          end 
          if(_tmp_36) begin
            _mystream_fsm_4 <= _mystream_fsm_4_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_6_1 = 1;
  localparam _mystream_fsm_6_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_6 <= _mystream_fsm_6_init;
      _mystream_flag_5 <= 0;
    end else begin
      case(_mystream_fsm_6)
        _mystream_fsm_6_init: begin
          if(th_comp == 7) begin
            _mystream_flag_5 <= 0;
          end 
          if(th_comp == 7) begin
            _mystream_fsm_6 <= _mystream_fsm_6_1;
          end 
        end
        _mystream_fsm_6_1: begin
          _mystream_fsm_6 <= _mystream_fsm_6_2;
        end
        _mystream_fsm_6_2: begin
          if(_tmp_48) begin
            _mystream_flag_5 <= 1;
          end 
          if(_tmp_48) begin
            _mystream_fsm_6 <= _mystream_fsm_6_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_8_1 = 1;
  localparam _mystream_fsm_8_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_8 <= _mystream_fsm_8_init;
      _mystream_flag_7 <= 0;
    end else begin
      case(_mystream_fsm_8)
        _mystream_fsm_8_init: begin
          if(th_comp == 7) begin
            _mystream_flag_7 <= 0;
          end 
          if(th_comp == 7) begin
            _mystream_fsm_8 <= _mystream_fsm_8_1;
          end 
        end
        _mystream_fsm_8_1: begin
          _mystream_fsm_8 <= _mystream_fsm_8_2;
        end
        _mystream_fsm_8_2: begin
          if(_tmp_51) begin
            _mystream_flag_7 <= 1;
          end 
          if(_tmp_51) begin
            _mystream_fsm_8 <= _mystream_fsm_8_init;
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
      _tmp_56 <= 0;
      _tmp_58 <= 0;
      _tmp_57 <= 0;
      _tmp_74 <= 0;
      __tmp_fsm_2_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_0_1) begin
            _tmp_74 <= 0;
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
          _tmp_56 <= (_tmp_54 >> 2) << 2;
          _tmp_58 <= _tmp_55;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_58 <= 256) && ((_tmp_56 & 4095) + (_tmp_58 << 2) >= 4096)) begin
            _tmp_57 <= 4096 - (_tmp_56 & 4095) >> 2;
            _tmp_58 <= _tmp_58 - (4096 - (_tmp_56 & 4095) >> 2);
          end else if(_tmp_58 <= 256) begin
            _tmp_57 <= _tmp_58;
            _tmp_58 <= 0;
          end else if((_tmp_56 & 4095) + 1024 >= 4096) begin
            _tmp_57 <= 4096 - (_tmp_56 & 4095) >> 2;
            _tmp_58 <= _tmp_58 - (4096 - (_tmp_56 & 4095) >> 2);
          end else begin
            _tmp_57 <= 256;
            _tmp_58 <= _tmp_58 - 256;
          end
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_4;
          end 
        end
        _tmp_fsm_2_4: begin
          if(_tmp_72 && myaxi_wvalid && myaxi_wready) begin
            _tmp_56 <= _tmp_56 + (_tmp_57 << 2);
          end 
          if(_tmp_72 && myaxi_wvalid && myaxi_wready && (_tmp_58 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(_tmp_72 && myaxi_wvalid && myaxi_wready && (_tmp_58 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_74 <= 1;
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
      _tmp_78 <= 0;
      _tmp_80 <= 0;
      _tmp_79 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_82 <= 0;
      _tmp_81 <= 0;
      _tmp_87 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_82 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_87 <= 0;
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
          _tmp_78 <= (_tmp_76 >> 2) << 2;
          _tmp_80 <= _tmp_77;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_80 <= 256) && ((_tmp_78 & 4095) + (_tmp_80 << 2) >= 4096)) begin
            _tmp_79 <= 4096 - (_tmp_78 & 4095) >> 2;
            _tmp_80 <= _tmp_80 - (4096 - (_tmp_78 & 4095) >> 2);
          end else if(_tmp_80 <= 256) begin
            _tmp_79 <= _tmp_80;
            _tmp_80 <= 0;
          end else if((_tmp_78 & 4095) + 1024 >= 4096) begin
            _tmp_79 <= 4096 - (_tmp_78 & 4095) >> 2;
            _tmp_80 <= _tmp_80 - (4096 - (_tmp_78 & 4095) >> 2);
          end else begin
            _tmp_79 <= 256;
            _tmp_80 <= _tmp_80 - 256;
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
            _tmp_81 <= myaxi_rdata;
            _tmp_82 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_78 <= _tmp_78 + (_tmp_79 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_80 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_80 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_87 <= 1;
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
      _tmp_91 <= 0;
      _tmp_93 <= 0;
      _tmp_92 <= 0;
      __tmp_fsm_4_cond_4_0_1 <= 0;
      _tmp_95 <= 0;
      _tmp_94 <= 0;
      _tmp_100 <= 0;
      __tmp_fsm_4_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_4 <= _tmp_fsm_4;
      case(_d1__tmp_fsm_4)
        _tmp_fsm_4_4: begin
          if(__tmp_fsm_4_cond_4_0_1) begin
            _tmp_95 <= 0;
          end 
        end
        _tmp_fsm_4_5: begin
          if(__tmp_fsm_4_cond_5_1_1) begin
            _tmp_100 <= 0;
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
          _tmp_91 <= (_tmp_89 >> 2) << 2;
          _tmp_93 <= _tmp_90;
          _tmp_fsm_4 <= _tmp_fsm_4_2;
        end
        _tmp_fsm_4_2: begin
          if((_tmp_93 <= 256) && ((_tmp_91 & 4095) + (_tmp_93 << 2) >= 4096)) begin
            _tmp_92 <= 4096 - (_tmp_91 & 4095) >> 2;
            _tmp_93 <= _tmp_93 - (4096 - (_tmp_91 & 4095) >> 2);
          end else if(_tmp_93 <= 256) begin
            _tmp_92 <= _tmp_93;
            _tmp_93 <= 0;
          end else if((_tmp_91 & 4095) + 1024 >= 4096) begin
            _tmp_92 <= 4096 - (_tmp_91 & 4095) >> 2;
            _tmp_93 <= _tmp_93 - (4096 - (_tmp_91 & 4095) >> 2);
          end else begin
            _tmp_92 <= 256;
            _tmp_93 <= _tmp_93 - 256;
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
            _tmp_94 <= myaxi_rdata;
            _tmp_95 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_91 <= _tmp_91 + (_tmp_92 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_93 > 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_93 == 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_5;
          end 
        end
        _tmp_fsm_4_5: begin
          _tmp_100 <= 1;
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
      _th_sequential_size_9 <= 0;
      _th_sequential_offset_10 <= 0;
      _th_sequential_bias_11 <= 0;
      _th_sequential_size_12 <= 0;
      _th_sequential_offset_13 <= 0;
      _th_sequential_bias_14 <= 0;
      _th_sequential_sum_15 <= 0;
      _th_sequential_i_16 <= 0;
      _tmp_102 <= 0;
      _th_sequential_a_17 <= 0;
      _tmp_104 <= 0;
      _th_sequential_b_18 <= 0;
    end else begin
      case(th_sequential)
        th_sequential_init: begin
          if(th_comp == 16) begin
            _th_sequential_called <= 1;
          end 
          if(th_comp == 16) begin
            _th_sequential_size_9 <= _th_comp_size_0;
          end 
          if(th_comp == 16) begin
            _th_sequential_offset_10 <= _th_comp_offset_1;
          end 
          if(th_comp == 16) begin
            _th_sequential_bias_11 <= _th_comp_bias_2;
          end 
          if(th_comp == 16) begin
            th_sequential <= th_sequential_1;
          end 
        end
        th_sequential_1: begin
          _th_sequential_size_12 <= _th_sequential_size_9;
          _th_sequential_offset_13 <= _th_sequential_offset_10;
          _th_sequential_bias_14 <= _th_sequential_bias_11;
          th_sequential <= th_sequential_2;
        end
        th_sequential_2: begin
          _th_sequential_sum_15 <= 0;
          th_sequential <= th_sequential_3;
        end
        th_sequential_3: begin
          _th_sequential_i_16 <= 0;
          th_sequential <= th_sequential_4;
        end
        th_sequential_4: begin
          if(_th_sequential_i_16 < _th_sequential_size_12) begin
            th_sequential <= th_sequential_5;
          end else begin
            th_sequential <= th_sequential_12;
          end
        end
        th_sequential_5: begin
          if(_tmp_101) begin
            _tmp_102 <= ram_a_0_rdata;
          end 
          if(_tmp_101) begin
            th_sequential <= th_sequential_6;
          end 
        end
        th_sequential_6: begin
          _th_sequential_a_17 <= _tmp_102;
          th_sequential <= th_sequential_7;
        end
        th_sequential_7: begin
          if(_tmp_103) begin
            _tmp_104 <= ram_b_0_rdata;
          end 
          if(_tmp_103) begin
            th_sequential <= th_sequential_8;
          end 
        end
        th_sequential_8: begin
          _th_sequential_b_18 <= _tmp_104;
          th_sequential <= th_sequential_9;
        end
        th_sequential_9: begin
          _th_sequential_sum_15 <= _th_sequential_a_17 + _th_sequential_b_18 + _th_sequential_bias_14;
          th_sequential <= th_sequential_10;
        end
        th_sequential_10: begin
          th_sequential <= th_sequential_11;
        end
        th_sequential_11: begin
          _th_sequential_i_16 <= _th_sequential_i_16 + 1;
          th_sequential <= th_sequential_4;
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
      _tmp_108 <= 0;
      _tmp_110 <= 0;
      _tmp_109 <= 0;
      _tmp_126 <= 0;
      __tmp_fsm_5_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_5 <= _tmp_fsm_5;
      case(_d1__tmp_fsm_5)
        _tmp_fsm_5_5: begin
          if(__tmp_fsm_5_cond_5_0_1) begin
            _tmp_126 <= 0;
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
          _tmp_108 <= (_tmp_106 >> 2) << 2;
          _tmp_110 <= _tmp_107;
          _tmp_fsm_5 <= _tmp_fsm_5_2;
        end
        _tmp_fsm_5_2: begin
          if((_tmp_110 <= 256) && ((_tmp_108 & 4095) + (_tmp_110 << 2) >= 4096)) begin
            _tmp_109 <= 4096 - (_tmp_108 & 4095) >> 2;
            _tmp_110 <= _tmp_110 - (4096 - (_tmp_108 & 4095) >> 2);
          end else if(_tmp_110 <= 256) begin
            _tmp_109 <= _tmp_110;
            _tmp_110 <= 0;
          end else if((_tmp_108 & 4095) + 1024 >= 4096) begin
            _tmp_109 <= 4096 - (_tmp_108 & 4095) >> 2;
            _tmp_110 <= _tmp_110 - (4096 - (_tmp_108 & 4095) >> 2);
          end else begin
            _tmp_109 <= 256;
            _tmp_110 <= _tmp_110 - 256;
          end
          _tmp_fsm_5 <= _tmp_fsm_5_3;
        end
        _tmp_fsm_5_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_5 <= _tmp_fsm_5_4;
          end 
        end
        _tmp_fsm_5_4: begin
          if(_tmp_124 && myaxi_wvalid && myaxi_wready) begin
            _tmp_108 <= _tmp_108 + (_tmp_109 << 2);
          end 
          if(_tmp_124 && myaxi_wvalid && myaxi_wready && (_tmp_110 > 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_2;
          end 
          if(_tmp_124 && myaxi_wvalid && myaxi_wready && (_tmp_110 == 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_5;
          end 
        end
        _tmp_fsm_5_5: begin
          _tmp_126 <= 1;
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
"""


def test():
    veriloggen.reset()
    test_module = thread_stream_parameter_variable.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
