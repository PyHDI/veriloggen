from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')

    # function to add an LED port
    def add_led(postfix, limit=1024):
        led = m.OutputReg('LED'+postfix, width)
        count = m.Reg('count'+postfix, 32)

        m.Always(Posedge(clk))(
            If(rst)(
                count(0)
            ).Else(
                If(count == limit - 1)(
                    count(0)
                ).Else(
                    count(count + 1)
                )
            ))
    
        m.Always(Posedge(clk))(
            If(rst)(
                led(0)
            ).Else(
                If(count == limit - 1)(
                    led(led + 1)
                )
            ))

    # call 'add_led' to add LED ports
    for i in range(4):
        add_led('_' + str(i), limit=i*10 + 10)
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
