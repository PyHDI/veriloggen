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
    sum = m.OutputReg('sum', 32, initval=0)

    myaxi = axi.AxiLiteSlave(m, 'myaxi', clk, rst)

    fsm = FSM(m, 'fsm', clk, rst)

    # request
    addr, readvalid, writevalid = myaxi.pull_request(cond=fsm)
    rdata = m.Reg('rdata', 32, initval=0)
    fsm.If(readvalid)(
        rdata(addr >> 2),
    )
    fsm.If(writevalid).goto(100)
    fsm.If(readvalid).goto_next()

    # read
    ack = myaxi.push_read_data(rdata, cond=fsm)
    fsm.If(ack)(
        rdata(rdata + 1),
    )
    fsm.If(ack).goto_next()

    fsm.goto_init()

    # write
    fsm.set_index(100)
    data, mask, valid = myaxi.pull_write_data(cond=fsm)

    fsm.If(valid)(
        sum(sum + data)
    )
    fsm.If(valid).goto_next()

    fsm.goto_init()

    return m


def mkTest():
    m = Module('test')

    # target instance
    main = mkMain()

    # copy paras and ports
    params = m.copy_params(main)
    ports = m.copy_sim_ports(main)
    sum = ports['sum']

    clk = ports['CLK']
    rst = ports['RST']

    _axi = axi.AxiLiteMaster(m, '_axi', clk, rst, noio=True)

    _axi.connect(ports, 'myaxi')

    # read
    read_fsm = FSM(m, 'read_fsm', clk, rst)

    # read request (1)
    araddr1 = 1024
    ack = _axi.read_request(araddr1, cond=read_fsm)
    read_fsm.If(ack).goto_next()

    # read data (1)
    data, valid = _axi.read_data(cond=read_fsm)
    rsum = m.Reg('rsum', width=32, initval=0)

    read_fsm.If(valid)(
        rsum.add(data)
    )
    read_fsm.If(valid).goto_next()

    # read request (2)
    araddr2 = 1024 + 1024
    ack = _axi.read_request(araddr2, cond=read_fsm)
    read_fsm.If(ack).goto_next()

    # read data (2)
    data, valid = _axi.read_data(cond=read_fsm)

    read_fsm.If(valid)(
        rsum.add(data)
    )
    read_fsm.If(valid).goto_next()

    # write
    write_fsm = FSM(m, 'write_fsm', clk, rst)

    # write request (1)
    awaddr1 = 1024
    ack = _axi.write_request(awaddr1, cond=write_fsm)
    write_fsm.If(ack).goto_next()

    # write data (1)
    wdata1 = 100
    ack = _axi.write_data(wdata1, cond=write_fsm)

    write_fsm.If(ack).goto_next()

    # write request (2)
    awaddr2 = 1024 + 1024
    ack = _axi.write_request(awaddr2, cond=write_fsm)
    write_fsm.If(ack).goto_next()

    # write data (2)
    wdata2 = 200
    ack = _axi.write_data(wdata2, cond=write_fsm)

    write_fsm.If(ack).goto_next()
    write_fsm.If(Not(_axi.wdata.wvalid)).goto_next()

    # verify
    fsm = FSM(m, 'fsm', clk, rst)
    fsm.If(read_fsm.here, write_fsm.here).goto_next()

    expected_rsum = araddr1 // 4 + araddr2 // 4
    expected_wsum = 100 + 200

    fsm(
        Systask('display', 'rsum=%d expected_rsum=%d', rsum, expected_rsum)
    )
    fsm(
        Systask('display', 'wsum=%d expected_wsum=%d', sum, expected_wsum)
    )
    fsm.If(rsum == expected_rsum, sum == expected_wsum)(
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
