from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.dataflow as dataflow

def mux(cond, x, y):
    if dataflow.is_dataflow_object(cond, x, y):
        return dataflow.Mux(cond, x, y)
    return x if cond else y

def compare(x, y):
    cond = x < y
    small = mux(cond, x, y)
    large = mux(cond, y, x)
    return small, large

def network(values, num):
    ret = []
    x = values[0]
    
    for i in range(num):
        small, large = compare(x, values[i+1])
        ret.append(small)
        x = large
        
    ret.append(x)
    
    for i in range(num+1, len(values)): 
        ret.append( values[i] )
        
    return ret

def sort(values):
    num = len(values)
    for i in range(num):
        values = network(values, num-i-1)
    return values

def mkSort(numports=4):
    values = [ dataflow.Variable('din%d' % i) for i in range(numports) ]
    rslt = sort(values)

    for i, r in enumerate(rslt):
        r.output('dout%d' % i)

    df = dataflow.Dataflow(*rslt)
    m = df.to_module('sort')

    return m

def mkTest(numports=4):

    m = Module('test')
    
    # target instance
    main = mkSort(numports)

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    din = [ ports['din%d' % i] for i in range(numports) ]
    dout = [ ports['dout%d' % i] for i in range(numports) ]

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    for i, d in enumerate(din):
        reset_stmt.append( d(0) )
        
    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(100000),
        Systask('finish'),
    )

    fsm = FSM(m, 'fsm', clk, rst)
    
    fsm.goto_next(cond=reset_done)

    for i, d in enumerate(din):
        fsm.add( d(100 - i) )
        
    fsm.goto_next()
    
    for i in range(numports ** 2):
        for d in dout:
            fsm.add( Systask('display', '%s = %d', d.name, d))
        fsm.add( Systask('display', '----') )
        fsm.goto_next()

    fsm.add( Systask('finish') )
    fsm.make_always()

    return m
    
if __name__ == '__main__':
    n = 4
    test = mkTest(n)
    verilog = test.to_verilog('tmp.v')
    #print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    ## only target RTL
    #main = mkSort(n)
    #verilog = main.to_verilog('tmp.v')
    #print(verilog)

    values = [ 100 - i for i in range(n) ]
    rslt = sort(values)
    print(rslt)
