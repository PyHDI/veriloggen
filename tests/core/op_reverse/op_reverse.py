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
    width = m.Parameter('WIDTH', 8)
    a = m.Input('A', 32)
    b = m.Output('B', width)

    b.assign(a[32 - width:32])

    return m


if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
