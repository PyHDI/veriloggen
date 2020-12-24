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


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    datawidth = 32
    addrwidth = 10
    myaxi = vthread.AXIM(m, 'myaxi', clk, rst, datawidth)

    saxi_length = 4
    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth=datawidth, length=saxi_length)

    ram_src = vthread.RAM(m, 'ram_src', clk, rst, datawidth, addrwidth)
    ram_dst = vthread.RAM(m, 'ram_dst', clk, rst, datawidth, addrwidth)

    strm = vthread.Stream(m, 'mystream', clk, rst)
    src = strm.source('src')
    counter = strm.Counter(initval=0)
    width = strm.parameter('width')
    height = strm.parameter('height')

    # shift x20
    # rotate x10
    # shift, rotate x34
    shift_cond = strm.Or((counter < 20), ((counter >= 30) & (counter & 1 == 0)))
    rotate_cond = strm.Or(((counter >= 20) & (counter < 30)),
                          ((counter >= 30) & (counter & 1 == 1)))

    linebuf = strm.LineBuffer(shape=(3, 3), memlens=[4],
                              data=src, head_initvals=[0], tail_initvals=[3],
                              shift_cond=shift_cond, rotate_conds=[rotate_cond])

    window = [None] * 9
    for y in range(3):
        for x in range(3):
            window[y * 3 + x] = linebuf.get_window(y * 3 + x)

    # The window register contains an invalid value in the beginning
    # because the initial value of shift memory is undefined.
    # Do not output sum until all the window register have valid value.
    dst = strm.Mux(counter < 20, window[8], strm.AddN(*window))
    strm.sink(dst, 'dst')

    # for sequential
    ram_bufs = [vthread.RAM(m, 'ram_buf' + str(i), clk, rst, datawidth, addrwidth)
                for i in range(3)]

    def comp_stream(width, height, offset):
        strm.set_source('src', ram_src, offset, width * height)
        strm.set_sink('dst', ram_dst, offset, width * height)
        strm.set_parameter('width', width)
        strm.set_parameter('height', height)
        strm.run()
        strm.join()

    def comp_sequential(width, height, offset):
        head = 0
        tail = 3
        window_0 = window_1 = window_2 = 0
        window_3 = window_4 = window_5 = 0
        window_6 = window_7 = window_8 = 0

        for i in range(width * height):
            src = ram_src.read(offset + i)
            shift = ((i < 20) or ((i >= 30) and (i & 1 == 0)))
            rotate = (((i >= 20) and (i < 30)) or ((i >= 30) and (i & 1 == 1)))
            if shift:
                ram_bufs[2].write(tail, window_8)
                window_8 = window_7
                window_7 = window_6
                window_6 = ram_bufs[1].read(head)
                ram_bufs[1].write(tail, window_5)
                window_5 = window_4
                window_4 = window_3
                window_3 = ram_bufs[0].read(head)
                ram_bufs[0].write(tail, window_2)
                window_2 = window_1
                window_1 = window_0
                window_0 = src
                head = head + 1 if head < 3 else 0
                tail = tail + 1 if tail < 3 else 0
            elif rotate:
                ram_bufs[2].write(tail, window_8)
                window_8 = window_7
                window_7 = window_6
                window_6 = ram_bufs[2].read(head)
                ram_bufs[1].write(tail, window_5)
                window_5 = window_4
                window_4 = window_3
                window_3 = ram_bufs[1].read(head)
                ram_bufs[0].write(tail, window_2)
                window_2 = window_1
                window_1 = window_0
                window_0 = ram_bufs[0].read(head)
                head = head + 1 if head < 3 else 0
                tail = tail + 1 if tail < 3 else 0
            sum = window_0 + window_1 + window_2 + window_3 + \
                window_4 + window_5 + window_6 + window_7 + window_8
            if i < 20:
                ram_dst.write(offset + i, window_0)
            else:
                ram_dst.write(offset + i, sum)

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
        width = saxi.read(2)
        height = saxi.read(3)
        size = width * height

        offset = 0
        myaxi.dma_read(ram_src, offset, 0, size)
        comp_stream(width, height, offset)
        myaxi.dma_write(ram_dst, offset, 1024, size)

        offset = size
        myaxi.dma_read(ram_src, offset, 0, size)
        comp_sequential(width, height, offset)
        myaxi.dma_write(ram_dst, offset, 2 * 1024, size)

        check(0, offset, size)
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
        width, height = [8, 8]

        awaddr = 2 * 4
        maxi.write(awaddr, width)

        awaddr = 3 * 4
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
