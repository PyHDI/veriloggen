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
    
    a = fixed.FixedReg(m, 'a', point=6)
    b = fixed.FixedReg(m, 'b', point=8)
    c = fixed.FixedReg(m, 'c', point=4)
    d = fixed.FixedReg(m, 'd', point=8)

    m.Always(Posedge(clk))(
        If(rst)(
            a(fixed.FixedConst(Int(2) * Int(2), 6)),
            b(fixed.FixedConst(1, 8, raw=True)),
            c(1),
            d.raw(1)
        ).Else(
            a(a + 1),
            b(a + 1),
            c.raw(b.raw + 1),
            d.raw((c + 1).raw)
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog('')
    print(verilog)
