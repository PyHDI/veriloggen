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
    led = m.OutputReg('LED', width, initval=0)
    count = m.Reg('count', 32, initval=0)
    
    seq = lib.Seq(m, 'seq', clk, rst)

    seq.add( count.inc(), cond=(count<1024-1) )
    seq.add( count(0), cond=(count>=1024-1) )
    seq.add( led.inc(), cond=(count>=1024-1) ) 
    
    #seq.make_always()
    # make_alway() is called when to_veirlog() is called.
    m.add_hook(seq.make_always, args=(), kwargs={})
    
    return m

if __name__ == '__main__':
    led = mkLed()
    # to_verilog() method is immuatable.
    # Hooked methods are called for the copied object to keep the internal state.
    dummy = led.to_verilog()
    verilog = led.to_verilog()
    print(verilog)