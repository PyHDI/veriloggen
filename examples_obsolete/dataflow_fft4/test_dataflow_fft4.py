from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_fft4

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg signed [16-1:0] din0re;
  reg signed [16-1:0] din0im;
  reg signed [16-1:0] din1re;
  reg signed [16-1:0] din1im;
  reg signed [16-1:0] din2re;
  reg signed [16-1:0] din2im;
  reg signed [16-1:0] din3re;
  reg signed [16-1:0] din3im;
  wire signed [16-1:0] dout3re;
  wire signed [16-1:0] dout3im;
  wire signed [16-1:0] dout0re;
  wire signed [16-1:0] dout0im;
  wire signed [16-1:0] dout2re;
  wire signed [16-1:0] dout2im;
  wire signed [16-1:0] dout1re;
  wire signed [16-1:0] dout1im;
  wire signed [8-1:0] _din0re;
  wire signed [8-1:0] _din0im;
  wire signed [8-1:0] _din1re;
  wire signed [8-1:0] _din1im;
  wire signed [8-1:0] _din2re;
  wire signed [8-1:0] _din2im;
  wire signed [8-1:0] _din3re;
  wire signed [8-1:0] _din3im;
  wire signed [8-1:0] _dout0re;
  wire signed [8-1:0] _dout0im;
  wire signed [8-1:0] _dout1re;
  wire signed [8-1:0] _dout1im;
  wire signed [8-1:0] _dout2re;
  wire signed [8-1:0] _dout2im;
  wire signed [8-1:0] _dout3re;
  wire signed [8-1:0] _dout3im;
  assign _din0re = din0re >>> 8;
  assign _din0im = din0im >>> 8;
  assign _din1re = din1re >>> 8;
  assign _din1im = din1im >>> 8;
  assign _din2re = din2re >>> 8;
  assign _din2im = din2im >>> 8;
  assign _din3re = din3re >>> 8;
  assign _din3im = din3im >>> 8;
  assign _dout0re = dout0re >>> 8;
  assign _dout0im = dout0im >>> 8;
  assign _dout1re = dout1re >>> 8;
  assign _dout1im = dout1im >>> 8;
  assign _dout2re = dout2re >>> 8;
  assign _dout2im = dout2im >>> 8;
  assign _dout3re = dout3re >>> 8;
  assign _dout3im = dout3im >>> 8;

  fft4
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .din0re(din0re),
    .din0im(din0im),
    .din1re(din1re),
    .din1im(din1im),
    .din2re(din2re),
    .din2im(din2im),
    .din3re(din3re),
    .din3im(din3im),
    .dout3re(dout3re),
    .dout3im(dout3im),
    .dout0re(dout0re),
    .dout0im(dout0im),
    .dout2re(dout2re),
    .dout2im(dout2im),
    .dout1re(dout1re),
    .dout1im(dout1im)
  );

  reg reset_done;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, _din0re, _din0im, _din1re, _din1im, _din2re, _din2im, _din3re, _din3im, _dout0re, _dout0im, _dout1re, _dout1im, _dout2re, _dout2im, _dout3re, _dout3im);
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
    din0re = 0;
    din0im = 0;
    din1re = 256;
    din1im = 256;
    din2re = 512;
    din2im = 512;
    din3re = 768;
    din3im = 768;
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

  reg [32-1:0] send_fsm;
  localparam send_fsm_init = 0;
  localparam send_fsm_1 = 1;
  localparam send_fsm_2 = 2;
  localparam send_fsm_3 = 3;
  localparam send_fsm_4 = 4;
  localparam send_fsm_5 = 5;
  localparam send_fsm_6 = 6;
  localparam send_fsm_7 = 7;
  localparam send_fsm_8 = 8;
  localparam send_fsm_9 = 9;
  localparam send_fsm_10 = 10;
  localparam send_fsm_11 = 11;
  localparam send_fsm_12 = 12;
  localparam send_fsm_13 = 13;
  localparam send_fsm_14 = 14;
  localparam send_fsm_15 = 15;
  localparam send_fsm_16 = 16;
  localparam send_fsm_17 = 17;
  localparam send_fsm_18 = 18;
  localparam send_fsm_19 = 19;
  localparam send_fsm_20 = 20;
  localparam send_fsm_21 = 21;
  localparam send_fsm_22 = 22;
  localparam send_fsm_23 = 23;
  localparam send_fsm_24 = 24;
  localparam send_fsm_25 = 25;
  localparam send_fsm_26 = 26;
  localparam send_fsm_27 = 27;
  localparam send_fsm_28 = 28;
  localparam send_fsm_29 = 29;
  localparam send_fsm_30 = 30;
  localparam send_fsm_31 = 31;
  localparam send_fsm_32 = 32;
  localparam send_fsm_33 = 33;
  localparam send_fsm_34 = 34;
  localparam send_fsm_35 = 35;
  localparam send_fsm_36 = 36;
  localparam send_fsm_37 = 37;
  localparam send_fsm_38 = 38;
  localparam send_fsm_39 = 39;
  localparam send_fsm_40 = 40;
  localparam send_fsm_41 = 41;
  localparam send_fsm_42 = 42;
  localparam send_fsm_43 = 43;
  localparam send_fsm_44 = 44;
  localparam send_fsm_45 = 45;
  localparam send_fsm_46 = 46;
  localparam send_fsm_47 = 47;
  localparam send_fsm_48 = 48;
  localparam send_fsm_49 = 49;
  localparam send_fsm_50 = 50;
  localparam send_fsm_51 = 51;
  localparam send_fsm_52 = 52;
  localparam send_fsm_53 = 53;
  localparam send_fsm_54 = 54;
  localparam send_fsm_55 = 55;
  localparam send_fsm_56 = 56;
  localparam send_fsm_57 = 57;
  localparam send_fsm_58 = 58;
  localparam send_fsm_59 = 59;
  localparam send_fsm_60 = 60;
  localparam send_fsm_61 = 61;
  localparam send_fsm_62 = 62;
  localparam send_fsm_63 = 63;
  localparam send_fsm_64 = 64;
  localparam send_fsm_65 = 65;
  localparam send_fsm_66 = 66;
  localparam send_fsm_67 = 67;
  localparam send_fsm_68 = 68;
  localparam send_fsm_69 = 69;
  localparam send_fsm_70 = 70;
  localparam send_fsm_71 = 71;
  localparam send_fsm_72 = 72;
  localparam send_fsm_73 = 73;
  localparam send_fsm_74 = 74;
  localparam send_fsm_75 = 75;
  localparam send_fsm_76 = 76;
  localparam send_fsm_77 = 77;
  localparam send_fsm_78 = 78;
  localparam send_fsm_79 = 79;
  localparam send_fsm_80 = 80;
  localparam send_fsm_81 = 81;
  localparam send_fsm_82 = 82;
  localparam send_fsm_83 = 83;
  localparam send_fsm_84 = 84;
  localparam send_fsm_85 = 85;
  localparam send_fsm_86 = 86;
  localparam send_fsm_87 = 87;
  localparam send_fsm_88 = 88;
  localparam send_fsm_89 = 89;
  localparam send_fsm_90 = 90;
  localparam send_fsm_91 = 91;
  localparam send_fsm_92 = 92;
  localparam send_fsm_93 = 93;
  localparam send_fsm_94 = 94;
  localparam send_fsm_95 = 95;
  localparam send_fsm_96 = 96;
  localparam send_fsm_97 = 97;
  localparam send_fsm_98 = 98;
  localparam send_fsm_99 = 99;
  localparam send_fsm_100 = 100;
  localparam send_fsm_101 = 101;
  localparam send_fsm_102 = 102;
  localparam send_fsm_103 = 103;

  always @(posedge CLK) begin
    if(RST) begin
      send_fsm <= send_fsm_init;
    end else begin
      case(send_fsm)
        send_fsm_init: begin
          if(reset_done) begin
            send_fsm <= send_fsm_1;
          end 
        end
        send_fsm_1: begin
          din0re <= 0;
          din0im <= 0;
          din1re <= 256;
          din1im <= 256;
          din2re <= 512;
          din2im <= 512;
          din3re <= 768;
          din3im <= 768;
          send_fsm <= send_fsm_2;
        end
        send_fsm_2: begin
          din0re <= 0;
          din0im <= 0;
          din1re <= 0;
          din1im <= 0;
          din2re <= 0;
          din2im <= 0;
          din3re <= 0;
          din3im <= 0;
          send_fsm <= send_fsm_3;
        end
        send_fsm_3: begin
          send_fsm <= send_fsm_4;
        end
        send_fsm_4: begin
          send_fsm <= send_fsm_5;
        end
        send_fsm_5: begin
          send_fsm <= send_fsm_6;
        end
        send_fsm_6: begin
          send_fsm <= send_fsm_7;
        end
        send_fsm_7: begin
          send_fsm <= send_fsm_8;
        end
        send_fsm_8: begin
          send_fsm <= send_fsm_9;
        end
        send_fsm_9: begin
          send_fsm <= send_fsm_10;
        end
        send_fsm_10: begin
          send_fsm <= send_fsm_11;
        end
        send_fsm_11: begin
          send_fsm <= send_fsm_12;
        end
        send_fsm_12: begin
          send_fsm <= send_fsm_13;
        end
        send_fsm_13: begin
          send_fsm <= send_fsm_14;
        end
        send_fsm_14: begin
          send_fsm <= send_fsm_15;
        end
        send_fsm_15: begin
          send_fsm <= send_fsm_16;
        end
        send_fsm_16: begin
          send_fsm <= send_fsm_17;
        end
        send_fsm_17: begin
          send_fsm <= send_fsm_18;
        end
        send_fsm_18: begin
          send_fsm <= send_fsm_19;
        end
        send_fsm_19: begin
          send_fsm <= send_fsm_20;
        end
        send_fsm_20: begin
          send_fsm <= send_fsm_21;
        end
        send_fsm_21: begin
          send_fsm <= send_fsm_22;
        end
        send_fsm_22: begin
          send_fsm <= send_fsm_23;
        end
        send_fsm_23: begin
          send_fsm <= send_fsm_24;
        end
        send_fsm_24: begin
          send_fsm <= send_fsm_25;
        end
        send_fsm_25: begin
          send_fsm <= send_fsm_26;
        end
        send_fsm_26: begin
          send_fsm <= send_fsm_27;
        end
        send_fsm_27: begin
          send_fsm <= send_fsm_28;
        end
        send_fsm_28: begin
          send_fsm <= send_fsm_29;
        end
        send_fsm_29: begin
          send_fsm <= send_fsm_30;
        end
        send_fsm_30: begin
          send_fsm <= send_fsm_31;
        end
        send_fsm_31: begin
          send_fsm <= send_fsm_32;
        end
        send_fsm_32: begin
          send_fsm <= send_fsm_33;
        end
        send_fsm_33: begin
          send_fsm <= send_fsm_34;
        end
        send_fsm_34: begin
          send_fsm <= send_fsm_35;
        end
        send_fsm_35: begin
          send_fsm <= send_fsm_36;
        end
        send_fsm_36: begin
          send_fsm <= send_fsm_37;
        end
        send_fsm_37: begin
          send_fsm <= send_fsm_38;
        end
        send_fsm_38: begin
          send_fsm <= send_fsm_39;
        end
        send_fsm_39: begin
          send_fsm <= send_fsm_40;
        end
        send_fsm_40: begin
          send_fsm <= send_fsm_41;
        end
        send_fsm_41: begin
          send_fsm <= send_fsm_42;
        end
        send_fsm_42: begin
          send_fsm <= send_fsm_43;
        end
        send_fsm_43: begin
          send_fsm <= send_fsm_44;
        end
        send_fsm_44: begin
          send_fsm <= send_fsm_45;
        end
        send_fsm_45: begin
          send_fsm <= send_fsm_46;
        end
        send_fsm_46: begin
          send_fsm <= send_fsm_47;
        end
        send_fsm_47: begin
          send_fsm <= send_fsm_48;
        end
        send_fsm_48: begin
          send_fsm <= send_fsm_49;
        end
        send_fsm_49: begin
          send_fsm <= send_fsm_50;
        end
        send_fsm_50: begin
          send_fsm <= send_fsm_51;
        end
        send_fsm_51: begin
          send_fsm <= send_fsm_52;
        end
        send_fsm_52: begin
          send_fsm <= send_fsm_53;
        end
        send_fsm_53: begin
          send_fsm <= send_fsm_54;
        end
        send_fsm_54: begin
          send_fsm <= send_fsm_55;
        end
        send_fsm_55: begin
          send_fsm <= send_fsm_56;
        end
        send_fsm_56: begin
          send_fsm <= send_fsm_57;
        end
        send_fsm_57: begin
          send_fsm <= send_fsm_58;
        end
        send_fsm_58: begin
          send_fsm <= send_fsm_59;
        end
        send_fsm_59: begin
          send_fsm <= send_fsm_60;
        end
        send_fsm_60: begin
          send_fsm <= send_fsm_61;
        end
        send_fsm_61: begin
          send_fsm <= send_fsm_62;
        end
        send_fsm_62: begin
          send_fsm <= send_fsm_63;
        end
        send_fsm_63: begin
          send_fsm <= send_fsm_64;
        end
        send_fsm_64: begin
          send_fsm <= send_fsm_65;
        end
        send_fsm_65: begin
          send_fsm <= send_fsm_66;
        end
        send_fsm_66: begin
          send_fsm <= send_fsm_67;
        end
        send_fsm_67: begin
          send_fsm <= send_fsm_68;
        end
        send_fsm_68: begin
          send_fsm <= send_fsm_69;
        end
        send_fsm_69: begin
          send_fsm <= send_fsm_70;
        end
        send_fsm_70: begin
          send_fsm <= send_fsm_71;
        end
        send_fsm_71: begin
          send_fsm <= send_fsm_72;
        end
        send_fsm_72: begin
          send_fsm <= send_fsm_73;
        end
        send_fsm_73: begin
          send_fsm <= send_fsm_74;
        end
        send_fsm_74: begin
          send_fsm <= send_fsm_75;
        end
        send_fsm_75: begin
          send_fsm <= send_fsm_76;
        end
        send_fsm_76: begin
          send_fsm <= send_fsm_77;
        end
        send_fsm_77: begin
          send_fsm <= send_fsm_78;
        end
        send_fsm_78: begin
          send_fsm <= send_fsm_79;
        end
        send_fsm_79: begin
          send_fsm <= send_fsm_80;
        end
        send_fsm_80: begin
          send_fsm <= send_fsm_81;
        end
        send_fsm_81: begin
          send_fsm <= send_fsm_82;
        end
        send_fsm_82: begin
          send_fsm <= send_fsm_83;
        end
        send_fsm_83: begin
          send_fsm <= send_fsm_84;
        end
        send_fsm_84: begin
          send_fsm <= send_fsm_85;
        end
        send_fsm_85: begin
          send_fsm <= send_fsm_86;
        end
        send_fsm_86: begin
          send_fsm <= send_fsm_87;
        end
        send_fsm_87: begin
          send_fsm <= send_fsm_88;
        end
        send_fsm_88: begin
          send_fsm <= send_fsm_89;
        end
        send_fsm_89: begin
          send_fsm <= send_fsm_90;
        end
        send_fsm_90: begin
          send_fsm <= send_fsm_91;
        end
        send_fsm_91: begin
          send_fsm <= send_fsm_92;
        end
        send_fsm_92: begin
          send_fsm <= send_fsm_93;
        end
        send_fsm_93: begin
          send_fsm <= send_fsm_94;
        end
        send_fsm_94: begin
          send_fsm <= send_fsm_95;
        end
        send_fsm_95: begin
          send_fsm <= send_fsm_96;
        end
        send_fsm_96: begin
          send_fsm <= send_fsm_97;
        end
        send_fsm_97: begin
          send_fsm <= send_fsm_98;
        end
        send_fsm_98: begin
          send_fsm <= send_fsm_99;
        end
        send_fsm_99: begin
          send_fsm <= send_fsm_100;
        end
        send_fsm_100: begin
          send_fsm <= send_fsm_101;
        end
        send_fsm_101: begin
          send_fsm <= send_fsm_102;
        end
        send_fsm_102: begin
          send_fsm <= send_fsm_103;
        end
        send_fsm_103: begin
          $finish;
        end
      endcase
    end
  end


endmodule



module fft4
(
  input CLK,
  input RST,
  input signed [16-1:0] din0re,
  input signed [16-1:0] din0im,
  input signed [16-1:0] din1re,
  input signed [16-1:0] din1im,
  input signed [16-1:0] din2re,
  input signed [16-1:0] din2im,
  input signed [16-1:0] din3re,
  input signed [16-1:0] din3im,
  output signed [16-1:0] dout3re,
  output signed [16-1:0] dout3im,
  output signed [16-1:0] dout0re,
  output signed [16-1:0] dout0im,
  output signed [16-1:0] dout2re,
  output signed [16-1:0] dout2im,
  output signed [16-1:0] dout1re,
  output signed [16-1:0] dout1im
);

  reg signed [16-1:0] _plus_data_0;
  reg _plus_valid_0;
  wire _plus_ready_0;
  reg signed [16-1:0] _plus_data_1;
  reg _plus_valid_1;
  wire _plus_ready_1;
  reg signed [16-1:0] _minus_data_2;
  reg _minus_valid_2;
  wire _minus_ready_2;
  reg signed [16-1:0] _minus_data_3;
  reg _minus_valid_3;
  wire _minus_ready_3;
  reg signed [16-1:0] _plus_data_4;
  reg _plus_valid_4;
  wire _plus_ready_4;
  reg signed [16-1:0] _plus_data_5;
  reg _plus_valid_5;
  wire _plus_ready_5;
  reg signed [16-1:0] _minus_data_6;
  reg _minus_valid_6;
  wire _minus_ready_6;
  reg signed [16-1:0] _minus_data_7;
  reg _minus_valid_7;
  wire _minus_ready_7;
  wire signed [16-1:0] _times_data_8;
  wire _times_valid_8;
  wire _times_ready_8;
  wire signed [18-1:0] _times_odata_8;
  reg signed [18-1:0] _times_data_reg_8;
  assign _times_data_8 = _times_data_reg_8;
  wire _times_ovalid_8;
  reg _times_valid_reg_8;
  assign _times_valid_8 = _times_valid_reg_8;
  wire _times_enable_8;
  wire _times_update_8;
  assign _times_enable_8 = (_times_ready_8 || !_times_valid_8) && _minus_ready_2 && _minus_valid_2;
  assign _times_update_8 = _times_ready_8 || !_times_valid_8;

  multiplier_0
  mul8
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_8),
    .enable(_times_enable_8),
    .valid(_times_ovalid_8),
    .a(_minus_data_2),
    .b(2'sd1),
    .c(_times_odata_8)
  );

  wire signed [16-1:0] _times_data_9;
  wire _times_valid_9;
  wire _times_ready_9;
  wire signed [17-1:0] _times_odata_9;
  reg signed [17-1:0] _times_data_reg_9;
  assign _times_data_9 = _times_data_reg_9;
  wire _times_ovalid_9;
  reg _times_valid_reg_9;
  assign _times_valid_9 = _times_valid_reg_9;
  wire _times_enable_9;
  wire _times_update_9;
  assign _times_enable_9 = (_times_ready_9 || !_times_valid_9) && _minus_ready_3 && _minus_valid_3;
  assign _times_update_9 = _times_ready_9 || !_times_valid_9;

  multiplier_1
  mul9
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_9),
    .enable(_times_enable_9),
    .valid(_times_ovalid_9),
    .a(_minus_data_3),
    .b(1'sd0),
    .c(_times_odata_9)
  );

  wire signed [16-1:0] _times_data_10;
  wire _times_valid_10;
  wire _times_ready_10;
  wire signed [17-1:0] _times_odata_10;
  reg signed [17-1:0] _times_data_reg_10;
  assign _times_data_10 = _times_data_reg_10;
  wire _times_ovalid_10;
  reg _times_valid_reg_10;
  assign _times_valid_10 = _times_valid_reg_10;
  wire _times_enable_10;
  wire _times_update_10;
  assign _times_enable_10 = (_times_ready_10 || !_times_valid_10) && _minus_ready_2 && _minus_valid_2;
  assign _times_update_10 = _times_ready_10 || !_times_valid_10;

  multiplier_2
  mul10
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_10),
    .enable(_times_enable_10),
    .valid(_times_ovalid_10),
    .a(_minus_data_2),
    .b(1'sd0),
    .c(_times_odata_10)
  );

  assign _minus_ready_2 = (_times_ready_8 || !_times_valid_8) && _minus_valid_2 && ((_times_ready_10 || !_times_valid_10) && _minus_valid_2);
  wire signed [16-1:0] _times_data_11;
  wire _times_valid_11;
  wire _times_ready_11;
  wire signed [18-1:0] _times_odata_11;
  reg signed [18-1:0] _times_data_reg_11;
  assign _times_data_11 = _times_data_reg_11;
  wire _times_ovalid_11;
  reg _times_valid_reg_11;
  assign _times_valid_11 = _times_valid_reg_11;
  wire _times_enable_11;
  wire _times_update_11;
  assign _times_enable_11 = (_times_ready_11 || !_times_valid_11) && _minus_ready_3 && _minus_valid_3;
  assign _times_update_11 = _times_ready_11 || !_times_valid_11;

  multiplier_3
  mul11
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_11),
    .enable(_times_enable_11),
    .valid(_times_ovalid_11),
    .a(_minus_data_3),
    .b(2'sd1),
    .c(_times_odata_11)
  );

  assign _minus_ready_3 = (_times_ready_9 || !_times_valid_9) && _minus_valid_3 && ((_times_ready_11 || !_times_valid_11) && _minus_valid_3);
  wire signed [16-1:0] _times_data_12;
  wire _times_valid_12;
  wire _times_ready_12;
  wire signed [17-1:0] _times_odata_12;
  reg signed [17-1:0] _times_data_reg_12;
  assign _times_data_12 = _times_data_reg_12;
  wire _times_ovalid_12;
  reg _times_valid_reg_12;
  assign _times_valid_12 = _times_valid_reg_12;
  wire _times_enable_12;
  wire _times_update_12;
  assign _times_enable_12 = (_times_ready_12 || !_times_valid_12) && _minus_ready_6 && _minus_valid_6;
  assign _times_update_12 = _times_ready_12 || !_times_valid_12;

  multiplier_4
  mul12
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_12),
    .enable(_times_enable_12),
    .valid(_times_ovalid_12),
    .a(_minus_data_6),
    .b(1'sd0),
    .c(_times_odata_12)
  );

  wire signed [16-1:0] _times_data_13;
  wire _times_valid_13;
  wire _times_ready_13;
  wire signed [18-1:0] _times_odata_13;
  reg signed [18-1:0] _times_data_reg_13;
  assign _times_data_13 = _times_data_reg_13;
  wire _times_ovalid_13;
  reg _times_valid_reg_13;
  assign _times_valid_13 = _times_valid_reg_13;
  wire _times_enable_13;
  wire _times_update_13;
  assign _times_enable_13 = (_times_ready_13 || !_times_valid_13) && _minus_ready_7 && _minus_valid_7;
  assign _times_update_13 = _times_ready_13 || !_times_valid_13;

  multiplier_5
  mul13
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_13),
    .enable(_times_enable_13),
    .valid(_times_ovalid_13),
    .a(_minus_data_7),
    .b(-2'sd1),
    .c(_times_odata_13)
  );

  wire signed [16-1:0] _times_data_14;
  wire _times_valid_14;
  wire _times_ready_14;
  wire signed [18-1:0] _times_odata_14;
  reg signed [18-1:0] _times_data_reg_14;
  assign _times_data_14 = _times_data_reg_14;
  wire _times_ovalid_14;
  reg _times_valid_reg_14;
  assign _times_valid_14 = _times_valid_reg_14;
  wire _times_enable_14;
  wire _times_update_14;
  assign _times_enable_14 = (_times_ready_14 || !_times_valid_14) && _minus_ready_6 && _minus_valid_6;
  assign _times_update_14 = _times_ready_14 || !_times_valid_14;

  multiplier_6
  mul14
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_14),
    .enable(_times_enable_14),
    .valid(_times_ovalid_14),
    .a(_minus_data_6),
    .b(-2'sd1),
    .c(_times_odata_14)
  );

  assign _minus_ready_6 = (_times_ready_12 || !_times_valid_12) && _minus_valid_6 && ((_times_ready_14 || !_times_valid_14) && _minus_valid_6);
  wire signed [16-1:0] _times_data_15;
  wire _times_valid_15;
  wire _times_ready_15;
  wire signed [17-1:0] _times_odata_15;
  reg signed [17-1:0] _times_data_reg_15;
  assign _times_data_15 = _times_data_reg_15;
  wire _times_ovalid_15;
  reg _times_valid_reg_15;
  assign _times_valid_15 = _times_valid_reg_15;
  wire _times_enable_15;
  wire _times_update_15;
  assign _times_enable_15 = (_times_ready_15 || !_times_valid_15) && _minus_ready_7 && _minus_valid_7;
  assign _times_update_15 = _times_ready_15 || !_times_valid_15;

  multiplier_7
  mul15
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_15),
    .enable(_times_enable_15),
    .valid(_times_ovalid_15),
    .a(_minus_data_7),
    .b(1'sd0),
    .c(_times_odata_15)
  );

  assign _minus_ready_7 = (_times_ready_13 || !_times_valid_13) && _minus_valid_7 && ((_times_ready_15 || !_times_valid_15) && _minus_valid_7);
  reg signed [16-1:0] _plus_data_16;
  reg _plus_valid_16;
  wire _plus_ready_16;
  reg signed [16-1:0] _plus_data_17;
  reg _plus_valid_17;
  wire _plus_ready_17;
  reg signed [16-1:0] _minus_data_18;
  reg _minus_valid_18;
  wire _minus_ready_18;
  assign _plus_ready_0 = (_plus_ready_16 || !_plus_valid_16) && (_plus_valid_0 && _plus_valid_4) && ((_minus_ready_18 || !_minus_valid_18) && (_plus_valid_0 && _plus_valid_4));
  assign _plus_ready_4 = (_plus_ready_16 || !_plus_valid_16) && (_plus_valid_0 && _plus_valid_4) && ((_minus_ready_18 || !_minus_valid_18) && (_plus_valid_0 && _plus_valid_4));
  reg signed [16-1:0] _minus_data_19;
  reg _minus_valid_19;
  wire _minus_ready_19;
  assign _plus_ready_1 = (_plus_ready_17 || !_plus_valid_17) && (_plus_valid_1 && _plus_valid_5) && ((_minus_ready_19 || !_minus_valid_19) && (_plus_valid_1 && _plus_valid_5));
  assign _plus_ready_5 = (_plus_ready_17 || !_plus_valid_17) && (_plus_valid_1 && _plus_valid_5) && ((_minus_ready_19 || !_minus_valid_19) && (_plus_valid_1 && _plus_valid_5));
  wire signed [16-1:0] _times_data_20;
  wire _times_valid_20;
  wire _times_ready_20;
  wire signed [18-1:0] _times_odata_20;
  reg signed [18-1:0] _times_data_reg_20;
  assign _times_data_20 = _times_data_reg_20;
  wire _times_ovalid_20;
  reg _times_valid_reg_20;
  assign _times_valid_20 = _times_valid_reg_20;
  wire _times_enable_20;
  wire _times_update_20;
  assign _times_enable_20 = (_times_ready_20 || !_times_valid_20) && _minus_ready_18 && _minus_valid_18;
  assign _times_update_20 = _times_ready_20 || !_times_valid_20;

  multiplier_8
  mul20
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_20),
    .enable(_times_enable_20),
    .valid(_times_ovalid_20),
    .a(_minus_data_18),
    .b(2'sd1),
    .c(_times_odata_20)
  );

  wire signed [16-1:0] _times_data_21;
  wire _times_valid_21;
  wire _times_ready_21;
  wire signed [17-1:0] _times_odata_21;
  reg signed [17-1:0] _times_data_reg_21;
  assign _times_data_21 = _times_data_reg_21;
  wire _times_ovalid_21;
  reg _times_valid_reg_21;
  assign _times_valid_21 = _times_valid_reg_21;
  wire _times_enable_21;
  wire _times_update_21;
  assign _times_enable_21 = (_times_ready_21 || !_times_valid_21) && _minus_ready_19 && _minus_valid_19;
  assign _times_update_21 = _times_ready_21 || !_times_valid_21;

  multiplier_9
  mul21
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_21),
    .enable(_times_enable_21),
    .valid(_times_ovalid_21),
    .a(_minus_data_19),
    .b(1'sd0),
    .c(_times_odata_21)
  );

  wire signed [16-1:0] _times_data_22;
  wire _times_valid_22;
  wire _times_ready_22;
  wire signed [17-1:0] _times_odata_22;
  reg signed [17-1:0] _times_data_reg_22;
  assign _times_data_22 = _times_data_reg_22;
  wire _times_ovalid_22;
  reg _times_valid_reg_22;
  assign _times_valid_22 = _times_valid_reg_22;
  wire _times_enable_22;
  wire _times_update_22;
  assign _times_enable_22 = (_times_ready_22 || !_times_valid_22) && _minus_ready_18 && _minus_valid_18;
  assign _times_update_22 = _times_ready_22 || !_times_valid_22;

  multiplier_10
  mul22
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_22),
    .enable(_times_enable_22),
    .valid(_times_ovalid_22),
    .a(_minus_data_18),
    .b(1'sd0),
    .c(_times_odata_22)
  );

  assign _minus_ready_18 = (_times_ready_20 || !_times_valid_20) && _minus_valid_18 && ((_times_ready_22 || !_times_valid_22) && _minus_valid_18);
  wire signed [16-1:0] _times_data_23;
  wire _times_valid_23;
  wire _times_ready_23;
  wire signed [18-1:0] _times_odata_23;
  reg signed [18-1:0] _times_data_reg_23;
  assign _times_data_23 = _times_data_reg_23;
  wire _times_ovalid_23;
  reg _times_valid_reg_23;
  assign _times_valid_23 = _times_valid_reg_23;
  wire _times_enable_23;
  wire _times_update_23;
  assign _times_enable_23 = (_times_ready_23 || !_times_valid_23) && _minus_ready_19 && _minus_valid_19;
  assign _times_update_23 = _times_ready_23 || !_times_valid_23;

  multiplier_11
  mul23
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_23),
    .enable(_times_enable_23),
    .valid(_times_ovalid_23),
    .a(_minus_data_19),
    .b(2'sd1),
    .c(_times_odata_23)
  );

  assign _minus_ready_19 = (_times_ready_21 || !_times_valid_21) && _minus_valid_19 && ((_times_ready_23 || !_times_valid_23) && _minus_valid_19);
  reg signed [16-1:0] __delay_data_24;
  reg __delay_valid_24;
  wire __delay_ready_24;
  assign _plus_ready_16 = (__delay_ready_24 || !__delay_valid_24) && _plus_valid_16;
  reg signed [16-1:0] __delay_data_25;
  reg __delay_valid_25;
  wire __delay_ready_25;
  assign _plus_ready_17 = (__delay_ready_25 || !__delay_valid_25) && _plus_valid_17;
  reg signed [16-1:0] __delay_data_26;
  reg __delay_valid_26;
  wire __delay_ready_26;
  assign __delay_ready_24 = (__delay_ready_26 || !__delay_valid_26) && __delay_valid_24;
  reg signed [16-1:0] __delay_data_27;
  reg __delay_valid_27;
  wire __delay_ready_27;
  assign __delay_ready_25 = (__delay_ready_27 || !__delay_valid_27) && __delay_valid_25;
  reg signed [16-1:0] __delay_data_28;
  reg __delay_valid_28;
  wire __delay_ready_28;
  assign __delay_ready_26 = (__delay_ready_28 || !__delay_valid_28) && __delay_valid_26;
  reg signed [16-1:0] __delay_data_29;
  reg __delay_valid_29;
  wire __delay_ready_29;
  assign __delay_ready_27 = (__delay_ready_29 || !__delay_valid_29) && __delay_valid_27;
  reg signed [16-1:0] __delay_data_30;
  reg __delay_valid_30;
  wire __delay_ready_30;
  assign __delay_ready_28 = (__delay_ready_30 || !__delay_valid_30) && __delay_valid_28;
  reg signed [16-1:0] __delay_data_31;
  reg __delay_valid_31;
  wire __delay_ready_31;
  assign __delay_ready_29 = (__delay_ready_31 || !__delay_valid_31) && __delay_valid_29;
  reg signed [16-1:0] __delay_data_32;
  reg __delay_valid_32;
  wire __delay_ready_32;
  assign __delay_ready_30 = (__delay_ready_32 || !__delay_valid_32) && __delay_valid_30;
  reg signed [16-1:0] __delay_data_33;
  reg __delay_valid_33;
  wire __delay_ready_33;
  assign __delay_ready_31 = (__delay_ready_33 || !__delay_valid_33) && __delay_valid_31;
  reg signed [16-1:0] __delay_data_34;
  reg __delay_valid_34;
  wire __delay_ready_34;
  assign __delay_ready_32 = (__delay_ready_34 || !__delay_valid_34) && __delay_valid_32;
  reg signed [16-1:0] __delay_data_35;
  reg __delay_valid_35;
  wire __delay_ready_35;
  assign __delay_ready_33 = (__delay_ready_35 || !__delay_valid_35) && __delay_valid_33;
  reg signed [16-1:0] _minus_data_36;
  reg _minus_valid_36;
  wire _minus_ready_36;
  assign _times_ready_8 = (_minus_ready_36 || !_minus_valid_36) && (_times_valid_8 && _times_valid_9);
  assign _times_ready_9 = (_minus_ready_36 || !_minus_valid_36) && (_times_valid_8 && _times_valid_9);
  reg signed [16-1:0] _plus_data_37;
  reg _plus_valid_37;
  wire _plus_ready_37;
  assign _times_ready_10 = (_plus_ready_37 || !_plus_valid_37) && (_times_valid_10 && _times_valid_11);
  assign _times_ready_11 = (_plus_ready_37 || !_plus_valid_37) && (_times_valid_10 && _times_valid_11);
  reg signed [16-1:0] _minus_data_38;
  reg _minus_valid_38;
  wire _minus_ready_38;
  assign _times_ready_12 = (_minus_ready_38 || !_minus_valid_38) && (_times_valid_12 && _times_valid_13);
  assign _times_ready_13 = (_minus_ready_38 || !_minus_valid_38) && (_times_valid_12 && _times_valid_13);
  reg signed [16-1:0] _plus_data_39;
  reg _plus_valid_39;
  wire _plus_ready_39;
  assign _times_ready_14 = (_plus_ready_39 || !_plus_valid_39) && (_times_valid_14 && _times_valid_15);
  assign _times_ready_15 = (_plus_ready_39 || !_plus_valid_39) && (_times_valid_14 && _times_valid_15);
  reg signed [16-1:0] __delay_data_40;
  reg __delay_valid_40;
  wire __delay_ready_40;
  assign __delay_ready_34 = (__delay_ready_40 || !__delay_valid_40) && __delay_valid_34;
  reg signed [16-1:0] __delay_data_41;
  reg __delay_valid_41;
  wire __delay_ready_41;
  assign __delay_ready_35 = (__delay_ready_41 || !__delay_valid_41) && __delay_valid_35;
  reg signed [16-1:0] _minus_data_42;
  reg _minus_valid_42;
  wire _minus_ready_42;
  assign _times_ready_20 = (_minus_ready_42 || !_minus_valid_42) && (_times_valid_20 && _times_valid_21);
  assign _times_ready_21 = (_minus_ready_42 || !_minus_valid_42) && (_times_valid_20 && _times_valid_21);
  reg signed [16-1:0] _plus_data_43;
  reg _plus_valid_43;
  wire _plus_ready_43;
  assign _times_ready_22 = (_plus_ready_43 || !_plus_valid_43) && (_times_valid_22 && _times_valid_23);
  assign _times_ready_23 = (_plus_ready_43 || !_plus_valid_43) && (_times_valid_22 && _times_valid_23);
  reg signed [16-1:0] _plus_data_44;
  reg _plus_valid_44;
  wire _plus_ready_44;
  reg signed [16-1:0] _plus_data_45;
  reg _plus_valid_45;
  wire _plus_ready_45;
  reg signed [16-1:0] _minus_data_46;
  reg _minus_valid_46;
  wire _minus_ready_46;
  assign _minus_ready_36 = (_plus_ready_44 || !_plus_valid_44) && (_minus_valid_36 && _minus_valid_38) && ((_minus_ready_46 || !_minus_valid_46) && (_minus_valid_36 && _minus_valid_38));
  assign _minus_ready_38 = (_plus_ready_44 || !_plus_valid_44) && (_minus_valid_36 && _minus_valid_38) && ((_minus_ready_46 || !_minus_valid_46) && (_minus_valid_36 && _minus_valid_38));
  reg signed [16-1:0] _minus_data_47;
  reg _minus_valid_47;
  wire _minus_ready_47;
  assign _plus_ready_37 = (_plus_ready_45 || !_plus_valid_45) && (_plus_valid_37 && _plus_valid_39) && ((_minus_ready_47 || !_minus_valid_47) && (_plus_valid_37 && _plus_valid_39));
  assign _plus_ready_39 = (_plus_ready_45 || !_plus_valid_45) && (_plus_valid_37 && _plus_valid_39) && ((_minus_ready_47 || !_minus_valid_47) && (_plus_valid_37 && _plus_valid_39));
  reg signed [16-1:0] __delay_data_48;
  reg __delay_valid_48;
  wire __delay_ready_48;
  assign __delay_ready_40 = (__delay_ready_48 || !__delay_valid_48) && __delay_valid_40;
  reg signed [16-1:0] __delay_data_49;
  reg __delay_valid_49;
  wire __delay_ready_49;
  assign __delay_ready_41 = (__delay_ready_49 || !__delay_valid_49) && __delay_valid_41;
  wire signed [16-1:0] _times_data_50;
  wire _times_valid_50;
  wire _times_ready_50;
  wire signed [18-1:0] _times_odata_50;
  reg signed [18-1:0] _times_data_reg_50;
  assign _times_data_50 = _times_data_reg_50;
  wire _times_ovalid_50;
  reg _times_valid_reg_50;
  assign _times_valid_50 = _times_valid_reg_50;
  wire _times_enable_50;
  wire _times_update_50;
  assign _times_enable_50 = (_times_ready_50 || !_times_valid_50) && _minus_ready_46 && _minus_valid_46;
  assign _times_update_50 = _times_ready_50 || !_times_valid_50;

  multiplier_12
  mul50
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_50),
    .enable(_times_enable_50),
    .valid(_times_ovalid_50),
    .a(_minus_data_46),
    .b(2'sd1),
    .c(_times_odata_50)
  );

  wire signed [16-1:0] _times_data_51;
  wire _times_valid_51;
  wire _times_ready_51;
  wire signed [17-1:0] _times_odata_51;
  reg signed [17-1:0] _times_data_reg_51;
  assign _times_data_51 = _times_data_reg_51;
  wire _times_ovalid_51;
  reg _times_valid_reg_51;
  assign _times_valid_51 = _times_valid_reg_51;
  wire _times_enable_51;
  wire _times_update_51;
  assign _times_enable_51 = (_times_ready_51 || !_times_valid_51) && _minus_ready_47 && _minus_valid_47;
  assign _times_update_51 = _times_ready_51 || !_times_valid_51;

  multiplier_13
  mul51
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_51),
    .enable(_times_enable_51),
    .valid(_times_ovalid_51),
    .a(_minus_data_47),
    .b(1'sd0),
    .c(_times_odata_51)
  );

  wire signed [16-1:0] _times_data_52;
  wire _times_valid_52;
  wire _times_ready_52;
  wire signed [17-1:0] _times_odata_52;
  reg signed [17-1:0] _times_data_reg_52;
  assign _times_data_52 = _times_data_reg_52;
  wire _times_ovalid_52;
  reg _times_valid_reg_52;
  assign _times_valid_52 = _times_valid_reg_52;
  wire _times_enable_52;
  wire _times_update_52;
  assign _times_enable_52 = (_times_ready_52 || !_times_valid_52) && _minus_ready_46 && _minus_valid_46;
  assign _times_update_52 = _times_ready_52 || !_times_valid_52;

  multiplier_14
  mul52
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_52),
    .enable(_times_enable_52),
    .valid(_times_ovalid_52),
    .a(_minus_data_46),
    .b(1'sd0),
    .c(_times_odata_52)
  );

  assign _minus_ready_46 = (_times_ready_50 || !_times_valid_50) && _minus_valid_46 && ((_times_ready_52 || !_times_valid_52) && _minus_valid_46);
  wire signed [16-1:0] _times_data_53;
  wire _times_valid_53;
  wire _times_ready_53;
  wire signed [18-1:0] _times_odata_53;
  reg signed [18-1:0] _times_data_reg_53;
  assign _times_data_53 = _times_data_reg_53;
  wire _times_ovalid_53;
  reg _times_valid_reg_53;
  assign _times_valid_53 = _times_valid_reg_53;
  wire _times_enable_53;
  wire _times_update_53;
  assign _times_enable_53 = (_times_ready_53 || !_times_valid_53) && _minus_ready_47 && _minus_valid_47;
  assign _times_update_53 = _times_ready_53 || !_times_valid_53;

  multiplier_15
  mul53
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_53),
    .enable(_times_enable_53),
    .valid(_times_ovalid_53),
    .a(_minus_data_47),
    .b(2'sd1),
    .c(_times_odata_53)
  );

  assign _minus_ready_47 = (_times_ready_51 || !_times_valid_51) && _minus_valid_47 && ((_times_ready_53 || !_times_valid_53) && _minus_valid_47);
  reg signed [16-1:0] __delay_data_54;
  reg __delay_valid_54;
  wire __delay_ready_54;
  assign __delay_ready_48 = (__delay_ready_54 || !__delay_valid_54) && __delay_valid_48;
  reg signed [16-1:0] __delay_data_55;
  reg __delay_valid_55;
  wire __delay_ready_55;
  assign __delay_ready_49 = (__delay_ready_55 || !__delay_valid_55) && __delay_valid_49;
  reg signed [16-1:0] __delay_data_56;
  reg __delay_valid_56;
  wire __delay_ready_56;
  assign _minus_ready_42 = (__delay_ready_56 || !__delay_valid_56) && _minus_valid_42;
  reg signed [16-1:0] __delay_data_57;
  reg __delay_valid_57;
  wire __delay_ready_57;
  assign _plus_ready_43 = (__delay_ready_57 || !__delay_valid_57) && _plus_valid_43;
  reg signed [16-1:0] __delay_data_58;
  reg __delay_valid_58;
  wire __delay_ready_58;
  assign _plus_ready_44 = (__delay_ready_58 || !__delay_valid_58) && _plus_valid_44;
  reg signed [16-1:0] __delay_data_59;
  reg __delay_valid_59;
  wire __delay_ready_59;
  assign _plus_ready_45 = (__delay_ready_59 || !__delay_valid_59) && _plus_valid_45;
  reg signed [16-1:0] __delay_data_60;
  reg __delay_valid_60;
  wire __delay_ready_60;
  assign __delay_ready_54 = (__delay_ready_60 || !__delay_valid_60) && __delay_valid_54;
  reg signed [16-1:0] __delay_data_61;
  reg __delay_valid_61;
  wire __delay_ready_61;
  assign __delay_ready_55 = (__delay_ready_61 || !__delay_valid_61) && __delay_valid_55;
  reg signed [16-1:0] __delay_data_62;
  reg __delay_valid_62;
  wire __delay_ready_62;
  assign __delay_ready_56 = (__delay_ready_62 || !__delay_valid_62) && __delay_valid_56;
  reg signed [16-1:0] __delay_data_63;
  reg __delay_valid_63;
  wire __delay_ready_63;
  assign __delay_ready_57 = (__delay_ready_63 || !__delay_valid_63) && __delay_valid_57;
  reg signed [16-1:0] __delay_data_64;
  reg __delay_valid_64;
  wire __delay_ready_64;
  assign __delay_ready_58 = (__delay_ready_64 || !__delay_valid_64) && __delay_valid_58;
  reg signed [16-1:0] __delay_data_65;
  reg __delay_valid_65;
  wire __delay_ready_65;
  assign __delay_ready_59 = (__delay_ready_65 || !__delay_valid_65) && __delay_valid_59;
  reg signed [16-1:0] __delay_data_66;
  reg __delay_valid_66;
  wire __delay_ready_66;
  assign __delay_ready_60 = (__delay_ready_66 || !__delay_valid_66) && __delay_valid_60;
  reg signed [16-1:0] __delay_data_67;
  reg __delay_valid_67;
  wire __delay_ready_67;
  assign __delay_ready_61 = (__delay_ready_67 || !__delay_valid_67) && __delay_valid_61;
  reg signed [16-1:0] __delay_data_68;
  reg __delay_valid_68;
  wire __delay_ready_68;
  assign __delay_ready_62 = (__delay_ready_68 || !__delay_valid_68) && __delay_valid_62;
  reg signed [16-1:0] __delay_data_69;
  reg __delay_valid_69;
  wire __delay_ready_69;
  assign __delay_ready_63 = (__delay_ready_69 || !__delay_valid_69) && __delay_valid_63;
  reg signed [16-1:0] __delay_data_70;
  reg __delay_valid_70;
  wire __delay_ready_70;
  assign __delay_ready_64 = (__delay_ready_70 || !__delay_valid_70) && __delay_valid_64;
  reg signed [16-1:0] __delay_data_71;
  reg __delay_valid_71;
  wire __delay_ready_71;
  assign __delay_ready_65 = (__delay_ready_71 || !__delay_valid_71) && __delay_valid_65;
  reg signed [16-1:0] __delay_data_72;
  reg __delay_valid_72;
  wire __delay_ready_72;
  assign __delay_ready_66 = (__delay_ready_72 || !__delay_valid_72) && __delay_valid_66;
  reg signed [16-1:0] __delay_data_73;
  reg __delay_valid_73;
  wire __delay_ready_73;
  assign __delay_ready_67 = (__delay_ready_73 || !__delay_valid_73) && __delay_valid_67;
  reg signed [16-1:0] __delay_data_74;
  reg __delay_valid_74;
  wire __delay_ready_74;
  assign __delay_ready_68 = (__delay_ready_74 || !__delay_valid_74) && __delay_valid_68;
  reg signed [16-1:0] __delay_data_75;
  reg __delay_valid_75;
  wire __delay_ready_75;
  assign __delay_ready_69 = (__delay_ready_75 || !__delay_valid_75) && __delay_valid_69;
  reg signed [16-1:0] __delay_data_76;
  reg __delay_valid_76;
  wire __delay_ready_76;
  assign __delay_ready_70 = (__delay_ready_76 || !__delay_valid_76) && __delay_valid_70;
  reg signed [16-1:0] __delay_data_77;
  reg __delay_valid_77;
  wire __delay_ready_77;
  assign __delay_ready_71 = (__delay_ready_77 || !__delay_valid_77) && __delay_valid_71;
  reg signed [16-1:0] __delay_data_78;
  reg __delay_valid_78;
  wire __delay_ready_78;
  assign __delay_ready_72 = (__delay_ready_78 || !__delay_valid_78) && __delay_valid_72;
  reg signed [16-1:0] __delay_data_79;
  reg __delay_valid_79;
  wire __delay_ready_79;
  assign __delay_ready_73 = (__delay_ready_79 || !__delay_valid_79) && __delay_valid_73;
  reg signed [16-1:0] __delay_data_80;
  reg __delay_valid_80;
  wire __delay_ready_80;
  assign __delay_ready_74 = (__delay_ready_80 || !__delay_valid_80) && __delay_valid_74;
  reg signed [16-1:0] __delay_data_81;
  reg __delay_valid_81;
  wire __delay_ready_81;
  assign __delay_ready_75 = (__delay_ready_81 || !__delay_valid_81) && __delay_valid_75;
  reg signed [16-1:0] __delay_data_82;
  reg __delay_valid_82;
  wire __delay_ready_82;
  assign __delay_ready_76 = (__delay_ready_82 || !__delay_valid_82) && __delay_valid_76;
  reg signed [16-1:0] __delay_data_83;
  reg __delay_valid_83;
  wire __delay_ready_83;
  assign __delay_ready_77 = (__delay_ready_83 || !__delay_valid_83) && __delay_valid_77;
  reg signed [16-1:0] __delay_data_84;
  reg __delay_valid_84;
  wire __delay_ready_84;
  assign __delay_ready_78 = (__delay_ready_84 || !__delay_valid_84) && __delay_valid_78;
  reg signed [16-1:0] __delay_data_85;
  reg __delay_valid_85;
  wire __delay_ready_85;
  assign __delay_ready_79 = (__delay_ready_85 || !__delay_valid_85) && __delay_valid_79;
  reg signed [16-1:0] __delay_data_86;
  reg __delay_valid_86;
  wire __delay_ready_86;
  assign __delay_ready_80 = (__delay_ready_86 || !__delay_valid_86) && __delay_valid_80;
  reg signed [16-1:0] __delay_data_87;
  reg __delay_valid_87;
  wire __delay_ready_87;
  assign __delay_ready_81 = (__delay_ready_87 || !__delay_valid_87) && __delay_valid_81;
  reg signed [16-1:0] __delay_data_88;
  reg __delay_valid_88;
  wire __delay_ready_88;
  assign __delay_ready_82 = (__delay_ready_88 || !__delay_valid_88) && __delay_valid_82;
  reg signed [16-1:0] __delay_data_89;
  reg __delay_valid_89;
  wire __delay_ready_89;
  assign __delay_ready_83 = (__delay_ready_89 || !__delay_valid_89) && __delay_valid_83;
  reg signed [16-1:0] __delay_data_90;
  reg __delay_valid_90;
  wire __delay_ready_90;
  assign __delay_ready_84 = (__delay_ready_90 || !__delay_valid_90) && __delay_valid_84;
  reg signed [16-1:0] __delay_data_91;
  reg __delay_valid_91;
  wire __delay_ready_91;
  assign __delay_ready_85 = (__delay_ready_91 || !__delay_valid_91) && __delay_valid_85;
  reg signed [16-1:0] __delay_data_92;
  reg __delay_valid_92;
  wire __delay_ready_92;
  assign __delay_ready_86 = (__delay_ready_92 || !__delay_valid_92) && __delay_valid_86;
  reg signed [16-1:0] __delay_data_93;
  reg __delay_valid_93;
  wire __delay_ready_93;
  assign __delay_ready_87 = (__delay_ready_93 || !__delay_valid_93) && __delay_valid_87;
  reg signed [16-1:0] __delay_data_94;
  reg __delay_valid_94;
  wire __delay_ready_94;
  assign __delay_ready_88 = (__delay_ready_94 || !__delay_valid_94) && __delay_valid_88;
  reg signed [16-1:0] __delay_data_95;
  reg __delay_valid_95;
  wire __delay_ready_95;
  assign __delay_ready_89 = (__delay_ready_95 || !__delay_valid_95) && __delay_valid_89;
  reg signed [16-1:0] _minus_data_96;
  reg _minus_valid_96;
  wire _minus_ready_96;
  assign _times_ready_50 = (_minus_ready_96 || !_minus_valid_96) && (_times_valid_50 && _times_valid_51);
  assign _times_ready_51 = (_minus_ready_96 || !_minus_valid_96) && (_times_valid_50 && _times_valid_51);
  reg signed [16-1:0] _plus_data_97;
  reg _plus_valid_97;
  wire _plus_ready_97;
  assign _times_ready_52 = (_plus_ready_97 || !_plus_valid_97) && (_times_valid_52 && _times_valid_53);
  assign _times_ready_53 = (_plus_ready_97 || !_plus_valid_97) && (_times_valid_52 && _times_valid_53);
  reg signed [16-1:0] __delay_data_98;
  reg __delay_valid_98;
  wire __delay_ready_98;
  assign __delay_ready_90 = (__delay_ready_98 || !__delay_valid_98) && __delay_valid_90;
  reg signed [16-1:0] __delay_data_99;
  reg __delay_valid_99;
  wire __delay_ready_99;
  assign __delay_ready_91 = (__delay_ready_99 || !__delay_valid_99) && __delay_valid_91;
  reg signed [16-1:0] __delay_data_100;
  reg __delay_valid_100;
  wire __delay_ready_100;
  assign __delay_ready_92 = (__delay_ready_100 || !__delay_valid_100) && __delay_valid_92;
  reg signed [16-1:0] __delay_data_101;
  reg __delay_valid_101;
  wire __delay_ready_101;
  assign __delay_ready_93 = (__delay_ready_101 || !__delay_valid_101) && __delay_valid_93;
  reg signed [16-1:0] __delay_data_102;
  reg __delay_valid_102;
  wire __delay_ready_102;
  assign __delay_ready_94 = (__delay_ready_102 || !__delay_valid_102) && __delay_valid_94;
  reg signed [16-1:0] __delay_data_103;
  reg __delay_valid_103;
  wire __delay_ready_103;
  assign __delay_ready_95 = (__delay_ready_103 || !__delay_valid_103) && __delay_valid_95;
  assign dout3re = _minus_data_96;
  assign _minus_ready_96 = 1;
  assign dout3im = _plus_data_97;
  assign _plus_ready_97 = 1;
  assign dout0re = __delay_data_98;
  assign __delay_ready_98 = 1;
  assign dout0im = __delay_data_99;
  assign __delay_ready_99 = 1;
  assign dout2re = __delay_data_100;
  assign __delay_ready_100 = 1;
  assign dout2im = __delay_data_101;
  assign __delay_ready_101 = 1;
  assign dout1re = __delay_data_102;
  assign __delay_ready_102 = 1;
  assign dout1im = __delay_data_103;
  assign __delay_ready_103 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_0 <= 0;
      _plus_valid_0 <= 0;
      _plus_data_1 <= 0;
      _plus_valid_1 <= 0;
      _minus_data_2 <= 0;
      _minus_valid_2 <= 0;
      _minus_data_3 <= 0;
      _minus_valid_3 <= 0;
      _plus_data_4 <= 0;
      _plus_valid_4 <= 0;
      _plus_data_5 <= 0;
      _plus_valid_5 <= 0;
      _minus_data_6 <= 0;
      _minus_valid_6 <= 0;
      _minus_data_7 <= 0;
      _minus_valid_7 <= 0;
      _times_data_reg_8 <= 0;
      _times_valid_reg_8 <= 0;
      _times_data_reg_9 <= 0;
      _times_valid_reg_9 <= 0;
      _times_data_reg_10 <= 0;
      _times_valid_reg_10 <= 0;
      _times_data_reg_11 <= 0;
      _times_valid_reg_11 <= 0;
      _times_data_reg_12 <= 0;
      _times_valid_reg_12 <= 0;
      _times_data_reg_13 <= 0;
      _times_valid_reg_13 <= 0;
      _times_data_reg_14 <= 0;
      _times_valid_reg_14 <= 0;
      _times_data_reg_15 <= 0;
      _times_valid_reg_15 <= 0;
      _plus_data_16 <= 0;
      _plus_valid_16 <= 0;
      _plus_data_17 <= 0;
      _plus_valid_17 <= 0;
      _minus_data_18 <= 0;
      _minus_valid_18 <= 0;
      _minus_data_19 <= 0;
      _minus_valid_19 <= 0;
      _times_data_reg_20 <= 0;
      _times_valid_reg_20 <= 0;
      _times_data_reg_21 <= 0;
      _times_valid_reg_21 <= 0;
      _times_data_reg_22 <= 0;
      _times_valid_reg_22 <= 0;
      _times_data_reg_23 <= 0;
      _times_valid_reg_23 <= 0;
      __delay_data_24 <= 0;
      __delay_valid_24 <= 0;
      __delay_data_25 <= 0;
      __delay_valid_25 <= 0;
      __delay_data_26 <= 0;
      __delay_valid_26 <= 0;
      __delay_data_27 <= 0;
      __delay_valid_27 <= 0;
      __delay_data_28 <= 0;
      __delay_valid_28 <= 0;
      __delay_data_29 <= 0;
      __delay_valid_29 <= 0;
      __delay_data_30 <= 0;
      __delay_valid_30 <= 0;
      __delay_data_31 <= 0;
      __delay_valid_31 <= 0;
      __delay_data_32 <= 0;
      __delay_valid_32 <= 0;
      __delay_data_33 <= 0;
      __delay_valid_33 <= 0;
      __delay_data_34 <= 0;
      __delay_valid_34 <= 0;
      __delay_data_35 <= 0;
      __delay_valid_35 <= 0;
      _minus_data_36 <= 0;
      _minus_valid_36 <= 0;
      _plus_data_37 <= 0;
      _plus_valid_37 <= 0;
      _minus_data_38 <= 0;
      _minus_valid_38 <= 0;
      _plus_data_39 <= 0;
      _plus_valid_39 <= 0;
      __delay_data_40 <= 0;
      __delay_valid_40 <= 0;
      __delay_data_41 <= 0;
      __delay_valid_41 <= 0;
      _minus_data_42 <= 0;
      _minus_valid_42 <= 0;
      _plus_data_43 <= 0;
      _plus_valid_43 <= 0;
      _plus_data_44 <= 0;
      _plus_valid_44 <= 0;
      _plus_data_45 <= 0;
      _plus_valid_45 <= 0;
      _minus_data_46 <= 0;
      _minus_valid_46 <= 0;
      _minus_data_47 <= 0;
      _minus_valid_47 <= 0;
      __delay_data_48 <= 0;
      __delay_valid_48 <= 0;
      __delay_data_49 <= 0;
      __delay_valid_49 <= 0;
      _times_data_reg_50 <= 0;
      _times_valid_reg_50 <= 0;
      _times_data_reg_51 <= 0;
      _times_valid_reg_51 <= 0;
      _times_data_reg_52 <= 0;
      _times_valid_reg_52 <= 0;
      _times_data_reg_53 <= 0;
      _times_valid_reg_53 <= 0;
      __delay_data_54 <= 0;
      __delay_valid_54 <= 0;
      __delay_data_55 <= 0;
      __delay_valid_55 <= 0;
      __delay_data_56 <= 0;
      __delay_valid_56 <= 0;
      __delay_data_57 <= 0;
      __delay_valid_57 <= 0;
      __delay_data_58 <= 0;
      __delay_valid_58 <= 0;
      __delay_data_59 <= 0;
      __delay_valid_59 <= 0;
      __delay_data_60 <= 0;
      __delay_valid_60 <= 0;
      __delay_data_61 <= 0;
      __delay_valid_61 <= 0;
      __delay_data_62 <= 0;
      __delay_valid_62 <= 0;
      __delay_data_63 <= 0;
      __delay_valid_63 <= 0;
      __delay_data_64 <= 0;
      __delay_valid_64 <= 0;
      __delay_data_65 <= 0;
      __delay_valid_65 <= 0;
      __delay_data_66 <= 0;
      __delay_valid_66 <= 0;
      __delay_data_67 <= 0;
      __delay_valid_67 <= 0;
      __delay_data_68 <= 0;
      __delay_valid_68 <= 0;
      __delay_data_69 <= 0;
      __delay_valid_69 <= 0;
      __delay_data_70 <= 0;
      __delay_valid_70 <= 0;
      __delay_data_71 <= 0;
      __delay_valid_71 <= 0;
      __delay_data_72 <= 0;
      __delay_valid_72 <= 0;
      __delay_data_73 <= 0;
      __delay_valid_73 <= 0;
      __delay_data_74 <= 0;
      __delay_valid_74 <= 0;
      __delay_data_75 <= 0;
      __delay_valid_75 <= 0;
      __delay_data_76 <= 0;
      __delay_valid_76 <= 0;
      __delay_data_77 <= 0;
      __delay_valid_77 <= 0;
      __delay_data_78 <= 0;
      __delay_valid_78 <= 0;
      __delay_data_79 <= 0;
      __delay_valid_79 <= 0;
      __delay_data_80 <= 0;
      __delay_valid_80 <= 0;
      __delay_data_81 <= 0;
      __delay_valid_81 <= 0;
      __delay_data_82 <= 0;
      __delay_valid_82 <= 0;
      __delay_data_83 <= 0;
      __delay_valid_83 <= 0;
      __delay_data_84 <= 0;
      __delay_valid_84 <= 0;
      __delay_data_85 <= 0;
      __delay_valid_85 <= 0;
      __delay_data_86 <= 0;
      __delay_valid_86 <= 0;
      __delay_data_87 <= 0;
      __delay_valid_87 <= 0;
      __delay_data_88 <= 0;
      __delay_valid_88 <= 0;
      __delay_data_89 <= 0;
      __delay_valid_89 <= 0;
      __delay_data_90 <= 0;
      __delay_valid_90 <= 0;
      __delay_data_91 <= 0;
      __delay_valid_91 <= 0;
      __delay_data_92 <= 0;
      __delay_valid_92 <= 0;
      __delay_data_93 <= 0;
      __delay_valid_93 <= 0;
      __delay_data_94 <= 0;
      __delay_valid_94 <= 0;
      __delay_data_95 <= 0;
      __delay_valid_95 <= 0;
      _minus_data_96 <= 0;
      _minus_valid_96 <= 0;
      _plus_data_97 <= 0;
      _plus_valid_97 <= 0;
      __delay_data_98 <= 0;
      __delay_valid_98 <= 0;
      __delay_data_99 <= 0;
      __delay_valid_99 <= 0;
      __delay_data_100 <= 0;
      __delay_valid_100 <= 0;
      __delay_data_101 <= 0;
      __delay_valid_101 <= 0;
      __delay_data_102 <= 0;
      __delay_valid_102 <= 0;
      __delay_data_103 <= 0;
      __delay_valid_103 <= 0;
    end else begin
      if((_plus_ready_0 || !_plus_valid_0) && 1 && 1) begin
        _plus_data_0 <= din0re + din2re;
      end 
      if(_plus_valid_0 && _plus_ready_0) begin
        _plus_valid_0 <= 0;
      end 
      if((_plus_ready_0 || !_plus_valid_0) && 1) begin
        _plus_valid_0 <= 1;
      end 
      if((_plus_ready_1 || !_plus_valid_1) && 1 && 1) begin
        _plus_data_1 <= din0im + din2im;
      end 
      if(_plus_valid_1 && _plus_ready_1) begin
        _plus_valid_1 <= 0;
      end 
      if((_plus_ready_1 || !_plus_valid_1) && 1) begin
        _plus_valid_1 <= 1;
      end 
      if((_minus_ready_2 || !_minus_valid_2) && 1 && 1) begin
        _minus_data_2 <= din0re - din2re;
      end 
      if(_minus_valid_2 && _minus_ready_2) begin
        _minus_valid_2 <= 0;
      end 
      if((_minus_ready_2 || !_minus_valid_2) && 1) begin
        _minus_valid_2 <= 1;
      end 
      if((_minus_ready_3 || !_minus_valid_3) && 1 && 1) begin
        _minus_data_3 <= din0im - din2im;
      end 
      if(_minus_valid_3 && _minus_ready_3) begin
        _minus_valid_3 <= 0;
      end 
      if((_minus_ready_3 || !_minus_valid_3) && 1) begin
        _minus_valid_3 <= 1;
      end 
      if((_plus_ready_4 || !_plus_valid_4) && 1 && 1) begin
        _plus_data_4 <= din1re + din3re;
      end 
      if(_plus_valid_4 && _plus_ready_4) begin
        _plus_valid_4 <= 0;
      end 
      if((_plus_ready_4 || !_plus_valid_4) && 1) begin
        _plus_valid_4 <= 1;
      end 
      if((_plus_ready_5 || !_plus_valid_5) && 1 && 1) begin
        _plus_data_5 <= din1im + din3im;
      end 
      if(_plus_valid_5 && _plus_ready_5) begin
        _plus_valid_5 <= 0;
      end 
      if((_plus_ready_5 || !_plus_valid_5) && 1) begin
        _plus_valid_5 <= 1;
      end 
      if((_minus_ready_6 || !_minus_valid_6) && 1 && 1) begin
        _minus_data_6 <= din1re - din3re;
      end 
      if(_minus_valid_6 && _minus_ready_6) begin
        _minus_valid_6 <= 0;
      end 
      if((_minus_ready_6 || !_minus_valid_6) && 1) begin
        _minus_valid_6 <= 1;
      end 
      if((_minus_ready_7 || !_minus_valid_7) && 1 && 1) begin
        _minus_data_7 <= din1im - din3im;
      end 
      if(_minus_valid_7 && _minus_ready_7) begin
        _minus_valid_7 <= 0;
      end 
      if((_minus_ready_7 || !_minus_valid_7) && 1) begin
        _minus_valid_7 <= 1;
      end 
      if(_times_ready_8 || !_times_valid_8) begin
        _times_data_reg_8 <= _times_odata_8;
      end 
      if(_times_ready_8 || !_times_valid_8) begin
        _times_valid_reg_8 <= _times_ovalid_8;
      end 
      if(_times_ready_9 || !_times_valid_9) begin
        _times_data_reg_9 <= _times_odata_9;
      end 
      if(_times_ready_9 || !_times_valid_9) begin
        _times_valid_reg_9 <= _times_ovalid_9;
      end 
      if(_times_ready_10 || !_times_valid_10) begin
        _times_data_reg_10 <= _times_odata_10;
      end 
      if(_times_ready_10 || !_times_valid_10) begin
        _times_valid_reg_10 <= _times_ovalid_10;
      end 
      if(_times_ready_11 || !_times_valid_11) begin
        _times_data_reg_11 <= _times_odata_11;
      end 
      if(_times_ready_11 || !_times_valid_11) begin
        _times_valid_reg_11 <= _times_ovalid_11;
      end 
      if(_times_ready_12 || !_times_valid_12) begin
        _times_data_reg_12 <= _times_odata_12;
      end 
      if(_times_ready_12 || !_times_valid_12) begin
        _times_valid_reg_12 <= _times_ovalid_12;
      end 
      if(_times_ready_13 || !_times_valid_13) begin
        _times_data_reg_13 <= _times_odata_13;
      end 
      if(_times_ready_13 || !_times_valid_13) begin
        _times_valid_reg_13 <= _times_ovalid_13;
      end 
      if(_times_ready_14 || !_times_valid_14) begin
        _times_data_reg_14 <= _times_odata_14;
      end 
      if(_times_ready_14 || !_times_valid_14) begin
        _times_valid_reg_14 <= _times_ovalid_14;
      end 
      if(_times_ready_15 || !_times_valid_15) begin
        _times_data_reg_15 <= _times_odata_15;
      end 
      if(_times_ready_15 || !_times_valid_15) begin
        _times_valid_reg_15 <= _times_ovalid_15;
      end 
      if((_plus_ready_16 || !_plus_valid_16) && (_plus_ready_0 && _plus_ready_4) && (_plus_valid_0 && _plus_valid_4)) begin
        _plus_data_16 <= _plus_data_0 + _plus_data_4;
      end 
      if(_plus_valid_16 && _plus_ready_16) begin
        _plus_valid_16 <= 0;
      end 
      if((_plus_ready_16 || !_plus_valid_16) && (_plus_ready_0 && _plus_ready_4)) begin
        _plus_valid_16 <= _plus_valid_0 && _plus_valid_4;
      end 
      if((_plus_ready_17 || !_plus_valid_17) && (_plus_ready_1 && _plus_ready_5) && (_plus_valid_1 && _plus_valid_5)) begin
        _plus_data_17 <= _plus_data_1 + _plus_data_5;
      end 
      if(_plus_valid_17 && _plus_ready_17) begin
        _plus_valid_17 <= 0;
      end 
      if((_plus_ready_17 || !_plus_valid_17) && (_plus_ready_1 && _plus_ready_5)) begin
        _plus_valid_17 <= _plus_valid_1 && _plus_valid_5;
      end 
      if((_minus_ready_18 || !_minus_valid_18) && (_plus_ready_0 && _plus_ready_4) && (_plus_valid_0 && _plus_valid_4)) begin
        _minus_data_18 <= _plus_data_0 - _plus_data_4;
      end 
      if(_minus_valid_18 && _minus_ready_18) begin
        _minus_valid_18 <= 0;
      end 
      if((_minus_ready_18 || !_minus_valid_18) && (_plus_ready_0 && _plus_ready_4)) begin
        _minus_valid_18 <= _plus_valid_0 && _plus_valid_4;
      end 
      if((_minus_ready_19 || !_minus_valid_19) && (_plus_ready_1 && _plus_ready_5) && (_plus_valid_1 && _plus_valid_5)) begin
        _minus_data_19 <= _plus_data_1 - _plus_data_5;
      end 
      if(_minus_valid_19 && _minus_ready_19) begin
        _minus_valid_19 <= 0;
      end 
      if((_minus_ready_19 || !_minus_valid_19) && (_plus_ready_1 && _plus_ready_5)) begin
        _minus_valid_19 <= _plus_valid_1 && _plus_valid_5;
      end 
      if(_times_ready_20 || !_times_valid_20) begin
        _times_data_reg_20 <= _times_odata_20;
      end 
      if(_times_ready_20 || !_times_valid_20) begin
        _times_valid_reg_20 <= _times_ovalid_20;
      end 
      if(_times_ready_21 || !_times_valid_21) begin
        _times_data_reg_21 <= _times_odata_21;
      end 
      if(_times_ready_21 || !_times_valid_21) begin
        _times_valid_reg_21 <= _times_ovalid_21;
      end 
      if(_times_ready_22 || !_times_valid_22) begin
        _times_data_reg_22 <= _times_odata_22;
      end 
      if(_times_ready_22 || !_times_valid_22) begin
        _times_valid_reg_22 <= _times_ovalid_22;
      end 
      if(_times_ready_23 || !_times_valid_23) begin
        _times_data_reg_23 <= _times_odata_23;
      end 
      if(_times_ready_23 || !_times_valid_23) begin
        _times_valid_reg_23 <= _times_ovalid_23;
      end 
      if((__delay_ready_24 || !__delay_valid_24) && _plus_ready_16 && _plus_valid_16) begin
        __delay_data_24 <= _plus_data_16;
      end 
      if(__delay_valid_24 && __delay_ready_24) begin
        __delay_valid_24 <= 0;
      end 
      if((__delay_ready_24 || !__delay_valid_24) && _plus_ready_16) begin
        __delay_valid_24 <= _plus_valid_16;
      end 
      if((__delay_ready_25 || !__delay_valid_25) && _plus_ready_17 && _plus_valid_17) begin
        __delay_data_25 <= _plus_data_17;
      end 
      if(__delay_valid_25 && __delay_ready_25) begin
        __delay_valid_25 <= 0;
      end 
      if((__delay_ready_25 || !__delay_valid_25) && _plus_ready_17) begin
        __delay_valid_25 <= _plus_valid_17;
      end 
      if((__delay_ready_26 || !__delay_valid_26) && __delay_ready_24 && __delay_valid_24) begin
        __delay_data_26 <= __delay_data_24;
      end 
      if(__delay_valid_26 && __delay_ready_26) begin
        __delay_valid_26 <= 0;
      end 
      if((__delay_ready_26 || !__delay_valid_26) && __delay_ready_24) begin
        __delay_valid_26 <= __delay_valid_24;
      end 
      if((__delay_ready_27 || !__delay_valid_27) && __delay_ready_25 && __delay_valid_25) begin
        __delay_data_27 <= __delay_data_25;
      end 
      if(__delay_valid_27 && __delay_ready_27) begin
        __delay_valid_27 <= 0;
      end 
      if((__delay_ready_27 || !__delay_valid_27) && __delay_ready_25) begin
        __delay_valid_27 <= __delay_valid_25;
      end 
      if((__delay_ready_28 || !__delay_valid_28) && __delay_ready_26 && __delay_valid_26) begin
        __delay_data_28 <= __delay_data_26;
      end 
      if(__delay_valid_28 && __delay_ready_28) begin
        __delay_valid_28 <= 0;
      end 
      if((__delay_ready_28 || !__delay_valid_28) && __delay_ready_26) begin
        __delay_valid_28 <= __delay_valid_26;
      end 
      if((__delay_ready_29 || !__delay_valid_29) && __delay_ready_27 && __delay_valid_27) begin
        __delay_data_29 <= __delay_data_27;
      end 
      if(__delay_valid_29 && __delay_ready_29) begin
        __delay_valid_29 <= 0;
      end 
      if((__delay_ready_29 || !__delay_valid_29) && __delay_ready_27) begin
        __delay_valid_29 <= __delay_valid_27;
      end 
      if((__delay_ready_30 || !__delay_valid_30) && __delay_ready_28 && __delay_valid_28) begin
        __delay_data_30 <= __delay_data_28;
      end 
      if(__delay_valid_30 && __delay_ready_30) begin
        __delay_valid_30 <= 0;
      end 
      if((__delay_ready_30 || !__delay_valid_30) && __delay_ready_28) begin
        __delay_valid_30 <= __delay_valid_28;
      end 
      if((__delay_ready_31 || !__delay_valid_31) && __delay_ready_29 && __delay_valid_29) begin
        __delay_data_31 <= __delay_data_29;
      end 
      if(__delay_valid_31 && __delay_ready_31) begin
        __delay_valid_31 <= 0;
      end 
      if((__delay_ready_31 || !__delay_valid_31) && __delay_ready_29) begin
        __delay_valid_31 <= __delay_valid_29;
      end 
      if((__delay_ready_32 || !__delay_valid_32) && __delay_ready_30 && __delay_valid_30) begin
        __delay_data_32 <= __delay_data_30;
      end 
      if(__delay_valid_32 && __delay_ready_32) begin
        __delay_valid_32 <= 0;
      end 
      if((__delay_ready_32 || !__delay_valid_32) && __delay_ready_30) begin
        __delay_valid_32 <= __delay_valid_30;
      end 
      if((__delay_ready_33 || !__delay_valid_33) && __delay_ready_31 && __delay_valid_31) begin
        __delay_data_33 <= __delay_data_31;
      end 
      if(__delay_valid_33 && __delay_ready_33) begin
        __delay_valid_33 <= 0;
      end 
      if((__delay_ready_33 || !__delay_valid_33) && __delay_ready_31) begin
        __delay_valid_33 <= __delay_valid_31;
      end 
      if((__delay_ready_34 || !__delay_valid_34) && __delay_ready_32 && __delay_valid_32) begin
        __delay_data_34 <= __delay_data_32;
      end 
      if(__delay_valid_34 && __delay_ready_34) begin
        __delay_valid_34 <= 0;
      end 
      if((__delay_ready_34 || !__delay_valid_34) && __delay_ready_32) begin
        __delay_valid_34 <= __delay_valid_32;
      end 
      if((__delay_ready_35 || !__delay_valid_35) && __delay_ready_33 && __delay_valid_33) begin
        __delay_data_35 <= __delay_data_33;
      end 
      if(__delay_valid_35 && __delay_ready_35) begin
        __delay_valid_35 <= 0;
      end 
      if((__delay_ready_35 || !__delay_valid_35) && __delay_ready_33) begin
        __delay_valid_35 <= __delay_valid_33;
      end 
      if((_minus_ready_36 || !_minus_valid_36) && (_times_ready_8 && _times_ready_9) && (_times_valid_8 && _times_valid_9)) begin
        _minus_data_36 <= _times_data_8 - _times_data_9;
      end 
      if(_minus_valid_36 && _minus_ready_36) begin
        _minus_valid_36 <= 0;
      end 
      if((_minus_ready_36 || !_minus_valid_36) && (_times_ready_8 && _times_ready_9)) begin
        _minus_valid_36 <= _times_valid_8 && _times_valid_9;
      end 
      if((_plus_ready_37 || !_plus_valid_37) && (_times_ready_10 && _times_ready_11) && (_times_valid_10 && _times_valid_11)) begin
        _plus_data_37 <= _times_data_10 + _times_data_11;
      end 
      if(_plus_valid_37 && _plus_ready_37) begin
        _plus_valid_37 <= 0;
      end 
      if((_plus_ready_37 || !_plus_valid_37) && (_times_ready_10 && _times_ready_11)) begin
        _plus_valid_37 <= _times_valid_10 && _times_valid_11;
      end 
      if((_minus_ready_38 || !_minus_valid_38) && (_times_ready_12 && _times_ready_13) && (_times_valid_12 && _times_valid_13)) begin
        _minus_data_38 <= _times_data_12 - _times_data_13;
      end 
      if(_minus_valid_38 && _minus_ready_38) begin
        _minus_valid_38 <= 0;
      end 
      if((_minus_ready_38 || !_minus_valid_38) && (_times_ready_12 && _times_ready_13)) begin
        _minus_valid_38 <= _times_valid_12 && _times_valid_13;
      end 
      if((_plus_ready_39 || !_plus_valid_39) && (_times_ready_14 && _times_ready_15) && (_times_valid_14 && _times_valid_15)) begin
        _plus_data_39 <= _times_data_14 + _times_data_15;
      end 
      if(_plus_valid_39 && _plus_ready_39) begin
        _plus_valid_39 <= 0;
      end 
      if((_plus_ready_39 || !_plus_valid_39) && (_times_ready_14 && _times_ready_15)) begin
        _plus_valid_39 <= _times_valid_14 && _times_valid_15;
      end 
      if((__delay_ready_40 || !__delay_valid_40) && __delay_ready_34 && __delay_valid_34) begin
        __delay_data_40 <= __delay_data_34;
      end 
      if(__delay_valid_40 && __delay_ready_40) begin
        __delay_valid_40 <= 0;
      end 
      if((__delay_ready_40 || !__delay_valid_40) && __delay_ready_34) begin
        __delay_valid_40 <= __delay_valid_34;
      end 
      if((__delay_ready_41 || !__delay_valid_41) && __delay_ready_35 && __delay_valid_35) begin
        __delay_data_41 <= __delay_data_35;
      end 
      if(__delay_valid_41 && __delay_ready_41) begin
        __delay_valid_41 <= 0;
      end 
      if((__delay_ready_41 || !__delay_valid_41) && __delay_ready_35) begin
        __delay_valid_41 <= __delay_valid_35;
      end 
      if((_minus_ready_42 || !_minus_valid_42) && (_times_ready_20 && _times_ready_21) && (_times_valid_20 && _times_valid_21)) begin
        _minus_data_42 <= _times_data_20 - _times_data_21;
      end 
      if(_minus_valid_42 && _minus_ready_42) begin
        _minus_valid_42 <= 0;
      end 
      if((_minus_ready_42 || !_minus_valid_42) && (_times_ready_20 && _times_ready_21)) begin
        _minus_valid_42 <= _times_valid_20 && _times_valid_21;
      end 
      if((_plus_ready_43 || !_plus_valid_43) && (_times_ready_22 && _times_ready_23) && (_times_valid_22 && _times_valid_23)) begin
        _plus_data_43 <= _times_data_22 + _times_data_23;
      end 
      if(_plus_valid_43 && _plus_ready_43) begin
        _plus_valid_43 <= 0;
      end 
      if((_plus_ready_43 || !_plus_valid_43) && (_times_ready_22 && _times_ready_23)) begin
        _plus_valid_43 <= _times_valid_22 && _times_valid_23;
      end 
      if((_plus_ready_44 || !_plus_valid_44) && (_minus_ready_36 && _minus_ready_38) && (_minus_valid_36 && _minus_valid_38)) begin
        _plus_data_44 <= _minus_data_36 + _minus_data_38;
      end 
      if(_plus_valid_44 && _plus_ready_44) begin
        _plus_valid_44 <= 0;
      end 
      if((_plus_ready_44 || !_plus_valid_44) && (_minus_ready_36 && _minus_ready_38)) begin
        _plus_valid_44 <= _minus_valid_36 && _minus_valid_38;
      end 
      if((_plus_ready_45 || !_plus_valid_45) && (_plus_ready_37 && _plus_ready_39) && (_plus_valid_37 && _plus_valid_39)) begin
        _plus_data_45 <= _plus_data_37 + _plus_data_39;
      end 
      if(_plus_valid_45 && _plus_ready_45) begin
        _plus_valid_45 <= 0;
      end 
      if((_plus_ready_45 || !_plus_valid_45) && (_plus_ready_37 && _plus_ready_39)) begin
        _plus_valid_45 <= _plus_valid_37 && _plus_valid_39;
      end 
      if((_minus_ready_46 || !_minus_valid_46) && (_minus_ready_36 && _minus_ready_38) && (_minus_valid_36 && _minus_valid_38)) begin
        _minus_data_46 <= _minus_data_36 - _minus_data_38;
      end 
      if(_minus_valid_46 && _minus_ready_46) begin
        _minus_valid_46 <= 0;
      end 
      if((_minus_ready_46 || !_minus_valid_46) && (_minus_ready_36 && _minus_ready_38)) begin
        _minus_valid_46 <= _minus_valid_36 && _minus_valid_38;
      end 
      if((_minus_ready_47 || !_minus_valid_47) && (_plus_ready_37 && _plus_ready_39) && (_plus_valid_37 && _plus_valid_39)) begin
        _minus_data_47 <= _plus_data_37 - _plus_data_39;
      end 
      if(_minus_valid_47 && _minus_ready_47) begin
        _minus_valid_47 <= 0;
      end 
      if((_minus_ready_47 || !_minus_valid_47) && (_plus_ready_37 && _plus_ready_39)) begin
        _minus_valid_47 <= _plus_valid_37 && _plus_valid_39;
      end 
      if((__delay_ready_48 || !__delay_valid_48) && __delay_ready_40 && __delay_valid_40) begin
        __delay_data_48 <= __delay_data_40;
      end 
      if(__delay_valid_48 && __delay_ready_48) begin
        __delay_valid_48 <= 0;
      end 
      if((__delay_ready_48 || !__delay_valid_48) && __delay_ready_40) begin
        __delay_valid_48 <= __delay_valid_40;
      end 
      if((__delay_ready_49 || !__delay_valid_49) && __delay_ready_41 && __delay_valid_41) begin
        __delay_data_49 <= __delay_data_41;
      end 
      if(__delay_valid_49 && __delay_ready_49) begin
        __delay_valid_49 <= 0;
      end 
      if((__delay_ready_49 || !__delay_valid_49) && __delay_ready_41) begin
        __delay_valid_49 <= __delay_valid_41;
      end 
      if(_times_ready_50 || !_times_valid_50) begin
        _times_data_reg_50 <= _times_odata_50;
      end 
      if(_times_ready_50 || !_times_valid_50) begin
        _times_valid_reg_50 <= _times_ovalid_50;
      end 
      if(_times_ready_51 || !_times_valid_51) begin
        _times_data_reg_51 <= _times_odata_51;
      end 
      if(_times_ready_51 || !_times_valid_51) begin
        _times_valid_reg_51 <= _times_ovalid_51;
      end 
      if(_times_ready_52 || !_times_valid_52) begin
        _times_data_reg_52 <= _times_odata_52;
      end 
      if(_times_ready_52 || !_times_valid_52) begin
        _times_valid_reg_52 <= _times_ovalid_52;
      end 
      if(_times_ready_53 || !_times_valid_53) begin
        _times_data_reg_53 <= _times_odata_53;
      end 
      if(_times_ready_53 || !_times_valid_53) begin
        _times_valid_reg_53 <= _times_ovalid_53;
      end 
      if((__delay_ready_54 || !__delay_valid_54) && __delay_ready_48 && __delay_valid_48) begin
        __delay_data_54 <= __delay_data_48;
      end 
      if(__delay_valid_54 && __delay_ready_54) begin
        __delay_valid_54 <= 0;
      end 
      if((__delay_ready_54 || !__delay_valid_54) && __delay_ready_48) begin
        __delay_valid_54 <= __delay_valid_48;
      end 
      if((__delay_ready_55 || !__delay_valid_55) && __delay_ready_49 && __delay_valid_49) begin
        __delay_data_55 <= __delay_data_49;
      end 
      if(__delay_valid_55 && __delay_ready_55) begin
        __delay_valid_55 <= 0;
      end 
      if((__delay_ready_55 || !__delay_valid_55) && __delay_ready_49) begin
        __delay_valid_55 <= __delay_valid_49;
      end 
      if((__delay_ready_56 || !__delay_valid_56) && _minus_ready_42 && _minus_valid_42) begin
        __delay_data_56 <= _minus_data_42;
      end 
      if(__delay_valid_56 && __delay_ready_56) begin
        __delay_valid_56 <= 0;
      end 
      if((__delay_ready_56 || !__delay_valid_56) && _minus_ready_42) begin
        __delay_valid_56 <= _minus_valid_42;
      end 
      if((__delay_ready_57 || !__delay_valid_57) && _plus_ready_43 && _plus_valid_43) begin
        __delay_data_57 <= _plus_data_43;
      end 
      if(__delay_valid_57 && __delay_ready_57) begin
        __delay_valid_57 <= 0;
      end 
      if((__delay_ready_57 || !__delay_valid_57) && _plus_ready_43) begin
        __delay_valid_57 <= _plus_valid_43;
      end 
      if((__delay_ready_58 || !__delay_valid_58) && _plus_ready_44 && _plus_valid_44) begin
        __delay_data_58 <= _plus_data_44;
      end 
      if(__delay_valid_58 && __delay_ready_58) begin
        __delay_valid_58 <= 0;
      end 
      if((__delay_ready_58 || !__delay_valid_58) && _plus_ready_44) begin
        __delay_valid_58 <= _plus_valid_44;
      end 
      if((__delay_ready_59 || !__delay_valid_59) && _plus_ready_45 && _plus_valid_45) begin
        __delay_data_59 <= _plus_data_45;
      end 
      if(__delay_valid_59 && __delay_ready_59) begin
        __delay_valid_59 <= 0;
      end 
      if((__delay_ready_59 || !__delay_valid_59) && _plus_ready_45) begin
        __delay_valid_59 <= _plus_valid_45;
      end 
      if((__delay_ready_60 || !__delay_valid_60) && __delay_ready_54 && __delay_valid_54) begin
        __delay_data_60 <= __delay_data_54;
      end 
      if(__delay_valid_60 && __delay_ready_60) begin
        __delay_valid_60 <= 0;
      end 
      if((__delay_ready_60 || !__delay_valid_60) && __delay_ready_54) begin
        __delay_valid_60 <= __delay_valid_54;
      end 
      if((__delay_ready_61 || !__delay_valid_61) && __delay_ready_55 && __delay_valid_55) begin
        __delay_data_61 <= __delay_data_55;
      end 
      if(__delay_valid_61 && __delay_ready_61) begin
        __delay_valid_61 <= 0;
      end 
      if((__delay_ready_61 || !__delay_valid_61) && __delay_ready_55) begin
        __delay_valid_61 <= __delay_valid_55;
      end 
      if((__delay_ready_62 || !__delay_valid_62) && __delay_ready_56 && __delay_valid_56) begin
        __delay_data_62 <= __delay_data_56;
      end 
      if(__delay_valid_62 && __delay_ready_62) begin
        __delay_valid_62 <= 0;
      end 
      if((__delay_ready_62 || !__delay_valid_62) && __delay_ready_56) begin
        __delay_valid_62 <= __delay_valid_56;
      end 
      if((__delay_ready_63 || !__delay_valid_63) && __delay_ready_57 && __delay_valid_57) begin
        __delay_data_63 <= __delay_data_57;
      end 
      if(__delay_valid_63 && __delay_ready_63) begin
        __delay_valid_63 <= 0;
      end 
      if((__delay_ready_63 || !__delay_valid_63) && __delay_ready_57) begin
        __delay_valid_63 <= __delay_valid_57;
      end 
      if((__delay_ready_64 || !__delay_valid_64) && __delay_ready_58 && __delay_valid_58) begin
        __delay_data_64 <= __delay_data_58;
      end 
      if(__delay_valid_64 && __delay_ready_64) begin
        __delay_valid_64 <= 0;
      end 
      if((__delay_ready_64 || !__delay_valid_64) && __delay_ready_58) begin
        __delay_valid_64 <= __delay_valid_58;
      end 
      if((__delay_ready_65 || !__delay_valid_65) && __delay_ready_59 && __delay_valid_59) begin
        __delay_data_65 <= __delay_data_59;
      end 
      if(__delay_valid_65 && __delay_ready_65) begin
        __delay_valid_65 <= 0;
      end 
      if((__delay_ready_65 || !__delay_valid_65) && __delay_ready_59) begin
        __delay_valid_65 <= __delay_valid_59;
      end 
      if((__delay_ready_66 || !__delay_valid_66) && __delay_ready_60 && __delay_valid_60) begin
        __delay_data_66 <= __delay_data_60;
      end 
      if(__delay_valid_66 && __delay_ready_66) begin
        __delay_valid_66 <= 0;
      end 
      if((__delay_ready_66 || !__delay_valid_66) && __delay_ready_60) begin
        __delay_valid_66 <= __delay_valid_60;
      end 
      if((__delay_ready_67 || !__delay_valid_67) && __delay_ready_61 && __delay_valid_61) begin
        __delay_data_67 <= __delay_data_61;
      end 
      if(__delay_valid_67 && __delay_ready_67) begin
        __delay_valid_67 <= 0;
      end 
      if((__delay_ready_67 || !__delay_valid_67) && __delay_ready_61) begin
        __delay_valid_67 <= __delay_valid_61;
      end 
      if((__delay_ready_68 || !__delay_valid_68) && __delay_ready_62 && __delay_valid_62) begin
        __delay_data_68 <= __delay_data_62;
      end 
      if(__delay_valid_68 && __delay_ready_68) begin
        __delay_valid_68 <= 0;
      end 
      if((__delay_ready_68 || !__delay_valid_68) && __delay_ready_62) begin
        __delay_valid_68 <= __delay_valid_62;
      end 
      if((__delay_ready_69 || !__delay_valid_69) && __delay_ready_63 && __delay_valid_63) begin
        __delay_data_69 <= __delay_data_63;
      end 
      if(__delay_valid_69 && __delay_ready_69) begin
        __delay_valid_69 <= 0;
      end 
      if((__delay_ready_69 || !__delay_valid_69) && __delay_ready_63) begin
        __delay_valid_69 <= __delay_valid_63;
      end 
      if((__delay_ready_70 || !__delay_valid_70) && __delay_ready_64 && __delay_valid_64) begin
        __delay_data_70 <= __delay_data_64;
      end 
      if(__delay_valid_70 && __delay_ready_70) begin
        __delay_valid_70 <= 0;
      end 
      if((__delay_ready_70 || !__delay_valid_70) && __delay_ready_64) begin
        __delay_valid_70 <= __delay_valid_64;
      end 
      if((__delay_ready_71 || !__delay_valid_71) && __delay_ready_65 && __delay_valid_65) begin
        __delay_data_71 <= __delay_data_65;
      end 
      if(__delay_valid_71 && __delay_ready_71) begin
        __delay_valid_71 <= 0;
      end 
      if((__delay_ready_71 || !__delay_valid_71) && __delay_ready_65) begin
        __delay_valid_71 <= __delay_valid_65;
      end 
      if((__delay_ready_72 || !__delay_valid_72) && __delay_ready_66 && __delay_valid_66) begin
        __delay_data_72 <= __delay_data_66;
      end 
      if(__delay_valid_72 && __delay_ready_72) begin
        __delay_valid_72 <= 0;
      end 
      if((__delay_ready_72 || !__delay_valid_72) && __delay_ready_66) begin
        __delay_valid_72 <= __delay_valid_66;
      end 
      if((__delay_ready_73 || !__delay_valid_73) && __delay_ready_67 && __delay_valid_67) begin
        __delay_data_73 <= __delay_data_67;
      end 
      if(__delay_valid_73 && __delay_ready_73) begin
        __delay_valid_73 <= 0;
      end 
      if((__delay_ready_73 || !__delay_valid_73) && __delay_ready_67) begin
        __delay_valid_73 <= __delay_valid_67;
      end 
      if((__delay_ready_74 || !__delay_valid_74) && __delay_ready_68 && __delay_valid_68) begin
        __delay_data_74 <= __delay_data_68;
      end 
      if(__delay_valid_74 && __delay_ready_74) begin
        __delay_valid_74 <= 0;
      end 
      if((__delay_ready_74 || !__delay_valid_74) && __delay_ready_68) begin
        __delay_valid_74 <= __delay_valid_68;
      end 
      if((__delay_ready_75 || !__delay_valid_75) && __delay_ready_69 && __delay_valid_69) begin
        __delay_data_75 <= __delay_data_69;
      end 
      if(__delay_valid_75 && __delay_ready_75) begin
        __delay_valid_75 <= 0;
      end 
      if((__delay_ready_75 || !__delay_valid_75) && __delay_ready_69) begin
        __delay_valid_75 <= __delay_valid_69;
      end 
      if((__delay_ready_76 || !__delay_valid_76) && __delay_ready_70 && __delay_valid_70) begin
        __delay_data_76 <= __delay_data_70;
      end 
      if(__delay_valid_76 && __delay_ready_76) begin
        __delay_valid_76 <= 0;
      end 
      if((__delay_ready_76 || !__delay_valid_76) && __delay_ready_70) begin
        __delay_valid_76 <= __delay_valid_70;
      end 
      if((__delay_ready_77 || !__delay_valid_77) && __delay_ready_71 && __delay_valid_71) begin
        __delay_data_77 <= __delay_data_71;
      end 
      if(__delay_valid_77 && __delay_ready_77) begin
        __delay_valid_77 <= 0;
      end 
      if((__delay_ready_77 || !__delay_valid_77) && __delay_ready_71) begin
        __delay_valid_77 <= __delay_valid_71;
      end 
      if((__delay_ready_78 || !__delay_valid_78) && __delay_ready_72 && __delay_valid_72) begin
        __delay_data_78 <= __delay_data_72;
      end 
      if(__delay_valid_78 && __delay_ready_78) begin
        __delay_valid_78 <= 0;
      end 
      if((__delay_ready_78 || !__delay_valid_78) && __delay_ready_72) begin
        __delay_valid_78 <= __delay_valid_72;
      end 
      if((__delay_ready_79 || !__delay_valid_79) && __delay_ready_73 && __delay_valid_73) begin
        __delay_data_79 <= __delay_data_73;
      end 
      if(__delay_valid_79 && __delay_ready_79) begin
        __delay_valid_79 <= 0;
      end 
      if((__delay_ready_79 || !__delay_valid_79) && __delay_ready_73) begin
        __delay_valid_79 <= __delay_valid_73;
      end 
      if((__delay_ready_80 || !__delay_valid_80) && __delay_ready_74 && __delay_valid_74) begin
        __delay_data_80 <= __delay_data_74;
      end 
      if(__delay_valid_80 && __delay_ready_80) begin
        __delay_valid_80 <= 0;
      end 
      if((__delay_ready_80 || !__delay_valid_80) && __delay_ready_74) begin
        __delay_valid_80 <= __delay_valid_74;
      end 
      if((__delay_ready_81 || !__delay_valid_81) && __delay_ready_75 && __delay_valid_75) begin
        __delay_data_81 <= __delay_data_75;
      end 
      if(__delay_valid_81 && __delay_ready_81) begin
        __delay_valid_81 <= 0;
      end 
      if((__delay_ready_81 || !__delay_valid_81) && __delay_ready_75) begin
        __delay_valid_81 <= __delay_valid_75;
      end 
      if((__delay_ready_82 || !__delay_valid_82) && __delay_ready_76 && __delay_valid_76) begin
        __delay_data_82 <= __delay_data_76;
      end 
      if(__delay_valid_82 && __delay_ready_82) begin
        __delay_valid_82 <= 0;
      end 
      if((__delay_ready_82 || !__delay_valid_82) && __delay_ready_76) begin
        __delay_valid_82 <= __delay_valid_76;
      end 
      if((__delay_ready_83 || !__delay_valid_83) && __delay_ready_77 && __delay_valid_77) begin
        __delay_data_83 <= __delay_data_77;
      end 
      if(__delay_valid_83 && __delay_ready_83) begin
        __delay_valid_83 <= 0;
      end 
      if((__delay_ready_83 || !__delay_valid_83) && __delay_ready_77) begin
        __delay_valid_83 <= __delay_valid_77;
      end 
      if((__delay_ready_84 || !__delay_valid_84) && __delay_ready_78 && __delay_valid_78) begin
        __delay_data_84 <= __delay_data_78;
      end 
      if(__delay_valid_84 && __delay_ready_84) begin
        __delay_valid_84 <= 0;
      end 
      if((__delay_ready_84 || !__delay_valid_84) && __delay_ready_78) begin
        __delay_valid_84 <= __delay_valid_78;
      end 
      if((__delay_ready_85 || !__delay_valid_85) && __delay_ready_79 && __delay_valid_79) begin
        __delay_data_85 <= __delay_data_79;
      end 
      if(__delay_valid_85 && __delay_ready_85) begin
        __delay_valid_85 <= 0;
      end 
      if((__delay_ready_85 || !__delay_valid_85) && __delay_ready_79) begin
        __delay_valid_85 <= __delay_valid_79;
      end 
      if((__delay_ready_86 || !__delay_valid_86) && __delay_ready_80 && __delay_valid_80) begin
        __delay_data_86 <= __delay_data_80;
      end 
      if(__delay_valid_86 && __delay_ready_86) begin
        __delay_valid_86 <= 0;
      end 
      if((__delay_ready_86 || !__delay_valid_86) && __delay_ready_80) begin
        __delay_valid_86 <= __delay_valid_80;
      end 
      if((__delay_ready_87 || !__delay_valid_87) && __delay_ready_81 && __delay_valid_81) begin
        __delay_data_87 <= __delay_data_81;
      end 
      if(__delay_valid_87 && __delay_ready_87) begin
        __delay_valid_87 <= 0;
      end 
      if((__delay_ready_87 || !__delay_valid_87) && __delay_ready_81) begin
        __delay_valid_87 <= __delay_valid_81;
      end 
      if((__delay_ready_88 || !__delay_valid_88) && __delay_ready_82 && __delay_valid_82) begin
        __delay_data_88 <= __delay_data_82;
      end 
      if(__delay_valid_88 && __delay_ready_88) begin
        __delay_valid_88 <= 0;
      end 
      if((__delay_ready_88 || !__delay_valid_88) && __delay_ready_82) begin
        __delay_valid_88 <= __delay_valid_82;
      end 
      if((__delay_ready_89 || !__delay_valid_89) && __delay_ready_83 && __delay_valid_83) begin
        __delay_data_89 <= __delay_data_83;
      end 
      if(__delay_valid_89 && __delay_ready_89) begin
        __delay_valid_89 <= 0;
      end 
      if((__delay_ready_89 || !__delay_valid_89) && __delay_ready_83) begin
        __delay_valid_89 <= __delay_valid_83;
      end 
      if((__delay_ready_90 || !__delay_valid_90) && __delay_ready_84 && __delay_valid_84) begin
        __delay_data_90 <= __delay_data_84;
      end 
      if(__delay_valid_90 && __delay_ready_90) begin
        __delay_valid_90 <= 0;
      end 
      if((__delay_ready_90 || !__delay_valid_90) && __delay_ready_84) begin
        __delay_valid_90 <= __delay_valid_84;
      end 
      if((__delay_ready_91 || !__delay_valid_91) && __delay_ready_85 && __delay_valid_85) begin
        __delay_data_91 <= __delay_data_85;
      end 
      if(__delay_valid_91 && __delay_ready_91) begin
        __delay_valid_91 <= 0;
      end 
      if((__delay_ready_91 || !__delay_valid_91) && __delay_ready_85) begin
        __delay_valid_91 <= __delay_valid_85;
      end 
      if((__delay_ready_92 || !__delay_valid_92) && __delay_ready_86 && __delay_valid_86) begin
        __delay_data_92 <= __delay_data_86;
      end 
      if(__delay_valid_92 && __delay_ready_92) begin
        __delay_valid_92 <= 0;
      end 
      if((__delay_ready_92 || !__delay_valid_92) && __delay_ready_86) begin
        __delay_valid_92 <= __delay_valid_86;
      end 
      if((__delay_ready_93 || !__delay_valid_93) && __delay_ready_87 && __delay_valid_87) begin
        __delay_data_93 <= __delay_data_87;
      end 
      if(__delay_valid_93 && __delay_ready_93) begin
        __delay_valid_93 <= 0;
      end 
      if((__delay_ready_93 || !__delay_valid_93) && __delay_ready_87) begin
        __delay_valid_93 <= __delay_valid_87;
      end 
      if((__delay_ready_94 || !__delay_valid_94) && __delay_ready_88 && __delay_valid_88) begin
        __delay_data_94 <= __delay_data_88;
      end 
      if(__delay_valid_94 && __delay_ready_94) begin
        __delay_valid_94 <= 0;
      end 
      if((__delay_ready_94 || !__delay_valid_94) && __delay_ready_88) begin
        __delay_valid_94 <= __delay_valid_88;
      end 
      if((__delay_ready_95 || !__delay_valid_95) && __delay_ready_89 && __delay_valid_89) begin
        __delay_data_95 <= __delay_data_89;
      end 
      if(__delay_valid_95 && __delay_ready_95) begin
        __delay_valid_95 <= 0;
      end 
      if((__delay_ready_95 || !__delay_valid_95) && __delay_ready_89) begin
        __delay_valid_95 <= __delay_valid_89;
      end 
      if((_minus_ready_96 || !_minus_valid_96) && (_times_ready_50 && _times_ready_51) && (_times_valid_50 && _times_valid_51)) begin
        _minus_data_96 <= _times_data_50 - _times_data_51;
      end 
      if(_minus_valid_96 && _minus_ready_96) begin
        _minus_valid_96 <= 0;
      end 
      if((_minus_ready_96 || !_minus_valid_96) && (_times_ready_50 && _times_ready_51)) begin
        _minus_valid_96 <= _times_valid_50 && _times_valid_51;
      end 
      if((_plus_ready_97 || !_plus_valid_97) && (_times_ready_52 && _times_ready_53) && (_times_valid_52 && _times_valid_53)) begin
        _plus_data_97 <= _times_data_52 + _times_data_53;
      end 
      if(_plus_valid_97 && _plus_ready_97) begin
        _plus_valid_97 <= 0;
      end 
      if((_plus_ready_97 || !_plus_valid_97) && (_times_ready_52 && _times_ready_53)) begin
        _plus_valid_97 <= _times_valid_52 && _times_valid_53;
      end 
      if((__delay_ready_98 || !__delay_valid_98) && __delay_ready_90 && __delay_valid_90) begin
        __delay_data_98 <= __delay_data_90;
      end 
      if(__delay_valid_98 && __delay_ready_98) begin
        __delay_valid_98 <= 0;
      end 
      if((__delay_ready_98 || !__delay_valid_98) && __delay_ready_90) begin
        __delay_valid_98 <= __delay_valid_90;
      end 
      if((__delay_ready_99 || !__delay_valid_99) && __delay_ready_91 && __delay_valid_91) begin
        __delay_data_99 <= __delay_data_91;
      end 
      if(__delay_valid_99 && __delay_ready_99) begin
        __delay_valid_99 <= 0;
      end 
      if((__delay_ready_99 || !__delay_valid_99) && __delay_ready_91) begin
        __delay_valid_99 <= __delay_valid_91;
      end 
      if((__delay_ready_100 || !__delay_valid_100) && __delay_ready_92 && __delay_valid_92) begin
        __delay_data_100 <= __delay_data_92;
      end 
      if(__delay_valid_100 && __delay_ready_100) begin
        __delay_valid_100 <= 0;
      end 
      if((__delay_ready_100 || !__delay_valid_100) && __delay_ready_92) begin
        __delay_valid_100 <= __delay_valid_92;
      end 
      if((__delay_ready_101 || !__delay_valid_101) && __delay_ready_93 && __delay_valid_93) begin
        __delay_data_101 <= __delay_data_93;
      end 
      if(__delay_valid_101 && __delay_ready_101) begin
        __delay_valid_101 <= 0;
      end 
      if((__delay_ready_101 || !__delay_valid_101) && __delay_ready_93) begin
        __delay_valid_101 <= __delay_valid_93;
      end 
      if((__delay_ready_102 || !__delay_valid_102) && __delay_ready_94 && __delay_valid_94) begin
        __delay_data_102 <= __delay_data_94;
      end 
      if(__delay_valid_102 && __delay_ready_102) begin
        __delay_valid_102 <= 0;
      end 
      if((__delay_ready_102 || !__delay_valid_102) && __delay_ready_94) begin
        __delay_valid_102 <= __delay_valid_94;
      end 
      if((__delay_ready_103 || !__delay_valid_103) && __delay_ready_95 && __delay_valid_95) begin
        __delay_data_103 <= __delay_data_95;
      end 
      if(__delay_valid_103 && __delay_ready_103) begin
        __delay_valid_103 <= 0;
      end 
      if((__delay_ready_103 || !__delay_valid_103) && __delay_ready_95) begin
        __delay_valid_103 <= __delay_valid_95;
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
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_1
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_1
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_1
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_2
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_2
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_2
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_3
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_3
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_3
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_4
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_4
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_4
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_5
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_5
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_5
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_6
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_6
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_6
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_7
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_7
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_7
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_8
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_8
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_8
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_9
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_9
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_9
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_10
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_10
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_10
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_11
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_11
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_11
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_12
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_12
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_12
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_13
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_13
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_13
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_14
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
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


  multiplier_core_14
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_14
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [1-1:0] b,
  output [17-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [1-1:0] _b;
  wire signed [17-1:0] _mul;
  reg signed [17-1:0] _pipe_mul0;
  reg signed [17-1:0] _pipe_mul1;
  reg signed [17-1:0] _pipe_mul2;
  reg signed [17-1:0] _pipe_mul3;
  reg signed [17-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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



module multiplier_15
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
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


  multiplier_core_15
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_15
(
  input CLK,
  input update,
  input [16-1:0] a,
  input [2-1:0] b,
  output [18-1:0] c
);

  reg signed [16-1:0] _a;
  reg signed [2-1:0] _b;
  wire signed [18-1:0] _mul;
  reg signed [18-1:0] _pipe_mul0;
  reg signed [18-1:0] _pipe_mul1;
  reg signed [18-1:0] _pipe_mul2;
  reg signed [18-1:0] _pipe_mul3;
  reg signed [18-1:0] _pipe_mul4;
  assign _mul = _a * _b;
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
    test_module = dataflow_fft4.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
