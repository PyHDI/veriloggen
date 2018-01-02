from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_movmin

expected_verilog = """
module test;

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

  reg signed [32-1:0] __prev_data_0;
  reg signed [32-1:0] __prev_data_1;
  reg signed [32-1:0] __prev_data_2;
  reg signed [32-1:0] __prev_data_3;
  reg signed [32-1:0] __prev_data_4;
  reg signed [32-1:0] __prev_data_5;
  reg signed [32-1:0] __prev_data_6;
  reg [1-1:0] _lessthan_data_7;
  reg _lessthan_valid_7;
  wire _lessthan_ready_7;
  reg [1-1:0] _lessthan_data_8;
  reg _lessthan_valid_8;
  wire _lessthan_ready_8;
  reg [1-1:0] _lessthan_data_9;
  reg _lessthan_valid_9;
  wire _lessthan_ready_9;
  reg [1-1:0] _lessthan_data_10;
  reg _lessthan_valid_10;
  wire _lessthan_ready_10;
  reg signed [32-1:0] __delay_data_11;
  reg __delay_valid_11;
  wire __delay_ready_11;
  reg signed [32-1:0] __delay_data_12;
  reg __delay_valid_12;
  wire __delay_ready_12;
  reg signed [32-1:0] __delay_data_13;
  reg __delay_valid_13;
  wire __delay_ready_13;
  reg signed [32-1:0] __delay_data_14;
  reg __delay_valid_14;
  wire __delay_ready_14;
  reg signed [32-1:0] __delay_data_15;
  reg __delay_valid_15;
  wire __delay_ready_15;
  reg signed [32-1:0] __delay_data_16;
  reg __delay_valid_16;
  wire __delay_ready_16;
  reg signed [32-1:0] __delay_data_17;
  reg __delay_valid_17;
  wire __delay_ready_17;
  reg signed [32-1:0] __delay_data_18;
  reg __delay_valid_18;
  wire __delay_ready_18;
  assign xready = (_lessthan_ready_7 || !_lessthan_valid_7) && (xvalid && xvalid) && ((_lessthan_ready_7 || !_lessthan_valid_7) && (xvalid && xvalid)) && ((_lessthan_ready_8 || !_lessthan_valid_8) && (xvalid && xvalid)) && ((_lessthan_ready_8 || !_lessthan_valid_8) && (xvalid && xvalid)) && ((_lessthan_ready_9 || !_lessthan_valid_9) && (xvalid && xvalid)) && ((_lessthan_ready_9 || !_lessthan_valid_9) && (xvalid && xvalid)) && ((_lessthan_ready_10 || !_lessthan_valid_10) && (xvalid && xvalid)) && ((_lessthan_ready_10 || !_lessthan_valid_10) && (xvalid && xvalid)) && ((__delay_ready_11 || !__delay_valid_11) && xvalid) && ((__delay_ready_12 || !__delay_valid_12) && xvalid) && ((__delay_ready_13 || !__delay_valid_13) && xvalid) && ((__delay_ready_14 || !__delay_valid_14) && xvalid) && ((__delay_ready_15 || !__delay_valid_15) && xvalid) && ((__delay_ready_16 || !__delay_valid_16) && xvalid) && ((__delay_ready_17 || !__delay_valid_17) && xvalid) && ((__delay_ready_18 || !__delay_valid_18) && xvalid);
  reg signed [32-1:0] _cond_data_19;
  reg _cond_valid_19;
  wire _cond_ready_19;
  assign _lessthan_ready_7 = (_cond_ready_19 || !_cond_valid_19) && (_lessthan_valid_7 && __delay_valid_11 && __delay_valid_12);
  assign __delay_ready_11 = (_cond_ready_19 || !_cond_valid_19) && (_lessthan_valid_7 && __delay_valid_11 && __delay_valid_12);
  assign __delay_ready_12 = (_cond_ready_19 || !_cond_valid_19) && (_lessthan_valid_7 && __delay_valid_11 && __delay_valid_12);
  reg signed [32-1:0] _cond_data_20;
  reg _cond_valid_20;
  wire _cond_ready_20;
  assign _lessthan_ready_8 = (_cond_ready_20 || !_cond_valid_20) && (_lessthan_valid_8 && __delay_valid_13 && __delay_valid_14);
  assign __delay_ready_13 = (_cond_ready_20 || !_cond_valid_20) && (_lessthan_valid_8 && __delay_valid_13 && __delay_valid_14);
  assign __delay_ready_14 = (_cond_ready_20 || !_cond_valid_20) && (_lessthan_valid_8 && __delay_valid_13 && __delay_valid_14);
  reg signed [32-1:0] _cond_data_21;
  reg _cond_valid_21;
  wire _cond_ready_21;
  assign _lessthan_ready_9 = (_cond_ready_21 || !_cond_valid_21) && (_lessthan_valid_9 && __delay_valid_15 && __delay_valid_16);
  assign __delay_ready_15 = (_cond_ready_21 || !_cond_valid_21) && (_lessthan_valid_9 && __delay_valid_15 && __delay_valid_16);
  assign __delay_ready_16 = (_cond_ready_21 || !_cond_valid_21) && (_lessthan_valid_9 && __delay_valid_15 && __delay_valid_16);
  reg signed [32-1:0] _cond_data_22;
  reg _cond_valid_22;
  wire _cond_ready_22;
  assign _lessthan_ready_10 = (_cond_ready_22 || !_cond_valid_22) && (_lessthan_valid_10 && __delay_valid_17 && __delay_valid_18);
  assign __delay_ready_17 = (_cond_ready_22 || !_cond_valid_22) && (_lessthan_valid_10 && __delay_valid_17 && __delay_valid_18);
  assign __delay_ready_18 = (_cond_ready_22 || !_cond_valid_22) && (_lessthan_valid_10 && __delay_valid_17 && __delay_valid_18);
  reg [1-1:0] _lessthan_data_23;
  reg _lessthan_valid_23;
  wire _lessthan_ready_23;
  reg [1-1:0] _lessthan_data_24;
  reg _lessthan_valid_24;
  wire _lessthan_ready_24;
  reg signed [32-1:0] __delay_data_25;
  reg __delay_valid_25;
  wire __delay_ready_25;
  assign _cond_ready_19 = (_lessthan_ready_23 || !_lessthan_valid_23) && (_cond_valid_19 && _cond_valid_20) && ((__delay_ready_25 || !__delay_valid_25) && _cond_valid_19);
  reg signed [32-1:0] __delay_data_26;
  reg __delay_valid_26;
  wire __delay_ready_26;
  assign _cond_ready_20 = (_lessthan_ready_23 || !_lessthan_valid_23) && (_cond_valid_19 && _cond_valid_20) && ((__delay_ready_26 || !__delay_valid_26) && _cond_valid_20);
  reg signed [32-1:0] __delay_data_27;
  reg __delay_valid_27;
  wire __delay_ready_27;
  assign _cond_ready_21 = (_lessthan_ready_24 || !_lessthan_valid_24) && (_cond_valid_21 && _cond_valid_22) && ((__delay_ready_27 || !__delay_valid_27) && _cond_valid_21);
  reg signed [32-1:0] __delay_data_28;
  reg __delay_valid_28;
  wire __delay_ready_28;
  assign _cond_ready_22 = (_lessthan_ready_24 || !_lessthan_valid_24) && (_cond_valid_21 && _cond_valid_22) && ((__delay_ready_28 || !__delay_valid_28) && _cond_valid_22);
  reg signed [32-1:0] _cond_data_29;
  reg _cond_valid_29;
  wire _cond_ready_29;
  assign _lessthan_ready_23 = (_cond_ready_29 || !_cond_valid_29) && (_lessthan_valid_23 && __delay_valid_25 && __delay_valid_26);
  assign __delay_ready_25 = (_cond_ready_29 || !_cond_valid_29) && (_lessthan_valid_23 && __delay_valid_25 && __delay_valid_26);
  assign __delay_ready_26 = (_cond_ready_29 || !_cond_valid_29) && (_lessthan_valid_23 && __delay_valid_25 && __delay_valid_26);
  reg signed [32-1:0] _cond_data_30;
  reg _cond_valid_30;
  wire _cond_ready_30;
  assign _lessthan_ready_24 = (_cond_ready_30 || !_cond_valid_30) && (_lessthan_valid_24 && __delay_valid_27 && __delay_valid_28);
  assign __delay_ready_27 = (_cond_ready_30 || !_cond_valid_30) && (_lessthan_valid_24 && __delay_valid_27 && __delay_valid_28);
  assign __delay_ready_28 = (_cond_ready_30 || !_cond_valid_30) && (_lessthan_valid_24 && __delay_valid_27 && __delay_valid_28);
  reg [1-1:0] _lessthan_data_31;
  reg _lessthan_valid_31;
  wire _lessthan_ready_31;
  reg signed [32-1:0] __delay_data_32;
  reg __delay_valid_32;
  wire __delay_ready_32;
  assign _cond_ready_29 = (_lessthan_ready_31 || !_lessthan_valid_31) && (_cond_valid_29 && _cond_valid_30) && ((__delay_ready_32 || !__delay_valid_32) && _cond_valid_29);
  reg signed [32-1:0] __delay_data_33;
  reg __delay_valid_33;
  wire __delay_ready_33;
  assign _cond_ready_30 = (_lessthan_ready_31 || !_lessthan_valid_31) && (_cond_valid_29 && _cond_valid_30) && ((__delay_ready_33 || !__delay_valid_33) && _cond_valid_30);
  reg signed [32-1:0] _cond_data_34;
  reg _cond_valid_34;
  wire _cond_ready_34;
  assign _lessthan_ready_31 = (_cond_ready_34 || !_cond_valid_34) && (_lessthan_valid_31 && __delay_valid_32 && __delay_valid_33);
  assign __delay_ready_32 = (_cond_ready_34 || !_cond_valid_34) && (_lessthan_valid_31 && __delay_valid_32 && __delay_valid_33);
  assign __delay_ready_33 = (_cond_ready_34 || !_cond_valid_34) && (_lessthan_valid_31 && __delay_valid_32 && __delay_valid_33);
  assign ydata = _cond_data_34;
  assign yvalid = _cond_valid_34;
  assign _cond_ready_34 = yready;

  always @(posedge CLK) begin
    if(RST) begin
      __prev_data_0 <= 0;
      __prev_data_1 <= 0;
      __prev_data_2 <= 0;
      __prev_data_3 <= 0;
      __prev_data_4 <= 0;
      __prev_data_5 <= 0;
      __prev_data_6 <= 0;
      _lessthan_data_7 <= 0;
      _lessthan_valid_7 <= 0;
      _lessthan_data_8 <= 0;
      _lessthan_valid_8 <= 0;
      _lessthan_data_9 <= 0;
      _lessthan_valid_9 <= 0;
      _lessthan_data_10 <= 0;
      _lessthan_valid_10 <= 0;
      __delay_data_11 <= 0;
      __delay_valid_11 <= 0;
      __delay_data_12 <= 0;
      __delay_valid_12 <= 0;
      __delay_data_13 <= 0;
      __delay_valid_13 <= 0;
      __delay_data_14 <= 0;
      __delay_valid_14 <= 0;
      __delay_data_15 <= 0;
      __delay_valid_15 <= 0;
      __delay_data_16 <= 0;
      __delay_valid_16 <= 0;
      __delay_data_17 <= 0;
      __delay_valid_17 <= 0;
      __delay_data_18 <= 0;
      __delay_valid_18 <= 0;
      _cond_data_19 <= 0;
      _cond_valid_19 <= 0;
      _cond_data_20 <= 0;
      _cond_valid_20 <= 0;
      _cond_data_21 <= 0;
      _cond_valid_21 <= 0;
      _cond_data_22 <= 0;
      _cond_valid_22 <= 0;
      _lessthan_data_23 <= 0;
      _lessthan_valid_23 <= 0;
      _lessthan_data_24 <= 0;
      _lessthan_valid_24 <= 0;
      __delay_data_25 <= 0;
      __delay_valid_25 <= 0;
      __delay_data_26 <= 0;
      __delay_valid_26 <= 0;
      __delay_data_27 <= 0;
      __delay_valid_27 <= 0;
      __delay_data_28 <= 0;
      __delay_valid_28 <= 0;
      _cond_data_29 <= 0;
      _cond_valid_29 <= 0;
      _cond_data_30 <= 0;
      _cond_valid_30 <= 0;
      _lessthan_data_31 <= 0;
      _lessthan_valid_31 <= 0;
      __delay_data_32 <= 0;
      __delay_valid_32 <= 0;
      __delay_data_33 <= 0;
      __delay_valid_33 <= 0;
      _cond_data_34 <= 0;
      _cond_valid_34 <= 0;
    end else begin
      if(xvalid && xready) begin
        __prev_data_0 <= xdata;
      end 
      if(xvalid && xready) begin
        __prev_data_1 <= __prev_data_0;
      end 
      if(xvalid && xready) begin
        __prev_data_2 <= __prev_data_1;
      end 
      if(xvalid && xready) begin
        __prev_data_3 <= __prev_data_2;
      end 
      if(xvalid && xready) begin
        __prev_data_4 <= __prev_data_3;
      end 
      if(xvalid && xready) begin
        __prev_data_5 <= __prev_data_4;
      end 
      if(xvalid && xready) begin
        __prev_data_6 <= __prev_data_5;
      end 
      if((_lessthan_ready_7 || !_lessthan_valid_7) && (xready && xready) && (xvalid && xvalid)) begin
        _lessthan_data_7 <= xdata < __prev_data_0;
      end 
      if(_lessthan_valid_7 && _lessthan_ready_7) begin
        _lessthan_valid_7 <= 0;
      end 
      if((_lessthan_ready_7 || !_lessthan_valid_7) && (xready && xready)) begin
        _lessthan_valid_7 <= xvalid && xvalid;
      end 
      if((_lessthan_ready_8 || !_lessthan_valid_8) && (xready && xready) && (xvalid && xvalid)) begin
        _lessthan_data_8 <= __prev_data_1 < __prev_data_2;
      end 
      if(_lessthan_valid_8 && _lessthan_ready_8) begin
        _lessthan_valid_8 <= 0;
      end 
      if((_lessthan_ready_8 || !_lessthan_valid_8) && (xready && xready)) begin
        _lessthan_valid_8 <= xvalid && xvalid;
      end 
      if((_lessthan_ready_9 || !_lessthan_valid_9) && (xready && xready) && (xvalid && xvalid)) begin
        _lessthan_data_9 <= __prev_data_3 < __prev_data_4;
      end 
      if(_lessthan_valid_9 && _lessthan_ready_9) begin
        _lessthan_valid_9 <= 0;
      end 
      if((_lessthan_ready_9 || !_lessthan_valid_9) && (xready && xready)) begin
        _lessthan_valid_9 <= xvalid && xvalid;
      end 
      if((_lessthan_ready_10 || !_lessthan_valid_10) && (xready && xready) && (xvalid && xvalid)) begin
        _lessthan_data_10 <= __prev_data_5 < __prev_data_6;
      end 
      if(_lessthan_valid_10 && _lessthan_ready_10) begin
        _lessthan_valid_10 <= 0;
      end 
      if((_lessthan_ready_10 || !_lessthan_valid_10) && (xready && xready)) begin
        _lessthan_valid_10 <= xvalid && xvalid;
      end 
      if((__delay_ready_11 || !__delay_valid_11) && xready && xvalid) begin
        __delay_data_11 <= xdata;
      end 
      if(__delay_valid_11 && __delay_ready_11) begin
        __delay_valid_11 <= 0;
      end 
      if((__delay_ready_11 || !__delay_valid_11) && xready) begin
        __delay_valid_11 <= xvalid;
      end 
      if((__delay_ready_12 || !__delay_valid_12) && xready && xvalid) begin
        __delay_data_12 <= __prev_data_0;
      end 
      if(__delay_valid_12 && __delay_ready_12) begin
        __delay_valid_12 <= 0;
      end 
      if((__delay_ready_12 || !__delay_valid_12) && xready) begin
        __delay_valid_12 <= xvalid;
      end 
      if((__delay_ready_13 || !__delay_valid_13) && xready && xvalid) begin
        __delay_data_13 <= __prev_data_1;
      end 
      if(__delay_valid_13 && __delay_ready_13) begin
        __delay_valid_13 <= 0;
      end 
      if((__delay_ready_13 || !__delay_valid_13) && xready) begin
        __delay_valid_13 <= xvalid;
      end 
      if((__delay_ready_14 || !__delay_valid_14) && xready && xvalid) begin
        __delay_data_14 <= __prev_data_2;
      end 
      if(__delay_valid_14 && __delay_ready_14) begin
        __delay_valid_14 <= 0;
      end 
      if((__delay_ready_14 || !__delay_valid_14) && xready) begin
        __delay_valid_14 <= xvalid;
      end 
      if((__delay_ready_15 || !__delay_valid_15) && xready && xvalid) begin
        __delay_data_15 <= __prev_data_3;
      end 
      if(__delay_valid_15 && __delay_ready_15) begin
        __delay_valid_15 <= 0;
      end 
      if((__delay_ready_15 || !__delay_valid_15) && xready) begin
        __delay_valid_15 <= xvalid;
      end 
      if((__delay_ready_16 || !__delay_valid_16) && xready && xvalid) begin
        __delay_data_16 <= __prev_data_4;
      end 
      if(__delay_valid_16 && __delay_ready_16) begin
        __delay_valid_16 <= 0;
      end 
      if((__delay_ready_16 || !__delay_valid_16) && xready) begin
        __delay_valid_16 <= xvalid;
      end 
      if((__delay_ready_17 || !__delay_valid_17) && xready && xvalid) begin
        __delay_data_17 <= __prev_data_5;
      end 
      if(__delay_valid_17 && __delay_ready_17) begin
        __delay_valid_17 <= 0;
      end 
      if((__delay_ready_17 || !__delay_valid_17) && xready) begin
        __delay_valid_17 <= xvalid;
      end 
      if((__delay_ready_18 || !__delay_valid_18) && xready && xvalid) begin
        __delay_data_18 <= __prev_data_6;
      end 
      if(__delay_valid_18 && __delay_ready_18) begin
        __delay_valid_18 <= 0;
      end 
      if((__delay_ready_18 || !__delay_valid_18) && xready) begin
        __delay_valid_18 <= xvalid;
      end 
      if((_cond_ready_19 || !_cond_valid_19) && (_lessthan_ready_7 && __delay_ready_11 && __delay_ready_12) && (_lessthan_valid_7 && __delay_valid_11 && __delay_valid_12)) begin
        _cond_data_19 <= (_lessthan_data_7)? __delay_data_11 : __delay_data_12;
      end 
      if(_cond_valid_19 && _cond_ready_19) begin
        _cond_valid_19 <= 0;
      end 
      if((_cond_ready_19 || !_cond_valid_19) && (_lessthan_ready_7 && __delay_ready_11 && __delay_ready_12)) begin
        _cond_valid_19 <= _lessthan_valid_7 && __delay_valid_11 && __delay_valid_12;
      end 
      if((_cond_ready_20 || !_cond_valid_20) && (_lessthan_ready_8 && __delay_ready_13 && __delay_ready_14) && (_lessthan_valid_8 && __delay_valid_13 && __delay_valid_14)) begin
        _cond_data_20 <= (_lessthan_data_8)? __delay_data_13 : __delay_data_14;
      end 
      if(_cond_valid_20 && _cond_ready_20) begin
        _cond_valid_20 <= 0;
      end 
      if((_cond_ready_20 || !_cond_valid_20) && (_lessthan_ready_8 && __delay_ready_13 && __delay_ready_14)) begin
        _cond_valid_20 <= _lessthan_valid_8 && __delay_valid_13 && __delay_valid_14;
      end 
      if((_cond_ready_21 || !_cond_valid_21) && (_lessthan_ready_9 && __delay_ready_15 && __delay_ready_16) && (_lessthan_valid_9 && __delay_valid_15 && __delay_valid_16)) begin
        _cond_data_21 <= (_lessthan_data_9)? __delay_data_15 : __delay_data_16;
      end 
      if(_cond_valid_21 && _cond_ready_21) begin
        _cond_valid_21 <= 0;
      end 
      if((_cond_ready_21 || !_cond_valid_21) && (_lessthan_ready_9 && __delay_ready_15 && __delay_ready_16)) begin
        _cond_valid_21 <= _lessthan_valid_9 && __delay_valid_15 && __delay_valid_16;
      end 
      if((_cond_ready_22 || !_cond_valid_22) && (_lessthan_ready_10 && __delay_ready_17 && __delay_ready_18) && (_lessthan_valid_10 && __delay_valid_17 && __delay_valid_18)) begin
        _cond_data_22 <= (_lessthan_data_10)? __delay_data_17 : __delay_data_18;
      end 
      if(_cond_valid_22 && _cond_ready_22) begin
        _cond_valid_22 <= 0;
      end 
      if((_cond_ready_22 || !_cond_valid_22) && (_lessthan_ready_10 && __delay_ready_17 && __delay_ready_18)) begin
        _cond_valid_22 <= _lessthan_valid_10 && __delay_valid_17 && __delay_valid_18;
      end 
      if((_lessthan_ready_23 || !_lessthan_valid_23) && (_cond_ready_19 && _cond_ready_20) && (_cond_valid_19 && _cond_valid_20)) begin
        _lessthan_data_23 <= _cond_data_19 < _cond_data_20;
      end 
      if(_lessthan_valid_23 && _lessthan_ready_23) begin
        _lessthan_valid_23 <= 0;
      end 
      if((_lessthan_ready_23 || !_lessthan_valid_23) && (_cond_ready_19 && _cond_ready_20)) begin
        _lessthan_valid_23 <= _cond_valid_19 && _cond_valid_20;
      end 
      if((_lessthan_ready_24 || !_lessthan_valid_24) && (_cond_ready_21 && _cond_ready_22) && (_cond_valid_21 && _cond_valid_22)) begin
        _lessthan_data_24 <= _cond_data_21 < _cond_data_22;
      end 
      if(_lessthan_valid_24 && _lessthan_ready_24) begin
        _lessthan_valid_24 <= 0;
      end 
      if((_lessthan_ready_24 || !_lessthan_valid_24) && (_cond_ready_21 && _cond_ready_22)) begin
        _lessthan_valid_24 <= _cond_valid_21 && _cond_valid_22;
      end 
      if((__delay_ready_25 || !__delay_valid_25) && _cond_ready_19 && _cond_valid_19) begin
        __delay_data_25 <= _cond_data_19;
      end 
      if(__delay_valid_25 && __delay_ready_25) begin
        __delay_valid_25 <= 0;
      end 
      if((__delay_ready_25 || !__delay_valid_25) && _cond_ready_19) begin
        __delay_valid_25 <= _cond_valid_19;
      end 
      if((__delay_ready_26 || !__delay_valid_26) && _cond_ready_20 && _cond_valid_20) begin
        __delay_data_26 <= _cond_data_20;
      end 
      if(__delay_valid_26 && __delay_ready_26) begin
        __delay_valid_26 <= 0;
      end 
      if((__delay_ready_26 || !__delay_valid_26) && _cond_ready_20) begin
        __delay_valid_26 <= _cond_valid_20;
      end 
      if((__delay_ready_27 || !__delay_valid_27) && _cond_ready_21 && _cond_valid_21) begin
        __delay_data_27 <= _cond_data_21;
      end 
      if(__delay_valid_27 && __delay_ready_27) begin
        __delay_valid_27 <= 0;
      end 
      if((__delay_ready_27 || !__delay_valid_27) && _cond_ready_21) begin
        __delay_valid_27 <= _cond_valid_21;
      end 
      if((__delay_ready_28 || !__delay_valid_28) && _cond_ready_22 && _cond_valid_22) begin
        __delay_data_28 <= _cond_data_22;
      end 
      if(__delay_valid_28 && __delay_ready_28) begin
        __delay_valid_28 <= 0;
      end 
      if((__delay_ready_28 || !__delay_valid_28) && _cond_ready_22) begin
        __delay_valid_28 <= _cond_valid_22;
      end 
      if((_cond_ready_29 || !_cond_valid_29) && (_lessthan_ready_23 && __delay_ready_25 && __delay_ready_26) && (_lessthan_valid_23 && __delay_valid_25 && __delay_valid_26)) begin
        _cond_data_29 <= (_lessthan_data_23)? __delay_data_25 : __delay_data_26;
      end 
      if(_cond_valid_29 && _cond_ready_29) begin
        _cond_valid_29 <= 0;
      end 
      if((_cond_ready_29 || !_cond_valid_29) && (_lessthan_ready_23 && __delay_ready_25 && __delay_ready_26)) begin
        _cond_valid_29 <= _lessthan_valid_23 && __delay_valid_25 && __delay_valid_26;
      end 
      if((_cond_ready_30 || !_cond_valid_30) && (_lessthan_ready_24 && __delay_ready_27 && __delay_ready_28) && (_lessthan_valid_24 && __delay_valid_27 && __delay_valid_28)) begin
        _cond_data_30 <= (_lessthan_data_24)? __delay_data_27 : __delay_data_28;
      end 
      if(_cond_valid_30 && _cond_ready_30) begin
        _cond_valid_30 <= 0;
      end 
      if((_cond_ready_30 || !_cond_valid_30) && (_lessthan_ready_24 && __delay_ready_27 && __delay_ready_28)) begin
        _cond_valid_30 <= _lessthan_valid_24 && __delay_valid_27 && __delay_valid_28;
      end 
      if((_lessthan_ready_31 || !_lessthan_valid_31) && (_cond_ready_29 && _cond_ready_30) && (_cond_valid_29 && _cond_valid_30)) begin
        _lessthan_data_31 <= _cond_data_29 < _cond_data_30;
      end 
      if(_lessthan_valid_31 && _lessthan_ready_31) begin
        _lessthan_valid_31 <= 0;
      end 
      if((_lessthan_ready_31 || !_lessthan_valid_31) && (_cond_ready_29 && _cond_ready_30)) begin
        _lessthan_valid_31 <= _cond_valid_29 && _cond_valid_30;
      end 
      if((__delay_ready_32 || !__delay_valid_32) && _cond_ready_29 && _cond_valid_29) begin
        __delay_data_32 <= _cond_data_29;
      end 
      if(__delay_valid_32 && __delay_ready_32) begin
        __delay_valid_32 <= 0;
      end 
      if((__delay_ready_32 || !__delay_valid_32) && _cond_ready_29) begin
        __delay_valid_32 <= _cond_valid_29;
      end 
      if((__delay_ready_33 || !__delay_valid_33) && _cond_ready_30 && _cond_valid_30) begin
        __delay_data_33 <= _cond_data_30;
      end 
      if(__delay_valid_33 && __delay_ready_33) begin
        __delay_valid_33 <= 0;
      end 
      if((__delay_ready_33 || !__delay_valid_33) && _cond_ready_30) begin
        __delay_valid_33 <= _cond_valid_30;
      end 
      if((_cond_ready_34 || !_cond_valid_34) && (_lessthan_ready_31 && __delay_ready_32 && __delay_ready_33) && (_lessthan_valid_31 && __delay_valid_32 && __delay_valid_33)) begin
        _cond_data_34 <= (_lessthan_data_31)? __delay_data_32 : __delay_data_33;
      end 
      if(_cond_valid_34 && _cond_ready_34) begin
        _cond_valid_34 <= 0;
      end 
      if((_cond_ready_34 || !_cond_valid_34) && (_lessthan_ready_31 && __delay_ready_32 && __delay_ready_33)) begin
        _cond_valid_34 <= _lessthan_valid_31 && __delay_valid_32 && __delay_valid_33;
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
