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

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Elif(count == 0)(
                count(count + 1)
            ).Elif(count == 1)(
                count(count + 2)
            ).Elif(count == 2)(
                count(count + 3)
            ).Elif(count == 3)(
                count(count + 4)
            ).Else(
                count(count + 5)
            )
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led( 0 )
        ).Else(
            If(count == 1023)(
                led( led + 1 )
            )
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
