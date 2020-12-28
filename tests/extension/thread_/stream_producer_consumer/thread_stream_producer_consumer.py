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

    # argmax
    argmaxstrm = vthread.Stream(m, 'argmax_stream', clk, rst)

    argmax_a = argmaxstrm.source('a')
    argmax_a_index = argmaxstrm.source('a_index')

    current_index = argmaxstrm.Consumer(initval=0)
    current_max = argmaxstrm.Consumer(initval=-1 * 2 ** 31)

    compare = current_max < argmax_a
    compare.latency = 0

    next_index = argmaxstrm.Mux(compare, argmax_a_index, current_index)
    next_index.latency = 0

    next_max = argmaxstrm.Mux(compare, argmax_a, current_max)
    next_max.latency = 0

    argmaxstrm.Producer(current_index, next_index)
    out_index = next_index

    argmaxstrm.Producer(current_max, next_max)

    argmaxstrm.sink(out_index, 'index')

    # main
    strm = vthread.Stream(m, 'mystream', clk, rst)

    a = strm.source('a')
    size = strm.parameter('size')
    a_index = strm.Counter(size=size)

    sub = strm.substream_multicycle(argmaxstrm)
    sub.to_source('a', a)
    sub.to_source('a_index', a_index)
    index = sub.from_sink('index')
    valid = a_index == size - 1

    strm.sink(index, 'index', when=valid, when_name='valid')

    def comp_stream(size, offset):
        strm.set_source('a', ram_a, offset, size)
        strm.set_parameter('size', size)
        strm.set_sink('index', ram_b, offset, 1)
        strm.run()
        strm.join()

    def comp_sequential(size, offset):
        index = 0
        _max = 0
        for i in range(size):
            a = ram_a.read(i + offset)
            if a > _max:
                index = i
                _max = a
        ram_b.write(offset, index)

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
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        ram_a.write(offset + 3, -100)
        ram_a.write(offset + 7, 200)
        comp_stream(size, offset)
        myaxi.dma_write(ram_b, offset, 1024, 1)

        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        ram_a.write(offset + 3, -100)
        ram_a.write(offset + 7, 200)
        comp_sequential(size, offset)
        myaxi.dma_write(ram_b, offset, 1024 * 2, 1)

        check(1, 0, offset)

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
