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
    point = 4
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    ram_a = vthread.FixedRAM(m, 'ram_a', clk, rst, datawidth, addrwidth,
                             point=point)
    ram_b = vthread.FixedRAM(m, 'ram_b', clk, rst, datawidth, addrwidth,
                             point=-point)
    ram_c = vthread.FixedRAM(m, 'ram_c', clk, rst, datawidth, addrwidth,
                             point=point)

    strm = vthread.Stream(m, 'mystream', clk, rst, dump=True)
    a = strm.source('a', point=point)
    b = strm.source('b', point=-point)
    const = strm.parameter('const', point=point)
    c = a * b + const
    strm.sink(c, 'c')

    def comp_stream(size, offset):
        strm.set_source('a', ram_a, offset, size)
        strm.set_source('b', ram_b, offset, size)
        strm.set_sink('c', ram_c, offset, size)
        const = vthread.fixed.FixedConst(10, point=point)
        strm.set_parameter('const', const)
        strm.run()
        strm.join()

    def comp_sequential(size, offset):
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            const = vthread.fixed.FixedConst(10, point=point)
            c = a * b + const
            ram_c.write(i + offset, c)
            print('a = %10g, b = %10g, const = %10g, c =  %10g' % (a, b, const, c))

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
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_stream(size, offset)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_sequential(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size)

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
