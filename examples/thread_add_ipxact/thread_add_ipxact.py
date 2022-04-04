from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi
import veriloggen.types.ipxact as ipxact


def mkLed():
    m = Module('add')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst,
                                    datawidth=32, length=8)

    def add():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy

            a = saxi.read(2)
            b = saxi.read(3)
            c = a + b

            saxi.write(4, c)
            saxi.write(1, 0)  # unset busy

    th = vthread.Thread(m, 'th_add', clk, rst, add)
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

    # AXI-Slave controller
    _saxi = vthread.AXIMLite(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(ports, 'saxi')

    # Timer
    counter = m.Reg('counter', 32, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        counter.inc()
    )

    def ctrl():
        for i in range(100):
            pass

        awaddr = 2 * 4
        a = 10
        print('# a = %d' % a)
        _saxi.write(awaddr, a)

        awaddr = 3 * 4
        b = 20
        print('# b = %d' % b)
        _saxi.write(awaddr, b)

        awaddr = 0 * 4
        start_time = counter
        print('# start time = %d' % start_time)
        _saxi.write(awaddr, 1)

        araddr = 1 * 4
        while True:
            busy = _saxi.read(araddr)
            if not busy:
                break

        araddr = 4 * 4
        c = _saxi.read(araddr)
        print('# c = %d' % c)

        end_time = counter
        print('# end time = %d' % end_time)
        time = end_time - start_time
        print('# exec time = %d' % time)

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(100000),
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

    m = mkLed()
    ipxact.to_ipxact(m,
                     clk_ports=[('CLK', ('RST',))],
                     rst_ports=[('RST', 'ACTIVE_HIGH')])
