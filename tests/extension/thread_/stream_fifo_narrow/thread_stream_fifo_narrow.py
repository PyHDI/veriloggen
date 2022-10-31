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


def mkLed(axi_datawidth=32, fifo_datawidth=64):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, axi_datawidth)

    axi_in = vthread.AXIStreamInFifo(m, 'axi_in', clk, rst, axi_datawidth,
                                     with_last=True, noio=True)
    maxi_in = vthread.AXIM_for_AXIStreamIn(axi_in, 'maxi_in')

    axi_out = vthread.AXIStreamOutFifo(m, 'axi_out', clk, rst, axi_datawidth,
                                       with_last=True, noio=True)
    maxi_out = vthread.AXIM_for_AXIStreamOut(axi_out, 'maxi_out')

    fifo_addrwidth = 8

    fifo_a = vthread.FIFO(m, 'fifo_a', clk, rst, fifo_datawidth, fifo_addrwidth)
    fifo_b = vthread.FIFO(m, 'fifo_b', clk, rst, fifo_datawidth, fifo_addrwidth)

    # for comp_sequential
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, fifo_datawidth, fifo_addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, fifo_datawidth, fifo_addrwidth)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = a * strm.Int(2)
    strm.sink(b, 'b')

    def comp_stream(size, offset):
        strm.set_source_fifo('a', fifo_a, size)
        strm.set_sink_fifo('b', fifo_b, size)
        strm.run()
        # strm.join()

    def comp_sequential(size, offset):
        for i in range(size):
            a = ram_a.read(i + offset)
            b = a * 2
            ram_b.write(i + offset, b)

    def check(size, offset_stream, offset_seq):
        all_ok = True
        for i in range(size):
            st = ram_b.read(i + offset_stream)
            sq = ram_b.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp(size):
        # initialization
        for i in range(size):
            ram_b.write(i, 1024 + i)

        myaxi.dma_write(ram_b, 0, 512, size)

        # stream
        offset = 0

        dma_size = size * fifo_datawidth // axi_datawidth

        # trial 1
        # AXI-stream read -> FIFO -> Stream
        # fifo_a
        maxi_in.dma_read_async(512, dma_size)
        axi_in.dma_read_async(fifo_a, size)

        comp_stream(size, offset)

        # Stream -> FIFO -> AXI-stream write
        # fifo_b
        maxi_out.dma_write_async(1024, dma_size)
        axi_out.dma_write_async(fifo_b, size)

        strm.join()

        # trial 2
        # AXI-stream read -> FIFO -> Stream
        # fifo_a
        maxi_in.dma_read_async(512, dma_size)
        axi_in.dma_read_async(fifo_a, size)

        comp_stream(size, offset)

        # Stream -> FIFO -> AXI-stream write
        # fifo_b
        maxi_out.dma_write_async(1024, dma_size)
        axi_out.dma_write_async(fifo_b, size)

        strm.join()

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 512, size)
        comp_sequential(size, offset)
        myaxi.dma_write(ram_b, offset, 1024 * 2, size)

        # verification
        myaxi.dma_read(ram_b, 0, 1024, size)
        myaxi.dma_read(ram_b, offset, 1024 * 2, size)
        check(size, 0, offset)

        vthread.finish()

    th = vthread.Thread(m, 'comp', clk, rst, comp)
    fsm = th.start(16)

    return m


def mkTest(memimg_name=None, axi_datawidth=32, fifo_datawidth=64):
    m = Module('test')

    # target instance
    led = mkLed(axi_datawidth, fifo_datawidth)

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMultiportMemoryModel(m, 'memory', clk, rst, axi_datawidth, numports=3,
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
