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

    # deep request FIFO
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth,
                         req_fifo_addrwidth=7)

    myram0 = vthread.RAM(m, 'myram0', clk, rst, datawidth, addrwidth)
    myram1 = vthread.RAM(m, 'myram1', clk, rst, datawidth, addrwidth)

    all_ok = m.TmpReg(initval=0, prefix='all_ok')
    wdata = m.TmpReg(width=datawidth, initval=0, prefix='wdata')
    rdata = m.TmpReg(width=datawidth, initval=0, prefix='rdata')
    rexpected = m.TmpReg(width=datawidth, initval=0, prefix='rexpected')

    num_transactions = 512

    def blink(size):
        all_ok.value = True

        for i in range(4):
            print('# iter %d start' % i)
            # Test for 4KB boundary check
            offset = i * 1024 * 16 + (myaxi.boundary_size - (datawidth // 8) * 3)
            body(size, offset)
            print('# iter %d end' % i)

        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    def body(size, offset):
        # write
        for i in range(size * num_transactions):
            wdata.value = i + 0x1000
            myram0.write(i, wdata)

        for i in range(num_transactions):
            laddr = size * i
            gaddr = size * i * 4 + offset
            myaxi.dma_write_async(myram0, laddr, gaddr, size)
            print('dma_write_async: [%d] -> [%d]' % (laddr, gaddr))

        myaxi.dma_wait()
        print('dma_wait')

        # write
        for i in range(size * num_transactions):
            wdata.value = i + 0x4000
            myram1.write(i, wdata)

        for i in range(num_transactions):
            laddr = size * i
            gaddr = size * num_transactions * 4 + size * i * 4 + offset
            myaxi.dma_write_async(myram1, laddr, gaddr, size)
            print('dma_write_async: [%d] -> [%d]' % (laddr, gaddr))

        myaxi.dma_wait()
        print('dma_wait')

        # read
        for i in range(num_transactions):
            laddr = size * i
            gaddr = size * i * 4 + offset
            myaxi.dma_read_async(myram1, laddr, gaddr, size)
            print('dma_read_async:  [%d] <- [%d]' % (laddr, gaddr))

        myaxi.dma_wait()
        print('dma_wait')

        for i in range(size * num_transactions):
            rdata.value = myram1.read(i)
            rexpected.value = i + 0x1000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        # read
        for i in range(num_transactions):
            laddr = size * i
            gaddr = size * num_transactions * 4 + size * i * 4 + offset
            myaxi.dma_read_async(myram0, laddr, gaddr, size)
            print('dma_read_async:  [%d] <- [%d]' % (laddr, gaddr))

        myaxi.dma_wait()
        print('dma_wait')

        for i in range(size * num_transactions):
            rdata.value = myram0.read(i)
            rexpected.value = i + 0x4000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(1)

    return m


def mkTest(memimg_name=None):
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    # fast memory
    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg_name=memimg_name,
                                write_delay=0, read_delay=10, req_fifo_addrwidth=7)
    memory.connect(ports, 'myaxi')

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000 * 2),
        Systask('finish'),
    )

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    if outputfile is None:
        outputfile = os.path.splitext(os.path.basename(__file__))[0] + '.out'

    memimg_name = 'memimg_' + outputfile

    test = mkTest(memimg_name=memimg_name)

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=outputfile)
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
