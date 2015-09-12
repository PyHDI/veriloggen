import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    x = m.Input('x', 32)
    vx = m.Input('vx')
    y = m.OutputReg('y', 32, initval=0)
    vy = m.OutputReg('vy', initval=0)
    
    pipe = lib.Pipeline(m, 'pipe')
    
    px = pipe.input(x, valid=vx)
    t0 = pipe(px.prev(2) + px.prev(3))
    py = pipe(t0 + px.prev(1))
    py.output(y, valid=vy)
    
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
    y = ports['y']
    vy = ports['vy']
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_stmt = []
    reset_stmt.append( x(0) )
    reset_stmt.append( vx(0) )
    
    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = lib.simulation.next_clock
    
    init.add(
        Delay(1000),
        nclk(clk),
        
        [ ( x(i), vx(1), nclk(clk), [ (vx(0), nclk(clk)) for _ in range(3)] ) for i in range(10) ],
        vx(0),
        [ nclk(clk) for _ in range(10) ],
        
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
