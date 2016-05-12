from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkLed():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/led.v'
    modules = from_verilog.read_verilog_module(filename)
    m = modules['blinkled']
    return m

def mkTop():
    m = Module('top')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', 8)
    
    params = ( )
    ports = ( clk, rst, led )

    led = mkLed()
    m.Instance(led, 'inst_blinkled', params, ports)

    return m

if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog()
    print(verilog)
