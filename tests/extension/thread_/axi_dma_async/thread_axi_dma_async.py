from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10

    # With async DMA, set enable_async = True
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth, enable_async=True)
    # If RAM is simultaneously accesseed with DMA, numports must be 2 or more.
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth, numports=2)

    all_ok = m.TmpReg(initval=0)

    def blink(size):
        all_ok.value = True

        for i in range(4):
            print('# iter %d start' % i)
            offset = i * 1024 * 16
            body(size, offset)
            print('# iter %d end' % i)

        if all_ok:
            print('ALL OK')

    def body(size, offset):
        # write
        for i in range(size):
            wdata = i + 100
            myram.write(i, wdata)

        laddr = 0
        gaddr = offset
        # If RAM is simultaneously accesseed with DMA, different port must be
        # used.
        myaxi.dma_write_async(myram, laddr, gaddr, size, port=1)
        print('dma_write: [%d] -> [%d] async' % (laddr, gaddr))

        # write
        for i in range(size):
            wdata = i + 1000
            myram.write(i + size, wdata)

        myaxi.dma_wait()
        print('dma_wait:  [%d] -> [%d]' % (laddr, gaddr))

        laddr = size
        gaddr = (size + size) * 4 + offset
        myaxi.dma_write(myram, laddr, gaddr, size, port=1)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # read
        laddr = 0
        gaddr = offset
        myaxi.dma_read_async(myram, laddr, gaddr, size, port=1)
        print('dma_read:  [%d] <- [%d] async' % (laddr, gaddr))

        for sleep in range(size):
            pass

        myaxi.dma_wait()
        print('dma_wait:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata = myram.read(i)
            if vthread.verilog.NotEql(rdata, i + 100):
                print('rdata[%d] = %d' % (i, rdata))
                all_ok.value = False

        # read
        laddr = 0
        gaddr = (size + size) * 4 + offset
        myaxi.dma_read(myram, laddr, gaddr, size, port=1)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for sleep in range(size):
            pass

        for i in range(size):
            rdata = myram.read(i)
            if vthread.verilog.NotEql(rdata, i + 1000):
                print('rdata[%d] = %d' % (i, rdata))
                all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(16)

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst)
    memory.connect(ports, 'myaxi')

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(100000),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)
