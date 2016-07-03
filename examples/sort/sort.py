from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

nclk = simulation.next_clock 

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
        for i in range(e):
            s, l = prim_net(x, regs[i+1])
            fsm.add( regs[i](s) )
            x = l
        fsm.add( regs[e](x) )
        for i in range(e + 1, len(regs)):
            fsm.add( regs[i](regs[i]) )
        fsm.goto_next()

    # build up
    fsm = FSM(m, 'fsm', clk, rst)
    idle = fsm.current

    # init state
    fsm.add(*[registers[i](inputs[i]) for i in range(numports)], cond=kick)
    fsm.add(busy(1), cond=kick)
    fsm.goto_next(cond=kick)

    # connect network
    for i in range(numports):
        chain_net(registers, fsm, numports-i-1)

    # finalize
    fsm.add(busy(0))
    fsm.goto(idle)

    fsm.make_always([ busy(0) ] + [ r(0) for r in registers ],
                    [Systask('display', r.name + ': %d', r) for r in registers])
    
    return m

def mkSimSort(numports=4):
    m = Module('simsort')
    width = m.Parameter('WIDTH', 32)
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    inputs = [ m.Reg('input_' + str(i), width) for i in range(numports) ] 
    outputs = [ m.Wire('output_' + str(i), width) for i in range(numports) ]
    kick = m.Reg('kick')
    busy = m.Wire('busy')

    uut = m.Instance(mkSort(numports), 'uut', (width,),
                     [clk, rst] + inputs + outputs + [kick, busy])
    
    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk)
    simulation.setup_reset(m, rst)

    m.Initial(
        [ ip(100 - i) for i, ip in enumerate(inputs) ],
        kick(0),
        
        Wait(rst),
        nclk(clk),
        
        Wait(Not(rst)),
        nclk(clk),
        nclk(clk),
        nclk(clk),
        
        kick(1),
        nclk(clk),
        kick(0),
    )

    m.Initial(
        Delay(100),
        Wait(kick),
        nclk(clk),
        
        Wait(busy),
        nclk(clk),
        
        Wait(Not(busy)),
        nclk(clk),
        
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    sort = mkSimSort()
    verilog = sort.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(sort)
    rslt = sim.run()
    print(rslt)
