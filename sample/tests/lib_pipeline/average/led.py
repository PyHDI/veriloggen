import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    x = m.Input('x', 32)
    y = m.OutputReg('y', 32, initval=0)
    
    pipe = lib.Pipeline(m, 'pipe')
    
    px = pipe.input(x)
    t0 = pipe(px.prev(1) + px.prev(2))
    py = pipe(t0 + px)
    py.output(y)
    
    pipe.make_always(clk, rst)

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
    
    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = lib.simulation.next_clock
    
    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(10000),
        Systask('finish'),
    )

    x_count = m.TmpReg(32, initval=0)

    xfsm = lib.FSM(m, 'xfsm')
    xfsm.goto_next(cond=reset_done)
    xfsm.add(x.inc())
    xfsm.add(x_count.inc())
    xfsm.goto_next(cond=x_count==10)
    xfsm.add( Systask('finish') )
    
    xfsm.make_always(clk, rst)
    
    
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
