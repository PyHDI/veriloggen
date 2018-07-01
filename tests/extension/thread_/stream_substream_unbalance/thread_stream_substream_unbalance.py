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
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)
    ram_d = vthread.RAM(m, 'ram_d', clk, rst, datawidth, addrwidth)

    addsubstrm = vthread.Stream(m, 'addsub_stream', clk, rst)
    a = addsubstrm.source('a')
    b = addsubstrm.source('b')
    c = a + b
    d = a - b
    d += 1
    d -= 1
    addsubstrm.sink(c, 'c')
    addsubstrm.sink(d, 'd')

    strm = vthread.Stream(m, 'main_stream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    a += 1
    a -= 1
    sub = strm.substream(addsubstrm)
    sub.to_source('a', a)
    sub.to_source('b', b)
    c = sub.from_sink('c')
    d = sub.from_sink('d')
    c += 1
    c -= 1
    strm.sink(c, 'c')
    strm.sink(d, 'd')

    all_ok = m.TmpReg(initval=0)

    def comp_stream_addsub(size, offset):
        addsubstrm.set_source('a', ram_a, offset, size)
        addsubstrm.set_source('b', ram_b, offset, size)
        addsubstrm.set_sink('c', ram_c, offset, size)
        addsubstrm.set_sink('d', ram_d, offset, size)
        addsubstrm.run()
        addsubstrm.join()

    def comp_stream_main(size, offset):
        strm.set_source('a', ram_a, offset, size)
        strm.set_source('b', ram_b, offset, size)
        strm.set_sink('c', ram_c, offset, size)
        strm.set_sink('d', ram_d, offset, size)
        strm.run()
        strm.join()

    def comp_sequential_addsub(size, offset):
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            c = a + b
            d = a - b
            ram_c.write(i + offset, c)
            ram_d.write(i + offset, d)

    def comp_sequential_main(size, offset):
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            c = a + b
            d = a - b
            ram_c.write(i + offset, c)
            ram_d.write(i + offset, d)

    def check(size, offset_stream, offset_seq):
        for i in range(size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok.value = False
                print('c: %d %d %d' % (i, st, sq))
            st = ram_d.read(i + offset_stream)
            sq = ram_d.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok.value = False
                print('d: %d %d %d' % (i, st, sq))
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp(size):
        all_ok.value = True

        # addsub
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_stream_addsub(size, offset)
        myaxi.dma_write(ram_c, offset, 512, size)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_sequential_addsub(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 + 512, size)
        myaxi.dma_write(ram_c, offset, 1024 + 1024, size)

        # verification
        print('# addsub')
        check(size, 0, offset)

        # main
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_stream_main(size, offset)
        myaxi.dma_write(ram_c, offset, 512, size)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        comp_sequential_main(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 + 512, size)
        myaxi.dma_write(ram_c, offset, 1024 + 1024, size)

        # verification
        print('# main')
        check(size, 0, offset)

        vthread.finish()

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
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
