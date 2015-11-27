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

    i = m.Integer('i')
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(1)
        ).Else(
            If(count == 1023)(
                count(0),
                led[0](led[width-1]),
                For(i(1), i<width, i(i+1))(
                    led[i](led[i-1])
                ),
            ).Else(
                count(count + 1),
            )
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
