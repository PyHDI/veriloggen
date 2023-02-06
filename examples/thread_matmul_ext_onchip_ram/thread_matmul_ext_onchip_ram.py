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

datawidth = 8
addrwidth = 8

matrix_size = 8
a_offset = 16
b_offset = a_offset + matrix_size * matrix_size
c_offset = b_offset + matrix_size * matrix_size


def mkLed():
    m = Module('user_module')
    clk = m.Input('clk')
    rst = m.Input('rst')
    start = m.Input('start')
    busy = m.OutputReg('busy', initval=0)

    ram = vthread.ExtRAM(m, 'ram', clk, rst, datawidth, addrwidth)

    def matmul():
        while True:
            wait()
            matrix_size = read_matrix_size()
            offset_a = read_matrix_a_offset()
            offset_b = read_matrix_b_offset()
            offset_c = read_matrix_c_offset()
            comp(matrix_size, offset_a, offset_b, offset_c)
            done()

    def wait():
        while not start:
            pass
        busy.value = 1

    def read_matrix_size():
        size0 = ram.read(0)
        size1 = ram.read(1)
        size = (size1 << 8) | size0
        return size

    def read_matrix_a_offset():
        offset0 = ram.read(4) & 0xff
        offset1 = ram.read(5) & 0xff
        offset = (offset1 << 8) | offset0
        return offset

    def read_matrix_b_offset():
        offset0 = ram.read(8) & 0xff
        offset1 = ram.read(9) & 0xff
        offset = (offset1 << 8) | offset0
        return offset

    def read_matrix_c_offset():
        offset0 = ram.read(12) & 0xff
        offset1 = ram.read(13) & 0xff
        offset = (offset1 << 8) | offset0
        return offset

    def comp(matrix_size, a_offset, b_offset, c_offset):
        a_addr, c_addr = a_offset, c_offset

        for i in range(matrix_size):
            b_addr = b_offset
            for j in range(matrix_size):
                sum = 0
                for k in range(matrix_size):
                    x = ram.read(a_addr + k)
                    y = ram.read(b_addr + k)
                    sum += x * y
                ram.write(c_addr + j, sum)

                b_addr += matrix_size * (datawidth // 8)

            a_addr += matrix_size * (datawidth // 8)
            c_addr += matrix_size * (datawidth // 8)

    def done():
        busy.value = 0

    th = vthread.Thread(m, 'th_matmul', clk, rst, matmul, datawidth=16)
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

    mem = np.zeros([2 ** addrwidth * (8 // datawidth)], dtype=np.int64)
    axi.set_memory(mem, a, datawidth, datawidth, a_addr)
    axi.set_memory(mem, b, datawidth, datawidth, b_addr)

    led = mkLed()

    m = Module('test')
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)
    clk = ports['clk']
    rst = ports['rst']

    start = ports['start']
    busy = ports['busy']

    start.initval = 0

    memory = vthread.RAM(m, 'memory', clk, rst, datawidth, addrwidth,
                         numports=2, initvals=mem.tolist())
    memory.connect_rtl(0, ports['ram_0_addr'], ports['ram_0_wdata'],
                       ports['ram_0_wenable'], ports['ram_0_rdata'],
                       ports['ram_0_enable'])

    # Timer
    counter = m.Reg('counter', 32, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        counter.inc()
    )

    def ctrl():
        for i in range(100):
            pass

        awaddr = 0
        v = (matrix_size & 0xff)
        print('# matrix_size[7:0] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 1
        v = ((matrix_size >> 8) & 0xff)
        print('# matrix_size[15:8] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 4
        v = (a_offset & 0xff)
        print('# a_offset[7:0] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 5
        v = ((a_offset >> 8) & 0xff)
        print('# a_offset[15:8] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 8
        v = (b_offset & 0xff)
        print('# b_offset[7:0] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 9
        v = ((b_offset >> 8) & 0xff)
        print('# b_offset[15:8] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 12
        v = (c_offset & 0xff)
        print('# c_offset[7:0] = %d' % v)
        memory.write(awaddr, v, port=1)

        awaddr = 13
        v = ((c_offset >> 8) & 0xff)
        print('# c_offset[15:8] = %d' % v)
        memory.write(awaddr, v, port=1)

        start_time = counter
        print('# start time = %d' % start_time)
        start.value = 1

        for _ in range(10):
            pass

        start.value = 0

        while True:
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
                    c_offset + (y * matrix_size + x) * datawidth // 8, port=1)
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

    # vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    # simulation.setup_waveform(m, uut, dumpfile=vcd_name)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000),
        Systask('finish'),
    )

    # return m

    # for VCD dump
    top = Module('top')
    uut = Submodule(top, m, name='test')

    vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    simulation.setup_waveform(top, uut, dumpfile=vcd_name)

    return top


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
