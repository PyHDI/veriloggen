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
    # df.enable_draw_graph()

    # input with register
    xdata = m.Reg('xdata', 32, initval=0)
    xvalid = m.Reg('xvalid', initval=0)
    xready = m.Wire('xready')
    x = df.Variable(xdata, xvalid, xready, signed=False)

    # input with name
    y = df.Variable('ydata', 'yvalid', 'yready', signed=False)

    # output
    a = x + y + 1
    b = a + x + y

    a.output('adata', 'avalid', 'aready')
    b.output('bdata', 'bvalid', 'bready')

    # write
    xfsm = FSM(m, 'xfsm', clk, rst)
    xcount = m.TmpReg(32, initval=0)

    xack = x.write(xcount, cond=xfsm)
    xfsm.If(xack)(
        xcount.inc()
    )
    xfsm.Then().If(xcount == 15).goto_next()

    # write
    yfsm = FSM(m, 'yfsm', clk, rst)
    ycount = m.TmpReg(32, initval=0)

    yack = y.write(ycount, cond=yfsm)
    yfsm.If(yack)(
        ycount(ycount + 1)
    )
    yfsm.Then().If(ycount == 15).goto_next()

    # read
    aseq = Seq(m, 'aseq', clk, rst)

    adata, avalid = a.read(cond=aseq)
    aseq.If(avalid)(
        Systask('display', "adata=%d", adata)
    )

    # read
    bseq = Seq(m, 'bseq', clk, rst)

    bdata, bvalid = b.read(cond=bseq)
    bseq.If(bvalid)(
        Systask('display', "bdata=%d", bdata)
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
