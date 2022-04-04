from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.axi as axi

import veriloggen.types.ipxact as ipxact


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', 32)

    myaxi = axi.AxiMaster(m, 'myaxi', clk, rst)
    myaxi.disable_write()

    fsm = FSM(m, 'fsm', clk, rst)

    # read request (1)
    araddr1 = 1024
    arlen1 = 64
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
    araddr2 = 1024 + 1024
    arlen2 = 64 + 64
    ack = myaxi.read_request(araddr2, arlen2, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (2)
    data, valid, last = myaxi.read_data(cond=fsm)

    fsm.If(valid)(
        sum.add(data)
    )
    fsm.If(valid, last).goto_next()

    # verify
    expected_sum = (((araddr1 // 4 + araddr1 // 4 + arlen1 - 1) * arlen1) // 2 +
                    ((araddr2 // 4 + araddr2 // 4 + arlen2 - 1) * arlen2) // 2)
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

    # IP-XACT
    m = mkMain()
    ipxact.to_ipxact(m,
                     clk_ports=[('CLK', ('RST',))],
                     rst_ports=[('RST', 'ACTIVE_HIGH')])
