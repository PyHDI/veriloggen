from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.dataflow as dataflow
import veriloggen.types.fixed as fixed


def mkMain(point=8):
    # input variiable
    x = dataflow.Variable('xdata', valid='xvalid', ready='xready', point=point, signed=False)
    y = dataflow.Variable('ydata', valid='yvalid', ready='yready', point=point, signed=False)

    # dataflow definition
    z = x * y

    # set output attribute
    z.output('zdata', valid='zvalid', ready='zready')

    df = dataflow.Dataflow(z)
    m = df.to_module('main')

    return m


def mkTest(point=8):
    m = Module('test')

    # target instance
    main = mkMain(point)

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

    xdata_orig = m.RegLike(ports['xdata'], name='xdata_orig', initval=0)
    ydata_orig = m.RegLike(ports['ydata'], name='ydata_orig', initval=0)
    zdata_orig = m.WireLike(ports['zdata'], name='zdata_orig')
    m.Always()(xdata(fixed.to_fixed(xdata_orig, point)))
    m.Always()(ydata(fixed.to_fixed(ydata_orig, point)))
    m.Assign(zdata_orig(fixed.fixed_to_int(zdata, point)))

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
    reset_stmt.append(xdata_orig(0))
    reset_stmt.append(ydata_orig(0))

    vcd_name = os.path.splitext(os.path.basename(__file__))[0] + '.vcd'
    simulation.setup_waveform(m, uut, xdata_orig, ydata_orig, zdata_orig, dumpfile=vcd_name)
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

    send('x', xdata_orig, xvalid, xready, step=1, waitnum=10)
    send('y', ydata_orig, yvalid, yready, step=1, waitnum=20)
    receive('z', zdata, zvalid, zready, waitnum=50)

    m.Always(Posedge(clk))(
        If(reset_done)(
            If(AndList(xvalid, xready))(
                Systask('display', 'xdata=%d', xdata_orig)
            ),
            If(AndList(yvalid, yready))(
                Systask('display', 'ydata=%d', ydata_orig)
            ),
            If(AndList(zvalid, zready))(
                Systask('display', 'zdata=%d', zdata_orig)
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
