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

    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0)
        ).Else(
            Case(count)(
                When(0, 1)( count(count+1), led(led)),
                When(1023)( count(0), led(led+1)),
                When(None)( count(count+1), led(led)),
            )
        ))

    return m

if __name__ == '__main__':
    led_module = mkLed()
    led_code = led_module.to_verilog()
    print(led_code)
