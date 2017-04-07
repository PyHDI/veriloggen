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

  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  reg [32-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  reg [32-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  reg [32-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  reg [32-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  reg [32-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  assign _tmp_ready_2 = (_tmp_ready_4 || !_tmp_valid_4) && (_tmp_valid_1 && _tmp_valid_2) && ((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_2 && _tmp_valid_0)) && ((_tmp_ready_6 || !_tmp_valid_6) && _tmp_valid_2);
  reg [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign _tmp_ready_0 = (_tmp_ready_3 || !_tmp_valid_3) && (_tmp_valid_0 && _tmp_valid_1) && ((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_2 && _tmp_valid_0)) && ((_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_0);
  reg [32-1:0] _tmp_data_8;
  reg _tmp_valid_8;
  wire _tmp_ready_8;
  assign _tmp_ready_1 = (_tmp_ready_3 || !_tmp_valid_3) && (_tmp_valid_0 && _tmp_valid_1) && ((_tmp_ready_4 || !_tmp_valid_4) && (_tmp_valid_1 && _tmp_valid_2)) && ((_tmp_ready_8 || !_tmp_valid_8) && _tmp_valid_1);
  reg [32-1:0] _tmp_data_9;
  reg _tmp_valid_9;
  wire _tmp_ready_9;
  assign _tmp_ready_3 = (_tmp_ready_9 || !_tmp_valid_9) && (_tmp_valid_3 && _tmp_valid_6);
  assign _tmp_ready_6 = (_tmp_ready_9 || !_tmp_valid_9) && (_tmp_valid_3 && _tmp_valid_6);
  reg [32-1:0] _tmp_data_10;
  reg _tmp_valid_10;
  wire _tmp_ready_10;
  assign _tmp_ready_4 = (_tmp_ready_10 || !_tmp_valid_10) && (_tmp_valid_4 && _tmp_valid_7);
  assign _tmp_ready_7 = (_tmp_ready_10 || !_tmp_valid_10) && (_tmp_valid_4 && _tmp_valid_7);
  reg [32-1:0] _tmp_data_11;
  reg _tmp_valid_11;
  wire _tmp_ready_11;
  assign _tmp_ready_5 = (_tmp_ready_11 || !_tmp_valid_11) && (_tmp_valid_5 && _tmp_valid_8);
  assign _tmp_ready_8 = (_tmp_ready_11 || !_tmp_valid_11) && (_tmp_valid_5 && _tmp_valid_8);
  wire [32-1:0] adata;
  wire avalid;
  assign adata = _tmp_data_9;
  assign avalid = _tmp_valid_9;
  assign _tmp_ready_9 = 1;
  wire [32-1:0] bdata;
  wire bvalid;
  assign bdata = _tmp_data_10;
  assign bvalid = _tmp_valid_10;
  assign _tmp_ready_10 = 1;
  wire [32-1:0] cdata;
  wire cvalid;
  assign cdata = _tmp_data_11;
  assign cvalid = _tmp_valid_11;
  assign _tmp_ready_11 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 1'd0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 1'd0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 1'd0;
      _tmp_valid_2 <= 0;
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
      _tmp_data_11 <= 0;
      _tmp_valid_11 <= 0;
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
      if((_tmp_ready_2 || !_tmp_valid_2) && 1 && 1) begin
        _tmp_data_2 <= _tmp_data_2 + 2'd1;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && 1) begin
        _tmp_valid_2 <= 1;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && (_tmp_ready_0 && _tmp_ready_1) && (_tmp_valid_0 && _tmp_valid_1)) begin
        _tmp_data_3 <= _tmp_data_0 + _tmp_data_1;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && (_tmp_ready_0 && _tmp_ready_1)) begin
        _tmp_valid_3 <= _tmp_valid_0 && _tmp_valid_1;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && (_tmp_ready_1 && _tmp_ready_2) && (_tmp_valid_1 && _tmp_valid_2)) begin
        _tmp_data_4 <= _tmp_data_1 + _tmp_data_2;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && (_tmp_ready_1 && _tmp_ready_2)) begin
        _tmp_valid_4 <= _tmp_valid_1 && _tmp_valid_2;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_ready_2 && _tmp_ready_0) && (_tmp_valid_2 && _tmp_valid_0)) begin
        _tmp_data_5 <= _tmp_data_2 + _tmp_data_0;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_ready_2 && _tmp_ready_0)) begin
        _tmp_valid_5 <= _tmp_valid_2 && _tmp_valid_0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_2 && _tmp_valid_2) begin
        _tmp_data_6 <= _tmp_data_2;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_2) begin
        _tmp_valid_6 <= _tmp_valid_2;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_7 <= _tmp_data_0;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_0) begin
        _tmp_valid_7 <= _tmp_valid_0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && _tmp_ready_1 && _tmp_valid_1) begin
        _tmp_data_8 <= _tmp_data_1;
      end 
      if(_tmp_valid_8 && _tmp_ready_8) begin
        _tmp_valid_8 <= 0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && _tmp_ready_1) begin
        _tmp_valid_8 <= _tmp_valid_1;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && (_tmp_ready_3 && _tmp_ready_6) && (_tmp_valid_3 && _tmp_valid_6)) begin
        _tmp_data_9 <= _tmp_data_3 + _tmp_data_6;
      end 
      if(_tmp_valid_9 && _tmp_ready_9) begin
        _tmp_valid_9 <= 0;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && (_tmp_ready_3 && _tmp_ready_6)) begin
        _tmp_valid_9 <= _tmp_valid_3 && _tmp_valid_6;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && (_tmp_ready_4 && _tmp_ready_7) && (_tmp_valid_4 && _tmp_valid_7)) begin
        _tmp_data_10 <= _tmp_data_4 + _tmp_data_7;
      end 
      if(_tmp_valid_10 && _tmp_ready_10) begin
        _tmp_valid_10 <= 0;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && (_tmp_ready_4 && _tmp_ready_7)) begin
        _tmp_valid_10 <= _tmp_valid_4 && _tmp_valid_7;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && (_tmp_ready_5 && _tmp_ready_8) && (_tmp_valid_5 && _tmp_valid_8)) begin
        _tmp_data_11 <= _tmp_data_5 + _tmp_data_8;
      end 
      if(_tmp_valid_11 && _tmp_ready_11) begin
        _tmp_valid_11 <= 0;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && (_tmp_ready_5 && _tmp_ready_8)) begin
        _tmp_valid_11 <= _tmp_valid_5 && _tmp_valid_8;
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
