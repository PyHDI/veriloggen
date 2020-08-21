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

    axi_in = vthread.AXIStreamInFifo(m, 'axi_in', clk, rst, datawidth,
                                     with_last=True, noio=True)
    axi_out = vthread.AXIStreamOutFifo(m, 'axi_out', clk, rst, datawidth,
                                       with_last=True, noio=True)

    maxi_in = vthread.AXIM_for_AXIStreamIn(axi_in, 'maxi_in')
    maxi_out = vthread.AXIM_for_AXIStreamOut(axi_out, 'maxi_out')

    fifo_addrwidth = 8
    fifo_in = vthread.FIFO(m, 'fifo_in', clk, rst, datawidth, fifo_addrwidth)
    fifo_out = vthread.FIFO(m, 'fifo_out', clk, rst, datawidth, fifo_addrwidth)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = a + 1000
    strm.sink(b, 'b')

    all_ok = m.TmpReg(initval=0)

    def comp_stream(size):
        strm.set_source_fifo('a', fifo_in, size)
        strm.set_sink_fifo('b', fifo_out, size)
        strm.run()
        strm.join()

    def comp(size):
        offset = 0

        # write a test vector
        for i in range(size):
            wdata = i + 100
            myram.write(i, wdata)

        laddr = 0
        gaddr = offset
        myaxi.dma_write(myram, laddr, gaddr, size, port=1)

        # AXI-stream read -> FIFO -> Stream -> FIFO -> AXI-stream write
        maxi_in.dma_read_async(gaddr, size)
        axi_in.write_fifo(fifo_in, size)

        comp_stream(size)

        out_gaddr = (size + size) * (datawidth // 8) + offset
        maxi_out.dma_write_async(out_gaddr, size)
        axi_out.read_fifo(fifo_out, size)

        # check
        myaxi.dma_read(myram, 0, gaddr, size, port=1)
        myaxi.dma_read(myram, size, out_gaddr, size, port=1)

        for i in range(size):
            v0 = myram.read(i)
            v1 = myram.read(i + size)
            if vthread.verilog.NotEql(v0 + 1000, v1):
                all_ok.value = False

        vthread.finish()

    th = vthread.Thread(m, 'comp', clk, rst, comp)
    fsm = th.start(17)

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
