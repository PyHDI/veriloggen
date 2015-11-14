import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width, initval=0)
    count = m.Reg('count', 32, initval=0)

    fsm = lib.FSM(m, 'fsm', clk, rst)
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
    fsm.goto( dst=init, cond=(count < 1024), else_dst=fsm.next() ).inc()
    
    fsm.add( led(led + 1) )
    # jump by using label "here"
    fsm.goto(here)

    fsm.make_always()

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
