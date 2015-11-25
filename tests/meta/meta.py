from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

# new intance methods for NewModule
_recipe_control = lambda m: (m.Input('CLK'), m.Input('RST'))
_recipe_led = lambda m, width=8: (m.OutputReg('LED', width, initval=0),
                                  m.Reg('count', 32, initval=0))

# new class based on Module
NewModule = type('NewModule', (Module,),
                 { 'recipe_control' : _recipe_control,
                   'recipe_led' : _recipe_led } )

def mkLed(width=8, maxcount=1024):
    m = NewModule('blinkled')
    clk, rst = m.recipe_control()
    led, count = m.recipe_led(width)
    seq = m.Seq('seq', clk, rst)
    seq( count.inc() )
    seq( count(0), cond=count==maxcount-1 )
    seq( led.inc(), cond=count==maxcount-1 )
    seq.make_always()
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
