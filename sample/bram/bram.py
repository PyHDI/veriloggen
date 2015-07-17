import sys
import os
import collections

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

    params = collections.OrderedDict()
    params.update(bramif.connect_all_parameters())
    
    ports = collections.OrderedDict()
    ports.update(clk.connect())
    ports.update(bramif.connect_all_ports())

    m.Instance(mkBram('my_'), 'inst_bram', params, ports)

    # FSM definition
    fsm = lib.FSM(m, 'fsm')
    init = fsm.get_index()
    
    fsm( bramif.init(), fsm.next() )
    first = fsm.get_index()
    
    fsm( bramif.datain(bramif.datain + 4), fsm.next() )
    fsm( bramif.write(0), fsm.next() )
    fsm( 
        If(bramif.addr == 128)(
            bramif.addr(0), fsm.goto(init)
        ).Else(
            bramif.addr(bramif.addr + 1), fsm.goto(first)
        ))
    
    m.Always(Posedge(clk))(
        If(rst)(
            bramif.addr(0), bramif.datain(0), bramif.write(0), fsm.init()
        ).Else(
            # inserting FSM body
            *fsm.to_if()
        ))

    return m

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    top = mkTop()
    # top.to_verilog(filename='tmp.v')
    verilog = top.to_verilog()
    print(verilog)
