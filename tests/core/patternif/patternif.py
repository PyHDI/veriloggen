from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    patterns = []
    patterns.append( (count < 10, count(count + 1)) )
    patterns.append( (count == 1023, (count(0), led(led + 1))) )
    patterns.append( (None, count(count + 1)) )

    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0)
        ).Else(
            PatternIf(*patterns)
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
