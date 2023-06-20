from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.dataflow as dataflow


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    a = dataflow.Parameter('aparam', 10)  # parameter
    b = dataflow.ParameterVariable('bparam')  # input / wire

    xparam = m.Parameter('xparam', 100)
    x = dataflow.ParameterVariable(xparam)

    yparam = m.Reg('yparam', 32, initval=0)
    y = dataflow.ParameterVariable(yparam)

    zparam = 30
    z = dataflow.ParameterVariable(zparam, signed=True)

    v = dataflow.Variable('vdata')
    w = dataflow.Variable('wdata')

    c = v + a + b + x + y + 1 + z + w
    c.output('cdata', valid='cvalid')

    # synthesize dataflow
    df = dataflow.Dataflow(c)
    df.implement(m, clk, rst, aswire=True)
    # df.draw_graph()

    fsm = FSM(m, 'fsm', clk, rst)
    count = m.TmpReg(32, initval=0)

    b.raw_data.assign(20)
    v.raw_data.assign(1000)
    w.raw_data.assign(2000)

    fsm(
        yparam(200)
    )
    fsm.goto_next()

    fsm.If(c.valid)(
        count.inc(),
        Systask('display', "c=%d", c.data)
    )

    fsm.If(count == 4).goto_next()

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

    vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    simulation.setup_waveform(m, uut, m.get_vars(), dumpfile=vcd_name)
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
