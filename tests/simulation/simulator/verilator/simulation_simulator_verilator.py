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
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width, initval=0)
    count = m.Reg('count', 32, initval=0)

    seq = Seq(m, 'seq', clk, rst)

    seq.If(count == 1024 - 1)(
        count(0)
    ).Else(
        count.inc()
    )

    seq.If(count == 1024 - 1)(
        led.inc()
    )

    seq(
        Systask('display', "LED:%d count:%d", led, count)
    )

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    uut = Submodule(m, led, name='uut')
    clk = uut['CLK']
    rst = uut['RST']

    # simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()

    sim = simulation.Simulator(test, sim='verilator')
    rslt = sim.run(outputfile='verilator.out', sim_time=1000 * 20)
    print(rslt)

    # sim.view_waveform()
