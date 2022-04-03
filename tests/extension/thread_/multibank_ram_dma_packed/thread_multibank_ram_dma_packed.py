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
    addrwidth = 4
    numbanks = 4
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, memory_datawidth)
    myram0 = vthread.MultibankRAM(m, 'myram0', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    myram1 = vthread.MultibankRAM(m, 'myram1', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)

    all_ok = m.TmpReg(initval=0, prefix='all_ok')
    wdata = m.TmpReg(width=datawidth, initval=0, prefix='wdata')
    rdata = m.TmpReg(width=datawidth, initval=0, prefix='rdata')
    rexpected = m.TmpReg(width=datawidth, initval=0, prefix='rexpected')

    array_len = 16
    array_size = (array_len + array_len) * 4 * numbanks

    laddr_offset = 32

    def blink(size):
        all_ok.value = True

        for i in range(4):
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
        # write
        ram_offset = laddr_offset // numbanks
        for bank in range(numbanks):
            for i in range(size):
                wdata.value = i + 0x1000 + (bank << 16)
                myram0.write_bank(bank, ram_offset + i, wdata)

        laddr = laddr_offset
        gaddr = offset
        myaxi.dma_write_packed(myram0, laddr, gaddr, size * numbanks)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # write
        ram_offset = laddr_offset // numbanks
        for bank in range(numbanks):
            for i in range(size):
                wdata.value = i + 0x4000 + (bank << 16)
                myram1.write_bank(bank, ram_offset + i, wdata)

        laddr = laddr_offset
        gaddr = array_size + offset
        myaxi.dma_write_packed(myram1, laddr, gaddr, size * numbanks)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # read
        laddr = laddr_offset
        gaddr = offset
        myaxi.dma_read_packed(myram1, laddr, gaddr, size * numbanks)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        ram_offset = laddr_offset // numbanks
        for bank in range(numbanks):
            for i in range(size):
                rdata.value = myram1.read_bank(bank, ram_offset + i)
                rexpected.value = i + 0x1000 + (bank << 16)
                if vthread.verilog.NotEql(rdata, rexpected):
                    print('rdata[%d:%d] = %d (expected %d)' % (bank, i, rdata, rexpected))
                    all_ok.value = False

        # read
        laddr = laddr_offset
        gaddr = array_size + offset
        myaxi.dma_read_packed(myram0, laddr, gaddr, size * numbanks)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        ram_offset = laddr_offset // numbanks
        for bank in range(numbanks):
            for i in range(size):
                rdata.value = myram0.read_bank(bank, ram_offset + i)
                rexpected.value = i + 0x4000 + (bank << 16)
                if vthread.verilog.NotEql(rdata, rexpected):
                    print('rdata[%d:%d] = %d (expected %d)' % (bank, i, rdata, rexpected))
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
