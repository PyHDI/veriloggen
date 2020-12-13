from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
from veriloggen.thread import FIFO


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2))

    myfifo = FIFO(m, 'myfifo', clk, rst, datawidth, addrwidth)

    # example how to access BRAM
    count = m.Reg('count', 32, initval=0)
    sum = m.Reg('sum', 32, initval=0)

    fsm = FSM(m, 'fsm', clk, rst)

    fsm(
        count(0),
    )

    fsm.goto_next()

    step = n - 2

    ack, ready = myfifo.enq_rtl(count, cond=fsm)

    fsm.If(ready)(
        count.inc()
    )

    fsm.If(ack)(
        Systask('display', 'count=%d space=%d has_space=%d',
                myfifo.count, myfifo.space, myfifo.has_space())
    )

    fsm.If(Ands(ready, count == step - 1)).goto_next()

    fsm(
        count(0)
    )

    fsm.goto_next()

    data, valid, ready = myfifo.deq_rtl(cond=fsm)

    fsm.If(valid)(
        sum(sum + data),
        count.inc(),
        Systask('write', 'count=%d space=%d has_space=%d ',
                myfifo.count, myfifo.space, myfifo.has_space())
    )

    fsm.Then().Delay(1)(
        Systask('display', "sum=%d", sum)
    )

    fsm.If(count == step).goto_next()

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
