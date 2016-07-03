from __future__ import absolute_import
from __future__ import print_function
import dataflow_getio


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
  wire [32-1:0] ydata;
  wire yvalid;
  wire yready;
  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign xready = (_tmp_ready_0 || !_tmp_valid_0) && (xvalid && yvalid);
  assign yready = (_tmp_ready_0 || !_tmp_valid_0) && (xvalid && yvalid);
  wire [32-1:0] zdata;
  wire zvalid;
  wire zready;
  assign zdata = _tmp_data_0;
  assign zvalid = _tmp_valid_0;
  assign _tmp_ready_0 = zready;
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  assign xdata = _tmp_2;
  reg _tmp_3;
  assign xvalid = _tmp_3;
  reg _seq_cond_0_1;
  localparam xfsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_1 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          if(xready || !_tmp_3) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((xready || !_tmp_3) && (_tmp_1 == 15)) begin
            xfsm <= xfsm_1;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] _tmp_4;
  reg [32-1:0] _tmp_5;
  assign ydata = _tmp_5;
  reg _tmp_6;
  assign yvalid = _tmp_6;
  reg _seq_cond_1_1;
  localparam yfsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
      _tmp_4 <= 0;
    end else begin
      case(yfsm)
        yfsm_init: begin
          if(yready || !_tmp_6) begin
            _tmp_4 <= _tmp_4 + 1;
          end 
          if((yready || !_tmp_6) && (_tmp_4 == 15)) begin
            yfsm <= yfsm_1;
          end 
        end
      endcase
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
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _seq_cond_0_1 <= 0;
      _tmp_5 <= 0;
      _tmp_6 <= 0;
      _seq_cond_1_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        _tmp_3 <= 0;
      end 
      if(_seq_cond_1_1) begin
        _tmp_6 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && (xready && yready) && (xvalid && yvalid)) begin
        _tmp_data_0 <= xdata + ydata;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && (xready && yready)) begin
        _tmp_valid_0 <= xvalid && yvalid;
      end 
      if((xfsm == 0) && (xready || !_tmp_3)) begin
        _tmp_2 <= _tmp_1;
      end 
      if((xfsm == 0) && (xready || !_tmp_3)) begin
        _tmp_3 <= 1;
      end 
      _seq_cond_0_1 <= 1;
      if(_tmp_3 && !xready) begin
        _tmp_3 <= _tmp_3;
      end 
      if((yfsm == 0) && (yready || !_tmp_6)) begin
        _tmp_5 <= _tmp_4;
      end 
      if((yfsm == 0) && (yready || !_tmp_6)) begin
        _tmp_6 <= 1;
      end 
      _seq_cond_1_1 <= 1;
      if(_tmp_6 && !yready) begin
        _tmp_6 <= _tmp_6;
      end 
    end
  end


endmodule
"""

def test():
    test_module = dataflow_getio.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
