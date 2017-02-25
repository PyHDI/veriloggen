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
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth)

    def blink():
        size = 256 * 2
        offset = 1024 * 4

        # write
        for i in range(size):
            wdata = i
            myram.write(i, wdata)

        laddr = 0
        gaddr = offset
        myram.dma_write(myaxi, laddr, gaddr, size)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # overwrite
        for i in range(size):
            wdata = 128
            myram.write(i, wdata)

        laddr = 0
        gaddr = offset + size * 4
        myram.dma_write(myaxi, laddr, gaddr, size)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # read
        all_ok = True

        laddr = 0
        gaddr = offset
        myram.dma_read(myaxi, laddr, gaddr, size)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata = myram.read(i)
            if rdata != i:
                print('rdata[%d] = %d' % (i, rdata))
                all_ok = False

        # read
        laddr = 0
        gaddr = offset + size * 4
        myram.dma_read(myaxi, laddr, gaddr, size)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata = myram.read(i)
            if rdata != 128:
                print('rdata[%d] = %d' % (i, rdata))
                all_ok = False

        if all_ok:
            print('ALL OK')

    th = vthread.Thread(m, clk, rst, 'th_blink', blink)
    fsm = th.start()

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
        Delay(200000),
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
