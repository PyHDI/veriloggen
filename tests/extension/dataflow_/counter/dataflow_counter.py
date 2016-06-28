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

    # counters
    a = dataflow.Counter(maxval=8, width=8)
    b = dataflow.Counter(step=2, maxval=16, width=8)
    
    c = a + b
    c.output('cdata', valid='cvalid')

    # synthesize dataflow
    df = dataflow.Dataflow(c)
    df.implement(m, clk, rst)
    df.draw_graph()
    
    fsm = FSM(m, 'fsm', clk, rst)
    count = m.TmpReg(32, initval=0)

    fsm.If(c.valid)(
        count.inc(),
        Systask('display', "c=%d", c.data)
    )

    fsm.If(count == 32).goto_next()
    
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

    #sim.view_waveform()
