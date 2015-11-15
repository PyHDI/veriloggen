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
    vx = m.Input('vx')
    y = m.Output('y', 32)
    vy = m.Output('vy')
    
    df = lib.Dataflow(m, 'df', clk, rst)
    
    px = df.input(x, valid=vx)
    t0 = df(px.prev(2) + px.prev(3))
    py = df(t0 + px.prev(1))
    py.output(y, valid=vy)
    
    df.make_always()

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
    vx = ports['vx']
    y = ports['y']
    vy = ports['vy']
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_done = m.Reg('reset_done', initval=0)
    
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( x(0) )
    reset_stmt.append( vx(0) )
    
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
    
    xfsm = lib.FSM(m, 'xfsm', clk, rst)
    xfsm.add(vx(0))
    xfsm.goto_next(cond=reset_done)
    xfsm.add(vx(1))
    xfsm.add(x.inc())
    xfsm.add(x_count.inc())
    xfsm.goto_next(cond=x_count==10)
    xfsm.add(vx(0))
    xfsm.make_always()

    
    m.Always(Posedge(clk))(
        If(reset_done)(
            If(vx)(
                Systask('display', 'x=%d', x)
            ),
            If(vy)(
                Systask('display', 'y=%d', y)
            )
        )
    )
    
    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
