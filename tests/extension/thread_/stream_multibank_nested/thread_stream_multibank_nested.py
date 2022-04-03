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


def mkLed(memory_datawidth=128):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    numbanks = 2
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, memory_datawidth)

    ram_a0 = vthread.MultibankRAM(m, 'ram_a0', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    ram_a1 = vthread.MultibankRAM(m, 'ram_a1', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    ram_a = vthread.to_multibank_ram((ram_a0, ram_a1), name='ram_a')

    ram_b0 = vthread.MultibankRAM(m, 'ram_b0', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    ram_b1 = vthread.MultibankRAM(m, 'ram_b1', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    ram_b = vthread.to_multibank_ram((ram_b0, ram_b1), name='ram_b')

    ram_c0 = vthread.MultibankRAM(m, 'ram_c0', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    ram_c1 = vthread.MultibankRAM(m, 'ram_c1', clk, rst, datawidth, addrwidth,
                                  numbanks=numbanks)
    ram_c = vthread.to_multibank_ram((ram_c0, ram_c1), name='ram_c')

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a + b
    strm.sink(c, 'c')

    def comp_stream(size, offset):
        strm.set_source('a', ram_a, offset, size)
        strm.set_source('b', ram_b, offset, size)
        strm.set_sink('c', ram_c, offset, size)
        strm.run()
        strm.join()

    def comp_sequential(size, offset):
        sum = 0
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            sum = a + b
            ram_c.write(i + offset, sum)

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
        dma_size = size
        comp_size = size

        dma_offset = 0
        comp_offset = 0
        myaxi.dma_read_packed(ram_a, dma_offset, 0, dma_size)
        myaxi.dma_read_packed(ram_b, dma_offset, 0, dma_size)
        comp_stream(size, comp_offset)
        myaxi.dma_write_packed(ram_c, dma_offset, 1024, dma_size)

        dma_offset = size
        comp_offset = comp_size
        myaxi.dma_read_packed(ram_a, dma_offset, 0, dma_size)
        myaxi.dma_read_packed(ram_b, dma_offset, 0, dma_size)
        comp_sequential(size, comp_offset)
        myaxi.dma_write_packed(ram_c, dma_offset, 1024 * 2, dma_size)

        check(comp_size, 0, comp_offset)

        vthread.finish()

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start(128)

    return m


def mkTest(memimg_name=None, memory_datawidth=128):
    m = Module('test')

    # target instance
    led = mkLed(memory_datawidth)

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memory_datawidth,
                                memimg_name=memimg_name)
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
