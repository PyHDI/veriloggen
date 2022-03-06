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
import veriloggen.types.ipxact as ipxact

pe_verilog_code = """
module processing_unit #
(
  parameter ADDR_WIDTH = 10,
  parameter DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  input start,
  output reg busy,
  input [ADDR_WIDTH-1:0] size,
  output reg [ADDR_WIDTH-1:0] addr,
  input [DATA_WIDTH-1:0] rdata,
  output reg [DATA_WIDTH-1:0] wdata,
  output reg wenable
);

  localparam INCR = 100;

  reg [ADDR_WIDTH-1:0] count;
  reg [DATA_WIDTH-1:0] rdata_buf;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      addr <= 0;
      count <= 0;
      busy <= 0;
      rdata_buf <= 0;
      wdata <= 0;
      wenable <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          if(start) begin
            addr <= 0;
            count <= size;
            busy <= 1;
          end 
          if(start) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          rdata_buf <= rdata;
          fsm <= fsm_3;
        end
        fsm_3: begin
          wdata <= rdata_buf + INCR;
          wenable <= 1;
          fsm <= fsm_4;
        end
        fsm_4: begin
          wenable <= 0;
          addr <= addr + 1;
          count <= count - 1;
          if(count > 1) begin
            fsm <= fsm_1;
          end 
          if(count <= 1) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          busy <= 0;
          fsm <= fsm_init;
        end
      endcase
    end
  end


endmodule
"""


def mkMemcpy():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('led', 8, initval=0)

    datawidth = 32
    addrwidth = 10
    ram_words = (2 ** addrwidth) // (datawidth // 8)

    ram_a = vthread.RAM(m, 'ram_a', clk, rst, datawidth, addrwidth, numports=2)
    maxi = vthread.AXIM(m, 'maxi', clk, rst, datawidth)
    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth, length=8)

    # import verilog submodule
    start = m.Reg('start', initval=0)
    busy = m.Wire('busy')
    size = m.Reg('size', addrwidth, initval=0)

    sub = Submodule(m, pe_verilog_code, 'inst_pe', prefix='pe_',
                    arg_params=(('ADDR_WIDTH', addrwidth),
                                ('DATA_WIDTH', datawidth)),
                    arg_ports=(('CLK', clk), ('RST', rst),
                               ('start', start), ('busy', busy), ('size', size)),
                    as_wire=('addr', 'rdata', 'wdata', 'wenable'))

    # connect ports to RAM
    ram_a.connect_rtl(1, sub['addr'], sub['wdata'],
                      sub['wenable'], sub['rdata'], 1)

    def control_processing_unit(v):
        size.value = v
        start.value = 1
        start.value = 0
        while busy:
            pass

    def memcpy():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy

            copy_bytes = saxi.read(2)
            src_offset = saxi.read(3)
            dst_offset = saxi.read(4)

            copy(copy_bytes, src_offset, dst_offset)

            saxi.write(1, 0)  # unset busy

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
            control_processing_unit(dma_size)
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

        awaddr = 2 * 4
        print('# copy_bytes = %d' % copy_bytes)
        _saxi.write(awaddr, copy_bytes)

        awaddr = 3 * 4
        src_offset = 0
        print('# src_offset = %d' % src_offset)
        _saxi.write(awaddr, src_offset)

        awaddr = 4 * 4
        dst_offset = 1024 * 8
        print('# dst_offset = %d' % dst_offset)
        _saxi.write(awaddr, dst_offset)

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

    m = mkMemcpy()
    ipxact.to_ipxact(m,
                     clk_ports=[('CLK', ('RST',))],
                     rst_ports=[('RST', 'ACTIVE_HIGH')])
