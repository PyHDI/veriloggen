import sys
import os
import collections

from veriloggen import *

def mkThread():
    modules = read_verilog_module('ctrl_thread.v')
    return modules

if __name__ == '__main__':
    modules = mkThread()
    code = ''.join([ m.to_verilog() for m in modules.values() ])
    print(code)
