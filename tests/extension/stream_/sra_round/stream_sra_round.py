from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.stream as stream

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from pprint import pprint


def mkMain():
    # input variiable
    x = stream.Variable('xdata')
    y = stream.Variable('ydata')

    # stream definition
    z = stream.SraRound(x, y)

    # set output attribute
    z.output('zdata')

    st = stream.Stream(z)
    m = st.to_module('main')

    # st.draw_graph()

    return m, st.pipeline_depth()


def mkTest(numports=8):
    m = Module('test')

    # target instance
    main, latency = mkMain()

    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    xdata = ports['xdata']
    ydata = ports['ydata']
    zdata = ports['zdata']
    xdata.signed = True
    zdata.signed = True

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    reset_done = m.Reg('reset_done', initval=0)
    reset_stmt = []
    reset_stmt.append(reset_done(0))
    reset_stmt.append(xdata(0))
    reset_stmt.append(ydata(0))

    end_of_sim = m.Reg('end_of_sim', initval=0)

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, reset_stmt, period=100)

    nclk = simulation.next_clock

    init.add(
        Delay(1000),
        reset_done(1),
        nclk(clk),
        Delay(10),
        Event(Posedge(end_of_sim)),
        Delay(100),
        Systask('finish'),
    )

    send_fsm = FSM(m, 'send_fsm', clk, rst)
    send_count = m.Reg('send_count', 32, initval=0)
    send_fsm.If(reset_done).goto_next()

    test_val_boader = [-2147483648, -10, 1, 2147483637]
    test_window = 9
    test_shift = [0, 1, 2, 3, 15, 16, 17, 30, 31, 32]

    for i in test_shift:
        for j in test_val_boader:
            send_fsm(
                xdata(j),
                ydata(i),
                send_count(0),
            )
            send_fsm.goto_next()

            send_fsm(
                xdata(xdata + 1),
                send_count.inc(),
                Display('xdata=%d', xdata),
                Display('ydata=%d', ydata)
            )
            send_fsm.goto_next(cond=send_count == test_window)

    recv_fsm = FSM(m, 'recv_fsm', clk, rst)
    recv_count = m.Reg('recv_count', 32, initval=0)
    recv_fsm.If(reset_done).goto_next()

    if latency >= 1:
        recv_fsm(
            recv_count(0),
        )
        recv_fsm.goto_next()

    if latency >= 2:
        recv_fsm.If(recv_count < latency - 2)(
            recv_count.inc()
        ).Else(
            recv_count(0)
        )
        recv_fsm.goto_next(cond=recv_count >= latency - 2)

    for i in test_shift:
        for j in test_val_boader:
            recv_fsm(
                recv_count(0),
            )
            recv_fsm.goto_next()

            recv_fsm(
                Display('zdata=%d', zdata),
                recv_count.inc()
            )
            recv_fsm.goto_next(cond=recv_count == test_window)

    recv_fsm(
        end_of_sim(1)
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
    # print(rslt)

    vx = list(map(lambda x: int(str.split(x, "=")[1]), filter(
        lambda x: "xdata" in x, str.split(rslt, "\n"))))
    vy = list(map(lambda x: int(str.split(x, "=")[1]), filter(
        lambda x: "ydata" in x, str.split(rslt, "\n"))))
    vz = list(map(lambda x: int(str.split(x, "=")[1]), filter(
        lambda x: "zdata" in x, str.split(rslt, "\n"))))
    ez = list(map(lambda x, y:
                  int(Decimal(str(x / (2.0**y))).quantize(
                      Decimal('0'), rounding=ROUND_HALF_UP)), vx, vy))

    pprint(list(zip(vx, vy, vz, ez)))
    assert(all(map(lambda v, e: v == e, vz, ez)))

    # launch waveform viewer (GTKwave)
    # sim.view_waveform() # background=False
    # sim.view_waveform(background=True)
