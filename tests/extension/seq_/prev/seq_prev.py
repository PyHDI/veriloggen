from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *


def mkLed(window_size=8):
    if window_size < 0:
        raise ValueError('window_size must be larger than 0')
    if math.log(window_size, 2) % 1.0 != 0.0:
        raise ValueError('window_size must be power of 2')

    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    x = m.Input('x', 32)
    y = m.OutputReg('y', 32, initval=0)

    seq = Seq(m, 'seq', clk, rst)
    v = x
    for w in range(window_size - 1):
        v = v + seq.Prev(x, w + 1)

    t = m.TmpReg(32)
    seq(
        t(v)
    )
    seq(
        y(t >> int(math.log(window_size, 2)))
    )

    seq.make_always()

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']
    x = ports['x']
    y = ports['y']

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_stmt = []
    reset_stmt.append(x(0))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),

        [(nclk(clk), x(i + 10)) for i in range(10)],
        nclk(clk), x(0),

        Delay(1000),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
