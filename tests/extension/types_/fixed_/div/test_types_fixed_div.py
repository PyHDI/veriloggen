from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_fixed_div

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

  reg [32-1:0] a;
  reg [32-1:0] b;
  reg [32-1:0] c;
  reg [32-1:0] d;
  reg signed [32-1:0] sa;
  reg signed [32-1:0] sb;
  reg signed [32-1:0] sc;
  reg signed [32-1:0] sd;

  always @(posedge CLK) begin
    if(RST) begin
      a <= 131072;
      b <= 4096;
      c <= 65536;
      d <= 65536;
      sa <= 131072;
      sb <= -4096;
      sc <= -65536;
      sd <= -65536;
    end else begin
      a <= a;
      b <= b;
      c <= (b << 8) / a << 16;
      d <= a / b << 8;
      sa <= sa;
      sb <= sb;
      sc <= (((($signed((sb << 8)) >> 31) & 1'b1) == sa[31])? ((!(($signed((sb << 8)) >> 31) & 1'b1))? $signed((sb << 8)) : ~$signed((sb << 8)) + 1) / ((!sa[31])? sa : ~sa + 1) : ~(((!(($signed((sb << 8)) >> 31) & 1'b1))? $signed((sb << 8)) : ~$signed((sb << 8)) + 1) / ((!sa[31])? sa : ~sa + 1)) + 1) << 16;
      sd <= ((sa[31] == sb[31])? ((!sa[31])? sa : ~sa + 1) / ((!sb[31])? sb : ~sb + 1) : ~(((!sa[31])? sa : ~sa + 1) / ((!sb[31])? sb : ~sb + 1)) + 1) << 8;
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_fixed_div.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
