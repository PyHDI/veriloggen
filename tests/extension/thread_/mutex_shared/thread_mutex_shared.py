from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread


def mkLed(numthreads=8):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', 8)

    count = vthread.Shared(m.Reg('count', 32, initval=0))
    led.assign(count.value)

    mymutex = vthread.Mutex(m, 'mymutex', clk, rst)

    def myfunc(tid):
        mymutex.lock()
        print("Thread %d Lock" % tid)

        for i in range(20):
            pass  # sleep

        count.write(count.value + 1)
        print("Thread %d count = %d" % (tid, count.value))

        mymutex.unlock()
        print("Thread %d Unlock" % tid)

    def blink():
        count.write(0)
        for tid in range(numthreads):
            pool.run(tid, tid)

        for tid in range(numthreads):
            pool.join(tid)

        print("result count = %d" % count.value)

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    pool = vthread.ThreadPool(m, 'th_myfunc', clk, rst, myfunc, numthreads)
    fsm = th.start()

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
