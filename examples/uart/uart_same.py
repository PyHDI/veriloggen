from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *

def mkUartTx(baudrate=19200, clockfreq=100*1000*1000):
    m = Module("UartTx")
    waitnum = int(clockfreq / baudrate)
    
    clk = m.Input('CLK')
    rst = m.Input('RST')

    din = m.Input('din', 8)
    enable = m.Input('enable')
    ready = m.OutputReg('ready', initval=1)
    txd = m.OutputReg('txd', initval=1)

    fsm = FSM(m, 'fsm', clk, rst)

    mem = m.TmpReg(9, initval=0)
    waitcount = m.TmpReg(int(math.log(waitnum, 2)) + 1, initval=0)
    datacount = m.TmpReg(int(math.log(10, 2) + 1), initval=0)

    fsm(
        waitcount(waitnum-1),
        datacount(10),
        txd(1),
        mem(Cat(din, Int(0, 1)))
    )
    
    fsm.If(enable)(
        ready(0)
    )
    fsm.Then().goto_next()
    
    fsm.If(waitcount>0)(
        waitcount.dec()
    ).Else(
        txd(mem[0]),
        mem(Cat(Int(1, 1), mem[1:9])),
        waitcount(waitnum-1),
        datacount.dec()
    )

    fsm.Then().If(datacount==1)(
        ready(1)
    )

    fsm.Then().goto_init()

    fsm.make_always()
    
    return m

def mkUartRx(baudrate=19200, clockfreq=100*1000*1000):
    m = Module("UartRx")
    waitnum = int(clockfreq / baudrate)
    
    clk = m.Input('CLK')
    rst = m.Input('RST')

    rxd = m.Input('rxd')
    dout = m.OutputReg('dout', 8, initval=0)
    valid = m.OutputReg('valid', initval=0)

    fsm = FSM(m, 'fsm', clk, rst)

    mem = m.TmpReg(9, initval=0)
    waitcount = m.TmpReg(int(math.log(waitnum, 2)) + 1, initval=0)
    datacount = m.TmpReg(int(math.log(10, 2) + 1), initval=0)

    fsm(
        valid(0),
        waitcount(int(waitnum/2)-1),
        datacount(0),
        mem(Cat(rxd, mem[1:9]))
    )
    
    fsm.If(rxd==0).goto_next()

    # check the start bit again
    fsm.If(waitcount==0).If(datacount==0).If(rxd!=0).goto_init()
    
    fsm.If(waitcount>0)(
        waitcount.dec()
    ).Else(
        mem(Cat(rxd, mem[1:9])),
        waitcount(waitnum-1),
        datacount.inc()
    )

    fsm.Then().If(datacount==9).goto_next()

    fsm(
        valid(1),
        dout(mem[0:9])
    )
    
    fsm.goto_init()

    fsm.make_always()

    return m
    
def mkTest(baudrate=10*1000*1000):
    m = Module('test')
    
    mtx = mkUartTx(baudrate)
    mrx = mkUartRx(baudrate)

    clk = m.Reg('CLK')
    rst = m.Reg('RST')

    din = m.Reg('din', 8)
    enable = m.Reg('enable')
    ready = m.Wire('ready')
    txd = m.Wire('txd')

    dout = m.Wire('dout', 8)
    valid = m.Wire('valid')
    rxd = m.Wire('rxd')

    rxd.assign(txd)

    txfsm = FSM(m, 'txfsm', clk, rst)
    count = m.TmpReg(32, initval=0)

    send_data_list = (0x55, 0x33, 0x00, 0xff)

    for send_data in send_data_list:
        txfsm.add( din(send_data), enable(1), cond=ready)
        txfsm.goto_next(cond=ready)
        txfsm.add( enable(0) )
        txfsm.goto_next()
    
    txfsm.make_always()
    
    
    rxfsm = FSM(m, 'rxfsm', clk, rst)
    for send_data in send_data_list:
        check = Mux(send_data == dout, "OK", "NG")
        rxfsm.add(Systask('display', "din=%02x dout=%02x %s", Int(send_data, width=8), dout, check), cond=valid)
        rxfsm.goto_next(cond=valid)

    rxfsm.make_always()
    
    
    imtx = m.Instance(mtx, 'mtx',
                      params=m.connect_params(mtx),
                      ports=m.connect_ports(mtx))
    imrx = m.Instance(mrx, 'mrx',
                      params=m.connect_params(mrx),
                      ports=m.connect_ports(mrx))

    simulation.setup_waveform(m, imtx, imrx, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    nclk = simulation.next_clock
    
    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run() # display=False
    #rslt = sim.run(display=True)
    print(rslt)

    # launch waveform viewer (GTKwave)
    #sim.view_waveform() # background=False
    #sim.view_waveform(background=True)
