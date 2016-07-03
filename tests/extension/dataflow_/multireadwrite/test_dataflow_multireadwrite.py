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
  reg _seq_cond_1_1;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;
  localparam xfsm_5 = 5;
  localparam xfsm_6 = 6;

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
          if((xready || !_tmp_3) && (_tmp_1 == 7)) begin
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
          if(xready || !_tmp_3) begin
            _tmp_1 <= _tmp_1 + 1;
          end 
          if((xready || !_tmp_3) && (_tmp_1 == 15)) begin
            xfsm <= xfsm_6;
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
  reg _seq_cond_2_1;
  reg _seq_cond_3_1;
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
      _tmp_4 <= 0;
    end else begin
      case(yfsm)
        yfsm_init: begin
          if(yready || !_tmp_6) begin
            _tmp_4 <= _tmp_4 + 1;
          end 
          if((yready || !_tmp_6) && (_tmp_4 == 7)) begin
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
          if(yready || !_tmp_6) begin
            _tmp_4 <= _tmp_4 + 1;
          end 
          if((yready || !_tmp_6) && (_tmp_4 == 15)) begin
            yfsm <= yfsm_8;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  reg [32-1:0] _tmp_7;
  assign zready = (zfsm == 0) || (zfsm == 9) && (_tmp_7 < 32);
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
      _tmp_7 <= 0;
    end else begin
      case(zfsm)
        zfsm_init: begin
          if(zvalid && (zfsm == 0)) begin
            $display("zfsm_%1d: zdata=%d", zfsm, zdata);
            _tmp_7 <= _tmp_7 + 1;
          end 
          if(_tmp_7 == 8) begin
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
          if(zvalid && ((zfsm == 9) && (_tmp_7 < 32))) begin
            $display("zfsm_%1d: zdata=%d", zfsm, zdata);
            _tmp_7 <= _tmp_7 + 1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_valid_0 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _seq_cond_0_1 <= 0;
      _seq_cond_1_1 <= 0;
      _tmp_5 <= 0;
      _tmp_6 <= 0;
      _seq_cond_2_1 <= 0;
      _seq_cond_3_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        _tmp_3 <= 0;
      end 
      if(_seq_cond_1_1) begin
        _tmp_3 <= 0;
      end 
      if(_seq_cond_2_1) begin
        _tmp_6 <= 0;
      end 
      if(_seq_cond_3_1) begin
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
      _seq_cond_0_1 <= (xfsm == 0) && (xready || !_tmp_3);
      if(_tmp_3 && !xready) begin
        _tmp_3 <= _tmp_3;
      end 
      if((xfsm == 5) && (xready || !_tmp_3)) begin
        _tmp_2 <= _tmp_1;
      end 
      if((xfsm == 5) && (xready || !_tmp_3)) begin
        _tmp_3 <= 1;
      end 
      _seq_cond_1_1 <= (xfsm == 5) && (xready || !_tmp_3);
      if(_tmp_3 && !xready) begin
        _tmp_3 <= _tmp_3;
      end 
      if((yfsm == 0) && (yready || !_tmp_6)) begin
        _tmp_5 <= _tmp_4;
      end 
      if((yfsm == 0) && (yready || !_tmp_6)) begin
        _tmp_6 <= 1;
      end 
      _seq_cond_2_1 <= (yfsm == 0) && (yready || !_tmp_6);
      if(_tmp_6 && !yready) begin
        _tmp_6 <= _tmp_6;
      end 
      if((yfsm == 7) && (yready || !_tmp_6)) begin
        _tmp_5 <= _tmp_4;
      end 
      if((yfsm == 7) && (yready || !_tmp_6)) begin
        _tmp_6 <= 1;
      end 
      _seq_cond_3_1 <= (yfsm == 7) && (yready || !_tmp_6);
      if(_tmp_6 && !yready) begin
        _tmp_6 <= _tmp_6;
      end 
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
