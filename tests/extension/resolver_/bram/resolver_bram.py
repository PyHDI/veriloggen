from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.resolver.resolver as resolver

def mkBram(datawidth=32, addrwidth=10, numports=2):
    m = Module('BRAM%d' % numports)

    datawidth = m.Parameter('DATA_WIDTH', datawidth)
    addrwidth = m.Parameter('ADDR_WIDTH', addrwidth)

    clk = m.Input('CLK')
    ports = []
    for i in range(numports):
        addr = m.Input('ADDR%d' % i, addrwidth)
        din = m.Input('DIN%d' % i, datawidth)
        we = m.Input('WE%d' % i)
        dout = m.Output('DOUT%d' % i, datawidth)
        delay_addr = m.Reg('delay_ADDR%d' % i, addrwidth)
        ports.append( (addr, din, we, dout, delay_addr) )

    mem = m.Reg('mem', datawidth, Int(2)**addrwidth)

    for i in range(numports):
        addr, din ,we, dout, delay_addr = ports[i]
        m.Always(Posedge(clk))(
            If(we)(
                mem[addr](din)
            ),
            delay_addr(addr)
        )
        m.Assign(dout(mem[delay_addr]))

    return m

def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2

    datawidth = m.Parameter('DATA_WIDTH', datawidth)
    addrwidth = m.Parameter('ADDR_WIDTH', addrwidth)
    
    bram = mkBram(datawidth, addrwidth, numports)

    bram_ports = []
    for i in range(numports):
        addr = m.Reg('bram_addr%d' % i, addrwidth)
        din = m.Reg('bram_din%d' % i, datawidth)
        we = m.Reg('bram_we%d' % i)
        dout = m.Wire('bram_dout%d' % i, datawidth)
        bram_ports.append( [addr, din, we, dout] )

    params = [ (datawidth.name, datawidth), 
               (addrwidth.name, addrwidth) ]
    ports = [ clk ]
    for bram_port in bram_ports:
        ports.extend(bram_port)

    # BRAM instance
    m.Instance(bram, 'bram_inst', params=params, ports=ports)

    # example how to access BRAM
    fsm = FSM(m, 'fsm', clk, rst)
    
    for addr, din, we, dout in bram_ports:
        fsm.add( addr(0), din(0), we(0) )

    fsm.goto_next()

    count = m.Reg('count', 32, initval=0)
    for port, (addr, din, we, dout) in enumerate(bram_ports):
        fsm.add( addr(count+port*n//numports), din(count), we(1), count.inc() )

    fsm.goto_next(cond=count==n//numports-1)
    
    fsm.make_always()
    
    return m

def mkOrig():
    m = mkMain()
    m = resolver.resolve(m)
    return m
    
if __name__ == '__main__':
    orig = mkOrig()
    verilog = orig.to_verilog()
    print(verilog)
