import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    valid = m.OutputReg('valid', initval=0)
    
    fsm = lib.FSM(m, 'fsm')
    
    for i in range(2):
        fsm.goto_next()

    fsm.add( valid(1) )
    fsm.add( valid(0), delay=1 )
    
    for i in range(4):
        fsm.goto_next()
    
    for i in range(4):
        fsm.add( valid(1) )
        fsm.add( valid(0), delay=1 )
        fsm.goto_next()
    
    for i in range(4):
        fsm.goto_next()
    
    m.Always(Posedge(clk))(
        If(rst)(
            m.reset(),
            fsm.reset()
        ).Else(
            fsm.to_case()
        ))

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
