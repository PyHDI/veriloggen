from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import _while

expected_verilog = """
module test;
  reg CLK;
  reg RST; 
  reg [32-1:0] count;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, CLK, RST, count);
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
    #1000;

    count = 0;
    while(count < 1024) begin
      count = count + 1;
      @(posedge CLK);
    end

    $finish;
  end
endmodule
"""

def test():
    veriloggen.reset()
    test_module = _while.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
