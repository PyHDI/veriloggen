from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

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
    
    fsm = FSM(m, 'fsm', clk, rst)

    fsm( led(0) )
    fsm.goto_next()
    
    init = fsm.current
    fsm( count(0) )
    fsm.goto_next()
    
    head = fsm.current
    cond = count < 1024
    fsm.goto_next(cond=cond)
    
    fsm( count.inc() )
    fsm.goto_next()
    
    fsm( count.inc() )
    fsm.goto(head)
    fsm.inc()
    
    tail = fsm.current
    fsm.goto_from(head, tail, cond=Not(cond))
    
    fsm( led.inc() )
    fsm.goto(init)
    
    #fsm.make_always()
    # make_alway() is called when to_veirlog() is called.
    #m.add_hook(fsm.make_always, args=(), kwargs={})
    # In the current implementation, make_always() is always and
    # automatically called with no registration.
    
    return m

if __name__ == '__main__':
    led = mkLed()
    # to_verilog() method is immuatable.
    # Hooked methods are called for the copied object to keep the internal state.
    dummy = led.to_verilog()
    verilog = led.to_verilog()
    print(verilog)
