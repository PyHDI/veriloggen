import sys
import os
from veriloggen import *

def mkSort(numports=4):
    m = Module('sort')
    width = m.Parameter('WIDTH', 32)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    inputs = [ m.Input('input_' + str(i), width) for i in range(numports) ] 
    outputs = [ m.Output('output_' + str(i), width) for i in range(numports) ]
    kick = m.Input('kick')
    busy = m.OutputReg('busy')
    registers = [ m.Reg('registers_' + str(i), width) for i in range(numports) ]
    for i in range(numports): m.Assign(outputs[i](registers[i]))
    
    _i = [0]
    def mk_pair():
        s = m.Wire('small_' + str(_i[0]), width)
        l = m.Wire('large_' + str(_i[0]), width)
        _i[0] += 1
        return s, l

    def prim_net(a, b):
        s, l = mk_pair()
        m.Assign(s( Cond(a < b, a, b) )) # small
        m.Assign(l( Cond(a < b, b, a) )) # large
        return s, l

    def chain_net(regs, fsm, e):
        x = regs[0]
        bind = []
        for i in range(e):
            s, l = prim_net(x, regs[i+1])
            bind.append( regs[i](s) )
            x = l
        bind.append( regs[e](x) )
        for i in range(e + 1, len(regs)):
            bind.append( regs[i](regs[i]) )
        fsm( bind, fsm.next() )
    
    fsm = lib.FSM(m, 'fsm')
    idle = fsm.get_index()

    fsm([ If(kick)([ registers[i](inputs[i]) for i in range(numports) ] +
                   [ busy(1), fsm.next()] ) ])

    for i in range(numports):
        chain_net(registers, fsm, numports-i-1)

    fsm( busy(0), fsm.goto(idle) )

    init = [ busy(0) ] + [ r(0) for r in registers ] + [ fsm.init() ]

    m.Always(Posedge(clk))(
        If(rst)(
            *init
        ).Else(
            fsm.to_case()
        ))
    
    return m

if __name__ == '__main__':
    led = mkSort()
    verilog = led.to_verilog()
    print(verilog)
