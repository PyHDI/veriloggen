import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *

def mkUserlogic():
    m = Module('userlogic')
    data_width = m.Parameter('DATA_WIDTH', 32)
    addr_len = m.Parameter('ADDR_LEN', 10)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    
    mem_addr = m.OutputReg('mem_addr', addr_len, initval=0)
    mem_wdata = m.OutputReg('mem_wdata', data_width, initval=0)
    mem_rdata = m.Input('mem_rdata', data_width)
    mem_wvalid = m.OutputReg('mem_wvalid', initval=0)
    mem_rvalid = m.OutputReg('mem_rvalid', initval=0)
    ch_wdata = m.OutputReg('ch_wdata', data_width, initval=0)
    ch_enq = m.OutputReg('ch_enq', initval=0)
    ch_almfull = m.Input('ch_almfull')
    ch_rdata = m.Input('ch_rdata', data_width)
    ch_deq = m.OutputReg('ch_deq', initval=0)
    ch_empty = m.Input('ch_empty')

    # Finite State Machine
    fsm = lib.FSM(m, 'fsm')

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
    fsm.goto_next(cond=Not(ch_empty))
    
    fsm.add( mem_addr( -Int(1) ))
    fsm.goto_next()
    
    fsm.add( mem_rvalid(1), mem_addr.inc(), read_count.inc() )
    fsm.add( mem_rvalid(0), delay=1 )
    fsm.add( sum.add(mem_rdata), delay=2 )
    fsm.goto_next( cond=(read_count==size-1) )
    
    fsm.add( Systask('display', 'sum=%d', sum), delay=2)
    fsm.add( ch_enq(1), cond=Not(ch_almfull) )
    fsm.add( ch_enq(0), delay=1 )
    fsm.add( ch_wdata(sum) )
    fsm.goto(start)
    
    # building always statement
    fsm.make_always(clk, rst, reset=m.make_reset())
    
    return m

def mkTest():
    m = Module('test')
    data_width = m.Parameter('DATA_WIDTH', 32)
    addr_len = m.Parameter('ADDR_LEN', 10)
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    mem_addr = m.Wire('mem_addr', addr_len)
    mem_wdata = m.Wire('mem_wdata', data_width)
    mem_rdata = m.Reg('mem_rdata', data_width, initval=0)
    mem_wvalid = m.Wire('mem_wvalid')
    mem_rvalid = m.Wire('mem_rvalid')
    ch_wdata = m.Wire('ch_wdata', data_width)
    ch_enq = m.Wire('ch_enq')
    ch_almfull = m.Reg('ch_almfull', initval=0)
    ch_rdata = m.Reg('ch_rdata', data_width, initval=0)
    ch_deq = m.Wire('ch_deq')
    ch_empty = m.Reg('ch_empty', initval=1)

    uut = m.Instance(mkUserlogic(), 'uut',
                     params=connect_same_name(data_width, addr_len),
                     ports=connect_same_name(clk, rst,
                                             mem_addr, mem_wdata, mem_rdata,
                                             mem_wvalid, mem_rvalid,
                                             ch_wdata, ch_enq, ch_almfull,
                                             ch_rdata, ch_deq, ch_empty))

    fsm = lib.FSM(m, 'test_fsm')
    lib.simulation.setup_waveform(m, uut, fsm.state)
    lib.simulation.setup_clock(m, clk, hperiod=5)
    init = lib.simulation.setup_reset(m, rst, m.make_reset(), period=100)

    #init.add(
    #    Delay(1000),
    #    Systask('finish'),
    #)

    for i in range(10):
        fsm.goto_next()
    
    fsm.add( ch_empty(0) )
    fsm.add( ch_rdata(10) )
    fsm.goto_next()
    
    fsm.add( ch_empty(1), cond=ch_deq)
    fsm.add( mem_rdata(0) )
    fsm.goto_next(cond=ch_deq)

    fsm.add( mem_rdata.inc(), cond=mem_rvalid, delay=1 )
    fsm.goto_next(cond=ch_enq)

    fsm.add( Systask('finish') )
    
    fsm.make_always(clk, rst)
    
    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)
