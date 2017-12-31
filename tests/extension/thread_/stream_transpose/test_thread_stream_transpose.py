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

  reg [32-1:0] _mystream_fsm;
  localparam _mystream_fsm_init = 0;
  reg _mystream_start;
  reg _mystream_busy;
  reg [16-1:0] _mystream_a_fsm_sel;
  reg _mystream_a_idle;
  reg [16-1:0] _mystream_b_fsm_sel;
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
  reg signed [32-1:0] _th_comp_offset_1;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  assign mystream_b_data = mystream_a_data;
  reg [32-1:0] _mystream_a_fsm_1;
  localparam _mystream_a_fsm_1_init = 0;
  reg [10-1:0] _mystream_a_offset_1;
  reg [10-1:0] _mystream_a_pat_offset_1_0;
  reg [10-1:0] _mystream_a_pat_offset_1_1;
  reg [10-1:0] _mystream_a_pat_offset_1_2;
  reg [11-1:0] _mystream_a_pat_size_1_0;
  reg [11-1:0] _mystream_a_pat_size_1_1;
  reg [11-1:0] _mystream_a_pat_size_1_2;
  reg [10-1:0] _mystream_a_pat_stride_1_0;
  reg [10-1:0] _mystream_a_pat_stride_1_1;
  reg [10-1:0] _mystream_a_pat_stride_1_2;
  reg [11-1:0] _mystream_a_pat_count_1_0;
  reg [11-1:0] _mystream_a_pat_count_1_1;
  reg [11-1:0] _mystream_a_pat_count_1_2;
  wire [10-1:0] _mystream_a_all_offset_1;
  assign _mystream_a_all_offset_1 = _mystream_a_offset_1 + _mystream_a_pat_offset_1_0 + _mystream_a_pat_offset_1_1 + _mystream_a_pat_offset_1_2;
  reg [10-1:0] _mystream_a_raddr_1;
  reg _mystream_a_renable_1;
  reg _tmp_13;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  reg [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _d1__mystream_a_fsm_1;
  reg __mystream_a_fsm_1_cond_1_0_1;
  reg [32-1:0] _mystream_b_fsm_2;
  localparam _mystream_b_fsm_2_init = 0;
  reg [10-1:0] _mystream_b_offset_2;
  reg [10-1:0] _mystream_b_pat_offset_2_0;
  reg [10-1:0] _mystream_b_pat_offset_2_1;
  reg [10-1:0] _mystream_b_pat_offset_2_2;
  reg [11-1:0] _mystream_b_pat_size_2_0;
  reg [11-1:0] _mystream_b_pat_size_2_1;
  reg [11-1:0] _mystream_b_pat_size_2_2;
  reg [10-1:0] _mystream_b_pat_stride_2_0;
  reg [10-1:0] _mystream_b_pat_stride_2_1;
  reg [10-1:0] _mystream_b_pat_stride_2_2;
  reg [11-1:0] _mystream_b_pat_count_2_0;
  reg [11-1:0] _mystream_b_pat_count_2_1;
  reg [11-1:0] _mystream_b_pat_count_2_2;
  wire [10-1:0] _mystream_b_all_offset_2;
  assign _mystream_b_all_offset_2 = _mystream_b_offset_2 + _mystream_b_pat_offset_2_0 + _mystream_b_pat_offset_2_1 + _mystream_b_pat_offset_2_2;
  reg [10-1:0] _mystream_b_waddr_2;
  reg _mystream_b_wenable_2;
  reg signed [32-1:0] _mystream_b_wdata_2;
  reg _ram_b_cond_0_1;
  reg [32-1:0] _d1__mystream_b_fsm_2;
  reg __mystream_b_fsm_2_cond_5_0_1;
  reg [32-1:0] _d1__mystream_fsm;
  reg __mystream_fsm_cond_0_0_1;
  wire _mystream_done;
  assign _mystream_done = _mystream_a_idle;
  reg [10-1:0] _tmp_14;
  reg [32-1:0] _tmp_15;
  reg [32-1:0] _tmp_16;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_17;
  reg [33-1:0] _tmp_18;
  reg [33-1:0] _tmp_19;
  reg _tmp_20;
  reg _tmp_21;
  wire _tmp_22;
  wire _tmp_23;
  assign _tmp_23 = 1;
  localparam _tmp_24 = 1;
  wire [_tmp_24-1:0] _tmp_25;
  assign _tmp_25 = (_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21);
  reg [_tmp_24-1:0] __tmp_25_1;
  wire signed [32-1:0] _tmp_26;
  reg signed [32-1:0] __tmp_26_1;
  assign _tmp_26 = (__tmp_25_1)? ram_b_0_rdata : __tmp_26_1;
  reg _tmp_27;
  reg _tmp_28;
  reg _tmp_29;
  reg _tmp_30;
  reg [33-1:0] _tmp_31;
  reg [9-1:0] _tmp_32;
  reg _myaxi_cond_1_1;
  reg _tmp_33;
  wire [32-1:0] __variable_data_34;
  wire __variable_valid_34;
  wire __variable_ready_34;
  assign __variable_ready_34 = (_tmp_fsm_1 == 4) && ((_tmp_32 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  reg _tmp_35;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_5_0_1;
  reg [10-1:0] _tmp_36;
  reg [32-1:0] _tmp_37;
  reg [32-1:0] _tmp_38;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_39;
  reg [33-1:0] _tmp_40;
  reg [33-1:0] _tmp_41;
  reg [32-1:0] _tmp_42;
  reg _tmp_43;
  reg [33-1:0] _tmp_44;
  reg _tmp_45;
  wire [32-1:0] __variable_data_46;
  wire __variable_valid_46;
  wire __variable_ready_46;
  assign __variable_ready_46 = (_tmp_44 > 0) && !_tmp_45;
  reg _ram_a_cond_3_1;
  reg [9-1:0] _tmp_47;
  reg _myaxi_cond_3_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_2 == 4);
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_4_0_1;
  reg _tmp_48;
  reg __tmp_fsm_2_cond_5_1_1;
  reg signed [32-1:0] _th_comp_offset_2;
  reg signed [32-1:0] _th_comp_zpos_3;
  reg signed [32-1:0] _th_comp_ypos_4;
  reg signed [32-1:0] _th_comp_xpos_5;
  reg signed [32-1:0] _th_comp_x_6;
  reg signed [32-1:0] _th_comp_y_7;
  reg signed [32-1:0] _th_comp_z_8;
  reg _tmp_49;
  reg _ram_a_cond_4_1;
  reg _ram_a_cond_5_1;
  reg _ram_a_cond_5_2;
  reg signed [32-1:0] _tmp_50;
  reg signed [32-1:0] _th_comp_a_9;
  reg _ram_b_cond_1_1;
  reg [10-1:0] _tmp_51;
  reg [32-1:0] _tmp_52;
  reg [32-1:0] _tmp_53;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_54;
  reg [33-1:0] _tmp_55;
  reg [33-1:0] _tmp_56;
  reg _tmp_57;
  reg _tmp_58;
  wire _tmp_59;
  wire _tmp_60;
  assign _tmp_60 = 1;
  localparam _tmp_61 = 1;
  wire [_tmp_61-1:0] _tmp_62;
  assign _tmp_62 = (_tmp_59 || !_tmp_57) && (_tmp_60 || !_tmp_58);
  reg [_tmp_61-1:0] __tmp_62_1;
  wire signed [32-1:0] _tmp_63;
  reg signed [32-1:0] __tmp_63_1;
  assign _tmp_63 = (__tmp_62_1)? ram_b_0_rdata : __tmp_63_1;
  reg _tmp_64;
  reg _tmp_65;
  reg _tmp_66;
  reg _tmp_67;
  reg [33-1:0] _tmp_68;
  reg [9-1:0] _tmp_69;
  reg _myaxi_cond_4_1;
  reg _tmp_70;
  wire [32-1:0] __variable_data_71;
  wire __variable_valid_71;
  wire __variable_ready_71;
  assign __variable_ready_71 = (_tmp_fsm_3 == 4) && ((_tmp_69 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_5_1;
  reg _tmp_72;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_5_0_1;
  reg signed [32-1:0] _th_comp_offset_stream_10;
  reg signed [32-1:0] _th_comp_offset_seq_11;
  reg signed [32-1:0] _th_comp_all_ok_12;
  reg signed [32-1:0] _th_comp_i_13;
  reg _tmp_73;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_3_2;
  reg signed [32-1:0] _tmp_74;
  reg signed [32-1:0] _th_comp_st_14;
  reg _tmp_75;
  reg _ram_b_cond_4_1;
  reg _ram_b_cond_5_1;
  reg _ram_b_cond_5_2;
  reg signed [32-1:0] _tmp_76;
  reg signed [32-1:0] _th_comp_sq_15;

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
      _tmp_32 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_33 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_47 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_69 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_70 <= 0;
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
        _tmp_33 <= 0;
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
        _tmp_70 <= 0;
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
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_32 == 0))) begin
        myaxi_awaddr <= _tmp_17;
        myaxi_awlen <= _tmp_18 - 1;
        myaxi_awvalid <= 1;
        _tmp_32 <= _tmp_18;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_32 == 0)) && (_tmp_18 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_34 && ((_tmp_fsm_1 == 4) && ((_tmp_32 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_32 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_32 > 0))) begin
        myaxi_wdata <= __variable_data_34;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_32 <= _tmp_32 - 1;
      end 
      if(__variable_valid_34 && ((_tmp_fsm_1 == 4) && ((_tmp_32 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_32 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_32 > 0)) && (_tmp_32 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_33 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_33 <= _tmp_33;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_47 == 0))) begin
        myaxi_araddr <= _tmp_39;
        myaxi_arlen <= _tmp_40 - 1;
        myaxi_arvalid <= 1;
        _tmp_47 <= _tmp_40;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_47 > 0)) begin
        _tmp_47 <= _tmp_47 - 1;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_69 == 0))) begin
        myaxi_awaddr <= _tmp_54;
        myaxi_awlen <= _tmp_55 - 1;
        myaxi_awvalid <= 1;
        _tmp_69 <= _tmp_55;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_69 == 0)) && (_tmp_55 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_71 && ((_tmp_fsm_3 == 4) && ((_tmp_69 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_69 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_69 > 0))) begin
        myaxi_wdata <= __variable_data_71;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_69 <= _tmp_69 - 1;
      end 
      if(__variable_valid_71 && ((_tmp_fsm_3 == 4) && ((_tmp_69 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_69 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_69 > 0)) && (_tmp_69 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_70 <= 1;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_70 <= _tmp_70;
      end 
    end
  end

  assign __variable_data_10 = _tmp_6;
  assign __variable_valid_10 = _tmp_7;
  assign __variable_data_46 = _tmp_42;
  assign __variable_valid_46 = _tmp_43;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_8 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_9 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_13 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
      _tmp_44 <= 0;
      _tmp_45 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_4_1 <= 0;
      _tmp_49 <= 0;
      _ram_a_cond_5_1 <= 0;
      _ram_a_cond_5_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_13 <= 0;
      end 
      if(_ram_a_cond_5_2) begin
        _tmp_49 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_9 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_13 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if(_ram_a_cond_3_1) begin
        ram_a_0_wenable <= 0;
        _tmp_45 <= 0;
      end 
      if(_ram_a_cond_4_1) begin
        _tmp_49 <= 1;
      end 
      _ram_a_cond_5_2 <= _ram_a_cond_5_1;
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
      if(_mystream_a_renable_1) begin
        ram_a_0_addr <= _mystream_a_raddr_1;
      end 
      _ram_a_cond_1_1 <= _mystream_a_renable_1;
      _ram_a_cond_2_1 <= _mystream_a_renable_1;
      if((_tmp_fsm_2 == 1) && (_tmp_44 == 0)) begin
        ram_a_0_addr <= _tmp_36 - 1;
        _tmp_44 <= _tmp_38;
      end 
      if(__variable_valid_46 && ((_tmp_44 > 0) && !_tmp_45) && (_tmp_44 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= __variable_data_46;
        ram_a_0_wenable <= 1;
        _tmp_44 <= _tmp_44 - 1;
      end 
      if(__variable_valid_46 && ((_tmp_44 > 0) && !_tmp_45) && (_tmp_44 == 1)) begin
        _tmp_45 <= 1;
      end 
      _ram_a_cond_3_1 <= 1;
      if(th_comp == 24) begin
        ram_a_0_addr <= ((_th_comp_z_8 << 2) << 1) + (_th_comp_y_7 << 2) + _th_comp_x_6 + _th_comp_offset_2;
      end 
      _ram_a_cond_4_1 <= th_comp == 24;
      _ram_a_cond_5_1 <= th_comp == 24;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_25_1 <= 0;
      __tmp_26_1 <= 0;
      _tmp_30 <= 0;
      _tmp_20 <= 0;
      _tmp_21 <= 0;
      _tmp_28 <= 0;
      _tmp_29 <= 0;
      _tmp_27 <= 0;
      _tmp_31 <= 0;
      _ram_b_cond_1_1 <= 0;
      __tmp_62_1 <= 0;
      __tmp_63_1 <= 0;
      _tmp_67 <= 0;
      _tmp_57 <= 0;
      _tmp_58 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_64 <= 0;
      _tmp_68 <= 0;
      _ram_b_cond_2_1 <= 0;
      _tmp_73 <= 0;
      _ram_b_cond_3_1 <= 0;
      _ram_b_cond_3_2 <= 0;
      _ram_b_cond_4_1 <= 0;
      _tmp_75 <= 0;
      _ram_b_cond_5_1 <= 0;
      _ram_b_cond_5_2 <= 0;
    end else begin
      if(_ram_b_cond_3_2) begin
        _tmp_73 <= 0;
      end 
      if(_ram_b_cond_5_2) begin
        _tmp_75 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        ram_b_0_wenable <= 0;
      end 
      if(_ram_b_cond_2_1) begin
        _tmp_73 <= 1;
      end 
      _ram_b_cond_3_2 <= _ram_b_cond_3_1;
      if(_ram_b_cond_4_1) begin
        _tmp_75 <= 1;
      end 
      _ram_b_cond_5_2 <= _ram_b_cond_5_1;
      if(_mystream_b_wenable_2) begin
        ram_b_0_addr <= _mystream_b_waddr_2;
        ram_b_0_wdata <= _mystream_b_wdata_2;
        ram_b_0_wenable <= 1;
      end 
      _ram_b_cond_0_1 <= _mystream_b_wenable_2;
      __tmp_25_1 <= _tmp_25;
      __tmp_26_1 <= _tmp_26;
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && _tmp_28) begin
        _tmp_30 <= 0;
        _tmp_20 <= 0;
        _tmp_21 <= 0;
        _tmp_28 <= 0;
      end 
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && _tmp_27) begin
        _tmp_20 <= 1;
        _tmp_21 <= 1;
        _tmp_30 <= _tmp_29;
        _tmp_29 <= 0;
        _tmp_27 <= 0;
        _tmp_28 <= 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_31 == 0) && !_tmp_29 && !_tmp_30) begin
        ram_b_0_addr <= _tmp_14;
        _tmp_31 <= _tmp_16 - 1;
        _tmp_27 <= 1;
        _tmp_29 <= _tmp_16 == 1;
      end 
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && (_tmp_31 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        _tmp_31 <= _tmp_31 - 1;
        _tmp_27 <= 1;
        _tmp_29 <= 0;
      end 
      if((_tmp_22 || !_tmp_20) && (_tmp_23 || !_tmp_21) && (_tmp_31 == 1)) begin
        _tmp_29 <= 1;
      end 
      if(th_comp == 26) begin
        ram_b_0_addr <= _th_comp_zpos_3 + _th_comp_ypos_4 + _th_comp_xpos_5 + _th_comp_offset_2;
        ram_b_0_wdata <= _th_comp_a_9;
        ram_b_0_wenable <= 1;
      end 
      _ram_b_cond_1_1 <= th_comp == 26;
      __tmp_62_1 <= _tmp_62;
      __tmp_63_1 <= _tmp_63;
      if((_tmp_59 || !_tmp_57) && (_tmp_60 || !_tmp_58) && _tmp_65) begin
        _tmp_67 <= 0;
        _tmp_57 <= 0;
        _tmp_58 <= 0;
        _tmp_65 <= 0;
      end 
      if((_tmp_59 || !_tmp_57) && (_tmp_60 || !_tmp_58) && _tmp_64) begin
        _tmp_57 <= 1;
        _tmp_58 <= 1;
        _tmp_67 <= _tmp_66;
        _tmp_66 <= 0;
        _tmp_64 <= 0;
        _tmp_65 <= 1;
      end 
      if((_tmp_fsm_3 == 1) && (_tmp_68 == 0) && !_tmp_66 && !_tmp_67) begin
        ram_b_0_addr <= _tmp_51;
        _tmp_68 <= _tmp_53 - 1;
        _tmp_64 <= 1;
        _tmp_66 <= _tmp_53 == 1;
      end 
      if((_tmp_59 || !_tmp_57) && (_tmp_60 || !_tmp_58) && (_tmp_68 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        _tmp_68 <= _tmp_68 - 1;
        _tmp_64 <= 1;
        _tmp_66 <= 0;
      end 
      if((_tmp_59 || !_tmp_57) && (_tmp_60 || !_tmp_58) && (_tmp_68 == 1)) begin
        _tmp_66 <= 1;
      end 
      if(th_comp == 43) begin
        ram_b_0_addr <= _th_comp_i_13 + _th_comp_offset_stream_10;
      end 
      _ram_b_cond_2_1 <= th_comp == 43;
      _ram_b_cond_3_1 <= th_comp == 43;
      if(th_comp == 45) begin
        ram_b_0_addr <= _th_comp_i_13 + _th_comp_offset_seq_11;
      end 
      _ram_b_cond_4_1 <= th_comp == 45;
      _ram_b_cond_5_1 <= th_comp == 45;
    end
  end

  assign __variable_data_34 = _tmp_26;
  assign __variable_valid_34 = _tmp_20;
  assign _tmp_22 = 1 && __variable_ready_34;
  assign __variable_data_71 = _tmp_63;
  assign __variable_valid_71 = _tmp_57;
  assign _tmp_59 = 1 && __variable_ready_71;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_fsm_sel <= 0;
      _mystream_a_idle <= 1;
      __variable_wdata_0 <= 0;
      _mystream_b_fsm_sel <= 0;
    end else begin
      if(th_comp == 5) begin
        _mystream_a_fsm_sel <= 1;
      end 
      if(_mystream_start) begin
        _mystream_a_idle <= 0;
      end 
      if(_tmp_13) begin
        __variable_wdata_0 <= ram_a_0_rdata;
      end 
      if((_mystream_a_fsm_1 == 1) && ((_mystream_a_pat_count_1_0 == 0) && (_mystream_a_pat_count_1_1 == 0) && (_mystream_a_pat_count_1_2 == 0))) begin
        _mystream_a_idle <= 1;
      end 
      if(th_comp == 6) begin
        _mystream_b_fsm_sel <= 2;
      end 
    end
  end

  localparam _mystream_fsm_1 = 1;
  localparam _mystream_fsm_2 = 2;
  localparam _mystream_fsm_3 = 3;
  localparam _mystream_fsm_4 = 4;
  localparam _mystream_fsm_5 = 5;
  localparam _mystream_fsm_6 = 6;
  localparam _mystream_fsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm <= _mystream_fsm_init;
      _d1__mystream_fsm <= _mystream_fsm_init;
      _mystream_start <= 0;
      _mystream_busy <= 0;
      __mystream_fsm_cond_0_0_1 <= 0;
    end else begin
      _d1__mystream_fsm <= _mystream_fsm;
      case(_d1__mystream_fsm)
        _mystream_fsm_init: begin
          if(__mystream_fsm_cond_0_0_1) begin
            _mystream_start <= 0;
          end 
        end
      endcase
      case(_mystream_fsm)
        _mystream_fsm_init: begin
          if(th_comp == 7) begin
            _mystream_start <= 1;
            _mystream_busy <= 1;
          end 
          __mystream_fsm_cond_0_0_1 <= th_comp == 7;
          if(th_comp == 7) begin
            _mystream_fsm <= _mystream_fsm_1;
          end 
        end
        _mystream_fsm_1: begin
          _mystream_fsm <= _mystream_fsm_2;
        end
        _mystream_fsm_2: begin
          if(_mystream_done) begin
            _mystream_fsm <= _mystream_fsm_3;
          end 
        end
        _mystream_fsm_3: begin
          _mystream_fsm <= _mystream_fsm_4;
        end
        _mystream_fsm_4: begin
          _mystream_fsm <= _mystream_fsm_5;
        end
        _mystream_fsm_5: begin
          _mystream_fsm <= _mystream_fsm_6;
        end
        _mystream_fsm_6: begin
          _mystream_fsm <= _mystream_fsm_7;
        end
        _mystream_fsm_7: begin
          _mystream_busy <= 0;
          _mystream_fsm <= _mystream_fsm_init;
        end
      endcase
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
  localparam th_comp_37 = 37;
  localparam th_comp_38 = 38;
  localparam th_comp_39 = 39;
  localparam th_comp_40 = 40;
  localparam th_comp_41 = 41;
  localparam th_comp_42 = 42;
  localparam th_comp_43 = 43;
  localparam th_comp_44 = 44;
  localparam th_comp_45 = 45;
  localparam th_comp_46 = 46;
  localparam th_comp_47 = 47;
  localparam th_comp_48 = 48;
  localparam th_comp_49 = 49;
  localparam th_comp_50 = 50;
  localparam th_comp_51 = 51;
  localparam th_comp_52 = 52;
  localparam th_comp_53 = 53;
  localparam th_comp_54 = 54;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_offset_0 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _th_comp_offset_1 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_16 <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _tmp_38 <= 0;
      _th_comp_offset_2 <= 0;
      _th_comp_zpos_3 <= 0;
      _th_comp_ypos_4 <= 0;
      _th_comp_xpos_5 <= 0;
      _th_comp_x_6 <= 0;
      _th_comp_y_7 <= 0;
      _th_comp_z_8 <= 0;
      _tmp_50 <= 0;
      _th_comp_a_9 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_53 <= 0;
      _th_comp_offset_stream_10 <= 0;
      _th_comp_offset_seq_11 <= 0;
      _th_comp_all_ok_12 <= 0;
      _th_comp_i_13 <= 0;
      _tmp_74 <= 0;
      _th_comp_st_14 <= 0;
      _tmp_76 <= 0;
      _th_comp_sq_15 <= 0;
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
          _tmp_2 <= 64;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          if(_tmp_12) begin
            th_comp <= th_comp_4;
          end 
        end
        th_comp_4: begin
          _th_comp_offset_1 <= _th_comp_offset_0;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_9;
          end 
        end
        th_comp_9: begin
          _tmp_14 <= _th_comp_offset_0;
          _tmp_15 <= 4096;
          _tmp_16 <= 64;
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          if(_tmp_35) begin
            th_comp <= th_comp_11;
          end 
        end
        th_comp_11: begin
          _th_comp_offset_0 <= 64;
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          _tmp_36 <= _th_comp_offset_0;
          _tmp_37 <= 0;
          _tmp_38 <= 64;
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          if(_tmp_48) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          _th_comp_offset_2 <= _th_comp_offset_0;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          _th_comp_zpos_3 <= 0;
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          _th_comp_ypos_4 <= 0;
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          _th_comp_xpos_5 <= 0;
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          _th_comp_x_6 <= 0;
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(_th_comp_x_6 < 4) begin
            th_comp <= th_comp_20;
          end else begin
            th_comp <= th_comp_37;
          end
        end
        th_comp_20: begin
          _th_comp_y_7 <= 0;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          if(_th_comp_y_7 < 2) begin
            th_comp <= th_comp_22;
          end else begin
            th_comp <= th_comp_36;
          end
        end
        th_comp_22: begin
          _th_comp_z_8 <= 0;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          if(_th_comp_z_8 < 8) begin
            th_comp <= th_comp_24;
          end else begin
            th_comp <= th_comp_35;
          end
        end
        th_comp_24: begin
          if(_tmp_49) begin
            _tmp_50 <= ram_a_0_rdata;
          end 
          if(_tmp_49) begin
            th_comp <= th_comp_25;
          end 
        end
        th_comp_25: begin
          _th_comp_a_9 <= _tmp_50;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          _th_comp_xpos_5 <= _th_comp_xpos_5 + 1;
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          if(_th_comp_xpos_5 == 4) begin
            th_comp <= th_comp_29;
          end else begin
            th_comp <= th_comp_34;
          end
        end
        th_comp_29: begin
          _th_comp_xpos_5 <= 0;
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          _th_comp_ypos_4 <= _th_comp_ypos_4 + 4;
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          if(_th_comp_ypos_4 == 8) begin
            th_comp <= th_comp_32;
          end else begin
            th_comp <= th_comp_34;
          end
        end
        th_comp_32: begin
          _th_comp_ypos_4 <= 0;
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          _th_comp_zpos_3 <= _th_comp_zpos_3 + 8;
          th_comp <= th_comp_34;
        end
        th_comp_34: begin
          _th_comp_z_8 <= _th_comp_z_8 + 1;
          th_comp <= th_comp_23;
        end
        th_comp_35: begin
          _th_comp_y_7 <= _th_comp_y_7 + 1;
          th_comp <= th_comp_21;
        end
        th_comp_36: begin
          _th_comp_x_6 <= _th_comp_x_6 + 1;
          th_comp <= th_comp_19;
        end
        th_comp_37: begin
          _tmp_51 <= _th_comp_offset_0;
          _tmp_52 <= 8192;
          _tmp_53 <= 64;
          th_comp <= th_comp_38;
        end
        th_comp_38: begin
          if(_tmp_72) begin
            th_comp <= th_comp_39;
          end 
        end
        th_comp_39: begin
          _th_comp_offset_stream_10 <= 0;
          _th_comp_offset_seq_11 <= _th_comp_offset_0;
          th_comp <= th_comp_40;
        end
        th_comp_40: begin
          _th_comp_all_ok_12 <= 1;
          th_comp <= th_comp_41;
        end
        th_comp_41: begin
          _th_comp_i_13 <= 0;
          th_comp <= th_comp_42;
        end
        th_comp_42: begin
          if(_th_comp_i_13 < 64) begin
            th_comp <= th_comp_43;
          end else begin
            th_comp <= th_comp_50;
          end
        end
        th_comp_43: begin
          if(_tmp_73) begin
            _tmp_74 <= ram_b_0_rdata;
          end 
          if(_tmp_73) begin
            th_comp <= th_comp_44;
          end 
        end
        th_comp_44: begin
          _th_comp_st_14 <= _tmp_74;
          th_comp <= th_comp_45;
        end
        th_comp_45: begin
          if(_tmp_75) begin
            _tmp_76 <= ram_b_0_rdata;
          end 
          if(_tmp_75) begin
            th_comp <= th_comp_46;
          end 
        end
        th_comp_46: begin
          _th_comp_sq_15 <= _tmp_76;
          th_comp <= th_comp_47;
        end
        th_comp_47: begin
          if(_th_comp_st_14 !== _th_comp_sq_15) begin
            th_comp <= th_comp_48;
          end else begin
            th_comp <= th_comp_49;
          end
        end
        th_comp_48: begin
          _th_comp_all_ok_12 <= 0;
          th_comp <= th_comp_49;
        end
        th_comp_49: begin
          _th_comp_i_13 <= _th_comp_i_13 + 1;
          th_comp <= th_comp_42;
        end
        th_comp_50: begin
          if(_th_comp_all_ok_12) begin
            th_comp <= th_comp_51;
          end else begin
            th_comp <= th_comp_53;
          end
        end
        th_comp_51: begin
          $display("OK");
          th_comp <= th_comp_52;
        end
        th_comp_52: begin
          th_comp <= th_comp_54;
        end
        th_comp_53: begin
          $display("NG");
          th_comp <= th_comp_54;
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

  localparam _mystream_a_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
      _d1__mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
      _mystream_a_offset_1 <= 0;
      _mystream_a_pat_offset_1_0 <= 0;
      _mystream_a_pat_offset_1_1 <= 0;
      _mystream_a_pat_offset_1_2 <= 0;
      _mystream_a_pat_size_1_0 <= 0;
      _mystream_a_pat_stride_1_0 <= 0;
      _mystream_a_pat_size_1_1 <= 0;
      _mystream_a_pat_stride_1_1 <= 0;
      _mystream_a_pat_size_1_2 <= 0;
      _mystream_a_pat_stride_1_2 <= 0;
      _mystream_a_pat_count_1_0 <= 0;
      _mystream_a_pat_count_1_1 <= 0;
      _mystream_a_pat_count_1_2 <= 0;
      _mystream_a_raddr_1 <= 0;
      _mystream_a_renable_1 <= 0;
      __mystream_a_fsm_1_cond_1_0_1 <= 0;
    end else begin
      _d1__mystream_a_fsm_1 <= _mystream_a_fsm_1;
      case(_d1__mystream_a_fsm_1)
        _mystream_a_fsm_1_1: begin
          if(__mystream_a_fsm_1_cond_1_0_1) begin
            _mystream_a_renable_1 <= 0;
          end 
        end
      endcase
      case(_mystream_a_fsm_1)
        _mystream_a_fsm_1_init: begin
          if(th_comp == 5) begin
            _mystream_a_offset_1 <= _th_comp_offset_1;
          end 
          if(th_comp == 5) begin
            _mystream_a_pat_offset_1_0 <= 0;
          end 
          if(th_comp == 5) begin
            _mystream_a_pat_offset_1_1 <= 0;
          end 
          if(th_comp == 5) begin
            _mystream_a_pat_offset_1_2 <= 0;
          end 
          if(th_comp == 5) begin
            _mystream_a_pat_size_1_0 <= 8;
            _mystream_a_pat_stride_1_0 <= 8;
          end 
          if(th_comp == 5) begin
            _mystream_a_pat_size_1_1 <= 2;
            _mystream_a_pat_stride_1_1 <= 4;
          end 
          if(th_comp == 5) begin
            _mystream_a_pat_size_1_2 <= 4;
            _mystream_a_pat_stride_1_2 <= 1;
          end 
          if(_mystream_start && (_mystream_a_fsm_sel == 1) && (_mystream_a_pat_size_1_0 > 0) && (_mystream_a_pat_size_1_1 > 0) && (_mystream_a_pat_size_1_2 > 0)) begin
            _mystream_a_pat_count_1_0 <= _mystream_a_pat_size_1_0 - 1;
          end 
          if(_mystream_start && (_mystream_a_fsm_sel == 1) && (_mystream_a_pat_size_1_0 > 0) && (_mystream_a_pat_size_1_1 > 0) && (_mystream_a_pat_size_1_2 > 0)) begin
            _mystream_a_pat_count_1_1 <= _mystream_a_pat_size_1_1 - 1;
          end 
          if(_mystream_start && (_mystream_a_fsm_sel == 1) && (_mystream_a_pat_size_1_0 > 0) && (_mystream_a_pat_size_1_1 > 0) && (_mystream_a_pat_size_1_2 > 0)) begin
            _mystream_a_pat_count_1_2 <= _mystream_a_pat_size_1_2 - 1;
          end 
          if(_mystream_start && (_mystream_a_fsm_sel == 1) && (_mystream_a_pat_size_1_0 > 0) && (_mystream_a_pat_size_1_1 > 0) && (_mystream_a_pat_size_1_2 > 0)) begin
            _mystream_a_fsm_1 <= _mystream_a_fsm_1_1;
          end 
        end
        _mystream_a_fsm_1_1: begin
          _mystream_a_raddr_1 <= _mystream_a_all_offset_1;
          _mystream_a_renable_1 <= 1;
          __mystream_a_fsm_1_cond_1_0_1 <= 1;
          _mystream_a_pat_offset_1_0 <= _mystream_a_pat_offset_1_0 + _mystream_a_pat_stride_1_0;
          _mystream_a_pat_count_1_0 <= _mystream_a_pat_count_1_0 - 1;
          if(_mystream_a_pat_count_1_0 == 0) begin
            _mystream_a_pat_offset_1_0 <= 0;
            _mystream_a_pat_count_1_0 <= _mystream_a_pat_size_1_0 - 1;
          end 
          if(_mystream_a_pat_count_1_0 == 0) begin
            _mystream_a_pat_offset_1_1 <= _mystream_a_pat_offset_1_1 + _mystream_a_pat_stride_1_1;
            _mystream_a_pat_count_1_1 <= _mystream_a_pat_count_1_1 - 1;
          end 
          if((_mystream_a_pat_count_1_0 == 0) && (_mystream_a_pat_count_1_1 == 0)) begin
            _mystream_a_pat_offset_1_1 <= 0;
            _mystream_a_pat_count_1_1 <= _mystream_a_pat_size_1_1 - 1;
          end 
          if((_mystream_a_pat_count_1_0 == 0) && (_mystream_a_pat_count_1_1 == 0)) begin
            _mystream_a_pat_offset_1_2 <= _mystream_a_pat_offset_1_2 + _mystream_a_pat_stride_1_2;
            _mystream_a_pat_count_1_2 <= _mystream_a_pat_count_1_2 - 1;
          end 
          if((_mystream_a_pat_count_1_0 == 0) && (_mystream_a_pat_count_1_1 == 0) && (_mystream_a_pat_count_1_2 == 0)) begin
            _mystream_a_pat_offset_1_2 <= 0;
            _mystream_a_pat_count_1_2 <= _mystream_a_pat_size_1_2 - 1;
          end 
          if((_mystream_a_pat_count_1_0 == 0) && (_mystream_a_pat_count_1_1 == 0) && (_mystream_a_pat_count_1_2 == 0)) begin
            _mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_b_fsm_2_1 = 1;
  localparam _mystream_b_fsm_2_2 = 2;
  localparam _mystream_b_fsm_2_3 = 3;
  localparam _mystream_b_fsm_2_4 = 4;
  localparam _mystream_b_fsm_2_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
      _d1__mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
      _mystream_b_offset_2 <= 0;
      _mystream_b_pat_offset_2_0 <= 0;
      _mystream_b_pat_offset_2_1 <= 0;
      _mystream_b_pat_offset_2_2 <= 0;
      _mystream_b_pat_size_2_0 <= 0;
      _mystream_b_pat_stride_2_0 <= 0;
      _mystream_b_pat_size_2_1 <= 0;
      _mystream_b_pat_stride_2_1 <= 0;
      _mystream_b_pat_size_2_2 <= 0;
      _mystream_b_pat_stride_2_2 <= 0;
      _mystream_b_pat_count_2_0 <= 0;
      _mystream_b_pat_count_2_1 <= 0;
      _mystream_b_pat_count_2_2 <= 0;
      _mystream_b_waddr_2 <= 0;
      _mystream_b_wdata_2 <= 0;
      _mystream_b_wenable_2 <= 0;
      __mystream_b_fsm_2_cond_5_0_1 <= 0;
    end else begin
      _d1__mystream_b_fsm_2 <= _mystream_b_fsm_2;
      case(_d1__mystream_b_fsm_2)
        _mystream_b_fsm_2_5: begin
          if(__mystream_b_fsm_2_cond_5_0_1) begin
            _mystream_b_wenable_2 <= 0;
          end 
        end
      endcase
      case(_mystream_b_fsm_2)
        _mystream_b_fsm_2_init: begin
          if(th_comp == 6) begin
            _mystream_b_offset_2 <= _th_comp_offset_1;
          end 
          if(th_comp == 6) begin
            _mystream_b_pat_offset_2_0 <= 0;
          end 
          if(th_comp == 6) begin
            _mystream_b_pat_offset_2_1 <= 0;
          end 
          if(th_comp == 6) begin
            _mystream_b_pat_offset_2_2 <= 0;
          end 
          if(th_comp == 6) begin
            _mystream_b_pat_size_2_0 <= 4;
            _mystream_b_pat_stride_2_0 <= 1;
          end 
          if(th_comp == 6) begin
            _mystream_b_pat_size_2_1 <= 2;
            _mystream_b_pat_stride_2_1 <= 4;
          end 
          if(th_comp == 6) begin
            _mystream_b_pat_size_2_2 <= 8;
            _mystream_b_pat_stride_2_2 <= 8;
          end 
          if(_mystream_start && (_mystream_b_fsm_sel == 2) && (_mystream_b_pat_size_2_0 > 0) && (_mystream_b_pat_size_2_1 > 0) && (_mystream_b_pat_size_2_2 > 0)) begin
            _mystream_b_pat_count_2_0 <= _mystream_b_pat_size_2_0 - 1;
          end 
          if(_mystream_start && (_mystream_b_fsm_sel == 2) && (_mystream_b_pat_size_2_0 > 0) && (_mystream_b_pat_size_2_1 > 0) && (_mystream_b_pat_size_2_2 > 0)) begin
            _mystream_b_pat_count_2_1 <= _mystream_b_pat_size_2_1 - 1;
          end 
          if(_mystream_start && (_mystream_b_fsm_sel == 2) && (_mystream_b_pat_size_2_0 > 0) && (_mystream_b_pat_size_2_1 > 0) && (_mystream_b_pat_size_2_2 > 0)) begin
            _mystream_b_pat_count_2_2 <= _mystream_b_pat_size_2_2 - 1;
          end 
          if(_mystream_start && (_mystream_b_fsm_sel == 2) && (_mystream_b_pat_size_2_0 > 0) && (_mystream_b_pat_size_2_1 > 0) && (_mystream_b_pat_size_2_2 > 0)) begin
            _mystream_b_fsm_2 <= _mystream_b_fsm_2_1;
          end 
        end
        _mystream_b_fsm_2_1: begin
          _mystream_b_fsm_2 <= _mystream_b_fsm_2_2;
        end
        _mystream_b_fsm_2_2: begin
          _mystream_b_fsm_2 <= _mystream_b_fsm_2_3;
        end
        _mystream_b_fsm_2_3: begin
          _mystream_b_fsm_2 <= _mystream_b_fsm_2_4;
        end
        _mystream_b_fsm_2_4: begin
          _mystream_b_fsm_2 <= _mystream_b_fsm_2_5;
        end
        _mystream_b_fsm_2_5: begin
          _mystream_b_waddr_2 <= _mystream_b_all_offset_2;
          _mystream_b_wdata_2 <= mystream_b_data;
          _mystream_b_wenable_2 <= 1;
          __mystream_b_fsm_2_cond_5_0_1 <= 1;
          _mystream_b_pat_offset_2_0 <= _mystream_b_pat_offset_2_0 + _mystream_b_pat_stride_2_0;
          _mystream_b_pat_count_2_0 <= _mystream_b_pat_count_2_0 - 1;
          if(_mystream_b_pat_count_2_0 == 0) begin
            _mystream_b_pat_offset_2_0 <= 0;
            _mystream_b_pat_count_2_0 <= _mystream_b_pat_size_2_0 - 1;
          end 
          if(_mystream_b_pat_count_2_0 == 0) begin
            _mystream_b_pat_offset_2_1 <= _mystream_b_pat_offset_2_1 + _mystream_b_pat_stride_2_1;
            _mystream_b_pat_count_2_1 <= _mystream_b_pat_count_2_1 - 1;
          end 
          if((_mystream_b_pat_count_2_0 == 0) && (_mystream_b_pat_count_2_1 == 0)) begin
            _mystream_b_pat_offset_2_1 <= 0;
            _mystream_b_pat_count_2_1 <= _mystream_b_pat_size_2_1 - 1;
          end 
          if((_mystream_b_pat_count_2_0 == 0) && (_mystream_b_pat_count_2_1 == 0)) begin
            _mystream_b_pat_offset_2_2 <= _mystream_b_pat_offset_2_2 + _mystream_b_pat_stride_2_2;
            _mystream_b_pat_count_2_2 <= _mystream_b_pat_count_2_2 - 1;
          end 
          if((_mystream_b_pat_count_2_0 == 0) && (_mystream_b_pat_count_2_1 == 0) && (_mystream_b_pat_count_2_2 == 0)) begin
            _mystream_b_pat_offset_2_2 <= 0;
            _mystream_b_pat_count_2_2 <= _mystream_b_pat_size_2_2 - 1;
          end 
          if((_mystream_b_pat_count_2_0 == 0) && (_mystream_b_pat_count_2_1 == 0) && (_mystream_b_pat_count_2_2 == 0)) begin
            _mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
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
      _tmp_17 <= 0;
      _tmp_19 <= 0;
      _tmp_18 <= 0;
      _tmp_35 <= 0;
      __tmp_fsm_1_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_0_1) begin
            _tmp_35 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_comp == 10) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_17 <= (_tmp_15 >> 2) << 2;
          _tmp_19 <= _tmp_16;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_19 <= 256) && ((_tmp_17 & 4095) + (_tmp_19 << 2) >= 4096)) begin
            _tmp_18 <= 4096 - (_tmp_17 & 4095) >> 2;
            _tmp_19 <= _tmp_19 - (4096 - (_tmp_17 & 4095) >> 2);
          end else if(_tmp_19 <= 256) begin
            _tmp_18 <= _tmp_19;
            _tmp_19 <= 0;
          end else if((_tmp_17 & 4095) + 1024 >= 4096) begin
            _tmp_18 <= 4096 - (_tmp_17 & 4095) >> 2;
            _tmp_19 <= _tmp_19 - (4096 - (_tmp_17 & 4095) >> 2);
          end else begin
            _tmp_18 <= 256;
            _tmp_19 <= _tmp_19 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          if(_tmp_33 && myaxi_wvalid && myaxi_wready) begin
            _tmp_17 <= _tmp_17 + (_tmp_18 << 2);
          end 
          if(_tmp_33 && myaxi_wvalid && myaxi_wready && (_tmp_19 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(_tmp_33 && myaxi_wvalid && myaxi_wready && (_tmp_19 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_35 <= 1;
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
      _tmp_39 <= 0;
      _tmp_41 <= 0;
      _tmp_40 <= 0;
      __tmp_fsm_2_cond_4_0_1 <= 0;
      _tmp_43 <= 0;
      _tmp_42 <= 0;
      _tmp_48 <= 0;
      __tmp_fsm_2_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_0_1) begin
            _tmp_43 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_1_1) begin
            _tmp_48 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_comp == 13) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_39 <= (_tmp_37 >> 2) << 2;
          _tmp_41 <= _tmp_38;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_41 <= 256) && ((_tmp_39 & 4095) + (_tmp_41 << 2) >= 4096)) begin
            _tmp_40 <= 4096 - (_tmp_39 & 4095) >> 2;
            _tmp_41 <= _tmp_41 - (4096 - (_tmp_39 & 4095) >> 2);
          end else if(_tmp_41 <= 256) begin
            _tmp_40 <= _tmp_41;
            _tmp_41 <= 0;
          end else if((_tmp_39 & 4095) + 1024 >= 4096) begin
            _tmp_40 <= 4096 - (_tmp_39 & 4095) >> 2;
            _tmp_41 <= _tmp_41 - (4096 - (_tmp_39 & 4095) >> 2);
          end else begin
            _tmp_40 <= 256;
            _tmp_41 <= _tmp_41 - 256;
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
            _tmp_42 <= myaxi_rdata;
            _tmp_43 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_39 <= _tmp_39 + (_tmp_40 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_41 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_41 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_48 <= 1;
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
      _tmp_54 <= 0;
      _tmp_56 <= 0;
      _tmp_55 <= 0;
      _tmp_72 <= 0;
      __tmp_fsm_3_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_0_1) begin
            _tmp_72 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_comp == 38) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_54 <= (_tmp_52 >> 2) << 2;
          _tmp_56 <= _tmp_53;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_56 <= 256) && ((_tmp_54 & 4095) + (_tmp_56 << 2) >= 4096)) begin
            _tmp_55 <= 4096 - (_tmp_54 & 4095) >> 2;
            _tmp_56 <= _tmp_56 - (4096 - (_tmp_54 & 4095) >> 2);
          end else if(_tmp_56 <= 256) begin
            _tmp_55 <= _tmp_56;
            _tmp_56 <= 0;
          end else if((_tmp_54 & 4095) + 1024 >= 4096) begin
            _tmp_55 <= 4096 - (_tmp_54 & 4095) >> 2;
            _tmp_56 <= _tmp_56 - (4096 - (_tmp_54 & 4095) >> 2);
          end else begin
            _tmp_55 <= 256;
            _tmp_56 <= _tmp_56 - 256;
          end
          _tmp_fsm_3 <= _tmp_fsm_3_3;
        end
        _tmp_fsm_3_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_3 <= _tmp_fsm_3_4;
          end 
        end
        _tmp_fsm_3_4: begin
          if(_tmp_70 && myaxi_wvalid && myaxi_wready) begin
            _tmp_54 <= _tmp_54 + (_tmp_55 << 2);
          end 
          if(_tmp_70 && myaxi_wvalid && myaxi_wready && (_tmp_56 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(_tmp_70 && myaxi_wvalid && myaxi_wready && (_tmp_56 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_72 <= 1;
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
