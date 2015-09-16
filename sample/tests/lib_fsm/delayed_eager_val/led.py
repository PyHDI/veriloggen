import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    valid = m.Output('valid')
    count = m.Reg('count', width=32, initval=0)
    
    valid_reg = m.Reg('valid_reg', 8, initval=0)
    m.Assign(valid(valid_reg[0]))
    
    up = m.Wire('up')
    down = m.Wire('down')
    m.Assign(up(1))
    m.Assign(down(0))
    
    fsm = lib.FSM(m, 'fsm')
    
    for i in range(4):
        fsm.goto_next()

    # condition alias
    c = count >= 16

    # assert valid if the condition is satisfied
    # then de-assert 3 cycles later with same condition
    fsm.add( valid_reg(up), cond=c, keep=3, eager_val=True)
    fsm.add( valid_reg(down), cond=c, delay=3, eager_val=True)
    fsm.goto_next(cond=c)
    
    for i in range(8):
        fsm.goto_next()

    # condition alias
    c = count >= 32

    # assert valid 1 cycle later if the condition is satisfied now
    # then de-assert 4 cycles later with same condition
    for i in range(8):
        fsm.add( valid_reg(up), cond=c, delay=1, keep=3, eager_val=True)
        fsm.add( valid_reg(down), cond=c, delay=4, eager_val=True)
        fsm.goto_next(cond=c)
    
    fsm.make_always(clk, rst, reset=[count.reset()], body=[count(count+1)])

    return m

def mkTest():
    m = Module('test')
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    valid = m.Wire('valid')

    uut = m.Instance(mkLed(), 'uut',
                     ports=(('CLK', clk), ('RST', rst), ('valid', valid)))

    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, period=100)

    init.add(
        Delay(1000),
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
