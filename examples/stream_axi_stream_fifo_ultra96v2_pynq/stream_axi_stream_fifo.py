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


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10

    maxi = vthread.AXIM(m, 'maxi', clk, rst, datawidth)
    maxi.disable_write()

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst,
                                    datawidth=32, length=8)

    axi_in = vthread.AXIStreamInFifo(m, 'axi_in', clk, rst, datawidth,
                                     with_last=True)
    axi_out = vthread.AXIStreamOutFifo(m, 'axi_out', clk, rst, datawidth,
                                       with_last=True)

    fifo_addrwidth = 8
    fifo_a = vthread.FIFO(m, 'fifo_a', clk, rst, datawidth, fifo_addrwidth)
    fifo_b = vthread.FIFO(m, 'fifo_b', clk, rst, datawidth, fifo_addrwidth)
    fifo_c = vthread.FIFO(m, 'fifo_c', clk, rst, datawidth, fifo_addrwidth)

    ram_b = vthread.RAM(m, 'ram_b', clk, rst, datawidth, addrwidth)

    strm0 = vthread.Stream(m, 'mystream_reduce', clk, rst)
    a = strm0.source('a')
    reduce_size = strm0.parameter('reduce_size')
    v = a * a
    sum, sum_valid = strm0.ReduceAddValid(v, reduce_size)
    strm0.sink(sum, 'sum', when=sum_valid, when_name='sum_valid')

    strm1 = vthread.Stream(m, 'mystream_bias', clk, rst)
    x = strm1.source('x')
    y = strm1.source('y')
    z = x + y
    strm1.sink(z, 'z')

    def comp():

        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)

            saxi.write(1, 1)  # set busy

            read_size = saxi.read(2)
            write_size = saxi.read(3)
            reduce_size = saxi.read(4)
            bias_addr = saxi.read(5)

            if read_size <= 0:
                read_size = 1
            if write_size <= 0:
                write_size = 1
            if reduce_size <= 0:
                reduce_size = 1

            maxi.dma_read(ram_b, 0, bias_addr, write_size)

            axi_in.dma_read_async(fifo_a, read_size)
            axi_out.dma_write_async(fifo_c, write_size)

            strm0.set_source_fifo('a', fifo_a, read_size)
            strm0.set_parameter('reduce_size', reduce_size)
            strm0.set_sink_fifo('sum', fifo_b, write_size)

            strm1.set_source_fifo('x', fifo_b, write_size)
            strm1.set_source('y', ram_b, 0, write_size)
            strm1.set_sink_fifo('z', fifo_c, write_size)

            strm0.run()
            strm1.run()

            strm0.join()
            strm1.join()

            saxi.write(1, 0)  # unset busy

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start()

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    test = mkLed()

    code = test.to_verilog(filename)
    return code


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
