from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import functools

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi
import veriloggen.types.util as util


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)

    saxi_length = 5
    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth=datawidth, length=saxi_length)

    ram_src = vthread.RAM(m, 'ram_src', clk, rst, datawidth, addrwidth)
    ram_dummy_src = vthread.RAM(m, 'ram_dummy_src', clk, rst, datawidth, addrwidth)
    ram_dst = vthread.RAM(m, 'ram_dst', clk, rst, datawidth, addrwidth)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    dummy_src = strm.source('dummy_src')
    c = strm.Counter(initval=0, size=4)
    x = strm.Counter(initval=0, size=8, enable=(c == 3))
    y = strm.Counter(initval=0, size=8, enable=((c == 3) & (x == 7)))

    shift_cond = (x & 1 == 0) & ((y & 1) == 0)
    rotate_cond1 = (((((x & 1) == 0) & ((y & 1) == 0)) == 0) & (((x & 1) == 0) == 0))
    rotate_cond2 = (((((x & 1) == 0) & ((y & 1) == 0)) == 0) & ((x & 1) == 0))
    read_cond = shift_cond
    addrcounter = strm.Counter(initval=0, enable=read_cond)
    src = strm.read_RAM('ram_src', addr=addrcounter, when=read_cond, datawidth=datawidth)
    counter = strm.Counter(initval=0)
    width = strm.parameter('width')
    height = strm.parameter('height')

    linebuf = strm.LineBuffer(shape=(1, 1, 1), memlens=[4, 13],
                              head_initvals=[0, 0], tail_initvals=[3, 12],
                              data=src, shift_cond=shift_cond,
                              rotate_conds=[rotate_cond1, rotate_cond2])
    dst = linebuf.get_window(0)

    strm.sink(dst, 'dst')

    # add a stall condition
    count = m.Reg('count', 4, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        count.inc()
    )

    util.add_disable_cond(strm.oready, 1, count == 0)

    def comp_stream(channel, width, height, offset):
        strm.set_source('dummy_src', ram_dummy_src, offset, channel * width * height * 2 * 2)
        strm.set_read_RAM('ram_src', ram_src)
        strm.set_sink('dst', ram_dst, offset, channel * width * height * 2 * 2)
        strm.set_parameter('width', width)
        strm.set_parameter('height', height)
        strm.run()
        strm.join()

    def comp_sequential(channel, width, height, roffset, woffset):
        for yy in range(height * 2):
            for xx in range(width * 2):
                for c in range(channel):
                    # f(c, x, y) = in(c, x/2, y/2);
                    src_i = (xx // 2) * channel + (yy // 2) * width * channel + c
                    dst_i = xx * channel + yy * width * 2 * channel + c
                    val = ram_src.read(roffset + src_i)
                    ram_dst.write(woffset + dst_i, val)

    def check(offset_stream, offset_seq, size):
        all_ok = True
        for i in range(size):
            st = ram_dst.read(offset_stream + i)
            sq = ram_dst.read(offset_seq + i)
            if vthread.verilog.NotEql(st, sq):
                all_ok = False
        if all_ok:
            print('# verify: PASSED')
        else:
            print('# verify: FAILED')

    def comp():
        saxi.write(addr=1, value=0)
        saxi.wait_flag(0, value=1, resetvalue=0)
        channel = saxi.read(2)
        width = saxi.read(3)
        height = saxi.read(4)
        insize = channel * width * height
        outsize = channel * width * 2 * height * 2

        roffset = 0
        woffset = 0
        myaxi.dma_read(ram_src, roffset, 0, insize)
        comp_stream(channel, width, height, roffset)
        myaxi.dma_write(ram_dst, woffset, 1024, outsize)

        roffset = insize
        woffset = outsize
        myaxi.dma_read(ram_src, roffset, 0, insize)
        comp_sequential(channel, width, height, roffset, woffset)
        myaxi.dma_write(ram_dst, woffset, 2 * 1024, outsize)

        check(0, woffset, outsize)
        saxi.write(addr=1, value=1)

    th = vthread.Thread(m, 'th_comp', clk, rst, comp)
    fsm = th.start()

    return m


def mkTest(memimg_name=None):
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    memory = axi.AxiMemoryModel(m, 'memory', clk, rst, memimg_name=memimg_name)
    memory.connect(ports, 'myaxi')
    maxi = vthread.AXIMLite(m, 'maxi', clk, rst, noio=True)
    maxi.connect(ports, 'saxi')

    def ctrl():
        channel, width, height = [4, 4, 4]

        awaddr = 2 * 4
        maxi.write(awaddr, channel)

        awaddr = 3 * 4
        maxi.write(awaddr, width)

        awaddr = 4 * 4
        maxi.write(awaddr, height)

        awaddr = 0 * 4
        maxi.write(awaddr, 1)

        araddr = 1 * 4
        v = maxi.read(araddr)
        while v == 0:
            v = maxi.read(araddr)
        vthread.finish()

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # simulation.setup_waveform(m, uut)
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
