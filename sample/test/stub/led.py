import sys
import os
import collections

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
    
    m.Instance(mkLed(), 'inst_blinkled', params, ports)

    return m

if __name__ == '__main__':
    top_module = mkTop()
    top_code = top_module.to_verilog()
    print(top_code)
