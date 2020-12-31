from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread


def mkLed(numthreads=4):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    def blink(times):
        for tid in range(numthreads * 2):
            pool.run(tid, tid)

        sum = 0
        for tid in range(numthreads * 2):
            pool.join(tid)
            sum += pool.ret(tid)

        print('sum = %d' % sum)

    def myfunc_a(tid):
        print('myfunc_a: tid = %d' % tid)
        for i in range(30 - tid):
            pass
        return tid + 100

    def myfunc_b(tid):
        print('myfunc_b: tid = %d' % tid)
        for i in range(30 - tid):
            pass
        return tid + 200

    threads = [vthread.Thread(m, 'th_myfunc_a_%d' % i, clk, rst, myfunc_a)
               for i in range(numthreads)]
    threads += [vthread.Thread(m, 'th_myfunc_b_%d' % i, clk, rst, myfunc_b)
                for i in range(numthreads)]
    pool = vthread.to_thread_pool(threads)
    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(20)

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
