from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import stream_div_validready

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg ivalid;
  wire iready;
  wire ovalid;
  reg oready;
  reg signed [32-1:0] xdata;
  reg signed [32-1:0] ydata;
  wire signed [32-1:0] zdata;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .ivalid(ivalid),
    .iready(iready),
    .ovalid(ovalid),
    .oready(oready),
    .xdata(xdata),
    .ydata(ydata),
    .zdata(zdata)
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
    xdata = 0;
    ydata = 0;
    ivalid = 0;
    oready = 0;
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
  reg [32-1:0] send_count;
  reg [32-1:0] recv_fsm;
  localparam recv_fsm_init = 0;
  reg [32-1:0] recv_count;
  localparam send_fsm_1 = 1;
  localparam send_fsm_2 = 2;
  localparam send_fsm_3 = 3;
  localparam send_fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      send_fsm <= send_fsm_init;
      send_count <= 0;
    end else begin
      case(send_fsm)
        send_fsm_init: begin
          if(reset_done) begin
            send_fsm <= send_fsm_1;
          end 
        end
        send_fsm_1: begin
          ivalid <= 0;
          send_count <= send_count + 1;
          if(send_count == 10) begin
            send_count <= 0;
          end 
          if(send_count == 10) begin
            send_fsm <= send_fsm_2;
          end 
        end
        send_fsm_2: begin
          xdata <= 128;
          ydata <= 1;
          ivalid <= 1;
          send_count <= send_count + 1;
          send_fsm <= send_fsm_3;
        end
        send_fsm_3: begin
          if(iready) begin
            xdata <= xdata;
            ydata <= ydata + 1;
            ivalid <= 1;
            $display("xdata=%d", xdata);
            $display("ydata=%d", ydata);
            send_count <= send_count + 1;
          end 
          if(iready && (send_count == 20)) begin
            ivalid <= 0;
          end 
          if(iready && (send_count == 20)) begin
            send_fsm <= send_fsm_4;
          end 
        end
      endcase
    end
  end

  localparam recv_fsm_1 = 1;
  localparam recv_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      recv_fsm <= recv_fsm_init;
      recv_count <= 0;
    end else begin
      case(recv_fsm)
        recv_fsm_init: begin
          if(reset_done) begin
            recv_fsm <= recv_fsm_1;
          end 
        end
        recv_fsm_1: begin
          recv_count <= recv_count + 1;
          if(recv_count == 20) begin
            recv_count <= 0;
          end 
          if(recv_count == 20) begin
            recv_fsm <= recv_fsm_2;
          end 
        end
        recv_fsm_2: begin
          oready <= !oready;
          if(ovalid && oready) begin
            $display("zdata=%d", zdata);
            recv_count <= recv_count + 1;
          end 
        end
      endcase
    end
  end


endmodule



module main
(
  input CLK,
  input RST,
  input ivalid,
  output iready,
  output ovalid,
  input oready,
  input signed [32-1:0] xdata,
  input signed [32-1:0] ydata,
  output signed [32-1:0] zdata
);

  reg _ivalid_1;
  reg _ivalid_2;
  reg _ivalid_3;
  reg _ivalid_4;
  reg _ivalid_5;
  reg _ivalid_6;
  reg _ivalid_7;
  reg _ivalid_8;
  reg _ivalid_9;
  reg _ivalid_10;
  reg _ivalid_11;
  reg _ivalid_12;
  reg _ivalid_13;
  reg _ivalid_14;
  reg _ivalid_15;
  reg _ivalid_16;
  reg _ivalid_17;
  reg _ivalid_18;
  reg _ivalid_19;
  reg _ivalid_20;
  reg _ivalid_21;
  reg _ivalid_22;
  reg _ivalid_23;
  reg _ivalid_24;
  reg _ivalid_25;
  reg _ivalid_26;
  reg _ivalid_27;
  reg _ivalid_28;
  reg _ivalid_29;
  reg _ivalid_30;
  reg _ivalid_31;
  reg _ivalid_32;
  reg _ivalid_33;
  reg _ivalid_34;
  reg _ivalid_35;
  reg _ivalid_36;
  reg _ivalid_37;
  assign ovalid = _ivalid_37;
  assign iready = oready;
  reg signed [32-1:0] _divide_div_ldata_2;
  reg signed [32-1:0] _divide_div_rdata_2;
  reg [32-1:0] _divide_div_abs_ldata_2;
  reg [32-1:0] _divide_div_abs_rdata_2;
  wire _divide_div_osign_2;
  wire signed [32-1:0] _divide_div_abs_odata_2;
  reg signed [32-1:0] _divide_div_odata_2;
  wire signed [32-1:0] _divide_data_2;
  assign _divide_data_2 = _divide_div_odata_2;
  reg _divide_div_sign_tmp_0_2;
  reg _divide_div_sign_tmp_1_2;
  reg _divide_div_sign_tmp_2_2;
  reg _divide_div_sign_tmp_3_2;
  reg _divide_div_sign_tmp_4_2;
  reg _divide_div_sign_tmp_5_2;
  reg _divide_div_sign_tmp_6_2;
  reg _divide_div_sign_tmp_7_2;
  reg _divide_div_sign_tmp_8_2;
  reg _divide_div_sign_tmp_9_2;
  reg _divide_div_sign_tmp_10_2;
  reg _divide_div_sign_tmp_11_2;
  reg _divide_div_sign_tmp_12_2;
  reg _divide_div_sign_tmp_13_2;
  reg _divide_div_sign_tmp_14_2;
  reg _divide_div_sign_tmp_15_2;
  reg _divide_div_sign_tmp_16_2;
  reg _divide_div_sign_tmp_17_2;
  reg _divide_div_sign_tmp_18_2;
  reg _divide_div_sign_tmp_19_2;
  reg _divide_div_sign_tmp_20_2;
  reg _divide_div_sign_tmp_21_2;
  reg _divide_div_sign_tmp_22_2;
  reg _divide_div_sign_tmp_23_2;
  reg _divide_div_sign_tmp_24_2;
  reg _divide_div_sign_tmp_25_2;
  reg _divide_div_sign_tmp_26_2;
  reg _divide_div_sign_tmp_27_2;
  reg _divide_div_sign_tmp_28_2;
  reg _divide_div_sign_tmp_29_2;
  reg _divide_div_sign_tmp_30_2;
  reg _divide_div_sign_tmp_31_2;
  reg _divide_div_sign_tmp_32_2;
  reg _divide_div_sign_tmp_33_2;
  reg _divide_div_sign_tmp_34_2;
  assign _divide_div_osign_2 = _divide_div_sign_tmp_34_2;
  wire _divide_div_update_2;
  assign _divide_div_update_2 = oready;

  Divider
  #(
    .W_D(32)
  )
  _divide_div_2
  (
    .CLK(CLK),
    .RST(RST),
    .update(_divide_div_update_2),
    .enable(1'd1),
    .in_a(_divide_div_abs_ldata_2),
    .in_b(_divide_div_abs_rdata_2),
    .rslt(_divide_div_abs_odata_2)
  );

  assign zdata = _divide_data_2;

  always @(posedge CLK) begin
    if(RST) begin
      _ivalid_1 <= 0;
      _ivalid_2 <= 0;
      _ivalid_3 <= 0;
      _ivalid_4 <= 0;
      _ivalid_5 <= 0;
      _ivalid_6 <= 0;
      _ivalid_7 <= 0;
      _ivalid_8 <= 0;
      _ivalid_9 <= 0;
      _ivalid_10 <= 0;
      _ivalid_11 <= 0;
      _ivalid_12 <= 0;
      _ivalid_13 <= 0;
      _ivalid_14 <= 0;
      _ivalid_15 <= 0;
      _ivalid_16 <= 0;
      _ivalid_17 <= 0;
      _ivalid_18 <= 0;
      _ivalid_19 <= 0;
      _ivalid_20 <= 0;
      _ivalid_21 <= 0;
      _ivalid_22 <= 0;
      _ivalid_23 <= 0;
      _ivalid_24 <= 0;
      _ivalid_25 <= 0;
      _ivalid_26 <= 0;
      _ivalid_27 <= 0;
      _ivalid_28 <= 0;
      _ivalid_29 <= 0;
      _ivalid_30 <= 0;
      _ivalid_31 <= 0;
      _ivalid_32 <= 0;
      _ivalid_33 <= 0;
      _ivalid_34 <= 0;
      _ivalid_35 <= 0;
      _ivalid_36 <= 0;
      _ivalid_37 <= 0;
      _divide_div_ldata_2 <= 0;
      _divide_div_rdata_2 <= 0;
      _divide_div_abs_ldata_2 <= 0;
      _divide_div_abs_rdata_2 <= 0;
      _divide_div_odata_2 <= 0;
      _divide_div_sign_tmp_0_2 <= 0;
      _divide_div_sign_tmp_1_2 <= 0;
      _divide_div_sign_tmp_2_2 <= 0;
      _divide_div_sign_tmp_3_2 <= 0;
      _divide_div_sign_tmp_4_2 <= 0;
      _divide_div_sign_tmp_5_2 <= 0;
      _divide_div_sign_tmp_6_2 <= 0;
      _divide_div_sign_tmp_7_2 <= 0;
      _divide_div_sign_tmp_8_2 <= 0;
      _divide_div_sign_tmp_9_2 <= 0;
      _divide_div_sign_tmp_10_2 <= 0;
      _divide_div_sign_tmp_11_2 <= 0;
      _divide_div_sign_tmp_12_2 <= 0;
      _divide_div_sign_tmp_13_2 <= 0;
      _divide_div_sign_tmp_14_2 <= 0;
      _divide_div_sign_tmp_15_2 <= 0;
      _divide_div_sign_tmp_16_2 <= 0;
      _divide_div_sign_tmp_17_2 <= 0;
      _divide_div_sign_tmp_18_2 <= 0;
      _divide_div_sign_tmp_19_2 <= 0;
      _divide_div_sign_tmp_20_2 <= 0;
      _divide_div_sign_tmp_21_2 <= 0;
      _divide_div_sign_tmp_22_2 <= 0;
      _divide_div_sign_tmp_23_2 <= 0;
      _divide_div_sign_tmp_24_2 <= 0;
      _divide_div_sign_tmp_25_2 <= 0;
      _divide_div_sign_tmp_26_2 <= 0;
      _divide_div_sign_tmp_27_2 <= 0;
      _divide_div_sign_tmp_28_2 <= 0;
      _divide_div_sign_tmp_29_2 <= 0;
      _divide_div_sign_tmp_30_2 <= 0;
      _divide_div_sign_tmp_31_2 <= 0;
      _divide_div_sign_tmp_32_2 <= 0;
      _divide_div_sign_tmp_33_2 <= 0;
      _divide_div_sign_tmp_34_2 <= 0;
    end else begin
      if(oready) begin
        _ivalid_1 <= ivalid;
      end 
      if(oready) begin
        _ivalid_2 <= _ivalid_1;
      end 
      if(oready) begin
        _ivalid_3 <= _ivalid_2;
      end 
      if(oready) begin
        _ivalid_4 <= _ivalid_3;
      end 
      if(oready) begin
        _ivalid_5 <= _ivalid_4;
      end 
      if(oready) begin
        _ivalid_6 <= _ivalid_5;
      end 
      if(oready) begin
        _ivalid_7 <= _ivalid_6;
      end 
      if(oready) begin
        _ivalid_8 <= _ivalid_7;
      end 
      if(oready) begin
        _ivalid_9 <= _ivalid_8;
      end 
      if(oready) begin
        _ivalid_10 <= _ivalid_9;
      end 
      if(oready) begin
        _ivalid_11 <= _ivalid_10;
      end 
      if(oready) begin
        _ivalid_12 <= _ivalid_11;
      end 
      if(oready) begin
        _ivalid_13 <= _ivalid_12;
      end 
      if(oready) begin
        _ivalid_14 <= _ivalid_13;
      end 
      if(oready) begin
        _ivalid_15 <= _ivalid_14;
      end 
      if(oready) begin
        _ivalid_16 <= _ivalid_15;
      end 
      if(oready) begin
        _ivalid_17 <= _ivalid_16;
      end 
      if(oready) begin
        _ivalid_18 <= _ivalid_17;
      end 
      if(oready) begin
        _ivalid_19 <= _ivalid_18;
      end 
      if(oready) begin
        _ivalid_20 <= _ivalid_19;
      end 
      if(oready) begin
        _ivalid_21 <= _ivalid_20;
      end 
      if(oready) begin
        _ivalid_22 <= _ivalid_21;
      end 
      if(oready) begin
        _ivalid_23 <= _ivalid_22;
      end 
      if(oready) begin
        _ivalid_24 <= _ivalid_23;
      end 
      if(oready) begin
        _ivalid_25 <= _ivalid_24;
      end 
      if(oready) begin
        _ivalid_26 <= _ivalid_25;
      end 
      if(oready) begin
        _ivalid_27 <= _ivalid_26;
      end 
      if(oready) begin
        _ivalid_28 <= _ivalid_27;
      end 
      if(oready) begin
        _ivalid_29 <= _ivalid_28;
      end 
      if(oready) begin
        _ivalid_30 <= _ivalid_29;
      end 
      if(oready) begin
        _ivalid_31 <= _ivalid_30;
      end 
      if(oready) begin
        _ivalid_32 <= _ivalid_31;
      end 
      if(oready) begin
        _ivalid_33 <= _ivalid_32;
      end 
      if(oready) begin
        _ivalid_34 <= _ivalid_33;
      end 
      if(oready) begin
        _ivalid_35 <= _ivalid_34;
      end 
      if(oready) begin
        _ivalid_36 <= _ivalid_35;
      end 
      if(oready) begin
        _ivalid_37 <= _ivalid_36;
      end 
      if(oready) begin
        _divide_div_ldata_2 <= xdata;
      end 
      if(oready) begin
        _divide_div_rdata_2 <= ydata;
      end 
      if(oready) begin
        _divide_div_abs_ldata_2 <= (_divide_div_ldata_2[31] == 0)? _divide_div_ldata_2 : ~_divide_div_ldata_2 + 1;
      end 
      if(oready) begin
        _divide_div_abs_rdata_2 <= (_divide_div_rdata_2[31] == 0)? _divide_div_rdata_2 : ~_divide_div_rdata_2 + 1;
      end 
      if(oready) begin
        _divide_div_odata_2 <= (_divide_div_osign_2 == 0)? _divide_div_abs_odata_2 : ~_divide_div_abs_odata_2 + 1;
      end 
      if(oready) begin
        _divide_div_sign_tmp_0_2 <= !((_divide_div_ldata_2[31] == 0) && (_divide_div_rdata_2[31] == 0) || (_divide_div_ldata_2[31] == 1) && (_divide_div_rdata_2[31] == 1));
      end 
      if(oready) begin
        _divide_div_sign_tmp_1_2 <= _divide_div_sign_tmp_0_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_2_2 <= _divide_div_sign_tmp_1_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_3_2 <= _divide_div_sign_tmp_2_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_4_2 <= _divide_div_sign_tmp_3_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_5_2 <= _divide_div_sign_tmp_4_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_6_2 <= _divide_div_sign_tmp_5_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_7_2 <= _divide_div_sign_tmp_6_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_8_2 <= _divide_div_sign_tmp_7_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_9_2 <= _divide_div_sign_tmp_8_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_10_2 <= _divide_div_sign_tmp_9_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_11_2 <= _divide_div_sign_tmp_10_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_12_2 <= _divide_div_sign_tmp_11_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_13_2 <= _divide_div_sign_tmp_12_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_14_2 <= _divide_div_sign_tmp_13_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_15_2 <= _divide_div_sign_tmp_14_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_16_2 <= _divide_div_sign_tmp_15_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_17_2 <= _divide_div_sign_tmp_16_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_18_2 <= _divide_div_sign_tmp_17_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_19_2 <= _divide_div_sign_tmp_18_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_20_2 <= _divide_div_sign_tmp_19_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_21_2 <= _divide_div_sign_tmp_20_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_22_2 <= _divide_div_sign_tmp_21_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_23_2 <= _divide_div_sign_tmp_22_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_24_2 <= _divide_div_sign_tmp_23_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_25_2 <= _divide_div_sign_tmp_24_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_26_2 <= _divide_div_sign_tmp_25_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_27_2 <= _divide_div_sign_tmp_26_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_28_2 <= _divide_div_sign_tmp_27_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_29_2 <= _divide_div_sign_tmp_28_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_30_2 <= _divide_div_sign_tmp_29_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_31_2 <= _divide_div_sign_tmp_30_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_32_2 <= _divide_div_sign_tmp_31_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_33_2 <= _divide_div_sign_tmp_32_2;
      end 
      if(oready) begin
        _divide_div_sign_tmp_34_2 <= _divide_div_sign_tmp_33_2;
      end 
    end
  end


endmodule



module Divider #
(
  parameter W_D = 32
)
(
  input CLK,
  input RST,
  input [W_D-1:0] in_a,
  input [W_D-1:0] in_b,
  input update,
  input enable,
  output reg [W_D-1:0] rslt,
  output reg [W_D-1:0] mod,
  output reg valid
);

  localparam DEPTH = W_D + 1;

  function [0:0] getsign;
    input [W_D-1:0] in;
    begin
      getsign = in[W_D - 1];
    end
  endfunction


  function [0:0] is_positive;
    input [W_D-1:0] in;
    begin
      is_positive = getsign(in) == 0;
    end
  endfunction


  function [W_D-1:0] complement2;
    input [W_D-1:0] in;
    begin
      complement2 = ~in + { { W_D - 1{ 1'b0 } }, 1'b1 };
    end
  endfunction


  function [W_D*2-1:0] complement2_2x;
    input [W_D*2-1:0] in;
    begin
      complement2_2x = ~in + { { W_D * 2 - 1{ 1'b0 } }, 1'b1 };
    end
  endfunction


  function [W_D-1:0] absolute;
    input [W_D-1:0] in;
    begin
      if(getsign(in)) begin
        absolute = complement2(in);
      end else begin
        absolute = in;
      end
    end
  endfunction

  wire [W_D-1:0] abs_in_a;
  wire [W_D-1:0] abs_in_b;
  assign abs_in_a = absolute(in_a);
  assign abs_in_b = absolute(in_b);
  genvar d;

  generate for(d=0; d<DEPTH; d=d+1) begin : s_depth
    reg stage_valid;
    reg in_a_positive;
    reg in_b_positive;
    reg [W_D*2-1:0] dividend;
    reg [W_D*2-1:0] divisor;
    reg [W_D*2-1:0] stage_rslt;
    wire [W_D*2-1:0] sub_value;
    wire is_large;
    assign sub_value = dividend - divisor;
    assign is_large = !sub_value[W_D * 2 - 1];
    if(d == 0) begin

      always @(posedge CLK) begin
        if(RST) begin
          stage_valid <= 0;
          in_a_positive <= 0;
          in_b_positive <= 0;
        end else begin
          if(update) begin
            stage_valid <= enable;
            in_a_positive <= is_positive(in_a);
            in_b_positive <= is_positive(in_b);
          end 
        end
      end

    end else begin

      always @(posedge CLK) begin
        if(RST) begin
          stage_valid <= 0;
          in_a_positive <= 0;
          in_b_positive <= 0;
        end else begin
          if(update) begin
            stage_valid <= s_depth[(d - 1)].stage_valid;
            in_a_positive <= s_depth[(d - 1)].in_a_positive;
            in_b_positive <= s_depth[(d - 1)].in_b_positive;
          end 
        end
      end

    end
    if(d == 0) begin

      always @(posedge CLK) begin
        if(update) begin
          dividend <= abs_in_a;
          divisor <= abs_in_b << W_D - 1;
          stage_rslt <= 0;
        end 
      end

    end else begin

      always @(posedge CLK) begin
        if(update) begin
          dividend <= (s_depth[(d - 1)].is_large)? s_depth[(d - 1)].sub_value : s_depth[(d - 1)].dividend;
          divisor <= s_depth[(d - 1)].divisor >> 1;
          stage_rslt <= { s_depth[(d - 1)].stage_rslt, s_depth[(d - 1)].is_large };
        end 
      end

    end
  end
  endgenerate


  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
    end else begin
      if(update) begin
        valid <= s_depth[(DEPTH - 1)].stage_valid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(update) begin
      rslt <= (s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].stage_rslt : 
              (!s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].stage_rslt) : 
              (s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].stage_rslt) : 
              (!s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].stage_rslt : 'hx;
      mod <= (s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].dividend[W_D-1:0] : 
             (!s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].dividend[W_D-1:0]) : 
             (s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].dividend[W_D-1:0] : 
             (!s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].dividend[W_D-1:0]) : 'hx;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = stream_div_validready.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
