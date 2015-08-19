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
    init = fsm.current()

    tmp = []
    for i in range(4):
        tmp.append( m.Reg('tmp_' + str(i), width) )
        
    for i in range(4):
        fsm.add( tmp[i](fsm.current()) ) 
        fsm.goto_next(cond=None) # = fsm.add( fsm.set_next() ).inc()
        
    fsm.add( led(led + 1) )
    fsm.goto(init, cond=None) # = fsm.add( fsm.set(init) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            *([ t(0) for t in tmp ] + [ led(0), fsm.set_init() ])
        ).Else(
            fsm.to_case()
        ))
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
