from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_lut

expected_verilog = """
module test;

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
    ydata = 0;
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
            ydata <= ydata + 2;
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
            ydata <= ydata + 2;
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

  wire [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  wire [8-1:0] _tmp_address_0;
  assign _tmp_address_0 = xdata;

  _LUT_0
  LUT_0
  (
    .CLK(CLK),
    .addr(_tmp_address_0),
    .enable((_tmp_ready_0 || !_tmp_valid_0) && xready && xvalid),
    .val(_tmp_data_0)
  );

  assign xready = (_tmp_ready_0 || !_tmp_valid_0) && xvalid;
  assign _tmp_ready_0 = (_tmp_ready_2 || !_tmp_valid_2) && (_tmp_valid_0 && _tmp_valid_1);
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign yready = (_tmp_ready_1 || !_tmp_valid_1) && yvalid;
  assign _tmp_ready_1 = (_tmp_ready_2 || !_tmp_valid_2) && (_tmp_valid_0 && _tmp_valid_1);
  reg [32-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign zdata = _tmp_data_2;
  assign zvalid = _tmp_valid_2;
  assign _tmp_ready_2 = zready;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
    end else begin
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && xready) begin
        _tmp_valid_0 <= xvalid;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && yready && yvalid) begin
        _tmp_data_1 <= ydata;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && yready) begin
        _tmp_valid_1 <= yvalid;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && (_tmp_ready_0 && _tmp_ready_1) && (_tmp_valid_0 && _tmp_valid_1)) begin
        _tmp_data_2 <= _tmp_data_0 + _tmp_data_1;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && (_tmp_ready_0 && _tmp_ready_1)) begin
        _tmp_valid_2 <= _tmp_valid_0 && _tmp_valid_1;
      end 
    end
  end


endmodule



module _LUT_0
(
  input CLK,
  input [8-1:0] addr,
  input enable,
  output reg [32-1:0] val
);


  always @(posedge CLK) begin
    if(enable) begin
      case(addr)
        0: begin
          val <= 0;
        end
        1: begin
          val <= 1;
        end
        2: begin
          val <= 4;
        end
        3: begin
          val <= 9;
        end
        4: begin
          val <= 16;
        end
        5: begin
          val <= 25;
        end
        6: begin
          val <= 36;
        end
        7: begin
          val <= 49;
        end
        8: begin
          val <= 64;
        end
        9: begin
          val <= 81;
        end
        10: begin
          val <= 100;
        end
        11: begin
          val <= 121;
        end
        12: begin
          val <= 144;
        end
        13: begin
          val <= 169;
        end
        14: begin
          val <= 196;
        end
        15: begin
          val <= 225;
        end
        16: begin
          val <= 256;
        end
        17: begin
          val <= 289;
        end
        18: begin
          val <= 324;
        end
        19: begin
          val <= 361;
        end
        20: begin
          val <= 400;
        end
        21: begin
          val <= 441;
        end
        22: begin
          val <= 484;
        end
        23: begin
          val <= 529;
        end
        24: begin
          val <= 576;
        end
        25: begin
          val <= 625;
        end
        26: begin
          val <= 676;
        end
        27: begin
          val <= 729;
        end
        28: begin
          val <= 784;
        end
        29: begin
          val <= 841;
        end
        30: begin
          val <= 900;
        end
        31: begin
          val <= 961;
        end
        32: begin
          val <= 1024;
        end
        33: begin
          val <= 1089;
        end
        34: begin
          val <= 1156;
        end
        35: begin
          val <= 1225;
        end
        36: begin
          val <= 1296;
        end
        37: begin
          val <= 1369;
        end
        38: begin
          val <= 1444;
        end
        39: begin
          val <= 1521;
        end
        40: begin
          val <= 1600;
        end
        41: begin
          val <= 1681;
        end
        42: begin
          val <= 1764;
        end
        43: begin
          val <= 1849;
        end
        44: begin
          val <= 1936;
        end
        45: begin
          val <= 2025;
        end
        46: begin
          val <= 2116;
        end
        47: begin
          val <= 2209;
        end
        48: begin
          val <= 2304;
        end
        49: begin
          val <= 2401;
        end
        50: begin
          val <= 2500;
        end
        51: begin
          val <= 2601;
        end
        52: begin
          val <= 2704;
        end
        53: begin
          val <= 2809;
        end
        54: begin
          val <= 2916;
        end
        55: begin
          val <= 3025;
        end
        56: begin
          val <= 3136;
        end
        57: begin
          val <= 3249;
        end
        58: begin
          val <= 3364;
        end
        59: begin
          val <= 3481;
        end
        60: begin
          val <= 3600;
        end
        61: begin
          val <= 3721;
        end
        62: begin
          val <= 3844;
        end
        63: begin
          val <= 3969;
        end
        64: begin
          val <= 4096;
        end
        65: begin
          val <= 4225;
        end
        66: begin
          val <= 4356;
        end
        67: begin
          val <= 4489;
        end
        68: begin
          val <= 4624;
        end
        69: begin
          val <= 4761;
        end
        70: begin
          val <= 4900;
        end
        71: begin
          val <= 5041;
        end
        72: begin
          val <= 5184;
        end
        73: begin
          val <= 5329;
        end
        74: begin
          val <= 5476;
        end
        75: begin
          val <= 5625;
        end
        76: begin
          val <= 5776;
        end
        77: begin
          val <= 5929;
        end
        78: begin
          val <= 6084;
        end
        79: begin
          val <= 6241;
        end
        80: begin
          val <= 6400;
        end
        81: begin
          val <= 6561;
        end
        82: begin
          val <= 6724;
        end
        83: begin
          val <= 6889;
        end
        84: begin
          val <= 7056;
        end
        85: begin
          val <= 7225;
        end
        86: begin
          val <= 7396;
        end
        87: begin
          val <= 7569;
        end
        88: begin
          val <= 7744;
        end
        89: begin
          val <= 7921;
        end
        90: begin
          val <= 8100;
        end
        91: begin
          val <= 8281;
        end
        92: begin
          val <= 8464;
        end
        93: begin
          val <= 8649;
        end
        94: begin
          val <= 8836;
        end
        95: begin
          val <= 9025;
        end
        96: begin
          val <= 9216;
        end
        97: begin
          val <= 9409;
        end
        98: begin
          val <= 9604;
        end
        99: begin
          val <= 9801;
        end
        100: begin
          val <= 10000;
        end
        101: begin
          val <= 10201;
        end
        102: begin
          val <= 10404;
        end
        103: begin
          val <= 10609;
        end
        104: begin
          val <= 10816;
        end
        105: begin
          val <= 11025;
        end
        106: begin
          val <= 11236;
        end
        107: begin
          val <= 11449;
        end
        108: begin
          val <= 11664;
        end
        109: begin
          val <= 11881;
        end
        110: begin
          val <= 12100;
        end
        111: begin
          val <= 12321;
        end
        112: begin
          val <= 12544;
        end
        113: begin
          val <= 12769;
        end
        114: begin
          val <= 12996;
        end
        115: begin
          val <= 13225;
        end
        116: begin
          val <= 13456;
        end
        117: begin
          val <= 13689;
        end
        118: begin
          val <= 13924;
        end
        119: begin
          val <= 14161;
        end
        120: begin
          val <= 14400;
        end
        121: begin
          val <= 14641;
        end
        122: begin
          val <= 14884;
        end
        123: begin
          val <= 15129;
        end
        124: begin
          val <= 15376;
        end
        125: begin
          val <= 15625;
        end
        126: begin
          val <= 15876;
        end
        127: begin
          val <= 16129;
        end
        128: begin
          val <= 16384;
        end
        129: begin
          val <= 16641;
        end
        130: begin
          val <= 16900;
        end
        131: begin
          val <= 17161;
        end
        132: begin
          val <= 17424;
        end
        133: begin
          val <= 17689;
        end
        134: begin
          val <= 17956;
        end
        135: begin
          val <= 18225;
        end
        136: begin
          val <= 18496;
        end
        137: begin
          val <= 18769;
        end
        138: begin
          val <= 19044;
        end
        139: begin
          val <= 19321;
        end
        140: begin
          val <= 19600;
        end
        141: begin
          val <= 19881;
        end
        142: begin
          val <= 20164;
        end
        143: begin
          val <= 20449;
        end
        144: begin
          val <= 20736;
        end
        145: begin
          val <= 21025;
        end
        146: begin
          val <= 21316;
        end
        147: begin
          val <= 21609;
        end
        148: begin
          val <= 21904;
        end
        149: begin
          val <= 22201;
        end
        150: begin
          val <= 22500;
        end
        151: begin
          val <= 22801;
        end
        152: begin
          val <= 23104;
        end
        153: begin
          val <= 23409;
        end
        154: begin
          val <= 23716;
        end
        155: begin
          val <= 24025;
        end
        156: begin
          val <= 24336;
        end
        157: begin
          val <= 24649;
        end
        158: begin
          val <= 24964;
        end
        159: begin
          val <= 25281;
        end
        160: begin
          val <= 25600;
        end
        161: begin
          val <= 25921;
        end
        162: begin
          val <= 26244;
        end
        163: begin
          val <= 26569;
        end
        164: begin
          val <= 26896;
        end
        165: begin
          val <= 27225;
        end
        166: begin
          val <= 27556;
        end
        167: begin
          val <= 27889;
        end
        168: begin
          val <= 28224;
        end
        169: begin
          val <= 28561;
        end
        170: begin
          val <= 28900;
        end
        171: begin
          val <= 29241;
        end
        172: begin
          val <= 29584;
        end
        173: begin
          val <= 29929;
        end
        174: begin
          val <= 30276;
        end
        175: begin
          val <= 30625;
        end
        176: begin
          val <= 30976;
        end
        177: begin
          val <= 31329;
        end
        178: begin
          val <= 31684;
        end
        179: begin
          val <= 32041;
        end
        180: begin
          val <= 32400;
        end
        181: begin
          val <= 32761;
        end
        182: begin
          val <= 33124;
        end
        183: begin
          val <= 33489;
        end
        184: begin
          val <= 33856;
        end
        185: begin
          val <= 34225;
        end
        186: begin
          val <= 34596;
        end
        187: begin
          val <= 34969;
        end
        188: begin
          val <= 35344;
        end
        189: begin
          val <= 35721;
        end
        190: begin
          val <= 36100;
        end
        191: begin
          val <= 36481;
        end
        192: begin
          val <= 36864;
        end
        193: begin
          val <= 37249;
        end
        194: begin
          val <= 37636;
        end
        195: begin
          val <= 38025;
        end
        196: begin
          val <= 38416;
        end
        197: begin
          val <= 38809;
        end
        198: begin
          val <= 39204;
        end
        199: begin
          val <= 39601;
        end
        200: begin
          val <= 40000;
        end
        201: begin
          val <= 40401;
        end
        202: begin
          val <= 40804;
        end
        203: begin
          val <= 41209;
        end
        204: begin
          val <= 41616;
        end
        205: begin
          val <= 42025;
        end
        206: begin
          val <= 42436;
        end
        207: begin
          val <= 42849;
        end
        208: begin
          val <= 43264;
        end
        209: begin
          val <= 43681;
        end
        210: begin
          val <= 44100;
        end
        211: begin
          val <= 44521;
        end
        212: begin
          val <= 44944;
        end
        213: begin
          val <= 45369;
        end
        214: begin
          val <= 45796;
        end
        215: begin
          val <= 46225;
        end
        216: begin
          val <= 46656;
        end
        217: begin
          val <= 47089;
        end
        218: begin
          val <= 47524;
        end
        219: begin
          val <= 47961;
        end
        220: begin
          val <= 48400;
        end
        221: begin
          val <= 48841;
        end
        222: begin
          val <= 49284;
        end
        223: begin
          val <= 49729;
        end
        224: begin
          val <= 50176;
        end
        225: begin
          val <= 50625;
        end
        226: begin
          val <= 51076;
        end
        227: begin
          val <= 51529;
        end
        228: begin
          val <= 51984;
        end
        229: begin
          val <= 52441;
        end
        230: begin
          val <= 52900;
        end
        231: begin
          val <= 53361;
        end
        232: begin
          val <= 53824;
        end
        233: begin
          val <= 54289;
        end
        234: begin
          val <= 54756;
        end
        235: begin
          val <= 55225;
        end
        236: begin
          val <= 55696;
        end
        237: begin
          val <= 56169;
        end
        238: begin
          val <= 56644;
        end
        239: begin
          val <= 57121;
        end
        240: begin
          val <= 57600;
        end
        241: begin
          val <= 58081;
        end
        242: begin
          val <= 58564;
        end
        243: begin
          val <= 59049;
        end
        244: begin
          val <= 59536;
        end
        245: begin
          val <= 60025;
        end
        246: begin
          val <= 60516;
        end
        247: begin
          val <= 61009;
        end
        248: begin
          val <= 61504;
        end
        249: begin
          val <= 62001;
        end
        250: begin
          val <= 62500;
        end
        251: begin
          val <= 63001;
        end
        252: begin
          val <= 63504;
        end
        253: begin
          val <= 64009;
        end
        254: begin
          val <= 64516;
        end
        255: begin
          val <= 65025;
        end
      endcase
    end 
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = dataflow_lut.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
