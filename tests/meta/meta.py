import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

# new intance methods for NewModule
_FSM = lambda self, *args, **kwargs: lib.FSM(self, *args, **kwargs)
_Seq = lambda self, *args, **kwargs: lib.Seq(self, 'seq', *args, **kwargs)
_recipe_control = lambda m: (m.Input('CLK'), m.Input('RST'))
_recipe_led = lambda m, width=8: (m.OutputReg('LED', width, initval=0),
                                  m.Reg('count', 32, initval=0))

# new class based on Module
NewModule = type('NewModule', (Module,),
                 { 'FSM' : _FSM,
                   'Seq' : _Seq,
                   'recipe_control' : _recipe_control,
                   'recipe_led' : _recipe_led })

def mkLed(width=8, maxcount=1024):
    m = NewModule('blinkled')
    clk, rst = m.recipe_control()
    led, count = m.recipe_led(width)
    seq = m.Seq()
    seq( count.inc() )
    seq( count(0), cond=count==maxcount-1 )
    seq( led.inc(), cond=count==maxcount-1 )
    seq.make_always(clk, rst)
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
