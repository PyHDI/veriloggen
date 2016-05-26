from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.resolver.resolver as resolver

def mkSubLed():
    m = Module('sub_blinkled')

    width = m.Parameter('WIDTH', 8)
    inc = m.Parameter('INC', 1)
    
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    
    count = m.Reg('count', width + 10)

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + inc)
            )
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led( 0 )
        ).Else(
            If(count == 1023)(
                led(led + inc)
            )
        ))

    return m

def mkOrigLed():
    m = Module('blinkled')
    sub = mkSubLed()
    
    width = m.Parameter('TOP_WIDTH', 16)
    inc = m.Parameter('TOP_INC', 1)
    
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led0 = m.Output('LED0', width)
    led1 = m.Output('LED1', width)
    
    m.Instance(sub, 'inst_sub_blinkled_0',
               params=[('WIDTH', width), ('INC', inc + 1)],
               ports=[('CLK', clk), ('RST', rst), ('LED', led0)])
    
    m.Instance(sub, 'inst_sub_blinkled_1',
               params=[('WIDTH', width), ('INC', inc + 2)],
               ports=[('CLK', clk), ('RST', rst), ('LED', led1)])
    
    return m

def mkLed():
    led = mkOrigLed()
    return resolver.resolve(led)

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
