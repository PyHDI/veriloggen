from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_prev

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  wire [32-1:0] y;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .y(y)
  );

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end

  initial begin
    RST = 0;
    x = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    x = 10;
    @(posedge CLK);
    #1;
    x = 11;
    @(posedge CLK);
    #1;
    x = 12;
    @(posedge CLK);
    #1;
    x = 13;
    @(posedge CLK);
    #1;
    x = 14;
    @(posedge CLK);
    #1;
    x = 15;
    @(posedge CLK);
    #1;
    x = 16;
    @(posedge CLK);
    #1;
    x = 17;
    @(posedge CLK);
    #1;
    x = 18;
    @(posedge CLK);
    #1;
    x = 19;
    @(posedge CLK);
    #1;
    x = 0;
    #1000;
    $finish;
  end

endmodule

module blinkled
  (
   input CLK,
   input RST,
   input [32-1:0] x,
   output reg [32-1:0] y
  );

  reg [32-1:0] _x_1;
  reg [32-1:0] _x_2;
  reg [32-1:0] _x_3;
  reg [32-1:0] _x_4;
  reg [32-1:0] _x_5;
  reg [32-1:0] _x_6;
  reg [32-1:0] _x_7;
  reg [32-1:0] _tmp_0;

  always @(posedge CLK) begin
    if(RST) begin
      _x_1 <= 0;
      _x_2 <= 0;
      _x_3 <= 0;
      _x_4 <= 0;
      _x_5 <= 0;
      _x_6 <= 0;
      _x_7 <= 0;
      y <= 0;
    end else begin
      _x_1 <= x;
      _x_2 <= _x_1;
      _x_3 <= _x_2;
      _x_4 <= _x_3;
      _x_5 <= _x_4;
      _x_6 <= _x_5;
      _x_7 <= _x_6;
      _tmp_0 <= (((((((x + _x_1) + _x_2) + _x_3) + _x_4) + _x_5) + _x_6) + _x_7);
      y <= (_tmp_0 >> 3);
    end
  end

endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_prev.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
