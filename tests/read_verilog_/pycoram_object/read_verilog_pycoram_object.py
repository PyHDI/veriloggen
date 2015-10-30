import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkUserlogic():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/userlogic.v'
    modules = read_verilog_module(filename)
    return modules

if __name__ == '__main__':
    modules = mkUserlogic()
    verilog = ''.join([ m.to_verilog() for m in modules.values() ])
    print(verilog)
