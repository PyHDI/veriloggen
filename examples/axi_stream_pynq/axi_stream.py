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

    axi_a = vthread.AXIStreamIn(m, 'axi_a', clk, rst, datawidth, with_last=True)
    axi_b = vthread.AXIStreamOut(m, 'axi_b', clk, rst, datawidth, with_last=True)

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth)

    def comp():

        while True:
            saxi.wait_flag(0, value=1, resetvalue=0)
            saxi.write(1, 1)  # set busy
            size = saxi.read(2)

            for i in range(size):
                a, a_last = axi_a.read()
                b = a + 1
                b_last = a_last
                axi_b.write(b, b_last)

            saxi.write(1, 0)  # unset busy

        vthread.finish()

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
