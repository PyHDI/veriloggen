from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_slave_write_lite

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] sum;
  reg [32-1:0] myaxi_awaddr;
  reg [4-1:0] myaxi_awcache;
  reg [3-1:0] myaxi_awprot;
  reg myaxi_awvalid;
  wire myaxi_awready;
  reg [32-1:0] myaxi_wdata;
  reg [4-1:0] myaxi_wstrb;
  reg myaxi_wvalid;
  wire myaxi_wready;
  wire [2-1:0] myaxi_bresp;
  wire myaxi_bvalid;
  reg myaxi_bready;
  reg [32-1:0] myaxi_araddr;
  reg [4-1:0] myaxi_arcache;
  reg [3-1:0] myaxi_arprot;
  reg myaxi_arvalid;
  wire myaxi_arready;
  wire [32-1:0] myaxi_rdata;
  wire [2-1:0] myaxi_rresp;
  wire myaxi_rvalid;
  reg myaxi_rready;
  reg [32-1:0] _axi_awaddr;
  wire [4-1:0] _axi_awcache;
  wire [3-1:0] _axi_awprot;
  reg _axi_awvalid;
  wire _axi_awready;
  reg [32-1:0] _axi_wdata;
  reg [4-1:0] _axi_wstrb;
  reg _axi_wvalid;
  wire _axi_wready;
  wire [2-1:0] _axi_bresp;
  wire _axi_bvalid;
  wire _axi_bready;
  reg [32-1:0] _axi_araddr;
  wire [4-1:0] _axi_arcache;
  wire [3-1:0] _axi_arprot;
  reg _axi_arvalid;
  wire _axi_arready;
  wire [32-1:0] _axi_rdata;
  wire [2-1:0] _axi_rresp;
  wire _axi_rvalid;
  wire _axi_rready;
  assign _axi_awcache = 3;
  assign _axi_awprot = 0;
  assign _axi_bready = 1;
  assign _axi_arcache = 3;
  assign _axi_arprot = 0;
  reg [3-1:0] outstanding_wcount_0;
  assign _axi_rready = 0;
  wire [32-1:0] _tmp_1;
  assign _tmp_1 = _axi_awaddr;

  always @(*) begin
    myaxi_awaddr = _tmp_1;
  end

  wire [4-1:0] _tmp_2;
  assign _tmp_2 = _axi_awcache;

  always @(*) begin
    myaxi_awcache = _tmp_2;
  end

  wire [3-1:0] _tmp_3;
  assign _tmp_3 = _axi_awprot;

  always @(*) begin
    myaxi_awprot = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = _axi_awvalid;

  always @(*) begin
    myaxi_awvalid = _tmp_4;
  end

  assign _axi_awready = myaxi_awready;
  wire [32-1:0] _tmp_5;
  assign _tmp_5 = _axi_wdata;

  always @(*) begin
    myaxi_wdata = _tmp_5;
  end

  wire [4-1:0] _tmp_6;
  assign _tmp_6 = _axi_wstrb;

  always @(*) begin
    myaxi_wstrb = _tmp_6;
  end

  wire _tmp_7;
  assign _tmp_7 = _axi_wvalid;

  always @(*) begin
    myaxi_wvalid = _tmp_7;
  end

  assign _axi_wready = myaxi_wready;
  assign _axi_bresp = myaxi_bresp;
  assign _axi_bvalid = myaxi_bvalid;
  wire _tmp_8;
  assign _tmp_8 = _axi_bready;

  always @(*) begin
    myaxi_bready = _tmp_8;
  end

  wire [32-1:0] _tmp_9;
  assign _tmp_9 = _axi_araddr;

  always @(*) begin
    myaxi_araddr = _tmp_9;
  end

  wire [4-1:0] _tmp_10;
  assign _tmp_10 = _axi_arcache;

  always @(*) begin
    myaxi_arcache = _tmp_10;
  end

  wire [3-1:0] _tmp_11;
  assign _tmp_11 = _axi_arprot;

  always @(*) begin
    myaxi_arprot = _tmp_11;
  end

  wire _tmp_12;
  assign _tmp_12 = _axi_arvalid;

  always @(*) begin
    myaxi_arvalid = _tmp_12;
  end

  assign _axi_arready = myaxi_arready;
  assign _axi_rdata = myaxi_rdata;
  assign _axi_rresp = myaxi_rresp;
  assign _axi_rvalid = myaxi_rvalid;
  wire _tmp_13;
  assign _tmp_13 = _axi_rready;

  always @(*) begin
    myaxi_rready = _tmp_13;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg __axi_cond_0_1;
  reg [32-1:0] wdata;
  reg __axi_cond_1_1;
  reg __axi_cond_2_1;
  reg __axi_cond_3_1;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .sum(sum),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awcache(myaxi_awcache),
    .myaxi_awprot(myaxi_awprot),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_bresp(myaxi_bresp),
    .myaxi_bvalid(myaxi_bvalid),
    .myaxi_bready(myaxi_bready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arcache(myaxi_arcache),
    .myaxi_arprot(myaxi_arprot),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rresp(myaxi_rresp),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    _axi_awaddr = 0;
    _axi_awvalid = 0;
    _axi_wdata = 0;
    _axi_wstrb = 0;
    _axi_wvalid = 0;
    _axi_araddr = 0;
    _axi_arvalid = 0;
    outstanding_wcount_0 = 0;
    fsm = fsm_init;
    __axi_cond_0_1 = 0;
    wdata = 0;
    __axi_cond_1_1 = 0;
    __axi_cond_2_1 = 0;
    __axi_cond_3_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wcount_0 <= 0;
      _axi_araddr <= 0;
      _axi_arvalid <= 0;
      _axi_awaddr <= 0;
      _axi_awvalid <= 0;
      __axi_cond_0_1 <= 0;
      _axi_wdata <= 0;
      _axi_wvalid <= 0;
      _axi_wstrb <= 0;
      __axi_cond_1_1 <= 0;
      __axi_cond_2_1 <= 0;
      __axi_cond_3_1 <= 0;
    end else begin
      if(__axi_cond_0_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_1_1) begin
        _axi_wvalid <= 0;
      end 
      if(__axi_cond_2_1) begin
        _axi_awvalid <= 0;
      end 
      if(__axi_cond_3_1) begin
        _axi_wvalid <= 0;
      end 
      if(_axi_wvalid && _axi_wready && !(_axi_bvalid && _axi_bready) && (outstanding_wcount_0 < 7)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 + 1;
      end 
      if(!(_axi_wvalid && _axi_wready) && (_axi_bvalid && _axi_bready) && (outstanding_wcount_0 > 0)) begin
        outstanding_wcount_0 <= outstanding_wcount_0 - 1;
      end 
      _axi_araddr <= 0;
      _axi_arvalid <= 0;
      if((fsm == 100) && (_axi_awready || !_axi_awvalid)) begin
        _axi_awaddr <= 1024;
        _axi_awvalid <= 1;
      end 
      __axi_cond_0_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 101) && ((outstanding_wcount_0 < 6) && (_axi_wready || !_axi_wvalid))) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wstrb <= { 4{ 1'd1 } };
      end 
      __axi_cond_1_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
      end 
      if((fsm == 102) && (_axi_awready || !_axi_awvalid)) begin
        _axi_awaddr <= 1024;
        _axi_awvalid <= 1;
      end 
      __axi_cond_2_1 <= 1;
      if(_axi_awvalid && !_axi_awready) begin
        _axi_awvalid <= _axi_awvalid;
      end 
      if((fsm == 103) && ((outstanding_wcount_0 < 6) && (_axi_wready || !_axi_wvalid))) begin
        _axi_wdata <= wdata;
        _axi_wvalid <= 1;
        _axi_wstrb <= { 4{ 1'd1 } };
      end 
      __axi_cond_3_1 <= 1;
      if(_axi_wvalid && !_axi_wready) begin
        _axi_wvalid <= _axi_wvalid;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  localparam fsm_16 = 16;
  localparam fsm_17 = 17;
  localparam fsm_18 = 18;
  localparam fsm_19 = 19;
  localparam fsm_20 = 20;
  localparam fsm_21 = 21;
  localparam fsm_22 = 22;
  localparam fsm_23 = 23;
  localparam fsm_24 = 24;
  localparam fsm_25 = 25;
  localparam fsm_26 = 26;
  localparam fsm_27 = 27;
  localparam fsm_28 = 28;
  localparam fsm_29 = 29;
  localparam fsm_30 = 30;
  localparam fsm_31 = 31;
  localparam fsm_32 = 32;
  localparam fsm_33 = 33;
  localparam fsm_34 = 34;
  localparam fsm_35 = 35;
  localparam fsm_36 = 36;
  localparam fsm_37 = 37;
  localparam fsm_38 = 38;
  localparam fsm_39 = 39;
  localparam fsm_40 = 40;
  localparam fsm_41 = 41;
  localparam fsm_42 = 42;
  localparam fsm_43 = 43;
  localparam fsm_44 = 44;
  localparam fsm_45 = 45;
  localparam fsm_46 = 46;
  localparam fsm_47 = 47;
  localparam fsm_48 = 48;
  localparam fsm_49 = 49;
  localparam fsm_50 = 50;
  localparam fsm_51 = 51;
  localparam fsm_52 = 52;
  localparam fsm_53 = 53;
  localparam fsm_54 = 54;
  localparam fsm_55 = 55;
  localparam fsm_56 = 56;
  localparam fsm_57 = 57;
  localparam fsm_58 = 58;
  localparam fsm_59 = 59;
  localparam fsm_60 = 60;
  localparam fsm_61 = 61;
  localparam fsm_62 = 62;
  localparam fsm_63 = 63;
  localparam fsm_64 = 64;
  localparam fsm_65 = 65;
  localparam fsm_66 = 66;
  localparam fsm_67 = 67;
  localparam fsm_68 = 68;
  localparam fsm_69 = 69;
  localparam fsm_70 = 70;
  localparam fsm_71 = 71;
  localparam fsm_72 = 72;
  localparam fsm_73 = 73;
  localparam fsm_74 = 74;
  localparam fsm_75 = 75;
  localparam fsm_76 = 76;
  localparam fsm_77 = 77;
  localparam fsm_78 = 78;
  localparam fsm_79 = 79;
  localparam fsm_80 = 80;
  localparam fsm_81 = 81;
  localparam fsm_82 = 82;
  localparam fsm_83 = 83;
  localparam fsm_84 = 84;
  localparam fsm_85 = 85;
  localparam fsm_86 = 86;
  localparam fsm_87 = 87;
  localparam fsm_88 = 88;
  localparam fsm_89 = 89;
  localparam fsm_90 = 90;
  localparam fsm_91 = 91;
  localparam fsm_92 = 92;
  localparam fsm_93 = 93;
  localparam fsm_94 = 94;
  localparam fsm_95 = 95;
  localparam fsm_96 = 96;
  localparam fsm_97 = 97;
  localparam fsm_98 = 98;
  localparam fsm_99 = 99;
  localparam fsm_100 = 100;
  localparam fsm_101 = 101;
  localparam fsm_102 = 102;
  localparam fsm_103 = 103;
  localparam fsm_104 = 104;
  localparam fsm_105 = 105;
  localparam fsm_106 = 106;
  localparam fsm_107 = 107;
  localparam fsm_108 = 108;
  localparam fsm_109 = 109;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      wdata <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          fsm <= fsm_1;
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          fsm <= fsm_3;
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          fsm <= fsm_5;
        end
        fsm_5: begin
          fsm <= fsm_6;
        end
        fsm_6: begin
          fsm <= fsm_7;
        end
        fsm_7: begin
          fsm <= fsm_8;
        end
        fsm_8: begin
          fsm <= fsm_9;
        end
        fsm_9: begin
          fsm <= fsm_10;
        end
        fsm_10: begin
          fsm <= fsm_11;
        end
        fsm_11: begin
          fsm <= fsm_12;
        end
        fsm_12: begin
          fsm <= fsm_13;
        end
        fsm_13: begin
          fsm <= fsm_14;
        end
        fsm_14: begin
          fsm <= fsm_15;
        end
        fsm_15: begin
          fsm <= fsm_16;
        end
        fsm_16: begin
          fsm <= fsm_17;
        end
        fsm_17: begin
          fsm <= fsm_18;
        end
        fsm_18: begin
          fsm <= fsm_19;
        end
        fsm_19: begin
          fsm <= fsm_20;
        end
        fsm_20: begin
          fsm <= fsm_21;
        end
        fsm_21: begin
          fsm <= fsm_22;
        end
        fsm_22: begin
          fsm <= fsm_23;
        end
        fsm_23: begin
          fsm <= fsm_24;
        end
        fsm_24: begin
          fsm <= fsm_25;
        end
        fsm_25: begin
          fsm <= fsm_26;
        end
        fsm_26: begin
          fsm <= fsm_27;
        end
        fsm_27: begin
          fsm <= fsm_28;
        end
        fsm_28: begin
          fsm <= fsm_29;
        end
        fsm_29: begin
          fsm <= fsm_30;
        end
        fsm_30: begin
          fsm <= fsm_31;
        end
        fsm_31: begin
          fsm <= fsm_32;
        end
        fsm_32: begin
          fsm <= fsm_33;
        end
        fsm_33: begin
          fsm <= fsm_34;
        end
        fsm_34: begin
          fsm <= fsm_35;
        end
        fsm_35: begin
          fsm <= fsm_36;
        end
        fsm_36: begin
          fsm <= fsm_37;
        end
        fsm_37: begin
          fsm <= fsm_38;
        end
        fsm_38: begin
          fsm <= fsm_39;
        end
        fsm_39: begin
          fsm <= fsm_40;
        end
        fsm_40: begin
          fsm <= fsm_41;
        end
        fsm_41: begin
          fsm <= fsm_42;
        end
        fsm_42: begin
          fsm <= fsm_43;
        end
        fsm_43: begin
          fsm <= fsm_44;
        end
        fsm_44: begin
          fsm <= fsm_45;
        end
        fsm_45: begin
          fsm <= fsm_46;
        end
        fsm_46: begin
          fsm <= fsm_47;
        end
        fsm_47: begin
          fsm <= fsm_48;
        end
        fsm_48: begin
          fsm <= fsm_49;
        end
        fsm_49: begin
          fsm <= fsm_50;
        end
        fsm_50: begin
          fsm <= fsm_51;
        end
        fsm_51: begin
          fsm <= fsm_52;
        end
        fsm_52: begin
          fsm <= fsm_53;
        end
        fsm_53: begin
          fsm <= fsm_54;
        end
        fsm_54: begin
          fsm <= fsm_55;
        end
        fsm_55: begin
          fsm <= fsm_56;
        end
        fsm_56: begin
          fsm <= fsm_57;
        end
        fsm_57: begin
          fsm <= fsm_58;
        end
        fsm_58: begin
          fsm <= fsm_59;
        end
        fsm_59: begin
          fsm <= fsm_60;
        end
        fsm_60: begin
          fsm <= fsm_61;
        end
        fsm_61: begin
          fsm <= fsm_62;
        end
        fsm_62: begin
          fsm <= fsm_63;
        end
        fsm_63: begin
          fsm <= fsm_64;
        end
        fsm_64: begin
          fsm <= fsm_65;
        end
        fsm_65: begin
          fsm <= fsm_66;
        end
        fsm_66: begin
          fsm <= fsm_67;
        end
        fsm_67: begin
          fsm <= fsm_68;
        end
        fsm_68: begin
          fsm <= fsm_69;
        end
        fsm_69: begin
          fsm <= fsm_70;
        end
        fsm_70: begin
          fsm <= fsm_71;
        end
        fsm_71: begin
          fsm <= fsm_72;
        end
        fsm_72: begin
          fsm <= fsm_73;
        end
        fsm_73: begin
          fsm <= fsm_74;
        end
        fsm_74: begin
          fsm <= fsm_75;
        end
        fsm_75: begin
          fsm <= fsm_76;
        end
        fsm_76: begin
          fsm <= fsm_77;
        end
        fsm_77: begin
          fsm <= fsm_78;
        end
        fsm_78: begin
          fsm <= fsm_79;
        end
        fsm_79: begin
          fsm <= fsm_80;
        end
        fsm_80: begin
          fsm <= fsm_81;
        end
        fsm_81: begin
          fsm <= fsm_82;
        end
        fsm_82: begin
          fsm <= fsm_83;
        end
        fsm_83: begin
          fsm <= fsm_84;
        end
        fsm_84: begin
          fsm <= fsm_85;
        end
        fsm_85: begin
          fsm <= fsm_86;
        end
        fsm_86: begin
          fsm <= fsm_87;
        end
        fsm_87: begin
          fsm <= fsm_88;
        end
        fsm_88: begin
          fsm <= fsm_89;
        end
        fsm_89: begin
          fsm <= fsm_90;
        end
        fsm_90: begin
          fsm <= fsm_91;
        end
        fsm_91: begin
          fsm <= fsm_92;
        end
        fsm_92: begin
          fsm <= fsm_93;
        end
        fsm_93: begin
          fsm <= fsm_94;
        end
        fsm_94: begin
          fsm <= fsm_95;
        end
        fsm_95: begin
          fsm <= fsm_96;
        end
        fsm_96: begin
          fsm <= fsm_97;
        end
        fsm_97: begin
          fsm <= fsm_98;
        end
        fsm_98: begin
          fsm <= fsm_99;
        end
        fsm_99: begin
          fsm <= fsm_100;
        end
        fsm_100: begin
          if(_axi_awready || !_axi_awvalid) begin
            wdata <= 100;
          end 
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_101;
          end 
        end
        fsm_101: begin
          if((outstanding_wcount_0 < 6) && (_axi_wready || !_axi_wvalid)) begin
            fsm <= fsm_102;
          end 
        end
        fsm_102: begin
          if(_axi_awready || !_axi_awvalid) begin
            wdata <= 200;
          end 
          if(_axi_awready || !_axi_awvalid) begin
            fsm <= fsm_103;
          end 
        end
        fsm_103: begin
          if((outstanding_wcount_0 < 6) && (_axi_wready || !_axi_wvalid)) begin
            fsm <= fsm_104;
          end 
        end
        fsm_104: begin
          fsm <= fsm_105;
        end
        fsm_105: begin
          fsm <= fsm_106;
        end
        fsm_106: begin
          fsm <= fsm_107;
        end
        fsm_107: begin
          fsm <= fsm_108;
        end
        fsm_108: begin
          $display("sum=%d expected_sum=%d", sum, 300);
          fsm <= fsm_109;
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  output reg [32-1:0] sum,
  input [32-1:0] myaxi_awaddr,
  input [4-1:0] myaxi_awcache,
  input [3-1:0] myaxi_awprot,
  input myaxi_awvalid,
  output myaxi_awready,
  input [32-1:0] myaxi_wdata,
  input [4-1:0] myaxi_wstrb,
  input myaxi_wvalid,
  output myaxi_wready,
  output [2-1:0] myaxi_bresp,
  output reg myaxi_bvalid,
  input myaxi_bready,
  input [32-1:0] myaxi_araddr,
  input [4-1:0] myaxi_arcache,
  input [3-1:0] myaxi_arprot,
  input myaxi_arvalid,
  output myaxi_arready,
  output reg [32-1:0] myaxi_rdata,
  output [2-1:0] myaxi_rresp,
  output reg myaxi_rvalid,
  input myaxi_rready
);

  assign myaxi_bresp = 0;
  assign myaxi_rresp = 0;
  assign myaxi_arready = 0;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] addr_0;
  reg valid_1;
  reg prev_awvalid_2;
  assign myaxi_awready = (fsm == 0) && !valid_1 && !myaxi_bvalid && prev_awvalid_2;
  assign myaxi_wready = fsm == 1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_bvalid <= 0;
      myaxi_rvalid <= 0;
      prev_awvalid_2 <= 0;
      addr_0 <= 0;
      valid_1 <= 0;
    end else begin
      if(myaxi_bvalid && myaxi_bready) begin
        myaxi_bvalid <= 0;
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        myaxi_bvalid <= 1;
      end 
      myaxi_rvalid <= 0;
      prev_awvalid_2 <= myaxi_awvalid;
      if(myaxi_awready && myaxi_awvalid && !myaxi_bvalid) begin
        addr_0 <= myaxi_awaddr;
      end 
      valid_1 <= myaxi_awready && myaxi_awvalid && !myaxi_bvalid;
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      sum <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(valid_1) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(myaxi_wready && myaxi_wvalid) begin
            sum <= sum + myaxi_wdata;
          end 
          if(myaxi_wready && myaxi_wvalid) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_slave_write_lite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
