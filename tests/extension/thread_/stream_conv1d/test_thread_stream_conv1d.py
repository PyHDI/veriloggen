from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_conv1d

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
  reg signed [32-1:0] _th_comp_k_0;
  reg _ram_b_cond_0_1;
  reg signed [32-1:0] _th_comp_roffset_1;
  reg signed [32-1:0] _th_comp_woffset_2;
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
  reg _mystream_flag_3;
  reg [32-1:0] _mystream_fsm_4;
  localparam _mystream_fsm_4_init = 0;
  reg _tmp_13;
  reg _tmp_14;
  wire _tmp_15;
  wire _tmp_16;
  assign _tmp_16 = 1;
  localparam _tmp_17 = 1;
  wire [_tmp_17-1:0] _tmp_18;
  assign _tmp_18 = (_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14);
  reg [_tmp_17-1:0] __tmp_18_1;
  wire [32-1:0] _tmp_19;
  reg [32-1:0] __tmp_19_1;
  assign _tmp_19 = (__tmp_18_1)? ram_a_0_rdata : __tmp_19_1;
  reg _tmp_20;
  reg _tmp_21;
  reg _tmp_22;
  reg _tmp_23;
  reg _tmp_24;
  wire [10-1:0] _tmp_25;
  wire [10-1:0] _tmp_26;
  reg [10-1:0] _tmp_27;
  assign _tmp_26 = _tmp_27 + _th_comp_roffset_1;
  reg [3-1:0] _tmp_28;
  reg [5-1:0] _tmp_29;
  assign _tmp_25 = (_tmp_28 == 0)? _tmp_26 : ram_a_0_addr + 1;
  reg _mystream_flag_5;
  reg [32-1:0] _mystream_fsm_6;
  localparam _mystream_fsm_6_init = 0;
  reg _tmp_30;
  reg _tmp_31;
  wire _tmp_32;
  wire _tmp_33;
  assign _tmp_33 = 1;
  localparam _tmp_34 = 1;
  wire [_tmp_34-1:0] _tmp_35;
  assign _tmp_35 = (_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31);
  reg [_tmp_34-1:0] __tmp_35_1;
  wire [32-1:0] _tmp_36;
  reg [32-1:0] __tmp_36_1;
  assign _tmp_36 = (__tmp_35_1)? ram_b_0_rdata : __tmp_36_1;
  reg _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  reg _tmp_40;
  reg _tmp_41;
  wire [10-1:0] _tmp_42;
  wire [10-1:0] _tmp_43;
  reg [10-1:0] _tmp_44;
  assign _tmp_43 = _tmp_44 + 0;
  reg [3-1:0] _tmp_45;
  reg [5-1:0] _tmp_46;
  assign _tmp_42 = (_tmp_45 == 0)? _tmp_43 : ram_b_0_addr + 1;
  reg _mystream_flag_7;
  reg [32-1:0] _mystream_fsm_8;
  localparam _mystream_fsm_8_init = 0;
  reg [5-1:0] _tmp_47;
  reg _tmp_48;
  wire _tmp_all_valid_49;
  wire [32-1:0] _tmp_data_50;
  wire _tmp_valid_50;
  wire _tmp_ready_50;
  assign _tmp_ready_50 = (_tmp_47 > 0) && !_tmp_48 && _tmp_all_valid_49;
  wire [1-1:0] _tmp_data_51;
  wire _tmp_valid_51;
  wire _tmp_ready_51;
  assign _tmp_ready_51 = (_tmp_47 > 0) && !_tmp_48 && _tmp_all_valid_49;
  assign _tmp_all_valid_49 = _tmp_valid_50 && _tmp_valid_51;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_52;
  reg [32-1:0] _tmp_53;
  reg [32-1:0] _tmp_54;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_55;
  reg [33-1:0] _tmp_56;
  reg [33-1:0] _tmp_57;
  reg _tmp_58;
  reg _tmp_59;
  wire _tmp_60;
  wire _tmp_61;
  assign _tmp_61 = 1;
  localparam _tmp_62 = 1;
  wire [_tmp_62-1:0] _tmp_63;
  assign _tmp_63 = (_tmp_60 || !_tmp_58) && (_tmp_61 || !_tmp_59);
  reg [_tmp_62-1:0] __tmp_63_1;
  wire [32-1:0] _tmp_64;
  reg [32-1:0] __tmp_64_1;
  assign _tmp_64 = (__tmp_63_1)? ram_c_0_rdata : __tmp_64_1;
  reg _tmp_65;
  reg _tmp_66;
  reg _tmp_67;
  reg _tmp_68;
  reg [33-1:0] _tmp_69;
  reg [9-1:0] _tmp_70;
  reg _myaxi_cond_1_1;
  reg _tmp_71;
  wire [32-1:0] _tmp_data_72;
  wire _tmp_valid_72;
  wire _tmp_ready_72;
  assign _tmp_ready_72 = (_tmp_fsm_1 == 4) && ((_tmp_70 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  reg _tmp_73;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_5_0_1;
  reg [10-1:0] _tmp_74;
  reg [32-1:0] _tmp_75;
  reg [32-1:0] _tmp_76;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_77;
  reg [33-1:0] _tmp_78;
  reg [33-1:0] _tmp_79;
  reg [32-1:0] _tmp_80;
  reg _tmp_81;
  reg [33-1:0] _tmp_82;
  reg _tmp_83;
  wire [32-1:0] _tmp_data_84;
  wire _tmp_valid_84;
  wire _tmp_ready_84;
  assign _tmp_ready_84 = (_tmp_82 > 0) && !_tmp_83;
  reg _ram_a_cond_1_1;
  reg [9-1:0] _tmp_85;
  reg _myaxi_cond_3_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_2 == 4);
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_4_0_1;
  reg _tmp_86;
  reg __tmp_fsm_2_cond_5_1_1;
  reg [32-1:0] th_sequential;
  localparam th_sequential_init = 0;
  reg _th_sequential_called;
  reg signed [32-1:0] _th_sequential_roffset_9;
  reg signed [32-1:0] _th_sequential_woffset_10;
  reg signed [32-1:0] _th_sequential_roffset_11;
  reg signed [32-1:0] _th_sequential_woffset_12;
  reg signed [32-1:0] _th_sequential_i_13;
  reg signed [32-1:0] _th_sequential_sum_14;
  reg signed [32-1:0] _th_sequential_k_15;
  reg _tmp_87;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_3_2;
  reg signed [32-1:0] _tmp_88;
  reg signed [32-1:0] _th_sequential_a_16;
  reg _tmp_89;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  reg signed [32-1:0] _tmp_90;
  reg signed [32-1:0] _th_sequential_b_17;
  reg _ram_c_cond_1_1;
  reg [10-1:0] _tmp_91;
  reg [32-1:0] _tmp_92;
  reg [32-1:0] _tmp_93;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_94;
  reg [33-1:0] _tmp_95;
  reg [33-1:0] _tmp_96;
  reg _tmp_97;
  reg _tmp_98;
  wire _tmp_99;
  wire _tmp_100;
  assign _tmp_100 = 1;
  localparam _tmp_101 = 1;
  wire [_tmp_101-1:0] _tmp_102;
  assign _tmp_102 = (_tmp_99 || !_tmp_97) && (_tmp_100 || !_tmp_98);
  reg [_tmp_101-1:0] __tmp_102_1;
  wire [32-1:0] _tmp_103;
  reg [32-1:0] __tmp_103_1;
  assign _tmp_103 = (__tmp_102_1)? ram_c_0_rdata : __tmp_103_1;
  reg _tmp_104;
  reg _tmp_105;
  reg _tmp_106;
  reg _tmp_107;
  reg [33-1:0] _tmp_108;
  reg [9-1:0] _tmp_109;
  reg _myaxi_cond_4_1;
  reg _tmp_110;
  wire [32-1:0] _tmp_data_111;
  wire _tmp_valid_111;
  wire _tmp_ready_111;
  assign _tmp_ready_111 = (_tmp_fsm_3 == 4) && ((_tmp_109 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_5_1;
  reg _tmp_112;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_5_0_1;
  reg signed [32-1:0] _th_comp_offset_stream_18;
  reg signed [32-1:0] _th_comp_offset_seq_19;
  reg signed [32-1:0] _th_comp_all_ok_20;
  reg signed [32-1:0] _th_comp_i_21;
  reg _tmp_113;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_114;
  reg signed [32-1:0] _th_comp_st_22;
  reg _tmp_115;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_116;
  reg signed [32-1:0] _th_comp_sq_23;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_11 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_70 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_71 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_85 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_109 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_110 <= 0;
      _myaxi_cond_5_1 <= 0;
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
        _tmp_71 <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_5_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_110 <= 0;
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
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_70 == 0))) begin
        myaxi_awaddr <= _tmp_55;
        myaxi_awlen <= _tmp_56 - 1;
        myaxi_awvalid <= 1;
        _tmp_70 <= _tmp_56;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_70 == 0)) && (_tmp_56 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_72 && ((_tmp_fsm_1 == 4) && ((_tmp_70 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_70 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_70 > 0))) begin
        myaxi_wdata <= _tmp_data_72;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_70 <= _tmp_70 - 1;
      end 
      if(_tmp_valid_72 && ((_tmp_fsm_1 == 4) && ((_tmp_70 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_70 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_70 > 0)) && (_tmp_70 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_71 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_71 <= _tmp_71;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_85 == 0))) begin
        myaxi_araddr <= _tmp_77;
        myaxi_arlen <= _tmp_78 - 1;
        myaxi_arvalid <= 1;
        _tmp_85 <= _tmp_78;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_85 > 0)) begin
        _tmp_85 <= _tmp_85 - 1;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_109 == 0))) begin
        myaxi_awaddr <= _tmp_94;
        myaxi_awlen <= _tmp_95 - 1;
        myaxi_awvalid <= 1;
        _tmp_109 <= _tmp_95;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_109 == 0)) && (_tmp_95 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_111 && ((_tmp_fsm_3 == 4) && ((_tmp_109 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_109 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_109 > 0))) begin
        myaxi_wdata <= _tmp_data_111;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_109 <= _tmp_109 - 1;
      end 
      if(_tmp_valid_111 && ((_tmp_fsm_3 == 4) && ((_tmp_109 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_109 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_109 > 0)) && (_tmp_109 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_110 <= 1;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_110 <= _tmp_110;
      end 
    end
  end

  assign _tmp_data_10 = _tmp_6;
  assign _tmp_valid_10 = _tmp_7;
  assign _tmp_data_84 = _tmp_80;
  assign _tmp_valid_84 = _tmp_81;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_8 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_9 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_18_1 <= 0;
      __tmp_19_1 <= 0;
      _tmp_23 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_21 <= 0;
      _tmp_22 <= 0;
      _tmp_20 <= 0;
      _tmp_24 <= 0;
      _tmp_28 <= 0;
      _tmp_29 <= 0;
      _tmp_27 <= 0;
      _tmp_82 <= 0;
      _tmp_83 <= 0;
      _ram_a_cond_1_1 <= 0;
      _ram_a_cond_2_1 <= 0;
      _tmp_87 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_3_2 <= 0;
    end else begin
      if(_ram_a_cond_3_2) begin
        _tmp_87 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_9 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        ram_a_0_wenable <= 0;
        _tmp_83 <= 0;
      end 
      if(_ram_a_cond_2_1) begin
        _tmp_87 <= 1;
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
      __tmp_18_1 <= _tmp_18;
      __tmp_19_1 <= _tmp_19;
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_21) begin
        _tmp_23 <= 0;
        _tmp_13 <= 0;
        _tmp_14 <= 0;
        _tmp_21 <= 0;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_20) begin
        _tmp_13 <= 1;
        _tmp_14 <= 1;
        _tmp_23 <= _tmp_22;
        _tmp_22 <= 0;
        _tmp_20 <= 0;
        _tmp_21 <= 1;
      end 
      if((_mystream_fsm_4 == 1) && !_tmp_24 && !_tmp_22 && !_tmp_23) begin
        ram_a_0_addr <= _th_comp_roffset_1;
        _tmp_24 <= 1;
        _tmp_20 <= 1;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24) begin
        ram_a_0_addr <= _tmp_25;
        _tmp_20 <= 1;
        _tmp_22 <= 0;
      end 
      if((_mystream_fsm_4 == 1) && !_tmp_24 && !_tmp_22 && !_tmp_23) begin
        _tmp_28 <= 2;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24) begin
        _tmp_28 <= _tmp_28 - 1;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24 && (_tmp_28 == 0)) begin
        _tmp_28 <= 2;
      end 
      if((_mystream_fsm_4 == 1) && !_tmp_24 && !_tmp_22 && !_tmp_23) begin
        _tmp_29 <= 13;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24 && (_tmp_28 == 0)) begin
        _tmp_29 <= _tmp_29 - 1;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24 && (_tmp_28 == 0) && (_tmp_29 == 0)) begin
        _tmp_29 <= 13;
      end 
      if((_mystream_fsm_4 == 1) && !_tmp_24 && !_tmp_22 && !_tmp_23) begin
        _tmp_27 <= 0;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24 && (_tmp_28 == 1) && !0) begin
        _tmp_27 <= _tmp_27 + 1;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24 && (_tmp_28 == 1) && (_tmp_29 == 0)) begin
        _tmp_27 <= 0;
      end 
      if((_tmp_15 || !_tmp_13) && (_tmp_16 || !_tmp_14) && _tmp_24 && ((_tmp_28 == 0) && (_tmp_29 == 0))) begin
        _tmp_24 <= 0;
        _tmp_22 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_82 == 0)) begin
        ram_a_0_addr <= _tmp_74 - 1;
        _tmp_82 <= _tmp_76;
      end 
      if(_tmp_valid_84 && ((_tmp_82 > 0) && !_tmp_83) && (_tmp_82 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_84;
        ram_a_0_wenable <= 1;
        _tmp_82 <= _tmp_82 - 1;
      end 
      if(_tmp_valid_84 && ((_tmp_82 > 0) && !_tmp_83) && (_tmp_82 == 1)) begin
        _tmp_83 <= 1;
      end 
      _ram_a_cond_1_1 <= 1;
      if(th_sequential == 7) begin
        ram_a_0_addr <= _th_sequential_i_13 + _th_sequential_k_15 + _th_sequential_roffset_11;
      end 
      _ram_a_cond_2_1 <= th_sequential == 7;
      _ram_a_cond_3_1 <= th_sequential == 7;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_35_1 <= 0;
      __tmp_36_1 <= 0;
      _tmp_40 <= 0;
      _tmp_30 <= 0;
      _tmp_31 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_37 <= 0;
      _tmp_41 <= 0;
      _tmp_45 <= 0;
      _tmp_46 <= 0;
      _tmp_44 <= 0;
      _ram_b_cond_1_1 <= 0;
      _tmp_89 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_89 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_89 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if(th_comp == 3) begin
        ram_b_0_addr <= _th_comp_k_0;
        ram_b_0_wdata <= _th_comp_k_0 + 1;
        ram_b_0_wenable <= 1;
      end 
      _ram_b_cond_0_1 <= th_comp == 3;
      __tmp_35_1 <= _tmp_35;
      __tmp_36_1 <= _tmp_36;
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_38) begin
        _tmp_40 <= 0;
        _tmp_30 <= 0;
        _tmp_31 <= 0;
        _tmp_38 <= 0;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_37) begin
        _tmp_30 <= 1;
        _tmp_31 <= 1;
        _tmp_40 <= _tmp_39;
        _tmp_39 <= 0;
        _tmp_37 <= 0;
        _tmp_38 <= 1;
      end 
      if((_mystream_fsm_6 == 1) && !_tmp_41 && !_tmp_39 && !_tmp_40) begin
        ram_b_0_addr <= 0;
        _tmp_41 <= 1;
        _tmp_37 <= 1;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41) begin
        ram_b_0_addr <= _tmp_42;
        _tmp_37 <= 1;
        _tmp_39 <= 0;
      end 
      if((_mystream_fsm_6 == 1) && !_tmp_41 && !_tmp_39 && !_tmp_40) begin
        _tmp_45 <= 2;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41) begin
        _tmp_45 <= _tmp_45 - 1;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41 && (_tmp_45 == 0)) begin
        _tmp_45 <= 2;
      end 
      if((_mystream_fsm_6 == 1) && !_tmp_41 && !_tmp_39 && !_tmp_40) begin
        _tmp_46 <= 13;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41 && (_tmp_45 == 0)) begin
        _tmp_46 <= _tmp_46 - 1;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41 && (_tmp_45 == 0) && (_tmp_46 == 0)) begin
        _tmp_46 <= 13;
      end 
      if((_mystream_fsm_6 == 1) && !_tmp_41 && !_tmp_39 && !_tmp_40) begin
        _tmp_44 <= 0;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41 && (_tmp_45 == 1) && !0) begin
        _tmp_44 <= _tmp_44 + 0;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41 && (_tmp_45 == 1) && (_tmp_46 == 0)) begin
        _tmp_44 <= 0;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_41 && ((_tmp_45 == 0) && (_tmp_46 == 0))) begin
        _tmp_41 <= 0;
        _tmp_39 <= 1;
      end 
      if(th_sequential == 9) begin
        ram_b_0_addr <= _th_sequential_k_15;
      end 
      _ram_b_cond_1_1 <= th_sequential == 9;
      _ram_b_cond_2_1 <= th_sequential == 9;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_47 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_48 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_63_1 <= 0;
      __tmp_64_1 <= 0;
      _tmp_68 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _tmp_66 <= 0;
      _tmp_67 <= 0;
      _tmp_65 <= 0;
      _tmp_69 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_102_1 <= 0;
      __tmp_103_1 <= 0;
      _tmp_107 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _tmp_105 <= 0;
      _tmp_106 <= 0;
      _tmp_104 <= 0;
      _tmp_108 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_113 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_115 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_113 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_115 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_48 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_113 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_115 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if((_mystream_fsm_8 == 1) && (_tmp_47 == 0)) begin
        ram_c_0_addr <= _th_comp_woffset_2 - 1;
        _tmp_47 <= 14;
      end 
      if(_tmp_data_51 && (_tmp_valid_50 && ((_tmp_47 > 0) && !_tmp_48 && _tmp_all_valid_49)) && (_tmp_47 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_50;
        ram_c_0_wenable <= 1;
        _tmp_47 <= _tmp_47 - 1;
      end 
      if(_tmp_data_51 && (_tmp_valid_50 && ((_tmp_47 > 0) && !_tmp_48 && _tmp_all_valid_49)) && (_tmp_47 == 1)) begin
        _tmp_48 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_63_1 <= _tmp_63;
      __tmp_64_1 <= _tmp_64;
      if((_tmp_60 || !_tmp_58) && (_tmp_61 || !_tmp_59) && _tmp_66) begin
        _tmp_68 <= 0;
        _tmp_58 <= 0;
        _tmp_59 <= 0;
        _tmp_66 <= 0;
      end 
      if((_tmp_60 || !_tmp_58) && (_tmp_61 || !_tmp_59) && _tmp_65) begin
        _tmp_58 <= 1;
        _tmp_59 <= 1;
        _tmp_68 <= _tmp_67;
        _tmp_67 <= 0;
        _tmp_65 <= 0;
        _tmp_66 <= 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_69 == 0) && !_tmp_67 && !_tmp_68) begin
        ram_c_0_addr <= _tmp_52;
        _tmp_69 <= _tmp_54 - 1;
        _tmp_65 <= 1;
        _tmp_67 <= _tmp_54 == 1;
      end 
      if((_tmp_60 || !_tmp_58) && (_tmp_61 || !_tmp_59) && (_tmp_69 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_69 <= _tmp_69 - 1;
        _tmp_65 <= 1;
        _tmp_67 <= 0;
      end 
      if((_tmp_60 || !_tmp_58) && (_tmp_61 || !_tmp_59) && (_tmp_69 == 1)) begin
        _tmp_67 <= 1;
      end 
      if(th_sequential == 13) begin
        ram_c_0_addr <= _th_sequential_i_13 + _th_sequential_woffset_12;
        ram_c_0_wdata <= _th_sequential_sum_14;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_sequential == 13;
      __tmp_102_1 <= _tmp_102;
      __tmp_103_1 <= _tmp_103;
      if((_tmp_99 || !_tmp_97) && (_tmp_100 || !_tmp_98) && _tmp_105) begin
        _tmp_107 <= 0;
        _tmp_97 <= 0;
        _tmp_98 <= 0;
        _tmp_105 <= 0;
      end 
      if((_tmp_99 || !_tmp_97) && (_tmp_100 || !_tmp_98) && _tmp_104) begin
        _tmp_97 <= 1;
        _tmp_98 <= 1;
        _tmp_107 <= _tmp_106;
        _tmp_106 <= 0;
        _tmp_104 <= 0;
        _tmp_105 <= 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_108 == 0) && !_tmp_106 && !_tmp_107) begin
        ram_c_0_addr <= _tmp_91;
        _tmp_108 <= _tmp_93 - 1;
        _tmp_104 <= 1;
        _tmp_106 <= _tmp_93 == 1;
      end 
      if((_tmp_99 || !_tmp_97) && (_tmp_100 || !_tmp_98) && (_tmp_108 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_108 <= _tmp_108 - 1;
        _tmp_104 <= 1;
        _tmp_106 <= 0;
      end 
      if((_tmp_99 || !_tmp_97) && (_tmp_100 || !_tmp_98) && (_tmp_108 == 1)) begin
        _tmp_106 <= 1;
      end 
      if(th_comp == 25) begin
        ram_c_0_addr <= _th_comp_i_21 + _th_comp_offset_stream_18;
      end 
      _ram_c_cond_2_1 <= th_comp == 25;
      _ram_c_cond_3_1 <= th_comp == 25;
      if(th_comp == 27) begin
        ram_c_0_addr <= _th_comp_i_21 + _th_comp_offset_seq_19;
      end 
      _ram_c_cond_4_1 <= th_comp == 27;
      _ram_c_cond_5_1 <= th_comp == 27;
    end
  end

  assign _tmp_data_72 = _tmp_64;
  assign _tmp_valid_72 = _tmp_58;
  assign _tmp_60 = 1 && _tmp_ready_72;
  assign _tmp_data_111 = _tmp_103;
  assign _tmp_valid_111 = _tmp_97;
  assign _tmp_99 = 1 && _tmp_ready_111;
  reg [32-1:0] _tmp_data_117;
  reg _tmp_valid_117;
  wire _tmp_ready_117;
  wire [32-1:0] _tmp_data_118;
  wire _tmp_valid_118;
  wire _tmp_ready_118;
  wire [64-1:0] _tmp_odata_118;
  reg [64-1:0] _tmp_data_reg_118;
  assign _tmp_data_118 = _tmp_data_reg_118;
  wire _tmp_ovalid_118;
  reg _tmp_valid_reg_118;
  assign _tmp_valid_118 = _tmp_valid_reg_118;
  wire _tmp_enable_118;
  wire _tmp_update_118;
  assign _tmp_enable_118 = (_tmp_ready_118 || !_tmp_valid_118) && (_tmp_15 && _tmp_32) && (_tmp_13 && _tmp_30);
  assign _tmp_update_118 = _tmp_ready_118 || !_tmp_valid_118;

  multiplier_0
  mul118
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_118),
    .enable(_tmp_enable_118),
    .valid(_tmp_ovalid_118),
    .a(_tmp_19),
    .b(_tmp_36),
    .c(_tmp_odata_118)
  );

  assign _tmp_15 = 1 && ((_tmp_ready_118 || !_tmp_valid_118) && (_tmp_13 && _tmp_30));
  assign _tmp_32 = 1 && ((_tmp_ready_118 || !_tmp_valid_118) && (_tmp_13 && _tmp_30));
  reg [1-1:0] _tmp_data_119;
  reg _tmp_valid_119;
  wire _tmp_ready_119;
  assign _tmp_ready_117 = (_tmp_ready_119 || !_tmp_valid_119) && _tmp_valid_117;
  reg [1-1:0] _tmp_data_120;
  reg [1-1:0] _tmp_data_121;
  reg [1-1:0] _tmp_data_122;
  reg _tmp_valid_122;
  wire _tmp_ready_122;
  reg [1-1:0] _tmp_data_123;
  reg _tmp_valid_123;
  wire _tmp_ready_123;
  assign _tmp_ready_119 = (_tmp_ready_122 || !_tmp_valid_122) && _tmp_valid_119 && ((_tmp_ready_123 || !_tmp_valid_123) && _tmp_valid_119);
  reg [1-1:0] _tmp_data_124;
  reg _tmp_valid_124;
  wire _tmp_ready_124;
  assign _tmp_ready_122 = (_tmp_ready_124 || !_tmp_valid_124) && _tmp_valid_122;
  reg [1-1:0] _tmp_data_125;
  reg _tmp_valid_125;
  wire _tmp_ready_125;
  assign _tmp_ready_123 = (_tmp_ready_125 || !_tmp_valid_125) && _tmp_valid_123;
  reg [1-1:0] _tmp_data_126;
  reg _tmp_valid_126;
  wire _tmp_ready_126;
  assign _tmp_ready_124 = (_tmp_ready_126 || !_tmp_valid_126) && _tmp_valid_124;
  reg [1-1:0] _tmp_data_127;
  reg _tmp_valid_127;
  wire _tmp_ready_127;
  assign _tmp_ready_125 = (_tmp_ready_127 || !_tmp_valid_127) && _tmp_valid_125;
  reg [1-1:0] _tmp_data_128;
  reg _tmp_valid_128;
  wire _tmp_ready_128;
  assign _tmp_ready_126 = (_tmp_ready_128 || !_tmp_valid_128) && _tmp_valid_126;
  reg [1-1:0] _tmp_data_129;
  reg _tmp_valid_129;
  wire _tmp_ready_129;
  assign _tmp_ready_127 = (_tmp_ready_129 || !_tmp_valid_129) && _tmp_valid_127;
  reg [1-1:0] _tmp_data_130;
  reg _tmp_valid_130;
  wire _tmp_ready_130;
  assign _tmp_ready_128 = (_tmp_ready_130 || !_tmp_valid_130) && _tmp_valid_128;
  reg [1-1:0] _tmp_data_131;
  reg _tmp_valid_131;
  wire _tmp_ready_131;
  assign _tmp_ready_129 = (_tmp_ready_131 || !_tmp_valid_131) && _tmp_valid_129;
  reg [1-1:0] _tmp_data_132;
  reg _tmp_valid_132;
  wire _tmp_ready_132;
  assign _tmp_ready_130 = (_tmp_ready_132 || !_tmp_valid_132) && _tmp_valid_130;
  reg [1-1:0] _tmp_data_133;
  reg _tmp_valid_133;
  wire _tmp_ready_133;
  assign _tmp_ready_131 = (_tmp_ready_133 || !_tmp_valid_133) && _tmp_valid_131;
  reg [32-1:0] _tmp_data_134;
  reg _tmp_valid_134;
  wire _tmp_ready_134;
  assign _tmp_ready_118 = (_tmp_ready_134 || !_tmp_valid_134) && (_tmp_valid_118 && _tmp_valid_132);
  assign _tmp_ready_132 = (_tmp_ready_134 || !_tmp_valid_134) && (_tmp_valid_118 && _tmp_valid_132);
  reg [1-1:0] _tmp_data_135;
  reg _tmp_valid_135;
  wire _tmp_ready_135;
  assign _tmp_ready_133 = (_tmp_ready_135 || !_tmp_valid_135) && _tmp_valid_133;
  assign _tmp_data_50 = _tmp_data_134;
  assign _tmp_valid_50 = _tmp_valid_134;
  assign _tmp_ready_134 = _tmp_ready_50;
  assign _tmp_data_51 = _tmp_data_135;
  assign _tmp_valid_51 = _tmp_valid_135;
  assign _tmp_ready_135 = _tmp_ready_51;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_117 <= 1'sd0;
      _tmp_valid_117 <= 0;
      _tmp_data_reg_118 <= 0;
      _tmp_valid_reg_118 <= 0;
      _tmp_data_119 <= 0;
      _tmp_valid_119 <= 0;
      _tmp_data_120 <= 0;
      _tmp_data_121 <= 0;
      _tmp_data_122 <= 0;
      _tmp_valid_122 <= 0;
      _tmp_data_123 <= 0;
      _tmp_valid_123 <= 0;
      _tmp_data_124 <= 0;
      _tmp_valid_124 <= 0;
      _tmp_data_125 <= 0;
      _tmp_valid_125 <= 0;
      _tmp_data_126 <= 0;
      _tmp_valid_126 <= 0;
      _tmp_data_127 <= 0;
      _tmp_valid_127 <= 0;
      _tmp_data_128 <= 0;
      _tmp_valid_128 <= 0;
      _tmp_data_129 <= 0;
      _tmp_valid_129 <= 0;
      _tmp_data_130 <= 0;
      _tmp_valid_130 <= 0;
      _tmp_data_131 <= 0;
      _tmp_valid_131 <= 0;
      _tmp_data_132 <= 0;
      _tmp_valid_132 <= 0;
      _tmp_data_133 <= 0;
      _tmp_valid_133 <= 0;
      _tmp_data_134 <= 1'sd0;
      _tmp_valid_134 <= 0;
      _tmp_data_135 <= 0;
      _tmp_valid_135 <= 0;
    end else begin
      if((_tmp_ready_117 || !_tmp_valid_117) && 1 && 1) begin
        _tmp_data_117 <= (_tmp_data_117 >= 2)? 0 : _tmp_data_117 + 2'sd1;
      end 
      if(_tmp_valid_117 && _tmp_ready_117) begin
        _tmp_valid_117 <= 0;
      end 
      if((_tmp_ready_117 || !_tmp_valid_117) && 1) begin
        _tmp_valid_117 <= 1;
      end 
      if(_tmp_ready_118 || !_tmp_valid_118) begin
        _tmp_data_reg_118 <= _tmp_odata_118;
      end 
      if(_tmp_ready_118 || !_tmp_valid_118) begin
        _tmp_valid_reg_118 <= _tmp_ovalid_118;
      end 
      if((_tmp_ready_119 || !_tmp_valid_119) && _tmp_ready_117 && _tmp_valid_117) begin
        _tmp_data_119 <= _tmp_data_117 == 3'sd2;
      end 
      if(_tmp_valid_119 && _tmp_ready_119) begin
        _tmp_valid_119 <= 0;
      end 
      if((_tmp_ready_119 || !_tmp_valid_119) && _tmp_ready_117) begin
        _tmp_valid_119 <= _tmp_valid_117;
      end 
      if(_tmp_valid_119 && _tmp_ready_119) begin
        _tmp_data_120 <= _tmp_data_119;
      end 
      if(_tmp_valid_119 && _tmp_ready_119) begin
        _tmp_data_121 <= _tmp_data_120;
      end 
      if((_tmp_ready_122 || !_tmp_valid_122) && _tmp_ready_119 && _tmp_valid_119) begin
        _tmp_data_122 <= _tmp_data_121;
      end 
      if(_tmp_valid_122 && _tmp_ready_122) begin
        _tmp_valid_122 <= 0;
      end 
      if((_tmp_ready_122 || !_tmp_valid_122) && _tmp_ready_119) begin
        _tmp_valid_122 <= _tmp_valid_119;
      end 
      if((_tmp_ready_123 || !_tmp_valid_123) && _tmp_ready_119 && _tmp_valid_119) begin
        _tmp_data_123 <= _tmp_data_120;
      end 
      if(_tmp_valid_123 && _tmp_ready_123) begin
        _tmp_valid_123 <= 0;
      end 
      if((_tmp_ready_123 || !_tmp_valid_123) && _tmp_ready_119) begin
        _tmp_valid_123 <= _tmp_valid_119;
      end 
      if((_tmp_ready_124 || !_tmp_valid_124) && _tmp_ready_122 && _tmp_valid_122) begin
        _tmp_data_124 <= _tmp_data_122;
      end 
      if(_tmp_valid_124 && _tmp_ready_124) begin
        _tmp_valid_124 <= 0;
      end 
      if((_tmp_ready_124 || !_tmp_valid_124) && _tmp_ready_122) begin
        _tmp_valid_124 <= _tmp_valid_122;
      end 
      if((_tmp_ready_125 || !_tmp_valid_125) && _tmp_ready_123 && _tmp_valid_123) begin
        _tmp_data_125 <= _tmp_data_123;
      end 
      if(_tmp_valid_125 && _tmp_ready_125) begin
        _tmp_valid_125 <= 0;
      end 
      if((_tmp_ready_125 || !_tmp_valid_125) && _tmp_ready_123) begin
        _tmp_valid_125 <= _tmp_valid_123;
      end 
      if((_tmp_ready_126 || !_tmp_valid_126) && _tmp_ready_124 && _tmp_valid_124) begin
        _tmp_data_126 <= _tmp_data_124;
      end 
      if(_tmp_valid_126 && _tmp_ready_126) begin
        _tmp_valid_126 <= 0;
      end 
      if((_tmp_ready_126 || !_tmp_valid_126) && _tmp_ready_124) begin
        _tmp_valid_126 <= _tmp_valid_124;
      end 
      if((_tmp_ready_127 || !_tmp_valid_127) && _tmp_ready_125 && _tmp_valid_125) begin
        _tmp_data_127 <= _tmp_data_125;
      end 
      if(_tmp_valid_127 && _tmp_ready_127) begin
        _tmp_valid_127 <= 0;
      end 
      if((_tmp_ready_127 || !_tmp_valid_127) && _tmp_ready_125) begin
        _tmp_valid_127 <= _tmp_valid_125;
      end 
      if((_tmp_ready_128 || !_tmp_valid_128) && _tmp_ready_126 && _tmp_valid_126) begin
        _tmp_data_128 <= _tmp_data_126;
      end 
      if(_tmp_valid_128 && _tmp_ready_128) begin
        _tmp_valid_128 <= 0;
      end 
      if((_tmp_ready_128 || !_tmp_valid_128) && _tmp_ready_126) begin
        _tmp_valid_128 <= _tmp_valid_126;
      end 
      if((_tmp_ready_129 || !_tmp_valid_129) && _tmp_ready_127 && _tmp_valid_127) begin
        _tmp_data_129 <= _tmp_data_127;
      end 
      if(_tmp_valid_129 && _tmp_ready_129) begin
        _tmp_valid_129 <= 0;
      end 
      if((_tmp_ready_129 || !_tmp_valid_129) && _tmp_ready_127) begin
        _tmp_valid_129 <= _tmp_valid_127;
      end 
      if((_tmp_ready_130 || !_tmp_valid_130) && _tmp_ready_128 && _tmp_valid_128) begin
        _tmp_data_130 <= _tmp_data_128;
      end 
      if(_tmp_valid_130 && _tmp_ready_130) begin
        _tmp_valid_130 <= 0;
      end 
      if((_tmp_ready_130 || !_tmp_valid_130) && _tmp_ready_128) begin
        _tmp_valid_130 <= _tmp_valid_128;
      end 
      if((_tmp_ready_131 || !_tmp_valid_131) && _tmp_ready_129 && _tmp_valid_129) begin
        _tmp_data_131 <= _tmp_data_129;
      end 
      if(_tmp_valid_131 && _tmp_ready_131) begin
        _tmp_valid_131 <= 0;
      end 
      if((_tmp_ready_131 || !_tmp_valid_131) && _tmp_ready_129) begin
        _tmp_valid_131 <= _tmp_valid_129;
      end 
      if((_tmp_ready_132 || !_tmp_valid_132) && _tmp_ready_130 && _tmp_valid_130) begin
        _tmp_data_132 <= _tmp_data_130;
      end 
      if(_tmp_valid_132 && _tmp_ready_132) begin
        _tmp_valid_132 <= 0;
      end 
      if((_tmp_ready_132 || !_tmp_valid_132) && _tmp_ready_130) begin
        _tmp_valid_132 <= _tmp_valid_130;
      end 
      if((_tmp_ready_133 || !_tmp_valid_133) && _tmp_ready_131 && _tmp_valid_131) begin
        _tmp_data_133 <= _tmp_data_131;
      end 
      if(_tmp_valid_133 && _tmp_ready_133) begin
        _tmp_valid_133 <= 0;
      end 
      if((_tmp_ready_133 || !_tmp_valid_133) && _tmp_ready_131) begin
        _tmp_valid_133 <= _tmp_valid_131;
      end 
      if((_tmp_ready_134 || !_tmp_valid_134) && (_tmp_ready_118 && _tmp_ready_132) && (_tmp_valid_118 && _tmp_valid_132)) begin
        _tmp_data_134 <= _tmp_data_134 + _tmp_data_118;
      end 
      if(_tmp_valid_134 && _tmp_ready_134) begin
        _tmp_valid_134 <= 0;
      end 
      if((_tmp_ready_134 || !_tmp_valid_134) && (_tmp_ready_118 && _tmp_ready_132)) begin
        _tmp_valid_134 <= _tmp_valid_118 && _tmp_valid_132;
      end 
      if((_tmp_ready_134 || !_tmp_valid_134) && (_tmp_ready_118 && _tmp_ready_132) && (_tmp_valid_118 && _tmp_valid_132) && _tmp_data_132) begin
        _tmp_data_134 <= 1'sd0 + _tmp_data_118;
      end 
      if((_tmp_ready_135 || !_tmp_valid_135) && _tmp_ready_133 && _tmp_valid_133) begin
        _tmp_data_135 <= _tmp_data_133;
      end 
      if(_tmp_valid_135 && _tmp_ready_135) begin
        _tmp_valid_135 <= 0;
      end 
      if((_tmp_ready_135 || !_tmp_valid_135) && _tmp_ready_133) begin
        _tmp_valid_135 <= _tmp_valid_133;
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
  localparam th_comp_33 = 33;
  localparam th_comp_34 = 34;
  localparam th_comp_35 = 35;
  localparam th_comp_36 = 36;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_k_0 <= 0;
      _th_comp_roffset_1 <= 0;
      _th_comp_woffset_2 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_54 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _tmp_91 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 0;
      _th_comp_offset_stream_18 <= 0;
      _th_comp_offset_seq_19 <= 0;
      _th_comp_all_ok_20 <= 0;
      _th_comp_i_21 <= 0;
      _tmp_114 <= 0;
      _th_comp_st_22 <= 0;
      _tmp_116 <= 0;
      _th_comp_sq_23 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_k_0 <= 0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          if(_th_comp_k_0 < 3) begin
            th_comp <= th_comp_3;
          end else begin
            th_comp <= th_comp_5;
          end
        end
        th_comp_3: begin
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          _th_comp_k_0 <= _th_comp_k_0 + 1;
          th_comp <= th_comp_2;
        end
        th_comp_5: begin
          _th_comp_roffset_1 <= 0;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          _th_comp_woffset_2 <= 0;
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          _tmp_0 <= _th_comp_roffset_1;
          _tmp_1 <= 0;
          _tmp_2 <= 16;
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if(_tmp_12) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if(_mystream_flag_3 && _mystream_flag_5 && _mystream_flag_7) begin
            th_comp <= th_comp_11;
          end 
        end
        th_comp_11: begin
          _tmp_52 <= _th_comp_woffset_2;
          _tmp_53 <= 4096;
          _tmp_54 <= 14;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if(_tmp_73) begin
            th_comp <= th_comp_13;
          end 
        end
        th_comp_13: begin
          _th_comp_roffset_1 <= 16;
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          _th_comp_woffset_2 <= 14;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          _tmp_74 <= _th_comp_roffset_1;
          _tmp_75 <= 0;
          _tmp_76 <= 16;
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          if(_tmp_86) begin
            th_comp <= th_comp_17;
          end 
        end
        th_comp_17: begin
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          if(th_sequential == 15) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          _tmp_91 <= _th_comp_woffset_2;
          _tmp_92 <= 8192;
          _tmp_93 <= 14;
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          if(_tmp_112) begin
            th_comp <= th_comp_21;
          end 
        end
        th_comp_21: begin
          _th_comp_offset_stream_18 <= 0;
          _th_comp_offset_seq_19 <= _th_comp_woffset_2;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          _th_comp_all_ok_20 <= 1;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          _th_comp_i_21 <= 0;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          if(_th_comp_i_21 < 14) begin
            th_comp <= th_comp_25;
          end else begin
            th_comp <= th_comp_32;
          end
        end
        th_comp_25: begin
          if(_tmp_113) begin
            _tmp_114 <= ram_c_0_rdata;
          end 
          if(_tmp_113) begin
            th_comp <= th_comp_26;
          end 
        end
        th_comp_26: begin
          _th_comp_st_22 <= _tmp_114;
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          if(_tmp_115) begin
            _tmp_116 <= ram_c_0_rdata;
          end 
          if(_tmp_115) begin
            th_comp <= th_comp_28;
          end 
        end
        th_comp_28: begin
          _th_comp_sq_23 <= _tmp_116;
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          if(_th_comp_st_22 !== _th_comp_sq_23) begin
            th_comp <= th_comp_30;
          end else begin
            th_comp <= th_comp_31;
          end
        end
        th_comp_30: begin
          _th_comp_all_ok_20 <= 0;
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          _th_comp_i_21 <= _th_comp_i_21 + 1;
          th_comp <= th_comp_24;
        end
        th_comp_32: begin
          if(_th_comp_all_ok_20) begin
            th_comp <= th_comp_33;
          end else begin
            th_comp <= th_comp_35;
          end
        end
        th_comp_33: begin
          $display("OK");
          th_comp <= th_comp_34;
        end
        th_comp_34: begin
          th_comp <= th_comp_36;
        end
        th_comp_35: begin
          $display("NG");
          th_comp <= th_comp_36;
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
          if(th_comp == 8) begin
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

  localparam _mystream_fsm_4_1 = 1;
  localparam _mystream_fsm_4_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_4 <= _mystream_fsm_4_init;
      _mystream_flag_3 <= 0;
    end else begin
      case(_mystream_fsm_4)
        _mystream_fsm_4_init: begin
          if(th_comp == 9) begin
            _mystream_flag_3 <= 0;
          end 
          if(th_comp == 9) begin
            _mystream_fsm_4 <= _mystream_fsm_4_1;
          end 
        end
        _mystream_fsm_4_1: begin
          _mystream_fsm_4 <= _mystream_fsm_4_2;
        end
        _mystream_fsm_4_2: begin
          if(_tmp_23) begin
            _mystream_flag_3 <= 1;
          end 
          if(_tmp_23) begin
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
          if(th_comp == 9) begin
            _mystream_flag_5 <= 0;
          end 
          if(th_comp == 9) begin
            _mystream_fsm_6 <= _mystream_fsm_6_1;
          end 
        end
        _mystream_fsm_6_1: begin
          _mystream_fsm_6 <= _mystream_fsm_6_2;
        end
        _mystream_fsm_6_2: begin
          if(_tmp_40) begin
            _mystream_flag_5 <= 1;
          end 
          if(_tmp_40) begin
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
          if(th_comp == 9) begin
            _mystream_flag_7 <= 0;
          end 
          if(th_comp == 9) begin
            _mystream_fsm_8 <= _mystream_fsm_8_1;
          end 
        end
        _mystream_fsm_8_1: begin
          _mystream_fsm_8 <= _mystream_fsm_8_2;
        end
        _mystream_fsm_8_2: begin
          if(_tmp_48) begin
            _mystream_flag_7 <= 1;
          end 
          if(_tmp_48) begin
            _mystream_fsm_8 <= _mystream_fsm_8_init;
          end 
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
      _tmp_55 <= 0;
      _tmp_57 <= 0;
      _tmp_56 <= 0;
      _tmp_73 <= 0;
      __tmp_fsm_1_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_0_1) begin
            _tmp_73 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_comp == 12) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_55 <= (_tmp_53 >> 2) << 2;
          _tmp_57 <= _tmp_54;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_57 <= 256) && ((_tmp_55 & 4095) + (_tmp_57 << 2) >= 4096)) begin
            _tmp_56 <= 4096 - (_tmp_55 & 4095) >> 2;
            _tmp_57 <= _tmp_57 - (4096 - (_tmp_55 & 4095) >> 2);
          end else if(_tmp_57 <= 256) begin
            _tmp_56 <= _tmp_57;
            _tmp_57 <= 0;
          end else if((_tmp_55 & 4095) + 1024 >= 4096) begin
            _tmp_56 <= 4096 - (_tmp_55 & 4095) >> 2;
            _tmp_57 <= _tmp_57 - (4096 - (_tmp_55 & 4095) >> 2);
          end else begin
            _tmp_56 <= 256;
            _tmp_57 <= _tmp_57 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          if(_tmp_71 && myaxi_wvalid && myaxi_wready) begin
            _tmp_55 <= _tmp_55 + (_tmp_56 << 2);
          end 
          if(_tmp_71 && myaxi_wvalid && myaxi_wready && (_tmp_57 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(_tmp_71 && myaxi_wvalid && myaxi_wready && (_tmp_57 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_73 <= 1;
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
      _tmp_77 <= 0;
      _tmp_79 <= 0;
      _tmp_78 <= 0;
      __tmp_fsm_2_cond_4_0_1 <= 0;
      _tmp_81 <= 0;
      _tmp_80 <= 0;
      _tmp_86 <= 0;
      __tmp_fsm_2_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_0_1) begin
            _tmp_81 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_1_1) begin
            _tmp_86 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_comp == 16) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_77 <= (_tmp_75 >> 2) << 2;
          _tmp_79 <= _tmp_76;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_79 <= 256) && ((_tmp_77 & 4095) + (_tmp_79 << 2) >= 4096)) begin
            _tmp_78 <= 4096 - (_tmp_77 & 4095) >> 2;
            _tmp_79 <= _tmp_79 - (4096 - (_tmp_77 & 4095) >> 2);
          end else if(_tmp_79 <= 256) begin
            _tmp_78 <= _tmp_79;
            _tmp_79 <= 0;
          end else if((_tmp_77 & 4095) + 1024 >= 4096) begin
            _tmp_78 <= 4096 - (_tmp_77 & 4095) >> 2;
            _tmp_79 <= _tmp_79 - (4096 - (_tmp_77 & 4095) >> 2);
          end else begin
            _tmp_78 <= 256;
            _tmp_79 <= _tmp_79 - 256;
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
            _tmp_80 <= myaxi_rdata;
            _tmp_81 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_77 <= _tmp_77 + (_tmp_78 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_79 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_79 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_86 <= 1;
          __tmp_fsm_2_cond_5_1_1 <= 1;
          _tmp_fsm_2 <= _tmp_fsm_2_6;
        end
        _tmp_fsm_2_6: begin
          _tmp_fsm_2 <= _tmp_fsm_2_init;
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
  localparam th_sequential_13 = 13;
  localparam th_sequential_14 = 14;
  localparam th_sequential_15 = 15;

  always @(posedge CLK) begin
    if(RST) begin
      th_sequential <= th_sequential_init;
      _th_sequential_called <= 0;
      _th_sequential_roffset_9 <= 0;
      _th_sequential_woffset_10 <= 0;
      _th_sequential_roffset_11 <= 0;
      _th_sequential_woffset_12 <= 0;
      _th_sequential_i_13 <= 0;
      _th_sequential_sum_14 <= 0;
      _th_sequential_k_15 <= 0;
      _tmp_88 <= 0;
      _th_sequential_a_16 <= 0;
      _tmp_90 <= 0;
      _th_sequential_b_17 <= 0;
    end else begin
      case(th_sequential)
        th_sequential_init: begin
          if(th_comp == 17) begin
            _th_sequential_called <= 1;
          end 
          if(th_comp == 17) begin
            _th_sequential_roffset_9 <= _th_comp_roffset_1;
          end 
          if(th_comp == 17) begin
            _th_sequential_woffset_10 <= _th_comp_woffset_2;
          end 
          if(th_comp == 17) begin
            th_sequential <= th_sequential_1;
          end 
        end
        th_sequential_1: begin
          _th_sequential_roffset_11 <= _th_sequential_roffset_9;
          _th_sequential_woffset_12 <= _th_sequential_woffset_10;
          th_sequential <= th_sequential_2;
        end
        th_sequential_2: begin
          _th_sequential_i_13 <= 0;
          th_sequential <= th_sequential_3;
        end
        th_sequential_3: begin
          if(_th_sequential_i_13 < 14) begin
            th_sequential <= th_sequential_4;
          end else begin
            th_sequential <= th_sequential_15;
          end
        end
        th_sequential_4: begin
          _th_sequential_sum_14 <= 0;
          th_sequential <= th_sequential_5;
        end
        th_sequential_5: begin
          _th_sequential_k_15 <= 0;
          th_sequential <= th_sequential_6;
        end
        th_sequential_6: begin
          if(_th_sequential_k_15 < 3) begin
            th_sequential <= th_sequential_7;
          end else begin
            th_sequential <= th_sequential_13;
          end
        end
        th_sequential_7: begin
          if(_tmp_87) begin
            _tmp_88 <= ram_a_0_rdata;
          end 
          if(_tmp_87) begin
            th_sequential <= th_sequential_8;
          end 
        end
        th_sequential_8: begin
          _th_sequential_a_16 <= _tmp_88;
          th_sequential <= th_sequential_9;
        end
        th_sequential_9: begin
          if(_tmp_89) begin
            _tmp_90 <= ram_b_0_rdata;
          end 
          if(_tmp_89) begin
            th_sequential <= th_sequential_10;
          end 
        end
        th_sequential_10: begin
          _th_sequential_b_17 <= _tmp_90;
          th_sequential <= th_sequential_11;
        end
        th_sequential_11: begin
          _th_sequential_sum_14 <= _th_sequential_sum_14 + _th_sequential_a_16 * _th_sequential_b_17;
          th_sequential <= th_sequential_12;
        end
        th_sequential_12: begin
          _th_sequential_k_15 <= _th_sequential_k_15 + 1;
          th_sequential <= th_sequential_6;
        end
        th_sequential_13: begin
          th_sequential <= th_sequential_14;
        end
        th_sequential_14: begin
          _th_sequential_i_13 <= _th_sequential_i_13 + 1;
          th_sequential <= th_sequential_3;
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
      _tmp_112 <= 0;
      __tmp_fsm_3_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_0_1) begin
            _tmp_112 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_comp == 20) begin
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
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_3 <= _tmp_fsm_3_4;
          end 
        end
        _tmp_fsm_3_4: begin
          if(_tmp_110 && myaxi_wvalid && myaxi_wready) begin
            _tmp_94 <= _tmp_94 + (_tmp_95 << 2);
          end 
          if(_tmp_110 && myaxi_wvalid && myaxi_wready && (_tmp_96 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(_tmp_110 && myaxi_wvalid && myaxi_wready && (_tmp_96 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_112 <= 1;
          __tmp_fsm_3_cond_5_0_1 <= 1;
          _tmp_fsm_3 <= _tmp_fsm_3_6;
        end
        _tmp_fsm_3_6: begin
          _tmp_fsm_3 <= _tmp_fsm_3_init;
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
    test_module = thread_stream_conv1d.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
