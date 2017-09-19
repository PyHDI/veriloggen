from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import math

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))

from veriloggen import *
import veriloggen.types.ram as ram
import veriloggen.dataflow as dataflow


def mkMain(n=128, datawidth=32, numports=2):
    m = Module('main')

    clk = m.Input('CLK')
    rst = m.Input('RST')

    addrwidth = int(math.log(n, 2)) * 2
    myram = ram.SyncRAMManager(m, 'myram', clk, rst, datawidth, addrwidth, 2)
    myram.disable_write(1)

    df = dataflow.DataflowManager(m, clk, rst)
    fsm = FSM(m, 'fsm', clk, rst)

    # dataflow
    value = df.Counter()

    # write dataflow (Dataflow -> RAM)
    wport = 0
    waddr = 0
    wlen = 64
    done = myram.write_dataflow(wport, waddr, value, wlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    fsm.goto_next()

    # read dataflow (RAM -> Dataflow)
    rport = 1
    raddr = 0
    rlen = 32
    rdata, rlast, done = myram.read_dataflow(rport, raddr, rlen, cond=fsm)
    fsm.goto_next()
    fsm.If(done).goto_next()

    # verify
    rdata_data, rdata_valid = rdata.read()
    rlast_data, rlast_valid = rlast.read()

    sum = m.Reg('sum', 32, initval=0)
    expected_sum = (raddr + raddr + rlen - 1) * rlen // 2

    seq = Seq(m, 'seq', clk, rst)

    seq.If(rdata_valid)(
        sum.add(rdata_data)
    )
    seq.Then().If(rlast_data == 1).Delay(1)(
        Systask('display', 'sum=%d expected_sum=%d', sum, expected_sum)
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
