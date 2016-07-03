from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

def mkAdd(numports=8, mode=1):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    
    inputs = [ (m.Input('d'+str(i), 32), m.Input('v'+str(i)), m.Output('r'+str(i)))
               for i in range(numports) ]
    
    dz = m.Output('dz', 32)
    vz = m.Output('vz')
    rz = m.Input('rz')
    
    df = Pipeline(m, 'df', clk, rst)

    dfvars = [ df.input(*p) for p in inputs ]

    if mode == 0:
        vars = dfvars
        for depth in range(int(math.log(numports,2))):
            tmp_vars = []
            for i in range(numports>>depth+1):
                tmp_vars.append( df(vars[i*2] + vars[i*2+1]) )
            vars = tmp_vars
        vars[0].output(dz, valid=vz, ready=rz)

    else:
        ret = None
        for v in dfvars:
            if ret is None:
                ret = v
                continue
            ret = df(ret + v)
        ret.output(dz, valid=vz, ready=rz)
    
    df.make_always()
    
    try:
        df.draw_graph()
    except:
        print('Dataflow graph could not be generated.', file=sys.stderr)

    return m

def mkTest(numports=8):
    m = Module('test')
    
    # target instance
    madd = mkAdd(numports)
    
    # copy paras and ports
    params = m.copy_params(madd)
    ports = m.copy_sim_ports(madd)

    clk = ports['CLK']
    rst = ports['RST']

    inputs = [ (ports['d'+str(i)], ports['v'+str(i)], ports['r'+str(i)])
               for i in range(numports) ]

    dz = ports['dz']
    vz = ports['vz']
    rz = ports['rz']
    
    uut = m.Instance(madd, 'uut',
                     params=m.connect_params(madd),
                     ports=m.connect_ports(madd))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append( reset_done(0) )

    for p in inputs:
        reset_stmt.extend( [ p[0](0), p[1](0) ] )

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

    for i,p in enumerate(inputs):
        count = m.TmpReg(32, initval=0)
        d = p[0]
        v = p[1]
        r = p[2]
        fsm = FSM(m, 'fsm'+str(i), clk, rst)
        fsm.add(v(0))
        fsm.goto_next(cond=reset_done)
        fsm.add(v(1))
        fsm.goto_next()
        fsm.add(d(d + i + 1), cond=r)
        fsm.add(count.inc(), cond=r)
        fsm.goto_next(cond=AndList(count==10, r))
        fsm.add(v(0))
        fsm.make_always()

    zfsm = FSM(m, 'zfsm', clk, rst)
    zfsm.add(rz(0))
    zfsm.goto_next(cond=reset_done)
    zfsm.goto_next()
    zinit= zfsm.current
    zfsm.add(rz(1), cond=vz)
    zfsm.goto_next(cond=vz)
    for i in range(10):
        zfsm.add(rz(0))
        zfsm.goto_next()
    zfsm.goto(zinit)
    zfsm.make_always()

    disp = []
    for p in inputs:
        d = p[0]
        v = p[1]
        r = p[2]

        disp.append( If(AndList(v, r))( Systask('display', d.name + '=%d', d) ) )

    m.Always(Posedge(clk))(
        If(reset_done)(
            disp,
            If(AndList(vz, rz))(
                Systask('display', dz.name + '=%d', dz)
            )))
    
    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    #sim.view_waveform()
