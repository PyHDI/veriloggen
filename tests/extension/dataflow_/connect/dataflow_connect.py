from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.dataflow as dataflow

def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    x = dataflow.Variable()
    y = x + 1
    z = y + 1

    y.output('ydata', 'yvalid', 'yready')
    z.output('zdata', 'zvalid', 'zready')

    # source variable
    xsrc = dataflow.Variable('xdata', 'xvalid', 'xready')
    # connect a variable to the variable that has no input_data
    x.connect(xsrc)

    # synthesize dataflow
    df = dataflow.Dataflow(z)
    df.implement(m, clk, rst, aswire=True)
    #df.draw_graph()

    
    # write
    xfsm = FSM(m, 'xfsm', clk, rst)
    xcount = m.TmpReg(32, initval=0)
    
    xack = x.write(xcount, cond=xfsm)
    xfsm.If(xack)(
        xcount.inc()
    )
    xfsm.Then().If(xcount == 15).goto_next()

    xfsm.make_always()

    
    # read
    yseq = Seq(m, 'yseq', clk, rst)
    
    ydata, yvalid = y.read(cond=yseq)
    yseq.If(yvalid)(
        Systask('display', "ydata=%d", ydata)
    )

    yseq.make_always()


    zseq = Seq(m, 'zseq', clk, rst)
    
    zdata, zvalid = z.read(cond=zseq)
    zseq.If(zvalid)(
        Systask('display', "zdata=%d", zdata)
    )

    zseq.make_always()

    
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

    #sim.view_waveform()
