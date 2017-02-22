from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.fixed as fixed

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
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

    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            If(count == 1024 - 1)(
                led(led + 1)
            )
        ))
    
    a = fixed.FixedReg(m, 'a', point=4)
    b = fixed.FixedReg(m, 'b', point=8)
    c = fixed.FixedReg(m, 'c', point=16)
    d = fixed.FixedReg(m, 'd', point=6)
    sa = fixed.FixedReg(m, 'sa', point=4, signed=True)
    sb = fixed.FixedReg(m, 'sb', point=8, signed=True)
    sc = fixed.FixedReg(m, 'sc', point=16, signed=True)
    sd = fixed.FixedReg(m, 'sd', point=6, signed=True)

    m.Always(Posedge(clk))(
        If(rst)(
            a(fixed.FixedConst(1, 4)),
            b(fixed.FixedConst(32, 4, raw=True)),
            c(fixed.FixedConst(32, 4, raw=True)),
            d(fixed.FixedConst(32, 4, raw=True)),
            sa(fixed.FixedConst(1, 4)),
            sb(fixed.FixedConst(32, 4, raw=True)),
            sc(fixed.FixedConst(32, 4, raw=True)),
            sd(fixed.FixedConst(32, 4, raw=True))
        ).Else(
            a(a * b),
            b(a * b),
            c(a * b),
            d(b * a),
            sa(sa * sb),
            sb(sa * sb),
            sc(sa * sb),
            sd(sb * sa)
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog('')
    print(verilog)
