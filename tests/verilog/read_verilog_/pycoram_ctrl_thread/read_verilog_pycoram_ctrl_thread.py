from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkThread():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/ctrl_thread.v'
    modules = from_verilog.read_verilog_module(filename)
    return modules

if __name__ == '__main__':
    modules = mkThread()
    verilog = ''.join([ m.to_verilog() for m in modules.values() ])
    print(verilog)
