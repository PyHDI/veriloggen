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

if __name__ == '__main__':
    led_module = mkLed()
    led_code = led_module.to_verilog()
    print(led_code)
