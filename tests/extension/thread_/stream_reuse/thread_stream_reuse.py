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
    reuse_size = 8

    def comp_stream(strm, size, offset):
        a0, a1 = strm.read_reuse(
            ram_a, offset, size, reuse_size=reuse_size, num_outputs=2)
        b0, b1 = strm.read_reuse(
            ram_b, offset, size, reuse_size=reuse_size, num_outputs=2)
        sum = a0 + a1 + b0 + b1
        strm.write(ram_c, offset, size * (reuse_size // 2), sum)

    def comp_sequential(size, offset):
        sum = 0
        w = 0
        for i in range(0, size, 2):
            for r in range(reuse_size):
                a0 = ram_a.read(i + 0 + offset)
                a1 = ram_a.read(i + 1 + offset)
                b0 = ram_b.read(i + 0 + offset)
                b1 = ram_b.read(i + 1 + offset)
                sum = a0 + a1 + b0 + b1
                ram_c.write(w + offset, sum)
                w += 1

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
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        stream.run(size, offset)
        stream.join()
        myaxi.dma_write(ram_c, offset, 1024, size)

        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 0, size)
        sequential.run(size, offset)
        sequential.join()
        myaxi.dma_write(ram_c, offset, 1024 * 2, size)

        check(size, 0, offset)

    stream = vthread.Stream(m, 'mystream', clk, rst, comp_stream)
    sequential = vthread.Thread(m, 'th_sequential', clk, rst, comp_sequential)

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
