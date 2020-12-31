from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
from veriloggen.thread import RAM


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2

    myram = RAM(m, 'myram', clk, rst, datawidth, addrwidth, 1)

    # example how to access RAM
    count = m.Reg('count', 32, initval=0)
    sum = m.Reg('sum', 32, initval=0)
    addr = m.Reg('addr', 32, initval=0)

    fsm = FSM(m, 'fsm', clk, rst)

    fsm(
        addr(0),
        count(0),
        sum(0)
    )

    fsm.goto_next()

    step = 16

    myram.write_rtl(addr, count, port=0, cond=fsm)

    fsm(
        addr.inc(),
        count.inc()
    )

    fsm.If(count == step - 1)(
        addr(0),
        count(0)
    )

    fsm.Then().goto_next()

    read_data, read_valid = myram.read_rtl(addr, port=0, cond=fsm)

    fsm(
        addr.inc(),
        count.inc()
    )

    fsm.If(read_valid)(
        sum(sum + read_data)
    )

    fsm.Then().Delay(1)(
        Systask('display', "sum=%d", sum)
    )

    fsm.If(count == step - 1)(
        addr(0),
        count(0)
    ).Then().goto_next()

    fsm.If(read_valid)(
        sum(sum + read_data)
    )

    fsm.Then().Delay(1)(
        Systask('display', "sum=%d", sum)
    )

    fsm.goto_next()

    fsm(
        Systask('display', "expected_sum=%d", (step - 1) * step // 2)
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
