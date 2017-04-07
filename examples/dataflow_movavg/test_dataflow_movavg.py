from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_movavg

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg signed [32-1:0] xdata;
  reg xvalid;
  wire xready;
  wire [32-1:0] ydata;
  wire yvalid;
  reg yready;

  movavg
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .xvalid(xvalid),
    .xready(xready),
    .ydata(ydata),
    .yvalid(yvalid),
    .yready(yready)
  );

  reg reset_done;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
    xdata = 0;
    xvalid = 0;
    yready = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;
  localparam xfsm_7 = 7;
  localparam xfsm_8 = 8;
  localparam xfsm_9 = 9;
  localparam xfsm_10 = 10;
  localparam xfsm_11 = 11;
  localparam xfsm_12 = 12;
  localparam xfsm_13 = 13;
  localparam xfsm_14 = 14;
  localparam xfsm_15 = 15;
  localparam xfsm_16 = 16;
  localparam xfsm_17 = 17;
  localparam xfsm_18 = 18;
  localparam xfsm_19 = 19;
  localparam xfsm_20 = 20;
  localparam xfsm_21 = 21;
  localparam xfsm_22 = 22;
  localparam xfsm_23 = 23;
  localparam xfsm_24 = 24;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          xvalid <= 0;
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          xfsm <= xfsm_2;
        end
        xfsm_2: begin
          xfsm <= xfsm_3;
        end
        xfsm_3: begin
          xfsm <= xfsm_4;
        end
        xfsm_4: begin
          xfsm <= xfsm_5;
        end
        xfsm_5: begin
          xfsm <= xfsm_6;
        end
        xfsm_6: begin
          xfsm <= xfsm_7;
        end
        xfsm_7: begin
          xfsm <= xfsm_8;
        end
        xfsm_8: begin
          xfsm <= xfsm_9;
        end
        xfsm_9: begin
          xfsm <= xfsm_10;
        end
        xfsm_10: begin
          xfsm <= xfsm_11;
        end
        xfsm_11: begin
          xvalid <= 1;
          xfsm <= xfsm_12;
        end
        xfsm_12: begin
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 15) && xready) begin
            xfsm <= xfsm_13;
          end 
        end
        xfsm_13: begin
          xvalid <= 0;
          xfsm <= xfsm_14;
        end
        xfsm_14: begin
          xfsm <= xfsm_15;
        end
        xfsm_15: begin
          xfsm <= xfsm_16;
        end
        xfsm_16: begin
          xfsm <= xfsm_17;
        end
        xfsm_17: begin
          xfsm <= xfsm_18;
        end
        xfsm_18: begin
          xfsm <= xfsm_19;
        end
        xfsm_19: begin
          xfsm <= xfsm_20;
        end
        xfsm_20: begin
          xfsm <= xfsm_21;
        end
        xfsm_21: begin
          xfsm <= xfsm_22;
        end
        xfsm_22: begin
          xfsm <= xfsm_23;
        end
        xfsm_23: begin
          xvalid <= 1;
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 30) && xready) begin
            xfsm <= xfsm_24;
          end 
        end
        xfsm_24: begin
          xvalid <= 0;
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  localparam yfsm_1 = 1;
  localparam yfsm_2 = 2;
  localparam yfsm_3 = 3;
  localparam yfsm_4 = 4;
  localparam yfsm_5 = 5;
  localparam yfsm_6 = 6;
  localparam yfsm_7 = 7;
  localparam yfsm_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
    end else begin
      case(yfsm)
        yfsm_init: begin
          yready <= 0;
          if(reset_done) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          yfsm <= yfsm_2;
        end
        yfsm_2: begin
          if(yvalid) begin
            yready <= 1;
          end 
          if(yvalid) begin
            yfsm <= yfsm_3;
          end 
        end
        yfsm_3: begin
          yready <= 0;
          yfsm <= yfsm_4;
        end
        yfsm_4: begin
          yready <= 0;
          yfsm <= yfsm_5;
        end
        yfsm_5: begin
          yready <= 0;
          yfsm <= yfsm_6;
        end
        yfsm_6: begin
          yready <= 0;
          yfsm <= yfsm_7;
        end
        yfsm_7: begin
          yready <= 0;
          yfsm <= yfsm_8;
        end
        yfsm_8: begin
          yfsm <= yfsm_2;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      if(xvalid && xready) begin
        $display("xdata=%d", xdata);
      end 
      if(yvalid && yready) begin
        $display("ydata=%d", ydata);
      end 
    end 
  end


endmodule



module movavg
(
  input CLK,
  input RST,
  input signed [32-1:0] xdata,
  input xvalid,
  output xready,
  output [32-1:0] ydata,
  output yvalid,
  input yready
);

  reg signed [32-1:0] _tmp_data_0;
  reg signed [32-1:0] _tmp_data_1;
  reg signed [32-1:0] _tmp_data_2;
  reg signed [32-1:0] _tmp_data_3;
  reg signed [32-1:0] _tmp_data_4;
  reg signed [32-1:0] _tmp_data_5;
  reg signed [32-1:0] _tmp_data_6;
  reg signed [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  reg signed [32-1:0] _tmp_data_8;
  reg _tmp_valid_8;
  wire _tmp_ready_8;
  reg signed [32-1:0] _tmp_data_9;
  reg _tmp_valid_9;
  wire _tmp_ready_9;
  reg signed [32-1:0] _tmp_data_10;
  reg _tmp_valid_10;
  wire _tmp_ready_10;
  assign xready = (_tmp_ready_7 || !_tmp_valid_7) && (xvalid && xvalid) && ((_tmp_ready_7 || !_tmp_valid_7) && (xvalid && xvalid)) && ((_tmp_ready_8 || !_tmp_valid_8) && (xvalid && xvalid)) && ((_tmp_ready_8 || !_tmp_valid_8) && (xvalid && xvalid)) && ((_tmp_ready_9 || !_tmp_valid_9) && (xvalid && xvalid)) && ((_tmp_ready_9 || !_tmp_valid_9) && (xvalid && xvalid)) && ((_tmp_ready_10 || !_tmp_valid_10) && (xvalid && xvalid)) && ((_tmp_ready_10 || !_tmp_valid_10) && (xvalid && xvalid));
  reg signed [32-1:0] _tmp_data_11;
  reg _tmp_valid_11;
  wire _tmp_ready_11;
  assign _tmp_ready_7 = (_tmp_ready_11 || !_tmp_valid_11) && (_tmp_valid_7 && _tmp_valid_8);
  assign _tmp_ready_8 = (_tmp_ready_11 || !_tmp_valid_11) && (_tmp_valid_7 && _tmp_valid_8);
  reg signed [32-1:0] _tmp_data_12;
  reg _tmp_valid_12;
  wire _tmp_ready_12;
  assign _tmp_ready_9 = (_tmp_ready_12 || !_tmp_valid_12) && (_tmp_valid_9 && _tmp_valid_10);
  assign _tmp_ready_10 = (_tmp_ready_12 || !_tmp_valid_12) && (_tmp_valid_9 && _tmp_valid_10);
  reg signed [32-1:0] _tmp_data_13;
  reg _tmp_valid_13;
  wire _tmp_ready_13;
  assign _tmp_ready_11 = (_tmp_ready_13 || !_tmp_valid_13) && (_tmp_valid_11 && _tmp_valid_12);
  assign _tmp_ready_12 = (_tmp_ready_13 || !_tmp_valid_13) && (_tmp_valid_11 && _tmp_valid_12);
  reg [32-1:0] _tmp_data_14;
  reg _tmp_valid_14;
  wire _tmp_ready_14;
  assign _tmp_ready_13 = (_tmp_ready_14 || !_tmp_valid_14) && _tmp_valid_13;
  assign ydata = _tmp_data_14;
  assign yvalid = _tmp_valid_14;
  assign _tmp_ready_14 = yready;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_data_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_data_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
      _tmp_data_8 <= 0;
      _tmp_valid_8 <= 0;
      _tmp_data_9 <= 0;
      _tmp_valid_9 <= 0;
      _tmp_data_10 <= 0;
      _tmp_valid_10 <= 0;
      _tmp_data_11 <= 0;
      _tmp_valid_11 <= 0;
      _tmp_data_12 <= 0;
      _tmp_valid_12 <= 0;
      _tmp_data_13 <= 0;
      _tmp_valid_13 <= 0;
      _tmp_data_14 <= 0;
      _tmp_valid_14 <= 0;
    end else begin
      if(xvalid && xready) begin
        _tmp_data_0 <= xdata;
      end 
      if(xvalid && xready) begin
        _tmp_data_1 <= _tmp_data_0;
      end 
      if(xvalid && xready) begin
        _tmp_data_2 <= _tmp_data_1;
      end 
      if(xvalid && xready) begin
        _tmp_data_3 <= _tmp_data_2;
      end 
      if(xvalid && xready) begin
        _tmp_data_4 <= _tmp_data_3;
      end 
      if(xvalid && xready) begin
        _tmp_data_5 <= _tmp_data_4;
      end 
      if(xvalid && xready) begin
        _tmp_data_6 <= _tmp_data_5;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && (xready && xready) && (xvalid && xvalid)) begin
        _tmp_data_7 <= $signed(xdata) + $signed(_tmp_data_0);
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && (xready && xready)) begin
        _tmp_valid_7 <= xvalid && xvalid;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (xready && xready) && (xvalid && xvalid)) begin
        _tmp_data_8 <= $signed(_tmp_data_1) + $signed(_tmp_data_2);
      end 
      if(_tmp_valid_8 && _tmp_ready_8) begin
        _tmp_valid_8 <= 0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (xready && xready)) begin
        _tmp_valid_8 <= xvalid && xvalid;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && (xready && xready) && (xvalid && xvalid)) begin
        _tmp_data_9 <= $signed(_tmp_data_3) + $signed(_tmp_data_4);
      end 
      if(_tmp_valid_9 && _tmp_ready_9) begin
        _tmp_valid_9 <= 0;
      end 
      if((_tmp_ready_9 || !_tmp_valid_9) && (xready && xready)) begin
        _tmp_valid_9 <= xvalid && xvalid;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && (xready && xready) && (xvalid && xvalid)) begin
        _tmp_data_10 <= $signed(_tmp_data_5) + $signed(_tmp_data_6);
      end 
      if(_tmp_valid_10 && _tmp_ready_10) begin
        _tmp_valid_10 <= 0;
      end 
      if((_tmp_ready_10 || !_tmp_valid_10) && (xready && xready)) begin
        _tmp_valid_10 <= xvalid && xvalid;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && (_tmp_ready_7 && _tmp_ready_8) && (_tmp_valid_7 && _tmp_valid_8)) begin
        _tmp_data_11 <= $signed(_tmp_data_7) + $signed(_tmp_data_8);
      end 
      if(_tmp_valid_11 && _tmp_ready_11) begin
        _tmp_valid_11 <= 0;
      end 
      if((_tmp_ready_11 || !_tmp_valid_11) && (_tmp_ready_7 && _tmp_ready_8)) begin
        _tmp_valid_11 <= _tmp_valid_7 && _tmp_valid_8;
      end 
      if((_tmp_ready_12 || !_tmp_valid_12) && (_tmp_ready_9 && _tmp_ready_10) && (_tmp_valid_9 && _tmp_valid_10)) begin
        _tmp_data_12 <= $signed(_tmp_data_9) + $signed(_tmp_data_10);
      end 
      if(_tmp_valid_12 && _tmp_ready_12) begin
        _tmp_valid_12 <= 0;
      end 
      if((_tmp_ready_12 || !_tmp_valid_12) && (_tmp_ready_9 && _tmp_ready_10)) begin
        _tmp_valid_12 <= _tmp_valid_9 && _tmp_valid_10;
      end 
      if((_tmp_ready_13 || !_tmp_valid_13) && (_tmp_ready_11 && _tmp_ready_12) && (_tmp_valid_11 && _tmp_valid_12)) begin
        _tmp_data_13 <= $signed(_tmp_data_11) + $signed(_tmp_data_12);
      end 
      if(_tmp_valid_13 && _tmp_ready_13) begin
        _tmp_valid_13 <= 0;
      end 
      if((_tmp_ready_13 || !_tmp_valid_13) && (_tmp_ready_11 && _tmp_ready_12)) begin
        _tmp_valid_13 <= _tmp_valid_11 && _tmp_valid_12;
      end 
      if((_tmp_ready_14 || !_tmp_valid_14) && _tmp_ready_13 && _tmp_valid_13) begin
        _tmp_data_14 <= _tmp_data_13 >> 3'd3;
      end 
      if(_tmp_valid_14 && _tmp_ready_14) begin
        _tmp_valid_14 <= 0;
      end 
      if((_tmp_ready_14 || !_tmp_valid_14) && _tmp_ready_13) begin
        _tmp_valid_14 <= _tmp_valid_13;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = dataflow_movavg.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
