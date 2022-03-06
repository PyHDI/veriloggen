from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.thread as vthread


def mkTop(numthreads=64, clk_name='clk', rst_name='btnCpuReset'):
    m = Module('top')
    clk = m.Input(clk_name)
    rst = m.Input(rst_name)

    new_clk = m.Wire('new_CLK')
    new_clk.assign(clk)

    rstbuf = m.Reg('RST_X')
    new_rst = m.Reg('RST')
    m.Always(Posedge(clk))(
        rstbuf(rst),
        new_rst(Not(rstbuf))
    )

    btnc = m.Input('btnC')
    btnu = m.Input('btnU')
    btnl = m.Input('btnL')
    btnr = m.Input('btnR')
    btnd = m.Input('btnD')
    sw = m.Input('sw', 16)
    led = m.Output('led', 16)

    blinkled = mkLed(numthreads)

    ports = []
    ports.append(('CLK', new_clk))
    ports.append(('RST', new_rst))
    ports.append(('btnC', btnc))
    ports.append(('btnU', btnu))
    ports.append(('btnL', btnl))
    ports.append(('btnR', btnr))
    ports.append(('btnD', btnd))
    ports.append(('sw', sw))
    ports.append(('led', led))

    m.Instance(blinkled, 'inst_' + blinkled.name, ports=ports)

    return m


def mkLed(numthreads=64):
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')

    btnc = m.Input('btnC')
    btnu = m.Input('btnU')
    btnl = m.Input('btnL')
    btnr = m.Input('btnR')
    btnd = m.Input('btnD')
    sw = m.Input('sw', 16)
    led = m.Output('led', 16)

    count = vthread.Shared(m.Reg('count', 15, initval=0))
    done = m.Reg('done', initval=0)
    led.assign(Cat(done, count.value))

    mymutex = vthread.Mutex(m, 'mymutex', clk, rst)

    def sleep(time):
        for i in range(time):
            for _ in range(1024):
                pass  # sleep

    def myfunc(tid):
        mymutex.lock()
        print("Thread %d Lock" % tid)

        sleep(sw)

        count.write(count.value + 1)
        print("Thread %d count = %d" % (tid, count.value))

        mymutex.unlock()
        print("Thread %d Unlock" % tid)

    def wait_start(polarity=True):
        while btnc != polarity:
            pass

    def blink():
        count.write(0)

        while True:
            done.value = 0
            wait_start()

            for tid in range(numthreads):
                pool.run(tid, tid)

            for tid in range(numthreads):
                pool.join(tid)

            for tid in range(numthreads):
                pool.reset(tid)

            done.value = 1

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    pool = vthread.ThreadPool(m, 'th_myfunc', clk, rst, myfunc, numthreads)
    fsm = th.start()

    return m


def mkTest():
    m = Module('test')

    # target instance
    led = mkLed()

    # copy paras and ports
    params = m.copy_params(led)
    ports = m.copy_sim_ports(led)

    clk = ports['CLK']
    rst = ports['RST']

    btnc = ports['btnC']
    sw = ports['sw']

    done = ports['led'][-1]

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(100000),
        Systask('finish'),
    )

    def test():
        sw.value = 0
        btnc.value = 0
        btnc.value = 1

        for i in range(4):
            sw.value = i
            btnc.value = 0
            btnc.value = 1

            while not done:
                pass

    th = vthread.Thread(m, 'test', clk, rst, test)
    th.start()

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    # for Nexys4 synthesis
    top = mkTop()
    verilog = top.to_verilog('thread_nexys4.v')
