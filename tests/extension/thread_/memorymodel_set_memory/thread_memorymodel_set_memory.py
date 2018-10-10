from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import numpy as np

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)
    myram = vthread.RAM(m, 'myram', clk, rst, datawidth, addrwidth)

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth)

    all_ok = m.TmpReg(initval=0)

    def blink(size):
        # wait start
        saxi.wait_flag(0, value=1, resetvalue=0)
        # reset done
        saxi.write(1, 0)

        all_ok.value = True
        # Test for 4KB boundary check
        offset = 1024 * 16 + (myaxi.boundary_size - 4)
        body(size, offset)

        if all_ok:
            print('# verify (local): PASSED')
        else:
            print('# verify (local): FAILED')

        # result
        saxi.write(2, all_ok)

        # done
        saxi.write_flag(1, 1, resetvalue=0)

    def body(size, offset):
        # read and modify
        laddr = 0
        gaddr = offset
        myaxi.dma_read(myram, laddr, gaddr, size)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata = myram.read(i)
            verify = (offset * 8 // datawidth + i)
            wdata = verify + 1000
            myram.write(i, wdata)
            if vthread.verilog.NotEql(rdata, verify):
                print('rdata[%d] = %d (!= %d)' % (i, rdata, verify))
                all_ok.value = False

        # write
        laddr = 0
        gaddr = offset
        myaxi.dma_write(myram, laddr, gaddr, size)
        print('dma_write: [%d] -> [%d]' % (laddr, gaddr))

        # read (verify)
        laddr = 0
        gaddr = offset
        myaxi.dma_read(myram, laddr, gaddr, size)
        print('dma_read:  [%d] <- [%d]' % (laddr, gaddr))

        for i in range(size):
            rdata = myram.read(i)
            verify = offset * 8 // datawidth + i + 1000
            if vthread.verilog.NotEql(rdata, verify):
                print('rdata[%d] = %d (!= %d)' % (i, rdata, verify))
                all_ok.value = False

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(1024)

    return m


def mkTest(memimg_name=None, memimg_datawidth=32):
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    length = 1024 * 1024 // (memimg_datawidth // 8)
    mem = np.zeros([length], dtype=np.int64)
    data = np.arange(length, dtype=np.int64)
    datawidth = 32
    addr = 0
    axi.set_memory(mem, data, memimg_datawidth, datawidth, addr, None)

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst,
                                memimg=mem, memimg_name=memimg_name,
                                memimg_datawidth=memimg_datawidth)
    memory.connect(ports, 'myaxi')

    # AXI-Slave controller
    _saxi = vthread.AXIMLite(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(ports, 'saxi')

    def ctrl():
        for i in range(100):
            pass

        awaddr = 0
        _saxi.write(awaddr, 1)

        araddr = 4
        v = _saxi.read(araddr)
        while v == 0:
            v = _saxi.read(araddr)

        araddr = 8
        v = _saxi.read(araddr)
        if v:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

        vthread.finish()

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    #simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(1000000),
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
