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

    a = fixed.FixedReg(m, 'a', point=16, signed=False, initval=2)
    b = fixed.FixedReg(m, 'b', point=8, signed=False, initval=16)
    c = fixed.FixedReg(m, 'c', point=16, signed=False, initval=1)
    d = fixed.FixedReg(m, 'd', point=16, signed=False, initval=1)
    sa = fixed.FixedReg(m, 'sa', point=16, initval=2)
    sb = fixed.FixedReg(m, 'sb', point=8, initval=-16)
    sc = fixed.FixedReg(m, 'sc', point=16, initval=-1)
    sd = fixed.FixedReg(m, 'sd', point=16, initval=-1)

    seq = Seq(m, 'seq', clk, rst)
    seq(
        a(a),
        b(b),
        c(b * a),
        d(a * b),
        sa(sa),
        sb(sb),
        sc(sb * sa),
        sd(fixed.to_signed(a) * sb)
    )

#    seq.Delay(1)(
#        Display("a=%h", a),
#        Display("b=%h", b),
#        Display("c=%h", c),
#        Display("d=%h", d),
#        Display("sa=%h", sa),
#        Display("sb=%h", sb),
#        Display("sc=%h", sc),
#        Display("sd=%h", sd),
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
