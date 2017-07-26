from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_matmul

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
    $readmemh("mymem.out", _memory_mem);
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

  reg [32-1:0] timer;
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

  reg [32-1:0] th_matmul;
  localparam th_matmul_init = 0;
  reg signed [32-1:0] _th_matmul_matrix_size_0;
  reg signed [32-1:0] _th_matmul_a_offset_1;
  reg signed [32-1:0] _th_matmul_b_offset_2;
  reg signed [32-1:0] _th_matmul_c_offset_3;
  reg signed [32-1:0] _th_matmul_start_time_4;
  reg signed [32-1:0] _th_matmul_matrix_size_5;
  reg signed [32-1:0] _th_matmul_a_offset_6;
  reg signed [32-1:0] _th_matmul_b_offset_7;
  reg signed [32-1:0] _th_matmul_c_offset_8;
  reg signed [32-1:0] _th_matmul_a_addr_9;
  reg signed [32-1:0] _th_matmul_c_addr_10;
  reg signed [32-1:0] _th_matmul_i_11;
  reg [10-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [9-1:0] _tmp_4;
  reg _myaxi_cond_0_1;
  reg [32-1:0] _tmp_5;
  reg _tmp_6;
  reg [33-1:0] _tmp_7;
  reg _tmp_8;
  wire [32-1:0] _tmp_data_9;
  wire _tmp_valid_9;
  wire _tmp_ready_9;
  assign _tmp_ready_9 = (_tmp_7 > 0) && !_tmp_8;
  reg _ram_a_cond_0_1;
  reg signed [32-1:0] _th_matmul_b_addr_12;
  reg signed [32-1:0] _th_matmul_j_13;
  reg [10-1:0] _tmp_10;
  reg [32-1:0] _tmp_11;
  reg [32-1:0] _tmp_12;
  reg [32-1:0] _tmp_13;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [9-1:0] _tmp_14;
  reg _myaxi_cond_1_1;
  reg [32-1:0] _tmp_15;
  reg _tmp_16;
  reg [33-1:0] _tmp_17;
  reg _tmp_18;
  wire [32-1:0] _tmp_data_19;
  wire _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_17 > 0) && !_tmp_18;
  reg _ram_b_cond_0_1;
  reg _strm_madd_flag_14;
  reg [32-1:0] _strm_madd_fsm_15;
  localparam _strm_madd_fsm_15_init = 0;
  reg _tmp_20;
  reg _tmp_21;
  wire _tmp_22;
  wire _tmp_23;
  assign _tmp_23 = 1;
  localparam _tmp_24 = 1;
  wire [_tmp_24-1:0] _tmp_25;
  assign _tmp_25 = (_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21);
  reg [_tmp_24-1:0] __tmp_25_1;
  wire [32-1:0] _tmp_26;
  reg [32-1:0] __tmp_26_1;
  assign _tmp_26 = (__tmp_25_1)? ram_a_0_rdata : __tmp_26_1;
  reg [33-1:0] _tmp_27;
  reg _tmp_28;
  reg _tmp_29;
  reg _tmp_30;
  reg _tmp_31;
  reg _strm_madd_flag_16;
  reg [32-1:0] _strm_madd_fsm_17;
  localparam _strm_madd_fsm_17_init = 0;
  reg _tmp_32;
  reg _tmp_33;
  wire _tmp_34;
  wire _tmp_35;
  assign _tmp_35 = 1;
  localparam _tmp_36 = 1;
  wire [_tmp_36-1:0] _tmp_37;
  assign _tmp_37 = (_tmp_34 || !_tmp_32) && (_tmp_35 || !_tmp_33);
  reg [_tmp_36-1:0] __tmp_37_1;
  wire [32-1:0] _tmp_38;
  reg [32-1:0] __tmp_38_1;
  assign _tmp_38 = (__tmp_37_1)? ram_b_0_rdata : __tmp_38_1;
  reg [33-1:0] _tmp_39;
  reg _tmp_40;
  reg _tmp_41;
  reg _tmp_42;
  reg _tmp_43;
  reg _strm_madd_flag_18;
  reg [32-1:0] _strm_madd_fsm_19;
  localparam _strm_madd_fsm_19_init = 0;
  reg [2-1:0] _tmp_44;
  reg _tmp_45;
  wire _tmp_all_valid_46;
  wire [32-1:0] _tmp_data_47;
  wire _tmp_valid_47;
  wire _tmp_ready_47;
  assign _tmp_ready_47 = (_tmp_44 > 0) && !_tmp_45 && _tmp_all_valid_46;
  wire [1-1:0] _tmp_data_48;
  wire _tmp_valid_48;
  wire _tmp_ready_48;
  assign _tmp_ready_48 = (_tmp_44 > 0) && !_tmp_45 && _tmp_all_valid_46;
  assign _tmp_all_valid_46 = _tmp_valid_47 && _tmp_valid_48;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_49;
  reg [32-1:0] _tmp_50;
  reg [32-1:0] _tmp_51;
  reg [32-1:0] _tmp_52;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [9-1:0] _tmp_53;
  reg _myaxi_cond_2_1;
  reg _tmp_54;
  reg _tmp_55;
  wire _tmp_56;
  wire _tmp_57;
  assign _tmp_57 = 1;
  localparam _tmp_58 = 1;
  wire [_tmp_58-1:0] _tmp_59;
  assign _tmp_59 = (_tmp_56 || !_tmp_54) && (_tmp_57 || !_tmp_55);
  reg [_tmp_58-1:0] __tmp_59_1;
  wire [32-1:0] _tmp_60;
  reg [32-1:0] __tmp_60_1;
  assign _tmp_60 = (__tmp_59_1)? ram_c_0_rdata : __tmp_60_1;
  reg [33-1:0] _tmp_61;
  reg _tmp_62;
  reg _tmp_63;
  reg _tmp_64;
  reg _tmp_65;
  reg _tmp_66;
  wire [32-1:0] _tmp_data_67;
  wire _tmp_valid_67;
  wire _tmp_ready_67;
  assign _tmp_ready_67 = (_tmp_fsm_2 == 3) && ((_tmp_53 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg signed [32-1:0] _th_matmul_end_time_20;
  reg signed [32-1:0] _th_matmul_time_21;
  reg signed [32-1:0] _th_matmul_matrix_size_22;
  reg signed [32-1:0] _th_matmul_a_offset_23;
  reg signed [32-1:0] _th_matmul_b_offset_24;
  reg signed [32-1:0] _th_matmul_c_offset_25;
  reg signed [32-1:0] _th_matmul_all_ok_26;
  reg signed [32-1:0] _th_matmul_c_addr_27;
  reg signed [32-1:0] _th_matmul_i_28;
  reg [10-1:0] _tmp_68;
  reg [32-1:0] _tmp_69;
  reg [32-1:0] _tmp_70;
  reg [32-1:0] _tmp_71;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [9-1:0] _tmp_72;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _tmp_73;
  reg _tmp_74;
  reg [33-1:0] _tmp_75;
  reg _tmp_76;
  wire [32-1:0] _tmp_data_77;
  wire _tmp_valid_77;
  wire _tmp_ready_77;
  assign _tmp_ready_77 = (_tmp_75 > 0) && !_tmp_76;
  reg _ram_c_cond_1_1;
  assign myaxi_rready = (_tmp_fsm_0 == 3) || (_tmp_fsm_1 == 3) || (_tmp_fsm_3 == 3);
  reg signed [32-1:0] _th_matmul_j_29;
  reg _tmp_78;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_79;
  reg signed [32-1:0] _th_matmul_v_30;

  always @(posedge CLK) begin
    if(RST) begin
      timer <= 0;
    end else begin
      timer <= timer + 1;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_7 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_8 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_25_1 <= 0;
      __tmp_26_1 <= 0;
      _tmp_31 <= 0;
      _tmp_20 <= 0;
      _tmp_21 <= 0;
      _tmp_29 <= 0;
      _tmp_30 <= 0;
      _tmp_28 <= 0;
      _tmp_27 <= 0;
    end else begin
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_8 <= 0;
      end 
      if((_tmp_fsm_0 == 2) && (_tmp_7 == 0)) begin
        ram_a_0_addr <= _tmp_0 - 1;
        _tmp_7 <= _tmp_2;
      end 
      if(_tmp_valid_9 && ((_tmp_7 > 0) && !_tmp_8) && (_tmp_7 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_9;
        ram_a_0_wenable <= 1;
        _tmp_7 <= _tmp_7 - 1;
      end 
      if(_tmp_valid_9 && ((_tmp_7 > 0) && !_tmp_8) && (_tmp_7 == 1)) begin
        _tmp_8 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      __tmp_25_1 <= _tmp_25;
      __tmp_26_1 <= _tmp_26;
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && _tmp_29) begin
        _tmp_31 <= 0;
        _tmp_20 <= 0;
        _tmp_21 <= 0;
        _tmp_29 <= 0;
      end 
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && _tmp_28) begin
        _tmp_20 <= 1;
        _tmp_21 <= 1;
        _tmp_31 <= _tmp_30;
        _tmp_30 <= 0;
        _tmp_28 <= 0;
        _tmp_29 <= 1;
      end 
      if((_strm_madd_fsm_15 == 1) && (_tmp_27 == 0) && !_tmp_30 && !_tmp_31) begin
        ram_a_0_addr <= 0;
        _tmp_27 <= _th_matmul_matrix_size_5 - 1;
        _tmp_28 <= 1;
      end 
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && (_tmp_27 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        _tmp_27 <= _tmp_27 - 1;
        _tmp_28 <= 1;
        _tmp_30 <= 0;
      end 
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && (_tmp_27 == 1)) begin
        _tmp_30 <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_17 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_18 <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_37_1 <= 0;
      __tmp_38_1 <= 0;
      _tmp_43 <= 0;
      _tmp_32 <= 0;
      _tmp_33 <= 0;
      _tmp_41 <= 0;
      _tmp_42 <= 0;
      _tmp_40 <= 0;
      _tmp_39 <= 0;
    end else begin
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_18 <= 0;
      end 
      if((_tmp_fsm_1 == 2) && (_tmp_17 == 0)) begin
        ram_b_0_addr <= _tmp_10 - 1;
        _tmp_17 <= _tmp_12;
      end 
      if(_tmp_valid_19 && ((_tmp_17 > 0) && !_tmp_18) && (_tmp_17 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_19;
        ram_b_0_wenable <= 1;
        _tmp_17 <= _tmp_17 - 1;
      end 
      if(_tmp_valid_19 && ((_tmp_17 > 0) && !_tmp_18) && (_tmp_17 == 1)) begin
        _tmp_18 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      __tmp_37_1 <= _tmp_37;
      __tmp_38_1 <= _tmp_38;
      if((_tmp_34 || !_tmp_32) && (_tmp_35 || !_tmp_33) && _tmp_41) begin
        _tmp_43 <= 0;
        _tmp_32 <= 0;
        _tmp_33 <= 0;
        _tmp_41 <= 0;
      end 
      if((_tmp_34 || !_tmp_32) && (_tmp_35 || !_tmp_33) && _tmp_40) begin
        _tmp_32 <= 1;
        _tmp_33 <= 1;
        _tmp_43 <= _tmp_42;
        _tmp_42 <= 0;
        _tmp_40 <= 0;
        _tmp_41 <= 1;
      end 
      if((_strm_madd_fsm_17 == 1) && (_tmp_39 == 0) && !_tmp_42 && !_tmp_43) begin
        ram_b_0_addr <= 0;
        _tmp_39 <= _th_matmul_matrix_size_5 - 1;
        _tmp_40 <= 1;
      end 
      if((_tmp_34 || !_tmp_32) && (_tmp_35 || !_tmp_33) && (_tmp_39 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        _tmp_39 <= _tmp_39 - 1;
        _tmp_40 <= 1;
        _tmp_42 <= 0;
      end 
      if((_tmp_34 || !_tmp_32) && (_tmp_35 || !_tmp_33) && (_tmp_39 == 1)) begin
        _tmp_42 <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_44 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_45 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_59_1 <= 0;
      __tmp_60_1 <= 0;
      _tmp_65 <= 0;
      _tmp_54 <= 0;
      _tmp_55 <= 0;
      _tmp_63 <= 0;
      _tmp_64 <= 0;
      _tmp_62 <= 0;
      _tmp_61 <= 0;
      _tmp_75 <= 0;
      _tmp_76 <= 0;
      _ram_c_cond_1_1 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_78 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_78 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_45 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
        _tmp_76 <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_78 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if((_strm_madd_fsm_19 == 1) && (_tmp_44 == 0)) begin
        ram_c_0_addr <= _th_matmul_j_13 - 1;
        _tmp_44 <= 1;
      end 
      if(_tmp_data_48 && (_tmp_valid_47 && ((_tmp_44 > 0) && !_tmp_45 && _tmp_all_valid_46)) && (_tmp_44 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_47;
        ram_c_0_wenable <= 1;
        _tmp_44 <= _tmp_44 - 1;
      end 
      if(_tmp_data_48 && (_tmp_valid_47 && ((_tmp_44 > 0) && !_tmp_45 && _tmp_all_valid_46)) && (_tmp_44 == 1)) begin
        _tmp_45 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_59_1 <= _tmp_59;
      __tmp_60_1 <= _tmp_60;
      if((_tmp_56 || !_tmp_54) && (_tmp_57 || !_tmp_55) && _tmp_63) begin
        _tmp_65 <= 0;
        _tmp_54 <= 0;
        _tmp_55 <= 0;
        _tmp_63 <= 0;
      end 
      if((_tmp_56 || !_tmp_54) && (_tmp_57 || !_tmp_55) && _tmp_62) begin
        _tmp_54 <= 1;
        _tmp_55 <= 1;
        _tmp_65 <= _tmp_64;
        _tmp_64 <= 0;
        _tmp_62 <= 0;
        _tmp_63 <= 1;
      end 
      if((_tmp_fsm_2 == 2) && (_tmp_61 == 0) && !_tmp_64 && !_tmp_65) begin
        ram_c_0_addr <= _tmp_49;
        _tmp_61 <= _tmp_51 - 1;
        _tmp_62 <= 1;
      end 
      if((_tmp_56 || !_tmp_54) && (_tmp_57 || !_tmp_55) && (_tmp_61 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_61 <= _tmp_61 - 1;
        _tmp_62 <= 1;
        _tmp_64 <= 0;
      end 
      if((_tmp_56 || !_tmp_54) && (_tmp_57 || !_tmp_55) && (_tmp_61 == 1)) begin
        _tmp_64 <= 1;
      end 
      if((_tmp_fsm_3 == 2) && (_tmp_75 == 0)) begin
        ram_c_0_addr <= _tmp_68 - 1;
        _tmp_75 <= _tmp_70;
      end 
      if(_tmp_valid_77 && ((_tmp_75 > 0) && !_tmp_76) && (_tmp_75 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_77;
        ram_c_0_wenable <= 1;
        _tmp_75 <= _tmp_75 - 1;
      end 
      if(_tmp_valid_77 && ((_tmp_75 > 0) && !_tmp_76) && (_tmp_75 == 1)) begin
        _tmp_76 <= 1;
      end 
      _ram_c_cond_1_1 <= 1;
      if(th_matmul == 38) begin
        ram_c_0_addr <= _th_matmul_j_29;
      end 
      _ram_c_cond_2_1 <= th_matmul == 38;
      _ram_c_cond_3_1 <= th_matmul == 38;
    end
  end

  assign _tmp_data_67 = _tmp_60;
  assign _tmp_valid_67 = _tmp_54;
  assign _tmp_56 = 1 && _tmp_ready_67;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_4 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_14 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_53 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_66 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_72 <= 0;
      _myaxi_cond_4_1 <= 0;
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
        _tmp_66 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_tmp_fsm_0 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_4 == 0))) begin
        myaxi_araddr <= _tmp_1;
        myaxi_arlen <= _tmp_2 - 1;
        myaxi_arvalid <= 1;
        _tmp_4 <= _tmp_2;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_4 > 0)) begin
        _tmp_4 <= _tmp_4 - 1;
      end 
      if((_tmp_fsm_1 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_14 == 0))) begin
        myaxi_araddr <= _tmp_11;
        myaxi_arlen <= _tmp_12 - 1;
        myaxi_arvalid <= 1;
        _tmp_14 <= _tmp_12;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_14 > 0)) begin
        _tmp_14 <= _tmp_14 - 1;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_53 == 0))) begin
        myaxi_awaddr <= _tmp_50;
        myaxi_awlen <= _tmp_51 - 1;
        myaxi_awvalid <= 1;
        _tmp_53 <= _tmp_51;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_53 == 0)) && (_tmp_51 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_67 && ((_tmp_fsm_2 == 3) && ((_tmp_53 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_53 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_53 > 0))) begin
        myaxi_wdata <= _tmp_data_67;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_53 <= _tmp_53 - 1;
      end 
      if(_tmp_valid_67 && ((_tmp_fsm_2 == 3) && ((_tmp_53 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_53 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_53 > 0)) && (_tmp_53 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_66 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_66 <= _tmp_66;
      end 
      if((_tmp_fsm_3 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_72 == 0))) begin
        myaxi_araddr <= _tmp_69;
        myaxi_arlen <= _tmp_70 - 1;
        myaxi_arvalid <= 1;
        _tmp_72 <= _tmp_70;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_72 > 0)) begin
        _tmp_72 <= _tmp_72 - 1;
      end 
    end
  end

  assign _tmp_data_9 = _tmp_5;
  assign _tmp_valid_9 = _tmp_6;
  assign _tmp_data_19 = _tmp_15;
  assign _tmp_valid_19 = _tmp_16;
  assign _tmp_data_77 = _tmp_73;
  assign _tmp_valid_77 = _tmp_74;
  reg [32-1:0] _tmp_data_80;
  reg _tmp_valid_80;
  wire _tmp_ready_80;
  wire [32-1:0] _tmp_data_81;
  wire _tmp_valid_81;
  wire _tmp_ready_81;
  wire [64-1:0] _tmp_odata_81;
  reg [64-1:0] _tmp_data_reg_81;
  assign _tmp_data_81 = _tmp_data_reg_81;
  wire _tmp_ovalid_81;
  reg _tmp_valid_reg_81;
  assign _tmp_valid_81 = _tmp_valid_reg_81;
  wire _tmp_enable_81;
  wire _tmp_update_81;
  assign _tmp_enable_81 = (_tmp_ready_81 || !_tmp_valid_81) && (_tmp_22 && _tmp_34) && (_tmp_20 && _tmp_32);
  assign _tmp_update_81 = _tmp_ready_81 || !_tmp_valid_81;

  multiplier_0
  mul81
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_81),
    .enable(_tmp_enable_81),
    .valid(_tmp_ovalid_81),
    .a(_tmp_26),
    .b(_tmp_38),
    .c(_tmp_odata_81)
  );

  assign _tmp_22 = 1 && ((_tmp_ready_81 || !_tmp_valid_81) && (_tmp_20 && _tmp_32));
  assign _tmp_34 = 1 && ((_tmp_ready_81 || !_tmp_valid_81) && (_tmp_20 && _tmp_32));
  reg [1-1:0] _tmp_data_82;
  reg _tmp_valid_82;
  wire _tmp_ready_82;
  assign _tmp_ready_80 = (_tmp_ready_82 || !_tmp_valid_82) && _tmp_valid_80;
  reg [1-1:0] _tmp_data_83;
  reg [1-1:0] _tmp_data_84;
  reg [1-1:0] _tmp_data_85;
  reg _tmp_valid_85;
  wire _tmp_ready_85;
  reg [1-1:0] _tmp_data_86;
  reg _tmp_valid_86;
  wire _tmp_ready_86;
  assign _tmp_ready_82 = (_tmp_ready_85 || !_tmp_valid_85) && _tmp_valid_82 && ((_tmp_ready_86 || !_tmp_valid_86) && _tmp_valid_82);
  reg [1-1:0] _tmp_data_87;
  reg _tmp_valid_87;
  wire _tmp_ready_87;
  assign _tmp_ready_85 = (_tmp_ready_87 || !_tmp_valid_87) && _tmp_valid_85;
  reg [1-1:0] _tmp_data_88;
  reg _tmp_valid_88;
  wire _tmp_ready_88;
  assign _tmp_ready_86 = (_tmp_ready_88 || !_tmp_valid_88) && _tmp_valid_86;
  reg [1-1:0] _tmp_data_89;
  reg _tmp_valid_89;
  wire _tmp_ready_89;
  assign _tmp_ready_87 = (_tmp_ready_89 || !_tmp_valid_89) && _tmp_valid_87;
  reg [1-1:0] _tmp_data_90;
  reg _tmp_valid_90;
  wire _tmp_ready_90;
  assign _tmp_ready_88 = (_tmp_ready_90 || !_tmp_valid_90) && _tmp_valid_88;
  reg [1-1:0] _tmp_data_91;
  reg _tmp_valid_91;
  wire _tmp_ready_91;
  assign _tmp_ready_89 = (_tmp_ready_91 || !_tmp_valid_91) && _tmp_valid_89;
  reg [1-1:0] _tmp_data_92;
  reg _tmp_valid_92;
  wire _tmp_ready_92;
  assign _tmp_ready_90 = (_tmp_ready_92 || !_tmp_valid_92) && _tmp_valid_90;
  reg [1-1:0] _tmp_data_93;
  reg _tmp_valid_93;
  wire _tmp_ready_93;
  assign _tmp_ready_91 = (_tmp_ready_93 || !_tmp_valid_93) && _tmp_valid_91;
  reg [1-1:0] _tmp_data_94;
  reg _tmp_valid_94;
  wire _tmp_ready_94;
  assign _tmp_ready_92 = (_tmp_ready_94 || !_tmp_valid_94) && _tmp_valid_92;
  reg [1-1:0] _tmp_data_95;
  reg _tmp_valid_95;
  wire _tmp_ready_95;
  assign _tmp_ready_93 = (_tmp_ready_95 || !_tmp_valid_95) && _tmp_valid_93;
  reg [1-1:0] _tmp_data_96;
  reg _tmp_valid_96;
  wire _tmp_ready_96;
  assign _tmp_ready_94 = (_tmp_ready_96 || !_tmp_valid_96) && _tmp_valid_94;
  reg [32-1:0] _tmp_data_97;
  reg _tmp_valid_97;
  wire _tmp_ready_97;
  assign _tmp_ready_81 = (_tmp_ready_97 || !_tmp_valid_97) && (_tmp_valid_81 && _tmp_valid_95);
  assign _tmp_ready_95 = (_tmp_ready_97 || !_tmp_valid_97) && (_tmp_valid_81 && _tmp_valid_95);
  reg [1-1:0] _tmp_data_98;
  reg _tmp_valid_98;
  wire _tmp_ready_98;
  assign _tmp_ready_96 = (_tmp_ready_98 || !_tmp_valid_98) && _tmp_valid_96;
  assign _tmp_data_47 = _tmp_data_97;
  assign _tmp_valid_47 = _tmp_valid_97;
  assign _tmp_ready_97 = _tmp_ready_47;
  assign _tmp_data_48 = _tmp_data_98;
  assign _tmp_valid_48 = _tmp_valid_98;
  assign _tmp_ready_98 = _tmp_ready_48;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_80 <= 1'sd0;
      _tmp_valid_80 <= 0;
      _tmp_data_reg_81 <= 0;
      _tmp_valid_reg_81 <= 0;
      _tmp_data_82 <= 0;
      _tmp_valid_82 <= 0;
      _tmp_data_83 <= 0;
      _tmp_data_84 <= 0;
      _tmp_data_85 <= 0;
      _tmp_valid_85 <= 0;
      _tmp_data_86 <= 0;
      _tmp_valid_86 <= 0;
      _tmp_data_87 <= 0;
      _tmp_valid_87 <= 0;
      _tmp_data_88 <= 0;
      _tmp_valid_88 <= 0;
      _tmp_data_89 <= 0;
      _tmp_valid_89 <= 0;
      _tmp_data_90 <= 0;
      _tmp_valid_90 <= 0;
      _tmp_data_91 <= 0;
      _tmp_valid_91 <= 0;
      _tmp_data_92 <= 0;
      _tmp_valid_92 <= 0;
      _tmp_data_93 <= 0;
      _tmp_valid_93 <= 0;
      _tmp_data_94 <= 0;
      _tmp_valid_94 <= 0;
      _tmp_data_95 <= 0;
      _tmp_valid_95 <= 0;
      _tmp_data_96 <= 0;
      _tmp_valid_96 <= 0;
      _tmp_data_97 <= 1'sd0;
      _tmp_valid_97 <= 0;
      _tmp_data_98 <= 0;
      _tmp_valid_98 <= 0;
    end else begin
      if((_tmp_ready_80 || !_tmp_valid_80) && 1 && 1) begin
        _tmp_data_80 <= (_tmp_data_80 >= _th_matmul_matrix_size_5 - 1)? 0 : _tmp_data_80 + 2'sd1;
      end 
      if(_tmp_valid_80 && _tmp_ready_80) begin
        _tmp_valid_80 <= 0;
      end 
      if((_tmp_ready_80 || !_tmp_valid_80) && 1) begin
        _tmp_valid_80 <= 1;
      end 
      if(_tmp_ready_81 || !_tmp_valid_81) begin
        _tmp_data_reg_81 <= _tmp_odata_81;
      end 
      if(_tmp_ready_81 || !_tmp_valid_81) begin
        _tmp_valid_reg_81 <= _tmp_ovalid_81;
      end 
      if((_tmp_ready_82 || !_tmp_valid_82) && _tmp_ready_80 && _tmp_valid_80) begin
        _tmp_data_82 <= _tmp_data_80 == _th_matmul_matrix_size_5 - 1;
      end 
      if(_tmp_valid_82 && _tmp_ready_82) begin
        _tmp_valid_82 <= 0;
      end 
      if((_tmp_ready_82 || !_tmp_valid_82) && _tmp_ready_80) begin
        _tmp_valid_82 <= _tmp_valid_80;
      end 
      if(_tmp_valid_82 && _tmp_ready_82) begin
        _tmp_data_83 <= _tmp_data_82;
      end 
      if(_tmp_valid_82 && _tmp_ready_82) begin
        _tmp_data_84 <= _tmp_data_83;
      end 
      if((_tmp_ready_85 || !_tmp_valid_85) && _tmp_ready_82 && _tmp_valid_82) begin
        _tmp_data_85 <= _tmp_data_84;
      end 
      if(_tmp_valid_85 && _tmp_ready_85) begin
        _tmp_valid_85 <= 0;
      end 
      if((_tmp_ready_85 || !_tmp_valid_85) && _tmp_ready_82) begin
        _tmp_valid_85 <= _tmp_valid_82;
      end 
      if((_tmp_ready_86 || !_tmp_valid_86) && _tmp_ready_82 && _tmp_valid_82) begin
        _tmp_data_86 <= _tmp_data_83;
      end 
      if(_tmp_valid_86 && _tmp_ready_86) begin
        _tmp_valid_86 <= 0;
      end 
      if((_tmp_ready_86 || !_tmp_valid_86) && _tmp_ready_82) begin
        _tmp_valid_86 <= _tmp_valid_82;
      end 
      if((_tmp_ready_87 || !_tmp_valid_87) && _tmp_ready_85 && _tmp_valid_85) begin
        _tmp_data_87 <= _tmp_data_85;
      end 
      if(_tmp_valid_87 && _tmp_ready_87) begin
        _tmp_valid_87 <= 0;
      end 
      if((_tmp_ready_87 || !_tmp_valid_87) && _tmp_ready_85) begin
        _tmp_valid_87 <= _tmp_valid_85;
      end 
      if((_tmp_ready_88 || !_tmp_valid_88) && _tmp_ready_86 && _tmp_valid_86) begin
        _tmp_data_88 <= _tmp_data_86;
      end 
      if(_tmp_valid_88 && _tmp_ready_88) begin
        _tmp_valid_88 <= 0;
      end 
      if((_tmp_ready_88 || !_tmp_valid_88) && _tmp_ready_86) begin
        _tmp_valid_88 <= _tmp_valid_86;
      end 
      if((_tmp_ready_89 || !_tmp_valid_89) && _tmp_ready_87 && _tmp_valid_87) begin
        _tmp_data_89 <= _tmp_data_87;
      end 
      if(_tmp_valid_89 && _tmp_ready_89) begin
        _tmp_valid_89 <= 0;
      end 
      if((_tmp_ready_89 || !_tmp_valid_89) && _tmp_ready_87) begin
        _tmp_valid_89 <= _tmp_valid_87;
      end 
      if((_tmp_ready_90 || !_tmp_valid_90) && _tmp_ready_88 && _tmp_valid_88) begin
        _tmp_data_90 <= _tmp_data_88;
      end 
      if(_tmp_valid_90 && _tmp_ready_90) begin
        _tmp_valid_90 <= 0;
      end 
      if((_tmp_ready_90 || !_tmp_valid_90) && _tmp_ready_88) begin
        _tmp_valid_90 <= _tmp_valid_88;
      end 
      if((_tmp_ready_91 || !_tmp_valid_91) && _tmp_ready_89 && _tmp_valid_89) begin
        _tmp_data_91 <= _tmp_data_89;
      end 
      if(_tmp_valid_91 && _tmp_ready_91) begin
        _tmp_valid_91 <= 0;
      end 
      if((_tmp_ready_91 || !_tmp_valid_91) && _tmp_ready_89) begin
        _tmp_valid_91 <= _tmp_valid_89;
      end 
      if((_tmp_ready_92 || !_tmp_valid_92) && _tmp_ready_90 && _tmp_valid_90) begin
        _tmp_data_92 <= _tmp_data_90;
      end 
      if(_tmp_valid_92 && _tmp_ready_92) begin
        _tmp_valid_92 <= 0;
      end 
      if((_tmp_ready_92 || !_tmp_valid_92) && _tmp_ready_90) begin
        _tmp_valid_92 <= _tmp_valid_90;
      end 
      if((_tmp_ready_93 || !_tmp_valid_93) && _tmp_ready_91 && _tmp_valid_91) begin
        _tmp_data_93 <= _tmp_data_91;
      end 
      if(_tmp_valid_93 && _tmp_ready_93) begin
        _tmp_valid_93 <= 0;
      end 
      if((_tmp_ready_93 || !_tmp_valid_93) && _tmp_ready_91) begin
        _tmp_valid_93 <= _tmp_valid_91;
      end 
      if((_tmp_ready_94 || !_tmp_valid_94) && _tmp_ready_92 && _tmp_valid_92) begin
        _tmp_data_94 <= _tmp_data_92;
      end 
      if(_tmp_valid_94 && _tmp_ready_94) begin
        _tmp_valid_94 <= 0;
      end 
      if((_tmp_ready_94 || !_tmp_valid_94) && _tmp_ready_92) begin
        _tmp_valid_94 <= _tmp_valid_92;
      end 
      if((_tmp_ready_95 || !_tmp_valid_95) && _tmp_ready_93 && _tmp_valid_93) begin
        _tmp_data_95 <= _tmp_data_93;
      end 
      if(_tmp_valid_95 && _tmp_ready_95) begin
        _tmp_valid_95 <= 0;
      end 
      if((_tmp_ready_95 || !_tmp_valid_95) && _tmp_ready_93) begin
        _tmp_valid_95 <= _tmp_valid_93;
      end 
      if((_tmp_ready_96 || !_tmp_valid_96) && _tmp_ready_94 && _tmp_valid_94) begin
        _tmp_data_96 <= _tmp_data_94;
      end 
      if(_tmp_valid_96 && _tmp_ready_96) begin
        _tmp_valid_96 <= 0;
      end 
      if((_tmp_ready_96 || !_tmp_valid_96) && _tmp_ready_94) begin
        _tmp_valid_96 <= _tmp_valid_94;
      end 
      if((_tmp_ready_97 || !_tmp_valid_97) && (_tmp_ready_81 && _tmp_ready_95) && (_tmp_valid_81 && _tmp_valid_95)) begin
        _tmp_data_97 <= _tmp_data_97 + _tmp_data_81;
      end 
      if(_tmp_valid_97 && _tmp_ready_97) begin
        _tmp_valid_97 <= 0;
      end 
      if((_tmp_ready_97 || !_tmp_valid_97) && (_tmp_ready_81 && _tmp_ready_95)) begin
        _tmp_valid_97 <= _tmp_valid_81 && _tmp_valid_95;
      end 
      if((_tmp_ready_97 || !_tmp_valid_97) && (_tmp_ready_81 && _tmp_ready_95) && (_tmp_valid_81 && _tmp_valid_95) && _tmp_data_95) begin
        _tmp_data_97 <= 1'sd0 + _tmp_data_81;
      end 
      if((_tmp_ready_98 || !_tmp_valid_98) && _tmp_ready_96 && _tmp_valid_96) begin
        _tmp_data_98 <= _tmp_data_96;
      end 
      if(_tmp_valid_98 && _tmp_ready_98) begin
        _tmp_valid_98 <= 0;
      end 
      if((_tmp_ready_98 || !_tmp_valid_98) && _tmp_ready_96) begin
        _tmp_valid_98 <= _tmp_valid_96;
      end 
    end
  end

  localparam th_matmul_1 = 1;
  localparam th_matmul_2 = 2;
  localparam th_matmul_3 = 3;
  localparam th_matmul_4 = 4;
  localparam th_matmul_5 = 5;
  localparam th_matmul_6 = 6;
  localparam th_matmul_7 = 7;
  localparam th_matmul_8 = 8;
  localparam th_matmul_9 = 9;
  localparam th_matmul_10 = 10;
  localparam th_matmul_11 = 11;
  localparam th_matmul_12 = 12;
  localparam th_matmul_13 = 13;
  localparam th_matmul_14 = 14;
  localparam th_matmul_15 = 15;
  localparam th_matmul_16 = 16;
  localparam th_matmul_17 = 17;
  localparam th_matmul_18 = 18;
  localparam th_matmul_19 = 19;
  localparam th_matmul_20 = 20;
  localparam th_matmul_21 = 21;
  localparam th_matmul_22 = 22;
  localparam th_matmul_23 = 23;
  localparam th_matmul_24 = 24;
  localparam th_matmul_25 = 25;
  localparam th_matmul_26 = 26;
  localparam th_matmul_27 = 27;
  localparam th_matmul_28 = 28;
  localparam th_matmul_29 = 29;
  localparam th_matmul_30 = 30;
  localparam th_matmul_31 = 31;
  localparam th_matmul_32 = 32;
  localparam th_matmul_33 = 33;
  localparam th_matmul_34 = 34;
  localparam th_matmul_35 = 35;
  localparam th_matmul_36 = 36;
  localparam th_matmul_37 = 37;
  localparam th_matmul_38 = 38;
  localparam th_matmul_39 = 39;
  localparam th_matmul_40 = 40;
  localparam th_matmul_41 = 41;
  localparam th_matmul_42 = 42;
  localparam th_matmul_43 = 43;
  localparam th_matmul_44 = 44;
  localparam th_matmul_45 = 45;
  localparam th_matmul_46 = 46;
  localparam th_matmul_47 = 47;
  localparam th_matmul_48 = 48;
  localparam th_matmul_49 = 49;
  localparam th_matmul_50 = 50;
  localparam th_matmul_51 = 51;
  localparam th_matmul_52 = 52;
  localparam th_matmul_53 = 53;

  always @(posedge CLK) begin
    if(RST) begin
      th_matmul <= th_matmul_init;
      _th_matmul_matrix_size_0 <= 0;
      _th_matmul_a_offset_1 <= 0;
      _th_matmul_b_offset_2 <= 0;
      _th_matmul_c_offset_3 <= 0;
      _th_matmul_start_time_4 <= 0;
      _th_matmul_matrix_size_5 <= 0;
      _th_matmul_a_offset_6 <= 0;
      _th_matmul_b_offset_7 <= 0;
      _th_matmul_c_offset_8 <= 0;
      _th_matmul_a_addr_9 <= 0;
      _th_matmul_c_addr_10 <= 0;
      _th_matmul_i_11 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_3 <= 0;
      _tmp_2 <= 0;
      _th_matmul_b_addr_12 <= 0;
      _th_matmul_j_13 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_13 <= 0;
      _tmp_12 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_52 <= 0;
      _tmp_51 <= 0;
      _th_matmul_end_time_20 <= 0;
      _th_matmul_time_21 <= 0;
      _th_matmul_matrix_size_22 <= 0;
      _th_matmul_a_offset_23 <= 0;
      _th_matmul_b_offset_24 <= 0;
      _th_matmul_c_offset_25 <= 0;
      _th_matmul_all_ok_26 <= 0;
      _th_matmul_c_addr_27 <= 0;
      _th_matmul_i_28 <= 0;
      _tmp_68 <= 0;
      _tmp_69 <= 0;
      _tmp_71 <= 0;
      _tmp_70 <= 0;
      _th_matmul_j_29 <= 0;
      _tmp_79 <= 0;
      _th_matmul_v_30 <= 0;
    end else begin
      case(th_matmul)
        th_matmul_init: begin
          _th_matmul_matrix_size_0 <= 16;
          _th_matmul_a_offset_1 <= 0;
          _th_matmul_b_offset_2 <= 1024;
          _th_matmul_c_offset_3 <= 2048;
          th_matmul <= th_matmul_1;
        end
        th_matmul_1: begin
          _th_matmul_start_time_4 <= timer;
          th_matmul <= th_matmul_2;
        end
        th_matmul_2: begin
          _th_matmul_matrix_size_5 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_6 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_7 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_8 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_3;
        end
        th_matmul_3: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_offset_6;
          _th_matmul_c_addr_10 <= _th_matmul_c_offset_8;
          th_matmul <= th_matmul_4;
        end
        th_matmul_4: begin
          _th_matmul_i_11 <= 0;
          th_matmul <= th_matmul_5;
        end
        th_matmul_5: begin
          if(_th_matmul_i_11 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_6;
          end else begin
            th_matmul <= th_matmul_25;
          end
        end
        th_matmul_6: begin
          _tmp_0 <= 0;
          _tmp_1 <= _th_matmul_a_addr_9;
          _tmp_3 <= _th_matmul_matrix_size_5;
          th_matmul <= th_matmul_7;
        end
        th_matmul_7: begin
          if(_tmp_3 <= 256) begin
            _tmp_2 <= _tmp_3;
            _tmp_3 <= 0;
          end else begin
            _tmp_2 <= 256;
            _tmp_3 <= _tmp_3 - 256;
          end
          th_matmul <= th_matmul_8;
        end
        th_matmul_8: begin
          if(_tmp_8) begin
            _tmp_0 <= _tmp_0 + _tmp_2;
            _tmp_1 <= _tmp_1 + (_tmp_2 << 2);
          end 
          if(_tmp_8 && (_tmp_3 > 0)) begin
            th_matmul <= th_matmul_7;
          end 
          if(_tmp_8 && (_tmp_3 == 0)) begin
            th_matmul <= th_matmul_9;
          end 
        end
        th_matmul_9: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_offset_7;
          th_matmul <= th_matmul_10;
        end
        th_matmul_10: begin
          _th_matmul_j_13 <= 0;
          th_matmul <= th_matmul_11;
        end
        th_matmul_11: begin
          if(_th_matmul_j_13 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_12;
          end else begin
            th_matmul <= th_matmul_19;
          end
        end
        th_matmul_12: begin
          _tmp_10 <= 0;
          _tmp_11 <= _th_matmul_b_addr_12;
          _tmp_13 <= _th_matmul_matrix_size_5;
          th_matmul <= th_matmul_13;
        end
        th_matmul_13: begin
          if(_tmp_13 <= 256) begin
            _tmp_12 <= _tmp_13;
            _tmp_13 <= 0;
          end else begin
            _tmp_12 <= 256;
            _tmp_13 <= _tmp_13 - 256;
          end
          th_matmul <= th_matmul_14;
        end
        th_matmul_14: begin
          if(_tmp_18) begin
            _tmp_10 <= _tmp_10 + _tmp_12;
            _tmp_11 <= _tmp_11 + (_tmp_12 << 2);
          end 
          if(_tmp_18 && (_tmp_13 > 0)) begin
            th_matmul <= th_matmul_13;
          end 
          if(_tmp_18 && (_tmp_13 == 0)) begin
            th_matmul <= th_matmul_15;
          end 
        end
        th_matmul_15: begin
          th_matmul <= th_matmul_16;
        end
        th_matmul_16: begin
          if(_strm_madd_flag_14 && _strm_madd_flag_16 && _strm_madd_flag_18) begin
            th_matmul <= th_matmul_17;
          end 
        end
        th_matmul_17: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_addr_12 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_18;
        end
        th_matmul_18: begin
          _th_matmul_j_13 <= _th_matmul_j_13 + 1;
          th_matmul <= th_matmul_11;
        end
        th_matmul_19: begin
          _tmp_49 <= 0;
          _tmp_50 <= _th_matmul_c_addr_10;
          _tmp_52 <= _th_matmul_matrix_size_5;
          th_matmul <= th_matmul_20;
        end
        th_matmul_20: begin
          if(_tmp_52 <= 256) begin
            _tmp_51 <= _tmp_52;
            _tmp_52 <= 0;
          end else begin
            _tmp_51 <= 256;
            _tmp_52 <= _tmp_52 - 256;
          end
          th_matmul <= th_matmul_21;
        end
        th_matmul_21: begin
          if(_tmp_66) begin
            _tmp_49 <= _tmp_49 + _tmp_51;
            _tmp_50 <= _tmp_50 + (_tmp_51 << 2);
          end 
          if(_tmp_66 && (_tmp_52 > 0)) begin
            th_matmul <= th_matmul_20;
          end 
          if(_tmp_66 && (_tmp_52 == 0)) begin
            th_matmul <= th_matmul_22;
          end 
        end
        th_matmul_22: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_addr_9 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_23;
        end
        th_matmul_23: begin
          _th_matmul_c_addr_10 <= _th_matmul_c_addr_10 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_24;
        end
        th_matmul_24: begin
          _th_matmul_i_11 <= _th_matmul_i_11 + 1;
          th_matmul <= th_matmul_5;
        end
        th_matmul_25: begin
          _th_matmul_end_time_20 <= timer;
          th_matmul <= th_matmul_26;
        end
        th_matmul_26: begin
          _th_matmul_time_21 <= _th_matmul_end_time_20 - _th_matmul_start_time_4;
          th_matmul <= th_matmul_27;
        end
        th_matmul_27: begin
          $display("Time (cycles): %d", _th_matmul_time_21);
          th_matmul <= th_matmul_28;
        end
        th_matmul_28: begin
          _th_matmul_matrix_size_22 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_23 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_24 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_25 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_29;
        end
        th_matmul_29: begin
          _th_matmul_all_ok_26 <= 1;
          th_matmul <= th_matmul_30;
        end
        th_matmul_30: begin
          _th_matmul_c_addr_27 <= _th_matmul_c_offset_25;
          th_matmul <= th_matmul_31;
        end
        th_matmul_31: begin
          _th_matmul_i_28 <= 0;
          th_matmul <= th_matmul_32;
        end
        th_matmul_32: begin
          if(_th_matmul_i_28 < _th_matmul_matrix_size_22) begin
            th_matmul <= th_matmul_33;
          end else begin
            th_matmul <= th_matmul_49;
          end
        end
        th_matmul_33: begin
          _tmp_68 <= 0;
          _tmp_69 <= _th_matmul_c_addr_27;
          _tmp_71 <= _th_matmul_matrix_size_22;
          th_matmul <= th_matmul_34;
        end
        th_matmul_34: begin
          if(_tmp_71 <= 256) begin
            _tmp_70 <= _tmp_71;
            _tmp_71 <= 0;
          end else begin
            _tmp_70 <= 256;
            _tmp_71 <= _tmp_71 - 256;
          end
          th_matmul <= th_matmul_35;
        end
        th_matmul_35: begin
          if(_tmp_76) begin
            _tmp_68 <= _tmp_68 + _tmp_70;
            _tmp_69 <= _tmp_69 + (_tmp_70 << 2);
          end 
          if(_tmp_76 && (_tmp_71 > 0)) begin
            th_matmul <= th_matmul_34;
          end 
          if(_tmp_76 && (_tmp_71 == 0)) begin
            th_matmul <= th_matmul_36;
          end 
        end
        th_matmul_36: begin
          _th_matmul_j_29 <= 0;
          th_matmul <= th_matmul_37;
        end
        th_matmul_37: begin
          if(_th_matmul_j_29 < _th_matmul_matrix_size_22) begin
            th_matmul <= th_matmul_38;
          end else begin
            th_matmul <= th_matmul_47;
          end
        end
        th_matmul_38: begin
          if(_tmp_78) begin
            _tmp_79 <= ram_c_0_rdata;
          end 
          if(_tmp_78) begin
            th_matmul <= th_matmul_39;
          end 
        end
        th_matmul_39: begin
          _th_matmul_v_30 <= _tmp_79;
          th_matmul <= th_matmul_40;
        end
        th_matmul_40: begin
          if((_th_matmul_i_28 == _th_matmul_j_29) && (_th_matmul_v_30 != (_th_matmul_i_28 + 1 << 1))) begin
            th_matmul <= th_matmul_41;
          end else begin
            th_matmul <= th_matmul_43;
          end
        end
        th_matmul_41: begin
          _th_matmul_all_ok_26 <= 0;
          th_matmul <= th_matmul_42;
        end
        th_matmul_42: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_28, _th_matmul_j_29, _th_matmul_v_30);
          th_matmul <= th_matmul_43;
        end
        th_matmul_43: begin
          if((_th_matmul_i_28 != _th_matmul_j_29) && (_th_matmul_v_30 != 0)) begin
            th_matmul <= th_matmul_44;
          end else begin
            th_matmul <= th_matmul_46;
          end
        end
        th_matmul_44: begin
          _th_matmul_all_ok_26 <= 0;
          th_matmul <= th_matmul_45;
        end
        th_matmul_45: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_28, _th_matmul_j_29, _th_matmul_v_30);
          th_matmul <= th_matmul_46;
        end
        th_matmul_46: begin
          _th_matmul_j_29 <= _th_matmul_j_29 + 1;
          th_matmul <= th_matmul_37;
        end
        th_matmul_47: begin
          _th_matmul_c_addr_27 <= _th_matmul_c_addr_27 + (_th_matmul_matrix_size_22 << 2);
          th_matmul <= th_matmul_48;
        end
        th_matmul_48: begin
          _th_matmul_i_28 <= _th_matmul_i_28 + 1;
          th_matmul <= th_matmul_32;
        end
        th_matmul_49: begin
          if(_th_matmul_all_ok_26) begin
            th_matmul <= th_matmul_50;
          end else begin
            th_matmul <= th_matmul_52;
          end
        end
        th_matmul_50: begin
          $display("OK");
          th_matmul <= th_matmul_51;
        end
        th_matmul_51: begin
          th_matmul <= th_matmul_53;
        end
        th_matmul_52: begin
          $display("NG");
          th_matmul <= th_matmul_53;
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
      _tmp_6 <= 0;
      _tmp_5 <= 0;
    end else begin
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_matmul == 8) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
        end
        _tmp_fsm_0_2: begin
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          _tmp_6 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_5 <= myaxi_rdata;
            _tmp_6 <= 1;
          end 
          if(_tmp_8) begin
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
      _tmp_16 <= 0;
      _tmp_15 <= 0;
    end else begin
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_matmul == 14) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
        end
        _tmp_fsm_1_2: begin
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          _tmp_16 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_15 <= myaxi_rdata;
            _tmp_16 <= 1;
          end 
          if(_tmp_18) begin
            _tmp_fsm_1 <= _tmp_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _strm_madd_fsm_15_1 = 1;
  localparam _strm_madd_fsm_15_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_fsm_15 <= _strm_madd_fsm_15_init;
      _strm_madd_flag_14 <= 0;
    end else begin
      case(_strm_madd_fsm_15)
        _strm_madd_fsm_15_init: begin
          if(th_matmul == 15) begin
            _strm_madd_flag_14 <= 0;
          end 
          if(th_matmul == 15) begin
            _strm_madd_fsm_15 <= _strm_madd_fsm_15_1;
          end 
        end
        _strm_madd_fsm_15_1: begin
          _strm_madd_fsm_15 <= _strm_madd_fsm_15_2;
        end
        _strm_madd_fsm_15_2: begin
          if(_tmp_31) begin
            _strm_madd_flag_14 <= 1;
          end 
          if(_tmp_31) begin
            _strm_madd_fsm_15 <= _strm_madd_fsm_15_init;
          end 
        end
      endcase
    end
  end

  localparam _strm_madd_fsm_17_1 = 1;
  localparam _strm_madd_fsm_17_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_fsm_17 <= _strm_madd_fsm_17_init;
      _strm_madd_flag_16 <= 0;
    end else begin
      case(_strm_madd_fsm_17)
        _strm_madd_fsm_17_init: begin
          if(th_matmul == 15) begin
            _strm_madd_flag_16 <= 0;
          end 
          if(th_matmul == 15) begin
            _strm_madd_fsm_17 <= _strm_madd_fsm_17_1;
          end 
        end
        _strm_madd_fsm_17_1: begin
          _strm_madd_fsm_17 <= _strm_madd_fsm_17_2;
        end
        _strm_madd_fsm_17_2: begin
          if(_tmp_43) begin
            _strm_madd_flag_16 <= 1;
          end 
          if(_tmp_43) begin
            _strm_madd_fsm_17 <= _strm_madd_fsm_17_init;
          end 
        end
      endcase
    end
  end

  localparam _strm_madd_fsm_19_1 = 1;
  localparam _strm_madd_fsm_19_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_fsm_19 <= _strm_madd_fsm_19_init;
      _strm_madd_flag_18 <= 0;
    end else begin
      case(_strm_madd_fsm_19)
        _strm_madd_fsm_19_init: begin
          if(th_matmul == 15) begin
            _strm_madd_flag_18 <= 0;
          end 
          if(th_matmul == 15) begin
            _strm_madd_fsm_19 <= _strm_madd_fsm_19_1;
          end 
        end
        _strm_madd_fsm_19_1: begin
          _strm_madd_fsm_19 <= _strm_madd_fsm_19_2;
        end
        _strm_madd_fsm_19_2: begin
          if(_tmp_45) begin
            _strm_madd_flag_18 <= 1;
          end 
          if(_tmp_45) begin
            _strm_madd_fsm_19 <= _strm_madd_fsm_19_init;
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
          if(th_matmul == 21) begin
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
          if(_tmp_66) begin
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
      _tmp_74 <= 0;
      _tmp_73 <= 0;
    end else begin
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_matmul == 35) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
        end
        _tmp_fsm_3_2: begin
          _tmp_fsm_3 <= _tmp_fsm_3_3;
        end
        _tmp_fsm_3_3: begin
          _tmp_74 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_73 <= myaxi_rdata;
            _tmp_74 <= 1;
          end 
          if(_tmp_76) begin
            _tmp_fsm_3 <= _tmp_fsm_3_init;
          end 
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
    test_module = thread_stream_matmul.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
