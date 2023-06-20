from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_reduceadd_valid_enable

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg xvalid;
  wire xready;
  reg [1-1:0] resetdata;
  reg resetvalid;
  wire resetready;
  reg [1-1:0] enabledata;
  reg enablevalid;
  wire enableready;
  wire [32-1:0] zdata;
  wire zvalid;
  reg zready;
  wire [1-1:0] vdata;
  wire vvalid;
  reg vready;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .resetdata(resetdata),
    .resetvalid(resetvalid),
    .resetready(resetready),
    .enabledata(enabledata),
    .enablevalid(enablevalid),
    .enableready(enableready),
    .zdata(zdata),
    .zvalid(zvalid),
    .zready(zready),
    .vdata(vdata),
    .vvalid(vvalid),
    .vready(vready)
  );

  reg reset_done;

  initial begin
    $dumpfile("dataflow_reduceadd_valid_enable.vcd");
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
    reset_done = 0;
    xdata = 0;
    xvalid = 0;
    enabledata = 0;
    enablevalid = 0;
    resetdata = 0;
    resetvalid = 0;
    zready = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;
  localparam xfsm_7 = 7;
  localparam xfsm_8 = 8;
  localparam xfsm_9 = 9;
  localparam xfsm_10 = 10;
  localparam xfsm_11 = 11;
  localparam xfsm_12 = 12;
  localparam xfsm_13 = 13;
  localparam xfsm_14 = 14;
  localparam xfsm_15 = 15;
  localparam xfsm_16 = 16;
  localparam xfsm_17 = 17;
  localparam xfsm_18 = 18;
  localparam xfsm_19 = 19;
  localparam xfsm_20 = 20;
  localparam xfsm_21 = 21;
  localparam xfsm_22 = 22;
  localparam xfsm_23 = 23;
  localparam xfsm_24 = 24;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          xvalid <= 0;
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          xfsm <= xfsm_2;
        end
        xfsm_2: begin
          xfsm <= xfsm_3;
        end
        xfsm_3: begin
          xfsm <= xfsm_4;
        end
        xfsm_4: begin
          xfsm <= xfsm_5;
        end
        xfsm_5: begin
          xfsm <= xfsm_6;
        end
        xfsm_6: begin
          xfsm <= xfsm_7;
        end
        xfsm_7: begin
          xfsm <= xfsm_8;
        end
        xfsm_8: begin
          xfsm <= xfsm_9;
        end
        xfsm_9: begin
          xfsm <= xfsm_10;
        end
        xfsm_10: begin
          xfsm <= xfsm_11;
        end
        xfsm_11: begin
          xvalid <= 1;
          xfsm <= xfsm_12;
        end
        xfsm_12: begin
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 5) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 5) && xready) begin
            xfsm <= xfsm_13;
          end 
        end
        xfsm_13: begin
          xfsm <= xfsm_14;
        end
        xfsm_14: begin
          xfsm <= xfsm_15;
        end
        xfsm_15: begin
          xfsm <= xfsm_16;
        end
        xfsm_16: begin
          xfsm <= xfsm_17;
        end
        xfsm_17: begin
          xfsm <= xfsm_18;
        end
        xfsm_18: begin
          xfsm <= xfsm_19;
        end
        xfsm_19: begin
          xfsm <= xfsm_20;
        end
        xfsm_20: begin
          xfsm <= xfsm_21;
        end
        xfsm_21: begin
          xfsm <= xfsm_22;
        end
        xfsm_22: begin
          xfsm <= xfsm_23;
        end
        xfsm_23: begin
          xvalid <= 1;
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 100) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 100) && xready) begin
            xfsm <= xfsm_24;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  localparam zfsm_1 = 1;
  localparam zfsm_2 = 2;
  localparam zfsm_3 = 3;
  localparam zfsm_4 = 4;
  localparam zfsm_5 = 5;
  localparam zfsm_6 = 6;
  localparam zfsm_7 = 7;
  localparam zfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
    end else begin
      case(zfsm)
        zfsm_init: begin
          zready <= 0;
          if(reset_done) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          if(zvalid && vvalid) begin
            zready <= 1;
          end 
          if(zvalid && vvalid) begin
            zfsm <= zfsm_3;
          end 
        end
        zfsm_3: begin
          zready <= 0;
          zfsm <= zfsm_4;
        end
        zfsm_4: begin
          zready <= 0;
          zfsm <= zfsm_5;
        end
        zfsm_5: begin
          zready <= 0;
          zfsm <= zfsm_6;
        end
        zfsm_6: begin
          zready <= 0;
          zfsm <= zfsm_7;
        end
        zfsm_7: begin
          zready <= 0;
          zfsm <= zfsm_8;
        end
        zfsm_8: begin
          zfsm <= zfsm_2;
        end
      endcase
    end
  end

  reg [32-1:0] vfsm;
  localparam vfsm_init = 0;
  localparam vfsm_1 = 1;
  localparam vfsm_2 = 2;
  localparam vfsm_3 = 3;
  localparam vfsm_4 = 4;
  localparam vfsm_5 = 5;
  localparam vfsm_6 = 6;
  localparam vfsm_7 = 7;
  localparam vfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      vfsm <= vfsm_init;
    end else begin
      case(vfsm)
        vfsm_init: begin
          vready <= 0;
          if(reset_done) begin
            vfsm <= vfsm_1;
          end 
        end
        vfsm_1: begin
          vfsm <= vfsm_2;
        end
        vfsm_2: begin
          if(zvalid && vvalid) begin
            vready <= 1;
          end 
          if(zvalid && vvalid) begin
            vfsm <= vfsm_3;
          end 
        end
        vfsm_3: begin
          vready <= 0;
          vfsm <= vfsm_4;
        end
        vfsm_4: begin
          vready <= 0;
          vfsm <= vfsm_5;
        end
        vfsm_5: begin
          vready <= 0;
          vfsm <= vfsm_6;
        end
        vfsm_6: begin
          vready <= 0;
          vfsm <= vfsm_7;
        end
        vfsm_7: begin
          vready <= 0;
          vfsm <= vfsm_8;
        end
        vfsm_8: begin
          vfsm <= vfsm_2;
        end
      endcase
    end
  end

  reg [32-1:0] enable;
  localparam enable_init = 0;
  reg [32-1:0] enable_count;
  localparam enable_1 = 1;
  localparam enable_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      enable <= enable_init;
      enable_count <= 0;
    end else begin
      case(enable)
        enable_init: begin
          if(reset_done) begin
            enable <= enable_1;
          end 
        end
        enable_1: begin
          enablevalid <= 1;
          if(enablevalid && enableready) begin
            enable_count <= enable_count + 1;
          end 
          if(enablevalid && enableready && (enable_count == 2)) begin
            enabledata <= 1;
          end 
          if(enablevalid && enableready && (enable_count == 2)) begin
            enable <= enable_2;
          end 
        end
        enable_2: begin
          if(enablevalid && enableready) begin
            enabledata <= 0;
          end 
          enable_count <= 0;
          if(enablevalid && enableready) begin
            enable <= enable_1;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] reset;
  localparam reset_init = 0;
  reg [32-1:0] reset_count;
  localparam reset_1 = 1;
  localparam reset_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      reset <= reset_init;
      reset_count <= 0;
    end else begin
      case(reset)
        reset_init: begin
          if(reset_done) begin
            reset <= reset_1;
          end 
        end
        reset_1: begin
          resetvalid <= 1;
          if(resetvalid && resetready) begin
            reset_count <= reset_count + 1;
          end 
          if(resetvalid && resetready && (reset_count == 2)) begin
            resetdata <= 0;
          end 
          if(resetvalid && resetready && (reset_count == 2)) begin
            reset <= reset_2;
          end 
        end
        reset_2: begin
          if(resetvalid && resetready) begin
            resetdata <= 0;
          end 
          reset_count <= 0;
          if(resetvalid && resetready) begin
            reset <= reset_1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(xvalid && xready) begin
        $display("xdata=%d", xdata);
      end 
      if(zvalid && zready) begin
        $display("zdata=%d", zdata);
      end 
      if(vvalid && vready) begin
        $display("vdata=%d", vdata);
      end 
    end 
  end


endmodule



module main
(
  input CLK,
  input RST,
  input [32-1:0] xdata,
  input xvalid,
  output xready,
  input [1-1:0] resetdata,
  input resetvalid,
  output resetready,
  input [1-1:0] enabledata,
  input enablevalid,
  output enableready,
  output [32-1:0] zdata,
  output zvalid,
  input zready,
  output [1-1:0] vdata,
  output vvalid,
  input vready
);

  wire [32-1:0] _dataflow_times_data_3;
  wire _dataflow_times_valid_3;
  wire _dataflow_times_ready_3;
  wire [64-1:0] _dataflow_times_mul_odata_3;
  reg [64-1:0] _dataflow_times_mul_odata_reg_3;
  assign _dataflow_times_data_3 = _dataflow_times_mul_odata_reg_3;
  wire _dataflow_times_mul_ovalid_3;
  reg _dataflow_times_mul_valid_reg_3;
  assign _dataflow_times_valid_3 = _dataflow_times_mul_valid_reg_3;
  wire _dataflow_times_mul_enable_3;
  wire _dataflow_times_mul_update_3;
  assign _dataflow_times_mul_enable_3 = (_dataflow_times_ready_3 || !_dataflow_times_valid_3) && (xready && xready) && (xvalid && xvalid);
  assign _dataflow_times_mul_update_3 = _dataflow_times_ready_3 || !_dataflow_times_valid_3;

  multiplier_0
  _dataflow_times_mul_3
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_3),
    .enable(_dataflow_times_mul_enable_3),
    .valid(_dataflow_times_mul_ovalid_3),
    .a(xdata),
    .b(xdata),
    .c(_dataflow_times_mul_odata_3)
  );

  assign xready = (_dataflow_times_ready_3 || !_dataflow_times_valid_3) && (xvalid && xvalid) && ((_dataflow_times_ready_3 || !_dataflow_times_valid_3) && (xvalid && xvalid));
  reg [1-1:0] _dataflow__delay_data_10;
  reg _dataflow__delay_valid_10;
  wire _dataflow__delay_ready_10;
  assign enableready = (_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && enablevalid;
  reg [1-1:0] _dataflow__delay_data_17;
  reg _dataflow__delay_valid_17;
  wire _dataflow__delay_ready_17;
  assign resetready = (_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && resetvalid;
  reg [1-1:0] _dataflow__delay_data_11;
  reg _dataflow__delay_valid_11;
  wire _dataflow__delay_ready_11;
  assign _dataflow__delay_ready_10 = (_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_valid_10;
  reg [1-1:0] _dataflow__delay_data_18;
  reg _dataflow__delay_valid_18;
  wire _dataflow__delay_ready_18;
  assign _dataflow__delay_ready_17 = (_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_valid_17;
  reg [1-1:0] _dataflow__delay_data_12;
  reg _dataflow__delay_valid_12;
  wire _dataflow__delay_ready_12;
  assign _dataflow__delay_ready_11 = (_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow__delay_valid_11;
  reg [1-1:0] _dataflow__delay_data_19;
  reg _dataflow__delay_valid_19;
  wire _dataflow__delay_ready_19;
  assign _dataflow__delay_ready_18 = (_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_valid_18;
  reg [1-1:0] _dataflow__delay_data_13;
  reg _dataflow__delay_valid_13;
  wire _dataflow__delay_ready_13;
  assign _dataflow__delay_ready_12 = (_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_valid_12;
  reg [1-1:0] _dataflow__delay_data_20;
  reg _dataflow__delay_valid_20;
  wire _dataflow__delay_ready_20;
  assign _dataflow__delay_ready_19 = (_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_valid_19;
  reg [1-1:0] _dataflow__delay_data_14;
  reg _dataflow__delay_valid_14;
  wire _dataflow__delay_ready_14;
  assign _dataflow__delay_ready_13 = (_dataflow__delay_ready_14 || !_dataflow__delay_valid_14) && _dataflow__delay_valid_13;
  reg [1-1:0] _dataflow__delay_data_21;
  reg _dataflow__delay_valid_21;
  wire _dataflow__delay_ready_21;
  assign _dataflow__delay_ready_20 = (_dataflow__delay_ready_21 || !_dataflow__delay_valid_21) && _dataflow__delay_valid_20;
  reg [1-1:0] _dataflow__delay_data_15;
  reg _dataflow__delay_valid_15;
  wire _dataflow__delay_ready_15;
  assign _dataflow__delay_ready_14 = (_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow__delay_valid_14;
  reg [1-1:0] _dataflow__delay_data_22;
  reg _dataflow__delay_valid_22;
  wire _dataflow__delay_ready_22;
  assign _dataflow__delay_ready_21 = (_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && _dataflow__delay_valid_21;
  reg [1-1:0] _dataflow__delay_data_16;
  reg _dataflow__delay_valid_16;
  wire _dataflow__delay_ready_16;
  assign _dataflow__delay_ready_15 = (_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow__delay_valid_15;
  reg [1-1:0] _dataflow__delay_data_23;
  reg _dataflow__delay_valid_23;
  wire _dataflow__delay_ready_23;
  assign _dataflow__delay_ready_22 = (_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && _dataflow__delay_valid_22;
  reg [32-1:0] _dataflow_reduceadd_data_6;
  reg _dataflow_reduceadd_valid_6;
  wire _dataflow_reduceadd_ready_6;
  reg [5-1:0] _dataflow_reduceadd_count_6;
  reg [1-1:0] _dataflow_pulse_data_9;
  reg _dataflow_pulse_valid_9;
  wire _dataflow_pulse_ready_9;
  reg [5-1:0] _dataflow_pulse_count_9;
  assign _dataflow__delay_ready_16 = (_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && ((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23));
  assign _dataflow_times_ready_3 = (_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && ((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23));
  assign _dataflow__delay_ready_23 = (_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && ((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23));
  assign zdata = _dataflow_reduceadd_data_6;
  assign zvalid = _dataflow_reduceadd_valid_6;
  assign _dataflow_reduceadd_ready_6 = zready;
  assign vdata = _dataflow_pulse_data_9;
  assign vvalid = _dataflow_pulse_valid_9;
  assign _dataflow_pulse_ready_9 = vready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_times_mul_odata_reg_3 <= 0;
      _dataflow_times_mul_valid_reg_3 <= 0;
      _dataflow__delay_data_10 <= 0;
      _dataflow__delay_valid_10 <= 0;
      _dataflow__delay_data_17 <= 0;
      _dataflow__delay_valid_17 <= 0;
      _dataflow__delay_data_11 <= 0;
      _dataflow__delay_valid_11 <= 0;
      _dataflow__delay_data_18 <= 0;
      _dataflow__delay_valid_18 <= 0;
      _dataflow__delay_data_12 <= 0;
      _dataflow__delay_valid_12 <= 0;
      _dataflow__delay_data_19 <= 0;
      _dataflow__delay_valid_19 <= 0;
      _dataflow__delay_data_13 <= 0;
      _dataflow__delay_valid_13 <= 0;
      _dataflow__delay_data_20 <= 0;
      _dataflow__delay_valid_20 <= 0;
      _dataflow__delay_data_14 <= 0;
      _dataflow__delay_valid_14 <= 0;
      _dataflow__delay_data_21 <= 0;
      _dataflow__delay_valid_21 <= 0;
      _dataflow__delay_data_15 <= 0;
      _dataflow__delay_valid_15 <= 0;
      _dataflow__delay_data_22 <= 0;
      _dataflow__delay_valid_22 <= 0;
      _dataflow__delay_data_16 <= 0;
      _dataflow__delay_valid_16 <= 0;
      _dataflow__delay_data_23 <= 0;
      _dataflow__delay_valid_23 <= 0;
      _dataflow_reduceadd_data_6 <= 1'sd0;
      _dataflow_reduceadd_count_6 <= 0;
      _dataflow_reduceadd_valid_6 <= 0;
      _dataflow_pulse_data_9 <= 1'sd0;
      _dataflow_pulse_count_9 <= 0;
      _dataflow_pulse_valid_9 <= 0;
    end else begin
      if(_dataflow_times_ready_3 || !_dataflow_times_valid_3) begin
        _dataflow_times_mul_odata_reg_3 <= _dataflow_times_mul_odata_3;
      end 
      if(_dataflow_times_ready_3 || !_dataflow_times_valid_3) begin
        _dataflow_times_mul_valid_reg_3 <= _dataflow_times_mul_ovalid_3;
      end 
      if((_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && enableready && enablevalid) begin
        _dataflow__delay_data_10 <= enabledata;
      end 
      if(_dataflow__delay_valid_10 && _dataflow__delay_ready_10) begin
        _dataflow__delay_valid_10 <= 0;
      end 
      if((_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && enableready) begin
        _dataflow__delay_valid_10 <= enablevalid;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && resetready && resetvalid) begin
        _dataflow__delay_data_17 <= resetdata;
      end 
      if(_dataflow__delay_valid_17 && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_17 <= 0;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && resetready) begin
        _dataflow__delay_valid_17 <= resetvalid;
      end 
      if((_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_ready_10 && _dataflow__delay_valid_10) begin
        _dataflow__delay_data_11 <= _dataflow__delay_data_10;
      end 
      if(_dataflow__delay_valid_11 && _dataflow__delay_ready_11) begin
        _dataflow__delay_valid_11 <= 0;
      end 
      if((_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_ready_10) begin
        _dataflow__delay_valid_11 <= _dataflow__delay_valid_10;
      end 
      if((_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_ready_17 && _dataflow__delay_valid_17) begin
        _dataflow__delay_data_18 <= _dataflow__delay_data_17;
      end 
      if(_dataflow__delay_valid_18 && _dataflow__delay_ready_18) begin
        _dataflow__delay_valid_18 <= 0;
      end 
      if((_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_18 <= _dataflow__delay_valid_17;
      end 
      if((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow__delay_ready_11 && _dataflow__delay_valid_11) begin
        _dataflow__delay_data_12 <= _dataflow__delay_data_11;
      end 
      if(_dataflow__delay_valid_12 && _dataflow__delay_ready_12) begin
        _dataflow__delay_valid_12 <= 0;
      end 
      if((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow__delay_ready_11) begin
        _dataflow__delay_valid_12 <= _dataflow__delay_valid_11;
      end 
      if((_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_ready_18 && _dataflow__delay_valid_18) begin
        _dataflow__delay_data_19 <= _dataflow__delay_data_18;
      end 
      if(_dataflow__delay_valid_19 && _dataflow__delay_ready_19) begin
        _dataflow__delay_valid_19 <= 0;
      end 
      if((_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_ready_18) begin
        _dataflow__delay_valid_19 <= _dataflow__delay_valid_18;
      end 
      if((_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_ready_12 && _dataflow__delay_valid_12) begin
        _dataflow__delay_data_13 <= _dataflow__delay_data_12;
      end 
      if(_dataflow__delay_valid_13 && _dataflow__delay_ready_13) begin
        _dataflow__delay_valid_13 <= 0;
      end 
      if((_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_ready_12) begin
        _dataflow__delay_valid_13 <= _dataflow__delay_valid_12;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_ready_19 && _dataflow__delay_valid_19) begin
        _dataflow__delay_data_20 <= _dataflow__delay_data_19;
      end 
      if(_dataflow__delay_valid_20 && _dataflow__delay_ready_20) begin
        _dataflow__delay_valid_20 <= 0;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_ready_19) begin
        _dataflow__delay_valid_20 <= _dataflow__delay_valid_19;
      end 
      if((_dataflow__delay_ready_14 || !_dataflow__delay_valid_14) && _dataflow__delay_ready_13 && _dataflow__delay_valid_13) begin
        _dataflow__delay_data_14 <= _dataflow__delay_data_13;
      end 
      if(_dataflow__delay_valid_14 && _dataflow__delay_ready_14) begin
        _dataflow__delay_valid_14 <= 0;
      end 
      if((_dataflow__delay_ready_14 || !_dataflow__delay_valid_14) && _dataflow__delay_ready_13) begin
        _dataflow__delay_valid_14 <= _dataflow__delay_valid_13;
      end 
      if((_dataflow__delay_ready_21 || !_dataflow__delay_valid_21) && _dataflow__delay_ready_20 && _dataflow__delay_valid_20) begin
        _dataflow__delay_data_21 <= _dataflow__delay_data_20;
      end 
      if(_dataflow__delay_valid_21 && _dataflow__delay_ready_21) begin
        _dataflow__delay_valid_21 <= 0;
      end 
      if((_dataflow__delay_ready_21 || !_dataflow__delay_valid_21) && _dataflow__delay_ready_20) begin
        _dataflow__delay_valid_21 <= _dataflow__delay_valid_20;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow__delay_ready_14 && _dataflow__delay_valid_14) begin
        _dataflow__delay_data_15 <= _dataflow__delay_data_14;
      end 
      if(_dataflow__delay_valid_15 && _dataflow__delay_ready_15) begin
        _dataflow__delay_valid_15 <= 0;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow__delay_ready_14) begin
        _dataflow__delay_valid_15 <= _dataflow__delay_valid_14;
      end 
      if((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && _dataflow__delay_ready_21 && _dataflow__delay_valid_21) begin
        _dataflow__delay_data_22 <= _dataflow__delay_data_21;
      end 
      if(_dataflow__delay_valid_22 && _dataflow__delay_ready_22) begin
        _dataflow__delay_valid_22 <= 0;
      end 
      if((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && _dataflow__delay_ready_21) begin
        _dataflow__delay_valid_22 <= _dataflow__delay_valid_21;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow__delay_ready_15 && _dataflow__delay_valid_15) begin
        _dataflow__delay_data_16 <= _dataflow__delay_data_15;
      end 
      if(_dataflow__delay_valid_16 && _dataflow__delay_ready_16) begin
        _dataflow__delay_valid_16 <= 0;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow__delay_ready_15) begin
        _dataflow__delay_valid_16 <= _dataflow__delay_valid_15;
      end 
      if((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && _dataflow__delay_ready_22 && _dataflow__delay_valid_22) begin
        _dataflow__delay_data_23 <= _dataflow__delay_data_22;
      end 
      if(_dataflow__delay_valid_23 && _dataflow__delay_ready_23) begin
        _dataflow__delay_valid_23 <= 0;
      end 
      if((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && _dataflow__delay_ready_22) begin
        _dataflow__delay_valid_23 <= _dataflow__delay_valid_22;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16) begin
        _dataflow_reduceadd_data_6 <= _dataflow_reduceadd_data_6 + _dataflow_times_data_3;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16) begin
        _dataflow_reduceadd_count_6 <= (_dataflow_reduceadd_count_6 == 4'sd4 - 1)? 0 : _dataflow_reduceadd_count_6 + 1;
      end 
      if(_dataflow_reduceadd_valid_6 && _dataflow_reduceadd_ready_6) begin
        _dataflow_reduceadd_valid_6 <= 0;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23)) begin
        _dataflow_reduceadd_valid_6 <= _dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_23) begin
        _dataflow_reduceadd_data_6 <= 1'sd0;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16 && _dataflow__delay_data_23) begin
        _dataflow_reduceadd_data_6 <= 1'sd0 + _dataflow_times_data_3;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16 && _dataflow__delay_data_23) begin
        _dataflow_reduceadd_count_6 <= 0;
      end 
      if((_dataflow_reduceadd_ready_6 || !_dataflow_reduceadd_valid_6) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16 && (_dataflow_reduceadd_count_6 == 0)) begin
        _dataflow_reduceadd_data_6 <= 1'sd0 + _dataflow_times_data_3;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16) begin
        _dataflow_pulse_data_9 <= _dataflow_pulse_count_9 == 4'sd4 - 1;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16) begin
        _dataflow_pulse_count_9 <= (_dataflow_pulse_count_9 == 4'sd4 - 1)? 0 : _dataflow_pulse_count_9 + 1;
      end 
      if(_dataflow_pulse_valid_9 && _dataflow_pulse_ready_9) begin
        _dataflow_pulse_valid_9 <= 0;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23)) begin
        _dataflow_pulse_valid_9 <= _dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_23) begin
        _dataflow_pulse_data_9 <= 1'sd0;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16 && _dataflow__delay_data_23) begin
        _dataflow_pulse_data_9 <= _dataflow_pulse_count_9 == 4'sd4 - 1;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16 && _dataflow__delay_data_23) begin
        _dataflow_pulse_count_9 <= 0;
      end 
      if((_dataflow_pulse_ready_9 || !_dataflow_pulse_valid_9) && (_dataflow_times_ready_3 && _dataflow__delay_ready_16 && _dataflow__delay_ready_23) && (_dataflow_times_valid_3 && _dataflow__delay_valid_16 && _dataflow__delay_valid_23) && _dataflow__delay_data_16 && (_dataflow_pulse_count_9 == 0)) begin
        _dataflow_pulse_data_9 <= _dataflow_pulse_count_9 == 4'sd4 - 1;
      end 
    end
  end


endmodule



module multiplier_0
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


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

  reg [32-1:0] _a;
  reg [32-1:0] _b;
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
  assign _mul = $signed({ 1'd0, _a }) * $signed({ 1'd0, _b });
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
    test_module = dataflow_reduceadd_valid_enable.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
