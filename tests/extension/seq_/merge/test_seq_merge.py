from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_merge

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );

  reg reset_done;


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
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


endmodule



module blinkled
(
  input CLK,
  input RST
);

  reg [32-1:0] x;
  reg [32-1:0] y;
  reg [32-1:0] z;
  reg _seq_x_cond_0_1;
  reg _seq_y_cond_0_1;
  reg _seq_y_cond_0_2;
  reg [32-1:0] _x_1;
  reg [32-1:0] _y_1;

  always @(posedge CLK) begin
    if(RST) begin
      x <= 0;
      _seq_x_cond_0_1 <= 0;
      _x_1 <= 0;
      y <= 0;
      _seq_y_cond_0_1 <= 0;
      _seq_y_cond_0_2 <= 0;
      _y_1 <= 0;
      z <= 0;
    end else begin
      if(_seq_y_cond_0_2) begin
        y <= 0;
      end 
      if(_seq_x_cond_0_1) begin
        x <= 0;
      end 
      _seq_y_cond_0_2 <= _seq_y_cond_0_1;
      if(x < 16) begin
        x <= x + 1;
      end 
      _seq_x_cond_0_1 <= x == 16;
      _x_1 <= x;
      if(y < 32) begin
        y <= y + 1;
      end 
      _seq_y_cond_0_1 <= y == 32;
      _y_1 <= y;
      z <= _x_1 + _y_1;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_merge.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
