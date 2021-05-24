from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.axi as axi
from veriloggen.thread import RAM
import veriloggen.dataflow as dataflow


def mkMain():
    m = Module('main')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    myaxi = axi.AxiMaster(m, 'myaxi', clk, rst)
    myaxi.disable_write()

    myram = RAM(m, 'myram', clk, rst, numports=1)

    df = dataflow.DataflowManager(m, clk, rst)
    fsm = FSM(m, 'fsm', clk, rst)

    # AXI read request
    araddr = 1024
    arlen = 64
    ack, axi_counter = myaxi.read_request_counter(araddr, arlen, cond=fsm)
    fsm.If(ack).goto_next()

    # AXI read dataflow (AXI -> Dataflow)
    axi_data, axi_last, done = myaxi.read_dataflow()
    sum = df.ReduceAdd(axi_data, reset=axi_last.prev(1))

    # RAM write dataflow (Dataflow -> RAM)
    wport = 0
    waddr = 0
    wlen = arlen
    done = myram.write_dataflow(wport, waddr, sum, wlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    # verify
    # read dataflow (RAM -> Dataflow)
    rport = 0
    raddr = 0
    rlen = arlen
    rdata, rlast, done = myram.read_dataflow(rport, raddr, rlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    rdata_data, rdata_valid = rdata.read()
    rlast_data, rlast_valid = rlast.read()

    sum = m.Reg('sum', 32, initval=0)
    expected_sum = 0
    for i in range(arlen):
        expected_sum += (araddr + araddr + i) * (i + 1) // 2

    seq = Seq(m, 'seq', clk, rst)

    seq.If(rdata_valid)(
        sum.add(rdata_data)
    )
    seq.Then().If(rlast_data == 1).Delay(1)(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum),
        If(NotEql(sum, expected_sum))(Display('# verify: FAILED')).Else(Display('# verify: PASSED'))
    )

    return m


def mkTest(memimg_name=None):
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
    raddr_fsm.If(Ands(ports['myaxi_rvalid'],
                      ports['myaxi_rready'])).goto_next()
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

    # simulation.setup_waveform(m, uut, m.get_vars())
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000 * 100),
        Systask('finish'),
    )

    return m


def run(filename='tmp.v', simtype='iverilog', outputfile=None):

    if outputfile is None:
        outputfile = os.path.splitext(os.path.basename(__file__))[0] + '.out'

    memimg_name = 'memimg_' + outputfile

    test = mkTest(memimg_name=memimg_name)

    if filename is not None:
        test.to_verilog(filename)

    sim = simulation.Simulator(test, sim=simtype)
    rslt = sim.run(outputfile=outputfile)
    lines = rslt.splitlines()
    if simtype == 'verilator' and lines[-1].startswith('-'):
        rslt = '\n'.join(lines[:-1])
    return rslt


if __name__ == '__main__':
    rslt = run(filename='tmp.v')
    print(rslt)
