from __future__ import absolute_import
from __future__ import print_function
import dataflow_sort

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] din0;
  reg [32-1:0] din1;
  reg [32-1:0] din2;
  reg [32-1:0] din3;
  wire [32-1:0] dout0;
  wire [32-1:0] dout1;
  wire [32-1:0] dout3;
  wire [32-1:0] dout2;

  sort
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .din0(din0),
    .din1(din1),
    .din2(din2),
    .din3(din3),
    .dout0(dout0),
    .dout1(dout1),
    .dout3(dout3),
    .dout2(dout2)
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
    din0 = 0;
    din1 = 0;
    din2 = 0;
    din3 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #100000;
    $finish;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
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

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
    end else begin
      case(fsm)
        fsm_init: begin
          if(reset_done) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          din0 <= 100;
          din1 <= 99;
          din2 <= 98;
          din3 <= 97;
          fsm <= fsm_2;
        end
        fsm_2: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_3;
        end
        fsm_3: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_4;
        end
        fsm_4: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_5;
        end
        fsm_5: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_6;
        end
        fsm_6: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_7;
        end
        fsm_7: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_8;
        end
        fsm_8: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_9;
        end
        fsm_9: begin
          $display("%s = %d", "dout0", dout0);
          $display("%s = %d", "dout1", dout1);
          $display("%s = %d", "dout2", dout2);
          $display("%s = %d", "dout3", dout3);
          $display("----");
          fsm <= fsm_10;
        end
        fsm_10: begin
          $finish;
        end
      endcase
    end
  end


endmodule



module sort
(
  input CLK,
  input RST,
  input [32-1:0] din0,
  input [32-1:0] din1,
  input [32-1:0] din2,
  input [32-1:0] din3,
  output [32-1:0] dout0,
  output [32-1:0] dout1,
  output [32-1:0] dout3,
  output [32-1:0] dout2
);

  reg [1-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign _tmp_ready_0 = (_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_0 && _tmp_valid_2 && _tmp_valid_1) && ((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_valid_0 && _tmp_valid_1 && _tmp_valid_2));
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign _tmp_ready_1 = (_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_0 && _tmp_valid_2 && _tmp_valid_1) && ((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_valid_0 && _tmp_valid_1 && _tmp_valid_2));
  reg [32-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign _tmp_ready_2 = (_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_0 && _tmp_valid_2 && _tmp_valid_1) && ((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_valid_0 && _tmp_valid_1 && _tmp_valid_2));
  reg [32-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_3 = (_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_3;
  reg [32-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_4 = (_tmp_ready_8 || !_tmp_valid_8) && _tmp_valid_4;
  reg [32-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (_tmp_ready_13 || !_tmp_valid_13) && _tmp_valid_5;
  reg [32-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  assign _tmp_ready_6 = (_tmp_ready_9 || !_tmp_valid_9) && (_tmp_valid_6 && _tmp_valid_7) && ((_tmp_ready_11 || !_tmp_valid_11) && _tmp_valid_6);
  reg [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign _tmp_ready_7 = (_tmp_ready_9 || !_tmp_valid_9) && (_tmp_valid_6 && _tmp_valid_7) && ((_tmp_ready_10 || !_tmp_valid_10) && _tmp_valid_7);
  reg [32-1:0] _tmp_data_8;
  reg _tmp_valid_8;
  wire _tmp_ready_8;
  assign _tmp_ready_8 = (_tmp_ready_12 || !_tmp_valid_12) && _tmp_valid_8;
  reg [1-1:0] _tmp_data_9;
  reg _tmp_valid_9;
  wire _tmp_ready_9;
  assign _tmp_ready_9 = (_tmp_ready_14 || !_tmp_valid_14) && (_tmp_valid_9 && _tmp_valid_11 && _tmp_valid_10) && ((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_valid_9 && _tmp_valid_10 && _tmp_valid_11));
  reg [32-1:0] _tmp_data_10;
  reg _tmp_valid_10;
  wire _tmp_ready_10;
  assign _tmp_ready_10 = (_tmp_ready_14 || !_tmp_valid_14) && (_tmp_valid_9 && _tmp_valid_11 && _tmp_valid_10) && ((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_valid_9 && _tmp_valid_10 && _tmp_valid_11));
  reg [32-1:0] _tmp_data_11;
  reg _tmp_valid_11;
  wire _tmp_ready_11;
  assign _tmp_ready_11 = (_tmp_ready_14 || !_tmp_valid_14) && (_tmp_valid_9 && _tmp_valid_11 && _tmp_valid_10) && ((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_valid_9 && _tmp_valid_10 && _tmp_valid_11));
  reg [32-1:0] _tmp_data_12;
  reg _tmp_valid_12;
  wire _tmp_ready_12;
  assign _tmp_ready_12 = (_tmp_ready_16 || !_tmp_valid_16) && _tmp_valid_12;
  reg [32-1:0] _tmp_data_13;
  reg _tmp_valid_13;
  wire _tmp_ready_13;
  assign _tmp_ready_13 = (_tmp_ready_17 || !_tmp_valid_17) && _tmp_valid_13;
  reg [32-1:0] _tmp_data_14;
  reg _tmp_valid_14;
  wire _tmp_ready_14;
  assign _tmp_ready_14 = (_tmp_ready_19 || !_tmp_valid_19) && (_tmp_valid_17 && _tmp_valid_14) && ((_tmp_ready_22 || !_tmp_valid_22) && _tmp_valid_14);
  reg [32-1:0] _tmp_data_15;
  reg _tmp_valid_15;
  wire _tmp_ready_15;
  assign _tmp_ready_15 = (_tmp_ready_18 || !_tmp_valid_18) && (_tmp_valid_15 && _tmp_valid_16) && ((_tmp_ready_21 || !_tmp_valid_21) && _tmp_valid_15);
  reg [32-1:0] _tmp_data_16;
  reg _tmp_valid_16;
  wire _tmp_ready_16;
  assign _tmp_ready_16 = (_tmp_ready_18 || !_tmp_valid_18) && (_tmp_valid_15 && _tmp_valid_16) && ((_tmp_ready_20 || !_tmp_valid_20) && _tmp_valid_16);
  reg [32-1:0] _tmp_data_17;
  reg _tmp_valid_17;
  wire _tmp_ready_17;
  assign _tmp_ready_17 = (_tmp_ready_19 || !_tmp_valid_19) && (_tmp_valid_17 && _tmp_valid_14) && ((_tmp_ready_23 || !_tmp_valid_23) && _tmp_valid_17);
  reg [1-1:0] _tmp_data_18;
  reg _tmp_valid_18;
  wire _tmp_ready_18;
  assign _tmp_ready_18 = (_tmp_ready_24 || !_tmp_valid_24) && (_tmp_valid_18 && _tmp_valid_21 && _tmp_valid_20) && ((_tmp_ready_25 || !_tmp_valid_25) && (_tmp_valid_18 && _tmp_valid_20 && _tmp_valid_21));
  reg [1-1:0] _tmp_data_19;
  reg _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_ready_26 || !_tmp_valid_26) && (_tmp_valid_19 && _tmp_valid_23 && _tmp_valid_22) && ((_tmp_ready_27 || !_tmp_valid_27) && (_tmp_valid_19 && _tmp_valid_22 && _tmp_valid_23));
  reg [32-1:0] _tmp_data_20;
  reg _tmp_valid_20;
  wire _tmp_ready_20;
  assign _tmp_ready_20 = (_tmp_ready_24 || !_tmp_valid_24) && (_tmp_valid_18 && _tmp_valid_21 && _tmp_valid_20) && ((_tmp_ready_25 || !_tmp_valid_25) && (_tmp_valid_18 && _tmp_valid_20 && _tmp_valid_21));
  reg [32-1:0] _tmp_data_21;
  reg _tmp_valid_21;
  wire _tmp_ready_21;
  assign _tmp_ready_21 = (_tmp_ready_24 || !_tmp_valid_24) && (_tmp_valid_18 && _tmp_valid_21 && _tmp_valid_20) && ((_tmp_ready_25 || !_tmp_valid_25) && (_tmp_valid_18 && _tmp_valid_20 && _tmp_valid_21));
  reg [32-1:0] _tmp_data_22;
  reg _tmp_valid_22;
  wire _tmp_ready_22;
  assign _tmp_ready_22 = (_tmp_ready_26 || !_tmp_valid_26) && (_tmp_valid_19 && _tmp_valid_23 && _tmp_valid_22) && ((_tmp_ready_27 || !_tmp_valid_27) && (_tmp_valid_19 && _tmp_valid_22 && _tmp_valid_23));
  reg [32-1:0] _tmp_data_23;
  reg _tmp_valid_23;
  wire _tmp_ready_23;
  assign _tmp_ready_23 = (_tmp_ready_26 || !_tmp_valid_26) && (_tmp_valid_19 && _tmp_valid_23 && _tmp_valid_22) && ((_tmp_ready_27 || !_tmp_valid_27) && (_tmp_valid_19 && _tmp_valid_22 && _tmp_valid_23));
  reg [32-1:0] _tmp_data_24;
  reg _tmp_valid_24;
  wire _tmp_ready_24;
  assign _tmp_ready_24 = (_tmp_ready_28 || !_tmp_valid_28) && (_tmp_valid_27 && _tmp_valid_24) && ((_tmp_ready_29 || !_tmp_valid_29) && _tmp_valid_24);
  reg [32-1:0] _tmp_data_25;
  reg _tmp_valid_25;
  wire _tmp_ready_25;
  assign _tmp_ready_25 = (_tmp_ready_32 || !_tmp_valid_32) && _tmp_valid_25;
  reg [32-1:0] _tmp_data_26;
  reg _tmp_valid_26;
  wire _tmp_ready_26;
  assign _tmp_ready_26 = (_tmp_ready_31 || !_tmp_valid_31) && _tmp_valid_26;
  reg [32-1:0] _tmp_data_27;
  reg _tmp_valid_27;
  wire _tmp_ready_27;
  assign _tmp_ready_27 = (_tmp_ready_28 || !_tmp_valid_28) && (_tmp_valid_27 && _tmp_valid_24) && ((_tmp_ready_30 || !_tmp_valid_30) && _tmp_valid_27);
  reg [1-1:0] _tmp_data_28;
  reg _tmp_valid_28;
  wire _tmp_ready_28;
  assign _tmp_ready_28 = (_tmp_ready_33 || !_tmp_valid_33) && (_tmp_valid_28 && _tmp_valid_30 && _tmp_valid_29) && ((_tmp_ready_34 || !_tmp_valid_34) && (_tmp_valid_28 && _tmp_valid_29 && _tmp_valid_30));
  reg [32-1:0] _tmp_data_29;
  reg _tmp_valid_29;
  wire _tmp_ready_29;
  assign _tmp_ready_29 = (_tmp_ready_33 || !_tmp_valid_33) && (_tmp_valid_28 && _tmp_valid_30 && _tmp_valid_29) && ((_tmp_ready_34 || !_tmp_valid_34) && (_tmp_valid_28 && _tmp_valid_29 && _tmp_valid_30));
  reg [32-1:0] _tmp_data_30;
  reg _tmp_valid_30;
  wire _tmp_ready_30;
  assign _tmp_ready_30 = (_tmp_ready_33 || !_tmp_valid_33) && (_tmp_valid_28 && _tmp_valid_30 && _tmp_valid_29) && ((_tmp_ready_34 || !_tmp_valid_34) && (_tmp_valid_28 && _tmp_valid_29 && _tmp_valid_30));
  reg [32-1:0] _tmp_data_31;
  reg _tmp_valid_31;
  wire _tmp_ready_31;
  assign _tmp_ready_31 = (_tmp_ready_35 || !_tmp_valid_35) && _tmp_valid_31;
  reg [32-1:0] _tmp_data_32;
  reg _tmp_valid_32;
  wire _tmp_ready_32;
  assign _tmp_ready_32 = (_tmp_ready_36 || !_tmp_valid_36) && _tmp_valid_32;
  reg [32-1:0] _tmp_data_33;
  reg _tmp_valid_33;
  wire _tmp_ready_33;
  assign _tmp_ready_33 = (_tmp_ready_37 || !_tmp_valid_37) && (_tmp_valid_35 && _tmp_valid_33) && ((_tmp_ready_39 || !_tmp_valid_39) && _tmp_valid_33);
  reg [32-1:0] _tmp_data_34;
  reg _tmp_valid_34;
  wire _tmp_ready_34;
  assign _tmp_ready_34 = (_tmp_ready_41 || !_tmp_valid_41) && _tmp_valid_34;
  reg [32-1:0] _tmp_data_35;
  reg _tmp_valid_35;
  wire _tmp_ready_35;
  assign _tmp_ready_35 = (_tmp_ready_37 || !_tmp_valid_37) && (_tmp_valid_35 && _tmp_valid_33) && ((_tmp_ready_38 || !_tmp_valid_38) && _tmp_valid_35);
  reg [32-1:0] _tmp_data_36;
  reg _tmp_valid_36;
  wire _tmp_ready_36;
  assign _tmp_ready_36 = (_tmp_ready_40 || !_tmp_valid_40) && _tmp_valid_36;
  reg [1-1:0] _tmp_data_37;
  reg _tmp_valid_37;
  wire _tmp_ready_37;
  assign _tmp_ready_37 = (_tmp_ready_42 || !_tmp_valid_42) && (_tmp_valid_37 && _tmp_valid_38 && _tmp_valid_39) && ((_tmp_ready_43 || !_tmp_valid_43) && (_tmp_valid_37 && _tmp_valid_39 && _tmp_valid_38));
  reg [32-1:0] _tmp_data_38;
  reg _tmp_valid_38;
  wire _tmp_ready_38;
  assign _tmp_ready_38 = (_tmp_ready_42 || !_tmp_valid_42) && (_tmp_valid_37 && _tmp_valid_38 && _tmp_valid_39) && ((_tmp_ready_43 || !_tmp_valid_43) && (_tmp_valid_37 && _tmp_valid_39 && _tmp_valid_38));
  reg [32-1:0] _tmp_data_39;
  reg _tmp_valid_39;
  wire _tmp_ready_39;
  assign _tmp_ready_39 = (_tmp_ready_42 || !_tmp_valid_42) && (_tmp_valid_37 && _tmp_valid_38 && _tmp_valid_39) && ((_tmp_ready_43 || !_tmp_valid_43) && (_tmp_valid_37 && _tmp_valid_39 && _tmp_valid_38));
  reg [32-1:0] _tmp_data_40;
  reg _tmp_valid_40;
  wire _tmp_ready_40;
  assign _tmp_ready_40 = (_tmp_ready_44 || !_tmp_valid_44) && _tmp_valid_40;
  reg [32-1:0] _tmp_data_41;
  reg _tmp_valid_41;
  wire _tmp_ready_41;
  assign _tmp_ready_41 = (_tmp_ready_45 || !_tmp_valid_45) && _tmp_valid_41;
  reg [32-1:0] _tmp_data_42;
  reg _tmp_valid_42;
  wire _tmp_ready_42;
  reg [32-1:0] _tmp_data_43;
  reg _tmp_valid_43;
  wire _tmp_ready_43;
  reg [32-1:0] _tmp_data_44;
  reg _tmp_valid_44;
  wire _tmp_ready_44;
  reg [32-1:0] _tmp_data_45;
  reg _tmp_valid_45;
  wire _tmp_ready_45;
  assign dout0 = _tmp_data_42;
  assign _tmp_ready_42 = 1;
  assign dout1 = _tmp_data_43;
  assign _tmp_ready_43 = 1;
  assign dout3 = _tmp_data_44;
  assign _tmp_ready_44 = 1;
  assign dout2 = _tmp_data_45;
  assign _tmp_ready_45 = 1;

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
      _tmp_data_6 <= 0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
      _tmp_data_8 <= 0;
      _tmp_valid_8 <= 0;
      _tmp_data_9 <= 0;
      _tmp_valid_9 <= 0;
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
      _tmp_data_26 <= 0;
      _tmp_valid_26 <= 0;
      _tmp_data_27 <= 0;
      _tmp_valid_27 <= 0;
      _tmp_data_28 <= 0;
      _tmp_valid_28 <= 0;
      _tmp_data_29 <= 0;
      _tmp_valid_29 <= 0;
      _tmp_data_30 <= 0;
      _tmp_valid_30 <= 0;
      _tmp_data_31 <= 0;
      _tmp_valid_31 <= 0;
      _tmp_data_32 <= 0;
      _tmp_valid_32 <= 0;
      _tmp_data_33 <= 0;
      _tmp_valid_33 <= 0;
      _tmp_data_34 <= 0;
      _tmp_valid_34 <= 0;
      _tmp_data_35 <= 0;
      _tmp_valid_35 <= 0;
      _tmp_data_36 <= 0;
      _tmp_valid_36 <= 0;
      _tmp_data_37 <= 0;
      _tmp_valid_37 <= 0;
      _tmp_data_38 <= 0;
      _tmp_valid_38 <= 0;
      _tmp_data_39 <= 0;
      _tmp_valid_39 <= 0;
      _tmp_data_40 <= 0;
      _tmp_valid_40 <= 0;
      _tmp_data_41 <= 0;
      _tmp_valid_41 <= 0;
      _tmp_data_42 <= 0;
      _tmp_valid_42 <= 0;
      _tmp_data_43 <= 0;
      _tmp_valid_43 <= 0;
      _tmp_data_44 <= 0;
      _tmp_valid_44 <= 0;
      _tmp_data_45 <= 0;
      _tmp_valid_45 <= 0;
    end else begin
      if((_tmp_ready_0 || !_tmp_valid_0) && 1 && 1) begin
        _tmp_data_0 <= din0 < din1;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && 1) begin
        _tmp_valid_0 <= 1;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1 && 1) begin
        _tmp_data_1 <= din1;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1) begin
        _tmp_valid_1 <= 1;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && 1 && 1) begin
        _tmp_data_2 <= din0;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && 1) begin
        _tmp_valid_2 <= 1;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && 1 && 1) begin
        _tmp_data_3 <= din2;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && 1) begin
        _tmp_valid_3 <= 1;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && 1 && 1) begin
        _tmp_data_4 <= din3;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && 1) begin
        _tmp_valid_4 <= 1;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_ready_0 && _tmp_ready_2 && _tmp_ready_1) && (_tmp_valid_0 && _tmp_valid_2 && _tmp_valid_1)) begin
        _tmp_data_5 <= (_tmp_data_0)? _tmp_data_2 : _tmp_data_1;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_ready_0 && _tmp_ready_2 && _tmp_ready_1)) begin
        _tmp_valid_5 <= _tmp_valid_0 && _tmp_valid_2 && _tmp_valid_1;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_ready_0 && _tmp_ready_1 && _tmp_ready_2) && (_tmp_valid_0 && _tmp_valid_1 && _tmp_valid_2)) begin
        _tmp_data_6 <= (_tmp_data_0)? _tmp_data_1 : _tmp_data_2;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_ready_0 && _tmp_ready_1 && _tmp_ready_2)) begin
        _tmp_valid_6 <= _tmp_valid_0 && _tmp_valid_1 && _tmp_valid_2;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_3 && _tmp_valid_3) begin
        _tmp_data_7 <= _tmp_data_3;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_3) begin
        _tmp_valid_7 <= _tmp_valid_3;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && _tmp_ready_4 && _tmp_valid_4) begin
        _tmp_data_8 <= _tmp_data_4;
      end 
      if(_tmp_valid_8 && _tmp_ready_8) begin
        _tmp_valid_8 <= 0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && _tmp_ready_4) begin
        _tmp_valid_8 <= _tmp_valid_4;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && (_tmp_ready_6 && _tmp_ready_7) && (_tmp_valid_6 && _tmp_valid_7)) begin
        _tmp_data_9 <= _tmp_data_6 < _tmp_data_7;
      end 
      if(_tmp_valid_9 && _tmp_ready_9) begin
        _tmp_valid_9 <= 0;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && (_tmp_ready_6 && _tmp_ready_7)) begin
        _tmp_valid_9 <= _tmp_valid_6 && _tmp_valid_7;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && _tmp_ready_7 && _tmp_valid_7) begin
        _tmp_data_10 <= _tmp_data_7;
      end 
      if(_tmp_valid_10 && _tmp_ready_10) begin
        _tmp_valid_10 <= 0;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && _tmp_ready_7) begin
        _tmp_valid_10 <= _tmp_valid_7;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && _tmp_ready_6 && _tmp_valid_6) begin
        _tmp_data_11 <= _tmp_data_6;
      end 
      if(_tmp_valid_11 && _tmp_ready_11) begin
        _tmp_valid_11 <= 0;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && _tmp_ready_6) begin
        _tmp_valid_11 <= _tmp_valid_6;
      end 
      if((_tmp_ready_12 || !_tmp_valid_12) && _tmp_ready_8 && _tmp_valid_8) begin
        _tmp_data_12 <= _tmp_data_8;
      end 
      if(_tmp_valid_12 && _tmp_ready_12) begin
        _tmp_valid_12 <= 0;
      end 
      if((_tmp_ready_12 || !_tmp_valid_12) && _tmp_ready_8) begin
        _tmp_valid_12 <= _tmp_valid_8;
      end 
      if((_tmp_ready_13 || !_tmp_valid_13) && _tmp_ready_5 && _tmp_valid_5) begin
        _tmp_data_13 <= _tmp_data_5;
      end 
      if(_tmp_valid_13 && _tmp_ready_13) begin
        _tmp_valid_13 <= 0;
      end 
      if((_tmp_ready_13 || !_tmp_valid_13) && _tmp_ready_5) begin
        _tmp_valid_13 <= _tmp_valid_5;
      end 
      if((_tmp_ready_14 || !_tmp_valid_14) && (_tmp_ready_9 && _tmp_ready_11 && _tmp_ready_10) && (_tmp_valid_9 && _tmp_valid_11 && _tmp_valid_10)) begin
        _tmp_data_14 <= (_tmp_data_9)? _tmp_data_11 : _tmp_data_10;
      end 
      if(_tmp_valid_14 && _tmp_ready_14) begin
        _tmp_valid_14 <= 0;
      end 
      if((_tmp_ready_14 || !_tmp_valid_14) && (_tmp_ready_9 && _tmp_ready_11 && _tmp_ready_10)) begin
        _tmp_valid_14 <= _tmp_valid_9 && _tmp_valid_11 && _tmp_valid_10;
      end 
      if((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_ready_9 && _tmp_ready_10 && _tmp_ready_11) && (_tmp_valid_9 && _tmp_valid_10 && _tmp_valid_11)) begin
        _tmp_data_15 <= (_tmp_data_9)? _tmp_data_10 : _tmp_data_11;
      end 
      if(_tmp_valid_15 && _tmp_ready_15) begin
        _tmp_valid_15 <= 0;
      end 
      if((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_ready_9 && _tmp_ready_10 && _tmp_ready_11)) begin
        _tmp_valid_15 <= _tmp_valid_9 && _tmp_valid_10 && _tmp_valid_11;
      end 
      if((_tmp_ready_16 || !_tmp_valid_16) && _tmp_ready_12 && _tmp_valid_12) begin
        _tmp_data_16 <= _tmp_data_12;
      end 
      if(_tmp_valid_16 && _tmp_ready_16) begin
        _tmp_valid_16 <= 0;
      end 
      if((_tmp_ready_16 || !_tmp_valid_16) && _tmp_ready_12) begin
        _tmp_valid_16 <= _tmp_valid_12;
      end 
      if((_tmp_ready_17 || !_tmp_valid_17) && _tmp_ready_13 && _tmp_valid_13) begin
        _tmp_data_17 <= _tmp_data_13;
      end 
      if(_tmp_valid_17 && _tmp_ready_17) begin
        _tmp_valid_17 <= 0;
      end 
      if((_tmp_ready_17 || !_tmp_valid_17) && _tmp_ready_13) begin
        _tmp_valid_17 <= _tmp_valid_13;
      end 
      if((_tmp_ready_18 || !_tmp_valid_18) && (_tmp_ready_15 && _tmp_ready_16) && (_tmp_valid_15 && _tmp_valid_16)) begin
        _tmp_data_18 <= _tmp_data_15 < _tmp_data_16;
      end 
      if(_tmp_valid_18 && _tmp_ready_18) begin
        _tmp_valid_18 <= 0;
      end 
      if((_tmp_ready_18 || !_tmp_valid_18) && (_tmp_ready_15 && _tmp_ready_16)) begin
        _tmp_valid_18 <= _tmp_valid_15 && _tmp_valid_16;
      end 
      if((_tmp_ready_19 || !_tmp_valid_19) && (_tmp_ready_17 && _tmp_ready_14) && (_tmp_valid_17 && _tmp_valid_14)) begin
        _tmp_data_19 <= _tmp_data_17 < _tmp_data_14;
      end 
      if(_tmp_valid_19 && _tmp_ready_19) begin
        _tmp_valid_19 <= 0;
      end 
      if((_tmp_ready_19 || !_tmp_valid_19) && (_tmp_ready_17 && _tmp_ready_14)) begin
        _tmp_valid_19 <= _tmp_valid_17 && _tmp_valid_14;
      end 
      if((_tmp_ready_20 || !_tmp_valid_20) && _tmp_ready_16 && _tmp_valid_16) begin
        _tmp_data_20 <= _tmp_data_16;
      end 
      if(_tmp_valid_20 && _tmp_ready_20) begin
        _tmp_valid_20 <= 0;
      end 
      if((_tmp_ready_20 || !_tmp_valid_20) && _tmp_ready_16) begin
        _tmp_valid_20 <= _tmp_valid_16;
      end 
      if((_tmp_ready_21 || !_tmp_valid_21) && _tmp_ready_15 && _tmp_valid_15) begin
        _tmp_data_21 <= _tmp_data_15;
      end 
      if(_tmp_valid_21 && _tmp_ready_21) begin
        _tmp_valid_21 <= 0;
      end 
      if((_tmp_ready_21 || !_tmp_valid_21) && _tmp_ready_15) begin
        _tmp_valid_21 <= _tmp_valid_15;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && _tmp_ready_14 && _tmp_valid_14) begin
        _tmp_data_22 <= _tmp_data_14;
      end 
      if(_tmp_valid_22 && _tmp_ready_22) begin
        _tmp_valid_22 <= 0;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && _tmp_ready_14) begin
        _tmp_valid_22 <= _tmp_valid_14;
      end 
      if((_tmp_ready_23 || !_tmp_valid_23) && _tmp_ready_17 && _tmp_valid_17) begin
        _tmp_data_23 <= _tmp_data_17;
      end 
      if(_tmp_valid_23 && _tmp_ready_23) begin
        _tmp_valid_23 <= 0;
      end 
      if((_tmp_ready_23 || !_tmp_valid_23) && _tmp_ready_17) begin
        _tmp_valid_23 <= _tmp_valid_17;
      end 
      if((_tmp_ready_24 || !_tmp_valid_24) && (_tmp_ready_18 && _tmp_ready_21 && _tmp_ready_20) && (_tmp_valid_18 && _tmp_valid_21 && _tmp_valid_20)) begin
        _tmp_data_24 <= (_tmp_data_18)? _tmp_data_21 : _tmp_data_20;
      end 
      if(_tmp_valid_24 && _tmp_ready_24) begin
        _tmp_valid_24 <= 0;
      end 
      if((_tmp_ready_24 || !_tmp_valid_24) && (_tmp_ready_18 && _tmp_ready_21 && _tmp_ready_20)) begin
        _tmp_valid_24 <= _tmp_valid_18 && _tmp_valid_21 && _tmp_valid_20;
      end 
      if((_tmp_ready_25 || !_tmp_valid_25) && (_tmp_ready_18 && _tmp_ready_20 && _tmp_ready_21) && (_tmp_valid_18 && _tmp_valid_20 && _tmp_valid_21)) begin
        _tmp_data_25 <= (_tmp_data_18)? _tmp_data_20 : _tmp_data_21;
      end 
      if(_tmp_valid_25 && _tmp_ready_25) begin
        _tmp_valid_25 <= 0;
      end 
      if((_tmp_ready_25 || !_tmp_valid_25) && (_tmp_ready_18 && _tmp_ready_20 && _tmp_ready_21)) begin
        _tmp_valid_25 <= _tmp_valid_18 && _tmp_valid_20 && _tmp_valid_21;
      end 
      if((_tmp_ready_26 || !_tmp_valid_26) && (_tmp_ready_19 && _tmp_ready_23 && _tmp_ready_22) && (_tmp_valid_19 && _tmp_valid_23 && _tmp_valid_22)) begin
        _tmp_data_26 <= (_tmp_data_19)? _tmp_data_23 : _tmp_data_22;
      end 
      if(_tmp_valid_26 && _tmp_ready_26) begin
        _tmp_valid_26 <= 0;
      end 
      if((_tmp_ready_26 || !_tmp_valid_26) && (_tmp_ready_19 && _tmp_ready_23 && _tmp_ready_22)) begin
        _tmp_valid_26 <= _tmp_valid_19 && _tmp_valid_23 && _tmp_valid_22;
      end 
      if((_tmp_ready_27 || !_tmp_valid_27) && (_tmp_ready_19 && _tmp_ready_22 && _tmp_ready_23) && (_tmp_valid_19 && _tmp_valid_22 && _tmp_valid_23)) begin
        _tmp_data_27 <= (_tmp_data_19)? _tmp_data_22 : _tmp_data_23;
      end 
      if(_tmp_valid_27 && _tmp_ready_27) begin
        _tmp_valid_27 <= 0;
      end 
      if((_tmp_ready_27 || !_tmp_valid_27) && (_tmp_ready_19 && _tmp_ready_22 && _tmp_ready_23)) begin
        _tmp_valid_27 <= _tmp_valid_19 && _tmp_valid_22 && _tmp_valid_23;
      end 
      if((_tmp_ready_28 || !_tmp_valid_28) && (_tmp_ready_27 && _tmp_ready_24) && (_tmp_valid_27 && _tmp_valid_24)) begin
        _tmp_data_28 <= _tmp_data_27 < _tmp_data_24;
      end 
      if(_tmp_valid_28 && _tmp_ready_28) begin
        _tmp_valid_28 <= 0;
      end 
      if((_tmp_ready_28 || !_tmp_valid_28) && (_tmp_ready_27 && _tmp_ready_24)) begin
        _tmp_valid_28 <= _tmp_valid_27 && _tmp_valid_24;
      end 
      if((_tmp_ready_29 || !_tmp_valid_29) && _tmp_ready_24 && _tmp_valid_24) begin
        _tmp_data_29 <= _tmp_data_24;
      end 
      if(_tmp_valid_29 && _tmp_ready_29) begin
        _tmp_valid_29 <= 0;
      end 
      if((_tmp_ready_29 || !_tmp_valid_29) && _tmp_ready_24) begin
        _tmp_valid_29 <= _tmp_valid_24;
      end 
      if((_tmp_ready_30 || !_tmp_valid_30) && _tmp_ready_27 && _tmp_valid_27) begin
        _tmp_data_30 <= _tmp_data_27;
      end 
      if(_tmp_valid_30 && _tmp_ready_30) begin
        _tmp_valid_30 <= 0;
      end 
      if((_tmp_ready_30 || !_tmp_valid_30) && _tmp_ready_27) begin
        _tmp_valid_30 <= _tmp_valid_27;
      end 
      if((_tmp_ready_31 || !_tmp_valid_31) && _tmp_ready_26 && _tmp_valid_26) begin
        _tmp_data_31 <= _tmp_data_26;
      end 
      if(_tmp_valid_31 && _tmp_ready_31) begin
        _tmp_valid_31 <= 0;
      end 
      if((_tmp_ready_31 || !_tmp_valid_31) && _tmp_ready_26) begin
        _tmp_valid_31 <= _tmp_valid_26;
      end 
      if((_tmp_ready_32 || !_tmp_valid_32) && _tmp_ready_25 && _tmp_valid_25) begin
        _tmp_data_32 <= _tmp_data_25;
      end 
      if(_tmp_valid_32 && _tmp_ready_32) begin
        _tmp_valid_32 <= 0;
      end 
      if((_tmp_ready_32 || !_tmp_valid_32) && _tmp_ready_25) begin
        _tmp_valid_32 <= _tmp_valid_25;
      end 
      if((_tmp_ready_33 || !_tmp_valid_33) && (_tmp_ready_28 && _tmp_ready_30 && _tmp_ready_29) && (_tmp_valid_28 && _tmp_valid_30 && _tmp_valid_29)) begin
        _tmp_data_33 <= (_tmp_data_28)? _tmp_data_30 : _tmp_data_29;
      end 
      if(_tmp_valid_33 && _tmp_ready_33) begin
        _tmp_valid_33 <= 0;
      end 
      if((_tmp_ready_33 || !_tmp_valid_33) && (_tmp_ready_28 && _tmp_ready_30 && _tmp_ready_29)) begin
        _tmp_valid_33 <= _tmp_valid_28 && _tmp_valid_30 && _tmp_valid_29;
      end 
      if((_tmp_ready_34 || !_tmp_valid_34) && (_tmp_ready_28 && _tmp_ready_29 && _tmp_ready_30) && (_tmp_valid_28 && _tmp_valid_29 && _tmp_valid_30)) begin
        _tmp_data_34 <= (_tmp_data_28)? _tmp_data_29 : _tmp_data_30;
      end 
      if(_tmp_valid_34 && _tmp_ready_34) begin
        _tmp_valid_34 <= 0;
      end 
      if((_tmp_ready_34 || !_tmp_valid_34) && (_tmp_ready_28 && _tmp_ready_29 && _tmp_ready_30)) begin
        _tmp_valid_34 <= _tmp_valid_28 && _tmp_valid_29 && _tmp_valid_30;
      end 
      if((_tmp_ready_35 || !_tmp_valid_35) && _tmp_ready_31 && _tmp_valid_31) begin
        _tmp_data_35 <= _tmp_data_31;
      end 
      if(_tmp_valid_35 && _tmp_ready_35) begin
        _tmp_valid_35 <= 0;
      end 
      if((_tmp_ready_35 || !_tmp_valid_35) && _tmp_ready_31) begin
        _tmp_valid_35 <= _tmp_valid_31;
      end 
      if((_tmp_ready_36 || !_tmp_valid_36) && _tmp_ready_32 && _tmp_valid_32) begin
        _tmp_data_36 <= _tmp_data_32;
      end 
      if(_tmp_valid_36 && _tmp_ready_36) begin
        _tmp_valid_36 <= 0;
      end 
      if((_tmp_ready_36 || !_tmp_valid_36) && _tmp_ready_32) begin
        _tmp_valid_36 <= _tmp_valid_32;
      end 
      if((_tmp_ready_37 || !_tmp_valid_37) && (_tmp_ready_35 && _tmp_ready_33) && (_tmp_valid_35 && _tmp_valid_33)) begin
        _tmp_data_37 <= _tmp_data_35 < _tmp_data_33;
      end 
      if(_tmp_valid_37 && _tmp_ready_37) begin
        _tmp_valid_37 <= 0;
      end 
      if((_tmp_ready_37 || !_tmp_valid_37) && (_tmp_ready_35 && _tmp_ready_33)) begin
        _tmp_valid_37 <= _tmp_valid_35 && _tmp_valid_33;
      end 
      if((_tmp_ready_38 || !_tmp_valid_38) && _tmp_ready_35 && _tmp_valid_35) begin
        _tmp_data_38 <= _tmp_data_35;
      end 
      if(_tmp_valid_38 && _tmp_ready_38) begin
        _tmp_valid_38 <= 0;
      end 
      if((_tmp_ready_38 || !_tmp_valid_38) && _tmp_ready_35) begin
        _tmp_valid_38 <= _tmp_valid_35;
      end 
      if((_tmp_ready_39 || !_tmp_valid_39) && _tmp_ready_33 && _tmp_valid_33) begin
        _tmp_data_39 <= _tmp_data_33;
      end 
      if(_tmp_valid_39 && _tmp_ready_39) begin
        _tmp_valid_39 <= 0;
      end 
      if((_tmp_ready_39 || !_tmp_valid_39) && _tmp_ready_33) begin
        _tmp_valid_39 <= _tmp_valid_33;
      end 
      if((_tmp_ready_40 || !_tmp_valid_40) && _tmp_ready_36 && _tmp_valid_36) begin
        _tmp_data_40 <= _tmp_data_36;
      end 
      if(_tmp_valid_40 && _tmp_ready_40) begin
        _tmp_valid_40 <= 0;
      end 
      if((_tmp_ready_40 || !_tmp_valid_40) && _tmp_ready_36) begin
        _tmp_valid_40 <= _tmp_valid_36;
      end 
      if((_tmp_ready_41 || !_tmp_valid_41) && _tmp_ready_34 && _tmp_valid_34) begin
        _tmp_data_41 <= _tmp_data_34;
      end 
      if(_tmp_valid_41 && _tmp_ready_41) begin
        _tmp_valid_41 <= 0;
      end 
      if((_tmp_ready_41 || !_tmp_valid_41) && _tmp_ready_34) begin
        _tmp_valid_41 <= _tmp_valid_34;
      end 
      if((_tmp_ready_42 || !_tmp_valid_42) && (_tmp_ready_37 && _tmp_ready_38 && _tmp_ready_39) && (_tmp_valid_37 && _tmp_valid_38 && _tmp_valid_39)) begin
        _tmp_data_42 <= (_tmp_data_37)? _tmp_data_38 : _tmp_data_39;
      end 
      if(_tmp_valid_42 && _tmp_ready_42) begin
        _tmp_valid_42 <= 0;
      end 
      if((_tmp_ready_42 || !_tmp_valid_42) && (_tmp_ready_37 && _tmp_ready_38 && _tmp_ready_39)) begin
        _tmp_valid_42 <= _tmp_valid_37 && _tmp_valid_38 && _tmp_valid_39;
      end 
      if((_tmp_ready_43 || !_tmp_valid_43) && (_tmp_ready_37 && _tmp_ready_39 && _tmp_ready_38) && (_tmp_valid_37 && _tmp_valid_39 && _tmp_valid_38)) begin
        _tmp_data_43 <= (_tmp_data_37)? _tmp_data_39 : _tmp_data_38;
      end 
      if(_tmp_valid_43 && _tmp_ready_43) begin
        _tmp_valid_43 <= 0;
      end 
      if((_tmp_ready_43 || !_tmp_valid_43) && (_tmp_ready_37 && _tmp_ready_39 && _tmp_ready_38)) begin
        _tmp_valid_43 <= _tmp_valid_37 && _tmp_valid_39 && _tmp_valid_38;
      end 
      if((_tmp_ready_44 || !_tmp_valid_44) && _tmp_ready_40 && _tmp_valid_40) begin
        _tmp_data_44 <= _tmp_data_40;
      end 
      if(_tmp_valid_44 && _tmp_ready_44) begin
        _tmp_valid_44 <= 0;
      end 
      if((_tmp_ready_44 || !_tmp_valid_44) && _tmp_ready_40) begin
        _tmp_valid_44 <= _tmp_valid_40;
      end 
      if((_tmp_ready_45 || !_tmp_valid_45) && _tmp_ready_41 && _tmp_valid_41) begin
        _tmp_data_45 <= _tmp_data_41;
      end 
      if(_tmp_valid_45 && _tmp_ready_45) begin
        _tmp_valid_45 <= 0;
      end 
      if((_tmp_ready_45 || !_tmp_valid_45) && _tmp_ready_41) begin
        _tmp_valid_45 <= _tmp_valid_41;
      end 
    end
  end


endmodule
"""

def test():
    test_module = dataflow_sort.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
