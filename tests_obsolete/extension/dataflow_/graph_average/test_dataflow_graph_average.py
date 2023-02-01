from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_graph_average

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  reg xvalid;
  wire xready;
  reg [32-1:0] ydata;
  reg yvalid;
  wire yready;
  wire [32-1:0] zdata;
  wire zvalid;
  reg zready;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .ydata(ydata),
    .yvalid(yvalid),
    .yready(yready),
    .zdata(zdata),
    .zvalid(zvalid),
    .zready(zready)
  );

  reg reset_done;

  initial begin
    $dumpfile("dataflow_graph_average.vcd");
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
    xdata = 2;
    xvalid = 0;
    ydata = 1;
    yvalid = 0;
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
            xdata <= xdata + 2;
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
            xdata <= xdata + 2;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 10) && xready) begin
            xvalid <= 0;
          end 
          if((_tmp_0 == 10) && xready) begin
            xfsm <= xfsm_24;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] _tmp_1;
  localparam yfsm_1 = 1;
  localparam yfsm_2 = 2;
  localparam yfsm_3 = 3;
  localparam yfsm_4 = 4;
  localparam yfsm_5 = 5;
  localparam yfsm_6 = 6;
  localparam yfsm_7 = 7;
  localparam yfsm_8 = 8;
  localparam yfsm_9 = 9;
  localparam yfsm_10 = 10;
  localparam yfsm_11 = 11;
  localparam yfsm_12 = 12;
  localparam yfsm_13 = 13;
  localparam yfsm_14 = 14;
  localparam yfsm_15 = 15;
  localparam yfsm_16 = 16;
  localparam yfsm_17 = 17;
  localparam yfsm_18 = 18;
  localparam yfsm_19 = 19;
  localparam yfsm_20 = 20;
  localparam yfsm_21 = 21;
  localparam yfsm_22 = 22;
  localparam yfsm_23 = 23;
  localparam yfsm_24 = 24;
  localparam yfsm_25 = 25;
  localparam yfsm_26 = 26;
  localparam yfsm_27 = 27;
  localparam yfsm_28 = 28;
  localparam yfsm_29 = 29;
  localparam yfsm_30 = 30;
  localparam yfsm_31 = 31;
  localparam yfsm_32 = 32;
  localparam yfsm_33 = 33;
  localparam yfsm_34 = 34;
  localparam yfsm_35 = 35;
  localparam yfsm_36 = 36;
  localparam yfsm_37 = 37;
  localparam yfsm_38 = 38;
  localparam yfsm_39 = 39;
  localparam yfsm_40 = 40;
  localparam yfsm_41 = 41;
  localparam yfsm_42 = 42;
  localparam yfsm_43 = 43;
  localparam yfsm_44 = 44;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
      _tmp_1 <= 0;
    end else begin
      case(yfsm)
        yfsm_init: begin
          yvalid <= 0;
          if(reset_done) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          yfsm <= yfsm_2;
        end
        yfsm_2: begin
          yfsm <= yfsm_3;
        end
        yfsm_3: begin
          yfsm <= yfsm_4;
        end
        yfsm_4: begin
          yfsm <= yfsm_5;
        end
        yfsm_5: begin
          yfsm <= yfsm_6;
        end
        yfsm_6: begin
          yfsm <= yfsm_7;
        end
        yfsm_7: begin
          yfsm <= yfsm_8;
        end
        yfsm_8: begin
          yfsm <= yfsm_9;
        end
        yfsm_9: begin
          yfsm <= yfsm_10;
        end
        yfsm_10: begin
          yfsm <= yfsm_11;
        end
        yfsm_11: begin
          yfsm <= yfsm_12;
        end
        yfsm_12: begin
          yfsm <= yfsm_13;
        end
        yfsm_13: begin
          yfsm <= yfsm_14;
        end
        yfsm_14: begin
          yfsm <= yfsm_15;
        end
        yfsm_15: begin
          yfsm <= yfsm_16;
        end
        yfsm_16: begin
          yfsm <= yfsm_17;
        end
        yfsm_17: begin
          yfsm <= yfsm_18;
        end
        yfsm_18: begin
          yfsm <= yfsm_19;
        end
        yfsm_19: begin
          yfsm <= yfsm_20;
        end
        yfsm_20: begin
          yfsm <= yfsm_21;
        end
        yfsm_21: begin
          yvalid <= 1;
          yfsm <= yfsm_22;
        end
        yfsm_22: begin
          if(yready) begin
            ydata <= ydata + 1;
          end 
          if(yready) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((_tmp_1 == 5) && yready) begin
            yvalid <= 0;
          end 
          if((_tmp_1 == 5) && yready) begin
            yfsm <= yfsm_23;
          end 
        end
        yfsm_23: begin
          yfsm <= yfsm_24;
        end
        yfsm_24: begin
          yfsm <= yfsm_25;
        end
        yfsm_25: begin
          yfsm <= yfsm_26;
        end
        yfsm_26: begin
          yfsm <= yfsm_27;
        end
        yfsm_27: begin
          yfsm <= yfsm_28;
        end
        yfsm_28: begin
          yfsm <= yfsm_29;
        end
        yfsm_29: begin
          yfsm <= yfsm_30;
        end
        yfsm_30: begin
          yfsm <= yfsm_31;
        end
        yfsm_31: begin
          yfsm <= yfsm_32;
        end
        yfsm_32: begin
          yfsm <= yfsm_33;
        end
        yfsm_33: begin
          yfsm <= yfsm_34;
        end
        yfsm_34: begin
          yfsm <= yfsm_35;
        end
        yfsm_35: begin
          yfsm <= yfsm_36;
        end
        yfsm_36: begin
          yfsm <= yfsm_37;
        end
        yfsm_37: begin
          yfsm <= yfsm_38;
        end
        yfsm_38: begin
          yfsm <= yfsm_39;
        end
        yfsm_39: begin
          yfsm <= yfsm_40;
        end
        yfsm_40: begin
          yfsm <= yfsm_41;
        end
        yfsm_41: begin
          yfsm <= yfsm_42;
        end
        yfsm_42: begin
          yfsm <= yfsm_43;
        end
        yfsm_43: begin
          yvalid <= 1;
          if(yready) begin
            ydata <= ydata + 1;
          end 
          if(yready) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((_tmp_1 == 10) && yready) begin
            yvalid <= 0;
          end 
          if((_tmp_1 == 10) && yready) begin
            yfsm <= yfsm_44;
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
  localparam zfsm_9 = 9;
  localparam zfsm_10 = 10;
  localparam zfsm_11 = 11;
  localparam zfsm_12 = 12;
  localparam zfsm_13 = 13;
  localparam zfsm_14 = 14;
  localparam zfsm_15 = 15;
  localparam zfsm_16 = 16;
  localparam zfsm_17 = 17;
  localparam zfsm_18 = 18;
  localparam zfsm_19 = 19;
  localparam zfsm_20 = 20;
  localparam zfsm_21 = 21;
  localparam zfsm_22 = 22;
  localparam zfsm_23 = 23;
  localparam zfsm_24 = 24;
  localparam zfsm_25 = 25;
  localparam zfsm_26 = 26;
  localparam zfsm_27 = 27;
  localparam zfsm_28 = 28;
  localparam zfsm_29 = 29;
  localparam zfsm_30 = 30;
  localparam zfsm_31 = 31;
  localparam zfsm_32 = 32;
  localparam zfsm_33 = 33;
  localparam zfsm_34 = 34;
  localparam zfsm_35 = 35;
  localparam zfsm_36 = 36;
  localparam zfsm_37 = 37;
  localparam zfsm_38 = 38;
  localparam zfsm_39 = 39;
  localparam zfsm_40 = 40;
  localparam zfsm_41 = 41;
  localparam zfsm_42 = 42;
  localparam zfsm_43 = 43;
  localparam zfsm_44 = 44;
  localparam zfsm_45 = 45;
  localparam zfsm_46 = 46;
  localparam zfsm_47 = 47;
  localparam zfsm_48 = 48;
  localparam zfsm_49 = 49;
  localparam zfsm_50 = 50;
  localparam zfsm_51 = 51;
  localparam zfsm_52 = 52;
  localparam zfsm_53 = 53;

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
          if(zvalid) begin
            zready <= 1;
          end 
          if(zvalid) begin
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
          zready <= 0;
          zfsm <= zfsm_9;
        end
        zfsm_9: begin
          zready <= 0;
          zfsm <= zfsm_10;
        end
        zfsm_10: begin
          zready <= 0;
          zfsm <= zfsm_11;
        end
        zfsm_11: begin
          zready <= 0;
          zfsm <= zfsm_12;
        end
        zfsm_12: begin
          zready <= 0;
          zfsm <= zfsm_13;
        end
        zfsm_13: begin
          zready <= 0;
          zfsm <= zfsm_14;
        end
        zfsm_14: begin
          zready <= 0;
          zfsm <= zfsm_15;
        end
        zfsm_15: begin
          zready <= 0;
          zfsm <= zfsm_16;
        end
        zfsm_16: begin
          zready <= 0;
          zfsm <= zfsm_17;
        end
        zfsm_17: begin
          zready <= 0;
          zfsm <= zfsm_18;
        end
        zfsm_18: begin
          zready <= 0;
          zfsm <= zfsm_19;
        end
        zfsm_19: begin
          zready <= 0;
          zfsm <= zfsm_20;
        end
        zfsm_20: begin
          zready <= 0;
          zfsm <= zfsm_21;
        end
        zfsm_21: begin
          zready <= 0;
          zfsm <= zfsm_22;
        end
        zfsm_22: begin
          zready <= 0;
          zfsm <= zfsm_23;
        end
        zfsm_23: begin
          zready <= 0;
          zfsm <= zfsm_24;
        end
        zfsm_24: begin
          zready <= 0;
          zfsm <= zfsm_25;
        end
        zfsm_25: begin
          zready <= 0;
          zfsm <= zfsm_26;
        end
        zfsm_26: begin
          zready <= 0;
          zfsm <= zfsm_27;
        end
        zfsm_27: begin
          zready <= 0;
          zfsm <= zfsm_28;
        end
        zfsm_28: begin
          zready <= 0;
          zfsm <= zfsm_29;
        end
        zfsm_29: begin
          zready <= 0;
          zfsm <= zfsm_30;
        end
        zfsm_30: begin
          zready <= 0;
          zfsm <= zfsm_31;
        end
        zfsm_31: begin
          zready <= 0;
          zfsm <= zfsm_32;
        end
        zfsm_32: begin
          zready <= 0;
          zfsm <= zfsm_33;
        end
        zfsm_33: begin
          zready <= 0;
          zfsm <= zfsm_34;
        end
        zfsm_34: begin
          zready <= 0;
          zfsm <= zfsm_35;
        end
        zfsm_35: begin
          zready <= 0;
          zfsm <= zfsm_36;
        end
        zfsm_36: begin
          zready <= 0;
          zfsm <= zfsm_37;
        end
        zfsm_37: begin
          zready <= 0;
          zfsm <= zfsm_38;
        end
        zfsm_38: begin
          zready <= 0;
          zfsm <= zfsm_39;
        end
        zfsm_39: begin
          zready <= 0;
          zfsm <= zfsm_40;
        end
        zfsm_40: begin
          zready <= 0;
          zfsm <= zfsm_41;
        end
        zfsm_41: begin
          zready <= 0;
          zfsm <= zfsm_42;
        end
        zfsm_42: begin
          zready <= 0;
          zfsm <= zfsm_43;
        end
        zfsm_43: begin
          zready <= 0;
          zfsm <= zfsm_44;
        end
        zfsm_44: begin
          zready <= 0;
          zfsm <= zfsm_45;
        end
        zfsm_45: begin
          zready <= 0;
          zfsm <= zfsm_46;
        end
        zfsm_46: begin
          zready <= 0;
          zfsm <= zfsm_47;
        end
        zfsm_47: begin
          zready <= 0;
          zfsm <= zfsm_48;
        end
        zfsm_48: begin
          zready <= 0;
          zfsm <= zfsm_49;
        end
        zfsm_49: begin
          zready <= 0;
          zfsm <= zfsm_50;
        end
        zfsm_50: begin
          zready <= 0;
          zfsm <= zfsm_51;
        end
        zfsm_51: begin
          zready <= 0;
          zfsm <= zfsm_52;
        end
        zfsm_52: begin
          zready <= 0;
          zfsm <= zfsm_53;
        end
        zfsm_53: begin
          zfsm <= zfsm_2;
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
      if(zvalid && zready) begin
        $display("zdata=%d", zdata);
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
  input [32-1:0] ydata,
  input yvalid,
  output yready,
  output [32-1:0] zdata,
  output zvalid,
  input zready
);

  reg [32-1:0] _dataflow_plus_data_2;
  reg _dataflow_plus_valid_2;
  wire _dataflow_plus_ready_2;
  assign xready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid);
  assign yready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid);
  reg [32-1:0] _dataflow__prev_data_3;
  reg [32-1:0] _dataflow_plus_data_4;
  reg _dataflow_plus_valid_4;
  wire _dataflow_plus_ready_4;
  reg [32-1:0] _dataflow__prev_data_5;
  reg [32-1:0] _dataflow__delay_data_9;
  reg _dataflow__delay_valid_9;
  wire _dataflow__delay_ready_9;
  assign _dataflow_plus_ready_2 = (_dataflow_plus_ready_4 || !_dataflow_plus_valid_4) && (_dataflow_plus_valid_2 && _dataflow_plus_valid_2) && ((_dataflow_plus_ready_4 || !_dataflow_plus_valid_4) && (_dataflow_plus_valid_2 && _dataflow_plus_valid_2)) && ((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_plus_valid_2);
  reg [32-1:0] _dataflow_plus_data_6;
  reg _dataflow_plus_valid_6;
  wire _dataflow_plus_ready_6;
  assign _dataflow_plus_ready_4 = (_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_valid_4 && _dataflow__delay_valid_9);
  assign _dataflow__delay_ready_9 = (_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_valid_4 && _dataflow__delay_valid_9);
  wire [32-1:0] _dataflow_divide_data_7;
  wire _dataflow_divide_valid_7;
  wire _dataflow_divide_ready_7;
  reg [32-1:0] _dataflow_divide_div_ldata_7;
  reg signed [32-1:0] _dataflow_divide_div_rdata_7;
  reg [32-1:0] _dataflow_divide_div_abs_ldata_7;
  reg [32-1:0] _dataflow_divide_div_abs_rdata_7;
  wire _dataflow_divide_div_osign_7;
  wire [32-1:0] _dataflow_divide_div_abs_odata_7;
  reg [32-1:0] _dataflow_divide_div_odata_7;
  assign _dataflow_divide_data_7 = _dataflow_divide_div_odata_7;
  wire _dataflow_divide_div_ovalid_7;
  reg _dataflow_divide_div_valid_reg_tmp_0_7;
  reg _dataflow_divide_div_valid_reg_tmp_1_7;
  reg _dataflow_divide_div_valid_reg_tmp_2_7;
  assign _dataflow_divide_valid_7 = _dataflow_divide_div_valid_reg_tmp_2_7;
  reg _dataflow_divide_div_sign_tmp_0_7;
  reg _dataflow_divide_div_sign_tmp_1_7;
  reg _dataflow_divide_div_sign_tmp_2_7;
  reg _dataflow_divide_div_sign_tmp_3_7;
  reg _dataflow_divide_div_sign_tmp_4_7;
  reg _dataflow_divide_div_sign_tmp_5_7;
  reg _dataflow_divide_div_sign_tmp_6_7;
  reg _dataflow_divide_div_sign_tmp_7_7;
  reg _dataflow_divide_div_sign_tmp_8_7;
  reg _dataflow_divide_div_sign_tmp_9_7;
  reg _dataflow_divide_div_sign_tmp_10_7;
  reg _dataflow_divide_div_sign_tmp_11_7;
  reg _dataflow_divide_div_sign_tmp_12_7;
  reg _dataflow_divide_div_sign_tmp_13_7;
  reg _dataflow_divide_div_sign_tmp_14_7;
  reg _dataflow_divide_div_sign_tmp_15_7;
  reg _dataflow_divide_div_sign_tmp_16_7;
  reg _dataflow_divide_div_sign_tmp_17_7;
  reg _dataflow_divide_div_sign_tmp_18_7;
  reg _dataflow_divide_div_sign_tmp_19_7;
  reg _dataflow_divide_div_sign_tmp_20_7;
  reg _dataflow_divide_div_sign_tmp_21_7;
  reg _dataflow_divide_div_sign_tmp_22_7;
  reg _dataflow_divide_div_sign_tmp_23_7;
  reg _dataflow_divide_div_sign_tmp_24_7;
  reg _dataflow_divide_div_sign_tmp_25_7;
  reg _dataflow_divide_div_sign_tmp_26_7;
  reg _dataflow_divide_div_sign_tmp_27_7;
  reg _dataflow_divide_div_sign_tmp_28_7;
  reg _dataflow_divide_div_sign_tmp_29_7;
  reg _dataflow_divide_div_sign_tmp_30_7;
  reg _dataflow_divide_div_sign_tmp_31_7;
  reg _dataflow_divide_div_sign_tmp_32_7;
  reg _dataflow_divide_div_sign_tmp_33_7;
  reg _dataflow_divide_div_sign_tmp_34_7;
  assign _dataflow_divide_div_osign_7 = _dataflow_divide_div_sign_tmp_34_7;
  wire _dataflow_divide_div_enable_7;
  wire _dataflow_divide_div_update_7;
  assign _dataflow_divide_div_enable_7 = (_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) && _dataflow_plus_ready_6 && _dataflow_plus_valid_6;
  assign _dataflow_divide_div_update_7 = _dataflow_divide_ready_7 || !_dataflow_divide_valid_7;

  Divider
  #(
    .W_D(32)
  )
  _dataflow_divide_div_7
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_divide_div_update_7),
    .enable(_dataflow_divide_div_enable_7),
    .valid(_dataflow_divide_div_ovalid_7),
    .in_a(_dataflow_divide_div_abs_ldata_7),
    .in_b(_dataflow_divide_div_abs_rdata_7),
    .rslt(_dataflow_divide_div_abs_odata_7)
  );

  assign _dataflow_plus_ready_6 = (_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) && _dataflow_plus_valid_6;
  assign zdata = _dataflow_divide_data_7;
  assign zvalid = _dataflow_divide_valid_7;
  assign _dataflow_divide_ready_7 = zready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_plus_data_2 <= 0;
      _dataflow_plus_valid_2 <= 0;
      _dataflow__prev_data_3 <= 0;
      _dataflow_plus_data_4 <= 0;
      _dataflow_plus_valid_4 <= 0;
      _dataflow__prev_data_5 <= 0;
      _dataflow__delay_data_9 <= 0;
      _dataflow__delay_valid_9 <= 0;
      _dataflow_plus_data_6 <= 0;
      _dataflow_plus_valid_6 <= 0;
      _dataflow_divide_div_ldata_7 <= 0;
      _dataflow_divide_div_rdata_7 <= 0;
      _dataflow_divide_div_abs_ldata_7 <= 0;
      _dataflow_divide_div_abs_rdata_7 <= 0;
      _dataflow_divide_div_odata_7 <= 0;
      _dataflow_divide_div_valid_reg_tmp_0_7 <= 0;
      _dataflow_divide_div_valid_reg_tmp_1_7 <= 0;
      _dataflow_divide_div_valid_reg_tmp_2_7 <= 0;
      _dataflow_divide_div_sign_tmp_0_7 <= 0;
      _dataflow_divide_div_sign_tmp_1_7 <= 0;
      _dataflow_divide_div_sign_tmp_2_7 <= 0;
      _dataflow_divide_div_sign_tmp_3_7 <= 0;
      _dataflow_divide_div_sign_tmp_4_7 <= 0;
      _dataflow_divide_div_sign_tmp_5_7 <= 0;
      _dataflow_divide_div_sign_tmp_6_7 <= 0;
      _dataflow_divide_div_sign_tmp_7_7 <= 0;
      _dataflow_divide_div_sign_tmp_8_7 <= 0;
      _dataflow_divide_div_sign_tmp_9_7 <= 0;
      _dataflow_divide_div_sign_tmp_10_7 <= 0;
      _dataflow_divide_div_sign_tmp_11_7 <= 0;
      _dataflow_divide_div_sign_tmp_12_7 <= 0;
      _dataflow_divide_div_sign_tmp_13_7 <= 0;
      _dataflow_divide_div_sign_tmp_14_7 <= 0;
      _dataflow_divide_div_sign_tmp_15_7 <= 0;
      _dataflow_divide_div_sign_tmp_16_7 <= 0;
      _dataflow_divide_div_sign_tmp_17_7 <= 0;
      _dataflow_divide_div_sign_tmp_18_7 <= 0;
      _dataflow_divide_div_sign_tmp_19_7 <= 0;
      _dataflow_divide_div_sign_tmp_20_7 <= 0;
      _dataflow_divide_div_sign_tmp_21_7 <= 0;
      _dataflow_divide_div_sign_tmp_22_7 <= 0;
      _dataflow_divide_div_sign_tmp_23_7 <= 0;
      _dataflow_divide_div_sign_tmp_24_7 <= 0;
      _dataflow_divide_div_sign_tmp_25_7 <= 0;
      _dataflow_divide_div_sign_tmp_26_7 <= 0;
      _dataflow_divide_div_sign_tmp_27_7 <= 0;
      _dataflow_divide_div_sign_tmp_28_7 <= 0;
      _dataflow_divide_div_sign_tmp_29_7 <= 0;
      _dataflow_divide_div_sign_tmp_30_7 <= 0;
      _dataflow_divide_div_sign_tmp_31_7 <= 0;
      _dataflow_divide_div_sign_tmp_32_7 <= 0;
      _dataflow_divide_div_sign_tmp_33_7 <= 0;
      _dataflow_divide_div_sign_tmp_34_7 <= 0;
    end else begin
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready) && (xvalid && yvalid)) begin
        _dataflow_plus_data_2 <= xdata + ydata;
      end 
      if(_dataflow_plus_valid_2 && _dataflow_plus_ready_2) begin
        _dataflow_plus_valid_2 <= 0;
      end 
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready)) begin
        _dataflow_plus_valid_2 <= xvalid && yvalid;
      end 
      if(_dataflow_plus_valid_2 && _dataflow_plus_ready_2) begin
        _dataflow__prev_data_3 <= _dataflow_plus_data_2;
      end 
      if((_dataflow_plus_ready_4 || !_dataflow_plus_valid_4) && (_dataflow_plus_ready_2 && _dataflow_plus_ready_2) && (_dataflow_plus_valid_2 && _dataflow_plus_valid_2)) begin
        _dataflow_plus_data_4 <= _dataflow_plus_data_2 + _dataflow__prev_data_3;
      end 
      if(_dataflow_plus_valid_4 && _dataflow_plus_ready_4) begin
        _dataflow_plus_valid_4 <= 0;
      end 
      if((_dataflow_plus_ready_4 || !_dataflow_plus_valid_4) && (_dataflow_plus_ready_2 && _dataflow_plus_ready_2)) begin
        _dataflow_plus_valid_4 <= _dataflow_plus_valid_2 && _dataflow_plus_valid_2;
      end 
      if(_dataflow_plus_valid_2 && _dataflow_plus_ready_2) begin
        _dataflow__prev_data_5 <= _dataflow__prev_data_3;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_plus_ready_2 && _dataflow_plus_valid_2) begin
        _dataflow__delay_data_9 <= _dataflow__prev_data_5;
      end 
      if(_dataflow__delay_valid_9 && _dataflow__delay_ready_9) begin
        _dataflow__delay_valid_9 <= 0;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_plus_ready_2) begin
        _dataflow__delay_valid_9 <= _dataflow_plus_valid_2;
      end 
      if((_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_ready_4 && _dataflow__delay_ready_9) && (_dataflow_plus_valid_4 && _dataflow__delay_valid_9)) begin
        _dataflow_plus_data_6 <= _dataflow_plus_data_4 + _dataflow__delay_data_9;
      end 
      if(_dataflow_plus_valid_6 && _dataflow_plus_ready_6) begin
        _dataflow_plus_valid_6 <= 0;
      end 
      if((_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_ready_4 && _dataflow__delay_ready_9)) begin
        _dataflow_plus_valid_6 <= _dataflow_plus_valid_4 && _dataflow__delay_valid_9;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_ldata_7 <= _dataflow_plus_data_6;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_rdata_7 <= 3'sd3;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_abs_ldata_7 <= _dataflow_divide_div_ldata_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_abs_rdata_7 <= (_dataflow_divide_div_rdata_7[31] == 0)? _dataflow_divide_div_rdata_7 : ~_dataflow_divide_div_rdata_7 + 1;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_odata_7 <= _dataflow_divide_div_abs_odata_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_valid_reg_tmp_0_7 <= _dataflow_divide_div_ovalid_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_valid_reg_tmp_1_7 <= _dataflow_divide_div_valid_reg_tmp_0_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_valid_reg_tmp_2_7 <= _dataflow_divide_div_valid_reg_tmp_1_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_0_7 <= !((_dataflow_divide_div_ldata_7[31] == 0) && (_dataflow_divide_div_rdata_7[31] == 0) || (_dataflow_divide_div_ldata_7[31] == 1) && (_dataflow_divide_div_rdata_7[31] == 1));
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_1_7 <= _dataflow_divide_div_sign_tmp_0_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_2_7 <= _dataflow_divide_div_sign_tmp_1_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_3_7 <= _dataflow_divide_div_sign_tmp_2_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_4_7 <= _dataflow_divide_div_sign_tmp_3_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_5_7 <= _dataflow_divide_div_sign_tmp_4_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_6_7 <= _dataflow_divide_div_sign_tmp_5_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_7_7 <= _dataflow_divide_div_sign_tmp_6_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_8_7 <= _dataflow_divide_div_sign_tmp_7_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_9_7 <= _dataflow_divide_div_sign_tmp_8_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_10_7 <= _dataflow_divide_div_sign_tmp_9_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_11_7 <= _dataflow_divide_div_sign_tmp_10_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_12_7 <= _dataflow_divide_div_sign_tmp_11_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_13_7 <= _dataflow_divide_div_sign_tmp_12_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_14_7 <= _dataflow_divide_div_sign_tmp_13_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_15_7 <= _dataflow_divide_div_sign_tmp_14_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_16_7 <= _dataflow_divide_div_sign_tmp_15_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_17_7 <= _dataflow_divide_div_sign_tmp_16_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_18_7 <= _dataflow_divide_div_sign_tmp_17_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_19_7 <= _dataflow_divide_div_sign_tmp_18_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_20_7 <= _dataflow_divide_div_sign_tmp_19_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_21_7 <= _dataflow_divide_div_sign_tmp_20_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_22_7 <= _dataflow_divide_div_sign_tmp_21_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_23_7 <= _dataflow_divide_div_sign_tmp_22_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_24_7 <= _dataflow_divide_div_sign_tmp_23_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_25_7 <= _dataflow_divide_div_sign_tmp_24_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_26_7 <= _dataflow_divide_div_sign_tmp_25_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_27_7 <= _dataflow_divide_div_sign_tmp_26_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_28_7 <= _dataflow_divide_div_sign_tmp_27_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_29_7 <= _dataflow_divide_div_sign_tmp_28_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_30_7 <= _dataflow_divide_div_sign_tmp_29_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_31_7 <= _dataflow_divide_div_sign_tmp_30_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_32_7 <= _dataflow_divide_div_sign_tmp_31_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_33_7 <= _dataflow_divide_div_sign_tmp_32_7;
      end 
      if(_dataflow_divide_ready_7 || !_dataflow_divide_valid_7) begin
        _dataflow_divide_div_sign_tmp_34_7 <= _dataflow_divide_div_sign_tmp_33_7;
      end 
    end
  end


endmodule



module Divider #
(
  parameter W_D = 32
)
(
  input CLK,
  input RST,
  input [W_D-1:0] in_a,
  input [W_D-1:0] in_b,
  input update,
  input enable,
  output reg [W_D-1:0] rslt,
  output reg [W_D-1:0] mod,
  output reg valid
);

  localparam DEPTH = W_D + 1;

  function [0:0] getsign;
    input [W_D-1:0] in;
    begin
      getsign = in[W_D - 1];
    end
  endfunction


  function [0:0] is_positive;
    input [W_D-1:0] in;
    begin
      is_positive = getsign(in) == 0;
    end
  endfunction


  function [W_D-1:0] complement2;
    input [W_D-1:0] in;
    begin
      complement2 = ~in + { { W_D - 1{ 1'b0 } }, 1'b1 };
    end
  endfunction


  function [W_D*2-1:0] complement2_2x;
    input [W_D*2-1:0] in;
    begin
      complement2_2x = ~in + { { W_D * 2 - 1{ 1'b0 } }, 1'b1 };
    end
  endfunction


  function [W_D-1:0] absolute;
    input [W_D-1:0] in;
    begin
      if(getsign(in)) begin
        absolute = complement2(in);
      end else begin
        absolute = in;
      end
    end
  endfunction

  wire [W_D-1:0] abs_in_a;
  wire [W_D-1:0] abs_in_b;
  assign abs_in_a = absolute(in_a);
  assign abs_in_b = absolute(in_b);
  genvar d;

  generate for(d=0; d<DEPTH; d=d+1) begin : s_depth
    reg stage_valid;
    reg in_a_positive;
    reg in_b_positive;
    reg [W_D*2-1:0] dividend;
    reg [W_D*2-1:0] divisor;
    reg [W_D*2-1:0] stage_rslt;
    wire [W_D*2-1:0] sub_value;
    wire is_large;
    assign sub_value = dividend - divisor;
    assign is_large = !sub_value[W_D * 2 - 1];
    if(d == 0) begin

      always @(posedge CLK) begin
        if(RST) begin
          stage_valid <= 0;
          in_a_positive <= 0;
          in_b_positive <= 0;
        end else begin
          if(update) begin
            stage_valid <= enable;
            in_a_positive <= is_positive(in_a);
            in_b_positive <= is_positive(in_b);
          end 
        end
      end

    end else begin

      always @(posedge CLK) begin
        if(RST) begin
          stage_valid <= 0;
          in_a_positive <= 0;
          in_b_positive <= 0;
        end else begin
          if(update) begin
            stage_valid <= s_depth[(d - 1)].stage_valid;
            in_a_positive <= s_depth[(d - 1)].in_a_positive;
            in_b_positive <= s_depth[(d - 1)].in_b_positive;
          end 
        end
      end

    end
    if(d == 0) begin

      always @(posedge CLK) begin
        if(update) begin
          dividend <= abs_in_a;
          divisor <= abs_in_b << W_D - 1;
          stage_rslt <= 0;
        end 
      end

    end else begin

      always @(posedge CLK) begin
        if(update) begin
          dividend <= (s_depth[(d - 1)].is_large)? s_depth[(d - 1)].sub_value : s_depth[(d - 1)].dividend;
          divisor <= s_depth[(d - 1)].divisor >> 1;
          stage_rslt <= { s_depth[(d - 1)].stage_rslt, s_depth[(d - 1)].is_large };
        end 
      end

    end
  end
  endgenerate


  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
    end else begin
      if(update) begin
        valid <= s_depth[(DEPTH - 1)].stage_valid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(update) begin
      rslt <= (s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].stage_rslt : 
              (!s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].stage_rslt) : 
              (s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].stage_rslt) : 
              (!s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].stage_rslt : 'hx;
      mod <= (s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].dividend[W_D-1:0] : 
             (!s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].dividend[W_D-1:0]) : 
             (s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].dividend[W_D-1:0] : 
             (!s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].dividend[W_D-1:0]) : 'hx;
    end 
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_graph_average.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
