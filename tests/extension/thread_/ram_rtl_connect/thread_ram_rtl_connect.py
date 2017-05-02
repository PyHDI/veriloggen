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
    addrwidth = 10
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth, numports=2)

    read_size = 10
    write_size = read_size

    write_done = m.Reg('write_done', initval=0)

    addr = m.Reg('addr', addrwidth, initval=0)
    wdata = m.Reg('wdata', datawidth, initval=0)
    wenable = m.Reg('wenable', initval=0)
    rdata = m.Wire('rdata', datawidth)
    sum = m.Reg('sum', datawidth, initval=0)

    fsm = FSM(m, 'fsm', clk, rst)
    fsm.If(write_done).goto_next()

    # write
    fsm(
        addr(-1),
        wdata(-1),
        wenable(0)
    )
    fsm.goto_next()

    fsm(
        addr.inc(),
        wdata.inc(),
        wenable(1)
    )
    fsm.Delay(1)(
        Display('wdata =  %d', wdata),
        wenable(0)
    )
    fsm.If(addr == write_size - 2).goto_next()

    # read
    fsm(
        addr(-1),
        wenable(0)
    )
    fsm.goto_next()

    fsm(
        addr.inc()
    )
    fsm.Delay(2)(
        sum.add(rdata),
        Display('rdata =  %d', rdata)
    )
    fsm.If(addr == read_size - 2).goto_next()

    fsm.goto_next()
    fsm.goto_next()

    # sum
    fsm(
        Display('sum =  %d', sum)
    )
    fsm.goto_next()

    # connect ports to RAM
    myram.connect_rtl(1, addr, wdata, wenable, rdata)

    def blink(times):
        write_done.value = 0
        for i in range(times):
            wdata = i + 100
            myram.write(i, wdata)
            print('wdata = %d' % wdata)
        write_done.value = 1

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(read_size)

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

    simulation.setup_waveform(m, uut)
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
