from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_compare

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  wire y;

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
    x = 9;
    @(posedge CLK);
    #1;
    x = 10;
    @(posedge CLK);
    #1;
    x = 101;
    #1000;
    $finish;
  end

endmodule

module blinkled
  (
   input CLK,
   input RST,
   input [32-1:0] x,
   output reg y
  );

  always @(posedge CLK) begin
    if(RST) begin
      y <= 0;
    end else begin
      if(x < 10) begin
        y <= 0;
      end 
      if(x >= 10) begin
        y <= 1;
      end 
      if(x > 100) begin
        y <= 0;
      end 
    end
  end

endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_compare.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
