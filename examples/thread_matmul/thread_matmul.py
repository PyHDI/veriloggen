from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)

    def matmul(matrix_size, a_offset, b_offset, c_offset):
        comp(matrix_size, a_offset, b_offset, c_offset)
        check(matrix_size, a_offset, b_offset, c_offset)

    def comp(matrix_size, a_offset, b_offset, c_offset):
        a_addr, c_addr = a_offset, c_offset

        for i in range(matrix_size):
            ram_a.dma_read(myaxi, 0, a_addr, matrix_size)

            b_addr = b_offset
            for j in range(matrix_size):
                ram_b.dma_read(myaxi, 0, b_addr, matrix_size)

                sum = 0
                for k in range(matrix_size):
                    x = ram_a.read(k)
                    y = ram_b.read(k)
                    sum += x * y
                ram_c.write(j, sum)

                b_addr += matrix_size * (datawidth // 8)

            ram_c.dma_write(myaxi, 0, c_addr, matrix_size)
            a_addr += matrix_size * (datawidth // 8)
            c_addr += matrix_size * (datawidth // 8)

    def check(matrix_size, a_offset, b_offset, c_offset):
        all_ok = True
        c_addr = c_offset
        for i in range(matrix_size):
            ram_c.dma_read(myaxi, 0, c_addr, matrix_size)
            for j in range(matrix_size):
                v = ram_c.read(j)
                if i == j and v != (i + 1) * 2:
                    all_ok = False
                if i != j and v != 0:
                    all_ok = False
            c_addr += matrix_size * (datawidth // 8)

        if all_ok:
            print("OK")
        else:
            print("NG")

    th = vthread.Thread(m, 'th_matmul', clk, rst, matmul)
    fsm = th.start(16, 0, 1024, 2048)

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

    # memory image
    memname = 'mymem.out'

    def fwrite(f, value):
        s = '%08x' % value
        f.write('%s\n' % s[6:8])
        f.write('%s\n' % s[4:6])
        f.write('%s\n' % s[2:4])
        f.write('%s\n' % s[0:2])

    with open(memname, 'w') as f:
        # ram_a
        addr = 0
        nv = 1
        for x in range(16):
            for y in range(16):
                addr += 4
                if x == y:
                    value = nv
                    nv += 1
                else:
                    value = 0
                fwrite(f, value)

        for i in range(1024 - addr):
            f.write('%s\n' % '00')

        # ram_b
        addr = 1024
        for x in range(16):
            for y in range(16):
                addr += 4
                if x == y:
                    value = 2
                else:
                    value = 0
                fwrite(f, value)

        for i in range(2048 - addr):
            f.write('%s\n' % '00')

        # ram_c
        addr = 2048
        for x in range(16):
            for y in range(16):
                addr += 4
                value = 100
                fwrite(f, value)

        for i in range(2 ** 20 - addr):
            f.write('%s\n' % '00')

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg=memname)
    memory.connect(ports, 'myaxi')

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000),
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
