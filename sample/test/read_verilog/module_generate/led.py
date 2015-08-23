import sys
import os
import collections

from veriloggen import *

def mkLed():
    modules = read_verilog_module('led.v')
    m = modules['blinkled']
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
