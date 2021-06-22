from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *

class SeqIfElse(object):
    def __init__(self, condition, true_statements, false_statements=()):
        self.condition = condition
        self.true_statements = true_statements
        self.false_statements = false_statements

    def __len__(self):
        return len(self.true_statements) + len(self.true_statements)
        
def add_if_else(fsm, ifelse):
    # future index
    index_else = fsm.current + len(ifelse.true_statements) + 1
    index_merge = fsm.current + len(ifelse.true_statements) + len(ifelse.false_statements) + 1
    index_true = fsm.current + 1 if ifelse.true_statements else index_merge
    
    fsm.goto( dst=index_true, cond=ifelse.condition, else_dst=index_else )
    fsm.inc()

    # then
    for i, s in enumerate(ifelse.true_statements):
        if i < len(ifelse.true_statements) - 1:
            fsm( *s )
            fsm.goto_next()
        else:
            fsm( *s )
            fsm.goto(index_merge)
            fsm.inc()

    # else
    for i, s in enumerate(ifelse.false_statements):
        if i < len(ifelse.false_statements) - 1:
            fsm( *s )
            fsm.goto_next()
        else:
            fsm( *s )
            fsm.goto_next()

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width, initval=0)
    count = m.Reg('count', 32, initval=0)

    fsm = FSM(m, 'fsm', clk, rst)
    # get the initial index (= 0)
    init = fsm.current

    fsm( count(count + 1) )
    fsm.goto_next()

    # if-then-else statements
    condition = count < 1024
    true_statements = [ [ count(count + 2) ],
                        [ count(count + 3) ] ]
    false_statements = [ [ led(led + 1) ],
                         [ led(led + 2) ] ]
    ifelse = SeqIfElse(condition, true_statements, false_statements)
    add_if_else(fsm, ifelse)
    
    # go to first
    fsm.goto(init)
    
    fsm.make_always()
    
    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
