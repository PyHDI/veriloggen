import sys
import os
import collections

from veriloggen import *

def mkLedTest():
    modules = read_verilog_module('led.v')
    led = modules['blinkled']
    test = modules['test']
    return led, test

if __name__ == '__main__':
    led, test = mkLedTest()
    verilog = ''.join([ test.to_verilog(), led.to_verilog() ])
    print(verilog)
