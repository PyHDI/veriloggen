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
    reuse_size = 4

    rdata0, rdata1, rlast, done = myram.read_dataflow_reuse(rport, raddr, rlen,
                                                            num_outputs=2,
                                                            reuse_size=reuse_size,
                                                            cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    # verify
    rdata0_data, rdata0_valid = rdata0.read()
    rdata1_data, rdata1_valid = rdata1.read()
    rlast_data, rlast_valid = rlast.read()

    sum0 = m.Reg('sum0', 32, initval=0)
    sum1 = m.Reg('sum1', 32, initval=0)
    expected_sum = ((raddr + raddr + rlen - 1) * rlen // 2) * reuse_size

    seq = Seq(m, 'seq', clk, rst)

    seq.If(rdata0_valid)(
        sum0.add(rdata0_data),
        Systask('display', 'rdata0_data=%d', rdata0_data)
    )
    seq.If(rdata1_valid)(
        sum1.add(rdata1_data),
        Systask('display', 'rdata1_data=%d', rdata1_data)
    )
    seq.Then().If(rlast_data == 1).Delay(1)(
        Systask('display', 'sum=%d expected_sum=%d', sum0 + sum1, expected_sum),
        If(NotEql(sum0 + sum1, expected_sum))(Display('# verify: FAILED')).Else(Display('# verify: PASSED'))
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
