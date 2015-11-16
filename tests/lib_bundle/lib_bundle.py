from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

class LedBundle(lib.Bundle):
    def __init__(self, m, prefix='', postfix='', width=8, maxvalue=1024, direction='child'):
        lib.Bundle.__init__(self, m, prefix, postfix)

        if direction != 'child' and direction != 'parent':
            raise ValueError("direction should be 'in or 'parent''")
        self.direction = direction

        self.width = width
        self.maxvalue = maxvalue
        
        In = self.Input if self.direction == 'child' else self.Wire
        Out = self.OutputReg if self.direction == 'child' else self.Output

        self.led = Out('LED', self.width)
        if direction == 'child':
            self.count = self.Reg('count', 32)

    def init(self):
        if self.direction == 'child':
            return self.count(0), self.led(0)
        raise Exception("init() is not allowed.")

    def step(self):
        ret = If( self.count == self.maxvalue -1 )(
            self.count( 0 ),
            self.led( self.led + 1 )
        ).Else(
            self.count( self.count + 1 )
        )
        return ret
    
def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    ledif = LedBundle(m, width=width, direction='child')

    m.Always(Posedge(clk))(
        If(rst)(
            *ledif.init()
        ).Else(
            ledif.step()
        ))

    return m

def mkTop(wid=8):
    m = Module('top')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    width = m.Parameter('WIDTH', wid)
    ledif = LedBundle(m, width=width, direction='parent')
    
    params = []
    params.extend(ledif.connect_all_parameters())
    
    ports = []
    ports.append(clk.connect())
    ports.append(rst.connect())
    ports.extend(ledif.connect_all_ports())
    
    m.Instance(mkLed(), 'inst_led', params, ports)
    
    return m

if __name__ == '__main__':
    led = mkTop()
    verilog = led.to_verilog()
    print(verilog)
