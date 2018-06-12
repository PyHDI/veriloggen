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
from veriloggen.thread.uart import UartTx, UartRx


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

    all_ok = m.TmpReg(initval=0)

    def test():
        all_ok = True
        for i in range(10):
            s = 100 + i
            uart_tx.send(s)
            r = uart_rx.recv()
            if r == s + sw:
                print('OK: %d + %d == %d' % (s, sw, r))
            else:
                print('NG: %d + %d != %d' % (s, sw, r))

        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    th = vthread.Thread(m, 'test', clk, rst, test)
    th.start()

    return m


def run(filename='tmp.v', simtype='iverilog'):

    test = mkTest()

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=simtype + '.out')
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)

    # for Nexys4 synthesis
    top = mkTop()
    verilog = top.to_verilog('thread_uart_nexys4.v')
