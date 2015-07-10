import sys
import os
from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)

    fsm = lib.FSM(m, 'fsm')
    init = fsm.get_index()
    for i in range(1023):
        fsm( fsm.next() )
    fsm( led(led + 1), fsm.goto(init) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(0),
            fsm.init()
        ).Else(
            *fsm.get_all()
        ))
    
    return m

if __name__ == '__main__':
    led = mkLed()
    # led.to_verilog(filename='tmp.v')
    verilog = led.to_verilog()
    print(verilog)
