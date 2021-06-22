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

    s0 = fsm.init  # -> State(fsm, 0)
    s1 = s0.If(valid).goto_next()  # -> State(fsm, 1)
    s2 = s1.If(valid).goto_next()  # -> State(fsm, 2)
    s3 = s2.If(counter[0] == 0).goto(s2.next)  # -> State(fsm, 3)
    s1_ = s2.Elif(counter[1] == 1).goto(s1)  # -> State(fsm, 1)
    s2_ = s2.Else.goto(s2)  # -> State(fsm, 2)
    s0_ = s3.goto(s0)  # -> State(fsm, 0)

    fsm.Always.If(counter <= 2 ** 8 - 1)(
        counter.inc()
    ).Else(
        counter(0)
    )

    s0.If(counter == 10)(
        valid(0)
    )
    s0.Else(
        valid(1)
    )

    s1.If(counter == 20)(
        valid(0)
    )
    s1.Else(
        valid(1)
    )

    s2.If(counter == 30)(
        valid(0)
    )
    s2.Else(
        valid(1)
    )

    s0_.If(counter == 40)(
        valid(0)
    )
    s0_.Else(
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
