from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_parameter

expected_verilog = """
module test #
(
  parameter xparam = 100,
  parameter signed [32-1:0] aparam = 10
)
(

);

  reg CLK;
  reg RST;

  main
  #(
    .xparam(xparam),
    .aparam(aparam)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


endmodule



module main #
(
  parameter xparam = 100,
  parameter signed [32-1:0] aparam = 10
)
(
  input CLK,
  input RST
);

  reg [32-1:0] yparam;
  wire signed [32-1:0] bparam;
  wire signed [32-1:0] vdata;
  wire signed [32-1:0] wdata;
  reg signed [32-1:0] _plus_data_0;
  reg _plus_valid_0;
  wire _plus_ready_0;
  reg signed [32-1:0] __delay_data_1;
  reg __delay_valid_1;
  wire __delay_ready_1;
  reg signed [32-1:0] _plus_data_2;
  reg _plus_valid_2;
  wire _plus_ready_2;
  assign _plus_ready_0 = (_plus_ready_2 || !_plus_valid_2) && _plus_valid_0;
  reg signed [32-1:0] __delay_data_3;
  reg __delay_valid_3;
  wire __delay_ready_3;
  assign __delay_ready_1 = (__delay_ready_3 || !__delay_valid_3) && __delay_valid_1;
  reg signed [32-1:0] _plus_data_4;
  reg _plus_valid_4;
  wire _plus_ready_4;
  assign _plus_ready_2 = (_plus_ready_4 || !_plus_valid_4) && _plus_valid_2;
  reg signed [32-1:0] __delay_data_5;
  reg __delay_valid_5;
  wire __delay_ready_5;
  assign __delay_ready_3 = (__delay_ready_5 || !__delay_valid_5) && __delay_valid_3;
  reg signed [32-1:0] _plus_data_6;
  reg _plus_valid_6;
  wire _plus_ready_6;
  assign _plus_ready_4 = (_plus_ready_6 || !_plus_valid_6) && _plus_valid_4;
  reg signed [32-1:0] __delay_data_7;
  reg __delay_valid_7;
  wire __delay_ready_7;
  assign __delay_ready_5 = (__delay_ready_7 || !__delay_valid_7) && __delay_valid_5;
  reg signed [32-1:0] _plus_data_8;
  reg _plus_valid_8;
  wire _plus_ready_8;
  assign _plus_ready_6 = (_plus_ready_8 || !_plus_valid_8) && _plus_valid_6;
  reg signed [32-1:0] __delay_data_9;
  reg __delay_valid_9;
  wire __delay_ready_9;
  assign __delay_ready_7 = (__delay_ready_9 || !__delay_valid_9) && __delay_valid_7;
  reg signed [32-1:0] _plus_data_10;
  reg _plus_valid_10;
  wire _plus_ready_10;
  assign _plus_ready_8 = (_plus_ready_10 || !_plus_valid_10) && _plus_valid_8;
  reg signed [32-1:0] __delay_data_11;
  reg __delay_valid_11;
  wire __delay_ready_11;
  assign __delay_ready_9 = (__delay_ready_11 || !__delay_valid_11) && __delay_valid_9;
  reg signed [32-1:0] _plus_data_12;
  reg _plus_valid_12;
  wire _plus_ready_12;
  assign _plus_ready_10 = (_plus_ready_12 || !_plus_valid_12) && (_plus_valid_10 && __delay_valid_11);
  assign __delay_ready_11 = (_plus_ready_12 || !_plus_valid_12) && (_plus_valid_10 && __delay_valid_11);
  wire signed [32-1:0] cdata;
  wire cvalid;
  assign cdata = _plus_data_12;
  assign cvalid = _plus_valid_12;
  assign _plus_ready_12 = 1;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_13;
  assign bparam = 20;
  assign vdata = 1000;
  assign wdata = 2000;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      yparam <= 0;
      _tmp_13 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          yparam <= 200;
          fsm <= fsm_1;
        end
        fsm_1: begin
          if(cvalid) begin
            _tmp_13 <= _tmp_13 + 1;
            $display("c=%d", cdata);
          end 
          if(_tmp_13 == 4) begin
            fsm <= fsm_2;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _plus_data_0 <= 0;
      _plus_valid_0 <= 0;
      __delay_data_1 <= 0;
      __delay_valid_1 <= 0;
      _plus_data_2 <= 0;
      _plus_valid_2 <= 0;
      __delay_data_3 <= 0;
      __delay_valid_3 <= 0;
      _plus_data_4 <= 0;
      _plus_valid_4 <= 0;
      __delay_data_5 <= 0;
      __delay_valid_5 <= 0;
      _plus_data_6 <= 0;
      _plus_valid_6 <= 0;
      __delay_data_7 <= 0;
      __delay_valid_7 <= 0;
      _plus_data_8 <= 0;
      _plus_valid_8 <= 0;
      __delay_data_9 <= 0;
      __delay_valid_9 <= 0;
      _plus_data_10 <= 0;
      _plus_valid_10 <= 0;
      __delay_data_11 <= 0;
      __delay_valid_11 <= 0;
      _plus_data_12 <= 0;
      _plus_valid_12 <= 0;
    end else begin
      if((_plus_ready_0 || !_plus_valid_0) && 1 && 1) begin
        _plus_data_0 <= vdata + aparam;
      end 
      if(_plus_valid_0 && _plus_ready_0) begin
        _plus_valid_0 <= 0;
      end 
      if((_plus_ready_0 || !_plus_valid_0) && 1) begin
        _plus_valid_0 <= 1;
      end 
      if((__delay_ready_1 || !__delay_valid_1) && 1 && 1) begin
        __delay_data_1 <= wdata;
      end 
      if(__delay_valid_1 && __delay_ready_1) begin
        __delay_valid_1 <= 0;
      end 
      if((__delay_ready_1 || !__delay_valid_1) && 1) begin
        __delay_valid_1 <= 1;
      end 
      if((_plus_ready_2 || !_plus_valid_2) && _plus_ready_0 && _plus_valid_0) begin
        _plus_data_2 <= _plus_data_0 + bparam;
      end 
      if(_plus_valid_2 && _plus_ready_2) begin
        _plus_valid_2 <= 0;
      end 
      if((_plus_ready_2 || !_plus_valid_2) && _plus_ready_0) begin
        _plus_valid_2 <= _plus_valid_0;
      end 
      if((__delay_ready_3 || !__delay_valid_3) && __delay_ready_1 && __delay_valid_1) begin
        __delay_data_3 <= __delay_data_1;
      end 
      if(__delay_valid_3 && __delay_ready_3) begin
        __delay_valid_3 <= 0;
      end 
      if((__delay_ready_3 || !__delay_valid_3) && __delay_ready_1) begin
        __delay_valid_3 <= __delay_valid_1;
      end 
      if((_plus_ready_4 || !_plus_valid_4) && _plus_ready_2 && _plus_valid_2) begin
        _plus_data_4 <= _plus_data_2 + xparam;
      end 
      if(_plus_valid_4 && _plus_ready_4) begin
        _plus_valid_4 <= 0;
      end 
      if((_plus_ready_4 || !_plus_valid_4) && _plus_ready_2) begin
        _plus_valid_4 <= _plus_valid_2;
      end 
      if((__delay_ready_5 || !__delay_valid_5) && __delay_ready_3 && __delay_valid_3) begin
        __delay_data_5 <= __delay_data_3;
      end 
      if(__delay_valid_5 && __delay_ready_5) begin
        __delay_valid_5 <= 0;
      end 
      if((__delay_ready_5 || !__delay_valid_5) && __delay_ready_3) begin
        __delay_valid_5 <= __delay_valid_3;
      end 
      if((_plus_ready_6 || !_plus_valid_6) && _plus_ready_4 && _plus_valid_4) begin
        _plus_data_6 <= _plus_data_4 + yparam;
      end 
      if(_plus_valid_6 && _plus_ready_6) begin
        _plus_valid_6 <= 0;
      end 
      if((_plus_ready_6 || !_plus_valid_6) && _plus_ready_4) begin
        _plus_valid_6 <= _plus_valid_4;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && __delay_ready_5 && __delay_valid_5) begin
        __delay_data_7 <= __delay_data_5;
      end 
      if(__delay_valid_7 && __delay_ready_7) begin
        __delay_valid_7 <= 0;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && __delay_ready_5) begin
        __delay_valid_7 <= __delay_valid_5;
      end 
      if((_plus_ready_8 || !_plus_valid_8) && _plus_ready_6 && _plus_valid_6) begin
        _plus_data_8 <= _plus_data_6 + 2'sd1;
      end 
      if(_plus_valid_8 && _plus_ready_8) begin
        _plus_valid_8 <= 0;
      end 
      if((_plus_ready_8 || !_plus_valid_8) && _plus_ready_6) begin
        _plus_valid_8 <= _plus_valid_6;
      end 
      if((__delay_ready_9 || !__delay_valid_9) && __delay_ready_7 && __delay_valid_7) begin
        __delay_data_9 <= __delay_data_7;
      end 
      if(__delay_valid_9 && __delay_ready_9) begin
        __delay_valid_9 <= 0;
      end 
      if((__delay_ready_9 || !__delay_valid_9) && __delay_ready_7) begin
        __delay_valid_9 <= __delay_valid_7;
      end 
      if((_plus_ready_10 || !_plus_valid_10) && _plus_ready_8 && _plus_valid_8) begin
        _plus_data_10 <= _plus_data_8 + 32'd30;
      end 
      if(_plus_valid_10 && _plus_ready_10) begin
        _plus_valid_10 <= 0;
      end 
      if((_plus_ready_10 || !_plus_valid_10) && _plus_ready_8) begin
        _plus_valid_10 <= _plus_valid_8;
      end 
      if((__delay_ready_11 || !__delay_valid_11) && __delay_ready_9 && __delay_valid_9) begin
        __delay_data_11 <= __delay_data_9;
      end 
      if(__delay_valid_11 && __delay_ready_11) begin
        __delay_valid_11 <= 0;
      end 
      if((__delay_ready_11 || !__delay_valid_11) && __delay_ready_9) begin
        __delay_valid_11 <= __delay_valid_9;
      end 
      if((_plus_ready_12 || !_plus_valid_12) && (_plus_ready_10 && __delay_ready_11) && (_plus_valid_10 && __delay_valid_11)) begin
        _plus_data_12 <= _plus_data_10 + __delay_data_11;
      end 
      if(_plus_valid_12 && _plus_ready_12) begin
        _plus_valid_12 <= 0;
      end 
      if((_plus_ready_12 || !_plus_valid_12) && (_plus_ready_10 && __delay_ready_11)) begin
        _plus_valid_12 <= _plus_valid_10 && __delay_valid_11;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = dataflow_parameter.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
