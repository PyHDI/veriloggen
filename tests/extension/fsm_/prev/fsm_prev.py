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

    fsm = FSM(m, 'fsm', clk, rst)

    for i in range(2):
        fsm.goto_next()

    # assert valid, then de-assert at the next cycle
    fsm.If(fsm.Prev(valid, 1) == 0)(
        valid(1)
    )
    fsm.Delay(1)(
        valid(0)
    )
    fsm.If(fsm.Prev(valid, 1) == 1).goto_next()

    for i in range(4):
        fsm.goto_next()

    # assert valid, then de-assert at the next cycle if not asserted again
    for i in range(4):
        fsm(valid(1))
        fsm.Delay(1)(valid(0))
        fsm.goto_next()

    fsm.make_always()

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
