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
    rx = m.Output('rx')
    
    y = m.Input('y', 32)
    vy = m.Input('vy')
    ry = m.Output('ry')

    z = m.Output('z', 32)
    vz = m.Output('vz')
    rz = m.Input('rz')
    
    df = lib.Dataflow(m, 'df', clk, rst)
    
    px = df.input(x, valid=vx, ready=rx)
    py = df.input(y, valid=vy, ready=ry)
    pz = df(Cond(px > py, px, py))
    pz.output(z, valid=vz, ready=rz)
    
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
    rx = ports['rx']
    y = ports['y']
    vy = ports['vy']
    ry = ports['ry']
    z = ports['z']
    vz = ports['vz']
    rz = ports['rz']
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_done = m.Reg('reset_done', initval=0)
    
    reset_stmt = []
    reset_stmt.append( reset_done(0) )
    reset_stmt.append( x(11) )
    reset_stmt.append( y(0) )
    reset_stmt.append( vx(0) )
    reset_stmt.append( vy(0) )
    reset_stmt.append( rz(0) )
    
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
    y_count = m.TmpReg(32, initval=0)
    z_count = m.TmpReg(32, initval=0)

    
    xfsm = lib.FSM(m, 'xfsm', clk, rst)
    xfsm.add(vx(0))
    xfsm.goto_next(cond=reset_done)
    xfsm.add(vx(1))
    xfsm.add(x.dec(), cond=rx)
    xfsm.add(x_count.inc(), cond=rx)
    xfsm.goto_next(cond=AndList(x_count==10, rx))
    xfsm.add(vx(0))
    xfsm.make_always()
    
    
    yfsm = lib.FSM(m, 'yfsm', clk, rst)
    yfsm.add(vy(0))
    yfsm.goto_next(cond=reset_done)
    yfsm.add(vy(1))
    yfsm.add(y.inc(), cond=ry)
    yfsm.add(y_count.inc(), cond=ry)
    yfsm.goto_next(cond=AndList(y_count==10, ry))
    yfsm.add(vy(0))
    yfsm.make_always()

    
    zfsm = lib.FSM(m, 'zfsm', clk, rst)
    zfsm.add(rz(0))
    zfsm.goto_next(cond=reset_done)
    zfsm.goto_next()
    zinit= zfsm.current()
    zfsm.add(rz(1), cond=vz)
    zfsm.goto_next(cond=vz)
    for i in range(10):
        zfsm.add(rz(0))
        zfsm.goto_next()
    zfsm.goto(zinit)
    zfsm.make_always()

    
    m.Always(Posedge(clk))(
        If(reset_done)(
            If(AndList(vx, rx))(
                Systask('display', 'x=%d', x)
            ),
            If(AndList(vy, ry))(
                Systask('display', 'y=%d', y)
            ),
            If(AndList(vz, rz))(
                Systask('display', 'z=%d', z)
            )
        )
    )
    
    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
