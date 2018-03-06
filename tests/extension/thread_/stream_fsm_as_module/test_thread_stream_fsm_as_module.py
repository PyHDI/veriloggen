from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_fsm_as_module

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

  reg [32-1:0] _mystream_fsm;
  localparam _mystream_fsm_init = 0;
  reg _mystream_start;
  reg _mystream_busy;
  reg [16-1:0] _mystream_a_fsm_sel;
  reg _mystream_a_idle;
  reg [16-1:0] _mystream_b_fsm_sel;
  reg _mystream_b_idle;
  reg [16-1:0] _mystream_c_fsm_sel;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_0;
  reg signed [32-1:0] _th_comp_offset_1;
  reg [10-1:0] req_local_addr_0;
  reg [32-1:0] req_global_addr_1;
  reg [33-1:0] req_size_2;
  reg [10-1:0] req_local_stride_3;
  reg set_req_4;
  reg [32-1:0] _d1_th_comp;
  reg _th_comp_cond_2_0_1;
  reg fsm_start_5;
  reg _th_comp_cond_3_1_1;
  reg [32-1:0] _fsm_dma_read_0;
  localparam _fsm_dma_read_0_init = 0;
  reg [32-1:0] _global_addr_6;
  reg [33-1:0] _size_7;
  reg [33-1:0] _rest_size_8;
  reg [32-1:0] _wdata_9;
  reg _wvalid_10;
  reg [34-1:0] _tmp_11;
  reg _tmp_12;
  wire [32-1:0] __variable_data_13;
  wire __variable_valid_13;
  wire __variable_ready_13;
  assign __variable_ready_13 = (_tmp_11 > 0) && !_tmp_12;
  reg _ram_a_cond_0_1;
  reg [9-1:0] _tmp_14;
  reg _myaxi_cond_0_1;
  reg [32-1:0] _d1__fsm_dma_read_0;
  reg __fsm_dma_read_0_cond_4_0_1;
  reg fsm_done_15;
  reg __fsm_dma_read_0_cond_5_1_1;
  reg [10-1:0] req_local_addr_16;
  reg [32-1:0] req_global_addr_17;
  reg [33-1:0] req_size_18;
  reg [10-1:0] req_local_stride_19;
  reg set_req_20;
  reg _th_comp_cond_6_2_1;
  reg fsm_start_21;
  reg _th_comp_cond_7_3_1;
  reg [32-1:0] _fsm_dma_read_1;
  localparam _fsm_dma_read_1_init = 0;
  reg [32-1:0] _global_addr_22;
  reg [33-1:0] _size_23;
  reg [33-1:0] _rest_size_24;
  reg [32-1:0] _wdata_25;
  reg _wvalid_26;
  reg [34-1:0] _tmp_27;
  reg _tmp_28;
  wire [32-1:0] __variable_data_29;
  wire __variable_valid_29;
  wire __variable_ready_29;
  assign __variable_ready_29 = (_tmp_27 > 0) && !_tmp_28;
  reg _ram_b_cond_0_1;
  reg [9-1:0] _tmp_30;
  reg _myaxi_cond_1_1;
  assign myaxi_rready = (_fsm_dma_read_0 == 4) || (_fsm_dma_read_1 == 4);
  reg [32-1:0] _d1__fsm_dma_read_1;
  reg __fsm_dma_read_1_cond_4_0_1;
  reg fsm_done_31;
  reg __fsm_dma_read_1_cond_5_1_1;
  reg signed [32-1:0] _th_comp_size_2;
  reg signed [32-1:0] _th_comp_offset_3;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  reg signed [32-1:0] _plus_data_2;
  wire signed [32-1:0] mystream_c_data;
  assign mystream_c_data = _plus_data_2;
  reg [32-1:0] _mystream_a_fsm_1;
  localparam _mystream_a_fsm_1_init = 0;
  reg [10-1:0] _mystream_a_offset_1;
  reg [11-1:0] _mystream_a_size_1;
  reg [10-1:0] _mystream_a_stride_1;
  reg [11-1:0] _mystream_a_count_1;
  reg [10-1:0] _mystream_a_raddr_1;
  reg _mystream_a_renable_1;
  reg _tmp_32;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _d1__mystream_a_fsm_1;
  reg __mystream_a_fsm_1_cond_1_0_1;
  reg __mystream_a_fsm_1_cond_2_1_1;
  reg [32-1:0] _mystream_b_fsm_2;
  localparam _mystream_b_fsm_2_init = 0;
  reg [10-1:0] _mystream_b_offset_2;
  reg [11-1:0] _mystream_b_size_2;
  reg [10-1:0] _mystream_b_stride_2;
  reg [11-1:0] _mystream_b_count_2;
  reg [10-1:0] _mystream_b_raddr_2;
  reg _mystream_b_renable_2;
  reg _tmp_33;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_b_data = __variable_wdata_1;
  reg [32-1:0] _d1__mystream_b_fsm_2;
  reg __mystream_b_fsm_2_cond_1_0_1;
  reg __mystream_b_fsm_2_cond_2_1_1;
  reg [32-1:0] _mystream_c_fsm_3;
  localparam _mystream_c_fsm_3_init = 0;
  reg [10-1:0] _mystream_c_offset_3;
  reg [11-1:0] _mystream_c_size_3;
  reg [10-1:0] _mystream_c_stride_3;
  reg [11-1:0] _mystream_c_count_3;
  reg [10-1:0] _mystream_c_waddr_3;
  reg _mystream_c_wenable_3;
  reg signed [32-1:0] _mystream_c_wdata_3;
  reg _ram_c_cond_0_1;
  reg [32-1:0] _d1__mystream_c_fsm_3;
  reg __mystream_c_fsm_3_cond_6_0_1;
  reg __mystream_c_fsm_3_cond_7_1_1;
  reg [32-1:0] _d1__mystream_fsm;
  reg __mystream_fsm_cond_0_0_1;
  wire _mystream_done;
  assign _mystream_done = _mystream_a_idle && _mystream_b_idle;
  reg [10-1:0] req_local_addr_34;
  reg [32-1:0] req_global_addr_35;
  reg [33-1:0] req_size_36;
  reg [10-1:0] req_local_stride_37;
  reg set_req_38;
  reg _th_comp_cond_16_4_1;
  reg fsm_start_39;
  reg _th_comp_cond_17_5_1;
  reg [32-1:0] _fsm_dma_write_2;
  localparam _fsm_dma_write_2_init = 0;
  reg [32-1:0] _global_addr_40;
  reg [33-1:0] _size_41;
  reg [33-1:0] _rest_size_42;
  reg _tmp_43;
  reg _tmp_44;
  wire _tmp_45;
  wire _tmp_46;
  assign _tmp_46 = 1;
  localparam _tmp_47 = 1;
  wire [_tmp_47-1:0] _tmp_48;
  assign _tmp_48 = (_tmp_45 || !_tmp_43) && (_tmp_46 || !_tmp_44);
  reg [_tmp_47-1:0] __tmp_48_1;
  wire signed [32-1:0] _tmp_49;
  reg signed [32-1:0] __tmp_49_1;
  assign _tmp_49 = (__tmp_48_1)? ram_c_0_rdata : __tmp_49_1;
  reg _tmp_50;
  reg _tmp_51;
  reg _tmp_52;
  reg _tmp_53;
  reg [34-1:0] _tmp_54;
  reg [9-1:0] _tmp_55;
  reg _myaxi_cond_2_1;
  reg _tmp_56;
  wire [32-1:0] __variable_data_57;
  wire __variable_valid_57;
  wire __variable_ready_57;
  assign __variable_ready_57 = (_fsm_dma_write_2 == 4) && ((_tmp_55 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg fsm_done_58;
  reg [32-1:0] _d1__fsm_dma_write_2;
  reg __fsm_dma_write_2_cond_5_0_1;
  reg set_req_59;
  reg _th_comp_cond_21_6_1;
  reg fsm_start_60;
  reg _th_comp_cond_22_7_1;
  reg set_req_61;
  reg _th_comp_cond_25_8_1;
  reg fsm_start_62;
  reg _th_comp_cond_26_9_1;
  reg signed [32-1:0] _th_comp_size_4;
  reg signed [32-1:0] _th_comp_offset_5;
  reg signed [32-1:0] _th_comp_sum_6;
  reg signed [32-1:0] _th_comp_i_7;
  reg _tmp_63;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_4_1;
  reg _ram_a_cond_4_2;
  reg signed [32-1:0] _tmp_64;
  reg signed [32-1:0] _th_comp_a_8;
  reg _tmp_65;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_4_1;
  reg _ram_b_cond_4_2;
  reg signed [32-1:0] _tmp_66;
  reg signed [32-1:0] _th_comp_b_9;
  reg _ram_c_cond_1_1;
  reg set_req_67;
  reg _th_comp_cond_40_10_1;
  reg fsm_start_68;
  reg _th_comp_cond_41_11_1;
  reg signed [32-1:0] _th_comp_size_10;
  reg signed [32-1:0] _th_comp_offset_stream_11;
  reg signed [32-1:0] _th_comp_offset_seq_12;
  reg signed [32-1:0] _th_comp_all_ok_13;
  reg signed [32-1:0] _th_comp_i_14;
  reg _tmp_69;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_70;
  reg signed [32-1:0] _th_comp_st_15;
  reg _tmp_71;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_72;
  reg signed [32-1:0] _th_comp_sq_16;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_14 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_30 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_55 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_56 <= 0;
      _myaxi_cond_3_1 <= 0;
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
        _tmp_56 <= 0;
      end 
      if((_fsm_dma_read_0 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_14 == 0))) begin
        myaxi_araddr <= _global_addr_6;
        myaxi_arlen <= _size_7 - 1;
        myaxi_arvalid <= 1;
        _tmp_14 <= _size_7;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_14 > 0)) begin
        _tmp_14 <= _tmp_14 - 1;
      end 
      if((_fsm_dma_read_1 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_30 == 0))) begin
        myaxi_araddr <= _global_addr_22;
        myaxi_arlen <= _size_23 - 1;
        myaxi_arvalid <= 1;
        _tmp_30 <= _size_23;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_30 > 0)) begin
        _tmp_30 <= _tmp_30 - 1;
      end 
      if((_fsm_dma_write_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_55 == 0))) begin
        myaxi_awaddr <= _global_addr_40;
        myaxi_awlen <= _size_41 - 1;
        myaxi_awvalid <= 1;
        _tmp_55 <= _size_41;
      end 
      if((_fsm_dma_write_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_55 == 0)) && (_size_41 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_57 && ((_fsm_dma_write_2 == 4) && ((_tmp_55 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_55 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_55 > 0))) begin
        myaxi_wdata <= __variable_data_57;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_55 <= _tmp_55 - 1;
      end 
      if(__variable_valid_57 && ((_fsm_dma_write_2 == 4) && ((_tmp_55 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_55 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_55 > 0)) && (_tmp_55 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_56 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_56 <= _tmp_56;
      end 
    end
  end

  assign __variable_data_13 = _wdata_9;
  assign __variable_valid_13 = _wvalid_10;
  assign __variable_data_29 = _wdata_25;
  assign __variable_valid_29 = _wvalid_26;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_11 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_12 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_32 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
      _ram_a_cond_3_1 <= 0;
      _tmp_63 <= 0;
      _ram_a_cond_4_1 <= 0;
      _ram_a_cond_4_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_32 <= 0;
      end 
      if(_ram_a_cond_4_2) begin
        _tmp_63 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_12 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_32 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if(_ram_a_cond_3_1) begin
        _tmp_63 <= 1;
      end 
      _ram_a_cond_4_2 <= _ram_a_cond_4_1;
      if((_fsm_dma_read_0 == 1) && (_tmp_11 == 0)) begin
        ram_a_0_addr <= req_local_addr_0 - req_local_stride_3;
        _tmp_11 <= req_size_2;
      end 
      if(__variable_valid_13 && ((_tmp_11 > 0) && !_tmp_12) && (_tmp_11 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + req_local_stride_3;
        ram_a_0_wdata <= __variable_data_13;
        ram_a_0_wenable <= 1;
        _tmp_11 <= _tmp_11 - 1;
      end 
      if(__variable_valid_13 && ((_tmp_11 > 0) && !_tmp_12) && (_tmp_11 == 1)) begin
        _tmp_12 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      if(_mystream_a_renable_1) begin
        ram_a_0_addr <= _mystream_a_raddr_1;
      end 
      _ram_a_cond_1_1 <= _mystream_a_renable_1;
      _ram_a_cond_2_1 <= _mystream_a_renable_1;
      if(th_comp == 33) begin
        ram_a_0_addr <= _th_comp_i_7 + _th_comp_offset_5;
      end 
      _ram_a_cond_3_1 <= th_comp == 33;
      _ram_a_cond_4_1 <= th_comp == 33;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_27 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_28 <= 0;
      _ram_b_cond_0_1 <= 0;
      _ram_b_cond_1_1 <= 0;
      _tmp_33 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
      _ram_b_cond_3_1 <= 0;
      _tmp_65 <= 0;
      _ram_b_cond_4_1 <= 0;
      _ram_b_cond_4_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_33 <= 0;
      end 
      if(_ram_b_cond_4_2) begin
        _tmp_65 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_28 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_33 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if(_ram_b_cond_3_1) begin
        _tmp_65 <= 1;
      end 
      _ram_b_cond_4_2 <= _ram_b_cond_4_1;
      if((_fsm_dma_read_1 == 1) && (_tmp_27 == 0)) begin
        ram_b_0_addr <= req_local_addr_16 - req_local_stride_19;
        _tmp_27 <= req_size_18;
      end 
      if(__variable_valid_29 && ((_tmp_27 > 0) && !_tmp_28) && (_tmp_27 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + req_local_stride_19;
        ram_b_0_wdata <= __variable_data_29;
        ram_b_0_wenable <= 1;
        _tmp_27 <= _tmp_27 - 1;
      end 
      if(__variable_valid_29 && ((_tmp_27 > 0) && !_tmp_28) && (_tmp_27 == 1)) begin
        _tmp_28 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      if(_mystream_b_renable_2) begin
        ram_b_0_addr <= _mystream_b_raddr_2;
      end 
      _ram_b_cond_1_1 <= _mystream_b_renable_2;
      _ram_b_cond_2_1 <= _mystream_b_renable_2;
      if(th_comp == 35) begin
        ram_b_0_addr <= _th_comp_i_7 + _th_comp_offset_5;
      end 
      _ram_b_cond_3_1 <= th_comp == 35;
      _ram_b_cond_4_1 <= th_comp == 35;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_48_1 <= 0;
      __tmp_49_1 <= 0;
      _tmp_53 <= 0;
      _tmp_43 <= 0;
      _tmp_44 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_50 <= 0;
      _tmp_54 <= 0;
      _ram_c_cond_1_1 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_69 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_71 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_69 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_71 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_69 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_71 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if(_mystream_c_wenable_3) begin
        ram_c_0_addr <= _mystream_c_waddr_3;
        ram_c_0_wdata <= _mystream_c_wdata_3;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= _mystream_c_wenable_3;
      __tmp_48_1 <= _tmp_48;
      __tmp_49_1 <= _tmp_49;
      if((_tmp_45 || !_tmp_43) && (_tmp_46 || !_tmp_44) && _tmp_51) begin
        _tmp_53 <= 0;
        _tmp_43 <= 0;
        _tmp_44 <= 0;
        _tmp_51 <= 0;
      end 
      if((_tmp_45 || !_tmp_43) && (_tmp_46 || !_tmp_44) && _tmp_50) begin
        _tmp_43 <= 1;
        _tmp_44 <= 1;
        _tmp_53 <= _tmp_52;
        _tmp_52 <= 0;
        _tmp_50 <= 0;
        _tmp_51 <= 1;
      end 
      if((_fsm_dma_write_2 == 1) && (_tmp_54 == 0) && !_tmp_52 && !_tmp_53) begin
        ram_c_0_addr <= req_local_addr_34;
        _tmp_54 <= req_size_36 - 1;
        _tmp_50 <= 1;
        _tmp_52 <= req_size_36 == 1;
      end 
      if((_tmp_45 || !_tmp_43) && (_tmp_46 || !_tmp_44) && (_tmp_54 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + req_local_stride_37;
        _tmp_54 <= _tmp_54 - 1;
        _tmp_50 <= 1;
        _tmp_52 <= 0;
      end 
      if((_tmp_45 || !_tmp_43) && (_tmp_46 || !_tmp_44) && (_tmp_54 == 1)) begin
        _tmp_52 <= 1;
      end 
      if(th_comp == 38) begin
        ram_c_0_addr <= _th_comp_i_7 + _th_comp_offset_5;
        ram_c_0_wdata <= _th_comp_sum_6;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_comp == 38;
      if(th_comp == 48) begin
        ram_c_0_addr <= _th_comp_i_14 + _th_comp_offset_stream_11;
      end 
      _ram_c_cond_2_1 <= th_comp == 48;
      _ram_c_cond_3_1 <= th_comp == 48;
      if(th_comp == 50) begin
        ram_c_0_addr <= _th_comp_i_14 + _th_comp_offset_seq_12;
      end 
      _ram_c_cond_4_1 <= th_comp == 50;
      _ram_c_cond_5_1 <= th_comp == 50;
    end
  end

  assign __variable_data_57 = _tmp_49;
  assign __variable_valid_57 = _tmp_43;
  assign _tmp_45 = 1 && __variable_ready_57;

  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_2 <= 0;
      _mystream_a_fsm_sel <= 0;
      _mystream_a_idle <= 1;
      __variable_wdata_0 <= 0;
      _mystream_b_fsm_sel <= 0;
      _mystream_b_idle <= 1;
      __variable_wdata_1 <= 0;
      _mystream_c_fsm_sel <= 0;
    end else begin
      _plus_data_2 <= mystream_a_data + mystream_b_data;
      if(th_comp == 11) begin
        _mystream_a_fsm_sel <= 1;
      end 
      if(_mystream_start) begin
        _mystream_a_idle <= 0;
      end 
      if(_tmp_32) begin
        __variable_wdata_0 <= ram_a_0_rdata;
      end 
      if((_mystream_a_fsm_1 == 1) && (_mystream_a_count_1 == 1)) begin
        _mystream_a_idle <= 1;
      end 
      if((_mystream_a_fsm_1 == 2) && (_mystream_a_count_1 == 1)) begin
        _mystream_a_idle <= 1;
      end 
      if(th_comp == 12) begin
        _mystream_b_fsm_sel <= 2;
      end 
      if(_mystream_start) begin
        _mystream_b_idle <= 0;
      end 
      if(_tmp_33) begin
        __variable_wdata_1 <= ram_b_0_rdata;
      end 
      if((_mystream_b_fsm_2 == 1) && (_mystream_b_count_2 == 1)) begin
        _mystream_b_idle <= 1;
      end 
      if((_mystream_b_fsm_2 == 2) && (_mystream_b_count_2 == 1)) begin
        _mystream_b_idle <= 1;
      end 
      if(th_comp == 13) begin
        _mystream_c_fsm_sel <= 3;
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
  localparam _mystream_fsm_8 = 8;
  wire [32-1:0] __mystream_fsm_out_73;

  always @(*) begin
    _mystream_fsm = __mystream_fsm_out_73;
  end

  wire [32-1:0] __d1__mystream_fsm_out_74;

  always @(*) begin
    _d1__mystream_fsm = __d1__mystream_fsm_out_74;
  end

  wire __mystream_fsm__mystream_start_75;

  always @(*) begin
    _mystream_start = __mystream_fsm__mystream_start_75;
  end

  wire __mystream_fsm__mystream_busy_76;

  always @(*) begin
    _mystream_busy = __mystream_fsm__mystream_busy_76;
  end

  localparam __mystream_fsm_th_comp_init = th_comp_init;

  sub__mystream_fsm
  #(
    .th_comp_init(__mystream_fsm_th_comp_init)
  )
  inst_sub__mystream_fsm
  (
    .CLK(CLK),
    .RST(RST),
    ._mystream_fsm(__mystream_fsm_out_73),
    ._d1__mystream_fsm(__d1__mystream_fsm_out_74),
    .i_th_comp(th_comp),
    .i__mystream_done(_mystream_done),
    ._mystream_start(__mystream_fsm__mystream_start_75),
    ._mystream_busy(__mystream_fsm__mystream_busy_76)
  );

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
  localparam th_comp_55 = 55;
  localparam th_comp_56 = 56;
  localparam th_comp_57 = 57;
  localparam th_comp_58 = 58;
  localparam th_comp_59 = 59;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _d1_th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_offset_1 <= 0;
      set_req_4 <= 0;
      _th_comp_cond_2_0_1 <= 0;
      fsm_start_5 <= 0;
      _th_comp_cond_3_1_1 <= 0;
      set_req_20 <= 0;
      _th_comp_cond_6_2_1 <= 0;
      fsm_start_21 <= 0;
      _th_comp_cond_7_3_1 <= 0;
      _th_comp_size_2 <= 0;
      _th_comp_offset_3 <= 0;
      set_req_38 <= 0;
      _th_comp_cond_16_4_1 <= 0;
      fsm_start_39 <= 0;
      _th_comp_cond_17_5_1 <= 0;
      set_req_59 <= 0;
      _th_comp_cond_21_6_1 <= 0;
      fsm_start_60 <= 0;
      _th_comp_cond_22_7_1 <= 0;
      set_req_61 <= 0;
      _th_comp_cond_25_8_1 <= 0;
      fsm_start_62 <= 0;
      _th_comp_cond_26_9_1 <= 0;
      _th_comp_size_4 <= 0;
      _th_comp_offset_5 <= 0;
      _th_comp_sum_6 <= 0;
      _th_comp_i_7 <= 0;
      _tmp_64 <= 0;
      _th_comp_a_8 <= 0;
      _tmp_66 <= 0;
      _th_comp_b_9 <= 0;
      set_req_67 <= 0;
      _th_comp_cond_40_10_1 <= 0;
      fsm_start_68 <= 0;
      _th_comp_cond_41_11_1 <= 0;
      _th_comp_size_10 <= 0;
      _th_comp_offset_stream_11 <= 0;
      _th_comp_offset_seq_12 <= 0;
      _th_comp_all_ok_13 <= 0;
      _th_comp_i_14 <= 0;
      _tmp_70 <= 0;
      _th_comp_st_15 <= 0;
      _tmp_72 <= 0;
      _th_comp_sq_16 <= 0;
    end else begin
      _d1_th_comp <= th_comp;
      case(_d1_th_comp)
        th_comp_2: begin
          if(_th_comp_cond_2_0_1) begin
            set_req_4 <= 0;
          end 
        end
        th_comp_3: begin
          if(_th_comp_cond_3_1_1) begin
            fsm_start_5 <= 0;
          end 
        end
        th_comp_6: begin
          if(_th_comp_cond_6_2_1) begin
            set_req_20 <= 0;
          end 
        end
        th_comp_7: begin
          if(_th_comp_cond_7_3_1) begin
            fsm_start_21 <= 0;
          end 
        end
        th_comp_16: begin
          if(_th_comp_cond_16_4_1) begin
            set_req_38 <= 0;
          end 
        end
        th_comp_17: begin
          if(_th_comp_cond_17_5_1) begin
            fsm_start_39 <= 0;
          end 
        end
        th_comp_21: begin
          if(_th_comp_cond_21_6_1) begin
            set_req_59 <= 0;
          end 
        end
        th_comp_22: begin
          if(_th_comp_cond_22_7_1) begin
            fsm_start_60 <= 0;
          end 
        end
        th_comp_25: begin
          if(_th_comp_cond_25_8_1) begin
            set_req_61 <= 0;
          end 
        end
        th_comp_26: begin
          if(_th_comp_cond_26_9_1) begin
            fsm_start_62 <= 0;
          end 
        end
        th_comp_40: begin
          if(_th_comp_cond_40_10_1) begin
            set_req_67 <= 0;
          end 
        end
        th_comp_41: begin
          if(_th_comp_cond_41_11_1) begin
            fsm_start_68 <= 0;
          end 
        end
      endcase
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
          set_req_4 <= 1;
          _th_comp_cond_2_0_1 <= 1;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          fsm_start_5 <= 1;
          _th_comp_cond_3_1_1 <= 1;
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          if(fsm_done_15) begin
            th_comp <= th_comp_6;
          end 
        end
        th_comp_6: begin
          set_req_20 <= 1;
          _th_comp_cond_6_2_1 <= 1;
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          fsm_start_21 <= 1;
          _th_comp_cond_7_3_1 <= 1;
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          if(fsm_done_31) begin
            th_comp <= th_comp_10;
          end 
        end
        th_comp_10: begin
          _th_comp_size_2 <= _th_comp_size_0;
          _th_comp_offset_3 <= _th_comp_offset_1;
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          set_req_38 <= 1;
          _th_comp_cond_16_4_1 <= 1;
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          fsm_start_39 <= 1;
          _th_comp_cond_17_5_1 <= 1;
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          th_comp <= th_comp_19;
        end
        th_comp_19: begin
          if(fsm_done_58) begin
            th_comp <= th_comp_20;
          end 
        end
        th_comp_20: begin
          _th_comp_offset_1 <= _th_comp_size_0;
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          set_req_59 <= 1;
          _th_comp_cond_21_6_1 <= 1;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          fsm_start_60 <= 1;
          _th_comp_cond_22_7_1 <= 1;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          if(fsm_done_15) begin
            th_comp <= th_comp_25;
          end 
        end
        th_comp_25: begin
          set_req_61 <= 1;
          _th_comp_cond_25_8_1 <= 1;
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          fsm_start_62 <= 1;
          _th_comp_cond_26_9_1 <= 1;
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          if(fsm_done_31) begin
            th_comp <= th_comp_29;
          end 
        end
        th_comp_29: begin
          _th_comp_size_4 <= _th_comp_size_0;
          _th_comp_offset_5 <= _th_comp_offset_1;
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          _th_comp_sum_6 <= 0;
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          _th_comp_i_7 <= 0;
          th_comp <= th_comp_32;
        end
        th_comp_32: begin
          if(_th_comp_i_7 < _th_comp_size_4) begin
            th_comp <= th_comp_33;
          end else begin
            th_comp <= th_comp_40;
          end
        end
        th_comp_33: begin
          if(_tmp_63) begin
            _tmp_64 <= ram_a_0_rdata;
          end 
          if(_tmp_63) begin
            th_comp <= th_comp_34;
          end 
        end
        th_comp_34: begin
          _th_comp_a_8 <= _tmp_64;
          th_comp <= th_comp_35;
        end
        th_comp_35: begin
          if(_tmp_65) begin
            _tmp_66 <= ram_b_0_rdata;
          end 
          if(_tmp_65) begin
            th_comp <= th_comp_36;
          end 
        end
        th_comp_36: begin
          _th_comp_b_9 <= _tmp_66;
          th_comp <= th_comp_37;
        end
        th_comp_37: begin
          _th_comp_sum_6 <= _th_comp_a_8 + _th_comp_b_9;
          th_comp <= th_comp_38;
        end
        th_comp_38: begin
          th_comp <= th_comp_39;
        end
        th_comp_39: begin
          _th_comp_i_7 <= _th_comp_i_7 + 1;
          th_comp <= th_comp_32;
        end
        th_comp_40: begin
          set_req_67 <= 1;
          _th_comp_cond_40_10_1 <= 1;
          th_comp <= th_comp_41;
        end
        th_comp_41: begin
          fsm_start_68 <= 1;
          _th_comp_cond_41_11_1 <= 1;
          th_comp <= th_comp_42;
        end
        th_comp_42: begin
          th_comp <= th_comp_43;
        end
        th_comp_43: begin
          if(fsm_done_58) begin
            th_comp <= th_comp_44;
          end 
        end
        th_comp_44: begin
          _th_comp_size_10 <= _th_comp_size_0;
          _th_comp_offset_stream_11 <= 0;
          _th_comp_offset_seq_12 <= _th_comp_offset_1;
          th_comp <= th_comp_45;
        end
        th_comp_45: begin
          _th_comp_all_ok_13 <= 1;
          th_comp <= th_comp_46;
        end
        th_comp_46: begin
          _th_comp_i_14 <= 0;
          th_comp <= th_comp_47;
        end
        th_comp_47: begin
          if(_th_comp_i_14 < _th_comp_size_10) begin
            th_comp <= th_comp_48;
          end else begin
            th_comp <= th_comp_55;
          end
        end
        th_comp_48: begin
          if(_tmp_69) begin
            _tmp_70 <= ram_c_0_rdata;
          end 
          if(_tmp_69) begin
            th_comp <= th_comp_49;
          end 
        end
        th_comp_49: begin
          _th_comp_st_15 <= _tmp_70;
          th_comp <= th_comp_50;
        end
        th_comp_50: begin
          if(_tmp_71) begin
            _tmp_72 <= ram_c_0_rdata;
          end 
          if(_tmp_71) begin
            th_comp <= th_comp_51;
          end 
        end
        th_comp_51: begin
          _th_comp_sq_16 <= _tmp_72;
          th_comp <= th_comp_52;
        end
        th_comp_52: begin
          if(_th_comp_st_15 !== _th_comp_sq_16) begin
            th_comp <= th_comp_53;
          end else begin
            th_comp <= th_comp_54;
          end
        end
        th_comp_53: begin
          _th_comp_all_ok_13 <= 0;
          th_comp <= th_comp_54;
        end
        th_comp_54: begin
          _th_comp_i_14 <= _th_comp_i_14 + 1;
          th_comp <= th_comp_47;
        end
        th_comp_55: begin
          if(_th_comp_all_ok_13) begin
            th_comp <= th_comp_56;
          end else begin
            th_comp <= th_comp_58;
          end
        end
        th_comp_56: begin
          $display("OK");
          th_comp <= th_comp_57;
        end
        th_comp_57: begin
          th_comp <= th_comp_59;
        end
        th_comp_58: begin
          $display("NG");
          th_comp <= th_comp_59;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      req_local_addr_0 <= 0;
      req_global_addr_1 <= 0;
      req_size_2 <= 0;
      req_local_stride_3 <= 1;
    end else begin
      if(set_req_4) begin
        req_local_addr_0 <= _th_comp_offset_1;
        req_global_addr_1 <= 0;
        req_size_2 <= _th_comp_size_0;
        req_local_stride_3 <= 1;
      end 
      if(set_req_59) begin
        req_local_addr_0 <= _th_comp_offset_1;
        req_global_addr_1 <= 0;
        req_size_2 <= _th_comp_size_0;
        req_local_stride_3 <= 1;
      end 
    end
  end

  localparam _fsm_dma_read_0_1 = 1;
  localparam _fsm_dma_read_0_2 = 2;
  localparam _fsm_dma_read_0_3 = 3;
  localparam _fsm_dma_read_0_4 = 4;
  localparam _fsm_dma_read_0_5 = 5;
  localparam _fsm_dma_read_0_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _fsm_dma_read_0 <= _fsm_dma_read_0_init;
      _d1__fsm_dma_read_0 <= _fsm_dma_read_0_init;
      _global_addr_6 <= 0;
      _rest_size_8 <= 0;
      _size_7 <= 0;
      __fsm_dma_read_0_cond_4_0_1 <= 0;
      _wvalid_10 <= 0;
      _wdata_9 <= 0;
      fsm_done_15 <= 0;
      __fsm_dma_read_0_cond_5_1_1 <= 0;
    end else begin
      _d1__fsm_dma_read_0 <= _fsm_dma_read_0;
      case(_d1__fsm_dma_read_0)
        _fsm_dma_read_0_4: begin
          if(__fsm_dma_read_0_cond_4_0_1) begin
            _wvalid_10 <= 0;
          end 
        end
        _fsm_dma_read_0_5: begin
          if(__fsm_dma_read_0_cond_5_1_1) begin
            fsm_done_15 <= 0;
          end 
        end
      endcase
      case(_fsm_dma_read_0)
        _fsm_dma_read_0_init: begin
          if(fsm_start_5) begin
            _fsm_dma_read_0 <= _fsm_dma_read_0_1;
          end 
          if(fsm_start_60) begin
            _fsm_dma_read_0 <= _fsm_dma_read_0_1;
          end 
        end
        _fsm_dma_read_0_1: begin
          _global_addr_6 <= (req_global_addr_1 >> 2) << 2;
          _rest_size_8 <= req_size_2;
          _fsm_dma_read_0 <= _fsm_dma_read_0_2;
        end
        _fsm_dma_read_0_2: begin
          if((_rest_size_8 <= 256) && ((_global_addr_6 & 4095) + (_rest_size_8 << 2) >= 4096)) begin
            _size_7 <= 4096 - (_global_addr_6 & 4095) >> 2;
            _rest_size_8 <= _rest_size_8 - (4096 - (_global_addr_6 & 4095) >> 2);
          end else if(_rest_size_8 <= 256) begin
            _size_7 <= _rest_size_8;
            _rest_size_8 <= 0;
          end else if((_global_addr_6 & 4095) + 1024 >= 4096) begin
            _size_7 <= 4096 - (_global_addr_6 & 4095) >> 2;
            _rest_size_8 <= _rest_size_8 - (4096 - (_global_addr_6 & 4095) >> 2);
          end else begin
            _size_7 <= 256;
            _rest_size_8 <= _rest_size_8 - 256;
          end
          _fsm_dma_read_0 <= _fsm_dma_read_0_3;
        end
        _fsm_dma_read_0_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _fsm_dma_read_0 <= _fsm_dma_read_0_4;
          end 
        end
        _fsm_dma_read_0_4: begin
          __fsm_dma_read_0_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _wdata_9 <= myaxi_rdata;
            _wvalid_10 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _global_addr_6 <= _global_addr_6 + (_size_7 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_rest_size_8 > 0)) begin
            _fsm_dma_read_0 <= _fsm_dma_read_0_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_rest_size_8 == 0)) begin
            _fsm_dma_read_0 <= _fsm_dma_read_0_5;
          end 
        end
        _fsm_dma_read_0_5: begin
          fsm_done_15 <= 1;
          __fsm_dma_read_0_cond_5_1_1 <= 1;
          _fsm_dma_read_0 <= _fsm_dma_read_0_6;
        end
        _fsm_dma_read_0_6: begin
          _fsm_dma_read_0 <= _fsm_dma_read_0_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      req_local_addr_16 <= 0;
      req_global_addr_17 <= 0;
      req_size_18 <= 0;
      req_local_stride_19 <= 1;
    end else begin
      if(set_req_20) begin
        req_local_addr_16 <= _th_comp_offset_1;
        req_global_addr_17 <= 512;
        req_size_18 <= _th_comp_size_0;
        req_local_stride_19 <= 1;
      end 
      if(set_req_61) begin
        req_local_addr_16 <= _th_comp_offset_1;
        req_global_addr_17 <= 512;
        req_size_18 <= _th_comp_size_0;
        req_local_stride_19 <= 1;
      end 
    end
  end

  localparam _fsm_dma_read_1_1 = 1;
  localparam _fsm_dma_read_1_2 = 2;
  localparam _fsm_dma_read_1_3 = 3;
  localparam _fsm_dma_read_1_4 = 4;
  localparam _fsm_dma_read_1_5 = 5;
  localparam _fsm_dma_read_1_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _fsm_dma_read_1 <= _fsm_dma_read_1_init;
      _d1__fsm_dma_read_1 <= _fsm_dma_read_1_init;
      _global_addr_22 <= 0;
      _rest_size_24 <= 0;
      _size_23 <= 0;
      __fsm_dma_read_1_cond_4_0_1 <= 0;
      _wvalid_26 <= 0;
      _wdata_25 <= 0;
      fsm_done_31 <= 0;
      __fsm_dma_read_1_cond_5_1_1 <= 0;
    end else begin
      _d1__fsm_dma_read_1 <= _fsm_dma_read_1;
      case(_d1__fsm_dma_read_1)
        _fsm_dma_read_1_4: begin
          if(__fsm_dma_read_1_cond_4_0_1) begin
            _wvalid_26 <= 0;
          end 
        end
        _fsm_dma_read_1_5: begin
          if(__fsm_dma_read_1_cond_5_1_1) begin
            fsm_done_31 <= 0;
          end 
        end
      endcase
      case(_fsm_dma_read_1)
        _fsm_dma_read_1_init: begin
          if(fsm_start_21) begin
            _fsm_dma_read_1 <= _fsm_dma_read_1_1;
          end 
          if(fsm_start_62) begin
            _fsm_dma_read_1 <= _fsm_dma_read_1_1;
          end 
        end
        _fsm_dma_read_1_1: begin
          _global_addr_22 <= (req_global_addr_17 >> 2) << 2;
          _rest_size_24 <= req_size_18;
          _fsm_dma_read_1 <= _fsm_dma_read_1_2;
        end
        _fsm_dma_read_1_2: begin
          if((_rest_size_24 <= 256) && ((_global_addr_22 & 4095) + (_rest_size_24 << 2) >= 4096)) begin
            _size_23 <= 4096 - (_global_addr_22 & 4095) >> 2;
            _rest_size_24 <= _rest_size_24 - (4096 - (_global_addr_22 & 4095) >> 2);
          end else if(_rest_size_24 <= 256) begin
            _size_23 <= _rest_size_24;
            _rest_size_24 <= 0;
          end else if((_global_addr_22 & 4095) + 1024 >= 4096) begin
            _size_23 <= 4096 - (_global_addr_22 & 4095) >> 2;
            _rest_size_24 <= _rest_size_24 - (4096 - (_global_addr_22 & 4095) >> 2);
          end else begin
            _size_23 <= 256;
            _rest_size_24 <= _rest_size_24 - 256;
          end
          _fsm_dma_read_1 <= _fsm_dma_read_1_3;
        end
        _fsm_dma_read_1_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _fsm_dma_read_1 <= _fsm_dma_read_1_4;
          end 
        end
        _fsm_dma_read_1_4: begin
          __fsm_dma_read_1_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _wdata_25 <= myaxi_rdata;
            _wvalid_26 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _global_addr_22 <= _global_addr_22 + (_size_23 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_rest_size_24 > 0)) begin
            _fsm_dma_read_1 <= _fsm_dma_read_1_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_rest_size_24 == 0)) begin
            _fsm_dma_read_1 <= _fsm_dma_read_1_5;
          end 
        end
        _fsm_dma_read_1_5: begin
          fsm_done_31 <= 1;
          __fsm_dma_read_1_cond_5_1_1 <= 1;
          _fsm_dma_read_1 <= _fsm_dma_read_1_6;
        end
        _fsm_dma_read_1_6: begin
          _fsm_dma_read_1 <= _fsm_dma_read_1_init;
        end
      endcase
    end
  end

  localparam _mystream_a_fsm_1_1 = 1;
  localparam _mystream_a_fsm_1_2 = 2;
  wire [32-1:0] __mystream_a_fsm_1_out_77;

  always @(*) begin
    _mystream_a_fsm_1 = __mystream_a_fsm_1_out_77;
  end

  wire [32-1:0] __d1__mystream_a_fsm_1_out_78;

  always @(*) begin
    _d1__mystream_a_fsm_1 = __d1__mystream_a_fsm_1_out_78;
  end

  wire [10-1:0] __mystream_a_fsm_1__mystream_a_offset_1_79;

  always @(*) begin
    _mystream_a_offset_1 = __mystream_a_fsm_1__mystream_a_offset_1_79;
  end

  wire [11-1:0] __mystream_a_fsm_1__mystream_a_size_1_80;

  always @(*) begin
    _mystream_a_size_1 = __mystream_a_fsm_1__mystream_a_size_1_80;
  end

  wire [10-1:0] __mystream_a_fsm_1__mystream_a_stride_1_81;

  always @(*) begin
    _mystream_a_stride_1 = __mystream_a_fsm_1__mystream_a_stride_1_81;
  end

  wire [11-1:0] __mystream_a_fsm_1__mystream_a_count_1_82;

  always @(*) begin
    _mystream_a_count_1 = __mystream_a_fsm_1__mystream_a_count_1_82;
  end

  wire [10-1:0] __mystream_a_fsm_1__mystream_a_raddr_1_83;

  always @(*) begin
    _mystream_a_raddr_1 = __mystream_a_fsm_1__mystream_a_raddr_1_83;
  end

  wire __mystream_a_fsm_1__mystream_a_renable_1_84;

  always @(*) begin
    _mystream_a_renable_1 = __mystream_a_fsm_1__mystream_a_renable_1_84;
  end

  localparam __mystream_a_fsm_1_th_comp_init = th_comp_init;

  sub__mystream_a_fsm_1
  #(
    .th_comp_init(__mystream_a_fsm_1_th_comp_init)
  )
  inst_sub__mystream_a_fsm_1
  (
    .CLK(CLK),
    .RST(RST),
    ._mystream_a_fsm_1(__mystream_a_fsm_1_out_77),
    ._d1__mystream_a_fsm_1(__d1__mystream_a_fsm_1_out_78),
    .i_th_comp(th_comp),
    .i__th_comp_offset_3(_th_comp_offset_3),
    .i__th_comp_size_2(_th_comp_size_2),
    .i__mystream_start(_mystream_start),
    .i__mystream_a_fsm_sel(_mystream_a_fsm_sel),
    .i__mystream_a_size_1(_mystream_a_size_1),
    .i__mystream_a_offset_1(_mystream_a_offset_1),
    .i__mystream_a_count_1(_mystream_a_count_1),
    .i__mystream_a_raddr_1(_mystream_a_raddr_1),
    .i__mystream_a_stride_1(_mystream_a_stride_1),
    ._mystream_a_offset_1(__mystream_a_fsm_1__mystream_a_offset_1_79),
    ._mystream_a_size_1(__mystream_a_fsm_1__mystream_a_size_1_80),
    ._mystream_a_stride_1(__mystream_a_fsm_1__mystream_a_stride_1_81),
    ._mystream_a_count_1(__mystream_a_fsm_1__mystream_a_count_1_82),
    ._mystream_a_raddr_1(__mystream_a_fsm_1__mystream_a_raddr_1_83),
    ._mystream_a_renable_1(__mystream_a_fsm_1__mystream_a_renable_1_84)
  );

  localparam _mystream_b_fsm_2_1 = 1;
  localparam _mystream_b_fsm_2_2 = 2;
  wire [32-1:0] __mystream_b_fsm_2_out_85;

  always @(*) begin
    _mystream_b_fsm_2 = __mystream_b_fsm_2_out_85;
  end

  wire [32-1:0] __d1__mystream_b_fsm_2_out_86;

  always @(*) begin
    _d1__mystream_b_fsm_2 = __d1__mystream_b_fsm_2_out_86;
  end

  wire [10-1:0] __mystream_b_fsm_2__mystream_b_offset_2_87;

  always @(*) begin
    _mystream_b_offset_2 = __mystream_b_fsm_2__mystream_b_offset_2_87;
  end

  wire [11-1:0] __mystream_b_fsm_2__mystream_b_size_2_88;

  always @(*) begin
    _mystream_b_size_2 = __mystream_b_fsm_2__mystream_b_size_2_88;
  end

  wire [10-1:0] __mystream_b_fsm_2__mystream_b_stride_2_89;

  always @(*) begin
    _mystream_b_stride_2 = __mystream_b_fsm_2__mystream_b_stride_2_89;
  end

  wire [11-1:0] __mystream_b_fsm_2__mystream_b_count_2_90;

  always @(*) begin
    _mystream_b_count_2 = __mystream_b_fsm_2__mystream_b_count_2_90;
  end

  wire [10-1:0] __mystream_b_fsm_2__mystream_b_raddr_2_91;

  always @(*) begin
    _mystream_b_raddr_2 = __mystream_b_fsm_2__mystream_b_raddr_2_91;
  end

  wire __mystream_b_fsm_2__mystream_b_renable_2_92;

  always @(*) begin
    _mystream_b_renable_2 = __mystream_b_fsm_2__mystream_b_renable_2_92;
  end

  localparam __mystream_b_fsm_2_th_comp_init = th_comp_init;

  sub__mystream_b_fsm_2
  #(
    .th_comp_init(__mystream_b_fsm_2_th_comp_init)
  )
  inst_sub__mystream_b_fsm_2
  (
    .CLK(CLK),
    .RST(RST),
    ._mystream_b_fsm_2(__mystream_b_fsm_2_out_85),
    ._d1__mystream_b_fsm_2(__d1__mystream_b_fsm_2_out_86),
    .i_th_comp(th_comp),
    .i__th_comp_offset_3(_th_comp_offset_3),
    .i__th_comp_size_2(_th_comp_size_2),
    .i__mystream_start(_mystream_start),
    .i__mystream_b_fsm_sel(_mystream_b_fsm_sel),
    .i__mystream_b_size_2(_mystream_b_size_2),
    .i__mystream_b_offset_2(_mystream_b_offset_2),
    .i__mystream_b_count_2(_mystream_b_count_2),
    .i__mystream_b_raddr_2(_mystream_b_raddr_2),
    .i__mystream_b_stride_2(_mystream_b_stride_2),
    ._mystream_b_offset_2(__mystream_b_fsm_2__mystream_b_offset_2_87),
    ._mystream_b_size_2(__mystream_b_fsm_2__mystream_b_size_2_88),
    ._mystream_b_stride_2(__mystream_b_fsm_2__mystream_b_stride_2_89),
    ._mystream_b_count_2(__mystream_b_fsm_2__mystream_b_count_2_90),
    ._mystream_b_raddr_2(__mystream_b_fsm_2__mystream_b_raddr_2_91),
    ._mystream_b_renable_2(__mystream_b_fsm_2__mystream_b_renable_2_92)
  );

  localparam _mystream_c_fsm_3_1 = 1;
  localparam _mystream_c_fsm_3_2 = 2;
  localparam _mystream_c_fsm_3_3 = 3;
  localparam _mystream_c_fsm_3_4 = 4;
  localparam _mystream_c_fsm_3_5 = 5;
  localparam _mystream_c_fsm_3_6 = 6;
  localparam _mystream_c_fsm_3_7 = 7;
  wire [32-1:0] __mystream_c_fsm_3_out_93;

  always @(*) begin
    _mystream_c_fsm_3 = __mystream_c_fsm_3_out_93;
  end

  wire [32-1:0] __d1__mystream_c_fsm_3_out_94;

  always @(*) begin
    _d1__mystream_c_fsm_3 = __d1__mystream_c_fsm_3_out_94;
  end

  wire [10-1:0] __mystream_c_fsm_3__mystream_c_offset_3_95;

  always @(*) begin
    _mystream_c_offset_3 = __mystream_c_fsm_3__mystream_c_offset_3_95;
  end

  wire [11-1:0] __mystream_c_fsm_3__mystream_c_size_3_96;

  always @(*) begin
    _mystream_c_size_3 = __mystream_c_fsm_3__mystream_c_size_3_96;
  end

  wire [10-1:0] __mystream_c_fsm_3__mystream_c_stride_3_97;

  always @(*) begin
    _mystream_c_stride_3 = __mystream_c_fsm_3__mystream_c_stride_3_97;
  end

  wire [11-1:0] __mystream_c_fsm_3__mystream_c_count_3_98;

  always @(*) begin
    _mystream_c_count_3 = __mystream_c_fsm_3__mystream_c_count_3_98;
  end

  wire [10-1:0] __mystream_c_fsm_3__mystream_c_waddr_3_99;

  always @(*) begin
    _mystream_c_waddr_3 = __mystream_c_fsm_3__mystream_c_waddr_3_99;
  end

  wire signed [32-1:0] __mystream_c_fsm_3__mystream_c_wdata_3_100;

  always @(*) begin
    _mystream_c_wdata_3 = __mystream_c_fsm_3__mystream_c_wdata_3_100;
  end

  wire __mystream_c_fsm_3__mystream_c_wenable_3_101;

  always @(*) begin
    _mystream_c_wenable_3 = __mystream_c_fsm_3__mystream_c_wenable_3_101;
  end

  localparam __mystream_c_fsm_3_th_comp_init = th_comp_init;

  sub__mystream_c_fsm_3
  #(
    .th_comp_init(__mystream_c_fsm_3_th_comp_init)
  )
  inst_sub__mystream_c_fsm_3
  (
    .CLK(CLK),
    .RST(RST),
    ._mystream_c_fsm_3(__mystream_c_fsm_3_out_93),
    ._d1__mystream_c_fsm_3(__d1__mystream_c_fsm_3_out_94),
    .i_th_comp(th_comp),
    .i__th_comp_offset_3(_th_comp_offset_3),
    .i__th_comp_size_2(_th_comp_size_2),
    .i__mystream_start(_mystream_start),
    .i__mystream_c_fsm_sel(_mystream_c_fsm_sel),
    .i__mystream_c_size_3(_mystream_c_size_3),
    .i__mystream_c_offset_3(_mystream_c_offset_3),
    .i_mystream_c_data(mystream_c_data),
    .i__mystream_c_count_3(_mystream_c_count_3),
    .i__mystream_c_waddr_3(_mystream_c_waddr_3),
    .i__mystream_c_stride_3(_mystream_c_stride_3),
    ._mystream_c_offset_3(__mystream_c_fsm_3__mystream_c_offset_3_95),
    ._mystream_c_size_3(__mystream_c_fsm_3__mystream_c_size_3_96),
    ._mystream_c_stride_3(__mystream_c_fsm_3__mystream_c_stride_3_97),
    ._mystream_c_count_3(__mystream_c_fsm_3__mystream_c_count_3_98),
    ._mystream_c_waddr_3(__mystream_c_fsm_3__mystream_c_waddr_3_99),
    ._mystream_c_wdata_3(__mystream_c_fsm_3__mystream_c_wdata_3_100),
    ._mystream_c_wenable_3(__mystream_c_fsm_3__mystream_c_wenable_3_101)
  );


  always @(posedge CLK) begin
    if(RST) begin
      req_local_addr_34 <= 0;
      req_global_addr_35 <= 0;
      req_size_36 <= 0;
      req_local_stride_37 <= 1;
    end else begin
      if(set_req_38) begin
        req_local_addr_34 <= _th_comp_offset_1;
        req_global_addr_35 <= 1024;
        req_size_36 <= _th_comp_size_0;
        req_local_stride_37 <= 1;
      end 
      if(set_req_67) begin
        req_local_addr_34 <= _th_comp_offset_1;
        req_global_addr_35 <= 2048;
        req_size_36 <= _th_comp_size_0;
        req_local_stride_37 <= 1;
      end 
    end
  end

  localparam _fsm_dma_write_2_1 = 1;
  localparam _fsm_dma_write_2_2 = 2;
  localparam _fsm_dma_write_2_3 = 3;
  localparam _fsm_dma_write_2_4 = 4;
  localparam _fsm_dma_write_2_5 = 5;
  localparam _fsm_dma_write_2_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _fsm_dma_write_2 <= _fsm_dma_write_2_init;
      _d1__fsm_dma_write_2 <= _fsm_dma_write_2_init;
      _global_addr_40 <= 0;
      _rest_size_42 <= 0;
      _size_41 <= 0;
      fsm_done_58 <= 0;
      __fsm_dma_write_2_cond_5_0_1 <= 0;
    end else begin
      _d1__fsm_dma_write_2 <= _fsm_dma_write_2;
      case(_d1__fsm_dma_write_2)
        _fsm_dma_write_2_5: begin
          if(__fsm_dma_write_2_cond_5_0_1) begin
            fsm_done_58 <= 0;
          end 
        end
      endcase
      case(_fsm_dma_write_2)
        _fsm_dma_write_2_init: begin
          if(fsm_start_39) begin
            _fsm_dma_write_2 <= _fsm_dma_write_2_1;
          end 
          if(fsm_start_68) begin
            _fsm_dma_write_2 <= _fsm_dma_write_2_1;
          end 
        end
        _fsm_dma_write_2_1: begin
          _global_addr_40 <= (req_global_addr_35 >> 2) << 2;
          _rest_size_42 <= req_size_36;
          _fsm_dma_write_2 <= _fsm_dma_write_2_2;
        end
        _fsm_dma_write_2_2: begin
          if((_rest_size_42 <= 256) && ((_global_addr_40 & 4095) + (_rest_size_42 << 2) >= 4096)) begin
            _size_41 <= 4096 - (_global_addr_40 & 4095) >> 2;
            _rest_size_42 <= _rest_size_42 - (4096 - (_global_addr_40 & 4095) >> 2);
          end else if(_rest_size_42 <= 256) begin
            _size_41 <= _rest_size_42;
            _rest_size_42 <= 0;
          end else if((_global_addr_40 & 4095) + 1024 >= 4096) begin
            _size_41 <= 4096 - (_global_addr_40 & 4095) >> 2;
            _rest_size_42 <= _rest_size_42 - (4096 - (_global_addr_40 & 4095) >> 2);
          end else begin
            _size_41 <= 256;
            _rest_size_42 <= _rest_size_42 - 256;
          end
          _fsm_dma_write_2 <= _fsm_dma_write_2_3;
        end
        _fsm_dma_write_2_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _fsm_dma_write_2 <= _fsm_dma_write_2_4;
          end 
        end
        _fsm_dma_write_2_4: begin
          if(_tmp_56 && myaxi_wvalid && myaxi_wready) begin
            _global_addr_40 <= _global_addr_40 + (_size_41 << 2);
          end 
          if(_tmp_56 && myaxi_wvalid && myaxi_wready && (_rest_size_42 > 0)) begin
            _fsm_dma_write_2 <= _fsm_dma_write_2_2;
          end 
          if(_tmp_56 && myaxi_wvalid && myaxi_wready && (_rest_size_42 == 0)) begin
            _fsm_dma_write_2 <= _fsm_dma_write_2_5;
          end 
        end
        _fsm_dma_write_2_5: begin
          fsm_done_58 <= 1;
          __fsm_dma_write_2_cond_5_0_1 <= 1;
          _fsm_dma_write_2 <= _fsm_dma_write_2_6;
        end
        _fsm_dma_write_2_6: begin
          _fsm_dma_write_2 <= _fsm_dma_write_2_init;
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



module sub__mystream_fsm #
(
  parameter th_comp_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] _mystream_fsm,
  output reg [32-1:0] _d1__mystream_fsm,
  input [32-1:0] i_th_comp,
  input i__mystream_done,
  output reg _mystream_start,
  output reg _mystream_busy
);

  localparam _mystream_fsm_init = 0;
  localparam _mystream_fsm_1 = 1;
  localparam _mystream_fsm_2 = 2;
  localparam _mystream_fsm_3 = 3;
  localparam _mystream_fsm_4 = 4;
  localparam _mystream_fsm_5 = 5;
  localparam _mystream_fsm_6 = 6;
  localparam _mystream_fsm_7 = 7;
  localparam _mystream_fsm_8 = 8;
  reg __mystream_fsm_cond_0_0_1;

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
          if(i_th_comp == 14) begin
            _mystream_start <= 1;
            _mystream_busy <= 1;
          end 
          __mystream_fsm_cond_0_0_1 <= i_th_comp == 14;
          if(i_th_comp == 14) begin
            _mystream_fsm <= _mystream_fsm_1;
          end 
        end
        _mystream_fsm_1: begin
          _mystream_fsm <= _mystream_fsm_2;
        end
        _mystream_fsm_2: begin
          if(i__mystream_done) begin
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
          _mystream_fsm <= _mystream_fsm_8;
        end
        _mystream_fsm_8: begin
          _mystream_busy <= 0;
          _mystream_fsm <= _mystream_fsm_init;
        end
      endcase
    end
  end


endmodule



module sub__mystream_a_fsm_1 #
(
  parameter th_comp_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] _mystream_a_fsm_1,
  output reg [32-1:0] _d1__mystream_a_fsm_1,
  input [32-1:0] i_th_comp,
  input signed [32-1:0] i__th_comp_offset_3,
  input signed [32-1:0] i__th_comp_size_2,
  input i__mystream_start,
  input [16-1:0] i__mystream_a_fsm_sel,
  input [11-1:0] i__mystream_a_size_1,
  input [10-1:0] i__mystream_a_offset_1,
  input [11-1:0] i__mystream_a_count_1,
  input [10-1:0] i__mystream_a_raddr_1,
  input [10-1:0] i__mystream_a_stride_1,
  output reg [10-1:0] _mystream_a_offset_1,
  output reg [11-1:0] _mystream_a_size_1,
  output reg [10-1:0] _mystream_a_stride_1,
  output reg [11-1:0] _mystream_a_count_1,
  output reg [10-1:0] _mystream_a_raddr_1,
  output reg _mystream_a_renable_1
);

  localparam _mystream_a_fsm_1_init = 0;
  localparam _mystream_a_fsm_1_1 = 1;
  localparam _mystream_a_fsm_1_2 = 2;
  reg __mystream_a_fsm_1_cond_1_0_1;
  reg __mystream_a_fsm_1_cond_2_1_1;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
      _d1__mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
      _mystream_a_offset_1 <= 0;
      _mystream_a_size_1 <= 0;
      _mystream_a_stride_1 <= 0;
      _mystream_a_count_1 <= 0;
      _mystream_a_raddr_1 <= 0;
      _mystream_a_renable_1 <= 0;
      __mystream_a_fsm_1_cond_1_0_1 <= 0;
      __mystream_a_fsm_1_cond_2_1_1 <= 0;
    end else begin
      _d1__mystream_a_fsm_1 <= _mystream_a_fsm_1;
      case(_d1__mystream_a_fsm_1)
        _mystream_a_fsm_1_1: begin
          if(__mystream_a_fsm_1_cond_1_0_1) begin
            _mystream_a_renable_1 <= 0;
          end 
        end
        _mystream_a_fsm_1_2: begin
          if(__mystream_a_fsm_1_cond_2_1_1) begin
            _mystream_a_renable_1 <= 0;
          end 
        end
      endcase
      case(_mystream_a_fsm_1)
        _mystream_a_fsm_1_init: begin
          if(i_th_comp == 11) begin
            _mystream_a_offset_1 <= i__th_comp_offset_3;
            _mystream_a_size_1 <= i__th_comp_size_2;
            _mystream_a_stride_1 <= 1;
          end 
          if(i__mystream_start && (i__mystream_a_fsm_sel == 1) && (i__mystream_a_size_1 > 0)) begin
            _mystream_a_count_1 <= i__mystream_a_size_1;
          end 
          if(i__mystream_start && (i__mystream_a_fsm_sel == 1) && (i__mystream_a_size_1 > 0)) begin
            _mystream_a_fsm_1 <= _mystream_a_fsm_1_1;
          end 
        end
        _mystream_a_fsm_1_1: begin
          _mystream_a_raddr_1 <= i__mystream_a_offset_1;
          _mystream_a_renable_1 <= 1;
          _mystream_a_count_1 <= i__mystream_a_count_1 - 1;
          __mystream_a_fsm_1_cond_1_0_1 <= 1;
          if(i__mystream_a_count_1 == 1) begin
            _mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
          end 
          if(i__mystream_a_count_1 > 1) begin
            _mystream_a_fsm_1 <= _mystream_a_fsm_1_2;
          end 
        end
        _mystream_a_fsm_1_2: begin
          _mystream_a_raddr_1 <= i__mystream_a_raddr_1 + i__mystream_a_stride_1;
          _mystream_a_renable_1 <= 1;
          _mystream_a_count_1 <= i__mystream_a_count_1 - 1;
          __mystream_a_fsm_1_cond_2_1_1 <= 1;
          if(i__mystream_a_count_1 == 1) begin
            _mystream_a_fsm_1 <= _mystream_a_fsm_1_init;
          end 
        end
      endcase
    end
  end


endmodule



module sub__mystream_b_fsm_2 #
(
  parameter th_comp_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] _mystream_b_fsm_2,
  output reg [32-1:0] _d1__mystream_b_fsm_2,
  input [32-1:0] i_th_comp,
  input signed [32-1:0] i__th_comp_offset_3,
  input signed [32-1:0] i__th_comp_size_2,
  input i__mystream_start,
  input [16-1:0] i__mystream_b_fsm_sel,
  input [11-1:0] i__mystream_b_size_2,
  input [10-1:0] i__mystream_b_offset_2,
  input [11-1:0] i__mystream_b_count_2,
  input [10-1:0] i__mystream_b_raddr_2,
  input [10-1:0] i__mystream_b_stride_2,
  output reg [10-1:0] _mystream_b_offset_2,
  output reg [11-1:0] _mystream_b_size_2,
  output reg [10-1:0] _mystream_b_stride_2,
  output reg [11-1:0] _mystream_b_count_2,
  output reg [10-1:0] _mystream_b_raddr_2,
  output reg _mystream_b_renable_2
);

  localparam _mystream_b_fsm_2_init = 0;
  localparam _mystream_b_fsm_2_1 = 1;
  localparam _mystream_b_fsm_2_2 = 2;
  reg __mystream_b_fsm_2_cond_1_0_1;
  reg __mystream_b_fsm_2_cond_2_1_1;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
      _d1__mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
      _mystream_b_offset_2 <= 0;
      _mystream_b_size_2 <= 0;
      _mystream_b_stride_2 <= 0;
      _mystream_b_count_2 <= 0;
      _mystream_b_raddr_2 <= 0;
      _mystream_b_renable_2 <= 0;
      __mystream_b_fsm_2_cond_1_0_1 <= 0;
      __mystream_b_fsm_2_cond_2_1_1 <= 0;
    end else begin
      _d1__mystream_b_fsm_2 <= _mystream_b_fsm_2;
      case(_d1__mystream_b_fsm_2)
        _mystream_b_fsm_2_1: begin
          if(__mystream_b_fsm_2_cond_1_0_1) begin
            _mystream_b_renable_2 <= 0;
          end 
        end
        _mystream_b_fsm_2_2: begin
          if(__mystream_b_fsm_2_cond_2_1_1) begin
            _mystream_b_renable_2 <= 0;
          end 
        end
      endcase
      case(_mystream_b_fsm_2)
        _mystream_b_fsm_2_init: begin
          if(i_th_comp == 12) begin
            _mystream_b_offset_2 <= i__th_comp_offset_3;
            _mystream_b_size_2 <= i__th_comp_size_2;
            _mystream_b_stride_2 <= 1;
          end 
          if(i__mystream_start && (i__mystream_b_fsm_sel == 2) && (i__mystream_b_size_2 > 0)) begin
            _mystream_b_count_2 <= i__mystream_b_size_2;
          end 
          if(i__mystream_start && (i__mystream_b_fsm_sel == 2) && (i__mystream_b_size_2 > 0)) begin
            _mystream_b_fsm_2 <= _mystream_b_fsm_2_1;
          end 
        end
        _mystream_b_fsm_2_1: begin
          _mystream_b_raddr_2 <= i__mystream_b_offset_2;
          _mystream_b_renable_2 <= 1;
          _mystream_b_count_2 <= i__mystream_b_count_2 - 1;
          __mystream_b_fsm_2_cond_1_0_1 <= 1;
          if(i__mystream_b_count_2 == 1) begin
            _mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
          end 
          if(i__mystream_b_count_2 > 1) begin
            _mystream_b_fsm_2 <= _mystream_b_fsm_2_2;
          end 
        end
        _mystream_b_fsm_2_2: begin
          _mystream_b_raddr_2 <= i__mystream_b_raddr_2 + i__mystream_b_stride_2;
          _mystream_b_renable_2 <= 1;
          _mystream_b_count_2 <= i__mystream_b_count_2 - 1;
          __mystream_b_fsm_2_cond_2_1_1 <= 1;
          if(i__mystream_b_count_2 == 1) begin
            _mystream_b_fsm_2 <= _mystream_b_fsm_2_init;
          end 
        end
      endcase
    end
  end


endmodule



module sub__mystream_c_fsm_3 #
(
  parameter th_comp_init = 0
)
(
  input CLK,
  input RST,
  output reg [32-1:0] _mystream_c_fsm_3,
  output reg [32-1:0] _d1__mystream_c_fsm_3,
  input [32-1:0] i_th_comp,
  input signed [32-1:0] i__th_comp_offset_3,
  input signed [32-1:0] i__th_comp_size_2,
  input i__mystream_start,
  input [16-1:0] i__mystream_c_fsm_sel,
  input [11-1:0] i__mystream_c_size_3,
  input [10-1:0] i__mystream_c_offset_3,
  input signed [32-1:0] i_mystream_c_data,
  input [11-1:0] i__mystream_c_count_3,
  input [10-1:0] i__mystream_c_waddr_3,
  input [10-1:0] i__mystream_c_stride_3,
  output reg [10-1:0] _mystream_c_offset_3,
  output reg [11-1:0] _mystream_c_size_3,
  output reg [10-1:0] _mystream_c_stride_3,
  output reg [11-1:0] _mystream_c_count_3,
  output reg [10-1:0] _mystream_c_waddr_3,
  output reg signed [32-1:0] _mystream_c_wdata_3,
  output reg _mystream_c_wenable_3
);

  localparam _mystream_c_fsm_3_init = 0;
  localparam _mystream_c_fsm_3_6 = 6;
  localparam _mystream_c_fsm_3_7 = 7;
  localparam _mystream_c_fsm_3_1 = 1;
  localparam _mystream_c_fsm_3_2 = 2;
  localparam _mystream_c_fsm_3_3 = 3;
  localparam _mystream_c_fsm_3_4 = 4;
  localparam _mystream_c_fsm_3_5 = 5;
  reg __mystream_c_fsm_3_cond_6_0_1;
  reg __mystream_c_fsm_3_cond_7_1_1;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_c_fsm_3 <= _mystream_c_fsm_3_init;
      _d1__mystream_c_fsm_3 <= _mystream_c_fsm_3_init;
      _mystream_c_offset_3 <= 0;
      _mystream_c_size_3 <= 0;
      _mystream_c_stride_3 <= 0;
      _mystream_c_count_3 <= 0;
      _mystream_c_waddr_3 <= 0;
      _mystream_c_wdata_3 <= 0;
      _mystream_c_wenable_3 <= 0;
      __mystream_c_fsm_3_cond_6_0_1 <= 0;
      __mystream_c_fsm_3_cond_7_1_1 <= 0;
    end else begin
      _d1__mystream_c_fsm_3 <= _mystream_c_fsm_3;
      case(_d1__mystream_c_fsm_3)
        _mystream_c_fsm_3_6: begin
          if(__mystream_c_fsm_3_cond_6_0_1) begin
            _mystream_c_wenable_3 <= 0;
          end 
        end
        _mystream_c_fsm_3_7: begin
          if(__mystream_c_fsm_3_cond_7_1_1) begin
            _mystream_c_wenable_3 <= 0;
          end 
        end
      endcase
      case(_mystream_c_fsm_3)
        _mystream_c_fsm_3_init: begin
          if(i_th_comp == 13) begin
            _mystream_c_offset_3 <= i__th_comp_offset_3;
            _mystream_c_size_3 <= i__th_comp_size_2;
            _mystream_c_stride_3 <= 1;
          end 
          if(i__mystream_start && (i__mystream_c_fsm_sel == 3) && (i__mystream_c_size_3 > 0)) begin
            _mystream_c_count_3 <= i__mystream_c_size_3;
          end 
          if(i__mystream_start && (i__mystream_c_fsm_sel == 3) && (i__mystream_c_size_3 > 0)) begin
            _mystream_c_fsm_3 <= _mystream_c_fsm_3_1;
          end 
        end
        _mystream_c_fsm_3_1: begin
          _mystream_c_fsm_3 <= _mystream_c_fsm_3_2;
        end
        _mystream_c_fsm_3_2: begin
          _mystream_c_fsm_3 <= _mystream_c_fsm_3_3;
        end
        _mystream_c_fsm_3_3: begin
          _mystream_c_fsm_3 <= _mystream_c_fsm_3_4;
        end
        _mystream_c_fsm_3_4: begin
          _mystream_c_fsm_3 <= _mystream_c_fsm_3_5;
        end
        _mystream_c_fsm_3_5: begin
          _mystream_c_fsm_3 <= _mystream_c_fsm_3_6;
        end
        _mystream_c_fsm_3_6: begin
          _mystream_c_waddr_3 <= i__mystream_c_offset_3;
          _mystream_c_wdata_3 <= i_mystream_c_data;
          _mystream_c_wenable_3 <= 1;
          _mystream_c_count_3 <= i__mystream_c_count_3 - 1;
          __mystream_c_fsm_3_cond_6_0_1 <= 1;
          if(i__mystream_c_count_3 == 1) begin
            _mystream_c_fsm_3 <= _mystream_c_fsm_3_init;
          end 
          if(i__mystream_c_count_3 > 1) begin
            _mystream_c_fsm_3 <= _mystream_c_fsm_3_7;
          end 
        end
        _mystream_c_fsm_3_7: begin
          _mystream_c_waddr_3 <= i__mystream_c_waddr_3 + i__mystream_c_stride_3;
          _mystream_c_wdata_3 <= i_mystream_c_data;
          _mystream_c_wenable_3 <= 1;
          _mystream_c_count_3 <= i__mystream_c_count_3 - 1;
          __mystream_c_fsm_3_cond_7_1_1 <= 1;
          if(i__mystream_c_count_3 == 1) begin
            _mystream_c_fsm_3 <= _mystream_c_fsm_3_init;
          end 
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_stream_fsm_as_module.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
