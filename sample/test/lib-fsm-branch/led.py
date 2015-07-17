import sys
import os

from veriloggen import *

class SeqIfElse(object):
    def __init__(self, condition, true_statements, false_statements=()):
        self.condition = condition
        self.true_statements = true_statements
        self.false_statements = false_statements

def add_if_else(fsm, ifelse):
    # future index
    index_else = fsm.get_index() + len(ifelse.true_statements) + 1
    index_merge = fsm.get_index() + len(ifelse.true_statements) + len(ifelse.false_statements) + 1
    index_true = fsm.get_index() + 1 if ifelse.true_statements else index_merge
    
    fsm(If(ifelse.condition)( fsm.goto(index_true) ).Else( fsm.goto(index_else) ))

    # then
    for i, s in enumerate(ifelse.true_statements):
        if i < len(ifelse.true_statements) - 1:
            fsm( *(s+[fsm.next()]) )
        else:
            fsm( *(s+[fsm.goto(index_merge)]) )

    # else
    for i, s in enumerate(ifelse.false_statements):
        if i < len(ifelse.false_statements) - 1:
            fsm( *(s+[fsm.next()]) )
        else:
            fsm( *(s+[fsm.next()]) )

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    fsm = lib.FSM(m, 'fsm')
    # get the initial index (= 0)
    init = fsm.get_index()

    fsm(count(count + 1), fsm.next())

    # if-then-else statements
    condition = count < 1024
    true_statements = [ [ count(count + 2) ],
                        [ count(count + 3) ] ]
    false_statements = [ [ led(led + 1) ],
                         [ led(led + 2) ] ]
    ifelse = SeqIfElse(condition, true_statements, false_statements)
    add_if_else(fsm, ifelse)
    
    # goto first
    fsm( fsm.goto(init) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0),
            fsm.init()
        ).Else(
            # inserting the FSM body
            #*fsm.to_if()
            fsm.to_case()
        ))

    return m

if __name__ == '__main__':
    led_module = mkLed()
    led_code = led_module.to_verilog()
    print(led_code)
