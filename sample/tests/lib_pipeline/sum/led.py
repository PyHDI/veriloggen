import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    x = m.Input('x', 32)
    y = m.Output('y', 32)
    prst = m.Input('prst')
    
    pipe = lib.Pipeline(m, 'pipe')
    
    sum = m.Wire('sum', 32)

    count = m.Reg('count', 32, initval=0)
    
    px = pipe.input(x)
    psum = pipe.input(sum)
    psumout = pipe(px + psum)
    
    psumout.output(sum)
    psumout.reset(prst)
    
    m.Assign( y(sum) )
    
    pipe.make_always(clk, rst, reset=[count.reset()], body=[count(count + 1)])

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
    prst = ports['prst']
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    reset_stmt = []
    reset_stmt.append( prst(0) )
    reset_stmt.append( x(0) )
    
    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = lib.simulation.next_clock
    
    init.add(
        Delay(1000),
        nclk(clk),
        
        [ ( x(i), nclk(clk) ) for i in range(10) ],
        [ nclk(clk) for _ in range(10) ],
        
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
