import sys
import os
from veriloggen import *

class Led(Module):
    def __init__(self, name='blinkled'):
        Module.__init__(self, name)
        self.width = self.Parameter('WIDTH', 8)
        self.clk = self.Input('CLK')
        self.rst = self.Input('RST')
        self.led = self.OutputReg('LED', self.width)
        self.count = self.Reg('count', 32)

        self.Always(Posedge(self.clk))(
            If(self.rst)(
                self.count(0)
            ).Else(
                self.count(self.count + 1)
            ))
        
        self.Always(Posedge(self.clk))(
            If(self.rst)(
                self.led(0)
            ).Else(
                If(self.count == 1024 - 1)(
                    self.led(self.led + 1)
                )
            ))
        
#-------------------------------------------------------------------------------
import unittest

expected_verilog = """
module blinkled #
  ( 
   parameter WIDTH = 8
  )
  ( 
   input CLK, 
   input RST,
   output reg [WIDTH-1:0] LED
  );
  reg [32-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      count <= count + 1;
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 1;
      end 
    end
  end
endmodule
"""

class TestLed(unittest.TestCase):
    def setUp(self):
        pass

    def test_sample(self):
        from pyverilog.vparser.parser import VerilogParser
        from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
        led = Led()
        verilog = led.to_verilog()
        parser = VerilogParser()
        expected_ast = parser.parse(expected_verilog)
        codegen = ASTCodeGenerator()
        expected_code = codegen.visit(expected_ast)
        self.assertTrue( expected_code == verilog )
        
        #import difflib
        #diff = difflib.unified_diff(verilog.splitlines(), expected_code.splitlines())
        #print('\n'.join(list(diff)))
        #self.assertTrue( len(list(diff)) == 0 )
    
if __name__ == '__main__':
    unittest.main()
