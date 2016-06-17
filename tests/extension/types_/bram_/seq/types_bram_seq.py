from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.bram as bram

def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2

    mybram = bram.Bram(m, 'mybram', clk, rst, datawidth, addrwidth, 2)
    mybram.disable_write(1)

    seq = Seq(m, 'seq', clk, rst)
    

    # write
    waddr = m.Reg('waddr', 32, initval=0)
    count = m.Reg('count', 32, initval=0)

    seq.If(waddr < 16)(
        waddr.inc(),
        count.inc()
    )

    mybram.write(seq.Then(), 0, waddr, count)

    
    # read
    raddr = m.Reg('raddr', 32, initval=0)
    sum = m.Reg('sum', 32, initval=0)
    
    seq.If(raddr < 16)(
        raddr.inc(),
    )
    
    read_data, read_valid = mybram.read(seq, 1, raddr, cond=raddr<16, delay=3)
    
    seq.If(read_valid)(
        sum(sum + read_data)
    )
    
    seq.Then().Delay(1)(
        Systask('display', "sum=%d", sum)
    )
    
    seq.make_always()
    
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
