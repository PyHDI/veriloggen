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

    fsm = lib.FSM(m, 'fsm')
    # get the initial index (= 0)
    init = fsm.current()

    fsm.add( count(count + 1) )
    fsm.goto_next()
    fsm.add( count(count + 2) )
    fsm.goto_next()
    
    # get the current index (= 2)
    here = fsm.current()
    fsm.add( count(count + 3) )
    fsm.goto_next()

    # jump by using label "init"
    fsm.goto( index=init, cond=(count < 1024), else_index=fsm.next() ).inc()
    # = fsm.add( If(count < 1024)( fsm.set(init) ).Else( fsm.set_next() ) ).inc()
    
    fsm.add( led(led + 1) )
    # jump by using label "here"
    fsm.goto(here)
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0),
            fsm.set_init()
        ).Else(
            # inserting the FSM body
            fsm.to_case()
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
