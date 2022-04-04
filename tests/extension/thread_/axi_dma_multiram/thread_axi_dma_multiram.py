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


def mkLed(memory_datawidth=128):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, memory_datawidth)
    myram0 = vthread.RAM(m, 'myram_0', clk, rst, datawidth, addrwidth)
    myram1 = vthread.RAM(m, 'myram_1', clk, rst, datawidth, addrwidth)
    myram2 = vthread.RAM(m, 'myram_2', clk, rst, datawidth, addrwidth)
    myram3 = vthread.RAM(m, 'myram_3', clk, rst, datawidth, addrwidth)

    all_ok = m.TmpReg(initval=0, prefix='all_ok')
    wdata = m.TmpReg(width=datawidth, initval=0, prefix='wdata')
    rdata = m.TmpReg(width=datawidth, initval=0, prefix='rdata')
    rexpected = m.TmpReg(width=datawidth, initval=0, prefix='rexpected')

    array_len = 256 + 128
    array_size = (array_len + array_len) * 4 * 4

    def blink(size):
        all_ok.value = True

        for i in range(2):
            print('# iter %d start' % i)
            # Test for 4KB boundary check
            offset = i * 1024 * 16 + (myaxi.boundary_size - (memory_datawidth // 8) * 3)
            body(size, offset)
            print('# iter %d end' % i)

        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    def body(size, offset):
        # narrow dma test
        myaxi.dma_read(myram0, 0, 0, size)
        myaxi.dma_read(myram1, 0, 0, size)
        myaxi.dma_read(myram2, 0, 0, size)
        myaxi.dma_read(myram3, 0, 0, size)
        myaxi.dma_write(myram0, 0, 0, size)
        myaxi.dma_write(myram1, 0, 0, size)
        myaxi.dma_write(myram2, 0, 0, size)
        myaxi.dma_write(myram3, 0, 0, size)

        # write
        for i in range(size):
            wdata.value = i + 0x1000
            myram0.write(i, wdata)

        for i in range(size):
            wdata.value = i + 0x2000
            myram1.write(i, wdata)

        for i in range(size):
            wdata.value = i + 0x3000
            myram2.write(i, wdata)

        for i in range(size):
            wdata.value = i + 0x4000
            myram3.write(i, wdata)

        laddr = 0
        gaddr = offset
        myaxi.dma_write_packed([myram0, myram1, myram2, myram3],
                               laddr, gaddr, size * 4)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # write
        for i in range(size):
            wdata = i + 0x5000
            myram0.write(i, wdata)

        for i in range(size):
            wdata = i + 0x6000
            myram1.write(i, wdata)

        for i in range(size):
            wdata = i + 0x7000
            myram2.write(i, wdata)

        for i in range(size):
            wdata = i + 0x8000
            myram3.write(i, wdata)

        laddr = 0
        gaddr = array_size + offset
        myaxi.dma_write_packed([myram0, myram1, myram2, myram3],
                               laddr, gaddr, size * 4)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # read
        laddr = 0
        gaddr = offset
        myaxi.dma_read_packed([myram0, myram1, myram2, myram3],
                              laddr, gaddr, size * 4)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata.value = myram0.read(i)
            rexpected.value = i + 0x1000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        for i in range(size):
            rdata.value = myram1.read(i)
            rexpected.value = i + 0x2000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        for i in range(size):
            rdata.value = myram2.read(i)
            rexpected.value = i + 0x3000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        for i in range(size):
            rdata.value = myram3.read(i)
            rexpected.value = i + 0x4000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        # read
        laddr = 0
        gaddr = array_size + offset
        myaxi.dma_read_packed([myram0, myram1, myram2, myram3],
                              laddr, gaddr, size * 4)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata.value = myram0.read(i)
            rexpected.value = i + 0x5000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        for i in range(size):
            rdata.value = myram1.read(i)
            rexpected.value = i + 0x6000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        for i in range(size):
            rdata.value = myram2.read(i)
            rexpected.value = i + 0x7000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

        for i in range(size):
            rdata.value = myram3.read(i)
            rexpected.value = i + 0x8000
            if vthread.verilog.NotEql(rdata, rexpected):
                print('rdata[%d] = %d (expected %d)' % (i, rdata, rexpected))
                all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(array_len)

    return m


def mkTest(memimg_name=None, memory_datawidth=128):
    m = Module('test')

    # target instance
    led = mkLed(memory_datawidth)

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memory_datawidth,
                                memimg_name=memimg_name)
    memory.connect(ports, 'myaxi')

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000),
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
