from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import numpy as np

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi

axi_datawidth = 64
datawidth = 32

matrix_size = 16
a_offset = 0
b_offset = 4096
c_offset = 4096 * 2


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = 10
    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)

    maxi = vthread.AXIM(m, 'maxi', clk, rst, datawidth *
                        (axi_datawidth // datawidth))
    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, 32, length=8)

    def matmul():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy

            matrix_size = saxi.read(2)
            a_offset = saxi.read(3)
            b_offset = saxi.read(4)
            c_offset = saxi.read(5)
            comp(matrix_size, a_offset, b_offset, c_offset)

            saxi.write(1, 0)  # unset busy

    def comp(matrix_size, a_offset, b_offset, c_offset):
        a_addr, c_addr = a_offset, c_offset

        for i in range(matrix_size):
            maxi.dma_read(ram_a, 0, a_addr, matrix_size)

            b_addr = b_offset
            for j in range(matrix_size):
                maxi.dma_read(ram_b, 0, b_addr, matrix_size)

                sum = 0
                for k in range(matrix_size):
                    x = ram_a.read(k)
                    y = ram_b.read(k)
                    sum += x * y
                ram_c.write(j, sum)

                b_addr += matrix_size * (datawidth // 8)

            maxi.dma_write(ram_c, 0, c_addr, matrix_size)
            a_addr += matrix_size * (datawidth // 8)
            c_addr += matrix_size * (datawidth // 8)

    th = vthread.Thread(m, 'th_matmul', clk, rst, matmul)
    fsm = th.start()

    return m


def mkTest(memimg_name=None):

    a_shape = (matrix_size, matrix_size)
    b_shape = (matrix_size, matrix_size)
    c_shape = (a_shape[0], b_shape[0])

    n_raw_a = axi.shape_to_length(a_shape)
    n_raw_b = axi.shape_to_length(b_shape)

    n_a = axi.shape_to_memory_size(a_shape, datawidth)
    n_b = axi.shape_to_memory_size(b_shape, datawidth)

    a = np.zeros(a_shape, dtype=np.int64)
    b = np.zeros(b_shape, dtype=np.int64)

    value = 1
    for y in range(a_shape[0]):
        for x in range(a_shape[1]):
            if x == y:
                a[y][x] = value
                value += 1
            else:
                a[y][x] = 0

    for y in range(b_shape[0]):
        for x in range(b_shape[1]):
            if x == y:
                b[y][x] = 2
            else:
                b[y][x] = 0

    a_addr = a_offset
    size_a = n_a * datawidth // 8
    b_addr = b_offset
    size_b = n_b * datawidth // 8

    mem = np.zeros([1024 * 1024 * 8 // axi_datawidth], dtype=np.int64)
    axi.set_memory(mem, a, axi_datawidth, datawidth, a_addr)
    axi.set_memory(mem, b, axi_datawidth, datawidth, b_addr)

    led = mkLed()

    m = Module('test')
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)
    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst,
                                datawidth=axi_datawidth,
                                mem_datawidth=axi_datawidth,
                                memimg=mem, memimg_name=memimg_name)

    memory.connect(ports, 'maxi')

    # AXI-Slave controller
    _saxi = vthread.AXIMLite(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(ports, 'saxi')

    # Timer
    counter = m.Reg('counter', 32, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        counter.inc()
    )

    def ctrl():
        for i in range(100):
            pass

        awaddr = 2 * 4
        print('# matrix_size = %d' % matrix_size)
        _saxi.write(awaddr, matrix_size)

        awaddr = 3 * 4
        print('# a_offset = %d' % a_offset)
        _saxi.write(awaddr, a_offset)

        awaddr = 4 * 4
        print('# b_offset = %d' % b_offset)
        _saxi.write(awaddr, b_offset)

        awaddr = 5 * 4
        print('# c_offset = %d' % c_offset)
        _saxi.write(awaddr, c_offset)

        awaddr = 0 * 4
        start_time = counter
        print('# start time = %d' % start_time)
        _saxi.write(awaddr, 1)

        araddr = 1 * 4
        while True:
            busy = _saxi.read(araddr)
            if not busy:
                break

        end_time = counter
        print('# end time = %d' % end_time)
        time = end_time - start_time
        print('# exec time = %d' % time)

        all_ok = True
        for y in range(matrix_size):
            for x in range(matrix_size):
                v = memory.read(
                    c_offset + (y * matrix_size + x) * datawidth // 8)
                if y == x and vthread.verilog.NotEql(v, (y + 1) * 2):
                    all_ok = False
                    print("NG [%d,%d] = %d" % (y, x, v))
                if y != x and vthread.verilog.NotEql(v, 0):
                    all_ok = False
                    print("NG [%d,%d] = %d" % (y, x, v))

        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

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
