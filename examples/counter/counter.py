from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

def counter(m, clk, rst, width=None, maxval=None, cond=None, initval=0):
    if maxval is None and width is not None:
        maxval = Int(2) ** width
    if width is None and maxval is not None:
        width = int(math.log(maxval, 2)) + 1
    if maxval is None and width is None:
        width = 10
        maxval = 1024
        
    c = m.TmpReg(width, initval=initval)
    seq = TmpSeq(m, clk, rst)
    
    if cond is not None:
        # setting the following condition
        seq.If(cond)
        
    seq(
        If(c == maxval-1)(
            c(0)
        ).Else(
            c.inc()
        )
    )
    
    seq.make_always()
    
    return c

def mkLed(width=8):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)
    
    step = 1024
    count = counter(m, clk, rst, maxval=step)
    led_count = counter(m, clk, rst, width=width, cond=(count==step-1))
    led.assign(led_count)
    
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
    
    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))
    
    simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)
    
    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog(filename='tmp.v')
    #verilog = test.to_verilog()
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    #sim.view_waveform()
