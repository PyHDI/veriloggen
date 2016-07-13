from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import uart

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [8-1:0] din;
  reg enable;
  wire ready;
  wire txd;
  wire [8-1:0] dout;
  wire valid;
  wire rxd;
  assign rxd = txd;
  reg [32-1:0] txfsm;
  localparam txfsm_init = 0;
  reg [32-1:0] _tmp_0;
  localparam txfsm_1 = 1;
  localparam txfsm_2 = 2;
  localparam txfsm_3 = 3;
  localparam txfsm_4 = 4;
  localparam txfsm_5 = 5;
  localparam txfsm_6 = 6;
  localparam txfsm_7 = 7;
  localparam txfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      txfsm <= txfsm_init;
    end else begin
      case(txfsm)
        txfsm_init: begin
          if(ready) begin
            din <= 85;
            enable <= 1;
          end 
          if(ready) begin
            txfsm <= txfsm_1;
          end 
        end
        txfsm_1: begin
          enable <= 0;
          txfsm <= txfsm_2;
        end
        txfsm_2: begin
          if(ready) begin
            din <= 51;
            enable <= 1;
          end 
          if(ready) begin
            txfsm <= txfsm_3;
          end 
        end
        txfsm_3: begin
          enable <= 0;
          txfsm <= txfsm_4;
        end
        txfsm_4: begin
          if(ready) begin
            din <= 0;
            enable <= 1;
          end 
          if(ready) begin
            txfsm <= txfsm_5;
          end 
        end
        txfsm_5: begin
          enable <= 0;
          txfsm <= txfsm_6;
        end
        txfsm_6: begin
          if(ready) begin
            din <= 255;
            enable <= 1;
          end 
          if(ready) begin
            txfsm <= txfsm_7;
          end 
        end
        txfsm_7: begin
          enable <= 0;
          txfsm <= txfsm_8;
        end
      endcase
    end
  end

  reg [32-1:0] rxfsm;
  localparam rxfsm_init = 0;
  localparam rxfsm_1 = 1;
  localparam rxfsm_2 = 2;
  localparam rxfsm_3 = 3;
  localparam rxfsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      rxfsm <= rxfsm_init;
    end else begin
      case(rxfsm)
        rxfsm_init: begin
          if(valid) begin
            $display("din=%02x dout=%02x %s", 8'd85, dout, ((dout == 85)? "OK" : "NG"));
          end 
          if(valid) begin
            rxfsm <= rxfsm_1;
          end 
        end
        rxfsm_1: begin
          if(valid) begin
            $display("din=%02x dout=%02x %s", 8'd51, dout, ((dout == 51)? "OK" : "NG"));
          end 
          if(valid) begin
            rxfsm <= rxfsm_2;
          end 
        end
        rxfsm_2: begin
          if(valid) begin
            $display("din=%02x dout=%02x %s", 8'd0, dout, ((dout == 0)? "OK" : "NG"));
          end 
          if(valid) begin
            rxfsm <= rxfsm_3;
          end 
        end
        rxfsm_3: begin
          if(valid) begin
            $display("din=%02x dout=%02x %s", 8'd255, dout, ((dout == 255)? "OK" : "NG"));
          end 
          if(valid) begin
            rxfsm <= rxfsm_4;
          end 
        end
      endcase
    end
  end


  UartTx
  mtx
  (
    .CLK(CLK),
    .RST(RST),
    .din(din),
    .enable(enable),
    .ready(ready),
    .txd(txd)
  );


  UartRx
  mrx
  (
    .CLK(CLK),
    .RST(RST),
    .rxd(rxd),
    .dout(dout),
    .valid(valid)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, mtx, mrx, CLK, RST, din, enable, ready, txd, dout, valid, rxd, txfsm, _tmp_0, rxfsm);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    txfsm = txfsm_init;
    _tmp_0 = 0;
    rxfsm = rxfsm_init;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
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
"""

def test():
    veriloggen.reset()
    test_module = uart.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
