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

    strm = vthread.Stream(m, 'mystream', clk, rst)
    img_width = strm.parameter('img_width')

    counter = strm.Counter()

    a = strm.source('a')
    buf = strm.RingBuffer(a, length=128)

    a0 = a
    a1 = a0.prev(1)
    a2 = a1.prev(1)

    a3 = buf.read(-img_width)
    a4 = a3.prev(1)
    a5 = a4.prev(1)

    a6 = buf.read(-img_width - img_width)
    a7 = a6.prev(1)
    a8 = a7.prev(1)

    #b = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
    b = strm.AddN(a0, a1, a2, a3, a4, a5, a6, a7, a8)

    strm.sink(b, 'b', when=counter >= img_width + img_width + 2)

    def comp_stream(size, offset):
        strm.set_source('a', ram_a, offset, size * 3)
        strm.set_sink('b', ram_b, offset, size - 2)
        strm.set_parameter('img_width', size)
        strm.run()
        strm.join()

    def comp_sequential(size, offset):
        for i in range(size - 2):
            a0 = ram_a.read(i + offset)
            a1 = ram_a.read(i + offset + 1)
            a2 = ram_a.read(i + offset + 2)
            a3 = ram_a.read(i + offset + size)
            a4 = ram_a.read(i + offset + size + 1)
            a5 = ram_a.read(i + offset + size + 2)
            a6 = ram_a.read(i + offset + size + size)
            a7 = ram_a.read(i + offset + size + size + 1)
            a8 = ram_a.read(i + offset + size + size + 2)
            b = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
            ram_b.write(i + offset, b)

    def check(size, offset_stream, offset_seq):
        all_ok = True
        for i in range(size - 2):
            st = ram_b.read(i + offset_stream)
            sq = ram_b.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp(size):
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size * 3)
        comp_stream(size, offset)
        myaxi.dma_write(ram_b, offset, 1024, size)

        # sequential
        offset = size * 4
        myaxi.dma_read(ram_a, offset, 0, size * 3)
        comp_sequential(size, offset)
        myaxi.dma_write(ram_b, offset, 1024 * 2, size)

        # verification
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
