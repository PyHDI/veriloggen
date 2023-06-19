from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_radix2

expected_verilog = """

module test
(

);

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
    $dumpfile("dataflow_radix2.vcd");
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

  reg signed [32-1:0] _dataflow_plus_data_6;
  reg _dataflow_plus_valid_6;
  wire _dataflow_plus_ready_6;
  reg signed [32-1:0] _dataflow_plus_data_7;
  reg _dataflow_plus_valid_7;
  wire _dataflow_plus_ready_7;
  reg signed [32-1:0] _dataflow_minus_data_8;
  reg _dataflow_minus_valid_8;
  wire _dataflow_minus_ready_8;
  reg signed [32-1:0] _dataflow_minus_data_9;
  reg _dataflow_minus_valid_9;
  wire _dataflow_minus_ready_9;
  reg signed [32-1:0] _dataflow__delay_data_16;
  reg _dataflow__delay_valid_16;
  wire _dataflow__delay_ready_16;
  reg signed [32-1:0] _dataflow__delay_data_17;
  reg _dataflow__delay_valid_17;
  wire _dataflow__delay_ready_17;
  wire signed [32-1:0] _dataflow_times_data_10;
  wire _dataflow_times_valid_10;
  wire _dataflow_times_ready_10;
  wire signed [64-1:0] _dataflow_times_mul_odata_10;
  reg signed [64-1:0] _dataflow_times_mul_odata_reg_10;
  assign _dataflow_times_data_10 = _dataflow_times_mul_odata_reg_10;
  wire _dataflow_times_mul_ovalid_10;
  reg _dataflow_times_mul_valid_reg_10;
  assign _dataflow_times_valid_10 = _dataflow_times_mul_valid_reg_10;
  wire _dataflow_times_mul_enable_10;
  wire _dataflow_times_mul_update_10;
  assign _dataflow_times_mul_enable_10 = (_dataflow_times_ready_10 || !_dataflow_times_valid_10) && (_dataflow_minus_ready_8 && _dataflow__delay_ready_16) && (_dataflow_minus_valid_8 && _dataflow__delay_valid_16);
  assign _dataflow_times_mul_update_10 = _dataflow_times_ready_10 || !_dataflow_times_valid_10;

  multiplier_0
  _dataflow_times_mul_10
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_10),
    .enable(_dataflow_times_mul_enable_10),
    .valid(_dataflow_times_mul_ovalid_10),
    .a(_dataflow_minus_data_8),
    .b(_dataflow__delay_data_16),
    .c(_dataflow_times_mul_odata_10)
  );

  wire signed [32-1:0] _dataflow_times_data_11;
  wire _dataflow_times_valid_11;
  wire _dataflow_times_ready_11;
  wire signed [64-1:0] _dataflow_times_mul_odata_11;
  reg signed [64-1:0] _dataflow_times_mul_odata_reg_11;
  assign _dataflow_times_data_11 = _dataflow_times_mul_odata_reg_11;
  wire _dataflow_times_mul_ovalid_11;
  reg _dataflow_times_mul_valid_reg_11;
  assign _dataflow_times_valid_11 = _dataflow_times_mul_valid_reg_11;
  wire _dataflow_times_mul_enable_11;
  wire _dataflow_times_mul_update_11;
  assign _dataflow_times_mul_enable_11 = (_dataflow_times_ready_11 || !_dataflow_times_valid_11) && (_dataflow_minus_ready_9 && _dataflow__delay_ready_17) && (_dataflow_minus_valid_9 && _dataflow__delay_valid_17);
  assign _dataflow_times_mul_update_11 = _dataflow_times_ready_11 || !_dataflow_times_valid_11;

  multiplier_1
  _dataflow_times_mul_11
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_11),
    .enable(_dataflow_times_mul_enable_11),
    .valid(_dataflow_times_mul_ovalid_11),
    .a(_dataflow_minus_data_9),
    .b(_dataflow__delay_data_17),
    .c(_dataflow_times_mul_odata_11)
  );

  wire signed [32-1:0] _dataflow_times_data_12;
  wire _dataflow_times_valid_12;
  wire _dataflow_times_ready_12;
  wire signed [64-1:0] _dataflow_times_mul_odata_12;
  reg signed [64-1:0] _dataflow_times_mul_odata_reg_12;
  assign _dataflow_times_data_12 = _dataflow_times_mul_odata_reg_12;
  wire _dataflow_times_mul_ovalid_12;
  reg _dataflow_times_mul_valid_reg_12;
  assign _dataflow_times_valid_12 = _dataflow_times_mul_valid_reg_12;
  wire _dataflow_times_mul_enable_12;
  wire _dataflow_times_mul_update_12;
  assign _dataflow_times_mul_enable_12 = (_dataflow_times_ready_12 || !_dataflow_times_valid_12) && (_dataflow_minus_ready_8 && _dataflow__delay_ready_17) && (_dataflow_minus_valid_8 && _dataflow__delay_valid_17);
  assign _dataflow_times_mul_update_12 = _dataflow_times_ready_12 || !_dataflow_times_valid_12;

  multiplier_2
  _dataflow_times_mul_12
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_12),
    .enable(_dataflow_times_mul_enable_12),
    .valid(_dataflow_times_mul_ovalid_12),
    .a(_dataflow_minus_data_8),
    .b(_dataflow__delay_data_17),
    .c(_dataflow_times_mul_odata_12)
  );

  assign _dataflow_minus_ready_8 = (_dataflow_times_ready_10 || !_dataflow_times_valid_10) && (_dataflow_minus_valid_8 && _dataflow__delay_valid_16) && ((_dataflow_times_ready_12 || !_dataflow_times_valid_12) && (_dataflow_minus_valid_8 && _dataflow__delay_valid_17));
  assign _dataflow__delay_ready_17 = (_dataflow_times_ready_11 || !_dataflow_times_valid_11) && (_dataflow_minus_valid_9 && _dataflow__delay_valid_17) && ((_dataflow_times_ready_12 || !_dataflow_times_valid_12) && (_dataflow_minus_valid_8 && _dataflow__delay_valid_17));
  wire signed [32-1:0] _dataflow_times_data_13;
  wire _dataflow_times_valid_13;
  wire _dataflow_times_ready_13;
  wire signed [64-1:0] _dataflow_times_mul_odata_13;
  reg signed [64-1:0] _dataflow_times_mul_odata_reg_13;
  assign _dataflow_times_data_13 = _dataflow_times_mul_odata_reg_13;
  wire _dataflow_times_mul_ovalid_13;
  reg _dataflow_times_mul_valid_reg_13;
  assign _dataflow_times_valid_13 = _dataflow_times_mul_valid_reg_13;
  wire _dataflow_times_mul_enable_13;
  wire _dataflow_times_mul_update_13;
  assign _dataflow_times_mul_enable_13 = (_dataflow_times_ready_13 || !_dataflow_times_valid_13) && (_dataflow_minus_ready_9 && _dataflow__delay_ready_16) && (_dataflow_minus_valid_9 && _dataflow__delay_valid_16);
  assign _dataflow_times_mul_update_13 = _dataflow_times_ready_13 || !_dataflow_times_valid_13;

  multiplier_3
  _dataflow_times_mul_13
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_13),
    .enable(_dataflow_times_mul_enable_13),
    .valid(_dataflow_times_mul_ovalid_13),
    .a(_dataflow_minus_data_9),
    .b(_dataflow__delay_data_16),
    .c(_dataflow_times_mul_odata_13)
  );

  assign _dataflow_minus_ready_9 = (_dataflow_times_ready_11 || !_dataflow_times_valid_11) && (_dataflow_minus_valid_9 && _dataflow__delay_valid_17) && ((_dataflow_times_ready_13 || !_dataflow_times_valid_13) && (_dataflow_minus_valid_9 && _dataflow__delay_valid_16));
  assign _dataflow__delay_ready_16 = (_dataflow_times_ready_10 || !_dataflow_times_valid_10) && (_dataflow_minus_valid_8 && _dataflow__delay_valid_16) && ((_dataflow_times_ready_13 || !_dataflow_times_valid_13) && (_dataflow_minus_valid_9 && _dataflow__delay_valid_16));
  reg signed [32-1:0] _dataflow__delay_data_18;
  reg _dataflow__delay_valid_18;
  wire _dataflow__delay_ready_18;
  assign _dataflow_plus_ready_6 = (_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow_plus_valid_6;
  reg signed [32-1:0] _dataflow__delay_data_26;
  reg _dataflow__delay_valid_26;
  wire _dataflow__delay_ready_26;
  assign _dataflow_plus_ready_7 = (_dataflow__delay_ready_26 || !_dataflow__delay_valid_26) && _dataflow_plus_valid_7;
  reg signed [32-1:0] _dataflow__delay_data_19;
  reg _dataflow__delay_valid_19;
  wire _dataflow__delay_ready_19;
  assign _dataflow__delay_ready_18 = (_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_valid_18;
  reg signed [32-1:0] _dataflow__delay_data_27;
  reg _dataflow__delay_valid_27;
  wire _dataflow__delay_ready_27;
  assign _dataflow__delay_ready_26 = (_dataflow__delay_ready_27 || !_dataflow__delay_valid_27) && _dataflow__delay_valid_26;
  reg signed [32-1:0] _dataflow__delay_data_20;
  reg _dataflow__delay_valid_20;
  wire _dataflow__delay_ready_20;
  assign _dataflow__delay_ready_19 = (_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_valid_19;
  reg signed [32-1:0] _dataflow__delay_data_28;
  reg _dataflow__delay_valid_28;
  wire _dataflow__delay_ready_28;
  assign _dataflow__delay_ready_27 = (_dataflow__delay_ready_28 || !_dataflow__delay_valid_28) && _dataflow__delay_valid_27;
  reg signed [32-1:0] _dataflow__delay_data_21;
  reg _dataflow__delay_valid_21;
  wire _dataflow__delay_ready_21;
  assign _dataflow__delay_ready_20 = (_dataflow__delay_ready_21 || !_dataflow__delay_valid_21) && _dataflow__delay_valid_20;
  reg signed [32-1:0] _dataflow__delay_data_29;
  reg _dataflow__delay_valid_29;
  wire _dataflow__delay_ready_29;
  assign _dataflow__delay_ready_28 = (_dataflow__delay_ready_29 || !_dataflow__delay_valid_29) && _dataflow__delay_valid_28;
  reg signed [32-1:0] _dataflow__delay_data_22;
  reg _dataflow__delay_valid_22;
  wire _dataflow__delay_ready_22;
  assign _dataflow__delay_ready_21 = (_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && _dataflow__delay_valid_21;
  reg signed [32-1:0] _dataflow__delay_data_30;
  reg _dataflow__delay_valid_30;
  wire _dataflow__delay_ready_30;
  assign _dataflow__delay_ready_29 = (_dataflow__delay_ready_30 || !_dataflow__delay_valid_30) && _dataflow__delay_valid_29;
  reg signed [32-1:0] _dataflow__delay_data_23;
  reg _dataflow__delay_valid_23;
  wire _dataflow__delay_ready_23;
  assign _dataflow__delay_ready_22 = (_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && _dataflow__delay_valid_22;
  reg signed [32-1:0] _dataflow__delay_data_31;
  reg _dataflow__delay_valid_31;
  wire _dataflow__delay_ready_31;
  assign _dataflow__delay_ready_30 = (_dataflow__delay_ready_31 || !_dataflow__delay_valid_31) && _dataflow__delay_valid_30;
  reg signed [32-1:0] _dataflow__delay_data_24;
  reg _dataflow__delay_valid_24;
  wire _dataflow__delay_ready_24;
  assign _dataflow__delay_ready_23 = (_dataflow__delay_ready_24 || !_dataflow__delay_valid_24) && _dataflow__delay_valid_23;
  reg signed [32-1:0] _dataflow__delay_data_32;
  reg _dataflow__delay_valid_32;
  wire _dataflow__delay_ready_32;
  assign _dataflow__delay_ready_31 = (_dataflow__delay_ready_32 || !_dataflow__delay_valid_32) && _dataflow__delay_valid_31;
  reg signed [32-1:0] _dataflow_minus_data_14;
  reg _dataflow_minus_valid_14;
  wire _dataflow_minus_ready_14;
  assign _dataflow_times_ready_10 = (_dataflow_minus_ready_14 || !_dataflow_minus_valid_14) && (_dataflow_times_valid_10 && _dataflow_times_valid_11);
  assign _dataflow_times_ready_11 = (_dataflow_minus_ready_14 || !_dataflow_minus_valid_14) && (_dataflow_times_valid_10 && _dataflow_times_valid_11);
  reg signed [32-1:0] _dataflow_plus_data_15;
  reg _dataflow_plus_valid_15;
  wire _dataflow_plus_ready_15;
  assign _dataflow_times_ready_12 = (_dataflow_plus_ready_15 || !_dataflow_plus_valid_15) && (_dataflow_times_valid_12 && _dataflow_times_valid_13);
  assign _dataflow_times_ready_13 = (_dataflow_plus_ready_15 || !_dataflow_plus_valid_15) && (_dataflow_times_valid_12 && _dataflow_times_valid_13);
  reg signed [32-1:0] _dataflow__delay_data_25;
  reg _dataflow__delay_valid_25;
  wire _dataflow__delay_ready_25;
  assign _dataflow__delay_ready_24 = (_dataflow__delay_ready_25 || !_dataflow__delay_valid_25) && _dataflow__delay_valid_24;
  reg signed [32-1:0] _dataflow__delay_data_33;
  reg _dataflow__delay_valid_33;
  wire _dataflow__delay_ready_33;
  assign _dataflow__delay_ready_32 = (_dataflow__delay_ready_33 || !_dataflow__delay_valid_33) && _dataflow__delay_valid_32;
  assign dout1re = _dataflow_minus_data_14;
  assign _dataflow_minus_ready_14 = 1;
  assign dout1im = _dataflow_plus_data_15;
  assign _dataflow_plus_ready_15 = 1;
  assign dout0re = _dataflow__delay_data_25;
  assign _dataflow__delay_ready_25 = 1;
  assign dout0im = _dataflow__delay_data_33;
  assign _dataflow__delay_ready_33 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_plus_data_6 <= 0;
      _dataflow_plus_valid_6 <= 0;
      _dataflow_plus_data_7 <= 0;
      _dataflow_plus_valid_7 <= 0;
      _dataflow_minus_data_8 <= 0;
      _dataflow_minus_valid_8 <= 0;
      _dataflow_minus_data_9 <= 0;
      _dataflow_minus_valid_9 <= 0;
      _dataflow__delay_data_16 <= 0;
      _dataflow__delay_valid_16 <= 0;
      _dataflow__delay_data_17 <= 0;
      _dataflow__delay_valid_17 <= 0;
      _dataflow_times_mul_odata_reg_10 <= 0;
      _dataflow_times_mul_valid_reg_10 <= 0;
      _dataflow_times_mul_odata_reg_11 <= 0;
      _dataflow_times_mul_valid_reg_11 <= 0;
      _dataflow_times_mul_odata_reg_12 <= 0;
      _dataflow_times_mul_valid_reg_12 <= 0;
      _dataflow_times_mul_odata_reg_13 <= 0;
      _dataflow_times_mul_valid_reg_13 <= 0;
      _dataflow__delay_data_18 <= 0;
      _dataflow__delay_valid_18 <= 0;
      _dataflow__delay_data_26 <= 0;
      _dataflow__delay_valid_26 <= 0;
      _dataflow__delay_data_19 <= 0;
      _dataflow__delay_valid_19 <= 0;
      _dataflow__delay_data_27 <= 0;
      _dataflow__delay_valid_27 <= 0;
      _dataflow__delay_data_20 <= 0;
      _dataflow__delay_valid_20 <= 0;
      _dataflow__delay_data_28 <= 0;
      _dataflow__delay_valid_28 <= 0;
      _dataflow__delay_data_21 <= 0;
      _dataflow__delay_valid_21 <= 0;
      _dataflow__delay_data_29 <= 0;
      _dataflow__delay_valid_29 <= 0;
      _dataflow__delay_data_22 <= 0;
      _dataflow__delay_valid_22 <= 0;
      _dataflow__delay_data_30 <= 0;
      _dataflow__delay_valid_30 <= 0;
      _dataflow__delay_data_23 <= 0;
      _dataflow__delay_valid_23 <= 0;
      _dataflow__delay_data_31 <= 0;
      _dataflow__delay_valid_31 <= 0;
      _dataflow__delay_data_24 <= 0;
      _dataflow__delay_valid_24 <= 0;
      _dataflow__delay_data_32 <= 0;
      _dataflow__delay_valid_32 <= 0;
      _dataflow_minus_data_14 <= 0;
      _dataflow_minus_valid_14 <= 0;
      _dataflow_plus_data_15 <= 0;
      _dataflow_plus_valid_15 <= 0;
      _dataflow__delay_data_25 <= 0;
      _dataflow__delay_valid_25 <= 0;
      _dataflow__delay_data_33 <= 0;
      _dataflow__delay_valid_33 <= 0;
    end else begin
      if((_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && 1 && 1) begin
        _dataflow_plus_data_6 <= din0re + din1re;
      end 
      if(_dataflow_plus_valid_6 && _dataflow_plus_ready_6) begin
        _dataflow_plus_valid_6 <= 0;
      end 
      if((_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && 1) begin
        _dataflow_plus_valid_6 <= 1;
      end 
      if((_dataflow_plus_ready_7 || !_dataflow_plus_valid_7) && 1 && 1) begin
        _dataflow_plus_data_7 <= din0im + din1im;
      end 
      if(_dataflow_plus_valid_7 && _dataflow_plus_ready_7) begin
        _dataflow_plus_valid_7 <= 0;
      end 
      if((_dataflow_plus_ready_7 || !_dataflow_plus_valid_7) && 1) begin
        _dataflow_plus_valid_7 <= 1;
      end 
      if((_dataflow_minus_ready_8 || !_dataflow_minus_valid_8) && 1 && 1) begin
        _dataflow_minus_data_8 <= din0re - din1re;
      end 
      if(_dataflow_minus_valid_8 && _dataflow_minus_ready_8) begin
        _dataflow_minus_valid_8 <= 0;
      end 
      if((_dataflow_minus_ready_8 || !_dataflow_minus_valid_8) && 1) begin
        _dataflow_minus_valid_8 <= 1;
      end 
      if((_dataflow_minus_ready_9 || !_dataflow_minus_valid_9) && 1 && 1) begin
        _dataflow_minus_data_9 <= din0im - din1im;
      end 
      if(_dataflow_minus_valid_9 && _dataflow_minus_ready_9) begin
        _dataflow_minus_valid_9 <= 0;
      end 
      if((_dataflow_minus_ready_9 || !_dataflow_minus_valid_9) && 1) begin
        _dataflow_minus_valid_9 <= 1;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && 1 && 1) begin
        _dataflow__delay_data_16 <= cnstre;
      end 
      if(_dataflow__delay_valid_16 && _dataflow__delay_ready_16) begin
        _dataflow__delay_valid_16 <= 0;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && 1) begin
        _dataflow__delay_valid_16 <= 1;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && 1 && 1) begin
        _dataflow__delay_data_17 <= cnstim;
      end 
      if(_dataflow__delay_valid_17 && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_17 <= 0;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && 1) begin
        _dataflow__delay_valid_17 <= 1;
      end 
      if(_dataflow_times_ready_10 || !_dataflow_times_valid_10) begin
        _dataflow_times_mul_odata_reg_10 <= _dataflow_times_mul_odata_10;
      end 
      if(_dataflow_times_ready_10 || !_dataflow_times_valid_10) begin
        _dataflow_times_mul_valid_reg_10 <= _dataflow_times_mul_ovalid_10;
      end 
      if(_dataflow_times_ready_11 || !_dataflow_times_valid_11) begin
        _dataflow_times_mul_odata_reg_11 <= _dataflow_times_mul_odata_11;
      end 
      if(_dataflow_times_ready_11 || !_dataflow_times_valid_11) begin
        _dataflow_times_mul_valid_reg_11 <= _dataflow_times_mul_ovalid_11;
      end 
      if(_dataflow_times_ready_12 || !_dataflow_times_valid_12) begin
        _dataflow_times_mul_odata_reg_12 <= _dataflow_times_mul_odata_12;
      end 
      if(_dataflow_times_ready_12 || !_dataflow_times_valid_12) begin
        _dataflow_times_mul_valid_reg_12 <= _dataflow_times_mul_ovalid_12;
      end 
      if(_dataflow_times_ready_13 || !_dataflow_times_valid_13) begin
        _dataflow_times_mul_odata_reg_13 <= _dataflow_times_mul_odata_13;
      end 
      if(_dataflow_times_ready_13 || !_dataflow_times_valid_13) begin
        _dataflow_times_mul_valid_reg_13 <= _dataflow_times_mul_ovalid_13;
      end 
      if((_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow_plus_ready_6 && _dataflow_plus_valid_6) begin
        _dataflow__delay_data_18 <= _dataflow_plus_data_6;
      end 
      if(_dataflow__delay_valid_18 && _dataflow__delay_ready_18) begin
        _dataflow__delay_valid_18 <= 0;
      end 
      if((_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow_plus_ready_6) begin
        _dataflow__delay_valid_18 <= _dataflow_plus_valid_6;
      end 
      if((_dataflow__delay_ready_26 || !_dataflow__delay_valid_26) && _dataflow_plus_ready_7 && _dataflow_plus_valid_7) begin
        _dataflow__delay_data_26 <= _dataflow_plus_data_7;
      end 
      if(_dataflow__delay_valid_26 && _dataflow__delay_ready_26) begin
        _dataflow__delay_valid_26 <= 0;
      end 
      if((_dataflow__delay_ready_26 || !_dataflow__delay_valid_26) && _dataflow_plus_ready_7) begin
        _dataflow__delay_valid_26 <= _dataflow_plus_valid_7;
      end 
      if((_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_ready_18 && _dataflow__delay_valid_18) begin
        _dataflow__delay_data_19 <= _dataflow__delay_data_18;
      end 
      if(_dataflow__delay_valid_19 && _dataflow__delay_ready_19) begin
        _dataflow__delay_valid_19 <= 0;
      end 
      if((_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_ready_18) begin
        _dataflow__delay_valid_19 <= _dataflow__delay_valid_18;
      end 
      if((_dataflow__delay_ready_27 || !_dataflow__delay_valid_27) && _dataflow__delay_ready_26 && _dataflow__delay_valid_26) begin
        _dataflow__delay_data_27 <= _dataflow__delay_data_26;
      end 
      if(_dataflow__delay_valid_27 && _dataflow__delay_ready_27) begin
        _dataflow__delay_valid_27 <= 0;
      end 
      if((_dataflow__delay_ready_27 || !_dataflow__delay_valid_27) && _dataflow__delay_ready_26) begin
        _dataflow__delay_valid_27 <= _dataflow__delay_valid_26;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_ready_19 && _dataflow__delay_valid_19) begin
        _dataflow__delay_data_20 <= _dataflow__delay_data_19;
      end 
      if(_dataflow__delay_valid_20 && _dataflow__delay_ready_20) begin
        _dataflow__delay_valid_20 <= 0;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_ready_19) begin
        _dataflow__delay_valid_20 <= _dataflow__delay_valid_19;
      end 
      if((_dataflow__delay_ready_28 || !_dataflow__delay_valid_28) && _dataflow__delay_ready_27 && _dataflow__delay_valid_27) begin
        _dataflow__delay_data_28 <= _dataflow__delay_data_27;
      end 
      if(_dataflow__delay_valid_28 && _dataflow__delay_ready_28) begin
        _dataflow__delay_valid_28 <= 0;
      end 
      if((_dataflow__delay_ready_28 || !_dataflow__delay_valid_28) && _dataflow__delay_ready_27) begin
        _dataflow__delay_valid_28 <= _dataflow__delay_valid_27;
      end 
      if((_dataflow__delay_ready_21 || !_dataflow__delay_valid_21) && _dataflow__delay_ready_20 && _dataflow__delay_valid_20) begin
        _dataflow__delay_data_21 <= _dataflow__delay_data_20;
      end 
      if(_dataflow__delay_valid_21 && _dataflow__delay_ready_21) begin
        _dataflow__delay_valid_21 <= 0;
      end 
      if((_dataflow__delay_ready_21 || !_dataflow__delay_valid_21) && _dataflow__delay_ready_20) begin
        _dataflow__delay_valid_21 <= _dataflow__delay_valid_20;
      end 
      if((_dataflow__delay_ready_29 || !_dataflow__delay_valid_29) && _dataflow__delay_ready_28 && _dataflow__delay_valid_28) begin
        _dataflow__delay_data_29 <= _dataflow__delay_data_28;
      end 
      if(_dataflow__delay_valid_29 && _dataflow__delay_ready_29) begin
        _dataflow__delay_valid_29 <= 0;
      end 
      if((_dataflow__delay_ready_29 || !_dataflow__delay_valid_29) && _dataflow__delay_ready_28) begin
        _dataflow__delay_valid_29 <= _dataflow__delay_valid_28;
      end 
      if((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && _dataflow__delay_ready_21 && _dataflow__delay_valid_21) begin
        _dataflow__delay_data_22 <= _dataflow__delay_data_21;
      end 
      if(_dataflow__delay_valid_22 && _dataflow__delay_ready_22) begin
        _dataflow__delay_valid_22 <= 0;
      end 
      if((_dataflow__delay_ready_22 || !_dataflow__delay_valid_22) && _dataflow__delay_ready_21) begin
        _dataflow__delay_valid_22 <= _dataflow__delay_valid_21;
      end 
      if((_dataflow__delay_ready_30 || !_dataflow__delay_valid_30) && _dataflow__delay_ready_29 && _dataflow__delay_valid_29) begin
        _dataflow__delay_data_30 <= _dataflow__delay_data_29;
      end 
      if(_dataflow__delay_valid_30 && _dataflow__delay_ready_30) begin
        _dataflow__delay_valid_30 <= 0;
      end 
      if((_dataflow__delay_ready_30 || !_dataflow__delay_valid_30) && _dataflow__delay_ready_29) begin
        _dataflow__delay_valid_30 <= _dataflow__delay_valid_29;
      end 
      if((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && _dataflow__delay_ready_22 && _dataflow__delay_valid_22) begin
        _dataflow__delay_data_23 <= _dataflow__delay_data_22;
      end 
      if(_dataflow__delay_valid_23 && _dataflow__delay_ready_23) begin
        _dataflow__delay_valid_23 <= 0;
      end 
      if((_dataflow__delay_ready_23 || !_dataflow__delay_valid_23) && _dataflow__delay_ready_22) begin
        _dataflow__delay_valid_23 <= _dataflow__delay_valid_22;
      end 
      if((_dataflow__delay_ready_31 || !_dataflow__delay_valid_31) && _dataflow__delay_ready_30 && _dataflow__delay_valid_30) begin
        _dataflow__delay_data_31 <= _dataflow__delay_data_30;
      end 
      if(_dataflow__delay_valid_31 && _dataflow__delay_ready_31) begin
        _dataflow__delay_valid_31 <= 0;
      end 
      if((_dataflow__delay_ready_31 || !_dataflow__delay_valid_31) && _dataflow__delay_ready_30) begin
        _dataflow__delay_valid_31 <= _dataflow__delay_valid_30;
      end 
      if((_dataflow__delay_ready_24 || !_dataflow__delay_valid_24) && _dataflow__delay_ready_23 && _dataflow__delay_valid_23) begin
        _dataflow__delay_data_24 <= _dataflow__delay_data_23;
      end 
      if(_dataflow__delay_valid_24 && _dataflow__delay_ready_24) begin
        _dataflow__delay_valid_24 <= 0;
      end 
      if((_dataflow__delay_ready_24 || !_dataflow__delay_valid_24) && _dataflow__delay_ready_23) begin
        _dataflow__delay_valid_24 <= _dataflow__delay_valid_23;
      end 
      if((_dataflow__delay_ready_32 || !_dataflow__delay_valid_32) && _dataflow__delay_ready_31 && _dataflow__delay_valid_31) begin
        _dataflow__delay_data_32 <= _dataflow__delay_data_31;
      end 
      if(_dataflow__delay_valid_32 && _dataflow__delay_ready_32) begin
        _dataflow__delay_valid_32 <= 0;
      end 
      if((_dataflow__delay_ready_32 || !_dataflow__delay_valid_32) && _dataflow__delay_ready_31) begin
        _dataflow__delay_valid_32 <= _dataflow__delay_valid_31;
      end 
      if((_dataflow_minus_ready_14 || !_dataflow_minus_valid_14) && (_dataflow_times_ready_10 && _dataflow_times_ready_11) && (_dataflow_times_valid_10 && _dataflow_times_valid_11)) begin
        _dataflow_minus_data_14 <= _dataflow_times_data_10 - _dataflow_times_data_11;
      end 
      if(_dataflow_minus_valid_14 && _dataflow_minus_ready_14) begin
        _dataflow_minus_valid_14 <= 0;
      end 
      if((_dataflow_minus_ready_14 || !_dataflow_minus_valid_14) && (_dataflow_times_ready_10 && _dataflow_times_ready_11)) begin
        _dataflow_minus_valid_14 <= _dataflow_times_valid_10 && _dataflow_times_valid_11;
      end 
      if((_dataflow_plus_ready_15 || !_dataflow_plus_valid_15) && (_dataflow_times_ready_12 && _dataflow_times_ready_13) && (_dataflow_times_valid_12 && _dataflow_times_valid_13)) begin
        _dataflow_plus_data_15 <= _dataflow_times_data_12 + _dataflow_times_data_13;
      end 
      if(_dataflow_plus_valid_15 && _dataflow_plus_ready_15) begin
        _dataflow_plus_valid_15 <= 0;
      end 
      if((_dataflow_plus_ready_15 || !_dataflow_plus_valid_15) && (_dataflow_times_ready_12 && _dataflow_times_ready_13)) begin
        _dataflow_plus_valid_15 <= _dataflow_times_valid_12 && _dataflow_times_valid_13;
      end 
      if((_dataflow__delay_ready_25 || !_dataflow__delay_valid_25) && _dataflow__delay_ready_24 && _dataflow__delay_valid_24) begin
        _dataflow__delay_data_25 <= _dataflow__delay_data_24;
      end 
      if(_dataflow__delay_valid_25 && _dataflow__delay_ready_25) begin
        _dataflow__delay_valid_25 <= 0;
      end 
      if((_dataflow__delay_ready_25 || !_dataflow__delay_valid_25) && _dataflow__delay_ready_24) begin
        _dataflow__delay_valid_25 <= _dataflow__delay_valid_24;
      end 
      if((_dataflow__delay_ready_33 || !_dataflow__delay_valid_33) && _dataflow__delay_ready_32 && _dataflow__delay_valid_32) begin
        _dataflow__delay_data_33 <= _dataflow__delay_data_32;
      end 
      if(_dataflow__delay_valid_33 && _dataflow__delay_ready_33) begin
        _dataflow__delay_valid_33 <= 0;
      end 
      if((_dataflow__delay_ready_33 || !_dataflow__delay_valid_33) && _dataflow__delay_ready_32) begin
        _dataflow__delay_valid_33 <= _dataflow__delay_valid_32;
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
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
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
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
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
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
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
  wire signed [64-1:0] _mul;
  reg signed [64-1:0] _pipe_mul0;
  reg signed [64-1:0] _pipe_mul1;
  reg signed [64-1:0] _pipe_mul2;
  reg signed [64-1:0] _pipe_mul3;
  reg signed [64-1:0] _pipe_mul4;
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
    test_module = dataflow_radix2.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
