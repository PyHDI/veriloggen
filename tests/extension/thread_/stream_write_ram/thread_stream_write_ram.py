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

    ram_ext = vthread.RAM(m, 'ram_ext', clk, rst, datawidth, addrwidth, numports=2)
    ram_ext.disable_write(1)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    img_width = strm.parameter('img_width')

    counter = strm.Counter()

    a = strm.source('a')
    a_addr = strm.Counter()

    strm.write_RAM('write_ext', a_addr, a, when=counter < img_width)

    a_old_addr = strm.Counter() - img_width
    a_old = strm.read_RAM('read_ext', a_old_addr)

    b = a + a_old

    strm.sink(b, 'b', when=counter >= img_width)

    def comp_stream(size, offset):
        strm.set_source('a', ram_a, offset, size * 2)
        strm.set_sink('b', ram_b, offset, size)
        strm.set_parameter('img_width', size)
        strm.set_write_RAM('write_ext', ram_ext, port=0)
        strm.set_read_RAM('read_ext', ram_ext, port=1)
        strm.run()
        strm.join()

    def comp_sequential(size, offset):
        for i in range(size):
            a_buf = ram_a.read(i + offset)
            a = ram_a.read(i + offset + size)
            b = a_buf + a
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
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size * 2)
        comp_stream(size, offset)
        myaxi.dma_write(ram_b, offset, 1024, size)

        # sequential
        offset = size * 4
        myaxi.dma_read(ram_a, offset, 0, size * 2)
        comp_sequential(size, offset)
        myaxi.dma_write(ram_b, offset, 1024 * 2, size)

        # verification
        myaxi.dma_read(ram_b, 0, 1024, size)
        myaxi.dma_read(ram_b, offset, 1024 * 2, size)
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
