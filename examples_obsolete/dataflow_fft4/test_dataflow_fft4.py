from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_fft4

expected_verilog = """

module test
(

);

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

  reg signed [16-1:0] _dataflow_plus_data_8;
  reg _dataflow_plus_valid_8;
  wire _dataflow_plus_ready_8;
  reg signed [16-1:0] _dataflow_plus_data_9;
  reg _dataflow_plus_valid_9;
  wire _dataflow_plus_ready_9;
  reg signed [16-1:0] _dataflow_minus_data_10;
  reg _dataflow_minus_valid_10;
  wire _dataflow_minus_ready_10;
  reg signed [16-1:0] _dataflow_minus_data_11;
  reg _dataflow_minus_valid_11;
  wire _dataflow_minus_ready_11;
  reg signed [16-1:0] _dataflow_plus_data_22;
  reg _dataflow_plus_valid_22;
  wire _dataflow_plus_ready_22;
  reg signed [16-1:0] _dataflow_plus_data_23;
  reg _dataflow_plus_valid_23;
  wire _dataflow_plus_ready_23;
  reg signed [16-1:0] _dataflow_minus_data_24;
  reg _dataflow_minus_valid_24;
  wire _dataflow_minus_ready_24;
  reg signed [16-1:0] _dataflow_minus_data_25;
  reg _dataflow_minus_valid_25;
  wire _dataflow_minus_ready_25;
  wire signed [16-1:0] _dataflow_times_data_12;
  wire _dataflow_times_valid_12;
  wire _dataflow_times_ready_12;
  wire signed [18-1:0] _dataflow_times_mul_odata_12;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_12;
  assign _dataflow_times_data_12 = _dataflow_times_mul_odata_reg_12;
  wire _dataflow_times_mul_ovalid_12;
  reg _dataflow_times_mul_valid_reg_12;
  assign _dataflow_times_valid_12 = _dataflow_times_mul_valid_reg_12;
  wire _dataflow_times_mul_enable_12;
  wire _dataflow_times_mul_update_12;
  assign _dataflow_times_mul_enable_12 = (_dataflow_times_ready_12 || !_dataflow_times_valid_12) && _dataflow_minus_ready_10 && _dataflow_minus_valid_10;
  assign _dataflow_times_mul_update_12 = _dataflow_times_ready_12 || !_dataflow_times_valid_12;

  multiplier_0
  _dataflow_times_mul_12
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_12),
    .enable(_dataflow_times_mul_enable_12),
    .valid(_dataflow_times_mul_ovalid_12),
    .a(_dataflow_minus_data_10),
    .b(2'sd1),
    .c(_dataflow_times_mul_odata_12)
  );

  wire signed [16-1:0] _dataflow_times_data_14;
  wire _dataflow_times_valid_14;
  wire _dataflow_times_ready_14;
  wire signed [17-1:0] _dataflow_times_mul_odata_14;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_14;
  assign _dataflow_times_data_14 = _dataflow_times_mul_odata_reg_14;
  wire _dataflow_times_mul_ovalid_14;
  reg _dataflow_times_mul_valid_reg_14;
  assign _dataflow_times_valid_14 = _dataflow_times_mul_valid_reg_14;
  wire _dataflow_times_mul_enable_14;
  wire _dataflow_times_mul_update_14;
  assign _dataflow_times_mul_enable_14 = (_dataflow_times_ready_14 || !_dataflow_times_valid_14) && _dataflow_minus_ready_11 && _dataflow_minus_valid_11;
  assign _dataflow_times_mul_update_14 = _dataflow_times_ready_14 || !_dataflow_times_valid_14;

  multiplier_1
  _dataflow_times_mul_14
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_14),
    .enable(_dataflow_times_mul_enable_14),
    .valid(_dataflow_times_mul_ovalid_14),
    .a(_dataflow_minus_data_11),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_14)
  );

  wire signed [16-1:0] _dataflow_times_data_16;
  wire _dataflow_times_valid_16;
  wire _dataflow_times_ready_16;
  wire signed [17-1:0] _dataflow_times_mul_odata_16;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_16;
  assign _dataflow_times_data_16 = _dataflow_times_mul_odata_reg_16;
  wire _dataflow_times_mul_ovalid_16;
  reg _dataflow_times_mul_valid_reg_16;
  assign _dataflow_times_valid_16 = _dataflow_times_mul_valid_reg_16;
  wire _dataflow_times_mul_enable_16;
  wire _dataflow_times_mul_update_16;
  assign _dataflow_times_mul_enable_16 = (_dataflow_times_ready_16 || !_dataflow_times_valid_16) && _dataflow_minus_ready_10 && _dataflow_minus_valid_10;
  assign _dataflow_times_mul_update_16 = _dataflow_times_ready_16 || !_dataflow_times_valid_16;

  multiplier_2
  _dataflow_times_mul_16
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_16),
    .enable(_dataflow_times_mul_enable_16),
    .valid(_dataflow_times_mul_ovalid_16),
    .a(_dataflow_minus_data_10),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_16)
  );

  assign _dataflow_minus_ready_10 = (_dataflow_times_ready_12 || !_dataflow_times_valid_12) && _dataflow_minus_valid_10 && ((_dataflow_times_ready_16 || !_dataflow_times_valid_16) && _dataflow_minus_valid_10);
  wire signed [16-1:0] _dataflow_times_data_18;
  wire _dataflow_times_valid_18;
  wire _dataflow_times_ready_18;
  wire signed [18-1:0] _dataflow_times_mul_odata_18;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_18;
  assign _dataflow_times_data_18 = _dataflow_times_mul_odata_reg_18;
  wire _dataflow_times_mul_ovalid_18;
  reg _dataflow_times_mul_valid_reg_18;
  assign _dataflow_times_valid_18 = _dataflow_times_mul_valid_reg_18;
  wire _dataflow_times_mul_enable_18;
  wire _dataflow_times_mul_update_18;
  assign _dataflow_times_mul_enable_18 = (_dataflow_times_ready_18 || !_dataflow_times_valid_18) && _dataflow_minus_ready_11 && _dataflow_minus_valid_11;
  assign _dataflow_times_mul_update_18 = _dataflow_times_ready_18 || !_dataflow_times_valid_18;

  multiplier_3
  _dataflow_times_mul_18
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_18),
    .enable(_dataflow_times_mul_enable_18),
    .valid(_dataflow_times_mul_ovalid_18),
    .a(_dataflow_minus_data_11),
    .b(2'sd1),
    .c(_dataflow_times_mul_odata_18)
  );

  assign _dataflow_minus_ready_11 = (_dataflow_times_ready_14 || !_dataflow_times_valid_14) && _dataflow_minus_valid_11 && ((_dataflow_times_ready_18 || !_dataflow_times_valid_18) && _dataflow_minus_valid_11);
  wire signed [16-1:0] _dataflow_times_data_26;
  wire _dataflow_times_valid_26;
  wire _dataflow_times_ready_26;
  wire signed [17-1:0] _dataflow_times_mul_odata_26;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_26;
  assign _dataflow_times_data_26 = _dataflow_times_mul_odata_reg_26;
  wire _dataflow_times_mul_ovalid_26;
  reg _dataflow_times_mul_valid_reg_26;
  assign _dataflow_times_valid_26 = _dataflow_times_mul_valid_reg_26;
  wire _dataflow_times_mul_enable_26;
  wire _dataflow_times_mul_update_26;
  assign _dataflow_times_mul_enable_26 = (_dataflow_times_ready_26 || !_dataflow_times_valid_26) && _dataflow_minus_ready_24 && _dataflow_minus_valid_24;
  assign _dataflow_times_mul_update_26 = _dataflow_times_ready_26 || !_dataflow_times_valid_26;

  multiplier_4
  _dataflow_times_mul_26
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_26),
    .enable(_dataflow_times_mul_enable_26),
    .valid(_dataflow_times_mul_ovalid_26),
    .a(_dataflow_minus_data_24),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_26)
  );

  wire signed [16-1:0] _dataflow_times_data_28;
  wire _dataflow_times_valid_28;
  wire _dataflow_times_ready_28;
  wire signed [18-1:0] _dataflow_times_mul_odata_28;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_28;
  assign _dataflow_times_data_28 = _dataflow_times_mul_odata_reg_28;
  wire _dataflow_times_mul_ovalid_28;
  reg _dataflow_times_mul_valid_reg_28;
  assign _dataflow_times_valid_28 = _dataflow_times_mul_valid_reg_28;
  wire _dataflow_times_mul_enable_28;
  wire _dataflow_times_mul_update_28;
  assign _dataflow_times_mul_enable_28 = (_dataflow_times_ready_28 || !_dataflow_times_valid_28) && _dataflow_minus_ready_25 && _dataflow_minus_valid_25;
  assign _dataflow_times_mul_update_28 = _dataflow_times_ready_28 || !_dataflow_times_valid_28;

  multiplier_5
  _dataflow_times_mul_28
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_28),
    .enable(_dataflow_times_mul_enable_28),
    .valid(_dataflow_times_mul_ovalid_28),
    .a(_dataflow_minus_data_25),
    .b(-2'sd1),
    .c(_dataflow_times_mul_odata_28)
  );

  wire signed [16-1:0] _dataflow_times_data_30;
  wire _dataflow_times_valid_30;
  wire _dataflow_times_ready_30;
  wire signed [18-1:0] _dataflow_times_mul_odata_30;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_30;
  assign _dataflow_times_data_30 = _dataflow_times_mul_odata_reg_30;
  wire _dataflow_times_mul_ovalid_30;
  reg _dataflow_times_mul_valid_reg_30;
  assign _dataflow_times_valid_30 = _dataflow_times_mul_valid_reg_30;
  wire _dataflow_times_mul_enable_30;
  wire _dataflow_times_mul_update_30;
  assign _dataflow_times_mul_enable_30 = (_dataflow_times_ready_30 || !_dataflow_times_valid_30) && _dataflow_minus_ready_24 && _dataflow_minus_valid_24;
  assign _dataflow_times_mul_update_30 = _dataflow_times_ready_30 || !_dataflow_times_valid_30;

  multiplier_6
  _dataflow_times_mul_30
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_30),
    .enable(_dataflow_times_mul_enable_30),
    .valid(_dataflow_times_mul_ovalid_30),
    .a(_dataflow_minus_data_24),
    .b(-2'sd1),
    .c(_dataflow_times_mul_odata_30)
  );

  assign _dataflow_minus_ready_24 = (_dataflow_times_ready_26 || !_dataflow_times_valid_26) && _dataflow_minus_valid_24 && ((_dataflow_times_ready_30 || !_dataflow_times_valid_30) && _dataflow_minus_valid_24);
  wire signed [16-1:0] _dataflow_times_data_32;
  wire _dataflow_times_valid_32;
  wire _dataflow_times_ready_32;
  wire signed [17-1:0] _dataflow_times_mul_odata_32;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_32;
  assign _dataflow_times_data_32 = _dataflow_times_mul_odata_reg_32;
  wire _dataflow_times_mul_ovalid_32;
  reg _dataflow_times_mul_valid_reg_32;
  assign _dataflow_times_valid_32 = _dataflow_times_mul_valid_reg_32;
  wire _dataflow_times_mul_enable_32;
  wire _dataflow_times_mul_update_32;
  assign _dataflow_times_mul_enable_32 = (_dataflow_times_ready_32 || !_dataflow_times_valid_32) && _dataflow_minus_ready_25 && _dataflow_minus_valid_25;
  assign _dataflow_times_mul_update_32 = _dataflow_times_ready_32 || !_dataflow_times_valid_32;

  multiplier_7
  _dataflow_times_mul_32
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_32),
    .enable(_dataflow_times_mul_enable_32),
    .valid(_dataflow_times_mul_ovalid_32),
    .a(_dataflow_minus_data_25),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_32)
  );

  assign _dataflow_minus_ready_25 = (_dataflow_times_ready_28 || !_dataflow_times_valid_28) && _dataflow_minus_valid_25 && ((_dataflow_times_ready_32 || !_dataflow_times_valid_32) && _dataflow_minus_valid_25);
  reg signed [16-1:0] _dataflow_plus_data_36;
  reg _dataflow_plus_valid_36;
  wire _dataflow_plus_ready_36;
  reg signed [16-1:0] _dataflow_plus_data_37;
  reg _dataflow_plus_valid_37;
  wire _dataflow_plus_ready_37;
  reg signed [16-1:0] _dataflow_minus_data_38;
  reg _dataflow_minus_valid_38;
  wire _dataflow_minus_ready_38;
  assign _dataflow_plus_ready_8 = (_dataflow_plus_ready_36 || !_dataflow_plus_valid_36) && (_dataflow_plus_valid_8 && _dataflow_plus_valid_22) && ((_dataflow_minus_ready_38 || !_dataflow_minus_valid_38) && (_dataflow_plus_valid_8 && _dataflow_plus_valid_22));
  assign _dataflow_plus_ready_22 = (_dataflow_plus_ready_36 || !_dataflow_plus_valid_36) && (_dataflow_plus_valid_8 && _dataflow_plus_valid_22) && ((_dataflow_minus_ready_38 || !_dataflow_minus_valid_38) && (_dataflow_plus_valid_8 && _dataflow_plus_valid_22));
  reg signed [16-1:0] _dataflow_minus_data_39;
  reg _dataflow_minus_valid_39;
  wire _dataflow_minus_ready_39;
  assign _dataflow_plus_ready_9 = (_dataflow_plus_ready_37 || !_dataflow_plus_valid_37) && (_dataflow_plus_valid_9 && _dataflow_plus_valid_23) && ((_dataflow_minus_ready_39 || !_dataflow_minus_valid_39) && (_dataflow_plus_valid_9 && _dataflow_plus_valid_23));
  assign _dataflow_plus_ready_23 = (_dataflow_plus_ready_37 || !_dataflow_plus_valid_37) && (_dataflow_plus_valid_9 && _dataflow_plus_valid_23) && ((_dataflow_minus_ready_39 || !_dataflow_minus_valid_39) && (_dataflow_plus_valid_9 && _dataflow_plus_valid_23));
  wire signed [16-1:0] _dataflow_times_data_40;
  wire _dataflow_times_valid_40;
  wire _dataflow_times_ready_40;
  wire signed [18-1:0] _dataflow_times_mul_odata_40;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_40;
  assign _dataflow_times_data_40 = _dataflow_times_mul_odata_reg_40;
  wire _dataflow_times_mul_ovalid_40;
  reg _dataflow_times_mul_valid_reg_40;
  assign _dataflow_times_valid_40 = _dataflow_times_mul_valid_reg_40;
  wire _dataflow_times_mul_enable_40;
  wire _dataflow_times_mul_update_40;
  assign _dataflow_times_mul_enable_40 = (_dataflow_times_ready_40 || !_dataflow_times_valid_40) && _dataflow_minus_ready_38 && _dataflow_minus_valid_38;
  assign _dataflow_times_mul_update_40 = _dataflow_times_ready_40 || !_dataflow_times_valid_40;

  multiplier_8
  _dataflow_times_mul_40
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_40),
    .enable(_dataflow_times_mul_enable_40),
    .valid(_dataflow_times_mul_ovalid_40),
    .a(_dataflow_minus_data_38),
    .b(2'sd1),
    .c(_dataflow_times_mul_odata_40)
  );

  wire signed [16-1:0] _dataflow_times_data_42;
  wire _dataflow_times_valid_42;
  wire _dataflow_times_ready_42;
  wire signed [17-1:0] _dataflow_times_mul_odata_42;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_42;
  assign _dataflow_times_data_42 = _dataflow_times_mul_odata_reg_42;
  wire _dataflow_times_mul_ovalid_42;
  reg _dataflow_times_mul_valid_reg_42;
  assign _dataflow_times_valid_42 = _dataflow_times_mul_valid_reg_42;
  wire _dataflow_times_mul_enable_42;
  wire _dataflow_times_mul_update_42;
  assign _dataflow_times_mul_enable_42 = (_dataflow_times_ready_42 || !_dataflow_times_valid_42) && _dataflow_minus_ready_39 && _dataflow_minus_valid_39;
  assign _dataflow_times_mul_update_42 = _dataflow_times_ready_42 || !_dataflow_times_valid_42;

  multiplier_9
  _dataflow_times_mul_42
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_42),
    .enable(_dataflow_times_mul_enable_42),
    .valid(_dataflow_times_mul_ovalid_42),
    .a(_dataflow_minus_data_39),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_42)
  );

  wire signed [16-1:0] _dataflow_times_data_44;
  wire _dataflow_times_valid_44;
  wire _dataflow_times_ready_44;
  wire signed [17-1:0] _dataflow_times_mul_odata_44;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_44;
  assign _dataflow_times_data_44 = _dataflow_times_mul_odata_reg_44;
  wire _dataflow_times_mul_ovalid_44;
  reg _dataflow_times_mul_valid_reg_44;
  assign _dataflow_times_valid_44 = _dataflow_times_mul_valid_reg_44;
  wire _dataflow_times_mul_enable_44;
  wire _dataflow_times_mul_update_44;
  assign _dataflow_times_mul_enable_44 = (_dataflow_times_ready_44 || !_dataflow_times_valid_44) && _dataflow_minus_ready_38 && _dataflow_minus_valid_38;
  assign _dataflow_times_mul_update_44 = _dataflow_times_ready_44 || !_dataflow_times_valid_44;

  multiplier_10
  _dataflow_times_mul_44
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_44),
    .enable(_dataflow_times_mul_enable_44),
    .valid(_dataflow_times_mul_ovalid_44),
    .a(_dataflow_minus_data_38),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_44)
  );

  assign _dataflow_minus_ready_38 = (_dataflow_times_ready_40 || !_dataflow_times_valid_40) && _dataflow_minus_valid_38 && ((_dataflow_times_ready_44 || !_dataflow_times_valid_44) && _dataflow_minus_valid_38);
  wire signed [16-1:0] _dataflow_times_data_46;
  wire _dataflow_times_valid_46;
  wire _dataflow_times_ready_46;
  wire signed [18-1:0] _dataflow_times_mul_odata_46;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_46;
  assign _dataflow_times_data_46 = _dataflow_times_mul_odata_reg_46;
  wire _dataflow_times_mul_ovalid_46;
  reg _dataflow_times_mul_valid_reg_46;
  assign _dataflow_times_valid_46 = _dataflow_times_mul_valid_reg_46;
  wire _dataflow_times_mul_enable_46;
  wire _dataflow_times_mul_update_46;
  assign _dataflow_times_mul_enable_46 = (_dataflow_times_ready_46 || !_dataflow_times_valid_46) && _dataflow_minus_ready_39 && _dataflow_minus_valid_39;
  assign _dataflow_times_mul_update_46 = _dataflow_times_ready_46 || !_dataflow_times_valid_46;

  multiplier_11
  _dataflow_times_mul_46
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_46),
    .enable(_dataflow_times_mul_enable_46),
    .valid(_dataflow_times_mul_ovalid_46),
    .a(_dataflow_minus_data_39),
    .b(2'sd1),
    .c(_dataflow_times_mul_odata_46)
  );

  assign _dataflow_minus_ready_39 = (_dataflow_times_ready_42 || !_dataflow_times_valid_42) && _dataflow_minus_valid_39 && ((_dataflow_times_ready_46 || !_dataflow_times_valid_46) && _dataflow_minus_valid_39);
  reg signed [16-1:0] _dataflow__delay_data_64;
  reg _dataflow__delay_valid_64;
  wire _dataflow__delay_ready_64;
  assign _dataflow_plus_ready_36 = (_dataflow__delay_ready_64 || !_dataflow__delay_valid_64) && _dataflow_plus_valid_36;
  reg signed [16-1:0] _dataflow__delay_data_80;
  reg _dataflow__delay_valid_80;
  wire _dataflow__delay_ready_80;
  assign _dataflow_plus_ready_37 = (_dataflow__delay_ready_80 || !_dataflow__delay_valid_80) && _dataflow_plus_valid_37;
  reg signed [16-1:0] _dataflow__delay_data_65;
  reg _dataflow__delay_valid_65;
  wire _dataflow__delay_ready_65;
  assign _dataflow__delay_ready_64 = (_dataflow__delay_ready_65 || !_dataflow__delay_valid_65) && _dataflow__delay_valid_64;
  reg signed [16-1:0] _dataflow__delay_data_81;
  reg _dataflow__delay_valid_81;
  wire _dataflow__delay_ready_81;
  assign _dataflow__delay_ready_80 = (_dataflow__delay_ready_81 || !_dataflow__delay_valid_81) && _dataflow__delay_valid_80;
  reg signed [16-1:0] _dataflow__delay_data_66;
  reg _dataflow__delay_valid_66;
  wire _dataflow__delay_ready_66;
  assign _dataflow__delay_ready_65 = (_dataflow__delay_ready_66 || !_dataflow__delay_valid_66) && _dataflow__delay_valid_65;
  reg signed [16-1:0] _dataflow__delay_data_82;
  reg _dataflow__delay_valid_82;
  wire _dataflow__delay_ready_82;
  assign _dataflow__delay_ready_81 = (_dataflow__delay_ready_82 || !_dataflow__delay_valid_82) && _dataflow__delay_valid_81;
  reg signed [16-1:0] _dataflow__delay_data_67;
  reg _dataflow__delay_valid_67;
  wire _dataflow__delay_ready_67;
  assign _dataflow__delay_ready_66 = (_dataflow__delay_ready_67 || !_dataflow__delay_valid_67) && _dataflow__delay_valid_66;
  reg signed [16-1:0] _dataflow__delay_data_83;
  reg _dataflow__delay_valid_83;
  wire _dataflow__delay_ready_83;
  assign _dataflow__delay_ready_82 = (_dataflow__delay_ready_83 || !_dataflow__delay_valid_83) && _dataflow__delay_valid_82;
  reg signed [16-1:0] _dataflow__delay_data_68;
  reg _dataflow__delay_valid_68;
  wire _dataflow__delay_ready_68;
  assign _dataflow__delay_ready_67 = (_dataflow__delay_ready_68 || !_dataflow__delay_valid_68) && _dataflow__delay_valid_67;
  reg signed [16-1:0] _dataflow__delay_data_84;
  reg _dataflow__delay_valid_84;
  wire _dataflow__delay_ready_84;
  assign _dataflow__delay_ready_83 = (_dataflow__delay_ready_84 || !_dataflow__delay_valid_84) && _dataflow__delay_valid_83;
  reg signed [16-1:0] _dataflow__delay_data_69;
  reg _dataflow__delay_valid_69;
  wire _dataflow__delay_ready_69;
  assign _dataflow__delay_ready_68 = (_dataflow__delay_ready_69 || !_dataflow__delay_valid_69) && _dataflow__delay_valid_68;
  reg signed [16-1:0] _dataflow__delay_data_85;
  reg _dataflow__delay_valid_85;
  wire _dataflow__delay_ready_85;
  assign _dataflow__delay_ready_84 = (_dataflow__delay_ready_85 || !_dataflow__delay_valid_85) && _dataflow__delay_valid_84;
  reg signed [16-1:0] _dataflow_minus_data_20;
  reg _dataflow_minus_valid_20;
  wire _dataflow_minus_ready_20;
  assign _dataflow_times_ready_12 = (_dataflow_minus_ready_20 || !_dataflow_minus_valid_20) && (_dataflow_times_valid_12 && _dataflow_times_valid_14);
  assign _dataflow_times_ready_14 = (_dataflow_minus_ready_20 || !_dataflow_minus_valid_20) && (_dataflow_times_valid_12 && _dataflow_times_valid_14);
  reg signed [16-1:0] _dataflow_plus_data_21;
  reg _dataflow_plus_valid_21;
  wire _dataflow_plus_ready_21;
  assign _dataflow_times_ready_16 = (_dataflow_plus_ready_21 || !_dataflow_plus_valid_21) && (_dataflow_times_valid_16 && _dataflow_times_valid_18);
  assign _dataflow_times_ready_18 = (_dataflow_plus_ready_21 || !_dataflow_plus_valid_21) && (_dataflow_times_valid_16 && _dataflow_times_valid_18);
  reg signed [16-1:0] _dataflow_minus_data_34;
  reg _dataflow_minus_valid_34;
  wire _dataflow_minus_ready_34;
  assign _dataflow_times_ready_26 = (_dataflow_minus_ready_34 || !_dataflow_minus_valid_34) && (_dataflow_times_valid_26 && _dataflow_times_valid_28);
  assign _dataflow_times_ready_28 = (_dataflow_minus_ready_34 || !_dataflow_minus_valid_34) && (_dataflow_times_valid_26 && _dataflow_times_valid_28);
  reg signed [16-1:0] _dataflow_plus_data_35;
  reg _dataflow_plus_valid_35;
  wire _dataflow_plus_ready_35;
  assign _dataflow_times_ready_30 = (_dataflow_plus_ready_35 || !_dataflow_plus_valid_35) && (_dataflow_times_valid_30 && _dataflow_times_valid_32);
  assign _dataflow_times_ready_32 = (_dataflow_plus_ready_35 || !_dataflow_plus_valid_35) && (_dataflow_times_valid_30 && _dataflow_times_valid_32);
  reg signed [16-1:0] _dataflow__delay_data_70;
  reg _dataflow__delay_valid_70;
  wire _dataflow__delay_ready_70;
  assign _dataflow__delay_ready_69 = (_dataflow__delay_ready_70 || !_dataflow__delay_valid_70) && _dataflow__delay_valid_69;
  reg signed [16-1:0] _dataflow__delay_data_86;
  reg _dataflow__delay_valid_86;
  wire _dataflow__delay_ready_86;
  assign _dataflow__delay_ready_85 = (_dataflow__delay_ready_86 || !_dataflow__delay_valid_86) && _dataflow__delay_valid_85;
  reg signed [16-1:0] _dataflow_minus_data_48;
  reg _dataflow_minus_valid_48;
  wire _dataflow_minus_ready_48;
  assign _dataflow_times_ready_40 = (_dataflow_minus_ready_48 || !_dataflow_minus_valid_48) && (_dataflow_times_valid_40 && _dataflow_times_valid_42);
  assign _dataflow_times_ready_42 = (_dataflow_minus_ready_48 || !_dataflow_minus_valid_48) && (_dataflow_times_valid_40 && _dataflow_times_valid_42);
  reg signed [16-1:0] _dataflow_plus_data_49;
  reg _dataflow_plus_valid_49;
  wire _dataflow_plus_ready_49;
  assign _dataflow_times_ready_44 = (_dataflow_plus_ready_49 || !_dataflow_plus_valid_49) && (_dataflow_times_valid_44 && _dataflow_times_valid_46);
  assign _dataflow_times_ready_46 = (_dataflow_plus_ready_49 || !_dataflow_plus_valid_49) && (_dataflow_times_valid_44 && _dataflow_times_valid_46);
  reg signed [16-1:0] _dataflow_plus_data_50;
  reg _dataflow_plus_valid_50;
  wire _dataflow_plus_ready_50;
  reg signed [16-1:0] _dataflow_plus_data_51;
  reg _dataflow_plus_valid_51;
  wire _dataflow_plus_ready_51;
  reg signed [16-1:0] _dataflow_minus_data_52;
  reg _dataflow_minus_valid_52;
  wire _dataflow_minus_ready_52;
  assign _dataflow_minus_ready_20 = (_dataflow_plus_ready_50 || !_dataflow_plus_valid_50) && (_dataflow_minus_valid_20 && _dataflow_minus_valid_34) && ((_dataflow_minus_ready_52 || !_dataflow_minus_valid_52) && (_dataflow_minus_valid_20 && _dataflow_minus_valid_34));
  assign _dataflow_minus_ready_34 = (_dataflow_plus_ready_50 || !_dataflow_plus_valid_50) && (_dataflow_minus_valid_20 && _dataflow_minus_valid_34) && ((_dataflow_minus_ready_52 || !_dataflow_minus_valid_52) && (_dataflow_minus_valid_20 && _dataflow_minus_valid_34));
  reg signed [16-1:0] _dataflow_minus_data_53;
  reg _dataflow_minus_valid_53;
  wire _dataflow_minus_ready_53;
  assign _dataflow_plus_ready_21 = (_dataflow_plus_ready_51 || !_dataflow_plus_valid_51) && (_dataflow_plus_valid_21 && _dataflow_plus_valid_35) && ((_dataflow_minus_ready_53 || !_dataflow_minus_valid_53) && (_dataflow_plus_valid_21 && _dataflow_plus_valid_35));
  assign _dataflow_plus_ready_35 = (_dataflow_plus_ready_51 || !_dataflow_plus_valid_51) && (_dataflow_plus_valid_21 && _dataflow_plus_valid_35) && ((_dataflow_minus_ready_53 || !_dataflow_minus_valid_53) && (_dataflow_plus_valid_21 && _dataflow_plus_valid_35));
  reg signed [16-1:0] _dataflow__delay_data_71;
  reg _dataflow__delay_valid_71;
  wire _dataflow__delay_ready_71;
  assign _dataflow__delay_ready_70 = (_dataflow__delay_ready_71 || !_dataflow__delay_valid_71) && _dataflow__delay_valid_70;
  reg signed [16-1:0] _dataflow__delay_data_87;
  reg _dataflow__delay_valid_87;
  wire _dataflow__delay_ready_87;
  assign _dataflow__delay_ready_86 = (_dataflow__delay_ready_87 || !_dataflow__delay_valid_87) && _dataflow__delay_valid_86;
  wire signed [16-1:0] _dataflow_times_data_54;
  wire _dataflow_times_valid_54;
  wire _dataflow_times_ready_54;
  wire signed [18-1:0] _dataflow_times_mul_odata_54;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_54;
  assign _dataflow_times_data_54 = _dataflow_times_mul_odata_reg_54;
  wire _dataflow_times_mul_ovalid_54;
  reg _dataflow_times_mul_valid_reg_54;
  assign _dataflow_times_valid_54 = _dataflow_times_mul_valid_reg_54;
  wire _dataflow_times_mul_enable_54;
  wire _dataflow_times_mul_update_54;
  assign _dataflow_times_mul_enable_54 = (_dataflow_times_ready_54 || !_dataflow_times_valid_54) && _dataflow_minus_ready_52 && _dataflow_minus_valid_52;
  assign _dataflow_times_mul_update_54 = _dataflow_times_ready_54 || !_dataflow_times_valid_54;

  multiplier_12
  _dataflow_times_mul_54
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_54),
    .enable(_dataflow_times_mul_enable_54),
    .valid(_dataflow_times_mul_ovalid_54),
    .a(_dataflow_minus_data_52),
    .b(2'sd1),
    .c(_dataflow_times_mul_odata_54)
  );

  wire signed [16-1:0] _dataflow_times_data_56;
  wire _dataflow_times_valid_56;
  wire _dataflow_times_ready_56;
  wire signed [17-1:0] _dataflow_times_mul_odata_56;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_56;
  assign _dataflow_times_data_56 = _dataflow_times_mul_odata_reg_56;
  wire _dataflow_times_mul_ovalid_56;
  reg _dataflow_times_mul_valid_reg_56;
  assign _dataflow_times_valid_56 = _dataflow_times_mul_valid_reg_56;
  wire _dataflow_times_mul_enable_56;
  wire _dataflow_times_mul_update_56;
  assign _dataflow_times_mul_enable_56 = (_dataflow_times_ready_56 || !_dataflow_times_valid_56) && _dataflow_minus_ready_53 && _dataflow_minus_valid_53;
  assign _dataflow_times_mul_update_56 = _dataflow_times_ready_56 || !_dataflow_times_valid_56;

  multiplier_13
  _dataflow_times_mul_56
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_56),
    .enable(_dataflow_times_mul_enable_56),
    .valid(_dataflow_times_mul_ovalid_56),
    .a(_dataflow_minus_data_53),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_56)
  );

  wire signed [16-1:0] _dataflow_times_data_58;
  wire _dataflow_times_valid_58;
  wire _dataflow_times_ready_58;
  wire signed [17-1:0] _dataflow_times_mul_odata_58;
  reg signed [17-1:0] _dataflow_times_mul_odata_reg_58;
  assign _dataflow_times_data_58 = _dataflow_times_mul_odata_reg_58;
  wire _dataflow_times_mul_ovalid_58;
  reg _dataflow_times_mul_valid_reg_58;
  assign _dataflow_times_valid_58 = _dataflow_times_mul_valid_reg_58;
  wire _dataflow_times_mul_enable_58;
  wire _dataflow_times_mul_update_58;
  assign _dataflow_times_mul_enable_58 = (_dataflow_times_ready_58 || !_dataflow_times_valid_58) && _dataflow_minus_ready_52 && _dataflow_minus_valid_52;
  assign _dataflow_times_mul_update_58 = _dataflow_times_ready_58 || !_dataflow_times_valid_58;

  multiplier_14
  _dataflow_times_mul_58
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_58),
    .enable(_dataflow_times_mul_enable_58),
    .valid(_dataflow_times_mul_ovalid_58),
    .a(_dataflow_minus_data_52),
    .b(1'sd0),
    .c(_dataflow_times_mul_odata_58)
  );

  assign _dataflow_minus_ready_52 = (_dataflow_times_ready_54 || !_dataflow_times_valid_54) && _dataflow_minus_valid_52 && ((_dataflow_times_ready_58 || !_dataflow_times_valid_58) && _dataflow_minus_valid_52);
  wire signed [16-1:0] _dataflow_times_data_60;
  wire _dataflow_times_valid_60;
  wire _dataflow_times_ready_60;
  wire signed [18-1:0] _dataflow_times_mul_odata_60;
  reg signed [18-1:0] _dataflow_times_mul_odata_reg_60;
  assign _dataflow_times_data_60 = _dataflow_times_mul_odata_reg_60;
  wire _dataflow_times_mul_ovalid_60;
  reg _dataflow_times_mul_valid_reg_60;
  assign _dataflow_times_valid_60 = _dataflow_times_mul_valid_reg_60;
  wire _dataflow_times_mul_enable_60;
  wire _dataflow_times_mul_update_60;
  assign _dataflow_times_mul_enable_60 = (_dataflow_times_ready_60 || !_dataflow_times_valid_60) && _dataflow_minus_ready_53 && _dataflow_minus_valid_53;
  assign _dataflow_times_mul_update_60 = _dataflow_times_ready_60 || !_dataflow_times_valid_60;

  multiplier_15
  _dataflow_times_mul_60
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_60),
    .enable(_dataflow_times_mul_enable_60),
    .valid(_dataflow_times_mul_ovalid_60),
    .a(_dataflow_minus_data_53),
    .b(2'sd1),
    .c(_dataflow_times_mul_odata_60)
  );

  assign _dataflow_minus_ready_53 = (_dataflow_times_ready_56 || !_dataflow_times_valid_56) && _dataflow_minus_valid_53 && ((_dataflow_times_ready_60 || !_dataflow_times_valid_60) && _dataflow_minus_valid_53);
  reg signed [16-1:0] _dataflow__delay_data_72;
  reg _dataflow__delay_valid_72;
  wire _dataflow__delay_ready_72;
  assign _dataflow__delay_ready_71 = (_dataflow__delay_ready_72 || !_dataflow__delay_valid_72) && _dataflow__delay_valid_71;
  reg signed [16-1:0] _dataflow__delay_data_88;
  reg _dataflow__delay_valid_88;
  wire _dataflow__delay_ready_88;
  assign _dataflow__delay_ready_87 = (_dataflow__delay_ready_88 || !_dataflow__delay_valid_88) && _dataflow__delay_valid_87;
  reg signed [16-1:0] _dataflow__delay_data_96;
  reg _dataflow__delay_valid_96;
  wire _dataflow__delay_ready_96;
  assign _dataflow_minus_ready_48 = (_dataflow__delay_ready_96 || !_dataflow__delay_valid_96) && _dataflow_minus_valid_48;
  reg signed [16-1:0] _dataflow__delay_data_104;
  reg _dataflow__delay_valid_104;
  wire _dataflow__delay_ready_104;
  assign _dataflow_plus_ready_49 = (_dataflow__delay_ready_104 || !_dataflow__delay_valid_104) && _dataflow_plus_valid_49;
  reg signed [16-1:0] _dataflow__delay_data_112;
  reg _dataflow__delay_valid_112;
  wire _dataflow__delay_ready_112;
  assign _dataflow_plus_ready_50 = (_dataflow__delay_ready_112 || !_dataflow__delay_valid_112) && _dataflow_plus_valid_50;
  reg signed [16-1:0] _dataflow__delay_data_120;
  reg _dataflow__delay_valid_120;
  wire _dataflow__delay_ready_120;
  assign _dataflow_plus_ready_51 = (_dataflow__delay_ready_120 || !_dataflow__delay_valid_120) && _dataflow_plus_valid_51;
  reg signed [16-1:0] _dataflow__delay_data_73;
  reg _dataflow__delay_valid_73;
  wire _dataflow__delay_ready_73;
  assign _dataflow__delay_ready_72 = (_dataflow__delay_ready_73 || !_dataflow__delay_valid_73) && _dataflow__delay_valid_72;
  reg signed [16-1:0] _dataflow__delay_data_89;
  reg _dataflow__delay_valid_89;
  wire _dataflow__delay_ready_89;
  assign _dataflow__delay_ready_88 = (_dataflow__delay_ready_89 || !_dataflow__delay_valid_89) && _dataflow__delay_valid_88;
  reg signed [16-1:0] _dataflow__delay_data_97;
  reg _dataflow__delay_valid_97;
  wire _dataflow__delay_ready_97;
  assign _dataflow__delay_ready_96 = (_dataflow__delay_ready_97 || !_dataflow__delay_valid_97) && _dataflow__delay_valid_96;
  reg signed [16-1:0] _dataflow__delay_data_105;
  reg _dataflow__delay_valid_105;
  wire _dataflow__delay_ready_105;
  assign _dataflow__delay_ready_104 = (_dataflow__delay_ready_105 || !_dataflow__delay_valid_105) && _dataflow__delay_valid_104;
  reg signed [16-1:0] _dataflow__delay_data_113;
  reg _dataflow__delay_valid_113;
  wire _dataflow__delay_ready_113;
  assign _dataflow__delay_ready_112 = (_dataflow__delay_ready_113 || !_dataflow__delay_valid_113) && _dataflow__delay_valid_112;
  reg signed [16-1:0] _dataflow__delay_data_121;
  reg _dataflow__delay_valid_121;
  wire _dataflow__delay_ready_121;
  assign _dataflow__delay_ready_120 = (_dataflow__delay_ready_121 || !_dataflow__delay_valid_121) && _dataflow__delay_valid_120;
  reg signed [16-1:0] _dataflow__delay_data_74;
  reg _dataflow__delay_valid_74;
  wire _dataflow__delay_ready_74;
  assign _dataflow__delay_ready_73 = (_dataflow__delay_ready_74 || !_dataflow__delay_valid_74) && _dataflow__delay_valid_73;
  reg signed [16-1:0] _dataflow__delay_data_90;
  reg _dataflow__delay_valid_90;
  wire _dataflow__delay_ready_90;
  assign _dataflow__delay_ready_89 = (_dataflow__delay_ready_90 || !_dataflow__delay_valid_90) && _dataflow__delay_valid_89;
  reg signed [16-1:0] _dataflow__delay_data_98;
  reg _dataflow__delay_valid_98;
  wire _dataflow__delay_ready_98;
  assign _dataflow__delay_ready_97 = (_dataflow__delay_ready_98 || !_dataflow__delay_valid_98) && _dataflow__delay_valid_97;
  reg signed [16-1:0] _dataflow__delay_data_106;
  reg _dataflow__delay_valid_106;
  wire _dataflow__delay_ready_106;
  assign _dataflow__delay_ready_105 = (_dataflow__delay_ready_106 || !_dataflow__delay_valid_106) && _dataflow__delay_valid_105;
  reg signed [16-1:0] _dataflow__delay_data_114;
  reg _dataflow__delay_valid_114;
  wire _dataflow__delay_ready_114;
  assign _dataflow__delay_ready_113 = (_dataflow__delay_ready_114 || !_dataflow__delay_valid_114) && _dataflow__delay_valid_113;
  reg signed [16-1:0] _dataflow__delay_data_122;
  reg _dataflow__delay_valid_122;
  wire _dataflow__delay_ready_122;
  assign _dataflow__delay_ready_121 = (_dataflow__delay_ready_122 || !_dataflow__delay_valid_122) && _dataflow__delay_valid_121;
  reg signed [16-1:0] _dataflow__delay_data_75;
  reg _dataflow__delay_valid_75;
  wire _dataflow__delay_ready_75;
  assign _dataflow__delay_ready_74 = (_dataflow__delay_ready_75 || !_dataflow__delay_valid_75) && _dataflow__delay_valid_74;
  reg signed [16-1:0] _dataflow__delay_data_91;
  reg _dataflow__delay_valid_91;
  wire _dataflow__delay_ready_91;
  assign _dataflow__delay_ready_90 = (_dataflow__delay_ready_91 || !_dataflow__delay_valid_91) && _dataflow__delay_valid_90;
  reg signed [16-1:0] _dataflow__delay_data_99;
  reg _dataflow__delay_valid_99;
  wire _dataflow__delay_ready_99;
  assign _dataflow__delay_ready_98 = (_dataflow__delay_ready_99 || !_dataflow__delay_valid_99) && _dataflow__delay_valid_98;
  reg signed [16-1:0] _dataflow__delay_data_107;
  reg _dataflow__delay_valid_107;
  wire _dataflow__delay_ready_107;
  assign _dataflow__delay_ready_106 = (_dataflow__delay_ready_107 || !_dataflow__delay_valid_107) && _dataflow__delay_valid_106;
  reg signed [16-1:0] _dataflow__delay_data_115;
  reg _dataflow__delay_valid_115;
  wire _dataflow__delay_ready_115;
  assign _dataflow__delay_ready_114 = (_dataflow__delay_ready_115 || !_dataflow__delay_valid_115) && _dataflow__delay_valid_114;
  reg signed [16-1:0] _dataflow__delay_data_123;
  reg _dataflow__delay_valid_123;
  wire _dataflow__delay_ready_123;
  assign _dataflow__delay_ready_122 = (_dataflow__delay_ready_123 || !_dataflow__delay_valid_123) && _dataflow__delay_valid_122;
  reg signed [16-1:0] _dataflow__delay_data_76;
  reg _dataflow__delay_valid_76;
  wire _dataflow__delay_ready_76;
  assign _dataflow__delay_ready_75 = (_dataflow__delay_ready_76 || !_dataflow__delay_valid_76) && _dataflow__delay_valid_75;
  reg signed [16-1:0] _dataflow__delay_data_92;
  reg _dataflow__delay_valid_92;
  wire _dataflow__delay_ready_92;
  assign _dataflow__delay_ready_91 = (_dataflow__delay_ready_92 || !_dataflow__delay_valid_92) && _dataflow__delay_valid_91;
  reg signed [16-1:0] _dataflow__delay_data_100;
  reg _dataflow__delay_valid_100;
  wire _dataflow__delay_ready_100;
  assign _dataflow__delay_ready_99 = (_dataflow__delay_ready_100 || !_dataflow__delay_valid_100) && _dataflow__delay_valid_99;
  reg signed [16-1:0] _dataflow__delay_data_108;
  reg _dataflow__delay_valid_108;
  wire _dataflow__delay_ready_108;
  assign _dataflow__delay_ready_107 = (_dataflow__delay_ready_108 || !_dataflow__delay_valid_108) && _dataflow__delay_valid_107;
  reg signed [16-1:0] _dataflow__delay_data_116;
  reg _dataflow__delay_valid_116;
  wire _dataflow__delay_ready_116;
  assign _dataflow__delay_ready_115 = (_dataflow__delay_ready_116 || !_dataflow__delay_valid_116) && _dataflow__delay_valid_115;
  reg signed [16-1:0] _dataflow__delay_data_124;
  reg _dataflow__delay_valid_124;
  wire _dataflow__delay_ready_124;
  assign _dataflow__delay_ready_123 = (_dataflow__delay_ready_124 || !_dataflow__delay_valid_124) && _dataflow__delay_valid_123;
  reg signed [16-1:0] _dataflow__delay_data_77;
  reg _dataflow__delay_valid_77;
  wire _dataflow__delay_ready_77;
  assign _dataflow__delay_ready_76 = (_dataflow__delay_ready_77 || !_dataflow__delay_valid_77) && _dataflow__delay_valid_76;
  reg signed [16-1:0] _dataflow__delay_data_93;
  reg _dataflow__delay_valid_93;
  wire _dataflow__delay_ready_93;
  assign _dataflow__delay_ready_92 = (_dataflow__delay_ready_93 || !_dataflow__delay_valid_93) && _dataflow__delay_valid_92;
  reg signed [16-1:0] _dataflow__delay_data_101;
  reg _dataflow__delay_valid_101;
  wire _dataflow__delay_ready_101;
  assign _dataflow__delay_ready_100 = (_dataflow__delay_ready_101 || !_dataflow__delay_valid_101) && _dataflow__delay_valid_100;
  reg signed [16-1:0] _dataflow__delay_data_109;
  reg _dataflow__delay_valid_109;
  wire _dataflow__delay_ready_109;
  assign _dataflow__delay_ready_108 = (_dataflow__delay_ready_109 || !_dataflow__delay_valid_109) && _dataflow__delay_valid_108;
  reg signed [16-1:0] _dataflow__delay_data_117;
  reg _dataflow__delay_valid_117;
  wire _dataflow__delay_ready_117;
  assign _dataflow__delay_ready_116 = (_dataflow__delay_ready_117 || !_dataflow__delay_valid_117) && _dataflow__delay_valid_116;
  reg signed [16-1:0] _dataflow__delay_data_125;
  reg _dataflow__delay_valid_125;
  wire _dataflow__delay_ready_125;
  assign _dataflow__delay_ready_124 = (_dataflow__delay_ready_125 || !_dataflow__delay_valid_125) && _dataflow__delay_valid_124;
  reg signed [16-1:0] _dataflow__delay_data_78;
  reg _dataflow__delay_valid_78;
  wire _dataflow__delay_ready_78;
  assign _dataflow__delay_ready_77 = (_dataflow__delay_ready_78 || !_dataflow__delay_valid_78) && _dataflow__delay_valid_77;
  reg signed [16-1:0] _dataflow__delay_data_94;
  reg _dataflow__delay_valid_94;
  wire _dataflow__delay_ready_94;
  assign _dataflow__delay_ready_93 = (_dataflow__delay_ready_94 || !_dataflow__delay_valid_94) && _dataflow__delay_valid_93;
  reg signed [16-1:0] _dataflow__delay_data_102;
  reg _dataflow__delay_valid_102;
  wire _dataflow__delay_ready_102;
  assign _dataflow__delay_ready_101 = (_dataflow__delay_ready_102 || !_dataflow__delay_valid_102) && _dataflow__delay_valid_101;
  reg signed [16-1:0] _dataflow__delay_data_110;
  reg _dataflow__delay_valid_110;
  wire _dataflow__delay_ready_110;
  assign _dataflow__delay_ready_109 = (_dataflow__delay_ready_110 || !_dataflow__delay_valid_110) && _dataflow__delay_valid_109;
  reg signed [16-1:0] _dataflow__delay_data_118;
  reg _dataflow__delay_valid_118;
  wire _dataflow__delay_ready_118;
  assign _dataflow__delay_ready_117 = (_dataflow__delay_ready_118 || !_dataflow__delay_valid_118) && _dataflow__delay_valid_117;
  reg signed [16-1:0] _dataflow__delay_data_126;
  reg _dataflow__delay_valid_126;
  wire _dataflow__delay_ready_126;
  assign _dataflow__delay_ready_125 = (_dataflow__delay_ready_126 || !_dataflow__delay_valid_126) && _dataflow__delay_valid_125;
  reg signed [16-1:0] _dataflow_minus_data_62;
  reg _dataflow_minus_valid_62;
  wire _dataflow_minus_ready_62;
  assign _dataflow_times_ready_54 = (_dataflow_minus_ready_62 || !_dataflow_minus_valid_62) && (_dataflow_times_valid_54 && _dataflow_times_valid_56);
  assign _dataflow_times_ready_56 = (_dataflow_minus_ready_62 || !_dataflow_minus_valid_62) && (_dataflow_times_valid_54 && _dataflow_times_valid_56);
  reg signed [16-1:0] _dataflow_plus_data_63;
  reg _dataflow_plus_valid_63;
  wire _dataflow_plus_ready_63;
  assign _dataflow_times_ready_58 = (_dataflow_plus_ready_63 || !_dataflow_plus_valid_63) && (_dataflow_times_valid_58 && _dataflow_times_valid_60);
  assign _dataflow_times_ready_60 = (_dataflow_plus_ready_63 || !_dataflow_plus_valid_63) && (_dataflow_times_valid_58 && _dataflow_times_valid_60);
  reg signed [16-1:0] _dataflow__delay_data_79;
  reg _dataflow__delay_valid_79;
  wire _dataflow__delay_ready_79;
  assign _dataflow__delay_ready_78 = (_dataflow__delay_ready_79 || !_dataflow__delay_valid_79) && _dataflow__delay_valid_78;
  reg signed [16-1:0] _dataflow__delay_data_95;
  reg _dataflow__delay_valid_95;
  wire _dataflow__delay_ready_95;
  assign _dataflow__delay_ready_94 = (_dataflow__delay_ready_95 || !_dataflow__delay_valid_95) && _dataflow__delay_valid_94;
  reg signed [16-1:0] _dataflow__delay_data_103;
  reg _dataflow__delay_valid_103;
  wire _dataflow__delay_ready_103;
  assign _dataflow__delay_ready_102 = (_dataflow__delay_ready_103 || !_dataflow__delay_valid_103) && _dataflow__delay_valid_102;
  reg signed [16-1:0] _dataflow__delay_data_111;
  reg _dataflow__delay_valid_111;
  wire _dataflow__delay_ready_111;
  assign _dataflow__delay_ready_110 = (_dataflow__delay_ready_111 || !_dataflow__delay_valid_111) && _dataflow__delay_valid_110;
  reg signed [16-1:0] _dataflow__delay_data_119;
  reg _dataflow__delay_valid_119;
  wire _dataflow__delay_ready_119;
  assign _dataflow__delay_ready_118 = (_dataflow__delay_ready_119 || !_dataflow__delay_valid_119) && _dataflow__delay_valid_118;
  reg signed [16-1:0] _dataflow__delay_data_127;
  reg _dataflow__delay_valid_127;
  wire _dataflow__delay_ready_127;
  assign _dataflow__delay_ready_126 = (_dataflow__delay_ready_127 || !_dataflow__delay_valid_127) && _dataflow__delay_valid_126;
  assign dout3re = _dataflow_minus_data_62;
  assign _dataflow_minus_ready_62 = 1;
  assign dout3im = _dataflow_plus_data_63;
  assign _dataflow_plus_ready_63 = 1;
  assign dout0re = _dataflow__delay_data_79;
  assign _dataflow__delay_ready_79 = 1;
  assign dout0im = _dataflow__delay_data_95;
  assign _dataflow__delay_ready_95 = 1;
  assign dout2re = _dataflow__delay_data_103;
  assign _dataflow__delay_ready_103 = 1;
  assign dout2im = _dataflow__delay_data_111;
  assign _dataflow__delay_ready_111 = 1;
  assign dout1re = _dataflow__delay_data_119;
  assign _dataflow__delay_ready_119 = 1;
  assign dout1im = _dataflow__delay_data_127;
  assign _dataflow__delay_ready_127 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_plus_data_8 <= 0;
      _dataflow_plus_valid_8 <= 0;
      _dataflow_plus_data_9 <= 0;
      _dataflow_plus_valid_9 <= 0;
      _dataflow_minus_data_10 <= 0;
      _dataflow_minus_valid_10 <= 0;
      _dataflow_minus_data_11 <= 0;
      _dataflow_minus_valid_11 <= 0;
      _dataflow_plus_data_22 <= 0;
      _dataflow_plus_valid_22 <= 0;
      _dataflow_plus_data_23 <= 0;
      _dataflow_plus_valid_23 <= 0;
      _dataflow_minus_data_24 <= 0;
      _dataflow_minus_valid_24 <= 0;
      _dataflow_minus_data_25 <= 0;
      _dataflow_minus_valid_25 <= 0;
      _dataflow_times_mul_odata_reg_12 <= 0;
      _dataflow_times_mul_valid_reg_12 <= 0;
      _dataflow_times_mul_odata_reg_14 <= 0;
      _dataflow_times_mul_valid_reg_14 <= 0;
      _dataflow_times_mul_odata_reg_16 <= 0;
      _dataflow_times_mul_valid_reg_16 <= 0;
      _dataflow_times_mul_odata_reg_18 <= 0;
      _dataflow_times_mul_valid_reg_18 <= 0;
      _dataflow_times_mul_odata_reg_26 <= 0;
      _dataflow_times_mul_valid_reg_26 <= 0;
      _dataflow_times_mul_odata_reg_28 <= 0;
      _dataflow_times_mul_valid_reg_28 <= 0;
      _dataflow_times_mul_odata_reg_30 <= 0;
      _dataflow_times_mul_valid_reg_30 <= 0;
      _dataflow_times_mul_odata_reg_32 <= 0;
      _dataflow_times_mul_valid_reg_32 <= 0;
      _dataflow_plus_data_36 <= 0;
      _dataflow_plus_valid_36 <= 0;
      _dataflow_plus_data_37 <= 0;
      _dataflow_plus_valid_37 <= 0;
      _dataflow_minus_data_38 <= 0;
      _dataflow_minus_valid_38 <= 0;
      _dataflow_minus_data_39 <= 0;
      _dataflow_minus_valid_39 <= 0;
      _dataflow_times_mul_odata_reg_40 <= 0;
      _dataflow_times_mul_valid_reg_40 <= 0;
      _dataflow_times_mul_odata_reg_42 <= 0;
      _dataflow_times_mul_valid_reg_42 <= 0;
      _dataflow_times_mul_odata_reg_44 <= 0;
      _dataflow_times_mul_valid_reg_44 <= 0;
      _dataflow_times_mul_odata_reg_46 <= 0;
      _dataflow_times_mul_valid_reg_46 <= 0;
      _dataflow__delay_data_64 <= 0;
      _dataflow__delay_valid_64 <= 0;
      _dataflow__delay_data_80 <= 0;
      _dataflow__delay_valid_80 <= 0;
      _dataflow__delay_data_65 <= 0;
      _dataflow__delay_valid_65 <= 0;
      _dataflow__delay_data_81 <= 0;
      _dataflow__delay_valid_81 <= 0;
      _dataflow__delay_data_66 <= 0;
      _dataflow__delay_valid_66 <= 0;
      _dataflow__delay_data_82 <= 0;
      _dataflow__delay_valid_82 <= 0;
      _dataflow__delay_data_67 <= 0;
      _dataflow__delay_valid_67 <= 0;
      _dataflow__delay_data_83 <= 0;
      _dataflow__delay_valid_83 <= 0;
      _dataflow__delay_data_68 <= 0;
      _dataflow__delay_valid_68 <= 0;
      _dataflow__delay_data_84 <= 0;
      _dataflow__delay_valid_84 <= 0;
      _dataflow__delay_data_69 <= 0;
      _dataflow__delay_valid_69 <= 0;
      _dataflow__delay_data_85 <= 0;
      _dataflow__delay_valid_85 <= 0;
      _dataflow_minus_data_20 <= 0;
      _dataflow_minus_valid_20 <= 0;
      _dataflow_plus_data_21 <= 0;
      _dataflow_plus_valid_21 <= 0;
      _dataflow_minus_data_34 <= 0;
      _dataflow_minus_valid_34 <= 0;
      _dataflow_plus_data_35 <= 0;
      _dataflow_plus_valid_35 <= 0;
      _dataflow__delay_data_70 <= 0;
      _dataflow__delay_valid_70 <= 0;
      _dataflow__delay_data_86 <= 0;
      _dataflow__delay_valid_86 <= 0;
      _dataflow_minus_data_48 <= 0;
      _dataflow_minus_valid_48 <= 0;
      _dataflow_plus_data_49 <= 0;
      _dataflow_plus_valid_49 <= 0;
      _dataflow_plus_data_50 <= 0;
      _dataflow_plus_valid_50 <= 0;
      _dataflow_plus_data_51 <= 0;
      _dataflow_plus_valid_51 <= 0;
      _dataflow_minus_data_52 <= 0;
      _dataflow_minus_valid_52 <= 0;
      _dataflow_minus_data_53 <= 0;
      _dataflow_minus_valid_53 <= 0;
      _dataflow__delay_data_71 <= 0;
      _dataflow__delay_valid_71 <= 0;
      _dataflow__delay_data_87 <= 0;
      _dataflow__delay_valid_87 <= 0;
      _dataflow_times_mul_odata_reg_54 <= 0;
      _dataflow_times_mul_valid_reg_54 <= 0;
      _dataflow_times_mul_odata_reg_56 <= 0;
      _dataflow_times_mul_valid_reg_56 <= 0;
      _dataflow_times_mul_odata_reg_58 <= 0;
      _dataflow_times_mul_valid_reg_58 <= 0;
      _dataflow_times_mul_odata_reg_60 <= 0;
      _dataflow_times_mul_valid_reg_60 <= 0;
      _dataflow__delay_data_72 <= 0;
      _dataflow__delay_valid_72 <= 0;
      _dataflow__delay_data_88 <= 0;
      _dataflow__delay_valid_88 <= 0;
      _dataflow__delay_data_96 <= 0;
      _dataflow__delay_valid_96 <= 0;
      _dataflow__delay_data_104 <= 0;
      _dataflow__delay_valid_104 <= 0;
      _dataflow__delay_data_112 <= 0;
      _dataflow__delay_valid_112 <= 0;
      _dataflow__delay_data_120 <= 0;
      _dataflow__delay_valid_120 <= 0;
      _dataflow__delay_data_73 <= 0;
      _dataflow__delay_valid_73 <= 0;
      _dataflow__delay_data_89 <= 0;
      _dataflow__delay_valid_89 <= 0;
      _dataflow__delay_data_97 <= 0;
      _dataflow__delay_valid_97 <= 0;
      _dataflow__delay_data_105 <= 0;
      _dataflow__delay_valid_105 <= 0;
      _dataflow__delay_data_113 <= 0;
      _dataflow__delay_valid_113 <= 0;
      _dataflow__delay_data_121 <= 0;
      _dataflow__delay_valid_121 <= 0;
      _dataflow__delay_data_74 <= 0;
      _dataflow__delay_valid_74 <= 0;
      _dataflow__delay_data_90 <= 0;
      _dataflow__delay_valid_90 <= 0;
      _dataflow__delay_data_98 <= 0;
      _dataflow__delay_valid_98 <= 0;
      _dataflow__delay_data_106 <= 0;
      _dataflow__delay_valid_106 <= 0;
      _dataflow__delay_data_114 <= 0;
      _dataflow__delay_valid_114 <= 0;
      _dataflow__delay_data_122 <= 0;
      _dataflow__delay_valid_122 <= 0;
      _dataflow__delay_data_75 <= 0;
      _dataflow__delay_valid_75 <= 0;
      _dataflow__delay_data_91 <= 0;
      _dataflow__delay_valid_91 <= 0;
      _dataflow__delay_data_99 <= 0;
      _dataflow__delay_valid_99 <= 0;
      _dataflow__delay_data_107 <= 0;
      _dataflow__delay_valid_107 <= 0;
      _dataflow__delay_data_115 <= 0;
      _dataflow__delay_valid_115 <= 0;
      _dataflow__delay_data_123 <= 0;
      _dataflow__delay_valid_123 <= 0;
      _dataflow__delay_data_76 <= 0;
      _dataflow__delay_valid_76 <= 0;
      _dataflow__delay_data_92 <= 0;
      _dataflow__delay_valid_92 <= 0;
      _dataflow__delay_data_100 <= 0;
      _dataflow__delay_valid_100 <= 0;
      _dataflow__delay_data_108 <= 0;
      _dataflow__delay_valid_108 <= 0;
      _dataflow__delay_data_116 <= 0;
      _dataflow__delay_valid_116 <= 0;
      _dataflow__delay_data_124 <= 0;
      _dataflow__delay_valid_124 <= 0;
      _dataflow__delay_data_77 <= 0;
      _dataflow__delay_valid_77 <= 0;
      _dataflow__delay_data_93 <= 0;
      _dataflow__delay_valid_93 <= 0;
      _dataflow__delay_data_101 <= 0;
      _dataflow__delay_valid_101 <= 0;
      _dataflow__delay_data_109 <= 0;
      _dataflow__delay_valid_109 <= 0;
      _dataflow__delay_data_117 <= 0;
      _dataflow__delay_valid_117 <= 0;
      _dataflow__delay_data_125 <= 0;
      _dataflow__delay_valid_125 <= 0;
      _dataflow__delay_data_78 <= 0;
      _dataflow__delay_valid_78 <= 0;
      _dataflow__delay_data_94 <= 0;
      _dataflow__delay_valid_94 <= 0;
      _dataflow__delay_data_102 <= 0;
      _dataflow__delay_valid_102 <= 0;
      _dataflow__delay_data_110 <= 0;
      _dataflow__delay_valid_110 <= 0;
      _dataflow__delay_data_118 <= 0;
      _dataflow__delay_valid_118 <= 0;
      _dataflow__delay_data_126 <= 0;
      _dataflow__delay_valid_126 <= 0;
      _dataflow_minus_data_62 <= 0;
      _dataflow_minus_valid_62 <= 0;
      _dataflow_plus_data_63 <= 0;
      _dataflow_plus_valid_63 <= 0;
      _dataflow__delay_data_79 <= 0;
      _dataflow__delay_valid_79 <= 0;
      _dataflow__delay_data_95 <= 0;
      _dataflow__delay_valid_95 <= 0;
      _dataflow__delay_data_103 <= 0;
      _dataflow__delay_valid_103 <= 0;
      _dataflow__delay_data_111 <= 0;
      _dataflow__delay_valid_111 <= 0;
      _dataflow__delay_data_119 <= 0;
      _dataflow__delay_valid_119 <= 0;
      _dataflow__delay_data_127 <= 0;
      _dataflow__delay_valid_127 <= 0;
    end else begin
      if((_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && 1 && 1) begin
        _dataflow_plus_data_8 <= din0re + din2re;
      end 
      if(_dataflow_plus_valid_8 && _dataflow_plus_ready_8) begin
        _dataflow_plus_valid_8 <= 0;
      end 
      if((_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && 1) begin
        _dataflow_plus_valid_8 <= 1;
      end 
      if((_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && 1 && 1) begin
        _dataflow_plus_data_9 <= din0im + din2im;
      end 
      if(_dataflow_plus_valid_9 && _dataflow_plus_ready_9) begin
        _dataflow_plus_valid_9 <= 0;
      end 
      if((_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && 1) begin
        _dataflow_plus_valid_9 <= 1;
      end 
      if((_dataflow_minus_ready_10 || !_dataflow_minus_valid_10) && 1 && 1) begin
        _dataflow_minus_data_10 <= din0re - din2re;
      end 
      if(_dataflow_minus_valid_10 && _dataflow_minus_ready_10) begin
        _dataflow_minus_valid_10 <= 0;
      end 
      if((_dataflow_minus_ready_10 || !_dataflow_minus_valid_10) && 1) begin
        _dataflow_minus_valid_10 <= 1;
      end 
      if((_dataflow_minus_ready_11 || !_dataflow_minus_valid_11) && 1 && 1) begin
        _dataflow_minus_data_11 <= din0im - din2im;
      end 
      if(_dataflow_minus_valid_11 && _dataflow_minus_ready_11) begin
        _dataflow_minus_valid_11 <= 0;
      end 
      if((_dataflow_minus_ready_11 || !_dataflow_minus_valid_11) && 1) begin
        _dataflow_minus_valid_11 <= 1;
      end 
      if((_dataflow_plus_ready_22 || !_dataflow_plus_valid_22) && 1 && 1) begin
        _dataflow_plus_data_22 <= din1re + din3re;
      end 
      if(_dataflow_plus_valid_22 && _dataflow_plus_ready_22) begin
        _dataflow_plus_valid_22 <= 0;
      end 
      if((_dataflow_plus_ready_22 || !_dataflow_plus_valid_22) && 1) begin
        _dataflow_plus_valid_22 <= 1;
      end 
      if((_dataflow_plus_ready_23 || !_dataflow_plus_valid_23) && 1 && 1) begin
        _dataflow_plus_data_23 <= din1im + din3im;
      end 
      if(_dataflow_plus_valid_23 && _dataflow_plus_ready_23) begin
        _dataflow_plus_valid_23 <= 0;
      end 
      if((_dataflow_plus_ready_23 || !_dataflow_plus_valid_23) && 1) begin
        _dataflow_plus_valid_23 <= 1;
      end 
      if((_dataflow_minus_ready_24 || !_dataflow_minus_valid_24) && 1 && 1) begin
        _dataflow_minus_data_24 <= din1re - din3re;
      end 
      if(_dataflow_minus_valid_24 && _dataflow_minus_ready_24) begin
        _dataflow_minus_valid_24 <= 0;
      end 
      if((_dataflow_minus_ready_24 || !_dataflow_minus_valid_24) && 1) begin
        _dataflow_minus_valid_24 <= 1;
      end 
      if((_dataflow_minus_ready_25 || !_dataflow_minus_valid_25) && 1 && 1) begin
        _dataflow_minus_data_25 <= din1im - din3im;
      end 
      if(_dataflow_minus_valid_25 && _dataflow_minus_ready_25) begin
        _dataflow_minus_valid_25 <= 0;
      end 
      if((_dataflow_minus_ready_25 || !_dataflow_minus_valid_25) && 1) begin
        _dataflow_minus_valid_25 <= 1;
      end 
      if(_dataflow_times_ready_12 || !_dataflow_times_valid_12) begin
        _dataflow_times_mul_odata_reg_12 <= _dataflow_times_mul_odata_12;
      end 
      if(_dataflow_times_ready_12 || !_dataflow_times_valid_12) begin
        _dataflow_times_mul_valid_reg_12 <= _dataflow_times_mul_ovalid_12;
      end 
      if(_dataflow_times_ready_14 || !_dataflow_times_valid_14) begin
        _dataflow_times_mul_odata_reg_14 <= _dataflow_times_mul_odata_14;
      end 
      if(_dataflow_times_ready_14 || !_dataflow_times_valid_14) begin
        _dataflow_times_mul_valid_reg_14 <= _dataflow_times_mul_ovalid_14;
      end 
      if(_dataflow_times_ready_16 || !_dataflow_times_valid_16) begin
        _dataflow_times_mul_odata_reg_16 <= _dataflow_times_mul_odata_16;
      end 
      if(_dataflow_times_ready_16 || !_dataflow_times_valid_16) begin
        _dataflow_times_mul_valid_reg_16 <= _dataflow_times_mul_ovalid_16;
      end 
      if(_dataflow_times_ready_18 || !_dataflow_times_valid_18) begin
        _dataflow_times_mul_odata_reg_18 <= _dataflow_times_mul_odata_18;
      end 
      if(_dataflow_times_ready_18 || !_dataflow_times_valid_18) begin
        _dataflow_times_mul_valid_reg_18 <= _dataflow_times_mul_ovalid_18;
      end 
      if(_dataflow_times_ready_26 || !_dataflow_times_valid_26) begin
        _dataflow_times_mul_odata_reg_26 <= _dataflow_times_mul_odata_26;
      end 
      if(_dataflow_times_ready_26 || !_dataflow_times_valid_26) begin
        _dataflow_times_mul_valid_reg_26 <= _dataflow_times_mul_ovalid_26;
      end 
      if(_dataflow_times_ready_28 || !_dataflow_times_valid_28) begin
        _dataflow_times_mul_odata_reg_28 <= _dataflow_times_mul_odata_28;
      end 
      if(_dataflow_times_ready_28 || !_dataflow_times_valid_28) begin
        _dataflow_times_mul_valid_reg_28 <= _dataflow_times_mul_ovalid_28;
      end 
      if(_dataflow_times_ready_30 || !_dataflow_times_valid_30) begin
        _dataflow_times_mul_odata_reg_30 <= _dataflow_times_mul_odata_30;
      end 
      if(_dataflow_times_ready_30 || !_dataflow_times_valid_30) begin
        _dataflow_times_mul_valid_reg_30 <= _dataflow_times_mul_ovalid_30;
      end 
      if(_dataflow_times_ready_32 || !_dataflow_times_valid_32) begin
        _dataflow_times_mul_odata_reg_32 <= _dataflow_times_mul_odata_32;
      end 
      if(_dataflow_times_ready_32 || !_dataflow_times_valid_32) begin
        _dataflow_times_mul_valid_reg_32 <= _dataflow_times_mul_ovalid_32;
      end 
      if((_dataflow_plus_ready_36 || !_dataflow_plus_valid_36) && (_dataflow_plus_ready_8 && _dataflow_plus_ready_22) && (_dataflow_plus_valid_8 && _dataflow_plus_valid_22)) begin
        _dataflow_plus_data_36 <= _dataflow_plus_data_8 + _dataflow_plus_data_22;
      end 
      if(_dataflow_plus_valid_36 && _dataflow_plus_ready_36) begin
        _dataflow_plus_valid_36 <= 0;
      end 
      if((_dataflow_plus_ready_36 || !_dataflow_plus_valid_36) && (_dataflow_plus_ready_8 && _dataflow_plus_ready_22)) begin
        _dataflow_plus_valid_36 <= _dataflow_plus_valid_8 && _dataflow_plus_valid_22;
      end 
      if((_dataflow_plus_ready_37 || !_dataflow_plus_valid_37) && (_dataflow_plus_ready_9 && _dataflow_plus_ready_23) && (_dataflow_plus_valid_9 && _dataflow_plus_valid_23)) begin
        _dataflow_plus_data_37 <= _dataflow_plus_data_9 + _dataflow_plus_data_23;
      end 
      if(_dataflow_plus_valid_37 && _dataflow_plus_ready_37) begin
        _dataflow_plus_valid_37 <= 0;
      end 
      if((_dataflow_plus_ready_37 || !_dataflow_plus_valid_37) && (_dataflow_plus_ready_9 && _dataflow_plus_ready_23)) begin
        _dataflow_plus_valid_37 <= _dataflow_plus_valid_9 && _dataflow_plus_valid_23;
      end 
      if((_dataflow_minus_ready_38 || !_dataflow_minus_valid_38) && (_dataflow_plus_ready_8 && _dataflow_plus_ready_22) && (_dataflow_plus_valid_8 && _dataflow_plus_valid_22)) begin
        _dataflow_minus_data_38 <= _dataflow_plus_data_8 - _dataflow_plus_data_22;
      end 
      if(_dataflow_minus_valid_38 && _dataflow_minus_ready_38) begin
        _dataflow_minus_valid_38 <= 0;
      end 
      if((_dataflow_minus_ready_38 || !_dataflow_minus_valid_38) && (_dataflow_plus_ready_8 && _dataflow_plus_ready_22)) begin
        _dataflow_minus_valid_38 <= _dataflow_plus_valid_8 && _dataflow_plus_valid_22;
      end 
      if((_dataflow_minus_ready_39 || !_dataflow_minus_valid_39) && (_dataflow_plus_ready_9 && _dataflow_plus_ready_23) && (_dataflow_plus_valid_9 && _dataflow_plus_valid_23)) begin
        _dataflow_minus_data_39 <= _dataflow_plus_data_9 - _dataflow_plus_data_23;
      end 
      if(_dataflow_minus_valid_39 && _dataflow_minus_ready_39) begin
        _dataflow_minus_valid_39 <= 0;
      end 
      if((_dataflow_minus_ready_39 || !_dataflow_minus_valid_39) && (_dataflow_plus_ready_9 && _dataflow_plus_ready_23)) begin
        _dataflow_minus_valid_39 <= _dataflow_plus_valid_9 && _dataflow_plus_valid_23;
      end 
      if(_dataflow_times_ready_40 || !_dataflow_times_valid_40) begin
        _dataflow_times_mul_odata_reg_40 <= _dataflow_times_mul_odata_40;
      end 
      if(_dataflow_times_ready_40 || !_dataflow_times_valid_40) begin
        _dataflow_times_mul_valid_reg_40 <= _dataflow_times_mul_ovalid_40;
      end 
      if(_dataflow_times_ready_42 || !_dataflow_times_valid_42) begin
        _dataflow_times_mul_odata_reg_42 <= _dataflow_times_mul_odata_42;
      end 
      if(_dataflow_times_ready_42 || !_dataflow_times_valid_42) begin
        _dataflow_times_mul_valid_reg_42 <= _dataflow_times_mul_ovalid_42;
      end 
      if(_dataflow_times_ready_44 || !_dataflow_times_valid_44) begin
        _dataflow_times_mul_odata_reg_44 <= _dataflow_times_mul_odata_44;
      end 
      if(_dataflow_times_ready_44 || !_dataflow_times_valid_44) begin
        _dataflow_times_mul_valid_reg_44 <= _dataflow_times_mul_ovalid_44;
      end 
      if(_dataflow_times_ready_46 || !_dataflow_times_valid_46) begin
        _dataflow_times_mul_odata_reg_46 <= _dataflow_times_mul_odata_46;
      end 
      if(_dataflow_times_ready_46 || !_dataflow_times_valid_46) begin
        _dataflow_times_mul_valid_reg_46 <= _dataflow_times_mul_ovalid_46;
      end 
      if((_dataflow__delay_ready_64 || !_dataflow__delay_valid_64) && _dataflow_plus_ready_36 && _dataflow_plus_valid_36) begin
        _dataflow__delay_data_64 <= _dataflow_plus_data_36;
      end 
      if(_dataflow__delay_valid_64 && _dataflow__delay_ready_64) begin
        _dataflow__delay_valid_64 <= 0;
      end 
      if((_dataflow__delay_ready_64 || !_dataflow__delay_valid_64) && _dataflow_plus_ready_36) begin
        _dataflow__delay_valid_64 <= _dataflow_plus_valid_36;
      end 
      if((_dataflow__delay_ready_80 || !_dataflow__delay_valid_80) && _dataflow_plus_ready_37 && _dataflow_plus_valid_37) begin
        _dataflow__delay_data_80 <= _dataflow_plus_data_37;
      end 
      if(_dataflow__delay_valid_80 && _dataflow__delay_ready_80) begin
        _dataflow__delay_valid_80 <= 0;
      end 
      if((_dataflow__delay_ready_80 || !_dataflow__delay_valid_80) && _dataflow_plus_ready_37) begin
        _dataflow__delay_valid_80 <= _dataflow_plus_valid_37;
      end 
      if((_dataflow__delay_ready_65 || !_dataflow__delay_valid_65) && _dataflow__delay_ready_64 && _dataflow__delay_valid_64) begin
        _dataflow__delay_data_65 <= _dataflow__delay_data_64;
      end 
      if(_dataflow__delay_valid_65 && _dataflow__delay_ready_65) begin
        _dataflow__delay_valid_65 <= 0;
      end 
      if((_dataflow__delay_ready_65 || !_dataflow__delay_valid_65) && _dataflow__delay_ready_64) begin
        _dataflow__delay_valid_65 <= _dataflow__delay_valid_64;
      end 
      if((_dataflow__delay_ready_81 || !_dataflow__delay_valid_81) && _dataflow__delay_ready_80 && _dataflow__delay_valid_80) begin
        _dataflow__delay_data_81 <= _dataflow__delay_data_80;
      end 
      if(_dataflow__delay_valid_81 && _dataflow__delay_ready_81) begin
        _dataflow__delay_valid_81 <= 0;
      end 
      if((_dataflow__delay_ready_81 || !_dataflow__delay_valid_81) && _dataflow__delay_ready_80) begin
        _dataflow__delay_valid_81 <= _dataflow__delay_valid_80;
      end 
      if((_dataflow__delay_ready_66 || !_dataflow__delay_valid_66) && _dataflow__delay_ready_65 && _dataflow__delay_valid_65) begin
        _dataflow__delay_data_66 <= _dataflow__delay_data_65;
      end 
      if(_dataflow__delay_valid_66 && _dataflow__delay_ready_66) begin
        _dataflow__delay_valid_66 <= 0;
      end 
      if((_dataflow__delay_ready_66 || !_dataflow__delay_valid_66) && _dataflow__delay_ready_65) begin
        _dataflow__delay_valid_66 <= _dataflow__delay_valid_65;
      end 
      if((_dataflow__delay_ready_82 || !_dataflow__delay_valid_82) && _dataflow__delay_ready_81 && _dataflow__delay_valid_81) begin
        _dataflow__delay_data_82 <= _dataflow__delay_data_81;
      end 
      if(_dataflow__delay_valid_82 && _dataflow__delay_ready_82) begin
        _dataflow__delay_valid_82 <= 0;
      end 
      if((_dataflow__delay_ready_82 || !_dataflow__delay_valid_82) && _dataflow__delay_ready_81) begin
        _dataflow__delay_valid_82 <= _dataflow__delay_valid_81;
      end 
      if((_dataflow__delay_ready_67 || !_dataflow__delay_valid_67) && _dataflow__delay_ready_66 && _dataflow__delay_valid_66) begin
        _dataflow__delay_data_67 <= _dataflow__delay_data_66;
      end 
      if(_dataflow__delay_valid_67 && _dataflow__delay_ready_67) begin
        _dataflow__delay_valid_67 <= 0;
      end 
      if((_dataflow__delay_ready_67 || !_dataflow__delay_valid_67) && _dataflow__delay_ready_66) begin
        _dataflow__delay_valid_67 <= _dataflow__delay_valid_66;
      end 
      if((_dataflow__delay_ready_83 || !_dataflow__delay_valid_83) && _dataflow__delay_ready_82 && _dataflow__delay_valid_82) begin
        _dataflow__delay_data_83 <= _dataflow__delay_data_82;
      end 
      if(_dataflow__delay_valid_83 && _dataflow__delay_ready_83) begin
        _dataflow__delay_valid_83 <= 0;
      end 
      if((_dataflow__delay_ready_83 || !_dataflow__delay_valid_83) && _dataflow__delay_ready_82) begin
        _dataflow__delay_valid_83 <= _dataflow__delay_valid_82;
      end 
      if((_dataflow__delay_ready_68 || !_dataflow__delay_valid_68) && _dataflow__delay_ready_67 && _dataflow__delay_valid_67) begin
        _dataflow__delay_data_68 <= _dataflow__delay_data_67;
      end 
      if(_dataflow__delay_valid_68 && _dataflow__delay_ready_68) begin
        _dataflow__delay_valid_68 <= 0;
      end 
      if((_dataflow__delay_ready_68 || !_dataflow__delay_valid_68) && _dataflow__delay_ready_67) begin
        _dataflow__delay_valid_68 <= _dataflow__delay_valid_67;
      end 
      if((_dataflow__delay_ready_84 || !_dataflow__delay_valid_84) && _dataflow__delay_ready_83 && _dataflow__delay_valid_83) begin
        _dataflow__delay_data_84 <= _dataflow__delay_data_83;
      end 
      if(_dataflow__delay_valid_84 && _dataflow__delay_ready_84) begin
        _dataflow__delay_valid_84 <= 0;
      end 
      if((_dataflow__delay_ready_84 || !_dataflow__delay_valid_84) && _dataflow__delay_ready_83) begin
        _dataflow__delay_valid_84 <= _dataflow__delay_valid_83;
      end 
      if((_dataflow__delay_ready_69 || !_dataflow__delay_valid_69) && _dataflow__delay_ready_68 && _dataflow__delay_valid_68) begin
        _dataflow__delay_data_69 <= _dataflow__delay_data_68;
      end 
      if(_dataflow__delay_valid_69 && _dataflow__delay_ready_69) begin
        _dataflow__delay_valid_69 <= 0;
      end 
      if((_dataflow__delay_ready_69 || !_dataflow__delay_valid_69) && _dataflow__delay_ready_68) begin
        _dataflow__delay_valid_69 <= _dataflow__delay_valid_68;
      end 
      if((_dataflow__delay_ready_85 || !_dataflow__delay_valid_85) && _dataflow__delay_ready_84 && _dataflow__delay_valid_84) begin
        _dataflow__delay_data_85 <= _dataflow__delay_data_84;
      end 
      if(_dataflow__delay_valid_85 && _dataflow__delay_ready_85) begin
        _dataflow__delay_valid_85 <= 0;
      end 
      if((_dataflow__delay_ready_85 || !_dataflow__delay_valid_85) && _dataflow__delay_ready_84) begin
        _dataflow__delay_valid_85 <= _dataflow__delay_valid_84;
      end 
      if((_dataflow_minus_ready_20 || !_dataflow_minus_valid_20) && (_dataflow_times_ready_12 && _dataflow_times_ready_14) && (_dataflow_times_valid_12 && _dataflow_times_valid_14)) begin
        _dataflow_minus_data_20 <= _dataflow_times_data_12 - _dataflow_times_data_14;
      end 
      if(_dataflow_minus_valid_20 && _dataflow_minus_ready_20) begin
        _dataflow_minus_valid_20 <= 0;
      end 
      if((_dataflow_minus_ready_20 || !_dataflow_minus_valid_20) && (_dataflow_times_ready_12 && _dataflow_times_ready_14)) begin
        _dataflow_minus_valid_20 <= _dataflow_times_valid_12 && _dataflow_times_valid_14;
      end 
      if((_dataflow_plus_ready_21 || !_dataflow_plus_valid_21) && (_dataflow_times_ready_16 && _dataflow_times_ready_18) && (_dataflow_times_valid_16 && _dataflow_times_valid_18)) begin
        _dataflow_plus_data_21 <= _dataflow_times_data_16 + _dataflow_times_data_18;
      end 
      if(_dataflow_plus_valid_21 && _dataflow_plus_ready_21) begin
        _dataflow_plus_valid_21 <= 0;
      end 
      if((_dataflow_plus_ready_21 || !_dataflow_plus_valid_21) && (_dataflow_times_ready_16 && _dataflow_times_ready_18)) begin
        _dataflow_plus_valid_21 <= _dataflow_times_valid_16 && _dataflow_times_valid_18;
      end 
      if((_dataflow_minus_ready_34 || !_dataflow_minus_valid_34) && (_dataflow_times_ready_26 && _dataflow_times_ready_28) && (_dataflow_times_valid_26 && _dataflow_times_valid_28)) begin
        _dataflow_minus_data_34 <= _dataflow_times_data_26 - _dataflow_times_data_28;
      end 
      if(_dataflow_minus_valid_34 && _dataflow_minus_ready_34) begin
        _dataflow_minus_valid_34 <= 0;
      end 
      if((_dataflow_minus_ready_34 || !_dataflow_minus_valid_34) && (_dataflow_times_ready_26 && _dataflow_times_ready_28)) begin
        _dataflow_minus_valid_34 <= _dataflow_times_valid_26 && _dataflow_times_valid_28;
      end 
      if((_dataflow_plus_ready_35 || !_dataflow_plus_valid_35) && (_dataflow_times_ready_30 && _dataflow_times_ready_32) && (_dataflow_times_valid_30 && _dataflow_times_valid_32)) begin
        _dataflow_plus_data_35 <= _dataflow_times_data_30 + _dataflow_times_data_32;
      end 
      if(_dataflow_plus_valid_35 && _dataflow_plus_ready_35) begin
        _dataflow_plus_valid_35 <= 0;
      end 
      if((_dataflow_plus_ready_35 || !_dataflow_plus_valid_35) && (_dataflow_times_ready_30 && _dataflow_times_ready_32)) begin
        _dataflow_plus_valid_35 <= _dataflow_times_valid_30 && _dataflow_times_valid_32;
      end 
      if((_dataflow__delay_ready_70 || !_dataflow__delay_valid_70) && _dataflow__delay_ready_69 && _dataflow__delay_valid_69) begin
        _dataflow__delay_data_70 <= _dataflow__delay_data_69;
      end 
      if(_dataflow__delay_valid_70 && _dataflow__delay_ready_70) begin
        _dataflow__delay_valid_70 <= 0;
      end 
      if((_dataflow__delay_ready_70 || !_dataflow__delay_valid_70) && _dataflow__delay_ready_69) begin
        _dataflow__delay_valid_70 <= _dataflow__delay_valid_69;
      end 
      if((_dataflow__delay_ready_86 || !_dataflow__delay_valid_86) && _dataflow__delay_ready_85 && _dataflow__delay_valid_85) begin
        _dataflow__delay_data_86 <= _dataflow__delay_data_85;
      end 
      if(_dataflow__delay_valid_86 && _dataflow__delay_ready_86) begin
        _dataflow__delay_valid_86 <= 0;
      end 
      if((_dataflow__delay_ready_86 || !_dataflow__delay_valid_86) && _dataflow__delay_ready_85) begin
        _dataflow__delay_valid_86 <= _dataflow__delay_valid_85;
      end 
      if((_dataflow_minus_ready_48 || !_dataflow_minus_valid_48) && (_dataflow_times_ready_40 && _dataflow_times_ready_42) && (_dataflow_times_valid_40 && _dataflow_times_valid_42)) begin
        _dataflow_minus_data_48 <= _dataflow_times_data_40 - _dataflow_times_data_42;
      end 
      if(_dataflow_minus_valid_48 && _dataflow_minus_ready_48) begin
        _dataflow_minus_valid_48 <= 0;
      end 
      if((_dataflow_minus_ready_48 || !_dataflow_minus_valid_48) && (_dataflow_times_ready_40 && _dataflow_times_ready_42)) begin
        _dataflow_minus_valid_48 <= _dataflow_times_valid_40 && _dataflow_times_valid_42;
      end 
      if((_dataflow_plus_ready_49 || !_dataflow_plus_valid_49) && (_dataflow_times_ready_44 && _dataflow_times_ready_46) && (_dataflow_times_valid_44 && _dataflow_times_valid_46)) begin
        _dataflow_plus_data_49 <= _dataflow_times_data_44 + _dataflow_times_data_46;
      end 
      if(_dataflow_plus_valid_49 && _dataflow_plus_ready_49) begin
        _dataflow_plus_valid_49 <= 0;
      end 
      if((_dataflow_plus_ready_49 || !_dataflow_plus_valid_49) && (_dataflow_times_ready_44 && _dataflow_times_ready_46)) begin
        _dataflow_plus_valid_49 <= _dataflow_times_valid_44 && _dataflow_times_valid_46;
      end 
      if((_dataflow_plus_ready_50 || !_dataflow_plus_valid_50) && (_dataflow_minus_ready_20 && _dataflow_minus_ready_34) && (_dataflow_minus_valid_20 && _dataflow_minus_valid_34)) begin
        _dataflow_plus_data_50 <= _dataflow_minus_data_20 + _dataflow_minus_data_34;
      end 
      if(_dataflow_plus_valid_50 && _dataflow_plus_ready_50) begin
        _dataflow_plus_valid_50 <= 0;
      end 
      if((_dataflow_plus_ready_50 || !_dataflow_plus_valid_50) && (_dataflow_minus_ready_20 && _dataflow_minus_ready_34)) begin
        _dataflow_plus_valid_50 <= _dataflow_minus_valid_20 && _dataflow_minus_valid_34;
      end 
      if((_dataflow_plus_ready_51 || !_dataflow_plus_valid_51) && (_dataflow_plus_ready_21 && _dataflow_plus_ready_35) && (_dataflow_plus_valid_21 && _dataflow_plus_valid_35)) begin
        _dataflow_plus_data_51 <= _dataflow_plus_data_21 + _dataflow_plus_data_35;
      end 
      if(_dataflow_plus_valid_51 && _dataflow_plus_ready_51) begin
        _dataflow_plus_valid_51 <= 0;
      end 
      if((_dataflow_plus_ready_51 || !_dataflow_plus_valid_51) && (_dataflow_plus_ready_21 && _dataflow_plus_ready_35)) begin
        _dataflow_plus_valid_51 <= _dataflow_plus_valid_21 && _dataflow_plus_valid_35;
      end 
      if((_dataflow_minus_ready_52 || !_dataflow_minus_valid_52) && (_dataflow_minus_ready_20 && _dataflow_minus_ready_34) && (_dataflow_minus_valid_20 && _dataflow_minus_valid_34)) begin
        _dataflow_minus_data_52 <= _dataflow_minus_data_20 - _dataflow_minus_data_34;
      end 
      if(_dataflow_minus_valid_52 && _dataflow_minus_ready_52) begin
        _dataflow_minus_valid_52 <= 0;
      end 
      if((_dataflow_minus_ready_52 || !_dataflow_minus_valid_52) && (_dataflow_minus_ready_20 && _dataflow_minus_ready_34)) begin
        _dataflow_minus_valid_52 <= _dataflow_minus_valid_20 && _dataflow_minus_valid_34;
      end 
      if((_dataflow_minus_ready_53 || !_dataflow_minus_valid_53) && (_dataflow_plus_ready_21 && _dataflow_plus_ready_35) && (_dataflow_plus_valid_21 && _dataflow_plus_valid_35)) begin
        _dataflow_minus_data_53 <= _dataflow_plus_data_21 - _dataflow_plus_data_35;
      end 
      if(_dataflow_minus_valid_53 && _dataflow_minus_ready_53) begin
        _dataflow_minus_valid_53 <= 0;
      end 
      if((_dataflow_minus_ready_53 || !_dataflow_minus_valid_53) && (_dataflow_plus_ready_21 && _dataflow_plus_ready_35)) begin
        _dataflow_minus_valid_53 <= _dataflow_plus_valid_21 && _dataflow_plus_valid_35;
      end 
      if((_dataflow__delay_ready_71 || !_dataflow__delay_valid_71) && _dataflow__delay_ready_70 && _dataflow__delay_valid_70) begin
        _dataflow__delay_data_71 <= _dataflow__delay_data_70;
      end 
      if(_dataflow__delay_valid_71 && _dataflow__delay_ready_71) begin
        _dataflow__delay_valid_71 <= 0;
      end 
      if((_dataflow__delay_ready_71 || !_dataflow__delay_valid_71) && _dataflow__delay_ready_70) begin
        _dataflow__delay_valid_71 <= _dataflow__delay_valid_70;
      end 
      if((_dataflow__delay_ready_87 || !_dataflow__delay_valid_87) && _dataflow__delay_ready_86 && _dataflow__delay_valid_86) begin
        _dataflow__delay_data_87 <= _dataflow__delay_data_86;
      end 
      if(_dataflow__delay_valid_87 && _dataflow__delay_ready_87) begin
        _dataflow__delay_valid_87 <= 0;
      end 
      if((_dataflow__delay_ready_87 || !_dataflow__delay_valid_87) && _dataflow__delay_ready_86) begin
        _dataflow__delay_valid_87 <= _dataflow__delay_valid_86;
      end 
      if(_dataflow_times_ready_54 || !_dataflow_times_valid_54) begin
        _dataflow_times_mul_odata_reg_54 <= _dataflow_times_mul_odata_54;
      end 
      if(_dataflow_times_ready_54 || !_dataflow_times_valid_54) begin
        _dataflow_times_mul_valid_reg_54 <= _dataflow_times_mul_ovalid_54;
      end 
      if(_dataflow_times_ready_56 || !_dataflow_times_valid_56) begin
        _dataflow_times_mul_odata_reg_56 <= _dataflow_times_mul_odata_56;
      end 
      if(_dataflow_times_ready_56 || !_dataflow_times_valid_56) begin
        _dataflow_times_mul_valid_reg_56 <= _dataflow_times_mul_ovalid_56;
      end 
      if(_dataflow_times_ready_58 || !_dataflow_times_valid_58) begin
        _dataflow_times_mul_odata_reg_58 <= _dataflow_times_mul_odata_58;
      end 
      if(_dataflow_times_ready_58 || !_dataflow_times_valid_58) begin
        _dataflow_times_mul_valid_reg_58 <= _dataflow_times_mul_ovalid_58;
      end 
      if(_dataflow_times_ready_60 || !_dataflow_times_valid_60) begin
        _dataflow_times_mul_odata_reg_60 <= _dataflow_times_mul_odata_60;
      end 
      if(_dataflow_times_ready_60 || !_dataflow_times_valid_60) begin
        _dataflow_times_mul_valid_reg_60 <= _dataflow_times_mul_ovalid_60;
      end 
      if((_dataflow__delay_ready_72 || !_dataflow__delay_valid_72) && _dataflow__delay_ready_71 && _dataflow__delay_valid_71) begin
        _dataflow__delay_data_72 <= _dataflow__delay_data_71;
      end 
      if(_dataflow__delay_valid_72 && _dataflow__delay_ready_72) begin
        _dataflow__delay_valid_72 <= 0;
      end 
      if((_dataflow__delay_ready_72 || !_dataflow__delay_valid_72) && _dataflow__delay_ready_71) begin
        _dataflow__delay_valid_72 <= _dataflow__delay_valid_71;
      end 
      if((_dataflow__delay_ready_88 || !_dataflow__delay_valid_88) && _dataflow__delay_ready_87 && _dataflow__delay_valid_87) begin
        _dataflow__delay_data_88 <= _dataflow__delay_data_87;
      end 
      if(_dataflow__delay_valid_88 && _dataflow__delay_ready_88) begin
        _dataflow__delay_valid_88 <= 0;
      end 
      if((_dataflow__delay_ready_88 || !_dataflow__delay_valid_88) && _dataflow__delay_ready_87) begin
        _dataflow__delay_valid_88 <= _dataflow__delay_valid_87;
      end 
      if((_dataflow__delay_ready_96 || !_dataflow__delay_valid_96) && _dataflow_minus_ready_48 && _dataflow_minus_valid_48) begin
        _dataflow__delay_data_96 <= _dataflow_minus_data_48;
      end 
      if(_dataflow__delay_valid_96 && _dataflow__delay_ready_96) begin
        _dataflow__delay_valid_96 <= 0;
      end 
      if((_dataflow__delay_ready_96 || !_dataflow__delay_valid_96) && _dataflow_minus_ready_48) begin
        _dataflow__delay_valid_96 <= _dataflow_minus_valid_48;
      end 
      if((_dataflow__delay_ready_104 || !_dataflow__delay_valid_104) && _dataflow_plus_ready_49 && _dataflow_plus_valid_49) begin
        _dataflow__delay_data_104 <= _dataflow_plus_data_49;
      end 
      if(_dataflow__delay_valid_104 && _dataflow__delay_ready_104) begin
        _dataflow__delay_valid_104 <= 0;
      end 
      if((_dataflow__delay_ready_104 || !_dataflow__delay_valid_104) && _dataflow_plus_ready_49) begin
        _dataflow__delay_valid_104 <= _dataflow_plus_valid_49;
      end 
      if((_dataflow__delay_ready_112 || !_dataflow__delay_valid_112) && _dataflow_plus_ready_50 && _dataflow_plus_valid_50) begin
        _dataflow__delay_data_112 <= _dataflow_plus_data_50;
      end 
      if(_dataflow__delay_valid_112 && _dataflow__delay_ready_112) begin
        _dataflow__delay_valid_112 <= 0;
      end 
      if((_dataflow__delay_ready_112 || !_dataflow__delay_valid_112) && _dataflow_plus_ready_50) begin
        _dataflow__delay_valid_112 <= _dataflow_plus_valid_50;
      end 
      if((_dataflow__delay_ready_120 || !_dataflow__delay_valid_120) && _dataflow_plus_ready_51 && _dataflow_plus_valid_51) begin
        _dataflow__delay_data_120 <= _dataflow_plus_data_51;
      end 
      if(_dataflow__delay_valid_120 && _dataflow__delay_ready_120) begin
        _dataflow__delay_valid_120 <= 0;
      end 
      if((_dataflow__delay_ready_120 || !_dataflow__delay_valid_120) && _dataflow_plus_ready_51) begin
        _dataflow__delay_valid_120 <= _dataflow_plus_valid_51;
      end 
      if((_dataflow__delay_ready_73 || !_dataflow__delay_valid_73) && _dataflow__delay_ready_72 && _dataflow__delay_valid_72) begin
        _dataflow__delay_data_73 <= _dataflow__delay_data_72;
      end 
      if(_dataflow__delay_valid_73 && _dataflow__delay_ready_73) begin
        _dataflow__delay_valid_73 <= 0;
      end 
      if((_dataflow__delay_ready_73 || !_dataflow__delay_valid_73) && _dataflow__delay_ready_72) begin
        _dataflow__delay_valid_73 <= _dataflow__delay_valid_72;
      end 
      if((_dataflow__delay_ready_89 || !_dataflow__delay_valid_89) && _dataflow__delay_ready_88 && _dataflow__delay_valid_88) begin
        _dataflow__delay_data_89 <= _dataflow__delay_data_88;
      end 
      if(_dataflow__delay_valid_89 && _dataflow__delay_ready_89) begin
        _dataflow__delay_valid_89 <= 0;
      end 
      if((_dataflow__delay_ready_89 || !_dataflow__delay_valid_89) && _dataflow__delay_ready_88) begin
        _dataflow__delay_valid_89 <= _dataflow__delay_valid_88;
      end 
      if((_dataflow__delay_ready_97 || !_dataflow__delay_valid_97) && _dataflow__delay_ready_96 && _dataflow__delay_valid_96) begin
        _dataflow__delay_data_97 <= _dataflow__delay_data_96;
      end 
      if(_dataflow__delay_valid_97 && _dataflow__delay_ready_97) begin
        _dataflow__delay_valid_97 <= 0;
      end 
      if((_dataflow__delay_ready_97 || !_dataflow__delay_valid_97) && _dataflow__delay_ready_96) begin
        _dataflow__delay_valid_97 <= _dataflow__delay_valid_96;
      end 
      if((_dataflow__delay_ready_105 || !_dataflow__delay_valid_105) && _dataflow__delay_ready_104 && _dataflow__delay_valid_104) begin
        _dataflow__delay_data_105 <= _dataflow__delay_data_104;
      end 
      if(_dataflow__delay_valid_105 && _dataflow__delay_ready_105) begin
        _dataflow__delay_valid_105 <= 0;
      end 
      if((_dataflow__delay_ready_105 || !_dataflow__delay_valid_105) && _dataflow__delay_ready_104) begin
        _dataflow__delay_valid_105 <= _dataflow__delay_valid_104;
      end 
      if((_dataflow__delay_ready_113 || !_dataflow__delay_valid_113) && _dataflow__delay_ready_112 && _dataflow__delay_valid_112) begin
        _dataflow__delay_data_113 <= _dataflow__delay_data_112;
      end 
      if(_dataflow__delay_valid_113 && _dataflow__delay_ready_113) begin
        _dataflow__delay_valid_113 <= 0;
      end 
      if((_dataflow__delay_ready_113 || !_dataflow__delay_valid_113) && _dataflow__delay_ready_112) begin
        _dataflow__delay_valid_113 <= _dataflow__delay_valid_112;
      end 
      if((_dataflow__delay_ready_121 || !_dataflow__delay_valid_121) && _dataflow__delay_ready_120 && _dataflow__delay_valid_120) begin
        _dataflow__delay_data_121 <= _dataflow__delay_data_120;
      end 
      if(_dataflow__delay_valid_121 && _dataflow__delay_ready_121) begin
        _dataflow__delay_valid_121 <= 0;
      end 
      if((_dataflow__delay_ready_121 || !_dataflow__delay_valid_121) && _dataflow__delay_ready_120) begin
        _dataflow__delay_valid_121 <= _dataflow__delay_valid_120;
      end 
      if((_dataflow__delay_ready_74 || !_dataflow__delay_valid_74) && _dataflow__delay_ready_73 && _dataflow__delay_valid_73) begin
        _dataflow__delay_data_74 <= _dataflow__delay_data_73;
      end 
      if(_dataflow__delay_valid_74 && _dataflow__delay_ready_74) begin
        _dataflow__delay_valid_74 <= 0;
      end 
      if((_dataflow__delay_ready_74 || !_dataflow__delay_valid_74) && _dataflow__delay_ready_73) begin
        _dataflow__delay_valid_74 <= _dataflow__delay_valid_73;
      end 
      if((_dataflow__delay_ready_90 || !_dataflow__delay_valid_90) && _dataflow__delay_ready_89 && _dataflow__delay_valid_89) begin
        _dataflow__delay_data_90 <= _dataflow__delay_data_89;
      end 
      if(_dataflow__delay_valid_90 && _dataflow__delay_ready_90) begin
        _dataflow__delay_valid_90 <= 0;
      end 
      if((_dataflow__delay_ready_90 || !_dataflow__delay_valid_90) && _dataflow__delay_ready_89) begin
        _dataflow__delay_valid_90 <= _dataflow__delay_valid_89;
      end 
      if((_dataflow__delay_ready_98 || !_dataflow__delay_valid_98) && _dataflow__delay_ready_97 && _dataflow__delay_valid_97) begin
        _dataflow__delay_data_98 <= _dataflow__delay_data_97;
      end 
      if(_dataflow__delay_valid_98 && _dataflow__delay_ready_98) begin
        _dataflow__delay_valid_98 <= 0;
      end 
      if((_dataflow__delay_ready_98 || !_dataflow__delay_valid_98) && _dataflow__delay_ready_97) begin
        _dataflow__delay_valid_98 <= _dataflow__delay_valid_97;
      end 
      if((_dataflow__delay_ready_106 || !_dataflow__delay_valid_106) && _dataflow__delay_ready_105 && _dataflow__delay_valid_105) begin
        _dataflow__delay_data_106 <= _dataflow__delay_data_105;
      end 
      if(_dataflow__delay_valid_106 && _dataflow__delay_ready_106) begin
        _dataflow__delay_valid_106 <= 0;
      end 
      if((_dataflow__delay_ready_106 || !_dataflow__delay_valid_106) && _dataflow__delay_ready_105) begin
        _dataflow__delay_valid_106 <= _dataflow__delay_valid_105;
      end 
      if((_dataflow__delay_ready_114 || !_dataflow__delay_valid_114) && _dataflow__delay_ready_113 && _dataflow__delay_valid_113) begin
        _dataflow__delay_data_114 <= _dataflow__delay_data_113;
      end 
      if(_dataflow__delay_valid_114 && _dataflow__delay_ready_114) begin
        _dataflow__delay_valid_114 <= 0;
      end 
      if((_dataflow__delay_ready_114 || !_dataflow__delay_valid_114) && _dataflow__delay_ready_113) begin
        _dataflow__delay_valid_114 <= _dataflow__delay_valid_113;
      end 
      if((_dataflow__delay_ready_122 || !_dataflow__delay_valid_122) && _dataflow__delay_ready_121 && _dataflow__delay_valid_121) begin
        _dataflow__delay_data_122 <= _dataflow__delay_data_121;
      end 
      if(_dataflow__delay_valid_122 && _dataflow__delay_ready_122) begin
        _dataflow__delay_valid_122 <= 0;
      end 
      if((_dataflow__delay_ready_122 || !_dataflow__delay_valid_122) && _dataflow__delay_ready_121) begin
        _dataflow__delay_valid_122 <= _dataflow__delay_valid_121;
      end 
      if((_dataflow__delay_ready_75 || !_dataflow__delay_valid_75) && _dataflow__delay_ready_74 && _dataflow__delay_valid_74) begin
        _dataflow__delay_data_75 <= _dataflow__delay_data_74;
      end 
      if(_dataflow__delay_valid_75 && _dataflow__delay_ready_75) begin
        _dataflow__delay_valid_75 <= 0;
      end 
      if((_dataflow__delay_ready_75 || !_dataflow__delay_valid_75) && _dataflow__delay_ready_74) begin
        _dataflow__delay_valid_75 <= _dataflow__delay_valid_74;
      end 
      if((_dataflow__delay_ready_91 || !_dataflow__delay_valid_91) && _dataflow__delay_ready_90 && _dataflow__delay_valid_90) begin
        _dataflow__delay_data_91 <= _dataflow__delay_data_90;
      end 
      if(_dataflow__delay_valid_91 && _dataflow__delay_ready_91) begin
        _dataflow__delay_valid_91 <= 0;
      end 
      if((_dataflow__delay_ready_91 || !_dataflow__delay_valid_91) && _dataflow__delay_ready_90) begin
        _dataflow__delay_valid_91 <= _dataflow__delay_valid_90;
      end 
      if((_dataflow__delay_ready_99 || !_dataflow__delay_valid_99) && _dataflow__delay_ready_98 && _dataflow__delay_valid_98) begin
        _dataflow__delay_data_99 <= _dataflow__delay_data_98;
      end 
      if(_dataflow__delay_valid_99 && _dataflow__delay_ready_99) begin
        _dataflow__delay_valid_99 <= 0;
      end 
      if((_dataflow__delay_ready_99 || !_dataflow__delay_valid_99) && _dataflow__delay_ready_98) begin
        _dataflow__delay_valid_99 <= _dataflow__delay_valid_98;
      end 
      if((_dataflow__delay_ready_107 || !_dataflow__delay_valid_107) && _dataflow__delay_ready_106 && _dataflow__delay_valid_106) begin
        _dataflow__delay_data_107 <= _dataflow__delay_data_106;
      end 
      if(_dataflow__delay_valid_107 && _dataflow__delay_ready_107) begin
        _dataflow__delay_valid_107 <= 0;
      end 
      if((_dataflow__delay_ready_107 || !_dataflow__delay_valid_107) && _dataflow__delay_ready_106) begin
        _dataflow__delay_valid_107 <= _dataflow__delay_valid_106;
      end 
      if((_dataflow__delay_ready_115 || !_dataflow__delay_valid_115) && _dataflow__delay_ready_114 && _dataflow__delay_valid_114) begin
        _dataflow__delay_data_115 <= _dataflow__delay_data_114;
      end 
      if(_dataflow__delay_valid_115 && _dataflow__delay_ready_115) begin
        _dataflow__delay_valid_115 <= 0;
      end 
      if((_dataflow__delay_ready_115 || !_dataflow__delay_valid_115) && _dataflow__delay_ready_114) begin
        _dataflow__delay_valid_115 <= _dataflow__delay_valid_114;
      end 
      if((_dataflow__delay_ready_123 || !_dataflow__delay_valid_123) && _dataflow__delay_ready_122 && _dataflow__delay_valid_122) begin
        _dataflow__delay_data_123 <= _dataflow__delay_data_122;
      end 
      if(_dataflow__delay_valid_123 && _dataflow__delay_ready_123) begin
        _dataflow__delay_valid_123 <= 0;
      end 
      if((_dataflow__delay_ready_123 || !_dataflow__delay_valid_123) && _dataflow__delay_ready_122) begin
        _dataflow__delay_valid_123 <= _dataflow__delay_valid_122;
      end 
      if((_dataflow__delay_ready_76 || !_dataflow__delay_valid_76) && _dataflow__delay_ready_75 && _dataflow__delay_valid_75) begin
        _dataflow__delay_data_76 <= _dataflow__delay_data_75;
      end 
      if(_dataflow__delay_valid_76 && _dataflow__delay_ready_76) begin
        _dataflow__delay_valid_76 <= 0;
      end 
      if((_dataflow__delay_ready_76 || !_dataflow__delay_valid_76) && _dataflow__delay_ready_75) begin
        _dataflow__delay_valid_76 <= _dataflow__delay_valid_75;
      end 
      if((_dataflow__delay_ready_92 || !_dataflow__delay_valid_92) && _dataflow__delay_ready_91 && _dataflow__delay_valid_91) begin
        _dataflow__delay_data_92 <= _dataflow__delay_data_91;
      end 
      if(_dataflow__delay_valid_92 && _dataflow__delay_ready_92) begin
        _dataflow__delay_valid_92 <= 0;
      end 
      if((_dataflow__delay_ready_92 || !_dataflow__delay_valid_92) && _dataflow__delay_ready_91) begin
        _dataflow__delay_valid_92 <= _dataflow__delay_valid_91;
      end 
      if((_dataflow__delay_ready_100 || !_dataflow__delay_valid_100) && _dataflow__delay_ready_99 && _dataflow__delay_valid_99) begin
        _dataflow__delay_data_100 <= _dataflow__delay_data_99;
      end 
      if(_dataflow__delay_valid_100 && _dataflow__delay_ready_100) begin
        _dataflow__delay_valid_100 <= 0;
      end 
      if((_dataflow__delay_ready_100 || !_dataflow__delay_valid_100) && _dataflow__delay_ready_99) begin
        _dataflow__delay_valid_100 <= _dataflow__delay_valid_99;
      end 
      if((_dataflow__delay_ready_108 || !_dataflow__delay_valid_108) && _dataflow__delay_ready_107 && _dataflow__delay_valid_107) begin
        _dataflow__delay_data_108 <= _dataflow__delay_data_107;
      end 
      if(_dataflow__delay_valid_108 && _dataflow__delay_ready_108) begin
        _dataflow__delay_valid_108 <= 0;
      end 
      if((_dataflow__delay_ready_108 || !_dataflow__delay_valid_108) && _dataflow__delay_ready_107) begin
        _dataflow__delay_valid_108 <= _dataflow__delay_valid_107;
      end 
      if((_dataflow__delay_ready_116 || !_dataflow__delay_valid_116) && _dataflow__delay_ready_115 && _dataflow__delay_valid_115) begin
        _dataflow__delay_data_116 <= _dataflow__delay_data_115;
      end 
      if(_dataflow__delay_valid_116 && _dataflow__delay_ready_116) begin
        _dataflow__delay_valid_116 <= 0;
      end 
      if((_dataflow__delay_ready_116 || !_dataflow__delay_valid_116) && _dataflow__delay_ready_115) begin
        _dataflow__delay_valid_116 <= _dataflow__delay_valid_115;
      end 
      if((_dataflow__delay_ready_124 || !_dataflow__delay_valid_124) && _dataflow__delay_ready_123 && _dataflow__delay_valid_123) begin
        _dataflow__delay_data_124 <= _dataflow__delay_data_123;
      end 
      if(_dataflow__delay_valid_124 && _dataflow__delay_ready_124) begin
        _dataflow__delay_valid_124 <= 0;
      end 
      if((_dataflow__delay_ready_124 || !_dataflow__delay_valid_124) && _dataflow__delay_ready_123) begin
        _dataflow__delay_valid_124 <= _dataflow__delay_valid_123;
      end 
      if((_dataflow__delay_ready_77 || !_dataflow__delay_valid_77) && _dataflow__delay_ready_76 && _dataflow__delay_valid_76) begin
        _dataflow__delay_data_77 <= _dataflow__delay_data_76;
      end 
      if(_dataflow__delay_valid_77 && _dataflow__delay_ready_77) begin
        _dataflow__delay_valid_77 <= 0;
      end 
      if((_dataflow__delay_ready_77 || !_dataflow__delay_valid_77) && _dataflow__delay_ready_76) begin
        _dataflow__delay_valid_77 <= _dataflow__delay_valid_76;
      end 
      if((_dataflow__delay_ready_93 || !_dataflow__delay_valid_93) && _dataflow__delay_ready_92 && _dataflow__delay_valid_92) begin
        _dataflow__delay_data_93 <= _dataflow__delay_data_92;
      end 
      if(_dataflow__delay_valid_93 && _dataflow__delay_ready_93) begin
        _dataflow__delay_valid_93 <= 0;
      end 
      if((_dataflow__delay_ready_93 || !_dataflow__delay_valid_93) && _dataflow__delay_ready_92) begin
        _dataflow__delay_valid_93 <= _dataflow__delay_valid_92;
      end 
      if((_dataflow__delay_ready_101 || !_dataflow__delay_valid_101) && _dataflow__delay_ready_100 && _dataflow__delay_valid_100) begin
        _dataflow__delay_data_101 <= _dataflow__delay_data_100;
      end 
      if(_dataflow__delay_valid_101 && _dataflow__delay_ready_101) begin
        _dataflow__delay_valid_101 <= 0;
      end 
      if((_dataflow__delay_ready_101 || !_dataflow__delay_valid_101) && _dataflow__delay_ready_100) begin
        _dataflow__delay_valid_101 <= _dataflow__delay_valid_100;
      end 
      if((_dataflow__delay_ready_109 || !_dataflow__delay_valid_109) && _dataflow__delay_ready_108 && _dataflow__delay_valid_108) begin
        _dataflow__delay_data_109 <= _dataflow__delay_data_108;
      end 
      if(_dataflow__delay_valid_109 && _dataflow__delay_ready_109) begin
        _dataflow__delay_valid_109 <= 0;
      end 
      if((_dataflow__delay_ready_109 || !_dataflow__delay_valid_109) && _dataflow__delay_ready_108) begin
        _dataflow__delay_valid_109 <= _dataflow__delay_valid_108;
      end 
      if((_dataflow__delay_ready_117 || !_dataflow__delay_valid_117) && _dataflow__delay_ready_116 && _dataflow__delay_valid_116) begin
        _dataflow__delay_data_117 <= _dataflow__delay_data_116;
      end 
      if(_dataflow__delay_valid_117 && _dataflow__delay_ready_117) begin
        _dataflow__delay_valid_117 <= 0;
      end 
      if((_dataflow__delay_ready_117 || !_dataflow__delay_valid_117) && _dataflow__delay_ready_116) begin
        _dataflow__delay_valid_117 <= _dataflow__delay_valid_116;
      end 
      if((_dataflow__delay_ready_125 || !_dataflow__delay_valid_125) && _dataflow__delay_ready_124 && _dataflow__delay_valid_124) begin
        _dataflow__delay_data_125 <= _dataflow__delay_data_124;
      end 
      if(_dataflow__delay_valid_125 && _dataflow__delay_ready_125) begin
        _dataflow__delay_valid_125 <= 0;
      end 
      if((_dataflow__delay_ready_125 || !_dataflow__delay_valid_125) && _dataflow__delay_ready_124) begin
        _dataflow__delay_valid_125 <= _dataflow__delay_valid_124;
      end 
      if((_dataflow__delay_ready_78 || !_dataflow__delay_valid_78) && _dataflow__delay_ready_77 && _dataflow__delay_valid_77) begin
        _dataflow__delay_data_78 <= _dataflow__delay_data_77;
      end 
      if(_dataflow__delay_valid_78 && _dataflow__delay_ready_78) begin
        _dataflow__delay_valid_78 <= 0;
      end 
      if((_dataflow__delay_ready_78 || !_dataflow__delay_valid_78) && _dataflow__delay_ready_77) begin
        _dataflow__delay_valid_78 <= _dataflow__delay_valid_77;
      end 
      if((_dataflow__delay_ready_94 || !_dataflow__delay_valid_94) && _dataflow__delay_ready_93 && _dataflow__delay_valid_93) begin
        _dataflow__delay_data_94 <= _dataflow__delay_data_93;
      end 
      if(_dataflow__delay_valid_94 && _dataflow__delay_ready_94) begin
        _dataflow__delay_valid_94 <= 0;
      end 
      if((_dataflow__delay_ready_94 || !_dataflow__delay_valid_94) && _dataflow__delay_ready_93) begin
        _dataflow__delay_valid_94 <= _dataflow__delay_valid_93;
      end 
      if((_dataflow__delay_ready_102 || !_dataflow__delay_valid_102) && _dataflow__delay_ready_101 && _dataflow__delay_valid_101) begin
        _dataflow__delay_data_102 <= _dataflow__delay_data_101;
      end 
      if(_dataflow__delay_valid_102 && _dataflow__delay_ready_102) begin
        _dataflow__delay_valid_102 <= 0;
      end 
      if((_dataflow__delay_ready_102 || !_dataflow__delay_valid_102) && _dataflow__delay_ready_101) begin
        _dataflow__delay_valid_102 <= _dataflow__delay_valid_101;
      end 
      if((_dataflow__delay_ready_110 || !_dataflow__delay_valid_110) && _dataflow__delay_ready_109 && _dataflow__delay_valid_109) begin
        _dataflow__delay_data_110 <= _dataflow__delay_data_109;
      end 
      if(_dataflow__delay_valid_110 && _dataflow__delay_ready_110) begin
        _dataflow__delay_valid_110 <= 0;
      end 
      if((_dataflow__delay_ready_110 || !_dataflow__delay_valid_110) && _dataflow__delay_ready_109) begin
        _dataflow__delay_valid_110 <= _dataflow__delay_valid_109;
      end 
      if((_dataflow__delay_ready_118 || !_dataflow__delay_valid_118) && _dataflow__delay_ready_117 && _dataflow__delay_valid_117) begin
        _dataflow__delay_data_118 <= _dataflow__delay_data_117;
      end 
      if(_dataflow__delay_valid_118 && _dataflow__delay_ready_118) begin
        _dataflow__delay_valid_118 <= 0;
      end 
      if((_dataflow__delay_ready_118 || !_dataflow__delay_valid_118) && _dataflow__delay_ready_117) begin
        _dataflow__delay_valid_118 <= _dataflow__delay_valid_117;
      end 
      if((_dataflow__delay_ready_126 || !_dataflow__delay_valid_126) && _dataflow__delay_ready_125 && _dataflow__delay_valid_125) begin
        _dataflow__delay_data_126 <= _dataflow__delay_data_125;
      end 
      if(_dataflow__delay_valid_126 && _dataflow__delay_ready_126) begin
        _dataflow__delay_valid_126 <= 0;
      end 
      if((_dataflow__delay_ready_126 || !_dataflow__delay_valid_126) && _dataflow__delay_ready_125) begin
        _dataflow__delay_valid_126 <= _dataflow__delay_valid_125;
      end 
      if((_dataflow_minus_ready_62 || !_dataflow_minus_valid_62) && (_dataflow_times_ready_54 && _dataflow_times_ready_56) && (_dataflow_times_valid_54 && _dataflow_times_valid_56)) begin
        _dataflow_minus_data_62 <= _dataflow_times_data_54 - _dataflow_times_data_56;
      end 
      if(_dataflow_minus_valid_62 && _dataflow_minus_ready_62) begin
        _dataflow_minus_valid_62 <= 0;
      end 
      if((_dataflow_minus_ready_62 || !_dataflow_minus_valid_62) && (_dataflow_times_ready_54 && _dataflow_times_ready_56)) begin
        _dataflow_minus_valid_62 <= _dataflow_times_valid_54 && _dataflow_times_valid_56;
      end 
      if((_dataflow_plus_ready_63 || !_dataflow_plus_valid_63) && (_dataflow_times_ready_58 && _dataflow_times_ready_60) && (_dataflow_times_valid_58 && _dataflow_times_valid_60)) begin
        _dataflow_plus_data_63 <= _dataflow_times_data_58 + _dataflow_times_data_60;
      end 
      if(_dataflow_plus_valid_63 && _dataflow_plus_ready_63) begin
        _dataflow_plus_valid_63 <= 0;
      end 
      if((_dataflow_plus_ready_63 || !_dataflow_plus_valid_63) && (_dataflow_times_ready_58 && _dataflow_times_ready_60)) begin
        _dataflow_plus_valid_63 <= _dataflow_times_valid_58 && _dataflow_times_valid_60;
      end 
      if((_dataflow__delay_ready_79 || !_dataflow__delay_valid_79) && _dataflow__delay_ready_78 && _dataflow__delay_valid_78) begin
        _dataflow__delay_data_79 <= _dataflow__delay_data_78;
      end 
      if(_dataflow__delay_valid_79 && _dataflow__delay_ready_79) begin
        _dataflow__delay_valid_79 <= 0;
      end 
      if((_dataflow__delay_ready_79 || !_dataflow__delay_valid_79) && _dataflow__delay_ready_78) begin
        _dataflow__delay_valid_79 <= _dataflow__delay_valid_78;
      end 
      if((_dataflow__delay_ready_95 || !_dataflow__delay_valid_95) && _dataflow__delay_ready_94 && _dataflow__delay_valid_94) begin
        _dataflow__delay_data_95 <= _dataflow__delay_data_94;
      end 
      if(_dataflow__delay_valid_95 && _dataflow__delay_ready_95) begin
        _dataflow__delay_valid_95 <= 0;
      end 
      if((_dataflow__delay_ready_95 || !_dataflow__delay_valid_95) && _dataflow__delay_ready_94) begin
        _dataflow__delay_valid_95 <= _dataflow__delay_valid_94;
      end 
      if((_dataflow__delay_ready_103 || !_dataflow__delay_valid_103) && _dataflow__delay_ready_102 && _dataflow__delay_valid_102) begin
        _dataflow__delay_data_103 <= _dataflow__delay_data_102;
      end 
      if(_dataflow__delay_valid_103 && _dataflow__delay_ready_103) begin
        _dataflow__delay_valid_103 <= 0;
      end 
      if((_dataflow__delay_ready_103 || !_dataflow__delay_valid_103) && _dataflow__delay_ready_102) begin
        _dataflow__delay_valid_103 <= _dataflow__delay_valid_102;
      end 
      if((_dataflow__delay_ready_111 || !_dataflow__delay_valid_111) && _dataflow__delay_ready_110 && _dataflow__delay_valid_110) begin
        _dataflow__delay_data_111 <= _dataflow__delay_data_110;
      end 
      if(_dataflow__delay_valid_111 && _dataflow__delay_ready_111) begin
        _dataflow__delay_valid_111 <= 0;
      end 
      if((_dataflow__delay_ready_111 || !_dataflow__delay_valid_111) && _dataflow__delay_ready_110) begin
        _dataflow__delay_valid_111 <= _dataflow__delay_valid_110;
      end 
      if((_dataflow__delay_ready_119 || !_dataflow__delay_valid_119) && _dataflow__delay_ready_118 && _dataflow__delay_valid_118) begin
        _dataflow__delay_data_119 <= _dataflow__delay_data_118;
      end 
      if(_dataflow__delay_valid_119 && _dataflow__delay_ready_119) begin
        _dataflow__delay_valid_119 <= 0;
      end 
      if((_dataflow__delay_ready_119 || !_dataflow__delay_valid_119) && _dataflow__delay_ready_118) begin
        _dataflow__delay_valid_119 <= _dataflow__delay_valid_118;
      end 
      if((_dataflow__delay_ready_127 || !_dataflow__delay_valid_127) && _dataflow__delay_ready_126 && _dataflow__delay_valid_126) begin
        _dataflow__delay_data_127 <= _dataflow__delay_data_126;
      end 
      if(_dataflow__delay_valid_127 && _dataflow__delay_ready_127) begin
        _dataflow__delay_valid_127 <= 0;
      end 
      if((_dataflow__delay_ready_127 || !_dataflow__delay_valid_127) && _dataflow__delay_ready_126) begin
        _dataflow__delay_valid_127 <= _dataflow__delay_valid_126;
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
