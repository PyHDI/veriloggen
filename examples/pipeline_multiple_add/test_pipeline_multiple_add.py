from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import pipeline_multiple_add
from veriloggen import *

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [32-1:0] d0;
  reg v0;
  wire r0;
  reg [32-1:0] d1;
  reg v1;
  wire r1;
  reg [32-1:0] d2;
  reg v2;
  wire r2;
  reg [32-1:0] d3;
  reg v3;
  wire r3;
  reg [32-1:0] d4;
  reg v4;
  wire r4;
  reg [32-1:0] d5;
  reg v5;
  wire r5;
  reg [32-1:0] d6;
  reg v6;
  wire r6;
  reg [32-1:0] d7;
  reg v7;
  wire r7;
  wire [32-1:0] dz;
  wire vz;
  reg rz;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .d0(d0),
    .v0(v0),
    .r0(r0),
    .d1(d1),
    .v1(v1),
    .r1(r1),
    .d2(d2),
    .v2(v2),
    .r2(r2),
    .d3(d3),
    .v3(v3),
    .r3(r3),
    .d4(d4),
    .v4(v4),
    .r4(r4),
    .d5(d5),
    .v5(v5),
    .r5(r5),
    .d6(d6),
    .v6(v6),
    .r6(r6),
    .d7(d7),
    .v7(v7),
    .r7(r7),
    .dz(dz),
    .vz(vz),
    .rz(rz)
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
    d0 = 0;
    v0 = 0;
    d1 = 0;
    v1 = 0;
    d2 = 0;
    v2 = 0;
    d3 = 0;
    v3 = 0;
    d4 = 0;
    v4 = 0;
    d5 = 0;
    v5 = 0;
    d6 = 0;
    v6 = 0;
    d7 = 0;
    v7 = 0;
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

  reg [32-1:0] _tmp_0;
  reg [32-1:0] fsm0;
  localparam fsm0_init = 0;
  localparam fsm0_1 = 1;
  localparam fsm0_2 = 2;
  localparam fsm0_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm0 <= fsm0_init;
      _tmp_0 <= 0;
    end else begin
      case(fsm0)
        fsm0_init: begin
          v0 <= 0;
          if(reset_done) begin
            fsm0 <= fsm0_1;
          end 
        end
        fsm0_1: begin
          v0 <= 1;
          fsm0 <= fsm0_2;
        end
        fsm0_2: begin
          if(r0) begin
            d0 <= d0 + 0 + 1;
          end 
          if(r0) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 10) && r0) begin
            fsm0 <= fsm0_3;
          end 
        end
        fsm0_3: begin
          v0 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_1;
  reg [32-1:0] fsm1;
  localparam fsm1_init = 0;
  localparam fsm1_1 = 1;
  localparam fsm1_2 = 2;
  localparam fsm1_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm1 <= fsm1_init;
      _tmp_1 <= 0;
    end else begin
      case(fsm1)
        fsm1_init: begin
          v1 <= 0;
          if(reset_done) begin
            fsm1 <= fsm1_1;
          end 
        end
        fsm1_1: begin
          v1 <= 1;
          fsm1 <= fsm1_2;
        end
        fsm1_2: begin
          if(r1) begin
            d1 <= d1 + 1 + 1;
          end 
          if(r1) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((_tmp_1 == 10) && r1) begin
            fsm1 <= fsm1_3;
          end 
        end
        fsm1_3: begin
          v1 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_2;
  reg [32-1:0] fsm2;
  localparam fsm2_init = 0;
  localparam fsm2_1 = 1;
  localparam fsm2_2 = 2;
  localparam fsm2_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm2 <= fsm2_init;
      _tmp_2 <= 0;
    end else begin
      case(fsm2)
        fsm2_init: begin
          v2 <= 0;
          if(reset_done) begin
            fsm2 <= fsm2_1;
          end 
        end
        fsm2_1: begin
          v2 <= 1;
          fsm2 <= fsm2_2;
        end
        fsm2_2: begin
          if(r2) begin
            d2 <= d2 + 2 + 1;
          end 
          if(r2) begin
            _tmp_2 <= _tmp_2 + 1;
          end 
          if((_tmp_2 == 10) && r2) begin
            fsm2 <= fsm2_3;
          end 
        end
        fsm2_3: begin
          v2 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_3;
  reg [32-1:0] fsm3;
  localparam fsm3_init = 0;
  localparam fsm3_1 = 1;
  localparam fsm3_2 = 2;
  localparam fsm3_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm3 <= fsm3_init;
      _tmp_3 <= 0;
    end else begin
      case(fsm3)
        fsm3_init: begin
          v3 <= 0;
          if(reset_done) begin
            fsm3 <= fsm3_1;
          end 
        end
        fsm3_1: begin
          v3 <= 1;
          fsm3 <= fsm3_2;
        end
        fsm3_2: begin
          if(r3) begin
            d3 <= d3 + 3 + 1;
          end 
          if(r3) begin
            _tmp_3 <= _tmp_3 + 1;
          end 
          if((_tmp_3 == 10) && r3) begin
            fsm3 <= fsm3_3;
          end 
        end
        fsm3_3: begin
          v3 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_4;
  reg [32-1:0] fsm4;
  localparam fsm4_init = 0;
  localparam fsm4_1 = 1;
  localparam fsm4_2 = 2;
  localparam fsm4_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm4 <= fsm4_init;
      _tmp_4 <= 0;
    end else begin
      case(fsm4)
        fsm4_init: begin
          v4 <= 0;
          if(reset_done) begin
            fsm4 <= fsm4_1;
          end 
        end
        fsm4_1: begin
          v4 <= 1;
          fsm4 <= fsm4_2;
        end
        fsm4_2: begin
          if(r4) begin
            d4 <= d4 + 4 + 1;
          end 
          if(r4) begin
            _tmp_4 <= _tmp_4 + 1;
          end 
          if((_tmp_4 == 10) && r4) begin
            fsm4 <= fsm4_3;
          end 
        end
        fsm4_3: begin
          v4 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_5;
  reg [32-1:0] fsm5;
  localparam fsm5_init = 0;
  localparam fsm5_1 = 1;
  localparam fsm5_2 = 2;
  localparam fsm5_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm5 <= fsm5_init;
      _tmp_5 <= 0;
    end else begin
      case(fsm5)
        fsm5_init: begin
          v5 <= 0;
          if(reset_done) begin
            fsm5 <= fsm5_1;
          end 
        end
        fsm5_1: begin
          v5 <= 1;
          fsm5 <= fsm5_2;
        end
        fsm5_2: begin
          if(r5) begin
            d5 <= d5 + 5 + 1;
          end 
          if(r5) begin
            _tmp_5 <= _tmp_5 + 1;
          end 
          if((_tmp_5 == 10) && r5) begin
            fsm5 <= fsm5_3;
          end 
        end
        fsm5_3: begin
          v5 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_6;
  reg [32-1:0] fsm6;
  localparam fsm6_init = 0;
  localparam fsm6_1 = 1;
  localparam fsm6_2 = 2;
  localparam fsm6_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm6 <= fsm6_init;
      _tmp_6 <= 0;
    end else begin
      case(fsm6)
        fsm6_init: begin
          v6 <= 0;
          if(reset_done) begin
            fsm6 <= fsm6_1;
          end 
        end
        fsm6_1: begin
          v6 <= 1;
          fsm6 <= fsm6_2;
        end
        fsm6_2: begin
          if(r6) begin
            d6 <= d6 + 6 + 1;
          end 
          if(r6) begin
            _tmp_6 <= _tmp_6 + 1;
          end 
          if((_tmp_6 == 10) && r6) begin
            fsm6 <= fsm6_3;
          end 
        end
        fsm6_3: begin
          v6 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] _tmp_7;
  reg [32-1:0] fsm7;
  localparam fsm7_init = 0;
  localparam fsm7_1 = 1;
  localparam fsm7_2 = 2;
  localparam fsm7_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm7 <= fsm7_init;
      _tmp_7 <= 0;
    end else begin
      case(fsm7)
        fsm7_init: begin
          v7 <= 0;
          if(reset_done) begin
            fsm7 <= fsm7_1;
          end 
        end
        fsm7_1: begin
          v7 <= 1;
          fsm7 <= fsm7_2;
        end
        fsm7_2: begin
          if(r7) begin
            d7 <= d7 + 7 + 1;
          end 
          if(r7) begin
            _tmp_7 <= _tmp_7 + 1;
          end 
          if((_tmp_7 == 10) && r7) begin
            fsm7 <= fsm7_3;
          end 
        end
        fsm7_3: begin
          v7 <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  localparam zfsm_1 = 1;
  localparam zfsm_2 = 2;
  localparam zfsm_3 = 3;
  localparam zfsm_4 = 4;
  localparam zfsm_5 = 5;
  localparam zfsm_6 = 6;
  localparam zfsm_7 = 7;
  localparam zfsm_8 = 8;
  localparam zfsm_9 = 9;
  localparam zfsm_10 = 10;
  localparam zfsm_11 = 11;
  localparam zfsm_12 = 12;
  localparam zfsm_13 = 13;

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
    end else begin
      case(zfsm)
        zfsm_init: begin
          rz <= 0;
          if(reset_done) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          if(vz) begin
            rz <= 1;
          end 
          if(vz) begin
            zfsm <= zfsm_3;
          end 
        end
        zfsm_3: begin
          rz <= 0;
          zfsm <= zfsm_4;
        end
        zfsm_4: begin
          rz <= 0;
          zfsm <= zfsm_5;
        end
        zfsm_5: begin
          rz <= 0;
          zfsm <= zfsm_6;
        end
        zfsm_6: begin
          rz <= 0;
          zfsm <= zfsm_7;
        end
        zfsm_7: begin
          rz <= 0;
          zfsm <= zfsm_8;
        end
        zfsm_8: begin
          rz <= 0;
          zfsm <= zfsm_9;
        end
        zfsm_9: begin
          rz <= 0;
          zfsm <= zfsm_10;
        end
        zfsm_10: begin
          rz <= 0;
          zfsm <= zfsm_11;
        end
        zfsm_11: begin
          rz <= 0;
          zfsm <= zfsm_12;
        end
        zfsm_12: begin
          rz <= 0;
          zfsm <= zfsm_13;
        end
        zfsm_13: begin
          zfsm <= zfsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(v0 && r0) begin
        $display("d0=%d", d0);
      end 
      if(v1 && r1) begin
        $display("d1=%d", d1);
      end 
      if(v2 && r2) begin
        $display("d2=%d", d2);
      end 
      if(v3 && r3) begin
        $display("d3=%d", d3);
      end 
      if(v4 && r4) begin
        $display("d4=%d", d4);
      end 
      if(v5 && r5) begin
        $display("d5=%d", d5);
      end 
      if(v6 && r6) begin
        $display("d6=%d", d6);
      end 
      if(v7 && r7) begin
        $display("d7=%d", d7);
      end 
      if(vz && rz) begin
        $display("dz=%d", dz);
      end 
    end 
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] d0,
  input v0,
  output r0,
  input [32-1:0] d1,
  input v1,
  output r1,
  input [32-1:0] d2,
  input v2,
  output r2,
  input [32-1:0] d3,
  input v3,
  output r3,
  input [32-1:0] d4,
  input v4,
  output r4,
  input [32-1:0] d5,
  input v5,
  output r5,
  input [32-1:0] d6,
  input v6,
  output r6,
  input [32-1:0] d7,
  input v7,
  output r7,
  output [32-1:0] dz,
  output vz,
  input rz
);

  assign r0 = (_df_ready_0 || !_df_valid_0) && (v0 && v1);
  assign r1 = (_df_ready_0 || !_df_valid_0) && (v0 && v1);
  assign r2 = (_df_ready_1 || !_df_valid_1) && v2;
  assign r3 = (_df_ready_3 || !_df_valid_3) && v3;
  assign r4 = (_df_ready_6 || !_df_valid_6) && v4;
  assign r5 = (_df_ready_10 || !_df_valid_10) && v5;
  assign r6 = (_df_ready_15 || !_df_valid_15) && v6;
  assign r7 = (_df_ready_21 || !_df_valid_21) && v7;
  reg [32-1:0] _df_data_0;
  reg _df_valid_0;
  wire _df_ready_0;
  assign _df_ready_0 = (_df_ready_2 || !_df_valid_2) && (_df_valid_0 && _df_valid_1);
  reg [32-1:0] _df_data_1;
  reg _df_valid_1;
  wire _df_ready_1;
  assign _df_ready_1 = (_df_ready_2 || !_df_valid_2) && (_df_valid_0 && _df_valid_1);
  reg [32-1:0] _df_data_2;
  reg _df_valid_2;
  wire _df_ready_2;
  assign _df_ready_2 = (_df_ready_5 || !_df_valid_5) && (_df_valid_2 && _df_valid_4);
  reg [32-1:0] _df_data_3;
  reg _df_valid_3;
  wire _df_ready_3;
  assign _df_ready_3 = (_df_ready_4 || !_df_valid_4) && _df_valid_3;
  reg [32-1:0] _df_data_4;
  reg _df_valid_4;
  wire _df_ready_4;
  assign _df_ready_4 = (_df_ready_5 || !_df_valid_5) && (_df_valid_2 && _df_valid_4);
  reg [32-1:0] _df_data_5;
  reg _df_valid_5;
  wire _df_ready_5;
  assign _df_ready_5 = (_df_ready_9 || !_df_valid_9) && (_df_valid_5 && _df_valid_8);
  reg [32-1:0] _df_data_6;
  reg _df_valid_6;
  wire _df_ready_6;
  assign _df_ready_6 = (_df_ready_7 || !_df_valid_7) && _df_valid_6;
  reg [32-1:0] _df_data_7;
  reg _df_valid_7;
  wire _df_ready_7;
  assign _df_ready_7 = (_df_ready_8 || !_df_valid_8) && _df_valid_7;
  reg [32-1:0] _df_data_8;
  reg _df_valid_8;
  wire _df_ready_8;
  assign _df_ready_8 = (_df_ready_9 || !_df_valid_9) && (_df_valid_5 && _df_valid_8);
  reg [32-1:0] _df_data_9;
  reg _df_valid_9;
  wire _df_ready_9;
  assign _df_ready_9 = (_df_ready_14 || !_df_valid_14) && (_df_valid_9 && _df_valid_13);
  reg [32-1:0] _df_data_10;
  reg _df_valid_10;
  wire _df_ready_10;
  assign _df_ready_10 = (_df_ready_11 || !_df_valid_11) && _df_valid_10;
  reg [32-1:0] _df_data_11;
  reg _df_valid_11;
  wire _df_ready_11;
  assign _df_ready_11 = (_df_ready_12 || !_df_valid_12) && _df_valid_11;
  reg [32-1:0] _df_data_12;
  reg _df_valid_12;
  wire _df_ready_12;
  assign _df_ready_12 = (_df_ready_13 || !_df_valid_13) && _df_valid_12;
  reg [32-1:0] _df_data_13;
  reg _df_valid_13;
  wire _df_ready_13;
  assign _df_ready_13 = (_df_ready_14 || !_df_valid_14) && (_df_valid_9 && _df_valid_13);
  reg [32-1:0] _df_data_14;
  reg _df_valid_14;
  wire _df_ready_14;
  assign _df_ready_14 = (_df_ready_20 || !_df_valid_20) && (_df_valid_14 && _df_valid_19);
  reg [32-1:0] _df_data_15;
  reg _df_valid_15;
  wire _df_ready_15;
  assign _df_ready_15 = (_df_ready_16 || !_df_valid_16) && _df_valid_15;
  reg [32-1:0] _df_data_16;
  reg _df_valid_16;
  wire _df_ready_16;
  assign _df_ready_16 = (_df_ready_17 || !_df_valid_17) && _df_valid_16;
  reg [32-1:0] _df_data_17;
  reg _df_valid_17;
  wire _df_ready_17;
  assign _df_ready_17 = (_df_ready_18 || !_df_valid_18) && _df_valid_17;
  reg [32-1:0] _df_data_18;
  reg _df_valid_18;
  wire _df_ready_18;
  assign _df_ready_18 = (_df_ready_19 || !_df_valid_19) && _df_valid_18;
  reg [32-1:0] _df_data_19;
  reg _df_valid_19;
  wire _df_ready_19;
  assign _df_ready_19 = (_df_ready_20 || !_df_valid_20) && (_df_valid_14 && _df_valid_19);
  reg [32-1:0] _df_data_20;
  reg _df_valid_20;
  wire _df_ready_20;
  assign _df_ready_20 = (_df_ready_27 || !_df_valid_27) && (_df_valid_20 && _df_valid_26);
  reg [32-1:0] _df_data_21;
  reg _df_valid_21;
  wire _df_ready_21;
  assign _df_ready_21 = (_df_ready_22 || !_df_valid_22) && _df_valid_21;
  reg [32-1:0] _df_data_22;
  reg _df_valid_22;
  wire _df_ready_22;
  assign _df_ready_22 = (_df_ready_23 || !_df_valid_23) && _df_valid_22;
  reg [32-1:0] _df_data_23;
  reg _df_valid_23;
  wire _df_ready_23;
  assign _df_ready_23 = (_df_ready_24 || !_df_valid_24) && _df_valid_23;
  reg [32-1:0] _df_data_24;
  reg _df_valid_24;
  wire _df_ready_24;
  assign _df_ready_24 = (_df_ready_25 || !_df_valid_25) && _df_valid_24;
  reg [32-1:0] _df_data_25;
  reg _df_valid_25;
  wire _df_ready_25;
  assign _df_ready_25 = (_df_ready_26 || !_df_valid_26) && _df_valid_25;
  reg [32-1:0] _df_data_26;
  reg _df_valid_26;
  wire _df_ready_26;
  assign _df_ready_26 = (_df_ready_27 || !_df_valid_27) && (_df_valid_20 && _df_valid_26);
  reg [32-1:0] _df_data_27;
  reg _df_valid_27;
  wire _df_ready_27;
  assign _df_ready_27 = rz;
  assign dz = _df_data_27;
  assign vz = _df_valid_27;

  always @(posedge CLK) begin
    if(RST) begin
      _df_data_0 <= 0;
      _df_valid_0 <= 0;
      _df_data_1 <= 0;
      _df_valid_1 <= 0;
      _df_data_2 <= 0;
      _df_valid_2 <= 0;
      _df_data_3 <= 0;
      _df_valid_3 <= 0;
      _df_data_4 <= 0;
      _df_valid_4 <= 0;
      _df_data_5 <= 0;
      _df_valid_5 <= 0;
      _df_data_6 <= 0;
      _df_valid_6 <= 0;
      _df_data_7 <= 0;
      _df_valid_7 <= 0;
      _df_data_8 <= 0;
      _df_valid_8 <= 0;
      _df_data_9 <= 0;
      _df_valid_9 <= 0;
      _df_data_10 <= 0;
      _df_valid_10 <= 0;
      _df_data_11 <= 0;
      _df_valid_11 <= 0;
      _df_data_12 <= 0;
      _df_valid_12 <= 0;
      _df_data_13 <= 0;
      _df_valid_13 <= 0;
      _df_data_14 <= 0;
      _df_valid_14 <= 0;
      _df_data_15 <= 0;
      _df_valid_15 <= 0;
      _df_data_16 <= 0;
      _df_valid_16 <= 0;
      _df_data_17 <= 0;
      _df_valid_17 <= 0;
      _df_data_18 <= 0;
      _df_valid_18 <= 0;
      _df_data_19 <= 0;
      _df_valid_19 <= 0;
      _df_data_20 <= 0;
      _df_valid_20 <= 0;
      _df_data_21 <= 0;
      _df_valid_21 <= 0;
      _df_data_22 <= 0;
      _df_valid_22 <= 0;
      _df_data_23 <= 0;
      _df_valid_23 <= 0;
      _df_data_24 <= 0;
      _df_valid_24 <= 0;
      _df_data_25 <= 0;
      _df_valid_25 <= 0;
      _df_data_26 <= 0;
      _df_valid_26 <= 0;
      _df_data_27 <= 0;
      _df_valid_27 <= 0;
    end else begin
      if(v0 && v1 && (r0 && r1) && (_df_ready_0 || !_df_valid_0)) begin
        _df_data_0 <= d0 + d1;
      end 
      if(_df_valid_0 && _df_ready_0) begin
        _df_valid_0 <= 0;
      end 
      if(r0 && r1 && (_df_ready_0 || !_df_valid_0)) begin
        _df_valid_0 <= v0 && v1;
      end 
      if(v2 && r2 && (_df_ready_1 || !_df_valid_1)) begin
        _df_data_1 <= d2;
      end 
      if(_df_valid_1 && _df_ready_1) begin
        _df_valid_1 <= 0;
      end 
      if(r2 && (_df_ready_1 || !_df_valid_1)) begin
        _df_valid_1 <= v2;
      end 
      if(_df_valid_0 && _df_valid_1 && (_df_ready_0 && _df_ready_1) && (_df_ready_2 || !_df_valid_2)) begin
        _df_data_2 <= _df_data_0 + _df_data_1;
      end 
      if(_df_valid_2 && _df_ready_2) begin
        _df_valid_2 <= 0;
      end 
      if(_df_ready_0 && _df_ready_1 && (_df_ready_2 || !_df_valid_2)) begin
        _df_valid_2 <= _df_valid_0 && _df_valid_1;
      end 
      if(v3 && r3 && (_df_ready_3 || !_df_valid_3)) begin
        _df_data_3 <= d3;
      end 
      if(_df_valid_3 && _df_ready_3) begin
        _df_valid_3 <= 0;
      end 
      if(r3 && (_df_ready_3 || !_df_valid_3)) begin
        _df_valid_3 <= v3;
      end 
      if(_df_valid_3 && _df_ready_3 && (_df_ready_4 || !_df_valid_4)) begin
        _df_data_4 <= _df_data_3;
      end 
      if(_df_valid_4 && _df_ready_4) begin
        _df_valid_4 <= 0;
      end 
      if(_df_ready_3 && (_df_ready_4 || !_df_valid_4)) begin
        _df_valid_4 <= _df_valid_3;
      end 
      if(_df_valid_2 && _df_valid_4 && (_df_ready_2 && _df_ready_4) && (_df_ready_5 || !_df_valid_5)) begin
        _df_data_5 <= _df_data_2 + _df_data_4;
      end 
      if(_df_valid_5 && _df_ready_5) begin
        _df_valid_5 <= 0;
      end 
      if(_df_ready_2 && _df_ready_4 && (_df_ready_5 || !_df_valid_5)) begin
        _df_valid_5 <= _df_valid_2 && _df_valid_4;
      end 
      if(v4 && r4 && (_df_ready_6 || !_df_valid_6)) begin
        _df_data_6 <= d4;
      end 
      if(_df_valid_6 && _df_ready_6) begin
        _df_valid_6 <= 0;
      end 
      if(r4 && (_df_ready_6 || !_df_valid_6)) begin
        _df_valid_6 <= v4;
      end 
      if(_df_valid_6 && _df_ready_6 && (_df_ready_7 || !_df_valid_7)) begin
        _df_data_7 <= _df_data_6;
      end 
      if(_df_valid_7 && _df_ready_7) begin
        _df_valid_7 <= 0;
      end 
      if(_df_ready_6 && (_df_ready_7 || !_df_valid_7)) begin
        _df_valid_7 <= _df_valid_6;
      end 
      if(_df_valid_7 && _df_ready_7 && (_df_ready_8 || !_df_valid_8)) begin
        _df_data_8 <= _df_data_7;
      end 
      if(_df_valid_8 && _df_ready_8) begin
        _df_valid_8 <= 0;
      end 
      if(_df_ready_7 && (_df_ready_8 || !_df_valid_8)) begin
        _df_valid_8 <= _df_valid_7;
      end 
      if(_df_valid_5 && _df_valid_8 && (_df_ready_5 && _df_ready_8) && (_df_ready_9 || !_df_valid_9)) begin
        _df_data_9 <= _df_data_5 + _df_data_8;
      end 
      if(_df_valid_9 && _df_ready_9) begin
        _df_valid_9 <= 0;
      end 
      if(_df_ready_5 && _df_ready_8 && (_df_ready_9 || !_df_valid_9)) begin
        _df_valid_9 <= _df_valid_5 && _df_valid_8;
      end 
      if(v5 && r5 && (_df_ready_10 || !_df_valid_10)) begin
        _df_data_10 <= d5;
      end 
      if(_df_valid_10 && _df_ready_10) begin
        _df_valid_10 <= 0;
      end 
      if(r5 && (_df_ready_10 || !_df_valid_10)) begin
        _df_valid_10 <= v5;
      end 
      if(_df_valid_10 && _df_ready_10 && (_df_ready_11 || !_df_valid_11)) begin
        _df_data_11 <= _df_data_10;
      end 
      if(_df_valid_11 && _df_ready_11) begin
        _df_valid_11 <= 0;
      end 
      if(_df_ready_10 && (_df_ready_11 || !_df_valid_11)) begin
        _df_valid_11 <= _df_valid_10;
      end 
      if(_df_valid_11 && _df_ready_11 && (_df_ready_12 || !_df_valid_12)) begin
        _df_data_12 <= _df_data_11;
      end 
      if(_df_valid_12 && _df_ready_12) begin
        _df_valid_12 <= 0;
      end 
      if(_df_ready_11 && (_df_ready_12 || !_df_valid_12)) begin
        _df_valid_12 <= _df_valid_11;
      end 
      if(_df_valid_12 && _df_ready_12 && (_df_ready_13 || !_df_valid_13)) begin
        _df_data_13 <= _df_data_12;
      end 
      if(_df_valid_13 && _df_ready_13) begin
        _df_valid_13 <= 0;
      end 
      if(_df_ready_12 && (_df_ready_13 || !_df_valid_13)) begin
        _df_valid_13 <= _df_valid_12;
      end 
      if(_df_valid_9 && _df_valid_13 && (_df_ready_9 && _df_ready_13) && (_df_ready_14 || !_df_valid_14)) begin
        _df_data_14 <= _df_data_9 + _df_data_13;
      end 
      if(_df_valid_14 && _df_ready_14) begin
        _df_valid_14 <= 0;
      end 
      if(_df_ready_9 && _df_ready_13 && (_df_ready_14 || !_df_valid_14)) begin
        _df_valid_14 <= _df_valid_9 && _df_valid_13;
      end 
      if(v6 && r6 && (_df_ready_15 || !_df_valid_15)) begin
        _df_data_15 <= d6;
      end 
      if(_df_valid_15 && _df_ready_15) begin
        _df_valid_15 <= 0;
      end 
      if(r6 && (_df_ready_15 || !_df_valid_15)) begin
        _df_valid_15 <= v6;
      end 
      if(_df_valid_15 && _df_ready_15 && (_df_ready_16 || !_df_valid_16)) begin
        _df_data_16 <= _df_data_15;
      end 
      if(_df_valid_16 && _df_ready_16) begin
        _df_valid_16 <= 0;
      end 
      if(_df_ready_15 && (_df_ready_16 || !_df_valid_16)) begin
        _df_valid_16 <= _df_valid_15;
      end 
      if(_df_valid_16 && _df_ready_16 && (_df_ready_17 || !_df_valid_17)) begin
        _df_data_17 <= _df_data_16;
      end 
      if(_df_valid_17 && _df_ready_17) begin
        _df_valid_17 <= 0;
      end 
      if(_df_ready_16 && (_df_ready_17 || !_df_valid_17)) begin
        _df_valid_17 <= _df_valid_16;
      end 
      if(_df_valid_17 && _df_ready_17 && (_df_ready_18 || !_df_valid_18)) begin
        _df_data_18 <= _df_data_17;
      end 
      if(_df_valid_18 && _df_ready_18) begin
        _df_valid_18 <= 0;
      end 
      if(_df_ready_17 && (_df_ready_18 || !_df_valid_18)) begin
        _df_valid_18 <= _df_valid_17;
      end 
      if(_df_valid_18 && _df_ready_18 && (_df_ready_19 || !_df_valid_19)) begin
        _df_data_19 <= _df_data_18;
      end 
      if(_df_valid_19 && _df_ready_19) begin
        _df_valid_19 <= 0;
      end 
      if(_df_ready_18 && (_df_ready_19 || !_df_valid_19)) begin
        _df_valid_19 <= _df_valid_18;
      end 
      if(_df_valid_14 && _df_valid_19 && (_df_ready_14 && _df_ready_19) && (_df_ready_20 || !_df_valid_20)) begin
        _df_data_20 <= _df_data_14 + _df_data_19;
      end 
      if(_df_valid_20 && _df_ready_20) begin
        _df_valid_20 <= 0;
      end 
      if(_df_ready_14 && _df_ready_19 && (_df_ready_20 || !_df_valid_20)) begin
        _df_valid_20 <= _df_valid_14 && _df_valid_19;
      end 
      if(v7 && r7 && (_df_ready_21 || !_df_valid_21)) begin
        _df_data_21 <= d7;
      end 
      if(_df_valid_21 && _df_ready_21) begin
        _df_valid_21 <= 0;
      end 
      if(r7 && (_df_ready_21 || !_df_valid_21)) begin
        _df_valid_21 <= v7;
      end 
      if(_df_valid_21 && _df_ready_21 && (_df_ready_22 || !_df_valid_22)) begin
        _df_data_22 <= _df_data_21;
      end 
      if(_df_valid_22 && _df_ready_22) begin
        _df_valid_22 <= 0;
      end 
      if(_df_ready_21 && (_df_ready_22 || !_df_valid_22)) begin
        _df_valid_22 <= _df_valid_21;
      end 
      if(_df_valid_22 && _df_ready_22 && (_df_ready_23 || !_df_valid_23)) begin
        _df_data_23 <= _df_data_22;
      end 
      if(_df_valid_23 && _df_ready_23) begin
        _df_valid_23 <= 0;
      end 
      if(_df_ready_22 && (_df_ready_23 || !_df_valid_23)) begin
        _df_valid_23 <= _df_valid_22;
      end 
      if(_df_valid_23 && _df_ready_23 && (_df_ready_24 || !_df_valid_24)) begin
        _df_data_24 <= _df_data_23;
      end 
      if(_df_valid_24 && _df_ready_24) begin
        _df_valid_24 <= 0;
      end 
      if(_df_ready_23 && (_df_ready_24 || !_df_valid_24)) begin
        _df_valid_24 <= _df_valid_23;
      end 
      if(_df_valid_24 && _df_ready_24 && (_df_ready_25 || !_df_valid_25)) begin
        _df_data_25 <= _df_data_24;
      end 
      if(_df_valid_25 && _df_ready_25) begin
        _df_valid_25 <= 0;
      end 
      if(_df_ready_24 && (_df_ready_25 || !_df_valid_25)) begin
        _df_valid_25 <= _df_valid_24;
      end 
      if(_df_valid_25 && _df_ready_25 && (_df_ready_26 || !_df_valid_26)) begin
        _df_data_26 <= _df_data_25;
      end 
      if(_df_valid_26 && _df_ready_26) begin
        _df_valid_26 <= 0;
      end 
      if(_df_ready_25 && (_df_ready_26 || !_df_valid_26)) begin
        _df_valid_26 <= _df_valid_25;
      end 
      if(_df_valid_20 && _df_valid_26 && (_df_ready_20 && _df_ready_26) && (_df_ready_27 || !_df_valid_27)) begin
        _df_data_27 <= _df_data_20 + _df_data_26;
      end 
      if(_df_valid_27 && _df_ready_27) begin
        _df_valid_27 <= 0;
      end 
      if(_df_ready_20 && _df_ready_26 && (_df_ready_27 || !_df_valid_27)) begin
        _df_valid_27 <= _df_valid_20 && _df_valid_26;
      end 
    end
  end


endmodule
"""

expected_rslt = """\
VCD info: dumpfile uut.vcd opened for output.
d0=         0
d1=         0
d2=         0
d3=         0
d4=         0
d5=         0
d6=         0
d7=         0
d0=         1
d1=         2
d2=         3
d3=         4
d4=         5
d5=         6
d6=         7
d7=         8
d0=         2
d1=         4
d2=         6
d3=         8
d4=        10
d5=        12
d6=        14
d7=        16
d0=         3
d1=         6
d2=         9
d3=        12
d4=        15
d5=        18
d6=        21
d7=        24
d0=         4
d1=         8
d2=        12
d3=        16
d4=        20
d5=        24
d6=        28
d7=        32
d0=         5
d1=        10
d2=        15
d3=        20
d4=        25
d5=        30
d6=        35
d7=        40
d0=         6
d1=        12
d2=        18
d3=        24
d4=        30
d5=        36
d6=        42
d7=        48
d0=         7
d1=        14
d2=        21
d3=        28
d4=        35
d5=        42
d6=        49
d7=        56
dz=         0
d0=         8
d1=        16
d2=        24
d3=        32
d4=        40
d5=        48
d6=        56
d7=        64
dz=        36
d0=         9
d1=        18
d2=        27
d3=        36
d4=        45
d5=        54
d6=        63
d7=        72
dz=        72
d0=        10
d1=        20
d2=        30
d3=        40
d4=        50
d5=        60
d6=        70
d7=        80
dz=       108
dz=       144
dz=       180
dz=       216
dz=       252
dz=       288
dz=       324
dz=       360
"""

def test():
    veriloggen.reset()
    test_module = pipeline_multiple_add.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)

    sim = simulation.Simulator(test_module)
    rslt = sim.run()

    assert(expected_rslt == rslt)
