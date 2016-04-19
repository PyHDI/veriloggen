from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkOrigLed():
    m = Module('blinkled')

    # dummy parameter definition for the next
    inc = AnyType(name='INC')
    width = m.Parameter('WIDTH', inc + 7)
    # overwrite the dummy
    inc = m.Parameter('INC', 1)
    
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
            ).Else(
                count(count + inc)
            )
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led( 0 )
        ).Else(
            If(count == 1023)(
                led(led + inc)
            )
        ))

    return m

def mkLed():
    led = mkOrigLed()
    return resolver.resolve_constant(led)

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
