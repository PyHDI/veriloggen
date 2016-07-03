from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.dataflow as dataflow

def mkMadd():
    x = dataflow.Variable('xd', valid='xv', signed=True)
    y = dataflow.Variable('yd', valid='yv', signed=True)
    vreset = dataflow.Variable('vreset_data', valid='vreset', width=1)
    
    xy = x * y
    
    z = dataflow.Iadd(xy, signed=True, initval=0, reset=vreset)

    z.output('zd', valid='zv')
    df = dataflow.Dataflow(z)
    m = df.to_module('madd')

    return m

def mkMatmul(n=16, datawidth=32):
    m = Module('Matmul')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    # BRAM I/F
    addrwidth = int(math.log(n, 2)) * 2
    
    xaddr = m.OutputReg('xaddr', addrwidth, initval=0)
    xdin = m.Input('xdin', datawidth)
    
    yaddr = m.OutputReg('yaddr', addrwidth, initval=0)
    ydin = m.Input('ydin', datawidth)
    
    zaddr = m.OutputReg('zaddr', addrwidth, initval=0)
    zdout = m.OutputReg('zdout', datawidth, initval=0)
    zwe = m.OutputReg('zwe')

    # External Control
    start = m.Input('start')
    busy = m.OutputReg('busy', initval=0)

    # MADD Instance
    madd = mkMadd()

    ivalid = m.Reg('ivalid', initval=0)
    odata = m.Wire('odata', datawidth)
    ovalid = m.Wire('ovalid')
    vreset = m.Reg('vreset', initval=0)

    m.Instance(madd, 'madd',
               ports=[ ('CLK', clk), ('RST', rst),
                       ('xd', xdin), ('xv', ivalid), ('yd', ydin), ('yv', ivalid),
                       ('zd', odata), ('zv', ovalid),
                       ('vreset_data', vreset), ('vreset', ivalid) ])

    read_count = m.TmpReg(int(addrwidth/2)+1, initval=0)
    sum_value = m.TmpReg(datawidth, initval=0)
    sum_count = m.TmpReg(int(addrwidth/2)+1, initval=0)
    
    # main FSM
    fsm = FSM(m, 'fsm', clk, rst)

    init = fsm.current

    # initial values
    fsm.add( xaddr(0-1), yaddr(0-1), zaddr(0-1), zwe(0),
             busy(0), vreset(0), ivalid(0), 
             read_count(0), sum_value(0), sum_count(0) )

    # start
    fsm.add( busy(1), cond=start )
    fsm.goto_next(cond=start)

    comp = fsm.current

    # reset pipeline for each 1st data
    fsm.add( vreset(0), delay=1 )
    fsm.add( vreset(1), delay=1, cond=read_count==0 )
    
    # read data
    fsm.add( xaddr.inc(), yaddr.inc(), cond=read_count<n )
    fsm.add( ivalid(0), delay=1 )
    fsm.add( ivalid(1), delay=1, cond=read_count<n )
    fsm.add( read_count.inc(), cond=read_count<n )

    # comp data
    fsm.add( sum_count.inc(), cond=ovalid )
    fsm.add( sum_value(odata), cond=ovalid )
    
    # dump
    #fsm.add( Systask('display', 'xaddr=%10d yaddr=%10d', xaddr, yaddr) )
    #fsm.add( Systask('display', 'xdin =%10d ydin =%10d', xdin, ydin), delay=1 )
    #fsm.add( Systask('display', 'count=%10d odata=%10d', sum_count, odata), cond=ovalid ) 
    
    fsm.goto_next(cond=sum_count==n)

    # write data
    fsm.add( zaddr.inc() )
    fsm.add( zdout(sum_value), zwe(1) )
    fsm.add( zwe(0), delay=1 )

    # set up for next
    fsm.add( yaddr(0-1), cond=yaddr==n*n-1 )
    fsm.add( xaddr(xaddr-n), cond=yaddr<n*n-1)
    fsm.add( read_count(0), sum_count(0) )

    done = (zaddr == n * n - 2)
    fsm.goto(comp, cond=Not(done))
    fsm.goto(init, cond=done)

    fsm.make_always()

    return m

def mkTest(n=16, datawidth=32):

    m = Module('test')

    # target instance
    main = mkMatmul(n, datawidth)

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    xaddr = ports['xaddr']
    xdin = ports['xdin']

    yaddr = ports['yaddr']
    ydin = ports['ydin']
    
    zaddr = ports['zaddr']
    zdout = ports['zdout']
    zwe = ports['zwe']

    start = ports['start']
    busy = ports['busy']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( start(0) )
    reset_stmt.append( xdin(0) )
    reset_stmt.append( ydin(0) )

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

    mag = 2

    fsm = FSM(m, 'fsm', clk, rst)
    
    fsm.goto_next(cond=reset_done)
    
    fsm.goto_next(cond=Not(busy))
    
    fsm.add( start(1) )
    fsm.add( start(0), delay=1 )
    #fsm.add( xdin(Mux(xaddr % n == xaddr / n, 1, 0)) )
    fsm.add( xdin(xaddr) )
    fsm.add( ydin(Mux(yaddr % n == yaddr / n, mag, 0)) )
    fsm.goto_next()
    
    #fsm.add( xdin(Mux(xaddr % n == xaddr / n, 1, 0)) )
    fsm.add( xdin(xaddr) )
    fsm.add( ydin(Mux(yaddr % n == yaddr / n, mag, 0)) )
    fsm.goto_next(cond=busy)

    #fsm.add( xdin(Mux(xaddr % n == xaddr / n, 1, 0)) )
    fsm.add( xdin(xaddr) )
    fsm.add( ydin(Mux(yaddr % n == yaddr / n, mag, 0)) )
    fsm.goto_next(cond=Not(busy))

    fsm.add( Systask('finish') )

    fsm.make_always()

    m.Always(Posedge(clk))(
        If(zwe)(
            Systask('display', 'zaddr=%10d zdout=%10d', zaddr, zdout),
            #If(AndList(zaddr % n == zaddr / n, zdout != 1))(
            #    Systask('display', '## wrong')
            #),
            #If(AndList(zaddr % n != zaddr / n, zdout != 0))(
            #    Systask('display', '## wrong')
            #)
            If(zaddr * mag != zdout)(
                Systask('display', '## wrong result')
            ),
        )
    )
    
    return m

if __name__ == '__main__':
    n = 16
    test = mkTest(n)
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
