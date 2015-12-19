from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkSub():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    count = m.OutputReg('count', 32)
    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))
    return m

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Wire('count', 32)

    tmp = m.Reg('tmp', 32)
    
    sub = mkSub()
    
    # by multiple definition, throws an exception here
    m.Instance(sub, 'tmp', m.connect_params(sub), m.connect_ports(sub))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            If(count == 1023)(
                led(led + 1)
            )
        ))
    
    return m

if __name__ == '__main__':
    try:
        led = mkLed()
    except ValueError as e:
        print(e.args[0])
        print('But it was detected')
        sys.exit()

    raise ValueError("Multiple definition was not detected.")

    #verilog = led.to_verilog()
    #print(verilog)
