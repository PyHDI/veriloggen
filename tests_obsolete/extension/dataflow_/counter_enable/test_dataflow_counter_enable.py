from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_counter_enable

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
  reg [32-1:0] _dataflow_counter_data_2;
  reg _dataflow_counter_valid_2;
  wire _dataflow_counter_ready_2;
  reg [6-1:0] _dataflow_counter_count_2;
  reg [1-1:0] _dataflow_eq_data_4;
  reg _dataflow_eq_valid_4;
  wire _dataflow_eq_ready_4;
  reg [1-1:0] _dataflow_eq_data_9;
  reg _dataflow_eq_valid_9;
  wire _dataflow_eq_ready_9;
  reg [1-1:0] _dataflow_eq_data_11;
  reg _dataflow_eq_valid_11;
  wire _dataflow_eq_ready_11;
  reg [32-1:0] _dataflow__delay_data_17;
  reg _dataflow__delay_valid_17;
  wire _dataflow__delay_ready_17;
  assign _dataflow_counter_ready_2 = (_dataflow_eq_ready_4 || !_dataflow_eq_valid_4) && _dataflow_counter_valid_2 && ((_dataflow_eq_ready_9 || !_dataflow_eq_valid_9) && _dataflow_counter_valid_2) && ((_dataflow_eq_ready_11 || !_dataflow_eq_valid_11) && _dataflow_counter_valid_2) && ((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow_counter_valid_2);
  reg [32-1:0] _dataflow_counter_data_7;
  reg _dataflow_counter_valid_7;
  wire _dataflow_counter_ready_7;
  assign _dataflow_eq_ready_4 = (_dataflow_counter_ready_7 || !_dataflow_counter_valid_7) && _dataflow_eq_valid_4;
  reg [1-1:0] _dataflow_or_data_13;
  reg _dataflow_or_valid_13;
  wire _dataflow_or_ready_13;
  assign _dataflow_eq_ready_9 = (_dataflow_or_ready_13 || !_dataflow_or_valid_13) && (_dataflow_eq_valid_9 && _dataflow_eq_valid_11);
  assign _dataflow_eq_ready_11 = (_dataflow_or_ready_13 || !_dataflow_or_valid_13) && (_dataflow_eq_valid_9 && _dataflow_eq_valid_11);
  reg [32-1:0] _dataflow__delay_data_18;
  reg _dataflow__delay_valid_18;
  wire _dataflow__delay_ready_18;
  assign _dataflow__delay_ready_17 = (_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_valid_17;
  reg [32-1:0] _dataflow_counter_data_15;
  reg _dataflow_counter_valid_15;
  wire _dataflow_counter_ready_15;
  assign _dataflow_or_ready_13 = (_dataflow_counter_ready_15 || !_dataflow_counter_valid_15) && _dataflow_or_valid_13;
  reg [32-1:0] _dataflow__delay_data_19;
  reg _dataflow__delay_valid_19;
  wire _dataflow__delay_ready_19;
  assign _dataflow__delay_ready_18 = (_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_valid_18;
  reg [32-1:0] _dataflow__delay_data_20;
  reg _dataflow__delay_valid_20;
  wire _dataflow__delay_ready_20;
  assign _dataflow_counter_ready_7 = (_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow_counter_valid_7;
  assign cdata = _dataflow_counter_data_15;
  assign cvalid = _dataflow_counter_valid_15;
  assign _dataflow_counter_ready_15 = cready;
  assign adata = _dataflow__delay_data_19;
  assign avalid = _dataflow__delay_valid_19;
  assign _dataflow__delay_ready_19 = aready;
  assign bdata = _dataflow__delay_data_20;
  assign bvalid = _dataflow__delay_valid_20;
  assign _dataflow__delay_ready_20 = bready;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_counter_data_2 <= -2'sd1;
      _dataflow_counter_count_2 <= 0;
      _dataflow_counter_valid_2 <= 0;
      _dataflow_eq_data_4 <= 0;
      _dataflow_eq_valid_4 <= 0;
      _dataflow_eq_data_9 <= 0;
      _dataflow_eq_valid_9 <= 0;
      _dataflow_eq_data_11 <= 0;
      _dataflow_eq_valid_11 <= 0;
      _dataflow__delay_data_17 <= 0;
      _dataflow__delay_valid_17 <= 0;
      _dataflow_counter_data_7 <= -2'sd1;
      _dataflow_counter_valid_7 <= 0;
      _dataflow_or_data_13 <= 0;
      _dataflow_or_valid_13 <= 0;
      _dataflow__delay_data_18 <= 0;
      _dataflow__delay_valid_18 <= 0;
      _dataflow_counter_data_15 <= -2'sd1;
      _dataflow_counter_valid_15 <= 0;
      _dataflow__delay_data_19 <= 0;
      _dataflow__delay_valid_19 <= 0;
      _dataflow__delay_data_20 <= 0;
      _dataflow__delay_valid_20 <= 0;
    end else begin
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1 && 1) begin
        _dataflow_counter_data_2 <= _dataflow_counter_data_2 + 1;
      end 
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1 && 1) begin
        _dataflow_counter_count_2 <= (_dataflow_counter_count_2 == 5'sd8 - 1)? 0 : _dataflow_counter_count_2 + 1;
      end 
      if(_dataflow_counter_valid_2 && _dataflow_counter_ready_2) begin
        _dataflow_counter_valid_2 <= 0;
      end 
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1) begin
        _dataflow_counter_valid_2 <= 1;
      end 
      if((_dataflow_counter_ready_2 || !_dataflow_counter_valid_2) && 1 && 1 && (_dataflow_counter_count_2 == 0)) begin
        _dataflow_counter_data_2 <= -2'sd1 + 1;
      end 
      if((_dataflow_eq_ready_4 || !_dataflow_eq_valid_4) && _dataflow_counter_ready_2 && _dataflow_counter_valid_2) begin
        _dataflow_eq_data_4 <= _dataflow_counter_data_2 == 1'sd0;
      end 
      if(_dataflow_eq_valid_4 && _dataflow_eq_ready_4) begin
        _dataflow_eq_valid_4 <= 0;
      end 
      if((_dataflow_eq_ready_4 || !_dataflow_eq_valid_4) && _dataflow_counter_ready_2) begin
        _dataflow_eq_valid_4 <= _dataflow_counter_valid_2;
      end 
      if((_dataflow_eq_ready_9 || !_dataflow_eq_valid_9) && _dataflow_counter_ready_2 && _dataflow_counter_valid_2) begin
        _dataflow_eq_data_9 <= _dataflow_counter_data_2 == 1'sd0;
      end 
      if(_dataflow_eq_valid_9 && _dataflow_eq_ready_9) begin
        _dataflow_eq_valid_9 <= 0;
      end 
      if((_dataflow_eq_ready_9 || !_dataflow_eq_valid_9) && _dataflow_counter_ready_2) begin
        _dataflow_eq_valid_9 <= _dataflow_counter_valid_2;
      end 
      if((_dataflow_eq_ready_11 || !_dataflow_eq_valid_11) && _dataflow_counter_ready_2 && _dataflow_counter_valid_2) begin
        _dataflow_eq_data_11 <= _dataflow_counter_data_2 == 4'sd4;
      end 
      if(_dataflow_eq_valid_11 && _dataflow_eq_ready_11) begin
        _dataflow_eq_valid_11 <= 0;
      end 
      if((_dataflow_eq_ready_11 || !_dataflow_eq_valid_11) && _dataflow_counter_ready_2) begin
        _dataflow_eq_valid_11 <= _dataflow_counter_valid_2;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow_counter_ready_2 && _dataflow_counter_valid_2) begin
        _dataflow__delay_data_17 <= _dataflow_counter_data_2;
      end 
      if(_dataflow__delay_valid_17 && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_17 <= 0;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow_counter_ready_2) begin
        _dataflow__delay_valid_17 <= _dataflow_counter_valid_2;
      end 
      if((_dataflow_counter_ready_7 || !_dataflow_counter_valid_7) && _dataflow_eq_ready_4 && _dataflow_eq_valid_4 && _dataflow_eq_data_4) begin
        _dataflow_counter_data_7 <= _dataflow_counter_data_7 + 1;
      end 
      if(_dataflow_counter_valid_7 && _dataflow_counter_ready_7) begin
        _dataflow_counter_valid_7 <= 0;
      end 
      if((_dataflow_counter_ready_7 || !_dataflow_counter_valid_7) && _dataflow_eq_ready_4) begin
        _dataflow_counter_valid_7 <= _dataflow_eq_valid_4;
      end 
      if((_dataflow_or_ready_13 || !_dataflow_or_valid_13) && (_dataflow_eq_ready_9 && _dataflow_eq_ready_11) && (_dataflow_eq_valid_9 && _dataflow_eq_valid_11)) begin
        _dataflow_or_data_13 <= _dataflow_eq_data_9 | _dataflow_eq_data_11;
      end 
      if(_dataflow_or_valid_13 && _dataflow_or_ready_13) begin
        _dataflow_or_valid_13 <= 0;
      end 
      if((_dataflow_or_ready_13 || !_dataflow_or_valid_13) && (_dataflow_eq_ready_9 && _dataflow_eq_ready_11)) begin
        _dataflow_or_valid_13 <= _dataflow_eq_valid_9 && _dataflow_eq_valid_11;
      end 
      if((_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_ready_17 && _dataflow__delay_valid_17) begin
        _dataflow__delay_data_18 <= _dataflow__delay_data_17;
      end 
      if(_dataflow__delay_valid_18 && _dataflow__delay_ready_18) begin
        _dataflow__delay_valid_18 <= 0;
      end 
      if((_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_18 <= _dataflow__delay_valid_17;
      end 
      if((_dataflow_counter_ready_15 || !_dataflow_counter_valid_15) && _dataflow_or_ready_13 && _dataflow_or_valid_13 && _dataflow_or_data_13) begin
        _dataflow_counter_data_15 <= _dataflow_counter_data_15 + 1;
      end 
      if(_dataflow_counter_valid_15 && _dataflow_counter_ready_15) begin
        _dataflow_counter_valid_15 <= 0;
      end 
      if((_dataflow_counter_ready_15 || !_dataflow_counter_valid_15) && _dataflow_or_ready_13) begin
        _dataflow_counter_valid_15 <= _dataflow_or_valid_13;
      end 
      if((_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_ready_18 && _dataflow__delay_valid_18) begin
        _dataflow__delay_data_19 <= _dataflow__delay_data_18;
      end 
      if(_dataflow__delay_valid_19 && _dataflow__delay_ready_19) begin
        _dataflow__delay_valid_19 <= 0;
      end 
      if((_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_ready_18) begin
        _dataflow__delay_valid_19 <= _dataflow__delay_valid_18;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow_counter_ready_7 && _dataflow_counter_valid_7) begin
        _dataflow__delay_data_20 <= _dataflow_counter_data_7;
      end 
      if(_dataflow__delay_valid_20 && _dataflow__delay_ready_20) begin
        _dataflow__delay_valid_20 <= 0;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow_counter_ready_7) begin
        _dataflow__delay_valid_20 <= _dataflow_counter_valid_7;
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
