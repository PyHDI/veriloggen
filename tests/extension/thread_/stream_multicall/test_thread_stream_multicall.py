from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_multicall

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
    myaxi_rdata = memory_rdata;
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

  reg _myaxi_read_start;
  reg [8-1:0] _myaxi_read_op_sel;
  reg [32-1:0] _myaxi_read_local_addr;
  reg [32-1:0] _myaxi_read_global_addr;
  reg [33-1:0] _myaxi_read_size;
  reg [32-1:0] _myaxi_read_local_stride;
  reg _myaxi_read_idle;
  reg _myaxi_write_start;
  reg [8-1:0] _myaxi_write_op_sel;
  reg [32-1:0] _myaxi_write_local_addr;
  reg [32-1:0] _myaxi_write_global_addr;
  reg [33-1:0] _myaxi_write_size;
  reg [32-1:0] _myaxi_write_local_stride;
  reg _myaxi_write_idle;
  wire _myaxi_write_data_done;
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
  wire _mystream_start_flag;
  reg _mystream_start;
  reg _mystream_busy;
  reg _mystream_a_idle;
  reg [3-1:0] _mystream_a_source_mode;
  reg [32-1:0] _mystream_a_source_offset;
  reg [33-1:0] _mystream_a_source_size;
  reg [32-1:0] _mystream_a_source_stride;
  reg [33-1:0] _mystream_a_source_count;
  reg [8-1:0] _mystream_a_source_ram_sel;
  reg [32-1:0] _mystream_a_source_ram_raddr;
  reg _mystream_a_source_ram_renable;
  wire [32-1:0] _mystream_a_source_ram_rdata;
  reg _mystream_a_source_ram_rvalid;
  reg _mystream_b_idle;
  reg [3-1:0] _mystream_b_source_mode;
  reg [32-1:0] _mystream_b_source_offset;
  reg [33-1:0] _mystream_b_source_size;
  reg [32-1:0] _mystream_b_source_stride;
  reg [33-1:0] _mystream_b_source_count;
  reg [8-1:0] _mystream_b_source_ram_sel;
  reg [32-1:0] _mystream_b_source_ram_raddr;
  reg _mystream_b_source_ram_renable;
  wire [32-1:0] _mystream_b_source_ram_rdata;
  reg _mystream_b_source_ram_rvalid;
  reg [3-1:0] _mystream_c_sink_mode;
  reg [32-1:0] _mystream_c_sink_offset;
  reg [33-1:0] _mystream_c_sink_size;
  reg [32-1:0] _mystream_c_sink_stride;
  reg [33-1:0] _mystream_c_sink_count;
  reg [8-1:0] _mystream_c_sink_ram_sel;
  reg [32-1:0] _mystream_c_sink_waddr;
  reg _mystream_c_sink_wenable;
  reg [32-1:0] _mystream_c_sink_wdata;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_0;
  reg signed [32-1:0] _th_comp_orig_size_1;
  reg signed [32-1:0] _th_comp_offset_2;
  reg axim_flag_0;
  reg [32-1:0] _d1_th_comp;
  reg _th_comp_cond_4_0_1;
  reg _myaxi_ram_a_0_read_start;
  reg [8-1:0] _myaxi_ram_a_0_read_op_sel;
  reg [32-1:0] _myaxi_ram_a_0_read_local_addr;
  reg [32-1:0] _myaxi_ram_a_0_read_global_addr;
  reg [33-1:0] _myaxi_ram_a_0_read_size;
  reg [32-1:0] _myaxi_ram_a_0_read_local_stride;
  reg [32-1:0] _myaxi_read_fsm;
  localparam _myaxi_read_fsm_init = 0;
  reg [32-1:0] _myaxi_read_cur_global_addr;
  reg [33-1:0] _myaxi_read_cur_size;
  reg [33-1:0] _myaxi_read_rest_size;
  reg [32-1:0] _wdata_1;
  reg _wvalid_2;
  reg [34-1:0] _tmp_3;
  reg _tmp_4;
  wire [32-1:0] __variable_data_5;
  wire __variable_valid_5;
  wire __variable_ready_5;
  assign __variable_ready_5 = (_tmp_3 > 0) && !_tmp_4;
  reg _ram_a_cond_0_1;
  reg [9-1:0] _tmp_6;
  reg _myaxi_cond_0_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_7;
  reg __myaxi_read_fsm_cond_4_1_1;
  reg axim_flag_8;
  reg _th_comp_cond_8_1_1;
  reg _myaxi_ram_b_0_read_start;
  reg [8-1:0] _myaxi_ram_b_0_read_op_sel;
  reg [32-1:0] _myaxi_ram_b_0_read_local_addr;
  reg [32-1:0] _myaxi_ram_b_0_read_global_addr;
  reg [33-1:0] _myaxi_ram_b_0_read_size;
  reg [32-1:0] _myaxi_ram_b_0_read_local_stride;
  reg [32-1:0] _wdata_9;
  reg _wvalid_10;
  reg [34-1:0] _tmp_11;
  reg _tmp_12;
  wire [32-1:0] __variable_data_13;
  wire __variable_valid_13;
  wire __variable_ready_13;
  assign __variable_ready_13 = (_tmp_11 > 0) && !_tmp_12;
  reg _ram_b_cond_0_1;
  reg __myaxi_read_fsm_cond_3_2_1;
  reg signed [32-1:0] _th_comp_size_3;
  reg signed [32-1:0] _th_comp_offset_4;
  wire signed [32-1:0] mystream_a_data;
  wire signed [32-1:0] mystream_b_data;
  wire signed [64-1:0] _times_mul_odata_2;
  reg signed [64-1:0] _times_mul_odata_reg_2;
  wire signed [32-1:0] _times_data_2;
  assign _times_data_2 = _times_mul_odata_reg_2;
  wire _times_mul_update_2;
  assign _times_mul_update_2 = 1;

  multiplier_0
  _times_mul_2
  (
    .CLK(CLK),
    .update(_times_mul_update_2),
    .a(mystream_a_data),
    .b(mystream_b_data),
    .c(_times_mul_odata_2)
  );

  wire signed [32-1:0] mystream_c_data;
  assign mystream_c_data = _times_data_2;
  reg _set_flag_14;
  reg _tmp_15;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  assign _mystream_a_source_ram_rdata = (_mystream_a_source_ram_sel == 1)? ram_a_0_rdata : 0;
  localparam _tmp_16 = 1;
  wire [_tmp_16-1:0] _tmp_17;
  assign _tmp_17 = _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
  reg [_tmp_16-1:0] __tmp_17_1;
  reg signed [32-1:0] __variable_wdata_0;
  assign mystream_a_data = __variable_wdata_0;
  reg [32-1:0] _mystream_a_source_fsm_0;
  localparam _mystream_a_source_fsm_0_init = 0;
  reg _set_flag_18;
  reg _tmp_19;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  assign _mystream_b_source_ram_rdata = (_mystream_b_source_ram_sel == 2)? ram_b_0_rdata : 0;
  localparam _tmp_20 = 1;
  wire [_tmp_20-1:0] _tmp_21;
  assign _tmp_21 = _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
  reg [_tmp_20-1:0] __tmp_21_1;
  reg signed [32-1:0] __variable_wdata_1;
  assign mystream_b_data = __variable_wdata_1;
  reg [32-1:0] _mystream_b_source_fsm_1;
  localparam _mystream_b_source_fsm_1_init = 0;
  reg _set_flag_22;
  reg _ram_c_cond_0_1;
  reg [32-1:0] _mystream_c_sink_fsm_2;
  localparam _mystream_c_sink_fsm_2_init = 0;
  reg _set_flag_23;
  wire _mystream_done;
  assign _mystream_done = _mystream_a_idle && _mystream_b_idle;
  reg axim_flag_24;
  reg _th_comp_cond_19_2_1;
  reg _myaxi_ram_c_0_write_start;
  reg [8-1:0] _myaxi_ram_c_0_write_op_sel;
  reg [32-1:0] _myaxi_ram_c_0_write_local_addr;
  reg [32-1:0] _myaxi_ram_c_0_write_global_addr;
  reg [33-1:0] _myaxi_ram_c_0_write_size;
  reg [32-1:0] _myaxi_ram_c_0_write_local_stride;
  reg [32-1:0] _myaxi_write_fsm;
  localparam _myaxi_write_fsm_init = 0;
  reg [32-1:0] _myaxi_write_cur_global_addr;
  reg [33-1:0] _myaxi_write_cur_size;
  reg [33-1:0] _myaxi_write_rest_size;
  reg _tmp_25;
  reg _tmp_26;
  wire _tmp_27;
  wire _tmp_28;
  assign _tmp_28 = 1;
  localparam _tmp_29 = 1;
  wire [_tmp_29-1:0] _tmp_30;
  assign _tmp_30 = (_tmp_27 || !_tmp_25) && (_tmp_28 || !_tmp_26);
  reg [_tmp_29-1:0] __tmp_30_1;
  wire signed [32-1:0] _tmp_31;
  reg signed [32-1:0] __tmp_31_1;
  assign _tmp_31 = (__tmp_30_1)? ram_c_0_rdata : __tmp_31_1;
  reg _tmp_32;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg [34-1:0] _tmp_36;
  reg [9-1:0] _tmp_37;
  reg _myaxi_cond_1_1;
  reg _tmp_38;
  wire [32-1:0] __variable_data_39;
  wire __variable_valid_39;
  wire __variable_ready_39;
  assign __variable_ready_39 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_37 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  assign _myaxi_write_data_done = (_tmp_38 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_40;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg axim_flag_41;
  reg _th_comp_cond_24_3_1;
  reg axim_flag_42;
  reg _th_comp_cond_28_4_1;
  reg signed [32-1:0] _th_comp_size_5;
  reg signed [32-1:0] _th_comp_offset_6;
  reg _set_flag_43;
  reg _set_flag_44;
  reg _set_flag_45;
  reg _set_flag_46;
  reg axim_flag_47;
  reg _th_comp_cond_39_5_1;
  reg axim_flag_48;
  reg _th_comp_cond_45_6_1;
  reg axim_flag_49;
  reg _th_comp_cond_49_7_1;
  reg signed [32-1:0] _th_comp_size_7;
  reg signed [32-1:0] _th_comp_offset_8;
  reg _set_flag_50;
  reg _set_flag_51;
  reg _set_flag_52;
  reg _set_flag_53;
  assign _mystream_start_flag = (_set_flag_53)? 1 : 
                                (_set_flag_46)? 1 : 
                                (_set_flag_23)? 1 : 0;
  reg axim_flag_54;
  reg _th_comp_cond_60_8_1;
  reg axim_flag_55;
  reg _th_comp_cond_65_9_1;
  reg axim_flag_56;
  reg _th_comp_cond_69_10_1;
  reg signed [32-1:0] _th_comp_size_9;
  reg signed [32-1:0] _th_comp_offset_10;
  reg signed [32-1:0] _th_comp_sum_11;
  reg signed [32-1:0] _th_comp_i_12;
  reg _tmp_57;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_4_1;
  reg _ram_a_cond_4_2;
  reg signed [32-1:0] _tmp_58;
  reg signed [32-1:0] _th_comp_a_13;
  reg _tmp_59;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_4_1;
  reg _ram_b_cond_4_2;
  reg signed [32-1:0] _tmp_60;
  reg signed [32-1:0] _th_comp_b_14;
  reg _ram_c_cond_1_1;
  reg axim_flag_61;
  reg _th_comp_cond_84_11_1;
  reg signed [32-1:0] _th_comp_size_15;
  reg signed [32-1:0] _th_comp_offset_stream_16;
  reg signed [32-1:0] _th_comp_offset_seq_17;
  reg signed [32-1:0] _th_comp_all_ok_18;
  reg signed [32-1:0] _th_comp_i_19;
  reg _tmp_62;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_63;
  reg signed [32-1:0] _th_comp_st_20;
  reg _tmp_64;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_65;
  reg signed [32-1:0] _th_comp_sq_21;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_ram_a_0_read_start <= 0;
      _myaxi_ram_a_0_read_op_sel <= 0;
      _myaxi_ram_a_0_read_local_addr <= 0;
      _myaxi_ram_a_0_read_global_addr <= 0;
      _myaxi_ram_a_0_read_size <= 0;
      _myaxi_ram_a_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_6 <= 0;
      _myaxi_cond_0_1 <= 0;
      _myaxi_ram_b_0_read_start <= 0;
      _myaxi_ram_b_0_read_op_sel <= 0;
      _myaxi_ram_b_0_read_local_addr <= 0;
      _myaxi_ram_b_0_read_global_addr <= 0;
      _myaxi_ram_b_0_read_size <= 0;
      _myaxi_ram_b_0_read_local_stride <= 0;
      _myaxi_ram_c_0_write_start <= 0;
      _myaxi_ram_c_0_write_op_sel <= 0;
      _myaxi_ram_c_0_write_local_addr <= 0;
      _myaxi_ram_c_0_write_global_addr <= 0;
      _myaxi_ram_c_0_write_size <= 0;
      _myaxi_ram_c_0_write_local_stride <= 0;
      _myaxi_write_idle <= 1;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_size <= 0;
      _myaxi_write_local_stride <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_37 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_38 <= 0;
      _myaxi_cond_2_1 <= 0;
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
        _tmp_38 <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_ram_a_0_read_start <= 0;
      if(axim_flag_0) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_0;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(_myaxi_ram_a_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_ram_a_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_ram_a_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_ram_a_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_ram_a_0_read_global_addr;
        _myaxi_read_size <= _myaxi_ram_a_0_read_size;
        _myaxi_read_local_stride <= _myaxi_ram_a_0_read_local_stride;
      end 
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_6 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_6 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_6 > 0)) begin
        _tmp_6 <= _tmp_6 - 1;
      end 
      if(axim_flag_7) begin
        _myaxi_read_idle <= 1;
      end 
      _myaxi_ram_b_0_read_start <= 0;
      if(axim_flag_8) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_0;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(_myaxi_ram_b_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_ram_b_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_ram_b_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_ram_b_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_ram_b_0_read_global_addr;
        _myaxi_read_size <= _myaxi_ram_b_0_read_size;
        _myaxi_read_local_stride <= _myaxi_ram_b_0_read_local_stride;
      end 
      _myaxi_ram_c_0_write_start <= 0;
      if(axim_flag_24) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_2;
        _myaxi_ram_c_0_write_global_addr <= 1024;
        _myaxi_ram_c_0_write_size <= _th_comp_size_0;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
      if(_myaxi_ram_c_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_ram_c_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_ram_c_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_ram_c_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_ram_c_0_write_global_addr;
        _myaxi_write_size <= _myaxi_ram_c_0_write_size;
        _myaxi_write_local_stride <= _myaxi_ram_c_0_write_local_stride;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_37 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_37 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_37 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_39 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_37 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_37 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_37 > 0))) begin
        myaxi_wdata <= __variable_data_39;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_37 <= _tmp_37 - 1;
      end 
      if(__variable_valid_39 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_37 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_37 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_37 > 0)) && (_tmp_37 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_38 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_38 <= _tmp_38;
      end 
      if(axim_flag_40) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_41) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_0;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_42) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_0;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_47) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_2;
        _myaxi_ram_c_0_write_global_addr <= 1024;
        _myaxi_ram_c_0_write_size <= _th_comp_size_0;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
      if(axim_flag_48) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_0;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_49) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_0;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_54) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_2;
        _myaxi_ram_c_0_write_global_addr <= 1024;
        _myaxi_ram_c_0_write_size <= _th_comp_size_0;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
      if(axim_flag_55) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_0;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_56) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_2;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_0;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_61) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_2;
        _myaxi_ram_c_0_write_global_addr <= 2048;
        _myaxi_ram_c_0_write_size <= _th_comp_size_0;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
    end
  end

  assign __variable_data_5 = _wdata_1;
  assign __variable_valid_5 = _wvalid_2;
  assign __variable_data_13 = _wdata_9;
  assign __variable_valid_13 = _wvalid_10;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_3 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_4 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_15 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
      _ram_a_cond_3_1 <= 0;
      _tmp_57 <= 0;
      _ram_a_cond_4_1 <= 0;
      _ram_a_cond_4_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_15 <= 0;
      end 
      if(_ram_a_cond_4_2) begin
        _tmp_57 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_4 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_15 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if(_ram_a_cond_3_1) begin
        _tmp_57 <= 1;
      end 
      _ram_a_cond_4_2 <= _ram_a_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_3 == 0)) begin
        ram_a_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_3 <= _myaxi_read_size;
      end 
      if(__variable_valid_5 && ((_tmp_3 > 0) && !_tmp_4) && (_tmp_3 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _myaxi_read_local_stride;
        ram_a_0_wdata <= __variable_data_5;
        ram_a_0_wenable <= 1;
        _tmp_3 <= _tmp_3 - 1;
      end 
      if(__variable_valid_5 && ((_tmp_3 > 0) && !_tmp_4) && (_tmp_3 == 1)) begin
        _tmp_4 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      if(_mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1)) begin
        ram_a_0_addr <= _mystream_a_source_ram_raddr;
      end 
      _ram_a_cond_1_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      _ram_a_cond_2_1 <= _mystream_a_source_ram_renable && (_mystream_a_source_ram_sel == 1);
      if(th_comp == 77) begin
        ram_a_0_addr <= _th_comp_i_12 + _th_comp_offset_10;
      end 
      _ram_a_cond_3_1 <= th_comp == 77;
      _ram_a_cond_4_1 <= th_comp == 77;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_11 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_12 <= 0;
      _ram_b_cond_0_1 <= 0;
      _ram_b_cond_1_1 <= 0;
      _tmp_19 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
      _ram_b_cond_3_1 <= 0;
      _tmp_59 <= 0;
      _ram_b_cond_4_1 <= 0;
      _ram_b_cond_4_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_19 <= 0;
      end 
      if(_ram_b_cond_4_2) begin
        _tmp_59 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_12 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_19 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if(_ram_b_cond_3_1) begin
        _tmp_59 <= 1;
      end 
      _ram_b_cond_4_2 <= _ram_b_cond_4_1;
      if(_myaxi_read_start && (_myaxi_read_op_sel == 2) && (_tmp_11 == 0)) begin
        ram_b_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_11 <= _myaxi_read_size;
      end 
      if(__variable_valid_13 && ((_tmp_11 > 0) && !_tmp_12) && (_tmp_11 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + _myaxi_read_local_stride;
        ram_b_0_wdata <= __variable_data_13;
        ram_b_0_wenable <= 1;
        _tmp_11 <= _tmp_11 - 1;
      end 
      if(__variable_valid_13 && ((_tmp_11 > 0) && !_tmp_12) && (_tmp_11 == 1)) begin
        _tmp_12 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      if(_mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2)) begin
        ram_b_0_addr <= _mystream_b_source_ram_raddr;
      end 
      _ram_b_cond_1_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      _ram_b_cond_2_1 <= _mystream_b_source_ram_renable && (_mystream_b_source_ram_sel == 2);
      if(th_comp == 79) begin
        ram_b_0_addr <= _th_comp_i_12 + _th_comp_offset_10;
      end 
      _ram_b_cond_3_1 <= th_comp == 79;
      _ram_b_cond_4_1 <= th_comp == 79;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_30_1 <= 0;
      __tmp_31_1 <= 0;
      _tmp_35 <= 0;
      _tmp_25 <= 0;
      _tmp_26 <= 0;
      _tmp_33 <= 0;
      _tmp_34 <= 0;
      _tmp_32 <= 0;
      _tmp_36 <= 0;
      _ram_c_cond_1_1 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_62 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_64 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_62 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_64 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_62 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_64 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if(_mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3)) begin
        ram_c_0_addr <= _mystream_c_sink_waddr;
        ram_c_0_wdata <= _mystream_c_sink_wdata;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= _mystream_c_sink_wenable && (_mystream_c_sink_ram_sel == 3);
      __tmp_30_1 <= _tmp_30;
      __tmp_31_1 <= _tmp_31;
      if((_tmp_27 || !_tmp_25) && (_tmp_28 || !_tmp_26) && _tmp_33) begin
        _tmp_35 <= 0;
        _tmp_25 <= 0;
        _tmp_26 <= 0;
        _tmp_33 <= 0;
      end 
      if((_tmp_27 || !_tmp_25) && (_tmp_28 || !_tmp_26) && _tmp_32) begin
        _tmp_25 <= 1;
        _tmp_26 <= 1;
        _tmp_35 <= _tmp_34;
        _tmp_34 <= 0;
        _tmp_32 <= 0;
        _tmp_33 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_36 == 0) && !_tmp_34 && !_tmp_35) begin
        ram_c_0_addr <= _myaxi_write_local_addr;
        _tmp_36 <= _myaxi_write_size - 1;
        _tmp_32 <= 1;
        _tmp_34 <= _myaxi_write_size == 1;
      end 
      if((_tmp_27 || !_tmp_25) && (_tmp_28 || !_tmp_26) && (_tmp_36 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + _myaxi_write_local_stride;
        _tmp_36 <= _tmp_36 - 1;
        _tmp_32 <= 1;
        _tmp_34 <= 0;
      end 
      if((_tmp_27 || !_tmp_25) && (_tmp_28 || !_tmp_26) && (_tmp_36 == 1)) begin
        _tmp_34 <= 1;
      end 
      if(th_comp == 82) begin
        ram_c_0_addr <= _th_comp_i_12 + _th_comp_offset_10;
        ram_c_0_wdata <= _th_comp_sum_11;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_comp == 82;
      if(th_comp == 92) begin
        ram_c_0_addr <= _th_comp_i_19 + _th_comp_offset_stream_16;
      end 
      _ram_c_cond_2_1 <= th_comp == 92;
      _ram_c_cond_3_1 <= th_comp == 92;
      if(th_comp == 94) begin
        ram_c_0_addr <= _th_comp_i_19 + _th_comp_offset_seq_17;
      end 
      _ram_c_cond_4_1 <= th_comp == 94;
      _ram_c_cond_5_1 <= th_comp == 94;
    end
  end

  assign __variable_data_39 = _tmp_31;
  assign __variable_valid_39 = _tmp_25;
  assign _tmp_27 = 1 && __variable_ready_39;

  always @(posedge CLK) begin
    if(RST) begin
      _times_mul_odata_reg_2 <= 0;
      _set_flag_14 <= 0;
      _mystream_a_source_mode <= 3'b0;
      _mystream_a_source_offset <= 0;
      _mystream_a_source_size <= 0;
      _mystream_a_source_stride <= 0;
      _mystream_a_source_ram_sel <= 0;
      __tmp_17_1 <= 0;
      _mystream_a_source_ram_rvalid <= 0;
      __variable_wdata_0 <= 0;
      _mystream_a_idle <= 1;
      _mystream_a_source_ram_raddr <= 0;
      _mystream_a_source_ram_renable <= 0;
      _mystream_a_source_count <= 0;
      _set_flag_18 <= 0;
      _mystream_b_source_mode <= 3'b0;
      _mystream_b_source_offset <= 0;
      _mystream_b_source_size <= 0;
      _mystream_b_source_stride <= 0;
      _mystream_b_source_ram_sel <= 0;
      __tmp_21_1 <= 0;
      _mystream_b_source_ram_rvalid <= 0;
      __variable_wdata_1 <= 0;
      _mystream_b_idle <= 1;
      _mystream_b_source_ram_raddr <= 0;
      _mystream_b_source_ram_renable <= 0;
      _mystream_b_source_count <= 0;
      _set_flag_22 <= 0;
      _mystream_c_sink_mode <= 3'b0;
      _mystream_c_sink_offset <= 0;
      _mystream_c_sink_size <= 0;
      _mystream_c_sink_stride <= 0;
      _mystream_c_sink_ram_sel <= 0;
      _mystream_c_sink_wenable <= 0;
      _mystream_c_sink_waddr <= 0;
      _mystream_c_sink_count <= 0;
      _mystream_c_sink_wdata <= 0;
      _set_flag_23 <= 0;
      _set_flag_43 <= 0;
      _set_flag_44 <= 0;
      _set_flag_45 <= 0;
      _set_flag_46 <= 0;
      _set_flag_50 <= 0;
      _set_flag_51 <= 0;
      _set_flag_52 <= 0;
      _set_flag_53 <= 0;
    end else begin
      _times_mul_odata_reg_2 <= _times_mul_odata_2;
      _set_flag_14 <= 0;
      if(th_comp == 13) begin
        _set_flag_14 <= 1;
      end 
      if(_set_flag_14) begin
        _mystream_a_source_mode <= 3'b1;
        _mystream_a_source_offset <= _th_comp_offset_4;
        _mystream_a_source_size <= _th_comp_size_3;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_14) begin
        _mystream_a_source_ram_sel <= 1;
      end 
      __tmp_17_1 <= _tmp_17;
      _mystream_a_source_ram_rvalid <= __tmp_17_1;
      if(_mystream_a_source_ram_rvalid) begin
        __variable_wdata_0 <= _mystream_a_source_ram_rdata;
      end 
      if(_mystream_start && _mystream_a_source_mode & 3'b1) begin
        _mystream_a_idle <= 0;
      end 
      if(_mystream_a_source_fsm_0 == 1) begin
        _mystream_a_source_ram_raddr <= _mystream_a_source_offset;
        _mystream_a_source_ram_renable <= 1;
        _mystream_a_source_count <= _mystream_a_source_size;
      end 
      if(_mystream_a_source_fsm_0 == 2) begin
        _mystream_a_source_ram_raddr <= _mystream_a_source_ram_raddr + _mystream_a_source_stride;
        _mystream_a_source_ram_renable <= 1;
        _mystream_a_source_count <= _mystream_a_source_count - 1;
      end 
      if((_mystream_a_source_fsm_0 == 2) && (_mystream_a_source_count == 1)) begin
        _mystream_a_source_ram_renable <= 0;
        _mystream_a_idle <= 1;
      end 
      _set_flag_18 <= 0;
      if(th_comp == 14) begin
        _set_flag_18 <= 1;
      end 
      if(_set_flag_18) begin
        _mystream_b_source_mode <= 3'b1;
        _mystream_b_source_offset <= _th_comp_offset_4;
        _mystream_b_source_size <= _th_comp_size_3;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_18) begin
        _mystream_b_source_ram_sel <= 2;
      end 
      __tmp_21_1 <= _tmp_21;
      _mystream_b_source_ram_rvalid <= __tmp_21_1;
      if(_mystream_b_source_ram_rvalid) begin
        __variable_wdata_1 <= _mystream_b_source_ram_rdata;
      end 
      if(_mystream_start && _mystream_b_source_mode & 3'b1) begin
        _mystream_b_idle <= 0;
      end 
      if(_mystream_b_source_fsm_1 == 1) begin
        _mystream_b_source_ram_raddr <= _mystream_b_source_offset;
        _mystream_b_source_ram_renable <= 1;
        _mystream_b_source_count <= _mystream_b_source_size;
      end 
      if(_mystream_b_source_fsm_1 == 2) begin
        _mystream_b_source_ram_raddr <= _mystream_b_source_ram_raddr + _mystream_b_source_stride;
        _mystream_b_source_ram_renable <= 1;
        _mystream_b_source_count <= _mystream_b_source_count - 1;
      end 
      if((_mystream_b_source_fsm_1 == 2) && (_mystream_b_source_count == 1)) begin
        _mystream_b_source_ram_renable <= 0;
        _mystream_b_idle <= 1;
      end 
      _set_flag_22 <= 0;
      if(th_comp == 15) begin
        _set_flag_22 <= 1;
      end 
      if(_set_flag_22) begin
        _mystream_c_sink_mode <= 3'b1;
        _mystream_c_sink_offset <= _th_comp_offset_4;
        _mystream_c_sink_size <= _th_comp_size_3;
        _mystream_c_sink_stride <= 1;
      end 
      if(_set_flag_22) begin
        _mystream_c_sink_ram_sel <= 3;
      end 
      if(_mystream_c_sink_fsm_2 == 0) begin
        _mystream_c_sink_wenable <= 0;
      end 
      if(_mystream_c_sink_fsm_2 == 1) begin
        _mystream_c_sink_waddr <= _mystream_c_sink_offset - _mystream_c_sink_stride;
        _mystream_c_sink_count <= _mystream_c_sink_size;
      end 
      if(_mystream_c_sink_fsm_2 == 12) begin
        _mystream_c_sink_wenable <= 0;
      end 
      if(_mystream_c_sink_fsm_2 == 12) begin
        _mystream_c_sink_waddr <= _mystream_c_sink_waddr + _mystream_c_sink_stride;
        _mystream_c_sink_wdata <= mystream_c_data;
        _mystream_c_sink_wenable <= 1;
        _mystream_c_sink_count <= _mystream_c_sink_count - 1;
      end 
      _set_flag_23 <= 0;
      if(th_comp == 16) begin
        _set_flag_23 <= 1;
      end 
      _set_flag_43 <= 0;
      if(th_comp == 33) begin
        _set_flag_43 <= 1;
      end 
      if(_set_flag_43) begin
        _mystream_a_source_mode <= 3'b1;
        _mystream_a_source_offset <= _th_comp_offset_6;
        _mystream_a_source_size <= _th_comp_size_5;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_43) begin
        _mystream_a_source_ram_sel <= 1;
      end 
      _set_flag_44 <= 0;
      if(th_comp == 34) begin
        _set_flag_44 <= 1;
      end 
      if(_set_flag_44) begin
        _mystream_b_source_mode <= 3'b1;
        _mystream_b_source_offset <= _th_comp_offset_6;
        _mystream_b_source_size <= _th_comp_size_5;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_44) begin
        _mystream_b_source_ram_sel <= 2;
      end 
      _set_flag_45 <= 0;
      if(th_comp == 35) begin
        _set_flag_45 <= 1;
      end 
      if(_set_flag_45) begin
        _mystream_c_sink_mode <= 3'b1;
        _mystream_c_sink_offset <= _th_comp_offset_6;
        _mystream_c_sink_size <= _th_comp_size_5;
        _mystream_c_sink_stride <= 1;
      end 
      if(_set_flag_45) begin
        _mystream_c_sink_ram_sel <= 3;
      end 
      _set_flag_46 <= 0;
      if(th_comp == 36) begin
        _set_flag_46 <= 1;
      end 
      _set_flag_50 <= 0;
      if(th_comp == 54) begin
        _set_flag_50 <= 1;
      end 
      if(_set_flag_50) begin
        _mystream_a_source_mode <= 3'b1;
        _mystream_a_source_offset <= _th_comp_offset_8;
        _mystream_a_source_size <= _th_comp_size_7;
        _mystream_a_source_stride <= 1;
      end 
      if(_set_flag_50) begin
        _mystream_a_source_ram_sel <= 1;
      end 
      _set_flag_51 <= 0;
      if(th_comp == 55) begin
        _set_flag_51 <= 1;
      end 
      if(_set_flag_51) begin
        _mystream_b_source_mode <= 3'b1;
        _mystream_b_source_offset <= _th_comp_offset_8;
        _mystream_b_source_size <= _th_comp_size_7;
        _mystream_b_source_stride <= 1;
      end 
      if(_set_flag_51) begin
        _mystream_b_source_ram_sel <= 2;
      end 
      _set_flag_52 <= 0;
      if(th_comp == 56) begin
        _set_flag_52 <= 1;
      end 
      if(_set_flag_52) begin
        _mystream_c_sink_mode <= 3'b1;
        _mystream_c_sink_offset <= _th_comp_offset_8;
        _mystream_c_sink_size <= _th_comp_size_7;
        _mystream_c_sink_stride <= 1;
      end 
      if(_set_flag_52) begin
        _mystream_c_sink_ram_sel <= 3;
      end 
      _set_flag_53 <= 0;
      if(th_comp == 57) begin
        _set_flag_53 <= 1;
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
  localparam _mystream_fsm_9 = 9;
  localparam _mystream_fsm_10 = 10;
  localparam _mystream_fsm_11 = 11;
  localparam _mystream_fsm_12 = 12;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_fsm <= _mystream_fsm_init;
      _mystream_start <= 0;
      _mystream_busy <= 0;
    end else begin
      case(_mystream_fsm)
        _mystream_fsm_init: begin
          if(_mystream_start_flag) begin
            _mystream_start <= 1;
            _mystream_busy <= 1;
          end 
          if(_mystream_start_flag) begin
            _mystream_fsm <= _mystream_fsm_1;
          end 
        end
        _mystream_fsm_1: begin
          _mystream_start <= 0;
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
          _mystream_fsm <= _mystream_fsm_8;
        end
        _mystream_fsm_8: begin
          _mystream_fsm <= _mystream_fsm_9;
        end
        _mystream_fsm_9: begin
          _mystream_fsm <= _mystream_fsm_10;
        end
        _mystream_fsm_10: begin
          _mystream_fsm <= _mystream_fsm_11;
        end
        _mystream_fsm_11: begin
          _mystream_fsm <= _mystream_fsm_12;
        end
        _mystream_fsm_12: begin
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
  localparam th_comp_55 = 55;
  localparam th_comp_56 = 56;
  localparam th_comp_57 = 57;
  localparam th_comp_58 = 58;
  localparam th_comp_59 = 59;
  localparam th_comp_60 = 60;
  localparam th_comp_61 = 61;
  localparam th_comp_62 = 62;
  localparam th_comp_63 = 63;
  localparam th_comp_64 = 64;
  localparam th_comp_65 = 65;
  localparam th_comp_66 = 66;
  localparam th_comp_67 = 67;
  localparam th_comp_68 = 68;
  localparam th_comp_69 = 69;
  localparam th_comp_70 = 70;
  localparam th_comp_71 = 71;
  localparam th_comp_72 = 72;
  localparam th_comp_73 = 73;
  localparam th_comp_74 = 74;
  localparam th_comp_75 = 75;
  localparam th_comp_76 = 76;
  localparam th_comp_77 = 77;
  localparam th_comp_78 = 78;
  localparam th_comp_79 = 79;
  localparam th_comp_80 = 80;
  localparam th_comp_81 = 81;
  localparam th_comp_82 = 82;
  localparam th_comp_83 = 83;
  localparam th_comp_84 = 84;
  localparam th_comp_85 = 85;
  localparam th_comp_86 = 86;
  localparam th_comp_87 = 87;
  localparam th_comp_88 = 88;
  localparam th_comp_89 = 89;
  localparam th_comp_90 = 90;
  localparam th_comp_91 = 91;
  localparam th_comp_92 = 92;
  localparam th_comp_93 = 93;
  localparam th_comp_94 = 94;
  localparam th_comp_95 = 95;
  localparam th_comp_96 = 96;
  localparam th_comp_97 = 97;
  localparam th_comp_98 = 98;
  localparam th_comp_99 = 99;
  localparam th_comp_100 = 100;
  localparam th_comp_101 = 101;
  localparam th_comp_102 = 102;
  localparam th_comp_103 = 103;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _d1_th_comp <= th_comp_init;
      _th_comp_size_0 <= 0;
      _th_comp_orig_size_1 <= 0;
      _th_comp_offset_2 <= 0;
      axim_flag_0 <= 0;
      _th_comp_cond_4_0_1 <= 0;
      axim_flag_8 <= 0;
      _th_comp_cond_8_1_1 <= 0;
      _th_comp_size_3 <= 0;
      _th_comp_offset_4 <= 0;
      axim_flag_24 <= 0;
      _th_comp_cond_19_2_1 <= 0;
      axim_flag_41 <= 0;
      _th_comp_cond_24_3_1 <= 0;
      axim_flag_42 <= 0;
      _th_comp_cond_28_4_1 <= 0;
      _th_comp_size_5 <= 0;
      _th_comp_offset_6 <= 0;
      axim_flag_47 <= 0;
      _th_comp_cond_39_5_1 <= 0;
      axim_flag_48 <= 0;
      _th_comp_cond_45_6_1 <= 0;
      axim_flag_49 <= 0;
      _th_comp_cond_49_7_1 <= 0;
      _th_comp_size_7 <= 0;
      _th_comp_offset_8 <= 0;
      axim_flag_54 <= 0;
      _th_comp_cond_60_8_1 <= 0;
      axim_flag_55 <= 0;
      _th_comp_cond_65_9_1 <= 0;
      axim_flag_56 <= 0;
      _th_comp_cond_69_10_1 <= 0;
      _th_comp_size_9 <= 0;
      _th_comp_offset_10 <= 0;
      _th_comp_sum_11 <= 0;
      _th_comp_i_12 <= 0;
      _tmp_58 <= 0;
      _th_comp_a_13 <= 0;
      _tmp_60 <= 0;
      _th_comp_b_14 <= 0;
      axim_flag_61 <= 0;
      _th_comp_cond_84_11_1 <= 0;
      _th_comp_size_15 <= 0;
      _th_comp_offset_stream_16 <= 0;
      _th_comp_offset_seq_17 <= 0;
      _th_comp_all_ok_18 <= 0;
      _th_comp_i_19 <= 0;
      _tmp_63 <= 0;
      _th_comp_st_20 <= 0;
      _tmp_65 <= 0;
      _th_comp_sq_21 <= 0;
    end else begin
      _d1_th_comp <= th_comp;
      case(_d1_th_comp)
        th_comp_4: begin
          if(_th_comp_cond_4_0_1) begin
            axim_flag_0 <= 0;
          end 
        end
        th_comp_8: begin
          if(_th_comp_cond_8_1_1) begin
            axim_flag_8 <= 0;
          end 
        end
        th_comp_19: begin
          if(_th_comp_cond_19_2_1) begin
            axim_flag_24 <= 0;
          end 
        end
        th_comp_24: begin
          if(_th_comp_cond_24_3_1) begin
            axim_flag_41 <= 0;
          end 
        end
        th_comp_28: begin
          if(_th_comp_cond_28_4_1) begin
            axim_flag_42 <= 0;
          end 
        end
        th_comp_39: begin
          if(_th_comp_cond_39_5_1) begin
            axim_flag_47 <= 0;
          end 
        end
        th_comp_45: begin
          if(_th_comp_cond_45_6_1) begin
            axim_flag_48 <= 0;
          end 
        end
        th_comp_49: begin
          if(_th_comp_cond_49_7_1) begin
            axim_flag_49 <= 0;
          end 
        end
        th_comp_60: begin
          if(_th_comp_cond_60_8_1) begin
            axim_flag_54 <= 0;
          end 
        end
        th_comp_65: begin
          if(_th_comp_cond_65_9_1) begin
            axim_flag_55 <= 0;
          end 
        end
        th_comp_69: begin
          if(_th_comp_cond_69_10_1) begin
            axim_flag_56 <= 0;
          end 
        end
        th_comp_84: begin
          if(_th_comp_cond_84_11_1) begin
            axim_flag_61 <= 0;
          end 
        end
      endcase
      case(th_comp)
        th_comp_init: begin
          _th_comp_size_0 <= 32;
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_orig_size_1 <= _th_comp_size_0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          _th_comp_size_0 <= _th_comp_size_0 + _th_comp_size_0;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          _th_comp_offset_2 <= _th_comp_size_0 + _th_comp_size_0;
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          axim_flag_0 <= 1;
          _th_comp_cond_4_0_1 <= 1;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          th_comp <= th_comp_6;
        end
        th_comp_6: begin
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_8;
          end 
        end
        th_comp_8: begin
          axim_flag_8 <= 1;
          _th_comp_cond_8_1_1 <= 1;
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          th_comp <= th_comp_10;
        end
        th_comp_10: begin
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_12;
          end 
        end
        th_comp_12: begin
          _th_comp_size_3 <= _th_comp_size_0;
          _th_comp_offset_4 <= _th_comp_offset_2;
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          th_comp <= th_comp_14;
        end
        th_comp_14: begin
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          axim_flag_24 <= 1;
          _th_comp_cond_19_2_1 <= 1;
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          th_comp <= th_comp_21;
        end
        th_comp_21: begin
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_23;
          end 
        end
        th_comp_23: begin
          _th_comp_offset_2 <= _th_comp_size_0 + _th_comp_size_0 + _th_comp_size_0;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          axim_flag_41 <= 1;
          _th_comp_cond_24_3_1 <= 1;
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          th_comp <= th_comp_26;
        end
        th_comp_26: begin
          th_comp <= th_comp_27;
        end
        th_comp_27: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_28;
          end 
        end
        th_comp_28: begin
          axim_flag_42 <= 1;
          _th_comp_cond_28_4_1 <= 1;
          th_comp <= th_comp_29;
        end
        th_comp_29: begin
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_32;
          end 
        end
        th_comp_32: begin
          _th_comp_size_5 <= _th_comp_size_0;
          _th_comp_offset_6 <= _th_comp_offset_2;
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          th_comp <= th_comp_34;
        end
        th_comp_34: begin
          th_comp <= th_comp_35;
        end
        th_comp_35: begin
          th_comp <= th_comp_36;
        end
        th_comp_36: begin
          th_comp <= th_comp_37;
        end
        th_comp_37: begin
          th_comp <= th_comp_38;
        end
        th_comp_38: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_39;
          end 
        end
        th_comp_39: begin
          axim_flag_47 <= 1;
          _th_comp_cond_39_5_1 <= 1;
          th_comp <= th_comp_40;
        end
        th_comp_40: begin
          th_comp <= th_comp_41;
        end
        th_comp_41: begin
          th_comp <= th_comp_42;
        end
        th_comp_42: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_43;
          end 
        end
        th_comp_43: begin
          _th_comp_size_0 <= _th_comp_orig_size_1;
          th_comp <= th_comp_44;
        end
        th_comp_44: begin
          _th_comp_offset_2 <= 0;
          th_comp <= th_comp_45;
        end
        th_comp_45: begin
          axim_flag_48 <= 1;
          _th_comp_cond_45_6_1 <= 1;
          th_comp <= th_comp_46;
        end
        th_comp_46: begin
          th_comp <= th_comp_47;
        end
        th_comp_47: begin
          th_comp <= th_comp_48;
        end
        th_comp_48: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_49;
          end 
        end
        th_comp_49: begin
          axim_flag_49 <= 1;
          _th_comp_cond_49_7_1 <= 1;
          th_comp <= th_comp_50;
        end
        th_comp_50: begin
          th_comp <= th_comp_51;
        end
        th_comp_51: begin
          th_comp <= th_comp_52;
        end
        th_comp_52: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_53;
          end 
        end
        th_comp_53: begin
          _th_comp_size_7 <= _th_comp_size_0;
          _th_comp_offset_8 <= _th_comp_offset_2;
          th_comp <= th_comp_54;
        end
        th_comp_54: begin
          th_comp <= th_comp_55;
        end
        th_comp_55: begin
          th_comp <= th_comp_56;
        end
        th_comp_56: begin
          th_comp <= th_comp_57;
        end
        th_comp_57: begin
          th_comp <= th_comp_58;
        end
        th_comp_58: begin
          th_comp <= th_comp_59;
        end
        th_comp_59: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_60;
          end 
        end
        th_comp_60: begin
          axim_flag_54 <= 1;
          _th_comp_cond_60_8_1 <= 1;
          th_comp <= th_comp_61;
        end
        th_comp_61: begin
          th_comp <= th_comp_62;
        end
        th_comp_62: begin
          th_comp <= th_comp_63;
        end
        th_comp_63: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_64;
          end 
        end
        th_comp_64: begin
          _th_comp_offset_2 <= _th_comp_size_0;
          th_comp <= th_comp_65;
        end
        th_comp_65: begin
          axim_flag_55 <= 1;
          _th_comp_cond_65_9_1 <= 1;
          th_comp <= th_comp_66;
        end
        th_comp_66: begin
          th_comp <= th_comp_67;
        end
        th_comp_67: begin
          th_comp <= th_comp_68;
        end
        th_comp_68: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_69;
          end 
        end
        th_comp_69: begin
          axim_flag_56 <= 1;
          _th_comp_cond_69_10_1 <= 1;
          th_comp <= th_comp_70;
        end
        th_comp_70: begin
          th_comp <= th_comp_71;
        end
        th_comp_71: begin
          th_comp <= th_comp_72;
        end
        th_comp_72: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_73;
          end 
        end
        th_comp_73: begin
          _th_comp_size_9 <= _th_comp_size_0;
          _th_comp_offset_10 <= _th_comp_offset_2;
          th_comp <= th_comp_74;
        end
        th_comp_74: begin
          _th_comp_sum_11 <= 0;
          th_comp <= th_comp_75;
        end
        th_comp_75: begin
          _th_comp_i_12 <= 0;
          th_comp <= th_comp_76;
        end
        th_comp_76: begin
          if(_th_comp_i_12 < _th_comp_size_9) begin
            th_comp <= th_comp_77;
          end else begin
            th_comp <= th_comp_84;
          end
        end
        th_comp_77: begin
          if(_tmp_57) begin
            _tmp_58 <= ram_a_0_rdata;
          end 
          if(_tmp_57) begin
            th_comp <= th_comp_78;
          end 
        end
        th_comp_78: begin
          _th_comp_a_13 <= _tmp_58;
          th_comp <= th_comp_79;
        end
        th_comp_79: begin
          if(_tmp_59) begin
            _tmp_60 <= ram_b_0_rdata;
          end 
          if(_tmp_59) begin
            th_comp <= th_comp_80;
          end 
        end
        th_comp_80: begin
          _th_comp_b_14 <= _tmp_60;
          th_comp <= th_comp_81;
        end
        th_comp_81: begin
          _th_comp_sum_11 <= _th_comp_a_13 * _th_comp_b_14;
          th_comp <= th_comp_82;
        end
        th_comp_82: begin
          th_comp <= th_comp_83;
        end
        th_comp_83: begin
          _th_comp_i_12 <= _th_comp_i_12 + 1;
          th_comp <= th_comp_76;
        end
        th_comp_84: begin
          axim_flag_61 <= 1;
          _th_comp_cond_84_11_1 <= 1;
          th_comp <= th_comp_85;
        end
        th_comp_85: begin
          th_comp <= th_comp_86;
        end
        th_comp_86: begin
          th_comp <= th_comp_87;
        end
        th_comp_87: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_88;
          end 
        end
        th_comp_88: begin
          _th_comp_size_15 <= _th_comp_size_0;
          _th_comp_offset_stream_16 <= 0;
          _th_comp_offset_seq_17 <= _th_comp_offset_2;
          th_comp <= th_comp_89;
        end
        th_comp_89: begin
          _th_comp_all_ok_18 <= 1;
          th_comp <= th_comp_90;
        end
        th_comp_90: begin
          _th_comp_i_19 <= 0;
          th_comp <= th_comp_91;
        end
        th_comp_91: begin
          if(_th_comp_i_19 < _th_comp_size_15) begin
            th_comp <= th_comp_92;
          end else begin
            th_comp <= th_comp_99;
          end
        end
        th_comp_92: begin
          if(_tmp_62) begin
            _tmp_63 <= ram_c_0_rdata;
          end 
          if(_tmp_62) begin
            th_comp <= th_comp_93;
          end 
        end
        th_comp_93: begin
          _th_comp_st_20 <= _tmp_63;
          th_comp <= th_comp_94;
        end
        th_comp_94: begin
          if(_tmp_64) begin
            _tmp_65 <= ram_c_0_rdata;
          end 
          if(_tmp_64) begin
            th_comp <= th_comp_95;
          end 
        end
        th_comp_95: begin
          _th_comp_sq_21 <= _tmp_65;
          th_comp <= th_comp_96;
        end
        th_comp_96: begin
          if(_th_comp_st_20 !== _th_comp_sq_21) begin
            th_comp <= th_comp_97;
          end else begin
            th_comp <= th_comp_98;
          end
        end
        th_comp_97: begin
          _th_comp_all_ok_18 <= 0;
          th_comp <= th_comp_98;
        end
        th_comp_98: begin
          _th_comp_i_19 <= _th_comp_i_19 + 1;
          th_comp <= th_comp_91;
        end
        th_comp_99: begin
          if(_th_comp_all_ok_18) begin
            th_comp <= th_comp_100;
          end else begin
            th_comp <= th_comp_102;
          end
        end
        th_comp_100: begin
          $display("OK");
          th_comp <= th_comp_101;
        end
        th_comp_101: begin
          th_comp <= th_comp_103;
        end
        th_comp_102: begin
          $display("NG");
          th_comp <= th_comp_103;
        end
      endcase
    end
  end

  localparam _myaxi_read_fsm_1 = 1;
  localparam _myaxi_read_fsm_2 = 2;
  localparam _myaxi_read_fsm_3 = 3;
  localparam _myaxi_read_fsm_4 = 4;
  localparam _myaxi_read_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_fsm <= _myaxi_read_fsm_init;
      _d1__myaxi_read_fsm <= _myaxi_read_fsm_init;
      _myaxi_read_cur_global_addr <= 0;
      _myaxi_read_rest_size <= 0;
      _myaxi_read_cur_size <= 0;
      __myaxi_read_fsm_cond_3_0_1 <= 0;
      _wvalid_2 <= 0;
      _wdata_1 <= 0;
      axim_flag_7 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
      __myaxi_read_fsm_cond_3_2_1 <= 0;
      _wvalid_10 <= 0;
      _wdata_9 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_2 <= 0;
          end 
          if(__myaxi_read_fsm_cond_3_2_1) begin
            _wvalid_10 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_7 <= 0;
          end 
        end
      endcase
      case(_myaxi_read_fsm)
        _myaxi_read_fsm_init: begin
          if(_myaxi_read_start) begin
            _myaxi_read_cur_global_addr <= (_myaxi_read_global_addr >> 2) << 2;
            _myaxi_read_rest_size <= _myaxi_read_size;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 1)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 2)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
        end
        _myaxi_read_fsm_1: begin
          if((_myaxi_read_rest_size <= 256) && ((_myaxi_read_cur_global_addr & 4095) + (_myaxi_read_rest_size << 2) >= 4096)) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 2;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 2);
          end else if(_myaxi_read_rest_size <= 256) begin
            _myaxi_read_cur_size <= _myaxi_read_rest_size;
            _myaxi_read_rest_size <= 0;
          end else if((_myaxi_read_cur_global_addr & 4095) + 1024 >= 4096) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 2;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 2);
          end else begin
            _myaxi_read_cur_size <= 256;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - 256;
          end
          _myaxi_read_fsm <= _myaxi_read_fsm_2;
        end
        _myaxi_read_fsm_2: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_3;
          end 
        end
        _myaxi_read_fsm_3: begin
          __myaxi_read_fsm_cond_3_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 1)) begin
            _wdata_1 <= myaxi_rdata;
            _wvalid_2 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 2);
          end 
          __myaxi_read_fsm_cond_3_2_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 2)) begin
            _wdata_9 <= myaxi_rdata;
            _wvalid_10 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_7 <= 1;
          __myaxi_read_fsm_cond_4_1_1 <= 1;
          _myaxi_read_fsm <= _myaxi_read_fsm_5;
        end
        _myaxi_read_fsm_5: begin
          _myaxi_read_fsm <= _myaxi_read_fsm_init;
        end
      endcase
    end
  end

  localparam _mystream_a_source_fsm_0_1 = 1;
  localparam _mystream_a_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
    end else begin
      case(_mystream_a_source_fsm_0)
        _mystream_a_source_fsm_0_init: begin
          if(_mystream_start && _mystream_a_source_mode & 3'b1) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_1;
          end 
        end
        _mystream_a_source_fsm_0_1: begin
          _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_2;
        end
        _mystream_a_source_fsm_0_2: begin
          if(_mystream_a_source_count == 1) begin
            _mystream_a_source_fsm_0 <= _mystream_a_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_b_source_fsm_1_1 = 1;
  localparam _mystream_b_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
    end else begin
      case(_mystream_b_source_fsm_1)
        _mystream_b_source_fsm_1_init: begin
          if(_mystream_start && _mystream_b_source_mode & 3'b1) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_1;
          end 
        end
        _mystream_b_source_fsm_1_1: begin
          _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_2;
        end
        _mystream_b_source_fsm_1_2: begin
          if(_mystream_b_source_count == 1) begin
            _mystream_b_source_fsm_1 <= _mystream_b_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_c_sink_fsm_2_1 = 1;
  localparam _mystream_c_sink_fsm_2_2 = 2;
  localparam _mystream_c_sink_fsm_2_3 = 3;
  localparam _mystream_c_sink_fsm_2_4 = 4;
  localparam _mystream_c_sink_fsm_2_5 = 5;
  localparam _mystream_c_sink_fsm_2_6 = 6;
  localparam _mystream_c_sink_fsm_2_7 = 7;
  localparam _mystream_c_sink_fsm_2_8 = 8;
  localparam _mystream_c_sink_fsm_2_9 = 9;
  localparam _mystream_c_sink_fsm_2_10 = 10;
  localparam _mystream_c_sink_fsm_2_11 = 11;
  localparam _mystream_c_sink_fsm_2_12 = 12;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
    end else begin
      case(_mystream_c_sink_fsm_2)
        _mystream_c_sink_fsm_2_init: begin
          if(_mystream_start && _mystream_c_sink_mode & 3'b1) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_1;
          end 
        end
        _mystream_c_sink_fsm_2_1: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_2;
        end
        _mystream_c_sink_fsm_2_2: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_3;
        end
        _mystream_c_sink_fsm_2_3: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_4;
        end
        _mystream_c_sink_fsm_2_4: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_5;
        end
        _mystream_c_sink_fsm_2_5: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_6;
        end
        _mystream_c_sink_fsm_2_6: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_7;
        end
        _mystream_c_sink_fsm_2_7: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_8;
        end
        _mystream_c_sink_fsm_2_8: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_9;
        end
        _mystream_c_sink_fsm_2_9: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_10;
        end
        _mystream_c_sink_fsm_2_10: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_11;
        end
        _mystream_c_sink_fsm_2_11: begin
          _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_12;
        end
        _mystream_c_sink_fsm_2_12: begin
          if(_mystream_c_sink_count == 1) begin
            _mystream_c_sink_fsm_2 <= _mystream_c_sink_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _myaxi_write_fsm_1 = 1;
  localparam _myaxi_write_fsm_2 = 2;
  localparam _myaxi_write_fsm_3 = 3;
  localparam _myaxi_write_fsm_4 = 4;
  localparam _myaxi_write_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_fsm <= _myaxi_write_fsm_init;
      _d1__myaxi_write_fsm <= _myaxi_write_fsm_init;
      _myaxi_write_cur_global_addr <= 0;
      _myaxi_write_rest_size <= 0;
      _myaxi_write_cur_size <= 0;
      axim_flag_40 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_40 <= 0;
          end 
        end
      endcase
      case(_myaxi_write_fsm)
        _myaxi_write_fsm_init: begin
          if(_myaxi_write_start) begin
            _myaxi_write_cur_global_addr <= (_myaxi_write_global_addr >> 2) << 2;
            _myaxi_write_rest_size <= _myaxi_write_size;
          end 
          if(_myaxi_write_start && (_myaxi_write_op_sel == 1)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
        end
        _myaxi_write_fsm_1: begin
          if((_myaxi_write_rest_size <= 256) && ((_myaxi_write_cur_global_addr & 4095) + (_myaxi_write_rest_size << 2) >= 4096)) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 2;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 2);
          end else if(_myaxi_write_rest_size <= 256) begin
            _myaxi_write_cur_size <= _myaxi_write_rest_size;
            _myaxi_write_rest_size <= 0;
          end else if((_myaxi_write_cur_global_addr & 4095) + 1024 >= 4096) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 2;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 2);
          end else begin
            _myaxi_write_cur_size <= 256;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - 256;
          end
          _myaxi_write_fsm <= _myaxi_write_fsm_2;
        end
        _myaxi_write_fsm_2: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_3;
          end 
        end
        _myaxi_write_fsm_3: begin
          if(_myaxi_write_data_done) begin
            _myaxi_write_cur_global_addr <= _myaxi_write_cur_global_addr + (_myaxi_write_cur_size << 2);
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size > 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size == 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_4;
          end 
        end
        _myaxi_write_fsm_4: begin
          axim_flag_40 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
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
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);


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

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_stream_multicall.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
