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

    shape = [8, 2, 4]
    size = functools.reduce(lambda x, y: x * y, shape, 1)
    read_order = [0, 1, 2]
    write_order = [2, 1, 0]

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = a
    strm.sink(b, 'b')

    def comp_stream(offset):
        strm.set_source_multidim('a', ram_a, offset, shape, read_order)
        strm.set_sink_multidim('b', ram_b, offset, shape, write_order)
        strm.run()
        strm.join()

    def comp_sequential(offset):
        zpos = 0
        ypos = 0
        xpos = 0
        for x in range(shape[2]):
            for y in range(shape[1]):
                for z in range(shape[0]):
                    a = ram_a.read(z * shape[2] * shape[1] +
                                   y * shape[2] + x + offset)
                    ram_b.write(zpos + ypos + xpos + offset, a)
                    xpos += 1
                    if xpos == shape[2]:
                        xpos = 0
                        ypos += shape[2]
                        if ypos == shape[1] * shape[2]:
                            ypos = 0
                            zpos += shape[1] * shape[2]

    def check(offset_stream, offset_seq):
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

    def comp():
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        comp_stream(offset)
        myaxi.dma_write(ram_b, offset, 1024 * 4, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        comp_sequential(offset)
        myaxi.dma_write(ram_b, offset, 1024 * 8, size)

        # verification
        myaxi.dma_read(ram_b, 0, 1024 * 4, size)
        myaxi.dma_read(ram_b, offset, 1024 * 8, size)
        check(0, offset)

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
