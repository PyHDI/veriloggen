from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_stream_substream_nested_reduce

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
  reg _macstream_start;
  reg _macstream_busy;
  reg [16-1:0] _macstream_a_fsm_sel;
  reg _macstream_a_idle;
  reg [16-1:0] _macstream_b_fsm_sel;
  reg _macstream_b_idle;
  reg [16-1:0] _macstream_const_fsm_sel;
  reg _macstream_reduce_reset;
  reg [16-1:0] _macstream_c_fsm_sel;
  reg [16-1:0] _macstream_v_fsm_sel;
  reg [32-1:0] _neststream_fsm;
  localparam _neststream_fsm_init = 0;
  reg _neststream_start;
  reg _neststream_busy;
  reg [16-1:0] _neststream_a_fsm_sel;
  reg _neststream_a_idle;
  reg [16-1:0] _neststream_b_fsm_sel;
  reg _neststream_b_idle;
  reg [16-1:0] _neststream_const_fsm_sel;
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

  reg signed [1-1:0] __delay_data_19;
  reg signed [1-1:0] __delay_data_20;
  reg signed [1-1:0] __delay_data_21;
  reg signed [1-1:0] __delay_data_22;
  reg signed [1-1:0] __delay_data_23;
  reg signed [1-1:0] __delay_data_24;
  reg signed [1-1:0] __delay_data_25;
  reg signed [32-1:0] _reduceadd_data_6;
  reg [33-1:0] _reduceadd_count_6;
  reg [1-1:0] _pulse_data_8;
  reg [33-1:0] _pulse_count_8;
  wire signed [32-1:0] macstream_c_data;
  assign macstream_c_data = _reduceadd_data_6;
  wire [1-1:0] macstream_v_data;
  assign macstream_v_data = _pulse_data_8;
  reg _substream_macstream_a_data_cond_18_0;
  reg _substream_macstream_b_data_cond_18_1;
  reg _substream_macstream_const_data_cond_18_2;
  reg [16-1:0] _neststream_c_fsm_sel;
  reg [16-1:0] _neststream_v_fsm_sel;
  reg [32-1:0] _mystream_fsm;
  localparam _mystream_fsm_init = 0;
  reg _mystream_start;
  reg _mystream_busy;
  reg [16-1:0] _mystream_x_fsm_sel;
  reg _mystream_x_idle;
  reg [16-1:0] _mystream_y_fsm_sel;
  reg _mystream_y_idle;
  reg [16-1:0] _mystream_const_fsm_sel;
  wire signed [32-1:0] neststream_a_data;
  wire signed [32-1:0] neststream_b_data;
  wire signed [32-1:0] neststream_const_data;
  reg signed [32-1:0] _plus_data_12;
  reg signed [32-1:0] _plus_data_16;
  reg signed [32-1:0] _plus_data_14;
  reg signed [32-1:0] __delay_data_35;
  reg signed [32-1:0] __variable_wdata_0;
  assign macstream_a_data = __variable_wdata_0;
  reg signed [32-1:0] __variable_wdata_1;
  assign macstream_b_data = __variable_wdata_1;
  reg signed [32-1:0] __parametervariable_wdata_2;
  assign macstream_const_data = __parametervariable_wdata_2;
  reg signed [32-1:0] __delay_data_36;
  reg signed [32-1:0] __delay_data_37;
  reg signed [32-1:0] __delay_data_38;
  reg signed [32-1:0] __delay_data_39;
  reg signed [32-1:0] __delay_data_40;
  reg signed [32-1:0] __delay_data_41;
  reg signed [32-1:0] __delay_data_42;
  reg signed [32-1:0] __delay_data_43;
  reg signed [32-1:0] __delay_data_44;
  reg signed [32-1:0] __substreamoutput_data_26;
  reg [1-1:0] __substreamoutput_data_30;
  reg signed [32-1:0] __delay_data_45;
  reg signed [32-1:0] _plus_data_27;
  reg [1-1:0] __delay_data_46;
  reg signed [32-1:0] _plus_data_28;
  reg [1-1:0] __delay_data_47;
  wire signed [32-1:0] neststream_c_data;
  assign neststream_c_data = _plus_data_28;
  wire [1-1:0] neststream_v_data;
  assign neststream_v_data = __delay_data_47;
  reg _substream_neststream_a_data_cond_34_3;
  reg _substream_neststream_b_data_cond_34_4;
  reg _substream_neststream_const_data_cond_34_5;
  reg [16-1:0] _mystream_z_fsm_sel;
  reg [16-1:0] _mystream_v_fsm_sel;
  reg [32-1:0] th_comp;
  localparam th_comp_init = 0;
  reg signed [32-1:0] _th_comp_size_6;
  reg signed [32-1:0] _th_comp_offset_7;
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
  reg signed [32-1:0] _th_comp_size_8;
  reg signed [32-1:0] _th_comp_offset_9;
  reg [32-1:0] _macstream_a_fsm_1;
  localparam _macstream_a_fsm_1_init = 0;
  reg [10-1:0] _macstream_a_offset_1;
  reg [11-1:0] _macstream_a_size_1;
  reg [10-1:0] _macstream_a_stride_1;
  reg [11-1:0] _macstream_a_count_1;
  reg [10-1:0] _macstream_a_raddr_1;
  reg _macstream_a_renable_1;
  reg _tmp_26;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  reg [32-1:0] _d1__macstream_a_fsm_1;
  reg __macstream_a_fsm_1_cond_1_0_1;
  reg __macstream_a_fsm_1_cond_2_1_1;
  reg [32-1:0] _macstream_b_fsm_2;
  localparam _macstream_b_fsm_2_init = 0;
  reg [10-1:0] _macstream_b_offset_2;
  reg [11-1:0] _macstream_b_size_2;
  reg [10-1:0] _macstream_b_stride_2;
  reg [11-1:0] _macstream_b_count_2;
  reg [10-1:0] _macstream_b_raddr_2;
  reg _macstream_b_renable_2;
  reg _tmp_27;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  reg [32-1:0] _d1__macstream_b_fsm_2;
  reg __macstream_b_fsm_2_cond_1_0_1;
  reg __macstream_b_fsm_2_cond_2_1_1;
  reg [32-1:0] _macstream_c_fsm_3;
  localparam _macstream_c_fsm_3_init = 0;
  reg [10-1:0] _macstream_c_offset_3;
  reg [11-1:0] _macstream_c_size_3;
  reg [10-1:0] _macstream_c_stride_3;
  reg [11-1:0] _macstream_c_count_3;
  reg [10-1:0] _macstream_c_waddr_3;
  reg _macstream_c_wenable_3;
  reg signed [32-1:0] _macstream_c_wdata_3;
  reg _ram_c_cond_0_1;
  reg [32-1:0] _d1__macstream_c_fsm_3;
  reg __macstream_c_fsm_3_cond_13_0_1;
  reg __macstream_c_fsm_3_cond_14_1_1;
  reg [32-1:0] _macstream_v_fsm_4;
  localparam _macstream_v_fsm_4_init = 0;
  reg [10-1:0] _macstream_v_offset_4;
  reg [11-1:0] _macstream_v_size_4;
  reg [10-1:0] _macstream_v_stride_4;
  reg [11-1:0] _macstream_v_count_4;
  reg [10-1:0] _macstream_v_waddr_4;
  reg _macstream_v_wenable_4;
  reg signed [32-1:0] _macstream_v_wdata_4;
  reg _ram_d_cond_0_1;
  reg [32-1:0] _d1__macstream_v_fsm_4;
  reg __macstream_v_fsm_4_cond_13_0_1;
  reg __macstream_v_fsm_4_cond_14_1_1;
  reg [32-1:0] _d1__macstream_fsm;
  reg __macstream_fsm_cond_0_0_1;
  reg [32-1:0] _d2__macstream_fsm;
  reg [32-1:0] _d3__macstream_fsm;
  reg [32-1:0] _d4__macstream_fsm;
  reg [32-1:0] _d5__macstream_fsm;
  reg __macstream_fsm_cond_0_1_1;
  reg __macstream_fsm_cond_0_1_2;
  reg __macstream_fsm_cond_0_1_3;
  reg __macstream_fsm_cond_0_1_4;
  reg __macstream_fsm_cond_0_1_5;
  wire _macstream_done;
  assign _macstream_done = _macstream_a_idle && _macstream_b_idle;
  reg [10-1:0] _tmp_28;
  reg [32-1:0] _tmp_29;
  reg [32-1:0] _tmp_30;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_31;
  reg [33-1:0] _tmp_32;
  reg [33-1:0] _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  wire _tmp_36;
  wire _tmp_37;
  assign _tmp_37 = 1;
  localparam _tmp_38 = 1;
  wire [_tmp_38-1:0] _tmp_39;
  assign _tmp_39 = (_tmp_36 || !_tmp_34) && (_tmp_37 || !_tmp_35);
  reg [_tmp_38-1:0] __tmp_39_1;
  wire signed [32-1:0] _tmp_40;
  reg signed [32-1:0] __tmp_40_1;
  assign _tmp_40 = (__tmp_39_1)? ram_c_0_rdata : __tmp_40_1;
  reg _tmp_41;
  reg _tmp_42;
  reg _tmp_43;
  reg _tmp_44;
  reg [33-1:0] _tmp_45;
  reg [9-1:0] _tmp_46;
  reg _myaxi_cond_2_1;
  reg _tmp_47;
  wire [32-1:0] __variable_data_48;
  wire __variable_valid_48;
  wire __variable_ready_48;
  assign __variable_ready_48 = (_tmp_fsm_2 == 4) && ((_tmp_46 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_49;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_5_0_1;
  reg [10-1:0] _tmp_50;
  reg [32-1:0] _tmp_51;
  reg [32-1:0] _tmp_52;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_53;
  reg [33-1:0] _tmp_54;
  reg [33-1:0] _tmp_55;
  reg [32-1:0] _tmp_56;
  reg _tmp_57;
  reg [33-1:0] _tmp_58;
  reg _tmp_59;
  wire [32-1:0] __variable_data_60;
  wire __variable_valid_60;
  wire __variable_ready_60;
  assign __variable_ready_60 = (_tmp_58 > 0) && !_tmp_59;
  reg _ram_a_cond_3_1;
  reg [9-1:0] _tmp_61;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_62;
  reg __tmp_fsm_3_cond_5_1_1;
  reg [10-1:0] _tmp_63;
  reg [32-1:0] _tmp_64;
  reg [32-1:0] _tmp_65;
  reg [32-1:0] _tmp_fsm_4;
  localparam _tmp_fsm_4_init = 0;
  reg [32-1:0] _tmp_66;
  reg [33-1:0] _tmp_67;
  reg [33-1:0] _tmp_68;
  reg [32-1:0] _tmp_69;
  reg _tmp_70;
  reg [33-1:0] _tmp_71;
  reg _tmp_72;
  wire [32-1:0] __variable_data_73;
  wire __variable_valid_73;
  wire __variable_ready_73;
  assign __variable_ready_73 = (_tmp_71 > 0) && !_tmp_72;
  reg _ram_b_cond_3_1;
  reg [9-1:0] _tmp_74;
  reg _myaxi_cond_5_1;
  reg [32-1:0] _d1__tmp_fsm_4;
  reg __tmp_fsm_4_cond_4_0_1;
  reg _tmp_75;
  reg __tmp_fsm_4_cond_5_1_1;
  reg signed [32-1:0] _th_comp_size_10;
  reg signed [32-1:0] _th_comp_offset_11;
  reg signed [32-1:0] _th_comp_sum_12;
  reg signed [32-1:0] _th_comp_count_13;
  reg signed [32-1:0] _th_comp_i_14;
  reg _tmp_76;
  reg _ram_a_cond_4_1;
  reg _ram_a_cond_5_1;
  reg _ram_a_cond_5_2;
  reg signed [32-1:0] _tmp_77;
  reg signed [32-1:0] _th_comp_a_15;
  reg _tmp_78;
  reg _ram_b_cond_4_1;
  reg _ram_b_cond_5_1;
  reg _ram_b_cond_5_2;
  reg signed [32-1:0] _tmp_79;
  reg signed [32-1:0] _th_comp_b_16;
  reg _ram_c_cond_1_1;
  reg _ram_d_cond_1_1;
  reg [10-1:0] _tmp_80;
  reg [32-1:0] _tmp_81;
  reg [32-1:0] _tmp_82;
  reg [32-1:0] _tmp_fsm_5;
  localparam _tmp_fsm_5_init = 0;
  reg [32-1:0] _tmp_83;
  reg [33-1:0] _tmp_84;
  reg [33-1:0] _tmp_85;
  reg _tmp_86;
  reg _tmp_87;
  wire _tmp_88;
  wire _tmp_89;
  assign _tmp_89 = 1;
  localparam _tmp_90 = 1;
  wire [_tmp_90-1:0] _tmp_91;
  assign _tmp_91 = (_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87);
  reg [_tmp_90-1:0] __tmp_91_1;
  wire signed [32-1:0] _tmp_92;
  reg signed [32-1:0] __tmp_92_1;
  assign _tmp_92 = (__tmp_91_1)? ram_c_0_rdata : __tmp_92_1;
  reg _tmp_93;
  reg _tmp_94;
  reg _tmp_95;
  reg _tmp_96;
  reg [33-1:0] _tmp_97;
  reg [9-1:0] _tmp_98;
  reg _myaxi_cond_6_1;
  reg _tmp_99;
  wire [32-1:0] __variable_data_100;
  wire __variable_valid_100;
  wire __variable_ready_100;
  assign __variable_ready_100 = (_tmp_fsm_5 == 4) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_7_1;
  reg _tmp_101;
  reg [32-1:0] _d1__tmp_fsm_5;
  reg __tmp_fsm_5_cond_5_0_1;
  reg signed [32-1:0] _th_comp_size_17;
  reg signed [32-1:0] _th_comp_offset_stream_18;
  reg signed [32-1:0] _th_comp_offset_seq_19;
  reg signed [32-1:0] _th_comp_all_ok_20;
  reg signed [32-1:0] _th_comp_i_21;
  reg _tmp_102;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_103;
  reg signed [32-1:0] _th_comp_st_22;
  reg _tmp_104;
  reg _ram_c_cond_4_1;
  reg _ram_c_cond_5_1;
  reg _ram_c_cond_5_2;
  reg signed [32-1:0] _tmp_105;
  reg signed [32-1:0] _th_comp_sq_23;
  reg [10-1:0] _tmp_106;
  reg [32-1:0] _tmp_107;
  reg [32-1:0] _tmp_108;
  reg [32-1:0] _tmp_fsm_6;
  localparam _tmp_fsm_6_init = 0;
  reg [32-1:0] _tmp_109;
  reg [33-1:0] _tmp_110;
  reg [33-1:0] _tmp_111;
  reg [32-1:0] _tmp_112;
  reg _tmp_113;
  reg [33-1:0] _tmp_114;
  reg _tmp_115;
  wire [32-1:0] __variable_data_116;
  wire __variable_valid_116;
  wire __variable_ready_116;
  assign __variable_ready_116 = (_tmp_114 > 0) && !_tmp_115;
  reg _ram_a_cond_6_1;
  reg [9-1:0] _tmp_117;
  reg _myaxi_cond_8_1;
  reg [32-1:0] _d1__tmp_fsm_6;
  reg __tmp_fsm_6_cond_4_0_1;
  reg _tmp_118;
  reg __tmp_fsm_6_cond_5_1_1;
  reg [10-1:0] _tmp_119;
  reg [32-1:0] _tmp_120;
  reg [32-1:0] _tmp_121;
  reg [32-1:0] _tmp_fsm_7;
  localparam _tmp_fsm_7_init = 0;
  reg [32-1:0] _tmp_122;
  reg [33-1:0] _tmp_123;
  reg [33-1:0] _tmp_124;
  reg [32-1:0] _tmp_125;
  reg _tmp_126;
  reg [33-1:0] _tmp_127;
  reg _tmp_128;
  wire [32-1:0] __variable_data_129;
  wire __variable_valid_129;
  wire __variable_ready_129;
  assign __variable_ready_129 = (_tmp_127 > 0) && !_tmp_128;
  reg _ram_b_cond_6_1;
  reg [9-1:0] _tmp_130;
  reg _myaxi_cond_9_1;
  reg [32-1:0] _d1__tmp_fsm_7;
  reg __tmp_fsm_7_cond_4_0_1;
  reg _tmp_131;
  reg __tmp_fsm_7_cond_5_1_1;
  reg signed [32-1:0] _th_comp_size_24;
  reg signed [32-1:0] _th_comp_offset_25;
  wire signed [32-1:0] mystream_x_data;
  wire signed [32-1:0] mystream_y_data;
  wire signed [32-1:0] mystream_const_data;
  reg signed [32-1:0] __variable_wdata_9;
  assign neststream_a_data = __variable_wdata_9;
  reg signed [32-1:0] __variable_wdata_10;
  assign neststream_b_data = __variable_wdata_10;
  reg signed [32-1:0] __parametervariable_wdata_11;
  assign neststream_const_data = __parametervariable_wdata_11;
  reg signed [32-1:0] __delay_data_51;
  reg signed [32-1:0] __delay_data_52;
  reg signed [32-1:0] __delay_data_53;
  reg signed [32-1:0] __delay_data_54;
  reg signed [32-1:0] __delay_data_55;
  reg signed [32-1:0] __delay_data_56;
  reg signed [32-1:0] __delay_data_57;
  reg signed [32-1:0] __delay_data_58;
  reg signed [32-1:0] __delay_data_59;
  reg signed [32-1:0] __delay_data_60;
  reg signed [32-1:0] __delay_data_61;
  reg signed [32-1:0] __delay_data_62;
  reg signed [32-1:0] __delay_data_63;
  reg signed [32-1:0] __delay_data_64;
  reg signed [32-1:0] __delay_data_65;
  reg signed [32-1:0] __substreamoutput_data_48;
  reg [1-1:0] __substreamoutput_data_49;
  reg signed [32-1:0] __delay_data_66;
  reg signed [32-1:0] _plus_data_50;
  reg [1-1:0] __delay_data_67;
  wire signed [32-1:0] mystream_z_data;
  assign mystream_z_data = _plus_data_50;
  wire [1-1:0] mystream_v_data;
  assign mystream_v_data = __delay_data_67;
  reg [32-1:0] _mystream_x_fsm_1;
  localparam _mystream_x_fsm_1_init = 0;
  reg [10-1:0] _mystream_x_offset_1;
  reg [11-1:0] _mystream_x_size_1;
  reg [10-1:0] _mystream_x_stride_1;
  reg [11-1:0] _mystream_x_count_1;
  reg [10-1:0] _mystream_x_raddr_1;
  reg _mystream_x_renable_1;
  reg _tmp_132;
  reg _ram_a_cond_7_1;
  reg _ram_a_cond_8_1;
  reg _ram_a_cond_8_2;
  reg signed [32-1:0] __variable_wdata_31;
  assign mystream_x_data = __variable_wdata_31;
  reg [32-1:0] _d1__mystream_x_fsm_1;
  reg __mystream_x_fsm_1_cond_1_0_1;
  reg __mystream_x_fsm_1_cond_2_1_1;
  reg [32-1:0] _mystream_y_fsm_2;
  localparam _mystream_y_fsm_2_init = 0;
  reg [10-1:0] _mystream_y_offset_2;
  reg [11-1:0] _mystream_y_size_2;
  reg [10-1:0] _mystream_y_stride_2;
  reg [11-1:0] _mystream_y_count_2;
  reg [10-1:0] _mystream_y_raddr_2;
  reg _mystream_y_renable_2;
  reg _tmp_133;
  reg _ram_b_cond_7_1;
  reg _ram_b_cond_8_1;
  reg _ram_b_cond_8_2;
  reg signed [32-1:0] __variable_wdata_32;
  assign mystream_y_data = __variable_wdata_32;
  reg [32-1:0] _d1__mystream_y_fsm_2;
  reg __mystream_y_fsm_2_cond_1_0_1;
  reg __mystream_y_fsm_2_cond_2_1_1;
  reg signed [32-1:0] __parametervariable_wdata_33;
  assign mystream_const_data = __parametervariable_wdata_33;
  reg [32-1:0] _mystream_z_fsm_3;
  localparam _mystream_z_fsm_3_init = 0;
  reg [10-1:0] _mystream_z_offset_3;
  reg [11-1:0] _mystream_z_size_3;
  reg [10-1:0] _mystream_z_stride_3;
  reg [11-1:0] _mystream_z_count_3;
  reg [10-1:0] _mystream_z_waddr_3;
  reg _mystream_z_wenable_3;
  reg signed [32-1:0] _mystream_z_wdata_3;
  reg _ram_c_cond_6_1;
  reg [32-1:0] _d1__mystream_z_fsm_3;
  reg __mystream_z_fsm_3_cond_22_0_1;
  reg __mystream_z_fsm_3_cond_23_1_1;
  reg [32-1:0] _d1__mystream_fsm;
  reg __mystream_fsm_cond_0_0_1;
  reg [32-1:0] _d6__macstream_fsm;
  reg [32-1:0] _d7__macstream_fsm;
  reg [32-1:0] _d8__macstream_fsm;
  reg [32-1:0] _d9__macstream_fsm;
  reg __macstream_fsm_cond_0_2_1;
  reg __macstream_fsm_cond_0_2_2;
  reg __macstream_fsm_cond_0_2_3;
  reg __macstream_fsm_cond_0_2_4;
  reg __macstream_fsm_cond_0_2_5;
  reg __macstream_fsm_cond_0_2_6;
  reg __macstream_fsm_cond_0_2_7;
  reg __macstream_fsm_cond_0_2_8;
  reg __macstream_fsm_cond_0_2_9;
  wire _mystream_done;
  assign _mystream_done = _mystream_x_idle && _mystream_y_idle;
  reg [10-1:0] _tmp_134;
  reg [32-1:0] _tmp_135;
  reg [32-1:0] _tmp_136;
  reg [32-1:0] _tmp_fsm_8;
  localparam _tmp_fsm_8_init = 0;
  reg [32-1:0] _tmp_137;
  reg [33-1:0] _tmp_138;
  reg [33-1:0] _tmp_139;
  reg _tmp_140;
  reg _tmp_141;
  wire _tmp_142;
  wire _tmp_143;
  assign _tmp_143 = 1;
  localparam _tmp_144 = 1;
  wire [_tmp_144-1:0] _tmp_145;
  assign _tmp_145 = (_tmp_142 || !_tmp_140) && (_tmp_143 || !_tmp_141);
  reg [_tmp_144-1:0] __tmp_145_1;
  wire signed [32-1:0] _tmp_146;
  reg signed [32-1:0] __tmp_146_1;
  assign _tmp_146 = (__tmp_145_1)? ram_c_0_rdata : __tmp_146_1;
  reg _tmp_147;
  reg _tmp_148;
  reg _tmp_149;
  reg _tmp_150;
  reg [33-1:0] _tmp_151;
  reg [9-1:0] _tmp_152;
  reg _myaxi_cond_10_1;
  reg _tmp_153;
  wire [32-1:0] __variable_data_154;
  wire __variable_valid_154;
  wire __variable_ready_154;
  assign __variable_ready_154 = (_tmp_fsm_8 == 4) && ((_tmp_152 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_11_1;
  reg _tmp_155;
  reg [32-1:0] _d1__tmp_fsm_8;
  reg __tmp_fsm_8_cond_5_0_1;
  reg [10-1:0] _tmp_156;
  reg [32-1:0] _tmp_157;
  reg [32-1:0] _tmp_158;
  reg [32-1:0] _tmp_fsm_9;
  localparam _tmp_fsm_9_init = 0;
  reg [32-1:0] _tmp_159;
  reg [33-1:0] _tmp_160;
  reg [33-1:0] _tmp_161;
  reg [32-1:0] _tmp_162;
  reg _tmp_163;
  reg [33-1:0] _tmp_164;
  reg _tmp_165;
  wire [32-1:0] __variable_data_166;
  wire __variable_valid_166;
  wire __variable_ready_166;
  assign __variable_ready_166 = (_tmp_164 > 0) && !_tmp_165;
  reg _ram_a_cond_9_1;
  reg [9-1:0] _tmp_167;
  reg _myaxi_cond_12_1;
  reg [32-1:0] _d1__tmp_fsm_9;
  reg __tmp_fsm_9_cond_4_0_1;
  reg _tmp_168;
  reg __tmp_fsm_9_cond_5_1_1;
  reg [10-1:0] _tmp_169;
  reg [32-1:0] _tmp_170;
  reg [32-1:0] _tmp_171;
  reg [32-1:0] _tmp_fsm_10;
  localparam _tmp_fsm_10_init = 0;
  reg [32-1:0] _tmp_172;
  reg [33-1:0] _tmp_173;
  reg [33-1:0] _tmp_174;
  reg [32-1:0] _tmp_175;
  reg _tmp_176;
  reg [33-1:0] _tmp_177;
  reg _tmp_178;
  wire [32-1:0] __variable_data_179;
  wire __variable_valid_179;
  wire __variable_ready_179;
  assign __variable_ready_179 = (_tmp_177 > 0) && !_tmp_178;
  reg _ram_b_cond_9_1;
  reg [9-1:0] _tmp_180;
  reg _myaxi_cond_13_1;
  assign myaxi_rready = (_tmp_fsm_0 == 4) || (_tmp_fsm_1 == 4) || (_tmp_fsm_3 == 4) || (_tmp_fsm_4 == 4) || (_tmp_fsm_6 == 4) || (_tmp_fsm_7 == 4) || (_tmp_fsm_9 == 4) || (_tmp_fsm_10 == 4);
  reg [32-1:0] _d1__tmp_fsm_10;
  reg __tmp_fsm_10_cond_4_0_1;
  reg _tmp_181;
  reg __tmp_fsm_10_cond_5_1_1;
  reg signed [32-1:0] _th_comp_size_26;
  reg signed [32-1:0] _th_comp_offset_27;
  reg signed [32-1:0] _th_comp_sum_28;
  reg signed [32-1:0] _th_comp_count_29;
  reg signed [32-1:0] _th_comp_write_offset_30;
  reg signed [32-1:0] _th_comp_i_31;
  reg _tmp_182;
  reg _ram_a_cond_10_1;
  reg _ram_a_cond_11_1;
  reg _ram_a_cond_11_2;
  reg signed [32-1:0] _tmp_183;
  reg signed [32-1:0] _th_comp_x_32;
  reg _tmp_184;
  reg _ram_b_cond_10_1;
  reg _ram_b_cond_11_1;
  reg _ram_b_cond_11_2;
  reg signed [32-1:0] _tmp_185;
  reg signed [32-1:0] _th_comp_y_33;
  reg signed [32-1:0] _th_comp_val_34;
  reg _ram_c_cond_7_1;
  reg [10-1:0] _tmp_186;
  reg [32-1:0] _tmp_187;
  reg [32-1:0] _tmp_188;
  reg [32-1:0] _tmp_fsm_11;
  localparam _tmp_fsm_11_init = 0;
  reg [32-1:0] _tmp_189;
  reg [33-1:0] _tmp_190;
  reg [33-1:0] _tmp_191;
  reg _tmp_192;
  reg _tmp_193;
  wire _tmp_194;
  wire _tmp_195;
  assign _tmp_195 = 1;
  localparam _tmp_196 = 1;
  wire [_tmp_196-1:0] _tmp_197;
  assign _tmp_197 = (_tmp_194 || !_tmp_192) && (_tmp_195 || !_tmp_193);
  reg [_tmp_196-1:0] __tmp_197_1;
  wire signed [32-1:0] _tmp_198;
  reg signed [32-1:0] __tmp_198_1;
  assign _tmp_198 = (__tmp_197_1)? ram_c_0_rdata : __tmp_198_1;
  reg _tmp_199;
  reg _tmp_200;
  reg _tmp_201;
  reg _tmp_202;
  reg [33-1:0] _tmp_203;
  reg [9-1:0] _tmp_204;
  reg _myaxi_cond_14_1;
  reg _tmp_205;
  wire [32-1:0] __variable_data_206;
  wire __variable_valid_206;
  wire __variable_ready_206;
  assign __variable_ready_206 = (_tmp_fsm_11 == 4) && ((_tmp_204 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_15_1;
  reg _tmp_207;
  reg [32-1:0] _d1__tmp_fsm_11;
  reg __tmp_fsm_11_cond_5_0_1;
  reg signed [32-1:0] _th_comp_size_35;
  reg signed [32-1:0] _th_comp_offset_stream_36;
  reg signed [32-1:0] _th_comp_offset_seq_37;
  reg signed [32-1:0] _th_comp_all_ok_38;
  reg signed [32-1:0] _th_comp_i_39;
  reg _tmp_208;
  reg _ram_c_cond_8_1;
  reg _ram_c_cond_9_1;
  reg _ram_c_cond_9_2;
  reg signed [32-1:0] _tmp_209;
  reg signed [32-1:0] _th_comp_st_40;
  reg _tmp_210;
  reg _ram_c_cond_10_1;
  reg _ram_c_cond_11_1;
  reg _ram_c_cond_11_2;
  reg signed [32-1:0] _tmp_211;
  reg signed [32-1:0] _th_comp_sq_41;

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
      _tmp_46 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_47 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_61 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_74 <= 0;
      _myaxi_cond_5_1 <= 0;
      _tmp_98 <= 0;
      _myaxi_cond_6_1 <= 0;
      _tmp_99 <= 0;
      _myaxi_cond_7_1 <= 0;
      _tmp_117 <= 0;
      _myaxi_cond_8_1 <= 0;
      _tmp_130 <= 0;
      _myaxi_cond_9_1 <= 0;
      _tmp_152 <= 0;
      _myaxi_cond_10_1 <= 0;
      _tmp_153 <= 0;
      _myaxi_cond_11_1 <= 0;
      _tmp_167 <= 0;
      _myaxi_cond_12_1 <= 0;
      _tmp_180 <= 0;
      _myaxi_cond_13_1 <= 0;
      _tmp_204 <= 0;
      _myaxi_cond_14_1 <= 0;
      _tmp_205 <= 0;
      _myaxi_cond_15_1 <= 0;
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
        _tmp_47 <= 0;
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
        _tmp_99 <= 0;
      end 
      if(_myaxi_cond_8_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_9_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_10_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_11_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_153 <= 0;
      end 
      if(_myaxi_cond_12_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_13_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_14_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_15_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_205 <= 0;
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
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_46 == 0))) begin
        myaxi_awaddr <= _tmp_31;
        myaxi_awlen <= _tmp_32 - 1;
        myaxi_awvalid <= 1;
        _tmp_46 <= _tmp_32;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_46 == 0)) && (_tmp_32 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_48 && ((_tmp_fsm_2 == 4) && ((_tmp_46 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_46 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_46 > 0))) begin
        myaxi_wdata <= __variable_data_48;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_46 <= _tmp_46 - 1;
      end 
      if(__variable_valid_48 && ((_tmp_fsm_2 == 4) && ((_tmp_46 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_46 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_46 > 0)) && (_tmp_46 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_47 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_47 <= _tmp_47;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_61 == 0))) begin
        myaxi_araddr <= _tmp_53;
        myaxi_arlen <= _tmp_54 - 1;
        myaxi_arvalid <= 1;
        _tmp_61 <= _tmp_54;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_61 > 0)) begin
        _tmp_61 <= _tmp_61 - 1;
      end 
      if((_tmp_fsm_4 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_74 == 0))) begin
        myaxi_araddr <= _tmp_66;
        myaxi_arlen <= _tmp_67 - 1;
        myaxi_arvalid <= 1;
        _tmp_74 <= _tmp_67;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_74 > 0)) begin
        _tmp_74 <= _tmp_74 - 1;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_98 == 0))) begin
        myaxi_awaddr <= _tmp_83;
        myaxi_awlen <= _tmp_84 - 1;
        myaxi_awvalid <= 1;
        _tmp_98 <= _tmp_84;
      end 
      if((_tmp_fsm_5 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_98 == 0)) && (_tmp_84 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_6_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_100 && ((_tmp_fsm_5 == 4) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_98 > 0))) begin
        myaxi_wdata <= __variable_data_100;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_98 <= _tmp_98 - 1;
      end 
      if(__variable_valid_100 && ((_tmp_fsm_5 == 4) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_98 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_98 > 0)) && (_tmp_98 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_99 <= 1;
      end 
      _myaxi_cond_7_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_99 <= _tmp_99;
      end 
      if((_tmp_fsm_6 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_117 == 0))) begin
        myaxi_araddr <= _tmp_109;
        myaxi_arlen <= _tmp_110 - 1;
        myaxi_arvalid <= 1;
        _tmp_117 <= _tmp_110;
      end 
      _myaxi_cond_8_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_117 > 0)) begin
        _tmp_117 <= _tmp_117 - 1;
      end 
      if((_tmp_fsm_7 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_130 == 0))) begin
        myaxi_araddr <= _tmp_122;
        myaxi_arlen <= _tmp_123 - 1;
        myaxi_arvalid <= 1;
        _tmp_130 <= _tmp_123;
      end 
      _myaxi_cond_9_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_130 > 0)) begin
        _tmp_130 <= _tmp_130 - 1;
      end 
      if((_tmp_fsm_8 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_152 == 0))) begin
        myaxi_awaddr <= _tmp_137;
        myaxi_awlen <= _tmp_138 - 1;
        myaxi_awvalid <= 1;
        _tmp_152 <= _tmp_138;
      end 
      if((_tmp_fsm_8 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_152 == 0)) && (_tmp_138 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_10_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_154 && ((_tmp_fsm_8 == 4) && ((_tmp_152 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_152 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_152 > 0))) begin
        myaxi_wdata <= __variable_data_154;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_152 <= _tmp_152 - 1;
      end 
      if(__variable_valid_154 && ((_tmp_fsm_8 == 4) && ((_tmp_152 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_152 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_152 > 0)) && (_tmp_152 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_153 <= 1;
      end 
      _myaxi_cond_11_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_153 <= _tmp_153;
      end 
      if((_tmp_fsm_9 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_167 == 0))) begin
        myaxi_araddr <= _tmp_159;
        myaxi_arlen <= _tmp_160 - 1;
        myaxi_arvalid <= 1;
        _tmp_167 <= _tmp_160;
      end 
      _myaxi_cond_12_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_167 > 0)) begin
        _tmp_167 <= _tmp_167 - 1;
      end 
      if((_tmp_fsm_10 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_180 == 0))) begin
        myaxi_araddr <= _tmp_172;
        myaxi_arlen <= _tmp_173 - 1;
        myaxi_arvalid <= 1;
        _tmp_180 <= _tmp_173;
      end 
      _myaxi_cond_13_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_180 > 0)) begin
        _tmp_180 <= _tmp_180 - 1;
      end 
      if((_tmp_fsm_11 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_204 == 0))) begin
        myaxi_awaddr <= _tmp_189;
        myaxi_awlen <= _tmp_190 - 1;
        myaxi_awvalid <= 1;
        _tmp_204 <= _tmp_190;
      end 
      if((_tmp_fsm_11 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_204 == 0)) && (_tmp_190 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_14_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(__variable_valid_206 && ((_tmp_fsm_11 == 4) && ((_tmp_204 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_204 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_204 > 0))) begin
        myaxi_wdata <= __variable_data_206;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_204 <= _tmp_204 - 1;
      end 
      if(__variable_valid_206 && ((_tmp_fsm_11 == 4) && ((_tmp_204 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_204 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_204 > 0)) && (_tmp_204 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_205 <= 1;
      end 
      _myaxi_cond_15_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_205 <= _tmp_205;
      end 
    end
  end

  assign __variable_data_10 = _tmp_6;
  assign __variable_valid_10 = _tmp_7;
  assign __variable_data_23 = _tmp_19;
  assign __variable_valid_23 = _tmp_20;
  assign __variable_data_60 = _tmp_56;
  assign __variable_valid_60 = _tmp_57;
  assign __variable_data_73 = _tmp_69;
  assign __variable_valid_73 = _tmp_70;
  assign __variable_data_116 = _tmp_112;
  assign __variable_valid_116 = _tmp_113;
  assign __variable_data_129 = _tmp_125;
  assign __variable_valid_129 = _tmp_126;
  assign __variable_data_166 = _tmp_162;
  assign __variable_valid_166 = _tmp_163;
  assign __variable_data_179 = _tmp_175;
  assign __variable_valid_179 = _tmp_176;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_8 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_9 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_26 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _ram_a_cond_3_1 <= 0;
      _ram_a_cond_4_1 <= 0;
      _tmp_76 <= 0;
      _ram_a_cond_5_1 <= 0;
      _ram_a_cond_5_2 <= 0;
      _tmp_114 <= 0;
      _tmp_115 <= 0;
      _ram_a_cond_6_1 <= 0;
      _ram_a_cond_7_1 <= 0;
      _tmp_132 <= 0;
      _ram_a_cond_8_1 <= 0;
      _ram_a_cond_8_2 <= 0;
      _tmp_164 <= 0;
      _tmp_165 <= 0;
      _ram_a_cond_9_1 <= 0;
      _ram_a_cond_10_1 <= 0;
      _tmp_182 <= 0;
      _ram_a_cond_11_1 <= 0;
      _ram_a_cond_11_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_26 <= 0;
      end 
      if(_ram_a_cond_5_2) begin
        _tmp_76 <= 0;
      end 
      if(_ram_a_cond_8_2) begin
        _tmp_132 <= 0;
      end 
      if(_ram_a_cond_11_2) begin
        _tmp_182 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_9 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_26 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if(_ram_a_cond_3_1) begin
        ram_a_0_wenable <= 0;
        _tmp_59 <= 0;
      end 
      if(_ram_a_cond_4_1) begin
        _tmp_76 <= 1;
      end 
      _ram_a_cond_5_2 <= _ram_a_cond_5_1;
      if(_ram_a_cond_6_1) begin
        ram_a_0_wenable <= 0;
        _tmp_115 <= 0;
      end 
      if(_ram_a_cond_7_1) begin
        _tmp_132 <= 1;
      end 
      _ram_a_cond_8_2 <= _ram_a_cond_8_1;
      if(_ram_a_cond_9_1) begin
        ram_a_0_wenable <= 0;
        _tmp_165 <= 0;
      end 
      if(_ram_a_cond_10_1) begin
        _tmp_182 <= 1;
      end 
      _ram_a_cond_11_2 <= _ram_a_cond_11_1;
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
      if(_macstream_a_renable_1) begin
        ram_a_0_addr <= _macstream_a_raddr_1;
      end 
      _ram_a_cond_1_1 <= _macstream_a_renable_1;
      _ram_a_cond_2_1 <= _macstream_a_renable_1;
      if((_tmp_fsm_3 == 1) && (_tmp_58 == 0)) begin
        ram_a_0_addr <= _tmp_50 - 1;
        _tmp_58 <= _tmp_52;
      end 
      if(__variable_valid_60 && ((_tmp_58 > 0) && !_tmp_59) && (_tmp_58 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= __variable_data_60;
        ram_a_0_wenable <= 1;
        _tmp_58 <= _tmp_58 - 1;
      end 
      if(__variable_valid_60 && ((_tmp_58 > 0) && !_tmp_59) && (_tmp_58 == 1)) begin
        _tmp_59 <= 1;
      end 
      _ram_a_cond_3_1 <= 1;
      if(th_comp == 26) begin
        ram_a_0_addr <= _th_comp_i_14 + _th_comp_offset_11;
      end 
      _ram_a_cond_4_1 <= th_comp == 26;
      _ram_a_cond_5_1 <= th_comp == 26;
      if((_tmp_fsm_6 == 1) && (_tmp_114 == 0)) begin
        ram_a_0_addr <= _tmp_106 - 1;
        _tmp_114 <= _tmp_108;
      end 
      if(__variable_valid_116 && ((_tmp_114 > 0) && !_tmp_115) && (_tmp_114 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= __variable_data_116;
        ram_a_0_wenable <= 1;
        _tmp_114 <= _tmp_114 - 1;
      end 
      if(__variable_valid_116 && ((_tmp_114 > 0) && !_tmp_115) && (_tmp_114 == 1)) begin
        _tmp_115 <= 1;
      end 
      _ram_a_cond_6_1 <= 1;
      if(_mystream_x_renable_1) begin
        ram_a_0_addr <= _mystream_x_raddr_1;
      end 
      _ram_a_cond_7_1 <= _mystream_x_renable_1;
      _ram_a_cond_8_1 <= _mystream_x_renable_1;
      if((_tmp_fsm_9 == 1) && (_tmp_164 == 0)) begin
        ram_a_0_addr <= _tmp_156 - 1;
        _tmp_164 <= _tmp_158;
      end 
      if(__variable_valid_166 && ((_tmp_164 > 0) && !_tmp_165) && (_tmp_164 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= __variable_data_166;
        ram_a_0_wenable <= 1;
        _tmp_164 <= _tmp_164 - 1;
      end 
      if(__variable_valid_166 && ((_tmp_164 > 0) && !_tmp_165) && (_tmp_164 == 1)) begin
        _tmp_165 <= 1;
      end 
      _ram_a_cond_9_1 <= 1;
      if(th_comp == 82) begin
        ram_a_0_addr <= _th_comp_i_31 + _th_comp_offset_27;
      end 
      _ram_a_cond_10_1 <= th_comp == 82;
      _ram_a_cond_11_1 <= th_comp == 82;
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
      _ram_b_cond_1_1 <= 0;
      _tmp_27 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
      _tmp_71 <= 0;
      _tmp_72 <= 0;
      _ram_b_cond_3_1 <= 0;
      _ram_b_cond_4_1 <= 0;
      _tmp_78 <= 0;
      _ram_b_cond_5_1 <= 0;
      _ram_b_cond_5_2 <= 0;
      _tmp_127 <= 0;
      _tmp_128 <= 0;
      _ram_b_cond_6_1 <= 0;
      _ram_b_cond_7_1 <= 0;
      _tmp_133 <= 0;
      _ram_b_cond_8_1 <= 0;
      _ram_b_cond_8_2 <= 0;
      _tmp_177 <= 0;
      _tmp_178 <= 0;
      _ram_b_cond_9_1 <= 0;
      _ram_b_cond_10_1 <= 0;
      _tmp_184 <= 0;
      _ram_b_cond_11_1 <= 0;
      _ram_b_cond_11_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_27 <= 0;
      end 
      if(_ram_b_cond_5_2) begin
        _tmp_78 <= 0;
      end 
      if(_ram_b_cond_8_2) begin
        _tmp_133 <= 0;
      end 
      if(_ram_b_cond_11_2) begin
        _tmp_184 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_22 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_27 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if(_ram_b_cond_3_1) begin
        ram_b_0_wenable <= 0;
        _tmp_72 <= 0;
      end 
      if(_ram_b_cond_4_1) begin
        _tmp_78 <= 1;
      end 
      _ram_b_cond_5_2 <= _ram_b_cond_5_1;
      if(_ram_b_cond_6_1) begin
        ram_b_0_wenable <= 0;
        _tmp_128 <= 0;
      end 
      if(_ram_b_cond_7_1) begin
        _tmp_133 <= 1;
      end 
      _ram_b_cond_8_2 <= _ram_b_cond_8_1;
      if(_ram_b_cond_9_1) begin
        ram_b_0_wenable <= 0;
        _tmp_178 <= 0;
      end 
      if(_ram_b_cond_10_1) begin
        _tmp_184 <= 1;
      end 
      _ram_b_cond_11_2 <= _ram_b_cond_11_1;
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
      if(_macstream_b_renable_2) begin
        ram_b_0_addr <= _macstream_b_raddr_2;
      end 
      _ram_b_cond_1_1 <= _macstream_b_renable_2;
      _ram_b_cond_2_1 <= _macstream_b_renable_2;
      if((_tmp_fsm_4 == 1) && (_tmp_71 == 0)) begin
        ram_b_0_addr <= _tmp_63 - 1;
        _tmp_71 <= _tmp_65;
      end 
      if(__variable_valid_73 && ((_tmp_71 > 0) && !_tmp_72) && (_tmp_71 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= __variable_data_73;
        ram_b_0_wenable <= 1;
        _tmp_71 <= _tmp_71 - 1;
      end 
      if(__variable_valid_73 && ((_tmp_71 > 0) && !_tmp_72) && (_tmp_71 == 1)) begin
        _tmp_72 <= 1;
      end 
      _ram_b_cond_3_1 <= 1;
      if(th_comp == 28) begin
        ram_b_0_addr <= _th_comp_i_14 + _th_comp_offset_11;
      end 
      _ram_b_cond_4_1 <= th_comp == 28;
      _ram_b_cond_5_1 <= th_comp == 28;
      if((_tmp_fsm_7 == 1) && (_tmp_127 == 0)) begin
        ram_b_0_addr <= _tmp_119 - 1;
        _tmp_127 <= _tmp_121;
      end 
      if(__variable_valid_129 && ((_tmp_127 > 0) && !_tmp_128) && (_tmp_127 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= __variable_data_129;
        ram_b_0_wenable <= 1;
        _tmp_127 <= _tmp_127 - 1;
      end 
      if(__variable_valid_129 && ((_tmp_127 > 0) && !_tmp_128) && (_tmp_127 == 1)) begin
        _tmp_128 <= 1;
      end 
      _ram_b_cond_6_1 <= 1;
      if(_mystream_y_renable_2) begin
        ram_b_0_addr <= _mystream_y_raddr_2;
      end 
      _ram_b_cond_7_1 <= _mystream_y_renable_2;
      _ram_b_cond_8_1 <= _mystream_y_renable_2;
      if((_tmp_fsm_10 == 1) && (_tmp_177 == 0)) begin
        ram_b_0_addr <= _tmp_169 - 1;
        _tmp_177 <= _tmp_171;
      end 
      if(__variable_valid_179 && ((_tmp_177 > 0) && !_tmp_178) && (_tmp_177 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= __variable_data_179;
        ram_b_0_wenable <= 1;
        _tmp_177 <= _tmp_177 - 1;
      end 
      if(__variable_valid_179 && ((_tmp_177 > 0) && !_tmp_178) && (_tmp_177 == 1)) begin
        _tmp_178 <= 1;
      end 
      _ram_b_cond_9_1 <= 1;
      if(th_comp == 84) begin
        ram_b_0_addr <= _th_comp_i_31 + _th_comp_offset_27;
      end 
      _ram_b_cond_10_1 <= th_comp == 84;
      _ram_b_cond_11_1 <= th_comp == 84;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_39_1 <= 0;
      __tmp_40_1 <= 0;
      _tmp_44 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_42 <= 0;
      _tmp_43 <= 0;
      _tmp_41 <= 0;
      _tmp_45 <= 0;
      _ram_c_cond_1_1 <= 0;
      __tmp_91_1 <= 0;
      __tmp_92_1 <= 0;
      _tmp_96 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_93 <= 0;
      _tmp_97 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_102 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
      _ram_c_cond_4_1 <= 0;
      _tmp_104 <= 0;
      _ram_c_cond_5_1 <= 0;
      _ram_c_cond_5_2 <= 0;
      _ram_c_cond_6_1 <= 0;
      __tmp_145_1 <= 0;
      __tmp_146_1 <= 0;
      _tmp_150 <= 0;
      _tmp_140 <= 0;
      _tmp_141 <= 0;
      _tmp_148 <= 0;
      _tmp_149 <= 0;
      _tmp_147 <= 0;
      _tmp_151 <= 0;
      _ram_c_cond_7_1 <= 0;
      __tmp_197_1 <= 0;
      __tmp_198_1 <= 0;
      _tmp_202 <= 0;
      _tmp_192 <= 0;
      _tmp_193 <= 0;
      _tmp_200 <= 0;
      _tmp_201 <= 0;
      _tmp_199 <= 0;
      _tmp_203 <= 0;
      _ram_c_cond_8_1 <= 0;
      _tmp_208 <= 0;
      _ram_c_cond_9_1 <= 0;
      _ram_c_cond_9_2 <= 0;
      _ram_c_cond_10_1 <= 0;
      _tmp_210 <= 0;
      _ram_c_cond_11_1 <= 0;
      _ram_c_cond_11_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_102 <= 0;
      end 
      if(_ram_c_cond_5_2) begin
        _tmp_104 <= 0;
      end 
      if(_ram_c_cond_9_2) begin
        _tmp_208 <= 0;
      end 
      if(_ram_c_cond_11_2) begin
        _tmp_210 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_102 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(_ram_c_cond_4_1) begin
        _tmp_104 <= 1;
      end 
      _ram_c_cond_5_2 <= _ram_c_cond_5_1;
      if(_ram_c_cond_6_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_7_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_8_1) begin
        _tmp_208 <= 1;
      end 
      _ram_c_cond_9_2 <= _ram_c_cond_9_1;
      if(_ram_c_cond_10_1) begin
        _tmp_210 <= 1;
      end 
      _ram_c_cond_11_2 <= _ram_c_cond_11_1;
      if(_macstream_c_wenable_3) begin
        ram_c_0_addr <= _macstream_c_waddr_3;
        ram_c_0_wdata <= _macstream_c_wdata_3;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= _macstream_c_wenable_3;
      __tmp_39_1 <= _tmp_39;
      __tmp_40_1 <= _tmp_40;
      if((_tmp_36 || !_tmp_34) && (_tmp_37 || !_tmp_35) && _tmp_42) begin
        _tmp_44 <= 0;
        _tmp_34 <= 0;
        _tmp_35 <= 0;
        _tmp_42 <= 0;
      end 
      if((_tmp_36 || !_tmp_34) && (_tmp_37 || !_tmp_35) && _tmp_41) begin
        _tmp_34 <= 1;
        _tmp_35 <= 1;
        _tmp_44 <= _tmp_43;
        _tmp_43 <= 0;
        _tmp_41 <= 0;
        _tmp_42 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_45 == 0) && !_tmp_43 && !_tmp_44) begin
        ram_c_0_addr <= _tmp_28;
        _tmp_45 <= _tmp_30 - 1;
        _tmp_41 <= 1;
        _tmp_43 <= _tmp_30 == 1;
      end 
      if((_tmp_36 || !_tmp_34) && (_tmp_37 || !_tmp_35) && (_tmp_45 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_45 <= _tmp_45 - 1;
        _tmp_41 <= 1;
        _tmp_43 <= 0;
      end 
      if((_tmp_36 || !_tmp_34) && (_tmp_37 || !_tmp_35) && (_tmp_45 == 1)) begin
        _tmp_43 <= 1;
      end 
      if(th_comp == 32) begin
        ram_c_0_addr <= _th_comp_i_14 + _th_comp_offset_11;
        ram_c_0_wdata <= _th_comp_sum_12;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_1_1 <= th_comp == 32;
      __tmp_91_1 <= _tmp_91;
      __tmp_92_1 <= _tmp_92;
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && _tmp_94) begin
        _tmp_96 <= 0;
        _tmp_86 <= 0;
        _tmp_87 <= 0;
        _tmp_94 <= 0;
      end 
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && _tmp_93) begin
        _tmp_86 <= 1;
        _tmp_87 <= 1;
        _tmp_96 <= _tmp_95;
        _tmp_95 <= 0;
        _tmp_93 <= 0;
        _tmp_94 <= 1;
      end 
      if((_tmp_fsm_5 == 1) && (_tmp_97 == 0) && !_tmp_95 && !_tmp_96) begin
        ram_c_0_addr <= _tmp_80;
        _tmp_97 <= _tmp_82 - 1;
        _tmp_93 <= 1;
        _tmp_95 <= _tmp_82 == 1;
      end 
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && (_tmp_97 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_97 <= _tmp_97 - 1;
        _tmp_93 <= 1;
        _tmp_95 <= 0;
      end 
      if((_tmp_88 || !_tmp_86) && (_tmp_89 || !_tmp_87) && (_tmp_97 == 1)) begin
        _tmp_95 <= 1;
      end 
      if(th_comp == 45) begin
        ram_c_0_addr <= _th_comp_i_21 + _th_comp_offset_stream_18;
      end 
      _ram_c_cond_2_1 <= th_comp == 45;
      _ram_c_cond_3_1 <= th_comp == 45;
      if(th_comp == 47) begin
        ram_c_0_addr <= _th_comp_i_21 + _th_comp_offset_seq_19;
      end 
      _ram_c_cond_4_1 <= th_comp == 47;
      _ram_c_cond_5_1 <= th_comp == 47;
      if(_mystream_z_wenable_3) begin
        ram_c_0_addr <= _mystream_z_waddr_3;
        ram_c_0_wdata <= _mystream_z_wdata_3;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_6_1 <= _mystream_z_wenable_3;
      __tmp_145_1 <= _tmp_145;
      __tmp_146_1 <= _tmp_146;
      if((_tmp_142 || !_tmp_140) && (_tmp_143 || !_tmp_141) && _tmp_148) begin
        _tmp_150 <= 0;
        _tmp_140 <= 0;
        _tmp_141 <= 0;
        _tmp_148 <= 0;
      end 
      if((_tmp_142 || !_tmp_140) && (_tmp_143 || !_tmp_141) && _tmp_147) begin
        _tmp_140 <= 1;
        _tmp_141 <= 1;
        _tmp_150 <= _tmp_149;
        _tmp_149 <= 0;
        _tmp_147 <= 0;
        _tmp_148 <= 1;
      end 
      if((_tmp_fsm_8 == 1) && (_tmp_151 == 0) && !_tmp_149 && !_tmp_150) begin
        ram_c_0_addr <= _tmp_134;
        _tmp_151 <= _tmp_136 - 1;
        _tmp_147 <= 1;
        _tmp_149 <= _tmp_136 == 1;
      end 
      if((_tmp_142 || !_tmp_140) && (_tmp_143 || !_tmp_141) && (_tmp_151 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_151 <= _tmp_151 - 1;
        _tmp_147 <= 1;
        _tmp_149 <= 0;
      end 
      if((_tmp_142 || !_tmp_140) && (_tmp_143 || !_tmp_141) && (_tmp_151 == 1)) begin
        _tmp_149 <= 1;
      end 
      if(th_comp == 90) begin
        ram_c_0_addr <= _th_comp_write_offset_30;
        ram_c_0_wdata <= _th_comp_val_34;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_7_1 <= th_comp == 90;
      __tmp_197_1 <= _tmp_197;
      __tmp_198_1 <= _tmp_198;
      if((_tmp_194 || !_tmp_192) && (_tmp_195 || !_tmp_193) && _tmp_200) begin
        _tmp_202 <= 0;
        _tmp_192 <= 0;
        _tmp_193 <= 0;
        _tmp_200 <= 0;
      end 
      if((_tmp_194 || !_tmp_192) && (_tmp_195 || !_tmp_193) && _tmp_199) begin
        _tmp_192 <= 1;
        _tmp_193 <= 1;
        _tmp_202 <= _tmp_201;
        _tmp_201 <= 0;
        _tmp_199 <= 0;
        _tmp_200 <= 1;
      end 
      if((_tmp_fsm_11 == 1) && (_tmp_203 == 0) && !_tmp_201 && !_tmp_202) begin
        ram_c_0_addr <= _tmp_186;
        _tmp_203 <= _tmp_188 - 1;
        _tmp_199 <= 1;
        _tmp_201 <= _tmp_188 == 1;
      end 
      if((_tmp_194 || !_tmp_192) && (_tmp_195 || !_tmp_193) && (_tmp_203 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_203 <= _tmp_203 - 1;
        _tmp_199 <= 1;
        _tmp_201 <= 0;
      end 
      if((_tmp_194 || !_tmp_192) && (_tmp_195 || !_tmp_193) && (_tmp_203 == 1)) begin
        _tmp_201 <= 1;
      end 
      if(th_comp == 102) begin
        ram_c_0_addr <= _th_comp_i_39 + _th_comp_offset_stream_36;
      end 
      _ram_c_cond_8_1 <= th_comp == 102;
      _ram_c_cond_9_1 <= th_comp == 102;
      if(th_comp == 104) begin
        ram_c_0_addr <= _th_comp_i_39 + _th_comp_offset_seq_37;
      end 
      _ram_c_cond_10_1 <= th_comp == 104;
      _ram_c_cond_11_1 <= th_comp == 104;
    end
  end

  assign __variable_data_48 = _tmp_40;
  assign __variable_valid_48 = _tmp_34;
  assign _tmp_36 = 1 && __variable_ready_48;
  assign __variable_data_100 = _tmp_92;
  assign __variable_valid_100 = _tmp_86;
  assign _tmp_88 = 1 && __variable_ready_100;
  assign __variable_data_154 = _tmp_146;
  assign __variable_valid_154 = _tmp_140;
  assign _tmp_142 = 1 && __variable_ready_154;
  assign __variable_data_206 = _tmp_198;
  assign __variable_valid_206 = _tmp_192;
  assign _tmp_194 = 1 && __variable_ready_206;

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
      if(_macstream_v_wenable_4) begin
        ram_d_0_addr <= _macstream_v_waddr_4;
        ram_d_0_wdata <= _macstream_v_wdata_4;
        ram_d_0_wenable <= 1;
      end 
      _ram_d_cond_0_1 <= _macstream_v_wenable_4;
      if(th_comp == 33) begin
        ram_d_0_addr <= _th_comp_i_14 + _th_comp_offset_11;
        ram_d_0_wdata <= _th_comp_count_13 == 3;
        ram_d_0_wenable <= 1;
      end 
      _ram_d_cond_1_1 <= th_comp == 33;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _times_mul_odata_reg_3 <= 0;
      __delay_data_19 <= 0;
      __delay_data_20 <= 0;
      __delay_data_21 <= 0;
      __delay_data_22 <= 0;
      __delay_data_23 <= 0;
      __delay_data_24 <= 0;
      __delay_data_25 <= 0;
      _reduceadd_data_6 <= 1'sd0;
      _reduceadd_count_6 <= 0;
      _pulse_data_8 <= 1'sd0;
      _pulse_count_8 <= 0;
      __variable_wdata_0 <= 0;
      __variable_wdata_1 <= 0;
      __parametervariable_wdata_2 <= 0;
      _macstream_a_fsm_sel <= 0;
      _macstream_a_idle <= 1;
      _macstream_b_fsm_sel <= 0;
      _macstream_b_idle <= 1;
      _macstream_c_fsm_sel <= 0;
      _macstream_v_fsm_sel <= 0;
    end else begin
      _times_mul_odata_reg_3 <= _times_mul_odata_3;
      __delay_data_19 <= _macstream_reduce_reset;
      __delay_data_20 <= __delay_data_19;
      __delay_data_21 <= __delay_data_20;
      __delay_data_22 <= __delay_data_21;
      __delay_data_23 <= __delay_data_22;
      __delay_data_24 <= __delay_data_23;
      __delay_data_25 <= __delay_data_24;
      _reduceadd_data_6 <= _reduceadd_data_6 + _times_data_3;
      _reduceadd_count_6 <= (_reduceadd_count_6 == macstream_const_data - 1)? 0 : _reduceadd_count_6 + 1;
      if(__delay_data_25) begin
        _reduceadd_data_6 <= 1'sd0 + _times_data_3;
      end 
      if(__delay_data_25) begin
        _reduceadd_count_6 <= 0;
      end 
      if(_reduceadd_count_6 == 0) begin
        _reduceadd_data_6 <= 1'sd0 + _times_data_3;
      end 
      _pulse_data_8 <= _pulse_count_8 == macstream_const_data - 1;
      _pulse_count_8 <= (_pulse_count_8 == macstream_const_data - 1)? 0 : _pulse_count_8 + 1;
      if(__delay_data_25) begin
        _pulse_data_8 <= _pulse_count_8 == macstream_const_data - 1;
      end 
      if(__delay_data_25) begin
        _pulse_count_8 <= 0;
      end 
      if(_pulse_count_8 == 0) begin
        _pulse_data_8 <= _pulse_count_8 == macstream_const_data - 1;
      end 
      if(_substream_macstream_a_data_cond_18_0) begin
        __variable_wdata_0 <= _plus_data_14;
      end 
      if(_substream_macstream_b_data_cond_18_1) begin
        __variable_wdata_1 <= __delay_data_35;
      end 
      if(_substream_macstream_const_data_cond_18_2) begin
        __parametervariable_wdata_2 <= neststream_const_data;
      end 
      if(th_comp == 7) begin
        _macstream_a_fsm_sel <= 1;
      end 
      if(_macstream_start) begin
        _macstream_a_idle <= 0;
      end 
      if(_tmp_26) begin
        __variable_wdata_0 <= ram_a_0_rdata;
      end 
      if((_macstream_a_fsm_1 == 1) && (_macstream_a_count_1 == 1)) begin
        _macstream_a_idle <= 1;
      end 
      if((_macstream_a_fsm_1 == 2) && (_macstream_a_count_1 == 1)) begin
        _macstream_a_idle <= 1;
      end 
      if(th_comp == 8) begin
        _macstream_b_fsm_sel <= 2;
      end 
      if(_macstream_start) begin
        _macstream_b_idle <= 0;
      end 
      if(_tmp_27) begin
        __variable_wdata_1 <= ram_b_0_rdata;
      end 
      if((_macstream_b_fsm_2 == 1) && (_macstream_b_count_2 == 1)) begin
        _macstream_b_idle <= 1;
      end 
      if((_macstream_b_fsm_2 == 2) && (_macstream_b_count_2 == 1)) begin
        _macstream_b_idle <= 1;
      end 
      if(th_comp == 9) begin
        __parametervariable_wdata_2 <= 4;
      end 
      if(th_comp == 10) begin
        _macstream_c_fsm_sel <= 3;
      end 
      if(th_comp == 11) begin
        _macstream_v_fsm_sel <= 4;
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
  localparam _macstream_fsm_15 = 15;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_fsm <= _macstream_fsm_init;
      _d1__macstream_fsm <= _macstream_fsm_init;
      _d2__macstream_fsm <= _macstream_fsm_init;
      _d3__macstream_fsm <= _macstream_fsm_init;
      _d4__macstream_fsm <= _macstream_fsm_init;
      _d5__macstream_fsm <= _macstream_fsm_init;
      _d6__macstream_fsm <= _macstream_fsm_init;
      _d7__macstream_fsm <= _macstream_fsm_init;
      _d8__macstream_fsm <= _macstream_fsm_init;
      _d9__macstream_fsm <= _macstream_fsm_init;
      _macstream_start <= 0;
      _macstream_busy <= 0;
      __macstream_fsm_cond_0_0_1 <= 0;
      __macstream_fsm_cond_0_1_1 <= 0;
      __macstream_fsm_cond_0_1_2 <= 0;
      __macstream_fsm_cond_0_1_3 <= 0;
      __macstream_fsm_cond_0_1_4 <= 0;
      __macstream_fsm_cond_0_1_5 <= 0;
      _macstream_reduce_reset <= 1;
      __macstream_fsm_cond_0_2_1 <= 0;
      __macstream_fsm_cond_0_2_2 <= 0;
      __macstream_fsm_cond_0_2_3 <= 0;
      __macstream_fsm_cond_0_2_4 <= 0;
      __macstream_fsm_cond_0_2_5 <= 0;
      __macstream_fsm_cond_0_2_6 <= 0;
      __macstream_fsm_cond_0_2_7 <= 0;
      __macstream_fsm_cond_0_2_8 <= 0;
      __macstream_fsm_cond_0_2_9 <= 0;
      _substream_macstream_a_data_cond_18_0 <= 0;
      _substream_macstream_b_data_cond_18_1 <= 0;
      _substream_macstream_const_data_cond_18_2 <= 0;
    end else begin
      _d1__macstream_fsm <= _macstream_fsm;
      _d2__macstream_fsm <= _d1__macstream_fsm;
      _d3__macstream_fsm <= _d2__macstream_fsm;
      _d4__macstream_fsm <= _d3__macstream_fsm;
      _d5__macstream_fsm <= _d4__macstream_fsm;
      _d6__macstream_fsm <= _d5__macstream_fsm;
      _d7__macstream_fsm <= _d6__macstream_fsm;
      _d8__macstream_fsm <= _d7__macstream_fsm;
      _d9__macstream_fsm <= _d8__macstream_fsm;
      case(_d9__macstream_fsm)
        _macstream_fsm_init: begin
          if(__macstream_fsm_cond_0_2_9) begin
            _macstream_reduce_reset <= 0;
          end 
        end
      endcase
      case(_d8__macstream_fsm)
        _macstream_fsm_init: begin
          __macstream_fsm_cond_0_2_9 <= __macstream_fsm_cond_0_2_8;
        end
      endcase
      case(_d7__macstream_fsm)
        _macstream_fsm_init: begin
          __macstream_fsm_cond_0_2_8 <= __macstream_fsm_cond_0_2_7;
        end
      endcase
      case(_d6__macstream_fsm)
        _macstream_fsm_init: begin
          __macstream_fsm_cond_0_2_7 <= __macstream_fsm_cond_0_2_6;
        end
      endcase
      case(_d5__macstream_fsm)
        _macstream_fsm_init: begin
          if(__macstream_fsm_cond_0_1_5) begin
            _macstream_reduce_reset <= 0;
          end 
          __macstream_fsm_cond_0_2_6 <= __macstream_fsm_cond_0_2_5;
        end
      endcase
      case(_d4__macstream_fsm)
        _macstream_fsm_init: begin
          __macstream_fsm_cond_0_1_5 <= __macstream_fsm_cond_0_1_4;
          __macstream_fsm_cond_0_2_5 <= __macstream_fsm_cond_0_2_4;
        end
      endcase
      case(_d3__macstream_fsm)
        _macstream_fsm_init: begin
          __macstream_fsm_cond_0_1_4 <= __macstream_fsm_cond_0_1_3;
          __macstream_fsm_cond_0_2_4 <= __macstream_fsm_cond_0_2_3;
        end
      endcase
      case(_d2__macstream_fsm)
        _macstream_fsm_init: begin
          __macstream_fsm_cond_0_1_3 <= __macstream_fsm_cond_0_1_2;
          __macstream_fsm_cond_0_2_3 <= __macstream_fsm_cond_0_2_2;
        end
      endcase
      case(_d1__macstream_fsm)
        _macstream_fsm_init: begin
          if(__macstream_fsm_cond_0_0_1) begin
            _macstream_start <= 0;
          end 
          __macstream_fsm_cond_0_1_2 <= __macstream_fsm_cond_0_1_1;
          __macstream_fsm_cond_0_2_2 <= __macstream_fsm_cond_0_2_1;
        end
      endcase
      case(_macstream_fsm)
        _macstream_fsm_init: begin
          if(th_comp == 12) begin
            _macstream_start <= 1;
            _macstream_busy <= 1;
          end 
          __macstream_fsm_cond_0_0_1 <= th_comp == 12;
          __macstream_fsm_cond_0_1_1 <= th_comp == 12;
          __macstream_fsm_cond_0_2_1 <= th_comp == 67;
          if(th_comp == 67) begin
            _substream_macstream_a_data_cond_18_0 <= 1;
          end 
          if(th_comp == 67) begin
            _substream_macstream_b_data_cond_18_1 <= 1;
          end 
          if(th_comp == 67) begin
            _substream_macstream_const_data_cond_18_2 <= 1;
          end 
          if(_mystream_fsm == 21) begin
            _macstream_reduce_reset <= 1;
          end 
          if(_mystream_fsm == 21) begin
            _substream_macstream_a_data_cond_18_0 <= 0;
          end 
          if(_mystream_fsm == 21) begin
            _substream_macstream_b_data_cond_18_1 <= 0;
          end 
          if(_mystream_fsm == 21) begin
            _substream_macstream_const_data_cond_18_2 <= 0;
          end 
          if(th_comp == 12) begin
            _macstream_fsm <= _macstream_fsm_1;
          end 
        end
        _macstream_fsm_1: begin
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
          _macstream_reduce_reset <= 1;
          _macstream_fsm <= _macstream_fsm_13;
        end
        _macstream_fsm_13: begin
          _macstream_fsm <= _macstream_fsm_14;
        end
        _macstream_fsm_14: begin
          _macstream_fsm <= _macstream_fsm_15;
        end
        _macstream_fsm_15: begin
          _macstream_busy <= 0;
          _macstream_fsm <= _macstream_fsm_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_12 <= 0;
      _plus_data_16 <= 0;
      _plus_data_14 <= 0;
      __delay_data_35 <= 0;
      __delay_data_36 <= 0;
      __delay_data_37 <= 0;
      __delay_data_38 <= 0;
      __delay_data_39 <= 0;
      __delay_data_40 <= 0;
      __delay_data_41 <= 0;
      __delay_data_42 <= 0;
      __delay_data_43 <= 0;
      __delay_data_44 <= 0;
      __substreamoutput_data_26 <= 0;
      __substreamoutput_data_30 <= 0;
      __delay_data_45 <= 0;
      _plus_data_27 <= 0;
      __delay_data_46 <= 0;
      _plus_data_28 <= 0;
      __delay_data_47 <= 0;
      __variable_wdata_9 <= 0;
      __variable_wdata_10 <= 0;
      __parametervariable_wdata_11 <= 0;
    end else begin
      _plus_data_12 <= neststream_a_data + 2'sd1;
      _plus_data_16 <= neststream_b_data + 2'sd1;
      _plus_data_14 <= _plus_data_12 + 1'sd0;
      __delay_data_35 <= _plus_data_16;
      __delay_data_36 <= _plus_data_14;
      __delay_data_37 <= __delay_data_36;
      __delay_data_38 <= __delay_data_37;
      __delay_data_39 <= __delay_data_38;
      __delay_data_40 <= __delay_data_39;
      __delay_data_41 <= __delay_data_40;
      __delay_data_42 <= __delay_data_41;
      __delay_data_43 <= __delay_data_42;
      __delay_data_44 <= __delay_data_43;
      __substreamoutput_data_26 <= macstream_c_data;
      __substreamoutput_data_30 <= macstream_v_data;
      __delay_data_45 <= __delay_data_44;
      _plus_data_27 <= __substreamoutput_data_26 + __delay_data_45;
      __delay_data_46 <= __substreamoutput_data_30;
      _plus_data_28 <= _plus_data_27 + 1'sd0;
      __delay_data_47 <= __delay_data_46;
      if(_substream_neststream_a_data_cond_34_3) begin
        __variable_wdata_9 <= mystream_x_data;
      end 
      if(_substream_neststream_b_data_cond_34_4) begin
        __variable_wdata_10 <= mystream_y_data;
      end 
      if(_substream_neststream_const_data_cond_34_5) begin
        __parametervariable_wdata_11 <= mystream_const_data;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _neststream_fsm <= _neststream_fsm_init;
      _substream_neststream_a_data_cond_34_3 <= 0;
      _substream_neststream_b_data_cond_34_4 <= 0;
      _substream_neststream_const_data_cond_34_5 <= 0;
    end else begin
      case(_neststream_fsm)
        _neststream_fsm_init: begin
          if(th_comp == 67) begin
            _substream_neststream_a_data_cond_34_3 <= 1;
          end 
          if(th_comp == 67) begin
            _substream_neststream_b_data_cond_34_4 <= 1;
          end 
          if(th_comp == 67) begin
            _substream_neststream_const_data_cond_34_5 <= 1;
          end 
          if(_mystream_fsm == 21) begin
            _substream_neststream_a_data_cond_34_3 <= 0;
          end 
          if(_mystream_fsm == 21) begin
            _substream_neststream_b_data_cond_34_4 <= 0;
          end 
          if(_mystream_fsm == 21) begin
            _substream_neststream_const_data_cond_34_5 <= 0;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __delay_data_51 <= 0;
      __delay_data_52 <= 0;
      __delay_data_53 <= 0;
      __delay_data_54 <= 0;
      __delay_data_55 <= 0;
      __delay_data_56 <= 0;
      __delay_data_57 <= 0;
      __delay_data_58 <= 0;
      __delay_data_59 <= 0;
      __delay_data_60 <= 0;
      __delay_data_61 <= 0;
      __delay_data_62 <= 0;
      __delay_data_63 <= 0;
      __delay_data_64 <= 0;
      __delay_data_65 <= 0;
      __substreamoutput_data_48 <= 0;
      __substreamoutput_data_49 <= 0;
      __delay_data_66 <= 0;
      _plus_data_50 <= 0;
      __delay_data_67 <= 0;
      _mystream_x_fsm_sel <= 0;
      _mystream_x_idle <= 1;
      __variable_wdata_31 <= 0;
      _mystream_y_fsm_sel <= 0;
      _mystream_y_idle <= 1;
      __variable_wdata_32 <= 0;
      __parametervariable_wdata_33 <= 0;
      _mystream_z_fsm_sel <= 0;
    end else begin
      __delay_data_51 <= mystream_y_data;
      __delay_data_52 <= __delay_data_51;
      __delay_data_53 <= __delay_data_52;
      __delay_data_54 <= __delay_data_53;
      __delay_data_55 <= __delay_data_54;
      __delay_data_56 <= __delay_data_55;
      __delay_data_57 <= __delay_data_56;
      __delay_data_58 <= __delay_data_57;
      __delay_data_59 <= __delay_data_58;
      __delay_data_60 <= __delay_data_59;
      __delay_data_61 <= __delay_data_60;
      __delay_data_62 <= __delay_data_61;
      __delay_data_63 <= __delay_data_62;
      __delay_data_64 <= __delay_data_63;
      __delay_data_65 <= __delay_data_64;
      __substreamoutput_data_48 <= neststream_c_data;
      __substreamoutput_data_49 <= neststream_v_data;
      __delay_data_66 <= __delay_data_65;
      _plus_data_50 <= __substreamoutput_data_48 + __delay_data_66;
      __delay_data_67 <= __substreamoutput_data_49;
      if(th_comp == 63) begin
        _mystream_x_fsm_sel <= 1;
      end 
      if(_mystream_start) begin
        _mystream_x_idle <= 0;
      end 
      if(_tmp_132) begin
        __variable_wdata_31 <= ram_a_0_rdata;
      end 
      if((_mystream_x_fsm_1 == 1) && (_mystream_x_count_1 == 1)) begin
        _mystream_x_idle <= 1;
      end 
      if((_mystream_x_fsm_1 == 2) && (_mystream_x_count_1 == 1)) begin
        _mystream_x_idle <= 1;
      end 
      if(th_comp == 64) begin
        _mystream_y_fsm_sel <= 2;
      end 
      if(_mystream_start) begin
        _mystream_y_idle <= 0;
      end 
      if(_tmp_133) begin
        __variable_wdata_32 <= ram_b_0_rdata;
      end 
      if((_mystream_y_fsm_2 == 1) && (_mystream_y_count_2 == 1)) begin
        _mystream_y_idle <= 1;
      end 
      if((_mystream_y_fsm_2 == 2) && (_mystream_y_count_2 == 1)) begin
        _mystream_y_idle <= 1;
      end 
      if(th_comp == 65) begin
        __parametervariable_wdata_33 <= 4;
      end 
      if(th_comp == 66) begin
        _mystream_z_fsm_sel <= 3;
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
  localparam _mystream_fsm_13 = 13;
  localparam _mystream_fsm_14 = 14;
  localparam _mystream_fsm_15 = 15;
  localparam _mystream_fsm_16 = 16;
  localparam _mystream_fsm_17 = 17;
  localparam _mystream_fsm_18 = 18;
  localparam _mystream_fsm_19 = 19;
  localparam _mystream_fsm_20 = 20;
  localparam _mystream_fsm_21 = 21;
  localparam _mystream_fsm_22 = 22;
  localparam _mystream_fsm_23 = 23;
  localparam _mystream_fsm_24 = 24;

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
          if(th_comp == 67) begin
            _mystream_start <= 1;
            _mystream_busy <= 1;
          end 
          __mystream_fsm_cond_0_0_1 <= th_comp == 67;
          if(th_comp == 67) begin
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
          _mystream_fsm <= _mystream_fsm_18;
        end
        _mystream_fsm_18: begin
          _mystream_fsm <= _mystream_fsm_19;
        end
        _mystream_fsm_19: begin
          _mystream_fsm <= _mystream_fsm_20;
        end
        _mystream_fsm_20: begin
          _mystream_fsm <= _mystream_fsm_21;
        end
        _mystream_fsm_21: begin
          _mystream_fsm <= _mystream_fsm_22;
        end
        _mystream_fsm_22: begin
          _mystream_fsm <= _mystream_fsm_23;
        end
        _mystream_fsm_23: begin
          _mystream_fsm <= _mystream_fsm_24;
        end
        _mystream_fsm_24: begin
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

  always @(posedge CLK) begin
    if(RST) begin
      th_comp <= th_comp_init;
      _th_comp_size_6 <= 0;
      _th_comp_offset_7 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _th_comp_size_8 <= 0;
      _th_comp_offset_9 <= 0;
      _tmp_28 <= 0;
      _tmp_29 <= 0;
      _tmp_30 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _tmp_52 <= 0;
      _tmp_63 <= 0;
      _tmp_64 <= 0;
      _tmp_65 <= 0;
      _th_comp_size_10 <= 0;
      _th_comp_offset_11 <= 0;
      _th_comp_sum_12 <= 0;
      _th_comp_count_13 <= 0;
      _th_comp_i_14 <= 0;
      _tmp_77 <= 0;
      _th_comp_a_15 <= 0;
      _tmp_79 <= 0;
      _th_comp_b_16 <= 0;
      _tmp_80 <= 0;
      _tmp_81 <= 0;
      _tmp_82 <= 0;
      _th_comp_size_17 <= 0;
      _th_comp_offset_stream_18 <= 0;
      _th_comp_offset_seq_19 <= 0;
      _th_comp_all_ok_20 <= 0;
      _th_comp_i_21 <= 0;
      _tmp_103 <= 0;
      _th_comp_st_22 <= 0;
      _tmp_105 <= 0;
      _th_comp_sq_23 <= 0;
      _tmp_106 <= 0;
      _tmp_107 <= 0;
      _tmp_108 <= 0;
      _tmp_119 <= 0;
      _tmp_120 <= 0;
      _tmp_121 <= 0;
      _th_comp_size_24 <= 0;
      _th_comp_offset_25 <= 0;
      _tmp_134 <= 0;
      _tmp_135 <= 0;
      _tmp_136 <= 0;
      _tmp_156 <= 0;
      _tmp_157 <= 0;
      _tmp_158 <= 0;
      _tmp_169 <= 0;
      _tmp_170 <= 0;
      _tmp_171 <= 0;
      _th_comp_size_26 <= 0;
      _th_comp_offset_27 <= 0;
      _th_comp_sum_28 <= 0;
      _th_comp_count_29 <= 0;
      _th_comp_write_offset_30 <= 0;
      _th_comp_i_31 <= 0;
      _tmp_183 <= 0;
      _th_comp_x_32 <= 0;
      _tmp_185 <= 0;
      _th_comp_y_33 <= 0;
      _th_comp_val_34 <= 0;
      _tmp_186 <= 0;
      _tmp_187 <= 0;
      _tmp_188 <= 0;
      _th_comp_size_35 <= 0;
      _th_comp_offset_stream_36 <= 0;
      _th_comp_offset_seq_37 <= 0;
      _th_comp_all_ok_38 <= 0;
      _th_comp_i_39 <= 0;
      _tmp_209 <= 0;
      _th_comp_st_40 <= 0;
      _tmp_211 <= 0;
      _th_comp_sq_41 <= 0;
    end else begin
      case(th_comp)
        th_comp_init: begin
          _th_comp_size_6 <= 16;
          th_comp <= th_comp_1;
        end
        th_comp_1: begin
          _th_comp_offset_7 <= 0;
          th_comp <= th_comp_2;
        end
        th_comp_2: begin
          _tmp_0 <= _th_comp_offset_7;
          _tmp_1 <= 0;
          _tmp_2 <= _th_comp_size_6;
          th_comp <= th_comp_3;
        end
        th_comp_3: begin
          if(_tmp_12) begin
            th_comp <= th_comp_4;
          end 
        end
        th_comp_4: begin
          _tmp_13 <= _th_comp_offset_7;
          _tmp_14 <= 0;
          _tmp_15 <= _th_comp_size_6;
          th_comp <= th_comp_5;
        end
        th_comp_5: begin
          if(_tmp_25) begin
            th_comp <= th_comp_6;
          end 
        end
        th_comp_6: begin
          _th_comp_size_8 <= _th_comp_size_6;
          _th_comp_offset_9 <= _th_comp_offset_7;
          th_comp <= th_comp_7;
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
          th_comp <= th_comp_11;
        end
        th_comp_11: begin
          th_comp <= th_comp_12;
        end
        th_comp_12: begin
          th_comp <= th_comp_13;
        end
        th_comp_13: begin
          if(!_macstream_busy) begin
            th_comp <= th_comp_14;
          end 
        end
        th_comp_14: begin
          _tmp_28 <= _th_comp_offset_7;
          _tmp_29 <= 1024;
          _tmp_30 <= _th_comp_size_6;
          th_comp <= th_comp_15;
        end
        th_comp_15: begin
          if(_tmp_49) begin
            th_comp <= th_comp_16;
          end 
        end
        th_comp_16: begin
          _th_comp_offset_7 <= _th_comp_size_6;
          th_comp <= th_comp_17;
        end
        th_comp_17: begin
          _tmp_50 <= _th_comp_offset_7;
          _tmp_51 <= 0;
          _tmp_52 <= _th_comp_size_6;
          th_comp <= th_comp_18;
        end
        th_comp_18: begin
          if(_tmp_62) begin
            th_comp <= th_comp_19;
          end 
        end
        th_comp_19: begin
          _tmp_63 <= _th_comp_offset_7;
          _tmp_64 <= 0;
          _tmp_65 <= _th_comp_size_6;
          th_comp <= th_comp_20;
        end
        th_comp_20: begin
          if(_tmp_75) begin
            th_comp <= th_comp_21;
          end 
        end
        th_comp_21: begin
          _th_comp_size_10 <= _th_comp_size_6;
          _th_comp_offset_11 <= _th_comp_offset_7;
          th_comp <= th_comp_22;
        end
        th_comp_22: begin
          _th_comp_sum_12 <= 0;
          th_comp <= th_comp_23;
        end
        th_comp_23: begin
          _th_comp_count_13 <= 0;
          th_comp <= th_comp_24;
        end
        th_comp_24: begin
          _th_comp_i_14 <= 0;
          th_comp <= th_comp_25;
        end
        th_comp_25: begin
          if(_th_comp_i_14 < _th_comp_size_10) begin
            th_comp <= th_comp_26;
          end else begin
            th_comp <= th_comp_38;
          end
        end
        th_comp_26: begin
          if(_tmp_76) begin
            _tmp_77 <= ram_a_0_rdata;
          end 
          if(_tmp_76) begin
            th_comp <= th_comp_27;
          end 
        end
        th_comp_27: begin
          _th_comp_a_15 <= _tmp_77;
          th_comp <= th_comp_28;
        end
        th_comp_28: begin
          if(_tmp_78) begin
            _tmp_79 <= ram_b_0_rdata;
          end 
          if(_tmp_78) begin
            th_comp <= th_comp_29;
          end 
        end
        th_comp_29: begin
          _th_comp_b_16 <= _tmp_79;
          th_comp <= th_comp_30;
        end
        th_comp_30: begin
          _th_comp_sum_12 <= _th_comp_sum_12 + _th_comp_a_15 * _th_comp_b_16;
          th_comp <= th_comp_31;
        end
        th_comp_31: begin
          _th_comp_count_13 <= _th_comp_count_13 + 1;
          th_comp <= th_comp_32;
        end
        th_comp_32: begin
          th_comp <= th_comp_33;
        end
        th_comp_33: begin
          th_comp <= th_comp_34;
        end
        th_comp_34: begin
          if(_th_comp_count_13 == 4) begin
            th_comp <= th_comp_35;
          end else begin
            th_comp <= th_comp_37;
          end
        end
        th_comp_35: begin
          _th_comp_sum_12 <= 0;
          th_comp <= th_comp_36;
        end
        th_comp_36: begin
          _th_comp_count_13 <= 0;
          th_comp <= th_comp_37;
        end
        th_comp_37: begin
          _th_comp_i_14 <= _th_comp_i_14 + 1;
          th_comp <= th_comp_25;
        end
        th_comp_38: begin
          _tmp_80 <= _th_comp_offset_7;
          _tmp_81 <= 2048;
          _tmp_82 <= _th_comp_size_6;
          th_comp <= th_comp_39;
        end
        th_comp_39: begin
          if(_tmp_101) begin
            th_comp <= th_comp_40;
          end 
        end
        th_comp_40: begin
          $display("# macstream");
          th_comp <= th_comp_41;
        end
        th_comp_41: begin
          _th_comp_size_17 <= _th_comp_size_6;
          _th_comp_offset_stream_18 <= 0;
          _th_comp_offset_seq_19 <= _th_comp_offset_7;
          th_comp <= th_comp_42;
        end
        th_comp_42: begin
          _th_comp_all_ok_20 <= 1;
          th_comp <= th_comp_43;
        end
        th_comp_43: begin
          _th_comp_i_21 <= 0;
          th_comp <= th_comp_44;
        end
        th_comp_44: begin
          if(_th_comp_i_21 < _th_comp_size_17) begin
            th_comp <= th_comp_45;
          end else begin
            th_comp <= th_comp_53;
          end
        end
        th_comp_45: begin
          if(_tmp_102) begin
            _tmp_103 <= ram_c_0_rdata;
          end 
          if(_tmp_102) begin
            th_comp <= th_comp_46;
          end 
        end
        th_comp_46: begin
          _th_comp_st_22 <= _tmp_103;
          th_comp <= th_comp_47;
        end
        th_comp_47: begin
          if(_tmp_104) begin
            _tmp_105 <= ram_c_0_rdata;
          end 
          if(_tmp_104) begin
            th_comp <= th_comp_48;
          end 
        end
        th_comp_48: begin
          _th_comp_sq_23 <= _tmp_105;
          th_comp <= th_comp_49;
        end
        th_comp_49: begin
          if(_th_comp_st_22 !== _th_comp_sq_23) begin
            th_comp <= th_comp_50;
          end else begin
            th_comp <= th_comp_52;
          end
        end
        th_comp_50: begin
          _th_comp_all_ok_20 <= 0;
          th_comp <= th_comp_51;
        end
        th_comp_51: begin
          $display("%d %d %d", _th_comp_i_21, _th_comp_st_22, _th_comp_sq_23);
          th_comp <= th_comp_52;
        end
        th_comp_52: begin
          _th_comp_i_21 <= _th_comp_i_21 + 1;
          th_comp <= th_comp_44;
        end
        th_comp_53: begin
          if(_th_comp_all_ok_20) begin
            th_comp <= th_comp_54;
          end else begin
            th_comp <= th_comp_56;
          end
        end
        th_comp_54: begin
          $display("OK");
          th_comp <= th_comp_55;
        end
        th_comp_55: begin
          th_comp <= th_comp_57;
        end
        th_comp_56: begin
          $display("NG");
          th_comp <= th_comp_57;
        end
        th_comp_57: begin
          _th_comp_offset_7 <= 0;
          th_comp <= th_comp_58;
        end
        th_comp_58: begin
          _tmp_106 <= _th_comp_offset_7;
          _tmp_107 <= 0;
          _tmp_108 <= _th_comp_size_6;
          th_comp <= th_comp_59;
        end
        th_comp_59: begin
          if(_tmp_118) begin
            th_comp <= th_comp_60;
          end 
        end
        th_comp_60: begin
          _tmp_119 <= _th_comp_offset_7;
          _tmp_120 <= 0;
          _tmp_121 <= _th_comp_size_6;
          th_comp <= th_comp_61;
        end
        th_comp_61: begin
          if(_tmp_131) begin
            th_comp <= th_comp_62;
          end 
        end
        th_comp_62: begin
          _th_comp_size_24 <= _th_comp_size_6;
          _th_comp_offset_25 <= _th_comp_offset_7;
          th_comp <= th_comp_63;
        end
        th_comp_63: begin
          th_comp <= th_comp_64;
        end
        th_comp_64: begin
          th_comp <= th_comp_65;
        end
        th_comp_65: begin
          th_comp <= th_comp_66;
        end
        th_comp_66: begin
          th_comp <= th_comp_67;
        end
        th_comp_67: begin
          th_comp <= th_comp_68;
        end
        th_comp_68: begin
          if(!_mystream_busy) begin
            th_comp <= th_comp_69;
          end 
        end
        th_comp_69: begin
          _tmp_134 <= _th_comp_offset_7;
          _tmp_135 <= 1024;
          _tmp_136 <= _th_comp_size_6 >>> 2;
          th_comp <= th_comp_70;
        end
        th_comp_70: begin
          if(_tmp_155) begin
            th_comp <= th_comp_71;
          end 
        end
        th_comp_71: begin
          _th_comp_offset_7 <= _th_comp_size_6;
          th_comp <= th_comp_72;
        end
        th_comp_72: begin
          _tmp_156 <= _th_comp_offset_7;
          _tmp_157 <= 0;
          _tmp_158 <= _th_comp_size_6;
          th_comp <= th_comp_73;
        end
        th_comp_73: begin
          if(_tmp_168) begin
            th_comp <= th_comp_74;
          end 
        end
        th_comp_74: begin
          _tmp_169 <= _th_comp_offset_7;
          _tmp_170 <= 0;
          _tmp_171 <= _th_comp_size_6;
          th_comp <= th_comp_75;
        end
        th_comp_75: begin
          if(_tmp_181) begin
            th_comp <= th_comp_76;
          end 
        end
        th_comp_76: begin
          _th_comp_size_26 <= _th_comp_size_6;
          _th_comp_offset_27 <= _th_comp_offset_7;
          th_comp <= th_comp_77;
        end
        th_comp_77: begin
          _th_comp_sum_28 <= 0;
          th_comp <= th_comp_78;
        end
        th_comp_78: begin
          _th_comp_count_29 <= 0;
          th_comp <= th_comp_79;
        end
        th_comp_79: begin
          _th_comp_write_offset_30 <= _th_comp_offset_27;
          th_comp <= th_comp_80;
        end
        th_comp_80: begin
          _th_comp_i_31 <= 0;
          th_comp <= th_comp_81;
        end
        th_comp_81: begin
          if(_th_comp_i_31 < _th_comp_size_26) begin
            th_comp <= th_comp_82;
          end else begin
            th_comp <= th_comp_95;
          end
        end
        th_comp_82: begin
          if(_tmp_182) begin
            _tmp_183 <= ram_a_0_rdata;
          end 
          if(_tmp_182) begin
            th_comp <= th_comp_83;
          end 
        end
        th_comp_83: begin
          _th_comp_x_32 <= _tmp_183;
          th_comp <= th_comp_84;
        end
        th_comp_84: begin
          if(_tmp_184) begin
            _tmp_185 <= ram_b_0_rdata;
          end 
          if(_tmp_184) begin
            th_comp <= th_comp_85;
          end 
        end
        th_comp_85: begin
          _th_comp_y_33 <= _tmp_185;
          th_comp <= th_comp_86;
        end
        th_comp_86: begin
          _th_comp_sum_28 <= _th_comp_sum_28 + (_th_comp_x_32 + 1) * (_th_comp_y_33 + 1);
          th_comp <= th_comp_87;
        end
        th_comp_87: begin
          _th_comp_val_34 <= _th_comp_sum_28 + (_th_comp_x_32 + 1) + _th_comp_y_33;
          th_comp <= th_comp_88;
        end
        th_comp_88: begin
          _th_comp_count_29 <= _th_comp_count_29 + 1;
          th_comp <= th_comp_89;
        end
        th_comp_89: begin
          if(_th_comp_count_29 == 4) begin
            th_comp <= th_comp_90;
          end else begin
            th_comp <= th_comp_94;
          end
        end
        th_comp_90: begin
          th_comp <= th_comp_91;
        end
        th_comp_91: begin
          _th_comp_write_offset_30 <= _th_comp_write_offset_30 + 1;
          th_comp <= th_comp_92;
        end
        th_comp_92: begin
          _th_comp_sum_28 <= 0;
          th_comp <= th_comp_93;
        end
        th_comp_93: begin
          _th_comp_count_29 <= 0;
          th_comp <= th_comp_94;
        end
        th_comp_94: begin
          _th_comp_i_31 <= _th_comp_i_31 + 1;
          th_comp <= th_comp_81;
        end
        th_comp_95: begin
          _tmp_186 <= _th_comp_offset_7;
          _tmp_187 <= 2048;
          _tmp_188 <= _th_comp_size_6 >>> 2;
          th_comp <= th_comp_96;
        end
        th_comp_96: begin
          if(_tmp_207) begin
            th_comp <= th_comp_97;
          end 
        end
        th_comp_97: begin
          $display("# mystream");
          th_comp <= th_comp_98;
        end
        th_comp_98: begin
          _th_comp_size_35 <= _th_comp_size_6 >>> 2;
          _th_comp_offset_stream_36 <= 0;
          _th_comp_offset_seq_37 <= _th_comp_offset_7;
          th_comp <= th_comp_99;
        end
        th_comp_99: begin
          _th_comp_all_ok_38 <= 1;
          th_comp <= th_comp_100;
        end
        th_comp_100: begin
          _th_comp_i_39 <= 0;
          th_comp <= th_comp_101;
        end
        th_comp_101: begin
          if(_th_comp_i_39 < _th_comp_size_35) begin
            th_comp <= th_comp_102;
          end else begin
            th_comp <= th_comp_110;
          end
        end
        th_comp_102: begin
          if(_tmp_208) begin
            _tmp_209 <= ram_c_0_rdata;
          end 
          if(_tmp_208) begin
            th_comp <= th_comp_103;
          end 
        end
        th_comp_103: begin
          _th_comp_st_40 <= _tmp_209;
          th_comp <= th_comp_104;
        end
        th_comp_104: begin
          if(_tmp_210) begin
            _tmp_211 <= ram_c_0_rdata;
          end 
          if(_tmp_210) begin
            th_comp <= th_comp_105;
          end 
        end
        th_comp_105: begin
          _th_comp_sq_41 <= _tmp_211;
          th_comp <= th_comp_106;
        end
        th_comp_106: begin
          if(_th_comp_st_40 !== _th_comp_sq_41) begin
            th_comp <= th_comp_107;
          end else begin
            th_comp <= th_comp_109;
          end
        end
        th_comp_107: begin
          _th_comp_all_ok_38 <= 0;
          th_comp <= th_comp_108;
        end
        th_comp_108: begin
          $display("%d %d %d", _th_comp_i_39, _th_comp_st_40, _th_comp_sq_41);
          th_comp <= th_comp_109;
        end
        th_comp_109: begin
          _th_comp_i_39 <= _th_comp_i_39 + 1;
          th_comp <= th_comp_101;
        end
        th_comp_110: begin
          if(_th_comp_all_ok_38) begin
            th_comp <= th_comp_111;
          end else begin
            th_comp <= th_comp_113;
          end
        end
        th_comp_111: begin
          $display("OK");
          th_comp <= th_comp_112;
        end
        th_comp_112: begin
          th_comp <= th_comp_114;
        end
        th_comp_113: begin
          $display("NG");
          th_comp <= th_comp_114;
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

  localparam _macstream_a_fsm_1_1 = 1;
  localparam _macstream_a_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_a_fsm_1 <= _macstream_a_fsm_1_init;
      _d1__macstream_a_fsm_1 <= _macstream_a_fsm_1_init;
      _macstream_a_offset_1 <= 0;
      _macstream_a_size_1 <= 0;
      _macstream_a_stride_1 <= 0;
      _macstream_a_count_1 <= 0;
      _macstream_a_raddr_1 <= 0;
      _macstream_a_renable_1 <= 0;
      __macstream_a_fsm_1_cond_1_0_1 <= 0;
      __macstream_a_fsm_1_cond_2_1_1 <= 0;
    end else begin
      _d1__macstream_a_fsm_1 <= _macstream_a_fsm_1;
      case(_d1__macstream_a_fsm_1)
        _macstream_a_fsm_1_1: begin
          if(__macstream_a_fsm_1_cond_1_0_1) begin
            _macstream_a_renable_1 <= 0;
          end 
        end
        _macstream_a_fsm_1_2: begin
          if(__macstream_a_fsm_1_cond_2_1_1) begin
            _macstream_a_renable_1 <= 0;
          end 
        end
      endcase
      case(_macstream_a_fsm_1)
        _macstream_a_fsm_1_init: begin
          if(th_comp == 7) begin
            _macstream_a_offset_1 <= _th_comp_offset_9;
            _macstream_a_size_1 <= _th_comp_size_8;
            _macstream_a_stride_1 <= 1;
          end 
          if(_macstream_start && (_macstream_a_fsm_sel == 1) && (_macstream_a_size_1 > 0)) begin
            _macstream_a_count_1 <= _macstream_a_size_1;
          end 
          if(_macstream_start && (_macstream_a_fsm_sel == 1) && (_macstream_a_size_1 > 0)) begin
            _macstream_a_fsm_1 <= _macstream_a_fsm_1_1;
          end 
        end
        _macstream_a_fsm_1_1: begin
          _macstream_a_raddr_1 <= _macstream_a_offset_1;
          _macstream_a_renable_1 <= 1;
          _macstream_a_count_1 <= _macstream_a_count_1 - 1;
          __macstream_a_fsm_1_cond_1_0_1 <= 1;
          if(_macstream_a_count_1 == 1) begin
            _macstream_a_fsm_1 <= _macstream_a_fsm_1_init;
          end 
          if(_macstream_a_count_1 > 1) begin
            _macstream_a_fsm_1 <= _macstream_a_fsm_1_2;
          end 
        end
        _macstream_a_fsm_1_2: begin
          _macstream_a_raddr_1 <= _macstream_a_raddr_1 + _macstream_a_stride_1;
          _macstream_a_renable_1 <= 1;
          _macstream_a_count_1 <= _macstream_a_count_1 - 1;
          __macstream_a_fsm_1_cond_2_1_1 <= 1;
          if(_macstream_a_count_1 == 1) begin
            _macstream_a_fsm_1 <= _macstream_a_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _macstream_b_fsm_2_1 = 1;
  localparam _macstream_b_fsm_2_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_b_fsm_2 <= _macstream_b_fsm_2_init;
      _d1__macstream_b_fsm_2 <= _macstream_b_fsm_2_init;
      _macstream_b_offset_2 <= 0;
      _macstream_b_size_2 <= 0;
      _macstream_b_stride_2 <= 0;
      _macstream_b_count_2 <= 0;
      _macstream_b_raddr_2 <= 0;
      _macstream_b_renable_2 <= 0;
      __macstream_b_fsm_2_cond_1_0_1 <= 0;
      __macstream_b_fsm_2_cond_2_1_1 <= 0;
    end else begin
      _d1__macstream_b_fsm_2 <= _macstream_b_fsm_2;
      case(_d1__macstream_b_fsm_2)
        _macstream_b_fsm_2_1: begin
          if(__macstream_b_fsm_2_cond_1_0_1) begin
            _macstream_b_renable_2 <= 0;
          end 
        end
        _macstream_b_fsm_2_2: begin
          if(__macstream_b_fsm_2_cond_2_1_1) begin
            _macstream_b_renable_2 <= 0;
          end 
        end
      endcase
      case(_macstream_b_fsm_2)
        _macstream_b_fsm_2_init: begin
          if(th_comp == 8) begin
            _macstream_b_offset_2 <= _th_comp_offset_9;
            _macstream_b_size_2 <= _th_comp_size_8;
            _macstream_b_stride_2 <= 1;
          end 
          if(_macstream_start && (_macstream_b_fsm_sel == 2) && (_macstream_b_size_2 > 0)) begin
            _macstream_b_count_2 <= _macstream_b_size_2;
          end 
          if(_macstream_start && (_macstream_b_fsm_sel == 2) && (_macstream_b_size_2 > 0)) begin
            _macstream_b_fsm_2 <= _macstream_b_fsm_2_1;
          end 
        end
        _macstream_b_fsm_2_1: begin
          _macstream_b_raddr_2 <= _macstream_b_offset_2;
          _macstream_b_renable_2 <= 1;
          _macstream_b_count_2 <= _macstream_b_count_2 - 1;
          __macstream_b_fsm_2_cond_1_0_1 <= 1;
          if(_macstream_b_count_2 == 1) begin
            _macstream_b_fsm_2 <= _macstream_b_fsm_2_init;
          end 
          if(_macstream_b_count_2 > 1) begin
            _macstream_b_fsm_2 <= _macstream_b_fsm_2_2;
          end 
        end
        _macstream_b_fsm_2_2: begin
          _macstream_b_raddr_2 <= _macstream_b_raddr_2 + _macstream_b_stride_2;
          _macstream_b_renable_2 <= 1;
          _macstream_b_count_2 <= _macstream_b_count_2 - 1;
          __macstream_b_fsm_2_cond_2_1_1 <= 1;
          if(_macstream_b_count_2 == 1) begin
            _macstream_b_fsm_2 <= _macstream_b_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _macstream_c_fsm_3_1 = 1;
  localparam _macstream_c_fsm_3_2 = 2;
  localparam _macstream_c_fsm_3_3 = 3;
  localparam _macstream_c_fsm_3_4 = 4;
  localparam _macstream_c_fsm_3_5 = 5;
  localparam _macstream_c_fsm_3_6 = 6;
  localparam _macstream_c_fsm_3_7 = 7;
  localparam _macstream_c_fsm_3_8 = 8;
  localparam _macstream_c_fsm_3_9 = 9;
  localparam _macstream_c_fsm_3_10 = 10;
  localparam _macstream_c_fsm_3_11 = 11;
  localparam _macstream_c_fsm_3_12 = 12;
  localparam _macstream_c_fsm_3_13 = 13;
  localparam _macstream_c_fsm_3_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_c_fsm_3 <= _macstream_c_fsm_3_init;
      _d1__macstream_c_fsm_3 <= _macstream_c_fsm_3_init;
      _macstream_c_offset_3 <= 0;
      _macstream_c_size_3 <= 0;
      _macstream_c_stride_3 <= 0;
      _macstream_c_count_3 <= 0;
      _macstream_c_waddr_3 <= 0;
      _macstream_c_wdata_3 <= 0;
      _macstream_c_wenable_3 <= 0;
      __macstream_c_fsm_3_cond_13_0_1 <= 0;
      __macstream_c_fsm_3_cond_14_1_1 <= 0;
    end else begin
      _d1__macstream_c_fsm_3 <= _macstream_c_fsm_3;
      case(_d1__macstream_c_fsm_3)
        _macstream_c_fsm_3_13: begin
          if(__macstream_c_fsm_3_cond_13_0_1) begin
            _macstream_c_wenable_3 <= 0;
          end 
        end
        _macstream_c_fsm_3_14: begin
          if(__macstream_c_fsm_3_cond_14_1_1) begin
            _macstream_c_wenable_3 <= 0;
          end 
        end
      endcase
      case(_macstream_c_fsm_3)
        _macstream_c_fsm_3_init: begin
          if(th_comp == 10) begin
            _macstream_c_offset_3 <= _th_comp_offset_9;
            _macstream_c_size_3 <= _th_comp_size_8;
            _macstream_c_stride_3 <= 1;
          end 
          if(_macstream_start && (_macstream_c_fsm_sel == 3) && (_macstream_c_size_3 > 0)) begin
            _macstream_c_count_3 <= _macstream_c_size_3;
          end 
          if(_macstream_start && (_macstream_c_fsm_sel == 3) && (_macstream_c_size_3 > 0)) begin
            _macstream_c_fsm_3 <= _macstream_c_fsm_3_1;
          end 
        end
        _macstream_c_fsm_3_1: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_2;
        end
        _macstream_c_fsm_3_2: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_3;
        end
        _macstream_c_fsm_3_3: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_4;
        end
        _macstream_c_fsm_3_4: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_5;
        end
        _macstream_c_fsm_3_5: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_6;
        end
        _macstream_c_fsm_3_6: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_7;
        end
        _macstream_c_fsm_3_7: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_8;
        end
        _macstream_c_fsm_3_8: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_9;
        end
        _macstream_c_fsm_3_9: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_10;
        end
        _macstream_c_fsm_3_10: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_11;
        end
        _macstream_c_fsm_3_11: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_12;
        end
        _macstream_c_fsm_3_12: begin
          _macstream_c_fsm_3 <= _macstream_c_fsm_3_13;
        end
        _macstream_c_fsm_3_13: begin
          _macstream_c_waddr_3 <= _macstream_c_offset_3;
          _macstream_c_wdata_3 <= macstream_c_data;
          _macstream_c_wenable_3 <= 1;
          _macstream_c_count_3 <= _macstream_c_count_3 - 1;
          __macstream_c_fsm_3_cond_13_0_1 <= 1;
          if(_macstream_c_count_3 == 1) begin
            _macstream_c_fsm_3 <= _macstream_c_fsm_3_init;
          end 
          if(_macstream_c_count_3 > 1) begin
            _macstream_c_fsm_3 <= _macstream_c_fsm_3_14;
          end 
        end
        _macstream_c_fsm_3_14: begin
          _macstream_c_waddr_3 <= _macstream_c_waddr_3 + _macstream_c_stride_3;
          _macstream_c_wdata_3 <= macstream_c_data;
          _macstream_c_wenable_3 <= 1;
          _macstream_c_count_3 <= _macstream_c_count_3 - 1;
          __macstream_c_fsm_3_cond_14_1_1 <= 1;
          if(_macstream_c_count_3 == 1) begin
            _macstream_c_fsm_3 <= _macstream_c_fsm_3_init;
          end 
        end
      endcase
    end
  end

  localparam _macstream_v_fsm_4_1 = 1;
  localparam _macstream_v_fsm_4_2 = 2;
  localparam _macstream_v_fsm_4_3 = 3;
  localparam _macstream_v_fsm_4_4 = 4;
  localparam _macstream_v_fsm_4_5 = 5;
  localparam _macstream_v_fsm_4_6 = 6;
  localparam _macstream_v_fsm_4_7 = 7;
  localparam _macstream_v_fsm_4_8 = 8;
  localparam _macstream_v_fsm_4_9 = 9;
  localparam _macstream_v_fsm_4_10 = 10;
  localparam _macstream_v_fsm_4_11 = 11;
  localparam _macstream_v_fsm_4_12 = 12;
  localparam _macstream_v_fsm_4_13 = 13;
  localparam _macstream_v_fsm_4_14 = 14;

  always @(posedge CLK) begin
    if(RST) begin
      _macstream_v_fsm_4 <= _macstream_v_fsm_4_init;
      _d1__macstream_v_fsm_4 <= _macstream_v_fsm_4_init;
      _macstream_v_offset_4 <= 0;
      _macstream_v_size_4 <= 0;
      _macstream_v_stride_4 <= 0;
      _macstream_v_count_4 <= 0;
      _macstream_v_waddr_4 <= 0;
      _macstream_v_wdata_4 <= 0;
      _macstream_v_wenable_4 <= 0;
      __macstream_v_fsm_4_cond_13_0_1 <= 0;
      __macstream_v_fsm_4_cond_14_1_1 <= 0;
    end else begin
      _d1__macstream_v_fsm_4 <= _macstream_v_fsm_4;
      case(_d1__macstream_v_fsm_4)
        _macstream_v_fsm_4_13: begin
          if(__macstream_v_fsm_4_cond_13_0_1) begin
            _macstream_v_wenable_4 <= 0;
          end 
        end
        _macstream_v_fsm_4_14: begin
          if(__macstream_v_fsm_4_cond_14_1_1) begin
            _macstream_v_wenable_4 <= 0;
          end 
        end
      endcase
      case(_macstream_v_fsm_4)
        _macstream_v_fsm_4_init: begin
          if(th_comp == 11) begin
            _macstream_v_offset_4 <= _th_comp_offset_9;
            _macstream_v_size_4 <= _th_comp_size_8;
            _macstream_v_stride_4 <= 1;
          end 
          if(_macstream_start && (_macstream_v_fsm_sel == 4) && (_macstream_v_size_4 > 0)) begin
            _macstream_v_count_4 <= _macstream_v_size_4;
          end 
          if(_macstream_start && (_macstream_v_fsm_sel == 4) && (_macstream_v_size_4 > 0)) begin
            _macstream_v_fsm_4 <= _macstream_v_fsm_4_1;
          end 
        end
        _macstream_v_fsm_4_1: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_2;
        end
        _macstream_v_fsm_4_2: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_3;
        end
        _macstream_v_fsm_4_3: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_4;
        end
        _macstream_v_fsm_4_4: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_5;
        end
        _macstream_v_fsm_4_5: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_6;
        end
        _macstream_v_fsm_4_6: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_7;
        end
        _macstream_v_fsm_4_7: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_8;
        end
        _macstream_v_fsm_4_8: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_9;
        end
        _macstream_v_fsm_4_9: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_10;
        end
        _macstream_v_fsm_4_10: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_11;
        end
        _macstream_v_fsm_4_11: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_12;
        end
        _macstream_v_fsm_4_12: begin
          _macstream_v_fsm_4 <= _macstream_v_fsm_4_13;
        end
        _macstream_v_fsm_4_13: begin
          _macstream_v_waddr_4 <= _macstream_v_offset_4;
          _macstream_v_wdata_4 <= macstream_v_data;
          _macstream_v_wenable_4 <= 1;
          _macstream_v_count_4 <= _macstream_v_count_4 - 1;
          __macstream_v_fsm_4_cond_13_0_1 <= 1;
          if(_macstream_v_count_4 == 1) begin
            _macstream_v_fsm_4 <= _macstream_v_fsm_4_init;
          end 
          if(_macstream_v_count_4 > 1) begin
            _macstream_v_fsm_4 <= _macstream_v_fsm_4_14;
          end 
        end
        _macstream_v_fsm_4_14: begin
          _macstream_v_waddr_4 <= _macstream_v_waddr_4 + _macstream_v_stride_4;
          _macstream_v_wdata_4 <= macstream_v_data;
          _macstream_v_wenable_4 <= 1;
          _macstream_v_count_4 <= _macstream_v_count_4 - 1;
          __macstream_v_fsm_4_cond_14_1_1 <= 1;
          if(_macstream_v_count_4 == 1) begin
            _macstream_v_fsm_4 <= _macstream_v_fsm_4_init;
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
      _tmp_31 <= 0;
      _tmp_33 <= 0;
      _tmp_32 <= 0;
      _tmp_49 <= 0;
      __tmp_fsm_2_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_0_1) begin
            _tmp_49 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_comp == 15) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_31 <= (_tmp_29 >> 2) << 2;
          _tmp_33 <= _tmp_30;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_33 <= 256) && ((_tmp_31 & 4095) + (_tmp_33 << 2) >= 4096)) begin
            _tmp_32 <= 4096 - (_tmp_31 & 4095) >> 2;
            _tmp_33 <= _tmp_33 - (4096 - (_tmp_31 & 4095) >> 2);
          end else if(_tmp_33 <= 256) begin
            _tmp_32 <= _tmp_33;
            _tmp_33 <= 0;
          end else if((_tmp_31 & 4095) + 1024 >= 4096) begin
            _tmp_32 <= 4096 - (_tmp_31 & 4095) >> 2;
            _tmp_33 <= _tmp_33 - (4096 - (_tmp_31 & 4095) >> 2);
          end else begin
            _tmp_32 <= 256;
            _tmp_33 <= _tmp_33 - 256;
          end
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_4;
          end 
        end
        _tmp_fsm_2_4: begin
          if(_tmp_47 && myaxi_wvalid && myaxi_wready) begin
            _tmp_31 <= _tmp_31 + (_tmp_32 << 2);
          end 
          if(_tmp_47 && myaxi_wvalid && myaxi_wready && (_tmp_33 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(_tmp_47 && myaxi_wvalid && myaxi_wready && (_tmp_33 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_49 <= 1;
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
      _tmp_53 <= 0;
      _tmp_55 <= 0;
      _tmp_54 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_57 <= 0;
      _tmp_56 <= 0;
      _tmp_62 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_57 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_62 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_comp == 18) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_53 <= (_tmp_51 >> 2) << 2;
          _tmp_55 <= _tmp_52;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_55 <= 256) && ((_tmp_53 & 4095) + (_tmp_55 << 2) >= 4096)) begin
            _tmp_54 <= 4096 - (_tmp_53 & 4095) >> 2;
            _tmp_55 <= _tmp_55 - (4096 - (_tmp_53 & 4095) >> 2);
          end else if(_tmp_55 <= 256) begin
            _tmp_54 <= _tmp_55;
            _tmp_55 <= 0;
          end else if((_tmp_53 & 4095) + 1024 >= 4096) begin
            _tmp_54 <= 4096 - (_tmp_53 & 4095) >> 2;
            _tmp_55 <= _tmp_55 - (4096 - (_tmp_53 & 4095) >> 2);
          end else begin
            _tmp_54 <= 256;
            _tmp_55 <= _tmp_55 - 256;
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
            _tmp_56 <= myaxi_rdata;
            _tmp_57 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_53 <= _tmp_53 + (_tmp_54 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_55 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_55 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_62 <= 1;
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
      _tmp_66 <= 0;
      _tmp_68 <= 0;
      _tmp_67 <= 0;
      __tmp_fsm_4_cond_4_0_1 <= 0;
      _tmp_70 <= 0;
      _tmp_69 <= 0;
      _tmp_75 <= 0;
      __tmp_fsm_4_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_4 <= _tmp_fsm_4;
      case(_d1__tmp_fsm_4)
        _tmp_fsm_4_4: begin
          if(__tmp_fsm_4_cond_4_0_1) begin
            _tmp_70 <= 0;
          end 
        end
        _tmp_fsm_4_5: begin
          if(__tmp_fsm_4_cond_5_1_1) begin
            _tmp_75 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_4)
        _tmp_fsm_4_init: begin
          if(th_comp == 20) begin
            _tmp_fsm_4 <= _tmp_fsm_4_1;
          end 
        end
        _tmp_fsm_4_1: begin
          _tmp_66 <= (_tmp_64 >> 2) << 2;
          _tmp_68 <= _tmp_65;
          _tmp_fsm_4 <= _tmp_fsm_4_2;
        end
        _tmp_fsm_4_2: begin
          if((_tmp_68 <= 256) && ((_tmp_66 & 4095) + (_tmp_68 << 2) >= 4096)) begin
            _tmp_67 <= 4096 - (_tmp_66 & 4095) >> 2;
            _tmp_68 <= _tmp_68 - (4096 - (_tmp_66 & 4095) >> 2);
          end else if(_tmp_68 <= 256) begin
            _tmp_67 <= _tmp_68;
            _tmp_68 <= 0;
          end else if((_tmp_66 & 4095) + 1024 >= 4096) begin
            _tmp_67 <= 4096 - (_tmp_66 & 4095) >> 2;
            _tmp_68 <= _tmp_68 - (4096 - (_tmp_66 & 4095) >> 2);
          end else begin
            _tmp_67 <= 256;
            _tmp_68 <= _tmp_68 - 256;
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
            _tmp_69 <= myaxi_rdata;
            _tmp_70 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_66 <= _tmp_66 + (_tmp_67 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_68 > 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_68 == 0)) begin
            _tmp_fsm_4 <= _tmp_fsm_4_5;
          end 
        end
        _tmp_fsm_4_5: begin
          _tmp_75 <= 1;
          __tmp_fsm_4_cond_5_1_1 <= 1;
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
      _tmp_83 <= 0;
      _tmp_85 <= 0;
      _tmp_84 <= 0;
      _tmp_101 <= 0;
      __tmp_fsm_5_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_5 <= _tmp_fsm_5;
      case(_d1__tmp_fsm_5)
        _tmp_fsm_5_5: begin
          if(__tmp_fsm_5_cond_5_0_1) begin
            _tmp_101 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_5)
        _tmp_fsm_5_init: begin
          if(th_comp == 39) begin
            _tmp_fsm_5 <= _tmp_fsm_5_1;
          end 
        end
        _tmp_fsm_5_1: begin
          _tmp_83 <= (_tmp_81 >> 2) << 2;
          _tmp_85 <= _tmp_82;
          _tmp_fsm_5 <= _tmp_fsm_5_2;
        end
        _tmp_fsm_5_2: begin
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
          _tmp_fsm_5 <= _tmp_fsm_5_3;
        end
        _tmp_fsm_5_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_5 <= _tmp_fsm_5_4;
          end 
        end
        _tmp_fsm_5_4: begin
          if(_tmp_99 && myaxi_wvalid && myaxi_wready) begin
            _tmp_83 <= _tmp_83 + (_tmp_84 << 2);
          end 
          if(_tmp_99 && myaxi_wvalid && myaxi_wready && (_tmp_85 > 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_2;
          end 
          if(_tmp_99 && myaxi_wvalid && myaxi_wready && (_tmp_85 == 0)) begin
            _tmp_fsm_5 <= _tmp_fsm_5_5;
          end 
        end
        _tmp_fsm_5_5: begin
          _tmp_101 <= 1;
          __tmp_fsm_5_cond_5_0_1 <= 1;
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
      _tmp_109 <= 0;
      _tmp_111 <= 0;
      _tmp_110 <= 0;
      __tmp_fsm_6_cond_4_0_1 <= 0;
      _tmp_113 <= 0;
      _tmp_112 <= 0;
      _tmp_118 <= 0;
      __tmp_fsm_6_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_6 <= _tmp_fsm_6;
      case(_d1__tmp_fsm_6)
        _tmp_fsm_6_4: begin
          if(__tmp_fsm_6_cond_4_0_1) begin
            _tmp_113 <= 0;
          end 
        end
        _tmp_fsm_6_5: begin
          if(__tmp_fsm_6_cond_5_1_1) begin
            _tmp_118 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_6)
        _tmp_fsm_6_init: begin
          if(th_comp == 59) begin
            _tmp_fsm_6 <= _tmp_fsm_6_1;
          end 
        end
        _tmp_fsm_6_1: begin
          _tmp_109 <= (_tmp_107 >> 2) << 2;
          _tmp_111 <= _tmp_108;
          _tmp_fsm_6 <= _tmp_fsm_6_2;
        end
        _tmp_fsm_6_2: begin
          if((_tmp_111 <= 256) && ((_tmp_109 & 4095) + (_tmp_111 << 2) >= 4096)) begin
            _tmp_110 <= 4096 - (_tmp_109 & 4095) >> 2;
            _tmp_111 <= _tmp_111 - (4096 - (_tmp_109 & 4095) >> 2);
          end else if(_tmp_111 <= 256) begin
            _tmp_110 <= _tmp_111;
            _tmp_111 <= 0;
          end else if((_tmp_109 & 4095) + 1024 >= 4096) begin
            _tmp_110 <= 4096 - (_tmp_109 & 4095) >> 2;
            _tmp_111 <= _tmp_111 - (4096 - (_tmp_109 & 4095) >> 2);
          end else begin
            _tmp_110 <= 256;
            _tmp_111 <= _tmp_111 - 256;
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
            _tmp_112 <= myaxi_rdata;
            _tmp_113 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_109 <= _tmp_109 + (_tmp_110 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_111 > 0)) begin
            _tmp_fsm_6 <= _tmp_fsm_6_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_111 == 0)) begin
            _tmp_fsm_6 <= _tmp_fsm_6_5;
          end 
        end
        _tmp_fsm_6_5: begin
          _tmp_118 <= 1;
          __tmp_fsm_6_cond_5_1_1 <= 1;
          _tmp_fsm_6 <= _tmp_fsm_6_6;
        end
        _tmp_fsm_6_6: begin
          _tmp_fsm_6 <= _tmp_fsm_6_init;
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
      _tmp_122 <= 0;
      _tmp_124 <= 0;
      _tmp_123 <= 0;
      __tmp_fsm_7_cond_4_0_1 <= 0;
      _tmp_126 <= 0;
      _tmp_125 <= 0;
      _tmp_131 <= 0;
      __tmp_fsm_7_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_7 <= _tmp_fsm_7;
      case(_d1__tmp_fsm_7)
        _tmp_fsm_7_4: begin
          if(__tmp_fsm_7_cond_4_0_1) begin
            _tmp_126 <= 0;
          end 
        end
        _tmp_fsm_7_5: begin
          if(__tmp_fsm_7_cond_5_1_1) begin
            _tmp_131 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_7)
        _tmp_fsm_7_init: begin
          if(th_comp == 61) begin
            _tmp_fsm_7 <= _tmp_fsm_7_1;
          end 
        end
        _tmp_fsm_7_1: begin
          _tmp_122 <= (_tmp_120 >> 2) << 2;
          _tmp_124 <= _tmp_121;
          _tmp_fsm_7 <= _tmp_fsm_7_2;
        end
        _tmp_fsm_7_2: begin
          if((_tmp_124 <= 256) && ((_tmp_122 & 4095) + (_tmp_124 << 2) >= 4096)) begin
            _tmp_123 <= 4096 - (_tmp_122 & 4095) >> 2;
            _tmp_124 <= _tmp_124 - (4096 - (_tmp_122 & 4095) >> 2);
          end else if(_tmp_124 <= 256) begin
            _tmp_123 <= _tmp_124;
            _tmp_124 <= 0;
          end else if((_tmp_122 & 4095) + 1024 >= 4096) begin
            _tmp_123 <= 4096 - (_tmp_122 & 4095) >> 2;
            _tmp_124 <= _tmp_124 - (4096 - (_tmp_122 & 4095) >> 2);
          end else begin
            _tmp_123 <= 256;
            _tmp_124 <= _tmp_124 - 256;
          end
          _tmp_fsm_7 <= _tmp_fsm_7_3;
        end
        _tmp_fsm_7_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_7 <= _tmp_fsm_7_4;
          end 
        end
        _tmp_fsm_7_4: begin
          __tmp_fsm_7_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_125 <= myaxi_rdata;
            _tmp_126 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_122 <= _tmp_122 + (_tmp_123 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_124 > 0)) begin
            _tmp_fsm_7 <= _tmp_fsm_7_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_124 == 0)) begin
            _tmp_fsm_7 <= _tmp_fsm_7_5;
          end 
        end
        _tmp_fsm_7_5: begin
          _tmp_131 <= 1;
          __tmp_fsm_7_cond_5_1_1 <= 1;
          _tmp_fsm_7 <= _tmp_fsm_7_6;
        end
        _tmp_fsm_7_6: begin
          _tmp_fsm_7 <= _tmp_fsm_7_init;
        end
      endcase
    end
  end

  localparam _mystream_x_fsm_1_1 = 1;
  localparam _mystream_x_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_x_fsm_1 <= _mystream_x_fsm_1_init;
      _d1__mystream_x_fsm_1 <= _mystream_x_fsm_1_init;
      _mystream_x_offset_1 <= 0;
      _mystream_x_size_1 <= 0;
      _mystream_x_stride_1 <= 0;
      _mystream_x_count_1 <= 0;
      _mystream_x_raddr_1 <= 0;
      _mystream_x_renable_1 <= 0;
      __mystream_x_fsm_1_cond_1_0_1 <= 0;
      __mystream_x_fsm_1_cond_2_1_1 <= 0;
    end else begin
      _d1__mystream_x_fsm_1 <= _mystream_x_fsm_1;
      case(_d1__mystream_x_fsm_1)
        _mystream_x_fsm_1_1: begin
          if(__mystream_x_fsm_1_cond_1_0_1) begin
            _mystream_x_renable_1 <= 0;
          end 
        end
        _mystream_x_fsm_1_2: begin
          if(__mystream_x_fsm_1_cond_2_1_1) begin
            _mystream_x_renable_1 <= 0;
          end 
        end
      endcase
      case(_mystream_x_fsm_1)
        _mystream_x_fsm_1_init: begin
          if(th_comp == 63) begin
            _mystream_x_offset_1 <= _th_comp_offset_25;
            _mystream_x_size_1 <= _th_comp_size_24;
            _mystream_x_stride_1 <= 1;
          end 
          if(_mystream_start && (_mystream_x_fsm_sel == 1) && (_mystream_x_size_1 > 0)) begin
            _mystream_x_count_1 <= _mystream_x_size_1;
          end 
          if(_mystream_start && (_mystream_x_fsm_sel == 1) && (_mystream_x_size_1 > 0)) begin
            _mystream_x_fsm_1 <= _mystream_x_fsm_1_1;
          end 
        end
        _mystream_x_fsm_1_1: begin
          _mystream_x_raddr_1 <= _mystream_x_offset_1;
          _mystream_x_renable_1 <= 1;
          _mystream_x_count_1 <= _mystream_x_count_1 - 1;
          __mystream_x_fsm_1_cond_1_0_1 <= 1;
          if(_mystream_x_count_1 == 1) begin
            _mystream_x_fsm_1 <= _mystream_x_fsm_1_init;
          end 
          if(_mystream_x_count_1 > 1) begin
            _mystream_x_fsm_1 <= _mystream_x_fsm_1_2;
          end 
        end
        _mystream_x_fsm_1_2: begin
          _mystream_x_raddr_1 <= _mystream_x_raddr_1 + _mystream_x_stride_1;
          _mystream_x_renable_1 <= 1;
          _mystream_x_count_1 <= _mystream_x_count_1 - 1;
          __mystream_x_fsm_1_cond_2_1_1 <= 1;
          if(_mystream_x_count_1 == 1) begin
            _mystream_x_fsm_1 <= _mystream_x_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_y_fsm_2_1 = 1;
  localparam _mystream_y_fsm_2_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_y_fsm_2 <= _mystream_y_fsm_2_init;
      _d1__mystream_y_fsm_2 <= _mystream_y_fsm_2_init;
      _mystream_y_offset_2 <= 0;
      _mystream_y_size_2 <= 0;
      _mystream_y_stride_2 <= 0;
      _mystream_y_count_2 <= 0;
      _mystream_y_raddr_2 <= 0;
      _mystream_y_renable_2 <= 0;
      __mystream_y_fsm_2_cond_1_0_1 <= 0;
      __mystream_y_fsm_2_cond_2_1_1 <= 0;
    end else begin
      _d1__mystream_y_fsm_2 <= _mystream_y_fsm_2;
      case(_d1__mystream_y_fsm_2)
        _mystream_y_fsm_2_1: begin
          if(__mystream_y_fsm_2_cond_1_0_1) begin
            _mystream_y_renable_2 <= 0;
          end 
        end
        _mystream_y_fsm_2_2: begin
          if(__mystream_y_fsm_2_cond_2_1_1) begin
            _mystream_y_renable_2 <= 0;
          end 
        end
      endcase
      case(_mystream_y_fsm_2)
        _mystream_y_fsm_2_init: begin
          if(th_comp == 64) begin
            _mystream_y_offset_2 <= _th_comp_offset_25;
            _mystream_y_size_2 <= _th_comp_size_24;
            _mystream_y_stride_2 <= 1;
          end 
          if(_mystream_start && (_mystream_y_fsm_sel == 2) && (_mystream_y_size_2 > 0)) begin
            _mystream_y_count_2 <= _mystream_y_size_2;
          end 
          if(_mystream_start && (_mystream_y_fsm_sel == 2) && (_mystream_y_size_2 > 0)) begin
            _mystream_y_fsm_2 <= _mystream_y_fsm_2_1;
          end 
        end
        _mystream_y_fsm_2_1: begin
          _mystream_y_raddr_2 <= _mystream_y_offset_2;
          _mystream_y_renable_2 <= 1;
          _mystream_y_count_2 <= _mystream_y_count_2 - 1;
          __mystream_y_fsm_2_cond_1_0_1 <= 1;
          if(_mystream_y_count_2 == 1) begin
            _mystream_y_fsm_2 <= _mystream_y_fsm_2_init;
          end 
          if(_mystream_y_count_2 > 1) begin
            _mystream_y_fsm_2 <= _mystream_y_fsm_2_2;
          end 
        end
        _mystream_y_fsm_2_2: begin
          _mystream_y_raddr_2 <= _mystream_y_raddr_2 + _mystream_y_stride_2;
          _mystream_y_renable_2 <= 1;
          _mystream_y_count_2 <= _mystream_y_count_2 - 1;
          __mystream_y_fsm_2_cond_2_1_1 <= 1;
          if(_mystream_y_count_2 == 1) begin
            _mystream_y_fsm_2 <= _mystream_y_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _mystream_z_fsm_3_1 = 1;
  localparam _mystream_z_fsm_3_2 = 2;
  localparam _mystream_z_fsm_3_3 = 3;
  localparam _mystream_z_fsm_3_4 = 4;
  localparam _mystream_z_fsm_3_5 = 5;
  localparam _mystream_z_fsm_3_6 = 6;
  localparam _mystream_z_fsm_3_7 = 7;
  localparam _mystream_z_fsm_3_8 = 8;
  localparam _mystream_z_fsm_3_9 = 9;
  localparam _mystream_z_fsm_3_10 = 10;
  localparam _mystream_z_fsm_3_11 = 11;
  localparam _mystream_z_fsm_3_12 = 12;
  localparam _mystream_z_fsm_3_13 = 13;
  localparam _mystream_z_fsm_3_14 = 14;
  localparam _mystream_z_fsm_3_15 = 15;
  localparam _mystream_z_fsm_3_16 = 16;
  localparam _mystream_z_fsm_3_17 = 17;
  localparam _mystream_z_fsm_3_18 = 18;
  localparam _mystream_z_fsm_3_19 = 19;
  localparam _mystream_z_fsm_3_20 = 20;
  localparam _mystream_z_fsm_3_21 = 21;
  localparam _mystream_z_fsm_3_22 = 22;
  localparam _mystream_z_fsm_3_23 = 23;

  always @(posedge CLK) begin
    if(RST) begin
      _mystream_z_fsm_3 <= _mystream_z_fsm_3_init;
      _d1__mystream_z_fsm_3 <= _mystream_z_fsm_3_init;
      _mystream_z_offset_3 <= 0;
      _mystream_z_size_3 <= 0;
      _mystream_z_stride_3 <= 0;
      _mystream_z_count_3 <= 0;
      _mystream_z_waddr_3 <= 0;
      _mystream_z_wdata_3 <= 0;
      _mystream_z_wenable_3 <= 0;
      __mystream_z_fsm_3_cond_22_0_1 <= 0;
      __mystream_z_fsm_3_cond_23_1_1 <= 0;
    end else begin
      _d1__mystream_z_fsm_3 <= _mystream_z_fsm_3;
      case(_d1__mystream_z_fsm_3)
        _mystream_z_fsm_3_22: begin
          if(__mystream_z_fsm_3_cond_22_0_1) begin
            _mystream_z_wenable_3 <= 0;
          end 
        end
        _mystream_z_fsm_3_23: begin
          if(__mystream_z_fsm_3_cond_23_1_1) begin
            _mystream_z_wenable_3 <= 0;
          end 
        end
      endcase
      case(_mystream_z_fsm_3)
        _mystream_z_fsm_3_init: begin
          if(th_comp == 66) begin
            _mystream_z_offset_3 <= _th_comp_offset_25;
            _mystream_z_size_3 <= _th_comp_size_24 >>> 2;
            _mystream_z_stride_3 <= 1;
          end 
          if(_mystream_start && (_mystream_z_fsm_sel == 3) && (_mystream_z_size_3 > 0)) begin
            _mystream_z_count_3 <= _mystream_z_size_3;
          end 
          if(_mystream_start && (_mystream_z_fsm_sel == 3) && (_mystream_z_size_3 > 0)) begin
            _mystream_z_fsm_3 <= _mystream_z_fsm_3_1;
          end 
        end
        _mystream_z_fsm_3_1: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_2;
        end
        _mystream_z_fsm_3_2: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_3;
        end
        _mystream_z_fsm_3_3: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_4;
        end
        _mystream_z_fsm_3_4: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_5;
        end
        _mystream_z_fsm_3_5: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_6;
        end
        _mystream_z_fsm_3_6: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_7;
        end
        _mystream_z_fsm_3_7: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_8;
        end
        _mystream_z_fsm_3_8: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_9;
        end
        _mystream_z_fsm_3_9: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_10;
        end
        _mystream_z_fsm_3_10: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_11;
        end
        _mystream_z_fsm_3_11: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_12;
        end
        _mystream_z_fsm_3_12: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_13;
        end
        _mystream_z_fsm_3_13: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_14;
        end
        _mystream_z_fsm_3_14: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_15;
        end
        _mystream_z_fsm_3_15: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_16;
        end
        _mystream_z_fsm_3_16: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_17;
        end
        _mystream_z_fsm_3_17: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_18;
        end
        _mystream_z_fsm_3_18: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_19;
        end
        _mystream_z_fsm_3_19: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_20;
        end
        _mystream_z_fsm_3_20: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_21;
        end
        _mystream_z_fsm_3_21: begin
          _mystream_z_fsm_3 <= _mystream_z_fsm_3_22;
        end
        _mystream_z_fsm_3_22: begin
          if(mystream_v_data) begin
            _mystream_z_waddr_3 <= _mystream_z_offset_3;
            _mystream_z_wdata_3 <= mystream_z_data;
            _mystream_z_wenable_3 <= 1;
            _mystream_z_count_3 <= _mystream_z_count_3 - 1;
          end 
          __mystream_z_fsm_3_cond_22_0_1 <= 1;
          if(mystream_v_data && (_mystream_z_count_3 == 1)) begin
            _mystream_z_fsm_3 <= _mystream_z_fsm_3_init;
          end 
          if(mystream_v_data && (_mystream_z_count_3 > 1)) begin
            _mystream_z_fsm_3 <= _mystream_z_fsm_3_23;
          end 
        end
        _mystream_z_fsm_3_23: begin
          if(mystream_v_data) begin
            _mystream_z_waddr_3 <= _mystream_z_waddr_3 + _mystream_z_stride_3;
            _mystream_z_wdata_3 <= mystream_z_data;
            _mystream_z_wenable_3 <= 1;
            _mystream_z_count_3 <= _mystream_z_count_3 - 1;
          end 
          __mystream_z_fsm_3_cond_23_1_1 <= 1;
          if(mystream_v_data && (_mystream_z_count_3 == 1)) begin
            _mystream_z_fsm_3 <= _mystream_z_fsm_3_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_8_1 = 1;
  localparam _tmp_fsm_8_2 = 2;
  localparam _tmp_fsm_8_3 = 3;
  localparam _tmp_fsm_8_4 = 4;
  localparam _tmp_fsm_8_5 = 5;
  localparam _tmp_fsm_8_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_8 <= _tmp_fsm_8_init;
      _d1__tmp_fsm_8 <= _tmp_fsm_8_init;
      _tmp_137 <= 0;
      _tmp_139 <= 0;
      _tmp_138 <= 0;
      _tmp_155 <= 0;
      __tmp_fsm_8_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_8 <= _tmp_fsm_8;
      case(_d1__tmp_fsm_8)
        _tmp_fsm_8_5: begin
          if(__tmp_fsm_8_cond_5_0_1) begin
            _tmp_155 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_8)
        _tmp_fsm_8_init: begin
          if(th_comp == 70) begin
            _tmp_fsm_8 <= _tmp_fsm_8_1;
          end 
        end
        _tmp_fsm_8_1: begin
          _tmp_137 <= (_tmp_135 >> 2) << 2;
          _tmp_139 <= _tmp_136;
          _tmp_fsm_8 <= _tmp_fsm_8_2;
        end
        _tmp_fsm_8_2: begin
          if((_tmp_139 <= 256) && ((_tmp_137 & 4095) + (_tmp_139 << 2) >= 4096)) begin
            _tmp_138 <= 4096 - (_tmp_137 & 4095) >> 2;
            _tmp_139 <= _tmp_139 - (4096 - (_tmp_137 & 4095) >> 2);
          end else if(_tmp_139 <= 256) begin
            _tmp_138 <= _tmp_139;
            _tmp_139 <= 0;
          end else if((_tmp_137 & 4095) + 1024 >= 4096) begin
            _tmp_138 <= 4096 - (_tmp_137 & 4095) >> 2;
            _tmp_139 <= _tmp_139 - (4096 - (_tmp_137 & 4095) >> 2);
          end else begin
            _tmp_138 <= 256;
            _tmp_139 <= _tmp_139 - 256;
          end
          _tmp_fsm_8 <= _tmp_fsm_8_3;
        end
        _tmp_fsm_8_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_8 <= _tmp_fsm_8_4;
          end 
        end
        _tmp_fsm_8_4: begin
          if(_tmp_153 && myaxi_wvalid && myaxi_wready) begin
            _tmp_137 <= _tmp_137 + (_tmp_138 << 2);
          end 
          if(_tmp_153 && myaxi_wvalid && myaxi_wready && (_tmp_139 > 0)) begin
            _tmp_fsm_8 <= _tmp_fsm_8_2;
          end 
          if(_tmp_153 && myaxi_wvalid && myaxi_wready && (_tmp_139 == 0)) begin
            _tmp_fsm_8 <= _tmp_fsm_8_5;
          end 
        end
        _tmp_fsm_8_5: begin
          _tmp_155 <= 1;
          __tmp_fsm_8_cond_5_0_1 <= 1;
          _tmp_fsm_8 <= _tmp_fsm_8_6;
        end
        _tmp_fsm_8_6: begin
          _tmp_fsm_8 <= _tmp_fsm_8_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_9_1 = 1;
  localparam _tmp_fsm_9_2 = 2;
  localparam _tmp_fsm_9_3 = 3;
  localparam _tmp_fsm_9_4 = 4;
  localparam _tmp_fsm_9_5 = 5;
  localparam _tmp_fsm_9_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_9 <= _tmp_fsm_9_init;
      _d1__tmp_fsm_9 <= _tmp_fsm_9_init;
      _tmp_159 <= 0;
      _tmp_161 <= 0;
      _tmp_160 <= 0;
      __tmp_fsm_9_cond_4_0_1 <= 0;
      _tmp_163 <= 0;
      _tmp_162 <= 0;
      _tmp_168 <= 0;
      __tmp_fsm_9_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_9 <= _tmp_fsm_9;
      case(_d1__tmp_fsm_9)
        _tmp_fsm_9_4: begin
          if(__tmp_fsm_9_cond_4_0_1) begin
            _tmp_163 <= 0;
          end 
        end
        _tmp_fsm_9_5: begin
          if(__tmp_fsm_9_cond_5_1_1) begin
            _tmp_168 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_9)
        _tmp_fsm_9_init: begin
          if(th_comp == 73) begin
            _tmp_fsm_9 <= _tmp_fsm_9_1;
          end 
        end
        _tmp_fsm_9_1: begin
          _tmp_159 <= (_tmp_157 >> 2) << 2;
          _tmp_161 <= _tmp_158;
          _tmp_fsm_9 <= _tmp_fsm_9_2;
        end
        _tmp_fsm_9_2: begin
          if((_tmp_161 <= 256) && ((_tmp_159 & 4095) + (_tmp_161 << 2) >= 4096)) begin
            _tmp_160 <= 4096 - (_tmp_159 & 4095) >> 2;
            _tmp_161 <= _tmp_161 - (4096 - (_tmp_159 & 4095) >> 2);
          end else if(_tmp_161 <= 256) begin
            _tmp_160 <= _tmp_161;
            _tmp_161 <= 0;
          end else if((_tmp_159 & 4095) + 1024 >= 4096) begin
            _tmp_160 <= 4096 - (_tmp_159 & 4095) >> 2;
            _tmp_161 <= _tmp_161 - (4096 - (_tmp_159 & 4095) >> 2);
          end else begin
            _tmp_160 <= 256;
            _tmp_161 <= _tmp_161 - 256;
          end
          _tmp_fsm_9 <= _tmp_fsm_9_3;
        end
        _tmp_fsm_9_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_9 <= _tmp_fsm_9_4;
          end 
        end
        _tmp_fsm_9_4: begin
          __tmp_fsm_9_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_162 <= myaxi_rdata;
            _tmp_163 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_159 <= _tmp_159 + (_tmp_160 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_161 > 0)) begin
            _tmp_fsm_9 <= _tmp_fsm_9_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_161 == 0)) begin
            _tmp_fsm_9 <= _tmp_fsm_9_5;
          end 
        end
        _tmp_fsm_9_5: begin
          _tmp_168 <= 1;
          __tmp_fsm_9_cond_5_1_1 <= 1;
          _tmp_fsm_9 <= _tmp_fsm_9_6;
        end
        _tmp_fsm_9_6: begin
          _tmp_fsm_9 <= _tmp_fsm_9_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_10_1 = 1;
  localparam _tmp_fsm_10_2 = 2;
  localparam _tmp_fsm_10_3 = 3;
  localparam _tmp_fsm_10_4 = 4;
  localparam _tmp_fsm_10_5 = 5;
  localparam _tmp_fsm_10_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_10 <= _tmp_fsm_10_init;
      _d1__tmp_fsm_10 <= _tmp_fsm_10_init;
      _tmp_172 <= 0;
      _tmp_174 <= 0;
      _tmp_173 <= 0;
      __tmp_fsm_10_cond_4_0_1 <= 0;
      _tmp_176 <= 0;
      _tmp_175 <= 0;
      _tmp_181 <= 0;
      __tmp_fsm_10_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_10 <= _tmp_fsm_10;
      case(_d1__tmp_fsm_10)
        _tmp_fsm_10_4: begin
          if(__tmp_fsm_10_cond_4_0_1) begin
            _tmp_176 <= 0;
          end 
        end
        _tmp_fsm_10_5: begin
          if(__tmp_fsm_10_cond_5_1_1) begin
            _tmp_181 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_10)
        _tmp_fsm_10_init: begin
          if(th_comp == 75) begin
            _tmp_fsm_10 <= _tmp_fsm_10_1;
          end 
        end
        _tmp_fsm_10_1: begin
          _tmp_172 <= (_tmp_170 >> 2) << 2;
          _tmp_174 <= _tmp_171;
          _tmp_fsm_10 <= _tmp_fsm_10_2;
        end
        _tmp_fsm_10_2: begin
          if((_tmp_174 <= 256) && ((_tmp_172 & 4095) + (_tmp_174 << 2) >= 4096)) begin
            _tmp_173 <= 4096 - (_tmp_172 & 4095) >> 2;
            _tmp_174 <= _tmp_174 - (4096 - (_tmp_172 & 4095) >> 2);
          end else if(_tmp_174 <= 256) begin
            _tmp_173 <= _tmp_174;
            _tmp_174 <= 0;
          end else if((_tmp_172 & 4095) + 1024 >= 4096) begin
            _tmp_173 <= 4096 - (_tmp_172 & 4095) >> 2;
            _tmp_174 <= _tmp_174 - (4096 - (_tmp_172 & 4095) >> 2);
          end else begin
            _tmp_173 <= 256;
            _tmp_174 <= _tmp_174 - 256;
          end
          _tmp_fsm_10 <= _tmp_fsm_10_3;
        end
        _tmp_fsm_10_3: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_10 <= _tmp_fsm_10_4;
          end 
        end
        _tmp_fsm_10_4: begin
          __tmp_fsm_10_cond_4_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_175 <= myaxi_rdata;
            _tmp_176 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_172 <= _tmp_172 + (_tmp_173 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_174 > 0)) begin
            _tmp_fsm_10 <= _tmp_fsm_10_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_174 == 0)) begin
            _tmp_fsm_10 <= _tmp_fsm_10_5;
          end 
        end
        _tmp_fsm_10_5: begin
          _tmp_181 <= 1;
          __tmp_fsm_10_cond_5_1_1 <= 1;
          _tmp_fsm_10 <= _tmp_fsm_10_6;
        end
        _tmp_fsm_10_6: begin
          _tmp_fsm_10 <= _tmp_fsm_10_init;
        end
      endcase
    end
  end

  localparam _tmp_fsm_11_1 = 1;
  localparam _tmp_fsm_11_2 = 2;
  localparam _tmp_fsm_11_3 = 3;
  localparam _tmp_fsm_11_4 = 4;
  localparam _tmp_fsm_11_5 = 5;
  localparam _tmp_fsm_11_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_11 <= _tmp_fsm_11_init;
      _d1__tmp_fsm_11 <= _tmp_fsm_11_init;
      _tmp_189 <= 0;
      _tmp_191 <= 0;
      _tmp_190 <= 0;
      _tmp_207 <= 0;
      __tmp_fsm_11_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_11 <= _tmp_fsm_11;
      case(_d1__tmp_fsm_11)
        _tmp_fsm_11_5: begin
          if(__tmp_fsm_11_cond_5_0_1) begin
            _tmp_207 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_11)
        _tmp_fsm_11_init: begin
          if(th_comp == 96) begin
            _tmp_fsm_11 <= _tmp_fsm_11_1;
          end 
        end
        _tmp_fsm_11_1: begin
          _tmp_189 <= (_tmp_187 >> 2) << 2;
          _tmp_191 <= _tmp_188;
          _tmp_fsm_11 <= _tmp_fsm_11_2;
        end
        _tmp_fsm_11_2: begin
          if((_tmp_191 <= 256) && ((_tmp_189 & 4095) + (_tmp_191 << 2) >= 4096)) begin
            _tmp_190 <= 4096 - (_tmp_189 & 4095) >> 2;
            _tmp_191 <= _tmp_191 - (4096 - (_tmp_189 & 4095) >> 2);
          end else if(_tmp_191 <= 256) begin
            _tmp_190 <= _tmp_191;
            _tmp_191 <= 0;
          end else if((_tmp_189 & 4095) + 1024 >= 4096) begin
            _tmp_190 <= 4096 - (_tmp_189 & 4095) >> 2;
            _tmp_191 <= _tmp_191 - (4096 - (_tmp_189 & 4095) >> 2);
          end else begin
            _tmp_190 <= 256;
            _tmp_191 <= _tmp_191 - 256;
          end
          _tmp_fsm_11 <= _tmp_fsm_11_3;
        end
        _tmp_fsm_11_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_11 <= _tmp_fsm_11_4;
          end 
        end
        _tmp_fsm_11_4: begin
          if(_tmp_205 && myaxi_wvalid && myaxi_wready) begin
            _tmp_189 <= _tmp_189 + (_tmp_190 << 2);
          end 
          if(_tmp_205 && myaxi_wvalid && myaxi_wready && (_tmp_191 > 0)) begin
            _tmp_fsm_11 <= _tmp_fsm_11_2;
          end 
          if(_tmp_205 && myaxi_wvalid && myaxi_wready && (_tmp_191 == 0)) begin
            _tmp_fsm_11 <= _tmp_fsm_11_5;
          end 
        end
        _tmp_fsm_11_5: begin
          _tmp_207 <= 1;
          __tmp_fsm_11_cond_5_0_1 <= 1;
          _tmp_fsm_11 <= _tmp_fsm_11_6;
        end
        _tmp_fsm_11_6: begin
          _tmp_fsm_11 <= _tmp_fsm_11_init;
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
    test_module = thread_stream_substream_nested_reduce.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
