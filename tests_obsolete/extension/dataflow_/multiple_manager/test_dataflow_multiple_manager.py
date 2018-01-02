from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_multiple_manager

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST)
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


endmodule



module main
(
  input CLK,
  input RST
);

  reg [32-1:0] _counter_data_0;
  reg _counter_valid_0;
  wire _counter_ready_0;
  reg [32-1:0] _counter_data_1;
  reg _counter_valid_1;
  wire _counter_ready_1;
  reg [32-1:0] _counter_data_2;
  reg _counter_valid_2;
  wire _counter_ready_2;
  reg [32-1:0] _plus_data_3;
  reg _plus_valid_3;
  wire _plus_ready_3;
  reg [32-1:0] _plus_data_4;
  reg _plus_valid_4;
  wire _plus_ready_4;
  reg [32-1:0] _plus_data_5;
  reg _plus_valid_5;
  wire _plus_ready_5;
  reg [32-1:0] __delay_data_6;
  reg __delay_valid_6;
  wire __delay_ready_6;
  assign _counter_ready_2 = (_plus_ready_4 || !_plus_valid_4) && (_counter_valid_1 && _counter_valid_2) && ((_plus_ready_5 || !_plus_valid_5) && (_counter_valid_2 && _counter_valid_0)) && ((__delay_ready_6 || !__delay_valid_6) && _counter_valid_2);
  reg [32-1:0] __delay_data_7;
  reg __delay_valid_7;
  wire __delay_ready_7;
  assign _counter_ready_0 = (_plus_ready_3 || !_plus_valid_3) && (_counter_valid_0 && _counter_valid_1) && ((_plus_ready_5 || !_plus_valid_5) && (_counter_valid_2 && _counter_valid_0)) && ((__delay_ready_7 || !__delay_valid_7) && _counter_valid_0);
  reg [32-1:0] __delay_data_8;
  reg __delay_valid_8;
  wire __delay_ready_8;
  assign _counter_ready_1 = (_plus_ready_3 || !_plus_valid_3) && (_counter_valid_0 && _counter_valid_1) && ((_plus_ready_4 || !_plus_valid_4) && (_counter_valid_1 && _counter_valid_2)) && ((__delay_ready_8 || !__delay_valid_8) && _counter_valid_1);
  reg [32-1:0] _plus_data_9;
  reg _plus_valid_9;
  wire _plus_ready_9;
  assign _plus_ready_3 = (_plus_ready_9 || !_plus_valid_9) && (_plus_valid_3 && __delay_valid_6);
  assign __delay_ready_6 = (_plus_ready_9 || !_plus_valid_9) && (_plus_valid_3 && __delay_valid_6);
  reg [32-1:0] _plus_data_10;
  reg _plus_valid_10;
  wire _plus_ready_10;
  assign _plus_ready_4 = (_plus_ready_10 || !_plus_valid_10) && (_plus_valid_4 && __delay_valid_7);
  assign __delay_ready_7 = (_plus_ready_10 || !_plus_valid_10) && (_plus_valid_4 && __delay_valid_7);
  reg [32-1:0] _plus_data_11;
  reg _plus_valid_11;
  wire _plus_ready_11;
  assign _plus_ready_5 = (_plus_ready_11 || !_plus_valid_11) && (_plus_valid_5 && __delay_valid_8);
  assign __delay_ready_8 = (_plus_ready_11 || !_plus_valid_11) && (_plus_valid_5 && __delay_valid_8);
  wire [32-1:0] adata;
  wire avalid;
  assign adata = _plus_data_9;
  assign avalid = _plus_valid_9;
  assign _plus_ready_9 = 1;
  wire [32-1:0] bdata;
  wire bvalid;
  assign bdata = _plus_data_10;
  assign bvalid = _plus_valid_10;
  assign _plus_ready_10 = 1;
  wire [32-1:0] cdata;
  wire cvalid;
  assign cdata = _plus_data_11;
  assign cvalid = _plus_valid_11;
  assign _plus_ready_11 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _counter_data_0 <= -2'sd1;
      _counter_valid_0 <= 0;
      _counter_data_1 <= -2'sd1;
      _counter_valid_1 <= 0;
      _counter_data_2 <= -2'sd1;
      _counter_valid_2 <= 0;
      _plus_data_3 <= 0;
      _plus_valid_3 <= 0;
      _plus_data_4 <= 0;
      _plus_valid_4 <= 0;
      _plus_data_5 <= 0;
      _plus_valid_5 <= 0;
      __delay_data_6 <= 0;
      __delay_valid_6 <= 0;
      __delay_data_7 <= 0;
      __delay_valid_7 <= 0;
      __delay_data_8 <= 0;
      __delay_valid_8 <= 0;
      _plus_data_9 <= 0;
      _plus_valid_9 <= 0;
      _plus_data_10 <= 0;
      _plus_valid_10 <= 0;
      _plus_data_11 <= 0;
      _plus_valid_11 <= 0;
    end else begin
      if((_counter_ready_0 || !_counter_valid_0) && 1 && 1) begin
        _counter_data_0 <= _counter_data_0 + 1;
      end 
      if(_counter_valid_0 && _counter_ready_0) begin
        _counter_valid_0 <= 0;
      end 
      if((_counter_ready_0 || !_counter_valid_0) && 1) begin
        _counter_valid_0 <= 1;
      end 
      if((_counter_ready_1 || !_counter_valid_1) && 1 && 1) begin
        _counter_data_1 <= _counter_data_1 + 1;
      end 
      if(_counter_valid_1 && _counter_ready_1) begin
        _counter_valid_1 <= 0;
      end 
      if((_counter_ready_1 || !_counter_valid_1) && 1) begin
        _counter_valid_1 <= 1;
      end 
      if((_counter_ready_2 || !_counter_valid_2) && 1 && 1) begin
        _counter_data_2 <= _counter_data_2 + 1;
      end 
      if(_counter_valid_2 && _counter_ready_2) begin
        _counter_valid_2 <= 0;
      end 
      if((_counter_ready_2 || !_counter_valid_2) && 1) begin
        _counter_valid_2 <= 1;
      end 
      if((_plus_ready_3 || !_plus_valid_3) && (_counter_ready_0 && _counter_ready_1) && (_counter_valid_0 && _counter_valid_1)) begin
        _plus_data_3 <= _counter_data_0 + _counter_data_1;
      end 
      if(_plus_valid_3 && _plus_ready_3) begin
        _plus_valid_3 <= 0;
      end 
      if((_plus_ready_3 || !_plus_valid_3) && (_counter_ready_0 && _counter_ready_1)) begin
        _plus_valid_3 <= _counter_valid_0 && _counter_valid_1;
      end 
      if((_plus_ready_4 || !_plus_valid_4) && (_counter_ready_1 && _counter_ready_2) && (_counter_valid_1 && _counter_valid_2)) begin
        _plus_data_4 <= _counter_data_1 + _counter_data_2;
      end 
      if(_plus_valid_4 && _plus_ready_4) begin
        _plus_valid_4 <= 0;
      end 
      if((_plus_ready_4 || !_plus_valid_4) && (_counter_ready_1 && _counter_ready_2)) begin
        _plus_valid_4 <= _counter_valid_1 && _counter_valid_2;
      end 
      if((_plus_ready_5 || !_plus_valid_5) && (_counter_ready_2 && _counter_ready_0) && (_counter_valid_2 && _counter_valid_0)) begin
        _plus_data_5 <= _counter_data_2 + _counter_data_0;
      end 
      if(_plus_valid_5 && _plus_ready_5) begin
        _plus_valid_5 <= 0;
      end 
      if((_plus_ready_5 || !_plus_valid_5) && (_counter_ready_2 && _counter_ready_0)) begin
        _plus_valid_5 <= _counter_valid_2 && _counter_valid_0;
      end 
      if((__delay_ready_6 || !__delay_valid_6) && _counter_ready_2 && _counter_valid_2) begin
        __delay_data_6 <= _counter_data_2;
      end 
      if(__delay_valid_6 && __delay_ready_6) begin
        __delay_valid_6 <= 0;
      end 
      if((__delay_ready_6 || !__delay_valid_6) && _counter_ready_2) begin
        __delay_valid_6 <= _counter_valid_2;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && _counter_ready_0 && _counter_valid_0) begin
        __delay_data_7 <= _counter_data_0;
      end 
      if(__delay_valid_7 && __delay_ready_7) begin
        __delay_valid_7 <= 0;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && _counter_ready_0) begin
        __delay_valid_7 <= _counter_valid_0;
      end 
      if((__delay_ready_8 || !__delay_valid_8) && _counter_ready_1 && _counter_valid_1) begin
        __delay_data_8 <= _counter_data_1;
      end 
      if(__delay_valid_8 && __delay_ready_8) begin
        __delay_valid_8 <= 0;
      end 
      if((__delay_ready_8 || !__delay_valid_8) && _counter_ready_1) begin
        __delay_valid_8 <= _counter_valid_1;
      end 
      if((_plus_ready_9 || !_plus_valid_9) && (_plus_ready_3 && __delay_ready_6) && (_plus_valid_3 && __delay_valid_6)) begin
        _plus_data_9 <= _plus_data_3 + __delay_data_6;
      end 
      if(_plus_valid_9 && _plus_ready_9) begin
        _plus_valid_9 <= 0;
      end 
      if((_plus_ready_9 || !_plus_valid_9) && (_plus_ready_3 && __delay_ready_6)) begin
        _plus_valid_9 <= _plus_valid_3 && __delay_valid_6;
      end 
      if((_plus_ready_10 || !_plus_valid_10) && (_plus_ready_4 && __delay_ready_7) && (_plus_valid_4 && __delay_valid_7)) begin
        _plus_data_10 <= _plus_data_4 + __delay_data_7;
      end 
      if(_plus_valid_10 && _plus_ready_10) begin
        _plus_valid_10 <= 0;
      end 
      if((_plus_ready_10 || !_plus_valid_10) && (_plus_ready_4 && __delay_ready_7)) begin
        _plus_valid_10 <= _plus_valid_4 && __delay_valid_7;
      end 
      if((_plus_ready_11 || !_plus_valid_11) && (_plus_ready_5 && __delay_ready_8) && (_plus_valid_5 && __delay_valid_8)) begin
        _plus_data_11 <= _plus_data_5 + __delay_data_8;
      end 
      if(_plus_valid_11 && _plus_ready_11) begin
        _plus_valid_11 <= 0;
      end 
      if((_plus_ready_11 || !_plus_valid_11) && (_plus_ready_5 && __delay_ready_8)) begin
        _plus_valid_11 <= _plus_valid_5 && __delay_valid_8;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = dataflow_multiple_manager.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
