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
    sum = m.OutputReg('sum', 32, initval=0)

    myaxi = axi.AxiLiteSlave(m, 'myaxi', clk, rst)
    myaxi.disable_read()

    fsm = FSM(m, 'fsm', clk, rst)

    # write address
    addr, valid = myaxi.pull_write_request(cond=fsm)
    fsm.If(valid).goto_next()

    # write data
    data, mask, valid = myaxi.pull_write_data(cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
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
    sum = ports['sum']

    _axi = axi.AxiLiteMaster(m, '_axi', clk, rst, noio=True)
    _axi.disable_read()

    _axi.connect(ports, 'myaxi')

    fsm = FSM(m, 'fsm', clk, rst)

    for i in range(100):
        fsm.goto_next()

    # write address (1)
    awaddr = 1024
    wval = 100
    expected_sum = wval

    ack = _axi.write_request(awaddr, cond=fsm)
    wdata = m.Reg('wdata', 32, initval=0)
    fsm.If(ack)(
        wdata(wval)
    )
    fsm.If(ack).goto_next()

    # write data (1)
    ack = _axi.write_data(wdata, cond=fsm)
    fsm.If(ack).goto_next()

    # write address (2)
    wval = 200
    expected_sum += wval

    ack = _axi.write_request(awaddr, cond=fsm)
    fsm.If(ack)(
        wdata(wval)
    )
    fsm.If(ack).goto_next()

    # write data (2)
    ack = _axi.write_data(wdata, cond=fsm)
    fsm.If(ack).goto_next()

    for i in range(4):
        fsm.goto_next()

    fsm(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )
    fsm.goto_next()

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


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # sim.view_waveform()
