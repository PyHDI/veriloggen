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

    incstrm = vthread.Stream(m, 'inc_stream', clk, rst)
    incstrm_a = incstrm.source('a')
    incstrm_b = incstrm.source('b')
    incstrm_const = incstrm.constant('const')
    incstrm_c = incstrm_a + incstrm_b + incstrm_const
    incstrm.sink(incstrm_c, 'c')

    strm = vthread.Stream(m, 'mystream', clk, rst)
    x = strm.source('x')
    y = strm.source('y')
    const = strm.constant('const')
    sub = strm.substream(incstrm)
    sub.to_source('a', x)
    sub.to_source('b', y)
    sub.to_constant('const', const)
    z = sub.from_sink('c')
    strm.sink(z, 'z')

    def comp_stream_inc(size, offset):
        incstrm.set_source('a', ram_a, offset, size)
        incstrm.set_source('b', ram_b, offset, size)
        incstrm.set_constant('const', 10)
        incstrm.set_sink('c', ram_c, offset, size)
        incstrm.run()
        incstrm.join()

    def comp_stream_main(size, offset):
        strm.set_source('x', ram_a, offset, size)
        strm.set_source('y', ram_b, offset, size)
        strm.set_constant('const', 100)
        strm.set_sink('z', ram_c, offset, size)
        strm.run()
        strm.join()

    def comp_sequential_inc(size, offset):
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            const = 10
            sum = a + b + const
            ram_c.write(i + offset, sum)

    def comp_sequential_main(size, offset):
        for i in range(size):
            x = ram_a.read(i + offset)
            y = ram_b.read(i + offset)
            const = 100
            sum = x + y + const
            ram_c.write(i + offset, sum)

    def check(size, offset_stream, offset_seq):
        all_ok = True
        for i in range(size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
                print(i, st, sq)
        if all_ok:
            print('OK')
        else:
            print('NG')

    def comp(size):
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_stream_inc(size, offset)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_sequential_inc(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size)

        # verification
        print('# INC')
        check(size, 0, offset)

        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_stream_main(size, offset)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_sequential_main(size, offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size)

        # verification
        print('# MAIN')
        check(size, 0, offset)

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start(32)

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst)
    memory.connect(ports, 'myaxi')

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(100000),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)
