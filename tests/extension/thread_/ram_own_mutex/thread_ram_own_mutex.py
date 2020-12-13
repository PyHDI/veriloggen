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
    led = m.OutputReg('LED', 8)

    datawidth = 32
    addrwidth = 10
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth)

    def myfunc(tid, size):
        myram.lock()
        print("Thread %d Lock" % tid)

        for i in range(size):
            read_data = myram.read(i)
            write_data = read_data + tid + i
            myram.write(i, write_data)
            print("Thread %d ram[%d] <- %d" % (tid, i, write_data))

        myram.unlock()
        print("Thread %d Unlock" % tid)

    def blink():
        all_ok = True

        size = 16
        for i in range(size):
            myram.write(i, 0)

        for tid in range(numthreads):
            pool.run(tid, tid, size)

        for tid in range(numthreads):
            pool.join(tid)

        for i in range(size):
            read_data = myram.read(i)
            led.value = read_data
            print("result ram[%d] = %d" % (i, read_data))

            expected = i * numthreads + (0 + numthreads - 1) * numthreads // 2
            if vthread.verilog.NotEql(read_data, expected):
                all_ok = False
                print(i, read_data, expected)

        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    pool = vthread.ThreadPool(m, 'th_myfunc', clk, rst, myfunc, numthreads)
    fsm = th.start()

    return m


def mkTest(memimg_name=None):
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
        # Delay(10000),
        Delay(100000),
        Systask('finish'),
    )

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    if outputfile is None:
        outputfile = os.path.splitext(os.path.basename(__file__))[0] + '.out'

    memimg_name = 'memimg_' + outputfile

    test = mkTest(memimg_name=memimg_name)

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=outputfile)
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
