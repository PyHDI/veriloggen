from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_stride

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
  reg signed [32-1:0] _th_comp_stride_2;
  reg [10-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  reg [10-1:0] _tmp_3;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _tmp_4;
  reg [33-1:0] _tmp_5;
  reg [33-1:0] _tmp_6;
  reg [32-1:0] _tmp_7;
  reg _tmp_8;
  reg [33-1:0] _tmp_9;
  reg _tmp_10;
  wire [32-1:0] __variable_data_11;
  wire __variable_valid_11;
  wire __variable_ready_11;
  assign __variable_ready_11 = (_tmp_9 > 0) && !_tmp_10;
  reg _ram_a_cond_0_1;
  reg [9-1:0] _tmp_12;
  reg _myaxi_cond_0_1;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_4_0_1;
  reg _tmp_13;
  reg __tmp_fsm_0_cond_5_1_1;
  reg [10-1:0] _tmp_14;
  reg [32-1:0] _tmp_15;
  reg [32-1:0] _tmp_16;
  reg [10-1:0] _tmp_17;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_18;
  reg [33-1:0] _tmp_19;
  reg [33-1:0] _tmp_20;
  reg [32-1:0] _tmp_21;
  reg _tmp_22;
  reg [33-1:0] _tmp_23;
  reg _tmp_24;
  wire [32-1:0] __variable_data_25;
  wire __variable_valid_25;
  wire __variable_ready_25;
  assign __variable_ready_25 = (_tmp_23 > 0) && !_tmp_24;
  reg _ram_b_cond_0_1;
  reg [9-1:0] _tmp_26;
  reg _myaxi_cond_1_1;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_4_0_1;
  reg _tmp_27;
  reg __tmp_fsm_1_cond_5_1_1;
  reg [32-1:0] mystream;
  localparam mystream_init = 0;
  reg _mystream_start_cond;
  reg _mystream_running_reg;
  wire _mystream_running;
  reg signed [32-1:0] _mystream_size_3;
  reg signed [32-1:0] _mystream_offset_4;
  reg signed [32-1:0] _mystream_stride_5;
  reg _mystream_done_flag_6;
  reg [32-1:0] _mystream_fsm_7;
  localparam _mystream_fsm_7_init = 0;
  reg _tmp_28;
  reg _tmp_29;
  wire _tmp_30;
  wire _tmp_31;
  assign _tmp_31 = 1;
  localparam _tmp_32 = 1;
  wire [_tmp_32-1:0] _tmp_33;
  assign _tmp_33 = (_tmp_30 || !_tmp_28) && (_tmp_31 || !_tmp_29);
  reg [_tmp_32-1:0] __tmp_33_1;
  wire [32-1:0] _tmp_34;
  reg [32-1:0] __tmp_34_1;
  assign _tmp_34 = (__tmp_33_1)? ram_a_0_rdata : __tmp_34_1;
  reg _tmp_35;
  reg _tmp_36;
  reg _tmp_37;
  reg _tmp_38;
  reg [33-1:0] _tmp_39;
  reg _mystream_done_flag_8;
  reg [32-1:0] _mystream_fsm_9;
  localparam _mystream_fsm_9_init = 0;
  reg _tmp_40;
  reg _tmp_41;
  wire _tmp_42;
  wire _tmp_43;
  assign _tmp_43 = 1;
  localparam _tmp_44 = 1;
  wire [_tmp_44-1:0] _tmp_45;
  assign _tmp_45 = (_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41);
  reg [_tmp_44-1:0] __tmp_45_1;
  wire [32-1:0] _tmp_46;
  reg [32-1:0] __tmp_46_1;
  assign _tmp_46 = (__tmp_45_1)? ram_b_0_rdata : __tmp_46_1;
  reg _tmp_47;
  reg _tmp_48;
  reg _tmp_49;
  reg _tmp_50;
  reg [33-1:0] _tmp_51;
  reg _mystream_done_flag_10;
  reg [32-1:0] _mystream_fsm_11;
  localparam _mystream_fsm_11_init = 0;
  reg [2-1:0] _tmp_52;
  reg _tmp_53;
  wire _tmp_all_valid_54;
  wire [32-1:0] _reduceadd_data_55;
  wire _reduceadd_valid_55;
  wire _reduceadd_ready_55;
  assign _reduceadd_ready_55 = (_tmp_52 > 0) && !_tmp_53 && _tmp_all_valid_54;
  wire [1-1:0] _pulse_data_56;
  wire _pulse_valid_56;
  wire _pulse_ready_56;
  assign _pulse_ready_56 = (_tmp_52 > 0) && !_tmp_53 && _tmp_all_valid_54;
  assign _tmp_all_valid_54 = _reduceadd_valid_55 && _pulse_valid_56;
  reg _ram_c_cond_0_1;
  assign _mystream_running = _mystream_running_reg && !(_mystream_done_flag_6 && _mystream_done_flag_8 && _mystream_done_flag_10);
  reg [10-1:0] _tmp_57;
  reg [32-1:0] _tmp_58;
  reg [32-1:0] _tmp_59;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_60;
  reg [33-1:0] _tmp_61;
  reg [33-1:0] _tmp_62;
  reg _tmp_63;
  reg _tmp_64;
  wire _tmp_65;
  wire _tmp_66;
  assign _tmp_66 = 1;
  localparam _tmp_67 = 1;
  wire [_tmp_67-1:0] _tmp_68;
  assign _tmp_68 = (_tmp_65 || !_tmp_63) && (_tmp_66 || !_tmp_64);
  reg [_tmp_67-1:0] __tmp_68_1;
  wire [32-1:0] _tmp_69;
  reg [32-1:0] __tmp_69_1;
  assign _tmp_69 = (__tmp_68_1)? ram_c_0_rdata : __tmp_69_1;
  reg _tmp_70;
  reg _tmp_71;
  reg _tmp_72;
  reg _tmp_73;
  reg [33-1:0] _tmp_74;
  reg [9-1:0] _tmp_75;
  reg _myaxi_cond_2_1;
  reg _tmp_76;
  wire [32-1:0] __variable_data_77;
  wire __variable_valid_77;
  wire __variable_ready_77;
  assign __variable_ready_77 = (_tmp_fsm_2 == 4) && ((_tmp_75 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_78;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_5_0_1;
  reg [10-1:0] _tmp_79;
  reg [32-1:0] _tmp_80;
  reg [32-1:0] _tmp_81;
  reg [10-1:0] _tmp_82;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_83;
  reg [33-1:0] _tmp_84;
  reg [33-1:0] _tmp_85;
  reg [32-1:0] _tmp_86;
  reg _tmp_87;
  reg [33-1:0] _tmp_88;
  reg _tmp_89;
  wire [32-1:0] __variable_data_90;
  wire __variable_valid_90;
  wire __variable_ready_90;
  assign __variable_ready_90 = (_tmp_88 > 0) && !_tmp_89;
  reg _ram_a_cond_1_1;
  reg [9-1:0] _tmp_91;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_92;
  reg __tmp_fsm_3_cond_5_1_1;
  reg [10-1:0] _tmp_93;
  reg [32-1:0] _tmp_94;
  reg [32-1:0] _tmp_95;
  reg [10-1:0] _tmp_96;
  reg [32-1:0] _tmp_fsm_4;
  localparam _tmp_fsm_4_init = 0;
  reg [32-1:0] _tmp_97;
  reg [33-1:0] _tmp_98;
  reg [33-1:0] _tmp_99;
  reg [32-1:0] _tmp_100;
  reg _tmp_101;
  reg [33-1:0] _tmp_102;
  reg _tmp_103;
  wire [32-1:0] __variable_data_104;
  wire __variable_valid_104;
  wire __variable_ready_104;
  assign __variable_ready_104 = (_tmp_102 > 0) && !_tmp_103;
  reg _ram_b_cond_1_1;
  reg [9-1:0] _tmp_105;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_1 == 4) || (_tmp_fsm_3 == 4) || (_tmp_fsm_4 == 4);
  reg [32-1:0] _d1__tmp_fsm_4;
  reg __tmp_fsm_4_cond_4_0_1;
  reg _tmp_106;
  reg __tmp_fsm_4_cond_5_1_1;
  reg [32-1:0] th_sequential;
  localparam th_sequential_init = 0;
  reg _th_sequential_called;
  reg signed [32-1:0] _th_sequential_size_12;
  reg signed [32-1:0] _th_sequential_offset_13;
  reg signed [32-1:0] _th_sequential_stride_14;
  reg signed [32-1:0] _th_sequential_size_15;
  reg signed [32-1:0] _th_sequential_offset_16;
  reg signed [32-1:0] _th_sequential_stride_17;
  reg signed [32-1:0] _th_sequential_sum_18;
  reg signed [32-1:0] _th_sequential_i_19;
  reg _tmp_107;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_3_2;
  reg signed [32-1:0] _tmp_108;
  reg signed [32-1:0] _th_sequential_a_20;
  reg _tmp_109;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_3_2;
  reg signed [32-1:0] _tmp_110;
  reg signed [32-1:0] _th_sequential_b_21;
  reg _ram_c_cond_1_1;
  reg [10-1:0] _tmp_111;
  reg [32-1:0] _tmp_112;
  reg [32-1:0] _tmp_113;
  reg [32-1:0] _tmp_fsm_5;
  localparam _tmp_fsm_5_init = 0;
  reg [32-1:0] _tmp_114;
  reg [33-1:0] _tmp_115;
  reg [33-1:0] _tmp_116;
  reg _tmp_117;
  reg _tmp_118;
  wire _tmp_119;
  wire _tmp_120;
  assign _tmp_120 = 1;
  localparam _tmp_121 = 1;
  wire [_tmp_121-1:0] _tmp_122;
  assign _tmp_122 = (_tmp_119 || !_tmp_117) && (_tmp_120 || !_tmp_118);
  reg [_tmp_121-1:0] __tmp_122_1;
  wire [32-1:0] _tmp_123;
  reg [32-1:0] __tmp_123_1;
  assign _tmp_123 = (__tmp_122_1)? ram_c_0_rdata : __tmp_123_1;
  reg _tmp_124;
  reg _tmp_125;
  reg _tmp_126;
  reg _tmp_127;
  reg [33-1:0] _tmp_128;
  reg [9-1:0] _tmp_129;
  reg _myaxi_cond_6_1;
  reg _tmp_130;
  wire [32-1:0] __variable_data_131;
  wire __variable_valid_131;
  wire __variable_ready_131;
  assign __variable_ready_131 = (_tmp_fsm_5 == 4) && ((_tmp_129 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_7_1;
  reg _tmp_132;
  reg [32-1:0] _d1__tmp_fsm_5;
  reg __tmp_fsm_5_cond_5_0_1;
  reg signed [32-1:0] _th_comp_size_22;
  reg signed [32-1:0] _th_comp_offset_stream_23;
  reg signed [32-1:0] _th_comp_offset_seq_24;
  reg signed [32-1:0] _th_comp_all_ok_25;
  reg _tmp_133;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_134;
  reg signed [32-1:0] _th_comp_st_26;
  reg _tmp_135;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_136;
  reg signed [32-1:0] _th_comp_sq_27;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_12 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_26 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_75 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_76 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_91 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_105 <= 0;
      _myaxi_cond_5_1 <= 0;
      _tmp_129 <= 0;
      _myaxi_cond_6_1 <= 0;
      _tmp_130 <= 0;
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
        _tmp_76 <= 0;
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
        _tmp_130 <= 0;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_12 == 0))) begin
        myaxi_araddr <= _tmp_4;
        myaxi_arlen <= _tmp_5 - 1;
        myaxi_arvalid <= 1;
        _tmp_12 <= _tmp_5;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_12 > 0)) begin
        _tmp_12 <= _tmp_12 - 1;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_26 == 0))) begin
        myaxi_araddr <= _tmp_18;
        myaxi_arlen <= _tmp_19 - 1;
        myaxi_arvalid <= 1;
        _tmp_26 <= _tmp_19;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_26 > 0)) begin
        _tmp_26 <= _tmp_26 - 1;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_75 == 0))) begin
        myaxi_awaddr <= _tmp_60;
        myaxi_awlen <= _tmp_61 - 1;
        myaxi_awvalid <= 1;
        _tmp_75 <= _tmp_61;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_75 == 0)) && (_tmp_61 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_77 && ((_tmp_fsm_2 == 4) && ((_tmp_75 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_75 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_75 > 0))) begin
        myaxi_wdata <= __variable_data_77;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_75 <= _tmp_75 - 1;
      end 
      if(__variable_valid_77 && ((_tmp_fsm_2 == 4) && ((_tmp_75 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_75 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_75 > 0)) && (_tmp_75 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_76 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_76 <= _tmp_76;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_91 == 0))) begin
        myaxi_araddr <= _tmp_83;
        myaxi_arlen <= _tmp_84 - 1;
        myaxi_arvalid <= 1;
        _tmp_91 <= _tmp_84;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_91 > 0)) begin
        _tmp_91 <= _tmp_91 - 1;
      end 
      if((_tmp_fsm_4 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_105 == 0))) begin
        myaxi_araddr <= _tmp_97;
        myaxi_arlen <= _tmp_98 - 1;
        myaxi_arvalid <= 1;
        _tmp_105 <= _tmp_98;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_105 > 0)) begin
        _tmp_105 <= _tmp_105 - 1;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_129 == 0))) begin
        myaxi_awaddr <= _tmp_114;
        myaxi_awlen <= _tmp_115 - 1;
        myaxi_awvalid <= 1;
        _tmp_129 <= _tmp_115;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_129 == 0)) && (_tmp_115 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_6_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_131 && ((_tmp_fsm_5 == 4) && ((_tmp_129 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_129 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_129 > 0))) begin
        myaxi_wdata <= __variable_data_131;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_129 <= _tmp_129 - 1;
      end 
      if(__variable_valid_131 && ((_tmp_fsm_5 == 4) && ((_tmp_129 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_129 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_129 > 0)) && (_tmp_129 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_130 <= 1;
      end 
      _myaxi_cond_7_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_130 <= _tmp_130;
      end 
    end
  end

  assign __variable_data_11 = _tmp_7;
  assign __variable_valid_11 = _tmp_8;
  assign __variable_data_25 = _tmp_21;
  assign __variable_valid_25 = _tmp_22;
  assign __variable_data_90 = _tmp_86;
  assign __variable_valid_90 = _tmp_87;
  assign __variable_data_104 = _tmp_100;
  assign __variable_valid_104 = _tmp_101;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_9 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_10 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_33_1 <= 0;
      __tmp_34_1 <= 0;
      _tmp_38 <= 0;
      _tmp_28 <= 0;
      _tmp_29 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _tmp_35 <= 0;
      _tmp_39 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _ram_a_cond_1_1 <= 0;
      _ram_a_cond_2_1 <= 0;
      _tmp_107 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_3_2 <= 0;
    end else begin
      if(_ram_a_cond_3_2) begin
        _tmp_107 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_10 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        ram_a_0_wenable <= 0;
        _tmp_89 <= 0;
      end 
      if(_ram_a_cond_2_1) begin
        _tmp_107 <= 1;
      end 
      _ram_a_cond_3_2 <= _ram_a_cond_3_1;
      if((_tmp_fsm_0 == 1) && (_tmp_9 == 0)) begin
        ram_a_0_addr <= _tmp_0 - _tmp_3;
        _tmp_9 <= _tmp_2;
      end 
      if(__variable_valid_11 && ((_tmp_9 > 0) && !_tmp_10) && (_tmp_9 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _tmp_3;
        ram_a_0_wdata <= __variable_data_11;
        ram_a_0_wenable <= 1;
        _tmp_9 <= _tmp_9 - 1;
      end 
      if(__variable_valid_11 && ((_tmp_9 > 0) && !_tmp_10) && (_tmp_9 == 1)) begin
        _tmp_10 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      __tmp_33_1 <= _tmp_33;
      __tmp_34_1 <= _tmp_34;
      if((_tmp_30 || !_tmp_28) && (_tmp_31 || !_tmp_29) && _tmp_36) begin
        _tmp_38 <= 0;
        _tmp_28 <= 0;
        _tmp_29 <= 0;
        _tmp_36 <= 0;
      end 
      if((_tmp_30 || !_tmp_28) && (_tmp_31 || !_tmp_29) && _tmp_35) begin
        _tmp_28 <= 1;
        _tmp_29 <= 1;
        _tmp_38 <= _tmp_37;
        _tmp_37 <= 0;
        _tmp_35 <= 0;
        _tmp_36 <= 1;
      end 
      if((_mystream_fsm_7 == 1) && (_tmp_39 == 0) && !_tmp_37 && !_tmp_38) begin
        ram_a_0_addr <= _mystream_offset_4;
        _tmp_39 <= _mystream_size_3 - 1;
        _tmp_35 <= 1;
        _tmp_37 <= _mystream_size_3 == 1;
      end 
      if((_tmp_30 || !_tmp_28) && (_tmp_31 || !_tmp_29) && (_tmp_39 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _mystream_stride_5;
        _tmp_39 <= _tmp_39 - 1;
        _tmp_35 <= 1;
        _tmp_37 <= 0;
      end 
      if((_tmp_30 || !_tmp_28) && (_tmp_31 || !_tmp_29) && (_tmp_39 == 1)) begin
        _tmp_37 <= 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_88 == 0)) begin
        ram_a_0_addr <= _tmp_79 - _tmp_82;
        _tmp_88 <= _tmp_81;
      end 
      if(__variable_valid_90 && ((_tmp_88 > 0) && !_tmp_89) && (_tmp_88 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _tmp_82;
        ram_a_0_wdata <= __variable_data_90;
        ram_a_0_wenable <= 1;
        _tmp_88 <= _tmp_88 - 1;
      end 
      if(__variable_valid_90 && ((_tmp_88 > 0) && !_tmp_89) && (_tmp_88 == 1)) begin
        _tmp_89 <= 1;
      end 
      _ram_a_cond_1_1 <= 1;
      if(th_sequential == 5) begin
        ram_a_0_addr <= _th_sequential_i_19 + _th_sequential_offset_16;
      end 
      _ram_a_cond_2_1 <= th_sequential == 5;
      _ram_a_cond_3_1 <= th_sequential == 5;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_23 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_24 <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_45_1 <= 0;
      __tmp_46_1 <= 0;
      _tmp_50 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
      _tmp_48 <= 0;
      _tmp_49 <= 0;
      _tmp_47 <= 0;
      _tmp_51 <= 0;
      _tmp_102 <= 0;
      _tmp_103 <= 0;
      _ram_b_cond_1_1 <= 0;
      _ram_b_cond_2_1 <= 0;
      _tmp_109 <= 0;
      _ram_b_cond_3_1 <= 0;
      _ram_b_cond_3_2 <= 0;
    end else begin
      if(_ram_b_cond_3_2) begin
        _tmp_109 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_24 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        ram_b_0_wenable <= 0;
        _tmp_103 <= 0;
      end 
      if(_ram_b_cond_2_1) begin
        _tmp_109 <= 1;
      end 
      _ram_b_cond_3_2 <= _ram_b_cond_3_1;
      if((_tmp_fsm_1 == 1) && (_tmp_23 == 0)) begin
        ram_b_0_addr <= _tmp_14 - _tmp_17;
        _tmp_23 <= _tmp_16;
      end 
      if(__variable_valid_25 && ((_tmp_23 > 0) && !_tmp_24) && (_tmp_23 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + _tmp_17;
        ram_b_0_wdata <= __variable_data_25;
        ram_b_0_wenable <= 1;
        _tmp_23 <= _tmp_23 - 1;
      end 
      if(__variable_valid_25 && ((_tmp_23 > 0) && !_tmp_24) && (_tmp_23 == 1)) begin
        _tmp_24 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      __tmp_45_1 <= _tmp_45;
      __tmp_46_1 <= _tmp_46;
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && _tmp_48) begin
        _tmp_50 <= 0;
        _tmp_40 <= 0;
        _tmp_41 <= 0;
        _tmp_48 <= 0;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && _tmp_47) begin
        _tmp_40 <= 1;
        _tmp_41 <= 1;
        _tmp_50 <= _tmp_49;
        _tmp_49 <= 0;
        _tmp_47 <= 0;
        _tmp_48 <= 1;
      end 
      if((_mystream_fsm_9 == 1) && (_tmp_51 == 0) && !_tmp_49 && !_tmp_50) begin
        ram_b_0_addr <= _mystream_offset_4;
        _tmp_51 <= _mystream_size_3 - 1;
        _tmp_47 <= 1;
        _tmp_49 <= _mystream_size_3 == 1;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && (_tmp_51 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + _mystream_stride_5;
        _tmp_51 <= _tmp_51 - 1;
        _tmp_47 <= 1;
        _tmp_49 <= 0;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && (_tmp_51 == 1)) begin
        _tmp_49 <= 1;
      end 
      if((_tmp_fsm_4 == 1) && (_tmp_102 == 0)) begin
        ram_b_0_addr <= _tmp_93 - _tmp_96;
        _tmp_102 <= _tmp_95;
      end 
      if(__variable_valid_104 && ((_tmp_102 > 0) && !_tmp_103) && (_tmp_102 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + _tmp_96;
        ram_b_0_wdata <= __variable_data_104;
        ram_b_0_wenable <= 1;
        _tmp_102 <= _tmp_102 - 1;
      end 
      if(__variable_valid_104 && ((_tmp_102 > 0) && !_tmp_103) && (_tmp_102 == 1)) begin
        _tmp_103 <= 1;
      end 
      _ram_b_cond_1_1 <= 1;
      if(th_sequential == 7) begin
        ram_b_0_addr <= _th_sequential_i_19 + _th_sequential_offset_16;
      end 
      _ram_b_cond_2_1 <= th_sequential == 7;
      _ram_b_cond_3_1 <= th_sequential == 7;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_52 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_53 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_68_1 <= 0;
      __tmp_69_1 <= 0;
      _tmp_73 <= 0;
      _tmp_63 <= 0;
      _tmp_64 <= 0;
      _tmp_71 <= 0;
      _tmp_72 <= 0;
      _tmp_70 <= 0;
      _tmp_74 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_122_1 <= 0;
      __tmp_123_1 <= 0;
      _tmp_127 <= 0;
      _tmp_117 <= 0;
      _tmp_118 <= 0;
      _tmp_125 <= 0;
      _tmp_126 <= 0;
      _tmp_124 <= 0;
      _tmp_128 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_133 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_135 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_133 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_135 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_53 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_133 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_135 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if((_mystream_fsm_11 == 1) && (_tmp_52 == 0)) begin
        ram_c_0_addr <= _mystream_offset_4 - 1;
        _tmp_52 <= 1;
      end 
      if(_pulse_data_56 && (_reduceadd_valid_55 && ((_tmp_52 > 0) && !_tmp_53 && _tmp_all_valid_54)) && (_tmp_52 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _reduceadd_data_55;
        ram_c_0_wenable <= 1;
        _tmp_52 <= _tmp_52 - 1;
      end 
      if(_pulse_data_56 && (_reduceadd_valid_55 && ((_tmp_52 > 0) && !_tmp_53 && _tmp_all_valid_54)) && (_tmp_52 == 1)) begin
        _tmp_53 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_68_1 <= _tmp_68;
      __tmp_69_1 <= _tmp_69;
      if((_tmp_65 || !_tmp_63) && (_tmp_66 || !_tmp_64) && _tmp_71) begin
        _tmp_73 <= 0;
        _tmp_63 <= 0;
        _tmp_64 <= 0;
        _tmp_71 <= 0;
      end 
      if((_tmp_65 || !_tmp_63) && (_tmp_66 || !_tmp_64) && _tmp_70) begin
        _tmp_63 <= 1;
        _tmp_64 <= 1;
        _tmp_73 <= _tmp_72;
        _tmp_72 <= 0;
        _tmp_70 <= 0;
        _tmp_71 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_74 == 0) && !_tmp_72 && !_tmp_73) begin
        ram_c_0_addr <= _tmp_57;
        _tmp_74 <= _tmp_59 - 1;
        _tmp_70 <= 1;
        _tmp_72 <= _tmp_59 == 1;
      end 
      if((_tmp_65 || !_tmp_63) && (_tmp_66 || !_tmp_64) && (_tmp_74 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_74 <= _tmp_74 - 1;
        _tmp_70 <= 1;
        _tmp_72 <= 0;
      end 
      if((_tmp_65 || !_tmp_63) && (_tmp_66 || !_tmp_64) && (_tmp_74 == 1)) begin
        _tmp_72 <= 1;
      end 
      if(th_sequential == 11) begin
        ram_c_0_addr <= _th_sequential_offset_16;
        ram_c_0_wdata <= _th_sequential_sum_18;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_sequential == 11;
      __tmp_122_1 <= _tmp_122;
      __tmp_123_1 <= _tmp_123;
      if((_tmp_119 || !_tmp_117) && (_tmp_120 || !_tmp_118) && _tmp_125) begin
        _tmp_127 <= 0;
        _tmp_117 <= 0;
        _tmp_118 <= 0;
        _tmp_125 <= 0;
      end 
      if((_tmp_119 || !_tmp_117) && (_tmp_120 || !_tmp_118) && _tmp_124) begin
        _tmp_117 <= 1;
        _tmp_118 <= 1;
        _tmp_127 <= _tmp_126;
        _tmp_126 <= 0;
        _tmp_124 <= 0;
        _tmp_125 <= 1;
      end 
      if((_tmp_fsm_5 == 1) && (_tmp_128 == 0) && !_tmp_126 && !_tmp_127) begin
        ram_c_0_addr <= _tmp_111;
        _tmp_128 <= _tmp_113 - 1;
        _tmp_124 <= 1;
        _tmp_126 <= _tmp_113 == 1;
      end 
      if((_tmp_119 || !_tmp_117) && (_tmp_120 || !_tmp_118) && (_tmp_128 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_128 <= _tmp_128 - 1;
        _tmp_124 <= 1;
        _tmp_126 <= 0;
      end 
      if((_tmp_119 || !_tmp_117) && (_tmp_120 || !_tmp_118) && (_tmp_128 == 1)) begin
        _tmp_126 <= 1;
      end 
      if(th_comp == 24) begin
        ram_c_0_addr <= _th_comp_offset_stream_23;
      end 
      _ram_c_cond_2_1 <= th_comp == 24;
      _ram_c_cond_3_1 <= th_comp == 24;
      if(th_comp == 26) begin
        ram_c_0_addr <= _th_comp_offset_seq_24;
      end 
      _ram_c_cond_4_1 <= th_comp == 26;
      _ram_c_cond_5_1 <= th_comp == 26;
    end
  end

  assign __variable_data_77 = _tmp_69;
  assign __variable_valid_77 = _tmp_63;
  assign _tmp_65 = 1 && __variable_ready_77;
  assign __variable_data_131 = _tmp_123;
  assign __variable_valid_131 = _tmp_117;
  assign _tmp_119 = 1 && __variable_ready_131;
  wire [32-1:0] _times_data_137;
  wire _times_valid_137;
  wire _times_ready_137;
  wire [64-1:0] _times_odata_137;
  reg [64-1:0] _times_data_reg_137;
  assign _times_data_137 = _times_data_reg_137;
  wire _times_ovalid_137;
  reg _times_valid_reg_137;
  assign _times_valid_137 = _times_valid_reg_137;
  wire _times_enable_137;
  wire _times_update_137;
  assign _times_enable_137 = (_times_ready_137 || !_times_valid_137) && (_tmp_30 && _tmp_42) && (_tmp_28 && _tmp_40);
  assign _times_update_137 = _times_ready_137 || !_times_valid_137;

  multiplier_0
  mul137
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_137),
    .enable(_times_enable_137),
    .valid(_times_ovalid_137),
    .a(_tmp_34),
    .b(_tmp_46),
    .c(_times_odata_137)
  );

  assign _tmp_30 = 1 && ((_times_ready_137 || !_times_valid_137) && (_tmp_28 && _tmp_40));
  assign _tmp_42 = 1 && ((_times_ready_137 || !_times_valid_137) && (_tmp_28 && _tmp_40));
  reg [32-1:0] _reduceadd_data_138;
  reg _reduceadd_valid_138;
  wire _reduceadd_ready_138;
  reg [33-1:0] _reduceadd_count_138;
  reg [1-1:0] _pulse_data_139;
  reg _pulse_valid_139;
  wire _pulse_ready_139;
  reg [33-1:0] _pulse_count_139;
  assign _times_ready_137 = (_reduceadd_ready_138 || !_reduceadd_valid_138) && _times_valid_137 && ((_pulse_ready_139 || !_pulse_valid_139) && _times_valid_137);
  assign _reduceadd_data_55 = _reduceadd_data_138;
  assign _reduceadd_valid_55 = _reduceadd_valid_138;
  assign _reduceadd_ready_138 = _reduceadd_ready_55;
  assign _pulse_data_56 = _pulse_data_139;
  assign _pulse_valid_56 = _pulse_valid_139;
  assign _pulse_ready_139 = _pulse_ready_56;

  always @(posedge CLK) begin
    if(RST) begin
      _times_data_reg_137 <= 0;
      _times_valid_reg_137 <= 0;
      _reduceadd_data_138 <= 1'sd0;
      _reduceadd_count_138 <= 0;
      _reduceadd_valid_138 <= 0;
      _pulse_data_139 <= 1'sd0;
      _pulse_count_139 <= 0;
      _pulse_valid_139 <= 0;
    end else begin
      if(_times_ready_137 || !_times_valid_137) begin
        _times_data_reg_137 <= _times_odata_137;
      end 
      if(_times_ready_137 || !_times_valid_137) begin
        _times_valid_reg_137 <= _times_ovalid_137;
      end 
      if((_reduceadd_ready_138 || !_reduceadd_valid_138) && _times_ready_137 && _times_valid_137) begin
        _reduceadd_data_138 <= _reduceadd_data_138 + _times_data_137;
      end 
      if((_reduceadd_ready_138 || !_reduceadd_valid_138) && _times_ready_137 && _times_valid_137) begin
        _reduceadd_count_138 <= (_reduceadd_count_138 == _mystream_size_3 - 1)? 0 : _reduceadd_count_138 + 1;
      end 
      if(_reduceadd_valid_138 && _reduceadd_ready_138) begin
        _reduceadd_valid_138 <= 0;
      end 
      if((_reduceadd_ready_138 || !_reduceadd_valid_138) && _times_ready_137) begin
        _reduceadd_valid_138 <= _times_valid_137;
      end 
      if((_reduceadd_ready_138 || !_reduceadd_valid_138) && _times_ready_137 && _times_valid_137 && (_reduceadd_count_138 == 0)) begin
        _reduceadd_data_138 <= 1'sd0 + _times_data_137;
      end 
      if((_pulse_ready_139 || !_pulse_valid_139) && _times_ready_137 && _times_valid_137) begin
        _pulse_data_139 <= _pulse_count_139 == _mystream_size_3 - 1;
      end 
      if((_pulse_ready_139 || !_pulse_valid_139) && _times_ready_137 && _times_valid_137) begin
        _pulse_count_139 <= (_pulse_count_139 == _mystream_size_3 - 1)? 0 : _pulse_count_139 + 1;
      end 
      if(_pulse_valid_139 && _pulse_ready_139) begin
        _pulse_valid_139 <= 0;
      end 
      if((_pulse_ready_139 || !_pulse_valid_139) && _times_ready_137) begin
        _pulse_valid_139 <= _times_valid_137;
      end 
      if((_pulse_ready_139 || !_pulse_valid_139) && _times_ready_137 && _times_valid_137 && (_pulse_count_139 == 0)) begin
        _pulse_data_139 <= _pulse_count_139 == _mystream_size_3 - 1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_offset_1 <= 0;
      _th_comp_stride_2 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 1;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_17 <= 1;
      _tmp_57 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _tmp_79 <= 0;
      _tmp_80 <= 0;
      _tmp_81 <= 0;
      _tmp_82 <= 1;
      _tmp_93 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 1;
      _tmp_111 <= 0;
      _tmp_112 <= 0;
      _tmp_113 <= 0;
      _th_comp_size_22 <= 0;
      _th_comp_offset_stream_23 <= 0;
      _th_comp_offset_seq_24 <= 0;
      _th_comp_all_ok_25 <= 0;
      _tmp_134 <= 0;
      _th_comp_st_26 <= 0;
      _tmp_136 <= 0;
      _th_comp_sq_27 <= 0;
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
          _th_comp_stride_2 <= 2;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          _tmp_0 <= _th_comp_offset_1;
          _tmp_1 <= 0;
          _tmp_2 <= _th_comp_size_0;
          _tmp_3 <= _th_comp_stride_2;
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          if(_tmp_13) begin
            th_comp <= th_comp_5;
          end 
        end
        th_comp_5: begin
          _tmp_14 <= _th_comp_offset_1;
          _tmp_15 <= 0;
          _tmp_16 <= _th_comp_size_0;
          _tmp_17 <= _th_comp_stride_2;
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          if(_tmp_27) begin
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
          _tmp_57 <= _th_comp_offset_1;
          _tmp_58 <= 1024;
          _tmp_59 <= 1;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if(_tmp_78) begin
            th_comp <= th_comp_13;
          end 
        end
        th_comp_13: begin
          _th_comp_offset_1 <= _th_comp_size_0;
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          _tmp_79 <= _th_comp_offset_1;
          _tmp_80 <= 0;
          _tmp_81 <= _th_comp_size_0;
          _tmp_82 <= _th_comp_stride_2;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(_tmp_92) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          _tmp_93 <= _th_comp_offset_1;
          _tmp_94 <= 0;
          _tmp_95 <= _th_comp_size_0;
          _tmp_96 <= _th_comp_stride_2;
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          if(_tmp_106) begin
            th_comp <= th_comp_18;
          end 
        end
        th_comp_18: begin
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(th_sequential == 12) begin
            th_comp <= th_comp_20;
          end 
        end
        th_comp_20: begin
          _tmp_111 <= _th_comp_offset_1;
          _tmp_112 <= 2048;
          _tmp_113 <= 1;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          if(_tmp_132) begin
            th_comp <= th_comp_22;
          end 
        end
        th_comp_22: begin
          _th_comp_size_22 <= _th_comp_size_0;
          _th_comp_offset_stream_23 <= 0;
          _th_comp_offset_seq_24 <= _th_comp_offset_1;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          _th_comp_all_ok_25 <= 1;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          if(_tmp_133) begin
            _tmp_134 <= ram_c_0_rdata;
          end 
          if(_tmp_133) begin
            th_comp <= th_comp_25;
          end 
        end
        th_comp_25: begin
          _th_comp_st_26 <= _tmp_134;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          if(_tmp_135) begin
            _tmp_136 <= ram_c_0_rdata;
          end 
          if(_tmp_135) begin
            th_comp <= th_comp_27;
          end 
        end
        th_comp_27: begin
          _th_comp_sq_27 <= _tmp_136;
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          if(_th_comp_st_26 !== _th_comp_sq_27) begin
            th_comp <= th_comp_29;
          end else begin
            th_comp <= th_comp_30;
          end
        end
        th_comp_29: begin
          _th_comp_all_ok_25 <= 0;
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          if(_th_comp_all_ok_25) begin
            th_comp <= th_comp_31;
          end else begin
            th_comp <= th_comp_33;
          end
        end
        th_comp_31: begin
          $display("OK");
          th_comp <= th_comp_32;
        end
        th_comp_32: begin
          th_comp <= th_comp_34;
        end
        th_comp_33: begin
          $display("NG");
          th_comp <= th_comp_34;
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
      __tmp_fsm_0_cond_4_0_1 <= 0;
      _tmp_8 <= 0;
      _tmp_7 <= 0;
      _tmp_13 <= 0;
      __tmp_fsm_0_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_4: begin
          if(__tmp_fsm_0_cond_4_0_1) begin
            _tmp_8 <= 0;
          end 
        end
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_1_1) begin
            _tmp_13 <= 0;
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
          _tmp_4 <= (_tmp_1 >> 2) << 2;
          _tmp_6 <= _tmp_2;
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
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_4;
          end 
        end
        _tmp_fsm_0_4: begin
          __tmp_fsm_0_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_7 <= myaxi_rdata;
            _tmp_8 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_4 <= _tmp_4 + (_tmp_5 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_6 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_6 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_13 <= 1;
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
      _tmp_18 <= 0;
      _tmp_20 <= 0;
      _tmp_19 <= 0;
      __tmp_fsm_1_cond_4_0_1 <= 0;
      _tmp_22 <= 0;
      _tmp_21 <= 0;
      _tmp_27 <= 0;
      __tmp_fsm_1_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_4: begin
          if(__tmp_fsm_1_cond_4_0_1) begin
            _tmp_22 <= 0;
          end 
        end
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_1_1) begin
            _tmp_27 <= 0;
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
          _tmp_18 <= (_tmp_15 >> 2) << 2;
          _tmp_20 <= _tmp_16;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_20 <= 256) && ((_tmp_18 & 4095) + (_tmp_20 << 2) >= 4096)) begin
            _tmp_19 <= 4096 - (_tmp_18 & 4095) >> 2;
            _tmp_20 <= _tmp_20 - (4096 - (_tmp_18 & 4095) >> 2);
          end else if(_tmp_20 <= 256) begin
            _tmp_19 <= _tmp_20;
            _tmp_20 <= 0;
          end else if((_tmp_18 & 4095) + 1024 >= 4096) begin
            _tmp_19 <= 4096 - (_tmp_18 & 4095) >> 2;
            _tmp_20 <= _tmp_20 - (4096 - (_tmp_18 & 4095) >> 2);
          end else begin
            _tmp_19 <= 256;
            _tmp_20 <= _tmp_20 - 256;
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
            _tmp_21 <= myaxi_rdata;
            _tmp_22 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_18 <= _tmp_18 + (_tmp_19 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_20 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_20 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_27 <= 1;
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
      _mystream_size_3 <= 0;
      _mystream_offset_4 <= 0;
      _mystream_stride_5 <= 0;
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
            _mystream_size_3 <= _th_comp_size_0;
          end 
          if(th_comp == 7) begin
            _mystream_offset_4 <= _th_comp_offset_1;
          end 
          if(th_comp == 7) begin
            _mystream_stride_5 <= _th_comp_stride_2;
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
          if(_mystream_done_flag_6 && _mystream_done_flag_8 && _mystream_done_flag_10) begin
            _mystream_running_reg <= 0;
          end 
          if(_mystream_done_flag_6 && _mystream_done_flag_8 && _mystream_done_flag_10) begin
            mystream <= mystream_init;
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
          if(_tmp_38) begin
            _mystream_done_flag_6 <= 1;
          end 
          if(_tmp_38) begin
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
          if(_tmp_50) begin
            _mystream_done_flag_8 <= 1;
          end 
          if(_tmp_50) begin
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

  localparam _mystream_fsm_11_1 = 1;
  localparam _mystream_fsm_11_2 = 2;
  localparam _mystream_fsm_11_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_11 <= _mystream_fsm_11_init;
      _mystream_done_flag_10 <= 0;
    end else begin
      case(_mystream_fsm_11)
        _mystream_fsm_11_init: begin
          if(_mystream_start_cond) begin
            _mystream_fsm_11 <= _mystream_fsm_11_1;
          end 
        end
        _mystream_fsm_11_1: begin
          _mystream_fsm_11 <= _mystream_fsm_11_2;
        end
        _mystream_fsm_11_2: begin
          if(_tmp_53) begin
            _mystream_done_flag_10 <= 1;
          end 
          if(_tmp_53) begin
            _mystream_fsm_11 <= _mystream_fsm_11_3;
          end 
        end
        _mystream_fsm_11_3: begin
          if(!_mystream_running) begin
            _mystream_done_flag_10 <= 0;
          end 
          if(!_mystream_running) begin
            _mystream_fsm_11 <= _mystream_fsm_11_init;
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
      _tmp_60 <= 0;
      _tmp_62 <= 0;
      _tmp_61 <= 0;
      _tmp_78 <= 0;
      __tmp_fsm_2_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_0_1) begin
            _tmp_78 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_comp == 12) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_60 <= (_tmp_58 >> 2) << 2;
          _tmp_62 <= _tmp_59;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_62 <= 256) && ((_tmp_60 & 4095) + (_tmp_62 << 2) >= 4096)) begin
            _tmp_61 <= 4096 - (_tmp_60 & 4095) >> 2;
            _tmp_62 <= _tmp_62 - (4096 - (_tmp_60 & 4095) >> 2);
          end else if(_tmp_62 <= 256) begin
            _tmp_61 <= _tmp_62;
            _tmp_62 <= 0;
          end else if((_tmp_60 & 4095) + 1024 >= 4096) begin
            _tmp_61 <= 4096 - (_tmp_60 & 4095) >> 2;
            _tmp_62 <= _tmp_62 - (4096 - (_tmp_60 & 4095) >> 2);
          end else begin
            _tmp_61 <= 256;
            _tmp_62 <= _tmp_62 - 256;
          end
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_4;
          end 
        end
        _tmp_fsm_2_4: begin
          if(_tmp_76 && myaxi_wvalid && myaxi_wready) begin
            _tmp_60 <= _tmp_60 + (_tmp_61 << 2);
          end 
          if(_tmp_76 && myaxi_wvalid && myaxi_wready && (_tmp_62 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(_tmp_76 && myaxi_wvalid && myaxi_wready && (_tmp_62 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_78 <= 1;
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
      _tmp_83 <= 0;
      _tmp_85 <= 0;
      _tmp_84 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_87 <= 0;
      _tmp_86 <= 0;
      _tmp_92 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_87 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_92 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_comp == 15) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_83 <= (_tmp_80 >> 2) << 2;
          _tmp_85 <= _tmp_81;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_85 <= 256) && ((_tmp_83 & 4095) + (_tmp_85 << 2) >= 4096)) begin
            _tmp_84 <= 4096 - (_tmp_83 & 4095) >> 2;
            _tmp_85 <= _tmp_85 - (4096 - (_tmp_83 & 4095) >> 2);
          end else if(_tmp_85 <= 256) begin
            _tmp_84 <= _tmp_85;
            _tmp_85 <= 0;
          end else if((_tmp_83 & 4095) + 1024 >= 4096) begin
            _tmp_84 <= 4096 - (_tmp_83 & 4095) >> 2;
            _tmp_85 <= _tmp_85 - (4096 - (_tmp_83 & 4095) >> 2);
          end else begin
            _tmp_84 <= 256;
            _tmp_85 <= _tmp_85 - 256;
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
            _tmp_86 <= myaxi_rdata;
            _tmp_87 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_83 <= _tmp_83 + (_tmp_84 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_85 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_85 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_92 <= 1;
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
      _tmp_97 <= 0;
      _tmp_99 <= 0;
      _tmp_98 <= 0;
      __tmp_fsm_4_cond_4_0_1 <= 0;
      _tmp_101 <= 0;
      _tmp_100 <= 0;
      _tmp_106 <= 0;
      __tmp_fsm_4_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_4 <= _tmp_fsm_4;
      case(_d1__tmp_fsm_4)
        _tmp_fsm_4_4: begin
          if(__tmp_fsm_4_cond_4_0_1) begin
            _tmp_101 <= 0;
          end 
        end
        _tmp_fsm_4_5: begin
          if(__tmp_fsm_4_cond_5_1_1) begin
            _tmp_106 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_4)
        _tmp_fsm_4_init: begin
          if(th_comp == 17) begin
            _tmp_fsm_4 <= _tmp_fsm_4_1;
          end 
        end
        _tmp_fsm_4_1: begin
          _tmp_97 <= (_tmp_94 >> 2) << 2;
          _tmp_99 <= _tmp_95;
          _tmp_fsm_4 <= _tmp_fsm_4_2;
        end
        _tmp_fsm_4_2: begin
          if((_tmp_99 <= 256) && ((_tmp_97 & 4095) + (_tmp_99 << 2) >= 4096)) begin
            _tmp_98 <= 4096 - (_tmp_97 & 4095) >> 2;
            _tmp_99 <= _tmp_99 - (4096 - (_tmp_97 & 4095) >> 2);
          end else if(_tmp_99 <= 256) begin
            _tmp_98 <= _tmp_99;
            _tmp_99 <= 0;
          end else if((_tmp_97 & 4095) + 1024 >= 4096) begin
            _tmp_98 <= 4096 - (_tmp_97 & 4095) >> 2;
            _tmp_99 <= _tmp_99 - (4096 - (_tmp_97 & 4095) >> 2);
          end else begin
            _tmp_98 <= 256;
            _tmp_99 <= _tmp_99 - 256;
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
            _tmp_100 <= myaxi_rdata;
            _tmp_101 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_97 <= _tmp_97 + (_tmp_98 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_99 > 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_99 == 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_5;
          end 
        end
        _tmp_fsm_4_5: begin
          _tmp_106 <= 1;
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
      _th_sequential_size_12 <= 0;
      _th_sequential_offset_13 <= 0;
      _th_sequential_stride_14 <= 0;
      _th_sequential_size_15 <= 0;
      _th_sequential_offset_16 <= 0;
      _th_sequential_stride_17 <= 0;
      _th_sequential_sum_18 <= 0;
      _th_sequential_i_19 <= 0;
      _tmp_108 <= 0;
      _th_sequential_a_20 <= 0;
      _tmp_110 <= 0;
      _th_sequential_b_21 <= 0;
    end else begin
      case(th_sequential)
        th_sequential_init: begin
          if(th_comp == 18) begin
            _th_sequential_called <= 1;
          end 
          if(th_comp == 18) begin
            _th_sequential_size_12 <= _th_comp_size_0;
          end 
          if(th_comp == 18) begin
            _th_sequential_offset_13 <= _th_comp_offset_1;
          end 
          if(th_comp == 18) begin
            _th_sequential_stride_14 <= _th_comp_stride_2;
          end 
          if(th_comp == 18) begin
            th_sequential <= th_sequential_1;
          end 
        end
        th_sequential_1: begin
          _th_sequential_size_15 <= _th_sequential_size_12;
          _th_sequential_offset_16 <= _th_sequential_offset_13;
          _th_sequential_stride_17 <= _th_sequential_stride_14;
          th_sequential <= th_sequential_2;
        end
        th_sequential_2: begin
          _th_sequential_sum_18 <= 0;
          th_sequential <= th_sequential_3;
        end
        th_sequential_3: begin
          _th_sequential_i_19 <= 0;
          th_sequential <= th_sequential_4;
        end
        th_sequential_4: begin
          if(_th_sequential_i_19 < (_th_sequential_size_15 << 1)) begin
            th_sequential <= th_sequential_5;
          end else begin
            th_sequential <= th_sequential_11;
          end
        end
        th_sequential_5: begin
          if(_tmp_107) begin
            _tmp_108 <= ram_a_0_rdata;
          end 
          if(_tmp_107) begin
            th_sequential <= th_sequential_6;
          end 
        end
        th_sequential_6: begin
          _th_sequential_a_20 <= _tmp_108;
          th_sequential <= th_sequential_7;
        end
        th_sequential_7: begin
          if(_tmp_109) begin
            _tmp_110 <= ram_b_0_rdata;
          end 
          if(_tmp_109) begin
            th_sequential <= th_sequential_8;
          end 
        end
        th_sequential_8: begin
          _th_sequential_b_21 <= _tmp_110;
          th_sequential <= th_sequential_9;
        end
        th_sequential_9: begin
          _th_sequential_sum_18 <= _th_sequential_sum_18 + _th_sequential_a_20 * _th_sequential_b_21;
          th_sequential <= th_sequential_10;
        end
        th_sequential_10: begin
          _th_sequential_i_19 <= _th_sequential_i_19 + _th_sequential_stride_17;
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
      _tmp_114 <= 0;
      _tmp_116 <= 0;
      _tmp_115 <= 0;
      _tmp_132 <= 0;
      __tmp_fsm_5_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_5 <= _tmp_fsm_5;
      case(_d1__tmp_fsm_5)
        _tmp_fsm_5_5: begin
          if(__tmp_fsm_5_cond_5_0_1) begin
            _tmp_132 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_5)
        _tmp_fsm_5_init: begin
          if(th_comp == 21) begin
            _tmp_fsm_5 <= _tmp_fsm_5_1;
          end 
        end
        _tmp_fsm_5_1: begin
          _tmp_114 <= (_tmp_112 >> 2) << 2;
          _tmp_116 <= _tmp_113;
          _tmp_fsm_5 <= _tmp_fsm_5_2;
        end
        _tmp_fsm_5_2: begin
          if((_tmp_116 <= 256) && ((_tmp_114 & 4095) + (_tmp_116 << 2) >= 4096)) begin
            _tmp_115 <= 4096 - (_tmp_114 & 4095) >> 2;
            _tmp_116 <= _tmp_116 - (4096 - (_tmp_114 & 4095) >> 2);
          end else if(_tmp_116 <= 256) begin
            _tmp_115 <= _tmp_116;
            _tmp_116 <= 0;
          end else if((_tmp_114 & 4095) + 1024 >= 4096) begin
            _tmp_115 <= 4096 - (_tmp_114 & 4095) >> 2;
            _tmp_116 <= _tmp_116 - (4096 - (_tmp_114 & 4095) >> 2);
          end else begin
            _tmp_115 <= 256;
            _tmp_116 <= _tmp_116 - 256;
          end
          _tmp_fsm_5 <= _tmp_fsm_5_3;
        end
        _tmp_fsm_5_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_5 <= _tmp_fsm_5_4;
          end 
        end
        _tmp_fsm_5_4: begin
          if(_tmp_130 && myaxi_wvalid && myaxi_wready) begin
            _tmp_114 <= _tmp_114 + (_tmp_115 << 2);
          end 
          if(_tmp_130 && myaxi_wvalid && myaxi_wready && (_tmp_116 > 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_2;
          end 
          if(_tmp_130 && myaxi_wvalid && myaxi_wready && (_tmp_116 == 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_5;
          end 
        end
        _tmp_fsm_5_5: begin
          _tmp_132 <= 1;
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
    test_module = thread_stream_stride.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
