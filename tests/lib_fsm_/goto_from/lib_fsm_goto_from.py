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

    """
    led = 0
    while True:
        count = 0
        while count < 1024:
            count += 1
        led += 1
    """
    
    fsm = lib.FSM(m, 'fsm', clk, rst)

    fsm.add( led(0) )
    fsm.goto_next()
    
    init = fsm.current()
    fsm.add( count(0) )
    fsm.goto_next()
    
    head = fsm.current()
    cond = count < 1024
    fsm.goto_next(cond=cond)
    
    fsm.add( count.inc() )
    fsm.goto_next()
    
    fsm.add( count.inc() )
    fsm.goto_next()
    
    fsm.add( count.inc() )
    fsm.goto_next()
    
    fsm.add( count.inc() )
    fsm.goto(head)
    fsm.inc()
    
    tail = fsm.current()
    fsm.add( led.inc() )
    fsm.goto_from(head, tail, cond=Not(cond))
    fsm.goto(init)
    
    fsm.make_always(reset=[count(0), led(0)])
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
