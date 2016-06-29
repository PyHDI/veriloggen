from __future__ import absolute_import
from __future__ import print_function
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

  reg [8-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign _tmp_ready_0 = (_tmp_ready_2 || !_tmp_valid_2) && (_tmp_valid_0 && _tmp_valid_1);
  reg [8-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign _tmp_ready_1 = (_tmp_ready_2 || !_tmp_valid_2) && (_tmp_valid_0 && _tmp_valid_1);
  reg [8-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign cdata = _tmp_data_2;
  assign cvalid = _tmp_valid_2;
  assign _tmp_ready_2 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 1'd0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 1'd0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
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
      if((_tmp_ready_1 || !_tmp_valid_1) && 1 && 1) begin
        _tmp_data_1 <= (_tmp_data_1 >= 14)? 0 : _tmp_data_1 + 3'd2;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1) begin
        _tmp_valid_1 <= 1;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && (_tmp_ready_0 && _tmp_ready_1) && (_tmp_valid_0 && _tmp_valid_1)) begin
        _tmp_data_2 <= _tmp_data_0 + _tmp_data_1;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && (_tmp_ready_0 && _tmp_ready_1)) begin
        _tmp_valid_2 <= _tmp_valid_0 && _tmp_valid_1;
      end 
    end
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_3;
  localparam fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _tmp_3 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(cvalid) begin
            _tmp_3 <= _tmp_3 + 1;
            $display("c=%d", cdata);
          end 
          if(_tmp_3 == 32) begin
            fsm <= fsm_1;
          end 
        end
      endcase
    end
  end


endmodule
"""

def test():
    test_module = dataflow_counter.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
