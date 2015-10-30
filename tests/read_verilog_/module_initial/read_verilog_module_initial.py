import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkLedTest():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/led.v'
    modules = read_verilog_module(filename)
    led = modules['blinkled']
    test = modules['test']
    return led, test

if __name__ == '__main__':
    led, test = mkLedTest()
    verilog = ''.join([ test.to_verilog(), led.to_verilog() ])
    print(verilog)
