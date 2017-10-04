from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_radix2

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg signed [32-1:0] din0re;
  reg signed [32-1:0] din0im;
  reg signed [32-1:0] din1re;
  reg signed [32-1:0] din1im;
  reg signed [32-1:0] cnstre;
  reg signed [32-1:0] cnstim;
  wire signed [32-1:0] dout1re;
  wire signed [32-1:0] dout1im;
  wire signed [32-1:0] dout0re;
  wire signed [32-1:0] dout0im;

  radix2
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .din0re(din0re),
    .din0im(din0im),
    .din1re(din1re),
    .din1im(din1im),
    .cnstre(cnstre),
    .cnstim(cnstim),
    .dout1re(dout1re),
    .dout1im(dout1im),
    .dout0re(dout0re),
    .dout0im(dout0im)
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
    din0re = 2;
    din0im = 0;
    din1re = 1;
    din1im = 0;
    cnstre = 0;
    cnstim = 1;
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
          send_fsm <= send_fsm_2;
        end
        send_fsm_2: begin
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
          $finish;
        end
      endcase
    end
  end


endmodule



module radix2
(
  input CLK,
  input RST,
  input signed [32-1:0] din0re,
  input signed [32-1:0] din0im,
  input signed [32-1:0] din1re,
  input signed [32-1:0] din1im,
  input signed [32-1:0] cnstre,
  input signed [32-1:0] cnstim,
  output signed [32-1:0] dout1re,
  output signed [32-1:0] dout1im,
  output signed [32-1:0] dout0re,
  output signed [32-1:0] dout0im
);

  reg signed [32-1:0] _plus_data_0;
  reg _plus_valid_0;
  wire _plus_ready_0;
  reg signed [32-1:0] _plus_data_1;
  reg _plus_valid_1;
  wire _plus_ready_1;
  reg signed [32-1:0] _minus_data_2;
  reg _minus_valid_2;
  wire _minus_ready_2;
  reg signed [32-1:0] _minus_data_3;
  reg _minus_valid_3;
  wire _minus_ready_3;
  reg signed [32-1:0] __delay_data_4;
  reg __delay_valid_4;
  wire __delay_ready_4;
  reg signed [32-1:0] __delay_data_5;
  reg __delay_valid_5;
  wire __delay_ready_5;
  wire signed [32-1:0] _times_data_6;
  wire _times_valid_6;
  wire _times_ready_6;
  wire signed [64-1:0] _times_odata_6;
  reg signed [64-1:0] _times_data_reg_6;
  assign _times_data_6 = _times_data_reg_6;
  wire _times_ovalid_6;
  reg _times_valid_reg_6;
  assign _times_valid_6 = _times_valid_reg_6;
  wire _times_enable_6;
  wire _times_update_6;
  assign _times_enable_6 = (_times_ready_6 || !_times_valid_6) && (_minus_ready_2 && __delay_ready_4) && (_minus_valid_2 && __delay_valid_4);
  assign _times_update_6 = _times_ready_6 || !_times_valid_6;

  multiplier_0
  mul6
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_6),
    .enable(_times_enable_6),
    .valid(_times_ovalid_6),
    .a(_minus_data_2),
    .b(__delay_data_4),
    .c(_times_odata_6)
  );

  wire signed [32-1:0] _times_data_7;
  wire _times_valid_7;
  wire _times_ready_7;
  wire signed [64-1:0] _times_odata_7;
  reg signed [64-1:0] _times_data_reg_7;
  assign _times_data_7 = _times_data_reg_7;
  wire _times_ovalid_7;
  reg _times_valid_reg_7;
  assign _times_valid_7 = _times_valid_reg_7;
  wire _times_enable_7;
  wire _times_update_7;
  assign _times_enable_7 = (_times_ready_7 || !_times_valid_7) && (_minus_ready_3 && __delay_ready_5) && (_minus_valid_3 && __delay_valid_5);
  assign _times_update_7 = _times_ready_7 || !_times_valid_7;

  multiplier_1
  mul7
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_7),
    .enable(_times_enable_7),
    .valid(_times_ovalid_7),
    .a(_minus_data_3),
    .b(__delay_data_5),
    .c(_times_odata_7)
  );

  wire signed [32-1:0] _times_data_8;
  wire _times_valid_8;
  wire _times_ready_8;
  wire signed [64-1:0] _times_odata_8;
  reg signed [64-1:0] _times_data_reg_8;
  assign _times_data_8 = _times_data_reg_8;
  wire _times_ovalid_8;
  reg _times_valid_reg_8;
  assign _times_valid_8 = _times_valid_reg_8;
  wire _times_enable_8;
  wire _times_update_8;
  assign _times_enable_8 = (_times_ready_8 || !_times_valid_8) && (_minus_ready_2 && __delay_ready_5) && (_minus_valid_2 && __delay_valid_5);
  assign _times_update_8 = _times_ready_8 || !_times_valid_8;

  multiplier_2
  mul8
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_8),
    .enable(_times_enable_8),
    .valid(_times_ovalid_8),
    .a(_minus_data_2),
    .b(__delay_data_5),
    .c(_times_odata_8)
  );

  assign _minus_ready_2 = (_times_ready_6 || !_times_valid_6) && (_minus_valid_2 && __delay_valid_4) && ((_times_ready_8 || !_times_valid_8) && (_minus_valid_2 && __delay_valid_5));
  assign __delay_ready_5 = (_times_ready_7 || !_times_valid_7) && (_minus_valid_3 && __delay_valid_5) && ((_times_ready_8 || !_times_valid_8) && (_minus_valid_2 && __delay_valid_5));
  wire signed [32-1:0] _times_data_9;
  wire _times_valid_9;
  wire _times_ready_9;
  wire signed [64-1:0] _times_odata_9;
  reg signed [64-1:0] _times_data_reg_9;
  assign _times_data_9 = _times_data_reg_9;
  wire _times_ovalid_9;
  reg _times_valid_reg_9;
  assign _times_valid_9 = _times_valid_reg_9;
  wire _times_enable_9;
  wire _times_update_9;
  assign _times_enable_9 = (_times_ready_9 || !_times_valid_9) && (_minus_ready_3 && __delay_ready_4) && (_minus_valid_3 && __delay_valid_4);
  assign _times_update_9 = _times_ready_9 || !_times_valid_9;

  multiplier_3
  mul9
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_9),
    .enable(_times_enable_9),
    .valid(_times_ovalid_9),
    .a(_minus_data_3),
    .b(__delay_data_4),
    .c(_times_odata_9)
  );

  assign _minus_ready_3 = (_times_ready_7 || !_times_valid_7) && (_minus_valid_3 && __delay_valid_5) && ((_times_ready_9 || !_times_valid_9) && (_minus_valid_3 && __delay_valid_4));
  assign __delay_ready_4 = (_times_ready_6 || !_times_valid_6) && (_minus_valid_2 && __delay_valid_4) && ((_times_ready_9 || !_times_valid_9) && (_minus_valid_3 && __delay_valid_4));
  reg signed [32-1:0] __delay_data_10;
  reg __delay_valid_10;
  wire __delay_ready_10;
  assign _plus_ready_0 = (__delay_ready_10 || !__delay_valid_10) && _plus_valid_0;
  reg signed [32-1:0] __delay_data_11;
  reg __delay_valid_11;
  wire __delay_ready_11;
  assign _plus_ready_1 = (__delay_ready_11 || !__delay_valid_11) && _plus_valid_1;
  reg signed [32-1:0] __delay_data_12;
  reg __delay_valid_12;
  wire __delay_ready_12;
  assign __delay_ready_10 = (__delay_ready_12 || !__delay_valid_12) && __delay_valid_10;
  reg signed [32-1:0] __delay_data_13;
  reg __delay_valid_13;
  wire __delay_ready_13;
  assign __delay_ready_11 = (__delay_ready_13 || !__delay_valid_13) && __delay_valid_11;
  reg signed [32-1:0] __delay_data_14;
  reg __delay_valid_14;
  wire __delay_ready_14;
  assign __delay_ready_12 = (__delay_ready_14 || !__delay_valid_14) && __delay_valid_12;
  reg signed [32-1:0] __delay_data_15;
  reg __delay_valid_15;
  wire __delay_ready_15;
  assign __delay_ready_13 = (__delay_ready_15 || !__delay_valid_15) && __delay_valid_13;
  reg signed [32-1:0] __delay_data_16;
  reg __delay_valid_16;
  wire __delay_ready_16;
  assign __delay_ready_14 = (__delay_ready_16 || !__delay_valid_16) && __delay_valid_14;
  reg signed [32-1:0] __delay_data_17;
  reg __delay_valid_17;
  wire __delay_ready_17;
  assign __delay_ready_15 = (__delay_ready_17 || !__delay_valid_17) && __delay_valid_15;
  reg signed [32-1:0] __delay_data_18;
  reg __delay_valid_18;
  wire __delay_ready_18;
  assign __delay_ready_16 = (__delay_ready_18 || !__delay_valid_18) && __delay_valid_16;
  reg signed [32-1:0] __delay_data_19;
  reg __delay_valid_19;
  wire __delay_ready_19;
  assign __delay_ready_17 = (__delay_ready_19 || !__delay_valid_19) && __delay_valid_17;
  reg signed [32-1:0] __delay_data_20;
  reg __delay_valid_20;
  wire __delay_ready_20;
  assign __delay_ready_18 = (__delay_ready_20 || !__delay_valid_20) && __delay_valid_18;
  reg signed [32-1:0] __delay_data_21;
  reg __delay_valid_21;
  wire __delay_ready_21;
  assign __delay_ready_19 = (__delay_ready_21 || !__delay_valid_21) && __delay_valid_19;
  reg signed [32-1:0] __delay_data_22;
  reg __delay_valid_22;
  wire __delay_ready_22;
  assign __delay_ready_20 = (__delay_ready_22 || !__delay_valid_22) && __delay_valid_20;
  reg signed [32-1:0] __delay_data_23;
  reg __delay_valid_23;
  wire __delay_ready_23;
  assign __delay_ready_21 = (__delay_ready_23 || !__delay_valid_23) && __delay_valid_21;
  reg signed [32-1:0] _minus_data_24;
  reg _minus_valid_24;
  wire _minus_ready_24;
  assign _times_ready_6 = (_minus_ready_24 || !_minus_valid_24) && (_times_valid_6 && _times_valid_7);
  assign _times_ready_7 = (_minus_ready_24 || !_minus_valid_24) && (_times_valid_6 && _times_valid_7);
  reg signed [32-1:0] _plus_data_25;
  reg _plus_valid_25;
  wire _plus_ready_25;
  assign _times_ready_8 = (_plus_ready_25 || !_plus_valid_25) && (_times_valid_8 && _times_valid_9);
  assign _times_ready_9 = (_plus_ready_25 || !_plus_valid_25) && (_times_valid_8 && _times_valid_9);
  reg signed [32-1:0] __delay_data_26;
  reg __delay_valid_26;
  wire __delay_ready_26;
  assign __delay_ready_22 = (__delay_ready_26 || !__delay_valid_26) && __delay_valid_22;
  reg signed [32-1:0] __delay_data_27;
  reg __delay_valid_27;
  wire __delay_ready_27;
  assign __delay_ready_23 = (__delay_ready_27 || !__delay_valid_27) && __delay_valid_23;
  assign dout1re = _minus_data_24;
  assign _minus_ready_24 = 1;
  assign dout1im = _plus_data_25;
  assign _plus_ready_25 = 1;
  assign dout0re = __delay_data_26;
  assign __delay_ready_26 = 1;
  assign dout0im = __delay_data_27;
  assign __delay_ready_27 = 1;

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
      __delay_data_4 <= 0;
      __delay_valid_4 <= 0;
      __delay_data_5 <= 0;
      __delay_valid_5 <= 0;
      _times_data_reg_6 <= 0;
      _times_valid_reg_6 <= 0;
      _times_data_reg_7 <= 0;
      _times_valid_reg_7 <= 0;
      _times_data_reg_8 <= 0;
      _times_valid_reg_8 <= 0;
      _times_data_reg_9 <= 0;
      _times_valid_reg_9 <= 0;
      __delay_data_10 <= 0;
      __delay_valid_10 <= 0;
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
      __delay_data_19 <= 0;
      __delay_valid_19 <= 0;
      __delay_data_20 <= 0;
      __delay_valid_20 <= 0;
      __delay_data_21 <= 0;
      __delay_valid_21 <= 0;
      __delay_data_22 <= 0;
      __delay_valid_22 <= 0;
      __delay_data_23 <= 0;
      __delay_valid_23 <= 0;
      _minus_data_24 <= 0;
      _minus_valid_24 <= 0;
      _plus_data_25 <= 0;
      _plus_valid_25 <= 0;
      __delay_data_26 <= 0;
      __delay_valid_26 <= 0;
      __delay_data_27 <= 0;
      __delay_valid_27 <= 0;
    end else begin
      if((_plus_ready_0 || !_plus_valid_0) && 1 && 1) begin
        _plus_data_0 <= din0re + din1re;
      end 
      if(_plus_valid_0 && _plus_ready_0) begin
        _plus_valid_0 <= 0;
      end 
      if((_plus_ready_0 || !_plus_valid_0) && 1) begin
        _plus_valid_0 <= 1;
      end 
      if((_plus_ready_1 || !_plus_valid_1) && 1 && 1) begin
        _plus_data_1 <= din0im + din1im;
      end 
      if(_plus_valid_1 && _plus_ready_1) begin
        _plus_valid_1 <= 0;
      end 
      if((_plus_ready_1 || !_plus_valid_1) && 1) begin
        _plus_valid_1 <= 1;
      end 
      if((_minus_ready_2 || !_minus_valid_2) && 1 && 1) begin
        _minus_data_2 <= din0re - din1re;
      end 
      if(_minus_valid_2 && _minus_ready_2) begin
        _minus_valid_2 <= 0;
      end 
      if((_minus_ready_2 || !_minus_valid_2) && 1) begin
        _minus_valid_2 <= 1;
      end 
      if((_minus_ready_3 || !_minus_valid_3) && 1 && 1) begin
        _minus_data_3 <= din0im - din1im;
      end 
      if(_minus_valid_3 && _minus_ready_3) begin
        _minus_valid_3 <= 0;
      end 
      if((_minus_ready_3 || !_minus_valid_3) && 1) begin
        _minus_valid_3 <= 1;
      end 
      if((__delay_ready_4 || !__delay_valid_4) && 1 && 1) begin
        __delay_data_4 <= cnstre;
      end 
      if(__delay_valid_4 && __delay_ready_4) begin
        __delay_valid_4 <= 0;
      end 
      if((__delay_ready_4 || !__delay_valid_4) && 1) begin
        __delay_valid_4 <= 1;
      end 
      if((__delay_ready_5 || !__delay_valid_5) && 1 && 1) begin
        __delay_data_5 <= cnstim;
      end 
      if(__delay_valid_5 && __delay_ready_5) begin
        __delay_valid_5 <= 0;
      end 
      if((__delay_ready_5 || !__delay_valid_5) && 1) begin
        __delay_valid_5 <= 1;
      end 
      if(_times_ready_6 || !_times_valid_6) begin
        _times_data_reg_6 <= _times_odata_6;
      end 
      if(_times_ready_6 || !_times_valid_6) begin
        _times_valid_reg_6 <= _times_ovalid_6;
      end 
      if(_times_ready_7 || !_times_valid_7) begin
        _times_data_reg_7 <= _times_odata_7;
      end 
      if(_times_ready_7 || !_times_valid_7) begin
        _times_valid_reg_7 <= _times_ovalid_7;
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
      if((__delay_ready_10 || !__delay_valid_10) && _plus_ready_0 && _plus_valid_0) begin
        __delay_data_10 <= _plus_data_0;
      end 
      if(__delay_valid_10 && __delay_ready_10) begin
        __delay_valid_10 <= 0;
      end 
      if((__delay_ready_10 || !__delay_valid_10) && _plus_ready_0) begin
        __delay_valid_10 <= _plus_valid_0;
      end 
      if((__delay_ready_11 || !__delay_valid_11) && _plus_ready_1 && _plus_valid_1) begin
        __delay_data_11 <= _plus_data_1;
      end 
      if(__delay_valid_11 && __delay_ready_11) begin
        __delay_valid_11 <= 0;
      end 
      if((__delay_ready_11 || !__delay_valid_11) && _plus_ready_1) begin
        __delay_valid_11 <= _plus_valid_1;
      end 
      if((__delay_ready_12 || !__delay_valid_12) && __delay_ready_10 && __delay_valid_10) begin
        __delay_data_12 <= __delay_data_10;
      end 
      if(__delay_valid_12 && __delay_ready_12) begin
        __delay_valid_12 <= 0;
      end 
      if((__delay_ready_12 || !__delay_valid_12) && __delay_ready_10) begin
        __delay_valid_12 <= __delay_valid_10;
      end 
      if((__delay_ready_13 || !__delay_valid_13) && __delay_ready_11 && __delay_valid_11) begin
        __delay_data_13 <= __delay_data_11;
      end 
      if(__delay_valid_13 && __delay_ready_13) begin
        __delay_valid_13 <= 0;
      end 
      if((__delay_ready_13 || !__delay_valid_13) && __delay_ready_11) begin
        __delay_valid_13 <= __delay_valid_11;
      end 
      if((__delay_ready_14 || !__delay_valid_14) && __delay_ready_12 && __delay_valid_12) begin
        __delay_data_14 <= __delay_data_12;
      end 
      if(__delay_valid_14 && __delay_ready_14) begin
        __delay_valid_14 <= 0;
      end 
      if((__delay_ready_14 || !__delay_valid_14) && __delay_ready_12) begin
        __delay_valid_14 <= __delay_valid_12;
      end 
      if((__delay_ready_15 || !__delay_valid_15) && __delay_ready_13 && __delay_valid_13) begin
        __delay_data_15 <= __delay_data_13;
      end 
      if(__delay_valid_15 && __delay_ready_15) begin
        __delay_valid_15 <= 0;
      end 
      if((__delay_ready_15 || !__delay_valid_15) && __delay_ready_13) begin
        __delay_valid_15 <= __delay_valid_13;
      end 
      if((__delay_ready_16 || !__delay_valid_16) && __delay_ready_14 && __delay_valid_14) begin
        __delay_data_16 <= __delay_data_14;
      end 
      if(__delay_valid_16 && __delay_ready_16) begin
        __delay_valid_16 <= 0;
      end 
      if((__delay_ready_16 || !__delay_valid_16) && __delay_ready_14) begin
        __delay_valid_16 <= __delay_valid_14;
      end 
      if((__delay_ready_17 || !__delay_valid_17) && __delay_ready_15 && __delay_valid_15) begin
        __delay_data_17 <= __delay_data_15;
      end 
      if(__delay_valid_17 && __delay_ready_17) begin
        __delay_valid_17 <= 0;
      end 
      if((__delay_ready_17 || !__delay_valid_17) && __delay_ready_15) begin
        __delay_valid_17 <= __delay_valid_15;
      end 
      if((__delay_ready_18 || !__delay_valid_18) && __delay_ready_16 && __delay_valid_16) begin
        __delay_data_18 <= __delay_data_16;
      end 
      if(__delay_valid_18 && __delay_ready_18) begin
        __delay_valid_18 <= 0;
      end 
      if((__delay_ready_18 || !__delay_valid_18) && __delay_ready_16) begin
        __delay_valid_18 <= __delay_valid_16;
      end 
      if((__delay_ready_19 || !__delay_valid_19) && __delay_ready_17 && __delay_valid_17) begin
        __delay_data_19 <= __delay_data_17;
      end 
      if(__delay_valid_19 && __delay_ready_19) begin
        __delay_valid_19 <= 0;
      end 
      if((__delay_ready_19 || !__delay_valid_19) && __delay_ready_17) begin
        __delay_valid_19 <= __delay_valid_17;
      end 
      if((__delay_ready_20 || !__delay_valid_20) && __delay_ready_18 && __delay_valid_18) begin
        __delay_data_20 <= __delay_data_18;
      end 
      if(__delay_valid_20 && __delay_ready_20) begin
        __delay_valid_20 <= 0;
      end 
      if((__delay_ready_20 || !__delay_valid_20) && __delay_ready_18) begin
        __delay_valid_20 <= __delay_valid_18;
      end 
      if((__delay_ready_21 || !__delay_valid_21) && __delay_ready_19 && __delay_valid_19) begin
        __delay_data_21 <= __delay_data_19;
      end 
      if(__delay_valid_21 && __delay_ready_21) begin
        __delay_valid_21 <= 0;
      end 
      if((__delay_ready_21 || !__delay_valid_21) && __delay_ready_19) begin
        __delay_valid_21 <= __delay_valid_19;
      end 
      if((__delay_ready_22 || !__delay_valid_22) && __delay_ready_20 && __delay_valid_20) begin
        __delay_data_22 <= __delay_data_20;
      end 
      if(__delay_valid_22 && __delay_ready_22) begin
        __delay_valid_22 <= 0;
      end 
      if((__delay_ready_22 || !__delay_valid_22) && __delay_ready_20) begin
        __delay_valid_22 <= __delay_valid_20;
      end 
      if((__delay_ready_23 || !__delay_valid_23) && __delay_ready_21 && __delay_valid_21) begin
        __delay_data_23 <= __delay_data_21;
      end 
      if(__delay_valid_23 && __delay_ready_23) begin
        __delay_valid_23 <= 0;
      end 
      if((__delay_ready_23 || !__delay_valid_23) && __delay_ready_21) begin
        __delay_valid_23 <= __delay_valid_21;
      end 
      if((_minus_ready_24 || !_minus_valid_24) && (_times_ready_6 && _times_ready_7) && (_times_valid_6 && _times_valid_7)) begin
        _minus_data_24 <= _times_data_6 - _times_data_7;
      end 
      if(_minus_valid_24 && _minus_ready_24) begin
        _minus_valid_24 <= 0;
      end 
      if((_minus_ready_24 || !_minus_valid_24) && (_times_ready_6 && _times_ready_7)) begin
        _minus_valid_24 <= _times_valid_6 && _times_valid_7;
      end 
      if((_plus_ready_25 || !_plus_valid_25) && (_times_ready_8 && _times_ready_9) && (_times_valid_8 && _times_valid_9)) begin
        _plus_data_25 <= _times_data_8 + _times_data_9;
      end 
      if(_plus_valid_25 && _plus_ready_25) begin
        _plus_valid_25 <= 0;
      end 
      if((_plus_ready_25 || !_plus_valid_25) && (_times_ready_8 && _times_ready_9)) begin
        _plus_valid_25 <= _times_valid_8 && _times_valid_9;
      end 
      if((__delay_ready_26 || !__delay_valid_26) && __delay_ready_22 && __delay_valid_22) begin
        __delay_data_26 <= __delay_data_22;
      end 
      if(__delay_valid_26 && __delay_ready_26) begin
        __delay_valid_26 <= 0;
      end 
      if((__delay_ready_26 || !__delay_valid_26) && __delay_ready_22) begin
        __delay_valid_26 <= __delay_valid_22;
      end 
      if((__delay_ready_27 || !__delay_valid_27) && __delay_ready_23 && __delay_valid_23) begin
        __delay_data_27 <= __delay_data_23;
      end 
      if(__delay_valid_27 && __delay_ready_27) begin
        __delay_valid_27 <= 0;
      end 
      if((__delay_ready_27 || !__delay_valid_27) && __delay_ready_23) begin
        __delay_valid_27 <= __delay_valid_23;
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
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
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = dataflow_radix2.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
