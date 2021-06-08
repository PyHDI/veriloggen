from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.stream as stream


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    mul_strm = stream.StreamManager(m, clk, rst, aswire=True, no_hook=True)
    mul_a = mul_strm.Variable('adata')
    mul_b = mul_strm.Variable('bdata')
    mul_c = mul_a * mul_b
    mul_c.output('cdata')

    strm = stream.StreamManager(m, clk, rst, aswire=False, no_hook=True)
    x = strm.Variable('xdata')
    y = strm.Variable('ydata')
    e = strm.Variable('edata')
    x = x + 1
    y = y + 2

    sub = strm.Substream(mul_strm)
    sub.write('adata', x)
    sub.write('bdata', y)
    mul = sub.read('cdata')

    z, v = strm.ReduceAddValid(mul, 8, enable=e)
    z = z + 1000

    z.output('zdata')
    v.output('vdata')

    strm.implement()

    return m


def mkTest(numports=8):
    m = Module('test')

    # target instance
    main = mkMain()

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    xdata = ports['xdata']
    ydata = ports['ydata']
    zdata = ports['zdata']
    edata = ports['edata']
    vdata = ports['vdata']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))
    reset_stmt.append(xdata(0))
    reset_stmt.append(ydata(0))
    reset_stmt.append(edata(0))

    # simulation.setup_waveform(m, uut)
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
    send_count = m.Reg('send_count', 32, initval=0)
    send_fsm.If(reset_done).goto_next()

    send_fsm(
        xdata(0),
        ydata(0),
        edata(1),
        send_count.inc()
    )
    send_fsm.Delay(1)(
        Display('xdata=%d', xdata),
        Display('ydata=%d', ydata)
    )
    send_fsm.goto_next()

    send_fsm(
        xdata(xdata + 1),
        ydata(ydata + 2),
        edata(1),
        send_count.inc()
    )
    send_fsm.Delay(1)(
        Display('xdata=%d', xdata),
        Display('ydata=%d', ydata)
    )
    send_fsm.If(send_count == 64).goto_next()

    send_fsm(
        edata(0)
    )

    recv_fsm = FSM(m, 'recv_fsm', clk, rst)
    recv_count = m.Reg('recv_count', 32, initval=0)
    recv_fsm.If(reset_done).goto_next()

    recv_fsm.If(vdata)(
        Display('zdata=%d', zdata),
        recv_count.inc()
    )
    recv_fsm.If(recv_count == 8).goto_next()

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

    # launch waveform viewer (GTKwave)
    # sim.view_waveform() # background=False
    # sim.view_waveform(background=True)
