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
    led = mkLed()

    clk = m.Input('CLK')
    rst = m.Input('RST')

    m.copy_params(led, prefix='A_')
    m.copy_ports(led, prefix='A_', exclude=('CLK', 'RST'))

    m.copy_params(led, prefix='B_')
    m.copy_ports(led, prefix='B_', exclude=('CLK', 'RST'))

    a_params = m.connect_params(led, prefix='A_')
    a_ports = collections.OrderedDict()
    a_ports['CLK'] = clk
    a_ports['RST'] = rst
    a_ports.update(m.connect_ports(led, prefix='A_'))

    b_params = m.connect_params(led, prefix='B_')
    b_ports = collections.OrderedDict()
    b_ports['CLK'] = clk
    b_ports['RST'] = rst
    b_ports.update(m.connect_ports(led, prefix='B_'))

    m.Instance(led, 'inst_blinkled_a',
               params=a_params, ports=a_ports)

    m.Instance(led, 'inst_blinkled_b',
               params=b_params, ports=b_ports)

    return m


if __name__ == '__main__':
    top = mkTop()
    verilog = top.to_verilog()
    print(verilog)
