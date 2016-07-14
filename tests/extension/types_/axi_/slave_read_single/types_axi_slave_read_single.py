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

    myaxi = axi.AxiSlave(m, 'myaxi', clk, rst)
    myaxi.disable_write()

    fsm = FSM(m, 'fsm', clk, rst)

    # read address
    addr, counter, valid = myaxi.pull_read_request(cond=fsm)
    fsm.If(valid).goto_next()

    # read rdata
    rdata = m.Reg('rdata', 32, initval=512)
    fsm.goto_next()

    ack, last = myaxi.push_read_data(rdata, counter, cond=fsm)
    fsm.If(ack)(
        rdata(rdata + 512)
    )
    fsm.If(last).goto_next()

    fsm.If(rdata < 4096).goto_init()
    fsm.If(rdata >= 4096).goto_next()

    seq = Seq(m, 'seq', clk, rst)
    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (512 + 512 * 7) * 7 // 2
    
    seq.If(myaxi.rdata.rvalid, myaxi.rdata.rready)(
        sum(sum + myaxi.rdata.rdata)
    )
    
    fsm(
        Systask('display', "sum=%d expected_sum=%d", sum, expected_sum)
    )
    fsm.goto_next()
    
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

    awvalid = ports['myaxi_awvalid']
    _awvalid = m.TmpWireLike(awvalid)
    _awvalid.assign(0)
    m.Always()(awvalid(_awvalid))

    awaddr = ports['myaxi_awaddr']
    _awaddr = m.TmpWireLike(awaddr)
    _awaddr.assign(0)
    m.Always()(awaddr(_awaddr))

    awlen = ports['myaxi_awlen']
    _awlen = m.TmpWireLike(awlen)
    _awlen.assign(0)
    m.Always()(awlen(_awlen))

    arvalid = ports['myaxi_arvalid']
    _arvalid = m.TmpWireLike(arvalid)
    _arvalid.assign(1)  # on
    m.Always()(arvalid(_arvalid))

    araddr = ports['myaxi_araddr']
    _araddr = m.TmpWireLike(araddr)
    _araddr.assign(0x100)  # on
    m.Always()(araddr(_araddr))

    arlen = ports['myaxi_arlen']
    _arlen = m.TmpWireLike(arlen)
    _arlen.assign(0)  # on
    m.Always()(arlen(_arlen))

    wvalid = ports['myaxi_wvalid']
    _wvalid = m.TmpWireLike(wvalid)
    _wvalid.assign(0)
    m.Always()(wvalid(_wvalid))

    wdata = ports['myaxi_wdata']
    _wdata = m.TmpWireLike(wdata)
    _wdata.assign(0)
    m.Always()(wdata(_wdata))

    wstrb = ports['myaxi_wstrb']
    _wstrb = m.TmpWireLike(wstrb)
    _wstrb.assign(Repeat(Int(1, 1), 32 // 8))
    m.Always()(wstrb(_wstrb))

    wlast = ports['myaxi_wlast']
    _wlast = m.TmpWireLike(wlast)
    _wlast.assign(0)
    m.Always()(wlast(_wlast))

    rready = ports['myaxi_rready']
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
