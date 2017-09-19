from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.dataflow as dataflow


def mkMain():
    # input variiable
    x = dataflow.Variable('xdata', valid='xvalid', ready='xready')
    y = dataflow.Variable('ydata', valid='yvalid', ready='yready')

    # dataflow definition
    z1 = x * y
    z2 = x * y + 1

    # set output attribute
    z1.output('z1data', valid='z1valid', ready='z1ready')
    z2.output('z2data', valid='z2valid', ready='z2ready')

    df = dataflow.Dataflow(z1, z2)
    m = df.to_module('main')

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
    xvalid = ports['xvalid']
    xready = ports['xready']

    ydata = ports['ydata']
    yvalid = ports['yvalid']
    yready = ports['yready']

    z1data = ports['z1data']
    z1valid = ports['z1valid']
    z1ready = ports['z1ready']

    z2data = ports['z2data']
    z2valid = ports['z2valid']
    z2ready = ports['z2ready']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))
    reset_stmt.append(xdata(0))
    reset_stmt.append(xvalid(0))
    reset_stmt.append(ydata(0))
    reset_stmt.append(yvalid(0))
    reset_stmt.append(z1ready(0))
    reset_stmt.append(z2ready(0))

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

    def send(name, data, valid, ready, step=1, waitnum=10):
        fsm = FSM(m, name + 'fsm', clk, rst)
        count = m.TmpReg(32, initval=0)

        fsm.add(valid(0))
        fsm.goto_next(cond=reset_done)
        for _ in range(waitnum):
            fsm.goto_next()

        fsm.add(valid(1))
        fsm.goto_next()

        fsm.add(data(data + step), cond=ready)
        fsm.add(count.inc(), cond=ready)
        fsm.add(valid(0), cond=AndList(count == 5, ready))
        fsm.goto_next(cond=AndList(count == 5, ready))

        for _ in range(waitnum):
            fsm.goto_next()
        fsm.add(valid(1))

        fsm.add(data(data + step), cond=ready)
        fsm.add(count.inc(), cond=ready)
        fsm.add(valid(0), cond=AndList(count == 10, ready))
        fsm.goto_next(cond=AndList(count == 10, ready))

        fsm.make_always()

    def receive(name, data, valid, ready, waitnum=10):
        fsm = FSM(m, name + 'fsm', clk, rst)

        fsm.add(ready(0))
        fsm.goto_next(cond=reset_done)
        fsm.goto_next()

        yinit = fsm.current
        fsm.add(ready(1), cond=valid)
        fsm.goto_next(cond=valid)
        for i in range(waitnum):
            fsm.add(ready(0))
            fsm.goto_next()

        fsm.goto(yinit)

        fsm.make_always()

    send('x', xdata, xvalid, xready, step=1, waitnum=10)
    send('y', ydata, yvalid, yready, step=2, waitnum=20)
    receive('z1', z1data, z1valid, z1ready, waitnum=5)
    receive('z2', z2data, z2valid, z2ready, waitnum=10)

    m.Always(Posedge(clk))(
        If(reset_done)(
            If(AndList(xvalid, xready))(
                Systask('display', 'xdata=%d', xdata)
            ),
            If(AndList(yvalid, yready))(
                Systask('display', 'ydata=%d', ydata)
            ),
            If(AndList(z1valid, z1ready))(
                Systask('display', 'z1data=%d', z1data)
            ),
            If(AndList(z2valid, z2ready))(
                Systask('display', 'z2data=%d', z2data)
            )
        )
    )

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
