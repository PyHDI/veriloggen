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

    myaxi = axi.AxiMaster(m, 'myaxi', clk, rst)

    fsm = FSM(m, 'fsm', clk, rst)

    # write request (1)
    awaddr1 = 1024
    awlen1 = 64
    ack = myaxi.write_request(awaddr1, awlen1, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (1)
    wdata1 = m.Reg('wdata1', 32, initval=0)
    wlast1 = wdata1 == awlen1 - 1
    ack = myaxi.write_data(wdata1, wlast1, cond=fsm)

    fsm.If(ack)(
        wdata1.inc()
    )
    fsm.If(ack, wlast1).goto_next()

    # write request (2)
    awaddr2 = 1024 + 1024
    awlen2 = 64 + 64
    ack = myaxi.write_request(awaddr2, awlen2, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (2)
    wdata2 = m.Reg('wdata2', 32, initval=0)
    wlast2 = wdata2 == awlen2 - 1
    ack = myaxi.write_data(wdata2, wlast2, cond=fsm)

    fsm.If(ack)(
        wdata2.inc()
    )
    fsm.If(ack, wlast2).goto_next()
    fsm.If(Not(myaxi.wdata.wvalid)).goto_next()

    # read request (1)
    araddr1 = awaddr1
    arlen1 = awlen1
    ack = myaxi.read_request(araddr1, arlen1, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (1)
    data, valid, last = myaxi.read_data(cond=fsm)
    sum = m.Reg('sum', width=32, initval=0)

    fsm.If(valid)(
        sum.add(data)
    )
    fsm.If(valid, last).goto_next()

    # read request (2)
    araddr2 = awaddr2
    arlen2 = awlen2
    ack = myaxi.read_request(araddr2, arlen2, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (2)
    data, valid, last = myaxi.read_data(cond=fsm)

    fsm.If(valid)(
        sum.add(data)
    )
    fsm.If(valid, last).goto_next()

    # verify
    expected_sum = (((0 + awlen1 - 1) * awlen1) // 2 +
                    ((0 + awlen2 - 1) * awlen2) // 2)
    fsm(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )
    fsm.If(sum == expected_sum)(
        Systask('display', '# verify: PASSED')
    ).Else(
        Systask('display', '# verify: FAILED')
    )
    fsm.goto_next()

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

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg_name=memimg_name)
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
