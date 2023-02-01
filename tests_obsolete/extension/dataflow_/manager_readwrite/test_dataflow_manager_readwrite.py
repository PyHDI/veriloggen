from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_manager_readwrite

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
    $dumpfile("dataflow_manager_readwrite.vcd");
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
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  reg __dataflow_seq_0_cond_0_1;
  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] _tmp_1;
  wire [32-1:0] ydata;
  wire yvalid;
  wire yready;
  reg [32-1:0] _tmp_2;
  assign ydata = _tmp_2;
  reg _tmp_3;
  assign yvalid = _tmp_3;
  reg __dataflow_seq_0_cond_1_1;
  wire [32-1:0] adata;
  wire avalid;
  wire aready;
  assign aready = 1;
  wire [32-1:0] bdata;
  wire bvalid;
  wire bready;
  assign bready = 1;
  reg [32-1:0] _dataflow_plus_data_2;
  reg _dataflow_plus_valid_2;
  wire _dataflow_plus_ready_2;
  reg [32-1:0] _dataflow__delay_data_7;
  reg _dataflow__delay_valid_7;
  wire _dataflow__delay_ready_7;
  assign xready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid) && ((_dataflow__delay_ready_7 || !_dataflow__delay_valid_7) && xvalid);
  reg [32-1:0] _dataflow__delay_data_9;
  reg _dataflow__delay_valid_9;
  wire _dataflow__delay_ready_9;
  assign yready = (_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xvalid && yvalid) && ((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && yvalid);
  reg [32-1:0] _dataflow_plus_data_3;
  reg _dataflow_plus_valid_3;
  wire _dataflow_plus_ready_3;
  assign _dataflow_plus_ready_2 = (_dataflow_plus_ready_3 || !_dataflow_plus_valid_3) && _dataflow_plus_valid_2;
  reg [32-1:0] _dataflow__delay_data_8;
  reg _dataflow__delay_valid_8;
  wire _dataflow__delay_ready_8;
  assign _dataflow__delay_ready_7 = (_dataflow__delay_ready_8 || !_dataflow__delay_valid_8) && _dataflow__delay_valid_7;
  reg [32-1:0] _dataflow__delay_data_10;
  reg _dataflow__delay_valid_10;
  wire _dataflow__delay_ready_10;
  assign _dataflow__delay_ready_9 = (_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && _dataflow__delay_valid_9;
  reg [32-1:0] _dataflow_plus_data_5;
  reg _dataflow_plus_valid_5;
  wire _dataflow_plus_ready_5;
  assign _dataflow__delay_ready_8 = (_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && (_dataflow_plus_valid_3 && _dataflow__delay_valid_8);
  reg [32-1:0] _dataflow__delay_data_11;
  reg _dataflow__delay_valid_11;
  wire _dataflow__delay_ready_11;
  assign _dataflow__delay_ready_10 = (_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_valid_10;
  reg [32-1:0] _dataflow__delay_data_12;
  reg _dataflow__delay_valid_12;
  wire _dataflow__delay_ready_12;
  assign _dataflow_plus_ready_3 = (_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && (_dataflow_plus_valid_3 && _dataflow__delay_valid_8) && ((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow_plus_valid_3);
  reg [32-1:0] _dataflow_plus_data_6;
  reg _dataflow_plus_valid_6;
  wire _dataflow_plus_ready_6;
  assign _dataflow_plus_ready_5 = (_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_valid_5 && _dataflow__delay_valid_11);
  assign _dataflow__delay_ready_11 = (_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_valid_5 && _dataflow__delay_valid_11);
  reg [32-1:0] _dataflow__delay_data_13;
  reg _dataflow__delay_valid_13;
  wire _dataflow__delay_ready_13;
  assign _dataflow__delay_ready_12 = (_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_valid_12;
  assign bdata = _dataflow_plus_data_6;
  assign bvalid = _dataflow_plus_valid_6;
  assign _dataflow_plus_ready_6 = bready;
  assign adata = _dataflow__delay_data_13;
  assign avalid = _dataflow__delay_valid_13;
  assign _dataflow__delay_ready_13 = aready;

  always @(posedge CLK) begin
    if(RST) begin
      xdata <= 0;
      xvalid <= 0;
      __dataflow_seq_0_cond_0_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      __dataflow_seq_0_cond_1_1 <= 0;
      _dataflow_plus_data_2 <= 0;
      _dataflow_plus_valid_2 <= 0;
      _dataflow__delay_data_7 <= 0;
      _dataflow__delay_valid_7 <= 0;
      _dataflow__delay_data_9 <= 0;
      _dataflow__delay_valid_9 <= 0;
      _dataflow_plus_data_3 <= 0;
      _dataflow_plus_valid_3 <= 0;
      _dataflow__delay_data_8 <= 0;
      _dataflow__delay_valid_8 <= 0;
      _dataflow__delay_data_10 <= 0;
      _dataflow__delay_valid_10 <= 0;
      _dataflow_plus_data_5 <= 0;
      _dataflow_plus_valid_5 <= 0;
      _dataflow__delay_data_11 <= 0;
      _dataflow__delay_valid_11 <= 0;
      _dataflow__delay_data_12 <= 0;
      _dataflow__delay_valid_12 <= 0;
      _dataflow_plus_data_6 <= 0;
      _dataflow_plus_valid_6 <= 0;
      _dataflow__delay_data_13 <= 0;
      _dataflow__delay_valid_13 <= 0;
    end else begin
      if(__dataflow_seq_0_cond_0_1) begin
        xvalid <= 0;
      end 
      if(__dataflow_seq_0_cond_1_1) begin
        _tmp_3 <= 0;
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
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready) && (xvalid && yvalid)) begin
        _dataflow_plus_data_2 <= xdata + ydata;
      end 
      if(_dataflow_plus_valid_2 && _dataflow_plus_ready_2) begin
        _dataflow_plus_valid_2 <= 0;
      end 
      if((_dataflow_plus_ready_2 || !_dataflow_plus_valid_2) && (xready && yready)) begin
        _dataflow_plus_valid_2 <= xvalid && yvalid;
      end 
      if((_dataflow__delay_ready_7 || !_dataflow__delay_valid_7) && xready && xvalid) begin
        _dataflow__delay_data_7 <= xdata;
      end 
      if(_dataflow__delay_valid_7 && _dataflow__delay_ready_7) begin
        _dataflow__delay_valid_7 <= 0;
      end 
      if((_dataflow__delay_ready_7 || !_dataflow__delay_valid_7) && xready) begin
        _dataflow__delay_valid_7 <= xvalid;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && yready && yvalid) begin
        _dataflow__delay_data_9 <= ydata;
      end 
      if(_dataflow__delay_valid_9 && _dataflow__delay_ready_9) begin
        _dataflow__delay_valid_9 <= 0;
      end 
      if((_dataflow__delay_ready_9 || !_dataflow__delay_valid_9) && yready) begin
        _dataflow__delay_valid_9 <= yvalid;
      end 
      if((_dataflow_plus_ready_3 || !_dataflow_plus_valid_3) && _dataflow_plus_ready_2 && _dataflow_plus_valid_2) begin
        _dataflow_plus_data_3 <= _dataflow_plus_data_2 + 2'sd1;
      end 
      if(_dataflow_plus_valid_3 && _dataflow_plus_ready_3) begin
        _dataflow_plus_valid_3 <= 0;
      end 
      if((_dataflow_plus_ready_3 || !_dataflow_plus_valid_3) && _dataflow_plus_ready_2) begin
        _dataflow_plus_valid_3 <= _dataflow_plus_valid_2;
      end 
      if((_dataflow__delay_ready_8 || !_dataflow__delay_valid_8) && _dataflow__delay_ready_7 && _dataflow__delay_valid_7) begin
        _dataflow__delay_data_8 <= _dataflow__delay_data_7;
      end 
      if(_dataflow__delay_valid_8 && _dataflow__delay_ready_8) begin
        _dataflow__delay_valid_8 <= 0;
      end 
      if((_dataflow__delay_ready_8 || !_dataflow__delay_valid_8) && _dataflow__delay_ready_7) begin
        _dataflow__delay_valid_8 <= _dataflow__delay_valid_7;
      end 
      if((_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && _dataflow__delay_ready_9 && _dataflow__delay_valid_9) begin
        _dataflow__delay_data_10 <= _dataflow__delay_data_9;
      end 
      if(_dataflow__delay_valid_10 && _dataflow__delay_ready_10) begin
        _dataflow__delay_valid_10 <= 0;
      end 
      if((_dataflow__delay_ready_10 || !_dataflow__delay_valid_10) && _dataflow__delay_ready_9) begin
        _dataflow__delay_valid_10 <= _dataflow__delay_valid_9;
      end 
      if((_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && (_dataflow_plus_ready_3 && _dataflow__delay_ready_8) && (_dataflow_plus_valid_3 && _dataflow__delay_valid_8)) begin
        _dataflow_plus_data_5 <= _dataflow_plus_data_3 + _dataflow__delay_data_8;
      end 
      if(_dataflow_plus_valid_5 && _dataflow_plus_ready_5) begin
        _dataflow_plus_valid_5 <= 0;
      end 
      if((_dataflow_plus_ready_5 || !_dataflow_plus_valid_5) && (_dataflow_plus_ready_3 && _dataflow__delay_ready_8)) begin
        _dataflow_plus_valid_5 <= _dataflow_plus_valid_3 && _dataflow__delay_valid_8;
      end 
      if((_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_ready_10 && _dataflow__delay_valid_10) begin
        _dataflow__delay_data_11 <= _dataflow__delay_data_10;
      end 
      if(_dataflow__delay_valid_11 && _dataflow__delay_ready_11) begin
        _dataflow__delay_valid_11 <= 0;
      end 
      if((_dataflow__delay_ready_11 || !_dataflow__delay_valid_11) && _dataflow__delay_ready_10) begin
        _dataflow__delay_valid_11 <= _dataflow__delay_valid_10;
      end 
      if((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow_plus_ready_3 && _dataflow_plus_valid_3) begin
        _dataflow__delay_data_12 <= _dataflow_plus_data_3;
      end 
      if(_dataflow__delay_valid_12 && _dataflow__delay_ready_12) begin
        _dataflow__delay_valid_12 <= 0;
      end 
      if((_dataflow__delay_ready_12 || !_dataflow__delay_valid_12) && _dataflow_plus_ready_3) begin
        _dataflow__delay_valid_12 <= _dataflow_plus_valid_3;
      end 
      if((_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_ready_5 && _dataflow__delay_ready_11) && (_dataflow_plus_valid_5 && _dataflow__delay_valid_11)) begin
        _dataflow_plus_data_6 <= _dataflow_plus_data_5 + _dataflow__delay_data_11;
      end 
      if(_dataflow_plus_valid_6 && _dataflow_plus_ready_6) begin
        _dataflow_plus_valid_6 <= 0;
      end 
      if((_dataflow_plus_ready_6 || !_dataflow_plus_valid_6) && (_dataflow_plus_ready_5 && _dataflow__delay_ready_11)) begin
        _dataflow_plus_valid_6 <= _dataflow_plus_valid_5 && _dataflow__delay_valid_11;
      end 
      if((_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_ready_12 && _dataflow__delay_valid_12) begin
        _dataflow__delay_data_13 <= _dataflow__delay_data_12;
      end 
      if(_dataflow__delay_valid_13 && _dataflow__delay_ready_13) begin
        _dataflow__delay_valid_13 <= 0;
      end 
      if((_dataflow__delay_ready_13 || !_dataflow__delay_valid_13) && _dataflow__delay_ready_12) begin
        _dataflow__delay_valid_13 <= _dataflow__delay_valid_12;
      end 
    end
  end

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


  always @(posedge CLK) begin
    if(avalid) begin
      $display("adata=%d", adata);
    end 
  end


  always @(posedge CLK) begin
    if(bvalid) begin
      $display("bdata=%d", bdata);
    end 
  end


endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_manager_readwrite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
