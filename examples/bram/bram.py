from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

#-------------------------------------------------------------------------------
# BRAM bundle
#-------------------------------------------------------------------------------
class BramBundle(lib.Bundle):
    def __init__(self, m, prefix='', postfix='', addrwidth=10, datawidth=32, direction='child'):
        lib.Bundle.__init__(self, m, prefix, postfix)

        if direction != 'child' and direction != 'parent':
            raise ValueError("direction should be 'in or 'parent''")
        self.direction = direction
        
        self.addrwidth = self.Parameter('ADDR_WIDTH', addrwidth)
        self.datawidth = self.Parameter('DATA_WIDTH', datawidth)
        
        In = self.Input if self.direction == 'child' else self.Reg # self.Wire
        Out = self.Output if self.direction == 'child' else self.Wire 
        
        self.addr = In('addr', addrwidth)
        self.datain = In('datain', datawidth)
        self.write = In('write')
        self.dataout = Out('dataout', datawidth)

    def init(self):
        if self.direction == 'parent':
            return self.addr(0), self.datain(0), self.write(0)
        raise Exception("init() is not allowed.")
        
#-------------------------------------------------------------------------------
# BRAM module
#-------------------------------------------------------------------------------
def mkBram(name):
    m = Module(name + 'bram')
    
    addrwidth = m.Parameter('ADDR_WIDTH', 10)
    datawidth = m.Parameter('DATA_WIDTH', 32)
    
    clk = m.Input('CLK')
    bramif = BramBundle(m, addrwidth=addrwidth, datawidth=datawidth, direction='child')
    
    d_addr = m.Reg('d_' + bramif.addr.name, datawidth)
    mem = m.Reg('mem', datawidth, Int(2)**addrwidth)
    
    m.Always(Posedge(clk))(
        If(bramif.write)( mem[bramif.addr](bramif.datain) ),
        d_addr(bramif.addr)
    )
    
    m.Assign(bramif.dataout(mem[d_addr]))
    
    return m

#-------------------------------------------------------------------------------
# Top module
#-------------------------------------------------------------------------------
def mkTop():
    m = Module('TOP')
    addrwidth = m.Parameter('ADDR_WIDTH', 10)
    datawidth = m.Parameter('DATA_WIDTH', 32)
    clk = m.Input('CLK')
    rst = m.Input('RST')

    bramif = BramBundle(m, prefix='bram_',
                        addrwidth=addrwidth, datawidth=datawidth, direction='parent')

    params = []
    params.extend( bramif.connect_all_parameters() )

    ports = [ clk.connect() ]
    ports.extend( bramif.connect_all_ports() )

    m.Instance(mkBram('my_'), 'inst_bram', params, ports)

    # FSM definition
    fsm = lib.FSM(m, 'fsm', clk, rst)

    # initialize
    fsm.add( bramif.init() )
    fsm.add(bramif.datain(-Int(4)))
    fsm.goto_next()

    # write
    cond = bramif.addr<128
    fsm.add(bramif.addr.inc(), bramif.write(1), bramif.datain(bramif.datain + 4), cond=cond)
    fsm.add(Systask('display', 'addr:%x write: %x', bramif.addr-1, bramif.datain),
            cond=cond, delay=1)
    
    fsm.add(bramif.init(), cond=Not(cond))
    fsm.goto_next(cond=Not(cond))

    # read
    cond = bramif.addr<128
    fsm.add(bramif.addr.inc(), cond=cond)
    prev_addr = m.TmpReg(addrwidth, initval=0)
    fsm.add(prev_addr(bramif.addr), delay=1)
    fsm.add(Systask('display', 'addr:%x read : %x', prev_addr-1, bramif.dataout),
            cond=cond, delay=2)
    
    fsm.add(bramif.init(), cond=Not(cond))
    fsm.goto_next(cond=Not(cond))

    fsm.make_always(reset=bramif.init())
    
    return m

#-------------------------------------------------------------------------------
# Testbench
#-------------------------------------------------------------------------------
def mkTest():
    m = Module('test')

    # target instance
    top = mkTop()

    # copy paras and ports
    params = m.copy_params(top)
    ports = m.copy_sim_ports(top)

    clk = ports['CLK']
    rst = ports['RST']
    
    uut = m.Instance(top, 'uut',
                     params=m.connect_params(top),
                     ports=m.connect_ports(top))
    
    #lib.simulation.setup_waveform(m, uut)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(10000),
        Systask('finish'),
    )

    return m

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog()
    print(verilog)

    sim = lib.simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)
