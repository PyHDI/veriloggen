from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_transpose

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
  reg _mystream_flag_1;
  wire [10-1:0] _mystream_req_addr_2;
  reg [10-1:0] _mystream_offset_0_3;
  reg [10-1:0] _mystream_offset_1_4;
  assign _mystream_req_addr_2 = _mystream_offset_1_4 + (_mystream_offset_0_3 + _th_comp_offset_0);
  reg [32-1:0] _mystream_fsm_5;
  localparam _mystream_fsm_5_init = 0;
  reg [3-1:0] _mystream_count_0_6;
  reg [4-1:0] _mystream_count_1_7;
  reg _tmp_10;
  reg _tmp_11;
  wire _tmp_12;
  wire _tmp_13;
  assign _tmp_13 = 1;
  localparam _tmp_14 = 1;
  wire [_tmp_14-1:0] _tmp_15;
  assign _tmp_15 = (_tmp_12 || !_tmp_10) && (_tmp_13 || !_tmp_11);
  reg [_tmp_14-1:0] __tmp_15_1;
  wire [32-1:0] _tmp_16;
  reg [32-1:0] __tmp_16_1;
  assign _tmp_16 = (__tmp_15_1)? ram_a_0_rdata : __tmp_16_1;
  reg [5-1:0] _tmp_17;
  reg _tmp_18;
  reg _tmp_19;
  reg _tmp_20;
  reg _tmp_21;
  reg _mystream_flag_8;
  wire [10-1:0] _mystream_req_addr_9;
  reg [10-1:0] _mystream_offset_0_10;
  reg [10-1:0] _mystream_offset_1_11;
  assign _mystream_req_addr_9 = _mystream_offset_1_11 + (_mystream_offset_0_10 + _th_comp_offset_0);
  reg [32-1:0] _mystream_fsm_12;
  localparam _mystream_fsm_12_init = 0;
  reg [3-1:0] _mystream_count_0_13;
  reg [5-1:0] _mystream_count_1_14;
  reg [4-1:0] _tmp_22;
  reg _tmp_23;
  wire [32-1:0] _tmp_data_24;
  wire _tmp_valid_24;
  wire _tmp_ready_24;
  assign _tmp_ready_24 = (_tmp_22 > 0) && !_tmp_23;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_25;
  reg [32-1:0] _tmp_26;
  reg [32-1:0] _tmp_27;
  reg [32-1:0] _tmp_28;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [9-1:0] _tmp_29;
  reg _myaxi_cond_1_1;
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
  assign _tmp_36 = (__tmp_35_1)? ram_c_0_rdata : __tmp_36_1;
  reg [33-1:0] _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  reg _tmp_40;
  reg _tmp_41;
  reg _tmp_42;
  wire [32-1:0] _tmp_data_43;
  wire _tmp_valid_43;
  wire _tmp_ready_43;
  assign _tmp_ready_43 = (_tmp_fsm_1 == 3) && ((_tmp_29 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  reg [10-1:0] _tmp_44;
  reg [32-1:0] _tmp_45;
  reg [32-1:0] _tmp_46;
  reg [32-1:0] _tmp_47;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [9-1:0] _tmp_48;
  reg _myaxi_cond_3_1;
  reg [32-1:0] _tmp_49;
  reg _tmp_50;
  reg [33-1:0] _tmp_51;
  reg _tmp_52;
  wire [32-1:0] _tmp_data_53;
  wire _tmp_valid_53;
  wire _tmp_ready_53;
  assign _tmp_ready_53 = (_tmp_51 > 0) && !_tmp_52;
  reg _ram_a_cond_1_1;
  assign myaxi_rready = (_tmp_fsm_0 == 3) || (_tmp_fsm_2 == 3);
  reg [32-1:0] th_sequential;
  localparam th_sequential_init = 0;
  reg _th_sequential_called;
  reg signed [32-1:0] _th_sequential_offset_15;
  reg signed [32-1:0] _th_sequential_offset_16;
  reg signed [32-1:0] _th_sequential_zpos_17;
  reg signed [32-1:0] _th_sequential_ypos_18;
  reg signed [32-1:0] _th_sequential_xpos_19;
  reg signed [32-1:0] _th_sequential_x_20;
  reg signed [32-1:0] _th_sequential_y_21;
  reg signed [32-1:0] _th_sequential_z_22;
  reg _tmp_54;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_3_2;
  reg signed [32-1:0] _tmp_55;
  reg signed [32-1:0] _th_sequential_a_23;
  reg _ram_c_cond_1_1;
  reg [10-1:0] _tmp_56;
  reg [32-1:0] _tmp_57;
  reg [32-1:0] _tmp_58;
  reg [32-1:0] _tmp_59;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [9-1:0] _tmp_60;
  reg _myaxi_cond_4_1;
  reg _tmp_61;
  reg _tmp_62;
  wire _tmp_63;
  wire _tmp_64;
  assign _tmp_64 = 1;
  localparam _tmp_65 = 1;
  wire [_tmp_65-1:0] _tmp_66;
  assign _tmp_66 = (_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62);
  reg [_tmp_65-1:0] __tmp_66_1;
  wire [32-1:0] _tmp_67;
  reg [32-1:0] __tmp_67_1;
  assign _tmp_67 = (__tmp_66_1)? ram_c_0_rdata : __tmp_67_1;
  reg [33-1:0] _tmp_68;
  reg _tmp_69;
  reg _tmp_70;
  reg _tmp_71;
  reg _tmp_72;
  reg _tmp_73;
  wire [32-1:0] _tmp_data_74;
  wire _tmp_valid_74;
  wire _tmp_ready_74;
  assign _tmp_ready_74 = (_tmp_fsm_3 == 3) && ((_tmp_60 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_5_1;
  reg signed [32-1:0] _th_comp_offset_stream_24;
  reg signed [32-1:0] _th_comp_offset_seq_25;
  reg signed [32-1:0] _th_comp_all_ok_26;
  reg signed [32-1:0] _th_comp_i_27;
  reg _tmp_75;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_76;
  reg signed [32-1:0] _th_comp_st_28;
  reg _tmp_77;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_78;
  reg signed [32-1:0] _th_comp_sq_29;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_4 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_29 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_42 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_48 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_60 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_73 <= 0;
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
        _tmp_42 <= 0;
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
        _tmp_73 <= 0;
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
      if((_tmp_fsm_1 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_29 == 0))) begin
        myaxi_awaddr <= _tmp_26;
        myaxi_awlen <= _tmp_27 - 1;
        myaxi_awvalid <= 1;
        _tmp_29 <= _tmp_27;
      end 
      if((_tmp_fsm_1 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_29 == 0)) && (_tmp_27 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_43 && ((_tmp_fsm_1 == 3) && ((_tmp_29 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_29 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_29 > 0))) begin
        myaxi_wdata <= _tmp_data_43;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_29 <= _tmp_29 - 1;
      end 
      if(_tmp_valid_43 && ((_tmp_fsm_1 == 3) && ((_tmp_29 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_29 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_29 > 0)) && (_tmp_29 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_42 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_42 <= _tmp_42;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_48 == 0))) begin
        myaxi_araddr <= _tmp_45;
        myaxi_arlen <= _tmp_46 - 1;
        myaxi_arvalid <= 1;
        _tmp_48 <= _tmp_46;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_48 > 0)) begin
        _tmp_48 <= _tmp_48 - 1;
      end 
      if((_tmp_fsm_3 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_60 == 0))) begin
        myaxi_awaddr <= _tmp_57;
        myaxi_awlen <= _tmp_58 - 1;
        myaxi_awvalid <= 1;
        _tmp_60 <= _tmp_58;
      end 
      if((_tmp_fsm_3 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_60 == 0)) && (_tmp_58 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_74 && ((_tmp_fsm_3 == 3) && ((_tmp_60 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_60 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_60 > 0))) begin
        myaxi_wdata <= _tmp_data_74;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_60 <= _tmp_60 - 1;
      end 
      if(_tmp_valid_74 && ((_tmp_fsm_3 == 3) && ((_tmp_60 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_60 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_60 > 0)) && (_tmp_60 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_73 <= 1;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_73 <= _tmp_73;
      end 
    end
  end

  assign _tmp_data_9 = _tmp_5;
  assign _tmp_valid_9 = _tmp_6;
  assign _tmp_data_53 = _tmp_49;
  assign _tmp_valid_53 = _tmp_50;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_7 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_8 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_15_1 <= 0;
      __tmp_16_1 <= 0;
      _tmp_21 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_19 <= 0;
      _tmp_20 <= 0;
      _tmp_18 <= 0;
      _tmp_17 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _ram_a_cond_1_1 <= 0;
      _ram_a_cond_2_1 <= 0;
      _tmp_54 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_3_2 <= 0;
    end else begin
      if(_ram_a_cond_3_2) begin
        _tmp_54 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_8 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        ram_a_0_wenable <= 0;
        _tmp_52 <= 0;
      end 
      if(_ram_a_cond_2_1) begin
        _tmp_54 <= 1;
      end 
      _ram_a_cond_3_2 <= _ram_a_cond_3_1;
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
      __tmp_15_1 <= _tmp_15;
      __tmp_16_1 <= _tmp_16;
      if((_tmp_12 || !_tmp_10) && (_tmp_13 || !_tmp_11) && _tmp_19) begin
        _tmp_21 <= 0;
        _tmp_10 <= 0;
        _tmp_11 <= 0;
        _tmp_19 <= 0;
      end 
      if((_tmp_12 || !_tmp_10) && (_tmp_13 || !_tmp_11) && _tmp_18) begin
        _tmp_10 <= 1;
        _tmp_11 <= 1;
        _tmp_21 <= _tmp_20;
        _tmp_20 <= 0;
        _tmp_18 <= 0;
        _tmp_19 <= 1;
      end 
      if((_mystream_fsm_5 == 1) && (_tmp_17 == 0) && !_tmp_20 && !_tmp_21) begin
        ram_a_0_addr <= _mystream_req_addr_2;
        _tmp_17 <= 7;
        _tmp_18 <= 1;
      end 
      if((_tmp_12 || !_tmp_10) && (_tmp_13 || !_tmp_11) && (_tmp_17 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 8;
        _tmp_17 <= _tmp_17 - 1;
        _tmp_18 <= 1;
        _tmp_20 <= 0;
      end 
      if((_tmp_12 || !_tmp_10) && (_tmp_13 || !_tmp_11) && (_tmp_17 == 1)) begin
        _tmp_20 <= 1;
      end 
      if((_tmp_fsm_2 == 2) && (_tmp_51 == 0)) begin
        ram_a_0_addr <= _tmp_44 - 1;
        _tmp_51 <= _tmp_46;
      end 
      if(_tmp_valid_53 && ((_tmp_51 > 0) && !_tmp_52) && (_tmp_51 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_53;
        ram_a_0_wenable <= 1;
        _tmp_51 <= _tmp_51 - 1;
      end 
      if(_tmp_valid_53 && ((_tmp_51 > 0) && !_tmp_52) && (_tmp_51 == 1)) begin
        _tmp_52 <= 1;
      end 
      _ram_a_cond_1_1 <= 1;
      if(th_sequential == 11) begin
        ram_a_0_addr <= ((_th_sequential_z_22 << 2) << 1) + (_th_sequential_y_21 << 2) + _th_sequential_x_20 + _th_sequential_offset_16;
      end 
      _ram_a_cond_2_1 <= th_sequential == 11;
      _ram_a_cond_3_1 <= th_sequential == 11;
    end
  end

  assign _tmp_data_24 = _tmp_16;
  assign _tmp_valid_24 = _tmp_10;
  assign _tmp_12 = 1 && _tmp_ready_24;

  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      _tmp_22 <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_23 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_35_1 <= 0;
      __tmp_36_1 <= 0;
      _tmp_41 <= 0;
      _tmp_30 <= 0;
      _tmp_31 <= 0;
      _tmp_39 <= 0;
      _tmp_40 <= 0;
      _tmp_38 <= 0;
      _tmp_37 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_66_1 <= 0;
      __tmp_67_1 <= 0;
      _tmp_72 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_69 <= 0;
      _tmp_68 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_75 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_77 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_75 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_77 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_23 <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_75 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_77 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if((_mystream_fsm_12 == 1) && (_tmp_22 == 0)) begin
        ram_c_0_addr <= _mystream_req_addr_9 - 1;
        _tmp_22 <= 4;
      end 
      if(_tmp_valid_24 && ((_tmp_22 > 0) && !_tmp_23) && (_tmp_22 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_24;
        ram_c_0_wenable <= 1;
        _tmp_22 <= _tmp_22 - 1;
      end 
      if(_tmp_valid_24 && ((_tmp_22 > 0) && !_tmp_23) && (_tmp_22 == 1)) begin
        _tmp_23 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_35_1 <= _tmp_35;
      __tmp_36_1 <= _tmp_36;
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_39) begin
        _tmp_41 <= 0;
        _tmp_30 <= 0;
        _tmp_31 <= 0;
        _tmp_39 <= 0;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && _tmp_38) begin
        _tmp_30 <= 1;
        _tmp_31 <= 1;
        _tmp_41 <= _tmp_40;
        _tmp_40 <= 0;
        _tmp_38 <= 0;
        _tmp_39 <= 1;
      end 
      if((_tmp_fsm_1 == 2) && (_tmp_37 == 0) && !_tmp_40 && !_tmp_41) begin
        ram_c_0_addr <= _tmp_25;
        _tmp_37 <= _tmp_27 - 1;
        _tmp_38 <= 1;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && (_tmp_37 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_37 <= _tmp_37 - 1;
        _tmp_38 <= 1;
        _tmp_40 <= 0;
      end 
      if((_tmp_32 || !_tmp_30) && (_tmp_33 || !_tmp_31) && (_tmp_37 == 1)) begin
        _tmp_40 <= 1;
      end 
      if(th_sequential == 13) begin
        ram_c_0_addr <= _th_sequential_zpos_17 + _th_sequential_ypos_18 + _th_sequential_xpos_19 + _th_sequential_offset_16;
        ram_c_0_wdata <= _th_sequential_a_23;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_sequential == 13;
      __tmp_66_1 <= _tmp_66;
      __tmp_67_1 <= _tmp_67;
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && _tmp_70) begin
        _tmp_72 <= 0;
        _tmp_61 <= 0;
        _tmp_62 <= 0;
        _tmp_70 <= 0;
      end 
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && _tmp_69) begin
        _tmp_61 <= 1;
        _tmp_62 <= 1;
        _tmp_72 <= _tmp_71;
        _tmp_71 <= 0;
        _tmp_69 <= 0;
        _tmp_70 <= 1;
      end 
      if((_tmp_fsm_3 == 2) && (_tmp_68 == 0) && !_tmp_71 && !_tmp_72) begin
        ram_c_0_addr <= _tmp_56;
        _tmp_68 <= _tmp_58 - 1;
        _tmp_69 <= 1;
      end 
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && (_tmp_68 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_68 <= _tmp_68 - 1;
        _tmp_69 <= 1;
        _tmp_71 <= 0;
      end 
      if((_tmp_63 || !_tmp_61) && (_tmp_64 || !_tmp_62) && (_tmp_68 == 1)) begin
        _tmp_71 <= 1;
      end 
      if(th_comp == 23) begin
        ram_c_0_addr <= _th_comp_i_27 + _th_comp_offset_stream_24;
      end 
      _ram_c_cond_2_1 <= th_comp == 23;
      _ram_c_cond_3_1 <= th_comp == 23;
      if(th_comp == 25) begin
        ram_c_0_addr <= _th_comp_i_27 + _th_comp_offset_seq_25;
      end 
      _ram_c_cond_4_1 <= th_comp == 25;
      _ram_c_cond_5_1 <= th_comp == 25;
    end
  end

  assign _tmp_data_43 = _tmp_36;
  assign _tmp_valid_43 = _tmp_30;
  assign _tmp_32 = 1 && _tmp_ready_43;
  assign _tmp_data_74 = _tmp_67;
  assign _tmp_valid_74 = _tmp_61;
  assign _tmp_63 = 1 && _tmp_ready_74;
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
      _th_comp_offset_0 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_3 <= 0;
      _tmp_2 <= 0;
      _tmp_25 <= 0;
      _tmp_26 <= 0;
      _tmp_28 <= 0;
      _tmp_27 <= 0;
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _tmp_47 <= 0;
      _tmp_46 <= 0;
      _tmp_56 <= 0;
      _tmp_57 <= 0;
      _tmp_59 <= 0;
      _tmp_58 <= 0;
      _th_comp_offset_stream_24 <= 0;
      _th_comp_offset_seq_25 <= 0;
      _th_comp_all_ok_26 <= 0;
      _th_comp_i_27 <= 0;
      _tmp_76 <= 0;
      _th_comp_st_28 <= 0;
      _tmp_78 <= 0;
      _th_comp_sq_29 <= 0;
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
          _tmp_3 <= 64;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          if(_tmp_3 <= 256) begin
            _tmp_2 <= _tmp_3;
            _tmp_3 <= 0;
          end else begin
            _tmp_2 <= 256;
            _tmp_3 <= _tmp_3 - 256;
          end
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          if(_tmp_8) begin
            _tmp_0 <= _tmp_0 + _tmp_2;
            _tmp_1 <= _tmp_1 + (_tmp_2 << 2);
          end 
          if(_tmp_8 && (_tmp_3 > 0)) begin
            th_comp <= th_comp_3;
          end 
          if(_tmp_8 && (_tmp_3 == 0)) begin
            th_comp <= th_comp_5;
          end 
        end
        th_comp_5: begin
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          if(_mystream_flag_1 && _mystream_flag_8) begin
            th_comp <= th_comp_7;
          end 
        end
        th_comp_7: begin
          _tmp_25 <= _th_comp_offset_0;
          _tmp_26 <= 4096;
          _tmp_28 <= 64;
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if(_tmp_28 <= 256) begin
            _tmp_27 <= _tmp_28;
            _tmp_28 <= 0;
          end else begin
            _tmp_27 <= 256;
            _tmp_28 <= _tmp_28 - 256;
          end
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          if(_tmp_42) begin
            _tmp_25 <= _tmp_25 + _tmp_27;
            _tmp_26 <= _tmp_26 + (_tmp_27 << 2);
          end 
          if(_tmp_42 && (_tmp_28 > 0)) begin
            th_comp <= th_comp_8;
          end 
          if(_tmp_42 && (_tmp_28 == 0)) begin
            th_comp <= th_comp_10;
          end 
        end
        th_comp_10: begin
          _th_comp_offset_0 <= 64;
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          _tmp_44 <= _th_comp_offset_0;
          _tmp_45 <= 0;
          _tmp_47 <= 64;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          if(_tmp_47 <= 256) begin
            _tmp_46 <= _tmp_47;
            _tmp_47 <= 0;
          end else begin
            _tmp_46 <= 256;
            _tmp_47 <= _tmp_47 - 256;
          end
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          if(_tmp_52) begin
            _tmp_44 <= _tmp_44 + _tmp_46;
            _tmp_45 <= _tmp_45 + (_tmp_46 << 2);
          end 
          if(_tmp_52 && (_tmp_47 > 0)) begin
            th_comp <= th_comp_12;
          end 
          if(_tmp_52 && (_tmp_47 == 0)) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(th_sequential == 24) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          _tmp_56 <= _th_comp_offset_0;
          _tmp_57 <= 8192;
          _tmp_59 <= 64;
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          if(_tmp_59 <= 256) begin
            _tmp_58 <= _tmp_59;
            _tmp_59 <= 0;
          end else begin
            _tmp_58 <= 256;
            _tmp_59 <= _tmp_59 - 256;
          end
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          if(_tmp_73) begin
            _tmp_56 <= _tmp_56 + _tmp_58;
            _tmp_57 <= _tmp_57 + (_tmp_58 << 2);
          end 
          if(_tmp_73 && (_tmp_59 > 0)) begin
            th_comp <= th_comp_17;
          end 
          if(_tmp_73 && (_tmp_59 == 0)) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          _th_comp_offset_stream_24 <= 0;
          _th_comp_offset_seq_25 <= _th_comp_offset_0;
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          _th_comp_all_ok_26 <= 1;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          _th_comp_i_27 <= 0;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          if(_th_comp_i_27 < 64) begin
            th_comp <= th_comp_23;
          end else begin
            th_comp <= th_comp_30;
          end
        end
        th_comp_23: begin
          if(_tmp_75) begin
            _tmp_76 <= ram_c_0_rdata;
          end 
          if(_tmp_75) begin
            th_comp <= th_comp_24;
          end 
        end
        th_comp_24: begin
          _th_comp_st_28 <= _tmp_76;
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          if(_tmp_77) begin
            _tmp_78 <= ram_c_0_rdata;
          end 
          if(_tmp_77) begin
            th_comp <= th_comp_26;
          end 
        end
        th_comp_26: begin
          _th_comp_sq_29 <= _tmp_78;
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          if(_th_comp_st_28 != _th_comp_sq_29) begin
            th_comp <= th_comp_28;
          end else begin
            th_comp <= th_comp_29;
          end
        end
        th_comp_28: begin
          _th_comp_all_ok_26 <= 0;
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          _th_comp_i_27 <= _th_comp_i_27 + 1;
          th_comp <= th_comp_22;
        end
        th_comp_30: begin
          if(_th_comp_all_ok_26) begin
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

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_0 <= _tmp_fsm_0_init;
      _tmp_6 <= 0;
      _tmp_5 <= 0;
    end else begin
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_comp == 4) begin
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

  localparam _mystream_fsm_5_1 = 1;
  localparam _mystream_fsm_5_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_5 <= _mystream_fsm_5_init;
      _mystream_flag_1 <= 0;
      _mystream_offset_0_3 <= 0;
      _mystream_offset_1_4 <= 0;
      _mystream_count_0_6 <= 0;
      _mystream_count_1_7 <= 0;
    end else begin
      case(_mystream_fsm_5)
        _mystream_fsm_5_init: begin
          if(th_comp == 5) begin
            _mystream_flag_1 <= 0;
            _mystream_offset_0_3 <= 0;
            _mystream_offset_1_4 <= 0;
          end 
          if(th_comp == 5) begin
            _mystream_fsm_5 <= _mystream_fsm_5_1;
          end 
        end
        _mystream_fsm_5_1: begin
          _mystream_fsm_5 <= _mystream_fsm_5_2;
        end
        _mystream_fsm_5_2: begin
          if(_tmp_21) begin
            _mystream_count_0_6 <= _mystream_count_0_6 + 1;
            _mystream_offset_0_3 <= _mystream_offset_0_3 + 4;
          end 
          if(_tmp_21 && (_mystream_count_0_6 == 1)) begin
            _mystream_count_0_6 <= 0;
            _mystream_offset_0_3 <= 0;
          end 
          if(_tmp_21 && (_mystream_count_0_6 == 1)) begin
            _mystream_count_1_7 <= _mystream_count_1_7 + 1;
            _mystream_offset_1_4 <= _mystream_offset_1_4 + 1;
          end 
          if(_tmp_21 && (_mystream_count_0_6 == 1) && (_mystream_count_1_7 == 3)) begin
            _mystream_count_1_7 <= 0;
            _mystream_offset_1_4 <= 0;
          end 
          if(_tmp_21 && ((_mystream_count_0_6 == 1) && (_mystream_count_1_7 == 3))) begin
            _mystream_flag_1 <= 1;
          end 
          if(_tmp_21) begin
            _mystream_fsm_5 <= _mystream_fsm_5_1;
          end 
          if(_tmp_21 && ((_mystream_count_0_6 == 1) && (_mystream_count_1_7 == 3))) begin
            _mystream_fsm_5 <= _mystream_fsm_5_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_fsm_12_1 = 1;
  localparam _mystream_fsm_12_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm_12 <= _mystream_fsm_12_init;
      _mystream_flag_8 <= 0;
      _mystream_offset_0_10 <= 0;
      _mystream_offset_1_11 <= 0;
      _mystream_count_0_13 <= 0;
      _mystream_count_1_14 <= 0;
    end else begin
      case(_mystream_fsm_12)
        _mystream_fsm_12_init: begin
          if(th_comp == 5) begin
            _mystream_flag_8 <= 0;
            _mystream_offset_0_10 <= 0;
            _mystream_offset_1_11 <= 0;
          end 
          if(th_comp == 5) begin
            _mystream_fsm_12 <= _mystream_fsm_12_1;
          end 
        end
        _mystream_fsm_12_1: begin
          _mystream_fsm_12 <= _mystream_fsm_12_2;
        end
        _mystream_fsm_12_2: begin
          if(_tmp_23) begin
            _mystream_count_0_13 <= _mystream_count_0_13 + 1;
            _mystream_offset_0_10 <= _mystream_offset_0_10 + 4;
          end 
          if(_tmp_23 && (_mystream_count_0_13 == 1)) begin
            _mystream_count_0_13 <= 0;
            _mystream_offset_0_10 <= 0;
          end 
          if(_tmp_23 && (_mystream_count_0_13 == 1)) begin
            _mystream_count_1_14 <= _mystream_count_1_14 + 1;
            _mystream_offset_1_11 <= _mystream_offset_1_11 + 8;
          end 
          if(_tmp_23 && (_mystream_count_0_13 == 1) && (_mystream_count_1_14 == 7)) begin
            _mystream_count_1_14 <= 0;
            _mystream_offset_1_11 <= 0;
          end 
          if(_tmp_23 && ((_mystream_count_0_13 == 1) && (_mystream_count_1_14 == 7))) begin
            _mystream_flag_8 <= 1;
          end 
          if(_tmp_23) begin
            _mystream_fsm_12 <= _mystream_fsm_12_1;
          end 
          if(_tmp_23 && ((_mystream_count_0_13 == 1) && (_mystream_count_1_14 == 7))) begin
            _mystream_fsm_12 <= _mystream_fsm_12_init;
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
          if(th_comp == 9) begin
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
          if(_tmp_42) begin
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
      _tmp_50 <= 0;
      _tmp_49 <= 0;
    end else begin
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_comp == 13) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
        end
        _tmp_fsm_2_2: begin
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          _tmp_50 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_49 <= myaxi_rdata;
            _tmp_50 <= 1;
          end 
          if(_tmp_52) begin
            _tmp_fsm_2 <= _tmp_fsm_2_init;
          end 
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
      _th_sequential_offset_15 <= 0;
      _th_sequential_offset_16 <= 0;
      _th_sequential_zpos_17 <= 0;
      _th_sequential_ypos_18 <= 0;
      _th_sequential_xpos_19 <= 0;
      _th_sequential_x_20 <= 0;
      _th_sequential_y_21 <= 0;
      _th_sequential_z_22 <= 0;
      _tmp_55 <= 0;
      _th_sequential_a_23 <= 0;
    end else begin
      case(th_sequential)
        th_sequential_init: begin
          if(th_comp == 14) begin
            _th_sequential_called <= 1;
          end 
          if(th_comp == 14) begin
            _th_sequential_offset_15 <= _th_comp_offset_0;
          end 
          if(th_comp == 14) begin
            th_sequential <= th_sequential_1;
          end 
        end
        th_sequential_1: begin
          _th_sequential_offset_16 <= _th_sequential_offset_15;
          th_sequential <= th_sequential_2;
        end
        th_sequential_2: begin
          _th_sequential_zpos_17 <= 0;
          th_sequential <= th_sequential_3;
        end
        th_sequential_3: begin
          _th_sequential_ypos_18 <= 0;
          th_sequential <= th_sequential_4;
        end
        th_sequential_4: begin
          _th_sequential_xpos_19 <= 0;
          th_sequential <= th_sequential_5;
        end
        th_sequential_5: begin
          _th_sequential_x_20 <= 0;
          th_sequential <= th_sequential_6;
        end
        th_sequential_6: begin
          if(_th_sequential_x_20 < 4) begin
            th_sequential <= th_sequential_7;
          end else begin
            th_sequential <= th_sequential_24;
          end
        end
        th_sequential_7: begin
          _th_sequential_y_21 <= 0;
          th_sequential <= th_sequential_8;
        end
        th_sequential_8: begin
          if(_th_sequential_y_21 < 2) begin
            th_sequential <= th_sequential_9;
          end else begin
            th_sequential <= th_sequential_23;
          end
        end
        th_sequential_9: begin
          _th_sequential_z_22 <= 0;
          th_sequential <= th_sequential_10;
        end
        th_sequential_10: begin
          if(_th_sequential_z_22 < 8) begin
            th_sequential <= th_sequential_11;
          end else begin
            th_sequential <= th_sequential_22;
          end
        end
        th_sequential_11: begin
          if(_tmp_54) begin
            _tmp_55 <= ram_a_0_rdata;
          end 
          if(_tmp_54) begin
            th_sequential <= th_sequential_12;
          end 
        end
        th_sequential_12: begin
          _th_sequential_a_23 <= _tmp_55;
          th_sequential <= th_sequential_13;
        end
        th_sequential_13: begin
          th_sequential <= th_sequential_14;
        end
        th_sequential_14: begin
          _th_sequential_xpos_19 <= _th_sequential_xpos_19 + 1;
          th_sequential <= th_sequential_15;
        end
        th_sequential_15: begin
          if(_th_sequential_xpos_19 == 4) begin
            th_sequential <= th_sequential_16;
          end else begin
            th_sequential <= th_sequential_21;
          end
        end
        th_sequential_16: begin
          _th_sequential_xpos_19 <= 0;
          th_sequential <= th_sequential_17;
        end
        th_sequential_17: begin
          _th_sequential_ypos_18 <= _th_sequential_ypos_18 + 4;
          th_sequential <= th_sequential_18;
        end
        th_sequential_18: begin
          if(_th_sequential_ypos_18 == 8) begin
            th_sequential <= th_sequential_19;
          end else begin
            th_sequential <= th_sequential_21;
          end
        end
        th_sequential_19: begin
          _th_sequential_ypos_18 <= 0;
          th_sequential <= th_sequential_20;
        end
        th_sequential_20: begin
          _th_sequential_zpos_17 <= _th_sequential_zpos_17 + 8;
          th_sequential <= th_sequential_21;
        end
        th_sequential_21: begin
          _th_sequential_z_22 <= _th_sequential_z_22 + 1;
          th_sequential <= th_sequential_10;
        end
        th_sequential_22: begin
          _th_sequential_y_21 <= _th_sequential_y_21 + 1;
          th_sequential <= th_sequential_8;
        end
        th_sequential_23: begin
          _th_sequential_x_20 <= _th_sequential_x_20 + 1;
          th_sequential <= th_sequential_6;
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
          if(th_comp == 18) begin
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
          if(_tmp_73) begin
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
"""


def test():
    veriloggen.reset()
    test_module = thread_stream_transpose.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
