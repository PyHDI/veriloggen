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

    myaxi = axi.AxiLiteSlave(m, 'myaxi', clk, rst)
    myaxi.disable_write()

    fsm = FSM(m, 'fsm', clk, rst)

    # read address
    addr, valid = myaxi.pull_read_request(cond=fsm)
    rdata = m.Reg('rdata', 32, initval=0)
    fsm.If(valid)(
        rdata(addr >> 2)
    )
    fsm.If(valid).goto_next()

    # read rdata
    ack = myaxi.push_read_data(rdata, cond=fsm)
    fsm.If(ack)(
        rdata(rdata + 1)
    )
    fsm.Then().goto_next()

    fsm.goto_init()

    return m


def mkTest():
    m = Module('test')

    # target instance
    main = mkMain()

    # copy paras and ports
    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    _axi = axi.AxiLiteMaster(m, '_axi', clk, rst, noio=True)
    _axi.disable_write()

    _axi.connect(ports, 'myaxi')

    fsm = FSM(m, 'fsm', clk, rst)
    sum = m.Reg('sum', 32, initval=0)

    # read address (1)
    araddr = 1024
    expected_sum = araddr // 4

    ack = _axi.read_request(araddr, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (1)
    data, valid = _axi.read_data(cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.Then().goto_next()

    # read address (2)
    araddr = 1024 + 1024
    expected_sum += araddr // 4

    ack = _axi.read_request(araddr, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (2)
    data, valid = _axi.read_data(cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.Then().goto_next()

    fsm(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )
    fsm.goto_next()

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
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

    # sim.view_waveform()
