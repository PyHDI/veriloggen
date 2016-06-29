from __future__ import absolute_import
from __future__ import print_function
import dataflow_multireadwrite

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

  reg [32-1:0] xdata;
  reg xvalid;
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

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_valid_0 <= 0;
    end else begin
      if((_tmp_ready_0 || !_tmp_valid_0) && (xready && yready) && (xvalid && yvalid)) begin
        _tmp_data_0 <= xdata + ydata;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && (xready && yready)) begin
        _tmp_valid_0 <= xvalid && yvalid;
      end 
    end
  end

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _d1_xfsm;
  reg _xfsm_cond_0_0_1;
  reg _xfsm_cond_5_1_1;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _d1_xfsm <= xfsm_init;
      xdata <= 0;
      xvalid <= 0;
      _xfsm_cond_0_0_1 <= 0;
      _tmp_1 <= 0;
      _xfsm_cond_5_1_1 <= 0;
    end else begin
      _d1_xfsm <= xfsm;
      case(_d1_xfsm)
        xfsm_init: begin
          if(_xfsm_cond_0_0_1) begin
            xvalid <= 0;
          end 
        end
        xfsm_5: begin
          if(_xfsm_cond_5_1_1) begin
            xvalid <= 0;
          end 
        end
      endcase
      case(xfsm)
        xfsm_init: begin
          if(xready || !xvalid) begin
            xdata <= _tmp_1;
          end 
          if(xready || !xvalid) begin
            xvalid <= 1;
          end 
          _xfsm_cond_0_0_1 <= xready || !xvalid;
          if(xvalid && !xready) begin
            xvalid <= xvalid;
          end 
          if(xready || !xvalid) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((xready || !xvalid) && (_tmp_1 == 7)) begin
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
          if(xready || !xvalid) begin
            xdata <= _tmp_1;
          end 
          if(xready || !xvalid) begin
            xvalid <= 1;
          end 
          _xfsm_cond_5_1_1 <= xready || !xvalid;
          if(xvalid && !xready) begin
            xvalid <= xvalid;
          end 
          if(xready || !xvalid) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((xready || !xvalid) && (_tmp_1 == 15)) begin
            xfsm <= xfsm_6;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  assign ydata = _tmp_3;
  reg _tmp_4;
  assign yvalid = _tmp_4;
  reg [32-1:0] _d1_yfsm;
  reg _yfsm_cond_0_0_1;
  reg _yfsm_cond_7_1_1;
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
      _d1_yfsm <= yfsm_init;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _yfsm_cond_0_0_1 <= 0;
      _tmp_2 <= 0;
      _yfsm_cond_7_1_1 <= 0;
    end else begin
      _d1_yfsm <= yfsm;
      case(_d1_yfsm)
        yfsm_init: begin
          if(_yfsm_cond_0_0_1) begin
            _tmp_4 <= 0;
          end 
        end
        yfsm_7: begin
          if(_yfsm_cond_7_1_1) begin
            _tmp_4 <= 0;
          end 
        end
      endcase
      case(yfsm)
        yfsm_init: begin
          if(yready || !_tmp_4) begin
            _tmp_3 <= _tmp_2;
          end 
          if(yready || !_tmp_4) begin
            _tmp_4 <= 1;
          end 
          _yfsm_cond_0_0_1 <= yready || !_tmp_4;
          if(_tmp_4 && !yready) begin
            _tmp_4 <= _tmp_4;
          end 
          if(yready || !_tmp_4) begin
            _tmp_2 <= _tmp_2 + 1;
          end 
          if((yready || !_tmp_4) && (_tmp_2 == 7)) begin
            yfsm <= yfsm_1;
          end 
        end
        yfsm_1: begin
          yfsm <= yfsm_2;
        end
        yfsm_2: begin
          yfsm <= yfsm_3;
        end
        yfsm_3: begin
          yfsm <= yfsm_4;
        end
        yfsm_4: begin
          yfsm <= yfsm_5;
        end
        yfsm_5: begin
          yfsm <= yfsm_6;
        end
        yfsm_6: begin
          yfsm <= yfsm_7;
        end
        yfsm_7: begin
          if(yready || !_tmp_4) begin
            _tmp_3 <= _tmp_2;
          end 
          if(yready || !_tmp_4) begin
            _tmp_4 <= 1;
          end 
          _yfsm_cond_7_1_1 <= yready || !_tmp_4;
          if(_tmp_4 && !yready) begin
            _tmp_4 <= _tmp_4;
          end 
          if(yready || !_tmp_4) begin
            _tmp_2 <= _tmp_2 + 1;
          end 
          if((yready || !_tmp_4) && (_tmp_2 == 15)) begin
            yfsm <= yfsm_8;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  reg [32-1:0] _tmp_5;
  assign zready = (zfsm == 0) || (zfsm == 9) && (_tmp_5 < 32);
  localparam zfsm_1 = 1;
  localparam zfsm_2 = 2;
  localparam zfsm_3 = 3;
  localparam zfsm_4 = 4;
  localparam zfsm_5 = 5;
  localparam zfsm_6 = 6;
  localparam zfsm_7 = 7;
  localparam zfsm_8 = 8;
  localparam zfsm_9 = 9;

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
      _tmp_5 <= 0;
    end else begin
      case(zfsm)
        zfsm_init: begin
          if(zvalid && (zfsm == 0)) begin
            $display("zfsm_%1d: zdata=%d", zfsm, zdata);
            _tmp_5 <= _tmp_5 + 1;
          end 
          if(_tmp_5 == 8) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          zfsm <= zfsm_3;
        end
        zfsm_3: begin
          zfsm <= zfsm_4;
        end
        zfsm_4: begin
          zfsm <= zfsm_5;
        end
        zfsm_5: begin
          zfsm <= zfsm_6;
        end
        zfsm_6: begin
          zfsm <= zfsm_7;
        end
        zfsm_7: begin
          zfsm <= zfsm_8;
        end
        zfsm_8: begin
          zfsm <= zfsm_9;
        end
        zfsm_9: begin
          if((_tmp_5 < 32) && (zvalid && ((zfsm == 9) && (_tmp_5 < 32)))) begin
            $display("zfsm_%1d: zdata=%d", zfsm, zdata);
            _tmp_5 <= _tmp_5 + 1;
          end 
        end
      endcase
    end
  end


endmodule
"""

def test():
    test_module = dataflow_multireadwrite.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
