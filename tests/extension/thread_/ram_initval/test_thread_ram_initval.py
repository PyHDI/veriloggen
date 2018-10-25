from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_ram_initval

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
  reg signed [32-1:0] _th_blink_rdata_2;
  reg signed [32-1:0] _th_blink_wdata_3;
  reg _myram_cond_2_1;
  reg signed [32-1:0] _th_blink_sum_4;
  reg _tmp_2;
  reg _myram_cond_3_1;
  reg _myram_cond_4_1;
  reg _myram_cond_4_2;
  reg signed [32-1:0] _tmp_3;

  always @(posedge CLK) begin
    if(RST) begin
      myram_0_addr <= 0;
      _myram_cond_0_1 <= 0;
      _tmp_0 <= 0;
      _myram_cond_1_1 <= 0;
      _myram_cond_1_2 <= 0;
      myram_0_wdata <= 0;
      myram_0_wenable <= 0;
      _myram_cond_2_1 <= 0;
      _myram_cond_3_1 <= 0;
      _tmp_2 <= 0;
      _myram_cond_4_1 <= 0;
      _myram_cond_4_2 <= 0;
    end else begin
      if(_myram_cond_1_2) begin
        _tmp_0 <= 0;
      end 
      if(_myram_cond_4_2) begin
        _tmp_2 <= 0;
      end 
      if(_myram_cond_0_1) begin
        _tmp_0 <= 1;
      end 
      _myram_cond_1_2 <= _myram_cond_1_1;
      if(_myram_cond_2_1) begin
        myram_0_wenable <= 0;
      end 
      if(_myram_cond_3_1) begin
        _tmp_2 <= 1;
      end 
      _myram_cond_4_2 <= _myram_cond_4_1;
      if(th_blink == 3) begin
        myram_0_addr <= _th_blink_i_1;
      end 
      _myram_cond_0_1 <= th_blink == 3;
      _myram_cond_1_1 <= th_blink == 3;
      if(th_blink == 7) begin
        myram_0_addr <= _th_blink_i_1;
        myram_0_wdata <= _th_blink_wdata_3;
        myram_0_wenable <= 1;
      end 
      _myram_cond_2_1 <= th_blink == 7;
      if(th_blink == 13) begin
        myram_0_addr <= _th_blink_i_1;
      end 
      _myram_cond_3_1 <= th_blink == 13;
      _myram_cond_4_1 <= th_blink == 13;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_times_0 <= 0;
      _th_blink_i_1 <= 0;
      _tmp_1 <= 0;
      _th_blink_rdata_2 <= 0;
      _th_blink_wdata_3 <= 0;
      _th_blink_sum_4 <= 0;
      _tmp_3 <= 0;
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
            th_blink <= th_blink_10;
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
          _th_blink_rdata_2 <= _tmp_1;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          $display("rdata = %d", _th_blink_rdata_2);
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_wdata_3 <= _th_blink_rdata_2 + 1;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          $display("wdata = %d", _th_blink_wdata_3);
          th_blink <= th_blink_9;
        end
        th_blink_9: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_2;
        end
        th_blink_10: begin
          _th_blink_sum_4 <= 0;
          th_blink <= th_blink_11;
        end
        th_blink_11: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          if(_th_blink_i_1 < _th_blink_times_0) begin
            th_blink <= th_blink_13;
          end else begin
            th_blink <= th_blink_18;
          end
        end
        th_blink_13: begin
          if(_tmp_2) begin
            _tmp_3 <= myram_0_rdata;
          end 
          if(_tmp_2) begin
            th_blink <= th_blink_14;
          end 
        end
        th_blink_14: begin
          _th_blink_rdata_2 <= _tmp_3;
          th_blink <= th_blink_15;
        end
        th_blink_15: begin
          _th_blink_sum_4 <= _th_blink_sum_4 + _th_blink_rdata_2;
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          $display("rdata = %d", _th_blink_rdata_2);
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_12;
        end
        th_blink_18: begin
          $display("sum = %d", _th_blink_sum_4);
          th_blink <= th_blink_19;
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
    mem[0] = 32'ha;
    mem[1] = 32'hb;
    mem[2] = 32'hc;
    mem[3] = 32'hd;
    mem[4] = 32'he;
    mem[5] = 32'hf;
    mem[6] = 32'h10;
    mem[7] = 32'h11;
    mem[8] = 32'h12;
    mem[9] = 32'h13;
    mem[10] = 32'h14;
    mem[11] = 32'h15;
    mem[12] = 32'h16;
    mem[13] = 32'h17;
    mem[14] = 32'h18;
    mem[15] = 32'h19;
    mem[16] = 32'h1a;
    mem[17] = 32'h1b;
    mem[18] = 32'h1c;
    mem[19] = 32'h1d;
    mem[20] = 32'h1e;
    mem[21] = 32'h1f;
    mem[22] = 32'h20;
    mem[23] = 32'h21;
    mem[24] = 32'h22;
    mem[25] = 32'h23;
    mem[26] = 32'h24;
    mem[27] = 32'h25;
    mem[28] = 32'h26;
    mem[29] = 32'h27;
    mem[30] = 32'h28;
    mem[31] = 32'h29;
    mem[32] = 32'h2a;
    mem[33] = 32'h2b;
    mem[34] = 32'h2c;
    mem[35] = 32'h2d;
    mem[36] = 32'h2e;
    mem[37] = 32'h2f;
    mem[38] = 32'h30;
    mem[39] = 32'h31;
    mem[40] = 32'h32;
    mem[41] = 32'h33;
    mem[42] = 32'h34;
    mem[43] = 32'h35;
    mem[44] = 32'h36;
    mem[45] = 32'h37;
    mem[46] = 32'h38;
    mem[47] = 32'h39;
    mem[48] = 32'h3a;
    mem[49] = 32'h3b;
    mem[50] = 32'h3c;
    mem[51] = 32'h3d;
    mem[52] = 32'h3e;
    mem[53] = 32'h3f;
    mem[54] = 32'h40;
    mem[55] = 32'h41;
    mem[56] = 32'h42;
    mem[57] = 32'h43;
    mem[58] = 32'h44;
    mem[59] = 32'h45;
    mem[60] = 32'h46;
    mem[61] = 32'h47;
    mem[62] = 32'h48;
    mem[63] = 32'h49;
    mem[64] = 32'h4a;
    mem[65] = 32'h4b;
    mem[66] = 32'h4c;
    mem[67] = 32'h4d;
    mem[68] = 32'h4e;
    mem[69] = 32'h4f;
    mem[70] = 32'h50;
    mem[71] = 32'h51;
    mem[72] = 32'h52;
    mem[73] = 32'h53;
    mem[74] = 32'h54;
    mem[75] = 32'h55;
    mem[76] = 32'h56;
    mem[77] = 32'h57;
    mem[78] = 32'h58;
    mem[79] = 32'h59;
    mem[80] = 32'h5a;
    mem[81] = 32'h5b;
    mem[82] = 32'h5c;
    mem[83] = 32'h5d;
    mem[84] = 32'h5e;
    mem[85] = 32'h5f;
    mem[86] = 32'h60;
    mem[87] = 32'h61;
    mem[88] = 32'h62;
    mem[89] = 32'h63;
    mem[90] = 32'h64;
    mem[91] = 32'h65;
    mem[92] = 32'h66;
    mem[93] = 32'h67;
    mem[94] = 32'h68;
    mem[95] = 32'h69;
    mem[96] = 32'h6a;
    mem[97] = 32'h6b;
    mem[98] = 32'h6c;
    mem[99] = 32'h6d;
    mem[100] = 32'h6e;
    mem[101] = 32'h6f;
    mem[102] = 32'h70;
    mem[103] = 32'h71;
    mem[104] = 32'h72;
    mem[105] = 32'h73;
    mem[106] = 32'h74;
    mem[107] = 32'h75;
    mem[108] = 32'h76;
    mem[109] = 32'h77;
    mem[110] = 32'h78;
    mem[111] = 32'h79;
    mem[112] = 32'h7a;
    mem[113] = 32'h7b;
    mem[114] = 32'h7c;
    mem[115] = 32'h7d;
    mem[116] = 32'h7e;
    mem[117] = 32'h7f;
    mem[118] = 32'h80;
    mem[119] = 32'h81;
    mem[120] = 32'h82;
    mem[121] = 32'h83;
    mem[122] = 32'h84;
    mem[123] = 32'h85;
    mem[124] = 32'h86;
    mem[125] = 32'h87;
    mem[126] = 32'h88;
    mem[127] = 32'h89;
    mem[128] = 32'h8a;
    mem[129] = 32'h8b;
    mem[130] = 32'h8c;
    mem[131] = 32'h8d;
    mem[132] = 32'h8e;
    mem[133] = 32'h8f;
    mem[134] = 32'h90;
    mem[135] = 32'h91;
    mem[136] = 32'h92;
    mem[137] = 32'h93;
    mem[138] = 32'h94;
    mem[139] = 32'h95;
    mem[140] = 32'h96;
    mem[141] = 32'h97;
    mem[142] = 32'h98;
    mem[143] = 32'h99;
    mem[144] = 32'h9a;
    mem[145] = 32'h9b;
    mem[146] = 32'h9c;
    mem[147] = 32'h9d;
    mem[148] = 32'h9e;
    mem[149] = 32'h9f;
    mem[150] = 32'ha0;
    mem[151] = 32'ha1;
    mem[152] = 32'ha2;
    mem[153] = 32'ha3;
    mem[154] = 32'ha4;
    mem[155] = 32'ha5;
    mem[156] = 32'ha6;
    mem[157] = 32'ha7;
    mem[158] = 32'ha8;
    mem[159] = 32'ha9;
    mem[160] = 32'haa;
    mem[161] = 32'hab;
    mem[162] = 32'hac;
    mem[163] = 32'had;
    mem[164] = 32'hae;
    mem[165] = 32'haf;
    mem[166] = 32'hb0;
    mem[167] = 32'hb1;
    mem[168] = 32'hb2;
    mem[169] = 32'hb3;
    mem[170] = 32'hb4;
    mem[171] = 32'hb5;
    mem[172] = 32'hb6;
    mem[173] = 32'hb7;
    mem[174] = 32'hb8;
    mem[175] = 32'hb9;
    mem[176] = 32'hba;
    mem[177] = 32'hbb;
    mem[178] = 32'hbc;
    mem[179] = 32'hbd;
    mem[180] = 32'hbe;
    mem[181] = 32'hbf;
    mem[182] = 32'hc0;
    mem[183] = 32'hc1;
    mem[184] = 32'hc2;
    mem[185] = 32'hc3;
    mem[186] = 32'hc4;
    mem[187] = 32'hc5;
    mem[188] = 32'hc6;
    mem[189] = 32'hc7;
    mem[190] = 32'hc8;
    mem[191] = 32'hc9;
    mem[192] = 32'hca;
    mem[193] = 32'hcb;
    mem[194] = 32'hcc;
    mem[195] = 32'hcd;
    mem[196] = 32'hce;
    mem[197] = 32'hcf;
    mem[198] = 32'hd0;
    mem[199] = 32'hd1;
    mem[200] = 32'hd2;
    mem[201] = 32'hd3;
    mem[202] = 32'hd4;
    mem[203] = 32'hd5;
    mem[204] = 32'hd6;
    mem[205] = 32'hd7;
    mem[206] = 32'hd8;
    mem[207] = 32'hd9;
    mem[208] = 32'hda;
    mem[209] = 32'hdb;
    mem[210] = 32'hdc;
    mem[211] = 32'hdd;
    mem[212] = 32'hde;
    mem[213] = 32'hdf;
    mem[214] = 32'he0;
    mem[215] = 32'he1;
    mem[216] = 32'he2;
    mem[217] = 32'he3;
    mem[218] = 32'he4;
    mem[219] = 32'he5;
    mem[220] = 32'he6;
    mem[221] = 32'he7;
    mem[222] = 32'he8;
    mem[223] = 32'he9;
    mem[224] = 32'hea;
    mem[225] = 32'heb;
    mem[226] = 32'hec;
    mem[227] = 32'hed;
    mem[228] = 32'hee;
    mem[229] = 32'hef;
    mem[230] = 32'hf0;
    mem[231] = 32'hf1;
    mem[232] = 32'hf2;
    mem[233] = 32'hf3;
    mem[234] = 32'hf4;
    mem[235] = 32'hf5;
    mem[236] = 32'hf6;
    mem[237] = 32'hf7;
    mem[238] = 32'hf8;
    mem[239] = 32'hf9;
    mem[240] = 32'hfa;
    mem[241] = 32'hfb;
    mem[242] = 32'hfc;
    mem[243] = 32'hfd;
    mem[244] = 32'hfe;
    mem[245] = 32'hff;
    mem[246] = 32'h100;
    mem[247] = 32'h101;
    mem[248] = 32'h102;
    mem[249] = 32'h103;
    mem[250] = 32'h104;
    mem[251] = 32'h105;
    mem[252] = 32'h106;
    mem[253] = 32'h107;
    mem[254] = 32'h108;
    mem[255] = 32'h109;
    mem[256] = 32'h10a;
    mem[257] = 32'h10b;
    mem[258] = 32'h10c;
    mem[259] = 32'h10d;
    mem[260] = 32'h10e;
    mem[261] = 32'h10f;
    mem[262] = 32'h110;
    mem[263] = 32'h111;
    mem[264] = 32'h112;
    mem[265] = 32'h113;
    mem[266] = 32'h114;
    mem[267] = 32'h115;
    mem[268] = 32'h116;
    mem[269] = 32'h117;
    mem[270] = 32'h118;
    mem[271] = 32'h119;
    mem[272] = 32'h11a;
    mem[273] = 32'h11b;
    mem[274] = 32'h11c;
    mem[275] = 32'h11d;
    mem[276] = 32'h11e;
    mem[277] = 32'h11f;
    mem[278] = 32'h120;
    mem[279] = 32'h121;
    mem[280] = 32'h122;
    mem[281] = 32'h123;
    mem[282] = 32'h124;
    mem[283] = 32'h125;
    mem[284] = 32'h126;
    mem[285] = 32'h127;
    mem[286] = 32'h128;
    mem[287] = 32'h129;
    mem[288] = 32'h12a;
    mem[289] = 32'h12b;
    mem[290] = 32'h12c;
    mem[291] = 32'h12d;
    mem[292] = 32'h12e;
    mem[293] = 32'h12f;
    mem[294] = 32'h130;
    mem[295] = 32'h131;
    mem[296] = 32'h132;
    mem[297] = 32'h133;
    mem[298] = 32'h134;
    mem[299] = 32'h135;
    mem[300] = 32'h136;
    mem[301] = 32'h137;
    mem[302] = 32'h138;
    mem[303] = 32'h139;
    mem[304] = 32'h13a;
    mem[305] = 32'h13b;
    mem[306] = 32'h13c;
    mem[307] = 32'h13d;
    mem[308] = 32'h13e;
    mem[309] = 32'h13f;
    mem[310] = 32'h140;
    mem[311] = 32'h141;
    mem[312] = 32'h142;
    mem[313] = 32'h143;
    mem[314] = 32'h144;
    mem[315] = 32'h145;
    mem[316] = 32'h146;
    mem[317] = 32'h147;
    mem[318] = 32'h148;
    mem[319] = 32'h149;
    mem[320] = 32'h14a;
    mem[321] = 32'h14b;
    mem[322] = 32'h14c;
    mem[323] = 32'h14d;
    mem[324] = 32'h14e;
    mem[325] = 32'h14f;
    mem[326] = 32'h150;
    mem[327] = 32'h151;
    mem[328] = 32'h152;
    mem[329] = 32'h153;
    mem[330] = 32'h154;
    mem[331] = 32'h155;
    mem[332] = 32'h156;
    mem[333] = 32'h157;
    mem[334] = 32'h158;
    mem[335] = 32'h159;
    mem[336] = 32'h15a;
    mem[337] = 32'h15b;
    mem[338] = 32'h15c;
    mem[339] = 32'h15d;
    mem[340] = 32'h15e;
    mem[341] = 32'h15f;
    mem[342] = 32'h160;
    mem[343] = 32'h161;
    mem[344] = 32'h162;
    mem[345] = 32'h163;
    mem[346] = 32'h164;
    mem[347] = 32'h165;
    mem[348] = 32'h166;
    mem[349] = 32'h167;
    mem[350] = 32'h168;
    mem[351] = 32'h169;
    mem[352] = 32'h16a;
    mem[353] = 32'h16b;
    mem[354] = 32'h16c;
    mem[355] = 32'h16d;
    mem[356] = 32'h16e;
    mem[357] = 32'h16f;
    mem[358] = 32'h170;
    mem[359] = 32'h171;
    mem[360] = 32'h172;
    mem[361] = 32'h173;
    mem[362] = 32'h174;
    mem[363] = 32'h175;
    mem[364] = 32'h176;
    mem[365] = 32'h177;
    mem[366] = 32'h178;
    mem[367] = 32'h179;
    mem[368] = 32'h17a;
    mem[369] = 32'h17b;
    mem[370] = 32'h17c;
    mem[371] = 32'h17d;
    mem[372] = 32'h17e;
    mem[373] = 32'h17f;
    mem[374] = 32'h180;
    mem[375] = 32'h181;
    mem[376] = 32'h182;
    mem[377] = 32'h183;
    mem[378] = 32'h184;
    mem[379] = 32'h185;
    mem[380] = 32'h186;
    mem[381] = 32'h187;
    mem[382] = 32'h188;
    mem[383] = 32'h189;
    mem[384] = 32'h18a;
    mem[385] = 32'h18b;
    mem[386] = 32'h18c;
    mem[387] = 32'h18d;
    mem[388] = 32'h18e;
    mem[389] = 32'h18f;
    mem[390] = 32'h190;
    mem[391] = 32'h191;
    mem[392] = 32'h192;
    mem[393] = 32'h193;
    mem[394] = 32'h194;
    mem[395] = 32'h195;
    mem[396] = 32'h196;
    mem[397] = 32'h197;
    mem[398] = 32'h198;
    mem[399] = 32'h199;
    mem[400] = 32'h19a;
    mem[401] = 32'h19b;
    mem[402] = 32'h19c;
    mem[403] = 32'h19d;
    mem[404] = 32'h19e;
    mem[405] = 32'h19f;
    mem[406] = 32'h1a0;
    mem[407] = 32'h1a1;
    mem[408] = 32'h1a2;
    mem[409] = 32'h1a3;
    mem[410] = 32'h1a4;
    mem[411] = 32'h1a5;
    mem[412] = 32'h1a6;
    mem[413] = 32'h1a7;
    mem[414] = 32'h1a8;
    mem[415] = 32'h1a9;
    mem[416] = 32'h1aa;
    mem[417] = 32'h1ab;
    mem[418] = 32'h1ac;
    mem[419] = 32'h1ad;
    mem[420] = 32'h1ae;
    mem[421] = 32'h1af;
    mem[422] = 32'h1b0;
    mem[423] = 32'h1b1;
    mem[424] = 32'h1b2;
    mem[425] = 32'h1b3;
    mem[426] = 32'h1b4;
    mem[427] = 32'h1b5;
    mem[428] = 32'h1b6;
    mem[429] = 32'h1b7;
    mem[430] = 32'h1b8;
    mem[431] = 32'h1b9;
    mem[432] = 32'h1ba;
    mem[433] = 32'h1bb;
    mem[434] = 32'h1bc;
    mem[435] = 32'h1bd;
    mem[436] = 32'h1be;
    mem[437] = 32'h1bf;
    mem[438] = 32'h1c0;
    mem[439] = 32'h1c1;
    mem[440] = 32'h1c2;
    mem[441] = 32'h1c3;
    mem[442] = 32'h1c4;
    mem[443] = 32'h1c5;
    mem[444] = 32'h1c6;
    mem[445] = 32'h1c7;
    mem[446] = 32'h1c8;
    mem[447] = 32'h1c9;
    mem[448] = 32'h1ca;
    mem[449] = 32'h1cb;
    mem[450] = 32'h1cc;
    mem[451] = 32'h1cd;
    mem[452] = 32'h1ce;
    mem[453] = 32'h1cf;
    mem[454] = 32'h1d0;
    mem[455] = 32'h1d1;
    mem[456] = 32'h1d2;
    mem[457] = 32'h1d3;
    mem[458] = 32'h1d4;
    mem[459] = 32'h1d5;
    mem[460] = 32'h1d6;
    mem[461] = 32'h1d7;
    mem[462] = 32'h1d8;
    mem[463] = 32'h1d9;
    mem[464] = 32'h1da;
    mem[465] = 32'h1db;
    mem[466] = 32'h1dc;
    mem[467] = 32'h1dd;
    mem[468] = 32'h1de;
    mem[469] = 32'h1df;
    mem[470] = 32'h1e0;
    mem[471] = 32'h1e1;
    mem[472] = 32'h1e2;
    mem[473] = 32'h1e3;
    mem[474] = 32'h1e4;
    mem[475] = 32'h1e5;
    mem[476] = 32'h1e6;
    mem[477] = 32'h1e7;
    mem[478] = 32'h1e8;
    mem[479] = 32'h1e9;
    mem[480] = 32'h1ea;
    mem[481] = 32'h1eb;
    mem[482] = 32'h1ec;
    mem[483] = 32'h1ed;
    mem[484] = 32'h1ee;
    mem[485] = 32'h1ef;
    mem[486] = 32'h1f0;
    mem[487] = 32'h1f1;
    mem[488] = 32'h1f2;
    mem[489] = 32'h1f3;
    mem[490] = 32'h1f4;
    mem[491] = 32'h1f5;
    mem[492] = 32'h1f6;
    mem[493] = 32'h1f7;
    mem[494] = 32'h1f8;
    mem[495] = 32'h1f9;
    mem[496] = 32'h1fa;
    mem[497] = 32'h1fb;
    mem[498] = 32'h1fc;
    mem[499] = 32'h1fd;
    mem[500] = 32'h1fe;
    mem[501] = 32'h1ff;
    mem[502] = 32'h200;
    mem[503] = 32'h201;
    mem[504] = 32'h202;
    mem[505] = 32'h203;
    mem[506] = 32'h204;
    mem[507] = 32'h205;
    mem[508] = 32'h206;
    mem[509] = 32'h207;
    mem[510] = 32'h208;
    mem[511] = 32'h209;
    mem[512] = 32'h20a;
    mem[513] = 32'h20b;
    mem[514] = 32'h20c;
    mem[515] = 32'h20d;
    mem[516] = 32'h20e;
    mem[517] = 32'h20f;
    mem[518] = 32'h210;
    mem[519] = 32'h211;
    mem[520] = 32'h212;
    mem[521] = 32'h213;
    mem[522] = 32'h214;
    mem[523] = 32'h215;
    mem[524] = 32'h216;
    mem[525] = 32'h217;
    mem[526] = 32'h218;
    mem[527] = 32'h219;
    mem[528] = 32'h21a;
    mem[529] = 32'h21b;
    mem[530] = 32'h21c;
    mem[531] = 32'h21d;
    mem[532] = 32'h21e;
    mem[533] = 32'h21f;
    mem[534] = 32'h220;
    mem[535] = 32'h221;
    mem[536] = 32'h222;
    mem[537] = 32'h223;
    mem[538] = 32'h224;
    mem[539] = 32'h225;
    mem[540] = 32'h226;
    mem[541] = 32'h227;
    mem[542] = 32'h228;
    mem[543] = 32'h229;
    mem[544] = 32'h22a;
    mem[545] = 32'h22b;
    mem[546] = 32'h22c;
    mem[547] = 32'h22d;
    mem[548] = 32'h22e;
    mem[549] = 32'h22f;
    mem[550] = 32'h230;
    mem[551] = 32'h231;
    mem[552] = 32'h232;
    mem[553] = 32'h233;
    mem[554] = 32'h234;
    mem[555] = 32'h235;
    mem[556] = 32'h236;
    mem[557] = 32'h237;
    mem[558] = 32'h238;
    mem[559] = 32'h239;
    mem[560] = 32'h23a;
    mem[561] = 32'h23b;
    mem[562] = 32'h23c;
    mem[563] = 32'h23d;
    mem[564] = 32'h23e;
    mem[565] = 32'h23f;
    mem[566] = 32'h240;
    mem[567] = 32'h241;
    mem[568] = 32'h242;
    mem[569] = 32'h243;
    mem[570] = 32'h244;
    mem[571] = 32'h245;
    mem[572] = 32'h246;
    mem[573] = 32'h247;
    mem[574] = 32'h248;
    mem[575] = 32'h249;
    mem[576] = 32'h24a;
    mem[577] = 32'h24b;
    mem[578] = 32'h24c;
    mem[579] = 32'h24d;
    mem[580] = 32'h24e;
    mem[581] = 32'h24f;
    mem[582] = 32'h250;
    mem[583] = 32'h251;
    mem[584] = 32'h252;
    mem[585] = 32'h253;
    mem[586] = 32'h254;
    mem[587] = 32'h255;
    mem[588] = 32'h256;
    mem[589] = 32'h257;
    mem[590] = 32'h258;
    mem[591] = 32'h259;
    mem[592] = 32'h25a;
    mem[593] = 32'h25b;
    mem[594] = 32'h25c;
    mem[595] = 32'h25d;
    mem[596] = 32'h25e;
    mem[597] = 32'h25f;
    mem[598] = 32'h260;
    mem[599] = 32'h261;
    mem[600] = 32'h262;
    mem[601] = 32'h263;
    mem[602] = 32'h264;
    mem[603] = 32'h265;
    mem[604] = 32'h266;
    mem[605] = 32'h267;
    mem[606] = 32'h268;
    mem[607] = 32'h269;
    mem[608] = 32'h26a;
    mem[609] = 32'h26b;
    mem[610] = 32'h26c;
    mem[611] = 32'h26d;
    mem[612] = 32'h26e;
    mem[613] = 32'h26f;
    mem[614] = 32'h270;
    mem[615] = 32'h271;
    mem[616] = 32'h272;
    mem[617] = 32'h273;
    mem[618] = 32'h274;
    mem[619] = 32'h275;
    mem[620] = 32'h276;
    mem[621] = 32'h277;
    mem[622] = 32'h278;
    mem[623] = 32'h279;
    mem[624] = 32'h27a;
    mem[625] = 32'h27b;
    mem[626] = 32'h27c;
    mem[627] = 32'h27d;
    mem[628] = 32'h27e;
    mem[629] = 32'h27f;
    mem[630] = 32'h280;
    mem[631] = 32'h281;
    mem[632] = 32'h282;
    mem[633] = 32'h283;
    mem[634] = 32'h284;
    mem[635] = 32'h285;
    mem[636] = 32'h286;
    mem[637] = 32'h287;
    mem[638] = 32'h288;
    mem[639] = 32'h289;
    mem[640] = 32'h28a;
    mem[641] = 32'h28b;
    mem[642] = 32'h28c;
    mem[643] = 32'h28d;
    mem[644] = 32'h28e;
    mem[645] = 32'h28f;
    mem[646] = 32'h290;
    mem[647] = 32'h291;
    mem[648] = 32'h292;
    mem[649] = 32'h293;
    mem[650] = 32'h294;
    mem[651] = 32'h295;
    mem[652] = 32'h296;
    mem[653] = 32'h297;
    mem[654] = 32'h298;
    mem[655] = 32'h299;
    mem[656] = 32'h29a;
    mem[657] = 32'h29b;
    mem[658] = 32'h29c;
    mem[659] = 32'h29d;
    mem[660] = 32'h29e;
    mem[661] = 32'h29f;
    mem[662] = 32'h2a0;
    mem[663] = 32'h2a1;
    mem[664] = 32'h2a2;
    mem[665] = 32'h2a3;
    mem[666] = 32'h2a4;
    mem[667] = 32'h2a5;
    mem[668] = 32'h2a6;
    mem[669] = 32'h2a7;
    mem[670] = 32'h2a8;
    mem[671] = 32'h2a9;
    mem[672] = 32'h2aa;
    mem[673] = 32'h2ab;
    mem[674] = 32'h2ac;
    mem[675] = 32'h2ad;
    mem[676] = 32'h2ae;
    mem[677] = 32'h2af;
    mem[678] = 32'h2b0;
    mem[679] = 32'h2b1;
    mem[680] = 32'h2b2;
    mem[681] = 32'h2b3;
    mem[682] = 32'h2b4;
    mem[683] = 32'h2b5;
    mem[684] = 32'h2b6;
    mem[685] = 32'h2b7;
    mem[686] = 32'h2b8;
    mem[687] = 32'h2b9;
    mem[688] = 32'h2ba;
    mem[689] = 32'h2bb;
    mem[690] = 32'h2bc;
    mem[691] = 32'h2bd;
    mem[692] = 32'h2be;
    mem[693] = 32'h2bf;
    mem[694] = 32'h2c0;
    mem[695] = 32'h2c1;
    mem[696] = 32'h2c2;
    mem[697] = 32'h2c3;
    mem[698] = 32'h2c4;
    mem[699] = 32'h2c5;
    mem[700] = 32'h2c6;
    mem[701] = 32'h2c7;
    mem[702] = 32'h2c8;
    mem[703] = 32'h2c9;
    mem[704] = 32'h2ca;
    mem[705] = 32'h2cb;
    mem[706] = 32'h2cc;
    mem[707] = 32'h2cd;
    mem[708] = 32'h2ce;
    mem[709] = 32'h2cf;
    mem[710] = 32'h2d0;
    mem[711] = 32'h2d1;
    mem[712] = 32'h2d2;
    mem[713] = 32'h2d3;
    mem[714] = 32'h2d4;
    mem[715] = 32'h2d5;
    mem[716] = 32'h2d6;
    mem[717] = 32'h2d7;
    mem[718] = 32'h2d8;
    mem[719] = 32'h2d9;
    mem[720] = 32'h2da;
    mem[721] = 32'h2db;
    mem[722] = 32'h2dc;
    mem[723] = 32'h2dd;
    mem[724] = 32'h2de;
    mem[725] = 32'h2df;
    mem[726] = 32'h2e0;
    mem[727] = 32'h2e1;
    mem[728] = 32'h2e2;
    mem[729] = 32'h2e3;
    mem[730] = 32'h2e4;
    mem[731] = 32'h2e5;
    mem[732] = 32'h2e6;
    mem[733] = 32'h2e7;
    mem[734] = 32'h2e8;
    mem[735] = 32'h2e9;
    mem[736] = 32'h2ea;
    mem[737] = 32'h2eb;
    mem[738] = 32'h2ec;
    mem[739] = 32'h2ed;
    mem[740] = 32'h2ee;
    mem[741] = 32'h2ef;
    mem[742] = 32'h2f0;
    mem[743] = 32'h2f1;
    mem[744] = 32'h2f2;
    mem[745] = 32'h2f3;
    mem[746] = 32'h2f4;
    mem[747] = 32'h2f5;
    mem[748] = 32'h2f6;
    mem[749] = 32'h2f7;
    mem[750] = 32'h2f8;
    mem[751] = 32'h2f9;
    mem[752] = 32'h2fa;
    mem[753] = 32'h2fb;
    mem[754] = 32'h2fc;
    mem[755] = 32'h2fd;
    mem[756] = 32'h2fe;
    mem[757] = 32'h2ff;
    mem[758] = 32'h300;
    mem[759] = 32'h301;
    mem[760] = 32'h302;
    mem[761] = 32'h303;
    mem[762] = 32'h304;
    mem[763] = 32'h305;
    mem[764] = 32'h306;
    mem[765] = 32'h307;
    mem[766] = 32'h308;
    mem[767] = 32'h309;
    mem[768] = 32'h30a;
    mem[769] = 32'h30b;
    mem[770] = 32'h30c;
    mem[771] = 32'h30d;
    mem[772] = 32'h30e;
    mem[773] = 32'h30f;
    mem[774] = 32'h310;
    mem[775] = 32'h311;
    mem[776] = 32'h312;
    mem[777] = 32'h313;
    mem[778] = 32'h314;
    mem[779] = 32'h315;
    mem[780] = 32'h316;
    mem[781] = 32'h317;
    mem[782] = 32'h318;
    mem[783] = 32'h319;
    mem[784] = 32'h31a;
    mem[785] = 32'h31b;
    mem[786] = 32'h31c;
    mem[787] = 32'h31d;
    mem[788] = 32'h31e;
    mem[789] = 32'h31f;
    mem[790] = 32'h320;
    mem[791] = 32'h321;
    mem[792] = 32'h322;
    mem[793] = 32'h323;
    mem[794] = 32'h324;
    mem[795] = 32'h325;
    mem[796] = 32'h326;
    mem[797] = 32'h327;
    mem[798] = 32'h328;
    mem[799] = 32'h329;
    mem[800] = 32'h32a;
    mem[801] = 32'h32b;
    mem[802] = 32'h32c;
    mem[803] = 32'h32d;
    mem[804] = 32'h32e;
    mem[805] = 32'h32f;
    mem[806] = 32'h330;
    mem[807] = 32'h331;
    mem[808] = 32'h332;
    mem[809] = 32'h333;
    mem[810] = 32'h334;
    mem[811] = 32'h335;
    mem[812] = 32'h336;
    mem[813] = 32'h337;
    mem[814] = 32'h338;
    mem[815] = 32'h339;
    mem[816] = 32'h33a;
    mem[817] = 32'h33b;
    mem[818] = 32'h33c;
    mem[819] = 32'h33d;
    mem[820] = 32'h33e;
    mem[821] = 32'h33f;
    mem[822] = 32'h340;
    mem[823] = 32'h341;
    mem[824] = 32'h342;
    mem[825] = 32'h343;
    mem[826] = 32'h344;
    mem[827] = 32'h345;
    mem[828] = 32'h346;
    mem[829] = 32'h347;
    mem[830] = 32'h348;
    mem[831] = 32'h349;
    mem[832] = 32'h34a;
    mem[833] = 32'h34b;
    mem[834] = 32'h34c;
    mem[835] = 32'h34d;
    mem[836] = 32'h34e;
    mem[837] = 32'h34f;
    mem[838] = 32'h350;
    mem[839] = 32'h351;
    mem[840] = 32'h352;
    mem[841] = 32'h353;
    mem[842] = 32'h354;
    mem[843] = 32'h355;
    mem[844] = 32'h356;
    mem[845] = 32'h357;
    mem[846] = 32'h358;
    mem[847] = 32'h359;
    mem[848] = 32'h35a;
    mem[849] = 32'h35b;
    mem[850] = 32'h35c;
    mem[851] = 32'h35d;
    mem[852] = 32'h35e;
    mem[853] = 32'h35f;
    mem[854] = 32'h360;
    mem[855] = 32'h361;
    mem[856] = 32'h362;
    mem[857] = 32'h363;
    mem[858] = 32'h364;
    mem[859] = 32'h365;
    mem[860] = 32'h366;
    mem[861] = 32'h367;
    mem[862] = 32'h368;
    mem[863] = 32'h369;
    mem[864] = 32'h36a;
    mem[865] = 32'h36b;
    mem[866] = 32'h36c;
    mem[867] = 32'h36d;
    mem[868] = 32'h36e;
    mem[869] = 32'h36f;
    mem[870] = 32'h370;
    mem[871] = 32'h371;
    mem[872] = 32'h372;
    mem[873] = 32'h373;
    mem[874] = 32'h374;
    mem[875] = 32'h375;
    mem[876] = 32'h376;
    mem[877] = 32'h377;
    mem[878] = 32'h378;
    mem[879] = 32'h379;
    mem[880] = 32'h37a;
    mem[881] = 32'h37b;
    mem[882] = 32'h37c;
    mem[883] = 32'h37d;
    mem[884] = 32'h37e;
    mem[885] = 32'h37f;
    mem[886] = 32'h380;
    mem[887] = 32'h381;
    mem[888] = 32'h382;
    mem[889] = 32'h383;
    mem[890] = 32'h384;
    mem[891] = 32'h385;
    mem[892] = 32'h386;
    mem[893] = 32'h387;
    mem[894] = 32'h388;
    mem[895] = 32'h389;
    mem[896] = 32'h38a;
    mem[897] = 32'h38b;
    mem[898] = 32'h38c;
    mem[899] = 32'h38d;
    mem[900] = 32'h38e;
    mem[901] = 32'h38f;
    mem[902] = 32'h390;
    mem[903] = 32'h391;
    mem[904] = 32'h392;
    mem[905] = 32'h393;
    mem[906] = 32'h394;
    mem[907] = 32'h395;
    mem[908] = 32'h396;
    mem[909] = 32'h397;
    mem[910] = 32'h398;
    mem[911] = 32'h399;
    mem[912] = 32'h39a;
    mem[913] = 32'h39b;
    mem[914] = 32'h39c;
    mem[915] = 32'h39d;
    mem[916] = 32'h39e;
    mem[917] = 32'h39f;
    mem[918] = 32'h3a0;
    mem[919] = 32'h3a1;
    mem[920] = 32'h3a2;
    mem[921] = 32'h3a3;
    mem[922] = 32'h3a4;
    mem[923] = 32'h3a5;
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
    test_module = thread_ram_initval.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
