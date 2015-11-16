from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkLed():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/led.v'
    modules = read_verilog_module(filename)
    m = modules['blinkled']
    
    # change the module name
    m.name = 'modified_led'
    
    # add new statements
    enable = m.Input('enable')
    busy = m.Output('busy')

    old_statement = m.always[0].statement[0].false_statement
    m.always[0].statement[0].false_statement = If(enable)(*old_statement)
    m.Assign( busy(m.variable['count'] < 1023) )
    
    return m

def mkTop():
    m = Module('top')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)
    
    params = ( width, )
    ports = ( clk, rst, led )

    led = mkLed()
    m.Instance(led, 'inst_blinkled', params, ports)

    return m

if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog()
    print(verilog)
