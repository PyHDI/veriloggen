from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.axi as axi


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    myaxi = axi.AxiLiteMaster(m, 'myaxi', clk, rst)
    myaxi.disable_read()

    fsm = FSM(m, 'fsm', clk, rst)

    # write address (1)
    awaddr = 1024

    ack = myaxi.write_request(awaddr, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (1)
    wdata = m.Reg('wdata', 32, initval=1024)

    ack = myaxi.write_data(wdata, cond=fsm)

    fsm.If(ack)(
        wdata.inc()
    )
    fsm.Then().goto_next()

    # write address (2)
    awaddr = 1024 + 1024

    ack = myaxi.write_request(awaddr, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (2)
    ack = myaxi.write_data(wdata, cond=fsm)

    fsm.If(ack)(
        wdata.inc()
    )
    fsm.Then().goto_next()

    fsm.goto_next()
    fsm.goto_next()

    sum = m.Reg('sum', 32, initval=0)
    expected_sum = 1024 + 1025

    seq = Seq(m, 'seq', clk, rst)
    seq.If(Ands(myaxi.wdata.wvalid, myaxi.wdata.wready))(
        sum.add(myaxi.wdata.wdata)
    )
    seq.Then().Delay(1)(
        Systask('display', "sum=%d expected_sum=%d", sum, expected_sum),
        If(fsm.here)(If(NotEql(sum, expected_sum))(
            Display('# verify: FAILED')).Else(Display('# verify: PASSED')))
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

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst)
    memory.connect(ports, 'myaxi')

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
