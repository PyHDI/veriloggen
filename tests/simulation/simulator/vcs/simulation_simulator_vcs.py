from __future__ import absolute_import
from __future__ import print_function
import sys
import os

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
            If(count == 16 - 1)(
                count(0)
            ).Else(
                count(count + 1)
            )
        ))

    m.Always(Posedge(clk))(
        If(rst)(
            led(0)
        ).Else(
            Systask('display', 'LED:%d count:%d', led, count),
            If(count == 16 - 1)(
                led(led + 1)
            )
        ))

    return m


def mkTest():
    m = Module('test')
    width = m.Parameter('WIDTH', 8)
    clk = m.Reg('CLK')
    rst = m.Reg('RST')
    led = m.Wire('LED', width)

    uut = m.Instance(mkLed(), 'uut',
                     params=connect_same_name(width),
                     ports=connect_same_name(clk, rst, led))

    #simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, period=100)

    init.add(
        Delay(1000),
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog()
    print(verilog)

    try:
        from shutil import which
    except:
        from distutils.spawn import find_executable as which

    if which('vcs'):
        # run simulator (Icarus Verilog)
        sim = simulation.Simulator(test, sim='vcs')
        rslt = sim.run()  # display=False
        #rslt = sim.run(display=True)
        print(rslt)

        # launch waveform viewer (GTKwave)
        # sim.view_waveform() # background=False
        # sim.view_waveform(background=True)

    else:
        print("'vcs' not found")
