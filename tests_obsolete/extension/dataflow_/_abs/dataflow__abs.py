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
    x = dataflow.Variable('xdata', valid='xvalid', ready='xready', signed=True)
    y = dataflow.Variable('ydata', valid='yvalid', ready='yready', signed=True)

    # dataflow definition
    z = x - y
    z = dataflow.Abs(z)

    # set output attribute
    z.output('zdata', valid='zvalid', ready='zready')

    df = dataflow.Dataflow(z)
    m = df.to_module('main')

    return m


def mkTest():
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

    zdata = ports['zdata']
    zvalid = ports['zvalid']
    zready = ports['zready']

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
    reset_stmt.append(zready(0))

    vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    simulation.setup_waveform(m, uut, dumpfile=vcd_name)
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
    receive('z', zdata, zvalid, zready, waitnum=5)

    m.Always(Posedge(clk))(
        If(reset_done)(
            If(AndList(xvalid, xready))(
                Systask('display', 'xdata=%d', xdata)
            ),
            If(AndList(yvalid, yready))(
                Systask('display', 'ydata=%d', ydata)
            ),
            If(AndList(zvalid, zready))(
                Systask('display', 'zdata=%d', zdata)
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
