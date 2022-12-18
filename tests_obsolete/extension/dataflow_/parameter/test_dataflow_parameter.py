from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_parameter

expected_verilog = """

module test #
(
  parameter xparam = 100,
  parameter signed [32-1:0] aparam = 10
)
(

);

  reg CLK;
  reg RST;

  main
  #(
    .xparam(xparam),
    .aparam(aparam)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    $dumpfile("dataflow_parameter.vcd");
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



module main #
(
  parameter xparam = 100,
  parameter signed [32-1:0] aparam = 10
)
(
  input CLK,
  input RST
);

  reg [32-1:0] yparam;
  wire signed [32-1:0] bparam;
  wire signed [32-1:0] vdata;
  wire signed [32-1:0] wdata;
  reg signed [32-1:0] _dataflow_plus_data_7;
  reg _dataflow_plus_valid_7;
  wire _dataflow_plus_ready_7;
  reg signed [32-1:0] _dataflow__delay_data_15;
  reg _dataflow__delay_valid_15;
  wire _dataflow__delay_ready_15;
  reg signed [32-1:0] _dataflow_plus_data_8;
  reg _dataflow_plus_valid_8;
  wire _dataflow_plus_ready_8;
  assign _dataflow_plus_ready_7 = (_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && _dataflow_plus_valid_7;
  reg signed [32-1:0] _dataflow__delay_data_16;
  reg _dataflow__delay_valid_16;
  wire _dataflow__delay_ready_16;
  assign _dataflow__delay_ready_15 = (_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow__delay_valid_15;
  reg signed [32-1:0] _dataflow_plus_data_9;
  reg _dataflow_plus_valid_9;
  wire _dataflow_plus_ready_9;
  assign _dataflow_plus_ready_8 = (_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && _dataflow_plus_valid_8;
  reg signed [32-1:0] _dataflow__delay_data_17;
  reg _dataflow__delay_valid_17;
  wire _dataflow__delay_ready_17;
  assign _dataflow__delay_ready_16 = (_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow__delay_valid_16;
  reg signed [32-1:0] _dataflow_plus_data_10;
  reg _dataflow_plus_valid_10;
  wire _dataflow_plus_ready_10;
  assign _dataflow_plus_ready_9 = (_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && _dataflow_plus_valid_9;
  reg signed [32-1:0] _dataflow__delay_data_18;
  reg _dataflow__delay_valid_18;
  wire _dataflow__delay_ready_18;
  assign _dataflow__delay_ready_17 = (_dataflow__delay_ready_18 || !_dataflow__delay_valid_18) && _dataflow__delay_valid_17;
  reg signed [32-1:0] _dataflow_plus_data_11;
  reg _dataflow_plus_valid_11;
  wire _dataflow_plus_ready_11;
  assign _dataflow_plus_ready_10 = (_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && _dataflow_plus_valid_10;
  reg signed [32-1:0] _dataflow__delay_data_19;
  reg _dataflow__delay_valid_19;
  wire _dataflow__delay_ready_19;
  assign _dataflow__delay_ready_18 = (_dataflow__delay_ready_19 || !_dataflow__delay_valid_19) && _dataflow__delay_valid_18;
  reg signed [32-1:0] _dataflow_plus_data_13;
  reg _dataflow_plus_valid_13;
  wire _dataflow_plus_ready_13;
  assign _dataflow_plus_ready_11 = (_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && _dataflow_plus_valid_11;
  reg signed [32-1:0] _dataflow__delay_data_20;
  reg _dataflow__delay_valid_20;
  wire _dataflow__delay_ready_20;
  assign _dataflow__delay_ready_19 = (_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_valid_19;
  reg signed [32-1:0] _dataflow_plus_data_14;
  reg _dataflow_plus_valid_14;
  wire _dataflow_plus_ready_14;
  assign _dataflow_plus_ready_13 = (_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_valid_13 && _dataflow__delay_valid_20);
  assign _dataflow__delay_ready_20 = (_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_valid_13 && _dataflow__delay_valid_20);
  wire signed [32-1:0] cdata;
  wire cvalid;
  assign cdata = _dataflow_plus_data_14;
  assign cvalid = _dataflow_plus_valid_14;
  assign _dataflow_plus_ready_14 = 1;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_0;
  assign bparam = 20;
  assign vdata = 1000;
  assign wdata = 2000;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      yparam <= 0;
      _tmp_0 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          yparam <= 200;
          fsm <= fsm_1;
        end
        fsm_1: begin
          if(cvalid) begin
            _tmp_0 <= _tmp_0 + 1;
            $display("c=%d", cdata);
          end 
          if(_tmp_0 == 4) begin
            fsm <= fsm_2;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _dataflow_plus_data_7 <= 0;
      _dataflow_plus_valid_7 <= 0;
      _dataflow__delay_data_15 <= 0;
      _dataflow__delay_valid_15 <= 0;
      _dataflow_plus_data_8 <= 0;
      _dataflow_plus_valid_8 <= 0;
      _dataflow__delay_data_16 <= 0;
      _dataflow__delay_valid_16 <= 0;
      _dataflow_plus_data_9 <= 0;
      _dataflow_plus_valid_9 <= 0;
      _dataflow__delay_data_17 <= 0;
      _dataflow__delay_valid_17 <= 0;
      _dataflow_plus_data_10 <= 0;
      _dataflow_plus_valid_10 <= 0;
      _dataflow__delay_data_18 <= 0;
      _dataflow__delay_valid_18 <= 0;
      _dataflow_plus_data_11 <= 0;
      _dataflow_plus_valid_11 <= 0;
      _dataflow__delay_data_19 <= 0;
      _dataflow__delay_valid_19 <= 0;
      _dataflow_plus_data_13 <= 0;
      _dataflow_plus_valid_13 <= 0;
      _dataflow__delay_data_20 <= 0;
      _dataflow__delay_valid_20 <= 0;
      _dataflow_plus_data_14 <= 0;
      _dataflow_plus_valid_14 <= 0;
    end else begin
      if((_dataflow_plus_ready_7 || !_dataflow_plus_valid_7) && 1 && 1) begin
        _dataflow_plus_data_7 <= vdata + aparam;
      end 
      if(_dataflow_plus_valid_7 && _dataflow_plus_ready_7) begin
        _dataflow_plus_valid_7 <= 0;
      end 
      if((_dataflow_plus_ready_7 || !_dataflow_plus_valid_7) && 1) begin
        _dataflow_plus_valid_7 <= 1;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && 1 && 1) begin
        _dataflow__delay_data_15 <= wdata;
      end 
      if(_dataflow__delay_valid_15 && _dataflow__delay_ready_15) begin
        _dataflow__delay_valid_15 <= 0;
      end 
      if((_dataflow__delay_ready_15 || !_dataflow__delay_valid_15) && 1) begin
        _dataflow__delay_valid_15 <= 1;
      end 
      if((_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && _dataflow_plus_ready_7 && _dataflow_plus_valid_7) begin
        _dataflow_plus_data_8 <= _dataflow_plus_data_7 + bparam;
      end 
      if(_dataflow_plus_valid_8 && _dataflow_plus_ready_8) begin
        _dataflow_plus_valid_8 <= 0;
      end 
      if((_dataflow_plus_ready_8 || !_dataflow_plus_valid_8) && _dataflow_plus_ready_7) begin
        _dataflow_plus_valid_8 <= _dataflow_plus_valid_7;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow__delay_ready_15 && _dataflow__delay_valid_15) begin
        _dataflow__delay_data_16 <= _dataflow__delay_data_15;
      end 
      if(_dataflow__delay_valid_16 && _dataflow__delay_ready_16) begin
        _dataflow__delay_valid_16 <= 0;
      end 
      if((_dataflow__delay_ready_16 || !_dataflow__delay_valid_16) && _dataflow__delay_ready_15) begin
        _dataflow__delay_valid_16 <= _dataflow__delay_valid_15;
      end 
      if((_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && _dataflow_plus_ready_8 && _dataflow_plus_valid_8) begin
        _dataflow_plus_data_9 <= _dataflow_plus_data_8 + xparam;
      end 
      if(_dataflow_plus_valid_9 && _dataflow_plus_ready_9) begin
        _dataflow_plus_valid_9 <= 0;
      end 
      if((_dataflow_plus_ready_9 || !_dataflow_plus_valid_9) && _dataflow_plus_ready_8) begin
        _dataflow_plus_valid_9 <= _dataflow_plus_valid_8;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow__delay_ready_16 && _dataflow__delay_valid_16) begin
        _dataflow__delay_data_17 <= _dataflow__delay_data_16;
      end 
      if(_dataflow__delay_valid_17 && _dataflow__delay_ready_17) begin
        _dataflow__delay_valid_17 <= 0;
      end 
      if((_dataflow__delay_ready_17 || !_dataflow__delay_valid_17) && _dataflow__delay_ready_16) begin
        _dataflow__delay_valid_17 <= _dataflow__delay_valid_16;
      end 
      if((_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && _dataflow_plus_ready_9 && _dataflow_plus_valid_9) begin
        _dataflow_plus_data_10 <= _dataflow_plus_data_9 + yparam;
      end 
      if(_dataflow_plus_valid_10 && _dataflow_plus_ready_10) begin
        _dataflow_plus_valid_10 <= 0;
      end 
      if((_dataflow_plus_ready_10 || !_dataflow_plus_valid_10) && _dataflow_plus_ready_9) begin
        _dataflow_plus_valid_10 <= _dataflow_plus_valid_9;
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
      if((_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && _dataflow_plus_ready_10 && _dataflow_plus_valid_10) begin
        _dataflow_plus_data_11 <= _dataflow_plus_data_10 + 2'sd1;
      end 
      if(_dataflow_plus_valid_11 && _dataflow_plus_ready_11) begin
        _dataflow_plus_valid_11 <= 0;
      end 
      if((_dataflow_plus_ready_11 || !_dataflow_plus_valid_11) && _dataflow_plus_ready_10) begin
        _dataflow_plus_valid_11 <= _dataflow_plus_valid_10;
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
      if((_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && _dataflow_plus_ready_11 && _dataflow_plus_valid_11) begin
        _dataflow_plus_data_13 <= _dataflow_plus_data_11 + 32'd30;
      end 
      if(_dataflow_plus_valid_13 && _dataflow_plus_ready_13) begin
        _dataflow_plus_valid_13 <= 0;
      end 
      if((_dataflow_plus_ready_13 || !_dataflow_plus_valid_13) && _dataflow_plus_ready_11) begin
        _dataflow_plus_valid_13 <= _dataflow_plus_valid_11;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_ready_19 && _dataflow__delay_valid_19) begin
        _dataflow__delay_data_20 <= _dataflow__delay_data_19;
      end 
      if(_dataflow__delay_valid_20 && _dataflow__delay_ready_20) begin
        _dataflow__delay_valid_20 <= 0;
      end 
      if((_dataflow__delay_ready_20 || !_dataflow__delay_valid_20) && _dataflow__delay_ready_19) begin
        _dataflow__delay_valid_20 <= _dataflow__delay_valid_19;
      end 
      if((_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_ready_13 && _dataflow__delay_ready_20) && (_dataflow_plus_valid_13 && _dataflow__delay_valid_20)) begin
        _dataflow_plus_data_14 <= _dataflow_plus_data_13 + _dataflow__delay_data_20;
      end 
      if(_dataflow_plus_valid_14 && _dataflow_plus_ready_14) begin
        _dataflow_plus_valid_14 <= 0;
      end 
      if((_dataflow_plus_ready_14 || !_dataflow_plus_valid_14) && (_dataflow_plus_ready_13 && _dataflow__delay_ready_20)) begin
        _dataflow_plus_valid_14 <= _dataflow_plus_valid_13 && _dataflow__delay_valid_20;
      end 
    end
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_parameter.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
