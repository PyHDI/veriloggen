from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_counter_enable

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



module main
(
  input CLK,
  input RST
);

  wire [32-1:0] adata;
  wire avalid;
  wire aready;
  assign aready = 1;
  wire [32-1:0] bdata;
  wire bvalid;
  wire bready;
  assign bready = 1;
  wire [32-1:0] cdata;
  wire cvalid;
  wire cready;
  assign cready = 1;
  reg [32-1:0] _counter_data_0;
  reg _counter_valid_0;
  wire _counter_ready_0;
  reg [6-1:0] _counter_count_0;
  reg [1-1:0] _eq_data_1;
  reg _eq_valid_1;
  wire _eq_ready_1;
  reg [1-1:0] _eq_data_2;
  reg _eq_valid_2;
  wire _eq_ready_2;
  reg [1-1:0] _eq_data_3;
  reg _eq_valid_3;
  wire _eq_ready_3;
  reg [32-1:0] __delay_data_4;
  reg __delay_valid_4;
  wire __delay_ready_4;
  assign _counter_ready_0 = (_eq_ready_1 || !_eq_valid_1) && _counter_valid_0 && ((_eq_ready_2 || !_eq_valid_2) && _counter_valid_0) && ((_eq_ready_3 || !_eq_valid_3) && _counter_valid_0) && ((__delay_ready_4 || !__delay_valid_4) && _counter_valid_0);
  reg [32-1:0] _counter_data_5;
  reg _counter_valid_5;
  wire _counter_ready_5;
  assign _eq_ready_1 = (_counter_ready_5 || !_counter_valid_5) && _eq_valid_1;
  reg [1-1:0] _or_data_6;
  reg _or_valid_6;
  wire _or_ready_6;
  assign _eq_ready_2 = (_or_ready_6 || !_or_valid_6) && (_eq_valid_2 && _eq_valid_3);
  assign _eq_ready_3 = (_or_ready_6 || !_or_valid_6) && (_eq_valid_2 && _eq_valid_3);
  reg [32-1:0] __delay_data_7;
  reg __delay_valid_7;
  wire __delay_ready_7;
  assign __delay_ready_4 = (__delay_ready_7 || !__delay_valid_7) && __delay_valid_4;
  reg [32-1:0] _counter_data_8;
  reg _counter_valid_8;
  wire _counter_ready_8;
  assign _or_ready_6 = (_counter_ready_8 || !_counter_valid_8) && _or_valid_6;
  reg [32-1:0] __delay_data_9;
  reg __delay_valid_9;
  wire __delay_ready_9;
  assign __delay_ready_7 = (__delay_ready_9 || !__delay_valid_9) && __delay_valid_7;
  reg [32-1:0] __delay_data_10;
  reg __delay_valid_10;
  wire __delay_ready_10;
  assign _counter_ready_5 = (__delay_ready_10 || !__delay_valid_10) && _counter_valid_5;
  assign cdata = _counter_data_8;
  assign cvalid = _counter_valid_8;
  assign _counter_ready_8 = cready;
  assign adata = __delay_data_9;
  assign avalid = __delay_valid_9;
  assign __delay_ready_9 = aready;
  assign bdata = __delay_data_10;
  assign bvalid = __delay_valid_10;
  assign __delay_ready_10 = bready;

  always @(posedge CLK) begin
    if(RST) begin
      _counter_data_0 <= -2'sd1;
      _counter_count_0 <= 0;
      _counter_valid_0 <= 0;
      _eq_data_1 <= 0;
      _eq_valid_1 <= 0;
      _eq_data_2 <= 0;
      _eq_valid_2 <= 0;
      _eq_data_3 <= 0;
      _eq_valid_3 <= 0;
      __delay_data_4 <= 0;
      __delay_valid_4 <= 0;
      _counter_data_5 <= -2'sd1;
      _counter_valid_5 <= 0;
      _or_data_6 <= 0;
      _or_valid_6 <= 0;
      __delay_data_7 <= 0;
      __delay_valid_7 <= 0;
      _counter_data_8 <= -2'sd1;
      _counter_valid_8 <= 0;
      __delay_data_9 <= 0;
      __delay_valid_9 <= 0;
      __delay_data_10 <= 0;
      __delay_valid_10 <= 0;
    end else begin
      if((_counter_ready_0 || !_counter_valid_0) && 1 && 1) begin
        _counter_data_0 <= _counter_data_0 + 1;
      end 
      if((_counter_ready_0 || !_counter_valid_0) && 1 && 1) begin
        _counter_count_0 <= (_counter_count_0 == 5'sd8 - 1)? 0 : _counter_count_0 + 1;
      end 
      if(_counter_valid_0 && _counter_ready_0) begin
        _counter_valid_0 <= 0;
      end 
      if((_counter_ready_0 || !_counter_valid_0) && 1) begin
        _counter_valid_0 <= 1;
      end 
      if((_counter_ready_0 || !_counter_valid_0) && 1 && 1 && (_counter_count_0 == 0)) begin
        _counter_data_0 <= -2'sd1 + 1;
      end 
      if((_eq_ready_1 || !_eq_valid_1) && _counter_ready_0 && _counter_valid_0) begin
        _eq_data_1 <= _counter_data_0 == 1'sd0;
      end 
      if(_eq_valid_1 && _eq_ready_1) begin
        _eq_valid_1 <= 0;
      end 
      if((_eq_ready_1 || !_eq_valid_1) && _counter_ready_0) begin
        _eq_valid_1 <= _counter_valid_0;
      end 
      if((_eq_ready_2 || !_eq_valid_2) && _counter_ready_0 && _counter_valid_0) begin
        _eq_data_2 <= _counter_data_0 == 1'sd0;
      end 
      if(_eq_valid_2 && _eq_ready_2) begin
        _eq_valid_2 <= 0;
      end 
      if((_eq_ready_2 || !_eq_valid_2) && _counter_ready_0) begin
        _eq_valid_2 <= _counter_valid_0;
      end 
      if((_eq_ready_3 || !_eq_valid_3) && _counter_ready_0 && _counter_valid_0) begin
        _eq_data_3 <= _counter_data_0 == 4'sd4;
      end 
      if(_eq_valid_3 && _eq_ready_3) begin
        _eq_valid_3 <= 0;
      end 
      if((_eq_ready_3 || !_eq_valid_3) && _counter_ready_0) begin
        _eq_valid_3 <= _counter_valid_0;
      end 
      if((__delay_ready_4 || !__delay_valid_4) && _counter_ready_0 && _counter_valid_0) begin
        __delay_data_4 <= _counter_data_0;
      end 
      if(__delay_valid_4 && __delay_ready_4) begin
        __delay_valid_4 <= 0;
      end 
      if((__delay_ready_4 || !__delay_valid_4) && _counter_ready_0) begin
        __delay_valid_4 <= _counter_valid_0;
      end 
      if((_counter_ready_5 || !_counter_valid_5) && _eq_ready_1 && _eq_valid_1 && _eq_data_1) begin
        _counter_data_5 <= _counter_data_5 + 1;
      end 
      if(_counter_valid_5 && _counter_ready_5) begin
        _counter_valid_5 <= 0;
      end 
      if((_counter_ready_5 || !_counter_valid_5) && _eq_ready_1) begin
        _counter_valid_5 <= _eq_valid_1;
      end 
      if((_or_ready_6 || !_or_valid_6) && (_eq_ready_2 && _eq_ready_3) && (_eq_valid_2 && _eq_valid_3)) begin
        _or_data_6 <= _eq_data_2 | _eq_data_3;
      end 
      if(_or_valid_6 && _or_ready_6) begin
        _or_valid_6 <= 0;
      end 
      if((_or_ready_6 || !_or_valid_6) && (_eq_ready_2 && _eq_ready_3)) begin
        _or_valid_6 <= _eq_valid_2 && _eq_valid_3;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && __delay_ready_4 && __delay_valid_4) begin
        __delay_data_7 <= __delay_data_4;
      end 
      if(__delay_valid_7 && __delay_ready_7) begin
        __delay_valid_7 <= 0;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && __delay_ready_4) begin
        __delay_valid_7 <= __delay_valid_4;
      end 
      if((_counter_ready_8 || !_counter_valid_8) && _or_ready_6 && _or_valid_6 && _or_data_6) begin
        _counter_data_8 <= _counter_data_8 + 1;
      end 
      if(_counter_valid_8 && _counter_ready_8) begin
        _counter_valid_8 <= 0;
      end 
      if((_counter_ready_8 || !_counter_valid_8) && _or_ready_6) begin
        _counter_valid_8 <= _or_valid_6;
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
      if((__delay_ready_10 || !__delay_valid_10) && _counter_ready_5 && _counter_valid_5) begin
        __delay_data_10 <= _counter_data_5;
      end 
      if(__delay_valid_10 && __delay_ready_10) begin
        __delay_valid_10 <= 0;
      end 
      if((__delay_ready_10 || !__delay_valid_10) && _counter_ready_5) begin
        __delay_valid_10 <= _counter_valid_5;
      end 
    end
  end


  always @(posedge CLK) begin
    if(bvalid && 1) begin
      $display("b=%d", bdata);
    end 
    if(cvalid && 1) begin
      $display("c=%d", cdata);
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = dataflow_counter_enable.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
