from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_fixed_add

expected_verilog = """
module test #
(
  parameter WIDTH = 8
)
(

);

  reg CLK;
  reg RST;

  blinkled
  #(
    .WIDTH(WIDTH)
  )
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



module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST
);

  reg signed [16-1:0] a;
  reg signed [16-1:0] b;
  reg signed [32-1:0] c;
  reg signed [32-1:0] d;
  reg signed [32-1:0] e;

  always @(posedge CLK) begin
    if(RST) begin
      a <= 64;
      b <= 'sd1;
      c <= -2048;
      d <= 'sd1;
      e <= 0;
    end else begin
      a <= b - 'sd256 >>> 4;
      b <= a - 'sd16 << 4;
      c <= b[15:0] + 1;
      d <= c + 'sd256;
      e <= e + 'sd65536;
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = types_fixed_add.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
