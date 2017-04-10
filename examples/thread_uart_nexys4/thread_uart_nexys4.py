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


class UartTx(Submodule):
    __intrinsics__ = ('send', )

    def __init__(self, m, name, prefix, clk, rst, txd=None,
                 arg_params=None, arg_ports=None,
                 as_io=None, as_wire=None,
                 baudrate=19200, clockfreq=100 * 1000 * 1000):

        if arg_ports is None:
            arg_ports = []

        arg_ports.insert(0, ('CLK', clk))
        arg_ports.insert(1, ('RST', rst))

        if txd is not None:
            arg_ports.insert(2, ('txd', txd))

        moddef = mkUartTx(baudrate, clockfreq)

        Submodule.__init__(self, m, moddef, name, prefix,
                           arg_params=arg_params, arg_ports=arg_ports,
                           as_io=as_io, as_wire=as_wire)

        self.tx_din = self['din']
        self.tx_enable = self['enable']
        self.tx_enable.initval = 0
        self.tx_ready = self['ready']

    def send(self, fsm, value):
        fsm(
            self.tx_din(value),
            self.tx_enable(1)
        )
        fsm.goto_next()
        fsm(
            self.tx_enable(0)
        )
        fsm.goto_next()
        fsm.If(self.tx_ready).goto_next()


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


class UartRx(Submodule):
    __intrinsics__ = ('recv', )

    def __init__(self, m, name, prefix, clk, rst, rxd=None,
                 arg_params=None, arg_ports=None,
                 as_io=None, as_wire=None,
                 baudrate=19200, clockfreq=100 * 1000 * 1000):

        if arg_ports is None:
            arg_ports = []

        arg_ports.insert(0, ('CLK', clk))
        arg_ports.insert(1, ('RST', rst))

        if rxd is not None:
            arg_ports.insert(2, ('rxd', rxd))

        moddef = mkUartRx(baudrate, clockfreq)
        Submodule.__init__(self, m, moddef, name, prefix,
                           arg_params=arg_params, arg_ports=arg_ports,
                           as_io=as_io, as_wire=as_wire)

        self.rx_dout = self['dout']
        self.rx_valid = self['valid']

    def recv(self, fsm):
        ret = fsm.m.TmpReg(self.rx_dout.width)
        fsm.If(self.rx_valid)(
            ret(self.rx_dout)
        )
        fsm.Then().goto_next()
        return ret


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
    uart_tx = UartTx(m, 'inst_tx', 'tx_', clk, rst, tx,
                     baudrate=baudrate, clockfreq=clockfreq)
    uart_rx = UartRx(m, 'inst_rx', 'rx_', clk, rst, rx,
                     baudrate=baudrate, clockfreq=clockfreq)

    def blink():
        while True:
            c = uart_rx.recv()
            data = c + sw
            led.value = data
            uart_tx.send(data)

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start()

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

    uart_tx = UartTx(m, 'inst_tx', 'tx_', clk, rst, as_wire='txd',
                     baudrate=baudrate, clockfreq=clockfreq)
    uart_rx = UartRx(m, 'inst_rx', 'rx_', clk, rst, as_wire='rxd',
                     baudrate=baudrate, clockfreq=clockfreq)

    txd = uart_tx['txd']
    rxd = uart_rx['rxd']
    rx.assign(txd)
    rxd.assign(tx)

    simulation.setup_waveform(m, uut, uart_tx, uart_rx)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        sw(10),
        Delay(100000),
        Systask('finish')
    )

    def test():
        for i in range(10):
            s = 100 + i
            uart_tx.send(s)
            r = uart_rx.recv()
            if r == s + sw:
                print('OK: %d + %d == %d' % (s, sw, r))
            else:
                print('NG: %d + %d != %d' % (s, sw, r))

    th = vthread.Thread(m, 'test', clk, rst, test)
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
