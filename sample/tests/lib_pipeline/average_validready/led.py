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
    y = m.OutputReg('y', 32, initval=0)
    vy = m.OutputReg('vy', initval=0)
    ry = m.Input('ry')
    
    pipe = lib.Pipeline(m, 'pipe')
    
    px = pipe.input(x, valid=vx, ready=rx)
    t0 = pipe(px.prev(1) + px.prev(2))
    py = pipe(t0 + px)
    py.output(y, valid=vy, ready=ry)
    
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
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_stmt = []
    reset_stmt.append( x(0) )
    reset_stmt.append( vx(0) )
    reset_stmt.append( ry(0) )
    
    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = lib.simulation.next_clock
    
    init.add(
        Delay(1000),
        nclk(clk),

        # Emulating wire signal
        [ (nclk(clk), Delay(3), ry(vx), nclk(clk), Delay(3), ry(0)) for _ in range(10) ],
        
        Systask('finish'),
    )

    m.Initial(
        Delay(1000),
        nclk(clk),

        While(1)(
            vx(1),
            If(rx)(
                x(x + 1)
            ),
            nclk(clk)
        )
    )
    
    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
