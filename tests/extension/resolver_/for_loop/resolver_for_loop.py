from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.resolver.resolver as resolver

def mkOrigLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    
    count = m.Reg('count', 32, width)
    i = m.Integer('i')

    m.Always(Posedge(clk))(
        If(rst)(
            For(i(0), i<width, i.inc())(
                count[i](0)
            )
        ).Else(
            For(i(0), i<width, i.inc())(
                If(count[i] == 1023)(
                    count[i](0)
                ).Else(
                    count[i](count[i] + i)
                )
            )
        ))
    
    _sum = m.Reg('_sum', 32)

    m.Always(Posedge(clk))(
        If(rst)(
            led( 0 )
        ).Else(
            _sum(0, blk=True),
            For(i(0), i<width, i.inc())(
                _sum(_sum + count[i], blk=True)
            ),
            If(_sum == Int(1024 - 1) * width)(
                led(led + 1)
            )
        ))

    return m

def mkLed():
    led = mkOrigLed()
    # resolve() is idempotent
    led = resolver.resolve(led)
    led = resolver.resolve(led)
    led = resolver.resolve(led)
    return resolver.resolve(led)

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
