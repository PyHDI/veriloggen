from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ipcore

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] led;
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
  wire [32-1:0] _tmp_0;
  assign _tmp_0 = _saxi_awaddr;

  always @(*) begin
    saxi_awaddr = _tmp_0;
  end

  wire _tmp_1;
  assign _tmp_1 = _saxi_awvalid;

  always @(*) begin
    saxi_awvalid = _tmp_1;
  end

  assign _saxi_awready = saxi_awready;
  wire [32-1:0] _tmp_2;
  assign _tmp_2 = _saxi_wdata;

  always @(*) begin
    saxi_wdata = _tmp_2;
  end

  wire [4-1:0] _tmp_3;
  assign _tmp_3 = _saxi_wstrb;

  always @(*) begin
    saxi_wstrb = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = _saxi_wvalid;

  always @(*) begin
    saxi_wvalid = _tmp_4;
  end

  assign _saxi_wready = saxi_wready;
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _saxi_araddr;

  always @(*) begin
    saxi_araddr = _tmp_5;
  end

  wire _tmp_6;
  assign _tmp_6 = _saxi_arvalid;

  always @(*) begin
    saxi_arvalid = _tmp_6;
  end

  assign _saxi_arready = saxi_arready;
  assign _saxi_rdata = saxi_rdata;
  assign _saxi_rvalid = saxi_rvalid;
  wire _tmp_7;
  assign _tmp_7 = _saxi_rready;

  always @(*) begin
    saxi_rready = _tmp_7;
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
  reg signed [32-1:0] axim_rdata_8;
  reg signed [32-1:0] _th_ctrl_v_9;
  reg __saxi_cond_7_1;
  assign _saxi_rready = (th_ctrl == 21) || (th_ctrl == 25);
  reg signed [32-1:0] axim_rdata_9;
  reg signed [32-1:0] _th_ctrl_end_time_10;
  reg signed [32-1:0] _th_ctrl_time_11;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .led(led),
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
    axim_rdata_8 = 0;
    _th_ctrl_v_9 = 0;
    __saxi_cond_7_1 = 0;
    axim_rdata_9 = 0;
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
      _saxi_araddr <= 0;
      _saxi_arvalid <= 0;
      __saxi_cond_6_1 <= 0;
      __saxi_cond_7_1 <= 0;
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
      if(__saxi_cond_7_1) begin
        _saxi_arvalid <= 0;
      end 
      __saxi_read_start <= 0;
      __saxi_write_start <= 0;
      if((th_ctrl == 7) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_0_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 8) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_sleep_5;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_1_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 12) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_2_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 13) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= _th_ctrl_size_6;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_3_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 17) && (_saxi_awready || !_saxi_awvalid)) begin
        _saxi_awaddr <= _th_ctrl_awaddr_4;
        _saxi_awvalid <= 1;
      end 
      __saxi_cond_4_1 <= 1;
      if(_saxi_awvalid && !_saxi_awready) begin
        _saxi_awvalid <= _saxi_awvalid;
      end 
      if((th_ctrl == 18) && (_saxi_wready || !_saxi_wvalid)) begin
        _saxi_wdata <= 1;
        _saxi_wvalid <= 1;
        _saxi_wstrb <= { 4{ 1'd1 } };
      end 
      __saxi_cond_5_1 <= 1;
      if(_saxi_wvalid && !_saxi_wready) begin
        _saxi_wvalid <= _saxi_wvalid;
      end 
      if((th_ctrl == 20) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_8;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_6_1 <= 1;
      if(_saxi_arvalid && !_saxi_arready) begin
        _saxi_arvalid <= _saxi_arvalid;
      end 
      if((th_ctrl == 24) && (_saxi_arready || !_saxi_arvalid)) begin
        _saxi_araddr <= _th_ctrl_araddr_8;
        _saxi_arvalid <= 1;
      end 
      __saxi_cond_7_1 <= 1;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_ctrl <= th_ctrl_init;
      _th_ctrl_i_3 <= 0;
      _th_ctrl_awaddr_4 <= 0;
      _th_ctrl_sleep_5 <= 0;
      _th_ctrl_size_6 <= 0;
      _th_ctrl_start_time_7 <= 0;
      _th_ctrl_araddr_8 <= 0;
      axim_rdata_8 <= 0;
      _th_ctrl_v_9 <= 0;
      axim_rdata_9 <= 0;
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
          _th_ctrl_awaddr_4 <= 4;
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
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_8;
          end 
        end
        th_ctrl_8: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_9;
          end 
        end
        th_ctrl_9: begin
          _th_ctrl_awaddr_4 <= 8;
          th_ctrl <= th_ctrl_10;
        end
        th_ctrl_10: begin
          _th_ctrl_size_6 <= 128;
          th_ctrl <= th_ctrl_11;
        end
        th_ctrl_11: begin
          $display("# size = %d", _th_ctrl_size_6);
          th_ctrl <= th_ctrl_12;
        end
        th_ctrl_12: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_13;
          end 
        end
        th_ctrl_13: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_14;
          end 
        end
        th_ctrl_14: begin
          _th_ctrl_awaddr_4 <= 0;
          th_ctrl <= th_ctrl_15;
        end
        th_ctrl_15: begin
          _th_ctrl_start_time_7 <= counter;
          th_ctrl <= th_ctrl_16;
        end
        th_ctrl_16: begin
          $display("# start time = %d", _th_ctrl_start_time_7);
          th_ctrl <= th_ctrl_17;
        end
        th_ctrl_17: begin
          if(_saxi_awready || !_saxi_awvalid) begin
            th_ctrl <= th_ctrl_18;
          end 
        end
        th_ctrl_18: begin
          if(_saxi_wready || !_saxi_wvalid) begin
            th_ctrl <= th_ctrl_19;
          end 
        end
        th_ctrl_19: begin
          _th_ctrl_araddr_8 <= 12;
          th_ctrl <= th_ctrl_20;
        end
        th_ctrl_20: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_21;
          end 
        end
        th_ctrl_21: begin
          if(_saxi_rready && _saxi_rvalid) begin
            axim_rdata_8 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_22;
          end 
        end
        th_ctrl_22: begin
          _th_ctrl_v_9 <= axim_rdata_8;
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_23: begin
          if(_th_ctrl_v_9 == 0) begin
            th_ctrl <= th_ctrl_24;
          end else begin
            th_ctrl <= th_ctrl_28;
          end
        end
        th_ctrl_24: begin
          if(_saxi_arready || !_saxi_arvalid) begin
            th_ctrl <= th_ctrl_25;
          end 
        end
        th_ctrl_25: begin
          if(_saxi_rready && _saxi_rvalid) begin
            axim_rdata_9 <= _saxi_rdata;
          end 
          if(_saxi_rready && _saxi_rvalid) begin
            th_ctrl <= th_ctrl_26;
          end 
        end
        th_ctrl_26: begin
          _th_ctrl_v_9 <= axim_rdata_9;
          th_ctrl <= th_ctrl_27;
        end
        th_ctrl_27: begin
          th_ctrl <= th_ctrl_23;
        end
        th_ctrl_28: begin
          _th_ctrl_end_time_10 <= counter;
          th_ctrl <= th_ctrl_29;
        end
        th_ctrl_29: begin
          $display("# end time = %d", _th_ctrl_end_time_10);
          th_ctrl <= th_ctrl_30;
        end
        th_ctrl_30: begin
          _th_ctrl_time_11 <= _th_ctrl_end_time_10 - _th_ctrl_start_time_7;
          th_ctrl <= th_ctrl_31;
        end
        th_ctrl_31: begin
          $display("# exec time = %d", _th_ctrl_time_11);
          th_ctrl <= th_ctrl_32;
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
                  (_tmp_5 == 3)? _saxi_register_3 : 'hx;
  wire _tmp_7;
  assign _tmp_7 = (_tmp_5 == 0)? _saxi_flag_0 : 
                  (_tmp_5 == 1)? _saxi_flag_1 : 
                  (_tmp_5 == 2)? _saxi_flag_2 : 
                  (_tmp_5 == 3)? _saxi_flag_3 : 'hx;
  wire signed [32-1:0] _tmp_8;
  assign _tmp_8 = (_tmp_5 == 0)? _saxi_resetval_0 : 
                  (_tmp_5 == 1)? _saxi_resetval_1 : 
                  (_tmp_5 == 2)? _saxi_resetval_2 : 
                  (_tmp_5 == 3)? _saxi_resetval_3 : 'hx;
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
      if((_saxi_register_0 == 1) && (th_blink == 2) && (0 == 0)) begin
        _saxi_register_0 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && (0 == 1)) begin
        _saxi_register_1 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && (0 == 2)) begin
        _saxi_register_2 <= 0;
      end 
      if((_saxi_register_0 == 1) && (th_blink == 2) && (0 == 3)) begin
        _saxi_register_3 <= 0;
      end 
      if((th_blink == 3) && (3 == 0)) begin
        _saxi_register_0 <= 0;
        _saxi_flag_0 <= 0;
      end 
      if((th_blink == 3) && (3 == 1)) begin
        _saxi_register_1 <= 0;
        _saxi_flag_1 <= 0;
      end 
      if((th_blink == 3) && (3 == 2)) begin
        _saxi_register_2 <= 0;
        _saxi_flag_2 <= 0;
      end 
      if((th_blink == 3) && (3 == 3)) begin
        _saxi_register_3 <= 0;
        _saxi_flag_3 <= 0;
      end 
      if((th_blink == 11) && (3 == 0)) begin
        _saxi_register_0 <= 1;
        _saxi_flag_0 <= 1;
        _saxi_resetval_0 <= 0;
      end 
      if((th_blink == 11) && (3 == 1)) begin
        _saxi_register_1 <= 1;
        _saxi_flag_1 <= 1;
        _saxi_resetval_1 <= 0;
      end 
      if((th_blink == 11) && (3 == 2)) begin
        _saxi_register_2 <= 1;
        _saxi_flag_2 <= 1;
        _saxi_resetval_2 <= 0;
      end 
      if((th_blink == 11) && (3 == 3)) begin
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
          _th_blink_sleep_1 <= _saxi_register_1;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_size_0 <= _saxi_register_2;
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
    test_module = thread_ipcore.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
