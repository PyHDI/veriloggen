from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkLedTest():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/led.v'
    modules = from_verilog.read_verilog_module(filename)
    test = modules['test']
    return test

if __name__ == '__main__':
    test = mkLedTest()
    verilog = test.to_verilog()
    print(verilog)
