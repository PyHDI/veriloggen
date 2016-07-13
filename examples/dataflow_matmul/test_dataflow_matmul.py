from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_matmul

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] xaddr;
  reg [32-1:0] xdin;
  wire [8-1:0] yaddr;
  reg [32-1:0] ydin;
  wire [8-1:0] zaddr;
  wire [32-1:0] zdout;
  wire zwe;
  reg start;
  wire busy;

  Matmul
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xaddr(xaddr),
    .xdin(xdin),
    .yaddr(yaddr),
    .ydin(ydin),
    .zaddr(zaddr),
    .zdout(zdout),
    .zwe(zwe),
    .start(start),
    .busy(busy)
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
    start = 0;
    xdin = 0;
    ydin = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #100000;
    $finish;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _fsm_cond_2_0_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_2: begin
          if(_fsm_cond_2_0_1) begin
            start <= 0;
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          if(reset_done) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(!busy) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          start <= 1;
          _fsm_cond_2_0_1 <= 1;
          xdin <= xaddr;
          ydin <= (yaddr % 16 == yaddr / 16)? 2 : 0;
          fsm <= fsm_3;
        end
        fsm_3: begin
          xdin <= xaddr;
          ydin <= (yaddr % 16 == yaddr / 16)? 2 : 0;
          if(busy) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          xdin <= xaddr;
          ydin <= (yaddr % 16 == yaddr / 16)? 2 : 0;
          if(!busy) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          $finish;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(zwe) begin
      $display("zaddr=%10d zdout=%10d", zaddr, zdout);
      if(zaddr * 2 != zdout) begin
        $display("## wrong result");
      end 
    end 
  end


endmodule



module Matmul
(
  input CLK,
  input RST,
  output reg [8-1:0] xaddr,
  input [32-1:0] xdin,
  output reg [8-1:0] yaddr,
  input [32-1:0] ydin,
  output reg [8-1:0] zaddr,
  output reg [32-1:0] zdout,
  output reg zwe,
  input start,
  output reg busy
);

  reg ivalid;
  wire [32-1:0] odata;
  wire ovalid;
  reg vreset;

  madd
  madd
  (
    .CLK(CLK),
    .RST(RST),
    .xd(xdin),
    .xv(ivalid),
    .yd(ydin),
    .yv(ivalid),
    .zd(odata),
    .zv(ovalid),
    .vreset_data(vreset),
    .vreset(ivalid)
  );

  reg [5-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg [5-1:0] _tmp_2;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_1_0_1;
  reg _fsm_cond_1_1_1;
  reg _fsm_cond_1_2_1;
  reg _fsm_cond_1_3_1;
  reg _fsm_cond_2_4_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      xaddr <= 0;
      yaddr <= 0;
      zaddr <= 0;
      busy <= 0;
      vreset <= 0;
      ivalid <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _fsm_cond_1_0_1 <= 0;
      _fsm_cond_1_1_1 <= 0;
      _fsm_cond_1_2_1 <= 0;
      _fsm_cond_1_3_1 <= 0;
      zdout <= 0;
      _fsm_cond_2_4_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_1: begin
          if(_fsm_cond_1_0_1) begin
            vreset <= 0;
          end 
          if(_fsm_cond_1_1_1) begin
            vreset <= 1;
          end 
          if(_fsm_cond_1_2_1) begin
            ivalid <= 0;
          end 
          if(_fsm_cond_1_3_1) begin
            ivalid <= 1;
          end 
        end
        fsm_2: begin
          if(_fsm_cond_2_4_1) begin
            zwe <= 0;
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          xaddr <= -1;
          yaddr <= -1;
          zaddr <= -1;
          zwe <= 0;
          busy <= 0;
          vreset <= 0;
          ivalid <= 0;
          _tmp_0 <= 0;
          _tmp_1 <= 0;
          _tmp_2 <= 0;
          if(start) begin
            busy <= 1;
          end 
          if(start) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          _fsm_cond_1_0_1 <= 1;
          _fsm_cond_1_1_1 <= _tmp_0 == 0;
          if(_tmp_0 < 16) begin
            xaddr <= xaddr + 1;
            yaddr <= yaddr + 1;
          end 
          _fsm_cond_1_2_1 <= 1;
          _fsm_cond_1_3_1 <= _tmp_0 < 16;
          if(_tmp_0 < 16) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if(ovalid) begin
            _tmp_2 <= _tmp_2 + 1;
          end 
          if(ovalid) begin
            _tmp_1 <= odata;
          end 
          if(_tmp_2 == 16) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          zaddr <= zaddr + 1;
          zdout <= _tmp_1;
          zwe <= 1;
          _fsm_cond_2_4_1 <= 1;
          if(yaddr == 255) begin
            yaddr <= -1;
          end 
          if(yaddr < 255) begin
            xaddr <= xaddr - 16;
          end 
          _tmp_0 <= 0;
          _tmp_2 <= 0;
          if(!(zaddr == 254)) begin
            fsm <= fsm_1;
          end 
          if(zaddr == 254) begin
            fsm <= fsm_init;
          end 
        end
      endcase
    end
  end


endmodule



module madd
(
  input CLK,
  input RST,
  input signed [32-1:0] xd,
  input xv,
  input signed [32-1:0] yd,
  input yv,
  input [1-1:0] vreset_data,
  input vreset,
  output signed [32-1:0] zd,
  output zv
);

  wire signed [32-1:0] _tmp_data_0;
  wire _tmp_valid_0;
  wire _tmp_ready_0;
  wire signed [64-1:0] _tmp_odata_0;
  reg signed [64-1:0] _tmp_data_reg_0;
  assign _tmp_data_0 = _tmp_data_reg_0;
  wire _tmp_ovalid_0;
  reg _tmp_valid_reg_0;
  assign _tmp_valid_0 = _tmp_valid_reg_0;
  wire _tmp_enable_0;
  wire _tmp_update_0;
  assign _tmp_enable_0 = (_tmp_ready_0 || !_tmp_valid_0) && 1 && (xv && yv);
  assign _tmp_update_0 = _tmp_ready_0 || !_tmp_valid_0;

  multiplier_0
  mul0
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_0),
    .enable(_tmp_enable_0),
    .valid(_tmp_ovalid_0),
    .a(xd),
    .b(yd),
    .c(_tmp_odata_0)
  );

  assign _tmp_ready_0 = (_tmp_ready_8 || !_tmp_valid_8) && (_tmp_valid_0 && _tmp_valid_7);
  reg [1-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign _tmp_ready_1 = (_tmp_ready_2 || !_tmp_valid_2) && _tmp_valid_1;
  reg [1-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign _tmp_ready_2 = (_tmp_ready_3 || !_tmp_valid_3) && _tmp_valid_2;
  reg [1-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_3 = (_tmp_ready_4 || !_tmp_valid_4) && _tmp_valid_3;
  reg [1-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_4 = (_tmp_ready_5 || !_tmp_valid_5) && _tmp_valid_4;
  reg [1-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (_tmp_ready_6 || !_tmp_valid_6) && _tmp_valid_5;
  reg [1-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  assign _tmp_ready_6 = (_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_6;
  reg [1-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign _tmp_ready_7 = (_tmp_ready_8 || !_tmp_valid_8) && (_tmp_valid_0 && _tmp_valid_7);
  reg signed [32-1:0] _tmp_data_8;
  reg _tmp_valid_8;
  wire _tmp_ready_8;
  assign zd = _tmp_data_8;
  assign zv = _tmp_valid_8;
  assign _tmp_ready_8 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_reg_0 <= 0;
      _tmp_valid_reg_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_valid_3 <= 0;
      _tmp_data_4 <= 0;
      _tmp_valid_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_valid_5 <= 0;
      _tmp_data_6 <= 0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
      _tmp_data_8 <= 1'd0;
      _tmp_valid_8 <= 0;
    end else begin
      if(_tmp_ready_0 || !_tmp_valid_0) begin
        _tmp_data_reg_0 <= _tmp_odata_0;
      end 
      if(_tmp_ready_0 || !_tmp_valid_0) begin
        _tmp_valid_reg_0 <= _tmp_ovalid_0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1 && vreset) begin
        _tmp_data_1 <= vreset_data;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1) begin
        _tmp_valid_1 <= vreset;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_1 && _tmp_valid_1) begin
        _tmp_data_2 <= _tmp_data_1;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_1) begin
        _tmp_valid_2 <= _tmp_valid_1;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_2 && _tmp_valid_2) begin
        _tmp_data_3 <= _tmp_data_2;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_2) begin
        _tmp_valid_3 <= _tmp_valid_2;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_3 && _tmp_valid_3) begin
        _tmp_data_4 <= _tmp_data_3;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_3) begin
        _tmp_valid_4 <= _tmp_valid_3;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && _tmp_ready_4 && _tmp_valid_4) begin
        _tmp_data_5 <= _tmp_data_4;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && _tmp_ready_4) begin
        _tmp_valid_5 <= _tmp_valid_4;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5 && _tmp_valid_5) begin
        _tmp_data_6 <= _tmp_data_5;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5) begin
        _tmp_valid_6 <= _tmp_valid_5;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_6 && _tmp_valid_6) begin
        _tmp_data_7 <= _tmp_data_6;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_6) begin
        _tmp_valid_7 <= _tmp_valid_6;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_0 && _tmp_ready_7) && (_tmp_valid_0 && _tmp_valid_7)) begin
        _tmp_data_8 <= _tmp_data_8 + _tmp_data_0;
      end 
      if(_tmp_valid_8 && _tmp_ready_8) begin
        _tmp_valid_8 <= 0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_0 && _tmp_ready_7)) begin
        _tmp_valid_8 <= _tmp_valid_0 && _tmp_valid_7;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_0 && _tmp_ready_7) && (_tmp_valid_0 && _tmp_valid_7) && _tmp_data_7) begin
        _tmp_data_8 <= 1'd0 + _tmp_data_0;
      end 
    end
  end


endmodule



module multiplier_0
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_0
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
    end 
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = dataflow_matmul.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
