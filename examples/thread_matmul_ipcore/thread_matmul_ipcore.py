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
import veriloggen.types.ipcore as ipcore

axi_wordsize = 4
data_wordsize = 4

matrix_size = 16
a_offset = 0
b_offset = 4096
c_offset = 4096 * 2


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('led', 8, initval=0)

    datawidth = 32
    addrwidth = 10

    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)
    ram_c = vthread.RAM(m, 'ram_c', clk, rst, datawidth, addrwidth)

    maxi = vthread.AXIM(m, 'maxi', clk, rst, datawidth)
    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth, length=8)

    def matmul():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            matrix_size = saxi.read(1)
            a_offset = saxi.read(2)
            b_offset = saxi.read(3)
            c_offset = saxi.read(4)
            comp(matrix_size, a_offset, b_offset, c_offset)
            saxi.write_flag(5, 1, resetvalue=0)

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


def mkTest():

    a_shape = (matrix_size, matrix_size)
    b_shape = (matrix_size, matrix_size)
    c_shape = (a_shape[0], b_shape[0])

    n_raw_a = axi.shape_to_length(a_shape)
    n_raw_b = axi.shape_to_length(b_shape)

    n_a = axi.memory_word_length(a_shape, data_wordsize)
    n_b = axi.memory_word_length(b_shape, data_wordsize)

    #a = np.arange(n_raw_a, dtype=np.int32).reshape(a_shape)
    #b = np.arange(n_raw_b, dtype=np.int32).reshape(b_shape) + [n_a]
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
    size_a = n_a * data_wordsize
    b_addr = b_offset
    size_b = n_b * data_wordsize

    mem = np.zeros([1024 * 1024 // axi_wordsize], dtype=np.int64)
    axi.set_memory(mem, a, axi_wordsize, data_wordsize, a_addr)
    axi.set_memory(mem, b, axi_wordsize, data_wordsize, b_addr)

    led = mkLed()

    m = Module('test')
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)
    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg=mem,
                                mem_datawidth=8 * axi_wordsize)
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

        awaddr = 4
        print('# matrix_size = %d' % matrix_size)
        _saxi.write(awaddr, matrix_size)

        awaddr = 8
        print('# a_offset = %d' % a_offset)
        _saxi.write(awaddr, a_offset)

        awaddr = 12
        print('# b_offset = %d' % b_offset)
        _saxi.write(awaddr, b_offset)

        awaddr = 16
        print('# c_offset = %d' % c_offset)
        _saxi.write(awaddr, c_offset)

        awaddr = 0
        start_time = counter
        print('# start time = %d' % start_time)
        _saxi.write(awaddr, 1)

        araddr = 20
        v = _saxi.read(araddr)
        while v == 0:
            v = _saxi.read(araddr)

        end_time = counter
        print('# end time = %d' % end_time)
        time = end_time - start_time
        print('# exec time = %d' % time)

        all_ok = True
        for y in range(matrix_size):
            for x in range(matrix_size):
                v = memory.read(
                    c_offset + (y * matrix_size + x) * data_wordsize)
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


def run(filename='tmp.v', simtype='iverilog'):

    test = mkTest()

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=simtype + '.out')
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)

    memname = '_memory_memimg_.out'
    simcode = """
reg [31:0] counter;
always @(posedge sim_clk) begin
  if(!sim_resetn) begin
    counter <= 0;
  end else begin
    counter <= counter + 1;
  end
end

reg [31:0] _start_time;
reg [31:0] _end_time;
reg [31:0] _time;

reg [31:0] _addr;
reg [31:0] _data;
initial begin
  #1000;
  _addr = 4;
  _data = {matrix_size};
  $display("# matrix_size = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 8;
  _data = {a_offset};
  $display("# a_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 12;
  _data = {b_offset};
  $display("# b_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 16;
  _data = {c_offset};
  $display("# c_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 0;
  _data = 1;
  _start_time = counter;
  $display("# start time = %d", _start_time);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 20;
  _data = 0;
  while(_data == 0) begin
    slave_read_ipgen_slave_lite_memory_saxi_1(_data, _addr);
    nclk();
  end
  _end_time = counter;
  $display("# end time = %d", _end_time);
  _time = _end_time - _start_time;
  $display("# exec time = %d", _time);

  #10000;
  $finish;
end
""".format(matrix_size=matrix_size, a_offset=a_offset,
           b_offset=b_offset, c_offset=c_offset)

    m = mkLed()
    ipcore.to_ipcore(m, simcode=simcode, simmemimg=memname, iftype='axi')
