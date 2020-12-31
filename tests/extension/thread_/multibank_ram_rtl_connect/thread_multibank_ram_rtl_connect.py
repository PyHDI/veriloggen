from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

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
    numbanks = 4
    ram_addrwidth = addrwidth - int(math.log(addrwidth, 2))
    myram = vthread.MultibankRAM(m, 'myram', clk, rst, datawidth, ram_addrwidth,
                                 numbanks=numbanks, numports=2)

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

    all_ok = m.Reg('all_ok', initval=1)
    i = m.Reg('i', 32, initval=0)

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
        wenable(0),
        i(0)
    )
    fsm.goto_next()

    fsm(
        addr.inc()
    )
    fsm.Delay(2)(
        sum.add(rdata),
        Display('rdata =  %d', rdata),
        If(NotEql(rdata,i))(all_ok(0)),
        i.inc(),
    )
    fsm.If(addr == read_size - 2).goto_next()

    fsm.goto_next()
    fsm.goto_next()

    # sum
    fsm(
        Display('sum =  %d', sum)
    )
    fsm.If(all_ok)(
        Display('# verify: PASSED')
    ).Else(
        Display('# verify: FAILED')
    )
    fsm.goto_next()

    # connect ports to RAM
    enable = 1
    myram.connect_rtl(1, addr, wdata, wenable, rdata, enable)

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
        Delay(10000),
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
