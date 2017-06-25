from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')
    a = m.Input('a')
    b = m.Input('b')
    c = m.Input('c')

    x = a + b + 1
    y = a
    y = y + b
    y = y + 1
    z = a - b

    c.assign(x + y + z)

    print(equals(x, y))
    print(equals(x, z))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
