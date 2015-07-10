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

    fsm = lib.FSM(m, 'fsm')
    # get the initial index (= 0)
    init = fsm.get_index()

    fsm(count(count + 1), fsm.next())
    fsm(count(count + 2), fsm.next())
    
    # get the current index (= 2)
    here = fsm.get_index()
    fsm(count(count + 3), fsm.next())

    # jump by using label "init"
    fsm(If(count < 1024)( fsm.goto(init) ).Else( fsm.next() ))
    
    # jump by using label "here"
    fsm(led(led + 1), fsm.goto(here))
    
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
