from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.fifo as fifo

def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2

    myfifo = fifo.Fifo(m, 'myfifo', clk, rst, datawidth, addrwidth)

    # example how to access BRAM
    count = m.Reg('count', 32, initval=0)
    sum = m.Reg('sum', 32, initval=0)
    
    fsm = FSM(m, 'fsm', clk, rst)

    fsm(
        count(0),
    )
    
    fsm.goto_next()

    step = 10

    ack = myfifo.enq(fsm, count)
    
    fsm.If(ack)(
        count.inc()
    )

    fsm.If(Ands(ack, count==step-1)).goto_next()

    fsm(
        count(0)
    )

    fsm.goto_next()
    
    data, valid = myfifo.deq(fsm)

    fsm.If(valid)(
        sum(sum + data),
        count.inc()
    )

    fsm.then.Delay(1)(
        Systask('display', "sum=%d", sum)
    )
    
    fsm.If(count == step).goto_next()
    
    fsm.make_always()
    
    return m
    
def mkTest():
    m = Module('test')
    
    # target instance
    main = mkMain()
    
    # copy paras and ports
    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)
    
    clk = ports['CLK']
    rst = ports['RST']
    
    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))
    
    simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)
    
    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m
    
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    #sim.view_waveform()
