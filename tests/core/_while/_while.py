from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkTest():
    m = Module('test')
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    count = m.Reg('count', width=32)

    m.Initial(
        Systask('dumpfile', 'uut.vcd'),
        Systask('dumpvars', 0, clk, rst, count),
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

        count(0),
        
        While(count < 1024)(
            count( count + 1 ),
            Event(Posedge(clk))
        ),
        
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('')
    print(verilog)
