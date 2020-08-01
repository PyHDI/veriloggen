from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_fixed_ram_initvals

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #10000;
    $finish;
  end


endmodule



module blinkled
(
  input CLK,
  input RST
);

  reg [10-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  reg [32-1:0] myram_0_wdata;
  reg myram_0_wenable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable)
  );

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_times_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg _tmp_0;
  reg _myram_cond_0_1;
  reg _myram_cond_1_1;
  reg _myram_cond_1_2;
  reg signed [32-1:0] _tmp_1;
  wire signed [32-1:0] _tmp_fixed_0;
  assign _tmp_fixed_0 = _tmp_1;
  reg signed [32-1:0] _th_blink_rdata_2;
  reg _tmp_2;
  reg _myram_cond_2_1;
  reg _myram_cond_3_1;
  reg _myram_cond_3_2;
  reg signed [32-1:0] _tmp_3;
  wire signed [32-1:0] _tmp_fixed_1;
  assign _tmp_fixed_1 = _tmp_3;
  reg signed [32-1:0] _th_blink_b_3;
  reg signed [33-1:0] _th_blink_wdata_4;
  reg _myram_cond_4_1;
  reg signed [32-1:0] _th_blink_sum_5;
  reg _tmp_4;
  reg _myram_cond_5_1;
  reg _myram_cond_6_1;
  reg _myram_cond_6_2;
  reg signed [32-1:0] _tmp_5;
  wire signed [32-1:0] _tmp_fixed_2;
  assign _tmp_fixed_2 = _tmp_5;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      _myram_cond_0_1 <= 0;
      _tmp_0 <= 0;
      _myram_cond_1_1 <= 0;
      _myram_cond_1_2 <= 0;
      _myram_cond_2_1 <= 0;
      _tmp_2 <= 0;
      _myram_cond_3_1 <= 0;
      _myram_cond_3_2 <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_4_1 <= 0;
      _myram_cond_5_1 <= 0;
      _tmp_4 <= 0;
      _myram_cond_6_1 <= 0;
      _myram_cond_6_2 <= 0;
    end else begin
      if(_myram_cond_1_2) begin
        _tmp_0 <= 0;
      end 
      if(_myram_cond_3_2) begin
        _tmp_2 <= 0;
      end 
      if(_myram_cond_6_2) begin
        _tmp_4 <= 0;
      end 
      if(_myram_cond_0_1) begin
        _tmp_0 <= 1;
      end 
      _myram_cond_1_2 <= _myram_cond_1_1;
      if(_myram_cond_2_1) begin
        _tmp_2 <= 1;
      end 
      _myram_cond_3_2 <= _myram_cond_3_1;
      if(_myram_cond_4_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_5_1) begin
        _tmp_4 <= 1;
      end 
      _myram_cond_6_2 <= _myram_cond_6_1;
      if(th_blink == 3) begin
        myram_0_addr <= _th_blink_i_1;
      end 
      _myram_cond_0_1 <= th_blink == 3;
      _myram_cond_1_1 <= th_blink == 3;
      if(th_blink == 9) begin
        myram_0_addr <= _th_blink_i_1;
      end 
      _myram_cond_2_1 <= th_blink == 9;
      _myram_cond_3_1 <= th_blink == 9;
      if(th_blink == 13) begin
        myram_0_addr <= _th_blink_i_1;
        myram_0_wdata <= _th_blink_wdata_4;
        myram_0_wenable <= 1;
      end 
      _myram_cond_4_1 <= th_blink == 13;
      if(th_blink == 19) begin
        myram_0_addr <= _th_blink_i_1;
      end 
      _myram_cond_5_1 <= th_blink == 19;
      _myram_cond_6_1 <= th_blink == 19;
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
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _tmp_1 <= 0;
      _tmp_3 <= 0;
      _tmp_5 <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          _th_blink_times_0 <= 10;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_3;
          end else begin
            th_blink <= th_blink_7;
          end
        end
        th_blink_3: begin
          if(_tmp_0) begin
            _tmp_1 <= myram_0_rdata;
          end 
          if(_tmp_0) begin
            th_blink <= th_blink_4;
          end 
        end
        th_blink_4: begin
          _th_blink_rdata_2 <= _tmp_fixed_0;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          $display("rdata = %f", ($itor(_th_blink_rdata_2) / 256.0));
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_7: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_16;
          end
        end
        th_blink_9: begin
          if(_tmp_2) begin
            _tmp_3 <= myram_0_rdata;
          end 
          if(_tmp_2) begin
            th_blink <= th_blink_10;
          end 
        end
        th_blink_10: begin
          _th_blink_rdata_2 <= _tmp_fixed_1;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_b_3 <= 'sd64;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          _th_blink_wdata_4 <= _th_blink_rdata_2 + _th_blink_b_3;
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          th_blink <= th_blink_14;
        end
        th_blink_14: begin
          $display("wdata = %f", ($itor(_th_blink_wdata_4) / 256.0));
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_8;
        end
        th_blink_16: begin
          _th_blink_sum_5 <= 'sd0;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_19;
          end else begin
            th_blink <= th_blink_24;
          end
        end
        th_blink_19: begin
          if(_tmp_4) begin
            _tmp_5 <= myram_0_rdata;
          end 
          if(_tmp_4) begin
            th_blink <= th_blink_20;
          end 
        end
        th_blink_20: begin
          _th_blink_rdata_2 <= _tmp_fixed_2;
          th_blink <= th_blink_21;
        end
        th_blink_21: begin
          $display("rdata = %f", ($itor(_th_blink_rdata_2) / 256.0));
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          _th_blink_sum_5 <= _th_blink_sum_5 + _th_blink_rdata_2;
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_18;
        end
        th_blink_24: begin
          $display("sum = %f", ($itor(_th_blink_sum_5) / 256.0));
          th_blink <= th_blink_25;
        end
      endcase
    end
  end


endmodule



module myram
(
  input CLK,
  input [10-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable
);

  reg [10-1:0] myram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  initial begin
    mem[0] = 32'ha00;
    mem[1] = 32'ha80;
    mem[2] = 32'hb00;
    mem[3] = 32'hb80;
    mem[4] = 32'hc00;
    mem[5] = 32'hc80;
    mem[6] = 32'hd00;
    mem[7] = 32'hd80;
    mem[8] = 32'he00;
    mem[9] = 32'he80;
    mem[10] = 32'hf00;
    mem[11] = 32'hf80;
    mem[12] = 32'h1000;
    mem[13] = 32'h1080;
    mem[14] = 32'h1100;
    mem[15] = 32'h1180;
    mem[16] = 32'h1200;
    mem[17] = 32'h1280;
    mem[18] = 32'h1300;
    mem[19] = 32'h1380;
    mem[20] = 32'h1400;
    mem[21] = 32'h1480;
    mem[22] = 32'h1500;
    mem[23] = 32'h1580;
    mem[24] = 32'h1600;
    mem[25] = 32'h1680;
    mem[26] = 32'h1700;
    mem[27] = 32'h1780;
    mem[28] = 32'h1800;
    mem[29] = 32'h1880;
    mem[30] = 32'h1900;
    mem[31] = 32'h1980;
    mem[32] = 32'h1a00;
    mem[33] = 32'h1a80;
    mem[34] = 32'h1b00;
    mem[35] = 32'h1b80;
    mem[36] = 32'h1c00;
    mem[37] = 32'h1c80;
    mem[38] = 32'h1d00;
    mem[39] = 32'h1d80;
    mem[40] = 32'h1e00;
    mem[41] = 32'h1e80;
    mem[42] = 32'h1f00;
    mem[43] = 32'h1f80;
    mem[44] = 32'h2000;
    mem[45] = 32'h2080;
    mem[46] = 32'h2100;
    mem[47] = 32'h2180;
    mem[48] = 32'h2200;
    mem[49] = 32'h2280;
    mem[50] = 32'h2300;
    mem[51] = 32'h2380;
    mem[52] = 32'h2400;
    mem[53] = 32'h2480;
    mem[54] = 32'h2500;
    mem[55] = 32'h2580;
    mem[56] = 32'h2600;
    mem[57] = 32'h2680;
    mem[58] = 32'h2700;
    mem[59] = 32'h2780;
    mem[60] = 32'h2800;
    mem[61] = 32'h2880;
    mem[62] = 32'h2900;
    mem[63] = 32'h2980;
    mem[64] = 32'h2a00;
    mem[65] = 32'h2a80;
    mem[66] = 32'h2b00;
    mem[67] = 32'h2b80;
    mem[68] = 32'h2c00;
    mem[69] = 32'h2c80;
    mem[70] = 32'h2d00;
    mem[71] = 32'h2d80;
    mem[72] = 32'h2e00;
    mem[73] = 32'h2e80;
    mem[74] = 32'h2f00;
    mem[75] = 32'h2f80;
    mem[76] = 32'h3000;
    mem[77] = 32'h3080;
    mem[78] = 32'h3100;
    mem[79] = 32'h3180;
    mem[80] = 32'h3200;
    mem[81] = 32'h3280;
    mem[82] = 32'h3300;
    mem[83] = 32'h3380;
    mem[84] = 32'h3400;
    mem[85] = 32'h3480;
    mem[86] = 32'h3500;
    mem[87] = 32'h3580;
    mem[88] = 32'h3600;
    mem[89] = 32'h3680;
    mem[90] = 32'h3700;
    mem[91] = 32'h3780;
    mem[92] = 32'h3800;
    mem[93] = 32'h3880;
    mem[94] = 32'h3900;
    mem[95] = 32'h3980;
    mem[96] = 32'h3a00;
    mem[97] = 32'h3a80;
    mem[98] = 32'h3b00;
    mem[99] = 32'h3b80;
    mem[100] = 32'h3c00;
    mem[101] = 32'h3c80;
    mem[102] = 32'h3d00;
    mem[103] = 32'h3d80;
    mem[104] = 32'h3e00;
    mem[105] = 32'h3e80;
    mem[106] = 32'h3f00;
    mem[107] = 32'h3f80;
    mem[108] = 32'h4000;
    mem[109] = 32'h4080;
    mem[110] = 32'h4100;
    mem[111] = 32'h4180;
    mem[112] = 32'h4200;
    mem[113] = 32'h4280;
    mem[114] = 32'h4300;
    mem[115] = 32'h4380;
    mem[116] = 32'h4400;
    mem[117] = 32'h4480;
    mem[118] = 32'h4500;
    mem[119] = 32'h4580;
    mem[120] = 32'h4600;
    mem[121] = 32'h4680;
    mem[122] = 32'h4700;
    mem[123] = 32'h4780;
    mem[124] = 32'h4800;
    mem[125] = 32'h4880;
    mem[126] = 32'h4900;
    mem[127] = 32'h4980;
    mem[128] = 32'h4a00;
    mem[129] = 32'h4a80;
    mem[130] = 32'h4b00;
    mem[131] = 32'h4b80;
    mem[132] = 32'h4c00;
    mem[133] = 32'h4c80;
    mem[134] = 32'h4d00;
    mem[135] = 32'h4d80;
    mem[136] = 32'h4e00;
    mem[137] = 32'h4e80;
    mem[138] = 32'h4f00;
    mem[139] = 32'h4f80;
    mem[140] = 32'h5000;
    mem[141] = 32'h5080;
    mem[142] = 32'h5100;
    mem[143] = 32'h5180;
    mem[144] = 32'h5200;
    mem[145] = 32'h5280;
    mem[146] = 32'h5300;
    mem[147] = 32'h5380;
    mem[148] = 32'h5400;
    mem[149] = 32'h5480;
    mem[150] = 32'h5500;
    mem[151] = 32'h5580;
    mem[152] = 32'h5600;
    mem[153] = 32'h5680;
    mem[154] = 32'h5700;
    mem[155] = 32'h5780;
    mem[156] = 32'h5800;
    mem[157] = 32'h5880;
    mem[158] = 32'h5900;
    mem[159] = 32'h5980;
    mem[160] = 32'h5a00;
    mem[161] = 32'h5a80;
    mem[162] = 32'h5b00;
    mem[163] = 32'h5b80;
    mem[164] = 32'h5c00;
    mem[165] = 32'h5c80;
    mem[166] = 32'h5d00;
    mem[167] = 32'h5d80;
    mem[168] = 32'h5e00;
    mem[169] = 32'h5e80;
    mem[170] = 32'h5f00;
    mem[171] = 32'h5f80;
    mem[172] = 32'h6000;
    mem[173] = 32'h6080;
    mem[174] = 32'h6100;
    mem[175] = 32'h6180;
    mem[176] = 32'h6200;
    mem[177] = 32'h6280;
    mem[178] = 32'h6300;
    mem[179] = 32'h6380;
    mem[180] = 32'h6400;
    mem[181] = 32'h6480;
    mem[182] = 32'h6500;
    mem[183] = 32'h6580;
    mem[184] = 32'h6600;
    mem[185] = 32'h6680;
    mem[186] = 32'h6700;
    mem[187] = 32'h6780;
    mem[188] = 32'h6800;
    mem[189] = 32'h6880;
    mem[190] = 32'h6900;
    mem[191] = 32'h6980;
    mem[192] = 32'h6a00;
    mem[193] = 32'h6a80;
    mem[194] = 32'h6b00;
    mem[195] = 32'h6b80;
    mem[196] = 32'h6c00;
    mem[197] = 32'h6c80;
    mem[198] = 32'h6d00;
    mem[199] = 32'h6d80;
    mem[200] = 32'h6e00;
    mem[201] = 32'h6e80;
    mem[202] = 32'h6f00;
    mem[203] = 32'h6f80;
    mem[204] = 32'h7000;
    mem[205] = 32'h7080;
    mem[206] = 32'h7100;
    mem[207] = 32'h7180;
    mem[208] = 32'h7200;
    mem[209] = 32'h7280;
    mem[210] = 32'h7300;
    mem[211] = 32'h7380;
    mem[212] = 32'h7400;
    mem[213] = 32'h7480;
    mem[214] = 32'h7500;
    mem[215] = 32'h7580;
    mem[216] = 32'h7600;
    mem[217] = 32'h7680;
    mem[218] = 32'h7700;
    mem[219] = 32'h7780;
    mem[220] = 32'h7800;
    mem[221] = 32'h7880;
    mem[222] = 32'h7900;
    mem[223] = 32'h7980;
    mem[224] = 32'h7a00;
    mem[225] = 32'h7a80;
    mem[226] = 32'h7b00;
    mem[227] = 32'h7b80;
    mem[228] = 32'h7c00;
    mem[229] = 32'h7c80;
    mem[230] = 32'h7d00;
    mem[231] = 32'h7d80;
    mem[232] = 32'h7e00;
    mem[233] = 32'h7e80;
    mem[234] = 32'h7f00;
    mem[235] = 32'h7f80;
    mem[236] = 32'h8000;
    mem[237] = 32'h8080;
    mem[238] = 32'h8100;
    mem[239] = 32'h8180;
    mem[240] = 32'h8200;
    mem[241] = 32'h8280;
    mem[242] = 32'h8300;
    mem[243] = 32'h8380;
    mem[244] = 32'h8400;
    mem[245] = 32'h8480;
    mem[246] = 32'h8500;
    mem[247] = 32'h8580;
    mem[248] = 32'h8600;
    mem[249] = 32'h8680;
    mem[250] = 32'h8700;
    mem[251] = 32'h8780;
    mem[252] = 32'h8800;
    mem[253] = 32'h8880;
    mem[254] = 32'h8900;
    mem[255] = 32'h8980;
    mem[256] = 32'h8a00;
    mem[257] = 32'h8a80;
    mem[258] = 32'h8b00;
    mem[259] = 32'h8b80;
    mem[260] = 32'h8c00;
    mem[261] = 32'h8c80;
    mem[262] = 32'h8d00;
    mem[263] = 32'h8d80;
    mem[264] = 32'h8e00;
    mem[265] = 32'h8e80;
    mem[266] = 32'h8f00;
    mem[267] = 32'h8f80;
    mem[268] = 32'h9000;
    mem[269] = 32'h9080;
    mem[270] = 32'h9100;
    mem[271] = 32'h9180;
    mem[272] = 32'h9200;
    mem[273] = 32'h9280;
    mem[274] = 32'h9300;
    mem[275] = 32'h9380;
    mem[276] = 32'h9400;
    mem[277] = 32'h9480;
    mem[278] = 32'h9500;
    mem[279] = 32'h9580;
    mem[280] = 32'h9600;
    mem[281] = 32'h9680;
    mem[282] = 32'h9700;
    mem[283] = 32'h9780;
    mem[284] = 32'h9800;
    mem[285] = 32'h9880;
    mem[286] = 32'h9900;
    mem[287] = 32'h9980;
    mem[288] = 32'h9a00;
    mem[289] = 32'h9a80;
    mem[290] = 32'h9b00;
    mem[291] = 32'h9b80;
    mem[292] = 32'h9c00;
    mem[293] = 32'h9c80;
    mem[294] = 32'h9d00;
    mem[295] = 32'h9d80;
    mem[296] = 32'h9e00;
    mem[297] = 32'h9e80;
    mem[298] = 32'h9f00;
    mem[299] = 32'h9f80;
    mem[300] = 32'ha000;
    mem[301] = 32'ha080;
    mem[302] = 32'ha100;
    mem[303] = 32'ha180;
    mem[304] = 32'ha200;
    mem[305] = 32'ha280;
    mem[306] = 32'ha300;
    mem[307] = 32'ha380;
    mem[308] = 32'ha400;
    mem[309] = 32'ha480;
    mem[310] = 32'ha500;
    mem[311] = 32'ha580;
    mem[312] = 32'ha600;
    mem[313] = 32'ha680;
    mem[314] = 32'ha700;
    mem[315] = 32'ha780;
    mem[316] = 32'ha800;
    mem[317] = 32'ha880;
    mem[318] = 32'ha900;
    mem[319] = 32'ha980;
    mem[320] = 32'haa00;
    mem[321] = 32'haa80;
    mem[322] = 32'hab00;
    mem[323] = 32'hab80;
    mem[324] = 32'hac00;
    mem[325] = 32'hac80;
    mem[326] = 32'had00;
    mem[327] = 32'had80;
    mem[328] = 32'hae00;
    mem[329] = 32'hae80;
    mem[330] = 32'haf00;
    mem[331] = 32'haf80;
    mem[332] = 32'hb000;
    mem[333] = 32'hb080;
    mem[334] = 32'hb100;
    mem[335] = 32'hb180;
    mem[336] = 32'hb200;
    mem[337] = 32'hb280;
    mem[338] = 32'hb300;
    mem[339] = 32'hb380;
    mem[340] = 32'hb400;
    mem[341] = 32'hb480;
    mem[342] = 32'hb500;
    mem[343] = 32'hb580;
    mem[344] = 32'hb600;
    mem[345] = 32'hb680;
    mem[346] = 32'hb700;
    mem[347] = 32'hb780;
    mem[348] = 32'hb800;
    mem[349] = 32'hb880;
    mem[350] = 32'hb900;
    mem[351] = 32'hb980;
    mem[352] = 32'hba00;
    mem[353] = 32'hba80;
    mem[354] = 32'hbb00;
    mem[355] = 32'hbb80;
    mem[356] = 32'hbc00;
    mem[357] = 32'hbc80;
    mem[358] = 32'hbd00;
    mem[359] = 32'hbd80;
    mem[360] = 32'hbe00;
    mem[361] = 32'hbe80;
    mem[362] = 32'hbf00;
    mem[363] = 32'hbf80;
    mem[364] = 32'hc000;
    mem[365] = 32'hc080;
    mem[366] = 32'hc100;
    mem[367] = 32'hc180;
    mem[368] = 32'hc200;
    mem[369] = 32'hc280;
    mem[370] = 32'hc300;
    mem[371] = 32'hc380;
    mem[372] = 32'hc400;
    mem[373] = 32'hc480;
    mem[374] = 32'hc500;
    mem[375] = 32'hc580;
    mem[376] = 32'hc600;
    mem[377] = 32'hc680;
    mem[378] = 32'hc700;
    mem[379] = 32'hc780;
    mem[380] = 32'hc800;
    mem[381] = 32'hc880;
    mem[382] = 32'hc900;
    mem[383] = 32'hc980;
    mem[384] = 32'hca00;
    mem[385] = 32'hca80;
    mem[386] = 32'hcb00;
    mem[387] = 32'hcb80;
    mem[388] = 32'hcc00;
    mem[389] = 32'hcc80;
    mem[390] = 32'hcd00;
    mem[391] = 32'hcd80;
    mem[392] = 32'hce00;
    mem[393] = 32'hce80;
    mem[394] = 32'hcf00;
    mem[395] = 32'hcf80;
    mem[396] = 32'hd000;
    mem[397] = 32'hd080;
    mem[398] = 32'hd100;
    mem[399] = 32'hd180;
    mem[400] = 32'hd200;
    mem[401] = 32'hd280;
    mem[402] = 32'hd300;
    mem[403] = 32'hd380;
    mem[404] = 32'hd400;
    mem[405] = 32'hd480;
    mem[406] = 32'hd500;
    mem[407] = 32'hd580;
    mem[408] = 32'hd600;
    mem[409] = 32'hd680;
    mem[410] = 32'hd700;
    mem[411] = 32'hd780;
    mem[412] = 32'hd800;
    mem[413] = 32'hd880;
    mem[414] = 32'hd900;
    mem[415] = 32'hd980;
    mem[416] = 32'hda00;
    mem[417] = 32'hda80;
    mem[418] = 32'hdb00;
    mem[419] = 32'hdb80;
    mem[420] = 32'hdc00;
    mem[421] = 32'hdc80;
    mem[422] = 32'hdd00;
    mem[423] = 32'hdd80;
    mem[424] = 32'hde00;
    mem[425] = 32'hde80;
    mem[426] = 32'hdf00;
    mem[427] = 32'hdf80;
    mem[428] = 32'he000;
    mem[429] = 32'he080;
    mem[430] = 32'he100;
    mem[431] = 32'he180;
    mem[432] = 32'he200;
    mem[433] = 32'he280;
    mem[434] = 32'he300;
    mem[435] = 32'he380;
    mem[436] = 32'he400;
    mem[437] = 32'he480;
    mem[438] = 32'he500;
    mem[439] = 32'he580;
    mem[440] = 32'he600;
    mem[441] = 32'he680;
    mem[442] = 32'he700;
    mem[443] = 32'he780;
    mem[444] = 32'he800;
    mem[445] = 32'he880;
    mem[446] = 32'he900;
    mem[447] = 32'he980;
    mem[448] = 32'hea00;
    mem[449] = 32'hea80;
    mem[450] = 32'heb00;
    mem[451] = 32'heb80;
    mem[452] = 32'hec00;
    mem[453] = 32'hec80;
    mem[454] = 32'hed00;
    mem[455] = 32'hed80;
    mem[456] = 32'hee00;
    mem[457] = 32'hee80;
    mem[458] = 32'hef00;
    mem[459] = 32'hef80;
    mem[460] = 32'hf000;
    mem[461] = 32'hf080;
    mem[462] = 32'hf100;
    mem[463] = 32'hf180;
    mem[464] = 32'hf200;
    mem[465] = 32'hf280;
    mem[466] = 32'hf300;
    mem[467] = 32'hf380;
    mem[468] = 32'hf400;
    mem[469] = 32'hf480;
    mem[470] = 32'hf500;
    mem[471] = 32'hf580;
    mem[472] = 32'hf600;
    mem[473] = 32'hf680;
    mem[474] = 32'hf700;
    mem[475] = 32'hf780;
    mem[476] = 32'hf800;
    mem[477] = 32'hf880;
    mem[478] = 32'hf900;
    mem[479] = 32'hf980;
    mem[480] = 32'hfa00;
    mem[481] = 32'hfa80;
    mem[482] = 32'hfb00;
    mem[483] = 32'hfb80;
    mem[484] = 32'hfc00;
    mem[485] = 32'hfc80;
    mem[486] = 32'hfd00;
    mem[487] = 32'hfd80;
    mem[488] = 32'hfe00;
    mem[489] = 32'hfe80;
    mem[490] = 32'hff00;
    mem[491] = 32'hff80;
    mem[492] = 32'h10000;
    mem[493] = 32'h10080;
    mem[494] = 32'h10100;
    mem[495] = 32'h10180;
    mem[496] = 32'h10200;
    mem[497] = 32'h10280;
    mem[498] = 32'h10300;
    mem[499] = 32'h10380;
    mem[500] = 32'h10400;
    mem[501] = 32'h10480;
    mem[502] = 32'h10500;
    mem[503] = 32'h10580;
    mem[504] = 32'h10600;
    mem[505] = 32'h10680;
    mem[506] = 32'h10700;
    mem[507] = 32'h10780;
    mem[508] = 32'h10800;
    mem[509] = 32'h10880;
    mem[510] = 32'h10900;
    mem[511] = 32'h10980;
    mem[512] = 32'h10a00;
    mem[513] = 32'h10a80;
    mem[514] = 32'h10b00;
    mem[515] = 32'h10b80;
    mem[516] = 32'h10c00;
    mem[517] = 32'h10c80;
    mem[518] = 32'h10d00;
    mem[519] = 32'h10d80;
    mem[520] = 32'h10e00;
    mem[521] = 32'h10e80;
    mem[522] = 32'h10f00;
    mem[523] = 32'h10f80;
    mem[524] = 32'h11000;
    mem[525] = 32'h11080;
    mem[526] = 32'h11100;
    mem[527] = 32'h11180;
    mem[528] = 32'h11200;
    mem[529] = 32'h11280;
    mem[530] = 32'h11300;
    mem[531] = 32'h11380;
    mem[532] = 32'h11400;
    mem[533] = 32'h11480;
    mem[534] = 32'h11500;
    mem[535] = 32'h11580;
    mem[536] = 32'h11600;
    mem[537] = 32'h11680;
    mem[538] = 32'h11700;
    mem[539] = 32'h11780;
    mem[540] = 32'h11800;
    mem[541] = 32'h11880;
    mem[542] = 32'h11900;
    mem[543] = 32'h11980;
    mem[544] = 32'h11a00;
    mem[545] = 32'h11a80;
    mem[546] = 32'h11b00;
    mem[547] = 32'h11b80;
    mem[548] = 32'h11c00;
    mem[549] = 32'h11c80;
    mem[550] = 32'h11d00;
    mem[551] = 32'h11d80;
    mem[552] = 32'h11e00;
    mem[553] = 32'h11e80;
    mem[554] = 32'h11f00;
    mem[555] = 32'h11f80;
    mem[556] = 32'h12000;
    mem[557] = 32'h12080;
    mem[558] = 32'h12100;
    mem[559] = 32'h12180;
    mem[560] = 32'h12200;
    mem[561] = 32'h12280;
    mem[562] = 32'h12300;
    mem[563] = 32'h12380;
    mem[564] = 32'h12400;
    mem[565] = 32'h12480;
    mem[566] = 32'h12500;
    mem[567] = 32'h12580;
    mem[568] = 32'h12600;
    mem[569] = 32'h12680;
    mem[570] = 32'h12700;
    mem[571] = 32'h12780;
    mem[572] = 32'h12800;
    mem[573] = 32'h12880;
    mem[574] = 32'h12900;
    mem[575] = 32'h12980;
    mem[576] = 32'h12a00;
    mem[577] = 32'h12a80;
    mem[578] = 32'h12b00;
    mem[579] = 32'h12b80;
    mem[580] = 32'h12c00;
    mem[581] = 32'h12c80;
    mem[582] = 32'h12d00;
    mem[583] = 32'h12d80;
    mem[584] = 32'h12e00;
    mem[585] = 32'h12e80;
    mem[586] = 32'h12f00;
    mem[587] = 32'h12f80;
    mem[588] = 32'h13000;
    mem[589] = 32'h13080;
    mem[590] = 32'h13100;
    mem[591] = 32'h13180;
    mem[592] = 32'h13200;
    mem[593] = 32'h13280;
    mem[594] = 32'h13300;
    mem[595] = 32'h13380;
    mem[596] = 32'h13400;
    mem[597] = 32'h13480;
    mem[598] = 32'h13500;
    mem[599] = 32'h13580;
    mem[600] = 32'h13600;
    mem[601] = 32'h13680;
    mem[602] = 32'h13700;
    mem[603] = 32'h13780;
    mem[604] = 32'h13800;
    mem[605] = 32'h13880;
    mem[606] = 32'h13900;
    mem[607] = 32'h13980;
    mem[608] = 32'h13a00;
    mem[609] = 32'h13a80;
    mem[610] = 32'h13b00;
    mem[611] = 32'h13b80;
    mem[612] = 32'h13c00;
    mem[613] = 32'h13c80;
    mem[614] = 32'h13d00;
    mem[615] = 32'h13d80;
    mem[616] = 32'h13e00;
    mem[617] = 32'h13e80;
    mem[618] = 32'h13f00;
    mem[619] = 32'h13f80;
    mem[620] = 32'h14000;
    mem[621] = 32'h14080;
    mem[622] = 32'h14100;
    mem[623] = 32'h14180;
    mem[624] = 32'h14200;
    mem[625] = 32'h14280;
    mem[626] = 32'h14300;
    mem[627] = 32'h14380;
    mem[628] = 32'h14400;
    mem[629] = 32'h14480;
    mem[630] = 32'h14500;
    mem[631] = 32'h14580;
    mem[632] = 32'h14600;
    mem[633] = 32'h14680;
    mem[634] = 32'h14700;
    mem[635] = 32'h14780;
    mem[636] = 32'h14800;
    mem[637] = 32'h14880;
    mem[638] = 32'h14900;
    mem[639] = 32'h14980;
    mem[640] = 32'h14a00;
    mem[641] = 32'h14a80;
    mem[642] = 32'h14b00;
    mem[643] = 32'h14b80;
    mem[644] = 32'h14c00;
    mem[645] = 32'h14c80;
    mem[646] = 32'h14d00;
    mem[647] = 32'h14d80;
    mem[648] = 32'h14e00;
    mem[649] = 32'h14e80;
    mem[650] = 32'h14f00;
    mem[651] = 32'h14f80;
    mem[652] = 32'h15000;
    mem[653] = 32'h15080;
    mem[654] = 32'h15100;
    mem[655] = 32'h15180;
    mem[656] = 32'h15200;
    mem[657] = 32'h15280;
    mem[658] = 32'h15300;
    mem[659] = 32'h15380;
    mem[660] = 32'h15400;
    mem[661] = 32'h15480;
    mem[662] = 32'h15500;
    mem[663] = 32'h15580;
    mem[664] = 32'h15600;
    mem[665] = 32'h15680;
    mem[666] = 32'h15700;
    mem[667] = 32'h15780;
    mem[668] = 32'h15800;
    mem[669] = 32'h15880;
    mem[670] = 32'h15900;
    mem[671] = 32'h15980;
    mem[672] = 32'h15a00;
    mem[673] = 32'h15a80;
    mem[674] = 32'h15b00;
    mem[675] = 32'h15b80;
    mem[676] = 32'h15c00;
    mem[677] = 32'h15c80;
    mem[678] = 32'h15d00;
    mem[679] = 32'h15d80;
    mem[680] = 32'h15e00;
    mem[681] = 32'h15e80;
    mem[682] = 32'h15f00;
    mem[683] = 32'h15f80;
    mem[684] = 32'h16000;
    mem[685] = 32'h16080;
    mem[686] = 32'h16100;
    mem[687] = 32'h16180;
    mem[688] = 32'h16200;
    mem[689] = 32'h16280;
    mem[690] = 32'h16300;
    mem[691] = 32'h16380;
    mem[692] = 32'h16400;
    mem[693] = 32'h16480;
    mem[694] = 32'h16500;
    mem[695] = 32'h16580;
    mem[696] = 32'h16600;
    mem[697] = 32'h16680;
    mem[698] = 32'h16700;
    mem[699] = 32'h16780;
    mem[700] = 32'h16800;
    mem[701] = 32'h16880;
    mem[702] = 32'h16900;
    mem[703] = 32'h16980;
    mem[704] = 32'h16a00;
    mem[705] = 32'h16a80;
    mem[706] = 32'h16b00;
    mem[707] = 32'h16b80;
    mem[708] = 32'h16c00;
    mem[709] = 32'h16c80;
    mem[710] = 32'h16d00;
    mem[711] = 32'h16d80;
    mem[712] = 32'h16e00;
    mem[713] = 32'h16e80;
    mem[714] = 32'h16f00;
    mem[715] = 32'h16f80;
    mem[716] = 32'h17000;
    mem[717] = 32'h17080;
    mem[718] = 32'h17100;
    mem[719] = 32'h17180;
    mem[720] = 32'h17200;
    mem[721] = 32'h17280;
    mem[722] = 32'h17300;
    mem[723] = 32'h17380;
    mem[724] = 32'h17400;
    mem[725] = 32'h17480;
    mem[726] = 32'h17500;
    mem[727] = 32'h17580;
    mem[728] = 32'h17600;
    mem[729] = 32'h17680;
    mem[730] = 32'h17700;
    mem[731] = 32'h17780;
    mem[732] = 32'h17800;
    mem[733] = 32'h17880;
    mem[734] = 32'h17900;
    mem[735] = 32'h17980;
    mem[736] = 32'h17a00;
    mem[737] = 32'h17a80;
    mem[738] = 32'h17b00;
    mem[739] = 32'h17b80;
    mem[740] = 32'h17c00;
    mem[741] = 32'h17c80;
    mem[742] = 32'h17d00;
    mem[743] = 32'h17d80;
    mem[744] = 32'h17e00;
    mem[745] = 32'h17e80;
    mem[746] = 32'h17f00;
    mem[747] = 32'h17f80;
    mem[748] = 32'h18000;
    mem[749] = 32'h18080;
    mem[750] = 32'h18100;
    mem[751] = 32'h18180;
    mem[752] = 32'h18200;
    mem[753] = 32'h18280;
    mem[754] = 32'h18300;
    mem[755] = 32'h18380;
    mem[756] = 32'h18400;
    mem[757] = 32'h18480;
    mem[758] = 32'h18500;
    mem[759] = 32'h18580;
    mem[760] = 32'h18600;
    mem[761] = 32'h18680;
    mem[762] = 32'h18700;
    mem[763] = 32'h18780;
    mem[764] = 32'h18800;
    mem[765] = 32'h18880;
    mem[766] = 32'h18900;
    mem[767] = 32'h18980;
    mem[768] = 32'h18a00;
    mem[769] = 32'h18a80;
    mem[770] = 32'h18b00;
    mem[771] = 32'h18b80;
    mem[772] = 32'h18c00;
    mem[773] = 32'h18c80;
    mem[774] = 32'h18d00;
    mem[775] = 32'h18d80;
    mem[776] = 32'h18e00;
    mem[777] = 32'h18e80;
    mem[778] = 32'h18f00;
    mem[779] = 32'h18f80;
    mem[780] = 32'h19000;
    mem[781] = 32'h19080;
    mem[782] = 32'h19100;
    mem[783] = 32'h19180;
    mem[784] = 32'h19200;
    mem[785] = 32'h19280;
    mem[786] = 32'h19300;
    mem[787] = 32'h19380;
    mem[788] = 32'h19400;
    mem[789] = 32'h19480;
    mem[790] = 32'h19500;
    mem[791] = 32'h19580;
    mem[792] = 32'h19600;
    mem[793] = 32'h19680;
    mem[794] = 32'h19700;
    mem[795] = 32'h19780;
    mem[796] = 32'h19800;
    mem[797] = 32'h19880;
    mem[798] = 32'h19900;
    mem[799] = 32'h19980;
    mem[800] = 32'h19a00;
    mem[801] = 32'h19a80;
    mem[802] = 32'h19b00;
    mem[803] = 32'h19b80;
    mem[804] = 32'h19c00;
    mem[805] = 32'h19c80;
    mem[806] = 32'h19d00;
    mem[807] = 32'h19d80;
    mem[808] = 32'h19e00;
    mem[809] = 32'h19e80;
    mem[810] = 32'h19f00;
    mem[811] = 32'h19f80;
    mem[812] = 32'h1a000;
    mem[813] = 32'h1a080;
    mem[814] = 32'h1a100;
    mem[815] = 32'h1a180;
    mem[816] = 32'h1a200;
    mem[817] = 32'h1a280;
    mem[818] = 32'h1a300;
    mem[819] = 32'h1a380;
    mem[820] = 32'h1a400;
    mem[821] = 32'h1a480;
    mem[822] = 32'h1a500;
    mem[823] = 32'h1a580;
    mem[824] = 32'h1a600;
    mem[825] = 32'h1a680;
    mem[826] = 32'h1a700;
    mem[827] = 32'h1a780;
    mem[828] = 32'h1a800;
    mem[829] = 32'h1a880;
    mem[830] = 32'h1a900;
    mem[831] = 32'h1a980;
    mem[832] = 32'h1aa00;
    mem[833] = 32'h1aa80;
    mem[834] = 32'h1ab00;
    mem[835] = 32'h1ab80;
    mem[836] = 32'h1ac00;
    mem[837] = 32'h1ac80;
    mem[838] = 32'h1ad00;
    mem[839] = 32'h1ad80;
    mem[840] = 32'h1ae00;
    mem[841] = 32'h1ae80;
    mem[842] = 32'h1af00;
    mem[843] = 32'h1af80;
    mem[844] = 32'h1b000;
    mem[845] = 32'h1b080;
    mem[846] = 32'h1b100;
    mem[847] = 32'h1b180;
    mem[848] = 32'h1b200;
    mem[849] = 32'h1b280;
    mem[850] = 32'h1b300;
    mem[851] = 32'h1b380;
    mem[852] = 32'h1b400;
    mem[853] = 32'h1b480;
    mem[854] = 32'h1b500;
    mem[855] = 32'h1b580;
    mem[856] = 32'h1b600;
    mem[857] = 32'h1b680;
    mem[858] = 32'h1b700;
    mem[859] = 32'h1b780;
    mem[860] = 32'h1b800;
    mem[861] = 32'h1b880;
    mem[862] = 32'h1b900;
    mem[863] = 32'h1b980;
    mem[864] = 32'h1ba00;
    mem[865] = 32'h1ba80;
    mem[866] = 32'h1bb00;
    mem[867] = 32'h1bb80;
    mem[868] = 32'h1bc00;
    mem[869] = 32'h1bc80;
    mem[870] = 32'h1bd00;
    mem[871] = 32'h1bd80;
    mem[872] = 32'h1be00;
    mem[873] = 32'h1be80;
    mem[874] = 32'h1bf00;
    mem[875] = 32'h1bf80;
    mem[876] = 32'h1c000;
    mem[877] = 32'h1c080;
    mem[878] = 32'h1c100;
    mem[879] = 32'h1c180;
    mem[880] = 32'h1c200;
    mem[881] = 32'h1c280;
    mem[882] = 32'h1c300;
    mem[883] = 32'h1c380;
    mem[884] = 32'h1c400;
    mem[885] = 32'h1c480;
    mem[886] = 32'h1c500;
    mem[887] = 32'h1c580;
    mem[888] = 32'h1c600;
    mem[889] = 32'h1c680;
    mem[890] = 32'h1c700;
    mem[891] = 32'h1c780;
    mem[892] = 32'h1c800;
    mem[893] = 32'h1c880;
    mem[894] = 32'h1c900;
    mem[895] = 32'h1c980;
    mem[896] = 32'h1ca00;
    mem[897] = 32'h1ca80;
    mem[898] = 32'h1cb00;
    mem[899] = 32'h1cb80;
    mem[900] = 32'h1cc00;
    mem[901] = 32'h1cc80;
    mem[902] = 32'h1cd00;
    mem[903] = 32'h1cd80;
    mem[904] = 32'h1ce00;
    mem[905] = 32'h1ce80;
    mem[906] = 32'h1cf00;
    mem[907] = 32'h1cf80;
    mem[908] = 32'h1d000;
    mem[909] = 32'h1d080;
    mem[910] = 32'h1d100;
    mem[911] = 32'h1d180;
    mem[912] = 32'h1d200;
    mem[913] = 32'h1d280;
    mem[914] = 32'h1d300;
    mem[915] = 32'h1d380;
    mem[916] = 32'h1d400;
    mem[917] = 32'h1d480;
    mem[918] = 32'h1d500;
    mem[919] = 32'h1d580;
    mem[920] = 32'h1d600;
    mem[921] = 32'h1d680;
    mem[922] = 32'h1d700;
    mem[923] = 32'h1d780;
    mem[924] = 32'h0;
    mem[925] = 32'h0;
    mem[926] = 32'h0;
    mem[927] = 32'h0;
    mem[928] = 32'h0;
    mem[929] = 32'h0;
    mem[930] = 32'h0;
    mem[931] = 32'h0;
    mem[932] = 32'h0;
    mem[933] = 32'h0;
    mem[934] = 32'h0;
    mem[935] = 32'h0;
    mem[936] = 32'h0;
    mem[937] = 32'h0;
    mem[938] = 32'h0;
    mem[939] = 32'h0;
    mem[940] = 32'h0;
    mem[941] = 32'h0;
    mem[942] = 32'h0;
    mem[943] = 32'h0;
    mem[944] = 32'h0;
    mem[945] = 32'h0;
    mem[946] = 32'h0;
    mem[947] = 32'h0;
    mem[948] = 32'h0;
    mem[949] = 32'h0;
    mem[950] = 32'h0;
    mem[951] = 32'h0;
    mem[952] = 32'h0;
    mem[953] = 32'h0;
    mem[954] = 32'h0;
    mem[955] = 32'h0;
    mem[956] = 32'h0;
    mem[957] = 32'h0;
    mem[958] = 32'h0;
    mem[959] = 32'h0;
    mem[960] = 32'h0;
    mem[961] = 32'h0;
    mem[962] = 32'h0;
    mem[963] = 32'h0;
    mem[964] = 32'h0;
    mem[965] = 32'h0;
    mem[966] = 32'h0;
    mem[967] = 32'h0;
    mem[968] = 32'h0;
    mem[969] = 32'h0;
    mem[970] = 32'h0;
    mem[971] = 32'h0;
    mem[972] = 32'h0;
    mem[973] = 32'h0;
    mem[974] = 32'h0;
    mem[975] = 32'h0;
    mem[976] = 32'h0;
    mem[977] = 32'h0;
    mem[978] = 32'h0;
    mem[979] = 32'h0;
    mem[980] = 32'h0;
    mem[981] = 32'h0;
    mem[982] = 32'h0;
    mem[983] = 32'h0;
    mem[984] = 32'h0;
    mem[985] = 32'h0;
    mem[986] = 32'h0;
    mem[987] = 32'h0;
    mem[988] = 32'h0;
    mem[989] = 32'h0;
    mem[990] = 32'h0;
    mem[991] = 32'h0;
    mem[992] = 32'h0;
    mem[993] = 32'h0;
    mem[994] = 32'h0;
    mem[995] = 32'h0;
    mem[996] = 32'h0;
    mem[997] = 32'h0;
    mem[998] = 32'h0;
    mem[999] = 32'h0;
    mem[1000] = 32'h0;
    mem[1001] = 32'h0;
    mem[1002] = 32'h0;
    mem[1003] = 32'h0;
    mem[1004] = 32'h0;
    mem[1005] = 32'h0;
    mem[1006] = 32'h0;
    mem[1007] = 32'h0;
    mem[1008] = 32'h0;
    mem[1009] = 32'h0;
    mem[1010] = 32'h0;
    mem[1011] = 32'h0;
    mem[1012] = 32'h0;
    mem[1013] = 32'h0;
    mem[1014] = 32'h0;
    mem[1015] = 32'h0;
    mem[1016] = 32'h0;
    mem[1017] = 32'h0;
    mem[1018] = 32'h0;
    mem[1019] = 32'h0;
    mem[1020] = 32'h0;
    mem[1021] = 32'h0;
    mem[1022] = 32'h0;
    mem[1023] = 32'h0;
  end


  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_fixed_ram_initvals.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
