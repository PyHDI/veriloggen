import sys
import os

from veriloggen import *

def add_if_then_else(fsm, condition, true_statements, false_statements):
    # future index
    index_else = fsm.get_index() + len(true_statements) + 1
    index_merge = fsm.get_index() + len(true_statements) + len(false_statements) + 1
    index_true = fsm.get_index() + 1 if true_statements else index_merge
    
    fsm(If(condition)( fsm.goto(index_true) ).Else( fsm.goto(index_else) ))

    # then
    for i, s in enumerate(true_statements):
        if i < len(true_statements) - 1:
            fsm( *(s+[fsm.next()]) )
        else:
            fsm( *(s+[fsm.goto(index_merge)]) )

    # else
    for i, s in enumerate(false_statements):
        if i < len(false_statements) - 1:
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
    add_if_then_else(fsm, condition, true_statements, false_statements)
    
    # goto first
    fsm( fsm.goto(init) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0),
            fsm.init()
        ).Else(
            # inserting the FSM body
            *fsm.get_all()
        ))

    return m

if __name__ == '__main__':
    led_module = mkLed()
    led_code = led_module.to_verilog()
    print(led_code)
