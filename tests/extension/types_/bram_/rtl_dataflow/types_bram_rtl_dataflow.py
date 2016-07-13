from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.bram as bram
import veriloggen.dataflow as dataflow


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2
    mybram = bram.Bram(m, 'mybram', clk, rst, datawidth, addrwidth, 2)

    xfsm = FSM(m, 'xfsm', clk, rst)
    xaddr = m.Reg('xaddr', 32, initval=0)
    xcount = m.Reg('xcount', 32, initval=0)

    # dataflow variables without manager
    x = dataflow.Variable('xdata', 'xvalid', 'xready')
    y = x + 100
    y.output('ydata', 'yvalid', 'yread')

    df = dataflow.Dataflow(y)
    df.implement(m, clk, rst)

    # Initialization
    xfsm(
        xaddr(0),
        xcount(0),
    )
    xfsm.goto_next()

    # write data to BRAM
    step = 16
    mybram.write(0, xaddr, xcount, cond=xfsm)
    xfsm(
        xaddr.inc(),
        xcount.inc()
    )
    xfsm.If(xcount == step - 1)(
        xaddr(0),
        xcount(0)
    )
    xfsm.Then().goto_next()

    # read data from BRAM
    read_data, read_valid = mybram.read(0, xaddr, cond=(xfsm, xaddr < step))
    # BRAM -> dataflow
    xack = x.write(read_data, cond=read_valid)
    xfsm(
        xaddr.inc()
    )
    xfsm.If(read_valid)(
        Systask('display', 'BRAM0[%d] = %d', xfsm.Prev(xaddr, 2), read_data)
    )
    xfsm.If(xfsm.Prev(xaddr, 1) == step).goto_next()

    # write result to BRAM
    yfsm = FSM(m, 'yfsm', clk, rst)
    yaddr = m.Reg('yaddr', 32, initval=0)
    yfsm(
        yaddr(0)
    )
    yfsm.goto_next()

    # read from dataflow
    rdata, rvalid = y.read(yfsm)
    # dataflow -> BRAM
    mybram.write(1, yaddr, rdata, cond=(yfsm, rvalid))
    yfsm.If(rvalid)(
        yaddr.inc()
    )
    yfsm.If(yaddr == step - 1)(
        yaddr(0)
    )
    yfsm.Then().goto_next()

    # read data from BRAM
    read_data, read_valid = mybram.read(1, yaddr, cond=(yfsm, yaddr < step))
    yfsm.If(yaddr < step)(
        yaddr.inc()
    )
    yfsm.If(read_valid)(
        Systask('display', 'BRAM1[%d] = %d', yfsm.Prev(yaddr, 2), read_data)
    )

    return m


def mkTest():
    m = Module('test')

    # target instance
    main = mkMain()

    # copy paras and ports
    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)

    clk = ports['CLK']
    rst = ports['RST']

    uut = m.Instance(main, 'uut',
                     params=m.connect_params(main),
                     ports=m.connect_ports(main))

    simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # sim.view_waveform()
