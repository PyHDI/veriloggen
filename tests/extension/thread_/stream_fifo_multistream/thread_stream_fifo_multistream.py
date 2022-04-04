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
    axi_in = vthread.AXIStreamInFifo(m, 'axi_in', clk, rst, datawidth,
                                     with_last=True, noio=True)
    maxi_in = vthread.AXIM_for_AXIStreamIn(axi_in, 'maxi_in')

    axi_out = vthread.AXIStreamOutFifo(m, 'axi_out', clk, rst, datawidth,
                                       with_last=True, noio=True)
    maxi_out = vthread.AXIM_for_AXIStreamOut(axi_out, 'maxi_out')

    fifo_addrwidth = 8
    fifo_a = vthread.FIFO(m, 'fifo_a', clk, rst, datawidth, fifo_addrwidth)
    fifo_b = vthread.FIFO(m, 'fifo_b', clk, rst, datawidth, fifo_addrwidth)
    fifo_c = vthread.FIFO(m, 'fifo_c', clk, rst, datawidth, fifo_addrwidth)

    # for comp_sequential
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)

    strm0 = vthread.Stream(m, 'mystream_reduce', clk, rst)
    a = strm0.source('a') + 10
    reduce_size = strm0.parameter('reduce_size')
    sum, sum_valid = strm0.ReduceAddValid(a, reduce_size)
    strm0.sink(sum, 'sum', when=sum_valid, when_name='sum_valid')

    strm1 = vthread.Stream(m, 'mystream_bias', clk, rst)
    x = strm1.source('x')
    y = strm1.source('y')
    z = x + y * 8 + 1
    strm1.sink(z, 'z')

    def comp_stream(size, reduce_size, offset):
        strm0.set_source_fifo('a', fifo_a, size)
        strm0.set_parameter('reduce_size', reduce_size)
        strm0.set_sink_fifo('sum', fifo_b, size // reduce_size)

        strm1.set_source_fifo('x', fifo_b, size // reduce_size)
        strm1.set_source('y', ram_b, 0, size // reduce_size)
        strm1.set_sink_fifo('z', fifo_c, size // reduce_size)

        strm0.run()
        strm1.run()

        # strm0.join()
        # strm1.join()

    def comp_sequential(size, reduce_size, offset):
        sum = 0
        reduce_count = 0
        write_addr = offset
        for i in range(size):
            a = ram_a.read(i + offset) + 10
            sum += a
            reduce_count += 1
            if reduce_count == reduce_size:
                y = ram_b.read(write_addr)
                sum += y * 8 + 1
                ram_c.write(write_addr, sum)
                write_addr += 1
                reduce_count = 0
                sum = 0

    def check(size, offset_stream, offset_seq):
        all_ok = True
        for i in range(size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp(size):
        # stream
        offset = 0
        reduce_size = 4

        # AXI-stream read -> FIFO -> Stream
        # fifo_a
        myaxi.dma_read(ram_b, offset, 0, size)
        maxi_in.dma_read_async(512, size)
        axi_in.dma_read_async(fifo_a, size)

        comp_stream(size, reduce_size, offset)

        # Stream -> FIFO -> AXI-stream write
        # fifo_c
        maxi_out.dma_write_async(1024, size // reduce_size)
        axi_out.dma_write_async(fifo_c, size // reduce_size)

        strm0.join()
        strm1.join()

        # sequential
        offset = size
        myaxi.dma_read(ram_b, offset, 0, size)
        myaxi.dma_read(ram_a, offset, 512, size)
        comp_sequential(size, reduce_size, offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size // reduce_size)

        # verification
        myaxi.dma_read(ram_c, 0, 1024, size // reduce_size)
        myaxi.dma_read(ram_c, offset, 1024 * 2, size // reduce_size)
        check(size // reduce_size, 0, offset)

        vthread.finish()

    th = vthread.Thread(m, 'comp', clk, rst, comp)
    fsm = th.start(32)

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
