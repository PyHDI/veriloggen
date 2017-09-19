from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.axi as axi
import veriloggen.dataflow as dataflow


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    myaxi = axi.AxiMaster(m, 'myaxi', clk, rst)
    myaxi.disable_read()

    df = dataflow.DataflowManager(m, clk, rst)

    fsm = FSM(m, 'fsm', clk, rst)

    # write request
    awaddr = 1024
    awlen = 64
    ack, counter = myaxi.write_request(awaddr, awlen, cond=fsm)
    fsm.If(ack).goto_next()

    # dataflow
    value = df.Counter()

    # write dataflow (Dataflow -> AXI)
    done = myaxi.write_dataflow(value, counter)
    fsm.If(done).goto_next()

    # verify
    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (awlen - 1) * awlen // 2

    seq = Seq(m, 'seq', clk, rst)
    seq.If(Ands(myaxi.wdata.wvalid, myaxi.wdata.wready))(
        sum.add(myaxi.wdata.wdata)
    )
    seq.Then().If(myaxi.wdata.wlast).Delay(1)(
        Systask('display', "sum=%d expected_sum=%d", sum, expected_sum)
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

    # awready (no stall)
    #awready = ports['myaxi_awready']
    #_awready = m.TmpWireLike(awready)
    #_awready.assign(1)
    #m.Always()( awready(_awready) )

    # wready (nostall)
    #wready = ports['myaxi_wready']
    #_wready = m.TmpWireLike(wready)
    #_wready.assign(1)
    #m.Always()( wready(_wready) )

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
        ports['myaxi_wready'](0),
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
    arready = ports['myaxi_arready']
    _arready = m.TmpWireLike(arready)
    _arready.assign(0)
    m.Always()(arready(_arready))

    # rvalid (no stall)
    rvalid = ports['myaxi_rvalid']
    _rvalid = m.TmpWireLike(rvalid)
    _rvalid.assign(0)
    m.Always()(rvalid(_rvalid))

    # rdata (no stall)
    rdata = ports['myaxi_rdata']
    _rdata = m.TmpWireLike(rdata)
    _rdata.assign(0)
    m.Always()(rdata(_rdata))

    # rlast (no stall)
    rlast = ports['myaxi_rlast']
    _rlast = m.TmpWireLike(rlast)
    _rlast.assign(0)
    m.Always()(rlast(_rlast))

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
