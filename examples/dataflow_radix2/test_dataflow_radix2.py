from __future__ import absolute_import
from __future__ import print_function
import dataflow_radix2

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] din0re;
  reg [32-1:0] din0im;
  reg [32-1:0] din1re;
  reg [32-1:0] din1im;
  reg [32-1:0] cnstre;
  reg [32-1:0] cnstim;
  wire [32-1:0] dout1re;
  wire [32-1:0] dout1im;
  wire [32-1:0] dout0re;
  wire [32-1:0] dout0im;

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
  input [32-1:0] din0re,
  input [32-1:0] din0im,
  input [32-1:0] din1re,
  input [32-1:0] din1im,
  input [32-1:0] cnstre,
  input [32-1:0] cnstim,
  output [32-1:0] dout1re,
  output [32-1:0] dout1im,
  output [32-1:0] dout0re,
  output [32-1:0] dout0im
);

  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign _tmp_ready_0 = (_tmp_ready_10 || !_tmp_valid_10) && _tmp_valid_0;
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign _tmp_ready_1 = (_tmp_ready_11 || !_tmp_valid_11) && _tmp_valid_1;
  reg [32-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign _tmp_ready_2 = (_tmp_ready_6 || !_tmp_valid_6) && (_tmp_valid_2 && _tmp_valid_4) && ((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_valid_2 && _tmp_valid_5));
  reg [32-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_3 = (_tmp_ready_7 || !_tmp_valid_7) && (_tmp_valid_3 && _tmp_valid_5) && ((_tmp_ready_9 || !_tmp_valid_9) && (_tmp_valid_3 && _tmp_valid_4));
  reg [32-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_4 = (_tmp_ready_6 || !_tmp_valid_6) && (_tmp_valid_2 && _tmp_valid_4) && ((_tmp_ready_9 || !_tmp_valid_9) && (_tmp_valid_3 && _tmp_valid_4));
  reg [32-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (_tmp_ready_7 || !_tmp_valid_7) && (_tmp_valid_3 && _tmp_valid_5) && ((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_valid_2 && _tmp_valid_5));
  wire [32-1:0] _tmp_data_6;
  wire _tmp_valid_6;
  wire _tmp_ready_6;
  wire [32-1:0] _tmp_ldata_6;
  wire [32-1:0] _tmp_rdata_6;
  assign _tmp_ldata_6 = _tmp_data_2;
  assign _tmp_rdata_6 = _tmp_data_4;
  wire [32-1:0] _tmp_abs_ldata_6;
  wire [32-1:0] _tmp_abs_rdata_6;
  assign _tmp_abs_ldata_6 = _tmp_ldata_6;
  assign _tmp_abs_rdata_6 = _tmp_rdata_6;
  wire _tmp_osign_6;
  wire [64-1:0] _tmp_abs_odata_6;
  wire [64-1:0] _tmp_odata_6;
  assign _tmp_odata_6 = _tmp_abs_odata_6;
  assign _tmp_data_6 = _tmp_odata_6;
  wire _tmp_enable_6;
  wire _tmp_update_6;
  assign _tmp_enable_6 = (_tmp_ready_6 || !_tmp_valid_6) && (_tmp_ready_2 && _tmp_ready_4) && (_tmp_valid_2 && _tmp_valid_4);
  assign _tmp_update_6 = _tmp_ready_6 || !_tmp_valid_6;

  multiplier
  #(
    .datawidth(32),
    .depth(6)
  )
  mul6
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_6),
    .enable(_tmp_enable_6),
    .valid(_tmp_valid_6),
    .a(_tmp_abs_ldata_6),
    .b(_tmp_abs_rdata_6),
    .c(_tmp_abs_odata_6)
  );

  reg _tmp_sign0_6;
  reg _tmp_sign1_6;
  reg _tmp_sign2_6;
  reg _tmp_sign3_6;
  reg _tmp_sign4_6;
  reg _tmp_sign5_6;
  assign _tmp_osign_6 = _tmp_sign5_6;
  assign _tmp_ready_6 = (_tmp_ready_22 || !_tmp_valid_22) && (_tmp_valid_6 && _tmp_valid_7);
  wire [32-1:0] _tmp_data_7;
  wire _tmp_valid_7;
  wire _tmp_ready_7;
  wire [32-1:0] _tmp_ldata_7;
  wire [32-1:0] _tmp_rdata_7;
  assign _tmp_ldata_7 = _tmp_data_3;
  assign _tmp_rdata_7 = _tmp_data_5;
  wire [32-1:0] _tmp_abs_ldata_7;
  wire [32-1:0] _tmp_abs_rdata_7;
  assign _tmp_abs_ldata_7 = _tmp_ldata_7;
  assign _tmp_abs_rdata_7 = _tmp_rdata_7;
  wire _tmp_osign_7;
  wire [64-1:0] _tmp_abs_odata_7;
  wire [64-1:0] _tmp_odata_7;
  assign _tmp_odata_7 = _tmp_abs_odata_7;
  assign _tmp_data_7 = _tmp_odata_7;
  wire _tmp_enable_7;
  wire _tmp_update_7;
  assign _tmp_enable_7 = (_tmp_ready_7 || !_tmp_valid_7) && (_tmp_ready_3 && _tmp_ready_5) && (_tmp_valid_3 && _tmp_valid_5);
  assign _tmp_update_7 = _tmp_ready_7 || !_tmp_valid_7;

  multiplier
  #(
    .datawidth(32),
    .depth(6)
  )
  mul7
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_7),
    .enable(_tmp_enable_7),
    .valid(_tmp_valid_7),
    .a(_tmp_abs_ldata_7),
    .b(_tmp_abs_rdata_7),
    .c(_tmp_abs_odata_7)
  );

  reg _tmp_sign0_7;
  reg _tmp_sign1_7;
  reg _tmp_sign2_7;
  reg _tmp_sign3_7;
  reg _tmp_sign4_7;
  reg _tmp_sign5_7;
  assign _tmp_osign_7 = _tmp_sign5_7;
  assign _tmp_ready_7 = (_tmp_ready_22 || !_tmp_valid_22) && (_tmp_valid_6 && _tmp_valid_7);
  wire [32-1:0] _tmp_data_8;
  wire _tmp_valid_8;
  wire _tmp_ready_8;
  wire [32-1:0] _tmp_ldata_8;
  wire [32-1:0] _tmp_rdata_8;
  assign _tmp_ldata_8 = _tmp_data_2;
  assign _tmp_rdata_8 = _tmp_data_5;
  wire [32-1:0] _tmp_abs_ldata_8;
  wire [32-1:0] _tmp_abs_rdata_8;
  assign _tmp_abs_ldata_8 = _tmp_ldata_8;
  assign _tmp_abs_rdata_8 = _tmp_rdata_8;
  wire _tmp_osign_8;
  wire [64-1:0] _tmp_abs_odata_8;
  wire [64-1:0] _tmp_odata_8;
  assign _tmp_odata_8 = _tmp_abs_odata_8;
  assign _tmp_data_8 = _tmp_odata_8;
  wire _tmp_enable_8;
  wire _tmp_update_8;
  assign _tmp_enable_8 = (_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_2 && _tmp_ready_5) && (_tmp_valid_2 && _tmp_valid_5);
  assign _tmp_update_8 = _tmp_ready_8 || !_tmp_valid_8;

  multiplier
  #(
    .datawidth(32),
    .depth(6)
  )
  mul8
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_8),
    .enable(_tmp_enable_8),
    .valid(_tmp_valid_8),
    .a(_tmp_abs_ldata_8),
    .b(_tmp_abs_rdata_8),
    .c(_tmp_abs_odata_8)
  );

  reg _tmp_sign0_8;
  reg _tmp_sign1_8;
  reg _tmp_sign2_8;
  reg _tmp_sign3_8;
  reg _tmp_sign4_8;
  reg _tmp_sign5_8;
  assign _tmp_osign_8 = _tmp_sign5_8;
  assign _tmp_ready_8 = (_tmp_ready_23 || !_tmp_valid_23) && (_tmp_valid_8 && _tmp_valid_9);
  wire [32-1:0] _tmp_data_9;
  wire _tmp_valid_9;
  wire _tmp_ready_9;
  wire [32-1:0] _tmp_ldata_9;
  wire [32-1:0] _tmp_rdata_9;
  assign _tmp_ldata_9 = _tmp_data_3;
  assign _tmp_rdata_9 = _tmp_data_4;
  wire [32-1:0] _tmp_abs_ldata_9;
  wire [32-1:0] _tmp_abs_rdata_9;
  assign _tmp_abs_ldata_9 = _tmp_ldata_9;
  assign _tmp_abs_rdata_9 = _tmp_rdata_9;
  wire _tmp_osign_9;
  wire [64-1:0] _tmp_abs_odata_9;
  wire [64-1:0] _tmp_odata_9;
  assign _tmp_odata_9 = _tmp_abs_odata_9;
  assign _tmp_data_9 = _tmp_odata_9;
  wire _tmp_enable_9;
  wire _tmp_update_9;
  assign _tmp_enable_9 = (_tmp_ready_9 || !_tmp_valid_9) && (_tmp_ready_3 && _tmp_ready_4) && (_tmp_valid_3 && _tmp_valid_4);
  assign _tmp_update_9 = _tmp_ready_9 || !_tmp_valid_9;

  multiplier
  #(
    .datawidth(32),
    .depth(6)
  )
  mul9
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_9),
    .enable(_tmp_enable_9),
    .valid(_tmp_valid_9),
    .a(_tmp_abs_ldata_9),
    .b(_tmp_abs_rdata_9),
    .c(_tmp_abs_odata_9)
  );

  reg _tmp_sign0_9;
  reg _tmp_sign1_9;
  reg _tmp_sign2_9;
  reg _tmp_sign3_9;
  reg _tmp_sign4_9;
  reg _tmp_sign5_9;
  assign _tmp_osign_9 = _tmp_sign5_9;
  assign _tmp_ready_9 = (_tmp_ready_23 || !_tmp_valid_23) && (_tmp_valid_8 && _tmp_valid_9);
  reg [32-1:0] _tmp_data_10;
  reg _tmp_valid_10;
  wire _tmp_ready_10;
  assign _tmp_ready_10 = (_tmp_ready_12 || !_tmp_valid_12) && _tmp_valid_10;
  reg [32-1:0] _tmp_data_11;
  reg _tmp_valid_11;
  wire _tmp_ready_11;
  assign _tmp_ready_11 = (_tmp_ready_13 || !_tmp_valid_13) && _tmp_valid_11;
  reg [32-1:0] _tmp_data_12;
  reg _tmp_valid_12;
  wire _tmp_ready_12;
  assign _tmp_ready_12 = (_tmp_ready_14 || !_tmp_valid_14) && _tmp_valid_12;
  reg [32-1:0] _tmp_data_13;
  reg _tmp_valid_13;
  wire _tmp_ready_13;
  assign _tmp_ready_13 = (_tmp_ready_15 || !_tmp_valid_15) && _tmp_valid_13;
  reg [32-1:0] _tmp_data_14;
  reg _tmp_valid_14;
  wire _tmp_ready_14;
  assign _tmp_ready_14 = (_tmp_ready_16 || !_tmp_valid_16) && _tmp_valid_14;
  reg [32-1:0] _tmp_data_15;
  reg _tmp_valid_15;
  wire _tmp_ready_15;
  assign _tmp_ready_15 = (_tmp_ready_17 || !_tmp_valid_17) && _tmp_valid_15;
  reg [32-1:0] _tmp_data_16;
  reg _tmp_valid_16;
  wire _tmp_ready_16;
  assign _tmp_ready_16 = (_tmp_ready_18 || !_tmp_valid_18) && _tmp_valid_16;
  reg [32-1:0] _tmp_data_17;
  reg _tmp_valid_17;
  wire _tmp_ready_17;
  assign _tmp_ready_17 = (_tmp_ready_19 || !_tmp_valid_19) && _tmp_valid_17;
  reg [32-1:0] _tmp_data_18;
  reg _tmp_valid_18;
  wire _tmp_ready_18;
  assign _tmp_ready_18 = (_tmp_ready_20 || !_tmp_valid_20) && _tmp_valid_18;
  reg [32-1:0] _tmp_data_19;
  reg _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_ready_21 || !_tmp_valid_21) && _tmp_valid_19;
  reg [32-1:0] _tmp_data_20;
  reg _tmp_valid_20;
  wire _tmp_ready_20;
  assign _tmp_ready_20 = (_tmp_ready_24 || !_tmp_valid_24) && _tmp_valid_20;
  reg [32-1:0] _tmp_data_21;
  reg _tmp_valid_21;
  wire _tmp_ready_21;
  assign _tmp_ready_21 = (_tmp_ready_25 || !_tmp_valid_25) && _tmp_valid_21;
  reg [32-1:0] _tmp_data_22;
  reg _tmp_valid_22;
  wire _tmp_ready_22;
  reg [32-1:0] _tmp_data_23;
  reg _tmp_valid_23;
  wire _tmp_ready_23;
  reg [32-1:0] _tmp_data_24;
  reg _tmp_valid_24;
  wire _tmp_ready_24;
  reg [32-1:0] _tmp_data_25;
  reg _tmp_valid_25;
  wire _tmp_ready_25;
  assign dout1re = _tmp_data_22;
  assign _tmp_ready_22 = 1;
  assign dout1im = _tmp_data_23;
  assign _tmp_ready_23 = 1;
  assign dout0re = _tmp_data_24;
  assign _tmp_ready_24 = 1;
  assign dout0im = _tmp_data_25;
  assign _tmp_ready_25 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_valid_3 <= 0;
      _tmp_data_4 <= 0;
      _tmp_valid_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_valid_5 <= 0;
      _tmp_sign0_6 <= 0;
      _tmp_sign1_6 <= 0;
      _tmp_sign2_6 <= 0;
      _tmp_sign3_6 <= 0;
      _tmp_sign4_6 <= 0;
      _tmp_sign5_6 <= 0;
      _tmp_sign0_7 <= 0;
      _tmp_sign1_7 <= 0;
      _tmp_sign2_7 <= 0;
      _tmp_sign3_7 <= 0;
      _tmp_sign4_7 <= 0;
      _tmp_sign5_7 <= 0;
      _tmp_sign0_8 <= 0;
      _tmp_sign1_8 <= 0;
      _tmp_sign2_8 <= 0;
      _tmp_sign3_8 <= 0;
      _tmp_sign4_8 <= 0;
      _tmp_sign5_8 <= 0;
      _tmp_sign0_9 <= 0;
      _tmp_sign1_9 <= 0;
      _tmp_sign2_9 <= 0;
      _tmp_sign3_9 <= 0;
      _tmp_sign4_9 <= 0;
      _tmp_sign5_9 <= 0;
      _tmp_data_10 <= 0;
      _tmp_valid_10 <= 0;
      _tmp_data_11 <= 0;
      _tmp_valid_11 <= 0;
      _tmp_data_12 <= 0;
      _tmp_valid_12 <= 0;
      _tmp_data_13 <= 0;
      _tmp_valid_13 <= 0;
      _tmp_data_14 <= 0;
      _tmp_valid_14 <= 0;
      _tmp_data_15 <= 0;
      _tmp_valid_15 <= 0;
      _tmp_data_16 <= 0;
      _tmp_valid_16 <= 0;
      _tmp_data_17 <= 0;
      _tmp_valid_17 <= 0;
      _tmp_data_18 <= 0;
      _tmp_valid_18 <= 0;
      _tmp_data_19 <= 0;
      _tmp_valid_19 <= 0;
      _tmp_data_20 <= 0;
      _tmp_valid_20 <= 0;
      _tmp_data_21 <= 0;
      _tmp_valid_21 <= 0;
      _tmp_data_22 <= 0;
      _tmp_valid_22 <= 0;
      _tmp_data_23 <= 0;
      _tmp_valid_23 <= 0;
      _tmp_data_24 <= 0;
      _tmp_valid_24 <= 0;
      _tmp_data_25 <= 0;
      _tmp_valid_25 <= 0;
    end else begin
      if((_tmp_ready_0 || !_tmp_valid_0) && 1 && 1) begin
        _tmp_data_0 <= din0re + din1re;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && 1) begin
        _tmp_valid_0 <= 1;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1 && 1) begin
        _tmp_data_1 <= din0im + din1im;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1) begin
        _tmp_valid_1 <= 1;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && 1 && 1) begin
        _tmp_data_2 <= din0re - din1re;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && 1) begin
        _tmp_valid_2 <= 1;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && 1 && 1) begin
        _tmp_data_3 <= din0im - din1im;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && 1) begin
        _tmp_valid_3 <= 1;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && 1 && 1) begin
        _tmp_data_4 <= cnstre;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && 1) begin
        _tmp_valid_4 <= 1;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && 1 && 1) begin
        _tmp_data_5 <= cnstim;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && 1) begin
        _tmp_valid_5 <= 1;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_sign0_6 <= (_tmp_ldata_6[31] == 0) && (_tmp_rdata_6[31] == 0) || (_tmp_ldata_6[31] == 1) && (_tmp_rdata_6[31] == 1);
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_sign1_6 <= _tmp_sign0_6;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_sign2_6 <= _tmp_sign1_6;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_sign3_6 <= _tmp_sign2_6;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_sign4_6 <= _tmp_sign3_6;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_sign5_6 <= _tmp_sign4_6;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_sign0_7 <= (_tmp_ldata_7[31] == 0) && (_tmp_rdata_7[31] == 0) || (_tmp_ldata_7[31] == 1) && (_tmp_rdata_7[31] == 1);
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_sign1_7 <= _tmp_sign0_7;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_sign2_7 <= _tmp_sign1_7;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_sign3_7 <= _tmp_sign2_7;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_sign4_7 <= _tmp_sign3_7;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_sign5_7 <= _tmp_sign4_7;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_sign0_8 <= (_tmp_ldata_8[31] == 0) && (_tmp_rdata_8[31] == 0) || (_tmp_ldata_8[31] == 1) && (_tmp_rdata_8[31] == 1);
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_sign1_8 <= _tmp_sign0_8;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_sign2_8 <= _tmp_sign1_8;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_sign3_8 <= _tmp_sign2_8;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_sign4_8 <= _tmp_sign3_8;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_sign5_8 <= _tmp_sign4_8;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_sign0_9 <= (_tmp_ldata_9[31] == 0) && (_tmp_rdata_9[31] == 0) || (_tmp_ldata_9[31] == 1) && (_tmp_rdata_9[31] == 1);
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_sign1_9 <= _tmp_sign0_9;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_sign2_9 <= _tmp_sign1_9;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_sign3_9 <= _tmp_sign2_9;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_sign4_9 <= _tmp_sign3_9;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_sign5_9 <= _tmp_sign4_9;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_10 <= _tmp_data_0;
      end 
      if(_tmp_valid_10 && _tmp_ready_10) begin
        _tmp_valid_10 <= 0;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && _tmp_ready_0) begin
        _tmp_valid_10 <= _tmp_valid_0;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && _tmp_ready_1 && _tmp_valid_1) begin
        _tmp_data_11 <= _tmp_data_1;
      end 
      if(_tmp_valid_11 && _tmp_ready_11) begin
        _tmp_valid_11 <= 0;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && _tmp_ready_1) begin
        _tmp_valid_11 <= _tmp_valid_1;
      end 
      if((_tmp_ready_12 || !_tmp_valid_12) && _tmp_ready_10 && _tmp_valid_10) begin
        _tmp_data_12 <= _tmp_data_10;
      end 
      if(_tmp_valid_12 && _tmp_ready_12) begin
        _tmp_valid_12 <= 0;
      end 
      if((_tmp_ready_12 || !_tmp_valid_12) && _tmp_ready_10) begin
        _tmp_valid_12 <= _tmp_valid_10;
      end 
      if((_tmp_ready_13 || !_tmp_valid_13) && _tmp_ready_11 && _tmp_valid_11) begin
        _tmp_data_13 <= _tmp_data_11;
      end 
      if(_tmp_valid_13 && _tmp_ready_13) begin
        _tmp_valid_13 <= 0;
      end 
      if((_tmp_ready_13 || !_tmp_valid_13) && _tmp_ready_11) begin
        _tmp_valid_13 <= _tmp_valid_11;
      end 
      if((_tmp_ready_14 || !_tmp_valid_14) && _tmp_ready_12 && _tmp_valid_12) begin
        _tmp_data_14 <= _tmp_data_12;
      end 
      if(_tmp_valid_14 && _tmp_ready_14) begin
        _tmp_valid_14 <= 0;
      end 
      if((_tmp_ready_14 || !_tmp_valid_14) && _tmp_ready_12) begin
        _tmp_valid_14 <= _tmp_valid_12;
      end 
      if((_tmp_ready_15 || !_tmp_valid_15) && _tmp_ready_13 && _tmp_valid_13) begin
        _tmp_data_15 <= _tmp_data_13;
      end 
      if(_tmp_valid_15 && _tmp_ready_15) begin
        _tmp_valid_15 <= 0;
      end 
      if((_tmp_ready_15 || !_tmp_valid_15) && _tmp_ready_13) begin
        _tmp_valid_15 <= _tmp_valid_13;
      end 
      if((_tmp_ready_16 || !_tmp_valid_16) && _tmp_ready_14 && _tmp_valid_14) begin
        _tmp_data_16 <= _tmp_data_14;
      end 
      if(_tmp_valid_16 && _tmp_ready_16) begin
        _tmp_valid_16 <= 0;
      end 
      if((_tmp_ready_16 || !_tmp_valid_16) && _tmp_ready_14) begin
        _tmp_valid_16 <= _tmp_valid_14;
      end 
      if((_tmp_ready_17 || !_tmp_valid_17) && _tmp_ready_15 && _tmp_valid_15) begin
        _tmp_data_17 <= _tmp_data_15;
      end 
      if(_tmp_valid_17 && _tmp_ready_17) begin
        _tmp_valid_17 <= 0;
      end 
      if((_tmp_ready_17 || !_tmp_valid_17) && _tmp_ready_15) begin
        _tmp_valid_17 <= _tmp_valid_15;
      end 
      if((_tmp_ready_18 || !_tmp_valid_18) && _tmp_ready_16 && _tmp_valid_16) begin
        _tmp_data_18 <= _tmp_data_16;
      end 
      if(_tmp_valid_18 && _tmp_ready_18) begin
        _tmp_valid_18 <= 0;
      end 
      if((_tmp_ready_18 || !_tmp_valid_18) && _tmp_ready_16) begin
        _tmp_valid_18 <= _tmp_valid_16;
      end 
      if((_tmp_ready_19 || !_tmp_valid_19) && _tmp_ready_17 && _tmp_valid_17) begin
        _tmp_data_19 <= _tmp_data_17;
      end 
      if(_tmp_valid_19 && _tmp_ready_19) begin
        _tmp_valid_19 <= 0;
      end 
      if((_tmp_ready_19 || !_tmp_valid_19) && _tmp_ready_17) begin
        _tmp_valid_19 <= _tmp_valid_17;
      end 
      if((_tmp_ready_20 || !_tmp_valid_20) && _tmp_ready_18 && _tmp_valid_18) begin
        _tmp_data_20 <= _tmp_data_18;
      end 
      if(_tmp_valid_20 && _tmp_ready_20) begin
        _tmp_valid_20 <= 0;
      end 
      if((_tmp_ready_20 || !_tmp_valid_20) && _tmp_ready_18) begin
        _tmp_valid_20 <= _tmp_valid_18;
      end 
      if((_tmp_ready_21 || !_tmp_valid_21) && _tmp_ready_19 && _tmp_valid_19) begin
        _tmp_data_21 <= _tmp_data_19;
      end 
      if(_tmp_valid_21 && _tmp_ready_21) begin
        _tmp_valid_21 <= 0;
      end 
      if((_tmp_ready_21 || !_tmp_valid_21) && _tmp_ready_19) begin
        _tmp_valid_21 <= _tmp_valid_19;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && (_tmp_ready_6 && _tmp_ready_7) && (_tmp_valid_6 && _tmp_valid_7)) begin
        _tmp_data_22 <= _tmp_data_6 - _tmp_data_7;
      end 
      if(_tmp_valid_22 && _tmp_ready_22) begin
        _tmp_valid_22 <= 0;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && (_tmp_ready_6 && _tmp_ready_7)) begin
        _tmp_valid_22 <= _tmp_valid_6 && _tmp_valid_7;
      end 
      if((_tmp_ready_23 || !_tmp_valid_23) && (_tmp_ready_8 && _tmp_ready_9) && (_tmp_valid_8 && _tmp_valid_9)) begin
        _tmp_data_23 <= _tmp_data_8 + _tmp_data_9;
      end 
      if(_tmp_valid_23 && _tmp_ready_23) begin
        _tmp_valid_23 <= 0;
      end 
      if((_tmp_ready_23 || !_tmp_valid_23) && (_tmp_ready_8 && _tmp_ready_9)) begin
        _tmp_valid_23 <= _tmp_valid_8 && _tmp_valid_9;
      end 
      if((_tmp_ready_24 || !_tmp_valid_24) && _tmp_ready_20 && _tmp_valid_20) begin
        _tmp_data_24 <= _tmp_data_20;
      end 
      if(_tmp_valid_24 && _tmp_ready_24) begin
        _tmp_valid_24 <= 0;
      end 
      if((_tmp_ready_24 || !_tmp_valid_24) && _tmp_ready_20) begin
        _tmp_valid_24 <= _tmp_valid_20;
      end 
      if((_tmp_ready_25 || !_tmp_valid_25) && _tmp_ready_21 && _tmp_valid_21) begin
        _tmp_data_25 <= _tmp_data_21;
      end 
      if(_tmp_valid_25 && _tmp_ready_25) begin
        _tmp_valid_25 <= 0;
      end 
      if((_tmp_ready_25 || !_tmp_valid_25) && _tmp_ready_21) begin
        _tmp_valid_25 <= _tmp_valid_21;
      end 
    end
  end


endmodule



module multiplier #
(
  parameter datawidth = 32,
  parameter depth = 6
)
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [datawidth-1:0] a,
  input [datawidth-1:0] b,
  output [datawidth*2-1:0] c
);

  reg [depth-1:0] valid_reg;
  assign valid = valid_reg[depth - 1];
  integer i;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg <= 0;
    end else begin
      if(update) begin
        valid_reg[0] <= enable;
        for(i=1; i<depth; i=i+1) begin
          valid_reg[i] <= valid_reg[i - 1];
        end
      end 
    end
  end


  multiplier_core
  #(
    .datawidth(datawidth),
    .depth(depth)
  )
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core #
(
  parameter datawidth = 32,
  parameter depth = 6
)
(
  input CLK,
  input update,
  input [datawidth-1:0] a,
  input [datawidth-1:0] b,
  output [datawidth*2-1:0] c
);

  wire [datawidth*2-1:0] rslt;
  reg [datawidth*2-1:0] mem [0:depth-1];
  assign rslt = a * b;
  assign c = mem[depth - 1];
  integer i;

  always @(posedge CLK) begin
    if(update) begin
      mem[0] <= rslt;
      for(i=1; i<depth; i=i+1) begin
        mem[i] <= mem[i - 1];
      end
    end 
  end


endmodule
"""

def test():
    test_module = dataflow_radix2.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
