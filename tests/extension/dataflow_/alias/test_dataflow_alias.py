from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_alias

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

  wire [32-1:0] xdata;
  wire xvalid;
  wire xready;
  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign xready = (_tmp_ready_0 || !_tmp_valid_0) && xvalid;
  assign _tmp_ready_0 = (_tmp_ready_1 || !_tmp_valid_1) && _tmp_valid_0 && ((_tmp_ready_2 || !_tmp_valid_2) && _tmp_valid_0);
  reg [32-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  reg [32-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  wire [32-1:0] zdata;
  wire zvalid;
  wire zready;
  assign zdata = _tmp_data_1;
  assign zvalid = _tmp_valid_1;
  assign _tmp_ready_1 = zready;
  wire [32-1:0] ydata;
  wire yvalid;
  wire yready;
  assign ydata = _tmp_data_2;
  assign yvalid = _tmp_valid_2;
  assign _tmp_ready_2 = yready;
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _tmp_4;
  assign xdata = _tmp_4;
  reg _tmp_5;
  assign xvalid = _tmp_5;
  reg __dataflow_seq_0_cond_0_1;
  localparam xfsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_3 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          if(xready || !_tmp_5) begin
            _tmp_3 <= _tmp_3 + 1;
          end 
          if((xready || !_tmp_5) && (_tmp_3 == 15)) begin
            xfsm <= xfsm_1;
          end 
        end
      endcase
    end
  end

  assign yready = 1;

  always @(posedge CLK) begin
    if(yvalid) begin
      $display("ydata=%d", ydata);
    end 
  end

  assign zready = 1;

  always @(posedge CLK) begin
    if(zvalid) begin
      $display("zdata=%d", zdata);
    end 
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_valid_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
      _tmp_4 <= 0;
      _tmp_5 <= 0;
      __dataflow_seq_0_cond_0_1 <= 0;
    end else begin
      if(__dataflow_seq_0_cond_0_1) begin
        _tmp_5 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && xready && xvalid) begin
        _tmp_data_0 <= xdata + 2'd1;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && xready) begin
        _tmp_valid_0 <= xvalid;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_1 <= _tmp_data_0 + 2'd1;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && _tmp_ready_0) begin
        _tmp_valid_1 <= _tmp_valid_0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_0 && _tmp_valid_0) begin
        _tmp_data_2 <= _tmp_data_0;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_0) begin
        _tmp_valid_2 <= _tmp_valid_0;
      end 
      if((xfsm == 0) && (xready || !_tmp_5)) begin
        _tmp_4 <= _tmp_3;
      end 
      if((xfsm == 0) && (xready || !_tmp_5)) begin
        _tmp_5 <= 1;
      end 
      __dataflow_seq_0_cond_0_1 <= 1;
      if(_tmp_5 && !xready) begin
        _tmp_5 <= _tmp_5;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = dataflow_alias.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
