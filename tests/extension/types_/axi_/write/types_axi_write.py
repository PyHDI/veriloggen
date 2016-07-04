from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

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
    myaxi.disable_read()
    
    fsm = FSM(m, 'fsm', clk, rst)

    # write address
    awaddr = 1024
    awlen = 64

    ack, counter = myaxi.write_request(awaddr, awlen, cond=fsm)
    fsm.If(ack).goto_next()

    # write data
    wdata = m.Reg('wdata', 32, initval=0)

    ack, last = myaxi.write_data(wdata, counter, cond=fsm)

    fsm.If(ack)(
        wdata.inc()
    )
    fsm.Then().If(last).goto_next()

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
    #awready = ports['myaxi_awready']
    #_awready = m.TmpWireLike(awready)
    #_awready.assign(1)
    #m.Always()( awready(_awready) )

    # awready (with stall)
    waddr_fsm = FSM(m, 'waddr', clk, rst)
    waddr_fsm(
        ports['myaxi_awready'](0)
    )
    waddr_fsm.If(ports['myaxi_awvalid']).goto_next()
    waddr_fsm.If(ports['myaxi_awvalid'])(
        ports['myaxi_awready'](1)
    )
    waddr_fsm.goto_next()
    waddr_fsm(
        ports['myaxi_awready'](0)
    )
    waddr_fsm.goto_init()
    waddr_fsm.make_always()

    
    # wready (nostall)
    #wready = ports['myaxi_wready']
    #_wready = m.TmpWireLike(wready)
    #_wready.assign(1)
    #m.Always()( wready(_wready) )

    # wready (with stall)
    wdata_fsm = FSM(m, 'wdata', clk, rst)
    wdata_fsm(
        ports['myaxi_wready'](0)
    )
    wdata_fsm.If(ports['myaxi_wvalid']).goto_next()
    wdata_fsm.If(ports['myaxi_wvalid'])(
        ports['myaxi_wready'](1)
    )
    wdata_fsm.goto_next()
    wdata_fsm(
        ports['myaxi_wready'](0)
    )
    wdata_fsm.goto_init()
    wdata_fsm.make_always()


    # arready (no stall)
    arready = ports['myaxi_arready']
    _arready = m.TmpWireLike(arready)
    _arready.assign(0)
    m.Always()( arready(_arready) )

    # rvalid (no stall)
    rvalid = ports['myaxi_rvalid']
    _rvalid = m.TmpWireLike(rvalid)
    _rvalid.assign(0)
    m.Always()( rvalid(_rvalid) )

    # rdata (no stall)
    rdata = ports['myaxi_rdata']
    _rdata = m.TmpWireLike(rdata)
    _rdata.assign(0)
    m.Always()( rdata(_rdata) )

    # rlast (no stall)
    rlast = ports['myaxi_rlast']
    _rlast = m.TmpWireLike(rlast)
    _rlast.assign(0)
    m.Always()( rlast(_rlast) )

    
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
