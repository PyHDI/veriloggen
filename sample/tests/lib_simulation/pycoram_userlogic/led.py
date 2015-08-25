import sys
import os
import collections

from veriloggen import *

def mkPycoram():
    modules = read_verilog_module('pycoram.v')
    return modules

def mkUserlogic():
    m = Module('userlogic')
    data_width = m.Parameter('DATA_WIDTH', 32)
    addr_len = m.Parameter('ADDR_LEN', 10)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    mem_addr = m.Reg('mem_addr', addr_len, initval=0)
    mem_wdata = m.Reg('mem_wdata', data_width, initval=0)
    mem_rdata = m.Wire('mem_rdata', data_width)
    mem_wvalid = m.Reg('mem_wvalid', initval=0)
    ch_wdata = m.Reg('ch_wdata', data_width, initval=0)
    ch_enq = m.Reg('ch_enq', initval=0)
    ch_almfull = m.Wire('ch_almfull')
    ch_rdata = m.Wire('ch_rdata', data_width)
    ch_deq = m.Reg('ch_deq', initval=0)
    ch_empty = m.Wire('ch_empty')
    
    m.Instance('CoramMemory1P', 'mem',
               (('CORAM_THREAD_NAME', 'ctrl_thread'),
                ('CORAM_THREAD_ID', 0),
                ('CORAM_ID', 0),
                ('CORAM_SUB_ID', 0),
                ('CORAM_ADDR_LEN', addr_len),
                ('CORAM_DATA_WIDTH', data_width)),
               (('CLK', clk),
                ('ADDR', mem_addr),
                ('D', mem_wdata),
                ('WE', mem_wvalid),
                ('Q', mem_rdata)))

    m.Instance('CoramChannel', 'ch',
               (('CORAM_THREAD_NAME', 'ctrl_thread'),
                ('CORAM_THREAD_ID', 0),
                ('CORAM_ID', 0),
                ('CORAM_SUB_ID', 0),
                ('CORAM_ADDR_LEN', 4),
                ('CORAM_DATA_WIDTH', data_width)),
               (('CLK', clk),
                ('RST', rst),
                ('D', ch_wdata),
                ('ENQ', ch_enq),
                ('ALM_FULL', ch_almfull),
                ('Q', ch_rdata),
                ('DEQ', ch_deq),
                ('EMPTY', ch_empty)))

    # Finite State Machine
    fsm = lib.FSM(m, 'fsm')

    def mem_write(addr, wdata):
        return mem_addr(addr), mem_wdata(wdata), mem_wvalid(1)
    def mem_read_request(addr):
        return mem_addr(addr)
    def mem_read_data(rdata):
        return rdata(mem_rdata)

    read_count = m.Reg('read_count', width=32, initval=0)
    sum = m.Reg('sum', width=32, initval=0)
    size = m.Reg('size', width=32, initval=0)

    # building FSM
    fsm.goto_next()
    fsm.goto_next()
    start = fsm.current()

    fsm.add( ch_deq(1), cond=Not(ch_empty) )
    fsm.add( ch_deq(0), delay=1 )
    fsm.add( size(ch_rdata), delay=2 )
    fsm.goto_next()
    fsm.goto_next()
    
    fsm.add( mem_read_request(0), read_count.inc() )
    fsm.add( mem_read_data(sum), delay=2 )
    fsm.goto_next( cond=(read_count==size-1) )
    
    fsm.add( Systask('display', 'sum=%d', sum), delay=2)
    fsm.add( ch_enq(1), cond=Not(ch_almfull) )
    fsm.add( ch_enq(0), delay=1 )
    fsm.add( ch_wdata(sum) )
    
    fsm.goto(start)
    
    # building always statement
    m.Always(Posedge(clk))(
        If(rst)( m.reset(), fsm.reset()
        ).Else( fsm.to_case() ))
    
    return m

if __name__ == '__main__':
    userlogic = mkUserlogic()
    pycoram_modules = mkPycoram()
    verilog = ''.join([userlogic.to_verilog()] +
                      [p.to_verilog() for p in pycoram_modules.values()])
    print(verilog)
