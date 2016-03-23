from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

prim_mux = None

def mkPrimMux():
    global prim_mux
    if prim_mux is not None:
        return prim_mux
    
    m = Module('prim_mux')
    width = m.Parameter('WIDTH', 1)
    sel = m.Input('sel')
    ina = m.Input('ina', width=width)
    inb = m.Input('inb', width=width)
    out = m.Output('out', width=width)
    m.Assign( out(Mux(sel, ina, inb)) )
    prim_mux = m
    return m

def Pmux(m, cond, true_value, false_value, width=32):
    mux = mkPrimMux()
    sel = m.TmpWire()
    ina = m.TmpWire(width=width)
    inb = m.TmpWire(width=width)
    out = m.TmpWire(width=width)
    m.Assign(sel(cond))
    m.Assign(ina(true_value))
    m.Assign(inb(false_value))
    m.Instance(mux, '_'.join(['inst', mux.name, out.name]),
               params=[('WIDTH', width)],
               ports=[sel, ina, inb, out])
    return out
    
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
            count( Pmux(m, count==1023, 0, count + 1, width=32) )
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            led( Pmux(m, count==1024-1, led+1, led, width=width) )
        ))
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog('')
    print(verilog)
