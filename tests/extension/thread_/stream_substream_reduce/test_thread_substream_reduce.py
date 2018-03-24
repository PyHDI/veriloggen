from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_substream_reduce

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

  reg [10-1:0] ram_d_0_addr;
  wire [32-1:0] ram_d_0_rdata;
  reg [32-1:0] ram_d_0_wdata;
  reg ram_d_0_wenable;

  ram_d
  inst_ram_d
  (
    .CLK(CLK),
    .ram_d_0_addr(ram_d_0_addr),
    .ram_d_0_rdata(ram_d_0_rdata),
    .ram_d_0_wdata(ram_d_0_wdata),
    .ram_d_0_wenable(ram_d_0_wenable)
  );

  reg [32-1:0] _macstream_fsm;
  localparam _macstream_fsm_init = 0;
  wire _macstream_start_flag;
  reg _macstream_start;
  reg _macstream_busy;
  reg _macstream_a_idle;
  reg _macstream_a_source_mode;
  reg [32-1:0] _macstream_a_source_offset;
  reg [33-1:0] _macstream_a_source_size;
  reg [32-1:0] _macstream_a_source_stride;
  reg [33-1:0] _macstream_a_source_count;
  reg [8-1:0] _macstream_a_source_ram_sel;
  reg [32-1:0] _macstream_a_source_ram_raddr;
  reg _macstream_a_source_ram_renable;
  wire [32-1:0] _macstream_a_source_ram_rdata;
  reg _macstream_a_source_ram_rvalid;
  reg _macstream_b_idle;
  reg _macstream_b_source_mode;
  reg [32-1:0] _macstream_b_source_offset;
  reg [33-1:0] _macstream_b_source_size;
  reg [32-1:0] _macstream_b_source_stride;
  reg [33-1:0] _macstream_b_source_count;
  reg [8-1:0] _macstream_b_source_ram_sel;
  reg [32-1:0] _macstream_b_source_ram_raddr;
  reg _macstream_b_source_ram_renable;
  wire [32-1:0] _macstream_b_source_ram_rdata;
  reg _macstream_b_source_ram_rvalid;
  reg _macstream_reduce_reset;
  reg _macstream_c_sink_mode;
  reg [32-1:0] _macstream_c_sink_offset;
  reg [33-1:0] _macstream_c_sink_size;
  reg [32-1:0] _macstream_c_sink_stride;
  reg [33-1:0] _macstream_c_sink_count;
  reg [8-1:0] _macstream_c_sink_ram_sel;
  reg [32-1:0] _macstream_c_sink_waddr;
  reg _macstream_c_sink_wenable;
  reg [32-1:0] _macstream_c_sink_wdata;
  reg _macstream_v_sink_mode;
  reg [32-1:0] _macstream_v_sink_offset;
  reg [33-1:0] _macstream_v_sink_size;
  reg [32-1:0] _macstream_v_sink_stride;
  reg [33-1:0] _macstream_v_sink_count;
  reg [8-1:0] _macstream_v_sink_ram_sel;
  reg [32-1:0] _macstream_v_sink_waddr;
  reg _macstream_v_sink_wenable;
  reg [32-1:0] _macstream_v_sink_wdata;
  reg [32-1:0] _mystream_fsm;
  localparam _mystream_fsm_init = 0;
  wire _mystream_start_flag;
  reg _mystream_start;
  reg _mystream_busy;
  reg _mystream_x_idle;
  reg _mystream_x_source_mode;
  reg [32-1:0] _mystream_x_source_offset;
  reg [33-1:0] _mystream_x_source_size;
  reg [32-1:0] _mystream_x_source_stride;
  reg [33-1:0] _mystream_x_source_count;
  reg [8-1:0] _mystream_x_source_ram_sel;
  reg [32-1:0] _mystream_x_source_ram_raddr;
  reg _mystream_x_source_ram_renable;
  wire [32-1:0] _mystream_x_source_ram_rdata;
  reg _mystream_x_source_ram_rvalid;
  reg _mystream_y_idle;
  reg _mystream_y_source_mode;
  reg [32-1:0] _mystream_y_source_offset;
  reg [33-1:0] _mystream_y_source_size;
  reg [32-1:0] _mystream_y_source_stride;
  reg [33-1:0] _mystream_y_source_count;
  reg [8-1:0] _mystream_y_source_ram_sel;
  reg [32-1:0] _mystream_y_source_ram_raddr;
  reg _mystream_y_source_ram_renable;
  wire [32-1:0] _mystream_y_source_ram_rdata;
  reg _mystream_y_source_ram_rvalid;
  wire signed [32-1:0] macstream_a_data;
  wire signed [32-1:0] macstream_b_data;
  wire signed [32-1:0] macstream_const_data;
  wire signed [64-1:0] _times_mul_odata_3;
  reg signed [64-1:0] _times_mul_odata_reg_3;
  wire signed [32-1:0] _times_data_3;
  assign _times_data_3 = _times_mul_odata_reg_3;
  wire _times_mul_update_3;
  assign _times_mul_update_3 = 1;

  multiplier_0
  _times_mul_3
  (
    .CLK(CLK),
    .update(_times_mul_update_3),
    .a(macstream_a_data),
    .b(macstream_b_data),
    .c(_times_mul_odata_3)
  );

  reg signed [1-1:0] __delay_data_15;
  reg signed [1-1:0] __delay_data_16;
  reg signed [1-1:0] __delay_data_17;
  reg signed [1-1:0] __delay_data_18;
  reg signed [1-1:0] __delay_data_19;
  reg signed [1-1:0] __delay_data_20;
  reg signed [1-1:0] __delay_data_21;
  reg signed [32-1:0] _reduceadd_data_6;
  reg [33-1:0] _reduceadd_count_6;
  reg [1-1:0] _pulse_data_8;
  reg [33-1:0] _pulse_count_8;
  reg [1-1:0] _plus_data_9;
  reg signed [32-1:0] __delay_data_22;
  wire [1-1:0] macstream_v_data;
  assign macstream_v_data = _plus_data_9;
  wire signed [32-1:0] macstream_c_data;
  assign macstream_c_data = __delay_data_22;
  reg _substream_macstream_a_data_cond_14_0;
  reg _substream_macstream_b_data_cond_14_1;
  reg _substream_macstream_const_data_cond_14_2;
  reg _mystream_z_sink_mode;
  reg [32-1:0] _mystream_z_sink_offset;
  reg [33-1:0] _mystream_z_sink_size;
  reg [32-1:0] _mystream_z_sink_stride;
  reg [33-1:0] _mystream_z_sink_count;
  reg [8-1:0] _mystream_z_sink_ram_sel;
  reg [32-1:0] _mystream_z_sink_waddr;
  reg _mystream_z_sink_wenable;
  reg [32-1:0] _mystream_z_sink_wdata;
  reg _mystream_v_sink_mode;
  reg [32-1:0] _mystream_v_sink_offset;
  reg [33-1:0] _mystream_v_sink_size;
  reg [32-1:0] _mystream_v_sink_stride;
  reg [33-1:0] _mystream_v_sink_count;
  reg [8-1:0] _mystream_v_sink_ram_sel;
  reg [32-1:0] _mystream_v_sink_waddr;
  reg _mystream_v_sink_wenable;
  reg [32-1:0] _mystream_v_sink_wdata;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_3;
  reg signed [32-1:0] _th_comp_offset_4;
  reg axim_flag_0;
  reg [32-1:0] _d1_th_comp;
  reg _th_comp_cond_2_0_1;
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
  reg _th_comp_cond_6_1_1;
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
  reg signed [32-1:0] _th_comp_size_5;
  reg signed [32-1:0] _th_comp_offset_6;
  reg _set_flag_14;
  reg _tmp_15;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  assign _macstream_a_source_ram_rdata = (_macstream_a_source_ram_sel == 1)? ram_a_0_rdata : 0;
  localparam _tmp_16 = 1;
  wire [_tmp_16-1:0] _tmp_17;
  assign _tmp_17 = _macstream_a_source_ram_renable && (_macstream_a_source_ram_sel == 1);
  reg [_tmp_16-1:0] __tmp_17_1;
  reg signed [32-1:0] __variable_wdata_0;
  assign macstream_a_data = __variable_wdata_0;
  reg [32-1:0] _macstream_a_source_fsm_0;
  localparam _macstream_a_source_fsm_0_init = 0;
  reg _set_flag_18;
  reg _tmp_19;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  assign _macstream_b_source_ram_rdata = (_macstream_b_source_ram_sel == 2)? ram_b_0_rdata : 0;
  localparam _tmp_20 = 1;
  wire [_tmp_20-1:0] _tmp_21;
  assign _tmp_21 = _macstream_b_source_ram_renable && (_macstream_b_source_ram_sel == 2);
  reg [_tmp_20-1:0] __tmp_21_1;
  reg signed [32-1:0] __variable_wdata_1;
  assign macstream_b_data = __variable_wdata_1;
  reg [32-1:0] _macstream_b_source_fsm_1;
  localparam _macstream_b_source_fsm_1_init = 0;
  reg _set_flag_22;
  reg signed [32-1:0] __parametervariable_wdata_2;
  assign macstream_const_data = __parametervariable_wdata_2;
  reg _set_flag_23;
  reg _ram_c_cond_0_1;
  reg [32-1:0] _macstream_c_sink_fsm_2;
  localparam _macstream_c_sink_fsm_2_init = 0;
  reg _set_flag_24;
  reg _ram_d_cond_0_1;
  reg [32-1:0] _macstream_v_sink_fsm_3;
  localparam _macstream_v_sink_fsm_3_init = 0;
  reg _set_flag_25;
  assign _macstream_start_flag = (_set_flag_25)? 1 : 0;
  reg __macstream_start_flag_1;
  reg __macstream_start_flag_2;
  reg __macstream_start_flag_3;
  reg __macstream_start_flag_4;
  reg __macstream_start_flag_5;
  wire _macstream_done;
  assign _macstream_done = _macstream_a_idle && _macstream_b_idle;
  reg axim_flag_26;
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
  reg _tmp_27;
  reg _tmp_28;
  wire _tmp_29;
  wire _tmp_30;
  assign _tmp_30 = 1;
  localparam _tmp_31 = 1;
  wire [_tmp_31-1:0] _tmp_32;
  assign _tmp_32 = (_tmp_29 || !_tmp_27) && (_tmp_30 || !_tmp_28);
  reg [_tmp_31-1:0] __tmp_32_1;
  wire signed [32-1:0] _tmp_33;
  reg signed [32-1:0] __tmp_33_1;
  assign _tmp_33 = (__tmp_32_1)? ram_c_0_rdata : __tmp_33_1;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg _tmp_37;
  reg [34-1:0] _tmp_38;
  reg [9-1:0] _tmp_39;
  reg _myaxi_cond_1_1;
  reg _tmp_40;
  wire [32-1:0] __variable_data_41;
  wire __variable_valid_41;
  wire __variable_ready_41;
  assign __variable_ready_41 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_2_1;
  assign _myaxi_write_data_done = (_tmp_40 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_42;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg axim_flag_43;
  reg _th_comp_cond_24_3_1;
  reg axim_flag_44;
  reg _th_comp_cond_28_4_1;
  reg signed [32-1:0] _th_comp_size_7;
  reg signed [32-1:0] _th_comp_offset_8;
  reg signed [32-1:0] _th_comp_sum_9;
  reg signed [32-1:0] _th_comp_count_10;
  reg signed [32-1:0] _th_comp_i_11;
  reg _tmp_45;
  reg _ram_a_cond_3_1;
  reg _ram_a_cond_4_1;
  reg _ram_a_cond_4_2;
  reg signed [32-1:0] _tmp_46;
  reg signed [32-1:0] _th_comp_a_12;
  reg _tmp_47;
  reg _ram_b_cond_3_1;
  reg _ram_b_cond_4_1;
  reg _ram_b_cond_4_2;
  reg signed [32-1:0] _tmp_48;
  reg signed [32-1:0] _th_comp_b_13;
  reg _ram_c_cond_1_1;
  reg _ram_d_cond_1_1;
  reg axim_flag_49;
  reg _th_comp_cond_49_5_1;
  reg signed [32-1:0] _th_comp_size_14;
  reg signed [32-1:0] _th_comp_offset_stream_15;
  reg signed [32-1:0] _th_comp_offset_seq_16;
  reg signed [32-1:0] _th_comp_all_ok_17;
  reg signed [32-1:0] _th_comp_i_18;
  reg _tmp_50;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_51;
  reg signed [32-1:0] _th_comp_st_19;
  reg _tmp_52;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_53;
  reg signed [32-1:0] _th_comp_sq_20;
  reg axim_flag_54;
  reg _th_comp_cond_71_6_1;
  reg axim_flag_55;
  reg _th_comp_cond_75_7_1;
  reg signed [32-1:0] _th_comp_size_21;
  reg signed [32-1:0] _th_comp_offset_22;
  wire signed [32-1:0] mystream_x_data;
  wire signed [32-1:0] mystream_y_data;
  wire signed [32-1:0] mystream_const_data;
  reg signed [32-1:0] __delay_data_26;
  reg signed [32-1:0] __delay_data_27;
  reg signed [32-1:0] __delay_data_28;
  reg signed [32-1:0] __delay_data_29;
  reg signed [32-1:0] __delay_data_30;
  reg signed [32-1:0] __delay_data_31;
  reg signed [32-1:0] __delay_data_32;
  reg signed [32-1:0] __delay_data_33;
  reg signed [32-1:0] __delay_data_34;
  reg signed [32-1:0] __delay_data_35;
  reg signed [32-1:0] __substreamoutput_data_23;
  reg [1-1:0] __substreamoutput_data_24;
  reg signed [32-1:0] __delay_data_36;
  reg signed [32-1:0] _plus_data_25;
  reg [1-1:0] __delay_data_37;
  wire signed [32-1:0] mystream_z_data;
  assign mystream_z_data = _plus_data_25;
  wire [1-1:0] mystream_v_data;
  assign mystream_v_data = __delay_data_37;
  reg _set_flag_56;
  reg _tmp_57;
  reg _ram_a_cond_5_1;
  reg _ram_a_cond_6_1;
  reg _ram_a_cond_6_2;
  assign _mystream_x_source_ram_rdata = (_mystream_x_source_ram_sel == 1)? ram_a_0_rdata : 0;
  localparam _tmp_58 = 1;
  wire [_tmp_58-1:0] _tmp_59;
  assign _tmp_59 = _mystream_x_source_ram_renable && (_mystream_x_source_ram_sel == 1);
  reg [_tmp_58-1:0] __tmp_59_1;
  reg signed [32-1:0] __variable_wdata_11;
  assign mystream_x_data = __variable_wdata_11;
  reg [32-1:0] _mystream_x_source_fsm_0;
  localparam _mystream_x_source_fsm_0_init = 0;
  reg _set_flag_60;
  reg _tmp_61;
  reg _ram_b_cond_5_1;
  reg _ram_b_cond_6_1;
  reg _ram_b_cond_6_2;
  assign _mystream_y_source_ram_rdata = (_mystream_y_source_ram_sel == 2)? ram_b_0_rdata : 0;
  localparam _tmp_62 = 1;
  wire [_tmp_62-1:0] _tmp_63;
  assign _tmp_63 = _mystream_y_source_ram_renable && (_mystream_y_source_ram_sel == 2);
  reg [_tmp_62-1:0] __tmp_63_1;
  reg signed [32-1:0] __variable_wdata_12;
  assign mystream_y_data = __variable_wdata_12;
  reg [32-1:0] _mystream_y_source_fsm_1;
  localparam _mystream_y_source_fsm_1_init = 0;
  reg _set_flag_64;
  reg signed [32-1:0] __parametervariable_wdata_13;
  assign mystream_const_data = __parametervariable_wdata_13;
  reg _set_flag_65;
  reg _ram_c_cond_6_1;
  reg [32-1:0] _mystream_z_sink_fsm_2;
  localparam _mystream_z_sink_fsm_2_init = 0;
  reg _set_flag_66;
  assign _mystream_start_flag = (_set_flag_66)? 1 : 0;
  reg __mystream_start_flag_1;
  reg __mystream_start_flag_2;
  reg __mystream_start_flag_3;
  reg __mystream_start_flag_4;
  reg __mystream_start_flag_5;
  reg __mystream_start_flag_6;
  wire _mystream_done;
  assign _mystream_done = _mystream_x_idle && _mystream_y_idle;
  reg axim_flag_67;
  reg _th_comp_cond_87_8_1;
  reg axim_flag_68;
  reg _th_comp_cond_92_9_1;
  reg axim_flag_69;
  reg _th_comp_cond_96_10_1;
  reg signed [32-1:0] _th_comp_size_23;
  reg signed [32-1:0] _th_comp_offset_24;
  reg signed [32-1:0] _th_comp_sum_25;
  reg signed [32-1:0] _th_comp_count_26;
  reg signed [32-1:0] _th_comp_write_offset_27;
  reg signed [32-1:0] _th_comp_i_28;
  reg _tmp_70;
  reg _ram_a_cond_7_1;
  reg _ram_a_cond_8_1;
  reg _ram_a_cond_8_2;
  reg signed [32-1:0] _tmp_71;
  reg signed [32-1:0] _th_comp_x_29;
  reg _tmp_72;
  reg _ram_b_cond_7_1;
  reg _ram_b_cond_8_1;
  reg _ram_b_cond_8_2;
  reg signed [32-1:0] _tmp_73;
  reg signed [32-1:0] _th_comp_y_30;
  reg signed [32-1:0] _th_comp_val_31;
  reg _ram_c_cond_7_1;
  reg axim_flag_74;
  reg _th_comp_cond_119_11_1;
  reg signed [32-1:0] _th_comp_size_32;
  reg signed [32-1:0] _th_comp_offset_stream_33;
  reg signed [32-1:0] _th_comp_offset_seq_34;
  reg signed [32-1:0] _th_comp_all_ok_35;
  reg signed [32-1:0] _th_comp_i_36;
  reg _tmp_75;
  reg _ram_c_cond_8_1;
  reg _ram_c_cond_9_1;
  reg _ram_c_cond_9_2;
  reg signed [32-1:0] _tmp_76;
  reg signed [32-1:0] _th_comp_st_37;
  reg _tmp_77;
  reg _ram_c_cond_10_1;
  reg _ram_c_cond_11_1;
  reg _ram_c_cond_11_2;
  reg signed [32-1:0] _tmp_78;
  reg signed [32-1:0] _th_comp_sq_38;

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
      _tmp_39 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_40 <= 0;
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
        _tmp_40 <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_ram_a_0_read_start <= 0;
      if(axim_flag_0) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_3;
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
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_3;
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
      if(axim_flag_26) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_4;
        _myaxi_ram_c_0_write_global_addr <= 1024;
        _myaxi_ram_c_0_write_size <= _th_comp_size_3;
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
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_39 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_39 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_39 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_41 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0))) begin
        myaxi_wdata <= __variable_data_41;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_39 <= _tmp_39 - 1;
      end 
      if(__variable_valid_41 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0)) && (_tmp_39 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_40 <= 1;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_40 <= _tmp_40;
      end 
      if(axim_flag_42) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_43) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_3;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_44) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_3;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_49) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_4;
        _myaxi_ram_c_0_write_global_addr <= 2048;
        _myaxi_ram_c_0_write_size <= _th_comp_size_3;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
      if(axim_flag_54) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_3;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_55) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_3;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_67) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_4;
        _myaxi_ram_c_0_write_global_addr <= 1024;
        _myaxi_ram_c_0_write_size <= _th_comp_size_3 >>> 2;
        _myaxi_ram_c_0_write_local_stride <= 1;
      end 
      if(axim_flag_68) begin
        _myaxi_ram_a_0_read_start <= 1;
        _myaxi_ram_a_0_read_op_sel <= 1;
        _myaxi_ram_a_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_a_0_read_global_addr <= 0;
        _myaxi_ram_a_0_read_size <= _th_comp_size_3;
        _myaxi_ram_a_0_read_local_stride <= 1;
      end 
      if(axim_flag_69) begin
        _myaxi_ram_b_0_read_start <= 1;
        _myaxi_ram_b_0_read_op_sel <= 2;
        _myaxi_ram_b_0_read_local_addr <= _th_comp_offset_4;
        _myaxi_ram_b_0_read_global_addr <= 0;
        _myaxi_ram_b_0_read_size <= _th_comp_size_3;
        _myaxi_ram_b_0_read_local_stride <= 1;
      end 
      if(axim_flag_74) begin
        _myaxi_ram_c_0_write_start <= 1;
        _myaxi_ram_c_0_write_op_sel <= 1;
        _myaxi_ram_c_0_write_local_addr <= _th_comp_offset_4;
        _myaxi_ram_c_0_write_global_addr <= 2048;
        _myaxi_ram_c_0_write_size <= _th_comp_size_3 >>> 2;
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
      _tmp_45 <= 0;
      _ram_a_cond_4_1 <= 0;
      _ram_a_cond_4_2 <= 0;
      _ram_a_cond_5_1 <= 0;
      _tmp_57 <= 0;
      _ram_a_cond_6_1 <= 0;
      _ram_a_cond_6_2 <= 0;
      _ram_a_cond_7_1 <= 0;
      _tmp_70 <= 0;
      _ram_a_cond_8_1 <= 0;
      _ram_a_cond_8_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_15 <= 0;
      end 
      if(_ram_a_cond_4_2) begin
        _tmp_45 <= 0;
      end 
      if(_ram_a_cond_6_2) begin
        _tmp_57 <= 0;
      end 
      if(_ram_a_cond_8_2) begin
        _tmp_70 <= 0;
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
        _tmp_45 <= 1;
      end 
      _ram_a_cond_4_2 <= _ram_a_cond_4_1;
      if(_ram_a_cond_5_1) begin
        _tmp_57 <= 1;
      end 
      _ram_a_cond_6_2 <= _ram_a_cond_6_1;
      if(_ram_a_cond_7_1) begin
        _tmp_70 <= 1;
      end 
      _ram_a_cond_8_2 <= _ram_a_cond_8_1;
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
      if(_macstream_a_source_ram_renable && (_macstream_a_source_ram_sel == 1)) begin
        ram_a_0_addr <= _macstream_a_source_ram_raddr;
      end 
      _ram_a_cond_1_1 <= _macstream_a_source_ram_renable && (_macstream_a_source_ram_sel == 1);
      _ram_a_cond_2_1 <= _macstream_a_source_ram_renable && (_macstream_a_source_ram_sel == 1);
      if(th_comp == 37) begin
        ram_a_0_addr <= _th_comp_i_11 + _th_comp_offset_8;
      end 
      _ram_a_cond_3_1 <= th_comp == 37;
      _ram_a_cond_4_1 <= th_comp == 37;
      if(_mystream_x_source_ram_renable && (_mystream_x_source_ram_sel == 1)) begin
        ram_a_0_addr <= _mystream_x_source_ram_raddr;
      end 
      _ram_a_cond_5_1 <= _mystream_x_source_ram_renable && (_mystream_x_source_ram_sel == 1);
      _ram_a_cond_6_1 <= _mystream_x_source_ram_renable && (_mystream_x_source_ram_sel == 1);
      if(th_comp == 106) begin
        ram_a_0_addr <= _th_comp_i_28 + _th_comp_offset_24;
      end 
      _ram_a_cond_7_1 <= th_comp == 106;
      _ram_a_cond_8_1 <= th_comp == 106;
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
      _tmp_47 <= 0;
      _ram_b_cond_4_1 <= 0;
      _ram_b_cond_4_2 <= 0;
      _ram_b_cond_5_1 <= 0;
      _tmp_61 <= 0;
      _ram_b_cond_6_1 <= 0;
      _ram_b_cond_6_2 <= 0;
      _ram_b_cond_7_1 <= 0;
      _tmp_72 <= 0;
      _ram_b_cond_8_1 <= 0;
      _ram_b_cond_8_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_19 <= 0;
      end 
      if(_ram_b_cond_4_2) begin
        _tmp_47 <= 0;
      end 
      if(_ram_b_cond_6_2) begin
        _tmp_61 <= 0;
      end 
      if(_ram_b_cond_8_2) begin
        _tmp_72 <= 0;
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
        _tmp_47 <= 1;
      end 
      _ram_b_cond_4_2 <= _ram_b_cond_4_1;
      if(_ram_b_cond_5_1) begin
        _tmp_61 <= 1;
      end 
      _ram_b_cond_6_2 <= _ram_b_cond_6_1;
      if(_ram_b_cond_7_1) begin
        _tmp_72 <= 1;
      end 
      _ram_b_cond_8_2 <= _ram_b_cond_8_1;
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
      if(_macstream_b_source_ram_renable && (_macstream_b_source_ram_sel == 2)) begin
        ram_b_0_addr <= _macstream_b_source_ram_raddr;
      end 
      _ram_b_cond_1_1 <= _macstream_b_source_ram_renable && (_macstream_b_source_ram_sel == 2);
      _ram_b_cond_2_1 <= _macstream_b_source_ram_renable && (_macstream_b_source_ram_sel == 2);
      if(th_comp == 39) begin
        ram_b_0_addr <= _th_comp_i_11 + _th_comp_offset_8;
      end 
      _ram_b_cond_3_1 <= th_comp == 39;
      _ram_b_cond_4_1 <= th_comp == 39;
      if(_mystream_y_source_ram_renable && (_mystream_y_source_ram_sel == 2)) begin
        ram_b_0_addr <= _mystream_y_source_ram_raddr;
      end 
      _ram_b_cond_5_1 <= _mystream_y_source_ram_renable && (_mystream_y_source_ram_sel == 2);
      _ram_b_cond_6_1 <= _mystream_y_source_ram_renable && (_mystream_y_source_ram_sel == 2);
      if(th_comp == 108) begin
        ram_b_0_addr <= _th_comp_i_28 + _th_comp_offset_24;
      end 
      _ram_b_cond_7_1 <= th_comp == 108;
      _ram_b_cond_8_1 <= th_comp == 108;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_32_1 <= 0;
      __tmp_33_1 <= 0;
      _tmp_37 <= 0;
      _tmp_27 <= 0;
      _tmp_28 <= 0;
      _tmp_35 <= 0;
      _tmp_36 <= 0;
      _tmp_34 <= 0;
      _tmp_38 <= 0;
      _ram_c_cond_1_1 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_50 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_52 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
      _ram_c_cond_6_1 <= 0;
      _ram_c_cond_7_1 <= 0;
      _ram_c_cond_8_1 <= 0;
      _tmp_75 <= 0;
      _ram_c_cond_9_1 <= 0;
      _ram_c_cond_9_2 <= 0;
      _ram_c_cond_10_1 <= 0;
      _tmp_77 <= 0;
      _ram_c_cond_11_1 <= 0;
      _ram_c_cond_11_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_50 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_52 <= 0;
      end 
      if(_ram_c_cond_9_2) begin
        _tmp_75 <= 0;
      end 
      if(_ram_c_cond_11_2) begin
        _tmp_77 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_50 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_52 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if(_ram_c_cond_6_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_7_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_8_1) begin
        _tmp_75 <= 1;
      end 
      _ram_c_cond_9_2 <= _ram_c_cond_9_1;
      if(_ram_c_cond_10_1) begin
        _tmp_77 <= 1;
      end 
      _ram_c_cond_11_2 <= _ram_c_cond_11_1;
      if(_macstream_c_sink_wenable && (_macstream_c_sink_ram_sel == 3)) begin
        ram_c_0_addr <= _macstream_c_sink_waddr;
        ram_c_0_wdata <= _macstream_c_sink_wdata;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= _macstream_c_sink_wenable && (_macstream_c_sink_ram_sel == 3);
      __tmp_32_1 <= _tmp_32;
      __tmp_33_1 <= _tmp_33;
      if((_tmp_29 || !_tmp_27) && (_tmp_30 || !_tmp_28) && _tmp_35) begin
        _tmp_37 <= 0;
        _tmp_27 <= 0;
        _tmp_28 <= 0;
        _tmp_35 <= 0;
      end 
      if((_tmp_29 || !_tmp_27) && (_tmp_30 || !_tmp_28) && _tmp_34) begin
        _tmp_27 <= 1;
        _tmp_28 <= 1;
        _tmp_37 <= _tmp_36;
        _tmp_36 <= 0;
        _tmp_34 <= 0;
        _tmp_35 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_38 == 0) && !_tmp_36 && !_tmp_37) begin
        ram_c_0_addr <= _myaxi_write_local_addr;
        _tmp_38 <= _myaxi_write_size - 1;
        _tmp_34 <= 1;
        _tmp_36 <= _myaxi_write_size == 1;
      end 
      if((_tmp_29 || !_tmp_27) && (_tmp_30 || !_tmp_28) && (_tmp_38 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + _myaxi_write_local_stride;
        _tmp_38 <= _tmp_38 - 1;
        _tmp_34 <= 1;
        _tmp_36 <= 0;
      end 
      if((_tmp_29 || !_tmp_27) && (_tmp_30 || !_tmp_28) && (_tmp_38 == 1)) begin
        _tmp_36 <= 1;
      end 
      if(th_comp == 43) begin
        ram_c_0_addr <= _th_comp_i_11 + _th_comp_offset_8;
        ram_c_0_wdata <= _th_comp_sum_9;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_comp == 43;
      if(th_comp == 58) begin
        ram_c_0_addr <= _th_comp_i_18 + _th_comp_offset_stream_15;
      end 
      _ram_c_cond_2_1 <= th_comp == 58;
      _ram_c_cond_3_1 <= th_comp == 58;
      if(th_comp == 60) begin
        ram_c_0_addr <= _th_comp_i_18 + _th_comp_offset_seq_16;
      end 
      _ram_c_cond_4_1 <= th_comp == 60;
      _ram_c_cond_5_1 <= th_comp == 60;
      if(_mystream_z_sink_wenable && (_mystream_z_sink_ram_sel == 3)) begin
        ram_c_0_addr <= _mystream_z_sink_waddr;
        ram_c_0_wdata <= _mystream_z_sink_wdata;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_6_1 <= _mystream_z_sink_wenable && (_mystream_z_sink_ram_sel == 3);
      if(th_comp == 114) begin
        ram_c_0_addr <= _th_comp_write_offset_27;
        ram_c_0_wdata <= _th_comp_val_31;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_7_1 <= th_comp == 114;
      if(th_comp == 128) begin
        ram_c_0_addr <= _th_comp_i_36 + _th_comp_offset_stream_33;
      end 
      _ram_c_cond_8_1 <= th_comp == 128;
      _ram_c_cond_9_1 <= th_comp == 128;
      if(th_comp == 130) begin
        ram_c_0_addr <= _th_comp_i_36 + _th_comp_offset_seq_34;
      end 
      _ram_c_cond_10_1 <= th_comp == 130;
      _ram_c_cond_11_1 <= th_comp == 130;
    end
  end

  assign __variable_data_41 = _tmp_33;
  assign __variable_valid_41 = _tmp_27;
  assign _tmp_29 = 1 && __variable_ready_41;

  always @(posedge CLK) begin
    if(RST) begin
      ram_d_0_addr <= 0;
      ram_d_0_wdata <= 0;
      ram_d_0_wenable <= 0;
      _ram_d_cond_0_1 <= 0;
      _ram_d_cond_1_1 <= 0;
    end else begin
      if(_ram_d_cond_0_1) begin
        ram_d_0_wenable <= 0;
      end 
      if(_ram_d_cond_1_1) begin
        ram_d_0_wenable <= 0;
      end 
      if(_macstream_v_sink_wenable && (_macstream_v_sink_ram_sel == 4)) begin
        ram_d_0_addr <= _macstream_v_sink_waddr;
        ram_d_0_wdata <= _macstream_v_sink_wdata;
        ram_d_0_wenable <= 1;
      end 
      _ram_d_cond_0_1 <= _macstream_v_sink_wenable && (_macstream_v_sink_ram_sel == 4);
      if(th_comp == 44) begin
        ram_d_0_addr <= _th_comp_i_11 + _th_comp_offset_8;
        ram_d_0_wdata <= _th_comp_count_10 == 3;
        ram_d_0_wenable <= 1;
      end 
      _ram_d_cond_1_1 <= th_comp == 44;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _times_mul_odata_reg_3 <= 0;
      __delay_data_15 <= 0;
      __delay_data_16 <= 0;
      __delay_data_17 <= 0;
      __delay_data_18 <= 0;
      __delay_data_19 <= 0;
      __delay_data_20 <= 0;
      __delay_data_21 <= 0;
      _reduceadd_data_6 <= 1'sd0;
      _reduceadd_count_6 <= 0;
      _pulse_data_8 <= 1'sd0;
      _pulse_count_8 <= 0;
      _plus_data_9 <= 0;
      __delay_data_22 <= 0;
      _set_flag_14 <= 0;
      _macstream_a_source_mode <= 0;
      _macstream_a_source_offset <= 0;
      _macstream_a_source_size <= 0;
      _macstream_a_source_stride <= 0;
      _macstream_a_source_ram_sel <= 0;
      __tmp_17_1 <= 0;
      _macstream_a_source_ram_rvalid <= 0;
      __variable_wdata_0 <= 0;
      _macstream_a_idle <= 1;
      _macstream_a_source_ram_raddr <= 0;
      _macstream_a_source_ram_renable <= 0;
      _macstream_a_source_count <= 0;
      _set_flag_18 <= 0;
      _macstream_b_source_mode <= 0;
      _macstream_b_source_offset <= 0;
      _macstream_b_source_size <= 0;
      _macstream_b_source_stride <= 0;
      _macstream_b_source_ram_sel <= 0;
      __tmp_21_1 <= 0;
      _macstream_b_source_ram_rvalid <= 0;
      __variable_wdata_1 <= 0;
      _macstream_b_idle <= 1;
      _macstream_b_source_ram_raddr <= 0;
      _macstream_b_source_ram_renable <= 0;
      _macstream_b_source_count <= 0;
      _set_flag_22 <= 0;
      __parametervariable_wdata_2 <= 0;
      _set_flag_23 <= 0;
      _macstream_c_sink_mode <= 0;
      _macstream_c_sink_offset <= 0;
      _macstream_c_sink_size <= 0;
      _macstream_c_sink_stride <= 0;
      _macstream_c_sink_ram_sel <= 0;
      _macstream_c_sink_wenable <= 0;
      _macstream_c_sink_waddr <= 0;
      _macstream_c_sink_count <= 0;
      _macstream_c_sink_wdata <= 0;
      _set_flag_24 <= 0;
      _macstream_v_sink_mode <= 0;
      _macstream_v_sink_offset <= 0;
      _macstream_v_sink_size <= 0;
      _macstream_v_sink_stride <= 0;
      _macstream_v_sink_ram_sel <= 0;
      _macstream_v_sink_wenable <= 0;
      _macstream_v_sink_waddr <= 0;
      _macstream_v_sink_count <= 0;
      _macstream_v_sink_wdata <= 0;
      _set_flag_25 <= 0;
      __macstream_start_flag_1 <= 0;
      __macstream_start_flag_2 <= 0;
      __macstream_start_flag_3 <= 0;
      __macstream_start_flag_4 <= 0;
      __macstream_start_flag_5 <= 0;
    end else begin
      _times_mul_odata_reg_3 <= _times_mul_odata_3;
      __delay_data_15 <= _macstream_reduce_reset;
      __delay_data_16 <= __delay_data_15;
      __delay_data_17 <= __delay_data_16;
      __delay_data_18 <= __delay_data_17;
      __delay_data_19 <= __delay_data_18;
      __delay_data_20 <= __delay_data_19;
      __delay_data_21 <= __delay_data_20;
      _reduceadd_data_6 <= _reduceadd_data_6 + _times_data_3;
      _reduceadd_count_6 <= (_reduceadd_count_6 == macstream_const_data - 1)? 0 : _reduceadd_count_6 + 1;
      if(__delay_data_21) begin
        _reduceadd_data_6 <= 1'sd0 + _times_data_3;
      end 
      if(__delay_data_21) begin
        _reduceadd_count_6 <= 0;
      end 
      if(_reduceadd_count_6 == 0) begin
        _reduceadd_data_6 <= 1'sd0 + _times_data_3;
      end 
      _pulse_data_8 <= _pulse_count_8 == macstream_const_data - 1;
      _pulse_count_8 <= (_pulse_count_8 == macstream_const_data - 1)? 0 : _pulse_count_8 + 1;
      if(__delay_data_21) begin
        _pulse_data_8 <= _pulse_count_8 == macstream_const_data - 1;
      end 
      if(__delay_data_21) begin
        _pulse_count_8 <= 0;
      end 
      if(_pulse_count_8 == 0) begin
        _pulse_data_8 <= _pulse_count_8 == macstream_const_data - 1;
      end 
      _plus_data_9 <= _pulse_data_8 + 1'sd0;
      __delay_data_22 <= _reduceadd_data_6;
      _set_flag_14 <= 0;
      if(th_comp == 11) begin
        _set_flag_14 <= 1;
      end 
      if(_set_flag_14) begin
        _macstream_a_source_mode <= 0;
        _macstream_a_source_offset <= _th_comp_offset_6;
        _macstream_a_source_size <= _th_comp_size_5;
        _macstream_a_source_stride <= 1;
      end 
      if(_set_flag_14) begin
        _macstream_a_source_ram_sel <= 1;
      end 
      __tmp_17_1 <= _tmp_17;
      _macstream_a_source_ram_rvalid <= __tmp_17_1;
      if(_macstream_a_source_ram_rvalid) begin
        __variable_wdata_0 <= _macstream_a_source_ram_rdata;
      end 
      if(_macstream_start && (_macstream_a_source_mode == 0) && (_macstream_a_source_size > 0)) begin
        _macstream_a_idle <= 0;
      end 
      if(_macstream_a_source_fsm_0 == 1) begin
        _macstream_a_source_ram_raddr <= _macstream_a_source_offset;
        _macstream_a_source_ram_renable <= 1;
        _macstream_a_source_count <= _macstream_a_source_size;
      end 
      if(_macstream_a_source_fsm_0 == 2) begin
        _macstream_a_source_ram_raddr <= _macstream_a_source_ram_raddr + _macstream_a_source_stride;
        _macstream_a_source_ram_renable <= 1;
        _macstream_a_source_count <= _macstream_a_source_count - 1;
      end 
      if((_macstream_a_source_fsm_0 == 2) && (_macstream_a_source_count == 1)) begin
        _macstream_a_source_ram_renable <= 0;
        _macstream_a_idle <= 1;
      end 
      _set_flag_18 <= 0;
      if(th_comp == 12) begin
        _set_flag_18 <= 1;
      end 
      if(_set_flag_18) begin
        _macstream_b_source_mode <= 0;
        _macstream_b_source_offset <= _th_comp_offset_6;
        _macstream_b_source_size <= _th_comp_size_5;
        _macstream_b_source_stride <= 1;
      end 
      if(_set_flag_18) begin
        _macstream_b_source_ram_sel <= 2;
      end 
      __tmp_21_1 <= _tmp_21;
      _macstream_b_source_ram_rvalid <= __tmp_21_1;
      if(_macstream_b_source_ram_rvalid) begin
        __variable_wdata_1 <= _macstream_b_source_ram_rdata;
      end 
      if(_macstream_start && (_macstream_b_source_mode == 0) && (_macstream_b_source_size > 0)) begin
        _macstream_b_idle <= 0;
      end 
      if(_macstream_b_source_fsm_1 == 1) begin
        _macstream_b_source_ram_raddr <= _macstream_b_source_offset;
        _macstream_b_source_ram_renable <= 1;
        _macstream_b_source_count <= _macstream_b_source_size;
      end 
      if(_macstream_b_source_fsm_1 == 2) begin
        _macstream_b_source_ram_raddr <= _macstream_b_source_ram_raddr + _macstream_b_source_stride;
        _macstream_b_source_ram_renable <= 1;
        _macstream_b_source_count <= _macstream_b_source_count - 1;
      end 
      if((_macstream_b_source_fsm_1 == 2) && (_macstream_b_source_count == 1)) begin
        _macstream_b_source_ram_renable <= 0;
        _macstream_b_idle <= 1;
      end 
      _set_flag_22 <= 0;
      if(th_comp == 13) begin
        _set_flag_22 <= 1;
      end 
      if(_set_flag_22) begin
        __parametervariable_wdata_2 <= 4;
      end 
      _set_flag_23 <= 0;
      if(th_comp == 14) begin
        _set_flag_23 <= 1;
      end 
      if(_set_flag_23) begin
        _macstream_c_sink_mode <= 0;
        _macstream_c_sink_offset <= _th_comp_offset_6;
        _macstream_c_sink_size <= _th_comp_size_5;
        _macstream_c_sink_stride <= 1;
      end 
      if(_set_flag_23) begin
        _macstream_c_sink_ram_sel <= 3;
      end 
      if(_macstream_c_sink_fsm_2 == 0) begin
        _macstream_c_sink_wenable <= 0;
      end 
      if(_macstream_c_sink_fsm_2 == 1) begin
        _macstream_c_sink_waddr <= _macstream_c_sink_offset - _macstream_c_sink_stride;
        _macstream_c_sink_count <= _macstream_c_sink_size;
      end 
      if(_macstream_c_sink_fsm_2 == 14) begin
        _macstream_c_sink_wenable <= 0;
      end 
      if(_macstream_c_sink_fsm_2 == 14) begin
        _macstream_c_sink_waddr <= _macstream_c_sink_waddr + _macstream_c_sink_stride;
        _macstream_c_sink_wdata <= macstream_c_data;
        _macstream_c_sink_wenable <= 1;
        _macstream_c_sink_count <= _macstream_c_sink_count - 1;
      end 
      _set_flag_24 <= 0;
      if(th_comp == 15) begin
        _set_flag_24 <= 1;
      end 
      if(_set_flag_24) begin
        _macstream_v_sink_mode <= 0;
        _macstream_v_sink_offset <= _th_comp_offset_6;
        _macstream_v_sink_size <= _th_comp_size_5;
        _macstream_v_sink_stride <= 1;
      end 
      if(_set_flag_24) begin
        _macstream_v_sink_ram_sel <= 4;
      end 
      if(_macstream_v_sink_fsm_3 == 0) begin
        _macstream_v_sink_wenable <= 0;
      end 
      if(_macstream_v_sink_fsm_3 == 1) begin
        _macstream_v_sink_waddr <= _macstream_v_sink_offset - _macstream_v_sink_stride;
        _macstream_v_sink_count <= _macstream_v_sink_size;
      end 
      if(_macstream_v_sink_fsm_3 == 14) begin
        _macstream_v_sink_wenable <= 0;
      end 
      if(_macstream_v_sink_fsm_3 == 14) begin
        _macstream_v_sink_waddr <= _macstream_v_sink_waddr + _macstream_v_sink_stride;
        _macstream_v_sink_wdata <= macstream_v_data;
        _macstream_v_sink_wenable <= 1;
        _macstream_v_sink_count <= _macstream_v_sink_count - 1;
      end 
      _set_flag_25 <= 0;
      if(th_comp == 16) begin
        _set_flag_25 <= 1;
      end 
      __macstream_start_flag_1 <= _macstream_start_flag;
      __macstream_start_flag_2 <= __macstream_start_flag_1;
      __macstream_start_flag_3 <= __macstream_start_flag_2;
      __macstream_start_flag_4 <= __macstream_start_flag_3;
      __macstream_start_flag_5 <= __macstream_start_flag_4;
      if(_substream_macstream_a_data_cond_14_0) begin
        __variable_wdata_0 <= mystream_x_data;
      end 
      if(_substream_macstream_b_data_cond_14_1) begin
        __variable_wdata_1 <= mystream_y_data;
      end 
      if(_substream_macstream_const_data_cond_14_2) begin
        __parametervariable_wdata_2 <= mystream_const_data;
      end 
    end
  end

  localparam _macstream_fsm_1 = 1;
  localparam _macstream_fsm_2 = 2;
  localparam _macstream_fsm_3 = 3;
  localparam _macstream_fsm_4 = 4;
  localparam _macstream_fsm_5 = 5;
  localparam _macstream_fsm_6 = 6;
  localparam _macstream_fsm_7 = 7;
  localparam _macstream_fsm_8 = 8;
  localparam _macstream_fsm_9 = 9;
  localparam _macstream_fsm_10 = 10;
  localparam _macstream_fsm_11 = 11;
  localparam _macstream_fsm_12 = 12;
  localparam _macstream_fsm_13 = 13;
  localparam _macstream_fsm_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_fsm <= _macstream_fsm_init;
      _macstream_start <= 0;
      _macstream_busy <= 0;
      _macstream_reduce_reset <= 1;
      _substream_macstream_a_data_cond_14_0 <= 0;
      _substream_macstream_b_data_cond_14_1 <= 0;
      _substream_macstream_const_data_cond_14_2 <= 0;
    end else begin
      if(__macstream_start_flag_5) begin
        _macstream_reduce_reset <= 0;
      end 
      if(__mystream_start_flag_6) begin
        _macstream_reduce_reset <= 0;
      end 
      case(_macstream_fsm)
        _macstream_fsm_init: begin
          if(_macstream_start_flag) begin
            _macstream_start <= 1;
            _macstream_busy <= 1;
          end 
          if(_mystream_start_flag) begin
            _substream_macstream_a_data_cond_14_0 <= 1;
          end 
          if(_mystream_start_flag) begin
            _substream_macstream_b_data_cond_14_1 <= 1;
          end 
          if(_mystream_start_flag) begin
            _substream_macstream_const_data_cond_14_2 <= 1;
          end 
          if(_mystream_fsm == 16) begin
            _macstream_reduce_reset <= 1;
          end 
          if(_mystream_fsm == 16) begin
            _substream_macstream_a_data_cond_14_0 <= 0;
          end 
          if(_mystream_fsm == 16) begin
            _substream_macstream_b_data_cond_14_1 <= 0;
          end 
          if(_mystream_fsm == 16) begin
            _substream_macstream_const_data_cond_14_2 <= 0;
          end 
          if(_macstream_start_flag) begin
            _macstream_fsm <= _macstream_fsm_1;
          end 
        end
        _macstream_fsm_1: begin
          _macstream_start <= 0;
          _macstream_fsm <= _macstream_fsm_2;
        end
        _macstream_fsm_2: begin
          if(_macstream_done) begin
            _macstream_fsm <= _macstream_fsm_3;
          end 
        end
        _macstream_fsm_3: begin
          _macstream_fsm <= _macstream_fsm_4;
        end
        _macstream_fsm_4: begin
          _macstream_fsm <= _macstream_fsm_5;
        end
        _macstream_fsm_5: begin
          _macstream_fsm <= _macstream_fsm_6;
        end
        _macstream_fsm_6: begin
          _macstream_fsm <= _macstream_fsm_7;
        end
        _macstream_fsm_7: begin
          _macstream_fsm <= _macstream_fsm_8;
        end
        _macstream_fsm_8: begin
          _macstream_fsm <= _macstream_fsm_9;
        end
        _macstream_fsm_9: begin
          _macstream_fsm <= _macstream_fsm_10;
        end
        _macstream_fsm_10: begin
          _macstream_fsm <= _macstream_fsm_11;
        end
        _macstream_fsm_11: begin
          _macstream_fsm <= _macstream_fsm_12;
        end
        _macstream_fsm_12: begin
          _macstream_fsm <= _macstream_fsm_13;
        end
        _macstream_fsm_13: begin
          _macstream_reduce_reset <= 1;
          _macstream_fsm <= _macstream_fsm_14;
        end
        _macstream_fsm_14: begin
          _macstream_busy <= 0;
          _macstream_fsm <= _macstream_fsm_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __delay_data_26 <= 0;
      __delay_data_27 <= 0;
      __delay_data_28 <= 0;
      __delay_data_29 <= 0;
      __delay_data_30 <= 0;
      __delay_data_31 <= 0;
      __delay_data_32 <= 0;
      __delay_data_33 <= 0;
      __delay_data_34 <= 0;
      __delay_data_35 <= 0;
      __substreamoutput_data_23 <= 0;
      __substreamoutput_data_24 <= 0;
      __delay_data_36 <= 0;
      _plus_data_25 <= 0;
      __delay_data_37 <= 0;
      _set_flag_56 <= 0;
      _mystream_x_source_mode <= 0;
      _mystream_x_source_offset <= 0;
      _mystream_x_source_size <= 0;
      _mystream_x_source_stride <= 0;
      _mystream_x_source_ram_sel <= 0;
      __tmp_59_1 <= 0;
      _mystream_x_source_ram_rvalid <= 0;
      __variable_wdata_11 <= 0;
      _mystream_x_idle <= 1;
      _mystream_x_source_ram_raddr <= 0;
      _mystream_x_source_ram_renable <= 0;
      _mystream_x_source_count <= 0;
      _set_flag_60 <= 0;
      _mystream_y_source_mode <= 0;
      _mystream_y_source_offset <= 0;
      _mystream_y_source_size <= 0;
      _mystream_y_source_stride <= 0;
      _mystream_y_source_ram_sel <= 0;
      __tmp_63_1 <= 0;
      _mystream_y_source_ram_rvalid <= 0;
      __variable_wdata_12 <= 0;
      _mystream_y_idle <= 1;
      _mystream_y_source_ram_raddr <= 0;
      _mystream_y_source_ram_renable <= 0;
      _mystream_y_source_count <= 0;
      _set_flag_64 <= 0;
      __parametervariable_wdata_13 <= 0;
      _set_flag_65 <= 0;
      _mystream_z_sink_mode <= 0;
      _mystream_z_sink_offset <= 0;
      _mystream_z_sink_size <= 0;
      _mystream_z_sink_stride <= 0;
      _mystream_z_sink_ram_sel <= 0;
      _mystream_z_sink_wenable <= 0;
      _mystream_z_sink_waddr <= 0;
      _mystream_z_sink_count <= 0;
      _mystream_z_sink_wdata <= 0;
      _set_flag_66 <= 0;
      __mystream_start_flag_1 <= 0;
      __mystream_start_flag_2 <= 0;
      __mystream_start_flag_3 <= 0;
      __mystream_start_flag_4 <= 0;
      __mystream_start_flag_5 <= 0;
      __mystream_start_flag_6 <= 0;
    end else begin
      __delay_data_26 <= mystream_x_data;
      __delay_data_27 <= __delay_data_26;
      __delay_data_28 <= __delay_data_27;
      __delay_data_29 <= __delay_data_28;
      __delay_data_30 <= __delay_data_29;
      __delay_data_31 <= __delay_data_30;
      __delay_data_32 <= __delay_data_31;
      __delay_data_33 <= __delay_data_32;
      __delay_data_34 <= __delay_data_33;
      __delay_data_35 <= __delay_data_34;
      __substreamoutput_data_23 <= macstream_c_data;
      __substreamoutput_data_24 <= macstream_v_data;
      __delay_data_36 <= __delay_data_35;
      _plus_data_25 <= __substreamoutput_data_23 + __delay_data_36;
      __delay_data_37 <= __substreamoutput_data_24;
      _set_flag_56 <= 0;
      if(th_comp == 80) begin
        _set_flag_56 <= 1;
      end 
      if(_set_flag_56) begin
        _mystream_x_source_mode <= 0;
        _mystream_x_source_offset <= _th_comp_offset_22;
        _mystream_x_source_size <= _th_comp_size_21;
        _mystream_x_source_stride <= 1;
      end 
      if(_set_flag_56) begin
        _mystream_x_source_ram_sel <= 1;
      end 
      __tmp_59_1 <= _tmp_59;
      _mystream_x_source_ram_rvalid <= __tmp_59_1;
      if(_mystream_x_source_ram_rvalid) begin
        __variable_wdata_11 <= _mystream_x_source_ram_rdata;
      end 
      if(_mystream_start && (_mystream_x_source_mode == 0) && (_mystream_x_source_size > 0)) begin
        _mystream_x_idle <= 0;
      end 
      if(_mystream_x_source_fsm_0 == 1) begin
        _mystream_x_source_ram_raddr <= _mystream_x_source_offset;
        _mystream_x_source_ram_renable <= 1;
        _mystream_x_source_count <= _mystream_x_source_size;
      end 
      if(_mystream_x_source_fsm_0 == 2) begin
        _mystream_x_source_ram_raddr <= _mystream_x_source_ram_raddr + _mystream_x_source_stride;
        _mystream_x_source_ram_renable <= 1;
        _mystream_x_source_count <= _mystream_x_source_count - 1;
      end 
      if((_mystream_x_source_fsm_0 == 2) && (_mystream_x_source_count == 1)) begin
        _mystream_x_source_ram_renable <= 0;
        _mystream_x_idle <= 1;
      end 
      _set_flag_60 <= 0;
      if(th_comp == 81) begin
        _set_flag_60 <= 1;
      end 
      if(_set_flag_60) begin
        _mystream_y_source_mode <= 0;
        _mystream_y_source_offset <= _th_comp_offset_22;
        _mystream_y_source_size <= _th_comp_size_21;
        _mystream_y_source_stride <= 1;
      end 
      if(_set_flag_60) begin
        _mystream_y_source_ram_sel <= 2;
      end 
      __tmp_63_1 <= _tmp_63;
      _mystream_y_source_ram_rvalid <= __tmp_63_1;
      if(_mystream_y_source_ram_rvalid) begin
        __variable_wdata_12 <= _mystream_y_source_ram_rdata;
      end 
      if(_mystream_start && (_mystream_y_source_mode == 0) && (_mystream_y_source_size > 0)) begin
        _mystream_y_idle <= 0;
      end 
      if(_mystream_y_source_fsm_1 == 1) begin
        _mystream_y_source_ram_raddr <= _mystream_y_source_offset;
        _mystream_y_source_ram_renable <= 1;
        _mystream_y_source_count <= _mystream_y_source_size;
      end 
      if(_mystream_y_source_fsm_1 == 2) begin
        _mystream_y_source_ram_raddr <= _mystream_y_source_ram_raddr + _mystream_y_source_stride;
        _mystream_y_source_ram_renable <= 1;
        _mystream_y_source_count <= _mystream_y_source_count - 1;
      end 
      if((_mystream_y_source_fsm_1 == 2) && (_mystream_y_source_count == 1)) begin
        _mystream_y_source_ram_renable <= 0;
        _mystream_y_idle <= 1;
      end 
      _set_flag_64 <= 0;
      if(th_comp == 82) begin
        _set_flag_64 <= 1;
      end 
      if(_set_flag_64) begin
        __parametervariable_wdata_13 <= 4;
      end 
      _set_flag_65 <= 0;
      if(th_comp == 83) begin
        _set_flag_65 <= 1;
      end 
      if(_set_flag_65) begin
        _mystream_z_sink_mode <= 0;
        _mystream_z_sink_offset <= _th_comp_offset_22;
        _mystream_z_sink_size <= _th_comp_size_21 >>> 2;
        _mystream_z_sink_stride <= 1;
      end 
      if(_set_flag_65) begin
        _mystream_z_sink_ram_sel <= 3;
      end 
      if(_mystream_z_sink_fsm_2 == 0) begin
        _mystream_z_sink_wenable <= 0;
      end 
      if(_mystream_z_sink_fsm_2 == 1) begin
        _mystream_z_sink_waddr <= _mystream_z_sink_offset - _mystream_z_sink_stride;
        _mystream_z_sink_count <= _mystream_z_sink_size;
      end 
      if(_mystream_z_sink_fsm_2 == 17) begin
        _mystream_z_sink_wenable <= 0;
      end 
      if((_mystream_z_sink_fsm_2 == 17) && mystream_v_data) begin
        _mystream_z_sink_waddr <= _mystream_z_sink_waddr + _mystream_z_sink_stride;
        _mystream_z_sink_wdata <= mystream_z_data;
        _mystream_z_sink_wenable <= 1;
        _mystream_z_sink_count <= _mystream_z_sink_count - 1;
      end 
      _set_flag_66 <= 0;
      if(th_comp == 84) begin
        _set_flag_66 <= 1;
      end 
      __mystream_start_flag_1 <= _mystream_start_flag;
      __mystream_start_flag_2 <= __mystream_start_flag_1;
      __mystream_start_flag_3 <= __mystream_start_flag_2;
      __mystream_start_flag_4 <= __mystream_start_flag_3;
      __mystream_start_flag_5 <= __mystream_start_flag_4;
      __mystream_start_flag_6 <= __mystream_start_flag_5;
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
  localparam _mystream_fsm_13 = 13;
  localparam _mystream_fsm_14 = 14;
  localparam _mystream_fsm_15 = 15;
  localparam _mystream_fsm_16 = 16;
  localparam _mystream_fsm_17 = 17;

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
          _mystream_fsm <= _mystream_fsm_13;
        end
        _mystream_fsm_13: begin
          _mystream_fsm <= _mystream_fsm_14;
        end
        _mystream_fsm_14: begin
          _mystream_fsm <= _mystream_fsm_15;
        end
        _mystream_fsm_15: begin
          _mystream_fsm <= _mystream_fsm_16;
        end
        _mystream_fsm_16: begin
          _mystream_fsm <= _mystream_fsm_17;
        end
        _mystream_fsm_17: begin
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
  localparam th_comp_104 = 104;
  localparam th_comp_105 = 105;
  localparam th_comp_106 = 106;
  localparam th_comp_107 = 107;
  localparam th_comp_108 = 108;
  localparam th_comp_109 = 109;
  localparam th_comp_110 = 110;
  localparam th_comp_111 = 111;
  localparam th_comp_112 = 112;
  localparam th_comp_113 = 113;
  localparam th_comp_114 = 114;
  localparam th_comp_115 = 115;
  localparam th_comp_116 = 116;
  localparam th_comp_117 = 117;
  localparam th_comp_118 = 118;
  localparam th_comp_119 = 119;
  localparam th_comp_120 = 120;
  localparam th_comp_121 = 121;
  localparam th_comp_122 = 122;
  localparam th_comp_123 = 123;
  localparam th_comp_124 = 124;
  localparam th_comp_125 = 125;
  localparam th_comp_126 = 126;
  localparam th_comp_127 = 127;
  localparam th_comp_128 = 128;
  localparam th_comp_129 = 129;
  localparam th_comp_130 = 130;
  localparam th_comp_131 = 131;
  localparam th_comp_132 = 132;
  localparam th_comp_133 = 133;
  localparam th_comp_134 = 134;
  localparam th_comp_135 = 135;
  localparam th_comp_136 = 136;
  localparam th_comp_137 = 137;
  localparam th_comp_138 = 138;
  localparam th_comp_139 = 139;
  localparam th_comp_140 = 140;

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _d1_th_comp <= th_comp_init;
      _th_comp_size_3 <= 0;
      _th_comp_offset_4 <= 0;
      axim_flag_0 <= 0;
      _th_comp_cond_2_0_1 <= 0;
      axim_flag_8 <= 0;
      _th_comp_cond_6_1_1 <= 0;
      _th_comp_size_5 <= 0;
      _th_comp_offset_6 <= 0;
      axim_flag_26 <= 0;
      _th_comp_cond_19_2_1 <= 0;
      axim_flag_43 <= 0;
      _th_comp_cond_24_3_1 <= 0;
      axim_flag_44 <= 0;
      _th_comp_cond_28_4_1 <= 0;
      _th_comp_size_7 <= 0;
      _th_comp_offset_8 <= 0;
      _th_comp_sum_9 <= 0;
      _th_comp_count_10 <= 0;
      _th_comp_i_11 <= 0;
      _tmp_46 <= 0;
      _th_comp_a_12 <= 0;
      _tmp_48 <= 0;
      _th_comp_b_13 <= 0;
      axim_flag_49 <= 0;
      _th_comp_cond_49_5_1 <= 0;
      _th_comp_size_14 <= 0;
      _th_comp_offset_stream_15 <= 0;
      _th_comp_offset_seq_16 <= 0;
      _th_comp_all_ok_17 <= 0;
      _th_comp_i_18 <= 0;
      _tmp_51 <= 0;
      _th_comp_st_19 <= 0;
      _tmp_53 <= 0;
      _th_comp_sq_20 <= 0;
      axim_flag_54 <= 0;
      _th_comp_cond_71_6_1 <= 0;
      axim_flag_55 <= 0;
      _th_comp_cond_75_7_1 <= 0;
      _th_comp_size_21 <= 0;
      _th_comp_offset_22 <= 0;
      axim_flag_67 <= 0;
      _th_comp_cond_87_8_1 <= 0;
      axim_flag_68 <= 0;
      _th_comp_cond_92_9_1 <= 0;
      axim_flag_69 <= 0;
      _th_comp_cond_96_10_1 <= 0;
      _th_comp_size_23 <= 0;
      _th_comp_offset_24 <= 0;
      _th_comp_sum_25 <= 0;
      _th_comp_count_26 <= 0;
      _th_comp_write_offset_27 <= 0;
      _th_comp_i_28 <= 0;
      _tmp_71 <= 0;
      _th_comp_x_29 <= 0;
      _tmp_73 <= 0;
      _th_comp_y_30 <= 0;
      _th_comp_val_31 <= 0;
      axim_flag_74 <= 0;
      _th_comp_cond_119_11_1 <= 0;
      _th_comp_size_32 <= 0;
      _th_comp_offset_stream_33 <= 0;
      _th_comp_offset_seq_34 <= 0;
      _th_comp_all_ok_35 <= 0;
      _th_comp_i_36 <= 0;
      _tmp_76 <= 0;
      _th_comp_st_37 <= 0;
      _tmp_78 <= 0;
      _th_comp_sq_38 <= 0;
    end else begin
      _d1_th_comp <= th_comp;
      case(_d1_th_comp)
        th_comp_2: begin
          if(_th_comp_cond_2_0_1) begin
            axim_flag_0 <= 0;
          end 
        end
        th_comp_6: begin
          if(_th_comp_cond_6_1_1) begin
            axim_flag_8 <= 0;
          end 
        end
        th_comp_19: begin
          if(_th_comp_cond_19_2_1) begin
            axim_flag_26 <= 0;
          end 
        end
        th_comp_24: begin
          if(_th_comp_cond_24_3_1) begin
            axim_flag_43 <= 0;
          end 
        end
        th_comp_28: begin
          if(_th_comp_cond_28_4_1) begin
            axim_flag_44 <= 0;
          end 
        end
        th_comp_49: begin
          if(_th_comp_cond_49_5_1) begin
            axim_flag_49 <= 0;
          end 
        end
        th_comp_71: begin
          if(_th_comp_cond_71_6_1) begin
            axim_flag_54 <= 0;
          end 
        end
        th_comp_75: begin
          if(_th_comp_cond_75_7_1) begin
            axim_flag_55 <= 0;
          end 
        end
        th_comp_87: begin
          if(_th_comp_cond_87_8_1) begin
            axim_flag_67 <= 0;
          end 
        end
        th_comp_92: begin
          if(_th_comp_cond_92_9_1) begin
            axim_flag_68 <= 0;
          end 
        end
        th_comp_96: begin
          if(_th_comp_cond_96_10_1) begin
            axim_flag_69 <= 0;
          end 
        end
        th_comp_119: begin
          if(_th_comp_cond_119_11_1) begin
            axim_flag_74 <= 0;
          end 
        end
      endcase
      case(th_comp)
        th_comp_init: begin
          _th_comp_size_3 <= 16;
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_offset_4 <= 0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          axim_flag_0 <= 1;
          _th_comp_cond_2_0_1 <= 1;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          th_comp <= th_comp_4;
        end
        th_comp_4: begin
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_6;
          end 
        end
        th_comp_6: begin
          axim_flag_8 <= 1;
          _th_comp_cond_6_1_1 <= 1;
          th_comp <= th_comp_7;
        end
        th_comp_7: begin
          th_comp <= th_comp_8;
        end
        th_comp_8: begin
          th_comp <= th_comp_9;
        end
        th_comp_9: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_10;
          end 
        end
        th_comp_10: begin
          _th_comp_size_5 <= _th_comp_size_3;
          _th_comp_offset_6 <= _th_comp_offset_4;
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
          th_comp <= th_comp_16;
        end
        th_comp_16: begin
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          if(!_macstream_busy) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          axim_flag_26 <= 1;
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
          _th_comp_offset_4 <= _th_comp_size_3;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          axim_flag_43 <= 1;
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
          axim_flag_44 <= 1;
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
          _th_comp_size_7 <= _th_comp_size_3;
          _th_comp_offset_8 <= _th_comp_offset_4;
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          _th_comp_sum_9 <= 0;
          th_comp <= th_comp_34;
        end
        th_comp_34: begin
          _th_comp_count_10 <= 0;
          th_comp <= th_comp_35;
        end
        th_comp_35: begin
          _th_comp_i_11 <= 0;
          th_comp <= th_comp_36;
        end
        th_comp_36: begin
          if(_th_comp_i_11 < _th_comp_size_7) begin
            th_comp <= th_comp_37;
          end else begin
            th_comp <= th_comp_49;
          end
        end
        th_comp_37: begin
          if(_tmp_45) begin
            _tmp_46 <= ram_a_0_rdata;
          end 
          if(_tmp_45) begin
            th_comp <= th_comp_38;
          end 
        end
        th_comp_38: begin
          _th_comp_a_12 <= _tmp_46;
          th_comp <= th_comp_39;
        end
        th_comp_39: begin
          if(_tmp_47) begin
            _tmp_48 <= ram_b_0_rdata;
          end 
          if(_tmp_47) begin
            th_comp <= th_comp_40;
          end 
        end
        th_comp_40: begin
          _th_comp_b_13 <= _tmp_48;
          th_comp <= th_comp_41;
        end
        th_comp_41: begin
          _th_comp_sum_9 <= _th_comp_sum_9 + _th_comp_a_12 * _th_comp_b_13;
          th_comp <= th_comp_42;
        end
        th_comp_42: begin
          _th_comp_count_10 <= _th_comp_count_10 + 1;
          th_comp <= th_comp_43;
        end
        th_comp_43: begin
          th_comp <= th_comp_44;
        end
        th_comp_44: begin
          th_comp <= th_comp_45;
        end
        th_comp_45: begin
          if(_th_comp_count_10 == 4) begin
            th_comp <= th_comp_46;
          end else begin
            th_comp <= th_comp_48;
          end
        end
        th_comp_46: begin
          _th_comp_sum_9 <= 0;
          th_comp <= th_comp_47;
        end
        th_comp_47: begin
          _th_comp_count_10 <= 0;
          th_comp <= th_comp_48;
        end
        th_comp_48: begin
          _th_comp_i_11 <= _th_comp_i_11 + 1;
          th_comp <= th_comp_36;
        end
        th_comp_49: begin
          axim_flag_49 <= 1;
          _th_comp_cond_49_5_1 <= 1;
          th_comp <= th_comp_50;
        end
        th_comp_50: begin
          th_comp <= th_comp_51;
        end
        th_comp_51: begin
          th_comp <= th_comp_52;
        end
        th_comp_52: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_53;
          end 
        end
        th_comp_53: begin
          $display("# macstream");
          th_comp <= th_comp_54;
        end
        th_comp_54: begin
          _th_comp_size_14 <= _th_comp_size_3;
          _th_comp_offset_stream_15 <= 0;
          _th_comp_offset_seq_16 <= _th_comp_offset_4;
          th_comp <= th_comp_55;
        end
        th_comp_55: begin
          _th_comp_all_ok_17 <= 1;
          th_comp <= th_comp_56;
        end
        th_comp_56: begin
          _th_comp_i_18 <= 0;
          th_comp <= th_comp_57;
        end
        th_comp_57: begin
          if(_th_comp_i_18 < _th_comp_size_14) begin
            th_comp <= th_comp_58;
          end else begin
            th_comp <= th_comp_66;
          end
        end
        th_comp_58: begin
          if(_tmp_50) begin
            _tmp_51 <= ram_c_0_rdata;
          end 
          if(_tmp_50) begin
            th_comp <= th_comp_59;
          end 
        end
        th_comp_59: begin
          _th_comp_st_19 <= _tmp_51;
          th_comp <= th_comp_60;
        end
        th_comp_60: begin
          if(_tmp_52) begin
            _tmp_53 <= ram_c_0_rdata;
          end 
          if(_tmp_52) begin
            th_comp <= th_comp_61;
          end 
        end
        th_comp_61: begin
          _th_comp_sq_20 <= _tmp_53;
          th_comp <= th_comp_62;
        end
        th_comp_62: begin
          if(_th_comp_st_19 !== _th_comp_sq_20) begin
            th_comp <= th_comp_63;
          end else begin
            th_comp <= th_comp_65;
          end
        end
        th_comp_63: begin
          _th_comp_all_ok_17 <= 0;
          th_comp <= th_comp_64;
        end
        th_comp_64: begin
          $display("%d %d %d", _th_comp_i_18, _th_comp_st_19, _th_comp_sq_20);
          th_comp <= th_comp_65;
        end
        th_comp_65: begin
          _th_comp_i_18 <= _th_comp_i_18 + 1;
          th_comp <= th_comp_57;
        end
        th_comp_66: begin
          if(_th_comp_all_ok_17) begin
            th_comp <= th_comp_67;
          end else begin
            th_comp <= th_comp_69;
          end
        end
        th_comp_67: begin
          $display("OK");
          th_comp <= th_comp_68;
        end
        th_comp_68: begin
          th_comp <= th_comp_70;
        end
        th_comp_69: begin
          $display("NG");
          th_comp <= th_comp_70;
        end
        th_comp_70: begin
          _th_comp_offset_4 <= 0;
          th_comp <= th_comp_71;
        end
        th_comp_71: begin
          axim_flag_54 <= 1;
          _th_comp_cond_71_6_1 <= 1;
          th_comp <= th_comp_72;
        end
        th_comp_72: begin
          th_comp <= th_comp_73;
        end
        th_comp_73: begin
          th_comp <= th_comp_74;
        end
        th_comp_74: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_75;
          end 
        end
        th_comp_75: begin
          axim_flag_55 <= 1;
          _th_comp_cond_75_7_1 <= 1;
          th_comp <= th_comp_76;
        end
        th_comp_76: begin
          th_comp <= th_comp_77;
        end
        th_comp_77: begin
          th_comp <= th_comp_78;
        end
        th_comp_78: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_79;
          end 
        end
        th_comp_79: begin
          _th_comp_size_21 <= _th_comp_size_3;
          _th_comp_offset_22 <= _th_comp_offset_4;
          th_comp <= th_comp_80;
        end
        th_comp_80: begin
          th_comp <= th_comp_81;
        end
        th_comp_81: begin
          th_comp <= th_comp_82;
        end
        th_comp_82: begin
          th_comp <= th_comp_83;
        end
        th_comp_83: begin
          th_comp <= th_comp_84;
        end
        th_comp_84: begin
          th_comp <= th_comp_85;
        end
        th_comp_85: begin
          th_comp <= th_comp_86;
        end
        th_comp_86: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_87;
          end 
        end
        th_comp_87: begin
          axim_flag_67 <= 1;
          _th_comp_cond_87_8_1 <= 1;
          th_comp <= th_comp_88;
        end
        th_comp_88: begin
          th_comp <= th_comp_89;
        end
        th_comp_89: begin
          th_comp <= th_comp_90;
        end
        th_comp_90: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_91;
          end 
        end
        th_comp_91: begin
          _th_comp_offset_4 <= _th_comp_size_3;
          th_comp <= th_comp_92;
        end
        th_comp_92: begin
          axim_flag_68 <= 1;
          _th_comp_cond_92_9_1 <= 1;
          th_comp <= th_comp_93;
        end
        th_comp_93: begin
          th_comp <= th_comp_94;
        end
        th_comp_94: begin
          th_comp <= th_comp_95;
        end
        th_comp_95: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_96;
          end 
        end
        th_comp_96: begin
          axim_flag_69 <= 1;
          _th_comp_cond_96_10_1 <= 1;
          th_comp <= th_comp_97;
        end
        th_comp_97: begin
          th_comp <= th_comp_98;
        end
        th_comp_98: begin
          th_comp <= th_comp_99;
        end
        th_comp_99: begin
          if(_myaxi_read_idle) begin
            th_comp <= th_comp_100;
          end 
        end
        th_comp_100: begin
          _th_comp_size_23 <= _th_comp_size_3;
          _th_comp_offset_24 <= _th_comp_offset_4;
          th_comp <= th_comp_101;
        end
        th_comp_101: begin
          _th_comp_sum_25 <= 0;
          th_comp <= th_comp_102;
        end
        th_comp_102: begin
          _th_comp_count_26 <= 0;
          th_comp <= th_comp_103;
        end
        th_comp_103: begin
          _th_comp_write_offset_27 <= _th_comp_offset_24;
          th_comp <= th_comp_104;
        end
        th_comp_104: begin
          _th_comp_i_28 <= 0;
          th_comp <= th_comp_105;
        end
        th_comp_105: begin
          if(_th_comp_i_28 < _th_comp_size_23) begin
            th_comp <= th_comp_106;
          end else begin
            th_comp <= th_comp_119;
          end
        end
        th_comp_106: begin
          if(_tmp_70) begin
            _tmp_71 <= ram_a_0_rdata;
          end 
          if(_tmp_70) begin
            th_comp <= th_comp_107;
          end 
        end
        th_comp_107: begin
          _th_comp_x_29 <= _tmp_71;
          th_comp <= th_comp_108;
        end
        th_comp_108: begin
          if(_tmp_72) begin
            _tmp_73 <= ram_b_0_rdata;
          end 
          if(_tmp_72) begin
            th_comp <= th_comp_109;
          end 
        end
        th_comp_109: begin
          _th_comp_y_30 <= _tmp_73;
          th_comp <= th_comp_110;
        end
        th_comp_110: begin
          _th_comp_sum_25 <= _th_comp_sum_25 + _th_comp_x_29 * _th_comp_y_30;
          th_comp <= th_comp_111;
        end
        th_comp_111: begin
          _th_comp_val_31 <= _th_comp_sum_25 + _th_comp_x_29;
          th_comp <= th_comp_112;
        end
        th_comp_112: begin
          _th_comp_count_26 <= _th_comp_count_26 + 1;
          th_comp <= th_comp_113;
        end
        th_comp_113: begin
          if(_th_comp_count_26 == 4) begin
            th_comp <= th_comp_114;
          end else begin
            th_comp <= th_comp_118;
          end
        end
        th_comp_114: begin
          th_comp <= th_comp_115;
        end
        th_comp_115: begin
          _th_comp_write_offset_27 <= _th_comp_write_offset_27 + 1;
          th_comp <= th_comp_116;
        end
        th_comp_116: begin
          _th_comp_sum_25 <= 0;
          th_comp <= th_comp_117;
        end
        th_comp_117: begin
          _th_comp_count_26 <= 0;
          th_comp <= th_comp_118;
        end
        th_comp_118: begin
          _th_comp_i_28 <= _th_comp_i_28 + 1;
          th_comp <= th_comp_105;
        end
        th_comp_119: begin
          axim_flag_74 <= 1;
          _th_comp_cond_119_11_1 <= 1;
          th_comp <= th_comp_120;
        end
        th_comp_120: begin
          th_comp <= th_comp_121;
        end
        th_comp_121: begin
          th_comp <= th_comp_122;
        end
        th_comp_122: begin
          if(_myaxi_write_idle) begin
            th_comp <= th_comp_123;
          end 
        end
        th_comp_123: begin
          $display("# mystream");
          th_comp <= th_comp_124;
        end
        th_comp_124: begin
          _th_comp_size_32 <= _th_comp_size_3 >>> 2;
          _th_comp_offset_stream_33 <= 0;
          _th_comp_offset_seq_34 <= _th_comp_offset_4;
          th_comp <= th_comp_125;
        end
        th_comp_125: begin
          _th_comp_all_ok_35 <= 1;
          th_comp <= th_comp_126;
        end
        th_comp_126: begin
          _th_comp_i_36 <= 0;
          th_comp <= th_comp_127;
        end
        th_comp_127: begin
          if(_th_comp_i_36 < _th_comp_size_32) begin
            th_comp <= th_comp_128;
          end else begin
            th_comp <= th_comp_136;
          end
        end
        th_comp_128: begin
          if(_tmp_75) begin
            _tmp_76 <= ram_c_0_rdata;
          end 
          if(_tmp_75) begin
            th_comp <= th_comp_129;
          end 
        end
        th_comp_129: begin
          _th_comp_st_37 <= _tmp_76;
          th_comp <= th_comp_130;
        end
        th_comp_130: begin
          if(_tmp_77) begin
            _tmp_78 <= ram_c_0_rdata;
          end 
          if(_tmp_77) begin
            th_comp <= th_comp_131;
          end 
        end
        th_comp_131: begin
          _th_comp_sq_38 <= _tmp_78;
          th_comp <= th_comp_132;
        end
        th_comp_132: begin
          if(_th_comp_st_37 !== _th_comp_sq_38) begin
            th_comp <= th_comp_133;
          end else begin
            th_comp <= th_comp_135;
          end
        end
        th_comp_133: begin
          _th_comp_all_ok_35 <= 0;
          th_comp <= th_comp_134;
        end
        th_comp_134: begin
          $display("%d %d %d", _th_comp_i_36, _th_comp_st_37, _th_comp_sq_38);
          th_comp <= th_comp_135;
        end
        th_comp_135: begin
          _th_comp_i_36 <= _th_comp_i_36 + 1;
          th_comp <= th_comp_127;
        end
        th_comp_136: begin
          if(_th_comp_all_ok_35) begin
            th_comp <= th_comp_137;
          end else begin
            th_comp <= th_comp_139;
          end
        end
        th_comp_137: begin
          $display("OK");
          th_comp <= th_comp_138;
        end
        th_comp_138: begin
          th_comp <= th_comp_140;
        end
        th_comp_139: begin
          $display("NG");
          th_comp <= th_comp_140;
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

  localparam _macstream_a_source_fsm_0_1 = 1;
  localparam _macstream_a_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_a_source_fsm_0 <= _macstream_a_source_fsm_0_init;
    end else begin
      case(_macstream_a_source_fsm_0)
        _macstream_a_source_fsm_0_init: begin
          if(_macstream_start && (_macstream_a_source_mode == 0) && (_macstream_a_source_size > 0)) begin
            _macstream_a_source_fsm_0 <= _macstream_a_source_fsm_0_1;
          end 
        end
        _macstream_a_source_fsm_0_1: begin
          _macstream_a_source_fsm_0 <= _macstream_a_source_fsm_0_2;
        end
        _macstream_a_source_fsm_0_2: begin
          if(_macstream_a_source_count == 1) begin
            _macstream_a_source_fsm_0 <= _macstream_a_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _macstream_b_source_fsm_1_1 = 1;
  localparam _macstream_b_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_b_source_fsm_1 <= _macstream_b_source_fsm_1_init;
    end else begin
      case(_macstream_b_source_fsm_1)
        _macstream_b_source_fsm_1_init: begin
          if(_macstream_start && (_macstream_b_source_mode == 0) && (_macstream_b_source_size > 0)) begin
            _macstream_b_source_fsm_1 <= _macstream_b_source_fsm_1_1;
          end 
        end
        _macstream_b_source_fsm_1_1: begin
          _macstream_b_source_fsm_1 <= _macstream_b_source_fsm_1_2;
        end
        _macstream_b_source_fsm_1_2: begin
          if(_macstream_b_source_count == 1) begin
            _macstream_b_source_fsm_1 <= _macstream_b_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _macstream_c_sink_fsm_2_1 = 1;
  localparam _macstream_c_sink_fsm_2_2 = 2;
  localparam _macstream_c_sink_fsm_2_3 = 3;
  localparam _macstream_c_sink_fsm_2_4 = 4;
  localparam _macstream_c_sink_fsm_2_5 = 5;
  localparam _macstream_c_sink_fsm_2_6 = 6;
  localparam _macstream_c_sink_fsm_2_7 = 7;
  localparam _macstream_c_sink_fsm_2_8 = 8;
  localparam _macstream_c_sink_fsm_2_9 = 9;
  localparam _macstream_c_sink_fsm_2_10 = 10;
  localparam _macstream_c_sink_fsm_2_11 = 11;
  localparam _macstream_c_sink_fsm_2_12 = 12;
  localparam _macstream_c_sink_fsm_2_13 = 13;
  localparam _macstream_c_sink_fsm_2_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_init;
    end else begin
      case(_macstream_c_sink_fsm_2)
        _macstream_c_sink_fsm_2_init: begin
          if(_macstream_start && (_macstream_c_sink_mode == 0) && (_macstream_c_sink_size > 0)) begin
            _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_1;
          end 
        end
        _macstream_c_sink_fsm_2_1: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_2;
        end
        _macstream_c_sink_fsm_2_2: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_3;
        end
        _macstream_c_sink_fsm_2_3: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_4;
        end
        _macstream_c_sink_fsm_2_4: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_5;
        end
        _macstream_c_sink_fsm_2_5: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_6;
        end
        _macstream_c_sink_fsm_2_6: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_7;
        end
        _macstream_c_sink_fsm_2_7: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_8;
        end
        _macstream_c_sink_fsm_2_8: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_9;
        end
        _macstream_c_sink_fsm_2_9: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_10;
        end
        _macstream_c_sink_fsm_2_10: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_11;
        end
        _macstream_c_sink_fsm_2_11: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_12;
        end
        _macstream_c_sink_fsm_2_12: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_13;
        end
        _macstream_c_sink_fsm_2_13: begin
          _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_14;
        end
        _macstream_c_sink_fsm_2_14: begin
          if(_macstream_c_sink_count == 1) begin
            _macstream_c_sink_fsm_2 <= _macstream_c_sink_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _macstream_v_sink_fsm_3_1 = 1;
  localparam _macstream_v_sink_fsm_3_2 = 2;
  localparam _macstream_v_sink_fsm_3_3 = 3;
  localparam _macstream_v_sink_fsm_3_4 = 4;
  localparam _macstream_v_sink_fsm_3_5 = 5;
  localparam _macstream_v_sink_fsm_3_6 = 6;
  localparam _macstream_v_sink_fsm_3_7 = 7;
  localparam _macstream_v_sink_fsm_3_8 = 8;
  localparam _macstream_v_sink_fsm_3_9 = 9;
  localparam _macstream_v_sink_fsm_3_10 = 10;
  localparam _macstream_v_sink_fsm_3_11 = 11;
  localparam _macstream_v_sink_fsm_3_12 = 12;
  localparam _macstream_v_sink_fsm_3_13 = 13;
  localparam _macstream_v_sink_fsm_3_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_init;
    end else begin
      case(_macstream_v_sink_fsm_3)
        _macstream_v_sink_fsm_3_init: begin
          if(_macstream_start && (_macstream_v_sink_mode == 0) && (_macstream_v_sink_size > 0)) begin
            _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_1;
          end 
        end
        _macstream_v_sink_fsm_3_1: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_2;
        end
        _macstream_v_sink_fsm_3_2: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_3;
        end
        _macstream_v_sink_fsm_3_3: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_4;
        end
        _macstream_v_sink_fsm_3_4: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_5;
        end
        _macstream_v_sink_fsm_3_5: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_6;
        end
        _macstream_v_sink_fsm_3_6: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_7;
        end
        _macstream_v_sink_fsm_3_7: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_8;
        end
        _macstream_v_sink_fsm_3_8: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_9;
        end
        _macstream_v_sink_fsm_3_9: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_10;
        end
        _macstream_v_sink_fsm_3_10: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_11;
        end
        _macstream_v_sink_fsm_3_11: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_12;
        end
        _macstream_v_sink_fsm_3_12: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_13;
        end
        _macstream_v_sink_fsm_3_13: begin
          _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_14;
        end
        _macstream_v_sink_fsm_3_14: begin
          if(_macstream_v_sink_count == 1) begin
            _macstream_v_sink_fsm_3 <= _macstream_v_sink_fsm_3_init;
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
      axim_flag_42 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_42 <= 0;
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
          axim_flag_42 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
        end
      endcase
    end
  end

  localparam _mystream_x_source_fsm_0_1 = 1;
  localparam _mystream_x_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_x_source_fsm_0 <= _mystream_x_source_fsm_0_init;
    end else begin
      case(_mystream_x_source_fsm_0)
        _mystream_x_source_fsm_0_init: begin
          if(_mystream_start && (_mystream_x_source_mode == 0) && (_mystream_x_source_size > 0)) begin
            _mystream_x_source_fsm_0 <= _mystream_x_source_fsm_0_1;
          end 
        end
        _mystream_x_source_fsm_0_1: begin
          _mystream_x_source_fsm_0 <= _mystream_x_source_fsm_0_2;
        end
        _mystream_x_source_fsm_0_2: begin
          if(_mystream_x_source_count == 1) begin
            _mystream_x_source_fsm_0 <= _mystream_x_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_y_source_fsm_1_1 = 1;
  localparam _mystream_y_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_y_source_fsm_1 <= _mystream_y_source_fsm_1_init;
    end else begin
      case(_mystream_y_source_fsm_1)
        _mystream_y_source_fsm_1_init: begin
          if(_mystream_start && (_mystream_y_source_mode == 0) && (_mystream_y_source_size > 0)) begin
            _mystream_y_source_fsm_1 <= _mystream_y_source_fsm_1_1;
          end 
        end
        _mystream_y_source_fsm_1_1: begin
          _mystream_y_source_fsm_1 <= _mystream_y_source_fsm_1_2;
        end
        _mystream_y_source_fsm_1_2: begin
          if(_mystream_y_source_count == 1) begin
            _mystream_y_source_fsm_1 <= _mystream_y_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_z_sink_fsm_2_1 = 1;
  localparam _mystream_z_sink_fsm_2_2 = 2;
  localparam _mystream_z_sink_fsm_2_3 = 3;
  localparam _mystream_z_sink_fsm_2_4 = 4;
  localparam _mystream_z_sink_fsm_2_5 = 5;
  localparam _mystream_z_sink_fsm_2_6 = 6;
  localparam _mystream_z_sink_fsm_2_7 = 7;
  localparam _mystream_z_sink_fsm_2_8 = 8;
  localparam _mystream_z_sink_fsm_2_9 = 9;
  localparam _mystream_z_sink_fsm_2_10 = 10;
  localparam _mystream_z_sink_fsm_2_11 = 11;
  localparam _mystream_z_sink_fsm_2_12 = 12;
  localparam _mystream_z_sink_fsm_2_13 = 13;
  localparam _mystream_z_sink_fsm_2_14 = 14;
  localparam _mystream_z_sink_fsm_2_15 = 15;
  localparam _mystream_z_sink_fsm_2_16 = 16;
  localparam _mystream_z_sink_fsm_2_17 = 17;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_init;
    end else begin
      case(_mystream_z_sink_fsm_2)
        _mystream_z_sink_fsm_2_init: begin
          if(_mystream_start && (_mystream_z_sink_mode == 0) && (_mystream_z_sink_size > 0)) begin
            _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_1;
          end 
        end
        _mystream_z_sink_fsm_2_1: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_2;
        end
        _mystream_z_sink_fsm_2_2: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_3;
        end
        _mystream_z_sink_fsm_2_3: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_4;
        end
        _mystream_z_sink_fsm_2_4: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_5;
        end
        _mystream_z_sink_fsm_2_5: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_6;
        end
        _mystream_z_sink_fsm_2_6: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_7;
        end
        _mystream_z_sink_fsm_2_7: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_8;
        end
        _mystream_z_sink_fsm_2_8: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_9;
        end
        _mystream_z_sink_fsm_2_9: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_10;
        end
        _mystream_z_sink_fsm_2_10: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_11;
        end
        _mystream_z_sink_fsm_2_11: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_12;
        end
        _mystream_z_sink_fsm_2_12: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_13;
        end
        _mystream_z_sink_fsm_2_13: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_14;
        end
        _mystream_z_sink_fsm_2_14: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_15;
        end
        _mystream_z_sink_fsm_2_15: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_16;
        end
        _mystream_z_sink_fsm_2_16: begin
          _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_17;
        end
        _mystream_z_sink_fsm_2_17: begin
          if(mystream_v_data && (_mystream_z_sink_count == 1)) begin
            _mystream_z_sink_fsm_2 <= _mystream_z_sink_fsm_2_init;
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



module ram_d
(
  input CLK,
  input [10-1:0] ram_d_0_addr,
  output [32-1:0] ram_d_0_rdata,
  input [32-1:0] ram_d_0_wdata,
  input ram_d_0_wenable
);

  reg [10-1:0] ram_d_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_d_0_wenable) begin
      mem[ram_d_0_addr] <= ram_d_0_wdata;
    end 
    ram_d_0_daddr <= ram_d_0_addr;
  end

  assign ram_d_0_rdata = mem[ram_d_0_daddr];

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
    test_module = thread_stream_substream_reduce.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
