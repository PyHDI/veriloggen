import sys
import os

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
    
    a = m.Output('a', 32)
    va = m.Output('va')
    ra = m.Input('ra')
    
    pipe = lib.Pipeline(m, 'pipe')
    
    px = pipe.input(x, valid=vx, ready=rx)
    py = pipe.input(y, valid=vy, ready=ry)
    pz = pipe(px + py)
    pa = pipe(py - px)
    pz.output(z, valid=vz, ready=rz)
    pa.output(a, valid=va, ready=ra)
    
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
    vx = ports['vx']
    rx = ports['rx']
    
    y = ports['y']
    vy = ports['vy']
    ry = ports['ry']
    
    z = ports['z']
    vz = ports['vz']
    rz = ports['rz']
    
    a = ports['a']
    va = ports['va']
    ra = ports['ra']
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_stmt = []
    reset_stmt.append( x(0) )
    reset_stmt.append( y(0) )
    reset_stmt.append( vx(0) )
    reset_stmt.append( vy(0) )
    reset_stmt.append( rz(0) )
    reset_stmt.append( ra(0) )
    
    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = lib.simulation.next_clock
    
    init.add(
        Delay(1000),
        nclk(clk),
        Delay(10000),
        Systask('finish'),
    )
    
    m.Initial(
        Delay(2000),
        nclk(clk),
        [( nclk(clk), Delay(3), rz(vx),
            nclk(clk), nclk(clk),
            nclk(clk), Delay(3), rz(0),
            nclk(clk), nclk(clk))
         for _ in range(20) ],
        rz(1),
    )
        
    m.Initial(
        Delay(2000),
        nclk(clk),
        [( nclk(clk), Delay(3), ra(vx),
            nclk(clk), nclk(clk), nclk(clk), nclk(clk),
            nclk(clk), Delay(3), ra(0),
            nclk(clk), nclk(clk), nclk(clk), nclk(clk))
         for _ in range(20) ],
        ra(1),
    )
    
    m.Initial(
        Delay(1000),
        nclk(clk),
        vx(1),
        [ (While(Not(rx))(nclk(clk)), x(x + 1), nclk(clk)) for _ in range(10) ],
        nclk(clk),
        vx(0),
    )
    
    m.Initial(
        Delay(1000),
        nclk(clk),
        vy(1),
        [ (While(Not(ry))(nclk(clk)), y(y + 2), nclk(clk)) for _ in range(10) ],
        nclk(clk),
        vy(0),
    )
    
    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
