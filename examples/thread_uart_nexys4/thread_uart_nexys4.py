from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.thread as vthread


def mkTop(clk_name='clk', rst_name='btnCpuReset'):
    m = Module('top')
    clk = m.Input(clk_name)
    rst = m.Input(rst_name)
    RsRx = m.Input('RsRx')
    RsTx = m.Output('RsTx')
    RsCts = m.Output('RsCts')
    RsRts = m.Input('RsRts')
    RsCts.assign(0)

    new_clk = m.Wire('new_CLK')
    new_clk.assign(clk)

    rstbuf = m.Reg('RST_X')
    new_rst = m.Reg('RST')
    m.Always(Posedge(clk))(
        rstbuf(rst),
        new_rst(Not(rstbuf))
    )

    blinkled = mkLed()

    ports = []
    ports.append(('CLK', new_clk))
    ports.append(('RST', new_rst))
    ports.append(('utx', RsTx))
    ports.append(('urx', RsRx))
    sub = Submodule(m, blinkled, name='inst_' + blinkled.name,
                    arg_ports=ports,
                    as_io=('sw', 'led'), as_wire=('utx', 'urx'))

    return m


def mkLed(baudrate=19200, clockfreq=100 * 1000 * 1000):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    sw = m.Input('sw', 16)
    led = m.OutputReg('led', 16, initval=0)

    tx = m.Output('utx')
    rx = m.Input('urx')

    uart_tx = Submodule(m, mkUartTx(baudrate, clockfreq), 'inst_tx', 'tx_',
                        arg_ports=(('CLK', clk), ('RST', rst), ('txd', tx)))
    uart_rx = Submodule(m, mkUartRx(baudrate, clockfreq), 'inst_rx', 'rx_',
                        arg_ports=(('CLK', clk), ('RST', rst), ('rxd', rx)))

    tx_din = uart_tx['din']
    tx_enable = uart_tx['enable']
    tx_enable.initval = 0
    tx_ready = uart_tx['ready']

    rx_dout = uart_rx['dout']
    rx_valid = uart_rx['valid']

    def send(fsm, value):
        fsm(
            tx_din(value),
            tx_enable(1)
        )
        fsm.goto_next()
        fsm(
            tx_enable(0)
        )
        fsm.goto_next()
        fsm.If(tx_ready).goto_next()

    def recv(fsm):
        ret = fsm.m.TmpReg(rx_dout.width)
        fsm.If(rx_valid)(
            ret(rx_dout)
        )
        fsm.Then().goto_next()
        return ret

    def blink():
        while True:
            c = recv()
            data = c + sw
            led.value = data
            send(data)

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    th.add_intrinsics(send, recv)
    fsm = th.start()

    return m


def mkUartTx(baudrate=19200, clockfreq=100 * 1000 * 1000):
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

    fsm(
        waitcount(waitnum - 1),
        txd(1),
        mem(Cat(din, Int(0, 1)))
    )

    fsm.If(enable)(
        ready(0)
    )

    fsm.Then().goto_next()

    for i in range(10):
        fsm.If(waitcount > 0)(
            waitcount.dec()
        ).Else(
            txd(mem[0]),
            mem(Cat(Int(1, 1), mem[1:9])),
            waitcount(waitnum - 1)
        )
        fsm.Then().goto_next()

    fsm(
        ready(1)
    )

    fsm.goto_init()

    fsm.make_always()

    return m


def mkUartRx(baudrate=19200, clockfreq=100 * 1000 * 1000):
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

    fsm(
        valid(0),
        waitcount(int(waitnum / 2) - 1),
        mem(Cat(rxd, mem[1:9]))
    )

    fsm.If(rxd == 0).goto_next()

    for i in range(10):
        if i == 0:  # check the start bit again
            fsm.If(Ands(waitcount == 1, rxd != 0)).goto_init()

        fsm.If(waitcount > 0)(
            waitcount.dec()
        ).Else(
            mem(Cat(rxd, mem[1:9])),
            waitcount(waitnum - 1)
        )
        fsm.Then().goto_next()

    fsm(
        valid(1),
        dout(mem[0:9])
    )

    fsm.goto_init()

    fsm.make_always()

    return m


def mkTest(baudrate=19200, clockfreq=19200 * 10):
    m = Module('test')

    # target instance
    led = mkLed(baudrate, clockfreq)

    uut = Submodule(m, led, name='uut', as_wire=('utx', 'urx'))
    clk = uut['CLK']
    rst = uut['RST']
    tx = uut['utx']
    rx = uut['urx']
    sw = uut['sw']

    uart_tx = Submodule(m, mkUartTx(baudrate, clockfreq), 'inst_tx', 'tx_',
                        arg_ports=(('CLK', clk), ('RST', rst)), as_wire='txd')
    uart_rx = Submodule(m, mkUartRx(baudrate, clockfreq), 'inst_rx', 'rx_',
                        arg_ports=(('CLK', clk), ('RST', rst)), as_wire='rxd')
    txd = uart_tx['txd']
    rxd = uart_rx['rxd']
    rx.assign(txd)
    rxd.assign(tx)

    tx_din = uart_tx['din']
    tx_enable = uart_tx['enable']
    tx_enable.initval = 0
    tx_ready = uart_tx['ready']

    rx_dout = uart_rx['dout']
    rx_valid = uart_rx['valid']

    simulation.setup_waveform(m, uut, uart_tx, uart_rx)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        sw(10),
        Delay(100000),
        Systask('finish')
    )

    def send(fsm, value):
        fsm(
            tx_din(value),
            tx_enable(1)
        )
        fsm.goto_next()
        fsm(
            tx_enable(0)
        )
        fsm.goto_next()
        fsm.If(tx_ready).goto_next()

    def recv(fsm):
        ret = fsm.m.TmpReg(rx_dout.width)
        fsm.If(rx_valid)(
            ret(rx_dout)
        )
        fsm.Then().goto_next()
        return ret

    def test():
        for i in range(10):
            s = 100 + i
            send(s)
            r = recv()
            if r == s + sw:
                print('OK: %d + %d == %d' % (s, sw, r))
            else:
                print('NG: %d + %d != %d' % (s, sw, r))

    th = vthread.Thread(m, 'test', clk, rst, test)
    th.add_intrinsics(send, recv)
    th.start()

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # for Nexys4 synthesis
    top = mkTop()
    verilog = top.to_verilog('thread_uart_nexys4.v')
