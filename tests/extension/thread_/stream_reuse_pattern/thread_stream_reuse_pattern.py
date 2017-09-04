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
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)

    shape = [4, 4, 4]
    size = functools.reduce(lambda x, y: x * y, shape, 1)
    order = [2, 1, 0]

    reuse_size = 4
    wshape = [4 * reuse_size, 4, 4]
    wsize = functools.reduce(lambda x, y: x * y, shape, 1)
    worder = [2, 1, 0]

    def to_pattern(shape, order):
        pattern = []
        for p in order:
            size = shape[p]
            stride = functools.reduce(lambda x, y: x * y,
                                      shape[:p], 1) if p > 0 else 1
            pattern.append((size, stride))
        return pattern

    pattern_a = to_pattern(shape, order)
    pattern_b = to_pattern(shape, order)
    pattern_c = to_pattern(wshape, worder)

    def comp_stream(strm, roffset, woffset):
        a = strm.read_reuse_pattern(
            ram_a, roffset, pattern_a, reuse_size=reuse_size)
        b = strm.read_reuse_pattern(
            ram_b, roffset, pattern_b, reuse_size=reuse_size)
        sum = a + b
        strm.write(ram_c, woffset, wsize * reuse_size, sum)

    def comp_sequential(roffset, woffset):
        sum = 0
        w = 0
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for r in range(reuse_size):
                        addr = i + j * shape[0] + k * (shape[0] * shape[1])
                        a = ram_a.read(addr + roffset)
                        b = ram_b.read(addr + roffset)
                        sum = a + b
                        ram_c.write(w + woffset, sum)
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

    def comp():
        roffset = 0
        woffset = 0
        myaxi.dma_read(ram_a, roffset, 0, size)
        myaxi.dma_read(ram_b, roffset, 0, size)
        stream.run(roffset, woffset)
        stream.join()
        myaxi.dma_write(ram_c, woffset, 1024, wsize)

        roffset = size
        woffset = size * (reuse_size // 2)
        myaxi.dma_read(ram_a, roffset, 0, size)
        myaxi.dma_read(ram_b, roffset, 0, size)
        sequential.run(roffset, woffset)
        sequential.join()
        myaxi.dma_write(ram_c, woffset, 1024 * 2, wsize)

        check(wsize, 0, woffset)

    stream = vthread.Stream(m, 'mystream', clk, rst, comp_stream)
    sequential = vthread.Thread(m, 'th_sequential', clk, rst, comp_sequential)

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start()

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
