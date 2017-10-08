from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', width)

    dummy_out0 = m.Output('dummy_out0', width)
    dummy_out1 = m.Output('dummy_out1', width)
    dummy_out2 = m.Output('dummy_out2', width)
    dummy_in0 = m.Input('dummy_in0', width)
    dummy_in1 = m.Input('dummy_in1', width)
    dummy_in2 = m.Input('dummy_in2', width)

    count = m.Reg('count', 32)

    m.Always(Posedge(clk))(
        If(rst)(
            count(0)
        ).Else(
            If(count == 1023)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))

    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            If(count == 1023)(
                led(led + 1)
            )
        ))

    return m


def mkTop():
    m = Module('top')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.Output('LED', width)

    sub = Submodule(m, mkLed(), 'inst_blinkled',
                    arg_params=(('WIDTH', width),),
                    arg_ports=(('LED', led), ('CLK', clk), ('RST', rst)),
                    as_io=('dummy_.*0',), as_wire=('dummy_.*1',))

    return m

if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog('tmp.v')
    print(verilog)
