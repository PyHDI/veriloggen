from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

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
    
    return m

def mkTest():
    m = Module('test')
    width = m.Parameter('WIDTH', 8)
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    led = m.Wire('LED', width)

    uut = m.Instance(mkLed(), 'uut',
                     params=(('WIDTH', width),),
                     ports=(('CLK', clk), ('RST', rst), ('LED', led)))

    m.Initial(
        Systask('dumpfile', 'uut.vcd'),
        Systask('dumpvars', 0, uut)
    )

    m.Initial(
        clk(0),
        Forever(clk(Not(clk), ldelay=5)) # forever #5 CLK = ~CLK;
    )

    m.Initial(
        rst(0),
        Delay(100),
        rst(1),
        Delay(100),
        rst(0),
        Delay(1000),
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('')
    print(verilog)
