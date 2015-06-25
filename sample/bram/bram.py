import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from veriloggen import *

def mkBramInterface(m, addrwidth, datawidth):
    addr = m.Input('addr', addrwidth)
    datain = m.Input('datain', datawidth)
    write = m.Input('write')
    dataout = m.Output('dataout', datawidth)
    return addr, datain, write, dataout
    
def mkBramUser(m, name, addrwidth, datawidth):
    addr = m.Reg(name + 'addr', addrwidth)
    datain = m.Reg(name + 'datain', datawidth)
    write = m.Reg(name + 'write')
    dataout = m.Wire(name + 'dataout', datawidth)
    return addr, datain, write, dataout
    
def mkBram(name):
    m = Module(name + '_bram')
    addrwidth = m.Parameter('ADDR_WIDTH', 10)
    datawidth = m.Parameter('DATA_WIDTH', 32)
    clk = m.Input('CLK')
    addr, datain, write, dataout = mkBramInterface(m, addrwidth, datawidth)
    d_addr = m.Reg('d_' + addr.name, datawidth)
    mem = m.Reg('mem', datawidth, addrwidth)
    
    m.Always(Posedge(clk))(
        If(write)( mem[addr](datain) ),
        d_addr(addr)
    )
    m.Assign(dataout(mem[d_addr]))

    return m

def mkUser(bram):
    m = Module('TOP')
    addrwidth = m.Parameter('ADDR_WIDTH', 10)
    datawidth = m.Parameter('DATA_WIDTH', 32)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    addr, datain, write, dataout = mkBramUser(m, 'my_', addrwidth, datawidth)
    
    params = ('ADDR_WIDTH', addrwidth), ('DATA_WIDTH', datawidth)
    ports = ('CLK', clk), ('addr', addr), ('datain', datain), ('write', write), ('dataout', dataout)
    m.Instance(bram, 'inst_bram', params, ports)

    state = m.Reg('state', 32)
    
    label = []
    label.append(m.Localparam('INIT' + str(len(label)), len(label)))
    
    def cond(name='label'):
        ret = state == label[-1]
        label.append(m.Localparam(name + str(len(label)), len(label)))
        return ret
    
    def goto_next():
        return state( state + 1 )
    
    m.Always(Posedge(clk))(
        If(rst)(
            addr(0), datain(0), write(0), state(0)
        ).els(
            If(cond())( addr(0), datain(0), write(0), goto_next() ),
            If(cond())( write(1), datain(datain + 4), goto_next() ),
            If(cond())( write(0), goto_next() ),
            If(cond())(
                If(addr == 128)(
                    addr(0), state(label[0])
                ).els(
                    addr(addr + 1), state(label[1])
                )
            )))

    return m

#-------------------------------------------------------------------------------
bram = mkBram('my')
user = mkUser(bram)
verilog = ''.join( (bram.toVerilog(), user.toVerilog()) )
print(verilog)
