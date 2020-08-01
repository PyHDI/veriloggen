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

    datawidth = 32
    addrwidth = 4
    myfifo = vthread.FixedFIFO(m, 'myfifo', clk, rst,
                               datawidth, addrwidth, point=8)

    def blink(times):
        # enque as many data as possible
        wdata = 0
        ack = True
        while ack:
            ack = myfifo.try_enq(wdata)
            if ack:
                print('wdata = %d' % wdata)
            wdata += 1

        # deque as many data as possible
        sum = vthread.fixed.FixedConst(0, point=8)
        rvalid = True
        while rvalid:
            rdata, rvalid = myfifo.try_deq()
            if rvalid:
                sum += rdata
                print('rdata = %d (%f)' % (rdata.int_part, rdata))

        print('sum = %d (%f)' % (sum.int_part, sum))

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
