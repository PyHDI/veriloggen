from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    ready = m.Input('ready')
    valid = m.OutputReg('valid', initval=0)
    count = m.Reg('count', width=32, initval=0)
    
    fsm = FSM(m, 'fsm', clk, rst)

    for i in range(2):
        fsm.goto_next()

    # assert valid, then de-assert at the next cycle
    fsm(
        valid(1)
    )
    
    fsm.Delay(1)(
        valid(0)
    )

    for i in range(2):
        fsm.goto_next()

    # assert valid and go to the next state if a condition is satisfied now
    # then de-assert at the next cycle with the same condition
    fsm.If(ready==1)(
        valid(1)
    )
    fsm.If(ready==1).Delay(1)(
        valid(0)
    )
    
    fsm.If(ready==1).goto_next()
    
    for i in range(2):
        fsm.goto_next()

    # condition alias
    c = AndList((count >= 16), (ready==1))

    # assert valid 1 cycle later if a condition is satisfied now
    # then de-assert 3 cycles later with the same condition
    for i in range(4):
        fsm.If(c).Delay(1).Keep(2)(
            valid(1)
        )
        fsm.If(c).Delay(3)(
            valid(0)
        )
        fsm.If(c).goto_next()

    # build always statement
    fsm.make_always(reset=[count(0)], body=[count(count + 1)])

    return m

def mkTest():
    m = Module('test')
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    ready = m.Reg('ready', initval=0)
    valid = m.Wire('valid')    

    uut = m.Instance(mkLed(), 'uut',
                     #ports=(('CLK', clk), ('RST', rst), ('ready', ready), ('valid', valid)))
                     ports=connect_same_name(clk, rst, ready, valid))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        [ simulation.next_clock(clk) for i in range(8) ],
        ready(1),
        Delay(1000),
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
