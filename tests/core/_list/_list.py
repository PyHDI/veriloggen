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
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = [m.OutputReg('LED_%d' % i, width) for i in range(8)]
    count = m.Reg('count', 32)

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))

    case_body = [When(i)(led[i](count[0:width], blk=True)) for i in range(8)]

    m.Always()(
        Case(count % 8)(
            *case_body
        )
    )

    return m


if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
