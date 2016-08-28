from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkUserlogic():
    here = os.path.dirname(os.path.abspath(__file__))
    filename = here + '/userlogic.v'
    modules = from_verilog.read_verilog_module(filename, include=[here])
    return modules

if __name__ == '__main__':
    modules = mkUserlogic()
    verilog = ''.join([ m.to_verilog() for m in modules.values() if not m.used ])
    print(verilog)
