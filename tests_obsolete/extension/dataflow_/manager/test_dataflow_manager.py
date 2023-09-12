from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_manager

expected_verilog = """

module test
(

);

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
    $dumpfile("dataflow_manager.vcd");
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

  reg [32-1:0] _dataflow_counter_data_1;
  reg _dataflow_counter_valid_1;
  wire _dataflow_counter_ready_1;
  reg [32-1:0] _dataflow_counter_data_4;
  reg _dataflow_counter_valid_4;
  wire _dataflow_counter_ready_4;
  wire [32-1:0] _dataflow_times_data_6;
  wire _dataflow_times_valid_6;
  wire _dataflow_times_ready_6;
  wire [35-1:0] _dataflow_times_mul_odata_6;
  reg [35-1:0] _dataflow_times_mul_odata_reg_6;
  assign _dataflow_times_data_6 = _dataflow_times_mul_odata_reg_6;
  wire _dataflow_times_mul_ovalid_6;
  reg _dataflow_times_mul_valid_reg_6;
  assign _dataflow_times_valid_6 = _dataflow_times_mul_valid_reg_6;
  wire _dataflow_times_mul_enable_6;
  wire _dataflow_times_mul_update_6;
  assign _dataflow_times_mul_enable_6 = (_dataflow_times_ready_6 || !_dataflow_times_valid_6) && _dataflow_counter_ready_1 && _dataflow_counter_valid_1;
  assign _dataflow_times_mul_update_6 = _dataflow_times_ready_6 || !_dataflow_times_valid_6;

  multiplier_0
  _dataflow_times_mul_6
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_6),
    .enable(_dataflow_times_mul_enable_6),
    .valid(_dataflow_times_mul_ovalid_6),
    .a(_dataflow_counter_data_1),
    .b(3'sd2),
    .c(_dataflow_times_mul_odata_6)
  );

  assign _dataflow_counter_ready_1 = (_dataflow_times_ready_6 || !_dataflow_times_valid_6) && _dataflow_counter_valid_1;
  reg [32-1:0] _dataflow__delay_data_9;
  reg _dataflow__delay_valid_9;
  wire _dataflow__delay_ready_9;
  assign _dataflow_counter_ready_4 = (_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_counter_valid_4;
  reg [32-1:0] _dataflow__delay_data_10;
  reg _dataflow__delay_valid_10;
  wire _dataflow__delay_ready_10;
  assign _dataflow__delay_ready_9 = (_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && _dataflow__delay_valid_9;
  reg [32-1:0] _dataflow__delay_data_11;
  reg _dataflow__delay_valid_11;
  wire _dataflow__delay_ready_11;
  assign _dataflow__delay_ready_10 = (_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_valid_10;
  reg [32-1:0] _dataflow__delay_data_12;
  reg _dataflow__delay_valid_12;
  wire _dataflow__delay_ready_12;
  assign _dataflow__delay_ready_11 = (_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow__delay_valid_11;
  reg [32-1:0] _dataflow__delay_data_13;
  reg _dataflow__delay_valid_13;
  wire _dataflow__delay_ready_13;
  assign _dataflow__delay_ready_12 = (_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_valid_12;
  reg [32-1:0] _dataflow__delay_data_14;
  reg _dataflow__delay_valid_14;
  wire _dataflow__delay_ready_14;
  assign _dataflow__delay_ready_13 = (_dataflow__delay_ready_14 || !_dataflow__delay_valid_14) && _dataflow__delay_valid_13;
  reg [32-1:0] _dataflow__delay_data_15;
  reg _dataflow__delay_valid_15;
  wire _dataflow__delay_ready_15;
  assign _dataflow__delay_ready_14 = (_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow__delay_valid_14;
  reg [32-1:0] _dataflow_minus_data_8;
  reg _dataflow_minus_valid_8;
  wire _dataflow_minus_ready_8;
  assign _dataflow_times_ready_6 = (_dataflow_minus_ready_8 || !_dataflow_minus_valid_8) && (_dataflow_times_valid_6 && _dataflow__delay_valid_15);
  assign _dataflow__delay_ready_15 = (_dataflow_minus_ready_8 || !_dataflow_minus_valid_8) && (_dataflow_times_valid_6 && _dataflow__delay_valid_15);
  wire [32-1:0] zdata;
  wire zvalid;
  assign zdata = _dataflow_minus_data_8;
  assign zvalid = _dataflow_minus_valid_8;
  assign _dataflow_minus_ready_8 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_counter_data_1 <= -2'sd1;
      _dataflow_counter_valid_1 <= 0;
      _dataflow_counter_data_4 <= -2'sd1;
      _dataflow_counter_valid_4 <= 0;
      _dataflow_times_mul_odata_reg_6 <= 0;
      _dataflow_times_mul_valid_reg_6 <= 0;
      _dataflow__delay_data_9 <= 0;
      _dataflow__delay_valid_9 <= 0;
      _dataflow__delay_data_10 <= 0;
      _dataflow__delay_valid_10 <= 0;
      _dataflow__delay_data_11 <= 0;
      _dataflow__delay_valid_11 <= 0;
      _dataflow__delay_data_12 <= 0;
      _dataflow__delay_valid_12 <= 0;
      _dataflow__delay_data_13 <= 0;
      _dataflow__delay_valid_13 <= 0;
      _dataflow__delay_data_14 <= 0;
      _dataflow__delay_valid_14 <= 0;
      _dataflow__delay_data_15 <= 0;
      _dataflow__delay_valid_15 <= 0;
      _dataflow_minus_data_8 <= 0;
      _dataflow_minus_valid_8 <= 0;
    end else begin
      if((_dataflow_counter_ready_1 || !_dataflow_counter_valid_1) && 1 && 1) begin
        _dataflow_counter_data_1 <= _dataflow_counter_data_1 + 1;
      end 
      if(_dataflow_counter_valid_1 && _dataflow_counter_ready_1) begin
        _dataflow_counter_valid_1 <= 0;
      end 
      if((_dataflow_counter_ready_1 || !_dataflow_counter_valid_1) && 1) begin
        _dataflow_counter_valid_1 <= 1;
      end 
      if((_dataflow_counter_ready_4 || !_dataflow_counter_valid_4) && 1 && 1) begin
        _dataflow_counter_data_4 <= _dataflow_counter_data_4 + 1;
      end 
      if(_dataflow_counter_valid_4 && _dataflow_counter_ready_4) begin
        _dataflow_counter_valid_4 <= 0;
      end 
      if((_dataflow_counter_ready_4 || !_dataflow_counter_valid_4) && 1) begin
        _dataflow_counter_valid_4 <= 1;
      end 
      if(_dataflow_times_ready_6 || !_dataflow_times_valid_6) begin
        _dataflow_times_mul_odata_reg_6 <= _dataflow_times_mul_odata_6;
      end 
      if(_dataflow_times_ready_6 || !_dataflow_times_valid_6) begin
        _dataflow_times_mul_valid_reg_6 <= _dataflow_times_mul_ovalid_6;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_counter_ready_4 && _dataflow_counter_valid_4) begin
        _dataflow__delay_data_9 <= _dataflow_counter_data_4;
      end 
      if(_dataflow__delay_valid_9 && _dataflow__delay_ready_9) begin
        _dataflow__delay_valid_9 <= 0;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && _dataflow_counter_ready_4) begin
        _dataflow__delay_valid_9 <= _dataflow_counter_valid_4;
      end 
      if((_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && _dataflow__delay_ready_9 && _dataflow__delay_valid_9) begin
        _dataflow__delay_data_10 <= _dataflow__delay_data_9;
      end 
      if(_dataflow__delay_valid_10 && _dataflow__delay_ready_10) begin
        _dataflow__delay_valid_10 <= 0;
      end 
      if((_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && _dataflow__delay_ready_9) begin
        _dataflow__delay_valid_10 <= _dataflow__delay_valid_9;
      end 
      if((_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_ready_10 && _dataflow__delay_valid_10) begin
        _dataflow__delay_data_11 <= _dataflow__delay_data_10;
      end 
      if(_dataflow__delay_valid_11 && _dataflow__delay_ready_11) begin
        _dataflow__delay_valid_11 <= 0;
      end 
      if((_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_ready_10) begin
        _dataflow__delay_valid_11 <= _dataflow__delay_valid_10;
      end 
      if((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow__delay_ready_11 && _dataflow__delay_valid_11) begin
        _dataflow__delay_data_12 <= _dataflow__delay_data_11;
      end 
      if(_dataflow__delay_valid_12 && _dataflow__delay_ready_12) begin
        _dataflow__delay_valid_12 <= 0;
      end 
      if((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow__delay_ready_11) begin
        _dataflow__delay_valid_12 <= _dataflow__delay_valid_11;
      end 
      if((_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_ready_12 && _dataflow__delay_valid_12) begin
        _dataflow__delay_data_13 <= _dataflow__delay_data_12;
      end 
      if(_dataflow__delay_valid_13 && _dataflow__delay_ready_13) begin
        _dataflow__delay_valid_13 <= 0;
      end 
      if((_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_ready_12) begin
        _dataflow__delay_valid_13 <= _dataflow__delay_valid_12;
      end 
      if((_dataflow__delay_ready_14 || !_dataflow__delay_valid_14) && _dataflow__delay_ready_13 && _dataflow__delay_valid_13) begin
        _dataflow__delay_data_14 <= _dataflow__delay_data_13;
      end 
      if(_dataflow__delay_valid_14 && _dataflow__delay_ready_14) begin
        _dataflow__delay_valid_14 <= 0;
      end 
      if((_dataflow__delay_ready_14 || !_dataflow__delay_valid_14) && _dataflow__delay_ready_13) begin
        _dataflow__delay_valid_14 <= _dataflow__delay_valid_13;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow__delay_ready_14 && _dataflow__delay_valid_14) begin
        _dataflow__delay_data_15 <= _dataflow__delay_data_14;
      end 
      if(_dataflow__delay_valid_15 && _dataflow__delay_ready_15) begin
        _dataflow__delay_valid_15 <= 0;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow__delay_ready_14) begin
        _dataflow__delay_valid_15 <= _dataflow__delay_valid_14;
      end 
      if((_dataflow_minus_ready_8 || !_dataflow_minus_valid_8) && (_dataflow_times_ready_6 && _dataflow__delay_ready_15) && (_dataflow_times_valid_6 && _dataflow__delay_valid_15)) begin
        _dataflow_minus_data_8 <= _dataflow_times_data_6 - _dataflow__delay_data_15;
      end 
      if(_dataflow_minus_valid_8 && _dataflow_minus_ready_8) begin
        _dataflow_minus_valid_8 <= 0;
      end 
      if((_dataflow_minus_ready_8 || !_dataflow_minus_valid_8) && (_dataflow_times_ready_6 && _dataflow__delay_ready_15)) begin
        _dataflow_minus_valid_8 <= _dataflow_times_valid_6 && _dataflow__delay_valid_15;
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
