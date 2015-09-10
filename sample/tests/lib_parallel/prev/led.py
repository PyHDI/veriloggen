import sys
import os
import math

from veriloggen import *

def mkLed(window_size=8):
    if window_size < 0:
        raise ValueError('window_size must be larger than 0')
    if math.log(window_size, 2) % 1.0 != 0.0:
        raise ValueError('window_size must be power of 2')
        
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    x = m.Input('x', 32)
    y = m.OutputReg('y', 32, initval=0)
    
    par = lib.Parallel(m, 'par')
    v = x
    for w in range(window_size-1):
        v = v + par.prev(x, w + 1)
        
    t = m.TmpReg(32)
    par.add( t(v) )
    par.add( y(t >> int(math.log(window_size, 2))) )
    
    par.make_always(clk, rst)

    return m

def mkTest():
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

    reset_stmt = []
    reset_stmt.append( x(0) )
    
    lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = lib.simulation.next_clock
    
    init.add(
        Delay(1000),
        
        [ (nclk(clk), x(i+10)) for i in range(10) ],
        nclk(clk), x(0),
        
        Delay(1000),
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
