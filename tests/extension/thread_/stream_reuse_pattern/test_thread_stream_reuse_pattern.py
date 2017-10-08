from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_reuse_pattern

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
  reg signed [32-1:0] _th_comp_roffset_0;
  reg signed [32-1:0] _th_comp_woffset_1;
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
  wire [32-1:0] __variable_data_10;
  wire __variable_valid_10;
  wire __variable_ready_10;
  assign __variable_ready_10 = (_tmp_8 > 0) && !_tmp_9;
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
  wire [32-1:0] __variable_data_23;
  wire __variable_valid_23;
  wire __variable_ready_23;
  assign __variable_ready_23 = (_tmp_21 > 0) && !_tmp_22;
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
  reg _mystream_running_reg;
  wire _mystream_running;
  reg signed [32-1:0] _mystream_roffset_2;
  reg signed [32-1:0] _mystream_woffset_3;
  reg _mystream_done_flag_4;
  reg [32-1:0] _mystream_fsm_5;
  localparam _mystream_fsm_5_init = 0;
  reg _tmp_26;
  reg _tmp_27;
  wire _tmp_28;
  wire _tmp_29;
  assign _tmp_29 = 1;
  wire [10-1:0] _tmp_30;
  wire [10-1:0] _tmp_31;
  reg [10-1:0] _tmp_32;
  reg [10-1:0] _tmp_33;
  assign _tmp_31 = _tmp_33 + (_tmp_32 + _mystream_roffset_2);
  reg [4-1:0] _tmp_34;
  reg [4-1:0] _tmp_35;
  reg [4-1:0] _tmp_36;
  reg _tmp_37;
  reg signed [32-1:0] _tmp_38;
  reg signed [32-1:0] _tmp_39;
  reg [4-1:0] _tmp_40;
  reg _tmp_41;
  reg _tmp_42;
  reg _tmp_43;
  assign _tmp_30 = ((0 && 0)? _tmp_36 == 0 : _tmp_34 == 0)? _tmp_31 : ram_a_0_addr + ((0 && 0)? 16 : 4);
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg [32-1:0] _d2__tmp_fsm_2;
  reg __tmp_fsm_2_cond_1_0_1;
  reg __tmp_fsm_2_cond_1_0_2;
  reg __tmp_fsm_2_cond_1_1_1;
  reg __tmp_fsm_2_cond_1_1_2;
  reg __tmp_fsm_2_cond_1_2_1;
  reg __tmp_fsm_2_cond_1_2_2;
  reg __tmp_fsm_2_cond_4_3_1;
  reg __tmp_fsm_2_cond_5_4_1;
  reg __tmp_fsm_2_cond_5_4_2;
  reg __tmp_fsm_2_cond_5_5_1;
  reg __tmp_fsm_2_cond_5_5_2;
  reg __tmp_fsm_2_cond_5_6_1;
  reg __tmp_fsm_2_cond_5_6_2;
  reg __tmp_fsm_2_cond_8_7_1;
  reg _mystream_done_flag_6;
  reg [32-1:0] _mystream_fsm_7;
  localparam _mystream_fsm_7_init = 0;
  reg _tmp_44;
  reg _tmp_45;
  wire _tmp_46;
  wire _tmp_47;
  assign _tmp_47 = 1;
  wire [10-1:0] _tmp_48;
  wire [10-1:0] _tmp_49;
  reg [10-1:0] _tmp_50;
  reg [10-1:0] _tmp_51;
  assign _tmp_49 = _tmp_51 + (_tmp_50 + _mystream_roffset_2);
  reg [4-1:0] _tmp_52;
  reg [4-1:0] _tmp_53;
  reg [4-1:0] _tmp_54;
  reg _tmp_55;
  reg signed [32-1:0] _tmp_56;
  reg signed [32-1:0] _tmp_57;
  reg [4-1:0] _tmp_58;
  reg _tmp_59;
  reg _tmp_60;
  reg _tmp_61;
  assign _tmp_48 = ((0 && 0)? _tmp_54 == 0 : _tmp_52 == 0)? _tmp_49 : ram_b_0_addr + ((0 && 0)? 16 : 4);
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg [32-1:0] _d2__tmp_fsm_3;
  reg __tmp_fsm_3_cond_1_0_1;
  reg __tmp_fsm_3_cond_1_0_2;
  reg __tmp_fsm_3_cond_1_1_1;
  reg __tmp_fsm_3_cond_1_1_2;
  reg __tmp_fsm_3_cond_1_2_1;
  reg __tmp_fsm_3_cond_1_2_2;
  reg __tmp_fsm_3_cond_4_3_1;
  reg __tmp_fsm_3_cond_5_4_1;
  reg __tmp_fsm_3_cond_5_4_2;
  reg __tmp_fsm_3_cond_5_5_1;
  reg __tmp_fsm_3_cond_5_5_2;
  reg __tmp_fsm_3_cond_5_6_1;
  reg __tmp_fsm_3_cond_5_6_2;
  reg __tmp_fsm_3_cond_8_7_1;
  reg _mystream_done_flag_8;
  reg [32-1:0] _mystream_fsm_9;
  localparam _mystream_fsm_9_init = 0;
  reg [10-1:0] _tmp_62;
  reg _tmp_63;
  wire signed [32-1:0] _plus_data_64;
  wire _plus_valid_64;
  wire _plus_ready_64;
  assign _plus_ready_64 = (_tmp_62 > 0) && !_tmp_63;
  reg _ram_c_cond_0_1;
  assign _mystream_running = _mystream_running_reg && !(_mystream_done_flag_4 && _mystream_done_flag_6 && _mystream_done_flag_8);
  reg [10-1:0] _tmp_65;
  reg [32-1:0] _tmp_66;
  reg [32-1:0] _tmp_67;
  reg [32-1:0] _tmp_fsm_4;
  localparam _tmp_fsm_4_init = 0;
  reg [32-1:0] _tmp_68;
  reg [33-1:0] _tmp_69;
  reg [33-1:0] _tmp_70;
  reg _tmp_71;
  reg _tmp_72;
  wire _tmp_73;
  wire _tmp_74;
  assign _tmp_74 = 1;
  localparam _tmp_75 = 1;
  wire [_tmp_75-1:0] _tmp_76;
  assign _tmp_76 = (_tmp_73 || !_tmp_71) && (_tmp_74 || !_tmp_72);
  reg [_tmp_75-1:0] __tmp_76_1;
  wire signed [32-1:0] _tmp_77;
  reg signed [32-1:0] __tmp_77_1;
  assign _tmp_77 = (__tmp_76_1)? ram_c_0_rdata : __tmp_77_1;
  reg _tmp_78;
  reg _tmp_79;
  reg _tmp_80;
  reg _tmp_81;
  reg [33-1:0] _tmp_82;
  reg [9-1:0] _tmp_83;
  reg _myaxi_cond_2_1;
  reg _tmp_84;
  wire [32-1:0] __variable_data_85;
  wire __variable_valid_85;
  wire __variable_ready_85;
  assign __variable_ready_85 = (_tmp_fsm_4 == 4) && ((_tmp_83 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_86;
  reg [32-1:0] _d1__tmp_fsm_4;
  reg __tmp_fsm_4_cond_5_0_1;
  reg [10-1:0] _tmp_87;
  reg [32-1:0] _tmp_88;
  reg [32-1:0] _tmp_89;
  reg [32-1:0] _tmp_fsm_5;
  localparam _tmp_fsm_5_init = 0;
  reg [32-1:0] _tmp_90;
  reg [33-1:0] _tmp_91;
  reg [33-1:0] _tmp_92;
  reg [32-1:0] _tmp_93;
  reg _tmp_94;
  reg [33-1:0] _tmp_95;
  reg _tmp_96;
  wire [32-1:0] __variable_data_97;
  wire __variable_valid_97;
  wire __variable_ready_97;
  assign __variable_ready_97 = (_tmp_95 > 0) && !_tmp_96;
  reg _ram_a_cond_1_1;
  reg [9-1:0] _tmp_98;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_5;
  reg __tmp_fsm_5_cond_4_0_1;
  reg _tmp_99;
  reg __tmp_fsm_5_cond_5_1_1;
  reg [10-1:0] _tmp_100;
  reg [32-1:0] _tmp_101;
  reg [32-1:0] _tmp_102;
  reg [32-1:0] _tmp_fsm_6;
  localparam _tmp_fsm_6_init = 0;
  reg [32-1:0] _tmp_103;
  reg [33-1:0] _tmp_104;
  reg [33-1:0] _tmp_105;
  reg [32-1:0] _tmp_106;
  reg _tmp_107;
  reg [33-1:0] _tmp_108;
  reg _tmp_109;
  wire [32-1:0] __variable_data_110;
  wire __variable_valid_110;
  wire __variable_ready_110;
  assign __variable_ready_110 = (_tmp_108 > 0) && !_tmp_109;
  reg _ram_b_cond_1_1;
  reg [9-1:0] _tmp_111;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_1 == 4) || (_tmp_fsm_5 == 4) || (_tmp_fsm_6 == 4);
  reg [32-1:0] _d1__tmp_fsm_6;
  reg __tmp_fsm_6_cond_4_0_1;
  reg _tmp_112;
  reg __tmp_fsm_6_cond_5_1_1;
  reg [32-1:0] th_sequential;
  localparam th_sequential_init = 0;
  reg _th_sequential_called;
  reg signed [32-1:0] _th_sequential_roffset_10;
  reg signed [32-1:0] _th_sequential_woffset_11;
  reg signed [32-1:0] _th_sequential_roffset_12;
  reg signed [32-1:0] _th_sequential_woffset_13;
  reg signed [32-1:0] _th_sequential_sum_14;
  reg signed [32-1:0] _th_sequential_w_15;
  reg signed [32-1:0] _th_sequential_i_16;
  reg signed [32-1:0] _th_sequential_k_17;
  reg signed [32-1:0] _th_sequential_j_18;
  reg signed [32-1:0] _th_sequential_r_19;
  reg signed [32-1:0] _th_sequential_addr_20;
  reg _tmp_113;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_3_2;
  reg signed [32-1:0] _tmp_114;
  reg signed [32-1:0] _th_sequential_a_21;
  reg _tmp_115;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_3_2;
  reg signed [32-1:0] _tmp_116;
  reg signed [32-1:0] _th_sequential_b_22;
  reg _ram_c_cond_1_1;
  reg [10-1:0] _tmp_117;
  reg [32-1:0] _tmp_118;
  reg [32-1:0] _tmp_119;
  reg [32-1:0] _tmp_fsm_7;
  localparam _tmp_fsm_7_init = 0;
  reg [32-1:0] _tmp_120;
  reg [33-1:0] _tmp_121;
  reg [33-1:0] _tmp_122;
  reg _tmp_123;
  reg _tmp_124;
  wire _tmp_125;
  wire _tmp_126;
  assign _tmp_126 = 1;
  localparam _tmp_127 = 1;
  wire [_tmp_127-1:0] _tmp_128;
  assign _tmp_128 = (_tmp_125 || !_tmp_123) && (_tmp_126 || !_tmp_124);
  reg [_tmp_127-1:0] __tmp_128_1;
  wire signed [32-1:0] _tmp_129;
  reg signed [32-1:0] __tmp_129_1;
  assign _tmp_129 = (__tmp_128_1)? ram_c_0_rdata : __tmp_129_1;
  reg _tmp_130;
  reg _tmp_131;
  reg _tmp_132;
  reg _tmp_133;
  reg [33-1:0] _tmp_134;
  reg [9-1:0] _tmp_135;
  reg _myaxi_cond_6_1;
  reg _tmp_136;
  wire [32-1:0] __variable_data_137;
  wire __variable_valid_137;
  wire __variable_ready_137;
  assign __variable_ready_137 = (_tmp_fsm_7 == 4) && ((_tmp_135 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_7_1;
  reg _tmp_138;
  reg [32-1:0] _d1__tmp_fsm_7;
  reg __tmp_fsm_7_cond_5_0_1;
  reg signed [32-1:0] _th_comp_size_23;
  reg signed [32-1:0] _th_comp_offset_stream_24;
  reg signed [32-1:0] _th_comp_offset_seq_25;
  reg signed [32-1:0] _th_comp_all_ok_26;
  reg signed [32-1:0] _th_comp_i_27;
  reg _tmp_139;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_140;
  reg signed [32-1:0] _th_comp_st_28;
  reg _tmp_141;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_142;
  reg signed [32-1:0] _th_comp_sq_29;

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
      _tmp_83 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_84 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_98 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_111 <= 0;
      _myaxi_cond_5_1 <= 0;
      _tmp_135 <= 0;
      _myaxi_cond_6_1 <= 0;
      _tmp_136 <= 0;
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
        _tmp_84 <= 0;
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
        _tmp_136 <= 0;
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
      if((_tmp_fsm_4 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_83 == 0))) begin
        myaxi_awaddr <= _tmp_68;
        myaxi_awlen <= _tmp_69 - 1;
        myaxi_awvalid <= 1;
        _tmp_83 <= _tmp_69;
      end 
      if((_tmp_fsm_4 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_83 == 0)) && (_tmp_69 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_85 && ((_tmp_fsm_4 == 4) && ((_tmp_83 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_83 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_83 > 0))) begin
        myaxi_wdata <= __variable_data_85;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_83 <= _tmp_83 - 1;
      end 
      if(__variable_valid_85 && ((_tmp_fsm_4 == 4) && ((_tmp_83 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_83 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_83 > 0)) && (_tmp_83 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_84 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_84 <= _tmp_84;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_98 == 0))) begin
        myaxi_araddr <= _tmp_90;
        myaxi_arlen <= _tmp_91 - 1;
        myaxi_arvalid <= 1;
        _tmp_98 <= _tmp_91;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_98 > 0)) begin
        _tmp_98 <= _tmp_98 - 1;
      end 
      if((_tmp_fsm_6 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_111 == 0))) begin
        myaxi_araddr <= _tmp_103;
        myaxi_arlen <= _tmp_104 - 1;
        myaxi_arvalid <= 1;
        _tmp_111 <= _tmp_104;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_111 > 0)) begin
        _tmp_111 <= _tmp_111 - 1;
      end 
      if((_tmp_fsm_7 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_135 == 0))) begin
        myaxi_awaddr <= _tmp_120;
        myaxi_awlen <= _tmp_121 - 1;
        myaxi_awvalid <= 1;
        _tmp_135 <= _tmp_121;
      end 
      if((_tmp_fsm_7 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_135 == 0)) && (_tmp_121 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_6_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_137 && ((_tmp_fsm_7 == 4) && ((_tmp_135 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_135 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_135 > 0))) begin
        myaxi_wdata <= __variable_data_137;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_135 <= _tmp_135 - 1;
      end 
      if(__variable_valid_137 && ((_tmp_fsm_7 == 4) && ((_tmp_135 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_135 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_135 > 0)) && (_tmp_135 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_136 <= 1;
      end 
      _myaxi_cond_7_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_136 <= _tmp_136;
      end 
    end
  end

  assign __variable_data_10 = _tmp_6;
  assign __variable_valid_10 = _tmp_7;
  assign __variable_data_23 = _tmp_19;
  assign __variable_valid_23 = _tmp_20;
  assign __variable_data_97 = _tmp_93;
  assign __variable_valid_97 = _tmp_94;
  assign __variable_data_110 = _tmp_106;
  assign __variable_valid_110 = _tmp_107;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_8 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_9 <= 0;
      _ram_a_cond_0_1 <= 0;
      _tmp_37 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_40 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 0;
      _ram_a_cond_1_1 <= 0;
      _ram_a_cond_2_1 <= 0;
      _tmp_113 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_3_2 <= 0;
    end else begin
      if(_ram_a_cond_3_2) begin
        _tmp_113 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_9 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        ram_a_0_wenable <= 0;
        _tmp_96 <= 0;
      end 
      if(_ram_a_cond_2_1) begin
        _tmp_113 <= 1;
      end 
      _ram_a_cond_3_2 <= _ram_a_cond_3_1;
      if((_tmp_fsm_0 == 1) && (_tmp_8 == 0)) begin
        ram_a_0_addr <= _tmp_0 - 1;
        _tmp_8 <= _tmp_2;
      end 
      if(__variable_valid_10 && ((_tmp_8 > 0) && !_tmp_9) && (_tmp_8 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= __variable_data_10;
        ram_a_0_wenable <= 1;
        _tmp_8 <= _tmp_8 - 1;
      end 
      if(__variable_valid_10 && ((_tmp_8 > 0) && !_tmp_9) && (_tmp_8 == 1)) begin
        _tmp_9 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_27) begin
        _tmp_37 <= 0;
        _tmp_26 <= 0;
        _tmp_27 <= 0;
      end 
      if(_tmp_41) begin
        _tmp_40 <= 4;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_40 > 0)) begin
        _tmp_40 <= _tmp_40 - 1;
        _tmp_26 <= 1;
        _tmp_27 <= 1;
        _tmp_37 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_40 == 1) && _tmp_43) begin
        _tmp_37 <= 1;
      end 
      if((_tmp_fsm_5 == 1) && (_tmp_95 == 0)) begin
        ram_a_0_addr <= _tmp_87 - 1;
        _tmp_95 <= _tmp_89;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= __variable_data_97;
        ram_a_0_wenable <= 1;
        _tmp_95 <= _tmp_95 - 1;
      end 
      if(__variable_valid_97 && ((_tmp_95 > 0) && !_tmp_96) && (_tmp_95 == 1)) begin
        _tmp_96 <= 1;
      end 
      _ram_a_cond_1_1 <= 1;
      if(th_sequential == 13) begin
        ram_a_0_addr <= _th_sequential_addr_20 + _th_sequential_roffset_12;
      end 
      _ram_a_cond_2_1 <= th_sequential == 13;
      _ram_a_cond_3_1 <= th_sequential == 13;
    end
  end

  reg signed [32-1:0] _plus_data_143;
  reg _plus_valid_143;
  wire _plus_ready_143;
  assign _tmp_28 = 1 && ((_plus_ready_143 || !_plus_valid_143) && (_tmp_26 && _tmp_44));
  assign _tmp_46 = 1 && ((_plus_ready_143 || !_plus_valid_143) && (_tmp_26 && _tmp_44));
  assign _plus_data_64 = _plus_data_143;
  assign _plus_valid_64 = _plus_valid_143;
  assign _plus_ready_143 = _plus_ready_64;

  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_143 <= 0;
      _plus_valid_143 <= 0;
    end else begin
      if((_plus_ready_143 || !_plus_valid_143) && (_tmp_28 && _tmp_46) && (_tmp_26 && _tmp_44)) begin
        _plus_data_143 <= _tmp_38 + _tmp_56;
      end 
      if(_plus_valid_143 && _plus_ready_143) begin
        _plus_valid_143 <= 0;
      end 
      if((_plus_ready_143 || !_plus_valid_143) && (_tmp_28 && _tmp_46)) begin
        _plus_valid_143 <= _tmp_26 && _tmp_44;
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
      _tmp_55 <= 0;
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _tmp_58 <= 0;
      _tmp_108 <= 0;
      _tmp_109 <= 0;
      _ram_b_cond_1_1 <= 0;
      _ram_b_cond_2_1 <= 0;
      _tmp_115 <= 0;
      _ram_b_cond_3_1 <= 0;
      _ram_b_cond_3_2 <= 0;
    end else begin
      if(_ram_b_cond_3_2) begin
        _tmp_115 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_22 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        ram_b_0_wenable <= 0;
        _tmp_109 <= 0;
      end 
      if(_ram_b_cond_2_1) begin
        _tmp_115 <= 1;
      end 
      _ram_b_cond_3_2 <= _ram_b_cond_3_1;
      if((_tmp_fsm_1 == 1) && (_tmp_21 == 0)) begin
        ram_b_0_addr <= _tmp_13 - 1;
        _tmp_21 <= _tmp_15;
      end 
      if(__variable_valid_23 && ((_tmp_21 > 0) && !_tmp_22) && (_tmp_21 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= __variable_data_23;
        ram_b_0_wenable <= 1;
        _tmp_21 <= _tmp_21 - 1;
      end 
      if(__variable_valid_23 && ((_tmp_21 > 0) && !_tmp_22) && (_tmp_21 == 1)) begin
        _tmp_22 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && _tmp_45) begin
        _tmp_55 <= 0;
        _tmp_44 <= 0;
        _tmp_45 <= 0;
      end 
      if(_tmp_59) begin
        _tmp_58 <= 4;
      end 
      if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && (_tmp_58 > 0)) begin
        _tmp_58 <= _tmp_58 - 1;
        _tmp_44 <= 1;
        _tmp_45 <= 1;
        _tmp_55 <= 0;
      end 
      if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && (_tmp_58 == 1) && _tmp_61) begin
        _tmp_55 <= 1;
      end 
      if((_tmp_fsm_6 == 1) && (_tmp_108 == 0)) begin
        ram_b_0_addr <= _tmp_100 - 1;
        _tmp_108 <= _tmp_102;
      end 
      if(__variable_valid_110 && ((_tmp_108 > 0) && !_tmp_109) && (_tmp_108 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= __variable_data_110;
        ram_b_0_wenable <= 1;
        _tmp_108 <= _tmp_108 - 1;
      end 
      if(__variable_valid_110 && ((_tmp_108 > 0) && !_tmp_109) && (_tmp_108 == 1)) begin
        _tmp_109 <= 1;
      end 
      _ram_b_cond_1_1 <= 1;
      if(th_sequential == 15) begin
        ram_b_0_addr <= _th_sequential_addr_20 + _th_sequential_roffset_12;
      end 
      _ram_b_cond_2_1 <= th_sequential == 15;
      _ram_b_cond_3_1 <= th_sequential == 15;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_62 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_63 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_76_1 <= 0;
      __tmp_77_1 <= 0;
      _tmp_81 <= 0;
      _tmp_71 <= 0;
      _tmp_72 <= 0;
      _tmp_79 <= 0;
      _tmp_80 <= 0;
      _tmp_78 <= 0;
      _tmp_82 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_128_1 <= 0;
      __tmp_129_1 <= 0;
      _tmp_133 <= 0;
      _tmp_123 <= 0;
      _tmp_124 <= 0;
      _tmp_131 <= 0;
      _tmp_132 <= 0;
      _tmp_130 <= 0;
      _tmp_134 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_139 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_141 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_139 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_141 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_63 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_139 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_141 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if((_mystream_fsm_9 == 1) && (_tmp_62 == 0)) begin
        ram_c_0_addr <= _mystream_woffset_3 - 1;
        _tmp_62 <= 256;
      end 
      if(_plus_valid_64 && ((_tmp_62 > 0) && !_tmp_63) && (_tmp_62 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _plus_data_64;
        ram_c_0_wenable <= 1;
        _tmp_62 <= _tmp_62 - 1;
      end 
      if(_plus_valid_64 && ((_tmp_62 > 0) && !_tmp_63) && (_tmp_62 == 1)) begin
        _tmp_63 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_76_1 <= _tmp_76;
      __tmp_77_1 <= _tmp_77;
      if((_tmp_73 || !_tmp_71) && (_tmp_74 || !_tmp_72) && _tmp_79) begin
        _tmp_81 <= 0;
        _tmp_71 <= 0;
        _tmp_72 <= 0;
        _tmp_79 <= 0;
      end 
      if((_tmp_73 || !_tmp_71) && (_tmp_74 || !_tmp_72) && _tmp_78) begin
        _tmp_71 <= 1;
        _tmp_72 <= 1;
        _tmp_81 <= _tmp_80;
        _tmp_80 <= 0;
        _tmp_78 <= 0;
        _tmp_79 <= 1;
      end 
      if((_tmp_fsm_4 == 1) && (_tmp_82 == 0) && !_tmp_80 && !_tmp_81) begin
        ram_c_0_addr <= _tmp_65;
        _tmp_82 <= _tmp_67 - 1;
        _tmp_78 <= 1;
        _tmp_80 <= _tmp_67 == 1;
      end 
      if((_tmp_73 || !_tmp_71) && (_tmp_74 || !_tmp_72) && (_tmp_82 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_82 <= _tmp_82 - 1;
        _tmp_78 <= 1;
        _tmp_80 <= 0;
      end 
      if((_tmp_73 || !_tmp_71) && (_tmp_74 || !_tmp_72) && (_tmp_82 == 1)) begin
        _tmp_80 <= 1;
      end 
      if(th_sequential == 18) begin
        ram_c_0_addr <= _th_sequential_w_15 + _th_sequential_woffset_13;
        ram_c_0_wdata <= _th_sequential_sum_14;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_sequential == 18;
      __tmp_128_1 <= _tmp_128;
      __tmp_129_1 <= _tmp_129;
      if((_tmp_125 || !_tmp_123) && (_tmp_126 || !_tmp_124) && _tmp_131) begin
        _tmp_133 <= 0;
        _tmp_123 <= 0;
        _tmp_124 <= 0;
        _tmp_131 <= 0;
      end 
      if((_tmp_125 || !_tmp_123) && (_tmp_126 || !_tmp_124) && _tmp_130) begin
        _tmp_123 <= 1;
        _tmp_124 <= 1;
        _tmp_133 <= _tmp_132;
        _tmp_132 <= 0;
        _tmp_130 <= 0;
        _tmp_131 <= 1;
      end 
      if((_tmp_fsm_7 == 1) && (_tmp_134 == 0) && !_tmp_132 && !_tmp_133) begin
        ram_c_0_addr <= _tmp_117;
        _tmp_134 <= _tmp_119 - 1;
        _tmp_130 <= 1;
        _tmp_132 <= _tmp_119 == 1;
      end 
      if((_tmp_125 || !_tmp_123) && (_tmp_126 || !_tmp_124) && (_tmp_134 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_134 <= _tmp_134 - 1;
        _tmp_130 <= 1;
        _tmp_132 <= 0;
      end 
      if((_tmp_125 || !_tmp_123) && (_tmp_126 || !_tmp_124) && (_tmp_134 == 1)) begin
        _tmp_132 <= 1;
      end 
      if(th_comp == 27) begin
        ram_c_0_addr <= _th_comp_i_27 + _th_comp_offset_stream_24;
      end 
      _ram_c_cond_2_1 <= th_comp == 27;
      _ram_c_cond_3_1 <= th_comp == 27;
      if(th_comp == 29) begin
        ram_c_0_addr <= _th_comp_i_27 + _th_comp_offset_seq_25;
      end 
      _ram_c_cond_4_1 <= th_comp == 29;
      _ram_c_cond_5_1 <= th_comp == 29;
    end
  end

  assign __variable_data_85 = _tmp_77;
  assign __variable_valid_85 = _tmp_71;
  assign _tmp_73 = 1 && __variable_ready_85;
  assign __variable_data_137 = _tmp_129;
  assign __variable_valid_137 = _tmp_123;
  assign _tmp_125 = 1 && __variable_ready_137;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_roffset_0 <= 0;
      _th_comp_woffset_1 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_67 <= 0;
      _tmp_87 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _tmp_100 <= 0;
      _tmp_101 <= 0;
      _tmp_102 <= 0;
      _tmp_117 <= 0;
      _tmp_118 <= 0;
      _tmp_119 <= 0;
      _th_comp_size_23 <= 0;
      _th_comp_offset_stream_24 <= 0;
      _th_comp_offset_seq_25 <= 0;
      _th_comp_all_ok_26 <= 0;
      _th_comp_i_27 <= 0;
      _tmp_140 <= 0;
      _th_comp_st_28 <= 0;
      _tmp_142 <= 0;
      _th_comp_sq_29 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_roffset_0 <= 0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          _th_comp_woffset_1 <= 0;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          _tmp_0 <= _th_comp_roffset_0;
          _tmp_1 <= 0;
          _tmp_2 <= 64;
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          if(_tmp_12) begin
            th_comp <= th_comp_5;
          end 
        end
        th_comp_5: begin
          _tmp_13 <= _th_comp_roffset_0;
          _tmp_14 <= 0;
          _tmp_15 <= 64;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          if(_tmp_25) begin
            th_comp <= th_comp_7;
          end 
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if(!_mystream_running) begin
            th_comp <= th_comp_11;
          end 
        end
        th_comp_11: begin
          _tmp_65 <= _th_comp_woffset_1;
          _tmp_66 <= 1024;
          _tmp_67 <= 64;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if(_tmp_86) begin
            th_comp <= th_comp_13;
          end 
        end
        th_comp_13: begin
          _th_comp_roffset_0 <= 64;
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          _th_comp_woffset_1 <= 128;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          _tmp_87 <= _th_comp_roffset_0;
          _tmp_88 <= 0;
          _tmp_89 <= 64;
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          if(_tmp_99) begin
            th_comp <= th_comp_17;
          end 
        end
        th_comp_17: begin
          _tmp_100 <= _th_comp_roffset_0;
          _tmp_101 <= 0;
          _tmp_102 <= 64;
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          if(_tmp_112) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          if(th_sequential == 24) begin
            th_comp <= th_comp_21;
          end 
        end
        th_comp_21: begin
          _tmp_117 <= _th_comp_woffset_1;
          _tmp_118 <= 2048;
          _tmp_119 <= 64;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          if(_tmp_138) begin
            th_comp <= th_comp_23;
          end 
        end
        th_comp_23: begin
          _th_comp_size_23 <= 64;
          _th_comp_offset_stream_24 <= 0;
          _th_comp_offset_seq_25 <= _th_comp_woffset_1;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          _th_comp_all_ok_26 <= 1;
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          _th_comp_i_27 <= 0;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          if(_th_comp_i_27 < _th_comp_size_23) begin
            th_comp <= th_comp_27;
          end else begin
            th_comp <= th_comp_34;
          end
        end
        th_comp_27: begin
          if(_tmp_139) begin
            _tmp_140 <= ram_c_0_rdata;
          end 
          if(_tmp_139) begin
            th_comp <= th_comp_28;
          end 
        end
        th_comp_28: begin
          _th_comp_st_28 <= _tmp_140;
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          if(_tmp_141) begin
            _tmp_142 <= ram_c_0_rdata;
          end 
          if(_tmp_141) begin
            th_comp <= th_comp_30;
          end 
        end
        th_comp_30: begin
          _th_comp_sq_29 <= _tmp_142;
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          if(_th_comp_st_28 !== _th_comp_sq_29) begin
            th_comp <= th_comp_32;
          end else begin
            th_comp <= th_comp_33;
          end
        end
        th_comp_32: begin
          _th_comp_all_ok_26 <= 0;
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          _th_comp_i_27 <= _th_comp_i_27 + 1;
          th_comp <= th_comp_26;
        end
        th_comp_34: begin
          if(_th_comp_all_ok_26) begin
            th_comp <= th_comp_35;
          end else begin
            th_comp <= th_comp_37;
          end
        end
        th_comp_35: begin
          $display("OK");
          th_comp <= th_comp_36;
        end
        th_comp_36: begin
          th_comp <= th_comp_38;
        end
        th_comp_37: begin
          $display("NG");
          th_comp <= th_comp_38;
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
          if(th_comp == 4) begin
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
          if(th_comp == 6) begin
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
  localparam mystream_2 = 2;
  localparam mystream_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      mystream <= mystream_init;
      _mystream_start_cond <= 0;
      _mystream_running_reg <= 0;
      _mystream_roffset_2 <= 0;
      _mystream_woffset_3 <= 0;
    end else begin
      case(mystream)
        mystream_init: begin
          if(th_comp == 7) begin
            _mystream_start_cond <= 1;
          end 
          if(th_comp == 7) begin
            _mystream_running_reg <= 1;
          end 
          if(th_comp == 7) begin
            _mystream_roffset_2 <= _th_comp_roffset_0;
          end 
          if(th_comp == 7) begin
            _mystream_woffset_3 <= _th_comp_woffset_1;
          end 
          if(th_comp == 7) begin
            mystream <= mystream_1;
          end 
        end
        mystream_1: begin
          _mystream_start_cond <= 0;
          mystream <= mystream_2;
        end
        mystream_2: begin
          mystream <= mystream_3;
        end
        mystream_3: begin
          if(_mystream_done_flag_4 && _mystream_done_flag_6 && _mystream_done_flag_8) begin
            _mystream_running_reg <= 0;
          end 
          if(_mystream_done_flag_4 && _mystream_done_flag_6 && _mystream_done_flag_8) begin
            mystream <= mystream_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_5_1 = 1;
  localparam _mystream_fsm_5_2 = 2;
  localparam _mystream_fsm_5_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_5 <= _mystream_fsm_5_init;
      _mystream_done_flag_4 <= 0;
    end else begin
      case(_mystream_fsm_5)
        _mystream_fsm_5_init: begin
          if(_mystream_start_cond) begin
            _mystream_fsm_5 <= _mystream_fsm_5_1;
          end 
        end
        _mystream_fsm_5_1: begin
          _mystream_fsm_5 <= _mystream_fsm_5_2;
        end
        _mystream_fsm_5_2: begin
          if(_tmp_37) begin
            _mystream_done_flag_4 <= 1;
          end 
          if(_tmp_37) begin
            _mystream_fsm_5 <= _mystream_fsm_5_3;
          end 
        end
        _mystream_fsm_5_3: begin
          if(!_mystream_running) begin
            _mystream_done_flag_4 <= 0;
          end 
          if(!_mystream_running) begin
            _mystream_fsm_5 <= _mystream_fsm_5_init;
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
  localparam _tmp_fsm_2_7 = 7;
  localparam _tmp_fsm_2_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_2 <= _tmp_fsm_2_init;
      _d1__tmp_fsm_2 <= _tmp_fsm_2_init;
      _d2__tmp_fsm_2 <= _tmp_fsm_2_init;
      ram_a_0_addr <= 0;
      _tmp_42 <= 0;
      _tmp_43 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_32 <= 0;
      _tmp_36 <= 0;
      _tmp_33 <= 0;
      __tmp_fsm_2_cond_1_0_1 <= 0;
      __tmp_fsm_2_cond_1_0_2 <= 0;
      _tmp_39 <= 0;
      __tmp_fsm_2_cond_1_1_1 <= 0;
      __tmp_fsm_2_cond_1_1_2 <= 0;
      __tmp_fsm_2_cond_1_2_1 <= 0;
      __tmp_fsm_2_cond_1_2_2 <= 0;
      _tmp_38 <= 0;
      _tmp_41 <= 0;
      __tmp_fsm_2_cond_4_3_1 <= 0;
      __tmp_fsm_2_cond_5_4_1 <= 0;
      __tmp_fsm_2_cond_5_4_2 <= 0;
      __tmp_fsm_2_cond_5_5_1 <= 0;
      __tmp_fsm_2_cond_5_5_2 <= 0;
      __tmp_fsm_2_cond_5_6_1 <= 0;
      __tmp_fsm_2_cond_5_6_2 <= 0;
      __tmp_fsm_2_cond_8_7_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      _d2__tmp_fsm_2 <= _d1__tmp_fsm_2;
      case(_d2__tmp_fsm_2)
        _tmp_fsm_2_1: begin
          if(__tmp_fsm_2_cond_1_0_2) begin
            _tmp_39 <= ram_a_0_rdata;
          end 
          if(__tmp_fsm_2_cond_1_1_2) begin
            _tmp_39 <= ram_a_0_rdata;
          end 
          if(__tmp_fsm_2_cond_1_2_2) begin
            _tmp_39 <= ram_a_0_rdata;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_4_2) begin
            _tmp_39 <= ram_a_0_rdata;
          end 
          if(__tmp_fsm_2_cond_5_5_2) begin
            _tmp_39 <= ram_a_0_rdata;
          end 
          if(__tmp_fsm_2_cond_5_6_2) begin
            _tmp_39 <= ram_a_0_rdata;
          end 
        end
      endcase
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_1: begin
          __tmp_fsm_2_cond_1_0_2 <= __tmp_fsm_2_cond_1_0_1;
          __tmp_fsm_2_cond_1_1_2 <= __tmp_fsm_2_cond_1_1_1;
          __tmp_fsm_2_cond_1_2_2 <= __tmp_fsm_2_cond_1_2_1;
        end
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_3_1) begin
            _tmp_41 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          __tmp_fsm_2_cond_5_4_2 <= __tmp_fsm_2_cond_5_4_1;
          __tmp_fsm_2_cond_5_5_2 <= __tmp_fsm_2_cond_5_5_1;
          __tmp_fsm_2_cond_5_6_2 <= __tmp_fsm_2_cond_5_6_1;
        end
        _tmp_fsm_2_8: begin
          if(__tmp_fsm_2_cond_8_7_1) begin
            _tmp_41 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(_mystream_fsm_5 == 1) begin
            ram_a_0_addr <= _mystream_roffset_2 - ((0 && 0)? 16 : 4);
            _tmp_42 <= 0;
            _tmp_43 <= 0;
          end 
          if(_mystream_fsm_5 == 1) begin
            _tmp_34 <= 4;
          end 
          if(_mystream_fsm_5 == 1) begin
            _tmp_35 <= 3;
          end 
          if(_mystream_fsm_5 == 1) begin
            _tmp_32 <= 0;
          end 
          if(_mystream_fsm_5 == 1) begin
            _tmp_36 <= 3;
          end 
          if(_mystream_fsm_5 == 1) begin
            _tmp_33 <= 0;
          end 
          if(_mystream_fsm_5 == 1) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_34 <= _tmp_34 - 1;
          if(_tmp_34 == 0) begin
            _tmp_34 <= 3;
          end 
          ram_a_0_addr <= _tmp_30;
          __tmp_fsm_2_cond_1_0_1 <= 1;
          if(_tmp_34 == 0) begin
            _tmp_35 <= _tmp_35 - 1;
          end 
          if((_tmp_34 == 0) && (_tmp_35 == 0)) begin
            _tmp_35 <= 3;
          end 
          ram_a_0_addr <= _tmp_30;
          __tmp_fsm_2_cond_1_1_1 <= 1;
          if((_tmp_34 == 1) && !0) begin
            _tmp_32 <= _tmp_32 + 1;
          end 
          if((_tmp_34 == 1) && (_tmp_35 == 0)) begin
            _tmp_32 <= 0;
          end 
          if((_tmp_34 == 0) && (_tmp_35 == 0)) begin
            _tmp_36 <= _tmp_36 - 1;
          end 
          if((_tmp_34 == 0) && (_tmp_35 == 0) && (_tmp_36 == 0)) begin
            _tmp_36 <= 3;
          end 
          ram_a_0_addr <= _tmp_30;
          __tmp_fsm_2_cond_1_2_1 <= 1;
          if((_tmp_34 == 1) && (_tmp_35 == 0) && !(0 && 0)) begin
            _tmp_33 <= _tmp_33 + 16;
          end 
          if((_tmp_34 == 1) && (_tmp_35 == 0) && (_tmp_36 == 0)) begin
            _tmp_33 <= 0;
          end 
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_34 == 0) && (_tmp_35 == 0) && (_tmp_36 == 0)) begin
            _tmp_42 <= 1;
          end 
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          _tmp_fsm_2 <= _tmp_fsm_2_4;
        end
        _tmp_fsm_2_4: begin
          _tmp_38 <= _tmp_39;
          _tmp_43 <= _tmp_42;
          _tmp_41 <= !_tmp_43;
          __tmp_fsm_2_cond_4_3_1 <= 1;
          _tmp_fsm_2 <= _tmp_fsm_2_5;
        end
        _tmp_fsm_2_5: begin
          _tmp_34 <= _tmp_34 - 1;
          if(_tmp_34 == 0) begin
            _tmp_34 <= 3;
          end 
          ram_a_0_addr <= _tmp_30;
          __tmp_fsm_2_cond_5_4_1 <= 1;
          if(_tmp_34 == 0) begin
            _tmp_35 <= _tmp_35 - 1;
          end 
          if((_tmp_34 == 0) && (_tmp_35 == 0)) begin
            _tmp_35 <= 3;
          end 
          ram_a_0_addr <= _tmp_30;
          __tmp_fsm_2_cond_5_5_1 <= 1;
          if((_tmp_34 == 1) && !0) begin
            _tmp_32 <= _tmp_32 + 1;
          end 
          if((_tmp_34 == 1) && (_tmp_35 == 0)) begin
            _tmp_32 <= 0;
          end 
          if((_tmp_34 == 0) && (_tmp_35 == 0)) begin
            _tmp_36 <= _tmp_36 - 1;
          end 
          if((_tmp_34 == 0) && (_tmp_35 == 0) && (_tmp_36 == 0)) begin
            _tmp_36 <= 3;
          end 
          ram_a_0_addr <= _tmp_30;
          __tmp_fsm_2_cond_5_6_1 <= 1;
          if((_tmp_34 == 1) && (_tmp_35 == 0) && !(0 && 0)) begin
            _tmp_33 <= _tmp_33 + 16;
          end 
          if((_tmp_34 == 1) && (_tmp_35 == 0) && (_tmp_36 == 0)) begin
            _tmp_33 <= 0;
          end 
          _tmp_fsm_2 <= _tmp_fsm_2_6;
        end
        _tmp_fsm_2_6: begin
          if((_tmp_34 == 0) && (_tmp_35 == 0) && (_tmp_36 == 0)) begin
            _tmp_42 <= 1;
          end 
          _tmp_fsm_2 <= _tmp_fsm_2_7;
        end
        _tmp_fsm_2_7: begin
          _tmp_fsm_2 <= _tmp_fsm_2_8;
        end
        _tmp_fsm_2_8: begin
          if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_40 == 0)) begin
            _tmp_38 <= _tmp_39;
          end 
          if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_40 == 0)) begin
            _tmp_43 <= _tmp_42;
            _tmp_41 <= !_tmp_43;
          end 
          __tmp_fsm_2_cond_8_7_1 <= 1;
          if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_40 == 0) && _tmp_43) begin
            _tmp_fsm_2 <= _tmp_fsm_2_init;
          end 
          if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_40 == 0) && !_tmp_43) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_7_1 = 1;
  localparam _mystream_fsm_7_2 = 2;
  localparam _mystream_fsm_7_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_7 <= _mystream_fsm_7_init;
      _mystream_done_flag_6 <= 0;
    end else begin
      case(_mystream_fsm_7)
        _mystream_fsm_7_init: begin
          if(_mystream_start_cond) begin
            _mystream_fsm_7 <= _mystream_fsm_7_1;
          end 
        end
        _mystream_fsm_7_1: begin
          _mystream_fsm_7 <= _mystream_fsm_7_2;
        end
        _mystream_fsm_7_2: begin
          if(_tmp_55) begin
            _mystream_done_flag_6 <= 1;
          end 
          if(_tmp_55) begin
            _mystream_fsm_7 <= _mystream_fsm_7_3;
          end 
        end
        _mystream_fsm_7_3: begin
          if(!_mystream_running) begin
            _mystream_done_flag_6 <= 0;
          end 
          if(!_mystream_running) begin
            _mystream_fsm_7 <= _mystream_fsm_7_init;
          end 
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
  localparam _tmp_fsm_3_7 = 7;
  localparam _tmp_fsm_3_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_3 <= _tmp_fsm_3_init;
      _d1__tmp_fsm_3 <= _tmp_fsm_3_init;
      _d2__tmp_fsm_3 <= _tmp_fsm_3_init;
      ram_b_0_addr <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _tmp_50 <= 0;
      _tmp_54 <= 0;
      _tmp_51 <= 0;
      __tmp_fsm_3_cond_1_0_1 <= 0;
      __tmp_fsm_3_cond_1_0_2 <= 0;
      _tmp_57 <= 0;
      __tmp_fsm_3_cond_1_1_1 <= 0;
      __tmp_fsm_3_cond_1_1_2 <= 0;
      __tmp_fsm_3_cond_1_2_1 <= 0;
      __tmp_fsm_3_cond_1_2_2 <= 0;
      _tmp_56 <= 0;
      _tmp_59 <= 0;
      __tmp_fsm_3_cond_4_3_1 <= 0;
      __tmp_fsm_3_cond_5_4_1 <= 0;
      __tmp_fsm_3_cond_5_4_2 <= 0;
      __tmp_fsm_3_cond_5_5_1 <= 0;
      __tmp_fsm_3_cond_5_5_2 <= 0;
      __tmp_fsm_3_cond_5_6_1 <= 0;
      __tmp_fsm_3_cond_5_6_2 <= 0;
      __tmp_fsm_3_cond_8_7_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      _d2__tmp_fsm_3 <= _d1__tmp_fsm_3;
      case(_d2__tmp_fsm_3)
        _tmp_fsm_3_1: begin
          if(__tmp_fsm_3_cond_1_0_2) begin
            _tmp_57 <= ram_b_0_rdata;
          end 
          if(__tmp_fsm_3_cond_1_1_2) begin
            _tmp_57 <= ram_b_0_rdata;
          end 
          if(__tmp_fsm_3_cond_1_2_2) begin
            _tmp_57 <= ram_b_0_rdata;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_4_2) begin
            _tmp_57 <= ram_b_0_rdata;
          end 
          if(__tmp_fsm_3_cond_5_5_2) begin
            _tmp_57 <= ram_b_0_rdata;
          end 
          if(__tmp_fsm_3_cond_5_6_2) begin
            _tmp_57 <= ram_b_0_rdata;
          end 
        end
      endcase
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_1: begin
          __tmp_fsm_3_cond_1_0_2 <= __tmp_fsm_3_cond_1_0_1;
          __tmp_fsm_3_cond_1_1_2 <= __tmp_fsm_3_cond_1_1_1;
          __tmp_fsm_3_cond_1_2_2 <= __tmp_fsm_3_cond_1_2_1;
        end
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_3_1) begin
            _tmp_59 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          __tmp_fsm_3_cond_5_4_2 <= __tmp_fsm_3_cond_5_4_1;
          __tmp_fsm_3_cond_5_5_2 <= __tmp_fsm_3_cond_5_5_1;
          __tmp_fsm_3_cond_5_6_2 <= __tmp_fsm_3_cond_5_6_1;
        end
        _tmp_fsm_3_8: begin
          if(__tmp_fsm_3_cond_8_7_1) begin
            _tmp_59 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(_mystream_fsm_7 == 1) begin
            ram_b_0_addr <= _mystream_roffset_2 - ((0 && 0)? 16 : 4);
            _tmp_60 <= 0;
            _tmp_61 <= 0;
          end 
          if(_mystream_fsm_7 == 1) begin
            _tmp_52 <= 4;
          end 
          if(_mystream_fsm_7 == 1) begin
            _tmp_53 <= 3;
          end 
          if(_mystream_fsm_7 == 1) begin
            _tmp_50 <= 0;
          end 
          if(_mystream_fsm_7 == 1) begin
            _tmp_54 <= 3;
          end 
          if(_mystream_fsm_7 == 1) begin
            _tmp_51 <= 0;
          end 
          if(_mystream_fsm_7 == 1) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_52 <= _tmp_52 - 1;
          if(_tmp_52 == 0) begin
            _tmp_52 <= 3;
          end 
          ram_b_0_addr <= _tmp_48;
          __tmp_fsm_3_cond_1_0_1 <= 1;
          if(_tmp_52 == 0) begin
            _tmp_53 <= _tmp_53 - 1;
          end 
          if((_tmp_52 == 0) && (_tmp_53 == 0)) begin
            _tmp_53 <= 3;
          end 
          ram_b_0_addr <= _tmp_48;
          __tmp_fsm_3_cond_1_1_1 <= 1;
          if((_tmp_52 == 1) && !0) begin
            _tmp_50 <= _tmp_50 + 1;
          end 
          if((_tmp_52 == 1) && (_tmp_53 == 0)) begin
            _tmp_50 <= 0;
          end 
          if((_tmp_52 == 0) && (_tmp_53 == 0)) begin
            _tmp_54 <= _tmp_54 - 1;
          end 
          if((_tmp_52 == 0) && (_tmp_53 == 0) && (_tmp_54 == 0)) begin
            _tmp_54 <= 3;
          end 
          ram_b_0_addr <= _tmp_48;
          __tmp_fsm_3_cond_1_2_1 <= 1;
          if((_tmp_52 == 1) && (_tmp_53 == 0) && !(0 && 0)) begin
            _tmp_51 <= _tmp_51 + 16;
          end 
          if((_tmp_52 == 1) && (_tmp_53 == 0) && (_tmp_54 == 0)) begin
            _tmp_51 <= 0;
          end 
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_52 == 0) && (_tmp_53 == 0) && (_tmp_54 == 0)) begin
            _tmp_60 <= 1;
          end 
          _tmp_fsm_3 <= _tmp_fsm_3_3;
        end
        _tmp_fsm_3_3: begin
          _tmp_fsm_3 <= _tmp_fsm_3_4;
        end
        _tmp_fsm_3_4: begin
          _tmp_56 <= _tmp_57;
          _tmp_61 <= _tmp_60;
          _tmp_59 <= !_tmp_61;
          __tmp_fsm_3_cond_4_3_1 <= 1;
          _tmp_fsm_3 <= _tmp_fsm_3_5;
        end
        _tmp_fsm_3_5: begin
          _tmp_52 <= _tmp_52 - 1;
          if(_tmp_52 == 0) begin
            _tmp_52 <= 3;
          end 
          ram_b_0_addr <= _tmp_48;
          __tmp_fsm_3_cond_5_4_1 <= 1;
          if(_tmp_52 == 0) begin
            _tmp_53 <= _tmp_53 - 1;
          end 
          if((_tmp_52 == 0) && (_tmp_53 == 0)) begin
            _tmp_53 <= 3;
          end 
          ram_b_0_addr <= _tmp_48;
          __tmp_fsm_3_cond_5_5_1 <= 1;
          if((_tmp_52 == 1) && !0) begin
            _tmp_50 <= _tmp_50 + 1;
          end 
          if((_tmp_52 == 1) && (_tmp_53 == 0)) begin
            _tmp_50 <= 0;
          end 
          if((_tmp_52 == 0) && (_tmp_53 == 0)) begin
            _tmp_54 <= _tmp_54 - 1;
          end 
          if((_tmp_52 == 0) && (_tmp_53 == 0) && (_tmp_54 == 0)) begin
            _tmp_54 <= 3;
          end 
          ram_b_0_addr <= _tmp_48;
          __tmp_fsm_3_cond_5_6_1 <= 1;
          if((_tmp_52 == 1) && (_tmp_53 == 0) && !(0 && 0)) begin
            _tmp_51 <= _tmp_51 + 16;
          end 
          if((_tmp_52 == 1) && (_tmp_53 == 0) && (_tmp_54 == 0)) begin
            _tmp_51 <= 0;
          end 
          _tmp_fsm_3 <= _tmp_fsm_3_6;
        end
        _tmp_fsm_3_6: begin
          if((_tmp_52 == 0) && (_tmp_53 == 0) && (_tmp_54 == 0)) begin
            _tmp_60 <= 1;
          end 
          _tmp_fsm_3 <= _tmp_fsm_3_7;
        end
        _tmp_fsm_3_7: begin
          _tmp_fsm_3 <= _tmp_fsm_3_8;
        end
        _tmp_fsm_3_8: begin
          if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && (_tmp_58 == 0)) begin
            _tmp_56 <= _tmp_57;
          end 
          if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && (_tmp_58 == 0)) begin
            _tmp_61 <= _tmp_60;
            _tmp_59 <= !_tmp_61;
          end 
          __tmp_fsm_3_cond_8_7_1 <= 1;
          if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && (_tmp_58 == 0) && _tmp_61) begin
            _tmp_fsm_3 <= _tmp_fsm_3_init;
          end 
          if((_tmp_46 || !_tmp_44) && (_tmp_47 || !_tmp_45) && (_tmp_58 == 0) && !_tmp_61) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_9_1 = 1;
  localparam _mystream_fsm_9_2 = 2;
  localparam _mystream_fsm_9_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_9 <= _mystream_fsm_9_init;
      _mystream_done_flag_8 <= 0;
    end else begin
      case(_mystream_fsm_9)
        _mystream_fsm_9_init: begin
          if(_mystream_start_cond) begin
            _mystream_fsm_9 <= _mystream_fsm_9_1;
          end 
        end
        _mystream_fsm_9_1: begin
          _mystream_fsm_9 <= _mystream_fsm_9_2;
        end
        _mystream_fsm_9_2: begin
          if(_tmp_63) begin
            _mystream_done_flag_8 <= 1;
          end 
          if(_tmp_63) begin
            _mystream_fsm_9 <= _mystream_fsm_9_3;
          end 
        end
        _mystream_fsm_9_3: begin
          if(!_mystream_running) begin
            _mystream_done_flag_8 <= 0;
          end 
          if(!_mystream_running) begin
            _mystream_fsm_9 <= _mystream_fsm_9_init;
          end 
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
      _tmp_68 <= 0;
      _tmp_70 <= 0;
      _tmp_69 <= 0;
      _tmp_86 <= 0;
      __tmp_fsm_4_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_4 <= _tmp_fsm_4;
      case(_d1__tmp_fsm_4)
        _tmp_fsm_4_5: begin
          if(__tmp_fsm_4_cond_5_0_1) begin
            _tmp_86 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_4)
        _tmp_fsm_4_init: begin
          if(th_comp == 12) begin
            _tmp_fsm_4 <= _tmp_fsm_4_1;
          end 
        end
        _tmp_fsm_4_1: begin
          _tmp_68 <= (_tmp_66 >> 2) << 2;
          _tmp_70 <= _tmp_67;
          _tmp_fsm_4 <= _tmp_fsm_4_2;
        end
        _tmp_fsm_4_2: begin
          if((_tmp_70 <= 256) && ((_tmp_68 & 4095) + (_tmp_70 << 2) >= 4096)) begin
            _tmp_69 <= 4096 - (_tmp_68 & 4095) >> 2;
            _tmp_70 <= _tmp_70 - (4096 - (_tmp_68 & 4095) >> 2);
          end else if(_tmp_70 <= 256) begin
            _tmp_69 <= _tmp_70;
            _tmp_70 <= 0;
          end else if((_tmp_68 & 4095) + 1024 >= 4096) begin
            _tmp_69 <= 4096 - (_tmp_68 & 4095) >> 2;
            _tmp_70 <= _tmp_70 - (4096 - (_tmp_68 & 4095) >> 2);
          end else begin
            _tmp_69 <= 256;
            _tmp_70 <= _tmp_70 - 256;
          end
          _tmp_fsm_4 <= _tmp_fsm_4_3;
        end
        _tmp_fsm_4_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_4 <= _tmp_fsm_4_4;
          end 
        end
        _tmp_fsm_4_4: begin
          if(_tmp_84 && myaxi_wvalid && myaxi_wready) begin
            _tmp_68 <= _tmp_68 + (_tmp_69 << 2);
          end 
          if(_tmp_84 && myaxi_wvalid && myaxi_wready && (_tmp_70 > 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_2;
          end 
          if(_tmp_84 && myaxi_wvalid && myaxi_wready && (_tmp_70 == 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_5;
          end 
        end
        _tmp_fsm_4_5: begin
          _tmp_86 <= 1;
          __tmp_fsm_4_cond_5_0_1 <= 1;
          _tmp_fsm_4 <= _tmp_fsm_4_6;
        end
        _tmp_fsm_4_6: begin
          _tmp_fsm_4 <= _tmp_fsm_4_init;
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
      _tmp_90 <= 0;
      _tmp_92 <= 0;
      _tmp_91 <= 0;
      __tmp_fsm_5_cond_4_0_1 <= 0;
      _tmp_94 <= 0;
      _tmp_93 <= 0;
      _tmp_99 <= 0;
      __tmp_fsm_5_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_5 <= _tmp_fsm_5;
      case(_d1__tmp_fsm_5)
        _tmp_fsm_5_4: begin
          if(__tmp_fsm_5_cond_4_0_1) begin
            _tmp_94 <= 0;
          end 
        end
        _tmp_fsm_5_5: begin
          if(__tmp_fsm_5_cond_5_1_1) begin
            _tmp_99 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_5)
        _tmp_fsm_5_init: begin
          if(th_comp == 16) begin
            _tmp_fsm_5 <= _tmp_fsm_5_1;
          end 
        end
        _tmp_fsm_5_1: begin
          _tmp_90 <= (_tmp_88 >> 2) << 2;
          _tmp_92 <= _tmp_89;
          _tmp_fsm_5 <= _tmp_fsm_5_2;
        end
        _tmp_fsm_5_2: begin
          if((_tmp_92 <= 256) && ((_tmp_90 & 4095) + (_tmp_92 << 2) >= 4096)) begin
            _tmp_91 <= 4096 - (_tmp_90 & 4095) >> 2;
            _tmp_92 <= _tmp_92 - (4096 - (_tmp_90 & 4095) >> 2);
          end else if(_tmp_92 <= 256) begin
            _tmp_91 <= _tmp_92;
            _tmp_92 <= 0;
          end else if((_tmp_90 & 4095) + 1024 >= 4096) begin
            _tmp_91 <= 4096 - (_tmp_90 & 4095) >> 2;
            _tmp_92 <= _tmp_92 - (4096 - (_tmp_90 & 4095) >> 2);
          end else begin
            _tmp_91 <= 256;
            _tmp_92 <= _tmp_92 - 256;
          end
          _tmp_fsm_5 <= _tmp_fsm_5_3;
        end
        _tmp_fsm_5_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_5 <= _tmp_fsm_5_4;
          end 
        end
        _tmp_fsm_5_4: begin
          __tmp_fsm_5_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_93 <= myaxi_rdata;
            _tmp_94 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_90 <= _tmp_90 + (_tmp_91 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_92 > 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_92 == 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_5;
          end 
        end
        _tmp_fsm_5_5: begin
          _tmp_99 <= 1;
          __tmp_fsm_5_cond_5_1_1 <= 1;
          _tmp_fsm_5 <= _tmp_fsm_5_6;
        end
        _tmp_fsm_5_6: begin
          _tmp_fsm_5 <= _tmp_fsm_5_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_6_1 = 1;
  localparam _tmp_fsm_6_2 = 2;
  localparam _tmp_fsm_6_3 = 3;
  localparam _tmp_fsm_6_4 = 4;
  localparam _tmp_fsm_6_5 = 5;
  localparam _tmp_fsm_6_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_6 <= _tmp_fsm_6_init;
      _d1__tmp_fsm_6 <= _tmp_fsm_6_init;
      _tmp_103 <= 0;
      _tmp_105 <= 0;
      _tmp_104 <= 0;
      __tmp_fsm_6_cond_4_0_1 <= 0;
      _tmp_107 <= 0;
      _tmp_106 <= 0;
      _tmp_112 <= 0;
      __tmp_fsm_6_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_6 <= _tmp_fsm_6;
      case(_d1__tmp_fsm_6)
        _tmp_fsm_6_4: begin
          if(__tmp_fsm_6_cond_4_0_1) begin
            _tmp_107 <= 0;
          end 
        end
        _tmp_fsm_6_5: begin
          if(__tmp_fsm_6_cond_5_1_1) begin
            _tmp_112 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_6)
        _tmp_fsm_6_init: begin
          if(th_comp == 18) begin
            _tmp_fsm_6 <= _tmp_fsm_6_1;
          end 
        end
        _tmp_fsm_6_1: begin
          _tmp_103 <= (_tmp_101 >> 2) << 2;
          _tmp_105 <= _tmp_102;
          _tmp_fsm_6 <= _tmp_fsm_6_2;
        end
        _tmp_fsm_6_2: begin
          if((_tmp_105 <= 256) && ((_tmp_103 & 4095) + (_tmp_105 << 2) >= 4096)) begin
            _tmp_104 <= 4096 - (_tmp_103 & 4095) >> 2;
            _tmp_105 <= _tmp_105 - (4096 - (_tmp_103 & 4095) >> 2);
          end else if(_tmp_105 <= 256) begin
            _tmp_104 <= _tmp_105;
            _tmp_105 <= 0;
          end else if((_tmp_103 & 4095) + 1024 >= 4096) begin
            _tmp_104 <= 4096 - (_tmp_103 & 4095) >> 2;
            _tmp_105 <= _tmp_105 - (4096 - (_tmp_103 & 4095) >> 2);
          end else begin
            _tmp_104 <= 256;
            _tmp_105 <= _tmp_105 - 256;
          end
          _tmp_fsm_6 <= _tmp_fsm_6_3;
        end
        _tmp_fsm_6_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_6 <= _tmp_fsm_6_4;
          end 
        end
        _tmp_fsm_6_4: begin
          __tmp_fsm_6_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_106 <= myaxi_rdata;
            _tmp_107 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_103 <= _tmp_103 + (_tmp_104 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_105 > 0)) begin
            _tmp_fsm_6 <= _tmp_fsm_6_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_105 == 0)) begin
            _tmp_fsm_6 <= _tmp_fsm_6_5;
          end 
        end
        _tmp_fsm_6_5: begin
          _tmp_112 <= 1;
          __tmp_fsm_6_cond_5_1_1 <= 1;
          _tmp_fsm_6 <= _tmp_fsm_6_6;
        end
        _tmp_fsm_6_6: begin
          _tmp_fsm_6 <= _tmp_fsm_6_init;
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
  localparam th_sequential_16 = 16;
  localparam th_sequential_17 = 17;
  localparam th_sequential_18 = 18;
  localparam th_sequential_19 = 19;
  localparam th_sequential_20 = 20;
  localparam th_sequential_21 = 21;
  localparam th_sequential_22 = 22;
  localparam th_sequential_23 = 23;
  localparam th_sequential_24 = 24;

  always @(posedge CLK) begin
    if(RST) begin
      th_sequential <= th_sequential_init;
      _th_sequential_called <= 0;
      _th_sequential_roffset_10 <= 0;
      _th_sequential_woffset_11 <= 0;
      _th_sequential_roffset_12 <= 0;
      _th_sequential_woffset_13 <= 0;
      _th_sequential_sum_14 <= 0;
      _th_sequential_w_15 <= 0;
      _th_sequential_i_16 <= 0;
      _th_sequential_k_17 <= 0;
      _th_sequential_j_18 <= 0;
      _th_sequential_r_19 <= 0;
      _th_sequential_addr_20 <= 0;
      _tmp_114 <= 0;
      _th_sequential_a_21 <= 0;
      _tmp_116 <= 0;
      _th_sequential_b_22 <= 0;
    end else begin
      case(th_sequential)
        th_sequential_init: begin
          if(th_comp == 19) begin
            _th_sequential_called <= 1;
          end 
          if(th_comp == 19) begin
            _th_sequential_roffset_10 <= _th_comp_roffset_0;
          end 
          if(th_comp == 19) begin
            _th_sequential_woffset_11 <= _th_comp_woffset_1;
          end 
          if(th_comp == 19) begin
            th_sequential <= th_sequential_1;
          end 
        end
        th_sequential_1: begin
          _th_sequential_roffset_12 <= _th_sequential_roffset_10;
          _th_sequential_woffset_13 <= _th_sequential_woffset_11;
          th_sequential <= th_sequential_2;
        end
        th_sequential_2: begin
          _th_sequential_sum_14 <= 0;
          th_sequential <= th_sequential_3;
        end
        th_sequential_3: begin
          _th_sequential_w_15 <= 0;
          th_sequential <= th_sequential_4;
        end
        th_sequential_4: begin
          _th_sequential_i_16 <= 0;
          th_sequential <= th_sequential_5;
        end
        th_sequential_5: begin
          if(_th_sequential_i_16 < 4) begin
            th_sequential <= th_sequential_6;
          end else begin
            th_sequential <= th_sequential_24;
          end
        end
        th_sequential_6: begin
          _th_sequential_k_17 <= 0;
          th_sequential <= th_sequential_7;
        end
        th_sequential_7: begin
          if(_th_sequential_k_17 < 4) begin
            th_sequential <= th_sequential_8;
          end else begin
            th_sequential <= th_sequential_23;
          end
        end
        th_sequential_8: begin
          _th_sequential_j_18 <= 0;
          th_sequential <= th_sequential_9;
        end
        th_sequential_9: begin
          if(_th_sequential_j_18 < 4) begin
            th_sequential <= th_sequential_10;
          end else begin
            th_sequential <= th_sequential_22;
          end
        end
        th_sequential_10: begin
          _th_sequential_r_19 <= 0;
          th_sequential <= th_sequential_11;
        end
        th_sequential_11: begin
          if(_th_sequential_r_19 < 4) begin
            th_sequential <= th_sequential_12;
          end else begin
            th_sequential <= th_sequential_21;
          end
        end
        th_sequential_12: begin
          _th_sequential_addr_20 <= _th_sequential_k_17 + (_th_sequential_j_18 << 2) + (_th_sequential_i_16 << 4);
          th_sequential <= th_sequential_13;
        end
        th_sequential_13: begin
          if(_tmp_113) begin
            _tmp_114 <= ram_a_0_rdata;
          end 
          if(_tmp_113) begin
            th_sequential <= th_sequential_14;
          end 
        end
        th_sequential_14: begin
          _th_sequential_a_21 <= _tmp_114;
          th_sequential <= th_sequential_15;
        end
        th_sequential_15: begin
          if(_tmp_115) begin
            _tmp_116 <= ram_b_0_rdata;
          end 
          if(_tmp_115) begin
            th_sequential <= th_sequential_16;
          end 
        end
        th_sequential_16: begin
          _th_sequential_b_22 <= _tmp_116;
          th_sequential <= th_sequential_17;
        end
        th_sequential_17: begin
          _th_sequential_sum_14 <= _th_sequential_a_21 + _th_sequential_b_22;
          th_sequential <= th_sequential_18;
        end
        th_sequential_18: begin
          th_sequential <= th_sequential_19;
        end
        th_sequential_19: begin
          _th_sequential_w_15 <= _th_sequential_w_15 + 1;
          th_sequential <= th_sequential_20;
        end
        th_sequential_20: begin
          _th_sequential_r_19 <= _th_sequential_r_19 + 1;
          th_sequential <= th_sequential_11;
        end
        th_sequential_21: begin
          _th_sequential_j_18 <= _th_sequential_j_18 + 1;
          th_sequential <= th_sequential_9;
        end
        th_sequential_22: begin
          _th_sequential_k_17 <= _th_sequential_k_17 + 1;
          th_sequential <= th_sequential_7;
        end
        th_sequential_23: begin
          _th_sequential_i_16 <= _th_sequential_i_16 + 1;
          th_sequential <= th_sequential_5;
        end
      endcase
    end
  end

  localparam _tmp_fsm_7_1 = 1;
  localparam _tmp_fsm_7_2 = 2;
  localparam _tmp_fsm_7_3 = 3;
  localparam _tmp_fsm_7_4 = 4;
  localparam _tmp_fsm_7_5 = 5;
  localparam _tmp_fsm_7_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_7 <= _tmp_fsm_7_init;
      _d1__tmp_fsm_7 <= _tmp_fsm_7_init;
      _tmp_120 <= 0;
      _tmp_122 <= 0;
      _tmp_121 <= 0;
      _tmp_138 <= 0;
      __tmp_fsm_7_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_7 <= _tmp_fsm_7;
      case(_d1__tmp_fsm_7)
        _tmp_fsm_7_5: begin
          if(__tmp_fsm_7_cond_5_0_1) begin
            _tmp_138 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_7)
        _tmp_fsm_7_init: begin
          if(th_comp == 22) begin
            _tmp_fsm_7 <= _tmp_fsm_7_1;
          end 
        end
        _tmp_fsm_7_1: begin
          _tmp_120 <= (_tmp_118 >> 2) << 2;
          _tmp_122 <= _tmp_119;
          _tmp_fsm_7 <= _tmp_fsm_7_2;
        end
        _tmp_fsm_7_2: begin
          if((_tmp_122 <= 256) && ((_tmp_120 & 4095) + (_tmp_122 << 2) >= 4096)) begin
            _tmp_121 <= 4096 - (_tmp_120 & 4095) >> 2;
            _tmp_122 <= _tmp_122 - (4096 - (_tmp_120 & 4095) >> 2);
          end else if(_tmp_122 <= 256) begin
            _tmp_121 <= _tmp_122;
            _tmp_122 <= 0;
          end else if((_tmp_120 & 4095) + 1024 >= 4096) begin
            _tmp_121 <= 4096 - (_tmp_120 & 4095) >> 2;
            _tmp_122 <= _tmp_122 - (4096 - (_tmp_120 & 4095) >> 2);
          end else begin
            _tmp_121 <= 256;
            _tmp_122 <= _tmp_122 - 256;
          end
          _tmp_fsm_7 <= _tmp_fsm_7_3;
        end
        _tmp_fsm_7_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_7 <= _tmp_fsm_7_4;
          end 
        end
        _tmp_fsm_7_4: begin
          if(_tmp_136 && myaxi_wvalid && myaxi_wready) begin
            _tmp_120 <= _tmp_120 + (_tmp_121 << 2);
          end 
          if(_tmp_136 && myaxi_wvalid && myaxi_wready && (_tmp_122 > 0)) begin
            _tmp_fsm_7 <= _tmp_fsm_7_2;
          end 
          if(_tmp_136 && myaxi_wvalid && myaxi_wready && (_tmp_122 == 0)) begin
            _tmp_fsm_7 <= _tmp_fsm_7_5;
          end 
        end
        _tmp_fsm_7_5: begin
          _tmp_138 <= 1;
          __tmp_fsm_7_cond_5_0_1 <= 1;
          _tmp_fsm_7 <= _tmp_fsm_7_6;
        end
        _tmp_fsm_7_6: begin
          _tmp_fsm_7 <= _tmp_fsm_7_init;
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
    test_module = thread_stream_reuse_pattern.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
