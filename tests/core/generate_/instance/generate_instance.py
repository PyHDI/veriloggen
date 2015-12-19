from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

def mkSubmod():
    m = Module('submod')
    pos = m.Parameter('POS', 0)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED')
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
    m.Assign( led(count[pos]) )
    return m

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)

    # genvar i;
    i = m.Genvar('i')
    
    # generate for(i=0; i<WIDTH; i=i+1) begin: gen_for;
    gen_for = m.GenerateFor(i(0), i<width, i(i+1), scope='gen_for')
    submod = mkSubmod()
    params = [ ('POS', i+2) ]
    ports = [ ('CLK', clk), ('RST', rst), ('LED', led[i]) ]
    gen_for.Instance(submod, 'inst_submod', params, ports)
    # ... end endgenerate
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
