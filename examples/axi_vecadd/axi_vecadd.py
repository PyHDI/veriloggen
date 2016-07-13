from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.types.axi as axi
import veriloggen.types.bram as bram
import veriloggen.dataflow as dataflow


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    bus = axi.AxiMaster(m, 'myaxi', clk, rst)
    ram_a = bram.Bram(m, 'ram_a', clk, rst, numports=1)
    ram_b = bram.Bram(m, 'ram_b', clk, rst, numports=1)
    ram_c = bram.Bram(m, 'ram_c', clk, rst, numports=1)

    fsm = FSM(m, 'fsm', clk, rst)

    bus_addr = 1024
    ram_addr = 0
    length = 64

    dma_done = axi.dma_read(bus, ram_a, bus_addr, ram_addr, length, cond=fsm)
    fsm.If(dma_done).goto_next()

    bus_addr = 1024 * 2

    dma_done = axi.dma_read(bus, ram_b, bus_addr, ram_addr, length, cond=fsm)
    fsm.If(dma_done).goto_next()

    adata, alast, adone = ram_a.read_dataflow(0, ram_addr, length, cond=fsm)
    bdata, blast, bdone = ram_b.read_dataflow(0, ram_addr, length, cond=fsm)
    fsm.If(adone).goto_next()

    cdata = adata + bdata

    done = ram_c.write_dataflow(0, ram_addr, cdata, length)
    fsm.If(done).goto_next()

    bus_addr = 1024 * 3

    dma_done = axi.dma_write(bus, ram_c, bus_addr, ram_addr, length, cond=fsm)
    fsm.If(dma_done).goto_next()

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
    #awready = ports['myaxi_awready']
    #_awready = m.TmpWireLike(awready)
    #_awready.assign(1)
    # m.Always()(awready(_awready))

    # wready (nostall)
    #wready = ports['myaxi_wready']
    #_wready = m.TmpWireLike(wready)
    #_wready.assign(1)
    # m.Always()(wready(_wready))

    # awready (with stall)
    waddr_fsm = FSM(m, 'waddr', clk, rst)
    _awlen = m.Reg('_awlen', 32, initval=0)

    waddr_fsm(
        ports['myaxi_awready'](0),
        ports['myaxi_wready'](0),
        _awlen(0)
    )
    waddr_fsm.If(ports['myaxi_awvalid']).goto_next()

    waddr_fsm.If(ports['myaxi_awvalid'])(
        ports['myaxi_awready'](1)
    )
    waddr_fsm.goto_next()

    waddr_fsm(
        ports['myaxi_awready'](0),
        _awlen(ports['myaxi_awlen'])
    )
    waddr_fsm.goto_next()

    # wready (with stall)
    waddr_init = waddr_fsm.current
    waddr_fsm(
        ports['myaxi_wready'](0)
    )
    waddr_fsm.If(ports['myaxi_wvalid']).goto_next()

    waddr_fsm.If(ports['myaxi_wvalid'])(
        ports['myaxi_wready'](1)
    )
    waddr_fsm.goto_next()

    waddr_fsm(
        ports['myaxi_wready'](0)
    )
    waddr_fsm.goto_next()
    waddr_fsm.goto_next()
    waddr_fsm.goto_next()

    waddr_fsm(
        _awlen.dec()
    )
    waddr_fsm.goto(waddr_init)
    waddr_fsm.If(_awlen == 0).goto_init()

    # wready (no stall)
#    waddr_fsm(
#        ports['myaxi_wready'](1)
#    )
#    waddr_fsm.Delay(1)(
#        ports['myaxi_wready'](0)
#    )
#    waddr_fsm.If(ports['myaxi_wvalid'])(
#        _awlen.dec()
#    )
#    waddr_fsm.Then().If(_awlen == 0).goto_next()

    # arready (no stall)
    #arready = ports['myaxi_arready']
    #_arready = m.TmpWireLike(arready)
    #_arready.assign(0)
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

    # nodelay
#    raddr_fsm.If(Ands(ack, Not(ports['myaxi_rlast'])))(
#        ports['myaxi_rdata'].inc(),
#        ports['myaxi_rvalid'](1),
#        ports['myaxi_rlast'](0),
#        _arlen.dec()
#    )
#    raddr_fsm.Then().If(_arlen == 0)(
#        ports['myaxi_rlast'](1),
#    )
#    raddr_fsm.Delay(1)(
#        ports['myaxi_rvalid'](0),
#        ports['myaxi_rlast'](0)
#    )
#    raddr_fsm.If(Ands(ports['myaxi_rvalid'], Not(ports['myaxi_rready'])))(
#        ports['myaxi_rvalid'](ports['myaxi_rvalid']),
#        ports['myaxi_rlast'](ports['myaxi_rlast']),
#    )
#    raddr_fsm.If(Ands(ports['myaxi_rvalid'], ports[
#                 'myaxi_rready'], ports['myaxi_rlast'])).goto_next()

    rdata_head = raddr_fsm.current
    raddr_fsm.If(Ands(ack, Not(ports['myaxi_rlast'])))(
        ports['myaxi_rdata'].inc(),
        ports['myaxi_rvalid'](1),
        ports['myaxi_rlast'](0),
        _arlen.dec()
    )
    raddr_fsm.Then().If(_arlen == 0)(
        ports['myaxi_rlast'](1)
    )
    raddr_fsm.Delay(1)(
        ports['myaxi_rvalid'](0),
        ports['myaxi_rlast'](0)
    )
    raddr_fsm.goto_next()
    raddr_fsm.If(Ands(ports['myaxi_rvalid'], Not(ports['myaxi_rready'])))(
        ports['myaxi_rvalid'](ports['myaxi_rvalid']),
        ports['myaxi_rlast'](ports['myaxi_rlast']),
    )
    raddr_fsm.If(Ands(ports['myaxi_rvalid'], ports[
                 'myaxi_rready'])).goto_next()
    raddr_fsm.goto_next()
    raddr_fsm.goto_next()
    raddr_fsm.goto_next()
    raddr_fsm.If((_arlen + 1) & 0xff != 0).goto(rdata_head)
    raddr_fsm.If((_arlen + 1) & 0xff == 0).goto_next()

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
