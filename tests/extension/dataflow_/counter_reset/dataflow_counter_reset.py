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

    df = dataflow.DataflowManager(m, clk, rst)

    a = df.Constant(2)
    b = df.Counter(1, initval=0, maxval=8)
    b = b.prev(1)
    c = df.Iadd(a, reset=(b == 0))

    b.output('bdata', 'bvalid', 'bready')
    c.output('cdata', 'cvalid', 'cready')

    ready = 1
    bdata, bvalid = b.read(ready)
    cdata, cvalid = c.read(ready)

    seq = Seq(m, 'seq', clk, rst)
    seq.If(bvalid)(
        Systask('display', 'b=%d', bdata)
    )
    seq.If(cvalid)(
        Systask('display', 'c=%d', cdata)
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
