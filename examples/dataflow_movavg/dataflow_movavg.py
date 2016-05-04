from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.dataflow as dataflow

def add_serial(v, length):
    ret = v
    for i in range(1, length):
        ret += v.prev(i)
    return ret

def add_parallel(v, length):
    srcs = [ v.prev(i) for i in range(length) ]
    
    while len(srcs) > 1:
        next_srcs = []
        while srcs:
            a = srcs.pop(0)
            b = srcs.pop(0) if srcs else None
            if b is None:
                next_srcs.append( a )
            else:
                next_srcs.append( a + b )
        srcs = next_srcs

    return srcs[0]

def mkMovAvg(length=8, datawidth=32):
    x = dataflow.Variable('xdata', valid='xvalid', ready='xready', signed=True, width=datawidth)
    
    #y = add_serial(x, length)
    y = add_parallel(x, length)

    if math.log(length, 2) % 1.0 == 0.0:
        y = y >> int(math.log(length, 2))
    else:
        y = y / length
    
    y.output('ydata', valid='yvalid', ready='yready')
    df = dataflow.Dataflow(y)
    m = df.to_module('movavg')

    df.draw_graph()

    return m

def mkTest():
    m = Module('test')

    # target instance
    main = mkMovAvg()

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    xdata = ports['xdata']
    xvalid = ports['xvalid']
    xready = ports['xready']
    
    ydata = ports['ydata']
    yvalid = ports['yvalid']
    yready = ports['yready']
    
    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( xdata(0) )
    reset_stmt.append( xvalid(0) )
    reset_stmt.append( yready(0) )

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

    def send(name, data, valid, ready, step=1, waitnum=10):
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
        fsm.goto_next(cond=AndList(count==15, ready))
        
        fsm.add(valid(0))
        for _ in range(waitnum):
            fsm.goto_next()
        fsm.add(valid(1))
        
        fsm.add(data(data + step), cond=ready)
        fsm.add(count.inc(), cond=ready)
        fsm.goto_next(cond=AndList(count==30, ready))
        
        fsm.add(valid(0))
        
        fsm.make_always()
    

    def receive(name, data, valid, ready, waitnum=10):
        fsm = FSM(m, name + 'fsm', clk, rst)
        
        fsm.add(ready(0))
        fsm.goto_next(cond=reset_done)
        fsm.goto_next()
        
        yinit= fsm.current()
        fsm.add(ready(1), cond=valid)
        fsm.goto_next(cond=valid)
        for i in range(waitnum):
            fsm.add(ready(0))
            fsm.goto_next()
            
        fsm.goto(yinit)
        
        fsm.make_always()

        
    send('x', xdata, xvalid, xready, step=1, waitnum=10)
    receive('y', ydata, yvalid, yready, waitnum=5)
    
    
    m.Always(Posedge(clk))(
        If(reset_done)(
            If(AndList(xvalid, xready))(
                Systask('display', 'xdata=%d', xdata)
            ),
            If(AndList(yvalid, yready))(
                Systask('display', 'ydata=%d', ydata)
            )
        )
    )
    
    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    #print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # only target RTL
    #main = mkMatmul(n)
    #verilog = main.to_verilog('tmp.v')
    #print(verilog)
