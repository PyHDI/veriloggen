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
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth, numports=2)

    # Read-Modify-Write
    rmwstrm = vthread.Stream(m, 'rmw_stream', clk, rst)
    numbins = rmwstrm.parameter('numbins')
    offset = rmwstrm.parameter('offset')
    a = rmwstrm.source('a')
    a = rmwstrm.Mux(a < 3, 3, a)
    a.latency = 0
    a = rmwstrm.Mux(a >= numbins, numbins - 1, a)
    a.latency = 0

    raddr = a + offset
    raddr.latency = 0
    rdata = rmwstrm.read_RAM('read_ram', raddr)
    wdata = rdata + 1
    wdata.latency = 0
    waddr = raddr
    out = rmwstrm.write_RAM('write_ram', waddr, wdata)
    rmwstrm.sink(out, 'out')

    # Main
    wrapstrm = vthread.Stream(m, 'wrap_stream', clk, rst)
    a = wrapstrm.source('a')
    numbins = wrapstrm.parameter('numbins')
    offset = wrapstrm.parameter('offset')
    sub = wrapstrm.substream_multicycle(rmwstrm)
    sub.to_source('a', a)
    sub.to_source('numbins', numbins)
    sub.to_source('offset', offset)
    out = sub.from_sink('out')
    wrapstrm.sink(out, 'out')

    def comp_stream(numbins, size, offset):
        for i in range(numbins):
            ram_b.write(i + offset, 0)

        wrapstrm.set_parameter('numbins', numbins)
        wrapstrm.set_parameter('offset', offset)
        wrapstrm.set_source('a', ram_a, offset, size)
        rmwstrm.set_read_RAM('read_ram', ram_b, port=0)
        rmwstrm.set_write_RAM('write_ram', ram_b, port=1)
        wrapstrm.run()
        wrapstrm.join()

    def comp_sequential(numbins, size, offset):
        for i in range(numbins):
            ram_b.write(i + offset, 0)

        for i in range(size):
            a = ram_a.read(i + offset)
            a = 3 if a < 3 else a
            a = numbins - 1 if a >= numbins else a
            current = ram_b.read(a + offset)
            updated = current + 1
            ram_b.write(a + offset, updated)

    def check(size, offset_stream, offset_seq):
        all_ok = True
        for i in range(size):
            st = ram_b.read(i + offset_stream)
            sq = ram_b.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok.value = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp(size):
        numbins = 8

        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        comp_stream(numbins, size, offset)
        myaxi.dma_write(ram_b, offset, 1024, numbins)

        # sequential
        offset = size * 4
        myaxi.dma_read(ram_a, offset, 0, size)
        comp_sequential(numbins, size, offset)
        myaxi.dma_write(ram_b, offset, 1024 * 2, numbins)

        # verification
        myaxi.dma_read(ram_b, 0, 1024, numbins)
        myaxi.dma_read(ram_b, offset, 1024 * 2, numbins)
        check(numbins, 0, offset)

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
