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

    m.Always(Posedge(clk))(
        If(rst)(
        ).Else(
            Systask('display', "LED:%d count:%d", led, count)
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
                    as_io=('dummy_out0', 'dummy_in0'), as_wire=('dummy_out1', 'dummy_in1'))

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkTop()
    uut = Submodule(m, led)

    # accessed via __getattr__
    clk = uut.CLK
    rst = uut.RST

    # simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog(filename='tmp.v')
    #verilog = test.to_verilog()
    # print(verilog)

    #sim = simulation.Simulator(test)
    #rslt = sim.run()
    # print(rslt)

    # sim.view_waveform()
