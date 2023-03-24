from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_multiple_manager

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
    $dumpfile("dataflow_multiple_manager.vcd");
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
  reg [32-1:0] _dataflow_counter_data_7;
  reg _dataflow_counter_valid_7;
  wire _dataflow_counter_ready_7;
  reg [32-1:0] _dataflow_plus_data_9;
  reg _dataflow_plus_valid_9;
  wire _dataflow_plus_ready_9;
  reg [32-1:0] _dataflow_plus_data_11;
  reg _dataflow_plus_valid_11;
  wire _dataflow_plus_ready_11;
  reg [32-1:0] _dataflow_plus_data_13;
  reg _dataflow_plus_valid_13;
  wire _dataflow_plus_ready_13;
  reg [32-1:0] _dataflow__delay_data_15;
  reg _dataflow__delay_valid_15;
  wire _dataflow__delay_ready_15;
  assign _dataflow_counter_ready_7 = (_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && (_dataflow_counter_valid_4 && _dataflow_counter_valid_7) && ((_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && (_dataflow_counter_valid_7 && _dataflow_counter_valid_1)) && ((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow_counter_valid_7);
  reg [32-1:0] _dataflow__delay_data_16;
  reg _dataflow__delay_valid_16;
  wire _dataflow__delay_ready_16;
  assign _dataflow_counter_ready_1 = (_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && (_dataflow_counter_valid_1 && _dataflow_counter_valid_4) && ((_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && (_dataflow_counter_valid_7 && _dataflow_counter_valid_1)) && ((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow_counter_valid_1);
  reg [32-1:0] _dataflow__delay_data_17;
  reg _dataflow__delay_valid_17;
  wire _dataflow__delay_ready_17;
  assign _dataflow_counter_ready_4 = (_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && (_dataflow_counter_valid_1 && _dataflow_counter_valid_4) && ((_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && (_dataflow_counter_valid_4 && _dataflow_counter_valid_7)) && ((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow_counter_valid_4);
  reg [32-1:0] _dataflow_plus_data_10;
  reg _dataflow_plus_valid_10;
  wire _dataflow_plus_ready_10;
  assign _dataflow_plus_ready_9 = (_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && (_dataflow_plus_valid_9 && _dataflow__delay_valid_15);
  assign _dataflow__delay_ready_15 = (_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && (_dataflow_plus_valid_9 && _dataflow__delay_valid_15);
  reg [32-1:0] _dataflow_plus_data_12;
  reg _dataflow_plus_valid_12;
  wire _dataflow_plus_ready_12;
  assign _dataflow_plus_ready_11 = (_dataflow_plus_ready_12 || !_dataflow_plus_valid_12) && (_dataflow_plus_valid_11 && _dataflow__delay_valid_16);
  assign _dataflow__delay_ready_16 = (_dataflow_plus_ready_12 || !_dataflow_plus_valid_12) && (_dataflow_plus_valid_11 && _dataflow__delay_valid_16);
  reg [32-1:0] _dataflow_plus_data_14;
  reg _dataflow_plus_valid_14;
  wire _dataflow_plus_ready_14;
  assign _dataflow_plus_ready_13 = (_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_valid_13 && _dataflow__delay_valid_17);
  assign _dataflow__delay_ready_17 = (_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_valid_13 && _dataflow__delay_valid_17);
  wire [32-1:0] adata;
  wire avalid;
  assign adata = _dataflow_plus_data_10;
  assign avalid = _dataflow_plus_valid_10;
  assign _dataflow_plus_ready_10 = 1;
  wire [32-1:0] bdata;
  wire bvalid;
  assign bdata = _dataflow_plus_data_12;
  assign bvalid = _dataflow_plus_valid_12;
  assign _dataflow_plus_ready_12 = 1;
  wire [32-1:0] cdata;
  wire cvalid;
  assign cdata = _dataflow_plus_data_14;
  assign cvalid = _dataflow_plus_valid_14;
  assign _dataflow_plus_ready_14 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_counter_data_1 <= -2'sd1;
      _dataflow_counter_valid_1 <= 0;
      _dataflow_counter_data_4 <= -2'sd1;
      _dataflow_counter_valid_4 <= 0;
      _dataflow_counter_data_7 <= -2'sd1;
      _dataflow_counter_valid_7 <= 0;
      _dataflow_plus_data_9 <= 0;
      _dataflow_plus_valid_9 <= 0;
      _dataflow_plus_data_11 <= 0;
      _dataflow_plus_valid_11 <= 0;
      _dataflow_plus_data_13 <= 0;
      _dataflow_plus_valid_13 <= 0;
      _dataflow__delay_data_15 <= 0;
      _dataflow__delay_valid_15 <= 0;
      _dataflow__delay_data_16 <= 0;
      _dataflow__delay_valid_16 <= 0;
      _dataflow__delay_data_17 <= 0;
      _dataflow__delay_valid_17 <= 0;
      _dataflow_plus_data_10 <= 0;
      _dataflow_plus_valid_10 <= 0;
      _dataflow_plus_data_12 <= 0;
      _dataflow_plus_valid_12 <= 0;
      _dataflow_plus_data_14 <= 0;
      _dataflow_plus_valid_14 <= 0;
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
      if((_dataflow_counter_ready_7 || !_dataflow_counter_valid_7) && 1 && 1) begin
        _dataflow_counter_data_7 <= _dataflow_counter_data_7 + 1;
      end 
      if(_dataflow_counter_valid_7 && _dataflow_counter_ready_7) begin
        _dataflow_counter_valid_7 <= 0;
      end 
      if((_dataflow_counter_ready_7 || !_dataflow_counter_valid_7) && 1) begin
        _dataflow_counter_valid_7 <= 1;
      end 
      if((_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && (_dataflow_counter_ready_1 && _dataflow_counter_ready_4) && (_dataflow_counter_valid_1 && _dataflow_counter_valid_4)) begin
        _dataflow_plus_data_9 <= _dataflow_counter_data_1 + _dataflow_counter_data_4;
      end 
      if(_dataflow_plus_valid_9 && _dataflow_plus_ready_9) begin
        _dataflow_plus_valid_9 <= 0;
      end 
      if((_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && (_dataflow_counter_ready_1 && _dataflow_counter_ready_4)) begin
        _dataflow_plus_valid_9 <= _dataflow_counter_valid_1 && _dataflow_counter_valid_4;
      end 
      if((_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && (_dataflow_counter_ready_4 && _dataflow_counter_ready_7) && (_dataflow_counter_valid_4 && _dataflow_counter_valid_7)) begin
        _dataflow_plus_data_11 <= _dataflow_counter_data_4 + _dataflow_counter_data_7;
      end 
      if(_dataflow_plus_valid_11 && _dataflow_plus_ready_11) begin
        _dataflow_plus_valid_11 <= 0;
      end 
      if((_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && (_dataflow_counter_ready_4 && _dataflow_counter_ready_7)) begin
        _dataflow_plus_valid_11 <= _dataflow_counter_valid_4 && _dataflow_counter_valid_7;
      end 
      if((_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && (_dataflow_counter_ready_7 && _dataflow_counter_ready_1) && (_dataflow_counter_valid_7 && _dataflow_counter_valid_1)) begin
        _dataflow_plus_data_13 <= _dataflow_counter_data_7 + _dataflow_counter_data_1;
      end 
      if(_dataflow_plus_valid_13 && _dataflow_plus_ready_13) begin
        _dataflow_plus_valid_13 <= 0;
      end 
      if((_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && (_dataflow_counter_ready_7 && _dataflow_counter_ready_1)) begin
        _dataflow_plus_valid_13 <= _dataflow_counter_valid_7 && _dataflow_counter_valid_1;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow_counter_ready_7 && _dataflow_counter_valid_7) begin
        _dataflow__delay_data_15 <= _dataflow_counter_data_7;
      end 
      if(_dataflow__delay_valid_15 && _dataflow__delay_ready_15) begin
        _dataflow__delay_valid_15 <= 0;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && _dataflow_counter_ready_7) begin
        _dataflow__delay_valid_15 <= _dataflow_counter_valid_7;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow_counter_ready_1 && _dataflow_counter_valid_1) begin
        _dataflow__delay_data_16 <= _dataflow_counter_data_1;
      end 
      if(_dataflow__delay_valid_16 && _dataflow__delay_ready_16) begin
        _dataflow__delay_valid_16 <= 0;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow_counter_ready_1) begin
        _dataflow__delay_valid_16 <= _dataflow_counter_valid_1;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow_counter_ready_4 && _dataflow_counter_valid_4) begin
        _dataflow__delay_data_17 <= _dataflow_counter_data_4;
      end 
      if(_dataflow__delay_valid_17 && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_17 <= 0;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow_counter_ready_4) begin
        _dataflow__delay_valid_17 <= _dataflow_counter_valid_4;
      end 
      if((_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && (_dataflow_plus_ready_9 && _dataflow__delay_ready_15) && (_dataflow_plus_valid_9 && _dataflow__delay_valid_15)) begin
        _dataflow_plus_data_10 <= _dataflow_plus_data_9 + _dataflow__delay_data_15;
      end 
      if(_dataflow_plus_valid_10 && _dataflow_plus_ready_10) begin
        _dataflow_plus_valid_10 <= 0;
      end 
      if((_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && (_dataflow_plus_ready_9 && _dataflow__delay_ready_15)) begin
        _dataflow_plus_valid_10 <= _dataflow_plus_valid_9 && _dataflow__delay_valid_15;
      end 
      if((_dataflow_plus_ready_12 || !_dataflow_plus_valid_12) && (_dataflow_plus_ready_11 && _dataflow__delay_ready_16) && (_dataflow_plus_valid_11 && _dataflow__delay_valid_16)) begin
        _dataflow_plus_data_12 <= _dataflow_plus_data_11 + _dataflow__delay_data_16;
      end 
      if(_dataflow_plus_valid_12 && _dataflow_plus_ready_12) begin
        _dataflow_plus_valid_12 <= 0;
      end 
      if((_dataflow_plus_ready_12 || !_dataflow_plus_valid_12) && (_dataflow_plus_ready_11 && _dataflow__delay_ready_16)) begin
        _dataflow_plus_valid_12 <= _dataflow_plus_valid_11 && _dataflow__delay_valid_16;
      end 
      if((_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_ready_13 && _dataflow__delay_ready_17) && (_dataflow_plus_valid_13 && _dataflow__delay_valid_17)) begin
        _dataflow_plus_data_14 <= _dataflow_plus_data_13 + _dataflow__delay_data_17;
      end 
      if(_dataflow_plus_valid_14 && _dataflow_plus_ready_14) begin
        _dataflow_plus_valid_14 <= 0;
      end 
      if((_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_ready_13 && _dataflow__delay_ready_17)) begin
        _dataflow_plus_valid_14 <= _dataflow_plus_valid_13 && _dataflow__delay_valid_17;
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
