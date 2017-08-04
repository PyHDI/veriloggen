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

    size = 16
    kernel = 3
    stride = 1
    read_pattern = ((kernel, 1), (int(size // stride) - kernel + 1, stride))
    write_size = int(size // stride) - kernel + 1

    def comp_stream(strm, roffset, woffset):
        a = strm.read_pattern(ram_a, roffset, read_pattern)
        sum, valid = strm.RegionAdd(a, kernel)
        strm.write(ram_c, woffset, write_size, sum, when=valid)

    def comp_sequential(roffset, woffset):
        for i in range(0, size - kernel + 1, stride):
            sum = 0
            for k in range(kernel):
                a = ram_a.read(i + k + roffset)
                sum += a
            ram_c.write(i + woffset, sum)

    def check(offset_stream, offset_seq):
        all_ok = True

        for i in range(write_size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)

            if st != sq:
                all_ok = False

        if all_ok:
            print('OK')
        else:
            print('NG')

    def comp():
        roffset = 0
        woffset = 0
        ram_a.dma_read(myaxi, roffset, 0, size)
        stream.run(roffset, woffset)
        stream.join()
        ram_c.dma_write(myaxi, woffset, 1024 * 4, write_size)

        roffset = size
        woffset = write_size
        ram_a.dma_read(myaxi, roffset, 0, size)
        sequential.run(roffset, woffset)
        sequential.join()
        ram_c.dma_write(myaxi, woffset, 1024 * 8, write_size)

        check(0, woffset)

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
