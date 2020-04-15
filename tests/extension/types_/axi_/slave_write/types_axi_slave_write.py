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

    myaxi = axi.AxiSlave(m, 'myaxi', clk, rst)
    myaxi.disable_read()

    fsm = FSM(m, 'fsm', clk, rst)

    # write address
    addr, counter, valid = myaxi.pull_write_request_counter(cond=fsm)
    fsm.If(valid).goto_next()

    # write data
    data, mask, valid, last = myaxi.pull_write_data(counter, cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.Then().If(last).goto_next()

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

    _axi = axi.AxiMaster(m, '_axi', clk, rst, noio=True)
    _axi.disable_read()

    _axi.connect(ports, 'myaxi')

    fsm = FSM(m, 'fsm', clk, rst)

    # write address (1)
    awaddr = 1024
    awlen = 64
    expected_sum = ((0 + (awlen - 1)) * awlen) // 2

    ack, counter = _axi.write_request_counter(awaddr, awlen, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (1)
    wdata = m.Reg('wdata', 32, initval=0)

    ack, last = _axi.write_data(wdata, counter, cond=fsm)

    fsm.If(ack)(
        wdata.inc()
    )
    fsm.If(last).goto_next()

    # write address (2)
    prev_awlen = awlen
    awlen = 128
    expected_sum += ((prev_awlen + (prev_awlen + awlen - 1)) * awlen) // 2

    ack, counter = _axi.write_request_counter(awaddr, awlen, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (2)
    ack, last = _axi.write_data(wdata, counter, cond=fsm)

    fsm.If(ack)(
        wdata.inc()
    )
    fsm.If(last).goto_next()

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
