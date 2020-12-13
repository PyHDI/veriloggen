from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread


class MySender(object):
    __intrinsics__ = ('send', 'wait')

    def __init__(self, m, clk, rst):
        self.m = m
        self.clk = clk
        self.rst = rst

        self.data = self.m.TmpReg(8, initval=0)
        self.enable = self.m.TmpReg(initval=0)
        self.ready = self.m.TmpWire()
        self.ready.assign(1)

    def send(self, fsm, value):
        fsm(
            self.data(value),
            self.enable(1),
            Display("data = %d", value)
        )
        fsm.goto_next()
        fsm(
            self.enable(0)
        )
        fsm.goto_next()
        return 0

    def wait(self, fsm):
        fsm.If(self.ready).goto_next()
        return 0


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    my_sender = MySender(m, clk, rst)

    def blink(times):
        for i in range(times):
            data = i + 100
            my_sender.send(data)
            my_sender.wait()

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(10)

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

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(10000),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)
