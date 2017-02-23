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
          val <= 100;
        end
        1: begin
          val <= 101;
        end
        2: begin
          val <= 102;
        end
        3: begin
          val <= 103;
        end
        4: begin
          val <= 104;
        end
        5: begin
          val <= 105;
        end
        6: begin
          val <= 106;
        end
        7: begin
          val <= 107;
        end
        8: begin
          val <= 108;
        end
        9: begin
          val <= 109;
        end
        10: begin
          val <= 110;
        end
        11: begin
          val <= 111;
        end
        12: begin
          val <= 112;
        end
        13: begin
          val <= 113;
        end
        14: begin
          val <= 114;
        end
        15: begin
          val <= 115;
        end
        16: begin
          val <= 116;
        end
        17: begin
          val <= 117;
        end
        18: begin
          val <= 118;
        end
        19: begin
          val <= 119;
        end
        20: begin
          val <= 120;
        end
        21: begin
          val <= 121;
        end
        22: begin
          val <= 122;
        end
        23: begin
          val <= 123;
        end
        24: begin
          val <= 124;
        end
        25: begin
          val <= 125;
        end
        26: begin
          val <= 126;
        end
        27: begin
          val <= 127;
        end
        28: begin
          val <= 128;
        end
        29: begin
          val <= 129;
        end
        30: begin
          val <= 130;
        end
        31: begin
          val <= 131;
        end
        32: begin
          val <= 132;
        end
        33: begin
          val <= 133;
        end
        34: begin
          val <= 134;
        end
        35: begin
          val <= 135;
        end
        36: begin
          val <= 136;
        end
        37: begin
          val <= 137;
        end
        38: begin
          val <= 138;
        end
        39: begin
          val <= 139;
        end
        40: begin
          val <= 140;
        end
        41: begin
          val <= 141;
        end
        42: begin
          val <= 142;
        end
        43: begin
          val <= 143;
        end
        44: begin
          val <= 144;
        end
        45: begin
          val <= 145;
        end
        46: begin
          val <= 146;
        end
        47: begin
          val <= 147;
        end
        48: begin
          val <= 148;
        end
        49: begin
          val <= 149;
        end
        50: begin
          val <= 150;
        end
        51: begin
          val <= 151;
        end
        52: begin
          val <= 152;
        end
        53: begin
          val <= 153;
        end
        54: begin
          val <= 154;
        end
        55: begin
          val <= 155;
        end
        56: begin
          val <= 156;
        end
        57: begin
          val <= 157;
        end
        58: begin
          val <= 158;
        end
        59: begin
          val <= 159;
        end
        60: begin
          val <= 160;
        end
        61: begin
          val <= 161;
        end
        62: begin
          val <= 162;
        end
        63: begin
          val <= 163;
        end
        64: begin
          val <= 164;
        end
        65: begin
          val <= 165;
        end
        66: begin
          val <= 166;
        end
        67: begin
          val <= 167;
        end
        68: begin
          val <= 168;
        end
        69: begin
          val <= 169;
        end
        70: begin
          val <= 170;
        end
        71: begin
          val <= 171;
        end
        72: begin
          val <= 172;
        end
        73: begin
          val <= 173;
        end
        74: begin
          val <= 174;
        end
        75: begin
          val <= 175;
        end
        76: begin
          val <= 176;
        end
        77: begin
          val <= 177;
        end
        78: begin
          val <= 178;
        end
        79: begin
          val <= 179;
        end
        80: begin
          val <= 180;
        end
        81: begin
          val <= 181;
        end
        82: begin
          val <= 182;
        end
        83: begin
          val <= 183;
        end
        84: begin
          val <= 184;
        end
        85: begin
          val <= 185;
        end
        86: begin
          val <= 186;
        end
        87: begin
          val <= 187;
        end
        88: begin
          val <= 188;
        end
        89: begin
          val <= 189;
        end
        90: begin
          val <= 190;
        end
        91: begin
          val <= 191;
        end
        92: begin
          val <= 192;
        end
        93: begin
          val <= 193;
        end
        94: begin
          val <= 194;
        end
        95: begin
          val <= 195;
        end
        96: begin
          val <= 196;
        end
        97: begin
          val <= 197;
        end
        98: begin
          val <= 198;
        end
        99: begin
          val <= 199;
        end
        100: begin
          val <= 200;
        end
        101: begin
          val <= 201;
        end
        102: begin
          val <= 202;
        end
        103: begin
          val <= 203;
        end
        104: begin
          val <= 204;
        end
        105: begin
          val <= 205;
        end
        106: begin
          val <= 206;
        end
        107: begin
          val <= 207;
        end
        108: begin
          val <= 208;
        end
        109: begin
          val <= 209;
        end
        110: begin
          val <= 210;
        end
        111: begin
          val <= 211;
        end
        112: begin
          val <= 212;
        end
        113: begin
          val <= 213;
        end
        114: begin
          val <= 214;
        end
        115: begin
          val <= 215;
        end
        116: begin
          val <= 216;
        end
        117: begin
          val <= 217;
        end
        118: begin
          val <= 218;
        end
        119: begin
          val <= 219;
        end
        120: begin
          val <= 220;
        end
        121: begin
          val <= 221;
        end
        122: begin
          val <= 222;
        end
        123: begin
          val <= 223;
        end
        124: begin
          val <= 224;
        end
        125: begin
          val <= 225;
        end
        126: begin
          val <= 226;
        end
        127: begin
          val <= 227;
        end
        128: begin
          val <= 228;
        end
        129: begin
          val <= 229;
        end
        130: begin
          val <= 230;
        end
        131: begin
          val <= 231;
        end
        132: begin
          val <= 232;
        end
        133: begin
          val <= 233;
        end
        134: begin
          val <= 234;
        end
        135: begin
          val <= 235;
        end
        136: begin
          val <= 236;
        end
        137: begin
          val <= 237;
        end
        138: begin
          val <= 238;
        end
        139: begin
          val <= 239;
        end
        140: begin
          val <= 240;
        end
        141: begin
          val <= 241;
        end
        142: begin
          val <= 242;
        end
        143: begin
          val <= 243;
        end
        144: begin
          val <= 244;
        end
        145: begin
          val <= 245;
        end
        146: begin
          val <= 246;
        end
        147: begin
          val <= 247;
        end
        148: begin
          val <= 248;
        end
        149: begin
          val <= 249;
        end
        150: begin
          val <= 250;
        end
        151: begin
          val <= 251;
        end
        152: begin
          val <= 252;
        end
        153: begin
          val <= 253;
        end
        154: begin
          val <= 254;
        end
        155: begin
          val <= 255;
        end
        156: begin
          val <= 256;
        end
        157: begin
          val <= 257;
        end
        158: begin
          val <= 258;
        end
        159: begin
          val <= 259;
        end
        160: begin
          val <= 260;
        end
        161: begin
          val <= 261;
        end
        162: begin
          val <= 262;
        end
        163: begin
          val <= 263;
        end
        164: begin
          val <= 264;
        end
        165: begin
          val <= 265;
        end
        166: begin
          val <= 266;
        end
        167: begin
          val <= 267;
        end
        168: begin
          val <= 268;
        end
        169: begin
          val <= 269;
        end
        170: begin
          val <= 270;
        end
        171: begin
          val <= 271;
        end
        172: begin
          val <= 272;
        end
        173: begin
          val <= 273;
        end
        174: begin
          val <= 274;
        end
        175: begin
          val <= 275;
        end
        176: begin
          val <= 276;
        end
        177: begin
          val <= 277;
        end
        178: begin
          val <= 278;
        end
        179: begin
          val <= 279;
        end
        180: begin
          val <= 280;
        end
        181: begin
          val <= 281;
        end
        182: begin
          val <= 282;
        end
        183: begin
          val <= 283;
        end
        184: begin
          val <= 284;
        end
        185: begin
          val <= 285;
        end
        186: begin
          val <= 286;
        end
        187: begin
          val <= 287;
        end
        188: begin
          val <= 288;
        end
        189: begin
          val <= 289;
        end
        190: begin
          val <= 290;
        end
        191: begin
          val <= 291;
        end
        192: begin
          val <= 292;
        end
        193: begin
          val <= 293;
        end
        194: begin
          val <= 294;
        end
        195: begin
          val <= 295;
        end
        196: begin
          val <= 296;
        end
        197: begin
          val <= 297;
        end
        198: begin
          val <= 298;
        end
        199: begin
          val <= 299;
        end
        200: begin
          val <= 300;
        end
        201: begin
          val <= 301;
        end
        202: begin
          val <= 302;
        end
        203: begin
          val <= 303;
        end
        204: begin
          val <= 304;
        end
        205: begin
          val <= 305;
        end
        206: begin
          val <= 306;
        end
        207: begin
          val <= 307;
        end
        208: begin
          val <= 308;
        end
        209: begin
          val <= 309;
        end
        210: begin
          val <= 310;
        end
        211: begin
          val <= 311;
        end
        212: begin
          val <= 312;
        end
        213: begin
          val <= 313;
        end
        214: begin
          val <= 314;
        end
        215: begin
          val <= 315;
        end
        216: begin
          val <= 316;
        end
        217: begin
          val <= 317;
        end
        218: begin
          val <= 318;
        end
        219: begin
          val <= 319;
        end
        220: begin
          val <= 320;
        end
        221: begin
          val <= 321;
        end
        222: begin
          val <= 322;
        end
        223: begin
          val <= 323;
        end
        224: begin
          val <= 324;
        end
        225: begin
          val <= 325;
        end
        226: begin
          val <= 326;
        end
        227: begin
          val <= 327;
        end
        228: begin
          val <= 328;
        end
        229: begin
          val <= 329;
        end
        230: begin
          val <= 330;
        end
        231: begin
          val <= 331;
        end
        232: begin
          val <= 332;
        end
        233: begin
          val <= 333;
        end
        234: begin
          val <= 334;
        end
        235: begin
          val <= 335;
        end
        236: begin
          val <= 336;
        end
        237: begin
          val <= 337;
        end
        238: begin
          val <= 338;
        end
        239: begin
          val <= 339;
        end
        240: begin
          val <= 340;
        end
        241: begin
          val <= 341;
        end
        242: begin
          val <= 342;
        end
        243: begin
          val <= 343;
        end
        244: begin
          val <= 344;
        end
        245: begin
          val <= 345;
        end
        246: begin
          val <= 346;
        end
        247: begin
          val <= 347;
        end
        248: begin
          val <= 348;
        end
        249: begin
          val <= 349;
        end
        250: begin
          val <= 350;
        end
        251: begin
          val <= 351;
        end
        252: begin
          val <= 352;
        end
        253: begin
          val <= 353;
        end
        254: begin
          val <= 354;
        end
        255: begin
          val <= 355;
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
