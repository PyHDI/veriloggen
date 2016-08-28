from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkMips():
    file = os.path.dirname(os.path.abspath(__file__)) + '/branch.v'
    modules = from_verilog.read_verilog_module(file)
    return modules

if __name__ == '__main__':
    mips_modules = mkMips()
    verilog = ''.join([ m.to_verilog() for m in mips_modules.values() if not m.used ])
    print(verilog)
