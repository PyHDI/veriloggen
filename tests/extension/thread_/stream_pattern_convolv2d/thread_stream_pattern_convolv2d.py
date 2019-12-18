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

    shape = [8, 10]
    size = functools.reduce(lambda x, y: x * y, shape, 1)

    ksize = [2, 2]
    klen = functools.reduce(lambda x, y: x * y, ksize, 1)

    stride = [2, 2]
    out_shape = [shape[0] // stride[0], shape[1] // stride[1]]
    out_size = functools.reduce(lambda x, y: x * y, out_shape, 1)

    # ((size, stride), (size, stride), ...)
    pattern_a = ((ksize[-1], 1), (ksize[-2], shape[-1]), (out_shape[-1], stride[-1]),
                 (out_shape[-2], stride[-2] * shape[-1]))
    pattern_b = ((klen, 1), (out_size, 0))

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a * b
    c, c_valid = strm.ReduceAddValid(c, ksize[0] * ksize[1])
    strm.sink(c, 'c', when=c_valid, when_name='c_valid')

    def comp_stream(offset):
        strm.set_source_pattern('a', ram_a, offset, pattern_a)
        strm.set_source_pattern('b', ram_b, offset, pattern_b)
        strm.set_sink('c', ram_c, offset, out_size)
        strm.run()
        strm.join()

    def comp_sequential(offset):
        sum = 0
        i = 0
        y = 0
        x = 0
        while y < shape[-2]:
            while x < shape[-1]:
                sum = 0
                for ky in range(ksize[-2]):
                    for kx in range(ksize[-1]):
                        a = ram_a.read(offset + (y + ky) * shape[-1] + x + kx)
                        b = ram_b.read(offset + ky * ksize[-1] + kx)
                        sum += a * b

                ram_c.write(offset + i, sum)
                i += 1
                x += stride[-1]

            x = 0
            y += stride[-2]

    def check(size, offset_stream, offset_seq):
        all_ok = True
        for i in range(size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
                print(i, st, sq)
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp():
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_stream(offset)
        myaxi.dma_write(ram_c, offset, 1024 * 4, out_size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_sequential(offset)
        myaxi.dma_write(ram_c, offset, 1024 * 8, out_size)

        # verification
        check(out_size, 0, offset)

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

    #simulation.setup_waveform(m, uut)
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
