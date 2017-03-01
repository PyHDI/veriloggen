from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.dataflow as dataflow

def mkMain():
    # input variiable
    x = dataflow.Variable('xdata', valid='xvalid', ready='xready')
    reset = dataflow.Variable('resetdata', valid='resetvalid', ready='resetready', width=1)
    enable = dataflow.Variable('enabledata', valid='enablevalid', ready='enableready', width=1)

    # dataflow definition
    z = dataflow.Iadd(x, initval=0, enable=enable, reset=reset)

    # set output attribute
    z.output('zdata', valid='zvalid', ready='zready')

    df = dataflow.Dataflow(z)
    m = df.to_module('main')
    #df.draw_graph()
    
    return m

def mkTest(numports=8):
    m = Module('test')

    # target instance
    main = mkMain()

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    xdata = ports['xdata']
    xvalid = ports['xvalid']
    xready = ports['xready']
    
    resetdata = ports['resetdata']
    resetvalid = ports['resetvalid']
    resetready = ports['resetready']
    
    enabledata = ports['enabledata']
    enablevalid = ports['enablevalid']
    enableready = ports['enableready']
    
    zdata = ports['zdata']
    zvalid = ports['zvalid']
    zready = ports['zready']
    
    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( xdata(0) )
    reset_stmt.append( xvalid(0) )
    reset_stmt.append( enabledata(0) )
    reset_stmt.append( enablevalid(0) )
    reset_stmt.append( resetdata(0) )
    reset_stmt.append( resetvalid(0) )
    reset_stmt.append( zready(0) )

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
 

    def send(name, data, valid, ready, step=1, waitnum=10, send_size=20):
        fsm = FSM(m, name + 'fsm', clk, rst)
        count = m.TmpReg(32, initval=0)
        
        fsm.add(valid(0))
        fsm.goto_next(cond=reset_done)
        for _ in range(waitnum):
            fsm.goto_next()
            
        fsm.add(valid(1))
        fsm.goto_next()
        
        fsm.add(data(data + step), cond=ready)
        fsm.add(count.inc(), cond=ready)
        fsm.add(valid(0), cond=AndList(count==5, ready))
        fsm.goto_next(cond=AndList(count==5, ready))
        
        for _ in range(waitnum):
            fsm.goto_next()
        fsm.add(valid(1))
        
        fsm.add(data(data + step), cond=ready)
        fsm.add(count.inc(), cond=ready)
        fsm.add(valid(0), cond=AndList(count==send_size, ready))
        fsm.goto_next(cond=AndList(count==send_size, ready))
        
        fsm.make_always()
    

    def receive(name, data, valid, ready, waitnum=10):
        fsm = FSM(m, name + 'fsm', clk, rst)
        
        fsm.add(ready(0))
        fsm.goto_next(cond=reset_done)
        fsm.goto_next()
        
        yinit = fsm.current
        fsm.add(ready(1), cond=valid)
        fsm.goto_next(cond=valid)
        for i in range(waitnum):
            fsm.add(ready(0))
            fsm.goto_next()
            
        fsm.goto(yinit)
        
        fsm.make_always()

        
    send('x', xdata, xvalid, xready, waitnum=10)
    receive('z', zdata, zvalid, zready, waitnum=5)

    
    # enable port
    enable_fsm = FSM(m, 'enable', clk, rst)
    enable_count = m.Reg('enable_count', 32, initval=0)

    enable_fsm.goto_next(cond=reset_done)
    
    enable_fsm_init = enable_fsm.current

    enable_fsm.add( enablevalid(1) ) # always High
    
    enable_fsm.add( enable_count.inc(), cond=AndList(enablevalid, enableready) )
    enable_fsm.add( enabledata(1), cond=AndList(enablevalid, enableready, enable_count==2) )
    enable_fsm.goto_next( cond=AndList(enablevalid, enableready, enable_count==2) )

    enable_fsm.add( enabledata(0), cond=AndList(enablevalid, enableready) )
    enable_fsm.add( enable_count(0) )
    enable_fsm.goto(enable_fsm_init, cond=AndList(enablevalid, enableready) )

    enable_fsm.make_always()

    
    # reset port
    reset_fsm = FSM(m, 'reset', clk, rst)
    reset_count = m.Reg('reset_count', 32, initval=0)

    reset_fsm.goto_next(cond=reset_done)
    
    reset_fsm_init = reset_fsm.current

    reset_fsm.add( resetvalid(1) ) # always High
    
    reset_fsm.add( reset_count.inc(), cond=AndList(resetvalid, resetready) )
    #reset_fsm.add( resetdata(1), cond=AndList(resetvalid, resetready, reset_count==2) )
    reset_fsm.add( resetdata(0), cond=AndList(resetvalid, resetready, reset_count==2) )
    reset_fsm.goto_next( cond=AndList(resetvalid, resetready, reset_count==2) )

    reset_fsm.add( resetdata(0), cond=AndList(resetvalid, resetready) )
    reset_fsm.add( reset_count(0) )
    reset_fsm.goto(reset_fsm_init, cond=AndList(resetvalid, resetready) )

    reset_fsm.make_always()

    
    m.Always(Posedge(clk))(
        If(reset_done)(
            If(AndList(xvalid, xready))(
                Systask('display', 'xdata=%d', xdata)
            ),
            If(AndList(zvalid, zready))(
                Systask('display', 'zdata=%d', zdata)
            )
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
