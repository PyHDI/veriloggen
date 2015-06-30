import sys
import os

from veriloggen import *

def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)
    count = m.Reg('count', 32)

    fsm = lib.FSM(m, '')
    fsm_contents = []
    fsm_contents.append( fsm(count(count + 1), fsm.next()) )
    fsm_contents.append( fsm(count(count + 2), fsm.next()) )
    fsm_contents.append( fsm(count(count + 3), fsm.next()) )
    fsm_contents.append( fsm(If(count < 1024)( fsm.next(0) ).els( fsm.next() )) )
    fsm_contents.append( fsm(led(led + 1), fsm.next(0)) )
    
    m.Always(Posedge(clk))(
        If(rst)(
            count(0),
            led(0),
            fsm.next(0)
        ).els(
            tuple(fsm_contents)
        ))

    return m

led = mkLed()
verilog = led.toVerilog()
print(verilog)
