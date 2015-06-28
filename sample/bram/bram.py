import sys
import os
import collections

from veriloggen import *

class BramInterface(Interface):
    def __init__(self, m, prefix, postfix, addrwidth, datawidth, io=False):
        Interface.__init__(self, m, prefix, postfix, io)
        
        self.addrwidth = self.Parameter('ADDR_WIDTH', addrwidth)
        self.datawidth = self.Parameter('DATA_WIDTH', datawidth)
        
        In = self.Input if self.io else self.Reg # self.Wire
        Out = self.Output if self.io else self.Wire 
        
        self.addr = In('addr', addrwidth)
        self.datain = In('datain', datawidth)
        self.write = In('write')
        self.dataout = Out('dataout', datawidth)
    
def mkBram(name):
    m = Module(name + 'bram')
    
    addrwidth = m.Parameter('ADDR_WIDTH', 10)
    datawidth = m.Parameter('DATA_WIDTH', 32)
    
    clk = m.Input('CLK')
    bramif = BramInterface(m, '', '', addrwidth, datawidth, io=True)
    
    d_addr = m.Reg('d_' + bramif.addr.name, datawidth)
    mem = m.Reg('mem', datawidth, Int(2)**addrwidth)
    
    m.Always(Posedge(clk))(
        If(bramif.write)( mem[bramif.addr](bramif.datain) ),
        d_addr(bramif.addr)
    )
    
    m.Assign(bramif.dataout(mem[d_addr]))
    
    return m

def mkTop():
    m = Module('TOP')
    addrwidth = m.Parameter('ADDR_WIDTH', 10)
    datawidth = m.Parameter('DATA_WIDTH', 32)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    bramif = BramInterface(m, 'bram_', '', addrwidth, datawidth)

    params = collections.OrderedDict()
    params.update(bramif.connectAllParameters())
    
    ports = collections.OrderedDict()
    ports.update(clk.connect())
    ports.update(bramif.connectAllPorts())

    m.Instance(bram, 'inst_bram', params, ports)

    fsm = lib.FSM(m, 'fsm')
    m.Always(Posedge(clk))(
        If(rst)(
            bramif.addr(0), bramif.datain(0), bramif.write(0), fsm.next(0)
        ).els(
            fsm( bramif.addr(0), bramif.datain(0), bramif.write(0), fsm.next() ),
            fsm( bramif.datain(bramif.datain + 4), fsm.next() ),
            fsm( bramif.write(0), fsm.next() ),
            fsm( 
                If(bramif.addr == 128)(
                    bramif.addr(0), fsm.next(0)
                ).els(
                    bramif.addr(bramif.addr + 1), fsm.next(1)
                ))
            ))

    return m

#-------------------------------------------------------------------------------
bram = mkBram('my_')
top = mkTop()
verilog = ''.join( (bram.toVerilog(), top.toVerilog()) )
print(verilog)
