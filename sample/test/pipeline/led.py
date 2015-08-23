import sys
import os
from veriloggen import *

def mkLed(pipe=True):
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)
    
    value = m.Reg('value', width) if pipe else m.Wire('value', width)
    next_value = value(10)

    if pipe: m.Always(Posedge(clk))( next_value )         
    else: m.Assign( next_value )
    
    m.Assign(led(value))
    return m

if __name__ == '__main__':
    led = mkLed(True)
    verilog = led.to_verilog()
    print(verilog)
