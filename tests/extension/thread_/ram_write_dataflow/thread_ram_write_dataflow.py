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

    fsm.goto_next()

    # dataflow
    value = df.Counter(size=64)
    value = value - 1

    # write dataflow (Dataflow -> RAM)
    wport = 0
    waddr = 0
    wlen = 64
    done = myram.write_dataflow(wport, waddr, value, wlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    # verify
    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (waddr + waddr + wlen - 1) * wlen // 2 - wlen

    seq = Seq(m, 'seq', clk, rst)
    seq.If(myram[0].wenable)(
        sum.add(myram[0].wdata)
    )
    seq.Then().If(myram[0].addr == wlen - 1).Delay(2)(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )

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
