from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_alias

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

  wire [32-1:0] xdata;
  wire xvalid;
  wire xready;
  reg [32-1:0] _dataflow_plus_data_3;
  reg _dataflow_plus_valid_3;
  wire _dataflow_plus_ready_3;
  assign xready = (_dataflow_plus_ready_3 || !_dataflow_plus_valid_3) && xvalid;
  reg [32-1:0] _dataflow_plus_data_5;
  reg _dataflow_plus_valid_5;
  wire _dataflow_plus_ready_5;
  reg [32-1:0] _dataflow__delay_data_7;
  reg _dataflow__delay_valid_7;
  wire _dataflow__delay_ready_7;
  assign _dataflow_plus_ready_3 = (_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && _dataflow_plus_valid_3 && ((_dataflow__delay_ready_7 || !_dataflow__delay_valid_7) && _dataflow_plus_valid_3);
  wire [32-1:0] zdata;
  wire zvalid;
  wire zready;
  assign zdata = _dataflow_plus_data_5;
  assign zvalid = _dataflow_plus_valid_5;
  assign _dataflow_plus_ready_5 = zready;
  wire [32-1:0] ydata;
  wire yvalid;
  wire yready;
  assign ydata = _dataflow__delay_data_7;
  assign yvalid = _dataflow__delay_valid_7;
  assign _dataflow__delay_ready_7 = yready;
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  assign xdata = _tmp_1;
  reg _tmp_2;
  assign xvalid = _tmp_2;
  reg __dataflow_seq_0_cond_0_1;
  localparam xfsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          if(xready || !_tmp_2) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((xready || !_tmp_2) && (_tmp_0 == 15)) begin
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
      _dataflow_plus_data_3 <= 0;
      _dataflow_plus_valid_3 <= 0;
      _dataflow_plus_data_5 <= 0;
      _dataflow_plus_valid_5 <= 0;
      _dataflow__delay_data_7 <= 0;
      _dataflow__delay_valid_7 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      __dataflow_seq_0_cond_0_1 <= 0;
    end else begin
      if(__dataflow_seq_0_cond_0_1) begin
        _tmp_2 <= 0;
      end 
      if((_dataflow_plus_ready_3 || !_dataflow_plus_valid_3) && xready && xvalid) begin
        _dataflow_plus_data_3 <= xdata + 2'sd1;
      end 
      if(_dataflow_plus_valid_3 && _dataflow_plus_ready_3) begin
        _dataflow_plus_valid_3 <= 0;
      end 
      if((_dataflow_plus_ready_3 || !_dataflow_plus_valid_3) && xready) begin
        _dataflow_plus_valid_3 <= xvalid;
      end 
      if((_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && _dataflow_plus_ready_3 && _dataflow_plus_valid_3) begin
        _dataflow_plus_data_5 <= _dataflow_plus_data_3 + 2'sd1;
      end 
      if(_dataflow_plus_valid_5 && _dataflow_plus_ready_5) begin
        _dataflow_plus_valid_5 <= 0;
      end 
      if((_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && _dataflow_plus_ready_3) begin
        _dataflow_plus_valid_5 <= _dataflow_plus_valid_3;
      end 
      if((_dataflow__delay_ready_7 || !_dataflow__delay_valid_7) && _dataflow_plus_ready_3 && _dataflow_plus_valid_3) begin
        _dataflow__delay_data_7 <= _dataflow_plus_data_3;
      end 
      if(_dataflow__delay_valid_7 && _dataflow__delay_ready_7) begin
        _dataflow__delay_valid_7 <= 0;
      end 
      if((_dataflow__delay_ready_7 || !_dataflow__delay_valid_7) && _dataflow_plus_ready_3) begin
        _dataflow__delay_valid_7 <= _dataflow_plus_valid_3;
      end 
      if((xfsm == 0) && (xready || !_tmp_2)) begin
        _tmp_1 <= _tmp_0;
      end 
      if((xfsm == 0) && (xready || !_tmp_2)) begin
        _tmp_2 <= 1;
      end 
      __dataflow_seq_0_cond_0_1 <= 1;
      if(_tmp_2 && !xready) begin
        _tmp_2 <= _tmp_2;
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
