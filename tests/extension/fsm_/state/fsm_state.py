from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    valid = m.OutputReg('valid', initval=0)
    counter = m.Reg('counter', 8, initval=0)

    fsm = FSM(m, 'fsm', clk, rst)

    s0 = fsm.init
    s1 = fsm.State(s0).If(valid).goto_next()
    s2 = fsm.State(s1).If(valid).goto_next()
    s3 = fsm.State(s2).If(counter[0] == 0).goto(fsm.next)
    s1_ = fsm.State(s2).Elif(counter[1] == 1).goto(s1)
    s2_ = fsm.State(s2).Else.goto(s2)
    s0_ = fsm.State(s3).goto(s0)

    fsm.Always.If(counter <= 2 ** 8 - 1)(
        counter.inc()
    ).Else(
        counter(0)
    )

    fsm.State(s0).If(counter == 10)(
        valid(0)
    ).Else(
        valid(1)
    )

    fsm.State(s1).If(counter == 20)(
        valid(0)
    ).Else(
        valid(1)
    )

    fsm.State(s2).If(counter == 30)(
        valid(0)
    ).Else(
        valid(1)
    )

    fsm.State(s0_).If(counter == 40)(
        valid(0)
    ).Else(
        valid(1)
    )

    return m


def mkTest():
    m = Module('test')
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    valid = m.Wire('valid')

    uut = m.Instance(mkLed(), 'uut',
                     ports=(('CLK', clk), ('RST', rst), ('valid', valid)))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, period=100)

    init.add(
        Delay(1000),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
