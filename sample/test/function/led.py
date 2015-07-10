import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    inc = m.Function('inc', width)
    inc_v = inc.Input('v', width)
    inc_o = inc.Input('o', width)
    inc_tmp = inc.Reg('tmp', width)
    inc.Body(
        inc_tmp(inc_v + 1),
        inc(inc_tmp)
    )
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            count( inc.call(count, 1) )
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(1)
        ).Else(
            If(count == 1024 - 1)(
                led[0](led[width-1]),
                led[width-1:1](led[width-2:0])
            )
        ))

    return m

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
  output reg [(WIDTH - 1):0] LED
 );
  reg [(32 - 1):0] count;

  function [(WIDTH - 1):0] inc;
    input [(WIDTH - 1):0] v;
    input [(WIDTH - 1):0] o;
    reg [(WIDTH - 1):0] tmp;
    begin        
      tmp = (v + 1);        
      inc = tmp;
    end 
  endfunction

  always @(posedge CLK)
    begin        
      if(RST) begin        
        count <= 0;
      end  
      else begin        
        count <= inc(count, 1);
      end 
    end 

  always @(posedge CLK)
    begin        
      if(RST) begin        
        LED <= 1;
      end  
      else begin        
        if((count == 1023)) begin        
          LED[0] <= LED[(WIDTH - 1)];        
          LED[(WIDTH - 1):1] <= LED[(WIDTH - 2):0];
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
        led = mkLed()
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
