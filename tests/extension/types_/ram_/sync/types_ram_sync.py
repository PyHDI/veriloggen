from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.ram as ram


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2

    myram = ram.SyncRAM(m, 'myram', clk, datawidth, addrwidth, 2)

    seq = Seq(m, 'seq', clk, rst)

    # write
    waddr = m.Reg('waddr', 32, initval=0)
    wdata = m.Reg('wdata', 32, initval=0)
    wenable = waddr < 16

    myram.connect(0, waddr, wdata, wenable)

    seq.If(wenable)(
        waddr.inc(),
        wdata.inc()
    )

    all_ok = m.Reg('all_ok', initval=1)
    i = m.Reg('i', 32, initval=0)

    seq.If(waddr == 15, wenable == 1)(
        all_ok(1),
        i(0)
    )

    # read
    raddr = m.Reg('raddr', 32, initval=0)
    renable = Ands(raddr < 16, waddr == 16)

    myram.connect(1, raddr, 0, 0)

    seq.If(renable)(
        raddr.inc()
    )

    rdata = myram.rdata(1)
    rvalid = seq.Prev(renable, 1)

    sum = m.Reg('sum', 32, initval=0)

    seq.If(rvalid)(
        sum(sum + rdata),
        If(NotEql(rdata, i))(all_ok(0)),
        i.inc()
    )

    seq.Then().Delay(1)(
        Systask('display', "sum=%d", sum)
    )

    seq.If(i == 15, rvalid).Delay(1)(
        If(all_ok)(
            Display('# verify: PASSED')
        ).Else(
            Display('# verify: FAILED')
        )
    )

    seq.make_always()

    return m


def mkTest(memimg_name=None):
    m = Module('test')

    # target instance
    main = mkMain()

    # copy paras and ports
    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    # simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
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
