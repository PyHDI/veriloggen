from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    x = m.Reg('x', 32, initval=0)
    y = m.Reg('y', 32, initval=0)
    z = m.Reg('z', 32, initval=0)

    seq_x = Seq(m, 'seq_x', clk, rst)
    seq_y = Seq(m, 'seq_y', clk, rst)
    seq_z = Seq(m, 'seq_z', clk, rst)

    seq_x.If(x < 16)(
        x.inc()
    )
    seq_x.If(x == 16).Delay(1)(
        x(0)
    )

    seq_y.If(y < 32)(
        y.inc()
    )
    seq_y.If(y == 32).Delay(2)(
        y(0)
    )

    prev_x = seq_x.Prev(x, 1)
    prev_y = seq_y.Prev(y, 1)

    seq_z(
        z(prev_x + prev_y)
    )

    seq_x.update(seq_y)
    seq_x.update(seq_z)

    seq_x.make_always()

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

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(10000),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
