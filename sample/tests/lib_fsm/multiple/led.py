import sys
import os
from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width, initval=0)

    fsm = lib.FSM(m, 'fsm')
    init = fsm.current()

    tmp = []
    for i in range(4):
        tmp.append( m.Reg('tmp_' + str(i), width, initval=0) )
        
    for i in range(4):
        fsm.add( tmp[i](fsm.current()) ) 
        fsm.goto_next(cond=None) # = fsm.add( fsm.set_next() ).inc()
        
    fsm.add( led(led + 1) )
    fsm.goto(init, cond=None) # = fsm.add( fsm.set(init) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            m.make_reset(),
        ).Else(
            fsm.make_case()
        ))
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
