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


def mkLed(word_datawidth=128):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    num_words = word_datawidth // datawidth
    numbanks = 4

    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    myram0 = vthread.MultibankRAM(m, 'myram0', clk, rst, word_datawidth, addrwidth,
                                  numbanks=numbanks)
    myram1 = vthread.MultibankRAM(m, 'myram1', clk, rst, word_datawidth, addrwidth,
                                  numbanks=numbanks)

    all_ok = m.TmpReg(initval=0, prefix='all_ok')
    wdata = m.TmpReg(width=word_datawidth, initval=0, prefix='wdata')
    rdata = m.TmpReg(width=word_datawidth, initval=0, prefix='rdata')
    rvalue = m.TmpReg(width=datawidth, initval=0, prefix='rvalue')
    rexpected = m.TmpReg(width=datawidth, initval=0, prefix='rexpected')

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
        for i in range(size):
            wdata.value = 0
            for j in range(num_words):
                wdata.value = (wdata >> datawidth) | (
                    (i * num_words + 0x1000 + j) << (word_datawidth - datawidth))
            myram0.write(i, wdata)

        laddr = 0
        gaddr = offset
        myaxi.dma_write(myram0, laddr, gaddr, size)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # write
        for i in range(size):
            wdata.value = 0
            for j in range(num_words):
                wdata.value = (wdata >> datawidth) | (
                    (i * num_words + 0x4000 + j) << (word_datawidth - datawidth))
            myram1.write(i, wdata)

        laddr = 0
        gaddr = (size + size) * (word_datawidth // 8) + offset
        myaxi.dma_write(myram1, laddr, gaddr, size)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # read
        laddr = 0
        gaddr = offset
        myaxi.dma_read(myram1, laddr, gaddr, size)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata.value = myram1.read(i)
            for j in range(num_words):
                rvalue.value = rdata >> (datawidth * j)
                rexpected.value = i * num_words + 0x1000 + j
                if vthread.verilog.NotEql(rvalue, rexpected):
                    print('rdata[%d] = %d (expected %d)' % (i, rvalue, rexpected))
                    all_ok.value = False

        # read
        laddr = 0
        gaddr = (size + size) * (word_datawidth // 8) + offset
        myaxi.dma_read(myram0, laddr, gaddr, size)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata.value = myram0.read(i)
            for j in range(num_words):
                rvalue.value = rdata >> (datawidth * j)
                rexpected.value = i * num_words + 0x4000 + j
                if vthread.verilog.NotEql(rvalue, rexpected):
                    print('rdata[%d] = %d (expected %d)' % (i, rvalue, rexpected))
                    all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(17)

    return m


def mkTest(memimg_name=None, word_datawidth=128):
    m = Module('test')

    # target instance
    led = mkLed(word_datawidth)

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg_name=memimg_name)
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
