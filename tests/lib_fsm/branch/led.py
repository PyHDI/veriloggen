import sys
import os

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
    index_else = fsm.current() + len(ifelse.true_statements) + 1
    index_merge = fsm.current() + len(ifelse.true_statements) + len(ifelse.false_statements) + 1
    index_true = fsm.current() + 1 if ifelse.true_statements else index_merge
    
    fsm.goto( index=index_true, cond=ifelse.condition, else_index=index_else ).inc()
    # = fsm.add(If(ifelse.condition)( fsm.set(index_true) ).Else( fsm.set(index_else) )).inc()

    # then
    for i, s in enumerate(ifelse.true_statements):
        if i < len(ifelse.true_statements) - 1:
            fsm.add( *s )
            fsm.goto_next()
            # = fsm.add( *(s+[fsm.set_next()]) ).inc()
        else:
            fsm.add( *s )
            fsm.goto(index_merge).inc()
            # = fsm.add( *(s+[fsm.set(index_merge)]) ).inc()

    # else
    for i, s in enumerate(ifelse.false_statements):
        if i < len(ifelse.false_statements) - 1:
            fsm.add( *s )
            fsm.goto_next()
            # = fsm.add( *(s+[fsm.set_next()]) ).inc()
        else:
            fsm.add( *s )
            fsm.goto_next()
            # = fsm.add( *(s+[fsm.set_next()]) ).inc()

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    fsm = lib.FSM(m, 'fsm')
    # get the initial index (= 0)
    init = fsm.current()

    fsm.add( count(count + 1) )
    fsm.goto_next()
    # = fsm.add(count(count + 1), fsm.set_next()).inc()

    # if-then-else statements
    condition = count < 1024
    true_statements = [ [ count(count + 2) ],
                        [ count(count + 3) ] ]
    false_statements = [ [ led(led + 1) ],
                         [ led(led + 2) ] ]
    ifelse = SeqIfElse(condition, true_statements, false_statements)
    add_if_else(fsm, ifelse)
    
    # go to first
    fsm.goto(init) # = fsm.add( fsm.set(init) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0),
            fsm.set_init()
        ).Else(
            # inserting the FSM body
            #*fsm.make_if()
            fsm.make_case()
        ))

    return m

if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
