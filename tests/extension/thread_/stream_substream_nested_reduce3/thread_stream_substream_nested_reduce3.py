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
    reduce_size = 4

    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)
    ram_d = vthread.RAM(m, 'ram_d', clk, rst, datawidth, addrwidth)

    macstrm = vthread.Stream(m, 'macstream', clk, rst)
    macstrm_a = macstrm.source('a')
    macstrm_b = macstrm.source('b')
    macstrm_const = macstrm.parameter('const')
    macstrm_mul = macstrm_a * macstrm_b
    macstrm_c, macstrm_v = macstrm.ReduceAddValid(macstrm_mul, macstrm_const)
    macstrm.sink(macstrm_c, 'c')
    macstrm.sink(macstrm_v, 'v')

    macstrm2 = vthread.Stream(m, 'macstream2', clk, rst)
    macstrm2_a = macstrm2.source('a')
    macstrm2_b = macstrm2.source('b')
    macstrm2_const = macstrm2.parameter('const')
    macstrm2_a = macstrm2_a + 1
    macstrm2_a = macstrm2_a - 1
    macstrm2_b = macstrm2_b * 1
    macsub = macstrm2.substream(macstrm)
    macsub.to_source('a', macstrm2_a)
    macsub.to_source('b', macstrm2_b)
    macsub.to_parameter('const', macstrm2_const)
    macstrm2_c = macsub.from_sink('c')
    macstrm2_v = macsub.from_sink('v')
    macstrm2.sink(macstrm2_c, 'c')
    macstrm2.sink(macstrm2_v, 'v')

    neststrm = vthread.Stream(m, 'neststream', clk, rst)
    neststrm_a = neststrm.source('a')
    neststrm_b = neststrm.source('b')
    neststrm_const = neststrm.parameter('const')
    neststrm_a += 1
    neststrm_a += 0
    neststrm_b += 1
    macsub = neststrm.substream(macstrm2)
    macsub.to_source('a', neststrm_a)
    macsub.to_source('b', neststrm_b)
    macsub.to_parameter('const', neststrm_const)
    neststrm_c = macsub.from_sink('c')
    neststrm_c += neststrm_a
    neststrm_c += 0
    neststrm_v = macsub.from_sink('v')
    neststrm.sink(neststrm_c, 'c')
    neststrm.sink(neststrm_v, 'v')

    strm = vthread.Stream(m, 'mystream', clk, rst)
    x = strm.source('x')
    y = strm.source('y')
    const = strm.parameter('const')
    sub = strm.substream(neststrm)
    sub.to_source('a', x)
    sub.to_source('b', y)
    sub.to_parameter('const', const)
    z = sub.from_sink('c')
    v = sub.from_sink('v')
    z = z + y
    strm.sink(z, 'z', when=v, when_name='v')

    all_ok = m.TmpReg(initval=0)

    def comp_stream_macstrm(size, offset):
        macstrm2.set_source('a', ram_a, offset, size)
        macstrm2.set_source('b', ram_b, offset, size)
        macstrm2.set_parameter('const', reduce_size)
        macstrm2.set_sink('c', ram_c, offset, size)
        macstrm2.set_sink('v', ram_d, offset, size)
        macstrm2.run()
        macstrm2.join()

    def comp_stream_mystrm(size, offset):
        strm.set_source('x', ram_a, offset, size)
        strm.set_source('y', ram_b, offset, size)
        strm.set_parameter('const', reduce_size)
        strm.set_sink('z', ram_c, offset, size // reduce_size)
        strm.run()
        strm.join()

    def comp_sequential_macstrm(size, offset):
        sum = 0
        count = 0
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            sum += a * b
            count += 1
            ram_c.write(i + offset, sum)
            ram_d.write(i + offset, count == (reduce_size - 1))
            if count == reduce_size:
                sum = 0
                count = 0

    def comp_sequential_mystrm(size, offset):
        sum = 0
        count = 0
        write_offset = offset
        for i in range(size):
            x = ram_a.read(i + offset)
            y = ram_b.read(i + offset)
            sum += (x + 1) * (y + 1)
            val = sum + (x + 1) + y
            count += 1
            if count == reduce_size:
                ram_c.write(write_offset, val)
                write_offset += 1
                sum = 0
                count = 0

    def check(size, offset_stream, offset_seq):
        for i in range(size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok.value = False
                print(i, st, sq)
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp(size):
        all_ok.value = True

        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_stream_macstrm(size, offset)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_sequential_macstrm(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size)

        # verification
        print('# macstream')
        check(size, 0, offset)

        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_stream_mystrm(size, offset)
        myaxi.dma_write(ram_c, offset, 1024, size // reduce_size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_sequential_mystrm(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size // reduce_size)

        # verification
        print('# mystream')
        check(size // reduce_size, 0, offset)

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start(16)

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
