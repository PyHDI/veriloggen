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

    shape = [4, 2, 8]
    size = functools.reduce(lambda x, y: x * y, shape, 1)
    read_order = [2, 1, 0]
    write_order = [0, 1, 2]

    def comp_stream(strm, offset):
        a = strm.read_multidim(ram_a, offset, shape, read_order)
        strm.write_multidim(ram_c, offset, a, shape, write_order)

    def comp_sequential(offset):
        zpos = 0
        ypos = 0
        xpos = 0
        for x in range(shape[0]):
            for y in range(shape[1]):
                for z in range(shape[2]):
                    a = ram_a.read(z * shape[0] * shape[1] +
                                   y * shape[0] + x + offset)
                    ram_c.write(zpos + ypos + xpos + offset, a)
                    xpos += 1
                    if xpos == shape[0]:
                        xpos = 0
                        ypos += shape[0]
                        if ypos == shape[1] * shape[0]:
                            ypos = 0
                            zpos += shape[1] * shape[0]

    def check(offset_stream, offset_seq):
        all_ok = True

        for i in range(size):
            st = ram_c.read(i + offset_stream)
            sq = ram_c.read(i + offset_seq)

            if st != sq:
                all_ok = False

        if all_ok:
            print('OK')
        else:
            print('NG')

    def comp():
        offset = 0
        ram_a.dma_read(myaxi, offset, 0, size)
        #ram_b.dma_read(myaxi, offset, 0, size)
        stream.run(offset)
        stream.join()
        ram_c.dma_write(myaxi, offset, 1024 * 4, size)

        offset = size
        ram_a.dma_read(myaxi, offset, 0, size)
        #ram_b.dma_read(myaxi, offset, 0, size)
        sequential.run(offset)
        sequential.join()
        ram_c.dma_write(myaxi, offset, 1024 * 8, size)

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
