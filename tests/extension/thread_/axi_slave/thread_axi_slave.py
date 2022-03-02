from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    saxi = vthread.AXISRegister(m, 'saxi', clk, rst, datawidth, length=4)

    def blink():

        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy
            size = saxi.read(2)

            sum = 0
            for i in range(size):
                sum += i

            saxi.write(3, sum)
            saxi.write(1, 0)  # unset busy

        vthread.finish()

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
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

    # memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg_name=memimg_name)
    # memory.connect(ports, 'myaxi')

    # AXI-Slave controller
    _saxi = vthread.AXIMVerify(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(ports, 'saxi')

    k = 100
    expected_sum = 0
    for i in range(k):
        expected_sum += i

    def ctrl():
        for i in range(100):
            pass

        # size
        awaddr = 8
        _saxi.write_delayed(awaddr, k, 10)

        # start
        awaddr = 0
        _saxi.write_delayed(awaddr, 1, 10)

        for _ in range(10):
            pass

        # busy check
        araddr = 4
        v = _saxi.read_delayed(araddr, 10)
        while v != 0:
            v = _saxi.read_delayed(araddr, 10)

        # result
        araddr = 12
        v = _saxi.read_delayed(araddr, 10)

        print('result = %d, expected = %d' % (v, expected_sum))

        if v == expected_sum:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000),
        Systask('finish'),
    )

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    if outputfile is None:
        outputfile = os.path.splitext(os.path.basename(__file__))[0] + '.out'

    memimg_name = 'memimg_' + outputfile

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
