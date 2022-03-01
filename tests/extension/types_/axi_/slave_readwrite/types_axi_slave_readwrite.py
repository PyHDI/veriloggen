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
    sum = m.Reg('sum', 32, initval=0)

    myaxi = axi.AxiSlave(m, 'myaxi', clk, rst)

    fsm = FSM(m, 'fsm', clk, rst)

    # request
    addr, length, readvalid, writevalid = myaxi.pull_request(cond=fsm)
    rdata = m.Reg('rdata', 32, initval=0)
    rlen = m.Reg('rlen', 32, initval=0)
    rlast = rlen <= 1
    fsm.If(readvalid)(
        rdata(sum + (addr >> 2)),
        rlen(length)
    )
    fsm.If(writevalid).goto(100)
    fsm.If(readvalid).goto_next()

    # read
    ack = myaxi.push_read_data(rdata, rlast, cond=fsm)
    fsm.If(ack)(
        rdata(rdata + 1),
        rlen.dec()
    )
    fsm.If(ack, rlast).goto_next()

    fsm.goto_init()

    # write
    fsm.set_index(100)
    data, mask, valid, last = myaxi.pull_write_data(cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.If(valid, last).goto_next()

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

    _axi = axi.AxiMaster(m, '_axi', clk, rst, noio=True)

    _axi.connect(ports, 'myaxi')

    fsm = FSM(m, 'fsm', clk, rst)

    # write request (1)
    awaddr1 = 1024
    awlen1 = 64
    ack = _axi.write_request(awaddr1, awlen1, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (1)
    wdata1 = m.Reg('wdata1', 32, initval=0)
    wlast1 = wdata1 == awlen1 - 1
    ack = _axi.write_data(wdata1, wlast1, cond=fsm)

    fsm.If(ack)(
        wdata1.inc()
    )
    fsm.If(ack, wlast1).goto_next()

    # write request (2)
    awaddr2 = 1024 + 1024
    awlen2 = 64 + 64
    ack = _axi.write_request(awaddr2, awlen2, cond=fsm)
    fsm.If(ack).goto_next()

    # write data (2)
    wdata2 = m.Reg('wdata2', 32, initval=0)
    wlast2 = wdata2 == awlen2 - 1
    ack = _axi.write_data(wdata2, wlast2, cond=fsm)

    fsm.If(ack)(
        wdata2.inc()
    )
    fsm.If(ack, wlast2).goto_next()
    fsm.If(Not(_axi.wdata.wvalid)).goto_next()

    # read request (1)
    araddr1 = 1024
    arlen1 = 64
    ack = _axi.read_request(araddr1, arlen1, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (1)
    data, valid, last = _axi.read_data(cond=fsm)
    sum = m.Reg('sum', width=32, initval=0)

    fsm.If(valid)(
        sum.add(data)
    )
    fsm.If(valid, last).goto_next()

    # read request (2)
    araddr2 = 1024 + 1024
    arlen2 = 64 + 64
    ack = _axi.read_request(araddr2, arlen2, cond=fsm)
    fsm.If(ack).goto_next()

    # read data (2)
    data, valid, last = _axi.read_data(cond=fsm)

    fsm.If(valid)(
        sum.add(data)
    )
    fsm.If(valid, last).goto_next()

    # verify
    write_sum = (((0 + awlen1 - 1) * awlen1 // 2) +
                 ((0 + awlen2 - 1) * awlen2 // 2))
    expected_sum = (((write_sum + araddr1 // 4 +
                      write_sum + araddr1 // 4 + arlen1 - 1) * arlen1 // 2) +
                    ((write_sum + araddr2 // 4 +
                      write_sum + araddr2 // 4 + arlen2 - 1) * arlen2 // 2))
    fsm(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
    )
    fsm.If(sum == expected_sum)(
        Systask('display', '# verify: PASSED')
    ).Else(
        Systask('display', '# verify: FAILED')
    )
    fsm.goto_next()

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

    # memimg_name = 'memimg_' + outputfile

    # test = mkTest(memimg_name=memimg_name)
    test = mkTest()

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
