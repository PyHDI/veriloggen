

module top
(
  input clk,
  input btnCpuReset,
  input RsRx,
  output RsTx,
  output RsCts,
  input RsRts,
  input [16-1:0] inst_blinkled_sw,
  output [16-1:0] inst_blinkled_led
);

  assign RsCts = 0;
  wire new_CLK;
  assign new_CLK = clk;
  reg RST_X;
  reg RST;

  always @(posedge clk) begin
    RST_X <= btnCpuReset;
    RST <= !RST_X;
  end

  wire inst_blinkled_utx;
  wire inst_blinkled_urx;

  blinkled
  inst_blinkled
  (
    .CLK(new_CLK),
    .RST(RST),
    .sw(inst_blinkled_sw),
    .led(inst_blinkled_led),
    .utx(RsTx),
    .urx(RsRx)
  );


endmodule



module blinkled
(
  input CLK,
  input RST,
  input [16-1:0] sw,
  output reg [16-1:0] led,
  output utx,
  input urx
);

  reg [8-1:0] tx_din;
  reg tx_enable;
  wire tx_ready;

  UartTx
  inst_tx
  (
    .CLK(CLK),
    .RST(RST),
    .din(tx_din),
    .enable(tx_enable),
    .ready(tx_ready),
    .txd(utx)
  );

  wire [8-1:0] rx_dout;
  wire rx_valid;

  UartRx
  inst_rx
  (
    .CLK(CLK),
    .RST(RST),
    .rxd(urx),
    .dout(rx_dout),
    .valid(rx_valid)
  );

  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg [8-1:0] _tmp_0;
  reg signed [32-1:0] _th_blink_c_6;
  reg signed [32-1:0] _th_blink_data_7;
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

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _th_blink_c_6 <= 0;
      _th_blink_data_7 <= 0;
      led <= 0;
      tx_enable <= 0;
    end else begin
      case(th_blink)
        th_blink_init: begin
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          if(1) begin
            th_blink <= th_blink_2;
          end else begin
            th_blink <= th_blink_10;
          end
        end
        th_blink_2: begin
          if(rx_valid) begin
            _tmp_0 <= rx_dout;
          end 
          if(rx_valid) begin
            th_blink <= th_blink_3;
          end 
        end
        th_blink_3: begin
          _th_blink_c_6 <= _tmp_0;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _th_blink_data_7 <= _th_blink_c_6 + sw;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          led <= _th_blink_data_7;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          tx_din <= _th_blink_data_7;
          tx_enable <= 1;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          tx_enable <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(tx_ready) begin
            th_blink <= th_blink_9;
          end 
        end
        th_blink_9: begin
          th_blink <= th_blink_1;
        end
      endcase
    end
  end


endmodule



module UartTx
(
  input CLK,
  input RST,
  input [8-1:0] din,
  input enable,
  output reg ready,
  output reg txd
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg [13-1:0] _tmp_1;
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

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _tmp_1 <= 0;
      txd <= 1;
      _tmp_0 <= 0;
      ready <= 1;
    end else begin
      case(fsm)
        fsm_init: begin
          _tmp_1 <= 5207;
          txd <= 1;
          _tmp_0 <= { din, 1'd0 };
          if(enable) begin
            ready <= 0;
          end 
          if(enable) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_7;
          end 
        end
        fsm_7: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            txd <= _tmp_0[0];
            _tmp_0 <= { 1'd1, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_11;
          end 
        end
        fsm_11: begin
          ready <= 1;
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule



module UartRx
(
  input CLK,
  input RST,
  input rxd,
  output reg [8-1:0] dout,
  output reg valid
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [9-1:0] _tmp_0;
  reg [13-1:0] _tmp_1;
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

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      valid <= 0;
      _tmp_1 <= 0;
      _tmp_0 <= 0;
      dout <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          valid <= 0;
          _tmp_1 <= 2603;
          _tmp_0 <= { rxd, _tmp_0[8:1] };
          if(rxd == 0) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if((_tmp_1 == 1) && (rxd != 0)) begin
            fsm <= fsm_init;
          end 
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_7;
          end 
        end
        fsm_7: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_8;
          end 
        end
        fsm_8: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_9;
          end 
        end
        fsm_9: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_10;
          end 
        end
        fsm_10: begin
          if(_tmp_1 > 0) begin
            _tmp_1 <= _tmp_1 - 1;
          end else begin
            _tmp_0 <= { rxd, _tmp_0[8:1] };
            _tmp_1 <= 5207;
          end
          if(!(_tmp_1 > 0)) begin
            fsm <= fsm_11;
          end 
        end
        fsm_11: begin
          valid <= 1;
          dout <= _tmp_0[8:0];
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule

