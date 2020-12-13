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
    myram = RAM(m, 'myram', clk, rst, datawidth, addrwidth, 2)
    myram.disable_write(1)

    df = dataflow.DataflowManager(m, clk, rst)
    fsm = FSM(m, 'fsm', clk, rst)

    # dataflow
    value = df.Counter()

    # write dataflow (Dataflow -> RAM)
    wport = 0
    waddr = 0
    wlen = 64
    done = myram.write_dataflow(wport, waddr, value, wlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    fsm.goto_next()

    # read dataflow (RAM -> Dataflow)
    rport = 1
    raddr = 0
    rlen = 32
    rdata, rlast, done = myram.read_dataflow(rport, raddr, rlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    # verify
    rdata_data, rdata_valid = rdata.read()
    rlast_data, rlast_valid = rlast.read()

    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (raddr + raddr + rlen - 1) * rlen // 2

    seq = Seq(m, 'seq', clk, rst)

    seq.If(rdata_valid)(
        sum.add(rdata_data)
    )
    seq.Then().If(rlast_data == 1).Delay(1)(
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
