from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *


def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')

    led = m.Output('LED', width)
    count = m.Reg('count', 32)

    # reg with same name
    _led = m.RegLike(led)

    # output with same name
    _count = m.OutputLike(count)

    # signals with different name
    width1 = m.ParameterLike(width, name='WIDTH1')
    width2 = m.LocalparamLike(width, name='WIDTH2')
    width3 = m.TmpLocalparamLike(width)

    input_count = m.OutputLike(count, name='input_count')
    output_count = m.OutputLike(count, name='output_count')
    wire_count = m.WireLike(count, name='wire_count')
    reg_count = m.RegLike(count, name='reg_count', initval=8)
    tmpwire_count = m.TmpWireLike(count)
    tmpreg_count = m.TmpRegLike(count)

    m.Assign(wire_count(input_count))
    m.Assign(output_count(reg_count))

    m.Always(Posedge(clk))(
        If(rst)(
            m.make_reset()
        ).Else(
            reg_count(wire_count)
        ))

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


if __name__ == '__main__':
    led = mkLed()
    verilog = led.to_verilog()
    print(verilog)
