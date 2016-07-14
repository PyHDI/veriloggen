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

    slave = axi.AxiSlave(m, 'slave', clk, rst)
    master = axi.AxiMaster(m, 'master', clk, rst)
    
    ram_a = bram.Bram(m, 'ram_a', clk, rst, numports=1)
    ram_b = bram.Bram(m, 'ram_b', clk, rst, numports=1)
    ram_c = bram.Bram(m, 'ram_c', clk, rst, numports=1)

    fsm = FSM(m, 'fsm', clk, rst)

    # wait for slave request
    slave_addr, slave_counter, slave_valid = slave.pull_write_request(cond=fsm)
    fsm.If(slave_valid).goto_next()

    data, mask, valid, last = slave.pull_write_data(slave_counter, cond=fsm)
    fsm.If(valid).goto_next()

    # computation
    master_addr = 1024
    ram_addr = 0
    length = 64

    dma_done = master.dma_read(ram_a, master_addr, ram_addr, length, cond=fsm)
    fsm.If(dma_done).goto_next()

    master_addr = 1024 * 2

    dma_done = master.dma_read(ram_b, master_addr, ram_addr, length, cond=fsm)
    fsm.If(dma_done).goto_next()

    adata, alast, adone = ram_a.read_dataflow(0, ram_addr, length, cond=fsm)
    bdata, blast, bdone = ram_b.read_dataflow(0, ram_addr, length, cond=fsm)
    
    cdata = adata + bdata

    done = ram_c.write_dataflow(0, ram_addr, cdata, length, cond=fsm)
    fsm.goto_next()
    
    fsm.If(done).goto_next()

    master_addr = 1024 * 3

    dma_done = master.dma_write(ram_c, master_addr, ram_addr, length, cond=fsm)
    fsm.If(dma_done).goto_next()

    # checksum
    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (((1024 + 1024 + 63) * 64 // 2) +
                    ((1024 * 2 + 1024 * 2 + 63) * 64 // 2))

    seq = Seq(m, 'seq', clk, rst)
    seq.If(fsm.state == 0)(
        sum(0)
    )
    seq.If(master.wdata.wvalid, master.wdata.wready)(
        sum(sum + master.wdata.wdata)
    )
    seq.If(master.wdata.wvalid, master.wdata.wready, master.wdata.wlast).Delay(1)(
        Systask('display', "sum=%d expected_sum=%d", sum, expected_sum)
    )

    fsm.If(master.wdata.wvalid, master.wdata.wready,
           master.wdata.wlast).Delay(1).goto_next()

    # return the checksum
    slave_addr, slave_counter, slave_valid = slave.pull_read_request(cond=fsm)
    fsm.If(slave_valid).goto_next()

    ack, last = slave.push_read_data(sum, slave_counter, cond=fsm)
    fsm.If(last).goto_next()

    # repeat
    fsm.goto_init()

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

    #--------------------------------------------------------------------------
    # Master

    # awready (no stall)
    #awready = ports['master_awready']
    #_awready = m.TmpWireLike(awready)
    #_awready.assign(1)
    # m.Always()(awready(_awready))

    # wready (nostall)
    #wready = ports['master_wready']
    #_wready = m.TmpWireLike(wready)
    #_wready.assign(1)
    # m.Always()(wready(_wready))

    # awready (with stall)
    waddr_fsm = FSM(m, 'waddr', clk, rst)
    _awlen = m.Reg('_awlen', 32, initval=0)

    waddr_fsm(
        ports['master_awready'](0),
        ports['master_wready'](0),
        _awlen(0)
    )
    waddr_fsm.If(ports['master_awvalid']).goto_next()

    waddr_fsm.If(ports['master_awvalid'])(
        ports['master_awready'](1)
    )
    waddr_fsm.goto_next()

    waddr_fsm(
        ports['master_awready'](0),
        _awlen(ports['master_awlen'])
    )
    waddr_fsm.goto_next()

    # wready (with stall)
    waddr_init = waddr_fsm.current
    waddr_fsm(
        ports['master_wready'](0)
    )
    waddr_fsm.If(ports['master_wvalid']).goto_next()

    waddr_fsm.If(ports['master_wvalid'])(
        ports['master_wready'](1)
    )
    waddr_fsm.goto_next()

    waddr_fsm(
        ports['master_wready'](0)
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
#        ports['master_wready'](1)
#    )
#    waddr_fsm.Delay(1)(
#        ports['master_wready'](0)
#    )
#    waddr_fsm.If(ports['master_wvalid'])(
#        _awlen.dec()
#    )
#    waddr_fsm.Then().If(_awlen == 0).goto_next()

    # arready (no stall)
    #arready = ports['master_arready']
    #_arready = m.TmpWireLike(arready)
    #_arready.assign(0)
    #m.Always()( arready(_arready) )

    # arready, rvalid, rdata, rlast
    raddr_fsm = FSM(m, 'raddr', clk, rst)
    _arlen = m.Reg('_arlen', 32, initval=0)
    raddr_fsm(
        ports['master_arready'](0),
        ports['master_rdata'](-1),
        ports['master_rvalid'](0),
        ports['master_rlast'](0)
    )
    raddr_fsm.If(ports['master_arvalid']).goto_next()

    raddr_fsm.If(ports['master_arvalid'])(
        ports['master_arready'](1),
        ports['master_rdata'](ports['master_araddr'] - 1)
    )
    raddr_fsm.goto_next()

    raddr_fsm(
        ports['master_arready'](0),
        _arlen(ports['master_arlen'])
    )
    raddr_fsm.goto_next()

    ack = Ors(ports['master_rready'], Not(ports['master_rvalid']))

    # nodelay
#    raddr_fsm.If(Ands(ack, Not(ports['master_rlast'])))(
#        ports['master_rdata'].inc(),
#        ports['master_rvalid'](1),
#        ports['master_rlast'](0),
#        _arlen.dec()
#    )
#    raddr_fsm.Then().If(_arlen == 0)(
#        ports['master_rlast'](1),
#    )
#    raddr_fsm.Delay(1)(
#        ports['master_rvalid'](0),
#        ports['master_rlast'](0)
#    )
#    raddr_fsm.If(Ands(ports['master_rvalid'], Not(ports['master_rready'])))(
#        ports['master_rvalid'](ports['master_rvalid']),
#        ports['master_rlast'](ports['master_rlast']),
#    )
#    raddr_fsm.If(Ands(ports['master_rvalid'], ports[
#                 'master_rready'], ports['master_rlast'])).goto_next()

    rdata_head = raddr_fsm.current
    raddr_fsm.If(Ands(ack, Not(ports['master_rlast'])))(
        ports['master_rdata'].inc(),
        ports['master_rvalid'](1),
        ports['master_rlast'](0),
        _arlen.dec()
    )
    raddr_fsm.Then().If(_arlen == 0)(
        ports['master_rlast'](1)
    )
    raddr_fsm.Delay(1)(
        ports['master_rvalid'](0),
        ports['master_rlast'](0)
    )
    raddr_fsm.goto_next()
    raddr_fsm.If(Ands(ports['master_rvalid'], Not(ports['master_rready'])))(
        ports['master_rvalid'](ports['master_rvalid']),
        ports['master_rlast'](ports['master_rlast']),
    )
    raddr_fsm.If(Ands(ports['master_rvalid'], ports[
                 'master_rready'])).goto_next()
    raddr_fsm.goto_next()
    raddr_fsm.goto_next()
    raddr_fsm.goto_next()
    raddr_fsm.If((_arlen + 1) & 0xff != 0).goto(rdata_head)
    raddr_fsm.If((_arlen + 1) & 0xff == 0).goto_next()

    raddr_fsm.goto_next()

    raddr_fsm.goto_init()


    #--------------------------------------------------------------------------
    # Slave
    awvalid = ports['slave_awvalid']
    _awvalid = m.TmpWireLike(awvalid)
    _awvalid.assign(1)  # on
    m.Always()(awvalid(_awvalid))

    awaddr = ports['slave_awaddr']
    _awaddr = m.TmpWireLike(awaddr)
    _awaddr.assign(0x100)  # on
    m.Always()(awaddr(_awaddr))

    awlen = ports['slave_awlen']
    _awlen = m.TmpWireLike(awlen)
    _awlen.assign(0)  # on
    m.Always()(awlen(_awlen))

    arvalid = ports['slave_arvalid']
    _arvalid = m.TmpWireLike(arvalid)
    _arvalid.assign(1)  # on
    m.Always()(arvalid(_arvalid))

    araddr = ports['slave_araddr']
    _araddr = m.TmpWireLike(araddr)
    _araddr.assign(0x100)  # on
    m.Always()(araddr(_araddr))

    arlen = ports['slave_arlen']
    _arlen = m.TmpWireLike(arlen)
    _arlen.assign(0)  # on
    m.Always()(arlen(_arlen))

    wvalid = ports['slave_wvalid']
    _wvalid = m.TmpWireLike(wvalid)
    _wvalid.assign(1)  # on
    m.Always()(wvalid(_wvalid))

    wdata = ports['slave_wdata']
    _wdata = m.TmpWireLike(wdata)
    _wdata.assign(0x200)  # on
    m.Always()(wdata(_wdata))

    wstrb = ports['slave_wstrb']
    _wstrb = m.TmpWireLike(wstrb)
    _wstrb.assign(Repeat(Int(1, 1), 32 // 8))  # on
    m.Always()(wstrb(_wstrb))

    wlast = ports['slave_wlast']
    _wlast = m.TmpWireLike(wlast)
    _wlast.assign(1)  # on
    m.Always()(wlast(_wlast))

    rready = ports['slave_rready']
    _rready = m.TmpWireLike(rready)
    _rready.assign(1)  # on
    m.Always()(rready(_rready))

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
