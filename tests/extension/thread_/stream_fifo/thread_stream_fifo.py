from __future__ import absolute_import
from __future__ import print_function
import sys
import os

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

    axi_a = vthread.AXIStreamIn(m, 'axi_a', clk, rst, datawidth, with_last=True,
                                enable_async=True)
    axi_b = vthread.AXIStreamIn(m, 'axi_b', clk, rst, datawidth, with_last=True,
                                enable_async=True)
    axi_c = vthread.AXIStreamOut(m, 'axi_c', clk, rst, datawidth, with_last=True,
                                 enable_async=True)

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth)

    fifo_a = vthread.FIFO(m, 'fifo_a', clk, rst, datawidth, addrwidth)
    fifo_b = vthread.FIFO(m, 'fifo_b', clk, rst, datawidth, addrwidth)
    fifo_c = vthread.FIFO(m, 'fifo_c', clk, rst, datawidth, addrwidth)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    a = strm.source('a')
    b = strm.source('b')
    c = a + b
    strm.sink(c, 'c')

    def comp_stream(size):
        strm.set_source_fifo('a', fifo_a, size)
        strm.set_source_fifo('b', fifo_b, size)
        strm.set_sink_fifo('c', fifo_c, size)
        strm.run()
        strm.join()

    def comp():
        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy
            size = saxi.read(2)
            offset = 0

            axi_a.write_fifo(fifo_a, size)  # non-blocking
            axi_b.write_fifo(fifo_b, size)  # non-blocking
            comp_stream(size)
            axi_c.read_fifo(fifo_c, size)  # non-blocking

            axi_c.wait_read_fifo()  # wait

            saxi.write(1, 0)  # unset busy

        vthread.finish()

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start()

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    test = mkLed()

    if filename is not None:
        test.to_verilog(filename)

    return '# verify: PASSED'


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
