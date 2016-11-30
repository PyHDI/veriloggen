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
    myram = ram.SyncRAMManager(m, 'myram', clk, rst, datawidth, addrwidth)

    df = dataflow.DataflowManager(m, clk, rst)
    # df.enable_draw_graph()

    fsm = FSM(m, 'fsm', clk, rst)

    length = 8
    a = df.Counter()
    b = df.Counter(maxval=length)
    c = b == 0

    wport = 0
    waddr = 0
    wlen = 32
    done = myram.write_dataflow(wport, waddr, a, wlen, cond=fsm, when=c)

    fsm.goto_next()
    fsm.If(done).goto_next()

    seq = Seq(m, 'seq', clk, rst)

    seq.If(myram[0].wenable)(
        Systask('display', '[%d] <- %d', myram[0].addr, myram[0].wdata)
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
