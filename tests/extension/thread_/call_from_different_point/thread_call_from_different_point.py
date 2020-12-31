from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    def blink(times):
        for i in range(times):
            if i & 0x1 == 0:
                th_func_a.run(i + 200, 2000)
            else:
                th_func_a.run(i + 100)

            for j in range(10):
                pass

            th_func_a.join()
            th_func_a.reset()
            v = th_func_a.ret()
            print("func_a: %d" % v)

    def func_a(a, b=1000):
        for i in range(4):
            pass
        return a + b

    th_blink = vthread.Thread(m, 'th_blink', clk, rst, blink)
    th_func_a = vthread.Thread(m, 'th_func_a', clk, rst, func_a)
    fsm = th_blink.start(20)

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
