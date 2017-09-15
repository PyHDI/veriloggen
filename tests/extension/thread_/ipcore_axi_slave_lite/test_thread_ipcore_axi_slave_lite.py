from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ipcore_axi_slave_lite

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
  reg [32-1:0] saxi_awaddr;
  reg saxi_awvalid;
  wire saxi_awready;
  reg [32-1:0] saxi_wdata;
  reg [4-1:0] saxi_wstrb;
  reg saxi_wvalid;
  wire saxi_wready;
  reg [32-1:0] saxi_araddr;
  reg saxi_arvalid;
  wire saxi_arready;
  wire [32-1:0] saxi_rdata;
  wire saxi_rvalid;
  reg saxi_rready;
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
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _saxi_awaddr;

  always @(*) begin
    saxi_awaddr = _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = _saxi_awvalid;

  always @(*) begin
    saxi_awvalid = _tmp_6;
  end

  assign _saxi_awready = saxi_awready;
  wire [32-1:0] _tmp_7;
  assign _tmp_7 = _saxi_wdata;

  always @(*) begin
    saxi_wdata = _tmp_7;
  end

  wire [4-1:0] _tmp_8;
  assign _tmp_8 = _saxi_wstrb;

  always @(*) begin
    saxi_wstrb = _tmp_8;
  end

  wire _tmp_9;
  assign _tmp_9 = _saxi_wvalid;

  always @(*) begin
    saxi_wvalid = _tmp_9;
  end

  assign _saxi_wready = saxi_wready;
  wire [32-1:0] _tmp_10;
  assign _tmp_10 = _saxi_araddr;

  always @(*) begin
    saxi_araddr = _tmp_10;
  end

  wire _tmp_11;
  assign _tmp_11 = _saxi_arvalid;

  always @(*) begin
    saxi_arvalid = _tmp_11;
  end

  assign _saxi_arready = saxi_arready;
  assign _saxi_rdata = saxi_rdata;
  assign _saxi_rvalid = saxi_rvalid;
  wire _tmp_12;
  assign _tmp_12 = _saxi_rready;

  always @(*) begin
    saxi_rready = _tmp_12;
  end

  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_10;
  reg signed [32-1:0] _th_ctrl_awaddr_11;
  reg __saxi_cond_0_1;
  reg __saxi_cond_1_1;
  reg signed [32-1:0] _th_ctrl_araddr_12;
  reg __saxi_cond_2_1;
  reg [32-1:0] _tmp_13;
  reg signed [32-1:0] _th_ctrl_v_13;
  reg __saxi_cond_3_1;
  reg [32-1:0] _tmp_14;
  reg __saxi_cond_4_1;
  assign _saxi_rready = (th_ctrl == 9) || (th_ctrl == 13) || (th_ctrl == 18);
  reg [32-1:0] _tmp_15;

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
    .myaxi_rready(myaxi_rready),
    .saxi_awaddr(saxi_awaddr),
    .saxi_awvalid(saxi_awvalid),
    .saxi_awready(saxi_awready),
    .saxi_wdata(saxi_wdata),
    .saxi_wstrb(saxi_wstrb),
    .saxi_wvalid(saxi_wvalid),
    .saxi_wready(saxi_wready),
    .saxi_araddr(saxi_araddr),
    .saxi_arvalid(saxi_arvalid),
    .saxi_arready(saxi_arready),
    .saxi_rdata(saxi_rdata),
    .saxi_rvalid(saxi_rvalid),
    .saxi_rready(saxi_rready)
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
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    _saxi_wdata = 0;
    _saxi_wstrb = 0;
    _saxi_wvalid = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_10 = 0;
    _th_ctrl_awaddr_11 = 0;
    __saxi_cond_0_1 = 0;
    __saxi_cond_1_1 = 0;
    _th_ctrl_araddr_12 = 0;
    __saxi_cond_2_1 = 0;
    _tmp_13 = 0;
    _th_ctrl_v_13 = 0;
    __saxi_cond_3_1 = 0;
    _tmp_14 = 0;
    __saxi_cond_4_1 = 0;
    _tmp_15 = 0;
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


  always @(posedge CLK) begin
    if(RST) begin
      _saxi_awaddr <= 0;
      _saxi_awvalid <= 0;
      __saxi_cond_0_1 <= 0;
      _saxi_wdata <= 0;
      _saxi_wvalid <= 0;
      _saxi_wstrb <= 0;
      __saxi_cond_1_1 <= 0;
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_2_1 <= 0;
      __saxi_cond_3_1 <= 0;
      __saxi_cond_4_1 <= 0;
    end else begin
      if(__saxi_cond_0_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_1_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_2_1) begin
        _saxi_arvalid <= 0;
      end 
      if(__saxi_cond_3_1) begin
        _saxi_arvalid <= 0;
      end 
      if(__saxi_cond_4_1) begin
        _saxi_arvalid <= 0;
      end 
      if((th_ctrl == 5) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_11;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 6) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 8) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_12;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
      if((th_ctrl == 12) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_12;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
      if((th_ctrl == 17) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_12;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
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

  always @(posedge CLK) begin
    if(RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_10 <= 0;
      _th_ctrl_awaddr_11 <= 0;
      _th_ctrl_araddr_12 <= 0;
      _tmp_13 <= 0;
      _th_ctrl_v_13 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_10 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_10 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_10 <= _th_ctrl_i_10 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_11 <= 0;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_6;
          end 
        end
        th_ctrl_6: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_7;
          end 
        end
        th_ctrl_7: begin
          _th_ctrl_araddr_12 <= 4;
          th_ctrl <= th_ctrl_8;
        end
        th_ctrl_8: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          if(_saxi_rready && _saxi_rvalid) begin
            _tmp_13 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_10;
          end 
        end
        th_ctrl_10: begin
          _th_ctrl_v_13 <= _tmp_13;
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          if(_th_ctrl_v_13 == 0) begin
            th_ctrl <= th_ctrl_12;
          end else begin
            th_ctrl <= th_ctrl_16;
          end
        end
        th_ctrl_12: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_13;
          end 
        end
        th_ctrl_13: begin
          if(_saxi_rready && _saxi_rvalid) begin
            _tmp_14 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_14;
          end 
        end
        th_ctrl_14: begin
          _th_ctrl_v_13 <= _tmp_14;
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_16: begin
          _th_ctrl_araddr_12 <= 8;
          th_ctrl <= th_ctrl_17;
        end
        th_ctrl_17: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_18;
          end 
        end
        th_ctrl_18: begin
          if(_saxi_rready && _saxi_rvalid) begin
            _tmp_15 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          _th_ctrl_v_13 <= _tmp_15;
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          if(_th_ctrl_v_13) begin
            th_ctrl <= th_ctrl_21;
          end else begin
            th_ctrl <= th_ctrl_23;
          end
        end
        th_ctrl_21: begin
          $display("SLAVE: ALL OK");
          th_ctrl <= th_ctrl_22;
        end
        th_ctrl_22: begin
          th_ctrl <= th_ctrl_24;
        end
        th_ctrl_23: begin
          $display("SLAVE: NOT ALL OK");
          th_ctrl <= th_ctrl_24;
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
  output myaxi_rready,
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

  reg [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg [32-1:0] _saxi_register_0;
  reg [32-1:0] _saxi_register_1;
  reg [32-1:0] _saxi_register_2;
  reg [32-1:0] _saxi_register_3;
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg [32-1:0] _saxi_resetval_0;
  reg [32-1:0] _saxi_resetval_1;
  reg [32-1:0] _saxi_resetval_2;
  reg [32-1:0] _saxi_resetval_3;
  localparam _saxi_maskwidth = 2;
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
  wire [32-1:0] _tmp_6;
  assign _tmp_6 = (_tmp_5 == 0)? _saxi_register_0 : 
                  (_tmp_5 == 1)? _saxi_register_1 : 
                  (_tmp_5 == 2)? _saxi_register_2 : 
                  (_tmp_5 == 3)? _saxi_register_3 : 'hx;
  wire _tmp_7;
  assign _tmp_7 = (_tmp_5 == 0)? _saxi_flag_0 : 
                  (_tmp_5 == 1)? _saxi_flag_1 : 
                  (_tmp_5 == 2)? _saxi_flag_2 : 
                  (_tmp_5 == 3)? _saxi_flag_3 : 'hx;
  wire [32-1:0] _tmp_8;
  assign _tmp_8 = (_tmp_5 == 0)? _saxi_resetval_0 : 
                  (_tmp_5 == 1)? _saxi_resetval_1 : 
                  (_tmp_5 == 2)? _saxi_resetval_2 : 
                  (_tmp_5 == 3)? _saxi_resetval_3 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg _tmp_9;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_offset_2;
  reg signed [32-1:0] _th_blink_size_3;
  reg signed [32-1:0] _th_blink_offset_4;
  reg signed [32-1:0] _th_blink_i_5;
  reg signed [32-1:0] _th_blink_wdata_6;
  reg _myram_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_7;
  reg signed [32-1:0] _th_blink_gaddr_8;
  reg [10-1:0] _tmp_10;
  reg [32-1:0] _tmp_11;
  reg [32-1:0] _tmp_12;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [32-1:0] _tmp_13;
  reg [33-1:0] _tmp_14;
  reg [33-1:0] _tmp_15;
  reg _tmp_16;
  reg _tmp_17;
  wire _tmp_18;
  wire _tmp_19;
  assign _tmp_19 = 1;
  localparam _tmp_20 = 1;
  wire [_tmp_20-1:0] _tmp_21;
  assign _tmp_21 = (_tmp_18 || !_tmp_16) && (_tmp_19 || !_tmp_17);
  reg [_tmp_20-1:0] __tmp_21_1;
  wire [32-1:0] _tmp_22;
  reg [32-1:0] __tmp_22_1;
  assign _tmp_22 = (__tmp_21_1)? myram_0_rdata : __tmp_22_1;
  reg _tmp_23;
  reg _tmp_24;
  reg _tmp_25;
  reg _tmp_26;
  reg [33-1:0] _tmp_27;
  reg [9-1:0] _tmp_28;
  reg _myaxi_cond_0_1;
  reg _tmp_29;
  wire [32-1:0] _tmp_data_30;
  wire _tmp_valid_30;
  wire _tmp_ready_30;
  assign _tmp_ready_30 = (_tmp_fsm_0 == 4) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  reg _tmp_31;
  reg [32-1:0] _d1__tmp_fsm_0;
  reg __tmp_fsm_0_cond_5_0_1;
  reg _myram_cond_1_1;
  reg [10-1:0] _tmp_32;
  reg [32-1:0] _tmp_33;
  reg [32-1:0] _tmp_34;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [32-1:0] _tmp_35;
  reg [33-1:0] _tmp_36;
  reg [33-1:0] _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  wire _tmp_40;
  wire _tmp_41;
  assign _tmp_41 = 1;
  localparam _tmp_42 = 1;
  wire [_tmp_42-1:0] _tmp_43;
  assign _tmp_43 = (_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39);
  reg [_tmp_42-1:0] __tmp_43_1;
  wire [32-1:0] _tmp_44;
  reg [32-1:0] __tmp_44_1;
  assign _tmp_44 = (__tmp_43_1)? myram_0_rdata : __tmp_44_1;
  reg _tmp_45;
  reg _tmp_46;
  reg _tmp_47;
  reg _tmp_48;
  reg [33-1:0] _tmp_49;
  reg [9-1:0] _tmp_50;
  reg _myaxi_cond_2_1;
  reg _tmp_51;
  wire [32-1:0] _tmp_data_52;
  wire _tmp_valid_52;
  wire _tmp_ready_52;
  assign _tmp_ready_52 = (_tmp_fsm_1 == 4) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg _tmp_53;
  reg [32-1:0] _d1__tmp_fsm_1;
  reg __tmp_fsm_1_cond_5_0_1;
  reg [10-1:0] _tmp_54;
  reg [32-1:0] _tmp_55;
  reg [32-1:0] _tmp_56;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [32-1:0] _tmp_57;
  reg [33-1:0] _tmp_58;
  reg [33-1:0] _tmp_59;
  reg [32-1:0] _tmp_60;
  reg _tmp_61;
  reg [33-1:0] _tmp_62;
  reg _tmp_63;
  wire [32-1:0] _tmp_data_64;
  wire _tmp_valid_64;
  wire _tmp_ready_64;
  assign _tmp_ready_64 = (_tmp_62 > 0) && !_tmp_63;
  reg _myram_cond_2_1;
  reg [9-1:0] _tmp_65;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _d1__tmp_fsm_2;
  reg __tmp_fsm_2_cond_4_0_1;
  reg _tmp_66;
  reg __tmp_fsm_2_cond_5_1_1;
  reg _tmp_67;
  reg _myram_cond_3_1;
  reg _myram_cond_4_1;
  reg _myram_cond_4_2;
  reg signed [32-1:0] _tmp_68;
  reg signed [32-1:0] _th_blink_rdata_9;
  reg [10-1:0] _tmp_69;
  reg [32-1:0] _tmp_70;
  reg [32-1:0] _tmp_71;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [32-1:0] _tmp_72;
  reg [33-1:0] _tmp_73;
  reg [33-1:0] _tmp_74;
  reg [32-1:0] _tmp_75;
  reg _tmp_76;
  reg [33-1:0] _tmp_77;
  reg _tmp_78;
  wire [32-1:0] _tmp_data_79;
  wire _tmp_valid_79;
  wire _tmp_ready_79;
  assign _tmp_ready_79 = (_tmp_77 > 0) && !_tmp_78;
  reg _myram_cond_5_1;
  reg [9-1:0] _tmp_80;
  reg _myaxi_cond_5_1;
  assign myaxi_rready = (_tmp_fsm_2 == 4) || (_tmp_fsm_3 == 4);
  reg [32-1:0] _d1__tmp_fsm_3;
  reg __tmp_fsm_3_cond_4_0_1;
  reg _tmp_81;
  reg __tmp_fsm_3_cond_5_1_1;
  reg _tmp_82;
  reg _myram_cond_6_1;
  reg _myram_cond_7_1;
  reg _myram_cond_7_2;
  reg signed [32-1:0] _tmp_83;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_28 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_29 <= 0;
      _myaxi_cond_1_1 <= 0;
      _tmp_50 <= 0;
      _myaxi_cond_2_1 <= 0;
      _tmp_51 <= 0;
      _myaxi_cond_3_1 <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_65 <= 0;
      _myaxi_cond_4_1 <= 0;
      _tmp_80 <= 0;
      _myaxi_cond_5_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_29 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_51 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_5_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_28 == 0))) begin
        myaxi_awaddr <= _tmp_13;
        myaxi_awlen <= _tmp_14 - 1;
        myaxi_awvalid <= 1;
        _tmp_28 <= _tmp_14;
      end 
      if((_tmp_fsm_0 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_28 == 0)) && (_tmp_14 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_30 && ((_tmp_fsm_0 == 4) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_28 > 0))) begin
        myaxi_wdata <= _tmp_data_30;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_28 <= _tmp_28 - 1;
      end 
      if(_tmp_valid_30 && ((_tmp_fsm_0 == 4) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_28 > 0)) && (_tmp_28 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_29 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_29 <= _tmp_29;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_50 == 0))) begin
        myaxi_awaddr <= _tmp_35;
        myaxi_awlen <= _tmp_36 - 1;
        myaxi_awvalid <= 1;
        _tmp_50 <= _tmp_36;
      end 
      if((_tmp_fsm_1 == 3) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_50 == 0)) && (_tmp_36 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_52 && ((_tmp_fsm_1 == 4) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_50 > 0))) begin
        myaxi_wdata <= _tmp_data_52;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_50 <= _tmp_50 - 1;
      end 
      if(_tmp_valid_52 && ((_tmp_fsm_1 == 4) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_50 > 0)) && (_tmp_50 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_51 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_51 <= _tmp_51;
      end 
      if((_tmp_fsm_2 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_65 == 0))) begin
        myaxi_araddr <= _tmp_57;
        myaxi_arlen <= _tmp_58 - 1;
        myaxi_arvalid <= 1;
        _tmp_65 <= _tmp_58;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_65 > 0)) begin
        _tmp_65 <= _tmp_65 - 1;
      end 
      if((_tmp_fsm_3 == 3) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_80 == 0))) begin
        myaxi_araddr <= _tmp_72;
        myaxi_arlen <= _tmp_73 - 1;
        myaxi_arvalid <= 1;
        _tmp_80 <= _tmp_73;
      end 
      _myaxi_cond_5_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_80 > 0)) begin
        _tmp_80 <= _tmp_80 - 1;
      end 
    end
  end

  assign _tmp_data_64 = _tmp_60;
  assign _tmp_valid_64 = _tmp_61;
  assign _tmp_data_79 = _tmp_75;
  assign _tmp_valid_79 = _tmp_76;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_0_1 <= 0;
      __tmp_21_1 <= 0;
      __tmp_22_1 <= 0;
      _tmp_26 <= 0;
      _tmp_16 <= 0;
      _tmp_17 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_23 <= 0;
      _tmp_27 <= 0;
      _myram_cond_1_1 <= 0;
      __tmp_43_1 <= 0;
      __tmp_44_1 <= 0;
      _tmp_48 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_45 <= 0;
      _tmp_49 <= 0;
      _tmp_62 <= 0;
      _tmp_63 <= 0;
      _myram_cond_2_1 <= 0;
      _myram_cond_3_1 <= 0;
      _tmp_67 <= 0;
      _myram_cond_4_1 <= 0;
      _myram_cond_4_2 <= 0;
      _tmp_77 <= 0;
      _tmp_78 <= 0;
      _myram_cond_5_1 <= 0;
      _myram_cond_6_1 <= 0;
      _tmp_82 <= 0;
      _myram_cond_7_1 <= 0;
      _myram_cond_7_2 <= 0;
    end else begin
      if(_myram_cond_4_2) begin
        _tmp_67 <= 0;
      end 
      if(_myram_cond_7_2) begin
        _tmp_82 <= 0;
      end 
      if(_myram_cond_0_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_1_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_2_1) begin
        myram_0_wenable <= 0;
        _tmp_63 <= 0;
      end 
      if(_myram_cond_3_1) begin
        _tmp_67 <= 1;
      end 
      _myram_cond_4_2 <= _myram_cond_4_1;
      if(_myram_cond_5_1) begin
        myram_0_wenable <= 0;
        _tmp_78 <= 0;
      end 
      if(_myram_cond_6_1) begin
        _tmp_82 <= 1;
      end 
      _myram_cond_7_2 <= _myram_cond_7_1;
      if(th_blink == 12) begin
        myram_0_addr <= _th_blink_i_5;
        myram_0_wdata <= _th_blink_wdata_6;
        myram_0_wenable <= 1;
      end 
      _myram_cond_0_1 <= th_blink == 12;
      __tmp_21_1 <= _tmp_21;
      __tmp_22_1 <= _tmp_22;
      if((_tmp_18 || !_tmp_16) && (_tmp_19 || !_tmp_17) && _tmp_24) begin
        _tmp_26 <= 0;
        _tmp_16 <= 0;
        _tmp_17 <= 0;
        _tmp_24 <= 0;
      end 
      if((_tmp_18 || !_tmp_16) && (_tmp_19 || !_tmp_17) && _tmp_23) begin
        _tmp_16 <= 1;
        _tmp_17 <= 1;
        _tmp_26 <= _tmp_25;
        _tmp_25 <= 0;
        _tmp_23 <= 0;
        _tmp_24 <= 1;
      end 
      if((_tmp_fsm_0 == 1) && (_tmp_27 == 0) && !_tmp_25 && !_tmp_26) begin
        myram_0_addr <= _tmp_10;
        _tmp_27 <= _tmp_12 - 1;
        _tmp_23 <= 1;
        _tmp_25 <= _tmp_12 == 1;
      end 
      if((_tmp_18 || !_tmp_16) && (_tmp_19 || !_tmp_17) && (_tmp_27 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        _tmp_27 <= _tmp_27 - 1;
        _tmp_23 <= 1;
        _tmp_25 <= 0;
      end 
      if((_tmp_18 || !_tmp_16) && (_tmp_19 || !_tmp_17) && (_tmp_27 == 1)) begin
        _tmp_25 <= 1;
      end 
      if(th_blink == 22) begin
        myram_0_addr <= _th_blink_i_5;
        myram_0_wdata <= _th_blink_wdata_6;
        myram_0_wenable <= 1;
      end 
      _myram_cond_1_1 <= th_blink == 22;
      __tmp_43_1 <= _tmp_43;
      __tmp_44_1 <= _tmp_44;
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && _tmp_46) begin
        _tmp_48 <= 0;
        _tmp_38 <= 0;
        _tmp_39 <= 0;
        _tmp_46 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && _tmp_45) begin
        _tmp_38 <= 1;
        _tmp_39 <= 1;
        _tmp_48 <= _tmp_47;
        _tmp_47 <= 0;
        _tmp_45 <= 0;
        _tmp_46 <= 1;
      end 
      if((_tmp_fsm_1 == 1) && (_tmp_49 == 0) && !_tmp_47 && !_tmp_48) begin
        myram_0_addr <= _tmp_32;
        _tmp_49 <= _tmp_34 - 1;
        _tmp_45 <= 1;
        _tmp_47 <= _tmp_34 == 1;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        _tmp_49 <= _tmp_49 - 1;
        _tmp_45 <= 1;
        _tmp_47 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 == 1)) begin
        _tmp_47 <= 1;
      end 
      if((_tmp_fsm_2 == 1) && (_tmp_62 == 0)) begin
        myram_0_addr <= _tmp_54 - 1;
        _tmp_62 <= _tmp_56;
      end 
      if(_tmp_valid_64 && ((_tmp_62 > 0) && !_tmp_63) && (_tmp_62 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _tmp_data_64;
        myram_0_wenable <= 1;
        _tmp_62 <= _tmp_62 - 1;
      end 
      if(_tmp_valid_64 && ((_tmp_62 > 0) && !_tmp_63) && (_tmp_62 == 1)) begin
        _tmp_63 <= 1;
      end 
      _myram_cond_2_1 <= 1;
      if(th_blink == 36) begin
        myram_0_addr <= _th_blink_i_5;
      end 
      _myram_cond_3_1 <= th_blink == 36;
      _myram_cond_4_1 <= th_blink == 36;
      if((_tmp_fsm_3 == 1) && (_tmp_77 == 0)) begin
        myram_0_addr <= _tmp_69 - 1;
        _tmp_77 <= _tmp_71;
      end 
      if(_tmp_valid_79 && ((_tmp_77 > 0) && !_tmp_78) && (_tmp_77 > 0)) begin
        myram_0_addr <= myram_0_addr + 1;
        myram_0_wdata <= _tmp_data_79;
        myram_0_wenable <= 1;
        _tmp_77 <= _tmp_77 - 1;
      end 
      if(_tmp_valid_79 && ((_tmp_77 > 0) && !_tmp_78) && (_tmp_77 == 1)) begin
        _tmp_78 <= 1;
      end 
      _myram_cond_5_1 <= 1;
      if(th_blink == 49) begin
        myram_0_addr <= _th_blink_i_5;
      end 
      _myram_cond_6_1 <= th_blink == 49;
      _myram_cond_7_1 <= th_blink == 49;
    end
  end

  assign _tmp_data_30 = _tmp_22;
  assign _tmp_valid_30 = _tmp_16;
  assign _tmp_18 = 1 && _tmp_ready_30;
  assign _tmp_data_52 = _tmp_44;
  assign _tmp_valid_52 = _tmp_38;
  assign _tmp_40 = 1 && _tmp_ready_52;

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
      _saxi_resetval_0 <= 0;
      _saxi_resetval_1 <= 0;
      _saxi_resetval_2 <= 0;
      _saxi_resetval_3 <= 0;
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
      if((_saxi_register_0 == 1) && (th_blink == 1) && (0 == 0)) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 1) && (0 == 1)) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 1) && (0 == 2)) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 1) && (0 == 3)) begin
        _saxi_register_3 <= 0;
      end 
      if((th_blink == 2) && (1 == 0)) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_blink == 2) && (1 == 1)) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_blink == 2) && (1 == 2)) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_blink == 2) && (1 == 3)) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_blink == 61) && (2 == 0)) begin
        _saxi_register_0 <= _tmp_9;
        _saxi_flag_0 <= 0;
      end 
      if((th_blink == 61) && (2 == 1)) begin
        _saxi_register_1 <= _tmp_9;
        _saxi_flag_1 <= 0;
      end 
      if((th_blink == 61) && (2 == 2)) begin
        _saxi_register_2 <= _tmp_9;
        _saxi_flag_2 <= 0;
      end 
      if((th_blink == 61) && (2 == 3)) begin
        _saxi_register_3 <= _tmp_9;
        _saxi_flag_3 <= 0;
      end 
      if((th_blink == 62) && (1 == 0)) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 1;
        _saxi_resetval_0 <= 0;
      end 
      if((th_blink == 62) && (1 == 1)) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 1;
        _saxi_resetval_1 <= 0;
      end 
      if((th_blink == 62) && (1 == 2)) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 1;
        _saxi_resetval_2 <= 0;
      end 
      if((th_blink == 62) && (1 == 3)) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 1;
        _saxi_resetval_3 <= 0;
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

  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;
  localparam th_blink_12 = 12;
  localparam th_blink_13 = 13;
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;
  localparam th_blink_26 = 26;
  localparam th_blink_27 = 27;
  localparam th_blink_28 = 28;
  localparam th_blink_29 = 29;
  localparam th_blink_30 = 30;
  localparam th_blink_31 = 31;
  localparam th_blink_32 = 32;
  localparam th_blink_33 = 33;
  localparam th_blink_34 = 34;
  localparam th_blink_35 = 35;
  localparam th_blink_36 = 36;
  localparam th_blink_37 = 37;
  localparam th_blink_38 = 38;
  localparam th_blink_39 = 39;
  localparam th_blink_40 = 40;
  localparam th_blink_41 = 41;
  localparam th_blink_42 = 42;
  localparam th_blink_43 = 43;
  localparam th_blink_44 = 44;
  localparam th_blink_45 = 45;
  localparam th_blink_46 = 46;
  localparam th_blink_47 = 47;
  localparam th_blink_48 = 48;
  localparam th_blink_49 = 49;
  localparam th_blink_50 = 50;
  localparam th_blink_51 = 51;
  localparam th_blink_52 = 52;
  localparam th_blink_53 = 53;
  localparam th_blink_54 = 54;
  localparam th_blink_55 = 55;
  localparam th_blink_56 = 56;
  localparam th_blink_57 = 57;
  localparam th_blink_58 = 58;
  localparam th_blink_59 = 59;
  localparam th_blink_60 = 60;
  localparam th_blink_61 = 61;
  localparam th_blink_62 = 62;
  localparam th_blink_63 = 63;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_9 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_offset_2 <= 0;
      _th_blink_size_3 <= 0;
      _th_blink_offset_4 <= 0;
      _th_blink_i_5 <= 0;
      _th_blink_wdata_6 <= 0;
      _th_blink_laddr_7 <= 0;
      _th_blink_gaddr_8 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_12 <= 0;
      _tmp_32 <= 0;
      _tmp_33 <= 0;
      _tmp_34 <= 0;
      _tmp_54 <= 0;
      _tmp_55 <= 0;
      _tmp_56 <= 0;
      _tmp_68 <= 0;
      _th_blink_rdata_9 <= 0;
      _tmp_69 <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_83 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 16;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          if(_saxi_register_0 == 1) begin
            th_blink <= th_blink_2;
          end 
        end
        th_blink_2: begin
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          _tmp_9 <= 1;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          if(_th_blink_i_1 < 4) begin
            th_blink <= th_blink_6;
          end else begin
            th_blink <= th_blink_57;
          end
        end
        th_blink_6: begin
          $display("# iter %d start", _th_blink_i_1);
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_offset_2 <= ((_th_blink_i_1 << 10) << 4) + 4092;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          _th_blink_size_3 <= _th_blink_size_0;
          _th_blink_offset_4 <= _th_blink_offset_2;
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_11;
          end else begin
            th_blink <= th_blink_14;
          end
        end
        th_blink_11: begin
          _th_blink_wdata_6 <= _th_blink_i_5 + 100;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_10;
        end
        th_blink_14: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          _th_blink_gaddr_8 <= _th_blink_offset_4;
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          _tmp_10 <= _th_blink_laddr_7;
          _tmp_11 <= _th_blink_gaddr_8;
          _tmp_12 <= _th_blink_size_3;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          if(_tmp_31) begin
            th_blink <= th_blink_18;
          end 
        end
        th_blink_18: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_21;
          end else begin
            th_blink <= th_blink_24;
          end
        end
        th_blink_21: begin
          _th_blink_wdata_6 <= _th_blink_i_5 + 1000;
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_20;
        end
        th_blink_24: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          _th_blink_gaddr_8 <= (_th_blink_size_3 + _th_blink_size_3 << 2) + _th_blink_offset_4;
          th_blink <= th_blink_26;
        end
        th_blink_26: begin
          _tmp_32 <= _th_blink_laddr_7;
          _tmp_33 <= _th_blink_gaddr_8;
          _tmp_34 <= _th_blink_size_3;
          th_blink <= th_blink_27;
        end
        th_blink_27: begin
          if(_tmp_53) begin
            th_blink <= th_blink_28;
          end 
        end
        th_blink_28: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_29;
        end
        th_blink_29: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_30;
        end
        th_blink_30: begin
          _th_blink_gaddr_8 <= _th_blink_offset_4;
          th_blink <= th_blink_31;
        end
        th_blink_31: begin
          _tmp_54 <= _th_blink_laddr_7;
          _tmp_55 <= _th_blink_gaddr_8;
          _tmp_56 <= _th_blink_size_3;
          th_blink <= th_blink_32;
        end
        th_blink_32: begin
          if(_tmp_66) begin
            th_blink <= th_blink_33;
          end 
        end
        th_blink_33: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_34;
        end
        th_blink_34: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_36;
          end else begin
            th_blink <= th_blink_42;
          end
        end
        th_blink_36: begin
          if(_tmp_67) begin
            _tmp_68 <= myram_0_rdata;
          end 
          if(_tmp_67) begin
            th_blink <= th_blink_37;
          end 
        end
        th_blink_37: begin
          _th_blink_rdata_9 <= _tmp_68;
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          if(_th_blink_rdata_9 !== _th_blink_i_5 + 100) begin
            th_blink <= th_blink_39;
          end else begin
            th_blink <= th_blink_41;
          end
        end
        th_blink_39: begin
          $display("rdata[%d] = %d", _th_blink_i_5, _th_blink_rdata_9);
          th_blink <= th_blink_40;
        end
        th_blink_40: begin
          _tmp_9 <= 0;
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_35;
        end
        th_blink_42: begin
          _th_blink_laddr_7 <= 0;
          th_blink <= th_blink_43;
        end
        th_blink_43: begin
          _th_blink_gaddr_8 <= (_th_blink_size_3 + _th_blink_size_3 << 2) + _th_blink_offset_4;
          th_blink <= th_blink_44;
        end
        th_blink_44: begin
          _tmp_69 <= _th_blink_laddr_7;
          _tmp_70 <= _th_blink_gaddr_8;
          _tmp_71 <= _th_blink_size_3;
          th_blink <= th_blink_45;
        end
        th_blink_45: begin
          if(_tmp_81) begin
            th_blink <= th_blink_46;
          end 
        end
        th_blink_46: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_7, _th_blink_gaddr_8);
          th_blink <= th_blink_47;
        end
        th_blink_47: begin
          _th_blink_i_5 <= 0;
          th_blink <= th_blink_48;
        end
        th_blink_48: begin
          if(_th_blink_i_5 < _th_blink_size_3) begin
            th_blink <= th_blink_49;
          end else begin
            th_blink <= th_blink_55;
          end
        end
        th_blink_49: begin
          if(_tmp_82) begin
            _tmp_83 <= myram_0_rdata;
          end 
          if(_tmp_82) begin
            th_blink <= th_blink_50;
          end 
        end
        th_blink_50: begin
          _th_blink_rdata_9 <= _tmp_83;
          th_blink <= th_blink_51;
        end
        th_blink_51: begin
          if(_th_blink_rdata_9 !== _th_blink_i_5 + 1000) begin
            th_blink <= th_blink_52;
          end else begin
            th_blink <= th_blink_54;
          end
        end
        th_blink_52: begin
          $display("rdata[%d] = %d", _th_blink_i_5, _th_blink_rdata_9);
          th_blink <= th_blink_53;
        end
        th_blink_53: begin
          _tmp_9 <= 0;
          th_blink <= th_blink_54;
        end
        th_blink_54: begin
          _th_blink_i_5 <= _th_blink_i_5 + 1;
          th_blink <= th_blink_48;
        end
        th_blink_55: begin
          $display("# iter %d end", _th_blink_i_1);
          th_blink <= th_blink_56;
        end
        th_blink_56: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_5;
        end
        th_blink_57: begin
          if(_tmp_9) begin
            th_blink <= th_blink_58;
          end else begin
            th_blink <= th_blink_60;
          end
        end
        th_blink_58: begin
          $display("ALL OK");
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          th_blink <= th_blink_61;
        end
        th_blink_60: begin
          $display("NOT ALL OK");
          th_blink <= th_blink_61;
        end
        th_blink_61: begin
          th_blink <= th_blink_62;
        end
        th_blink_62: begin
          th_blink <= th_blink_63;
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
      _tmp_13 <= 0;
      _tmp_15 <= 0;
      _tmp_14 <= 0;
      _tmp_31 <= 0;
      __tmp_fsm_0_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_0 <= _tmp_fsm_0;
      case(_d1__tmp_fsm_0)
        _tmp_fsm_0_5: begin
          if(__tmp_fsm_0_cond_5_0_1) begin
            _tmp_31 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_blink == 17) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          _tmp_13 <= (_tmp_11 >> 2) << 2;
          _tmp_15 <= _tmp_12;
          _tmp_fsm_0 <= _tmp_fsm_0_2;
        end
        _tmp_fsm_0_2: begin
          if((_tmp_15 <= 256) && ((_tmp_13 & 4095) + (_tmp_15 << 2) >= 4096)) begin
            _tmp_14 <= 4096 - (_tmp_13 & 4095) >> 2;
            _tmp_15 <= _tmp_15 - (4096 - (_tmp_13 & 4095) >> 2);
          end else if(_tmp_15 <= 256) begin
            _tmp_14 <= _tmp_15;
            _tmp_15 <= 0;
          end else if((_tmp_13 & 4095) + 1024 >= 4096) begin
            _tmp_14 <= 4096 - (_tmp_13 & 4095) >> 2;
            _tmp_15 <= _tmp_15 - (4096 - (_tmp_13 & 4095) >> 2);
          end else begin
            _tmp_14 <= 256;
            _tmp_15 <= _tmp_15 - 256;
          end
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_4;
          end 
        end
        _tmp_fsm_0_4: begin
          if(_tmp_29 && myaxi_wvalid && myaxi_wready) begin
            _tmp_13 <= _tmp_13 + (_tmp_14 << 2);
          end 
          if(_tmp_29 && myaxi_wvalid && myaxi_wready && (_tmp_15 > 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
          if(_tmp_29 && myaxi_wvalid && myaxi_wready && (_tmp_15 == 0)) begin
            _tmp_fsm_0 <= _tmp_fsm_0_5;
          end 
        end
        _tmp_fsm_0_5: begin
          _tmp_31 <= 1;
          __tmp_fsm_0_cond_5_0_1 <= 1;
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
      _tmp_35 <= 0;
      _tmp_37 <= 0;
      _tmp_36 <= 0;
      _tmp_53 <= 0;
      __tmp_fsm_1_cond_5_0_1 <= 0;
    end else begin
      _d1__tmp_fsm_1 <= _tmp_fsm_1;
      case(_d1__tmp_fsm_1)
        _tmp_fsm_1_5: begin
          if(__tmp_fsm_1_cond_5_0_1) begin
            _tmp_53 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_blink == 27) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          _tmp_35 <= (_tmp_33 >> 2) << 2;
          _tmp_37 <= _tmp_34;
          _tmp_fsm_1 <= _tmp_fsm_1_2;
        end
        _tmp_fsm_1_2: begin
          if((_tmp_37 <= 256) && ((_tmp_35 & 4095) + (_tmp_37 << 2) >= 4096)) begin
            _tmp_36 <= 4096 - (_tmp_35 & 4095) >> 2;
            _tmp_37 <= _tmp_37 - (4096 - (_tmp_35 & 4095) >> 2);
          end else if(_tmp_37 <= 256) begin
            _tmp_36 <= _tmp_37;
            _tmp_37 <= 0;
          end else if((_tmp_35 & 4095) + 1024 >= 4096) begin
            _tmp_36 <= 4096 - (_tmp_35 & 4095) >> 2;
            _tmp_37 <= _tmp_37 - (4096 - (_tmp_35 & 4095) >> 2);
          end else begin
            _tmp_36 <= 256;
            _tmp_37 <= _tmp_37 - 256;
          end
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_4;
          end 
        end
        _tmp_fsm_1_4: begin
          if(_tmp_51 && myaxi_wvalid && myaxi_wready) begin
            _tmp_35 <= _tmp_35 + (_tmp_36 << 2);
          end 
          if(_tmp_51 && myaxi_wvalid && myaxi_wready && (_tmp_37 > 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
          if(_tmp_51 && myaxi_wvalid && myaxi_wready && (_tmp_37 == 0)) begin
            _tmp_fsm_1 <= _tmp_fsm_1_5;
          end 
        end
        _tmp_fsm_1_5: begin
          _tmp_53 <= 1;
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
      _tmp_57 <= 0;
      _tmp_59 <= 0;
      _tmp_58 <= 0;
      __tmp_fsm_2_cond_4_0_1 <= 0;
      _tmp_61 <= 0;
      _tmp_60 <= 0;
      _tmp_66 <= 0;
      __tmp_fsm_2_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_2 <= _tmp_fsm_2;
      case(_d1__tmp_fsm_2)
        _tmp_fsm_2_4: begin
          if(__tmp_fsm_2_cond_4_0_1) begin
            _tmp_61 <= 0;
          end 
        end
        _tmp_fsm_2_5: begin
          if(__tmp_fsm_2_cond_5_1_1) begin
            _tmp_66 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_blink == 32) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          _tmp_57 <= (_tmp_55 >> 2) << 2;
          _tmp_59 <= _tmp_56;
          _tmp_fsm_2 <= _tmp_fsm_2_2;
        end
        _tmp_fsm_2_2: begin
          if((_tmp_59 <= 256) && ((_tmp_57 & 4095) + (_tmp_59 << 2) >= 4096)) begin
            _tmp_58 <= 4096 - (_tmp_57 & 4095) >> 2;
            _tmp_59 <= _tmp_59 - (4096 - (_tmp_57 & 4095) >> 2);
          end else if(_tmp_59 <= 256) begin
            _tmp_58 <= _tmp_59;
            _tmp_59 <= 0;
          end else if((_tmp_57 & 4095) + 1024 >= 4096) begin
            _tmp_58 <= 4096 - (_tmp_57 & 4095) >> 2;
            _tmp_59 <= _tmp_59 - (4096 - (_tmp_57 & 4095) >> 2);
          end else begin
            _tmp_58 <= 256;
            _tmp_59 <= _tmp_59 - 256;
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
            _tmp_60 <= myaxi_rdata;
            _tmp_61 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_57 <= _tmp_57 + (_tmp_58 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_59 > 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_59 == 0)) begin
            _tmp_fsm_2 <= _tmp_fsm_2_5;
          end 
        end
        _tmp_fsm_2_5: begin
          _tmp_66 <= 1;
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
      _tmp_72 <= 0;
      _tmp_74 <= 0;
      _tmp_73 <= 0;
      __tmp_fsm_3_cond_4_0_1 <= 0;
      _tmp_76 <= 0;
      _tmp_75 <= 0;
      _tmp_81 <= 0;
      __tmp_fsm_3_cond_5_1_1 <= 0;
    end else begin
      _d1__tmp_fsm_3 <= _tmp_fsm_3;
      case(_d1__tmp_fsm_3)
        _tmp_fsm_3_4: begin
          if(__tmp_fsm_3_cond_4_0_1) begin
            _tmp_76 <= 0;
          end 
        end
        _tmp_fsm_3_5: begin
          if(__tmp_fsm_3_cond_5_1_1) begin
            _tmp_81 <= 0;
          end 
        end
      endcase
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_blink == 45) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          _tmp_72 <= (_tmp_70 >> 2) << 2;
          _tmp_74 <= _tmp_71;
          _tmp_fsm_3 <= _tmp_fsm_3_2;
        end
        _tmp_fsm_3_2: begin
          if((_tmp_74 <= 256) && ((_tmp_72 & 4095) + (_tmp_74 << 2) >= 4096)) begin
            _tmp_73 <= 4096 - (_tmp_72 & 4095) >> 2;
            _tmp_74 <= _tmp_74 - (4096 - (_tmp_72 & 4095) >> 2);
          end else if(_tmp_74 <= 256) begin
            _tmp_73 <= _tmp_74;
            _tmp_74 <= 0;
          end else if((_tmp_72 & 4095) + 1024 >= 4096) begin
            _tmp_73 <= 4096 - (_tmp_72 & 4095) >> 2;
            _tmp_74 <= _tmp_74 - (4096 - (_tmp_72 & 4095) >> 2);
          end else begin
            _tmp_73 <= 256;
            _tmp_74 <= _tmp_74 - 256;
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
            _tmp_75 <= myaxi_rdata;
            _tmp_76 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _tmp_72 <= _tmp_72 + (_tmp_73 << 2);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_74 > 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_tmp_74 == 0)) begin
            _tmp_fsm_3 <= _tmp_fsm_3_5;
          end 
        end
        _tmp_fsm_3_5: begin
          _tmp_81 <= 1;
          __tmp_fsm_3_cond_5_1_1 <= 1;
          _tmp_fsm_3 <= _tmp_fsm_3_6;
        end
        _tmp_fsm_3_6: begin
          _tmp_fsm_3 <= _tmp_fsm_3_init;
        end
      endcase
    end
  end


endmodule



module myram
(
  input CLK,
  input [10-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_ipcore_axi_slave_lite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
