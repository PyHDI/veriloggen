from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_axi_slave_ipxact

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] led;
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
  reg [3-1:0] outstanding_wcount_0;
  wire [32-1:0] _tmp_1;
  assign _tmp_1 = _saxi_awaddr;

  always @(*) begin
    saxi_awaddr = _tmp_1;
  end

  wire [4-1:0] _tmp_2;
  assign _tmp_2 = _saxi_awcache;

  always @(*) begin
    saxi_awcache = _tmp_2;
  end

  wire [3-1:0] _tmp_3;
  assign _tmp_3 = _saxi_awprot;

  always @(*) begin
    saxi_awprot = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = _saxi_awvalid;

  always @(*) begin
    saxi_awvalid = _tmp_4;
  end

  assign _saxi_awready = saxi_awready;
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _saxi_wdata;

  always @(*) begin
    saxi_wdata = _tmp_5;
  end

  wire [4-1:0] _tmp_6;
  assign _tmp_6 = _saxi_wstrb;

  always @(*) begin
    saxi_wstrb = _tmp_6;
  end

  wire _tmp_7;
  assign _tmp_7 = _saxi_wvalid;

  always @(*) begin
    saxi_wvalid = _tmp_7;
  end

  assign _saxi_wready = saxi_wready;
  assign _saxi_bresp = saxi_bresp;
  assign _saxi_bvalid = saxi_bvalid;
  wire _tmp_8;
  assign _tmp_8 = _saxi_bready;

  always @(*) begin
    saxi_bready = _tmp_8;
  end

  wire [32-1:0] _tmp_9;
  assign _tmp_9 = _saxi_araddr;

  always @(*) begin
    saxi_araddr = _tmp_9;
  end

  wire [4-1:0] _tmp_10;
  assign _tmp_10 = _saxi_arcache;

  always @(*) begin
    saxi_arcache = _tmp_10;
  end

  wire [3-1:0] _tmp_11;
  assign _tmp_11 = _saxi_arprot;

  always @(*) begin
    saxi_arprot = _tmp_11;
  end

  wire _tmp_12;
  assign _tmp_12 = _saxi_arvalid;

  always @(*) begin
    saxi_arvalid = _tmp_12;
  end

  assign _saxi_arready = saxi_arready;
  assign _saxi_rdata = saxi_rdata;
  assign _saxi_rresp = saxi_rresp;
  assign _saxi_rvalid = saxi_rvalid;
  wire _tmp_13;
  assign _tmp_13 = _saxi_rready;

  always @(*) begin
    saxi_rready = _tmp_13;
  end

  reg [32-1:0] counter;
  reg [32-1:0] th_ctrl;
  localparam th_ctrl_init = 0;
  reg signed [32-1:0] _th_ctrl_i_3;
  reg signed [32-1:0] _th_ctrl_awaddr_4;
  reg signed [32-1:0] _th_ctrl_sleep_5;
  reg __saxi_cond_0_1;
  reg __saxi_cond_1_1;
  reg signed [32-1:0] _th_ctrl_size_6;
  reg __saxi_cond_2_1;
  reg __saxi_cond_3_1;
  reg signed [32-1:0] _th_ctrl_start_time_7;
  reg __saxi_cond_4_1;
  reg __saxi_cond_5_1;
  reg signed [32-1:0] _th_ctrl_araddr_8;
  reg __saxi_cond_6_1;
  reg signed [32-1:0] axim_rdata_14;
  assign _saxi_rready = th_ctrl == 26;
  reg signed [32-1:0] _th_ctrl_busy_9;
  reg signed [32-1:0] _th_ctrl_end_time_10;
  reg signed [32-1:0] _th_ctrl_time_11;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .led(led),
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
    _saxi_awaddr = 0;
    _saxi_awvalid = 0;
    _saxi_wdata = 0;
    _saxi_wstrb = 0;
    _saxi_wvalid = 0;
    _saxi_araddr = 0;
    _saxi_arvalid = 0;
    outstanding_wcount_0 = 0;
    counter = 0;
    th_ctrl = th_ctrl_init;
    _th_ctrl_i_3 = 0;
    _th_ctrl_awaddr_4 = 0;
    _th_ctrl_sleep_5 = 0;
    __saxi_cond_0_1 = 0;
    __saxi_cond_1_1 = 0;
    _th_ctrl_size_6 = 0;
    __saxi_cond_2_1 = 0;
    __saxi_cond_3_1 = 0;
    _th_ctrl_start_time_7 = 0;
    __saxi_cond_4_1 = 0;
    __saxi_cond_5_1 = 0;
    _th_ctrl_araddr_8 = 0;
    __saxi_cond_6_1 = 0;
    axim_rdata_14 = 0;
    _th_ctrl_busy_9 = 0;
    _th_ctrl_end_time_10 = 0;
    _th_ctrl_time_11 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wcount_0 <= 0;
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
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_6_1 <= 0;
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
        _saxi_arvalid <= 0;
      end 
      if(_saxi_wvalid && _saxi_wready && !(_saxi_bvalid && _saxi_bready) && (outstanding_wcount_0 < 7)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 + 1;
      end 
      if(!(_saxi_wvalid && _saxi_wready) && (_saxi_bvalid && _saxi_bready) && (outstanding_wcount_0 > 0)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 - 1;
      end 
      if((th_ctrl == 7) && ((outstanding_wcount_0 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 9) && ((outstanding_wcount_0 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= _th_ctrl_sleep_5;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 13) && ((outstanding_wcount_0 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 15) && ((outstanding_wcount_0 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= _th_ctrl_size_6;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 19) && ((outstanding_wcount_0 < 6) && (_saxi_awready || !_saxi_awvalid))) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 21) && ((outstanding_wcount_0 < 6) && (_saxi_wready || !_saxi_wvalid))) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_5_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 24) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_8;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_6_1 <= 1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_3 <= 0;
      _th_ctrl_awaddr_4 <= 0;
      _th_ctrl_sleep_5 <= 0;
      _th_ctrl_size_6 <= 0;
      _th_ctrl_start_time_7 <= 0;
      _th_ctrl_araddr_8 <= 0;
      axim_rdata_14 <= 0;
      _th_ctrl_busy_9 <= 0;
      _th_ctrl_end_time_10 <= 0;
      _th_ctrl_time_11 <= 0;
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
          _th_ctrl_sleep_5 <= 16;
          th_ctrl <= th_ctrl_6;
        end
        th_ctrl_6: begin
          $display("# sleep = %d", _th_ctrl_sleep_5);
          th_ctrl <= th_ctrl_7;
        end
        th_ctrl_7: begin
          if((outstanding_wcount_0 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_8;
          end 
        end
        th_ctrl_8: begin
          th_ctrl <= th_ctrl_9;
        end
        th_ctrl_9: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_10;
          end 
        end
        th_ctrl_10: begin
          _th_ctrl_awaddr_4 <= 12;
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          _th_ctrl_size_6 <= 128;
          th_ctrl <= th_ctrl_12;
        end
        th_ctrl_12: begin
          $display("# size = %d", _th_ctrl_size_6);
          th_ctrl <= th_ctrl_13;
        end
        th_ctrl_13: begin
          if((outstanding_wcount_0 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_14;
          end 
        end
        th_ctrl_14: begin
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_16;
          end 
        end
        th_ctrl_16: begin
          _th_ctrl_awaddr_4 <= 0;
          th_ctrl <= th_ctrl_17;
        end
        th_ctrl_17: begin
          _th_ctrl_start_time_7 <= counter;
          th_ctrl <= th_ctrl_18;
        end
        th_ctrl_18: begin
          $display("# start time = %d", _th_ctrl_start_time_7);
          th_ctrl <= th_ctrl_19;
        end
        th_ctrl_19: begin
          if((outstanding_wcount_0 < 6) && (_saxi_awready || !_saxi_awvalid)) begin
            th_ctrl <= th_ctrl_20;
          end 
        end
        th_ctrl_20: begin
          th_ctrl <= th_ctrl_21;
        end
        th_ctrl_21: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_22;
          end 
        end
        th_ctrl_22: begin
          _th_ctrl_araddr_8 <= 4;
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_23: begin
          if(1) begin
            th_ctrl <= th_ctrl_24;
          end else begin
            th_ctrl <= th_ctrl_31;
          end
        end
        th_ctrl_24: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_25;
          end 
        end
        th_ctrl_25: begin
          th_ctrl <= th_ctrl_26;
        end
        th_ctrl_26: begin
          if(_saxi_rvalid) begin
            axim_rdata_14 <= _saxi_rdata;
          end 
          if(_saxi_rvalid) begin
            th_ctrl <= th_ctrl_27;
          end 
        end
        th_ctrl_27: begin
          _th_ctrl_busy_9 <= axim_rdata_14;
          th_ctrl <= th_ctrl_28;
        end
        th_ctrl_28: begin
          if(!_th_ctrl_busy_9) begin
            th_ctrl <= th_ctrl_29;
          end else begin
            th_ctrl <= th_ctrl_30;
          end
        end
        th_ctrl_29: begin
          th_ctrl <= th_ctrl_31;
        end
        th_ctrl_30: begin
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_31: begin
          _th_ctrl_end_time_10 <= counter;
          th_ctrl <= th_ctrl_32;
        end
        th_ctrl_32: begin
          $display("# end time = %d", _th_ctrl_end_time_10);
          th_ctrl <= th_ctrl_33;
        end
        th_ctrl_33: begin
          _th_ctrl_time_11 <= _th_ctrl_end_time_10 - _th_ctrl_start_time_7;
          th_ctrl <= th_ctrl_34;
        end
        th_ctrl_34: begin
          $display("# exec time = %d", _th_ctrl_time_11);
          th_ctrl <= th_ctrl_35;
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
  reg _saxi_flag_0;
  reg _saxi_flag_1;
  reg _saxi_flag_2;
  reg _saxi_flag_3;
  reg signed [32-1:0] _saxi_resetval_0;
  reg signed [32-1:0] _saxi_resetval_1;
  reg signed [32-1:0] _saxi_resetval_2;
  reg signed [32-1:0] _saxi_resetval_3;
  localparam _saxi_maskwidth = 2;
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
                            (axis_maskaddr_5 == 3)? _saxi_register_3 : 'hx;
  wire axislite_flag_7;
  assign axislite_flag_7 = (axis_maskaddr_5 == 0)? _saxi_flag_0 : 
                           (axis_maskaddr_5 == 1)? _saxi_flag_1 : 
                           (axis_maskaddr_5 == 2)? _saxi_flag_2 : 
                           (axis_maskaddr_5 == 3)? _saxi_flag_3 : 'hx;
  wire signed [32-1:0] axislite_resetval_8;
  assign axislite_resetval_8 = (axis_maskaddr_5 == 0)? _saxi_resetval_0 : 
                               (axis_maskaddr_5 == 1)? _saxi_resetval_1 : 
                               (axis_maskaddr_5 == 2)? _saxi_resetval_2 : 
                               (axis_maskaddr_5 == 3)? _saxi_resetval_3 : 'hx;
  reg _saxi_cond_0_1;
  assign saxi_wready = _saxi_register_fsm == 2;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_sleep_1;
  reg signed [32-1:0] _th_blink_i_2;
  reg [32-1:0] _tmp_9;

  always @(posedge CLK) begin
    if(RST) begin
      saxi_bvalid <= 0;
      prev_awvalid_3 <= 0;
      prev_arvalid_4 <= 0;
      writevalid_1 <= 0;
      readvalid_2 <= 0;
      addr_0 <= 0;
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
      if((_saxi_register_fsm == 1) && (saxi_rready || !saxi_rvalid)) begin
        saxi_rdata <= axislite_rdata_6;
        saxi_rvalid <= 1;
      end 
      _saxi_cond_0_1 <= 1;
      if(saxi_rvalid && !saxi_rready) begin
        saxi_rvalid <= saxi_rvalid;
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
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 0)) begin
        _saxi_register_0 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 1)) begin
        _saxi_register_1 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 2)) begin
        _saxi_register_2 <= saxi_wdata;
      end 
      if((_saxi_register_fsm == 2) && saxi_wvalid && (axis_maskaddr_5 == 3)) begin
        _saxi_register_3 <= saxi_wdata;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && 1) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && 0) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && 0) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && 0) begin
        _saxi_register_3 <= 0;
      end 
      if((th_blink == 3) && 0) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 0;
      end 
      if((th_blink == 3) && 1) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 0;
      end 
      if((th_blink == 3) && 0) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 0;
      end 
      if((th_blink == 3) && 0) begin
        _saxi_register_3 <= 1;
        _saxi_flag_3 <= 0;
      end 
      if((th_blink == 11) && 0) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_blink == 11) && 1) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_blink == 11) && 0) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_blink == 11) && 0) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
    end
  end

  localparam _saxi_register_fsm_1 = 1;
  localparam _saxi_register_fsm_2 = 2;

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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _th_blink_sleep_1 <= 0;
      _th_blink_i_2 <= 0;
      _tmp_9 <= 0;
      led <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 16;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          if(1) begin
            th_blink <= th_blink_2;
          end else begin
            th_blink <= th_blink_13;
          end
        end
        th_blink_2: begin
          if(_saxi_register_0 == 1) begin
            th_blink <= th_blink_3;
          end 
        end
        th_blink_3: begin
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _th_blink_sleep_1 <= _saxi_register_2;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_size_0 <= _saxi_register_3;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_i_2 <= 0;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          if(_th_blink_i_2 < _th_blink_size_0) begin
            th_blink <= th_blink_8;
          end else begin
            th_blink <= th_blink_11;
          end
        end
        th_blink_8: begin
          if(_tmp_9 < _th_blink_sleep_1) begin
            _tmp_9 <= _tmp_9 + 1;
          end 
          if(_tmp_9 >= _th_blink_sleep_1) begin
            _tmp_9 <= 0;
          end 
          if(_tmp_9 >= _th_blink_sleep_1) begin
            th_blink <= th_blink_9;
          end 
        end
        th_blink_9: begin
          led <= led + 1;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          _th_blink_i_2 <= _th_blink_i_2 + 1;
          th_blink <= th_blink_7;
        end
        th_blink_11: begin
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          th_blink <= th_blink_1;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_axi_slave_ipxact.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
