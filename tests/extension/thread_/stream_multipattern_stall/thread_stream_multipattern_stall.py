from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import functools

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi
import veriloggen.types.util as util


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)

    patterns = (((8, 1), (2, 8)),  # pattern 1
                ((8, 2), (2, 16)))  # pattern 2

    sizes = [functools.reduce(lambda x, y: x * y, [pat[0] for pat in pattern], 1)
             for pattern in patterns]
    strides = [pattern[0][1] for pattern in patterns]
    offsets = [0]
    i = 0
    for size, stride in zip(sizes[:-1], strides[:-1]):
        offsets.append(offsets[i] + size * stride)
        i += 1
    dma_size = functools.reduce(lambda x, y: x + y,
                                [size * stride for size, stride in zip(sizes, strides)])

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a + b
    strm.sink(c, 'c')

    # add a stall condition
    count = m.Reg('count', 4, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        count.inc()
    )

    util.add_disable_cond(strm.oready, 1, count == 0)

    def comp_stream():
        strm.set_source_multipattern('a', ram_a, offsets, patterns)
        strm.set_source_multipattern('b', ram_b, offsets, patterns)
        strm.set_sink_multipattern('c', ram_c, offsets, patterns)
        strm.run()
        strm.join()

    def comp_sequential(global_offset):
        addr = 0
        for i in range(sizes[0]):
            a = ram_a.read(addr + offsets[0] + global_offset)
            b = ram_b.read(addr + offsets[0] + global_offset)
            sum = a + b
            ram_c.write(addr + offsets[0] + global_offset, sum)
            addr += strides[0]

        addr = 0
        for i in range(sizes[1]):
            a = ram_a.read(addr + offsets[1] + global_offset)
            b = ram_b.read(addr + offsets[1] + global_offset)
            sum = a + b
            ram_c.write(addr + offsets[1] + global_offset, sum)
            addr += strides[1]

    def check(offset_stream, offset_seq):
        all_ok = True
        addr = 0
        for i in range(sizes[0]):
            st = ram_c.read(addr + offsets[0] + offset_stream)
            sq = ram_c.read(addr + offsets[0] + offset_seq)
            addr += strides[0]
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        addr = 0
        for i in range(sizes[1]):
            st = ram_c.read(addr + offsets[1] + offset_stream)
            sq = ram_c.read(addr + offsets[1] + offset_seq)
            addr += strides[1]
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp():
        # stream
        myaxi.dma_read(ram_a, 0, 0, dma_size)
        myaxi.dma_read(ram_b, 0, 0, dma_size)
        comp_stream()
        myaxi.dma_write(ram_c, 0, 1024 * 8, dma_size)

        # sequential
        myaxi.dma_read(ram_a, dma_size, 0, dma_size)
        myaxi.dma_read(ram_b, dma_size, 0, dma_size)
        comp_sequential(dma_size)
        myaxi.dma_write(ram_c, dma_size, 1024 * 12, dma_size)

        # verification
        myaxi.dma_read(ram_c, 0, 1024 * 8, dma_size)
        myaxi.dma_read(ram_c, dma_size, 1024 * 12, dma_size)
        check(0, dma_size)

        vthread.finish()

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start()

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

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg_name=memimg_name)
    memory.connect(ports, 'myaxi')

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(200000),
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
