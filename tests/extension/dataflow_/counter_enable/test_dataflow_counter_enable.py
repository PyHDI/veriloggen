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

  wire [32-1:0] bdata;
  wire bvalid;
  wire bready;
  assign bready = 1;
  wire [32-1:0] cdata;
  wire cvalid;
  wire cready;
  assign cready = 1;
  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign _tmp_ready_0 = (_tmp_ready_1 || !_tmp_valid_1) && _tmp_valid_0 && ((_tmp_ready_2 || !_tmp_valid_2) && _tmp_valid_0) && ((_tmp_ready_3 || !_tmp_valid_3) && _tmp_valid_0);
  reg [1-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign _tmp_ready_1 = (_tmp_ready_4 || !_tmp_valid_4) && _tmp_valid_1;
  reg [1-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign _tmp_ready_2 = (_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_2 && _tmp_valid_3);
  reg [1-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_3 = (_tmp_ready_5 || !_tmp_valid_5) && (_tmp_valid_2 && _tmp_valid_3);
  reg [32-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_4 = (_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_4;
  reg [1-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (_tmp_ready_6 || !_tmp_valid_6) && _tmp_valid_5;
  reg [32-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  reg [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign cdata = _tmp_data_6;
  assign cvalid = _tmp_valid_6;
  assign _tmp_ready_6 = cready;
  assign bdata = _tmp_data_7;
  assign bvalid = _tmp_valid_7;
  assign _tmp_ready_7 = bready;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 1'd0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_valid_3 <= 0;
      _tmp_data_4 <= 1'd0;
      _tmp_valid_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_valid_5 <= 0;
      _tmp_data_6 <= 1'd0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
    end else begin
      if((_tmp_ready_0 || !_tmp_valid_0) && 1 && 1) begin
        _tmp_data_0 <= (_tmp_data_0 >= 7)? 0 : _tmp_data_0 + 2'd1;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && 1) begin
        _tmp_valid_0 <= 1;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_1 <= _tmp_data_0 == 1'd0;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && _tmp_ready_0) begin
        _tmp_valid_1 <= _tmp_valid_0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_2 <= _tmp_data_0 == 1'd0;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_0) begin
        _tmp_valid_2 <= _tmp_valid_0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_3 <= _tmp_data_0 == 4'd4;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_0) begin
        _tmp_valid_3 <= _tmp_valid_0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_1 && _tmp_valid_1 && _tmp_data_1) begin
        _tmp_data_4 <= _tmp_data_4 + 2'd1;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_1) begin
        _tmp_valid_4 <= _tmp_valid_1;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_ready_2 && _tmp_ready_3) && (_tmp_valid_2 && _tmp_valid_3)) begin
        _tmp_data_5 <= _tmp_data_2 | _tmp_data_3;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && (_tmp_ready_2 && _tmp_ready_3)) begin
        _tmp_valid_5 <= _tmp_valid_2 && _tmp_valid_3;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5 && _tmp_valid_5 && _tmp_data_5) begin
        _tmp_data_6 <= _tmp_data_6 + 2'd1;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5) begin
        _tmp_valid_6 <= _tmp_valid_5;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_4 && _tmp_valid_4) begin
        _tmp_data_7 <= _tmp_data_4;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_4) begin
        _tmp_valid_7 <= _tmp_valid_4;
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
