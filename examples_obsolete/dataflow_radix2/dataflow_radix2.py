from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.dataflow as dataflow


def complex_add(x, y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    return (a + c), (b + d)


def complex_sub(x, y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    return (a - c), (b - d)


def complex_mult(x, y):
    a = x[0]
    b = x[1]
    c = y[0]
    d = y[1]
    # (a + jb) * (c + jd) = ac - bd + j(ad + bc)
    ac = a * c
    bd = b * d
    ad = a * d
    bc = b * c
    re = ac - bd
    im = ad + bc
    return re, im


def radix2(x, y, c):
    d0 = complex_add(x, y)
    d1 = complex_sub(x, y)
    r0 = d0  # as-is
    r1 = complex_mult(d1, c)
    return r0, r1


def mkRadix2(datawidth=32):
    din0 = (dataflow.Variable('din0re', width=datawidth),
            dataflow.Variable('din0im', width=datawidth))
    din1 = (dataflow.Variable('din1re', width=datawidth),
            dataflow.Variable('din1im', width=datawidth))
    cnst = (dataflow.Variable('cnstre', width=datawidth),
            dataflow.Variable('cnstim', width=datawidth))

    r0, r1 = radix2(din0, din1, cnst)

    r0[0].output('dout0re')
    r0[1].output('dout0im')
    r1[0].output('dout1re')
    r1[1].output('dout1im')

    rslt = list(r0) + list(r1)
    df = dataflow.Dataflow(*rslt)

    m = df.to_module('radix2')

    try:
        df.draw_graph()
    except:
        print('Dataflow graph could not be generated.', file=sys.stderr)

    return m


def mkTest(datawidth=32):
    m = Module('test')

    main = mkRadix2(datawidth)

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    din0re = ports['din0re']
    din0im = ports['din0im']
    din1re = ports['din1re']
    din1im = ports['din1im']
    cnstre = ports['cnstre']
    cnstim = ports['cnstim']
    dout0re = ports['dout0re']
    dout0im = ports['dout0im']
    dout1re = ports['dout1re']
    dout1im = ports['dout1im']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))
    reset_stmt.append(din0re(2))
    reset_stmt.append(din0im(0))
    reset_stmt.append(din1re(1))
    reset_stmt.append(din1im(0))
    reset_stmt.append(cnstre(0))
    reset_stmt.append(cnstim(1))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(10000),
        Systask('finish'),
    )

    send_fsm = FSM(m, 'send_fsm', clk, rst)
    send_fsm.goto_next(cond=reset_done)

    for i in range(10):
        send_fsm.goto_next()

    send_fsm.add(Systask('finish'))

    send_fsm.make_always()

    return m


if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run()  # display=False
    #rslt = sim.run(display=True)
    print(rslt)
