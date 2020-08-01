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
    led = m.Output('LED', 8)
    led.assign(0)

    def blink(times):
        a, b, c = 100, 200, 300
        th_subth.run(a, b, c)
        print('# subth run')

        th_subth.join()
        rslt = th_subth.ret()
        print('# subth join: rslt=%d' % rslt)

        th_subth.reset()

        a, b, c = 100, 200, 300
        th_subth.run(a, b, c)
        print('# subth run')

        th_subth.join()
        rslt = th_subth.ret()
        print('# subth join: rslt=%d' % rslt)

    def subth(a, b, c):
        print('# subth start: %d, %d, %d' % (a, b, c))

        for i in range(10):
            print('# subth wait: %d' % i)

        ret = a + b + c
        print('# subth end: %d' % ret)

        return ret

    th_blink = vthread.Thread(m, 'th_blink', clk, rst, blink)
    th_subth = vthread.Thread(m, 'th_subth', clk, rst, subth)
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
