from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_uart_nexys4

expected_verilog = """
module test;

  reg uut_CLK;
  reg uut_RST;
  reg [16-1:0] uut_sw;
  wire [16-1:0] uut_led;
  wire uut_utx;
  wire uut_urx;

  blinkled
  uut
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .sw(uut_sw),
    .led(uut_led),
    .utx(uut_utx),
    .urx(uut_urx)
  );

  reg [8-1:0] tx_din;
  reg tx_enable;
  wire tx_ready;
  wire tx_txd;

  UartTx_
  inst_tx
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .din(tx_din),
    .enable(tx_enable),
    .ready(tx_ready),
    .txd(tx_txd)
  );

  wire [8-1:0] rx_dout;
  wire rx_valid;
  wire rx_rxd;

  UartRx_
  inst_rx
  (
    .CLK(uut_CLK),
    .RST(uut_RST),
    .rxd(rx_rxd),
    .dout(rx_dout),
    .valid(rx_valid)
  );

  assign uut_urx = tx_txd;
  assign rx_rxd = uut_utx;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, inst_tx, inst_rx);
  end


  initial begin
    uut_CLK = 0;
    forever begin
      #5 uut_CLK = !uut_CLK;
    end
  end


  initial begin
    uut_RST = 0;
    tx_enable = 0;
    #100;
    uut_RST = 1;
    #100;
    uut_RST = 0;
    uut_sw = 10;
    #100000;
    $finish;
  end

  reg [32-1:0] test;
  localparam test_init = 0;
  reg signed [32-1:0] _test_i_2;
  reg signed [32-1:0] _test_s_3;
  reg [8-1:0] _tmp_0;
  reg signed [32-1:0] _test_r_4;
  localparam test_1 = 1;
  localparam test_2 = 2;
  localparam test_3 = 3;
  localparam test_4 = 4;
  localparam test_5 = 5;
  localparam test_6 = 6;
  localparam test_7 = 7;
  localparam test_8 = 8;
  localparam test_9 = 9;
  localparam test_10 = 10;
  localparam test_11 = 11;
  localparam test_12 = 12;
  localparam test_13 = 13;
  localparam test_14 = 14;

  always @(posedge uut_CLK) begin
    if(uut_RST) begin
      test <= test_init;
      _test_i_2 <= 0;
      _test_s_3 <= 0;
      tx_enable <= 0;
      _test_r_4 <= 0;
    end else begin
      case(test)
        test_init: begin
          test <= test_1;
        end
        test_1: begin
          _test_i_2 <= 0;
          test <= test_2;
        end
        test_2: begin
          if(_test_i_2 < 10) begin
            test <= test_3;
          end else begin
            test <= test_14;
          end
        end
        test_3: begin
          _test_s_3 <= 100 + _test_i_2;
          test <= test_4;
        end
        test_4: begin
          tx_din <= _test_s_3;
          tx_enable <= 1;
          test <= test_5;
        end
        test_5: begin
          tx_enable <= 0;
          test <= test_6;
        end
        test_6: begin
          if(tx_ready) begin
            test <= test_7;
          end 
        end
        test_7: begin
          if(rx_valid) begin
            _tmp_0 <= rx_dout;
          end 
          if(rx_valid) begin
            test <= test_8;
          end 
        end
        test_8: begin
          _test_r_4 <= _tmp_0;
          test <= test_9;
        end
        test_9: begin
          if(_test_r_4 == _test_s_3 + uut_sw) begin
            test <= test_10;
          end else begin
            test <= test_12;
          end
        end
        test_10: begin
          $display("OK: %d + %d == %d", _test_s_3, uut_sw, _test_r_4);
          test <= test_11;
        end
        test_11: begin
          test <= test_13;
        end
        test_12: begin
          $display("NG: %d + %d != %d", _test_s_3, uut_sw, _test_r_4);
          test <= test_13;
        end
        test_13: begin
          _test_i_2 <= _test_i_2 + 1;
          test <= test_2;
        end
      endcase
    end
  end


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
  reg signed [32-1:0] _th_blink_c_0;
  reg signed [32-1:0] _th_blink_data_1;
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
      _th_blink_c_0 <= 0;
      _th_blink_data_1 <= 0;
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
          _th_blink_c_0 <= _tmp_0;
          th_blink <= th_blink_4;
        end
        th_blink_4: begin
          _th_blink_data_1 <= _th_blink_c_0 + sw;
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          led <= _th_blink_data_1;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          tx_din <= _th_blink_data_1;
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
  reg [4-1:0] _tmp_1;
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
          _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
  reg [4-1:0] _tmp_1;
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
          _tmp_1 <= 4;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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



module UartTx_
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
  reg [4-1:0] _tmp_1;
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
          _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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



module UartRx_
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
  reg [4-1:0] _tmp_1;
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
          _tmp_1 <= 4;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
            _tmp_1 <= 9;
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
"""


def test():
    veriloggen.reset()
    test_module = thread_uart_nexys4.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
