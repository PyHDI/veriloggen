from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.fixed as fixed


def mkLed():
    m = Module('blinkled')
    width = m.Parameter('WIDTH', 8)
    clk = m.Input('CLK')
    rst = m.Input('RST')

    a = fixed.FixedReg(m, 'a', width=16, point=4, initval=4)
    b = fixed.FixedReg(m, 'b', width=16, point=8,
                       initval=fixed.FixedConst(1, point=8, raw=True))
    c = fixed.FixedReg(m, 'c', width=32, point=8, initval=-8)
    d = fixed.FixedReg(m, 'd', width=32, point=16,
                       initval=fixed.FixedConst(1, point=16, raw=True))
    e = fixed.FixedReg(m, 'e', width=32, point=16, initval=0)

    seq = Seq(m, 'seq', clk, rst)
    seq(
        a(b - 1),
        b(a - 1),
        c.write_raw(b.raw + 1),
        d.write_raw(c + 1),
        e.inc()
    )

#    seq.Delay(1)(
#        Display("a=%h", a),
#        Display("b=%h", b),
#        Display("c=%h", c),
#        Display("d=%h", d),
#        Display("e=%h", e)
#    )

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    uut = Submodule(m, led, name='uut')
    clk = uut['CLK']
    rst = uut['RST']

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
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # sim.view_waveform()
