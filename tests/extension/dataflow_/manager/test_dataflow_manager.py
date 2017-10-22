from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_manager

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
  wire [32-1:0] _times_data_2;
  wire _times_valid_2;
  wire _times_ready_2;
  wire [35-1:0] _times_odata_2;
  reg [35-1:0] _times_data_reg_2;
  assign _times_data_2 = _times_data_reg_2;
  wire _times_ovalid_2;
  reg _times_valid_reg_2;
  assign _times_valid_2 = _times_valid_reg_2;
  wire _times_enable_2;
  wire _times_update_2;
  assign _times_enable_2 = (_times_ready_2 || !_times_valid_2) && _counter_ready_0 && _counter_valid_0;
  assign _times_update_2 = _times_ready_2 || !_times_valid_2;

  multiplier_0
  mul2
  (
    .CLK(CLK),
    .RST(RST),
    .update(_times_update_2),
    .enable(_times_enable_2),
    .valid(_times_ovalid_2),
    .a(_counter_data_0),
    .b(3'sd2),
    .c(_times_odata_2)
  );

  assign _counter_ready_0 = (_times_ready_2 || !_times_valid_2) && _counter_valid_0;
  reg [32-1:0] __delay_data_3;
  reg __delay_valid_3;
  wire __delay_ready_3;
  assign _counter_ready_1 = (__delay_ready_3 || !__delay_valid_3) && _counter_valid_1;
  reg [32-1:0] __delay_data_4;
  reg __delay_valid_4;
  wire __delay_ready_4;
  assign __delay_ready_3 = (__delay_ready_4 || !__delay_valid_4) && __delay_valid_3;
  reg [32-1:0] __delay_data_5;
  reg __delay_valid_5;
  wire __delay_ready_5;
  assign __delay_ready_4 = (__delay_ready_5 || !__delay_valid_5) && __delay_valid_4;
  reg [32-1:0] __delay_data_6;
  reg __delay_valid_6;
  wire __delay_ready_6;
  assign __delay_ready_5 = (__delay_ready_6 || !__delay_valid_6) && __delay_valid_5;
  reg [32-1:0] __delay_data_7;
  reg __delay_valid_7;
  wire __delay_ready_7;
  assign __delay_ready_6 = (__delay_ready_7 || !__delay_valid_7) && __delay_valid_6;
  reg [32-1:0] __delay_data_8;
  reg __delay_valid_8;
  wire __delay_ready_8;
  assign __delay_ready_7 = (__delay_ready_8 || !__delay_valid_8) && __delay_valid_7;
  reg [32-1:0] __delay_data_9;
  reg __delay_valid_9;
  wire __delay_ready_9;
  assign __delay_ready_8 = (__delay_ready_9 || !__delay_valid_9) && __delay_valid_8;
  reg [32-1:0] _minus_data_10;
  reg _minus_valid_10;
  wire _minus_ready_10;
  assign _times_ready_2 = (_minus_ready_10 || !_minus_valid_10) && (_times_valid_2 && __delay_valid_9);
  assign __delay_ready_9 = (_minus_ready_10 || !_minus_valid_10) && (_times_valid_2 && __delay_valid_9);
  wire [32-1:0] zdata;
  wire zvalid;
  assign zdata = _minus_data_10;
  assign zvalid = _minus_valid_10;
  assign _minus_ready_10 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _counter_data_0 <= -2'sd1;
      _counter_valid_0 <= 0;
      _counter_data_1 <= -2'sd1;
      _counter_valid_1 <= 0;
      _times_data_reg_2 <= 0;
      _times_valid_reg_2 <= 0;
      __delay_data_3 <= 0;
      __delay_valid_3 <= 0;
      __delay_data_4 <= 0;
      __delay_valid_4 <= 0;
      __delay_data_5 <= 0;
      __delay_valid_5 <= 0;
      __delay_data_6 <= 0;
      __delay_valid_6 <= 0;
      __delay_data_7 <= 0;
      __delay_valid_7 <= 0;
      __delay_data_8 <= 0;
      __delay_valid_8 <= 0;
      __delay_data_9 <= 0;
      __delay_valid_9 <= 0;
      _minus_data_10 <= 0;
      _minus_valid_10 <= 0;
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
      if(_times_ready_2 || !_times_valid_2) begin
        _times_data_reg_2 <= _times_odata_2;
      end 
      if(_times_ready_2 || !_times_valid_2) begin
        _times_valid_reg_2 <= _times_ovalid_2;
      end 
      if((__delay_ready_3 || !__delay_valid_3) && _counter_ready_1 && _counter_valid_1) begin
        __delay_data_3 <= _counter_data_1;
      end 
      if(__delay_valid_3 && __delay_ready_3) begin
        __delay_valid_3 <= 0;
      end 
      if((__delay_ready_3 || !__delay_valid_3) && _counter_ready_1) begin
        __delay_valid_3 <= _counter_valid_1;
      end 
      if((__delay_ready_4 || !__delay_valid_4) && __delay_ready_3 && __delay_valid_3) begin
        __delay_data_4 <= __delay_data_3;
      end 
      if(__delay_valid_4 && __delay_ready_4) begin
        __delay_valid_4 <= 0;
      end 
      if((__delay_ready_4 || !__delay_valid_4) && __delay_ready_3) begin
        __delay_valid_4 <= __delay_valid_3;
      end 
      if((__delay_ready_5 || !__delay_valid_5) && __delay_ready_4 && __delay_valid_4) begin
        __delay_data_5 <= __delay_data_4;
      end 
      if(__delay_valid_5 && __delay_ready_5) begin
        __delay_valid_5 <= 0;
      end 
      if((__delay_ready_5 || !__delay_valid_5) && __delay_ready_4) begin
        __delay_valid_5 <= __delay_valid_4;
      end 
      if((__delay_ready_6 || !__delay_valid_6) && __delay_ready_5 && __delay_valid_5) begin
        __delay_data_6 <= __delay_data_5;
      end 
      if(__delay_valid_6 && __delay_ready_6) begin
        __delay_valid_6 <= 0;
      end 
      if((__delay_ready_6 || !__delay_valid_6) && __delay_ready_5) begin
        __delay_valid_6 <= __delay_valid_5;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && __delay_ready_6 && __delay_valid_6) begin
        __delay_data_7 <= __delay_data_6;
      end 
      if(__delay_valid_7 && __delay_ready_7) begin
        __delay_valid_7 <= 0;
      end 
      if((__delay_ready_7 || !__delay_valid_7) && __delay_ready_6) begin
        __delay_valid_7 <= __delay_valid_6;
      end 
      if((__delay_ready_8 || !__delay_valid_8) && __delay_ready_7 && __delay_valid_7) begin
        __delay_data_8 <= __delay_data_7;
      end 
      if(__delay_valid_8 && __delay_ready_8) begin
        __delay_valid_8 <= 0;
      end 
      if((__delay_ready_8 || !__delay_valid_8) && __delay_ready_7) begin
        __delay_valid_8 <= __delay_valid_7;
      end 
      if((__delay_ready_9 || !__delay_valid_9) && __delay_ready_8 && __delay_valid_8) begin
        __delay_data_9 <= __delay_data_8;
      end 
      if(__delay_valid_9 && __delay_ready_9) begin
        __delay_valid_9 <= 0;
      end 
      if((__delay_ready_9 || !__delay_valid_9) && __delay_ready_8) begin
        __delay_valid_9 <= __delay_valid_8;
      end 
      if((_minus_ready_10 || !_minus_valid_10) && (_times_ready_2 && __delay_ready_9) && (_times_valid_2 && __delay_valid_9)) begin
        _minus_data_10 <= _times_data_2 - __delay_data_9;
      end 
      if(_minus_valid_10 && _minus_ready_10) begin
        _minus_valid_10 <= 0;
      end 
      if((_minus_ready_10 || !_minus_valid_10) && (_times_ready_2 && __delay_ready_9)) begin
        _minus_valid_10 <= _times_valid_2 && __delay_valid_9;
      end 
    end
  end


endmodule



module multiplier_0
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [3-1:0] b,
  output [35-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_0
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [3-1:0] b,
  output [35-1:0] c
);

  reg [32-1:0] _a;
  reg signed [3-1:0] _b;
  wire signed [35-1:0] _mul;
  reg signed [35-1:0] _pipe_mul0;
  reg signed [35-1:0] _pipe_mul1;
  reg signed [35-1:0] _pipe_mul2;
  reg signed [35-1:0] _pipe_mul3;
  reg signed [35-1:0] _pipe_mul4;
  assign _mul = $signed({ 1'd0, _a }) * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = dataflow_manager.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
