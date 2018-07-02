from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_counter

expected_verilog = """

module test
(

);

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

  reg [8-1:0] _dataflow_counter_data_2;
  reg _dataflow_counter_valid_2;
  wire _dataflow_counter_ready_2;
  reg [6-1:0] _dataflow_counter_count_2;
  reg [8-1:0] _dataflow_counter_data_6;
  reg _dataflow_counter_valid_6;
  wire _dataflow_counter_ready_6;
  reg [7-1:0] _dataflow_counter_count_6;
  reg [8-1:0] _dataflow_plus_data_8;
  reg _dataflow_plus_valid_8;
  wire _dataflow_plus_ready_8;
  assign _dataflow_counter_ready_2 = (_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && (_dataflow_counter_valid_2 && _dataflow_counter_valid_6);
  assign _dataflow_counter_ready_6 = (_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && (_dataflow_counter_valid_2 && _dataflow_counter_valid_6);
  assign cdata = _dataflow_plus_data_8;
  assign cvalid = _dataflow_plus_valid_8;
  assign _dataflow_plus_ready_8 = 1;
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
      _dataflow_counter_data_2 <= -2'sd1;
      _dataflow_counter_count_2 <= 0;
      _dataflow_counter_valid_2 <= 0;
      _dataflow_counter_data_6 <= -3'sd2;
      _dataflow_counter_count_6 <= 0;
      _dataflow_counter_valid_6 <= 0;
      _dataflow_plus_data_8 <= 0;
      _dataflow_plus_valid_8 <= 0;
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
      if((_dataflow_counter_ready_6 || !_dataflow_counter_valid_6) && 1 && 1) begin
        _dataflow_counter_data_6 <= _dataflow_counter_data_6 + 2;
      end 
      if((_dataflow_counter_ready_6 || !_dataflow_counter_valid_6) && 1 && 1) begin
        _dataflow_counter_count_6 <= (_dataflow_counter_count_6 == 6'sd16 - 1)? 0 : _dataflow_counter_count_6 + 1;
      end 
      if(_dataflow_counter_valid_6 && _dataflow_counter_ready_6) begin
        _dataflow_counter_valid_6 <= 0;
      end 
      if((_dataflow_counter_ready_6 || !_dataflow_counter_valid_6) && 1) begin
        _dataflow_counter_valid_6 <= 1;
      end 
      if((_dataflow_counter_ready_6 || !_dataflow_counter_valid_6) && 1 && 1 && (_dataflow_counter_count_6 == 0)) begin
        _dataflow_counter_data_6 <= -3'sd2 + 2;
      end 
      if((_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && (_dataflow_counter_ready_2 && _dataflow_counter_ready_6) && (_dataflow_counter_valid_2 && _dataflow_counter_valid_6)) begin
        _dataflow_plus_data_8 <= _dataflow_counter_data_2 + _dataflow_counter_data_6;
      end 
      if(_dataflow_plus_valid_8 && _dataflow_plus_ready_8) begin
        _dataflow_plus_valid_8 <= 0;
      end 
      if((_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && (_dataflow_counter_ready_2 && _dataflow_counter_ready_6)) begin
        _dataflow_plus_valid_8 <= _dataflow_counter_valid_2 && _dataflow_counter_valid_6;
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
