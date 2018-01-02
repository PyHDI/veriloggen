from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_counter

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] cdata;
  wire cvalid;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .cdata(cdata),
    .cvalid(cvalid)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, cdata, cvalid);
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
  input RST,
  output [8-1:0] cdata,
  output cvalid
);

  reg [8-1:0] _counter_data_0;
  reg _counter_valid_0;
  wire _counter_ready_0;
  reg [6-1:0] _counter_count_0;
  reg [8-1:0] _counter_data_1;
  reg _counter_valid_1;
  wire _counter_ready_1;
  reg [7-1:0] _counter_count_1;
  reg [8-1:0] _plus_data_2;
  reg _plus_valid_2;
  wire _plus_ready_2;
  assign _counter_ready_0 = (_plus_ready_2 || !_plus_valid_2) && (_counter_valid_0 && _counter_valid_1);
  assign _counter_ready_1 = (_plus_ready_2 || !_plus_valid_2) && (_counter_valid_0 && _counter_valid_1);
  assign cdata = _plus_data_2;
  assign cvalid = _plus_valid_2;
  assign _plus_ready_2 = 1;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] count;
  localparam fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      count <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(cvalid) begin
            count <= count + 1;
            $display("c=%d", cdata);
          end 
          if(count == 32) begin
            fsm <= fsm_1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _counter_data_0 <= -2'sd1;
      _counter_count_0 <= 0;
      _counter_valid_0 <= 0;
      _counter_data_1 <= -3'sd2;
      _counter_count_1 <= 0;
      _counter_valid_1 <= 0;
      _plus_data_2 <= 0;
      _plus_valid_2 <= 0;
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
      if((_counter_ready_1 || !_counter_valid_1) && 1 && 1) begin
        _counter_data_1 <= _counter_data_1 + 2;
      end 
      if((_counter_ready_1 || !_counter_valid_1) && 1 && 1) begin
        _counter_count_1 <= (_counter_count_1 == 6'sd16 - 1)? 0 : _counter_count_1 + 1;
      end 
      if(_counter_valid_1 && _counter_ready_1) begin
        _counter_valid_1 <= 0;
      end 
      if((_counter_ready_1 || !_counter_valid_1) && 1) begin
        _counter_valid_1 <= 1;
      end 
      if((_counter_ready_1 || !_counter_valid_1) && 1 && 1 && (_counter_count_1 == 0)) begin
        _counter_data_1 <= -3'sd2 + 2;
      end 
      if((_plus_ready_2 || !_plus_valid_2) && (_counter_ready_0 && _counter_ready_1) && (_counter_valid_0 && _counter_valid_1)) begin
        _plus_data_2 <= _counter_data_0 + _counter_data_1;
      end 
      if(_plus_valid_2 && _plus_ready_2) begin
        _plus_valid_2 <= 0;
      end 
      if((_plus_ready_2 || !_plus_valid_2) && (_counter_ready_0 && _counter_ready_1)) begin
        _plus_valid_2 <= _counter_valid_0 && _counter_valid_1;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = dataflow_counter.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
