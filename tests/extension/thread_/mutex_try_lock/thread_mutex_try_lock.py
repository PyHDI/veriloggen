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

    mymutex = vthread.Mutex(m, 'mymutex', clk, rst)

    def myfunc(tid):
        print("-- Thread %d TryLock" % tid)
        lock = mymutex.try_lock()
        waitcount = 0
        while not lock:
            print("-- Thread %d TryLock" % tid)
            waitcount += 1
            lock = mymutex.try_lock()

        print("Thread %d Lock: waitcount=%d" % (tid, waitcount))

        for i in range(20):
            pass  # sleep

        print("Thread %d Hello" % tid)

        mymutex.unlock()
        print("Thread %d Unlock" % tid)

    def blink():
        for tid in range(numthreads):
            pool.run(tid, tid)

        for tid in range(numthreads):
            pool.join(tid)

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
