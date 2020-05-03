from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.axi as axi


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    myaxi = axi.AxiMaster(m, 'myaxi', clk, rst)
    myaxi.disable_write()

    fsm = FSM(m, 'fsm', clk, rst)
    sum = m.Reg('sum', 32, initval=0)

    # read address
    araddr = 1024
    arlen = 64
    expected_sum = (araddr + araddr + arlen - 1) * arlen // 2

    ack, counter = myaxi.read_request_counter(araddr, arlen, cond=fsm)
    fsm.If(ack).goto_next()

    # read data
    ready = m.Wire('ready')
    ready.assign(myaxi.rdata.rvalid)
    data, valid, last = myaxi.read_data(counter, cond=(fsm, ready))

    fsm.If(Ands(valid, ready))(
        sum(sum + data)
    )
    fsm.Then().If(last).goto_next()

    fsm(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )
    fsm.goto_next()

    fsm.make_always()

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

    # awready (no stall)
    awready = ports['myaxi_awready']
    _awready = m.TmpWireLike(awready)
    _awready.assign(1)
    m.Always()(awready(_awready))

    # wready (nostall)
    wready = ports['myaxi_wready']
    _wready = m.TmpWireLike(wready)
    _wready.assign(1)
    m.Always()(wready(_wready))

    # arready (no stall)
    #arready = ports['myaxi_arready']
    #_arready = m.TmpWireLike(arready)
    # _arready.assign(0)
    #m.Always()( arready(_arready) )

    # arready, rvalid, rdata, rlast
    raddr_fsm = FSM(m, 'raddr', clk, rst)
    _arlen = m.Reg('_arlen', 32, initval=0)
    raddr_fsm(
        ports['myaxi_arready'](0),
        ports['myaxi_rdata'](-1),
        ports['myaxi_rvalid'](0),
        ports['myaxi_rlast'](0)
    )
    raddr_fsm.If(ports['myaxi_arvalid']).goto_next()

    raddr_fsm.If(ports['myaxi_arvalid'])(
        ports['myaxi_arready'](1),
        ports['myaxi_rdata'](ports['myaxi_araddr'] - 1)
    )
    raddr_fsm.goto_next()

    raddr_fsm(
        ports['myaxi_arready'](0),
        _arlen(ports['myaxi_arlen'])
    )
    raddr_fsm.goto_next()

    ack = Ors(ports['myaxi_rready'], Not(ports['myaxi_rvalid']))

    raddr_fsm.If(Ands(ack, Not(ports['myaxi_rlast'])))(
        ports['myaxi_rdata'].inc(),
        ports['myaxi_rvalid'](1),
        ports['myaxi_rlast'](0),
        _arlen.dec()
    )
    raddr_fsm.Then().If(_arlen == 0)(
        ports['myaxi_rlast'](1),
    )
    raddr_fsm.Delay(1)(
        ports['myaxi_rvalid'](0),
        ports['myaxi_rlast'](0)
    )
    raddr_fsm.If(Ands(ports['myaxi_rvalid'], Not(ports['myaxi_rready'])))(
        ports['myaxi_rvalid'](ports['myaxi_rvalid']),
        ports['myaxi_rlast'](ports['myaxi_rlast']),
    )
    raddr_fsm.If(Ands(ports['myaxi_rvalid'],
                      ports['myaxi_rready'], ports['myaxi_rlast'])).goto_next()

    raddr_fsm.goto_next()

    raddr_fsm.goto_init()

    raddr_fsm.make_always()

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
