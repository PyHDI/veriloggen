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
    ram_a = vthread.MultibankRAM(m, 'ram_a', clk, rst, datawidth, addrwidth,
                                 numbanks=numbanks)
    ram_b = vthread.MultibankRAM(m, 'ram_b', clk, rst, datawidth, addrwidth,
                                 numbanks=numbanks)
    ram_c = vthread.MultibankRAM(m, 'ram_c', clk, rst, datawidth, addrwidth,
                                 numbanks=numbanks)

    def comp_stream(strm, size, offset):
        a = strm.read_sequential(ram_a, offset, size)
        b = strm.read_sequential(ram_b, offset, size)
        sum = a + b
        strm.write_sequential(ram_c, offset, size, sum)

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
            print('OK')
        else:
            print('NG')

    def comp(size):
        dma_size = size
        comp_size = size * numbanks

        dma_offset = 0
        comp_offset = 0
        myaxi.dma_read(ram_a, dma_offset, 0, dma_size)
        myaxi.dma_read(ram_b, dma_offset, 0, dma_size)
        stream.run(comp_size, comp_offset)
        stream.join()
        myaxi.dma_write(ram_c, dma_offset, 1024, dma_size)

        dma_offset = size
        comp_offset = comp_size
        myaxi.dma_read(ram_a, dma_offset, 0, dma_size)
        myaxi.dma_read(ram_b, dma_offset, 0, dma_size)
        sequential.run(comp_size, comp_offset)
        sequential.join()
        myaxi.dma_write(ram_c, dma_offset, 1024 * 2, dma_size)

        check(comp_size, 0, comp_offset)

    stream = vthread.Stream(m, 'mystream', clk, rst, comp_stream)
    sequential = vthread.Thread(m, 'th_sequential', clk, rst, comp_sequential)

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start(32)

    return m


def mkTest(memory_datawidth=128):
    m = Module('test')

    # target instance
    led = mkLed(memory_datawidth)

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memory_datawidth)
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
