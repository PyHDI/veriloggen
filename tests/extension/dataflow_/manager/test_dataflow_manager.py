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

  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  wire [32-1:0] _tmp_data_2;
  wire _tmp_valid_2;
  wire _tmp_ready_2;
  wire [35-1:0] _tmp_odata_2;
  reg [35-1:0] _tmp_data_reg_2;
  assign _tmp_data_2 = _tmp_data_reg_2;
  wire _tmp_ovalid_2;
  reg _tmp_valid_reg_2;
  assign _tmp_valid_2 = _tmp_valid_reg_2;
  wire _tmp_enable_2;
  wire _tmp_update_2;
  assign _tmp_enable_2 = (_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_0 && _tmp_valid_0;
  assign _tmp_update_2 = _tmp_ready_2 || !_tmp_valid_2;

  multiplier_0
  mul2
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_2),
    .enable(_tmp_enable_2),
    .valid(_tmp_ovalid_2),
    .a(_tmp_data_0),
    .b(3'd2),
    .c(_tmp_odata_2)
  );

  assign _tmp_ready_0 = (_tmp_ready_2 || !_tmp_valid_2) && _tmp_valid_0;
  reg [32-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_1 = (_tmp_ready_3 || !_tmp_valid_3) && _tmp_valid_1;
  reg [32-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_3 = (_tmp_ready_4 || !_tmp_valid_4) && _tmp_valid_3;
  reg [32-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_4 = (_tmp_ready_5 || !_tmp_valid_5) && _tmp_valid_4;
  reg [32-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  assign _tmp_ready_5 = (_tmp_ready_6 || !_tmp_valid_6) && _tmp_valid_5;
  reg [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign _tmp_ready_6 = (_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_6;
  reg [32-1:0] _tmp_data_8;
  reg _tmp_valid_8;
  wire _tmp_ready_8;
  assign _tmp_ready_7 = (_tmp_ready_8 || !_tmp_valid_8) && _tmp_valid_7;
  reg [32-1:0] _tmp_data_9;
  reg _tmp_valid_9;
  wire _tmp_ready_9;
  assign _tmp_ready_8 = (_tmp_ready_9 || !_tmp_valid_9) && _tmp_valid_8;
  reg [32-1:0] _tmp_data_10;
  reg _tmp_valid_10;
  wire _tmp_ready_10;
  assign _tmp_ready_2 = (_tmp_ready_10 || !_tmp_valid_10) && (_tmp_valid_2 && _tmp_valid_9);
  assign _tmp_ready_9 = (_tmp_ready_10 || !_tmp_valid_10) && (_tmp_valid_2 && _tmp_valid_9);
  wire [32-1:0] zdata;
  wire zvalid;
  assign zdata = _tmp_data_10;
  assign zvalid = _tmp_valid_10;
  assign _tmp_ready_10 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 1'd0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 1'd0;
      _tmp_valid_1 <= 0;
      _tmp_data_reg_2 <= 0;
      _tmp_valid_reg_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_valid_3 <= 0;
      _tmp_data_4 <= 0;
      _tmp_valid_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_valid_5 <= 0;
      _tmp_data_6 <= 0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
      _tmp_data_8 <= 0;
      _tmp_valid_8 <= 0;
      _tmp_data_9 <= 0;
      _tmp_valid_9 <= 0;
      _tmp_data_10 <= 0;
      _tmp_valid_10 <= 0;
    end else begin
      if((_tmp_ready_0 || !_tmp_valid_0) && 1 && 1) begin
        _tmp_data_0 <= _tmp_data_0 + 2'd1;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && 1) begin
        _tmp_valid_0 <= 1;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1 && 1) begin
        _tmp_data_1 <= _tmp_data_1 + 2'd1;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1) begin
        _tmp_valid_1 <= 1;
      end 
      if(_tmp_ready_2 || !_tmp_valid_2) begin
        _tmp_data_reg_2 <= _tmp_odata_2;
      end 
      if(_tmp_ready_2 || !_tmp_valid_2) begin
        _tmp_valid_reg_2 <= _tmp_ovalid_2;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_1 && _tmp_valid_1) begin
        _tmp_data_3 <= _tmp_data_1;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_1) begin
        _tmp_valid_3 <= _tmp_valid_1;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_3 && _tmp_valid_3) begin
        _tmp_data_4 <= _tmp_data_3;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_3) begin
        _tmp_valid_4 <= _tmp_valid_3;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && _tmp_ready_4 && _tmp_valid_4) begin
        _tmp_data_5 <= _tmp_data_4;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && _tmp_ready_4) begin
        _tmp_valid_5 <= _tmp_valid_4;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5 && _tmp_valid_5) begin
        _tmp_data_6 <= _tmp_data_5;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5) begin
        _tmp_valid_6 <= _tmp_valid_5;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_6 && _tmp_valid_6) begin
        _tmp_data_7 <= _tmp_data_6;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_6) begin
        _tmp_valid_7 <= _tmp_valid_6;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && _tmp_ready_7 && _tmp_valid_7) begin
        _tmp_data_8 <= _tmp_data_7;
      end 
      if(_tmp_valid_8 && _tmp_ready_8) begin
        _tmp_valid_8 <= 0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && _tmp_ready_7) begin
        _tmp_valid_8 <= _tmp_valid_7;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && _tmp_ready_8 && _tmp_valid_8) begin
        _tmp_data_9 <= _tmp_data_8;
      end 
      if(_tmp_valid_9 && _tmp_ready_9) begin
        _tmp_valid_9 <= 0;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && _tmp_ready_8) begin
        _tmp_valid_9 <= _tmp_valid_8;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && (_tmp_ready_2 && _tmp_ready_9) && (_tmp_valid_2 && _tmp_valid_9)) begin
        _tmp_data_10 <= _tmp_data_2 - _tmp_data_9;
      end 
      if(_tmp_valid_10 && _tmp_ready_10) begin
        _tmp_valid_10 <= 0;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && (_tmp_ready_2 && _tmp_ready_9)) begin
        _tmp_valid_10 <= _tmp_valid_2 && _tmp_valid_9;
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
  reg signed [35-1:0] _tmpval0;
  reg signed [35-1:0] _tmpval1;
  reg signed [35-1:0] _tmpval2;
  reg signed [35-1:0] _tmpval3;
  reg signed [35-1:0] _tmpval4;
  wire signed [35-1:0] rslt;
  assign rslt = $signed({ 1'd0, _a }) * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
