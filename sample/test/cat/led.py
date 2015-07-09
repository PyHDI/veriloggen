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
            count(0)
        ).Else(
            count(count + 1)
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(Int(0b00000001, width=8, base=2))
        ).Else(
            If(count == 1024 - 1)(
                led( Cat(led[width-2:0], led[width-1]) )
            )
        ))

    return m

led = mkLed()
verilog = led.to_verilog()
print(verilog)
