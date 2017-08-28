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
import veriloggen.types.ipcore as ipcore


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
            #check(matrix_size, a_offset, b_offset, c_offset)
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

    def check(matrix_size, a_offset, b_offset, c_offset):
        all_ok = True
        c_addr = c_offset
        for i in range(matrix_size):
            myaxi.dma_read(ram_c, 0, c_addr, matrix_size)
            for j in range(matrix_size):
                v = ram_c.read(j)
                if i == j and vthread.verilog.NotEql(v, (i + 1) * 2):
                    all_ok = False
                    print("NG [%d,%d] = %d" % (i, j, v))
                if i != j and vthread.verilog.NotEql(v, 0):
                    all_ok = False
                    print("NG [%d,%d] = %d" % (i, j, v))
            c_addr += matrix_size * (datawidth // 8)

        if all_ok:
            led.value = 0b01010101
            print("OK")
        else:
            led.value = 0x0f
            print("NG")

    th = vthread.Thread(m, 'th_matmul', clk, rst, matmul)
    fsm = th.start()

    return m


def mkTest(memname='mymem.out'):
    m = Module('test')

    matrix_size = 16

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    # memory image
    #memname = 'mymem.out'

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
        for x in range(matrix_size):
            for y in range(matrix_size):
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
        for x in range(matrix_size):
            for y in range(matrix_size):
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
        for x in range(matrix_size):
            for y in range(matrix_size):
                addr += 4
                value = 100
                fwrite(f, value)

        for i in range(2 ** 20 - addr):
            f.write('%s\n' % '00')

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg=memname)
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
        matrix_size = 16
        print('# matrix_size = %d' % matrix_size)
        _saxi.write(awaddr, matrix_size)

        awaddr = 8
        a_offset = 0
        print('# a_offset = %d' % a_offset)
        _saxi.write(awaddr, a_offset)

        awaddr = 12
        b_offset = 1024 * 1
        print('# b_offset = %d' % b_offset)
        _saxi.write(awaddr, b_offset)

        awaddr = 16
        c_offset = 1024 * 2
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


if __name__ == '__main__':
    memname = 'mymem.out'
    test = mkTest(memname)
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

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
  _data = 16;
  $display("# matrix_size = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 8;
  _data = 0;
  $display("# a_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 12;
  _data = 1024 * 1;
  $display("# b_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 16;
  _data = 1024 * 2;
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
"""

    m = mkLed()
    ipcore.to_ipcore(m, 'myipcore', simcode=simcode,
                     simmemimg=memname, iftype='axi')
