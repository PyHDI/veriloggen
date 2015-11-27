from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkLed():
    m = StubModule('blinkled')
    return m

def mkTop():
    m = Module('top')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)
    
    params = ( width, )
    ports = ( clk, rst, led )
    
    # StubModule is automatically created inside
    m.Instance('blinkled', 'inst_blinkled', params, ports)

    return m

if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog()
    print(verilog)
