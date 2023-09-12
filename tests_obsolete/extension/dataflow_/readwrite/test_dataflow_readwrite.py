from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_readwrite

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
    $dumpfile("dataflow_readwrite.vcd");
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

  reg [32-1:0] xdata;
  reg xvalid;
  wire xready;
  wire [32-1:0] ydata;
  wire yvalid;
  wire yready;
  reg [32-1:0] _dataflow_plus_data_2;
  reg _dataflow_plus_valid_2;
  wire _dataflow_plus_ready_2;
  assign xready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid);
  assign yready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid);
  wire [32-1:0] zdata;
  wire zvalid;
  wire zready;
  assign zdata = _dataflow_plus_data_2;
  assign zvalid = _dataflow_plus_valid_2;
  assign _dataflow_plus_ready_2 = zready;
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg __dataflow_seq_0_cond_0_1;
  localparam xfsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          if(xready || !xvalid) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((xready || !xvalid) && (_tmp_0 == 15)) begin
            xfsm <= xfsm_1;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  assign ydata = _tmp_2;
  reg _tmp_3;
  assign yvalid = _tmp_3;
  reg __dataflow_seq_0_cond_1_1;
  localparam yfsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
      _tmp_1 <= 0;
    end else begin
      case(yfsm)
        yfsm_init: begin
          if(yready || !_tmp_3) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((yready || !_tmp_3) && (_tmp_1 == 15)) begin
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
      _dataflow_plus_data_2 <= 0;
      _dataflow_plus_valid_2 <= 0;
      xdata <= 0;
      xvalid <= 0;
      __dataflow_seq_0_cond_0_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      __dataflow_seq_0_cond_1_1 <= 0;
    end else begin
      if(__dataflow_seq_0_cond_0_1) begin
        xvalid <= 0;
      end 
      if(__dataflow_seq_0_cond_1_1) begin
        _tmp_3 <= 0;
      end 
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready) && (xvalid && yvalid)) begin
        _dataflow_plus_data_2 <= xdata + ydata;
      end 
      if(_dataflow_plus_valid_2 && _dataflow_plus_ready_2) begin
        _dataflow_plus_valid_2 <= 0;
      end 
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready)) begin
        _dataflow_plus_valid_2 <= xvalid && yvalid;
      end 
      if((xfsm == 0) && (xready || !xvalid)) begin
        xdata <= _tmp_0;
      end 
      if((xfsm == 0) && (xready || !xvalid)) begin
        xvalid <= 1;
      end 
      __dataflow_seq_0_cond_0_1 <= 1;
      if(xvalid && !xready) begin
        xvalid <= xvalid;
      end 
      if((yfsm == 0) && (yready || !_tmp_3)) begin
        _tmp_2 <= _tmp_1;
      end 
      if((yfsm == 0) && (yready || !_tmp_3)) begin
        _tmp_3 <= 1;
      end 
      __dataflow_seq_0_cond_1_1 <= 1;
      if(_tmp_3 && !yready) begin
        _tmp_3 <= _tmp_3;
      end 
    end
  end


endmodule

"""


def test():
    veriloggen.reset()
    test_module = dataflow_readwrite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
