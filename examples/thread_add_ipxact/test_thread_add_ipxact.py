from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_add_ipxact

expected_verilog = """
module test;

  reg CLK;
  reg RST;
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
  reg [32-1:0] _saxi_awaddr;
  wire [4-1:0] _saxi_awcache;
  wire [3-1:0] _saxi_awprot;
  reg _saxi_awvalid;
  wire _saxi_awready;
  assign _saxi_awcache = 3;
  assign _saxi_awprot = 0;
  wire [32-1:0] _saxi_wdata;
  wire [4-1:0] _saxi_wstrb;
  wire _saxi_wvalid;
  wire _saxi_wready;
  reg [32-1:0] __saxi_wdata_sb_0;
  reg [4-1:0] __saxi_wstrb_sb_0;
  reg __saxi_wvalid_sb_0;
  wire __saxi_wready_sb_0;
  wire [4-1:0] _sb__saxi_writedata_s_value_0;
  assign _sb__saxi_writedata_s_value_0 = __saxi_wstrb_sb_0;
  wire [32-1:0] _sb__saxi_writedata_s_value_1;
  assign _sb__saxi_writedata_s_value_1 = __saxi_wdata_sb_0;
  wire [36-1:0] _sb__saxi_writedata_s_data_2;
  assign _sb__saxi_writedata_s_data_2 = { _sb__saxi_writedata_s_value_0, _sb__saxi_writedata_s_value_1 };
  wire _sb__saxi_writedata_s_valid_3;
  assign _sb__saxi_writedata_s_valid_3 = __saxi_wvalid_sb_0;
  wire _sb__saxi_writedata_m_ready_4;
  assign _sb__saxi_writedata_m_ready_4 = _saxi_wready;
  reg [36-1:0] _sb__saxi_writedata_data_5;
  reg _sb__saxi_writedata_valid_6;
  wire _sb__saxi_writedata_ready_7;
  reg [36-1:0] _sb__saxi_writedata_tmp_data_8;
  reg _sb__saxi_writedata_tmp_valid_9;
  wire [36-1:0] _sb__saxi_writedata_next_data_10;
  wire _sb__saxi_writedata_next_valid_11;
  assign _sb__saxi_writedata_ready_7 = !_sb__saxi_writedata_tmp_valid_9;
  assign _sb__saxi_writedata_next_data_10 = (_sb__saxi_writedata_tmp_valid_9)? _sb__saxi_writedata_tmp_data_8 : _sb__saxi_writedata_s_data_2;
  assign _sb__saxi_writedata_next_valid_11 = _sb__saxi_writedata_tmp_valid_9 || _sb__saxi_writedata_s_valid_3;
  wire [4-1:0] _sb__saxi_writedata_m_value_12;
  assign _sb__saxi_writedata_m_value_12 = _sb__saxi_writedata_data_5[35:32];
  wire [32-1:0] _sb__saxi_writedata_m_value_13;
  assign _sb__saxi_writedata_m_value_13 = _sb__saxi_writedata_data_5[31:0];
  assign __saxi_wready_sb_0 = _sb__saxi_writedata_ready_7;
  assign _saxi_wdata = _sb__saxi_writedata_m_value_13;
  assign _saxi_wstrb = _sb__saxi_writedata_m_value_12;
  assign _saxi_wvalid = _sb__saxi_writedata_valid_6;
  wire [2-1:0] _saxi_bresp;
  wire _saxi_bvalid;
  wire _saxi_bready;
  assign _saxi_bready = 1;
  reg [32-1:0] _saxi_araddr;
  wire [4-1:0] _saxi_arcache;
  wire [3-1:0] _saxi_arprot;
  reg _saxi_arvalid;
  wire _saxi_arready;
  assign _saxi_arcache = 3;
  assign _saxi_arprot = 0;
  wire [32-1:0] _saxi_rdata;
  wire [2-1:0] _saxi_rresp;
  wire _saxi_rvalid;
  wire _saxi_rready;
  wire [32-1:0] __saxi_rdata_sb_0;
  wire __saxi_rvalid_sb_0;
  wire __saxi_rready_sb_0;
  wire [32-1:0] _sb__saxi_readdata_s_value_14;
  assign _sb__saxi_readdata_s_value_14 = _saxi_rdata;
  wire [32-1:0] _sb__saxi_readdata_s_data_15;
  assign _sb__saxi_readdata_s_data_15 = { _sb__saxi_readdata_s_value_14 };
  wire _sb__saxi_readdata_s_valid_16;
  assign _sb__saxi_readdata_s_valid_16 = _saxi_rvalid;
  wire _sb__saxi_readdata_m_ready_17;
  assign _sb__saxi_readdata_m_ready_17 = __saxi_rready_sb_0;
  reg [32-1:0] _sb__saxi_readdata_data_18;
  reg _sb__saxi_readdata_valid_19;
  wire _sb__saxi_readdata_ready_20;
  reg [32-1:0] _sb__saxi_readdata_tmp_data_21;
  reg _sb__saxi_readdata_tmp_valid_22;
  wire [32-1:0] _sb__saxi_readdata_next_data_23;
  wire _sb__saxi_readdata_next_valid_24;
  assign _sb__saxi_readdata_ready_20 = !_sb__saxi_readdata_tmp_valid_22;
  assign _sb__saxi_readdata_next_data_23 = (_sb__saxi_readdata_tmp_valid_22)? _sb__saxi_readdata_tmp_data_21 : _sb__saxi_readdata_s_data_15;
  assign _sb__saxi_readdata_next_valid_24 = _sb__saxi_readdata_tmp_valid_22 || _sb__saxi_readdata_s_valid_16;
  wire [32-1:0] _sb__saxi_readdata_m_value_25;
  assign _sb__saxi_readdata_m_value_25 = _sb__saxi_readdata_data_18[31:0];
  assign __saxi_rdata_sb_0 = _sb__saxi_readdata_m_value_25;
  assign __saxi_rvalid_sb_0 = _sb__saxi_readdata_valid_19;
  assign _saxi_rready = _sb__saxi_readdata_ready_20;
  reg [3-1:0] __saxi_outstanding_wcount;
  wire __saxi_has_outstanding_write;
  assign __saxi_has_outstanding_write = (__saxi_outstanding_wcount > 0) || _saxi_awvalid;
  wire [32-1:0] _tmp_26;
  assign _tmp_26 = _saxi_awaddr;

  always @(*) begin
    saxi_awaddr = _tmp_26;
  end

  wire [4-1:0] _tmp_27;
  assign _tmp_27 = _saxi_awcache;

  always @(*) begin
    saxi_awcache = _tmp_27;
  end

  wire [3-1:0] _tmp_28;
  assign _tmp_28 = _saxi_awprot;

  always @(*) begin
    saxi_awprot = _tmp_28;
  end

  wire _tmp_29;
  assign _tmp_29 = _saxi_awvalid;

  always @(*) begin
    saxi_awvalid = _tmp_29;
  end

  assign _saxi_awready = saxi_awready;
  wire [32-1:0] _tmp_30;
  assign _tmp_30 = _saxi_wdata;

  always @(*) begin
    saxi_wdata = _tmp_30;
  end

  wire [4-1:0] _tmp_31;
  assign _tmp_31 = _saxi_wstrb;

  always @(*) begin
    saxi_wstrb = _tmp_31;
  end

  wire _tmp_32;
  assign _tmp_32 = _saxi_wvalid;

  always @(*) begin
    saxi_wvalid = _tmp_32;
  end

  assign _saxi_wready = saxi_wready;
  assign _saxi_bresp = saxi_bresp;
  assign _saxi_bvalid = saxi_bvalid;
  wire _tmp_33;
  assign _tmp_33 = _saxi_bready;

  always @(*) begin
    saxi_bready = _tmp_33;
  end

  wire [32-1:0] _tmp_34;
  assign _tmp_34 = _saxi_araddr;

  always @(*) begin
    saxi_araddr = _tmp_34;
  end

  wire [4-1:0] _tmp_35;
  assign _tmp_35 = _saxi_arcache;

  always @(*) begin
    saxi_arcache = _tmp_35;
  end

  wire [3-1:0] _tmp_36;
  assign _tmp_36 = _saxi_arprot;

  always @(*) begin
    saxi_arprot = _tmp_36;
  end

  wire _tmp_37;
  assign _tmp_37 = _saxi_arvalid;

  always @(*) begin
    saxi_arvalid = _tmp_37;
  end

  assign _saxi_arready = saxi_arready;
  assign _saxi_rdata = saxi_rdata;
  assign _saxi_rresp = saxi_rresp;
  assign _saxi_rvalid = saxi_rvalid;
  wire _tmp_38;
  assign _tmp_38 = _saxi_rready;

  always @(*) begin
    saxi_rready = _tmp_38;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_3;
  reg signed [32-1:0] _th_ctrl_awaddr_4;
  reg signed [32-1:0] _th_ctrl_a_5;
  reg __saxi_waddr_cond_0_1;
  reg __saxi_wdata_cond_0_1;
  reg signed [32-1:0] _th_ctrl_b_6;
  reg __saxi_waddr_cond_1_1;
  reg __saxi_wdata_cond_1_1;
  reg signed [32-1:0] _th_ctrl_start_time_7;
  reg __saxi_waddr_cond_2_1;
  reg __saxi_wdata_cond_2_1;
  reg signed [32-1:0] _th_ctrl_araddr_8;
  reg __saxi_raddr_cond_0_1;
  reg signed [32-1:0] axim_rdata_39;
  reg signed [32-1:0] _th_ctrl_busy_9;
  reg __saxi_raddr_cond_1_1;
  reg signed [32-1:0] axim_rdata_40;
  assign __saxi_rready_sb_0 = (th_ctrl == 32) || (th_ctrl == 40);
  reg signed [32-1:0] _th_ctrl_c_10;
  reg signed [32-1:0] _th_ctrl_end_time_11;
  reg signed [32-1:0] _th_ctrl_time_12;

  add
  uut
  (
    .CLK(CLK),
    .RST(RST),
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
    $dumpfile("thread_add_ipxact.vcd");
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
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    __saxi_wdata_sb_0 = 0;
    __saxi_wstrb_sb_0 = 0;
    __saxi_wvalid_sb_0 = 0;
    _sb__saxi_writedata_data_5 = 0;
    _sb__saxi_writedata_valid_6 = 0;
    _sb__saxi_writedata_tmp_data_8 = 0;
    _sb__saxi_writedata_tmp_valid_9 = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    _sb__saxi_readdata_data_18 = 0;
    _sb__saxi_readdata_valid_19 = 0;
    _sb__saxi_readdata_tmp_data_21 = 0;
    _sb__saxi_readdata_tmp_valid_22 = 0;
    __saxi_outstanding_wcount = 0;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_3 = 0;
    _th_ctrl_awaddr_4 = 0;
    _th_ctrl_a_5 = 0;
    __saxi_waddr_cond_0_1 = 0;
    __saxi_wdata_cond_0_1 = 0;
    _th_ctrl_b_6 = 0;
    __saxi_waddr_cond_1_1 = 0;
    __saxi_wdata_cond_1_1 = 0;
    _th_ctrl_start_time_7 = 0;
    __saxi_waddr_cond_2_1 = 0;
    __saxi_wdata_cond_2_1 = 0;
    _th_ctrl_araddr_8 = 0;
    __saxi_raddr_cond_0_1 = 0;
    axim_rdata_39 = 0;
    _th_ctrl_busy_9 = 0;
    __saxi_raddr_cond_1_1 = 0;
    axim_rdata_40 = 0;
    _th_ctrl_c_10 = 0;
    _th_ctrl_end_time_11 = 0;
    _th_ctrl_time_12 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      _saxi_awaddr <= 0;
      _saxi_awvalid <= 0;
      __saxi_waddr_cond_0_1 <= 0;
      __saxi_waddr_cond_1_1 <= 0;
      __saxi_waddr_cond_2_1 <= 0;
    end else begin
      if(__saxi_waddr_cond_0_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_waddr_cond_1_1) begin
        _saxi_awvalid <= 0;
      end 
      if(__saxi_waddr_cond_2_1) begin
        _saxi_awvalid <= 0;
      end 
      if((th_ctrl == 7) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 15) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_1_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 23) && ((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_waddr_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __saxi_wdata_sb_0 <= 0;
      __saxi_wvalid_sb_0 <= 0;
      __saxi_wstrb_sb_0 <= 0;
      __saxi_wdata_cond_0_1 <= 0;
      __saxi_wdata_cond_1_1 <= 0;
      __saxi_wdata_cond_2_1 <= 0;
    end else begin
      if(__saxi_wdata_cond_0_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if(__saxi_wdata_cond_1_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if(__saxi_wdata_cond_2_1) begin
        __saxi_wvalid_sb_0 <= 0;
      end 
      if((th_ctrl == 9) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= _th_ctrl_a_5;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_0_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
      if((th_ctrl == 17) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= _th_ctrl_b_6;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_1_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
      if((th_ctrl == 25) && (__saxi_wready_sb_0 || !__saxi_wvalid_sb_0)) begin
        __saxi_wdata_sb_0 <= 1;
        __saxi_wvalid_sb_0 <= 1;
        __saxi_wstrb_sb_0 <= { 4{ 1'd1 } };
      end 
      __saxi_wdata_cond_2_1 <= 1;
      if(__saxi_wvalid_sb_0 && !__saxi_wready_sb_0) begin
        __saxi_wvalid_sb_0 <= __saxi_wvalid_sb_0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb__saxi_writedata_data_5 <= 0;
      _sb__saxi_writedata_valid_6 <= 0;
      _sb__saxi_writedata_tmp_data_8 <= 0;
      _sb__saxi_writedata_tmp_valid_9 <= 0;
    end else begin
      if(_sb__saxi_writedata_m_ready_4 || !_sb__saxi_writedata_valid_6) begin
        _sb__saxi_writedata_data_5 <= _sb__saxi_writedata_next_data_10;
        _sb__saxi_writedata_valid_6 <= _sb__saxi_writedata_next_valid_11;
      end 
      if(!_sb__saxi_writedata_tmp_valid_9 && _sb__saxi_writedata_valid_6 && !_sb__saxi_writedata_m_ready_4) begin
        _sb__saxi_writedata_tmp_data_8 <= _sb__saxi_writedata_s_data_2;
        _sb__saxi_writedata_tmp_valid_9 <= _sb__saxi_writedata_s_valid_3;
      end 
      if(_sb__saxi_writedata_tmp_valid_9 && _sb__saxi_writedata_m_ready_4) begin
        _sb__saxi_writedata_tmp_valid_9 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_raddr_cond_0_1 <= 0;
      __saxi_raddr_cond_1_1 <= 0;
    end else begin
      if(__saxi_raddr_cond_0_1) begin
        _saxi_arvalid <= 0;
      end 
      if(__saxi_raddr_cond_1_1) begin
        _saxi_arvalid <= 0;
      end 
      if((th_ctrl == 30) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_8;
        _saxi_arvalid <= 1;
      end 
      __saxi_raddr_cond_0_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
      if((th_ctrl == 38) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_8;
        _saxi_arvalid <= 1;
      end 
      __saxi_raddr_cond_1_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _sb__saxi_readdata_data_18 <= 0;
      _sb__saxi_readdata_valid_19 <= 0;
      _sb__saxi_readdata_tmp_data_21 <= 0;
      _sb__saxi_readdata_tmp_valid_22 <= 0;
    end else begin
      if(_sb__saxi_readdata_m_ready_17 || !_sb__saxi_readdata_valid_19) begin
        _sb__saxi_readdata_data_18 <= _sb__saxi_readdata_next_data_23;
        _sb__saxi_readdata_valid_19 <= _sb__saxi_readdata_next_valid_24;
      end 
      if(!_sb__saxi_readdata_tmp_valid_22 && _sb__saxi_readdata_valid_19 && !_sb__saxi_readdata_m_ready_17) begin
        _sb__saxi_readdata_tmp_data_21 <= _sb__saxi_readdata_s_data_15;
        _sb__saxi_readdata_tmp_valid_22 <= _sb__saxi_readdata_s_valid_16;
      end 
      if(_sb__saxi_readdata_tmp_valid_22 && _sb__saxi_readdata_m_ready_17) begin
        _sb__saxi_readdata_tmp_valid_22 <= 0;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __saxi_outstanding_wcount <= 0;
    end else begin
      if(_saxi_awvalid && _saxi_awready && !(_saxi_bvalid && _saxi_bready) && (__saxi_outstanding_wcount < 7)) begin
        __saxi_outstanding_wcount <= __saxi_outstanding_wcount + 1;
      end 
      if(!(_saxi_awvalid && _saxi_awready) && (_saxi_bvalid && _saxi_bready) && (__saxi_outstanding_wcount > 0)) begin
        __saxi_outstanding_wcount <= __saxi_outstanding_wcount - 1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_3 <= 0;
      _th_ctrl_awaddr_4 <= 0;
      _th_ctrl_a_5 <= 0;
      _th_ctrl_b_6 <= 0;
      _th_ctrl_start_time_7 <= 0;
      _th_ctrl_araddr_8 <= 0;
      axim_rdata_39 <= 0;
      _th_ctrl_busy_9 <= 0;
      axim_rdata_40 <= 0;
      _th_ctrl_c_10 <= 0;
      _th_ctrl_end_time_11 <= 0;
      _th_ctrl_time_12 <= 0;
    end else begin
      case(th_ctrl)
        th_ctrl_init: begin
          th_ctrl <= th_ctrl_1;
        end
        th_ctrl_1: begin
          _th_ctrl_i_3 <= 0;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_2: begin
          if(_th_ctrl_i_3 < 100) begin
            th_ctrl <= th_ctrl_3;
          end else begin
            th_ctrl <= th_ctrl_4;
          end
        end
        th_ctrl_3: begin
          _th_ctrl_i_3 <= _th_ctrl_i_3 + 1;
          th_ctrl <= th_ctrl_2;
        end
        th_ctrl_4: begin
          _th_ctrl_awaddr_4 <= 8;
          th_ctrl <= th_ctrl_5;
        end
        th_ctrl_5: begin
          _th_ctrl_a_5 <= 10;
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          $display("# a = %d", _th_ctrl_a_5);
          th_ctrl <= th_ctrl_7;
        end
        th_ctrl_7: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_8;
          end 
        end
        th_ctrl_8: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_10;
          end 
        end
        th_ctrl_10: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_11;
          end 
        end
        th_ctrl_11: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_12;
          end 
        end
        th_ctrl_12: begin
          _th_ctrl_awaddr_4 <= 12;
          th_ctrl <= th_ctrl_13;
        end
        th_ctrl_13: begin
          _th_ctrl_b_6 <= 20;
          th_ctrl <= th_ctrl_14;
        end
        th_ctrl_14: begin
          $display("# b = %d", _th_ctrl_b_6);
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_16;
          end 
        end
        th_ctrl_16: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_17;
          end 
        end
        th_ctrl_17: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_18;
          end 
        end
        th_ctrl_18: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_20;
          end 
        end
        th_ctrl_20: begin
          _th_ctrl_awaddr_4 <= 0;
          th_ctrl <= th_ctrl_21;
        end
        th_ctrl_21: begin
          _th_ctrl_start_time_7 <= counter;
          th_ctrl <= th_ctrl_22;
        end
        th_ctrl_22: begin
          $display("# start time = %d", _th_ctrl_start_time_7);
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_23: begin
          if((__saxi_outstanding_wcount == 0) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_24;
          end 
        end
        th_ctrl_24: begin
          if(_saxi_awvalid && _saxi_awready) begin
            th_ctrl <= th_ctrl_25;
          end 
        end
        th_ctrl_25: begin
          if(__saxi_wready_sb_0 || !__saxi_wvalid_sb_0) begin
            th_ctrl <= th_ctrl_26;
          end 
        end
        th_ctrl_26: begin
          if(__saxi_wvalid_sb_0 && __saxi_wready_sb_0) begin
            th_ctrl <= th_ctrl_27;
          end 
        end
        th_ctrl_27: begin
          if(!__saxi_has_outstanding_write) begin
            th_ctrl <= th_ctrl_28;
          end 
        end
        th_ctrl_28: begin
          _th_ctrl_araddr_8 <= 4;
          th_ctrl <= th_ctrl_29;
        end
        th_ctrl_29: begin
          if(1) begin
            th_ctrl <= th_ctrl_30;
          end else begin
            th_ctrl <= th_ctrl_37;
          end
        end
        th_ctrl_30: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_31;
          end 
        end
        th_ctrl_31: begin
          if(_saxi_arvalid && _saxi_arready) begin
            th_ctrl <= th_ctrl_32;
          end 
        end
        th_ctrl_32: begin
          if(__saxi_rvalid_sb_0) begin
            axim_rdata_39 <= __saxi_rdata_sb_0;
          end 
          if(__saxi_rvalid_sb_0) begin
            th_ctrl <= th_ctrl_33;
          end 
        end
        th_ctrl_33: begin
          _th_ctrl_busy_9 <= axim_rdata_39;
          th_ctrl <= th_ctrl_34;
        end
        th_ctrl_34: begin
          if(!_th_ctrl_busy_9) begin
            th_ctrl <= th_ctrl_35;
          end else begin
            th_ctrl <= th_ctrl_36;
          end
        end
        th_ctrl_35: begin
          th_ctrl <= th_ctrl_37;
        end
        th_ctrl_36: begin
          th_ctrl <= th_ctrl_29;
        end
        th_ctrl_37: begin
          _th_ctrl_araddr_8 <= 16;
          th_ctrl <= th_ctrl_38;
        end
        th_ctrl_38: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_39;
          end 
        end
        th_ctrl_39: begin
          if(_saxi_arvalid && _saxi_arready) begin
            th_ctrl <= th_ctrl_40;
          end 
        end
        th_ctrl_40: begin
          if(__saxi_rvalid_sb_0) begin
            axim_rdata_40 <= __saxi_rdata_sb_0;
          end 
          if(__saxi_rvalid_sb_0) begin
            th_ctrl <= th_ctrl_41;
          end 
        end
        th_ctrl_41: begin
          _th_ctrl_c_10 <= axim_rdata_40;
          th_ctrl <= th_ctrl_42;
        end
        th_ctrl_42: begin
          $display("# c = %d", _th_ctrl_c_10);
          th_ctrl <= th_ctrl_43;
        end
        th_ctrl_43: begin
          _th_ctrl_end_time_11 <= counter;
          th_ctrl <= th_ctrl_44;
        end
        th_ctrl_44: begin
          $display("# end time = %d", _th_ctrl_end_time_11);
          th_ctrl <= th_ctrl_45;
        end
        th_ctrl_45: begin
          _th_ctrl_time_12 <= _th_ctrl_end_time_11 - _th_ctrl_start_time_7;
          th_ctrl <= th_ctrl_46;
        end
        th_ctrl_46: begin
          $display("# exec time = %d", _th_ctrl_time_12);
          th_ctrl <= th_ctrl_47;
        end
      endcase
    end
  end


endmodule



module add
(
  input CLK,
  input RST,
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
  reg [32-1:0] addr_0;
  reg writevalid_1;
  reg readvalid_2;
  reg prev_awvalid_3;
  reg prev_arvalid_4;
  assign saxi_awready = (_saxi_register_fsm == 0) && (!writevalid_1 && !readvalid_2 && !saxi_bvalid && prev_awvalid_3);
  assign saxi_arready = (_saxi_register_fsm == 0) && (!readvalid_2 && !writevalid_1 && prev_arvalid_4 && !prev_awvalid_3);
  reg [_saxi_maskwidth-1:0] axis_maskaddr_5;
  wire signed [32-1:0] axislite_rdata_6;
  assign axislite_rdata_6 = (axis_maskaddr_5 == 0)? _saxi_register_0 : 
                            (axis_maskaddr_5 == 1)? _saxi_register_1 : 
                            (axis_maskaddr_5 == 2)? _saxi_register_2 : 
                            (axis_maskaddr_5 == 3)? _saxi_register_3 : 
                            (axis_maskaddr_5 == 4)? _saxi_register_4 : 
                            (axis_maskaddr_5 == 5)? _saxi_register_5 : 
                            (axis_maskaddr_5 == 6)? _saxi_register_6 : 
                            (axis_maskaddr_5 == 7)? _saxi_register_7 : 'hx;
  wire axislite_flag_7;
  assign axislite_flag_7 = (axis_maskaddr_5 == 0)? _saxi_flag_0 : 
                           (axis_maskaddr_5 == 1)? _saxi_flag_1 : 
                           (axis_maskaddr_5 == 2)? _saxi_flag_2 : 
                           (axis_maskaddr_5 == 3)? _saxi_flag_3 : 
                           (axis_maskaddr_5 == 4)? _saxi_flag_4 : 
                           (axis_maskaddr_5 == 5)? _saxi_flag_5 : 
                           (axis_maskaddr_5 == 6)? _saxi_flag_6 : 
                           (axis_maskaddr_5 == 7)? _saxi_flag_7 : 'hx;
  wire signed [32-1:0] axislite_resetval_8;
  assign axislite_resetval_8 = (axis_maskaddr_5 == 0)? _saxi_resetval_0 : 
                               (axis_maskaddr_5 == 1)? _saxi_resetval_1 : 
                               (axis_maskaddr_5 == 2)? _saxi_resetval_2 : 
                               (axis_maskaddr_5 == 3)? _saxi_resetval_3 : 
                               (axis_maskaddr_5 == 4)? _saxi_resetval_4 : 
                               (axis_maskaddr_5 == 5)? _saxi_resetval_5 : 
                               (axis_maskaddr_5 == 6)? _saxi_resetval_6 : 
                               (axis_maskaddr_5 == 7)? _saxi_resetval_7 : 'hx;
  reg _saxi_rdata_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 3;
  reg [32-1:0] th_add;
  localparam th_add_init = 0;
  reg signed [32-1:0] _th_add_a_0;
  reg signed [32-1:0] _th_add_b_1;
  reg signed [32-1:0] _th_add_c_2;

  always @(posedge CLK) begin
    if(RST) begin
      saxi_rdata <= 0;
      saxi_rvalid <= 0;
      _saxi_rdata_cond_0_1 <= 0;
    end else begin
      if(_saxi_rdata_cond_0_1) begin
        saxi_rvalid <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_6;
        saxi_rvalid <= 1;
      end 
      _saxi_rdata_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_3 <= 0;
      prev_arvalid_4 <= 0;
      writevalid_1 <= 0;
      readvalid_2 <= 0;
      addr_0 <= 0;
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
      if(saxi_bvalid && saxi_bready) begin
        saxi_bvalid <= 0;
      end 
      if(saxi_wvalid && saxi_wready) begin
        saxi_bvalid <= 1;
      end 
      prev_awvalid_3 <= saxi_awvalid;
      prev_arvalid_4 <= saxi_arvalid;
      writevalid_1 <= 0;
      readvalid_2 <= 0;
      if(saxi_awready && saxi_awvalid && !saxi_bvalid) begin
        addr_0 <= saxi_awaddr;
        writevalid_1 <= 1;
      end else if(saxi_arready && saxi_arvalid) begin
        addr_0 <= saxi_araddr;
        readvalid_2 <= 1;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 0)) begin
        _saxi_register_0 <= axislite_resetval_8;
        _saxi_flag_0 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 1)) begin
        _saxi_register_1 <= axislite_resetval_8;
        _saxi_flag_1 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 2)) begin
        _saxi_register_2 <= axislite_resetval_8;
        _saxi_flag_2 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 3)) begin
        _saxi_register_3 <= axislite_resetval_8;
        _saxi_flag_3 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 4)) begin
        _saxi_register_4 <= axislite_resetval_8;
        _saxi_flag_4 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 5)) begin
        _saxi_register_5 <= axislite_resetval_8;
        _saxi_flag_5 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 6)) begin
        _saxi_register_6 <= axislite_resetval_8;
        _saxi_flag_6 <= 0;
      end 
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid) && axislite_flag_7 && (axis_maskaddr_5 == 7)) begin
        _saxi_register_7 <= axislite_resetval_8;
        _saxi_flag_7 <= 0;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 4)) begin
        _saxi_register_4 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 5)) begin
        _saxi_register_5 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 6)) begin
        _saxi_register_6 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 3) && saxi_wvalid && (axis_maskaddr_5 == 7)) begin
        _saxi_register_7 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_4 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_5 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_6 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_add == 2) && 0) begin
        _saxi_register_7 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 0;
      end 
      if((th_add == 3) && 1) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_4 <= 1;
        _saxi_flag_4 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_5 <= 1;
        _saxi_flag_5 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_6 <= 1;
        _saxi_flag_6 <= 0;
      end 
      if((th_add == 3) && 0) begin
        _saxi_register_7 <= 1;
        _saxi_flag_7 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_0 <= _th_add_c_2;
        _saxi_flag_0 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_1 <= _th_add_c_2;
        _saxi_flag_1 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_2 <= _th_add_c_2;
        _saxi_flag_2 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_3 <= _th_add_c_2;
        _saxi_flag_3 <= 0;
      end 
      if((th_add == 7) && 1) begin
        _saxi_register_4 <= _th_add_c_2;
        _saxi_flag_4 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_5 <= _th_add_c_2;
        _saxi_flag_5 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_6 <= _th_add_c_2;
        _saxi_flag_6 <= 0;
      end 
      if((th_add == 7) && 0) begin
        _saxi_register_7 <= _th_add_c_2;
        _saxi_flag_7 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_add == 8) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_4 <= 0;
        _saxi_flag_4 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_5 <= 0;
        _saxi_flag_5 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_6 <= 0;
        _saxi_flag_6 <= 0;
      end 
      if((th_add == 8) && 0) begin
        _saxi_register_7 <= 0;
        _saxi_flag_7 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;
  localparam _saxi_register_fsm_3 = 3;
  localparam _saxi_register_fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      _saxi_register_fsm <= _saxi_register_fsm_init;
      axis_maskaddr_5 <= 0;
    end else begin
      case(_saxi_register_fsm)
        _saxi_register_fsm_init: begin
          if(readvalid_2 || writevalid_1) begin
            axis_maskaddr_5 <= (addr_0 >> _saxi_shift) & _saxi_mask;
          end 
          if(readvalid_2) begin
            _saxi_register_fsm <= _saxi_register_fsm_1;
          end 
          if(writevalid_1) begin
            _saxi_register_fsm <= _saxi_register_fsm_3;
          end 
        end
        _saxi_register_fsm_1: begin
          if(saxi_rready || !saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_2;
          end 
        end
        _saxi_register_fsm_2: begin
          if(saxi_rready && saxi_rvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
        _saxi_register_fsm_3: begin
          if(saxi_wvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_4;
          end 
        end
        _saxi_register_fsm_4: begin
          if(saxi_bready && saxi_bvalid) begin
            _saxi_register_fsm <= _saxi_register_fsm_init;
          end 
        end
      endcase
    end
  end

  localparam th_add_1 = 1;
  localparam th_add_2 = 2;
  localparam th_add_3 = 3;
  localparam th_add_4 = 4;
  localparam th_add_5 = 5;
  localparam th_add_6 = 6;
  localparam th_add_7 = 7;
  localparam th_add_8 = 8;
  localparam th_add_9 = 9;
  localparam th_add_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      th_add <= th_add_init;
      _th_add_a_0 <= 0;
      _th_add_b_1 <= 0;
      _th_add_c_2 <= 0;
    end else begin
      case(th_add)
        th_add_init: begin
          th_add <= th_add_1;
        end
        th_add_1: begin
          if(1) begin
            th_add <= th_add_2;
          end else begin
            th_add <= th_add_10;
          end
        end
        th_add_2: begin
          if(_saxi_register_0 == 1) begin
            th_add <= th_add_3;
          end 
        end
        th_add_3: begin
          th_add <= th_add_4;
        end
        th_add_4: begin
          _th_add_a_0 <= _saxi_register_2;
          th_add <= th_add_5;
        end
        th_add_5: begin
          _th_add_b_1 <= _saxi_register_3;
          th_add <= th_add_6;
        end
        th_add_6: begin
          _th_add_c_2 <= _th_add_a_0 + _th_add_b_1;
          th_add <= th_add_7;
        end
        th_add_7: begin
          th_add <= th_add_8;
        end
        th_add_8: begin
          th_add <= th_add_9;
        end
        th_add_9: begin
          th_add <= th_add_1;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_add_ipxact.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
