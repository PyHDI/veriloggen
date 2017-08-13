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

    shape = [16, 4, 8]
    size = functools.reduce(lambda x, y: x * y, shape, 1)
    order = [2, 1, 0]

    def comp_stream(strm, offset):
        a = strm.read_multidim(ram_a, offset, shape, order)
        b = strm.read_multidim(ram_b, offset, shape, order)
        sum, valid = strm.RegionAdd(a * b, size)
        strm.write(ram_c, offset, 1, sum, when=valid)

    def comp_sequential(offset):
        sum = 0
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            sum += a * b
        ram_c.write(offset, sum)

    def check(offset_stream, offset_seq):
        all_ok = True
        st = ram_c.read(offset_stream)
        sq = ram_c.read(offset_seq)
        if vthread.verilog.NotEql(st, sq):
            all_ok = False

        if all_ok:
            print('OK')
        else:
            print('NG')

    def comp():
        offset = 0
        ram_a.dma_read(myaxi, offset, 0, size)
        ram_b.dma_read(myaxi, offset, 0, size)
        stream.run(offset)
        stream.join()
        ram_c.dma_write(myaxi, offset, 1024 * 4, 1)

        offset = size
        ram_a.dma_read(myaxi, offset, 0, size)
        ram_b.dma_read(myaxi, offset, 0, size)
        sequential.run(offset)
        sequential.join()
        ram_c.dma_write(myaxi, offset, 1024 * 8, 1)

        check(0, offset)

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
