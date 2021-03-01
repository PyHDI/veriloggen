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

    def addr_func(addr, z_offset, y_offset, x_offset, z, y, x, offset):
        next_addr = offset + z_offset + y_offset + x_offset

        next_x = Mux(x == shape[-1] - 1, 0, x + 1)
        next_y = Mux(Ands(y == shape[-2] - 1, x == shape[-1] - 1), 0,
                     Mux(x == shape[-1] - 1, y + 1, y))
        next_z = Mux(Ands(z == shape[-3] - 1, y == shape[-2] - 1, x == shape[-1] - 1), 0,
                     Mux(Ands(y == shape[-2] - 1, x == shape[-1] - 1), z + 1, z))

        next_x_offset = next_x
        next_y_offset = Mux(Ands(y == shape[-2] - 1, x == shape[-1] - 1), 0,
                            Mux(x == shape[-1] - 1, y_offset + shape[-1], y_offset))
        next_z_offset = Mux(Ands(z == shape[-3] - 1, y == shape[-2] - 1, x == shape[-1] - 1), 0,
                            Mux(Ands(y == shape[-2] - 1, x == shape[-1] - 1),
                                z_offset + shape[-2] * shape[-1], z_offset))

        last = Ands(z == 0, y == 0, x == 0)
        return last, next_addr, next_z_offset, next_y_offset, next_x_offset, next_z, next_y, next_x

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a + b
    strm.sink(c, 'c')

    def comp_stream(offset):
        strm.set_source_generator('a', ram_a,
                                  func=addr_func,
                                  initvals=(offset, 0, 0, 1, 0, 0, 1), args=(offset,))
        strm.set_source_generator('b', ram_b,
                                  func=addr_func,
                                  initvals=(offset, 0, 0, 1, 0, 0, 1), args=(offset,))
        strm.set_sink_generator('c', ram_c,
                                func=addr_func,
                                initvals=(offset, 0, 0, 1, 0, 0, 1), args=(offset,))
        strm.run()
        strm.join()

    def comp_sequential(offset):
        sum = 0
        for i in range(size):
            a = ram_a.read(i + offset)
            b = ram_b.read(i + offset)
            sum = a + b
            ram_c.write(i + offset, sum)

    def check(offset_stream, offset_seq):
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

    def comp():
        # stream
        offset = 0
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_stream(offset)
        myaxi.dma_write(ram_c, offset, 1024, size)

        # sequential
        offset = size
        myaxi.dma_read(ram_a, offset, 0, size)
        myaxi.dma_read(ram_b, offset, 512, size)
        comp_sequential(offset)
        myaxi.dma_write(ram_c, offset, 1024 * 2, size)

        # verification
        myaxi.dma_read(ram_c, 0, 1024, size)
        myaxi.dma_read(ram_c, offset, 1024 * 2, size)
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
        Delay(400000),
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
