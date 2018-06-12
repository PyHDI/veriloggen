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
    offsets = (0, 16)
    sizes = (16, 16)
    strides = (1, 2)
    dma_size = 48

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a + b
    strm.sink(c, 'c')

    def comp_stream():
        strm.set_source_multipattern('a', ram_a, offsets, patterns)
        strm.set_source_multipattern('b', ram_b, offsets, patterns)
        strm.set_sink_multipattern('c', ram_c, offsets, patterns)
        strm.run()
        strm.join()

    def comp_sequential(global_offset):
        for i in range(sizes[0], strides[0]):
            a = ram_a.read(i + offsets[0] + global_offset)
            b = ram_b.read(i + offsets[0] + global_offset)
            sum = a + b
            ram_c.write(i + offsets[0] + global_offset, sum)
        for i in range(sizes[1], strides[1]):
            a = ram_a.read(i + offsets[1] + global_offset)
            b = ram_b.read(i + offsets[1] + global_offset)
            sum = a + b
            ram_c.write(i + offsets[1] + global_offset, sum)

    def check(bias, offset_stream, offset_seq):
        all_ok = True
        for i in range(sizes[0], strides[0]):
            st = ram_c.read(i + offset_stream + bias)
            sq = ram_c.read(i + offset_seq + bias)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        for i in range(sizes[1], strides[1]):
            st = ram_c.read(i + offset_stream + bias)
            sq = ram_c.read(i + offset_seq + bias)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp():
        # stream
        myaxi.dma_read(ram_a, offsets[0], 0, dma_size)
        myaxi.dma_read(ram_b, offsets[0], 0, dma_size)
        comp_stream()
        myaxi.dma_write(ram_c, offsets[0], 1024 * 4, 1)

        # sequential
        bias = dma_size
        myaxi.dma_read(ram_a, offsets[0], 0, dma_size)
        myaxi.dma_read(ram_b, offsets[0], 0, dma_size)
        comp_sequential(bias)
        myaxi.dma_write(ram_c, offsets[0], 1024 * 8, 1)

        # verification
        check(bias, 0, bias)

        vthread.finish()

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
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

    #simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(200000),
        Systask('finish'),
    )

    return m


def run(filename='tmp.v', simtype='iverilog'):

    test = mkTest()

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=simtype + '.out')
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
