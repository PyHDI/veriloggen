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

    tmp = m.TmpReg(initval=0)

    fsm = FSM(m, 'fsm', clk, rst)

    fsm(
        Systask('display', 'LED:%d count:%d', led, count)
    )
    
    fsm.If(count<interval-1)(
        count(count + 1)
    ).Elif(count==100)(
        count(101),
        tmp.inc()
    ).Else(
        count(0)
    )

    # recall the last condition by 'Then()' 
    fsm.Then().goto_next()

    fsm(
        led(led + 1)
    )

    fsm.Then().goto_init()
    
    fsm.make_always()
    
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
    
    # vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    # simulation.setup_waveform(m, uut, dumpfile=vcd_name)
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
