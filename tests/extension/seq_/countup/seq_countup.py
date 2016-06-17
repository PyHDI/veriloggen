from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    interval = m.Parameter('INTERVAL', 16)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', 8, initval=0)
    count = m.Reg('count', 32, initval=0)
    
    seq = Seq(m, 'seq', clk, rst)
    
    seq(
        Systask('display', 'LED:%d count:%d', led, count)
    )

    seq.If(count<interval-1)(
        count(count + 1)
    )
    seq.If(count==interval-1)(
        count(0)
    ) 
    seq.If(count==interval-1)(
        led(led + 1)
    )

    seq.make_always()
    
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
    
    #simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000),
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog()
    print(verilog)
