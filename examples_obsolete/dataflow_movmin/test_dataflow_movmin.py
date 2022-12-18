from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_movmin

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg signed [32-1:0] xdata;
  reg xvalid;
  wire xready;
  wire signed [32-1:0] ydata;
  wire yvalid;
  reg yready;

  movmin
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .ydata(ydata),
    .yvalid(yvalid),
    .yready(yready)
  );

  reg reset_done;

  initial begin
    $dumpfile("dataflow_movmin.vcd");
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
    yready = 0;
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
          if((_tmp_0 == 15) && xready) begin
            xfsm <= xfsm_13;
          end 
        end
        xfsm_13: begin
          xvalid <= 0;
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
          if((_tmp_0 == 30) && xready) begin
            xfsm <= xfsm_24;
          end 
        end
        xfsm_24: begin
          xvalid <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  localparam yfsm_1 = 1;
  localparam yfsm_2 = 2;
  localparam yfsm_3 = 3;
  localparam yfsm_4 = 4;
  localparam yfsm_5 = 5;
  localparam yfsm_6 = 6;
  localparam yfsm_7 = 7;
  localparam yfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
    end else begin
      case(yfsm)
        yfsm_init: begin
          yready <= 0;
          if(reset_done) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          yfsm <= yfsm_2;
        end
        yfsm_2: begin
          if(yvalid) begin
            yready <= 1;
          end 
          if(yvalid) begin
            yfsm <= yfsm_3;
          end 
        end
        yfsm_3: begin
          yready <= 0;
          yfsm <= yfsm_4;
        end
        yfsm_4: begin
          yready <= 0;
          yfsm <= yfsm_5;
        end
        yfsm_5: begin
          yready <= 0;
          yfsm <= yfsm_6;
        end
        yfsm_6: begin
          yready <= 0;
          yfsm <= yfsm_7;
        end
        yfsm_7: begin
          yready <= 0;
          yfsm <= yfsm_8;
        end
        yfsm_8: begin
          yfsm <= yfsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(xvalid && xready) begin
        $display("xdata=%d", xdata);
      end 
      if(yvalid && yready) begin
        $display("ydata=%d", ydata);
      end 
    end 
  end


endmodule



module movmin
(
  input CLK,
  input RST,
  input signed [32-1:0] xdata,
  input xvalid,
  output xready,
  output signed [32-1:0] ydata,
  output yvalid,
  input yready
);

  reg signed [32-1:0] _dataflow__prev_data_1;
  reg signed [32-1:0] _dataflow__prev_data_2;
  reg signed [32-1:0] _dataflow__prev_data_3;
  reg signed [32-1:0] _dataflow__prev_data_4;
  reg signed [32-1:0] _dataflow__prev_data_5;
  reg signed [32-1:0] _dataflow__prev_data_6;
  reg signed [32-1:0] _dataflow__prev_data_7;
  reg [1-1:0] _dataflow_lessthan_data_8;
  reg _dataflow_lessthan_valid_8;
  wire _dataflow_lessthan_ready_8;
  reg [1-1:0] _dataflow_lessthan_data_10;
  reg _dataflow_lessthan_valid_10;
  wire _dataflow_lessthan_ready_10;
  reg [1-1:0] _dataflow_lessthan_data_12;
  reg _dataflow_lessthan_valid_12;
  wire _dataflow_lessthan_ready_12;
  reg [1-1:0] _dataflow_lessthan_data_14;
  reg _dataflow_lessthan_valid_14;
  wire _dataflow_lessthan_ready_14;
  reg signed [32-1:0] _dataflow__delay_data_22;
  reg _dataflow__delay_valid_22;
  wire _dataflow__delay_ready_22;
  reg signed [32-1:0] _dataflow__delay_data_23;
  reg _dataflow__delay_valid_23;
  wire _dataflow__delay_ready_23;
  reg signed [32-1:0] _dataflow__delay_data_24;
  reg _dataflow__delay_valid_24;
  wire _dataflow__delay_ready_24;
  reg signed [32-1:0] _dataflow__delay_data_25;
  reg _dataflow__delay_valid_25;
  wire _dataflow__delay_ready_25;
  reg signed [32-1:0] _dataflow__delay_data_28;
  reg _dataflow__delay_valid_28;
  wire _dataflow__delay_ready_28;
  reg signed [32-1:0] _dataflow__delay_data_29;
  reg _dataflow__delay_valid_29;
  wire _dataflow__delay_ready_29;
  reg signed [32-1:0] _dataflow__delay_data_30;
  reg _dataflow__delay_valid_30;
  wire _dataflow__delay_ready_30;
  reg signed [32-1:0] _dataflow__delay_data_31;
  reg _dataflow__delay_valid_31;
  wire _dataflow__delay_ready_31;
  assign xready = (_dataflow_lessthan_ready_8 || !_dataflow_lessthan_valid_8) && (xvalid && xvalid) && ((_dataflow_lessthan_ready_8 || !_dataflow_lessthan_valid_8) && (xvalid && xvalid)) && ((_dataflow_lessthan_ready_10 || !_dataflow_lessthan_valid_10) && (xvalid && xvalid)) && ((_dataflow_lessthan_ready_10 || !_dataflow_lessthan_valid_10) && (xvalid && xvalid)) && ((_dataflow_lessthan_ready_12 || !_dataflow_lessthan_valid_12) && (xvalid && xvalid)) && ((_dataflow_lessthan_ready_12 || !_dataflow_lessthan_valid_12) && (xvalid && xvalid)) && ((_dataflow_lessthan_ready_14 || !_dataflow_lessthan_valid_14) && (xvalid && xvalid)) && ((_dataflow_lessthan_ready_14 || !_dataflow_lessthan_valid_14) && (xvalid && xvalid)) && ((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && xvalid) && ((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && xvalid) && ((_dataflow__delay_ready_24 || !_dataflow__delay_valid_24) && xvalid) && ((_dataflow__delay_ready_25 || !_dataflow__delay_valid_25) && xvalid) && ((_dataflow__delay_ready_28 || !_dataflow__delay_valid_28) && xvalid) && ((_dataflow__delay_ready_29 || !_dataflow__delay_valid_29) && xvalid) && ((_dataflow__delay_ready_30 || !_dataflow__delay_valid_30) && xvalid) && ((_dataflow__delay_ready_31 || !_dataflow__delay_valid_31) && xvalid);
  reg signed [32-1:0] _dataflow_cond_data_9;
  reg _dataflow_cond_valid_9;
  wire _dataflow_cond_ready_9;
  assign _dataflow_lessthan_ready_8 = (_dataflow_cond_ready_9 || !_dataflow_cond_valid_9) && (_dataflow_lessthan_valid_8 && _dataflow__delay_valid_22 && _dataflow__delay_valid_23);
  assign _dataflow__delay_ready_22 = (_dataflow_cond_ready_9 || !_dataflow_cond_valid_9) && (_dataflow_lessthan_valid_8 && _dataflow__delay_valid_22 && _dataflow__delay_valid_23);
  assign _dataflow__delay_ready_23 = (_dataflow_cond_ready_9 || !_dataflow_cond_valid_9) && (_dataflow_lessthan_valid_8 && _dataflow__delay_valid_22 && _dataflow__delay_valid_23);
  reg signed [32-1:0] _dataflow_cond_data_11;
  reg _dataflow_cond_valid_11;
  wire _dataflow_cond_ready_11;
  assign _dataflow_lessthan_ready_10 = (_dataflow_cond_ready_11 || !_dataflow_cond_valid_11) && (_dataflow_lessthan_valid_10 && _dataflow__delay_valid_24 && _dataflow__delay_valid_25);
  assign _dataflow__delay_ready_24 = (_dataflow_cond_ready_11 || !_dataflow_cond_valid_11) && (_dataflow_lessthan_valid_10 && _dataflow__delay_valid_24 && _dataflow__delay_valid_25);
  assign _dataflow__delay_ready_25 = (_dataflow_cond_ready_11 || !_dataflow_cond_valid_11) && (_dataflow_lessthan_valid_10 && _dataflow__delay_valid_24 && _dataflow__delay_valid_25);
  reg signed [32-1:0] _dataflow_cond_data_13;
  reg _dataflow_cond_valid_13;
  wire _dataflow_cond_ready_13;
  assign _dataflow_lessthan_ready_12 = (_dataflow_cond_ready_13 || !_dataflow_cond_valid_13) && (_dataflow_lessthan_valid_12 && _dataflow__delay_valid_28 && _dataflow__delay_valid_29);
  assign _dataflow__delay_ready_28 = (_dataflow_cond_ready_13 || !_dataflow_cond_valid_13) && (_dataflow_lessthan_valid_12 && _dataflow__delay_valid_28 && _dataflow__delay_valid_29);
  assign _dataflow__delay_ready_29 = (_dataflow_cond_ready_13 || !_dataflow_cond_valid_13) && (_dataflow_lessthan_valid_12 && _dataflow__delay_valid_28 && _dataflow__delay_valid_29);
  reg signed [32-1:0] _dataflow_cond_data_15;
  reg _dataflow_cond_valid_15;
  wire _dataflow_cond_ready_15;
  assign _dataflow_lessthan_ready_14 = (_dataflow_cond_ready_15 || !_dataflow_cond_valid_15) && (_dataflow_lessthan_valid_14 && _dataflow__delay_valid_30 && _dataflow__delay_valid_31);
  assign _dataflow__delay_ready_30 = (_dataflow_cond_ready_15 || !_dataflow_cond_valid_15) && (_dataflow_lessthan_valid_14 && _dataflow__delay_valid_30 && _dataflow__delay_valid_31);
  assign _dataflow__delay_ready_31 = (_dataflow_cond_ready_15 || !_dataflow_cond_valid_15) && (_dataflow_lessthan_valid_14 && _dataflow__delay_valid_30 && _dataflow__delay_valid_31);
  reg [1-1:0] _dataflow_lessthan_data_16;
  reg _dataflow_lessthan_valid_16;
  wire _dataflow_lessthan_ready_16;
  reg [1-1:0] _dataflow_lessthan_data_18;
  reg _dataflow_lessthan_valid_18;
  wire _dataflow_lessthan_ready_18;
  reg signed [32-1:0] _dataflow__delay_data_26;
  reg _dataflow__delay_valid_26;
  wire _dataflow__delay_ready_26;
  assign _dataflow_cond_ready_9 = (_dataflow_lessthan_ready_16 || !_dataflow_lessthan_valid_16) && (_dataflow_cond_valid_9 && _dataflow_cond_valid_11) && ((_dataflow__delay_ready_26 || !_dataflow__delay_valid_26) && _dataflow_cond_valid_9);
  reg signed [32-1:0] _dataflow__delay_data_27;
  reg _dataflow__delay_valid_27;
  wire _dataflow__delay_ready_27;
  assign _dataflow_cond_ready_11 = (_dataflow_lessthan_ready_16 || !_dataflow_lessthan_valid_16) && (_dataflow_cond_valid_9 && _dataflow_cond_valid_11) && ((_dataflow__delay_ready_27 || !_dataflow__delay_valid_27) && _dataflow_cond_valid_11);
  reg signed [32-1:0] _dataflow__delay_data_32;
  reg _dataflow__delay_valid_32;
  wire _dataflow__delay_ready_32;
  assign _dataflow_cond_ready_13 = (_dataflow_lessthan_ready_18 || !_dataflow_lessthan_valid_18) && (_dataflow_cond_valid_13 && _dataflow_cond_valid_15) && ((_dataflow__delay_ready_32 || !_dataflow__delay_valid_32) && _dataflow_cond_valid_13);
  reg signed [32-1:0] _dataflow__delay_data_33;
  reg _dataflow__delay_valid_33;
  wire _dataflow__delay_ready_33;
  assign _dataflow_cond_ready_15 = (_dataflow_lessthan_ready_18 || !_dataflow_lessthan_valid_18) && (_dataflow_cond_valid_13 && _dataflow_cond_valid_15) && ((_dataflow__delay_ready_33 || !_dataflow__delay_valid_33) && _dataflow_cond_valid_15);
  reg signed [32-1:0] _dataflow_cond_data_17;
  reg _dataflow_cond_valid_17;
  wire _dataflow_cond_ready_17;
  assign _dataflow_lessthan_ready_16 = (_dataflow_cond_ready_17 || !_dataflow_cond_valid_17) && (_dataflow_lessthan_valid_16 && _dataflow__delay_valid_26 && _dataflow__delay_valid_27);
  assign _dataflow__delay_ready_26 = (_dataflow_cond_ready_17 || !_dataflow_cond_valid_17) && (_dataflow_lessthan_valid_16 && _dataflow__delay_valid_26 && _dataflow__delay_valid_27);
  assign _dataflow__delay_ready_27 = (_dataflow_cond_ready_17 || !_dataflow_cond_valid_17) && (_dataflow_lessthan_valid_16 && _dataflow__delay_valid_26 && _dataflow__delay_valid_27);
  reg signed [32-1:0] _dataflow_cond_data_19;
  reg _dataflow_cond_valid_19;
  wire _dataflow_cond_ready_19;
  assign _dataflow_lessthan_ready_18 = (_dataflow_cond_ready_19 || !_dataflow_cond_valid_19) && (_dataflow_lessthan_valid_18 && _dataflow__delay_valid_32 && _dataflow__delay_valid_33);
  assign _dataflow__delay_ready_32 = (_dataflow_cond_ready_19 || !_dataflow_cond_valid_19) && (_dataflow_lessthan_valid_18 && _dataflow__delay_valid_32 && _dataflow__delay_valid_33);
  assign _dataflow__delay_ready_33 = (_dataflow_cond_ready_19 || !_dataflow_cond_valid_19) && (_dataflow_lessthan_valid_18 && _dataflow__delay_valid_32 && _dataflow__delay_valid_33);
  reg [1-1:0] _dataflow_lessthan_data_20;
  reg _dataflow_lessthan_valid_20;
  wire _dataflow_lessthan_ready_20;
  reg signed [32-1:0] _dataflow__delay_data_34;
  reg _dataflow__delay_valid_34;
  wire _dataflow__delay_ready_34;
  assign _dataflow_cond_ready_17 = (_dataflow_lessthan_ready_20 || !_dataflow_lessthan_valid_20) && (_dataflow_cond_valid_17 && _dataflow_cond_valid_19) && ((_dataflow__delay_ready_34 || !_dataflow__delay_valid_34) && _dataflow_cond_valid_17);
  reg signed [32-1:0] _dataflow__delay_data_35;
  reg _dataflow__delay_valid_35;
  wire _dataflow__delay_ready_35;
  assign _dataflow_cond_ready_19 = (_dataflow_lessthan_ready_20 || !_dataflow_lessthan_valid_20) && (_dataflow_cond_valid_17 && _dataflow_cond_valid_19) && ((_dataflow__delay_ready_35 || !_dataflow__delay_valid_35) && _dataflow_cond_valid_19);
  reg signed [32-1:0] _dataflow_cond_data_21;
  reg _dataflow_cond_valid_21;
  wire _dataflow_cond_ready_21;
  assign _dataflow_lessthan_ready_20 = (_dataflow_cond_ready_21 || !_dataflow_cond_valid_21) && (_dataflow_lessthan_valid_20 && _dataflow__delay_valid_34 && _dataflow__delay_valid_35);
  assign _dataflow__delay_ready_34 = (_dataflow_cond_ready_21 || !_dataflow_cond_valid_21) && (_dataflow_lessthan_valid_20 && _dataflow__delay_valid_34 && _dataflow__delay_valid_35);
  assign _dataflow__delay_ready_35 = (_dataflow_cond_ready_21 || !_dataflow_cond_valid_21) && (_dataflow_lessthan_valid_20 && _dataflow__delay_valid_34 && _dataflow__delay_valid_35);
  assign ydata = _dataflow_cond_data_21;
  assign yvalid = _dataflow_cond_valid_21;
  assign _dataflow_cond_ready_21 = yready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow__prev_data_1 <= 0;
      _dataflow__prev_data_2 <= 0;
      _dataflow__prev_data_3 <= 0;
      _dataflow__prev_data_4 <= 0;
      _dataflow__prev_data_5 <= 0;
      _dataflow__prev_data_6 <= 0;
      _dataflow__prev_data_7 <= 0;
      _dataflow_lessthan_data_8 <= 0;
      _dataflow_lessthan_valid_8 <= 0;
      _dataflow_lessthan_data_10 <= 0;
      _dataflow_lessthan_valid_10 <= 0;
      _dataflow_lessthan_data_12 <= 0;
      _dataflow_lessthan_valid_12 <= 0;
      _dataflow_lessthan_data_14 <= 0;
      _dataflow_lessthan_valid_14 <= 0;
      _dataflow__delay_data_22 <= 0;
      _dataflow__delay_valid_22 <= 0;
      _dataflow__delay_data_23 <= 0;
      _dataflow__delay_valid_23 <= 0;
      _dataflow__delay_data_24 <= 0;
      _dataflow__delay_valid_24 <= 0;
      _dataflow__delay_data_25 <= 0;
      _dataflow__delay_valid_25 <= 0;
      _dataflow__delay_data_28 <= 0;
      _dataflow__delay_valid_28 <= 0;
      _dataflow__delay_data_29 <= 0;
      _dataflow__delay_valid_29 <= 0;
      _dataflow__delay_data_30 <= 0;
      _dataflow__delay_valid_30 <= 0;
      _dataflow__delay_data_31 <= 0;
      _dataflow__delay_valid_31 <= 0;
      _dataflow_cond_data_9 <= 0;
      _dataflow_cond_valid_9 <= 0;
      _dataflow_cond_data_11 <= 0;
      _dataflow_cond_valid_11 <= 0;
      _dataflow_cond_data_13 <= 0;
      _dataflow_cond_valid_13 <= 0;
      _dataflow_cond_data_15 <= 0;
      _dataflow_cond_valid_15 <= 0;
      _dataflow_lessthan_data_16 <= 0;
      _dataflow_lessthan_valid_16 <= 0;
      _dataflow_lessthan_data_18 <= 0;
      _dataflow_lessthan_valid_18 <= 0;
      _dataflow__delay_data_26 <= 0;
      _dataflow__delay_valid_26 <= 0;
      _dataflow__delay_data_27 <= 0;
      _dataflow__delay_valid_27 <= 0;
      _dataflow__delay_data_32 <= 0;
      _dataflow__delay_valid_32 <= 0;
      _dataflow__delay_data_33 <= 0;
      _dataflow__delay_valid_33 <= 0;
      _dataflow_cond_data_17 <= 0;
      _dataflow_cond_valid_17 <= 0;
      _dataflow_cond_data_19 <= 0;
      _dataflow_cond_valid_19 <= 0;
      _dataflow_lessthan_data_20 <= 0;
      _dataflow_lessthan_valid_20 <= 0;
      _dataflow__delay_data_34 <= 0;
      _dataflow__delay_valid_34 <= 0;
      _dataflow__delay_data_35 <= 0;
      _dataflow__delay_valid_35 <= 0;
      _dataflow_cond_data_21 <= 0;
      _dataflow_cond_valid_21 <= 0;
    end else begin
      if(xvalid && xready) begin
        _dataflow__prev_data_1 <= xdata;
      end 
      if(xvalid && xready) begin
        _dataflow__prev_data_2 <= _dataflow__prev_data_1;
      end 
      if(xvalid && xready) begin
        _dataflow__prev_data_3 <= _dataflow__prev_data_2;
      end 
      if(xvalid && xready) begin
        _dataflow__prev_data_4 <= _dataflow__prev_data_3;
      end 
      if(xvalid && xready) begin
        _dataflow__prev_data_5 <= _dataflow__prev_data_4;
      end 
      if(xvalid && xready) begin
        _dataflow__prev_data_6 <= _dataflow__prev_data_5;
      end 
      if(xvalid && xready) begin
        _dataflow__prev_data_7 <= _dataflow__prev_data_6;
      end 
      if((_dataflow_lessthan_ready_8 || !_dataflow_lessthan_valid_8) && (xready && xready) && (xvalid && xvalid)) begin
        _dataflow_lessthan_data_8 <= xdata < _dataflow__prev_data_1;
      end 
      if(_dataflow_lessthan_valid_8 && _dataflow_lessthan_ready_8) begin
        _dataflow_lessthan_valid_8 <= 0;
      end 
      if((_dataflow_lessthan_ready_8 || !_dataflow_lessthan_valid_8) && (xready && xready)) begin
        _dataflow_lessthan_valid_8 <= xvalid && xvalid;
      end 
      if((_dataflow_lessthan_ready_10 || !_dataflow_lessthan_valid_10) && (xready && xready) && (xvalid && xvalid)) begin
        _dataflow_lessthan_data_10 <= _dataflow__prev_data_2 < _dataflow__prev_data_3;
      end 
      if(_dataflow_lessthan_valid_10 && _dataflow_lessthan_ready_10) begin
        _dataflow_lessthan_valid_10 <= 0;
      end 
      if((_dataflow_lessthan_ready_10 || !_dataflow_lessthan_valid_10) && (xready && xready)) begin
        _dataflow_lessthan_valid_10 <= xvalid && xvalid;
      end 
      if((_dataflow_lessthan_ready_12 || !_dataflow_lessthan_valid_12) && (xready && xready) && (xvalid && xvalid)) begin
        _dataflow_lessthan_data_12 <= _dataflow__prev_data_4 < _dataflow__prev_data_5;
      end 
      if(_dataflow_lessthan_valid_12 && _dataflow_lessthan_ready_12) begin
        _dataflow_lessthan_valid_12 <= 0;
      end 
      if((_dataflow_lessthan_ready_12 || !_dataflow_lessthan_valid_12) && (xready && xready)) begin
        _dataflow_lessthan_valid_12 <= xvalid && xvalid;
      end 
      if((_dataflow_lessthan_ready_14 || !_dataflow_lessthan_valid_14) && (xready && xready) && (xvalid && xvalid)) begin
        _dataflow_lessthan_data_14 <= _dataflow__prev_data_6 < _dataflow__prev_data_7;
      end 
      if(_dataflow_lessthan_valid_14 && _dataflow_lessthan_ready_14) begin
        _dataflow_lessthan_valid_14 <= 0;
      end 
      if((_dataflow_lessthan_ready_14 || !_dataflow_lessthan_valid_14) && (xready && xready)) begin
        _dataflow_lessthan_valid_14 <= xvalid && xvalid;
      end 
      if((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && xready && xvalid) begin
        _dataflow__delay_data_22 <= xdata;
      end 
      if(_dataflow__delay_valid_22 && _dataflow__delay_ready_22) begin
        _dataflow__delay_valid_22 <= 0;
      end 
      if((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && xready) begin
        _dataflow__delay_valid_22 <= xvalid;
      end 
      if((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && xready && xvalid) begin
        _dataflow__delay_data_23 <= _dataflow__prev_data_1;
      end 
      if(_dataflow__delay_valid_23 && _dataflow__delay_ready_23) begin
        _dataflow__delay_valid_23 <= 0;
      end 
      if((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && xready) begin
        _dataflow__delay_valid_23 <= xvalid;
      end 
      if((_dataflow__delay_ready_24 || !_dataflow__delay_valid_24) && xready && xvalid) begin
        _dataflow__delay_data_24 <= _dataflow__prev_data_2;
      end 
      if(_dataflow__delay_valid_24 && _dataflow__delay_ready_24) begin
        _dataflow__delay_valid_24 <= 0;
      end 
      if((_dataflow__delay_ready_24 || !_dataflow__delay_valid_24) && xready) begin
        _dataflow__delay_valid_24 <= xvalid;
      end 
      if((_dataflow__delay_ready_25 || !_dataflow__delay_valid_25) && xready && xvalid) begin
        _dataflow__delay_data_25 <= _dataflow__prev_data_3;
      end 
      if(_dataflow__delay_valid_25 && _dataflow__delay_ready_25) begin
        _dataflow__delay_valid_25 <= 0;
      end 
      if((_dataflow__delay_ready_25 || !_dataflow__delay_valid_25) && xready) begin
        _dataflow__delay_valid_25 <= xvalid;
      end 
      if((_dataflow__delay_ready_28 || !_dataflow__delay_valid_28) && xready && xvalid) begin
        _dataflow__delay_data_28 <= _dataflow__prev_data_4;
      end 
      if(_dataflow__delay_valid_28 && _dataflow__delay_ready_28) begin
        _dataflow__delay_valid_28 <= 0;
      end 
      if((_dataflow__delay_ready_28 || !_dataflow__delay_valid_28) && xready) begin
        _dataflow__delay_valid_28 <= xvalid;
      end 
      if((_dataflow__delay_ready_29 || !_dataflow__delay_valid_29) && xready && xvalid) begin
        _dataflow__delay_data_29 <= _dataflow__prev_data_5;
      end 
      if(_dataflow__delay_valid_29 && _dataflow__delay_ready_29) begin
        _dataflow__delay_valid_29 <= 0;
      end 
      if((_dataflow__delay_ready_29 || !_dataflow__delay_valid_29) && xready) begin
        _dataflow__delay_valid_29 <= xvalid;
      end 
      if((_dataflow__delay_ready_30 || !_dataflow__delay_valid_30) && xready && xvalid) begin
        _dataflow__delay_data_30 <= _dataflow__prev_data_6;
      end 
      if(_dataflow__delay_valid_30 && _dataflow__delay_ready_30) begin
        _dataflow__delay_valid_30 <= 0;
      end 
      if((_dataflow__delay_ready_30 || !_dataflow__delay_valid_30) && xready) begin
        _dataflow__delay_valid_30 <= xvalid;
      end 
      if((_dataflow__delay_ready_31 || !_dataflow__delay_valid_31) && xready && xvalid) begin
        _dataflow__delay_data_31 <= _dataflow__prev_data_7;
      end 
      if(_dataflow__delay_valid_31 && _dataflow__delay_ready_31) begin
        _dataflow__delay_valid_31 <= 0;
      end 
      if((_dataflow__delay_ready_31 || !_dataflow__delay_valid_31) && xready) begin
        _dataflow__delay_valid_31 <= xvalid;
      end 
      if((_dataflow_cond_ready_9 || !_dataflow_cond_valid_9) && (_dataflow_lessthan_ready_8 && _dataflow__delay_ready_22 && _dataflow__delay_ready_23) && (_dataflow_lessthan_valid_8 && _dataflow__delay_valid_22 && _dataflow__delay_valid_23)) begin
        _dataflow_cond_data_9 <= (_dataflow_lessthan_data_8)? _dataflow__delay_data_22 : _dataflow__delay_data_23;
      end 
      if(_dataflow_cond_valid_9 && _dataflow_cond_ready_9) begin
        _dataflow_cond_valid_9 <= 0;
      end 
      if((_dataflow_cond_ready_9 || !_dataflow_cond_valid_9) && (_dataflow_lessthan_ready_8 && _dataflow__delay_ready_22 && _dataflow__delay_ready_23)) begin
        _dataflow_cond_valid_9 <= _dataflow_lessthan_valid_8 && _dataflow__delay_valid_22 && _dataflow__delay_valid_23;
      end 
      if((_dataflow_cond_ready_11 || !_dataflow_cond_valid_11) && (_dataflow_lessthan_ready_10 && _dataflow__delay_ready_24 && _dataflow__delay_ready_25) && (_dataflow_lessthan_valid_10 && _dataflow__delay_valid_24 && _dataflow__delay_valid_25)) begin
        _dataflow_cond_data_11 <= (_dataflow_lessthan_data_10)? _dataflow__delay_data_24 : _dataflow__delay_data_25;
      end 
      if(_dataflow_cond_valid_11 && _dataflow_cond_ready_11) begin
        _dataflow_cond_valid_11 <= 0;
      end 
      if((_dataflow_cond_ready_11 || !_dataflow_cond_valid_11) && (_dataflow_lessthan_ready_10 && _dataflow__delay_ready_24 && _dataflow__delay_ready_25)) begin
        _dataflow_cond_valid_11 <= _dataflow_lessthan_valid_10 && _dataflow__delay_valid_24 && _dataflow__delay_valid_25;
      end 
      if((_dataflow_cond_ready_13 || !_dataflow_cond_valid_13) && (_dataflow_lessthan_ready_12 && _dataflow__delay_ready_28 && _dataflow__delay_ready_29) && (_dataflow_lessthan_valid_12 && _dataflow__delay_valid_28 && _dataflow__delay_valid_29)) begin
        _dataflow_cond_data_13 <= (_dataflow_lessthan_data_12)? _dataflow__delay_data_28 : _dataflow__delay_data_29;
      end 
      if(_dataflow_cond_valid_13 && _dataflow_cond_ready_13) begin
        _dataflow_cond_valid_13 <= 0;
      end 
      if((_dataflow_cond_ready_13 || !_dataflow_cond_valid_13) && (_dataflow_lessthan_ready_12 && _dataflow__delay_ready_28 && _dataflow__delay_ready_29)) begin
        _dataflow_cond_valid_13 <= _dataflow_lessthan_valid_12 && _dataflow__delay_valid_28 && _dataflow__delay_valid_29;
      end 
      if((_dataflow_cond_ready_15 || !_dataflow_cond_valid_15) && (_dataflow_lessthan_ready_14 && _dataflow__delay_ready_30 && _dataflow__delay_ready_31) && (_dataflow_lessthan_valid_14 && _dataflow__delay_valid_30 && _dataflow__delay_valid_31)) begin
        _dataflow_cond_data_15 <= (_dataflow_lessthan_data_14)? _dataflow__delay_data_30 : _dataflow__delay_data_31;
      end 
      if(_dataflow_cond_valid_15 && _dataflow_cond_ready_15) begin
        _dataflow_cond_valid_15 <= 0;
      end 
      if((_dataflow_cond_ready_15 || !_dataflow_cond_valid_15) && (_dataflow_lessthan_ready_14 && _dataflow__delay_ready_30 && _dataflow__delay_ready_31)) begin
        _dataflow_cond_valid_15 <= _dataflow_lessthan_valid_14 && _dataflow__delay_valid_30 && _dataflow__delay_valid_31;
      end 
      if((_dataflow_lessthan_ready_16 || !_dataflow_lessthan_valid_16) && (_dataflow_cond_ready_9 && _dataflow_cond_ready_11) && (_dataflow_cond_valid_9 && _dataflow_cond_valid_11)) begin
        _dataflow_lessthan_data_16 <= _dataflow_cond_data_9 < _dataflow_cond_data_11;
      end 
      if(_dataflow_lessthan_valid_16 && _dataflow_lessthan_ready_16) begin
        _dataflow_lessthan_valid_16 <= 0;
      end 
      if((_dataflow_lessthan_ready_16 || !_dataflow_lessthan_valid_16) && (_dataflow_cond_ready_9 && _dataflow_cond_ready_11)) begin
        _dataflow_lessthan_valid_16 <= _dataflow_cond_valid_9 && _dataflow_cond_valid_11;
      end 
      if((_dataflow_lessthan_ready_18 || !_dataflow_lessthan_valid_18) && (_dataflow_cond_ready_13 && _dataflow_cond_ready_15) && (_dataflow_cond_valid_13 && _dataflow_cond_valid_15)) begin
        _dataflow_lessthan_data_18 <= _dataflow_cond_data_13 < _dataflow_cond_data_15;
      end 
      if(_dataflow_lessthan_valid_18 && _dataflow_lessthan_ready_18) begin
        _dataflow_lessthan_valid_18 <= 0;
      end 
      if((_dataflow_lessthan_ready_18 || !_dataflow_lessthan_valid_18) && (_dataflow_cond_ready_13 && _dataflow_cond_ready_15)) begin
        _dataflow_lessthan_valid_18 <= _dataflow_cond_valid_13 && _dataflow_cond_valid_15;
      end 
      if((_dataflow__delay_ready_26 || !_dataflow__delay_valid_26) && _dataflow_cond_ready_9 && _dataflow_cond_valid_9) begin
        _dataflow__delay_data_26 <= _dataflow_cond_data_9;
      end 
      if(_dataflow__delay_valid_26 && _dataflow__delay_ready_26) begin
        _dataflow__delay_valid_26 <= 0;
      end 
      if((_dataflow__delay_ready_26 || !_dataflow__delay_valid_26) && _dataflow_cond_ready_9) begin
        _dataflow__delay_valid_26 <= _dataflow_cond_valid_9;
      end 
      if((_dataflow__delay_ready_27 || !_dataflow__delay_valid_27) && _dataflow_cond_ready_11 && _dataflow_cond_valid_11) begin
        _dataflow__delay_data_27 <= _dataflow_cond_data_11;
      end 
      if(_dataflow__delay_valid_27 && _dataflow__delay_ready_27) begin
        _dataflow__delay_valid_27 <= 0;
      end 
      if((_dataflow__delay_ready_27 || !_dataflow__delay_valid_27) && _dataflow_cond_ready_11) begin
        _dataflow__delay_valid_27 <= _dataflow_cond_valid_11;
      end 
      if((_dataflow__delay_ready_32 || !_dataflow__delay_valid_32) && _dataflow_cond_ready_13 && _dataflow_cond_valid_13) begin
        _dataflow__delay_data_32 <= _dataflow_cond_data_13;
      end 
      if(_dataflow__delay_valid_32 && _dataflow__delay_ready_32) begin
        _dataflow__delay_valid_32 <= 0;
      end 
      if((_dataflow__delay_ready_32 || !_dataflow__delay_valid_32) && _dataflow_cond_ready_13) begin
        _dataflow__delay_valid_32 <= _dataflow_cond_valid_13;
      end 
      if((_dataflow__delay_ready_33 || !_dataflow__delay_valid_33) && _dataflow_cond_ready_15 && _dataflow_cond_valid_15) begin
        _dataflow__delay_data_33 <= _dataflow_cond_data_15;
      end 
      if(_dataflow__delay_valid_33 && _dataflow__delay_ready_33) begin
        _dataflow__delay_valid_33 <= 0;
      end 
      if((_dataflow__delay_ready_33 || !_dataflow__delay_valid_33) && _dataflow_cond_ready_15) begin
        _dataflow__delay_valid_33 <= _dataflow_cond_valid_15;
      end 
      if((_dataflow_cond_ready_17 || !_dataflow_cond_valid_17) && (_dataflow_lessthan_ready_16 && _dataflow__delay_ready_26 && _dataflow__delay_ready_27) && (_dataflow_lessthan_valid_16 && _dataflow__delay_valid_26 && _dataflow__delay_valid_27)) begin
        _dataflow_cond_data_17 <= (_dataflow_lessthan_data_16)? _dataflow__delay_data_26 : _dataflow__delay_data_27;
      end 
      if(_dataflow_cond_valid_17 && _dataflow_cond_ready_17) begin
        _dataflow_cond_valid_17 <= 0;
      end 
      if((_dataflow_cond_ready_17 || !_dataflow_cond_valid_17) && (_dataflow_lessthan_ready_16 && _dataflow__delay_ready_26 && _dataflow__delay_ready_27)) begin
        _dataflow_cond_valid_17 <= _dataflow_lessthan_valid_16 && _dataflow__delay_valid_26 && _dataflow__delay_valid_27;
      end 
      if((_dataflow_cond_ready_19 || !_dataflow_cond_valid_19) && (_dataflow_lessthan_ready_18 && _dataflow__delay_ready_32 && _dataflow__delay_ready_33) && (_dataflow_lessthan_valid_18 && _dataflow__delay_valid_32 && _dataflow__delay_valid_33)) begin
        _dataflow_cond_data_19 <= (_dataflow_lessthan_data_18)? _dataflow__delay_data_32 : _dataflow__delay_data_33;
      end 
      if(_dataflow_cond_valid_19 && _dataflow_cond_ready_19) begin
        _dataflow_cond_valid_19 <= 0;
      end 
      if((_dataflow_cond_ready_19 || !_dataflow_cond_valid_19) && (_dataflow_lessthan_ready_18 && _dataflow__delay_ready_32 && _dataflow__delay_ready_33)) begin
        _dataflow_cond_valid_19 <= _dataflow_lessthan_valid_18 && _dataflow__delay_valid_32 && _dataflow__delay_valid_33;
      end 
      if((_dataflow_lessthan_ready_20 || !_dataflow_lessthan_valid_20) && (_dataflow_cond_ready_17 && _dataflow_cond_ready_19) && (_dataflow_cond_valid_17 && _dataflow_cond_valid_19)) begin
        _dataflow_lessthan_data_20 <= _dataflow_cond_data_17 < _dataflow_cond_data_19;
      end 
      if(_dataflow_lessthan_valid_20 && _dataflow_lessthan_ready_20) begin
        _dataflow_lessthan_valid_20 <= 0;
      end 
      if((_dataflow_lessthan_ready_20 || !_dataflow_lessthan_valid_20) && (_dataflow_cond_ready_17 && _dataflow_cond_ready_19)) begin
        _dataflow_lessthan_valid_20 <= _dataflow_cond_valid_17 && _dataflow_cond_valid_19;
      end 
      if((_dataflow__delay_ready_34 || !_dataflow__delay_valid_34) && _dataflow_cond_ready_17 && _dataflow_cond_valid_17) begin
        _dataflow__delay_data_34 <= _dataflow_cond_data_17;
      end 
      if(_dataflow__delay_valid_34 && _dataflow__delay_ready_34) begin
        _dataflow__delay_valid_34 <= 0;
      end 
      if((_dataflow__delay_ready_34 || !_dataflow__delay_valid_34) && _dataflow_cond_ready_17) begin
        _dataflow__delay_valid_34 <= _dataflow_cond_valid_17;
      end 
      if((_dataflow__delay_ready_35 || !_dataflow__delay_valid_35) && _dataflow_cond_ready_19 && _dataflow_cond_valid_19) begin
        _dataflow__delay_data_35 <= _dataflow_cond_data_19;
      end 
      if(_dataflow__delay_valid_35 && _dataflow__delay_ready_35) begin
        _dataflow__delay_valid_35 <= 0;
      end 
      if((_dataflow__delay_ready_35 || !_dataflow__delay_valid_35) && _dataflow_cond_ready_19) begin
        _dataflow__delay_valid_35 <= _dataflow_cond_valid_19;
      end 
      if((_dataflow_cond_ready_21 || !_dataflow_cond_valid_21) && (_dataflow_lessthan_ready_20 && _dataflow__delay_ready_34 && _dataflow__delay_ready_35) && (_dataflow_lessthan_valid_20 && _dataflow__delay_valid_34 && _dataflow__delay_valid_35)) begin
        _dataflow_cond_data_21 <= (_dataflow_lessthan_data_20)? _dataflow__delay_data_34 : _dataflow__delay_data_35;
      end 
      if(_dataflow_cond_valid_21 && _dataflow_cond_ready_21) begin
        _dataflow_cond_valid_21 <= 0;
      end 
      if((_dataflow_cond_ready_21 || !_dataflow_cond_valid_21) && (_dataflow_lessthan_ready_20 && _dataflow__delay_ready_34 && _dataflow__delay_ready_35)) begin
        _dataflow_cond_valid_21 <= _dataflow_lessthan_valid_20 && _dataflow__delay_valid_34 && _dataflow__delay_valid_35;
      end 
    end
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_movmin.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
