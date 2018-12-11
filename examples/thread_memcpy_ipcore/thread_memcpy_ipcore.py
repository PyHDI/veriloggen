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


def mkMemcpy():
    m = Module('memcpy')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10

    ram_words = (2 ** addrwidth) // (datawidth // 8)

    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth)
    maxi = vthread.AXIM(m, 'maxi', clk, rst, datawidth)
    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth, length=8)

    def memcpy():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)

            copy_bytes = saxi.read(1)
            src_offset = saxi.read(2)
            dst_offset = saxi.read(3)

            copy(copy_bytes, src_offset, dst_offset)

            saxi.write_flag(4, 1, resetvalue=0)

    def copy(copy_bytes, src_offset, dst_offset):
        rest_words = copy_bytes // (datawidth // 8)
        src_global_addr = src_offset
        dst_global_addr = dst_offset
        local_addr = 0

        while rest_words > 0:
            if rest_words > ram_words:
                dma_size = ram_words
            else:
                dma_size = rest_words

            maxi.dma_read(ram_a, local_addr, src_global_addr, dma_size)
            maxi.dma_write(ram_a, local_addr, dst_global_addr, dma_size)

            src_global_addr += dma_size * (datawidth // 8)
            dst_global_addr += dma_size * (datawidth // 8)
            rest_words -= dma_size

    th = vthread.Thread(m, 'th_memcpy', clk, rst, memcpy)
    fsm = th.start()

    return m


def mkTest():
    m = Module('test')

    copy_bytes = 1024 * 4

    # target instance
    memcpy = mkMemcpy()

    uut = Submodule(m, memcpy, name='uut')
    clk = uut['CLK']
    rst = uut['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst)
    memory.connect(uut.get_inst_ports(), 'maxi')

    # AXI-Slave controller
    _saxi = vthread.AXIMLite(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(uut.get_inst_ports(), 'saxi')

    # Timer
    counter = m.Reg('counter', 32, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        counter.inc()
    )

    def ctrl():
        for i in range(100):
            pass

        awaddr = 4 * 1
        print('# copy_bytes = %d' % copy_bytes)
        _saxi.write(awaddr, copy_bytes)

        awaddr = 4 * 2
        src_offset = 0
        print('# src_offset = %d' % src_offset)
        _saxi.write(awaddr, src_offset)

        awaddr = 4 * 3
        dst_offset = 1024 * 8
        print('# dst_offset = %d' % dst_offset)
        _saxi.write(awaddr, dst_offset)

        awaddr = 4 * 0
        start_time = counter
        print('# start time = %d' % start_time)
        _saxi.write(awaddr, 1)

        araddr = 4 * 4
        v = _saxi.read(araddr)
        while v == 0:
            v = _saxi.read(araddr)

        end_time = counter
        print('# end time = %d' % end_time)
        time = end_time - start_time
        print('# exec time = %d' % time)

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

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
  _data = 1024 * 4;
  $display("# copy_bytes = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 8;
  _data = 0;
  $display("# src_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 12;
  _data = 1024 * 8;
  $display("# dst_offset = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 0;
  _data = 1;
  _start_time = counter;
  $display("# start time = %d", _start_time);
  slave_write_ipgen_slave_lite_memory_saxi_1(_data, _addr);

  _addr = 16;
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

    m = mkMemcpy()
    ipcore.to_ipcore(m, simcode=simcode, iftype='axi')
