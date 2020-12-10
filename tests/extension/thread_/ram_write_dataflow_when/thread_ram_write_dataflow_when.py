from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
from veriloggen.thread import RAM
import veriloggen.dataflow as dataflow


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2
    myram = RAM(m, 'myram', clk, rst, datawidth, addrwidth)

    df = dataflow.DataflowManager(m, clk, rst)
    # df.enable_draw_graph()

    fsm = FSM(m, 'fsm', clk, rst)

    length = 8
    a = df.Counter()
    b = df.Counter(size=length)
    c = b == 0

    wport = 0
    waddr = 0
    wlen = 32
    done = myram.write_dataflow(wport, waddr, a, wlen, cond=fsm, when=c)

    fsm.goto_next()
    fsm.If(done).goto_next()

    # verify
    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (waddr + waddr + (wlen - 1) * length) * wlen // 2

    seq = Seq(m, 'seq', clk, rst)

    seq.If(myram[0].wenable)(
        sum.add(myram[0].wdata)
    )
    seq.Then().If(myram[0].addr == wlen - 1).Delay(2)(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum),
        If(NotEql(sum, expected_sum))(Display('# verify: FAILED')).Else(Display('# verify: PASSED'))
    )

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
