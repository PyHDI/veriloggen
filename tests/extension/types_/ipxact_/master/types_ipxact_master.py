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
    sum = m.Reg('sum', 32, initval=0)
    led.assign(sum)

    # read address (1)
    araddr = 1024
    arlen = 64
    expected_sum = (araddr // 4 + araddr // 4 + arlen - 1) * arlen // 2

    ack, counter = myaxi.read_request_counter(araddr, arlen, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (1)
    data, valid, last = myaxi.read_data(counter, cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.Then().If(last).goto_next()

    # read address (2)
    araddr = 1024 + 1024
    arlen = 64
    expected_sum += (araddr // 4 + araddr // 4 + arlen - 1) * arlen // 2

    ack, counter = myaxi.read_request_counter(araddr, arlen, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (2)
    data, valid, last = myaxi.read_data(counter, cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.Then().If(last).goto_next()

    fsm(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )
    fsm.goto_next()

    fsm.make_always()

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

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst)
    memory.connect(ports, 'myaxi')

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

    m = mkMain()
    ipxact.to_ipxact(m,
                     clk_ports=[('CLK', ('RST',))],
                     rst_ports=[('RST', 'ACTIVE_HIGH')])
