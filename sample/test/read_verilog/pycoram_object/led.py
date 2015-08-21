import sys
import os
import collections

from veriloggen import *

def mkUserlogic():
    modules = read_verilog_module('userlogic.v')
    return modules

if __name__ == '__main__':
    modules = mkUserlogic()
    code = ''.join([ m.to_verilog() for m in modules.values() ])
    print(code)
