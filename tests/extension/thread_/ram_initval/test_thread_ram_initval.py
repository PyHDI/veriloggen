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
    mem[0] = 10;
    mem[1] = 11;
    mem[2] = 12;
    mem[3] = 13;
    mem[4] = 14;
    mem[5] = 15;
    mem[6] = 16;
    mem[7] = 17;
    mem[8] = 18;
    mem[9] = 19;
    mem[10] = 20;
    mem[11] = 21;
    mem[12] = 22;
    mem[13] = 23;
    mem[14] = 24;
    mem[15] = 25;
    mem[16] = 26;
    mem[17] = 27;
    mem[18] = 28;
    mem[19] = 29;
    mem[20] = 30;
    mem[21] = 31;
    mem[22] = 32;
    mem[23] = 33;
    mem[24] = 34;
    mem[25] = 35;
    mem[26] = 36;
    mem[27] = 37;
    mem[28] = 38;
    mem[29] = 39;
    mem[30] = 40;
    mem[31] = 41;
    mem[32] = 42;
    mem[33] = 43;
    mem[34] = 44;
    mem[35] = 45;
    mem[36] = 46;
    mem[37] = 47;
    mem[38] = 48;
    mem[39] = 49;
    mem[40] = 50;
    mem[41] = 51;
    mem[42] = 52;
    mem[43] = 53;
    mem[44] = 54;
    mem[45] = 55;
    mem[46] = 56;
    mem[47] = 57;
    mem[48] = 58;
    mem[49] = 59;
    mem[50] = 60;
    mem[51] = 61;
    mem[52] = 62;
    mem[53] = 63;
    mem[54] = 64;
    mem[55] = 65;
    mem[56] = 66;
    mem[57] = 67;
    mem[58] = 68;
    mem[59] = 69;
    mem[60] = 70;
    mem[61] = 71;
    mem[62] = 72;
    mem[63] = 73;
    mem[64] = 74;
    mem[65] = 75;
    mem[66] = 76;
    mem[67] = 77;
    mem[68] = 78;
    mem[69] = 79;
    mem[70] = 80;
    mem[71] = 81;
    mem[72] = 82;
    mem[73] = 83;
    mem[74] = 84;
    mem[75] = 85;
    mem[76] = 86;
    mem[77] = 87;
    mem[78] = 88;
    mem[79] = 89;
    mem[80] = 90;
    mem[81] = 91;
    mem[82] = 92;
    mem[83] = 93;
    mem[84] = 94;
    mem[85] = 95;
    mem[86] = 96;
    mem[87] = 97;
    mem[88] = 98;
    mem[89] = 99;
    mem[90] = 100;
    mem[91] = 101;
    mem[92] = 102;
    mem[93] = 103;
    mem[94] = 104;
    mem[95] = 105;
    mem[96] = 106;
    mem[97] = 107;
    mem[98] = 108;
    mem[99] = 109;
    mem[100] = 110;
    mem[101] = 111;
    mem[102] = 112;
    mem[103] = 113;
    mem[104] = 114;
    mem[105] = 115;
    mem[106] = 116;
    mem[107] = 117;
    mem[108] = 118;
    mem[109] = 119;
    mem[110] = 120;
    mem[111] = 121;
    mem[112] = 122;
    mem[113] = 123;
    mem[114] = 124;
    mem[115] = 125;
    mem[116] = 126;
    mem[117] = 127;
    mem[118] = 128;
    mem[119] = 129;
    mem[120] = 130;
    mem[121] = 131;
    mem[122] = 132;
    mem[123] = 133;
    mem[124] = 134;
    mem[125] = 135;
    mem[126] = 136;
    mem[127] = 137;
    mem[128] = 138;
    mem[129] = 139;
    mem[130] = 140;
    mem[131] = 141;
    mem[132] = 142;
    mem[133] = 143;
    mem[134] = 144;
    mem[135] = 145;
    mem[136] = 146;
    mem[137] = 147;
    mem[138] = 148;
    mem[139] = 149;
    mem[140] = 150;
    mem[141] = 151;
    mem[142] = 152;
    mem[143] = 153;
    mem[144] = 154;
    mem[145] = 155;
    mem[146] = 156;
    mem[147] = 157;
    mem[148] = 158;
    mem[149] = 159;
    mem[150] = 160;
    mem[151] = 161;
    mem[152] = 162;
    mem[153] = 163;
    mem[154] = 164;
    mem[155] = 165;
    mem[156] = 166;
    mem[157] = 167;
    mem[158] = 168;
    mem[159] = 169;
    mem[160] = 170;
    mem[161] = 171;
    mem[162] = 172;
    mem[163] = 173;
    mem[164] = 174;
    mem[165] = 175;
    mem[166] = 176;
    mem[167] = 177;
    mem[168] = 178;
    mem[169] = 179;
    mem[170] = 180;
    mem[171] = 181;
    mem[172] = 182;
    mem[173] = 183;
    mem[174] = 184;
    mem[175] = 185;
    mem[176] = 186;
    mem[177] = 187;
    mem[178] = 188;
    mem[179] = 189;
    mem[180] = 190;
    mem[181] = 191;
    mem[182] = 192;
    mem[183] = 193;
    mem[184] = 194;
    mem[185] = 195;
    mem[186] = 196;
    mem[187] = 197;
    mem[188] = 198;
    mem[189] = 199;
    mem[190] = 200;
    mem[191] = 201;
    mem[192] = 202;
    mem[193] = 203;
    mem[194] = 204;
    mem[195] = 205;
    mem[196] = 206;
    mem[197] = 207;
    mem[198] = 208;
    mem[199] = 209;
    mem[200] = 210;
    mem[201] = 211;
    mem[202] = 212;
    mem[203] = 213;
    mem[204] = 214;
    mem[205] = 215;
    mem[206] = 216;
    mem[207] = 217;
    mem[208] = 218;
    mem[209] = 219;
    mem[210] = 220;
    mem[211] = 221;
    mem[212] = 222;
    mem[213] = 223;
    mem[214] = 224;
    mem[215] = 225;
    mem[216] = 226;
    mem[217] = 227;
    mem[218] = 228;
    mem[219] = 229;
    mem[220] = 230;
    mem[221] = 231;
    mem[222] = 232;
    mem[223] = 233;
    mem[224] = 234;
    mem[225] = 235;
    mem[226] = 236;
    mem[227] = 237;
    mem[228] = 238;
    mem[229] = 239;
    mem[230] = 240;
    mem[231] = 241;
    mem[232] = 242;
    mem[233] = 243;
    mem[234] = 244;
    mem[235] = 245;
    mem[236] = 246;
    mem[237] = 247;
    mem[238] = 248;
    mem[239] = 249;
    mem[240] = 250;
    mem[241] = 251;
    mem[242] = 252;
    mem[243] = 253;
    mem[244] = 254;
    mem[245] = 255;
    mem[246] = 256;
    mem[247] = 257;
    mem[248] = 258;
    mem[249] = 259;
    mem[250] = 260;
    mem[251] = 261;
    mem[252] = 262;
    mem[253] = 263;
    mem[254] = 264;
    mem[255] = 265;
    mem[256] = 266;
    mem[257] = 267;
    mem[258] = 268;
    mem[259] = 269;
    mem[260] = 270;
    mem[261] = 271;
    mem[262] = 272;
    mem[263] = 273;
    mem[264] = 274;
    mem[265] = 275;
    mem[266] = 276;
    mem[267] = 277;
    mem[268] = 278;
    mem[269] = 279;
    mem[270] = 280;
    mem[271] = 281;
    mem[272] = 282;
    mem[273] = 283;
    mem[274] = 284;
    mem[275] = 285;
    mem[276] = 286;
    mem[277] = 287;
    mem[278] = 288;
    mem[279] = 289;
    mem[280] = 290;
    mem[281] = 291;
    mem[282] = 292;
    mem[283] = 293;
    mem[284] = 294;
    mem[285] = 295;
    mem[286] = 296;
    mem[287] = 297;
    mem[288] = 298;
    mem[289] = 299;
    mem[290] = 300;
    mem[291] = 301;
    mem[292] = 302;
    mem[293] = 303;
    mem[294] = 304;
    mem[295] = 305;
    mem[296] = 306;
    mem[297] = 307;
    mem[298] = 308;
    mem[299] = 309;
    mem[300] = 310;
    mem[301] = 311;
    mem[302] = 312;
    mem[303] = 313;
    mem[304] = 314;
    mem[305] = 315;
    mem[306] = 316;
    mem[307] = 317;
    mem[308] = 318;
    mem[309] = 319;
    mem[310] = 320;
    mem[311] = 321;
    mem[312] = 322;
    mem[313] = 323;
    mem[314] = 324;
    mem[315] = 325;
    mem[316] = 326;
    mem[317] = 327;
    mem[318] = 328;
    mem[319] = 329;
    mem[320] = 330;
    mem[321] = 331;
    mem[322] = 332;
    mem[323] = 333;
    mem[324] = 334;
    mem[325] = 335;
    mem[326] = 336;
    mem[327] = 337;
    mem[328] = 338;
    mem[329] = 339;
    mem[330] = 340;
    mem[331] = 341;
    mem[332] = 342;
    mem[333] = 343;
    mem[334] = 344;
    mem[335] = 345;
    mem[336] = 346;
    mem[337] = 347;
    mem[338] = 348;
    mem[339] = 349;
    mem[340] = 350;
    mem[341] = 351;
    mem[342] = 352;
    mem[343] = 353;
    mem[344] = 354;
    mem[345] = 355;
    mem[346] = 356;
    mem[347] = 357;
    mem[348] = 358;
    mem[349] = 359;
    mem[350] = 360;
    mem[351] = 361;
    mem[352] = 362;
    mem[353] = 363;
    mem[354] = 364;
    mem[355] = 365;
    mem[356] = 366;
    mem[357] = 367;
    mem[358] = 368;
    mem[359] = 369;
    mem[360] = 370;
    mem[361] = 371;
    mem[362] = 372;
    mem[363] = 373;
    mem[364] = 374;
    mem[365] = 375;
    mem[366] = 376;
    mem[367] = 377;
    mem[368] = 378;
    mem[369] = 379;
    mem[370] = 380;
    mem[371] = 381;
    mem[372] = 382;
    mem[373] = 383;
    mem[374] = 384;
    mem[375] = 385;
    mem[376] = 386;
    mem[377] = 387;
    mem[378] = 388;
    mem[379] = 389;
    mem[380] = 390;
    mem[381] = 391;
    mem[382] = 392;
    mem[383] = 393;
    mem[384] = 394;
    mem[385] = 395;
    mem[386] = 396;
    mem[387] = 397;
    mem[388] = 398;
    mem[389] = 399;
    mem[390] = 400;
    mem[391] = 401;
    mem[392] = 402;
    mem[393] = 403;
    mem[394] = 404;
    mem[395] = 405;
    mem[396] = 406;
    mem[397] = 407;
    mem[398] = 408;
    mem[399] = 409;
    mem[400] = 410;
    mem[401] = 411;
    mem[402] = 412;
    mem[403] = 413;
    mem[404] = 414;
    mem[405] = 415;
    mem[406] = 416;
    mem[407] = 417;
    mem[408] = 418;
    mem[409] = 419;
    mem[410] = 420;
    mem[411] = 421;
    mem[412] = 422;
    mem[413] = 423;
    mem[414] = 424;
    mem[415] = 425;
    mem[416] = 426;
    mem[417] = 427;
    mem[418] = 428;
    mem[419] = 429;
    mem[420] = 430;
    mem[421] = 431;
    mem[422] = 432;
    mem[423] = 433;
    mem[424] = 434;
    mem[425] = 435;
    mem[426] = 436;
    mem[427] = 437;
    mem[428] = 438;
    mem[429] = 439;
    mem[430] = 440;
    mem[431] = 441;
    mem[432] = 442;
    mem[433] = 443;
    mem[434] = 444;
    mem[435] = 445;
    mem[436] = 446;
    mem[437] = 447;
    mem[438] = 448;
    mem[439] = 449;
    mem[440] = 450;
    mem[441] = 451;
    mem[442] = 452;
    mem[443] = 453;
    mem[444] = 454;
    mem[445] = 455;
    mem[446] = 456;
    mem[447] = 457;
    mem[448] = 458;
    mem[449] = 459;
    mem[450] = 460;
    mem[451] = 461;
    mem[452] = 462;
    mem[453] = 463;
    mem[454] = 464;
    mem[455] = 465;
    mem[456] = 466;
    mem[457] = 467;
    mem[458] = 468;
    mem[459] = 469;
    mem[460] = 470;
    mem[461] = 471;
    mem[462] = 472;
    mem[463] = 473;
    mem[464] = 474;
    mem[465] = 475;
    mem[466] = 476;
    mem[467] = 477;
    mem[468] = 478;
    mem[469] = 479;
    mem[470] = 480;
    mem[471] = 481;
    mem[472] = 482;
    mem[473] = 483;
    mem[474] = 484;
    mem[475] = 485;
    mem[476] = 486;
    mem[477] = 487;
    mem[478] = 488;
    mem[479] = 489;
    mem[480] = 490;
    mem[481] = 491;
    mem[482] = 492;
    mem[483] = 493;
    mem[484] = 494;
    mem[485] = 495;
    mem[486] = 496;
    mem[487] = 497;
    mem[488] = 498;
    mem[489] = 499;
    mem[490] = 500;
    mem[491] = 501;
    mem[492] = 502;
    mem[493] = 503;
    mem[494] = 504;
    mem[495] = 505;
    mem[496] = 506;
    mem[497] = 507;
    mem[498] = 508;
    mem[499] = 509;
    mem[500] = 510;
    mem[501] = 511;
    mem[502] = 512;
    mem[503] = 513;
    mem[504] = 514;
    mem[505] = 515;
    mem[506] = 516;
    mem[507] = 517;
    mem[508] = 518;
    mem[509] = 519;
    mem[510] = 520;
    mem[511] = 521;
    mem[512] = 522;
    mem[513] = 523;
    mem[514] = 524;
    mem[515] = 525;
    mem[516] = 526;
    mem[517] = 527;
    mem[518] = 528;
    mem[519] = 529;
    mem[520] = 530;
    mem[521] = 531;
    mem[522] = 532;
    mem[523] = 533;
    mem[524] = 534;
    mem[525] = 535;
    mem[526] = 536;
    mem[527] = 537;
    mem[528] = 538;
    mem[529] = 539;
    mem[530] = 540;
    mem[531] = 541;
    mem[532] = 542;
    mem[533] = 543;
    mem[534] = 544;
    mem[535] = 545;
    mem[536] = 546;
    mem[537] = 547;
    mem[538] = 548;
    mem[539] = 549;
    mem[540] = 550;
    mem[541] = 551;
    mem[542] = 552;
    mem[543] = 553;
    mem[544] = 554;
    mem[545] = 555;
    mem[546] = 556;
    mem[547] = 557;
    mem[548] = 558;
    mem[549] = 559;
    mem[550] = 560;
    mem[551] = 561;
    mem[552] = 562;
    mem[553] = 563;
    mem[554] = 564;
    mem[555] = 565;
    mem[556] = 566;
    mem[557] = 567;
    mem[558] = 568;
    mem[559] = 569;
    mem[560] = 570;
    mem[561] = 571;
    mem[562] = 572;
    mem[563] = 573;
    mem[564] = 574;
    mem[565] = 575;
    mem[566] = 576;
    mem[567] = 577;
    mem[568] = 578;
    mem[569] = 579;
    mem[570] = 580;
    mem[571] = 581;
    mem[572] = 582;
    mem[573] = 583;
    mem[574] = 584;
    mem[575] = 585;
    mem[576] = 586;
    mem[577] = 587;
    mem[578] = 588;
    mem[579] = 589;
    mem[580] = 590;
    mem[581] = 591;
    mem[582] = 592;
    mem[583] = 593;
    mem[584] = 594;
    mem[585] = 595;
    mem[586] = 596;
    mem[587] = 597;
    mem[588] = 598;
    mem[589] = 599;
    mem[590] = 600;
    mem[591] = 601;
    mem[592] = 602;
    mem[593] = 603;
    mem[594] = 604;
    mem[595] = 605;
    mem[596] = 606;
    mem[597] = 607;
    mem[598] = 608;
    mem[599] = 609;
    mem[600] = 610;
    mem[601] = 611;
    mem[602] = 612;
    mem[603] = 613;
    mem[604] = 614;
    mem[605] = 615;
    mem[606] = 616;
    mem[607] = 617;
    mem[608] = 618;
    mem[609] = 619;
    mem[610] = 620;
    mem[611] = 621;
    mem[612] = 622;
    mem[613] = 623;
    mem[614] = 624;
    mem[615] = 625;
    mem[616] = 626;
    mem[617] = 627;
    mem[618] = 628;
    mem[619] = 629;
    mem[620] = 630;
    mem[621] = 631;
    mem[622] = 632;
    mem[623] = 633;
    mem[624] = 634;
    mem[625] = 635;
    mem[626] = 636;
    mem[627] = 637;
    mem[628] = 638;
    mem[629] = 639;
    mem[630] = 640;
    mem[631] = 641;
    mem[632] = 642;
    mem[633] = 643;
    mem[634] = 644;
    mem[635] = 645;
    mem[636] = 646;
    mem[637] = 647;
    mem[638] = 648;
    mem[639] = 649;
    mem[640] = 650;
    mem[641] = 651;
    mem[642] = 652;
    mem[643] = 653;
    mem[644] = 654;
    mem[645] = 655;
    mem[646] = 656;
    mem[647] = 657;
    mem[648] = 658;
    mem[649] = 659;
    mem[650] = 660;
    mem[651] = 661;
    mem[652] = 662;
    mem[653] = 663;
    mem[654] = 664;
    mem[655] = 665;
    mem[656] = 666;
    mem[657] = 667;
    mem[658] = 668;
    mem[659] = 669;
    mem[660] = 670;
    mem[661] = 671;
    mem[662] = 672;
    mem[663] = 673;
    mem[664] = 674;
    mem[665] = 675;
    mem[666] = 676;
    mem[667] = 677;
    mem[668] = 678;
    mem[669] = 679;
    mem[670] = 680;
    mem[671] = 681;
    mem[672] = 682;
    mem[673] = 683;
    mem[674] = 684;
    mem[675] = 685;
    mem[676] = 686;
    mem[677] = 687;
    mem[678] = 688;
    mem[679] = 689;
    mem[680] = 690;
    mem[681] = 691;
    mem[682] = 692;
    mem[683] = 693;
    mem[684] = 694;
    mem[685] = 695;
    mem[686] = 696;
    mem[687] = 697;
    mem[688] = 698;
    mem[689] = 699;
    mem[690] = 700;
    mem[691] = 701;
    mem[692] = 702;
    mem[693] = 703;
    mem[694] = 704;
    mem[695] = 705;
    mem[696] = 706;
    mem[697] = 707;
    mem[698] = 708;
    mem[699] = 709;
    mem[700] = 710;
    mem[701] = 711;
    mem[702] = 712;
    mem[703] = 713;
    mem[704] = 714;
    mem[705] = 715;
    mem[706] = 716;
    mem[707] = 717;
    mem[708] = 718;
    mem[709] = 719;
    mem[710] = 720;
    mem[711] = 721;
    mem[712] = 722;
    mem[713] = 723;
    mem[714] = 724;
    mem[715] = 725;
    mem[716] = 726;
    mem[717] = 727;
    mem[718] = 728;
    mem[719] = 729;
    mem[720] = 730;
    mem[721] = 731;
    mem[722] = 732;
    mem[723] = 733;
    mem[724] = 734;
    mem[725] = 735;
    mem[726] = 736;
    mem[727] = 737;
    mem[728] = 738;
    mem[729] = 739;
    mem[730] = 740;
    mem[731] = 741;
    mem[732] = 742;
    mem[733] = 743;
    mem[734] = 744;
    mem[735] = 745;
    mem[736] = 746;
    mem[737] = 747;
    mem[738] = 748;
    mem[739] = 749;
    mem[740] = 750;
    mem[741] = 751;
    mem[742] = 752;
    mem[743] = 753;
    mem[744] = 754;
    mem[745] = 755;
    mem[746] = 756;
    mem[747] = 757;
    mem[748] = 758;
    mem[749] = 759;
    mem[750] = 760;
    mem[751] = 761;
    mem[752] = 762;
    mem[753] = 763;
    mem[754] = 764;
    mem[755] = 765;
    mem[756] = 766;
    mem[757] = 767;
    mem[758] = 768;
    mem[759] = 769;
    mem[760] = 770;
    mem[761] = 771;
    mem[762] = 772;
    mem[763] = 773;
    mem[764] = 774;
    mem[765] = 775;
    mem[766] = 776;
    mem[767] = 777;
    mem[768] = 778;
    mem[769] = 779;
    mem[770] = 780;
    mem[771] = 781;
    mem[772] = 782;
    mem[773] = 783;
    mem[774] = 784;
    mem[775] = 785;
    mem[776] = 786;
    mem[777] = 787;
    mem[778] = 788;
    mem[779] = 789;
    mem[780] = 790;
    mem[781] = 791;
    mem[782] = 792;
    mem[783] = 793;
    mem[784] = 794;
    mem[785] = 795;
    mem[786] = 796;
    mem[787] = 797;
    mem[788] = 798;
    mem[789] = 799;
    mem[790] = 800;
    mem[791] = 801;
    mem[792] = 802;
    mem[793] = 803;
    mem[794] = 804;
    mem[795] = 805;
    mem[796] = 806;
    mem[797] = 807;
    mem[798] = 808;
    mem[799] = 809;
    mem[800] = 810;
    mem[801] = 811;
    mem[802] = 812;
    mem[803] = 813;
    mem[804] = 814;
    mem[805] = 815;
    mem[806] = 816;
    mem[807] = 817;
    mem[808] = 818;
    mem[809] = 819;
    mem[810] = 820;
    mem[811] = 821;
    mem[812] = 822;
    mem[813] = 823;
    mem[814] = 824;
    mem[815] = 825;
    mem[816] = 826;
    mem[817] = 827;
    mem[818] = 828;
    mem[819] = 829;
    mem[820] = 830;
    mem[821] = 831;
    mem[822] = 832;
    mem[823] = 833;
    mem[824] = 834;
    mem[825] = 835;
    mem[826] = 836;
    mem[827] = 837;
    mem[828] = 838;
    mem[829] = 839;
    mem[830] = 840;
    mem[831] = 841;
    mem[832] = 842;
    mem[833] = 843;
    mem[834] = 844;
    mem[835] = 845;
    mem[836] = 846;
    mem[837] = 847;
    mem[838] = 848;
    mem[839] = 849;
    mem[840] = 850;
    mem[841] = 851;
    mem[842] = 852;
    mem[843] = 853;
    mem[844] = 854;
    mem[845] = 855;
    mem[846] = 856;
    mem[847] = 857;
    mem[848] = 858;
    mem[849] = 859;
    mem[850] = 860;
    mem[851] = 861;
    mem[852] = 862;
    mem[853] = 863;
    mem[854] = 864;
    mem[855] = 865;
    mem[856] = 866;
    mem[857] = 867;
    mem[858] = 868;
    mem[859] = 869;
    mem[860] = 870;
    mem[861] = 871;
    mem[862] = 872;
    mem[863] = 873;
    mem[864] = 874;
    mem[865] = 875;
    mem[866] = 876;
    mem[867] = 877;
    mem[868] = 878;
    mem[869] = 879;
    mem[870] = 880;
    mem[871] = 881;
    mem[872] = 882;
    mem[873] = 883;
    mem[874] = 884;
    mem[875] = 885;
    mem[876] = 886;
    mem[877] = 887;
    mem[878] = 888;
    mem[879] = 889;
    mem[880] = 890;
    mem[881] = 891;
    mem[882] = 892;
    mem[883] = 893;
    mem[884] = 894;
    mem[885] = 895;
    mem[886] = 896;
    mem[887] = 897;
    mem[888] = 898;
    mem[889] = 899;
    mem[890] = 900;
    mem[891] = 901;
    mem[892] = 902;
    mem[893] = 903;
    mem[894] = 904;
    mem[895] = 905;
    mem[896] = 906;
    mem[897] = 907;
    mem[898] = 908;
    mem[899] = 909;
    mem[900] = 910;
    mem[901] = 911;
    mem[902] = 912;
    mem[903] = 913;
    mem[904] = 914;
    mem[905] = 915;
    mem[906] = 916;
    mem[907] = 917;
    mem[908] = 918;
    mem[909] = 919;
    mem[910] = 920;
    mem[911] = 921;
    mem[912] = 922;
    mem[913] = 923;
    mem[914] = 924;
    mem[915] = 925;
    mem[916] = 926;
    mem[917] = 927;
    mem[918] = 928;
    mem[919] = 929;
    mem[920] = 930;
    mem[921] = 931;
    mem[922] = 932;
    mem[923] = 933;
    mem[924] = 934;
    mem[925] = 935;
    mem[926] = 936;
    mem[927] = 937;
    mem[928] = 938;
    mem[929] = 939;
    mem[930] = 940;
    mem[931] = 941;
    mem[932] = 942;
    mem[933] = 943;
    mem[934] = 944;
    mem[935] = 945;
    mem[936] = 946;
    mem[937] = 947;
    mem[938] = 948;
    mem[939] = 949;
    mem[940] = 950;
    mem[941] = 951;
    mem[942] = 952;
    mem[943] = 953;
    mem[944] = 954;
    mem[945] = 955;
    mem[946] = 956;
    mem[947] = 957;
    mem[948] = 958;
    mem[949] = 959;
    mem[950] = 960;
    mem[951] = 961;
    mem[952] = 962;
    mem[953] = 963;
    mem[954] = 964;
    mem[955] = 965;
    mem[956] = 966;
    mem[957] = 967;
    mem[958] = 968;
    mem[959] = 969;
    mem[960] = 970;
    mem[961] = 971;
    mem[962] = 972;
    mem[963] = 973;
    mem[964] = 974;
    mem[965] = 975;
    mem[966] = 976;
    mem[967] = 977;
    mem[968] = 978;
    mem[969] = 979;
    mem[970] = 980;
    mem[971] = 981;
    mem[972] = 982;
    mem[973] = 983;
    mem[974] = 984;
    mem[975] = 985;
    mem[976] = 986;
    mem[977] = 987;
    mem[978] = 988;
    mem[979] = 989;
    mem[980] = 990;
    mem[981] = 991;
    mem[982] = 992;
    mem[983] = 993;
    mem[984] = 994;
    mem[985] = 995;
    mem[986] = 996;
    mem[987] = 997;
    mem[988] = 998;
    mem[989] = 999;
    mem[990] = 1000;
    mem[991] = 1001;
    mem[992] = 1002;
    mem[993] = 1003;
    mem[994] = 1004;
    mem[995] = 1005;
    mem[996] = 1006;
    mem[997] = 1007;
    mem[998] = 1008;
    mem[999] = 1009;
    mem[1000] = 1010;
    mem[1001] = 1011;
    mem[1002] = 1012;
    mem[1003] = 1013;
    mem[1004] = 1014;
    mem[1005] = 1015;
    mem[1006] = 1016;
    mem[1007] = 1017;
    mem[1008] = 1018;
    mem[1009] = 1019;
    mem[1010] = 1020;
    mem[1011] = 1021;
    mem[1012] = 1022;
    mem[1013] = 1023;
    mem[1014] = 1024;
    mem[1015] = 1025;
    mem[1016] = 1026;
    mem[1017] = 1027;
    mem[1018] = 1028;
    mem[1019] = 1029;
    mem[1020] = 1030;
    mem[1021] = 1031;
    mem[1022] = 1032;
    mem[1023] = 1033;
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
