

module test
(

);

  reg CLK;
  reg RST;
  wire [32-1:0] maxi_awaddr;
  wire [8-1:0] maxi_awlen;
  wire [3-1:0] maxi_awsize;
  wire [2-1:0] maxi_awburst;
  wire [1-1:0] maxi_awlock;
  wire [4-1:0] maxi_awcache;
  wire [3-1:0] maxi_awprot;
  wire [4-1:0] maxi_awqos;
  wire [2-1:0] maxi_awuser;
  wire maxi_awvalid;
  reg maxi_awready;
  wire [32-1:0] maxi_wdata;
  wire [4-1:0] maxi_wstrb;
  wire maxi_wlast;
  wire maxi_wvalid;
  reg maxi_wready;
  reg [2-1:0] maxi_bresp;
  reg maxi_bvalid;
  wire maxi_bready;
  wire [32-1:0] maxi_araddr;
  wire [8-1:0] maxi_arlen;
  wire [3-1:0] maxi_arsize;
  wire [2-1:0] maxi_arburst;
  wire [1-1:0] maxi_arlock;
  wire [4-1:0] maxi_arcache;
  wire [3-1:0] maxi_arprot;
  wire [4-1:0] maxi_arqos;
  wire [2-1:0] maxi_aruser;
  wire maxi_arvalid;
  reg maxi_arready;
  reg [32-1:0] maxi_rdata;
  reg [2-1:0] maxi_rresp;
  reg maxi_rlast;
  reg maxi_rvalid;
  wire maxi_rready;
  reg [32-1:0] saxi_awaddr;
  reg [4-1:0] saxi_awcache;
  reg [3-1:0] saxi_awprot;
  reg saxi_awvalid;
  wire saxi_awready;
  reg [32-1:0] saxi_wdata;
  reg [4-1:0] saxi_wstrb;
  reg saxi_wvalid;
  wire saxi_wready;
  wire [2-1:0] saxi_bresp;
  wire saxi_bvalid;
  reg saxi_bready;
  reg [32-1:0] saxi_araddr;
  reg [4-1:0] saxi_arcache;
  reg [3-1:0] saxi_arprot;
  reg saxi_arvalid;
  wire saxi_arready;
  wire [32-1:0] saxi_rdata;
  wire [2-1:0] saxi_rresp;
  wire saxi_rvalid;
  reg saxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire [3-1:0] memory_awsize;
  wire [2-1:0] memory_awburst;
  wire [1-1:0] memory_awlock;
  wire [4-1:0] memory_awcache;
  wire [3-1:0] memory_awprot;
  wire [4-1:0] memory_awqos;
  wire [2-1:0] memory_awuser;
  wire memory_awvalid;
  reg memory_awready;
  wire [32-1:0] memory_wdata;
  wire [4-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [2-1:0] memory_bresp;
  reg memory_bvalid;
  wire memory_bready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire [3-1:0] memory_arsize;
  wire [2-1:0] memory_arburst;
  wire [1-1:0] memory_arlock;
  wire [4-1:0] memory_arcache;
  wire [3-1:0] memory_arprot;
  wire [4-1:0] memory_arqos;
  wire [2-1:0] memory_aruser;
  wire memory_arvalid;
  reg memory_arready;
  reg [32-1:0] memory_rdata;
  wire [2-1:0] memory_rresp;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  assign memory_bresp = 0;
  assign memory_rresp = 0;
  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("memimg_stream_matmul.out", _memory_mem);
  end

  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_count;
  reg [33-1:0] _sub_sleep_count;
  reg [32-1:0] _d1__memory_fsm;
  reg __memory_fsm_cond_100_0_1;
  reg __memory_fsm_cond_200_1_1;
  reg __memory_fsm_cond_211_2_1;
  assign memory_awaddr = maxi_awaddr;
  assign memory_awlen = maxi_awlen;
  assign memory_awsize = maxi_awsize;
  assign memory_awburst = maxi_awburst;
  assign memory_awlock = maxi_awlock;
  assign memory_awcache = maxi_awcache;
  assign memory_awprot = maxi_awprot;
  assign memory_awqos = maxi_awqos;
  assign memory_awuser = maxi_awuser;
  assign memory_awvalid = maxi_awvalid;
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    maxi_awready = _tmp_0;
  end

  assign memory_wdata = maxi_wdata;
  assign memory_wstrb = maxi_wstrb;
  assign memory_wlast = maxi_wlast;
  assign memory_wvalid = maxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    maxi_wready = _tmp_1;
  end

  wire [2-1:0] _tmp_2;
  assign _tmp_2 = memory_bresp;

  always @(*) begin
    maxi_bresp = _tmp_2;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_bvalid;

  always @(*) begin
    maxi_bvalid = _tmp_3;
  end

  assign memory_bready = maxi_bready;
  assign memory_araddr = maxi_araddr;
  assign memory_arlen = maxi_arlen;
  assign memory_arsize = maxi_arsize;
  assign memory_arburst = maxi_arburst;
  assign memory_arlock = maxi_arlock;
  assign memory_arcache = maxi_arcache;
  assign memory_arprot = maxi_arprot;
  assign memory_arqos = maxi_arqos;
  assign memory_aruser = maxi_aruser;
  assign memory_arvalid = maxi_arvalid;
  wire _tmp_4;
  assign _tmp_4 = memory_arready;

  always @(*) begin
    maxi_arready = _tmp_4;
  end

  wire [32-1:0] _tmp_5;
  assign _tmp_5 = memory_rdata;

  always @(*) begin
    maxi_rdata = _tmp_5;
  end

  wire [2-1:0] _tmp_6;
  assign _tmp_6 = memory_rresp;

  always @(*) begin
    maxi_rresp = _tmp_6;
  end

  wire _tmp_7;
  assign _tmp_7 = memory_rlast;

  always @(*) begin
    maxi_rlast = _tmp_7;
  end

  wire _tmp_8;
  assign _tmp_8 = memory_rvalid;

  always @(*) begin
    maxi_rvalid = _tmp_8;
  end

  assign memory_rready = maxi_rready;
  reg [32-1:0] _saxi_awaddr;
  wire [4-1:0] _saxi_awcache;
  wire [3-1:0] _saxi_awprot;
  reg _saxi_awvalid;
  wire _saxi_awready;
  reg [32-1:0] _saxi_wdata;
  reg [4-1:0] _saxi_wstrb;
  reg _saxi_wvalid;
  wire _saxi_wready;
  wire [2-1:0] _saxi_bresp;
  wire _saxi_bvalid;
  wire _saxi_bready;
  reg [32-1:0] _saxi_araddr;
  wire [4-1:0] _saxi_arcache;
  wire [3-1:0] _saxi_arprot;
  reg _saxi_arvalid;
  wire _saxi_arready;
  wire [32-1:0] _saxi_rdata;
  wire [2-1:0] _saxi_rresp;
  wire _saxi_rvalid;
  wire _saxi_rready;
  assign _saxi_awcache = 3;
  assign _saxi_awprot = 0;
  assign _saxi_bready = 1;
  assign _saxi_arcache = 3;
  assign _saxi_arprot = 0;
  reg [3-1:0] outstanding_wcount_9;
  wire [32-1:0] _tmp_10;
  assign _tmp_10 = _saxi_awaddr;

  always @(*) begin
    saxi_awaddr = _tmp_10;
  end

  wire [4-1:0] _tmp_11;
  assign _tmp_11 = _saxi_awcache;

  always @(*) begin
    saxi_awcache = _tmp_11;
  end

  wire [3-1:0] _tmp_12;
  assign _tmp_12 = _saxi_awprot;

  always @(*) begin
    saxi_awprot = _tmp_12;
  end

  wire _tmp_13;
  assign _tmp_13 = _saxi_awvalid;

  always @(*) begin
    saxi_awvalid = _tmp_13;
  end

  assign _saxi_awready = saxi_awready;
  wire [32-1:0] _tmp_14;
  assign _tmp_14 = _saxi_wdata;

  always @(*) begin
    saxi_wdata = _tmp_14;
  end

  wire [4-1:0] _tmp_15;
  assign _tmp_15 = _saxi_wstrb;

  always @(*) begin
    saxi_wstrb = _tmp_15;
  end

  wire _tmp_16;
  assign _tmp_16 = _saxi_wvalid;

  always @(*) begin
    saxi_wvalid = _tmp_16;
  end

  assign _saxi_wready = saxi_wready;
  assign _saxi_bresp = saxi_bresp;
  assign _saxi_bvalid = saxi_bvalid;
  wire _tmp_17;
  assign _tmp_17 = _saxi_bready;

  always @(*) begin
    saxi_bready = _tmp_17;
  end

  wire [32-1:0] _tmp_18;
  assign _tmp_18 = _saxi_araddr;

  always @(*) begin
    saxi_araddr = _tmp_18;
  end

  wire [4-1:0] _tmp_19;
  assign _tmp_19 = _saxi_arcache;

  always @(*) begin
    saxi_arcache = _tmp_19;
  end

  wire [3-1:0] _tmp_20;
  assign _tmp_20 = _saxi_arprot;

  always @(*) begin
    saxi_arprot = _tmp_20;
  end

  wire _tmp_21;
  assign _tmp_21 = _saxi_arvalid;

  always @(*) begin
    saxi_arvalid = _tmp_21;
  end

  assign _saxi_arready = saxi_arready;
  assign _saxi_rdata = saxi_rdata;
  assign _saxi_rresp = saxi_rresp;
  assign _saxi_rvalid = saxi_rvalid;
  wire _tmp_22;
  assign _tmp_22 = _saxi_rready;

  always @(*) begin
    saxi_rready = _tmp_22;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_15;
  reg signed [32-1:0] _th_ctrl_awaddr_16;
  reg __saxi_cond_0_1;
  reg __saxi_cond_1_1;
  reg __saxi_cond_2_1;
  reg __saxi_cond_3_1;
  reg __saxi_cond_4_1;
  reg __saxi_cond_5_1;
  reg __saxi_cond_6_1;
  reg __saxi_cond_7_1;
  reg signed [32-1:0] _th_ctrl_start_time_17;
  reg __saxi_cond_8_1;
  reg __saxi_cond_9_1;
  reg signed [32-1:0] _th_ctrl_araddr_18;
  reg __saxi_cond_10_1;
  reg signed [32-1:0] axim_rdata_23;
  assign _saxi_rready = th_ctrl == 34;
  reg signed [32-1:0] _th_ctrl_busy_19;
  reg signed [32-1:0] _th_ctrl_end_time_20;
  reg signed [32-1:0] _th_ctrl_time_21;
  reg signed [32-1:0] _th_ctrl_all_ok_22;
  reg signed [32-1:0] _th_ctrl_y_23;
  reg signed [32-1:0] _th_ctrl_x_24;
  reg signed [32-1:0] rdata_24;
  reg signed [32-1:0] _th_ctrl_v_25;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .maxi_awaddr(maxi_awaddr),
    .maxi_awlen(maxi_awlen),
    .maxi_awsize(maxi_awsize),
    .maxi_awburst(maxi_awburst),
    .maxi_awlock(maxi_awlock),
    .maxi_awcache(maxi_awcache),
    .maxi_awprot(maxi_awprot),
    .maxi_awqos(maxi_awqos),
    .maxi_awuser(maxi_awuser),
    .maxi_awvalid(maxi_awvalid),
    .maxi_awready(maxi_awready),
    .maxi_wdata(maxi_wdata),
    .maxi_wstrb(maxi_wstrb),
    .maxi_wlast(maxi_wlast),
    .maxi_wvalid(maxi_wvalid),
    .maxi_wready(maxi_wready),
    .maxi_bresp(maxi_bresp),
    .maxi_bvalid(maxi_bvalid),
    .maxi_bready(maxi_bready),
    .maxi_araddr(maxi_araddr),
    .maxi_arlen(maxi_arlen),
    .maxi_arsize(maxi_arsize),
    .maxi_arburst(maxi_arburst),
    .maxi_arlock(maxi_arlock),
    .maxi_arcache(maxi_arcache),
    .maxi_arprot(maxi_arprot),
    .maxi_arqos(maxi_arqos),
    .maxi_aruser(maxi_aruser),
    .maxi_arvalid(maxi_arvalid),
    .maxi_arready(maxi_arready),
    .maxi_rdata(maxi_rdata),
    .maxi_rresp(maxi_rresp),
    .maxi_rlast(maxi_rlast),
    .maxi_rvalid(maxi_rvalid),
    .maxi_rready(maxi_rready),
    .saxi_awaddr(saxi_awaddr),
    .saxi_awcache(saxi_awcache),
    .saxi_awprot(saxi_awprot),
    .saxi_awvalid(saxi_awvalid),
    .saxi_awready(saxi_awready),
    .saxi_wdata(saxi_wdata),
    .saxi_wstrb(saxi_wstrb),
    .saxi_wvalid(saxi_wvalid),
    .saxi_wready(saxi_wready),
    .saxi_bresp(saxi_bresp),
    .saxi_bvalid(saxi_bvalid),
    .saxi_bready(saxi_bready),
    .saxi_araddr(saxi_araddr),
    .saxi_arcache(saxi_arcache),
    .saxi_arprot(saxi_arprot),
    .saxi_arvalid(saxi_arvalid),
    .saxi_arready(saxi_arready),
    .saxi_rdata(saxi_rdata),
    .saxi_rresp(saxi_rresp),
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
    memory_bvalid = 0;
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
    _sub_sleep_count = 0;
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
    outstanding_wcount_9 = 0;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_15 = 0;
    _th_ctrl_awaddr_16 = 0;
    __saxi_cond_0_1 = 0;
    __saxi_cond_1_1 = 0;
    __saxi_cond_2_1 = 0;
    __saxi_cond_3_1 = 0;
    __saxi_cond_4_1 = 0;
    __saxi_cond_5_1 = 0;
    __saxi_cond_6_1 = 0;
    __saxi_cond_7_1 = 0;
    _th_ctrl_start_time_17 = 0;
    __saxi_cond_8_1 = 0;
    __saxi_cond_9_1 = 0;
    _th_ctrl_araddr_18 = 0;
    __saxi_cond_10_1 = 0;
    axim_rdata_23 = 0;
    _th_ctrl_busy_19 = 0;
    _th_ctrl_end_time_20 = 0;
    _th_ctrl_time_21 = 0;
    _th_ctrl_all_ok_22 = 0;
    _th_ctrl_y_23 = 0;
    _th_ctrl_x_24 = 0;
    rdata_24 = 0;
    _th_ctrl_v_25 = 0;
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
      memory_bvalid <= 0;
      _sub_sleep_count <= 0;
      _sleep_count <= 0;
    end else begin
      if(memory_bvalid && memory_bready) begin
        memory_bvalid <= 0;
      end 
      if(memory_wvalid && memory_wready && memory_wlast) begin
        memory_bvalid <= 1;
      end 
      if(_sleep_count == 3) begin
        _sub_sleep_count <= _sub_sleep_count + 1;
      end 
      if((_sleep_count == 3) && (_sub_sleep_count == 3)) begin
        _sub_sleep_count <= 0;
      end 
      if(_sleep_count < 3) begin
        _sleep_count <= _sleep_count + 1;
      end 
      if((_sub_sleep_count == 3) && (_sleep_count == 3)) begin
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
          if(memory_awvalid && !memory_bvalid) begin
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
      outstanding_wcount_9 <= 0;
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
      __saxi_cond_8_1 <= 0;
      __saxi_cond_9_1 <= 0;
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_10_1 <= 0;
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
        _saxi_awvalid <= 0;
      end 
      if(__saxi_cond_9_1) begin
        _saxi_wvalid <= 0;
      end 
      if(__saxi_cond_10_1) begin
        _saxi_arvalid <= 0;
      end 
      if(_saxi_wvalid && _saxi_wready && !(_saxi_bvalid && _saxi_bready) && (outstanding_wcount_9 < 7)) begin
        outstanding_wcount_9 <= outstanding_wcount_9 + 1;
      end 
      if(!(_saxi_wvalid && _saxi_wready) && (_saxi_bvalid && _saxi_bready) && (outstanding_wcount_9 > 0)) begin
        outstanding_wcount_9 <= outstanding_wcount_9 - 1;
      end 
      if((th_ctrl == 6) && ((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_16;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 8) && ((outstanding_wcount_9 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 16;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 11) && ((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_16;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 13) && ((outstanding_wcount_9 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 0;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 16) && ((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_16;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 18) && ((outstanding_wcount_9 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 4096;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_5_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 21) && ((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_16;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_6_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 23) && ((outstanding_wcount_9 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 8192;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_7_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 27) && ((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_16;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_8_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 29) && ((outstanding_wcount_9 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_9_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 32) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_18;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_10_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
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
  localparam th_ctrl_37 = 37;
  localparam th_ctrl_38 = 38;
  localparam th_ctrl_39 = 39;
  localparam th_ctrl_40 = 40;
  localparam th_ctrl_41 = 41;
  localparam th_ctrl_42 = 42;
  localparam th_ctrl_43 = 43;
  localparam th_ctrl_44 = 44;
  localparam th_ctrl_45 = 45;
  localparam th_ctrl_46 = 46;
  localparam th_ctrl_47 = 47;
  localparam th_ctrl_48 = 48;
  localparam th_ctrl_49 = 49;
  localparam th_ctrl_50 = 50;
  localparam th_ctrl_51 = 51;
  localparam th_ctrl_52 = 52;
  localparam th_ctrl_53 = 53;
  localparam th_ctrl_54 = 54;
  localparam th_ctrl_55 = 55;
  localparam th_ctrl_56 = 56;
  localparam th_ctrl_57 = 57;
  localparam th_ctrl_58 = 58;
  localparam th_ctrl_59 = 59;
  localparam th_ctrl_60 = 60;
  localparam th_ctrl_61 = 61;
  localparam th_ctrl_62 = 62;
  localparam th_ctrl_63 = 63;

  always @(posedge CLK) begin
    if(RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_15 <= 0;
      _th_ctrl_awaddr_16 <= 0;
      _th_ctrl_start_time_17 <= 0;
      _th_ctrl_araddr_18 <= 0;
      axim_rdata_23 <= 0;
      _th_ctrl_busy_19 <= 0;
      _th_ctrl_end_time_20 <= 0;
      _th_ctrl_time_21 <= 0;
      _th_ctrl_all_ok_22 <= 0;
      _th_ctrl_y_23 <= 0;
      _th_ctrl_x_24 <= 0;
      rdata_24 <= 0;
      _th_ctrl_v_25 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_15 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_15 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_15 <= _th_ctrl_i_15 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_16 <= 8;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          $display("# matrix_size = %d", 16);
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          if((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_7;
          end 
        end
        th_ctrl_7: begin
          th_ctrl <= th_ctrl_8;
        end
        th_ctrl_8: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          _th_ctrl_awaddr_16 <= 12;
          th_ctrl <= th_ctrl_10;
        end
        th_ctrl_10: begin
          $display("# a_offset = %d", 0);
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          if((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_12;
          end 
        end
        th_ctrl_12: begin
          th_ctrl <= th_ctrl_13;
        end
        th_ctrl_13: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_14;
          end 
        end
        th_ctrl_14: begin
          _th_ctrl_awaddr_16 <= 16;
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          $display("# b_offset = %d", 4096);
          th_ctrl <= th_ctrl_16;
        end
        th_ctrl_16: begin
          if((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_17;
          end 
        end
        th_ctrl_17: begin
          th_ctrl <= th_ctrl_18;
        end
        th_ctrl_18: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          _th_ctrl_awaddr_16 <= 20;
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          $display("# c_offset = %d", 8192);
          th_ctrl <= th_ctrl_21;
        end
        th_ctrl_21: begin
          if((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_22;
          end 
        end
        th_ctrl_22: begin
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_23: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_24;
          end 
        end
        th_ctrl_24: begin
          _th_ctrl_awaddr_16 <= 0;
          th_ctrl <= th_ctrl_25;
        end
        th_ctrl_25: begin
          _th_ctrl_start_time_17 <= counter;
          th_ctrl <= th_ctrl_26;
        end
        th_ctrl_26: begin
          $display("# start time = %d", _th_ctrl_start_time_17);
          th_ctrl <= th_ctrl_27;
        end
        th_ctrl_27: begin
          if((outstanding_wcount_9 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_28;
          end 
        end
        th_ctrl_28: begin
          th_ctrl <= th_ctrl_29;
        end
        th_ctrl_29: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_30;
          end 
        end
        th_ctrl_30: begin
          _th_ctrl_araddr_18 <= 4;
          th_ctrl <= th_ctrl_31;
        end
        th_ctrl_31: begin
          if(1) begin
            th_ctrl <= th_ctrl_32;
          end else begin
            th_ctrl <= th_ctrl_39;
          end
        end
        th_ctrl_32: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_33;
          end 
        end
        th_ctrl_33: begin
          th_ctrl <= th_ctrl_34;
        end
        th_ctrl_34: begin
          if(_saxi_rvalid) begin
            axim_rdata_23 <= _saxi_rdata;
          end 
          if(_saxi_rvalid) begin
            th_ctrl <= th_ctrl_35;
          end 
        end
        th_ctrl_35: begin
          _th_ctrl_busy_19 <= axim_rdata_23;
          th_ctrl <= th_ctrl_36;
        end
        th_ctrl_36: begin
          if(!_th_ctrl_busy_19) begin
            th_ctrl <= th_ctrl_37;
          end else begin
            th_ctrl <= th_ctrl_38;
          end
        end
        th_ctrl_37: begin
          th_ctrl <= th_ctrl_39;
        end
        th_ctrl_38: begin
          th_ctrl <= th_ctrl_31;
        end
        th_ctrl_39: begin
          _th_ctrl_end_time_20 <= counter;
          th_ctrl <= th_ctrl_40;
        end
        th_ctrl_40: begin
          $display("# end time = %d", _th_ctrl_end_time_20);
          th_ctrl <= th_ctrl_41;
        end
        th_ctrl_41: begin
          _th_ctrl_time_21 <= _th_ctrl_end_time_20 - _th_ctrl_start_time_17;
          th_ctrl <= th_ctrl_42;
        end
        th_ctrl_42: begin
          $display("# exec time = %d", _th_ctrl_time_21);
          th_ctrl <= th_ctrl_43;
        end
        th_ctrl_43: begin
          _th_ctrl_all_ok_22 <= 1;
          th_ctrl <= th_ctrl_44;
        end
        th_ctrl_44: begin
          _th_ctrl_y_23 <= 0;
          th_ctrl <= th_ctrl_45;
        end
        th_ctrl_45: begin
          if(_th_ctrl_y_23 < 16) begin
            th_ctrl <= th_ctrl_46;
          end else begin
            th_ctrl <= th_ctrl_58;
          end
        end
        th_ctrl_46: begin
          _th_ctrl_x_24 <= 0;
          th_ctrl <= th_ctrl_47;
        end
        th_ctrl_47: begin
          if(_th_ctrl_x_24 < 16) begin
            th_ctrl <= th_ctrl_48;
          end else begin
            th_ctrl <= th_ctrl_57;
          end
        end
        th_ctrl_48: begin
          if(th_ctrl == 48) begin
            rdata_24 <= { _memory_mem[8192 + (((_th_ctrl_y_23 << 4) + _th_ctrl_x_24 << 5) >>> 3) + 3], _memory_mem[8192 + (((_th_ctrl_y_23 << 4) + _th_ctrl_x_24 << 5) >>> 3) + 2], _memory_mem[8192 + (((_th_ctrl_y_23 << 4) + _th_ctrl_x_24 << 5) >>> 3) + 1], _memory_mem[8192 + (((_th_ctrl_y_23 << 4) + _th_ctrl_x_24 << 5) >>> 3) + 0] };
          end 
          th_ctrl <= th_ctrl_49;
        end
        th_ctrl_49: begin
          _th_ctrl_v_25 <= rdata_24;
          th_ctrl <= th_ctrl_50;
        end
        th_ctrl_50: begin
          if((_th_ctrl_y_23 == _th_ctrl_x_24) && (_th_ctrl_v_25 !== (_th_ctrl_y_23 + 1 << 1))) begin
            th_ctrl <= th_ctrl_51;
          end else begin
            th_ctrl <= th_ctrl_53;
          end
        end
        th_ctrl_51: begin
          _th_ctrl_all_ok_22 <= 0;
          th_ctrl <= th_ctrl_52;
        end
        th_ctrl_52: begin
          $display("NG [%d,%d] = %d", _th_ctrl_y_23, _th_ctrl_x_24, _th_ctrl_v_25);
          th_ctrl <= th_ctrl_53;
        end
        th_ctrl_53: begin
          if((_th_ctrl_y_23 != _th_ctrl_x_24) && (_th_ctrl_v_25 !== 0)) begin
            th_ctrl <= th_ctrl_54;
          end else begin
            th_ctrl <= th_ctrl_56;
          end
        end
        th_ctrl_54: begin
          _th_ctrl_all_ok_22 <= 0;
          th_ctrl <= th_ctrl_55;
        end
        th_ctrl_55: begin
          $display("NG [%d,%d] = %d", _th_ctrl_y_23, _th_ctrl_x_24, _th_ctrl_v_25);
          th_ctrl <= th_ctrl_56;
        end
        th_ctrl_56: begin
          _th_ctrl_x_24 <= _th_ctrl_x_24 + 1;
          th_ctrl <= th_ctrl_47;
        end
        th_ctrl_57: begin
          _th_ctrl_y_23 <= _th_ctrl_y_23 + 1;
          th_ctrl <= th_ctrl_45;
        end
        th_ctrl_58: begin
          if(_th_ctrl_all_ok_22) begin
            th_ctrl <= th_ctrl_59;
          end else begin
            th_ctrl <= th_ctrl_61;
          end
        end
        th_ctrl_59: begin
          $display("# verify: PASSED");
          th_ctrl <= th_ctrl_60;
        end
        th_ctrl_60: begin
          th_ctrl <= th_ctrl_62;
        end
        th_ctrl_61: begin
          $display("# verify: FAILED");
          th_ctrl <= th_ctrl_62;
        end
        th_ctrl_62: begin
          $finish;
          th_ctrl <= th_ctrl_63;
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [32-1:0] maxi_awaddr,
  output reg [8-1:0] maxi_awlen,
  output [3-1:0] maxi_awsize,
  output [2-1:0] maxi_awburst,
  output [1-1:0] maxi_awlock,
  output [4-1:0] maxi_awcache,
  output [3-1:0] maxi_awprot,
  output [4-1:0] maxi_awqos,
  output [2-1:0] maxi_awuser,
  output reg maxi_awvalid,
  input maxi_awready,
  output reg [32-1:0] maxi_wdata,
  output reg [4-1:0] maxi_wstrb,
  output reg maxi_wlast,
  output reg maxi_wvalid,
  input maxi_wready,
  input [2-1:0] maxi_bresp,
  input maxi_bvalid,
  output maxi_bready,
  output reg [32-1:0] maxi_araddr,
  output reg [8-1:0] maxi_arlen,
  output [3-1:0] maxi_arsize,
  output [2-1:0] maxi_arburst,
  output [1-1:0] maxi_arlock,
  output [4-1:0] maxi_arcache,
  output [3-1:0] maxi_arprot,
  output [4-1:0] maxi_arqos,
  output [2-1:0] maxi_aruser,
  output reg maxi_arvalid,
  input maxi_arready,
  input [32-1:0] maxi_rdata,
  input [2-1:0] maxi_rresp,
  input maxi_rlast,
  input maxi_rvalid,
  output maxi_rready,
  input [32-1:0] saxi_awaddr,
  input [4-1:0] saxi_awcache,
  input [3-1:0] saxi_awprot,
  input saxi_awvalid,
  output saxi_awready,
  input [32-1:0] saxi_wdata,
  input [4-1:0] saxi_wstrb,
  input saxi_wvalid,
  output saxi_wready,
  output [2-1:0] saxi_bresp,
  output reg saxi_bvalid,
  input saxi_bready,
  input [32-1:0] saxi_araddr,
  input [4-1:0] saxi_arcache,
  input [3-1:0] saxi_arprot,
  input saxi_arvalid,
  output saxi_arready,
  output reg [32-1:0] saxi_rdata,
  output [2-1:0] saxi_rresp,
  output reg saxi_rvalid,
  input saxi_rready
);

  wire [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  wire [32-1:0] ram_a_0_wdata;
  wire ram_a_0_wenable;
  wire ram_a_0_enable;

  ram_a
  inst_ram_a
  (
    .CLK(CLK),
    .ram_a_0_addr(ram_a_0_addr),
    .ram_a_0_rdata(ram_a_0_rdata),
    .ram_a_0_wdata(ram_a_0_wdata),
    .ram_a_0_wenable(ram_a_0_wenable),
    .ram_a_0_enable(ram_a_0_enable)
  );

  wire [10-1:0] ram_b_0_addr;
  wire [32-1:0] ram_b_0_rdata;
  wire [32-1:0] ram_b_0_wdata;
  wire ram_b_0_wenable;
  wire ram_b_0_enable;

  ram_b
  inst_ram_b
  (
    .CLK(CLK),
    .ram_b_0_addr(ram_b_0_addr),
    .ram_b_0_rdata(ram_b_0_rdata),
    .ram_b_0_wdata(ram_b_0_wdata),
    .ram_b_0_wenable(ram_b_0_wenable),
    .ram_b_0_enable(ram_b_0_enable)
  );

  wire [10-1:0] ram_c_0_addr;
  wire [32-1:0] ram_c_0_rdata;
  wire [32-1:0] ram_c_0_wdata;
  wire ram_c_0_wenable;
  wire ram_c_0_enable;

  ram_c
  inst_ram_c
  (
    .CLK(CLK),
    .ram_c_0_addr(ram_c_0_addr),
    .ram_c_0_rdata(ram_c_0_rdata),
    .ram_c_0_wdata(ram_c_0_wdata),
    .ram_c_0_wenable(ram_c_0_wenable),
    .ram_c_0_enable(ram_c_0_enable)
  );

  assign maxi_awsize = 2;
  assign maxi_awburst = 1;
  assign maxi_awlock = 0;
  assign maxi_awcache = 3;
  assign maxi_awprot = 0;
  assign maxi_awqos = 0;
  assign maxi_awuser = 0;
  assign maxi_bready = 1;
  assign maxi_arsize = 2;
  assign maxi_arburst = 1;
  assign maxi_arlock = 0;
  assign maxi_arcache = 3;
  assign maxi_arprot = 0;
  assign maxi_arqos = 0;
  assign maxi_aruser = 0;
  reg [3-1:0] outstanding_wcount_0;
  reg _maxi_read_start;
  reg [8-1:0] _maxi_read_op_sel;
  reg [32-1:0] _maxi_read_global_addr;
  reg [33-1:0] _maxi_read_global_size;
  reg [32-1:0] _maxi_read_local_addr;
  reg [32-1:0] _maxi_read_local_stride;
  reg [33-1:0] _maxi_read_local_size;
  wire _maxi_read_req_fifo_enq;
  wire [105-1:0] _maxi_read_req_fifo_wdata;
  wire _maxi_read_req_fifo_full;
  wire _maxi_read_req_fifo_almost_full;
  wire _maxi_read_req_fifo_deq;
  wire [105-1:0] _maxi_read_req_fifo_rdata;
  wire _maxi_read_req_fifo_empty;
  wire _maxi_read_req_fifo_almost_empty;

  _maxi_read_req_fifo
  inst__maxi_read_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._maxi_read_req_fifo_enq(_maxi_read_req_fifo_enq),
    ._maxi_read_req_fifo_wdata(_maxi_read_req_fifo_wdata),
    ._maxi_read_req_fifo_full(_maxi_read_req_fifo_full),
    ._maxi_read_req_fifo_almost_full(_maxi_read_req_fifo_almost_full),
    ._maxi_read_req_fifo_deq(_maxi_read_req_fifo_deq),
    ._maxi_read_req_fifo_rdata(_maxi_read_req_fifo_rdata),
    ._maxi_read_req_fifo_empty(_maxi_read_req_fifo_empty),
    ._maxi_read_req_fifo_almost_empty(_maxi_read_req_fifo_almost_empty)
  );

  reg [4-1:0] count__maxi_read_req_fifo;
  wire [8-1:0] _maxi_read_op_sel_fifo;
  wire [32-1:0] _maxi_read_local_addr_fifo;
  wire [32-1:0] _maxi_read_local_stride_fifo;
  wire [33-1:0] _maxi_read_local_size_fifo;
  wire [8-1:0] unpack_read_req_op_sel_1;
  wire [32-1:0] unpack_read_req_local_addr_2;
  wire [32-1:0] unpack_read_req_local_stride_3;
  wire [33-1:0] unpack_read_req_local_size_4;
  assign unpack_read_req_op_sel_1 = _maxi_read_req_fifo_rdata[104:97];
  assign unpack_read_req_local_addr_2 = _maxi_read_req_fifo_rdata[96:65];
  assign unpack_read_req_local_stride_3 = _maxi_read_req_fifo_rdata[64:33];
  assign unpack_read_req_local_size_4 = _maxi_read_req_fifo_rdata[32:0];
  assign _maxi_read_op_sel_fifo = unpack_read_req_op_sel_1;
  assign _maxi_read_local_addr_fifo = unpack_read_req_local_addr_2;
  assign _maxi_read_local_stride_fifo = unpack_read_req_local_stride_3;
  assign _maxi_read_local_size_fifo = unpack_read_req_local_size_4;
  reg [8-1:0] _maxi_read_op_sel_buf;
  reg [32-1:0] _maxi_read_local_addr_buf;
  reg [32-1:0] _maxi_read_local_stride_buf;
  reg [33-1:0] _maxi_read_local_size_buf;
  reg _maxi_read_req_idle;
  reg _maxi_read_data_idle;
  wire _maxi_read_idle;
  assign _maxi_read_idle = !_maxi_read_start && _maxi_read_req_idle && _maxi_read_req_fifo_empty && _maxi_read_data_idle;
  reg _maxi_write_start;
  reg [8-1:0] _maxi_write_op_sel;
  reg [32-1:0] _maxi_write_global_addr;
  reg [33-1:0] _maxi_write_global_size;
  reg [32-1:0] _maxi_write_local_addr;
  reg [32-1:0] _maxi_write_local_stride;
  reg [33-1:0] _maxi_write_local_size;
  wire _maxi_write_req_fifo_enq;
  wire [105-1:0] _maxi_write_req_fifo_wdata;
  wire _maxi_write_req_fifo_full;
  wire _maxi_write_req_fifo_almost_full;
  wire _maxi_write_req_fifo_deq;
  wire [105-1:0] _maxi_write_req_fifo_rdata;
  wire _maxi_write_req_fifo_empty;
  wire _maxi_write_req_fifo_almost_empty;

  _maxi_write_req_fifo
  inst__maxi_write_req_fifo
  (
    .CLK(CLK),
    .RST(RST),
    ._maxi_write_req_fifo_enq(_maxi_write_req_fifo_enq),
    ._maxi_write_req_fifo_wdata(_maxi_write_req_fifo_wdata),
    ._maxi_write_req_fifo_full(_maxi_write_req_fifo_full),
    ._maxi_write_req_fifo_almost_full(_maxi_write_req_fifo_almost_full),
    ._maxi_write_req_fifo_deq(_maxi_write_req_fifo_deq),
    ._maxi_write_req_fifo_rdata(_maxi_write_req_fifo_rdata),
    ._maxi_write_req_fifo_empty(_maxi_write_req_fifo_empty),
    ._maxi_write_req_fifo_almost_empty(_maxi_write_req_fifo_almost_empty)
  );

  reg [4-1:0] count__maxi_write_req_fifo;
  wire [8-1:0] _maxi_write_op_sel_fifo;
  wire [32-1:0] _maxi_write_local_addr_fifo;
  wire [32-1:0] _maxi_write_local_stride_fifo;
  wire [33-1:0] _maxi_write_size_fifo;
  wire [8-1:0] unpack_write_req_op_sel_5;
  wire [32-1:0] unpack_write_req_local_addr_6;
  wire [32-1:0] unpack_write_req_local_stride_7;
  wire [33-1:0] unpack_write_req_size_8;
  assign unpack_write_req_op_sel_5 = _maxi_write_req_fifo_rdata[104:97];
  assign unpack_write_req_local_addr_6 = _maxi_write_req_fifo_rdata[96:65];
  assign unpack_write_req_local_stride_7 = _maxi_write_req_fifo_rdata[64:33];
  assign unpack_write_req_size_8 = _maxi_write_req_fifo_rdata[32:0];
  assign _maxi_write_op_sel_fifo = unpack_write_req_op_sel_5;
  assign _maxi_write_local_addr_fifo = unpack_write_req_local_addr_6;
  assign _maxi_write_local_stride_fifo = unpack_write_req_local_stride_7;
  assign _maxi_write_size_fifo = unpack_write_req_size_8;
  reg [8-1:0] _maxi_write_op_sel_buf;
  reg [32-1:0] _maxi_write_local_addr_buf;
  reg [32-1:0] _maxi_write_local_stride_buf;
  reg [33-1:0] _maxi_write_size_buf;
  reg _maxi_write_req_idle;
  reg _maxi_write_data_idle;
  wire _maxi_write_idle;
  assign _maxi_write_idle = !_maxi_write_start && _maxi_write_req_idle && _maxi_write_req_fifo_empty && _maxi_write_data_idle;
  assign saxi_bresp = 0;
  assign saxi_rresp = 0;
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
  reg [32-1:0] addr_9;
  reg writevalid_10;
  reg readvalid_11;
  reg prev_awvalid_12;
  reg prev_arvalid_13;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_10 && !readvalid_11 && !saxi_bvalid && prev_awvalid_12);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_11 && !writevalid_10 && prev_arvalid_13 && !prev_awvalid_12);
  reg [_saxi_maskwidth-1:0] axis_maskaddr_14;
  wire signed [32-1:0] axislite_rdata_15;
  assign axislite_rdata_15 = (axis_maskaddr_14 == 0)? _saxi_register_0 : 
                             (axis_maskaddr_14 == 1)? _saxi_register_1 : 
                             (axis_maskaddr_14 == 2)? _saxi_register_2 : 
                             (axis_maskaddr_14 == 3)? _saxi_register_3 : 
                             (axis_maskaddr_14 == 4)? _saxi_register_4 : 
                             (axis_maskaddr_14 == 5)? _saxi_register_5 : 
                             (axis_maskaddr_14 == 6)? _saxi_register_6 : 
                             (axis_maskaddr_14 == 7)? _saxi_register_7 : 'hx;
  wire axislite_flag_16;
  assign axislite_flag_16 = (axis_maskaddr_14 == 0)? _saxi_flag_0 : 
                            (axis_maskaddr_14 == 1)? _saxi_flag_1 : 
                            (axis_maskaddr_14 == 2)? _saxi_flag_2 : 
                            (axis_maskaddr_14 == 3)? _saxi_flag_3 : 
                            (axis_maskaddr_14 == 4)? _saxi_flag_4 : 
                            (axis_maskaddr_14 == 5)? _saxi_flag_5 : 
                            (axis_maskaddr_14 == 6)? _saxi_flag_6 : 
                            (axis_maskaddr_14 == 7)? _saxi_flag_7 : 'hx;
  wire signed [32-1:0] axislite_resetval_17;
  assign axislite_resetval_17 = (axis_maskaddr_14 == 0)? _saxi_resetval_0 : 
                                (axis_maskaddr_14 == 1)? _saxi_resetval_1 : 
                                (axis_maskaddr_14 == 2)? _saxi_resetval_2 : 
                                (axis_maskaddr_14 == 3)? _saxi_resetval_3 : 
                                (axis_maskaddr_14 == 4)? _saxi_resetval_4 : 
                                (axis_maskaddr_14 == 5)? _saxi_resetval_5 : 
                                (axis_maskaddr_14 == 6)? _saxi_resetval_6 : 
                                (axis_maskaddr_14 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg _strm_madd_stream_ivalid;
  wire _strm_madd_stream_oready;
  wire _strm_madd_stream_internal_oready;
  assign _strm_madd_stream_internal_oready = 1;
  assign _strm_madd_stream_oready = _strm_madd_stream_internal_oready;
  reg [32-1:0] _strm_madd_fsm;
  localparam _strm_madd_fsm_init = 0;
  wire _strm_madd_run_flag;
  reg _strm_madd_source_start;
  wire _strm_madd_source_stop;
  reg _strm_madd_source_busy;
  wire _strm_madd_sink_start;
  wire _strm_madd_sink_stop;
  wire _strm_madd_sink_busy;
  wire _strm_madd_busy;
  reg _strm_madd_busy_reg;
  wire _strm_madd_is_root;
  assign _strm_madd_is_root = 1;
  reg _strm_madd_a_idle;
  reg [33-1:0] _strm_madd_a_source_count;
  reg [5-1:0] _strm_madd_a_source_mode;
  reg [16-1:0] _strm_madd_a_source_generator_id;
  reg [32-1:0] _strm_madd_a_source_offset;
  reg [33-1:0] _strm_madd_a_source_size;
  reg [32-1:0] _strm_madd_a_source_stride;
  reg [32-1:0] _strm_madd_a_source_offset_buf;
  reg [33-1:0] _strm_madd_a_source_size_buf;
  reg [32-1:0] _strm_madd_a_source_stride_buf;
  reg [8-1:0] _strm_madd_a_source_sel;
  reg [32-1:0] _strm_madd_a_source_ram_raddr;
  reg _strm_madd_a_source_ram_renable;
  wire [32-1:0] _strm_madd_a_source_ram_rdata;
  reg _strm_madd_a_source_fifo_deq;
  wire [32-1:0] _strm_madd_a_source_fifo_rdata;
  reg [32-1:0] _strm_madd_a_source_empty_data;
  reg _strm_madd_b_idle;
  reg [33-1:0] _strm_madd_b_source_count;
  reg [5-1:0] _strm_madd_b_source_mode;
  reg [16-1:0] _strm_madd_b_source_generator_id;
  reg [32-1:0] _strm_madd_b_source_offset;
  reg [33-1:0] _strm_madd_b_source_size;
  reg [32-1:0] _strm_madd_b_source_stride;
  reg [32-1:0] _strm_madd_b_source_offset_buf;
  reg [33-1:0] _strm_madd_b_source_size_buf;
  reg [32-1:0] _strm_madd_b_source_stride_buf;
  reg [8-1:0] _strm_madd_b_source_sel;
  reg [32-1:0] _strm_madd_b_source_ram_raddr;
  reg _strm_madd_b_source_ram_renable;
  wire [32-1:0] _strm_madd_b_source_ram_rdata;
  reg _strm_madd_b_source_fifo_deq;
  wire [32-1:0] _strm_madd_b_source_fifo_rdata;
  reg [32-1:0] _strm_madd_b_source_empty_data;
  reg [32-1:0] _strm_madd_size_next_parameter_data;
  reg [33-1:0] _strm_madd_sum_sink_count;
  reg [5-1:0] _strm_madd_sum_sink_mode;
  reg [16-1:0] _strm_madd_sum_sink_generator_id;
  reg [32-1:0] _strm_madd_sum_sink_offset;
  reg [33-1:0] _strm_madd_sum_sink_size;
  reg [32-1:0] _strm_madd_sum_sink_stride;
  reg [32-1:0] _strm_madd_sum_sink_offset_buf;
  reg [33-1:0] _strm_madd_sum_sink_size_buf;
  reg [32-1:0] _strm_madd_sum_sink_stride_buf;
  reg [8-1:0] _strm_madd_sum_sink_sel;
  reg [32-1:0] _strm_madd_sum_sink_waddr;
  reg _strm_madd_sum_sink_wenable;
  reg [32-1:0] _strm_madd_sum_sink_wdata;
  reg _strm_madd_sum_sink_fifo_enq;
  reg [32-1:0] _strm_madd_sum_sink_fifo_wdata;
  reg [32-1:0] _strm_madd_sum_sink_immediate;
  reg [33-1:0] _strm_madd_sum_valid_sink_count;
  reg [5-1:0] _strm_madd_sum_valid_sink_mode;
  reg [16-1:0] _strm_madd_sum_valid_sink_generator_id;
  reg [32-1:0] _strm_madd_sum_valid_sink_offset;
  reg [33-1:0] _strm_madd_sum_valid_sink_size;
  reg [32-1:0] _strm_madd_sum_valid_sink_stride;
  reg [32-1:0] _strm_madd_sum_valid_sink_offset_buf;
  reg [33-1:0] _strm_madd_sum_valid_sink_size_buf;
  reg [32-1:0] _strm_madd_sum_valid_sink_stride_buf;
  reg [8-1:0] _strm_madd_sum_valid_sink_sel;
  reg [32-1:0] _strm_madd_sum_valid_sink_waddr;
  reg _strm_madd_sum_valid_sink_wenable;
  reg [1-1:0] _strm_madd_sum_valid_sink_wdata;
  reg _strm_madd_sum_valid_sink_fifo_enq;
  reg [1-1:0] _strm_madd_sum_valid_sink_fifo_wdata;
  reg [1-1:0] _strm_madd_sum_valid_sink_immediate;
  reg [32-1:0] th_matmul;
  localparam th_matmul_init = 0;
  reg signed [32-1:0] _th_matmul_matrix_size_0;
  reg signed [32-1:0] _th_matmul_a_offset_1;
  reg signed [32-1:0] _th_matmul_b_offset_2;
  reg signed [32-1:0] _th_matmul_c_offset_3;
  reg signed [32-1:0] _th_matmul_matrix_size_4;
  reg signed [32-1:0] _th_matmul_a_offset_5;
  reg signed [32-1:0] _th_matmul_b_offset_6;
  reg signed [32-1:0] _th_matmul_c_offset_7;
  reg signed [32-1:0] _th_matmul_a_addr_8;
  reg signed [32-1:0] _th_matmul_c_addr_9;
  reg signed [32-1:0] _th_matmul_i_10;
  wire [32-1:0] mask_addr_shifted_18;
  assign mask_addr_shifted_18 = _th_matmul_a_addr_8 >> 2;
  wire [32-1:0] mask_addr_masked_19;
  assign mask_addr_masked_19 = mask_addr_shifted_18 << 2;
  reg [32-1:0] _maxi_read_req_fsm;
  localparam _maxi_read_req_fsm_init = 0;
  reg [33-1:0] _maxi_read_cur_global_size;
  reg _maxi_read_cont;
  wire [8-1:0] pack_read_req_op_sel_20;
  wire [32-1:0] pack_read_req_local_addr_21;
  wire [32-1:0] pack_read_req_local_stride_22;
  wire [33-1:0] pack_read_req_local_size_23;
  assign pack_read_req_op_sel_20 = _maxi_read_op_sel;
  assign pack_read_req_local_addr_21 = _maxi_read_local_addr;
  assign pack_read_req_local_stride_22 = _maxi_read_local_stride;
  assign pack_read_req_local_size_23 = _maxi_read_local_size;
  wire [105-1:0] pack_read_req_packed_24;
  assign pack_read_req_packed_24 = { pack_read_req_op_sel_20, pack_read_req_local_addr_21, pack_read_req_local_stride_22, pack_read_req_local_size_23 };
  assign _maxi_read_req_fifo_wdata = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? pack_read_req_packed_24 : 'hx;
  assign _maxi_read_req_fifo_enq = ((_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full)? (_maxi_read_req_fsm == 0) && _maxi_read_start && !_maxi_read_req_fifo_almost_full && !_maxi_read_req_fifo_almost_full : 0;
  localparam _tmp_25 = 1;
  wire [_tmp_25-1:0] _tmp_26;
  assign _tmp_26 = !_maxi_read_req_fifo_almost_full;
  reg [_tmp_25-1:0] __tmp_26_1;
  wire [32-1:0] mask_addr_shifted_27;
  assign mask_addr_shifted_27 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_28;
  assign mask_addr_masked_28 = mask_addr_shifted_27 << 2;
  wire [32-1:0] mask_addr_shifted_29;
  assign mask_addr_shifted_29 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_30;
  assign mask_addr_masked_30 = mask_addr_shifted_29 << 2;
  wire [32-1:0] mask_addr_shifted_31;
  assign mask_addr_shifted_31 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_32;
  assign mask_addr_masked_32 = mask_addr_shifted_31 << 2;
  wire [32-1:0] mask_addr_shifted_33;
  assign mask_addr_shifted_33 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_34;
  assign mask_addr_masked_34 = mask_addr_shifted_33 << 2;
  wire [32-1:0] mask_addr_shifted_35;
  assign mask_addr_shifted_35 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_36;
  assign mask_addr_masked_36 = mask_addr_shifted_35 << 2;
  wire [32-1:0] mask_addr_shifted_37;
  assign mask_addr_shifted_37 = _maxi_read_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_38;
  assign mask_addr_masked_38 = mask_addr_shifted_37 << 2;
  reg _maxi_cond_0_1;
  reg [32-1:0] _maxi_read_data_fsm;
  localparam _maxi_read_data_fsm_init = 0;
  reg [32-1:0] write_burst_fsm_0;
  localparam write_burst_fsm_0_init = 0;
  reg [10-1:0] write_burst_addr_39;
  reg [10-1:0] write_burst_stride_40;
  reg [11-1:0] write_burst_length_41;
  reg write_burst_done_42;
  assign ram_a_0_wdata = ((write_burst_fsm_0 == 1) && maxi_rvalid)? maxi_rdata : 'hx;
  assign ram_a_0_wenable = ((write_burst_fsm_0 == 1) && maxi_rvalid)? 1'd1 : 0;
  reg signed [32-1:0] _th_matmul_b_addr_11;
  reg signed [32-1:0] _th_matmul_j_12;
  wire [32-1:0] mask_addr_shifted_43;
  assign mask_addr_shifted_43 = _th_matmul_b_addr_11 >> 2;
  wire [32-1:0] mask_addr_masked_44;
  assign mask_addr_masked_44 = mask_addr_shifted_43 << 2;
  assign _maxi_read_req_fifo_deq = ((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 2)) && !_maxi_read_req_fifo_empty)? 1 : 
                                   ((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) && !_maxi_read_req_fifo_empty)? 1 : 0;
  reg [32-1:0] write_burst_fsm_1;
  localparam write_burst_fsm_1_init = 0;
  reg [10-1:0] write_burst_addr_45;
  reg [10-1:0] write_burst_stride_46;
  reg [11-1:0] write_burst_length_47;
  reg write_burst_done_48;
  assign ram_b_0_wdata = ((write_burst_fsm_1 == 1) && maxi_rvalid)? maxi_rdata : 'hx;
  assign ram_b_0_wenable = ((write_burst_fsm_1 == 1) && maxi_rvalid)? 1'd1 : 0;
  assign maxi_rready = (_maxi_read_data_fsm == 2) || (_maxi_read_data_fsm == 2);
  reg signed [32-1:0] _th_matmul_size_13;
  reg signed [32-1:0] _th_matmul_waddr_14;
  wire signed [32-1:0] strm_madd_a_data;
  wire signed [32-1:0] strm_madd_b_data;
  wire signed [32-1:0] strm_madd_size_data;
  wire [1-1:0] strm_madd__reduce_reset_data;
  reg __strm_madd_stream_ivalid_1;
  reg __strm_madd_stream_ivalid_2;
  reg __strm_madd_stream_ivalid_3;
  reg __strm_madd_stream_ivalid_4;
  wire signed [64-1:0] _times_mul_odata_4;
  reg signed [64-1:0] _times_mul_odata_reg_4;
  wire signed [32-1:0] _times_data_4;
  assign _times_data_4 = _times_mul_odata_reg_4;
  wire _times_mul_update_4;
  assign _times_mul_update_4 = _strm_madd_stream_oready;

  multiplier_0
  _times_mul_4
  (
    .CLK(CLK),
    .update(_times_mul_update_4),
    .a(strm_madd_a_data),
    .b(strm_madd_b_data),
    .c(_times_mul_odata_4)
  );

  reg signed [32-1:0] __delay_data_9__variable_2;
  reg [1-1:0] __delay_data_12__variable_3;
  reg signed [32-1:0] __delay_data_10__delay_9__variable_2;
  reg [1-1:0] __delay_data_13__delay_12__variable_3;
  reg signed [32-1:0] __delay_data_11__delay_10__delay_9__variable_2;
  reg [1-1:0] __delay_data_14__delay_13__delay_12__variable_3;
  reg signed [32-1:0] _reduceadd_data_5;
  reg [33-1:0] _reduceadd_count_5;
  reg _reduceadd_prev_count_max_5;
  wire _reduceadd_reset_cond_5;
  assign _reduceadd_reset_cond_5 = __delay_data_14__delay_13__delay_12__variable_3 || _reduceadd_prev_count_max_5;
  wire [33-1:0] _reduceadd_current_count_5;
  assign _reduceadd_current_count_5 = (_reduceadd_reset_cond_5)? 0 : _reduceadd_count_5;
  wire signed [32-1:0] _reduceadd_current_data_5;
  assign _reduceadd_current_data_5 = (_reduceadd_reset_cond_5)? 1'sd0 : _reduceadd_data_5;
  reg [1-1:0] _pulse_data_7;
  reg [33-1:0] _pulse_count_7;
  reg _pulse_prev_count_max_7;
  wire _pulse_reset_cond_7;
  assign _pulse_reset_cond_7 = __delay_data_14__delay_13__delay_12__variable_3 || _pulse_prev_count_max_7;
  wire [33-1:0] _pulse_current_count_7;
  assign _pulse_current_count_7 = (_pulse_reset_cond_7)? 0 : _pulse_count_7;
  wire [1-1:0] _pulse_current_data_7;
  assign _pulse_current_data_7 = (_pulse_reset_cond_7)? 1'sd0 : _pulse_data_7;
  wire signed [32-1:0] strm_madd_sum_data;
  assign strm_madd_sum_data = _reduceadd_data_5;
  wire [1-1:0] strm_madd_sum_valid_data;
  assign strm_madd_sum_valid_data = _pulse_data_7;
  wire _set_flag_49;
  assign _set_flag_49 = th_matmul == 20;
  assign ram_a_0_addr = (_strm_madd_stream_oready && _strm_madd_a_source_ram_renable && (_strm_madd_a_source_sel == 1))? _strm_madd_a_source_ram_raddr : 
                        ((write_burst_fsm_0 == 1) && maxi_rvalid)? write_burst_addr_39 : 'hx;
  assign ram_a_0_enable = (_strm_madd_stream_oready && _strm_madd_a_source_ram_renable && (_strm_madd_a_source_sel == 1))? 1'd1 : 
                          ((write_burst_fsm_0 == 1) && maxi_rvalid)? 1'd1 : 0;
  localparam _tmp_50 = 1;
  wire [_tmp_50-1:0] _tmp_51;
  assign _tmp_51 = _strm_madd_stream_oready && _strm_madd_a_source_ram_renable && (_strm_madd_a_source_sel == 1);
  reg [_tmp_50-1:0] __tmp_51_1;
  assign _strm_madd_a_source_ram_rdata = (_strm_madd_a_source_sel == 1)? ram_a_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_0;
  assign strm_madd_a_data = __variable_wdata_0;
  reg [32-1:0] _strm_madd_a_source_fsm_0;
  localparam _strm_madd_a_source_fsm_0_init = 0;
  wire _set_flag_52;
  assign _set_flag_52 = th_matmul == 21;
  assign ram_b_0_addr = (_strm_madd_stream_oready && _strm_madd_b_source_ram_renable && (_strm_madd_b_source_sel == 2))? _strm_madd_b_source_ram_raddr : 
                        ((write_burst_fsm_1 == 1) && maxi_rvalid)? write_burst_addr_45 : 'hx;
  assign ram_b_0_enable = (_strm_madd_stream_oready && _strm_madd_b_source_ram_renable && (_strm_madd_b_source_sel == 2))? 1'd1 : 
                          ((write_burst_fsm_1 == 1) && maxi_rvalid)? 1'd1 : 0;
  localparam _tmp_53 = 1;
  wire [_tmp_53-1:0] _tmp_54;
  assign _tmp_54 = _strm_madd_stream_oready && _strm_madd_b_source_ram_renable && (_strm_madd_b_source_sel == 2);
  reg [_tmp_53-1:0] __tmp_54_1;
  assign _strm_madd_b_source_ram_rdata = (_strm_madd_b_source_sel == 2)? ram_b_0_rdata : 'hx;
  reg signed [32-1:0] __variable_wdata_1;
  assign strm_madd_b_data = __variable_wdata_1;
  reg [32-1:0] _strm_madd_b_source_fsm_1;
  localparam _strm_madd_b_source_fsm_1_init = 0;
  wire _set_flag_55;
  assign _set_flag_55 = th_matmul == 22;
  reg signed [32-1:0] __variable_wdata_2;
  assign strm_madd_size_data = __variable_wdata_2;
  wire _set_flag_56;
  assign _set_flag_56 = th_matmul == 23;
  reg _tmp_57;
  reg _tmp_58;
  reg _tmp_59;
  reg _tmp_60;
  reg _tmp_61;
  reg _tmp_62;
  reg signed [32-1:0] _tmp_63;
  reg signed [32-1:0] _tmp_64;
  reg signed [32-1:0] _tmp_65;
  reg signed [32-1:0] _tmp_66;
  reg signed [32-1:0] _tmp_67;
  reg signed [32-1:0] _tmp_68;
  assign ram_c_0_wdata = (_strm_madd_stream_oready && _strm_madd_sum_sink_wenable && (_strm_madd_sum_sink_sel == 3))? _strm_madd_sum_sink_wdata : 'hx;
  assign ram_c_0_wenable = (_strm_madd_stream_oready && _strm_madd_sum_sink_wenable && (_strm_madd_sum_sink_sel == 3))? 1'd1 : 0;
  reg [32-1:0] _strm_madd_sum_sink_fsm_2;
  localparam _strm_madd_sum_sink_fsm_2_init = 0;
  wire _set_flag_69;
  assign _set_flag_69 = th_matmul == 24;
  assign _strm_madd_run_flag = (_set_flag_69)? 1 : 0;
  reg _tmp_70;
  reg _tmp_71;
  reg _tmp_72;
  reg _tmp_73;
  reg _tmp_74;
  reg _tmp_75;
  reg [1-1:0] __variable_wdata_3;
  assign strm_madd__reduce_reset_data = __variable_wdata_3;
  reg _tmp_76;
  reg _tmp_77;
  reg _tmp_78;
  reg _tmp_79;
  assign _strm_madd_source_stop = _strm_madd_stream_oready && (_strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3));
  localparam _tmp_80 = 1;
  wire [_tmp_80-1:0] _tmp_81;
  assign _tmp_81 = _strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3);
  reg [_tmp_80-1:0] _tmp_82;
  localparam _tmp_83 = 1;
  wire [_tmp_83-1:0] _tmp_84;
  assign _tmp_84 = _strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3);
  reg [_tmp_83-1:0] _tmp_85;
  reg _tmp_86;
  reg _tmp_87;
  reg _tmp_88;
  reg _tmp_89;
  reg _tmp_90;
  reg _tmp_91;
  assign _strm_madd_sink_start = _tmp_91;
  reg _tmp_92;
  reg _tmp_93;
  reg _tmp_94;
  reg _tmp_95;
  reg _tmp_96;
  reg _tmp_97;
  assign _strm_madd_sink_stop = _tmp_97;
  reg _tmp_98;
  reg _tmp_99;
  reg _tmp_100;
  reg _tmp_101;
  reg _tmp_102;
  reg _tmp_103;
  assign _strm_madd_sink_busy = _tmp_103;
  reg _tmp_104;
  assign _strm_madd_busy = _strm_madd_source_busy || _strm_madd_sink_busy || _strm_madd_busy_reg;
  wire [32-1:0] mask_addr_shifted_105;
  assign mask_addr_shifted_105 = _th_matmul_c_addr_9 >> 2;
  wire [32-1:0] mask_addr_masked_106;
  assign mask_addr_masked_106 = mask_addr_shifted_105 << 2;
  reg [32-1:0] _maxi_write_req_fsm;
  localparam _maxi_write_req_fsm_init = 0;
  reg [33-1:0] _maxi_write_cur_global_size;
  reg _maxi_write_cont;
  wire [8-1:0] pack_write_req_op_sel_107;
  wire [32-1:0] pack_write_req_local_addr_108;
  wire [32-1:0] pack_write_req_local_stride_109;
  wire [33-1:0] pack_write_req_size_110;
  assign pack_write_req_op_sel_107 = _maxi_write_op_sel;
  assign pack_write_req_local_addr_108 = _maxi_write_local_addr;
  assign pack_write_req_local_stride_109 = _maxi_write_local_stride;
  assign pack_write_req_size_110 = _maxi_write_local_size;
  wire [105-1:0] pack_write_req_packed_111;
  assign pack_write_req_packed_111 = { pack_write_req_op_sel_107, pack_write_req_local_addr_108, pack_write_req_local_stride_109, pack_write_req_size_110 };
  localparam _tmp_112 = 1;
  wire [_tmp_112-1:0] _tmp_113;
  assign _tmp_113 = !_maxi_write_req_fifo_almost_full;
  reg [_tmp_112-1:0] __tmp_113_1;
  wire [32-1:0] mask_addr_shifted_114;
  assign mask_addr_shifted_114 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_115;
  assign mask_addr_masked_115 = mask_addr_shifted_114 << 2;
  wire [32-1:0] mask_addr_shifted_116;
  assign mask_addr_shifted_116 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_117;
  assign mask_addr_masked_117 = mask_addr_shifted_116 << 2;
  wire [32-1:0] mask_addr_shifted_118;
  assign mask_addr_shifted_118 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_119;
  assign mask_addr_masked_119 = mask_addr_shifted_118 << 2;
  wire [32-1:0] mask_addr_shifted_120;
  assign mask_addr_shifted_120 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_121;
  assign mask_addr_masked_121 = mask_addr_shifted_120 << 2;
  wire [32-1:0] mask_addr_shifted_122;
  assign mask_addr_shifted_122 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_123;
  assign mask_addr_masked_123 = mask_addr_shifted_122 << 2;
  wire [32-1:0] mask_addr_shifted_124;
  assign mask_addr_shifted_124 = _maxi_write_global_addr >> 2;
  wire [32-1:0] mask_addr_masked_125;
  assign mask_addr_masked_125 = mask_addr_shifted_124 << 2;
  wire [8-1:0] pack_write_req_op_sel_126;
  wire [32-1:0] pack_write_req_local_addr_127;
  wire [32-1:0] pack_write_req_local_stride_128;
  wire [33-1:0] pack_write_req_size_129;
  assign pack_write_req_op_sel_126 = _maxi_write_op_sel;
  assign pack_write_req_local_addr_127 = _maxi_write_local_addr;
  assign pack_write_req_local_stride_128 = _maxi_write_local_stride;
  assign pack_write_req_size_129 = _maxi_write_cur_global_size;
  wire [105-1:0] pack_write_req_packed_130;
  assign pack_write_req_packed_130 = { pack_write_req_op_sel_126, pack_write_req_local_addr_127, pack_write_req_local_stride_128, pack_write_req_size_129 };
  assign _maxi_write_req_fifo_wdata = ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6))? pack_write_req_packed_130 : 
                                      ((_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full)? pack_write_req_packed_111 : 'hx;
  assign _maxi_write_req_fifo_enq = ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6))? (_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6) && !_maxi_write_req_fifo_almost_full : 
                                    ((_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full)? (_maxi_write_req_fsm == 0) && _maxi_write_start && !_maxi_write_req_fifo_almost_full && !_maxi_write_req_fifo_almost_full : 0;
  localparam _tmp_131 = 1;
  wire [_tmp_131-1:0] _tmp_132;
  assign _tmp_132 = !_maxi_write_req_fifo_almost_full;
  reg [_tmp_131-1:0] __tmp_132_1;
  reg _maxi_cond_1_1;
  reg [32-1:0] _maxi_write_data_fsm;
  localparam _maxi_write_data_fsm_init = 0;
  reg [32-1:0] read_burst_fsm_2;
  localparam read_burst_fsm_2_init = 0;
  reg [10-1:0] read_burst_addr_133;
  reg [10-1:0] read_burst_stride_134;
  reg [11-1:0] read_burst_length_135;
  reg read_burst_rvalid_136;
  reg read_burst_rlast_137;
  assign ram_c_0_addr = ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_136 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)))? read_burst_addr_133 : 
                        (_strm_madd_stream_oready && _strm_madd_sum_sink_wenable && (_strm_madd_sum_sink_sel == 3))? _strm_madd_sum_sink_waddr : 'hx;
  assign ram_c_0_enable = ((read_burst_fsm_2 == 1) && (!read_burst_rvalid_136 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)))? 1'd1 : 
                          (_strm_madd_stream_oready && _strm_madd_sum_sink_wenable && (_strm_madd_sum_sink_sel == 3))? 1'd1 : 0;
  localparam _tmp_138 = 1;
  wire [_tmp_138-1:0] _tmp_139;
  assign _tmp_139 = (read_burst_fsm_2 == 1) && (!read_burst_rvalid_136 || (maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0));
  reg [_tmp_138-1:0] __tmp_139_1;
  wire [32-1:0] read_burst_rdata_140;
  assign read_burst_rdata_140 = ram_c_0_rdata;
  assign _maxi_write_req_fifo_deq = ((_maxi_write_data_fsm == 2) && (!_maxi_write_req_fifo_empty && (_maxi_write_size_buf == 0)) && !_maxi_write_req_fifo_empty)? 1 : 
                                    ((_maxi_write_data_fsm == 0) && (_maxi_write_data_idle && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1)) && !_maxi_write_req_fifo_empty)? 1 : 0;
  reg _maxi_cond_2_1;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_51_1 <= 0;
    end else begin
      __tmp_51_1 <= _tmp_51;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_54_1 <= 0;
    end else begin
      __tmp_54_1 <= _tmp_54;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_139_1 <= 0;
    end else begin
      __tmp_139_1 <= _tmp_139;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wcount_0 <= 0;
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      _maxi_read_op_sel <= 0;
      _maxi_read_global_addr <= 0;
      _maxi_read_global_size <= 0;
      _maxi_read_local_addr <= 0;
      _maxi_read_local_stride <= 0;
      _maxi_read_local_size <= 0;
      _maxi_read_req_idle <= 1;
      _maxi_read_cur_global_size <= 0;
      maxi_araddr <= 0;
      maxi_arlen <= 0;
      maxi_arvalid <= 0;
      _maxi_cond_0_1 <= 0;
      _maxi_read_data_idle <= 1;
      _maxi_read_op_sel_buf <= 0;
      _maxi_read_local_addr_buf <= 0;
      _maxi_read_local_stride_buf <= 0;
      _maxi_read_local_size_buf <= 0;
      _maxi_write_op_sel <= 0;
      _maxi_write_global_addr <= 0;
      _maxi_write_global_size <= 0;
      _maxi_write_local_addr <= 0;
      _maxi_write_local_stride <= 0;
      _maxi_write_local_size <= 0;
      _maxi_write_req_idle <= 1;
      _maxi_write_cur_global_size <= 0;
      maxi_awaddr <= 0;
      maxi_awlen <= 0;
      maxi_awvalid <= 0;
      _maxi_cond_1_1 <= 0;
      _maxi_write_data_idle <= 1;
      _maxi_write_op_sel_buf <= 0;
      _maxi_write_local_addr_buf <= 0;
      _maxi_write_local_stride_buf <= 0;
      _maxi_write_size_buf <= 0;
      maxi_wdata <= 0;
      maxi_wvalid <= 0;
      maxi_wlast <= 0;
      maxi_wstrb <= 0;
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
      end 
      if(maxi_awvalid && maxi_awready && !(maxi_bvalid && maxi_bready) && (outstanding_wcount_0 < 7)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 + 1;
      end 
      if(!(maxi_awvalid && maxi_awready) && (maxi_bvalid && maxi_bready) && (outstanding_wcount_0 > 0)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 - 1;
      end 
      _maxi_read_start <= 0;
      _maxi_write_start <= 0;
      if((th_matmul == 12) && _maxi_read_req_idle) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= 1;
        _maxi_read_global_addr <= mask_addr_masked_19;
        _maxi_read_global_size <= _th_matmul_matrix_size_4;
        _maxi_read_local_addr <= 0;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_matmul_matrix_size_4;
      end 
      if((_maxi_read_req_fsm == 0) && _maxi_read_start) begin
        _maxi_read_req_idle <= 0;
      end 
      if(_maxi_read_start && _maxi_read_req_fifo_almost_full) begin
        _maxi_read_start <= 1;
      end 
      if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256) && ((mask_addr_masked_28 & 4095) + (_maxi_read_global_size << 2) >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_30 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_32 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && (_maxi_read_global_size <= 256)) begin
        _maxi_read_cur_global_size <= _maxi_read_global_size;
        _maxi_read_global_size <= 0;
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full && ((mask_addr_masked_34 & 4095) + 1024 >= 4096)) begin
        _maxi_read_cur_global_size <= 4096 - (mask_addr_masked_36 & 4095) >> 2;
        _maxi_read_global_size <= _maxi_read_global_size - (4096 - (mask_addr_masked_38 & 4095) >> 2);
      end else if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full) begin
        _maxi_read_cur_global_size <= 256;
        _maxi_read_global_size <= _maxi_read_global_size - 256;
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid)) begin
        maxi_araddr <= _maxi_read_global_addr;
        maxi_arlen <= _maxi_read_cur_global_size - 1;
        maxi_arvalid <= 1;
      end 
      _maxi_cond_0_1 <= 1;
      if(maxi_arvalid && !maxi_arready) begin
        maxi_arvalid <= maxi_arvalid;
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid)) begin
        _maxi_read_global_addr <= _maxi_read_global_addr + (_maxi_read_cur_global_size << 2);
      end 
      if((_maxi_read_req_fsm == 1) && (maxi_arready || !maxi_arvalid) && (_maxi_read_global_size == 0)) begin
        _maxi_read_req_idle <= 1;
      end 
      if((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1))) begin
        _maxi_read_data_idle <= 0;
        _maxi_read_op_sel_buf <= _maxi_read_op_sel_fifo;
        _maxi_read_local_addr_buf <= _maxi_read_local_addr_fifo;
        _maxi_read_local_stride_buf <= _maxi_read_local_stride_fifo;
        _maxi_read_local_size_buf <= _maxi_read_local_size_fifo;
      end 
      if((_maxi_read_data_fsm == 2) && maxi_rvalid) begin
        _maxi_read_local_size_buf <= _maxi_read_local_size_buf - 1;
      end 
      if((_maxi_read_data_fsm == 2) && maxi_rvalid && (_maxi_read_local_size_buf <= 1)) begin
        _maxi_read_data_idle <= 1;
      end 
      if((th_matmul == 17) && _maxi_read_req_idle) begin
        _maxi_read_start <= 1;
        _maxi_read_op_sel <= 2;
        _maxi_read_global_addr <= mask_addr_masked_44;
        _maxi_read_global_size <= _th_matmul_matrix_size_4;
        _maxi_read_local_addr <= 0;
        _maxi_read_local_stride <= 1;
        _maxi_read_local_size <= _th_matmul_matrix_size_4;
      end 
      if((_maxi_read_data_fsm == 0) && (_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 2))) begin
        _maxi_read_data_idle <= 0;
        _maxi_read_op_sel_buf <= _maxi_read_op_sel_fifo;
        _maxi_read_local_addr_buf <= _maxi_read_local_addr_fifo;
        _maxi_read_local_stride_buf <= _maxi_read_local_stride_fifo;
        _maxi_read_local_size_buf <= _maxi_read_local_size_fifo;
      end 
      if((_maxi_read_data_fsm == 2) && maxi_rvalid) begin
        _maxi_read_local_size_buf <= _maxi_read_local_size_buf - 1;
      end 
      if((_maxi_read_data_fsm == 2) && maxi_rvalid && (_maxi_read_local_size_buf <= 1)) begin
        _maxi_read_data_idle <= 1;
      end 
      if((th_matmul == 29) && _maxi_write_req_idle) begin
        _maxi_write_start <= 1;
        _maxi_write_op_sel <= 1;
        _maxi_write_global_addr <= mask_addr_masked_106;
        _maxi_write_global_size <= _th_matmul_matrix_size_4;
        _maxi_write_local_addr <= 0;
        _maxi_write_local_stride <= 1;
        _maxi_write_local_size <= _th_matmul_matrix_size_4;
      end 
      if((_maxi_write_req_fsm == 0) && _maxi_write_start) begin
        _maxi_write_req_idle <= 0;
      end 
      if(_maxi_write_start && _maxi_write_req_fifo_almost_full) begin
        _maxi_write_start <= 1;
      end 
      if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && (_maxi_write_global_size <= 256) && ((mask_addr_masked_115 & 4095) + (_maxi_write_global_size << 2) >= 4096)) begin
        _maxi_write_cur_global_size <= 4096 - (mask_addr_masked_117 & 4095) >> 2;
        _maxi_write_global_size <= _maxi_write_global_size - (4096 - (mask_addr_masked_119 & 4095) >> 2);
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && (_maxi_write_global_size <= 256)) begin
        _maxi_write_cur_global_size <= _maxi_write_global_size;
        _maxi_write_global_size <= 0;
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full && ((mask_addr_masked_121 & 4095) + 1024 >= 4096)) begin
        _maxi_write_cur_global_size <= 4096 - (mask_addr_masked_123 & 4095) >> 2;
        _maxi_write_global_size <= _maxi_write_global_size - (4096 - (mask_addr_masked_125 & 4095) >> 2);
      end else if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full) begin
        _maxi_write_cur_global_size <= 256;
        _maxi_write_global_size <= _maxi_write_global_size - 256;
      end 
      if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (outstanding_wcount_0 < 6) && ((outstanding_wcount_0 < 6) && (maxi_awready || !maxi_awvalid))) begin
        maxi_awaddr <= _maxi_write_global_addr;
        maxi_awlen <= _maxi_write_cur_global_size - 1;
        maxi_awvalid <= 1;
      end 
      if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (outstanding_wcount_0 < 6) && ((outstanding_wcount_0 < 6) && (maxi_awready || !maxi_awvalid)) && (_maxi_write_cur_global_size == 0)) begin
        maxi_awvalid <= 0;
      end 
      _maxi_cond_1_1 <= 1;
      if(maxi_awvalid && !maxi_awready) begin
        maxi_awvalid <= maxi_awvalid;
      end 
      if((_maxi_write_req_fsm == 1) && ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6))) begin
        _maxi_write_global_addr <= _maxi_write_global_addr + (_maxi_write_cur_global_size << 2);
      end 
      if((_maxi_write_req_fsm == 1) && ((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6)) && (_maxi_write_global_size == 0)) begin
        _maxi_write_req_idle <= 1;
      end 
      if((_maxi_write_data_fsm == 0) && (_maxi_write_data_idle && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1))) begin
        _maxi_write_data_idle <= 0;
        _maxi_write_op_sel_buf <= _maxi_write_op_sel_fifo;
        _maxi_write_local_addr_buf <= _maxi_write_local_addr_fifo;
        _maxi_write_local_stride_buf <= _maxi_write_local_stride_fifo;
        _maxi_write_size_buf <= _maxi_write_size_fifo;
      end 
      if(_maxi_write_data_fsm == 1) begin
        _maxi_write_size_buf <= 0;
      end 
      if((_maxi_write_data_fsm == 2) && (!_maxi_write_req_fifo_empty && (_maxi_write_size_buf == 0))) begin
        _maxi_write_size_buf <= _maxi_write_size_fifo;
      end 
      if((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_136 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)) && ((outstanding_wcount_0 < 6) && (maxi_wready || !maxi_wvalid))) begin
        maxi_wdata <= read_burst_rdata_140;
        maxi_wvalid <= 1;
        maxi_wlast <= read_burst_rlast_137 || (_maxi_write_size_buf == 1);
        maxi_wstrb <= { 4{ 1'd1 } };
      end 
      _maxi_cond_2_1 <= 1;
      if(maxi_wvalid && !maxi_wready) begin
        maxi_wvalid <= maxi_wvalid;
        maxi_wlast <= maxi_wlast;
      end 
      if((_maxi_write_data_fsm == 2) && read_burst_rvalid_136 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) begin
        _maxi_write_size_buf <= _maxi_write_size_buf - 1;
      end 
      if((_maxi_write_data_fsm == 2) && ((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_136 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) && read_burst_rlast_137) begin
        _maxi_write_data_idle <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_read_req_fifo <= 0;
      __tmp_26_1 <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full && (_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty)) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo;
      end else if(_maxi_read_req_fifo_enq && !_maxi_read_req_fifo_full) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo + 1;
      end else if(_maxi_read_req_fifo_deq && !_maxi_read_req_fifo_empty) begin
        count__maxi_read_req_fifo <= count__maxi_read_req_fifo - 1;
      end 
      __tmp_26_1 <= _tmp_26;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count__maxi_write_req_fifo <= 0;
      __tmp_113_1 <= 0;
      __tmp_132_1 <= 0;
    end else begin
      if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full && (_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty)) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo;
      end else if(_maxi_write_req_fifo_enq && !_maxi_write_req_fifo_full) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo + 1;
      end else if(_maxi_write_req_fifo_deq && !_maxi_write_req_fifo_empty) begin
        count__maxi_write_req_fifo <= count__maxi_write_req_fifo - 1;
      end 
      __tmp_113_1 <= _tmp_113;
      __tmp_132_1 <= _tmp_132;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_12 <= 0;
      prev_arvalid_13 <= 0;
      writevalid_10 <= 0;
      readvalid_11 <= 0;
      addr_9 <= 0;
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
    end else begin
      if(_saxi_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      if(saxi_bvalid && saxi_bready) begin
        saxi_bvalid <= 0;
      end 
      if(saxi_wvalid && saxi_wready) begin
        saxi_bvalid <= 1;
      end 
      prev_awvalid_12 <= saxi_awvalid;
      prev_arvalid_13 <= saxi_arvalid;
      writevalid_10 <= 0;
      readvalid_11 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_9 <= saxi_awaddr;
        writevalid_10 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_9 <= saxi_araddr;
        readvalid_11 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_15;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 0)) begin
        _saxi_register_0 <= axislite_resetval_17;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 1)) begin
        _saxi_register_1 <= axislite_resetval_17;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 2)) begin
        _saxi_register_2 <= axislite_resetval_17;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 3)) begin
        _saxi_register_3 <= axislite_resetval_17;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 4)) begin
        _saxi_register_4 <= axislite_resetval_17;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 5)) begin
        _saxi_register_5 <= axislite_resetval_17;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 6)) begin
        _saxi_register_6 <= axislite_resetval_17;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_16 && (axis_maskaddr_14 == 7)) begin
        _saxi_register_7 <= axislite_resetval_17;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_14 == 7)) begin
        _saxi_register_7 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_4 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_5 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_6 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_matmul == 2) && 0) begin
        _saxi_register_7 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 0;
      end 
      if((th_matmul == 3) && 1) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_4 <= 1;
        _saxi_flag_4 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_5 <= 1;
        _saxi_flag_5 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_6 <= 1;
        _saxi_flag_6 <= 0;
      end 
      if((th_matmul == 3) && 0) begin
        _saxi_register_7 <= 1;
        _saxi_flag_7 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_matmul == 34) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_4 <= 0;
        _saxi_flag_4 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_5 <= 0;
        _saxi_flag_5 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_6 <= 0;
        _saxi_flag_6 <= 0;
      end 
      if((th_matmul == 34) && 0) begin
        _saxi_register_7 <= 0;
        _saxi_flag_7 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
      axis_maskaddr_14 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_11 || writevalid_10) begin
            axis_maskaddr_14 <= (addr_9 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_11) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_10) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_2: begin
          if(saxi_wvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_a_source_ram_renable <= 0;
      _strm_madd_a_source_fifo_deq <= 0;
      _strm_madd_a_idle <= 1;
      _strm_madd_b_source_ram_renable <= 0;
      _strm_madd_b_source_fifo_deq <= 0;
      _strm_madd_b_idle <= 1;
      _strm_madd_sum_sink_wenable <= 0;
      _strm_madd_sum_sink_fifo_enq <= 0;
      _strm_madd_sum_valid_sink_wenable <= 0;
      _strm_madd_sum_valid_sink_fifo_enq <= 0;
      __strm_madd_stream_ivalid_1 <= 0;
      __strm_madd_stream_ivalid_2 <= 0;
      __strm_madd_stream_ivalid_3 <= 0;
      __strm_madd_stream_ivalid_4 <= 0;
      _times_mul_odata_reg_4 <= 0;
      __delay_data_9__variable_2 <= 0;
      __delay_data_12__variable_3 <= 0;
      __delay_data_10__delay_9__variable_2 <= 0;
      __delay_data_13__delay_12__variable_3 <= 0;
      __delay_data_11__delay_10__delay_9__variable_2 <= 0;
      __delay_data_14__delay_13__delay_12__variable_3 <= 0;
      _reduceadd_data_5 <= 1'sd0;
      _reduceadd_count_5 <= 0;
      _reduceadd_prev_count_max_5 <= 0;
      _pulse_data_7 <= 1'sd0;
      _pulse_count_7 <= 0;
      _pulse_prev_count_max_7 <= 0;
      _strm_madd_a_source_mode <= 5'b0;
      _strm_madd_a_source_offset <= 0;
      _strm_madd_a_source_size <= 0;
      _strm_madd_a_source_stride <= 0;
      _strm_madd_a_source_sel <= 0;
      _strm_madd_a_source_offset_buf <= 0;
      _strm_madd_a_source_size_buf <= 0;
      _strm_madd_a_source_stride_buf <= 0;
      __variable_wdata_0 <= 0;
      _strm_madd_a_source_ram_raddr <= 0;
      _strm_madd_a_source_count <= 0;
      _strm_madd_b_source_mode <= 5'b0;
      _strm_madd_b_source_offset <= 0;
      _strm_madd_b_source_size <= 0;
      _strm_madd_b_source_stride <= 0;
      _strm_madd_b_source_sel <= 0;
      _strm_madd_b_source_offset_buf <= 0;
      _strm_madd_b_source_size_buf <= 0;
      _strm_madd_b_source_stride_buf <= 0;
      __variable_wdata_1 <= 0;
      _strm_madd_b_source_ram_raddr <= 0;
      _strm_madd_b_source_count <= 0;
      _strm_madd_size_next_parameter_data <= 0;
      __variable_wdata_2 <= 0;
      _tmp_57 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _tmp_60 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _tmp_63 <= 0;
      _tmp_64 <= 0;
      _tmp_65 <= 0;
      _tmp_66 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _strm_madd_sum_sink_mode <= 5'b0;
      _strm_madd_sum_sink_offset <= 0;
      _strm_madd_sum_sink_size <= 0;
      _strm_madd_sum_sink_stride <= 0;
      _strm_madd_sum_sink_sel <= 0;
      _strm_madd_sum_sink_offset_buf <= 0;
      _strm_madd_sum_sink_size_buf <= 0;
      _strm_madd_sum_sink_stride_buf <= 0;
      _strm_madd_sum_sink_waddr <= 0;
      _strm_madd_sum_sink_count <= 0;
      _strm_madd_sum_sink_wdata <= 0;
      _tmp_70 <= 0;
      _tmp_71 <= 0;
      _tmp_72 <= 0;
      _tmp_73 <= 0;
      _tmp_74 <= 0;
      _tmp_75 <= 0;
      __variable_wdata_3 <= 0;
      _tmp_76 <= 0;
      _tmp_77 <= 0;
      _tmp_78 <= 0;
      _tmp_79 <= 0;
      _tmp_82 <= 0;
      _tmp_85 <= 0;
      _tmp_86 <= 0;
      _tmp_87 <= 0;
      _tmp_88 <= 0;
      _tmp_89 <= 0;
      _tmp_90 <= 0;
      _tmp_91 <= 0;
      _tmp_92 <= 0;
      _tmp_93 <= 0;
      _tmp_94 <= 0;
      _tmp_95 <= 0;
      _tmp_96 <= 0;
      _tmp_97 <= 0;
      _tmp_98 <= 0;
      _tmp_99 <= 0;
      _tmp_100 <= 0;
      _tmp_101 <= 0;
      _tmp_102 <= 0;
      _tmp_103 <= 0;
      _tmp_104 <= 0;
      _strm_madd_busy_reg <= 0;
    end else begin
      if(_strm_madd_stream_oready) begin
        _strm_madd_a_source_ram_renable <= 0;
        _strm_madd_a_source_fifo_deq <= 0;
      end 
      _strm_madd_a_idle <= _strm_madd_a_idle;
      if(_strm_madd_stream_oready) begin
        _strm_madd_b_source_ram_renable <= 0;
        _strm_madd_b_source_fifo_deq <= 0;
      end 
      _strm_madd_b_idle <= _strm_madd_b_idle;
      if(_strm_madd_stream_oready) begin
        _strm_madd_sum_sink_wenable <= 0;
        _strm_madd_sum_sink_fifo_enq <= 0;
      end 
      if(_strm_madd_stream_oready) begin
        _strm_madd_sum_valid_sink_wenable <= 0;
        _strm_madd_sum_valid_sink_fifo_enq <= 0;
      end 
      if(_strm_madd_stream_oready) begin
        __strm_madd_stream_ivalid_1 <= _strm_madd_stream_ivalid;
      end 
      if(_strm_madd_stream_oready) begin
        __strm_madd_stream_ivalid_2 <= __strm_madd_stream_ivalid_1;
      end 
      if(_strm_madd_stream_oready) begin
        __strm_madd_stream_ivalid_3 <= __strm_madd_stream_ivalid_2;
      end 
      if(_strm_madd_stream_oready) begin
        __strm_madd_stream_ivalid_4 <= __strm_madd_stream_ivalid_3;
      end 
      if(_strm_madd_stream_oready) begin
        _times_mul_odata_reg_4 <= _times_mul_odata_4;
      end 
      if(_strm_madd_stream_oready) begin
        __delay_data_9__variable_2 <= strm_madd_size_data;
      end 
      if(_strm_madd_stream_oready) begin
        __delay_data_12__variable_3 <= strm_madd__reduce_reset_data;
      end 
      if(_strm_madd_stream_oready) begin
        __delay_data_10__delay_9__variable_2 <= __delay_data_9__variable_2;
      end 
      if(_strm_madd_stream_oready) begin
        __delay_data_13__delay_12__variable_3 <= __delay_data_12__variable_3;
      end 
      if(_strm_madd_stream_oready) begin
        __delay_data_11__delay_10__delay_9__variable_2 <= __delay_data_10__delay_9__variable_2;
      end 
      if(_strm_madd_stream_oready) begin
        __delay_data_14__delay_13__delay_12__variable_3 <= __delay_data_13__delay_12__variable_3;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready && _reduceadd_reset_cond_5) begin
        _reduceadd_data_5 <= 1'sd0;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready) begin
        _reduceadd_count_5 <= (_reduceadd_current_count_5 >= __delay_data_11__delay_10__delay_9__variable_2 - 1)? 0 : _reduceadd_current_count_5 + 1;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready) begin
        _reduceadd_prev_count_max_5 <= _reduceadd_current_count_5 >= __delay_data_11__delay_10__delay_9__variable_2 - 1;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready) begin
        _reduceadd_data_5 <= _reduceadd_current_data_5 + _times_data_4;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready && _pulse_reset_cond_7) begin
        _pulse_data_7 <= 1'sd0;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready) begin
        _pulse_count_7 <= (_pulse_current_count_7 >= __delay_data_11__delay_10__delay_9__variable_2 - 1)? 0 : _pulse_current_count_7 + 1;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready) begin
        _pulse_prev_count_max_7 <= _pulse_current_count_7 >= __delay_data_11__delay_10__delay_9__variable_2 - 1;
      end 
      if(__strm_madd_stream_ivalid_3 && _strm_madd_stream_oready) begin
        _pulse_data_7 <= _pulse_current_count_7 >= __delay_data_11__delay_10__delay_9__variable_2 - 1;
      end 
      if(_set_flag_49) begin
        _strm_madd_a_source_mode <= 5'b1;
        _strm_madd_a_source_offset <= 0;
        _strm_madd_a_source_size <= _th_matmul_size_13;
        _strm_madd_a_source_stride <= 1;
      end 
      if(_set_flag_49) begin
        _strm_madd_a_source_sel <= 1;
      end 
      if(_strm_madd_source_start && _strm_madd_a_source_mode & 5'b1 && _strm_madd_stream_oready) begin
        _strm_madd_a_source_offset_buf <= _strm_madd_a_source_offset;
        _strm_madd_a_source_size_buf <= _strm_madd_a_source_size;
        _strm_madd_a_source_stride_buf <= _strm_madd_a_source_stride;
      end 
      if(_strm_madd_stream_oready && _strm_madd_source_busy && _strm_madd_is_root) begin
        __variable_wdata_0 <= _strm_madd_a_source_ram_rdata;
      end 
      if((_strm_madd_a_source_fsm_0 == 1) && _strm_madd_stream_oready) begin
        _strm_madd_a_idle <= 0;
        _strm_madd_a_source_ram_raddr <= _strm_madd_a_source_offset_buf;
        _strm_madd_a_source_ram_renable <= 1;
        _strm_madd_a_source_count <= _strm_madd_a_source_size_buf;
      end 
      if((_strm_madd_a_source_fsm_0 == 2) && _strm_madd_stream_oready) begin
        _strm_madd_a_source_ram_raddr <= _strm_madd_a_source_ram_raddr + _strm_madd_a_source_stride_buf;
        _strm_madd_a_source_ram_renable <= 1;
        _strm_madd_a_source_count <= _strm_madd_a_source_count - 1;
      end 
      if((_strm_madd_a_source_fsm_0 == 2) && (_strm_madd_a_source_count == 1) && _strm_madd_stream_oready) begin
        _strm_madd_a_source_ram_renable <= 0;
        _strm_madd_a_idle <= 1;
      end 
      if((_strm_madd_a_source_fsm_0 == 2) && _strm_madd_source_stop && _strm_madd_stream_oready) begin
        _strm_madd_a_source_ram_renable <= 0;
        _strm_madd_a_idle <= 1;
      end 
      if(_set_flag_52) begin
        _strm_madd_b_source_mode <= 5'b1;
        _strm_madd_b_source_offset <= 0;
        _strm_madd_b_source_size <= _th_matmul_size_13;
        _strm_madd_b_source_stride <= 1;
      end 
      if(_set_flag_52) begin
        _strm_madd_b_source_sel <= 2;
      end 
      if(_strm_madd_source_start && _strm_madd_b_source_mode & 5'b1 && _strm_madd_stream_oready) begin
        _strm_madd_b_source_offset_buf <= _strm_madd_b_source_offset;
        _strm_madd_b_source_size_buf <= _strm_madd_b_source_size;
        _strm_madd_b_source_stride_buf <= _strm_madd_b_source_stride;
      end 
      if(_strm_madd_stream_oready && _strm_madd_source_busy && _strm_madd_is_root) begin
        __variable_wdata_1 <= _strm_madd_b_source_ram_rdata;
      end 
      if((_strm_madd_b_source_fsm_1 == 1) && _strm_madd_stream_oready) begin
        _strm_madd_b_idle <= 0;
        _strm_madd_b_source_ram_raddr <= _strm_madd_b_source_offset_buf;
        _strm_madd_b_source_ram_renable <= 1;
        _strm_madd_b_source_count <= _strm_madd_b_source_size_buf;
      end 
      if((_strm_madd_b_source_fsm_1 == 2) && _strm_madd_stream_oready) begin
        _strm_madd_b_source_ram_raddr <= _strm_madd_b_source_ram_raddr + _strm_madd_b_source_stride_buf;
        _strm_madd_b_source_ram_renable <= 1;
        _strm_madd_b_source_count <= _strm_madd_b_source_count - 1;
      end 
      if((_strm_madd_b_source_fsm_1 == 2) && (_strm_madd_b_source_count == 1) && _strm_madd_stream_oready) begin
        _strm_madd_b_source_ram_renable <= 0;
        _strm_madd_b_idle <= 1;
      end 
      if((_strm_madd_b_source_fsm_1 == 2) && _strm_madd_source_stop && _strm_madd_stream_oready) begin
        _strm_madd_b_source_ram_renable <= 0;
        _strm_madd_b_idle <= 1;
      end 
      if(_set_flag_55) begin
        _strm_madd_size_next_parameter_data <= _th_matmul_size_13;
      end 
      if(_strm_madd_source_start) begin
        __variable_wdata_2 <= _strm_madd_size_next_parameter_data;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_57 <= _set_flag_56;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_58 <= _tmp_57;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_59 <= _tmp_58;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_60 <= _tmp_59;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_61 <= _tmp_60;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_62 <= _tmp_61;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_63 <= _th_matmul_waddr_14;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_64 <= _tmp_63;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_65 <= _tmp_64;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_66 <= _tmp_65;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_67 <= _tmp_66;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_68 <= _tmp_67;
      end 
      if(_tmp_62) begin
        _strm_madd_sum_sink_mode <= 5'b1;
        _strm_madd_sum_sink_offset <= _tmp_68;
        _strm_madd_sum_sink_size <= 1;
        _strm_madd_sum_sink_stride <= 1;
      end 
      if(_tmp_62) begin
        _strm_madd_sum_sink_sel <= 3;
      end 
      if(_strm_madd_sink_start && _strm_madd_sum_sink_mode & 5'b1 && _strm_madd_stream_oready) begin
        _strm_madd_sum_sink_offset_buf <= _strm_madd_sum_sink_offset;
        _strm_madd_sum_sink_size_buf <= _strm_madd_sum_sink_size;
        _strm_madd_sum_sink_stride_buf <= _strm_madd_sum_sink_stride;
      end 
      if((_strm_madd_sum_sink_fsm_2 == 1) && _strm_madd_stream_oready) begin
        _strm_madd_sum_sink_waddr <= _strm_madd_sum_sink_offset_buf - _strm_madd_sum_sink_stride_buf;
        _strm_madd_sum_sink_count <= _strm_madd_sum_sink_size_buf;
      end 
      if((_strm_madd_sum_sink_fsm_2 == 2) && strm_madd_sum_valid_data && _strm_madd_stream_oready) begin
        _strm_madd_sum_sink_waddr <= _strm_madd_sum_sink_waddr + _strm_madd_sum_sink_stride_buf;
        _strm_madd_sum_sink_wdata <= strm_madd_sum_data;
        _strm_madd_sum_sink_wenable <= 1;
        _strm_madd_sum_sink_count <= _strm_madd_sum_sink_count - 1;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_70 <= _strm_madd_source_start;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_71 <= _tmp_70;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_72 <= _tmp_71;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_73 <= _strm_madd_source_start;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_74 <= _tmp_73;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_75 <= _tmp_74;
      end 
      if(_strm_madd_stream_oready && _tmp_75) begin
        __variable_wdata_3 <= 1;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_76 <= _strm_madd_source_start;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_77 <= _tmp_76;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_78 <= _tmp_77;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_79 <= _tmp_78;
      end 
      if(_strm_madd_stream_oready && _tmp_79) begin
        __variable_wdata_3 <= 0;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_82 <= _tmp_81;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_85 <= _tmp_84;
      end 
      if(_strm_madd_stream_oready && _tmp_85) begin
        __variable_wdata_3 <= 1;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_86 <= _strm_madd_source_start;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_87 <= _tmp_86;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_88 <= _tmp_87;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_89 <= _tmp_88;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_90 <= _tmp_89;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_91 <= _tmp_90;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_92 <= _strm_madd_source_stop;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_93 <= _tmp_92;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_94 <= _tmp_93;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_95 <= _tmp_94;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_96 <= _tmp_95;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_97 <= _tmp_96;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_98 <= _strm_madd_source_busy;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_99 <= _tmp_98;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_100 <= _tmp_99;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_101 <= _tmp_100;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_102 <= _tmp_101;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_103 <= _tmp_102;
      end 
      if(_strm_madd_stream_oready) begin
        _tmp_104 <= _strm_madd_sink_busy;
      end 
      if(!_strm_madd_sink_busy && _tmp_104) begin
        _strm_madd_busy_reg <= 0;
      end 
      if(_strm_madd_source_busy) begin
        _strm_madd_busy_reg <= 1;
      end 
    end
  end

  localparam _strm_madd_fsm_1 = 1;
  localparam _strm_madd_fsm_2 = 2;
  localparam _strm_madd_fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_fsm <= _strm_madd_fsm_init;
      _strm_madd_source_start <= 0;
      _strm_madd_source_busy <= 0;
      _strm_madd_stream_ivalid <= 0;
    end else begin
      if(_strm_madd_stream_oready && _tmp_72) begin
        _strm_madd_stream_ivalid <= 1;
      end 
      if(_strm_madd_stream_oready && _tmp_82) begin
        _strm_madd_stream_ivalid <= 0;
      end 
      case(_strm_madd_fsm)
        _strm_madd_fsm_init: begin
          if(_strm_madd_run_flag) begin
            _strm_madd_source_start <= 1;
          end 
          if(_strm_madd_run_flag) begin
            _strm_madd_fsm <= _strm_madd_fsm_1;
          end 
        end
        _strm_madd_fsm_1: begin
          if(_strm_madd_source_start && _strm_madd_stream_oready) begin
            _strm_madd_source_start <= 0;
            _strm_madd_source_busy <= 1;
          end 
          if(_strm_madd_source_start && _strm_madd_stream_oready) begin
            _strm_madd_fsm <= _strm_madd_fsm_2;
          end 
        end
        _strm_madd_fsm_2: begin
          if(_strm_madd_stream_oready) begin
            _strm_madd_fsm <= _strm_madd_fsm_3;
          end 
        end
        _strm_madd_fsm_3: begin
          if(_strm_madd_stream_oready && (_strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3))) begin
            _strm_madd_source_busy <= 0;
          end 
          if(_strm_madd_stream_oready && (_strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3)) && _strm_madd_run_flag) begin
            _strm_madd_source_start <= 1;
          end 
          if(_strm_madd_stream_oready && (_strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3))) begin
            _strm_madd_fsm <= _strm_madd_fsm_init;
          end 
          if(_strm_madd_stream_oready && (_strm_madd_a_idle && _strm_madd_b_idle && (_strm_madd_fsm == 3)) && _strm_madd_run_flag) begin
            _strm_madd_fsm <= _strm_madd_fsm_1;
          end 
        end
      endcase
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

  always @(posedge CLK) begin
    if(RST) begin
      th_matmul <= th_matmul_init;
      _th_matmul_matrix_size_0 <= 0;
      _th_matmul_a_offset_1 <= 0;
      _th_matmul_b_offset_2 <= 0;
      _th_matmul_c_offset_3 <= 0;
      _th_matmul_matrix_size_4 <= 0;
      _th_matmul_a_offset_5 <= 0;
      _th_matmul_b_offset_6 <= 0;
      _th_matmul_c_offset_7 <= 0;
      _th_matmul_a_addr_8 <= 0;
      _th_matmul_c_addr_9 <= 0;
      _th_matmul_i_10 <= 0;
      _th_matmul_b_addr_11 <= 0;
      _th_matmul_j_12 <= 0;
      _th_matmul_size_13 <= 0;
      _th_matmul_waddr_14 <= 0;
    end else begin
      case(th_matmul)
        th_matmul_init: begin
          th_matmul <= th_matmul_1;
        end
        th_matmul_1: begin
          if(1) begin
            th_matmul <= th_matmul_2;
          end else begin
            th_matmul <= th_matmul_36;
          end
        end
        th_matmul_2: begin
          if(_saxi_register_0 == 1) begin
            th_matmul <= th_matmul_3;
          end 
        end
        th_matmul_3: begin
          th_matmul <= th_matmul_4;
        end
        th_matmul_4: begin
          _th_matmul_matrix_size_0 <= _saxi_register_2;
          th_matmul <= th_matmul_5;
        end
        th_matmul_5: begin
          _th_matmul_a_offset_1 <= _saxi_register_3;
          th_matmul <= th_matmul_6;
        end
        th_matmul_6: begin
          _th_matmul_b_offset_2 <= _saxi_register_4;
          th_matmul <= th_matmul_7;
        end
        th_matmul_7: begin
          _th_matmul_c_offset_3 <= _saxi_register_5;
          th_matmul <= th_matmul_8;
        end
        th_matmul_8: begin
          _th_matmul_matrix_size_4 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_5 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_6 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_7 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_9;
        end
        th_matmul_9: begin
          _th_matmul_a_addr_8 <= _th_matmul_a_offset_5;
          _th_matmul_c_addr_9 <= _th_matmul_c_offset_7;
          th_matmul <= th_matmul_10;
        end
        th_matmul_10: begin
          _th_matmul_i_10 <= 0;
          th_matmul <= th_matmul_11;
        end
        th_matmul_11: begin
          if(_th_matmul_i_10 < _th_matmul_matrix_size_4) begin
            th_matmul <= th_matmul_12;
          end else begin
            th_matmul <= th_matmul_34;
          end
        end
        th_matmul_12: begin
          if(_maxi_read_req_idle) begin
            th_matmul <= th_matmul_13;
          end 
        end
        th_matmul_13: begin
          if(_maxi_read_idle) begin
            th_matmul <= th_matmul_14;
          end 
        end
        th_matmul_14: begin
          _th_matmul_b_addr_11 <= _th_matmul_b_offset_6;
          th_matmul <= th_matmul_15;
        end
        th_matmul_15: begin
          _th_matmul_j_12 <= 0;
          th_matmul <= th_matmul_16;
        end
        th_matmul_16: begin
          if(_th_matmul_j_12 < _th_matmul_matrix_size_4) begin
            th_matmul <= th_matmul_17;
          end else begin
            th_matmul <= th_matmul_29;
          end
        end
        th_matmul_17: begin
          if(_maxi_read_req_idle) begin
            th_matmul <= th_matmul_18;
          end 
        end
        th_matmul_18: begin
          if(_maxi_read_idle) begin
            th_matmul <= th_matmul_19;
          end 
        end
        th_matmul_19: begin
          _th_matmul_size_13 <= _th_matmul_matrix_size_4;
          _th_matmul_waddr_14 <= _th_matmul_j_12;
          th_matmul <= th_matmul_20;
        end
        th_matmul_20: begin
          th_matmul <= th_matmul_21;
        end
        th_matmul_21: begin
          th_matmul <= th_matmul_22;
        end
        th_matmul_22: begin
          th_matmul <= th_matmul_23;
        end
        th_matmul_23: begin
          if(_strm_madd_stream_oready) begin
            th_matmul <= th_matmul_24;
          end 
        end
        th_matmul_24: begin
          th_matmul <= th_matmul_25;
        end
        th_matmul_25: begin
          if(_strm_madd_busy) begin
            th_matmul <= th_matmul_26;
          end 
        end
        th_matmul_26: begin
          if(!_strm_madd_busy) begin
            th_matmul <= th_matmul_27;
          end 
        end
        th_matmul_27: begin
          _th_matmul_b_addr_11 <= _th_matmul_b_addr_11 + (_th_matmul_matrix_size_4 << 2);
          th_matmul <= th_matmul_28;
        end
        th_matmul_28: begin
          _th_matmul_j_12 <= _th_matmul_j_12 + 1;
          th_matmul <= th_matmul_16;
        end
        th_matmul_29: begin
          if(_maxi_write_req_idle) begin
            th_matmul <= th_matmul_30;
          end 
        end
        th_matmul_30: begin
          if(_maxi_write_idle && (outstanding_wcount_0 == 0)) begin
            th_matmul <= th_matmul_31;
          end 
        end
        th_matmul_31: begin
          _th_matmul_a_addr_8 <= _th_matmul_a_addr_8 + (_th_matmul_matrix_size_4 << 2);
          th_matmul <= th_matmul_32;
        end
        th_matmul_32: begin
          _th_matmul_c_addr_9 <= _th_matmul_c_addr_9 + (_th_matmul_matrix_size_4 << 2);
          th_matmul <= th_matmul_33;
        end
        th_matmul_33: begin
          _th_matmul_i_10 <= _th_matmul_i_10 + 1;
          th_matmul <= th_matmul_11;
        end
        th_matmul_34: begin
          th_matmul <= th_matmul_35;
        end
        th_matmul_35: begin
          th_matmul <= th_matmul_1;
        end
      endcase
    end
  end

  localparam _maxi_read_req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_req_fsm <= _maxi_read_req_fsm_init;
      _maxi_read_cont <= 0;
    end else begin
      case(_maxi_read_req_fsm)
        _maxi_read_req_fsm_init: begin
          if((_maxi_read_req_fsm == 0) && (_maxi_read_start || _maxi_read_cont) && !_maxi_read_req_fifo_almost_full) begin
            _maxi_read_req_fsm <= _maxi_read_req_fsm_1;
          end 
        end
        _maxi_read_req_fsm_1: begin
          if(maxi_arready || !maxi_arvalid) begin
            _maxi_read_cont <= 1;
          end 
          if((maxi_arready || !maxi_arvalid) && (_maxi_read_global_size == 0)) begin
            _maxi_read_cont <= 0;
          end 
          if(maxi_arready || !maxi_arvalid) begin
            _maxi_read_req_fsm <= _maxi_read_req_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _maxi_read_data_fsm_1 = 1;
  localparam _maxi_read_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_read_data_fsm <= _maxi_read_data_fsm_init;
    end else begin
      case(_maxi_read_data_fsm)
        _maxi_read_data_fsm_init: begin
          if(_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_1;
          end 
          if(_maxi_read_data_idle && !_maxi_read_req_fifo_empty && (_maxi_read_op_sel_fifo == 2)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_1;
          end 
        end
        _maxi_read_data_fsm_1: begin
          _maxi_read_data_fsm <= _maxi_read_data_fsm_2;
          _maxi_read_data_fsm <= _maxi_read_data_fsm_2;
        end
        _maxi_read_data_fsm_2: begin
          if(maxi_rvalid && (_maxi_read_local_size_buf <= 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_init;
          end 
          if(maxi_rvalid && (_maxi_read_local_size_buf <= 1)) begin
            _maxi_read_data_fsm <= _maxi_read_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_0_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_0 <= write_burst_fsm_0_init;
      write_burst_addr_39 <= 0;
      write_burst_stride_40 <= 0;
      write_burst_length_41 <= 0;
      write_burst_done_42 <= 0;
    end else begin
      case(write_burst_fsm_0)
        write_burst_fsm_0_init: begin
          write_burst_addr_39 <= _maxi_read_local_addr_buf;
          write_burst_stride_40 <= _maxi_read_local_stride_buf;
          write_burst_length_41 <= _maxi_read_local_size_buf;
          write_burst_done_42 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 1) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_1;
          end 
        end
        write_burst_fsm_0_1: begin
          if(maxi_rvalid) begin
            write_burst_addr_39 <= write_burst_addr_39 + write_burst_stride_40;
            write_burst_length_41 <= write_burst_length_41 - 1;
            write_burst_done_42 <= 0;
          end 
          if(maxi_rvalid && (write_burst_length_41 <= 1)) begin
            write_burst_done_42 <= 1;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_done_42 <= 1;
          end 
          if(maxi_rvalid && (write_burst_length_41 <= 1)) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
          if(0) begin
            write_burst_fsm_0 <= write_burst_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam write_burst_fsm_1_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      write_burst_fsm_1 <= write_burst_fsm_1_init;
      write_burst_addr_45 <= 0;
      write_burst_stride_46 <= 0;
      write_burst_length_47 <= 0;
      write_burst_done_48 <= 0;
    end else begin
      case(write_burst_fsm_1)
        write_burst_fsm_1_init: begin
          write_burst_addr_45 <= _maxi_read_local_addr_buf;
          write_burst_stride_46 <= _maxi_read_local_stride_buf;
          write_burst_length_47 <= _maxi_read_local_size_buf;
          write_burst_done_48 <= 0;
          if((_maxi_read_data_fsm == 1) && (_maxi_read_op_sel_buf == 2) && (_maxi_read_local_size_buf > 0)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_1;
          end 
        end
        write_burst_fsm_1_1: begin
          if(maxi_rvalid) begin
            write_burst_addr_45 <= write_burst_addr_45 + write_burst_stride_46;
            write_burst_length_47 <= write_burst_length_47 - 1;
            write_burst_done_48 <= 0;
          end 
          if(maxi_rvalid && (write_burst_length_47 <= 1)) begin
            write_burst_done_48 <= 1;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_done_48 <= 1;
          end 
          if(maxi_rvalid && (write_burst_length_47 <= 1)) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(maxi_rvalid && 0) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
          if(0) begin
            write_burst_fsm_1 <= write_burst_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _strm_madd_a_source_fsm_0_1 = 1;
  localparam _strm_madd_a_source_fsm_0_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_a_source_fsm_0 <= _strm_madd_a_source_fsm_0_init;
    end else begin
      case(_strm_madd_a_source_fsm_0)
        _strm_madd_a_source_fsm_0_init: begin
          if(_strm_madd_source_start && _strm_madd_a_source_mode & 5'b1 && _strm_madd_stream_oready) begin
            _strm_madd_a_source_fsm_0 <= _strm_madd_a_source_fsm_0_1;
          end 
        end
        _strm_madd_a_source_fsm_0_1: begin
          if(_strm_madd_stream_oready) begin
            _strm_madd_a_source_fsm_0 <= _strm_madd_a_source_fsm_0_2;
          end 
        end
        _strm_madd_a_source_fsm_0_2: begin
          if((_strm_madd_a_source_count == 1) && _strm_madd_stream_oready) begin
            _strm_madd_a_source_fsm_0 <= _strm_madd_a_source_fsm_0_init;
          end 
          if(_strm_madd_source_stop && _strm_madd_stream_oready) begin
            _strm_madd_a_source_fsm_0 <= _strm_madd_a_source_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _strm_madd_b_source_fsm_1_1 = 1;
  localparam _strm_madd_b_source_fsm_1_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_b_source_fsm_1 <= _strm_madd_b_source_fsm_1_init;
    end else begin
      case(_strm_madd_b_source_fsm_1)
        _strm_madd_b_source_fsm_1_init: begin
          if(_strm_madd_source_start && _strm_madd_b_source_mode & 5'b1 && _strm_madd_stream_oready) begin
            _strm_madd_b_source_fsm_1 <= _strm_madd_b_source_fsm_1_1;
          end 
        end
        _strm_madd_b_source_fsm_1_1: begin
          if(_strm_madd_stream_oready) begin
            _strm_madd_b_source_fsm_1 <= _strm_madd_b_source_fsm_1_2;
          end 
        end
        _strm_madd_b_source_fsm_1_2: begin
          if((_strm_madd_b_source_count == 1) && _strm_madd_stream_oready) begin
            _strm_madd_b_source_fsm_1 <= _strm_madd_b_source_fsm_1_init;
          end 
          if(_strm_madd_source_stop && _strm_madd_stream_oready) begin
            _strm_madd_b_source_fsm_1 <= _strm_madd_b_source_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _strm_madd_sum_sink_fsm_2_1 = 1;
  localparam _strm_madd_sum_sink_fsm_2_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _strm_madd_sum_sink_fsm_2 <= _strm_madd_sum_sink_fsm_2_init;
    end else begin
      case(_strm_madd_sum_sink_fsm_2)
        _strm_madd_sum_sink_fsm_2_init: begin
          if(_strm_madd_sink_start && _strm_madd_sum_sink_mode & 5'b1 && _strm_madd_stream_oready) begin
            _strm_madd_sum_sink_fsm_2 <= _strm_madd_sum_sink_fsm_2_1;
          end 
        end
        _strm_madd_sum_sink_fsm_2_1: begin
          if(_strm_madd_stream_oready) begin
            _strm_madd_sum_sink_fsm_2 <= _strm_madd_sum_sink_fsm_2_2;
          end 
        end
        _strm_madd_sum_sink_fsm_2_2: begin
          if(strm_madd_sum_valid_data && (_strm_madd_sum_sink_count == 1) && _strm_madd_stream_oready) begin
            _strm_madd_sum_sink_fsm_2 <= _strm_madd_sum_sink_fsm_2_init;
          end 
          if(_strm_madd_sink_stop && _strm_madd_stream_oready) begin
            _strm_madd_sum_sink_fsm_2 <= _strm_madd_sum_sink_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _maxi_write_req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_write_req_fsm <= _maxi_write_req_fsm_init;
      _maxi_write_cont <= 0;
    end else begin
      case(_maxi_write_req_fsm)
        _maxi_write_req_fsm_init: begin
          if((_maxi_write_req_fsm == 0) && (_maxi_write_start || _maxi_write_cont) && !_maxi_write_req_fifo_almost_full) begin
            _maxi_write_req_fsm <= _maxi_write_req_fsm_1;
          end 
        end
        _maxi_write_req_fsm_1: begin
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6)) begin
            _maxi_write_cont <= 1;
          end 
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6) && (_maxi_write_global_size == 0)) begin
            _maxi_write_cont <= 0;
          end 
          if((_maxi_write_req_fsm == 1) && !_maxi_write_req_fifo_almost_full && (maxi_awready || !maxi_awvalid) && (outstanding_wcount_0 < 6)) begin
            _maxi_write_req_fsm <= _maxi_write_req_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam _maxi_write_data_fsm_1 = 1;
  localparam _maxi_write_data_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      _maxi_write_data_fsm <= _maxi_write_data_fsm_init;
    end else begin
      case(_maxi_write_data_fsm)
        _maxi_write_data_fsm_init: begin
          if(_maxi_write_data_idle && !_maxi_write_req_fifo_empty && (_maxi_write_op_sel_fifo == 1)) begin
            _maxi_write_data_fsm <= _maxi_write_data_fsm_1;
          end 
        end
        _maxi_write_data_fsm_1: begin
          _maxi_write_data_fsm <= _maxi_write_data_fsm_2;
        end
        _maxi_write_data_fsm_2: begin
          if((_maxi_write_op_sel_buf == 1) && read_burst_rvalid_136 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0)) && read_burst_rlast_137) begin
            _maxi_write_data_fsm <= _maxi_write_data_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam read_burst_fsm_2_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      read_burst_fsm_2 <= read_burst_fsm_2_init;
      read_burst_addr_133 <= 0;
      read_burst_stride_134 <= 0;
      read_burst_length_135 <= 0;
      read_burst_rvalid_136 <= 0;
      read_burst_rlast_137 <= 0;
    end else begin
      case(read_burst_fsm_2)
        read_burst_fsm_2_init: begin
          read_burst_addr_133 <= _maxi_write_local_addr_buf;
          read_burst_stride_134 <= _maxi_write_local_stride_buf;
          read_burst_length_135 <= _maxi_write_size_buf;
          read_burst_rvalid_136 <= 0;
          read_burst_rlast_137 <= 0;
          if((_maxi_write_data_fsm == 1) && (_maxi_write_op_sel_buf == 1) && (_maxi_write_size_buf > 0)) begin
            read_burst_fsm_2 <= read_burst_fsm_2_1;
          end 
        end
        read_burst_fsm_2_1: begin
          if((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0) && (read_burst_length_135 > 0)) begin
            read_burst_addr_133 <= read_burst_addr_133 + read_burst_stride_134;
            read_burst_length_135 <= read_burst_length_135 - 1;
            read_burst_rvalid_136 <= 1;
          end 
          if((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0) && (read_burst_length_135 <= 1)) begin
            read_burst_rlast_137 <= 1;
          end 
          if(read_burst_rlast_137 && read_burst_rvalid_136 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) begin
            read_burst_rvalid_136 <= 0;
            read_burst_rlast_137 <= 0;
          end 
          if(0) begin
            read_burst_rvalid_136 <= 0;
            read_burst_rlast_137 <= 0;
          end 
          if(read_burst_rlast_137 && read_burst_rvalid_136 && ((maxi_wready || !maxi_wvalid) && (_maxi_write_size_buf > 0))) begin
            read_burst_fsm_2 <= read_burst_fsm_2_init;
          end 
          if(0) begin
            read_burst_fsm_2 <= read_burst_fsm_2_init;
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
  input ram_a_0_wenable,
  input ram_a_0_enable
);

  reg [32-1:0] ram_a_0_rdata_out;
  assign ram_a_0_rdata = ram_a_0_rdata_out;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_0_enable) begin
      if(ram_a_0_wenable) begin
        mem[ram_a_0_addr] <= ram_a_0_wdata;
        ram_a_0_rdata_out <= ram_a_0_wdata;
      end else begin
        ram_a_0_rdata_out <= mem[ram_a_0_addr];
      end
    end 
  end


endmodule



module ram_b
(
  input CLK,
  input [10-1:0] ram_b_0_addr,
  output [32-1:0] ram_b_0_rdata,
  input [32-1:0] ram_b_0_wdata,
  input ram_b_0_wenable,
  input ram_b_0_enable
);

  reg [32-1:0] ram_b_0_rdata_out;
  assign ram_b_0_rdata = ram_b_0_rdata_out;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_0_enable) begin
      if(ram_b_0_wenable) begin
        mem[ram_b_0_addr] <= ram_b_0_wdata;
        ram_b_0_rdata_out <= ram_b_0_wdata;
      end else begin
        ram_b_0_rdata_out <= mem[ram_b_0_addr];
      end
    end 
  end


endmodule



module ram_c
(
  input CLK,
  input [10-1:0] ram_c_0_addr,
  output [32-1:0] ram_c_0_rdata,
  input [32-1:0] ram_c_0_wdata,
  input ram_c_0_wenable,
  input ram_c_0_enable
);

  reg [32-1:0] ram_c_0_rdata_out;
  assign ram_c_0_rdata = ram_c_0_rdata_out;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_0_enable) begin
      if(ram_c_0_wenable) begin
        mem[ram_c_0_addr] <= ram_c_0_wdata;
        ram_c_0_rdata_out <= ram_c_0_wdata;
      end else begin
        ram_c_0_rdata_out <= mem[ram_c_0_addr];
      end
    end 
  end


endmodule



module _maxi_read_req_fifo
(
  input CLK,
  input RST,
  input _maxi_read_req_fifo_enq,
  input [105-1:0] _maxi_read_req_fifo_wdata,
  output _maxi_read_req_fifo_full,
  output _maxi_read_req_fifo_almost_full,
  input _maxi_read_req_fifo_deq,
  output [105-1:0] _maxi_read_req_fifo_rdata,
  output _maxi_read_req_fifo_empty,
  output _maxi_read_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _maxi_read_req_fifo_full = is_full;
  assign _maxi_read_req_fifo_almost_full = is_almost_full || is_full;
  assign _maxi_read_req_fifo_empty = is_empty;
  assign _maxi_read_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _maxi_read_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_maxi_read_req_fifo_enq && !is_full) begin
        mem[head] <= _maxi_read_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_maxi_read_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


endmodule



module _maxi_write_req_fifo
(
  input CLK,
  input RST,
  input _maxi_write_req_fifo_enq,
  input [105-1:0] _maxi_write_req_fifo_wdata,
  output _maxi_write_req_fifo_full,
  output _maxi_write_req_fifo_almost_full,
  input _maxi_write_req_fifo_deq,
  output [105-1:0] _maxi_write_req_fifo_rdata,
  output _maxi_write_req_fifo_empty,
  output _maxi_write_req_fifo_almost_empty
);

  reg [105-1:0] mem [0:8-1];
  reg [3-1:0] head;
  reg [3-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 7);
  assign is_full = (head + 1 & 7) == tail;
  assign is_almost_full = (head + 2 & 7) == tail;
  wire [105-1:0] rdata;
  assign _maxi_write_req_fifo_full = is_full;
  assign _maxi_write_req_fifo_almost_full = is_almost_full || is_full;
  assign _maxi_write_req_fifo_empty = is_empty;
  assign _maxi_write_req_fifo_almost_empty = is_almost_empty || is_empty;
  assign rdata = mem[tail];
  assign _maxi_write_req_fifo_rdata = rdata;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      tail <= 0;
    end else begin
      if(_maxi_write_req_fifo_enq && !is_full) begin
        mem[head] <= _maxi_write_req_fifo_wdata;
        head <= head + 1;
      end 
      if(_maxi_write_req_fifo_deq && !is_empty) begin
        tail <= tail + 1;
      end 
    end
  end


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
  assign _mul = _a * _b;
  assign c = _pipe_mul0;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
    end 
  end


endmodule

