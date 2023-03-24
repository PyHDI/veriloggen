from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math
import cmath

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.dataflow as dataflow
import veriloggen.types.fixed as fixed


def _log2(v):
    return math.log(v, 2)


log2 = math.log2 if hasattr(math, 'log2') else _log2


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

#-------------------------------------------------------------------------------


def gen_weight(n):
    c = cmath.rect(1, -2 * cmath.pi / n)
    weight = []

    for i in range(int(log2(n))):
        offset = 0
        offset_count = 0
        for k in range(int(n / 2)):
            first = k + offset
            p = (first * (2 ** i)) % int(n / 2)
            _w = c ** p
            w = (_w.real, _w.imag)
            weight.append(w)

            offset_count += 1
            if offset_count == (n >> (i + 1)):
                offset_count = 0
                offset += (n >> (i + 1))

    return weight


def fft_weight(din, n, weight):
    for i in range(int(log2(n))):
        offset = 0
        offset_count = 0

        ndin0 = []
        ndin1 = []
        ndin = []

        for k in range(int(n / 2)):
            first = k + offset
            second = k + offset + (n >> (i + 1))

            w = weight.pop(0)
            r0, r1 = radix2(din[first], din[second], w)

            ndin0.append(r0)
            ndin1.append(r1)

            offset_count += 1
            if offset_count == (n >> (i + 1)):
                offset_count = 0
                offset += (n >> (i + 1))
                ndin.extend(ndin0)
                ndin.extend(ndin1)
                ndin0 = []
                ndin1 = []

        din = ndin

    # reorder by bit-inversed index
    ret = []
    for i in range(len(din)):
        # bit-inversion
        fm = '{:0' + str(int(log2(n))) + 'b}'
        index = int(fm.format(i)[::-1], 2)
        #print(i, '->', index)
        re, im = din[index]
        ret.append((re, im))

    return ret


def fft(din, n):
    weight = gen_weight(n)
    return fft_weight(din, n, weight)

#-------------------------------------------------------------------------------


def mkFFT(n, datawidth=16, point=8):
    din = [(dataflow.Variable('din' + str(i) + 're', width=datawidth, point=point, signed=True),
            dataflow.Variable('din' + str(i) + 'im', width=datawidth, point=point, signed=True))
           for i in range(n)]

    weight = [(dataflow.Variable('weight' + str(i) + 're', width=datawidth,
                                 point=point, signed=True),
               dataflow.Variable('weight' + str(i) + 'im', width=datawidth,
                                 point=point, signed=True))
              for i in range(int(n * log2(n) / 2))]

    # call software-defined method
    rslt = fft_weight(din, n, weight)

    vars = []
    for i, (re, im) in enumerate(rslt):
        re.output('dout' + str(i) + 're')
        im.output('dout' + str(i) + 'im')
        vars.append(re)
        vars.append(im)

    df = dataflow.Dataflow(*vars)
    m = df.to_module('fft')

    # try:
    #    df.draw_graph()
    # except:
    #    print('Dataflow graph could not be generated.', file=sys.stderr)

    return m

#-------------------------------------------------------------------------------


def mkTest(n=8, datawidth=16, point=8):
    m = Module('test')

    main = mkFFT(n, datawidth, point)

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    din = [(ports['din' + str(i) + 're'], ports['din' + str(i) + 'im'])
           for i in range(n)]
    dout = [(ports['dout' + str(i) + 're'], ports['dout' + str(i) + 'im'])
            for i in range(n)]
    weight = [(ports['weight' + str(i) + 're'], ports['weight' + str(i) + 'im'])
              for i in range(int(n * log2(n) / 2))]

    _din = [(m.WireLike(re, name='_' + re.name, width=datawidth - point),
             m.WireLike(im, name='_' + im.name, width=datawidth - point))
            for re, im in din]
    _dout = [(m.WireLike(re, name='_' + re.name, width=datawidth - point),
              m.WireLike(im, name='_' + im.name, width=datawidth - point))
             for re, im in dout]
    _weight = [(m.WireLike(re, name='_' + re.name, width=datawidth - point),
                m.WireLike(im, name='_' + im.name, width=datawidth - point))
               for re, im in weight]

    for (lre, lim), (rre, rim) in zip(_din, din):
        m.Assign(lre(fixed.fixed_to_int(rre, point)))
        m.Assign(lim(fixed.fixed_to_int(rim, point)))

    for (lre, lim), (rre, rim) in zip(_dout, dout):
        m.Assign(lre(fixed.fixed_to_int(rre, point)))
        m.Assign(lim(fixed.fixed_to_int(rim, point)))

    for (lre, lim), (rre, rim) in zip(_weight, weight):
        m.Assign(lre(fixed.fixed_to_int(rre, point)))
        m.Assign(lim(fixed.fixed_to_int(rim, point)))

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))
    for i, (re, im) in enumerate(din):
        reset_stmt.append(re(fixed.to_fixed(i, point)))
        reset_stmt.append(im(fixed.to_fixed(i, point)))

    weight_value = gen_weight(n)

    for i, (re, im) in enumerate(weight):
        wr, wi = weight_value[i]
        reset_stmt.append(re(fixed.to_fixed(wr, point)))
        reset_stmt.append(im(fixed.to_fixed(wi, point)))

    vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    simulation.setup_waveform(m, uut, *(_din + _dout + _weight), dumpfile=vcd_name)
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

    def dump(name, v, point):
        return Systask('display', name + '= %f', fixed.fixed_to_real(v, point))

    send_fsm = FSM(m, 'send_fsm', clk, rst)
    send_fsm.goto_next(cond=reset_done)

    # for i, (re, im) in enumerate(weight):
    #    send_fsm.add( dump('w[%d]re' % i, re, point) )
    #    send_fsm.add( dump('w[%d]im' % i, im, point) )

    for i, (re, im) in enumerate(din):
        send_fsm.add(re(fixed.to_fixed(i, point)))
        send_fsm.add(im(fixed.to_fixed(i, point)))
    #    send_fsm.add( dump('din[%d]re' % i, re, point), delay=1 )
    #    send_fsm.add( dump('din[%d]im' % i, im, point), delay=1 )

    send_fsm.goto_next()

    for i, (re, im) in enumerate(din):
        send_fsm.add(re(fixed.to_fixed(0, point)))
        send_fsm.add(im(fixed.to_fixed(0, point)))

    send_fsm.goto_next()

    for _ in range(100):
        # for i, (re, im) in enumerate(dout):
        #    send_fsm.add( dump('dout[%d]re' % i, re, point), delay=1 )
        #    send_fsm.add( dump('dout[%d]im' % i, im, point), delay=1 )

        send_fsm.goto_next()

    send_fsm.add(Systask('finish'))

    send_fsm.make_always()

    return m


if __name__ == '__main__':
    n = 8
    point = 8
    test = mkTest(n, point=point)
    verilog = test.to_verilog('tmp.v')
    # print(verilog)

    # run simulator (Icarus Verilog)
    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # only target RTL
    #main = mkFFT(n)
    #verilog = main.to_verilog('tmp.v')
    # print(verilog)

    din = [(i, i) for i in range(n)]
    rslt = fft(din, n)
    for r in rslt:
        print(complex(round(r[0] * (2 ** point), 5), round(r[1] * (2 ** point), 5)), ':',
              complex(round(r[0], 5), round(r[1], 5)))
