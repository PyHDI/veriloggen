from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.resolver.resolver as resolver
import veriloggen.stream.div as div


def mkDiv():
    return div.get_div()


def mkOrig():
    m = mkDiv()
    m = resolver.resolve(m)
    return m


if __name__ == '__main__':
    orig = mkOrig()
    verilog = orig.to_verilog()
    print(verilog)
