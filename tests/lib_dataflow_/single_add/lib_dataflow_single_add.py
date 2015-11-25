from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    x = m.Input('x', 32)
    y = m.Output('y', 32)
    
    df = lib.Dataflow(m, 'df', clk, rst)
    
    px = df.input(x)
    t0 = df(px.prev(1) + px.prev(2))
    py = df(t0 + px)
    py.output(y)
    
    df.make_always()

    try:
        df.draw_graph()
    except:
        print('Dataflow graph could not be generated.', file=sys.stderr)

    return m

def mkTest(numports=8):
    m = Module('test')

    # target instance
    led = mkLed()
    
    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']
    x = ports['x']
    y = ports['y']
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_done = m.Reg('reset_done', initval=0)
    
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( x(0) )
    
    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock
    
    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(10000),
        Systask('finish'),
    )

    x_count = m.TmpReg(32, initval=0)

    xfsm = lib.FSM(m, 'xfsm', clk, rst)
    xfsm.goto_next(cond=reset_done)
    xfsm.add(x.inc())
    xfsm.add(x_count.inc())
    xfsm.goto_next(cond=x_count==10)
    xfsm.add(x(0))
    for i in range(5):
        xfsm.goto_next()
    xfsm.add( Systask('finish') )
    
    xfsm.make_always()
    
    
    m.Always(Posedge(clk))(
        If(reset_done)(
            Systask('display', 'x=%d', x),
            Systask('display', 'y=%d', y)
        )
    )
    
    return m
    
if __name__ == '__main__':
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
