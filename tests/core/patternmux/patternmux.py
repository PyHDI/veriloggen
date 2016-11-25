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

    patterns_count = []
    patterns_count.append( (count < 10, count + 1) )
    patterns_count.append( (count == 1023, 0) )
    patterns_count.append( (None, count + 1) )

    patterns_led = []
    patterns_led.append( (count < 10, led) )
    patterns_led.append( (count == 1023, led + 1) )
    patterns_led.append( (None, led) )

    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0)
        ).Else(
            count(PatternMux(*patterns_count)),
            led(PatternMux(*patterns_led)),
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
