from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_embedded_verilog_ipcore

expected_verilog = """
module test;

  reg uut_CLK;
  reg uut_RST;
  wire [8-1:0] uut_led;
  wire [32-1:0] uut_maxi_awaddr;
  wire [8-1:0] uut_maxi_awlen;
  wire uut_maxi_awvalid;
  reg uut_maxi_awready;
  wire [32-1:0] uut_maxi_wdata;
  wire [4-1:0] uut_maxi_wstrb;
  wire uut_maxi_wlast;
  wire uut_maxi_wvalid;
  reg uut_maxi_wready;
  wire [32-1:0] uut_maxi_araddr;
  wire [8-1:0] uut_maxi_arlen;
  wire uut_maxi_arvalid;
  reg uut_maxi_arready;
  reg [32-1:0] uut_maxi_rdata;
  reg uut_maxi_rlast;
  reg uut_maxi_rvalid;
  wire uut_maxi_rready;
  reg [32-1:0] uut_saxi_awaddr;
  reg uut_saxi_awvalid;
  wire uut_saxi_awready;
  reg [32-1:0] uut_saxi_wdata;
  reg [4-1:0] uut_saxi_wstrb;
  reg uut_saxi_wvalid;
  wire uut_saxi_wready;
  reg [32-1:0] uut_saxi_araddr;
  reg uut_saxi_arvalid;
  wire uut_saxi_arready;
  wire [32-1:0] uut_saxi_rdata;
  wire uut_saxi_rvalid;
  reg uut_saxi_rready;

  blinkled
  uut
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .led(uut_led),
    .maxi_awaddr(uut_maxi_awaddr),
    .maxi_awlen(uut_maxi_awlen),
    .maxi_awvalid(uut_maxi_awvalid),
    .maxi_awready(uut_maxi_awready),
    .maxi_wdata(uut_maxi_wdata),
    .maxi_wstrb(uut_maxi_wstrb),
    .maxi_wlast(uut_maxi_wlast),
    .maxi_wvalid(uut_maxi_wvalid),
    .maxi_wready(uut_maxi_wready),
    .maxi_araddr(uut_maxi_araddr),
    .maxi_arlen(uut_maxi_arlen),
    .maxi_arvalid(uut_maxi_arvalid),
    .maxi_arready(uut_maxi_arready),
    .maxi_rdata(uut_maxi_rdata),
    .maxi_rlast(uut_maxi_rlast),
    .maxi_rvalid(uut_maxi_rvalid),
    .maxi_rready(uut_maxi_rready),
    .saxi_awaddr(uut_saxi_awaddr),
    .saxi_awvalid(uut_saxi_awvalid),
    .saxi_awready(uut_saxi_awready),
    .saxi_wdata(uut_saxi_wdata),
    .saxi_wstrb(uut_saxi_wstrb),
    .saxi_wvalid(uut_saxi_wvalid),
    .saxi_wready(uut_saxi_wready),
    .saxi_araddr(uut_saxi_araddr),
    .saxi_arvalid(uut_saxi_arvalid),
    .saxi_arready(uut_saxi_arready),
    .saxi_rdata(uut_saxi_rdata),
    .saxi_rvalid(uut_saxi_rvalid),
    .saxi_rready(uut_saxi_rready)
  );

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
  assign memory_awaddr = uut_maxi_awaddr;
  assign memory_awlen = uut_maxi_awlen;
  assign memory_awvalid = uut_maxi_awvalid;
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    uut_maxi_awready = _tmp_0;
  end

  assign memory_wdata = uut_maxi_wdata;
  assign memory_wstrb = uut_maxi_wstrb;
  assign memory_wlast = uut_maxi_wlast;
  assign memory_wvalid = uut_maxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    uut_maxi_wready = _tmp_1;
  end

  assign memory_araddr = uut_maxi_araddr;
  assign memory_arlen = uut_maxi_arlen;
  assign memory_arvalid = uut_maxi_arvalid;
  wire _tmp_2;
  assign _tmp_2 = memory_arready;

  always @(*) begin
    uut_maxi_arready = _tmp_2;
  end


  always @(*) begin
    uut_maxi_rdata = memory_rdata;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_rlast;

  always @(*) begin
    uut_maxi_rlast = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = memory_rvalid;

  always @(*) begin
    uut_maxi_rvalid = _tmp_4;
  end

  assign memory_rready = uut_maxi_rready;
  reg [32-1:0] _saxi_awaddr;
  reg _saxi_awvalid;
  wire _saxi_awready;
  reg [32-1:0] _saxi_wdata;
  reg [4-1:0] _saxi_wstrb;
  reg _saxi_wvalid;
  wire _saxi_wready;
  reg [32-1:0] _saxi_araddr;
  reg _saxi_arvalid;
  wire _saxi_arready;
  wire [32-1:0] _saxi_rdata;
  wire _saxi_rvalid;
  wire _saxi_rready;
  reg __saxi_read_start;
  reg [8-1:0] __saxi_read_op_sel;
  reg [32-1:0] __saxi_read_local_addr;
  reg [32-1:0] __saxi_read_global_addr;
  reg [33-1:0] __saxi_read_size;
  reg [32-1:0] __saxi_read_local_stride;
  reg __saxi_read_idle;
  reg __saxi_write_start;
  reg [8-1:0] __saxi_write_op_sel;
  reg [32-1:0] __saxi_write_local_addr;
  reg [32-1:0] __saxi_write_global_addr;
  reg [33-1:0] __saxi_write_size;
  reg [32-1:0] __saxi_write_local_stride;
  reg __saxi_write_idle;
  wire __saxi_write_data_done;
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _saxi_awaddr;

  always @(*) begin
    uut_saxi_awaddr = _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = _saxi_awvalid;

  always @(*) begin
    uut_saxi_awvalid = _tmp_6;
  end

  assign _saxi_awready = uut_saxi_awready;
  wire [32-1:0] _tmp_7;
  assign _tmp_7 = _saxi_wdata;

  always @(*) begin
    uut_saxi_wdata = _tmp_7;
  end

  wire [4-1:0] _tmp_8;
  assign _tmp_8 = _saxi_wstrb;

  always @(*) begin
    uut_saxi_wstrb = _tmp_8;
  end

  wire _tmp_9;
  assign _tmp_9 = _saxi_wvalid;

  always @(*) begin
    uut_saxi_wvalid = _tmp_9;
  end

  assign _saxi_wready = uut_saxi_wready;
  wire [32-1:0] _tmp_10;
  assign _tmp_10 = _saxi_araddr;

  always @(*) begin
    uut_saxi_araddr = _tmp_10;
  end

  wire _tmp_11;
  assign _tmp_11 = _saxi_arvalid;

  always @(*) begin
    uut_saxi_arvalid = _tmp_11;
  end

  assign _saxi_arready = uut_saxi_arready;
  assign _saxi_rdata = uut_saxi_rdata;
  assign _saxi_rvalid = uut_saxi_rvalid;
  wire _tmp_12;
  assign _tmp_12 = _saxi_rready;

  always @(*) begin
    uut_saxi_rready = _tmp_12;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_11;
  reg signed [32-1:0] _th_ctrl_awaddr_12;
  reg __saxi_cond_0_1;
  reg __saxi_cond_1_1;
  reg signed [32-1:0] _th_ctrl_src_offset_13;
  reg __saxi_cond_2_1;
  reg __saxi_cond_3_1;
  reg signed [32-1:0] _th_ctrl_dst_offset_14;
  reg __saxi_cond_4_1;
  reg __saxi_cond_5_1;
  reg signed [32-1:0] _th_ctrl_start_time_15;
  reg __saxi_cond_6_1;
  reg __saxi_cond_7_1;
  reg signed [32-1:0] _th_ctrl_araddr_16;
  reg __saxi_cond_8_1;
  reg signed [32-1:0] axim_rdata_13;
  reg signed [32-1:0] _th_ctrl_v_17;
  reg __saxi_cond_9_1;
  assign _saxi_rready = (th_ctrl == 25) || (th_ctrl == 29);
  reg signed [32-1:0] axim_rdata_14;
  reg signed [32-1:0] _th_ctrl_end_time_18;
  reg signed [32-1:0] _th_ctrl_time_19;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    uut_CLK = 0;
    forever begin
      #5 uut_CLK = !uut_CLK;
    end
  end


  initial begin
    uut_RST = 0;
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
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    _saxi_wdata = 0;
    _saxi_wstrb = 0;
    _saxi_wvalid = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    __saxi_read_start = 0;
    __saxi_read_op_sel = 0;
    __saxi_read_local_addr = 0;
    __saxi_read_global_addr = 0;
    __saxi_read_size = 0;
    __saxi_read_local_stride = 0;
    __saxi_read_idle = 1;
    __saxi_write_start = 0;
    __saxi_write_op_sel = 0;
    __saxi_write_local_addr = 0;
    __saxi_write_global_addr = 0;
    __saxi_write_size = 0;
    __saxi_write_local_stride = 0;
    __saxi_write_idle = 1;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_11 = 0;
    _th_ctrl_awaddr_12 = 0;
    __saxi_cond_0_1 = 0;
    __saxi_cond_1_1 = 0;
    _th_ctrl_src_offset_13 = 0;
    __saxi_cond_2_1 = 0;
    __saxi_cond_3_1 = 0;
    _th_ctrl_dst_offset_14 = 0;
    __saxi_cond_4_1 = 0;
    __saxi_cond_5_1 = 0;
    _th_ctrl_start_time_15 = 0;
    __saxi_cond_6_1 = 0;
    __saxi_cond_7_1 = 0;
    _th_ctrl_araddr_16 = 0;
    __saxi_cond_8_1 = 0;
    axim_rdata_13 = 0;
    _th_ctrl_v_17 = 0;
    __saxi_cond_9_1 = 0;
    axim_rdata_14 = 0;
    _th_ctrl_end_time_18 = 0;
    _th_ctrl_time_19 = 0;
    #100;
    uut_RST = 1;
    #100;
    uut_RST = 0;
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

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
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


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      __saxi_read_start <= 0;
      __saxi_write_start <= 0;
      _saxi_awaddr <= 0;
      _saxi_awvalid <= 0;
      __saxi_cond_0_1 <= 0;
      _saxi_wdata <= 0;
      _saxi_wvalid <= 0;
      _saxi_wstrb <= 0;
      __saxi_cond_1_1 <= 0;
      __saxi_cond_2_1 <= 0;
      __saxi_cond_3_1 <= 0;
      __saxi_cond_4_1 <= 0;
      __saxi_cond_5_1 <= 0;
      __saxi_cond_6_1 <= 0;
      __saxi_cond_7_1 <= 0;
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_8_1 <= 0;
      __saxi_cond_9_1 <= 0;
    end else begin
      if(__saxi_cond_0_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_1_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_2_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_3_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_4_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_5_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_6_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_7_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_8_1) begin
        _saxi_arvalid <= 0;
      end 
      if(__saxi_cond_9_1) begin
        _saxi_arvalid <= 0;
      end 
      __saxi_read_start <= 0;
      __saxi_write_start <= 0;
      if((th_ctrl == 6) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 7) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= 4096;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 11) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 12) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_src_offset_13;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 16) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 17) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_dst_offset_14;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_5_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 21) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_12;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_6_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 22) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_7_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 24) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_16;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_8_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
      if((th_ctrl == 28) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_16;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_9_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
    end
  end


  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      counter <= 0;
    end else begin
      counter <= counter + 1;
    end
  end

  localparam th_ctrl_1 = 1;
  localparam th_ctrl_2 = 2;
  localparam th_ctrl_3 = 3;
  localparam th_ctrl_4 = 4;
  localparam th_ctrl_5 = 5;
  localparam th_ctrl_6 = 6;
  localparam th_ctrl_7 = 7;
  localparam th_ctrl_8 = 8;
  localparam th_ctrl_9 = 9;
  localparam th_ctrl_10 = 10;
  localparam th_ctrl_11 = 11;
  localparam th_ctrl_12 = 12;
  localparam th_ctrl_13 = 13;
  localparam th_ctrl_14 = 14;
  localparam th_ctrl_15 = 15;
  localparam th_ctrl_16 = 16;
  localparam th_ctrl_17 = 17;
  localparam th_ctrl_18 = 18;
  localparam th_ctrl_19 = 19;
  localparam th_ctrl_20 = 20;
  localparam th_ctrl_21 = 21;
  localparam th_ctrl_22 = 22;
  localparam th_ctrl_23 = 23;
  localparam th_ctrl_24 = 24;
  localparam th_ctrl_25 = 25;
  localparam th_ctrl_26 = 26;
  localparam th_ctrl_27 = 27;
  localparam th_ctrl_28 = 28;
  localparam th_ctrl_29 = 29;
  localparam th_ctrl_30 = 30;
  localparam th_ctrl_31 = 31;
  localparam th_ctrl_32 = 32;
  localparam th_ctrl_33 = 33;
  localparam th_ctrl_34 = 34;
  localparam th_ctrl_35 = 35;
  localparam th_ctrl_36 = 36;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_11 <= 0;
      _th_ctrl_awaddr_12 <= 0;
      _th_ctrl_src_offset_13 <= 0;
      _th_ctrl_dst_offset_14 <= 0;
      _th_ctrl_start_time_15 <= 0;
      _th_ctrl_araddr_16 <= 0;
      axim_rdata_13 <= 0;
      _th_ctrl_v_17 <= 0;
      axim_rdata_14 <= 0;
      _th_ctrl_end_time_18 <= 0;
      _th_ctrl_time_19 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_11 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_11 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_11 <= _th_ctrl_i_11 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_12 <= 4;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          $display("# copy_bytes = %d", 4096);
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_7;
          end 
        end
        th_ctrl_7: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_8;
          end 
        end
        th_ctrl_8: begin
          _th_ctrl_awaddr_12 <= 8;
          th_ctrl <= th_ctrl_9;
        end
        th_ctrl_9: begin
          _th_ctrl_src_offset_13 <= 0;
          th_ctrl <= th_ctrl_10;
        end
        th_ctrl_10: begin
          $display("# src_offset = %d", _th_ctrl_src_offset_13);
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_12;
          end 
        end
        th_ctrl_12: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_13;
          end 
        end
        th_ctrl_13: begin
          _th_ctrl_awaddr_12 <= 12;
          th_ctrl <= th_ctrl_14;
        end
        th_ctrl_14: begin
          _th_ctrl_dst_offset_14 <= 8192;
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          $display("# dst_offset = %d", _th_ctrl_dst_offset_14);
          th_ctrl <= th_ctrl_16;
        end
        th_ctrl_16: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_17;
          end 
        end
        th_ctrl_17: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_18;
          end 
        end
        th_ctrl_18: begin
          _th_ctrl_awaddr_12 <= 0;
          th_ctrl <= th_ctrl_19;
        end
        th_ctrl_19: begin
          _th_ctrl_start_time_15 <= counter;
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          $display("# start time = %d", _th_ctrl_start_time_15);
          th_ctrl <= th_ctrl_21;
        end
        th_ctrl_21: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_22;
          end 
        end
        th_ctrl_22: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_23;
          end 
        end
        th_ctrl_23: begin
          _th_ctrl_araddr_16 <= 16;
          th_ctrl <= th_ctrl_24;
        end
        th_ctrl_24: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_25;
          end 
        end
        th_ctrl_25: begin
          if(_saxi_rready && _saxi_rvalid) begin
            axim_rdata_13 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_26;
          end 
        end
        th_ctrl_26: begin
          _th_ctrl_v_17 <= axim_rdata_13;
          th_ctrl <= th_ctrl_27;
        end
        th_ctrl_27: begin
          if(_th_ctrl_v_17 == 0) begin
            th_ctrl <= th_ctrl_28;
          end else begin
            th_ctrl <= th_ctrl_32;
          end
        end
        th_ctrl_28: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_29;
          end 
        end
        th_ctrl_29: begin
          if(_saxi_rready && _saxi_rvalid) begin
            axim_rdata_14 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_30;
          end 
        end
        th_ctrl_30: begin
          _th_ctrl_v_17 <= axim_rdata_14;
          th_ctrl <= th_ctrl_31;
        end
        th_ctrl_31: begin
          th_ctrl <= th_ctrl_27;
        end
        th_ctrl_32: begin
          _th_ctrl_end_time_18 <= counter;
          th_ctrl <= th_ctrl_33;
        end
        th_ctrl_33: begin
          $display("# end time = %d", _th_ctrl_end_time_18);
          th_ctrl <= th_ctrl_34;
        end
        th_ctrl_34: begin
          _th_ctrl_time_19 <= _th_ctrl_end_time_18 - _th_ctrl_start_time_15;
          th_ctrl <= th_ctrl_35;
        end
        th_ctrl_35: begin
          $display("# exec time = %d", _th_ctrl_time_19);
          th_ctrl <= th_ctrl_36;
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [8-1:0] led,
  output reg [32-1:0] maxi_awaddr,
  output reg [8-1:0] maxi_awlen,
  output reg maxi_awvalid,
  input maxi_awready,
  output reg [32-1:0] maxi_wdata,
  output reg [4-1:0] maxi_wstrb,
  output reg maxi_wlast,
  output reg maxi_wvalid,
  input maxi_wready,
  output reg [32-1:0] maxi_araddr,
  output reg [8-1:0] maxi_arlen,
  output reg maxi_arvalid,
  input maxi_arready,
  input [32-1:0] maxi_rdata,
  input maxi_rlast,
  input maxi_rvalid,
  output maxi_rready,
  input [32-1:0] saxi_awaddr,
  input saxi_awvalid,
  output saxi_awready,
  input [32-1:0] saxi_wdata,
  input [4-1:0] saxi_wstrb,
  input saxi_wvalid,
  output saxi_wready,
  input [32-1:0] saxi_araddr,
  input saxi_arvalid,
  output saxi_arready,
  output reg [32-1:0] saxi_rdata,
  output reg saxi_rvalid,
  input saxi_rready
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

  reg _maxi_read_start;
  reg [8-1:0] _maxi_read_op_sel;
  reg [32-1:0] _maxi_read_local_addr;
  reg [32-1:0] _maxi_read_global_addr;
  reg [33-1:0] _maxi_read_size;
  reg [32-1:0] _maxi_read_local_stride;
  reg _maxi_read_idle;
  reg _maxi_write_start;
  reg [8-1:0] _maxi_write_op_sel;
  reg [32-1:0] _maxi_write_local_addr;
  reg [32-1:0] _maxi_write_global_addr;
  reg [33-1:0] _maxi_write_size;
  reg [32-1:0] _maxi_write_local_stride;
  reg _maxi_write_idle;
  wire _maxi_write_data_done;
  reg signed [32-1:0] _saxi_register_0;
  reg signed [32-1:0] _saxi_register_1;
  reg signed [32-1:0] _saxi_register_2;
  reg signed [32-1:0] _saxi_register_3;
  reg signed [32-1:0] _saxi_register_4;
  reg signed [32-1:0] _saxi_register_5;
  reg signed [32-1:0] _saxi_register_6;
  reg signed [32-1:0] _saxi_register_7;
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg _saxi_flag_4;
  reg _saxi_flag_5;
  reg _saxi_flag_6;
  reg _saxi_flag_7;
  reg signed [32-1:0] _saxi_resetval_0;
  reg signed [32-1:0] _saxi_resetval_1;
  reg signed [32-1:0] _saxi_resetval_2;
  reg signed [32-1:0] _saxi_resetval_3;
  reg signed [32-1:0] _saxi_resetval_4;
  reg signed [32-1:0] _saxi_resetval_5;
  reg signed [32-1:0] _saxi_resetval_6;
  reg signed [32-1:0] _saxi_resetval_7;
  localparam _saxi_maskwidth = 3;
  localparam _saxi_mask = { _saxi_maskwidth{ 1'd1 } };
  localparam _saxi_shift = 2;
  reg [32-1:0] _saxi_register_fsm;
  localparam _saxi_register_fsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg _tmp_1;
  reg _tmp_2;
  reg _tmp_3;
  reg _tmp_4;
  assign saxi_awready = (_saxi_register_fsm == 0) && !_tmp_1 && !_tmp_2 && _tmp_3;
  assign saxi_arready = (_saxi_register_fsm == 0) && !_tmp_2 && !_tmp_1 && _tmp_4;
  reg [_saxi_maskwidth-1:0] _tmp_5;
  wire signed [32-1:0] _tmp_6;
  assign _tmp_6 = (_tmp_5 == 0)? _saxi_register_0 : 
                  (_tmp_5 == 1)? _saxi_register_1 : 
                  (_tmp_5 == 2)? _saxi_register_2 : 
                  (_tmp_5 == 3)? _saxi_register_3 : 
                  (_tmp_5 == 4)? _saxi_register_4 : 
                  (_tmp_5 == 5)? _saxi_register_5 : 
                  (_tmp_5 == 6)? _saxi_register_6 : 
                  (_tmp_5 == 7)? _saxi_register_7 : 'hx;
  wire _tmp_7;
  assign _tmp_7 = (_tmp_5 == 0)? _saxi_flag_0 : 
                  (_tmp_5 == 1)? _saxi_flag_1 : 
                  (_tmp_5 == 2)? _saxi_flag_2 : 
                  (_tmp_5 == 3)? _saxi_flag_3 : 
                  (_tmp_5 == 4)? _saxi_flag_4 : 
                  (_tmp_5 == 5)? _saxi_flag_5 : 
                  (_tmp_5 == 6)? _saxi_flag_6 : 
                  (_tmp_5 == 7)? _saxi_flag_7 : 'hx;
  wire signed [32-1:0] _tmp_8;
  assign _tmp_8 = (_tmp_5 == 0)? _saxi_resetval_0 : 
                  (_tmp_5 == 1)? _saxi_resetval_1 : 
                  (_tmp_5 == 2)? _saxi_resetval_2 : 
                  (_tmp_5 == 3)? _saxi_resetval_3 : 
                  (_tmp_5 == 4)? _saxi_resetval_4 : 
                  (_tmp_5 == 5)? _saxi_resetval_5 : 
                  (_tmp_5 == 6)? _saxi_resetval_6 : 
                  (_tmp_5 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;

  reg [31:0] sum;
  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      led <= 0;
    end else begin
      if(ram_a_0_wenable) begin
        sum <= sum + ram_a_0_wdata;
      end
      led <= sum;
    end 
  end

  reg [32-1:0] th_memcpy;
  localparam th_memcpy_init = 0;
  reg signed [32-1:0] _th_memcpy_copy_bytes_0;
  reg signed [32-1:0] _th_memcpy_src_offset_1;
  reg signed [32-1:0] _th_memcpy_dst_offset_2;
  reg signed [32-1:0] _th_memcpy_copy_bytes_3;
  reg signed [32-1:0] _th_memcpy_src_offset_4;
  reg signed [32-1:0] _th_memcpy_dst_offset_5;
  reg signed [32-1:0] _th_memcpy_rest_words_6;
  reg signed [32-1:0] _th_memcpy_src_global_addr_7;
  reg signed [32-1:0] _th_memcpy_dst_global_addr_8;
  reg signed [32-1:0] _th_memcpy_local_addr_9;
  reg signed [32-1:0] _th_memcpy_dma_size_10;
  reg axim_flag_9;
  reg [32-1:0] _d1_th_memcpy;
  reg _th_memcpy_cond_16_0_1;
  reg _maxi_ram_a_0_read_start;
  reg [8-1:0] _maxi_ram_a_0_read_op_sel;
  reg [32-1:0] _maxi_ram_a_0_read_local_addr;
  reg [32-1:0] _maxi_ram_a_0_read_global_addr;
  reg [33-1:0] _maxi_ram_a_0_read_size;
  reg [32-1:0] _maxi_ram_a_0_read_local_stride;
  reg [32-1:0] _maxi_read_fsm;
  localparam _maxi_read_fsm_init = 0;
  reg [32-1:0] _maxi_read_cur_global_addr;
  reg [33-1:0] _maxi_read_cur_size;
  reg [33-1:0] _maxi_read_rest_size;
  reg [32-1:0] _wdata_10;
  reg _wvalid_11;
  reg [34-1:0] _tmp_12;
  reg _tmp_13;
  wire [32-1:0] _dataflow__variable_odata_0;
  wire _dataflow__variable_ovalid_0;
  wire _dataflow__variable_oready_0;
  assign _dataflow__variable_oready_0 = (_tmp_12 > 0) && !_tmp_13;
  reg _ram_a_cond_0_1;
  reg [9-1:0] _tmp_14;
  reg _maxi_cond_0_1;
  assign maxi_rready = _maxi_read_fsm == 3;
  reg [32-1:0] _d1__maxi_read_fsm;
  reg __maxi_read_fsm_cond_3_0_1;
  reg axim_flag_15;
  reg __maxi_read_fsm_cond_4_1_1;
  reg axim_flag_16;
  reg _th_memcpy_cond_20_1_1;
  reg _maxi_ram_a_0_write_start;
  reg [8-1:0] _maxi_ram_a_0_write_op_sel;
  reg [32-1:0] _maxi_ram_a_0_write_local_addr;
  reg [32-1:0] _maxi_ram_a_0_write_global_addr;
  reg [33-1:0] _maxi_ram_a_0_write_size;
  reg [32-1:0] _maxi_ram_a_0_write_local_stride;
  reg [32-1:0] _maxi_write_fsm;
  localparam _maxi_write_fsm_init = 0;
  reg [32-1:0] _maxi_write_cur_global_addr;
  reg [33-1:0] _maxi_write_cur_size;
  reg [33-1:0] _maxi_write_rest_size;
  reg _tmp_17;
  reg _tmp_18;
  wire _tmp_19;
  wire _tmp_20;
  assign _tmp_20 = 1;
  localparam _tmp_21 = 1;
  wire [_tmp_21-1:0] _tmp_22;
  assign _tmp_22 = (_tmp_19 || !_tmp_17) && (_tmp_20 || !_tmp_18);
  reg [_tmp_21-1:0] __tmp_22_1;
  wire signed [32-1:0] _tmp_23;
  reg signed [32-1:0] __tmp_23_1;
  assign _tmp_23 = (__tmp_22_1)? ram_a_0_rdata : __tmp_23_1;
  reg _tmp_24;
  reg _tmp_25;
  reg _tmp_26;
  reg _tmp_27;
  reg [34-1:0] _tmp_28;
  reg [9-1:0] _tmp_29;
  reg _maxi_cond_1_1;
  reg _tmp_30;
  wire [32-1:0] _dataflow__variable_odata_1;
  wire _dataflow__variable_ovalid_1;
  wire _dataflow__variable_oready_1;
  assign _dataflow__variable_oready_1 = (_maxi_write_fsm == 3) && (_maxi_write_op_sel == 1) && ((_tmp_29 > 0) && (maxi_wready || !maxi_wvalid));
  reg _maxi_cond_2_1;
  assign _maxi_write_data_done = (_tmp_30 && maxi_wvalid && maxi_wready)? 1 : 0;
  reg axim_flag_31;
  reg [32-1:0] _d1__maxi_write_fsm;
  reg __maxi_write_fsm_cond_4_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_12 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_13 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_22_1 <= 0;
      __tmp_23_1 <= 0;
      _tmp_27 <= 0;
      _tmp_17 <= 0;
      _tmp_18 <= 0;
      _tmp_25 <= 0;
      _tmp_26 <= 0;
      _tmp_24 <= 0;
      _tmp_28 <= 0;
    end else begin
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_13 <= 0;
      end 
      if(_maxi_read_start && (_maxi_read_op_sel == 1) && (_tmp_12 == 0)) begin
        ram_a_0_addr <= _maxi_read_local_addr - _maxi_read_local_stride;
        _tmp_12 <= _maxi_read_size;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _maxi_read_local_stride;
        ram_a_0_wdata <= _dataflow__variable_odata_0;
        ram_a_0_wenable <= 1;
        _tmp_12 <= _tmp_12 - 1;
      end 
      if(_dataflow__variable_ovalid_0 && ((_tmp_12 > 0) && !_tmp_13) && (_tmp_12 == 1)) begin
        _tmp_13 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      __tmp_22_1 <= _tmp_22;
      __tmp_23_1 <= _tmp_23;
      if((_tmp_19 || !_tmp_17) && (_tmp_20 || !_tmp_18) && _tmp_25) begin
        _tmp_27 <= 0;
        _tmp_17 <= 0;
        _tmp_18 <= 0;
        _tmp_25 <= 0;
      end 
      if((_tmp_19 || !_tmp_17) && (_tmp_20 || !_tmp_18) && _tmp_24) begin
        _tmp_17 <= 1;
        _tmp_18 <= 1;
        _tmp_27 <= _tmp_26;
        _tmp_26 <= 0;
        _tmp_24 <= 0;
        _tmp_25 <= 1;
      end 
      if(_maxi_write_start && (_maxi_write_op_sel == 1) && (_tmp_28 == 0) && !_tmp_26 && !_tmp_27) begin
        ram_a_0_addr <= _maxi_write_local_addr;
        _tmp_28 <= _maxi_write_size - 1;
        _tmp_24 <= 1;
        _tmp_26 <= _maxi_write_size == 1;
      end 
      if((_tmp_19 || !_tmp_17) && (_tmp_20 || !_tmp_18) && (_tmp_28 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + _maxi_write_local_stride;
        _tmp_28 <= _tmp_28 - 1;
        _tmp_24 <= 1;
        _tmp_26 <= 0;
      end 
      if((_tmp_19 || !_tmp_17) && (_tmp_20 || !_tmp_18) && (_tmp_28 == 1)) begin
        _tmp_26 <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_1 = _tmp_23;
  assign _dataflow__variable_ovalid_1 = _tmp_17;
  assign _tmp_19 = 1 && _dataflow__variable_oready_1;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      _maxi_ram_a_0_read_start <= 0;
      _maxi_ram_a_0_read_op_sel <= 0;
      _maxi_ram_a_0_read_local_addr <= 0;
      _maxi_ram_a_0_read_global_addr <= 0;
      _maxi_ram_a_0_read_size <= 0;
      _maxi_ram_a_0_read_local_stride <= 0;
      _maxi_read_idle <= 1;
      _maxi_read_op_sel <= 0;
      _maxi_read_local_addr <= 0;
      _maxi_read_global_addr <= 0;
      _maxi_read_size <= 0;
      _maxi_read_local_stride <= 0;
      maxi_araddr <= 0;
      maxi_arlen <= 0;
      maxi_arvalid <= 0;
      _tmp_14 <= 0;
      _maxi_cond_0_1 <= 0;
      _maxi_ram_a_0_write_start <= 0;
      _maxi_ram_a_0_write_op_sel <= 0;
      _maxi_ram_a_0_write_local_addr <= 0;
      _maxi_ram_a_0_write_global_addr <= 0;
      _maxi_ram_a_0_write_size <= 0;
      _maxi_ram_a_0_write_local_stride <= 0;
      _maxi_write_idle <= 1;
      _maxi_write_op_sel <= 0;
      _maxi_write_local_addr <= 0;
      _maxi_write_global_addr <= 0;
      _maxi_write_size <= 0;
      _maxi_write_local_stride <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      _tmp_29 <= 0;
      _maxi_cond_1_1 <= 0;
      maxi_wdata <= 0;
      maxi_wvalid <= 0;
      maxi_wlast <= 0;
      maxi_wstrb <= 0;
      _tmp_30 <= 0;
      _maxi_cond_2_1 <= 0;
    end else begin
      if(_maxi_cond_0_1) begin
        maxi_arvalid <= 0;
      end 
      if(_maxi_cond_1_1) begin
        maxi_awvalid <= 0;
      end 
      if(_maxi_cond_2_1) begin
        maxi_wvalid <= 0;
        maxi_wlast <= 0;
        _tmp_30 <= 0;
      end 
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      _maxi_ram_a_0_read_start <= 0;
      if(axim_flag_9) begin
        _maxi_ram_a_0_read_start <= 1;
        _maxi_ram_a_0_read_op_sel <= 1;
        _maxi_ram_a_0_read_local_addr <= _th_memcpy_local_addr_9;
        _maxi_ram_a_0_read_global_addr <= _th_memcpy_src_global_addr_7;
        _maxi_ram_a_0_read_size <= _th_memcpy_dma_size_10;
        _maxi_ram_a_0_read_local_stride <= 1;
      end 
      if(_maxi_ram_a_0_read_start) begin
        _maxi_read_idle <= 0;
      end 
      if(_maxi_ram_a_0_read_start) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= _maxi_ram_a_0_read_op_sel;
        _maxi_read_local_addr <= _maxi_ram_a_0_read_local_addr;
        _maxi_read_global_addr <= _maxi_ram_a_0_read_global_addr;
        _maxi_read_size <= _maxi_ram_a_0_read_size;
        _maxi_read_local_stride <= _maxi_ram_a_0_read_local_stride;
      end 
      if((_maxi_read_fsm == 2) && ((maxi_arready || !maxi_arvalid) && (_tmp_14 == 0))) begin
        maxi_araddr <= _maxi_read_cur_global_addr;
        maxi_arlen <= _maxi_read_cur_size - 1;
        maxi_arvalid <= 1;
        _tmp_14 <= _maxi_read_cur_size;
      end 
      _maxi_cond_0_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
      if(maxi_rready && maxi_rvalid && (_tmp_14 > 0)) begin
        _tmp_14 <= _tmp_14 - 1;
      end 
      if(axim_flag_15) begin
        _maxi_read_idle <= 1;
      end 
      _maxi_ram_a_0_write_start <= 0;
      if(axim_flag_16) begin
        _maxi_ram_a_0_write_start <= 1;
        _maxi_ram_a_0_write_op_sel <= 1;
        _maxi_ram_a_0_write_local_addr <= _th_memcpy_local_addr_9;
        _maxi_ram_a_0_write_global_addr <= _th_memcpy_dst_global_addr_8;
        _maxi_ram_a_0_write_size <= _th_memcpy_dma_size_10;
        _maxi_ram_a_0_write_local_stride <= 1;
      end 
      if(_maxi_ram_a_0_write_start) begin
        _maxi_write_idle <= 0;
      end 
      if(_maxi_ram_a_0_write_start) begin
        _maxi_write_start <= 1;
        _maxi_write_op_sel <= _maxi_ram_a_0_write_op_sel;
        _maxi_write_local_addr <= _maxi_ram_a_0_write_local_addr;
        _maxi_write_global_addr <= _maxi_ram_a_0_write_global_addr;
        _maxi_write_size <= _maxi_ram_a_0_write_size;
        _maxi_write_local_stride <= _maxi_ram_a_0_write_local_stride;
      end 
      if((_maxi_write_fsm == 2) && ((maxi_awready || !maxi_awvalid) && (_tmp_29 == 0))) begin
        maxi_awaddr <= _maxi_write_cur_global_addr;
        maxi_awlen <= _maxi_write_cur_size - 1;
        maxi_awvalid <= 1;
        _tmp_29 <= _maxi_write_cur_size;
      end 
      if((_maxi_write_fsm == 2) && ((maxi_awready || !maxi_awvalid) && (_tmp_29 == 0)) && (_maxi_write_cur_size == 0)) begin
        maxi_awvalid <= 0;
      end 
      _maxi_cond_1_1 <= 1;
      if(maxi_awvalid && !maxi_awready) begin
        maxi_awvalid <= maxi_awvalid;
      end 
      if(_dataflow__variable_ovalid_1 && ((_maxi_write_fsm == 3) && (_maxi_write_op_sel == 1) && ((_tmp_29 > 0) && (maxi_wready || !maxi_wvalid))) && ((_tmp_29 > 0) && (maxi_wready || !maxi_wvalid) && (_tmp_29 > 0))) begin
        maxi_wdata <= _dataflow__variable_odata_1;
        maxi_wvalid <= 1;
        maxi_wlast <= 0;
        maxi_wstrb <= { 4{ 1'd1 } };
        _tmp_29 <= _tmp_29 - 1;
      end 
      if(_dataflow__variable_ovalid_1 && ((_maxi_write_fsm == 3) && (_maxi_write_op_sel == 1) && ((_tmp_29 > 0) && (maxi_wready || !maxi_wvalid))) && ((_tmp_29 > 0) && (maxi_wready || !maxi_wvalid) && (_tmp_29 > 0)) && (_tmp_29 == 1)) begin
        maxi_wlast <= 1;
        _tmp_30 <= 1;
      end 
      _maxi_cond_2_1 <= 1;
      if(maxi_wvalid && !maxi_wready) begin
        maxi_wvalid <= maxi_wvalid;
        maxi_wlast <= maxi_wlast;
        _tmp_30 <= _tmp_30;
      end 
      if(axim_flag_31) begin
        _maxi_write_idle <= 1;
      end 
    end
  end

  assign _dataflow__variable_odata_0 = _wdata_10;
  assign _dataflow__variable_ovalid_0 = _wvalid_11;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_0 <= 0;
      saxi_rdata <= 0;
      saxi_rvalid <= 0;
      _saxi_cond_0_1 <= 0;
      _saxi_register_0 <= 0;
      _saxi_flag_0 <= 0;
      _saxi_register_1 <= 0;
      _saxi_flag_1 <= 0;
      _saxi_register_2 <= 0;
      _saxi_flag_2 <= 0;
      _saxi_register_3 <= 0;
      _saxi_flag_3 <= 0;
      _saxi_register_4 <= 0;
      _saxi_flag_4 <= 0;
      _saxi_register_5 <= 0;
      _saxi_flag_5 <= 0;
      _saxi_register_6 <= 0;
      _saxi_flag_6 <= 0;
      _saxi_register_7 <= 0;
      _saxi_flag_7 <= 0;
      _saxi_resetval_0 <= 0;
      _saxi_resetval_1 <= 0;
      _saxi_resetval_2 <= 0;
      _saxi_resetval_3 <= 0;
      _saxi_resetval_4 <= 0;
      _saxi_resetval_5 <= 0;
      _saxi_resetval_6 <= 0;
      _saxi_resetval_7 <= 0;
    end else begin
      if(_saxi_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      _tmp_3 <= saxi_awvalid;
      _tmp_4 <= saxi_arvalid;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      if(saxi_awready && saxi_awvalid) begin
        _tmp_0 <= saxi_awaddr;
        _tmp_1 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        _tmp_0 <= saxi_araddr;
        _tmp_2 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= _tmp_6;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 0)) begin
        _saxi_register_0 <= _tmp_8;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 1)) begin
        _saxi_register_1 <= _tmp_8;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 2)) begin
        _saxi_register_2 <= _tmp_8;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 3)) begin
        _saxi_register_3 <= _tmp_8;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 4)) begin
        _saxi_register_4 <= _tmp_8;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 5)) begin
        _saxi_register_5 <= _tmp_8;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 6)) begin
        _saxi_register_6 <= _tmp_8;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && _tmp_7 && (_tmp_5 == 7)) begin
        _saxi_register_7 <= _tmp_8;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && (saxi_wready && saxi_wvalid) && (_tmp_5 == 7)) begin
        _saxi_register_7 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_4 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_5 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_6 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_memcpy == 2) && 0) begin
        _saxi_register_7 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 1;
        _saxi_resetval_0 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 1;
        _saxi_resetval_1 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 1;
        _saxi_resetval_2 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 1;
        _saxi_resetval_3 <= 0;
      end 
      if((th_memcpy == 28) && 1) begin
        _saxi_register_4 <= 1;
        _saxi_flag_4 <= 1;
        _saxi_resetval_4 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_5 <= 1;
        _saxi_flag_5 <= 1;
        _saxi_resetval_5 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_6 <= 1;
        _saxi_flag_6 <= 1;
        _saxi_resetval_6 <= 0;
      end 
      if((th_memcpy == 28) && 0) begin
        _saxi_register_7 <= 1;
        _saxi_flag_7 <= 1;
        _saxi_resetval_7 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(_tmp_2 || _tmp_1) begin
            _tmp_5 <= (_tmp_0 >> _saxi_shift) & _saxi_mask;
          end 
          if(_tmp_2) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(_tmp_1) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_2: begin
          _saxi_register_fsm <= _saxi_register_fsm_init;
        end
      endcase
    end
  end

  localparam th_memcpy_1 = 1;
  localparam th_memcpy_2 = 2;
  localparam th_memcpy_3 = 3;
  localparam th_memcpy_4 = 4;
  localparam th_memcpy_5 = 5;
  localparam th_memcpy_6 = 6;
  localparam th_memcpy_7 = 7;
  localparam th_memcpy_8 = 8;
  localparam th_memcpy_9 = 9;
  localparam th_memcpy_10 = 10;
  localparam th_memcpy_11 = 11;
  localparam th_memcpy_12 = 12;
  localparam th_memcpy_13 = 13;
  localparam th_memcpy_14 = 14;
  localparam th_memcpy_15 = 15;
  localparam th_memcpy_16 = 16;
  localparam th_memcpy_17 = 17;
  localparam th_memcpy_18 = 18;
  localparam th_memcpy_19 = 19;
  localparam th_memcpy_20 = 20;
  localparam th_memcpy_21 = 21;
  localparam th_memcpy_22 = 22;
  localparam th_memcpy_23 = 23;
  localparam th_memcpy_24 = 24;
  localparam th_memcpy_25 = 25;
  localparam th_memcpy_26 = 26;
  localparam th_memcpy_27 = 27;
  localparam th_memcpy_28 = 28;
  localparam th_memcpy_29 = 29;
  localparam th_memcpy_30 = 30;

  always @(posedge CLK) begin
    if(RST) begin
      th_memcpy <= th_memcpy_init;
      _d1_th_memcpy <= th_memcpy_init;
      _th_memcpy_copy_bytes_0 <= 0;
      _th_memcpy_src_offset_1 <= 0;
      _th_memcpy_dst_offset_2 <= 0;
      _th_memcpy_copy_bytes_3 <= 0;
      _th_memcpy_src_offset_4 <= 0;
      _th_memcpy_dst_offset_5 <= 0;
      _th_memcpy_rest_words_6 <= 0;
      _th_memcpy_src_global_addr_7 <= 0;
      _th_memcpy_dst_global_addr_8 <= 0;
      _th_memcpy_local_addr_9 <= 0;
      _th_memcpy_dma_size_10 <= 0;
      axim_flag_9 <= 0;
      _th_memcpy_cond_16_0_1 <= 0;
      axim_flag_16 <= 0;
      _th_memcpy_cond_20_1_1 <= 0;
    end else begin
      _d1_th_memcpy <= th_memcpy;
      case(_d1_th_memcpy)
        th_memcpy_16: begin
          if(_th_memcpy_cond_16_0_1) begin
            axim_flag_9 <= 0;
          end 
        end
        th_memcpy_20: begin
          if(_th_memcpy_cond_20_1_1) begin
            axim_flag_16 <= 0;
          end 
        end
      endcase
      case(th_memcpy)
        th_memcpy_init: begin
          th_memcpy <= th_memcpy_1;
        end
        th_memcpy_1: begin
          if(1) begin
            th_memcpy <= th_memcpy_2;
          end else begin
            th_memcpy <= th_memcpy_30;
          end
        end
        th_memcpy_2: begin
          if(_saxi_register_0 == 1) begin
            th_memcpy <= th_memcpy_3;
          end 
        end
        th_memcpy_3: begin
          _th_memcpy_copy_bytes_0 <= _saxi_register_1;
          th_memcpy <= th_memcpy_4;
        end
        th_memcpy_4: begin
          _th_memcpy_src_offset_1 <= _saxi_register_2;
          th_memcpy <= th_memcpy_5;
        end
        th_memcpy_5: begin
          _th_memcpy_dst_offset_2 <= _saxi_register_3;
          th_memcpy <= th_memcpy_6;
        end
        th_memcpy_6: begin
          _th_memcpy_copy_bytes_3 <= _th_memcpy_copy_bytes_0;
          _th_memcpy_src_offset_4 <= _th_memcpy_src_offset_1;
          _th_memcpy_dst_offset_5 <= _th_memcpy_dst_offset_2;
          th_memcpy <= th_memcpy_7;
        end
        th_memcpy_7: begin
          _th_memcpy_rest_words_6 <= _th_memcpy_copy_bytes_3 >>> 2;
          th_memcpy <= th_memcpy_8;
        end
        th_memcpy_8: begin
          _th_memcpy_src_global_addr_7 <= _th_memcpy_src_offset_4;
          th_memcpy <= th_memcpy_9;
        end
        th_memcpy_9: begin
          _th_memcpy_dst_global_addr_8 <= _th_memcpy_dst_offset_5;
          th_memcpy <= th_memcpy_10;
        end
        th_memcpy_10: begin
          _th_memcpy_local_addr_9 <= 0;
          th_memcpy <= th_memcpy_11;
        end
        th_memcpy_11: begin
          if(_th_memcpy_rest_words_6 > 0) begin
            th_memcpy <= th_memcpy_12;
          end else begin
            th_memcpy <= th_memcpy_28;
          end
        end
        th_memcpy_12: begin
          if(_th_memcpy_rest_words_6 > 256) begin
            th_memcpy <= th_memcpy_13;
          end else begin
            th_memcpy <= th_memcpy_15;
          end
        end
        th_memcpy_13: begin
          _th_memcpy_dma_size_10 <= 256;
          th_memcpy <= th_memcpy_14;
        end
        th_memcpy_14: begin
          th_memcpy <= th_memcpy_16;
        end
        th_memcpy_15: begin
          _th_memcpy_dma_size_10 <= _th_memcpy_rest_words_6;
          th_memcpy <= th_memcpy_16;
        end
        th_memcpy_16: begin
          axim_flag_9 <= 1;
          _th_memcpy_cond_16_0_1 <= 1;
          th_memcpy <= th_memcpy_17;
        end
        th_memcpy_17: begin
          th_memcpy <= th_memcpy_18;
        end
        th_memcpy_18: begin
          th_memcpy <= th_memcpy_19;
        end
        th_memcpy_19: begin
          if(_maxi_read_idle) begin
            th_memcpy <= th_memcpy_20;
          end 
        end
        th_memcpy_20: begin
          axim_flag_16 <= 1;
          _th_memcpy_cond_20_1_1 <= 1;
          th_memcpy <= th_memcpy_21;
        end
        th_memcpy_21: begin
          th_memcpy <= th_memcpy_22;
        end
        th_memcpy_22: begin
          th_memcpy <= th_memcpy_23;
        end
        th_memcpy_23: begin
          if(_maxi_write_idle) begin
            th_memcpy <= th_memcpy_24;
          end 
        end
        th_memcpy_24: begin
          _th_memcpy_src_global_addr_7 <= _th_memcpy_src_global_addr_7 + (_th_memcpy_dma_size_10 << 2);
          th_memcpy <= th_memcpy_25;
        end
        th_memcpy_25: begin
          _th_memcpy_dst_global_addr_8 <= _th_memcpy_dst_global_addr_8 + (_th_memcpy_dma_size_10 << 2);
          th_memcpy <= th_memcpy_26;
        end
        th_memcpy_26: begin
          _th_memcpy_rest_words_6 <= _th_memcpy_rest_words_6 - _th_memcpy_dma_size_10;
          th_memcpy <= th_memcpy_27;
        end
        th_memcpy_27: begin
          th_memcpy <= th_memcpy_11;
        end
        th_memcpy_28: begin
          th_memcpy <= th_memcpy_29;
        end
        th_memcpy_29: begin
          th_memcpy <= th_memcpy_1;
        end
      endcase
    end
  end

  localparam _maxi_read_fsm_1 = 1;
  localparam _maxi_read_fsm_2 = 2;
  localparam _maxi_read_fsm_3 = 3;
  localparam _maxi_read_fsm_4 = 4;
  localparam _maxi_read_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_fsm <= _maxi_read_fsm_init;
      _d1__maxi_read_fsm <= _maxi_read_fsm_init;
      _maxi_read_cur_global_addr <= 0;
      _maxi_read_rest_size <= 0;
      _maxi_read_cur_size <= 0;
      __maxi_read_fsm_cond_3_0_1 <= 0;
      _wvalid_11 <= 0;
      _wdata_10 <= 0;
      axim_flag_15 <= 0;
      __maxi_read_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__maxi_read_fsm <= _maxi_read_fsm;
      case(_d1__maxi_read_fsm)
        _maxi_read_fsm_3: begin
          if(__maxi_read_fsm_cond_3_0_1) begin
            _wvalid_11 <= 0;
          end 
        end
        _maxi_read_fsm_4: begin
          if(__maxi_read_fsm_cond_4_1_1) begin
            axim_flag_15 <= 0;
          end 
        end
      endcase
      case(_maxi_read_fsm)
        _maxi_read_fsm_init: begin
          if(_maxi_read_start) begin
            _maxi_read_cur_global_addr <= (_maxi_read_global_addr >> 2) << 2;
            _maxi_read_rest_size <= _maxi_read_size;
          end 
          if(_maxi_read_start && (_maxi_read_op_sel == 1)) begin
            _maxi_read_fsm <= _maxi_read_fsm_1;
          end 
        end
        _maxi_read_fsm_1: begin
          if((_maxi_read_rest_size <= 256) && ((_maxi_read_cur_global_addr & 4095) + (_maxi_read_rest_size << 2) >= 4096)) begin
            _maxi_read_cur_size <= 4096 - (_maxi_read_cur_global_addr & 4095) >> 2;
            _maxi_read_rest_size <= _maxi_read_rest_size - (4096 - (_maxi_read_cur_global_addr & 4095) >> 2);
          end else if(_maxi_read_rest_size <= 256) begin
            _maxi_read_cur_size <= _maxi_read_rest_size;
            _maxi_read_rest_size <= 0;
          end else if((_maxi_read_cur_global_addr & 4095) + 1024 >= 4096) begin
            _maxi_read_cur_size <= 4096 - (_maxi_read_cur_global_addr & 4095) >> 2;
            _maxi_read_rest_size <= _maxi_read_rest_size - (4096 - (_maxi_read_cur_global_addr & 4095) >> 2);
          end else begin
            _maxi_read_cur_size <= 256;
            _maxi_read_rest_size <= _maxi_read_rest_size - 256;
          end
          _maxi_read_fsm <= _maxi_read_fsm_2;
        end
        _maxi_read_fsm_2: begin
          if(maxi_arready || !maxi_arvalid) begin
            _maxi_read_fsm <= _maxi_read_fsm_3;
          end 
        end
        _maxi_read_fsm_3: begin
          __maxi_read_fsm_cond_3_0_1 <= 1;
          if(maxi_rready && maxi_rvalid && (_maxi_read_op_sel == 1)) begin
            _wdata_10 <= maxi_rdata;
            _wvalid_11 <= 1;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast) begin
            _maxi_read_cur_global_addr <= _maxi_read_cur_global_addr + (_maxi_read_cur_size << 2);
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_maxi_read_rest_size > 0)) begin
            _maxi_read_fsm <= _maxi_read_fsm_1;
          end 
          if(maxi_rready && maxi_rvalid && maxi_rlast && (_maxi_read_rest_size == 0)) begin
            _maxi_read_fsm <= _maxi_read_fsm_4;
          end 
        end
        _maxi_read_fsm_4: begin
          axim_flag_15 <= 1;
          __maxi_read_fsm_cond_4_1_1 <= 1;
          _maxi_read_fsm <= _maxi_read_fsm_5;
        end
        _maxi_read_fsm_5: begin
          _maxi_read_fsm <= _maxi_read_fsm_init;
        end
      endcase
    end
  end

  localparam _maxi_write_fsm_1 = 1;
  localparam _maxi_write_fsm_2 = 2;
  localparam _maxi_write_fsm_3 = 3;
  localparam _maxi_write_fsm_4 = 4;
  localparam _maxi_write_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_write_fsm <= _maxi_write_fsm_init;
      _d1__maxi_write_fsm <= _maxi_write_fsm_init;
      _maxi_write_cur_global_addr <= 0;
      _maxi_write_rest_size <= 0;
      _maxi_write_cur_size <= 0;
      axim_flag_31 <= 0;
      __maxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__maxi_write_fsm <= _maxi_write_fsm;
      case(_d1__maxi_write_fsm)
        _maxi_write_fsm_4: begin
          if(__maxi_write_fsm_cond_4_0_1) begin
            axim_flag_31 <= 0;
          end 
        end
      endcase
      case(_maxi_write_fsm)
        _maxi_write_fsm_init: begin
          if(_maxi_write_start) begin
            _maxi_write_cur_global_addr <= (_maxi_write_global_addr >> 2) << 2;
            _maxi_write_rest_size <= _maxi_write_size;
          end 
          if(_maxi_write_start && (_maxi_write_op_sel == 1)) begin
            _maxi_write_fsm <= _maxi_write_fsm_1;
          end 
        end
        _maxi_write_fsm_1: begin
          if((_maxi_write_rest_size <= 256) && ((_maxi_write_cur_global_addr & 4095) + (_maxi_write_rest_size << 2) >= 4096)) begin
            _maxi_write_cur_size <= 4096 - (_maxi_write_cur_global_addr & 4095) >> 2;
            _maxi_write_rest_size <= _maxi_write_rest_size - (4096 - (_maxi_write_cur_global_addr & 4095) >> 2);
          end else if(_maxi_write_rest_size <= 256) begin
            _maxi_write_cur_size <= _maxi_write_rest_size;
            _maxi_write_rest_size <= 0;
          end else if((_maxi_write_cur_global_addr & 4095) + 1024 >= 4096) begin
            _maxi_write_cur_size <= 4096 - (_maxi_write_cur_global_addr & 4095) >> 2;
            _maxi_write_rest_size <= _maxi_write_rest_size - (4096 - (_maxi_write_cur_global_addr & 4095) >> 2);
          end else begin
            _maxi_write_cur_size <= 256;
            _maxi_write_rest_size <= _maxi_write_rest_size - 256;
          end
          _maxi_write_fsm <= _maxi_write_fsm_2;
        end
        _maxi_write_fsm_2: begin
          if(maxi_awready || !maxi_awvalid) begin
            _maxi_write_fsm <= _maxi_write_fsm_3;
          end 
        end
        _maxi_write_fsm_3: begin
          if(_maxi_write_data_done) begin
            _maxi_write_cur_global_addr <= _maxi_write_cur_global_addr + (_maxi_write_cur_size << 2);
          end 
          if(_maxi_write_data_done && (_maxi_write_rest_size > 0)) begin
            _maxi_write_fsm <= _maxi_write_fsm_1;
          end 
          if(_maxi_write_data_done && (_maxi_write_rest_size == 0)) begin
            _maxi_write_fsm <= _maxi_write_fsm_4;
          end 
        end
        _maxi_write_fsm_4: begin
          axim_flag_31 <= 1;
          __maxi_write_fsm_cond_4_0_1 <= 1;
          _maxi_write_fsm <= _maxi_write_fsm_5;
        end
        _maxi_write_fsm_5: begin
          _maxi_write_fsm <= _maxi_write_fsm_init;
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
"""


def test():
    veriloggen.reset()
    test_module = thread_embedded_verilog_ipcore.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    # reformat due to embedded codes
    code_ast = parser.parse(code)
    code = codegen.visit(code_ast)

    assert(expected_code == code)
