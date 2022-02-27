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
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth, numports=2)

    axi_in = vthread.AXIStreamIn(m, 'axi_in', clk, rst, datawidth,
                                 with_last=True, noio=True)
    axi_out = vthread.AXIStreamOut(m, 'axi_out', clk, rst, datawidth,
                                   with_last=True, noio=True)

    maxi_in = vthread.AXIM_for_AXIStreamIn(axi_in, 'maxi_in')
    maxi_out = vthread.AXIM_for_AXIStreamOut(axi_out, 'maxi_out')

    all_ok = m.TmpReg(initval=0, prefix='all_ok')
    wdata = m.TmpReg(width=datawidth, initval=0, prefix='wdata')
    rdata0 = m.TmpReg(width=datawidth, initval=0, prefix='rdata0')
    rdata1 = m.TmpReg(width=datawidth, initval=0, prefix='rdata1')

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
        # write a test vector
        for i in range(size):
            wdata.value = i + 0x1000
            myram.write(i, wdata)

        laddr = 0
        gaddr = offset
        myaxi.dma_write(myram, laddr, gaddr, size, port=1)

        # AXI-stream read -> AXI-stream write
        maxi_in.dma_read_async(gaddr, size)

        out_gaddr = (size + size) * 4 + offset
        maxi_out.dma_write_async(out_gaddr, size)

        for i in range(size):
            va, va_last = axi_in.read()
            axi_out.write(va, va_last)

        maxi_out.dma_wait_write()

        # check
        myaxi.dma_read(myram, 0, gaddr, size, port=1)
        myaxi.dma_read(myram, size, out_gaddr, size, port=1)

        for i in range(size):
            rdata0.value = myram.read(i)
            rdata1.value = myram.read(i + size)
            if vthread.verilog.NotEql(rdata0, rdata1):
                print('rdata[%d] = %d (expected %d)' % (i, rdata1, rdata0))
                all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(77)

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

    memory = axi.AxiMultiportMemoryModel(m, 'memory', clk, rst, numports=3,
                                         memimg_name=memimg_name)
    memory.connect(0, ports, 'myaxi')
    memory.connect(1, ports, 'maxi_in')
    memory.connect(2, ports, 'maxi_out')

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
