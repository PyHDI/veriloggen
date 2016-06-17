from __future__ import absolute_import
from __future__ import print_function
import os
import sys

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

def mkChatterClear(length=1024):
    m = Module("chatter_clear")

    length = m.Parameter('length', length)
    
    clk = m.Input('CLK')
    rst = m.Input('RST')

    din = m.Input('din')
    dout = m.OutputReg('dout', initval=0)

    seq = Seq(m, 'seq', clk, rst)

    count = m.TmpReg(32)
    
    seq.If(din==dout)(
        count(0)
    )
    seq.If(din!=dout)(
        count.inc()
    )
    
    seq.If(count==length)(
        count(0)
    )
    seq.If(count==length)(
        dout(din)
    )

    seq.make_always()

    return m

def mkTest(length=1024):
    m = Module('test')
    
    main = mkChatterClear(length)
    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']
    din = ports['din']
    dout = ports['dout']

    fsm = FSM(m, 'fsm', clk, rst)
    count = m.TmpReg(32, initval=0)

    fsm( din(0) )
    fsm( count.inc() )
    fsm.If(count==2000)( count(0) )
    fsm.goto_next(count==2000)

    fsm( din(1) )
    fsm( count.inc() )
    fsm.If(count==10)( count(0) )
    fsm.goto_next(count==10)

    fsm( din(0) )
    fsm( count.inc() )
    fsm.If(count==10)( count(0) )
    fsm.goto_next(count==10)

    fsm( din(1) )
    fsm( count.inc() )
    fsm.If(count==2000)( count(0) )
    fsm.goto_next(count==2000)

    fsm( din(0) )
    fsm( count.inc() )
    fsm.If(count==10)( count(0) )
    fsm.goto_next(count==10)

    fsm( din(1) )
    fsm( count.inc() )
    fsm.If(count==10)( count(0) )
    fsm.goto_next(count==10)

    fsm( din(0) )
    fsm( count.inc() )
    fsm.If(count==2000)( count(0) )
    fsm.goto_next(count==2000)

    fsm.make_always()
    
    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    nclk = simulation.next_clock
    
    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    #main = mkChatterClear()
    #verilog = main.to_verilog('tmp.v')
    #print(verilog)
    #exit()
    
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run() # display=False
    #rslt = sim.run(display=True)
    print(rslt)

    # launch waveform viewer (GTKwave)
    #sim.view_waveform() # background=False
    #sim.view_waveform(background=True)
