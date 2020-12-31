from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

from veriloggen import *
import veriloggen.thread as vthread


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('LED', 8, initval=0)

    count = m.Reg('count', 8, initval=0)

    def blink(times):
        led.value = 0
        count.value = 0
        for i in range(times):
            for x in range(8):
                # pointer
                led.value[x] = count[x]
            print("led = ", led)
            count.value += 1

        led.value = 0
        count.value = 0
        for i in range(times):
            # slice
            led.value = count[0:2]
            print("led = ", led)
            count.value += 1

        led.value = 0
        count.value = 0
        for i in range(times):
            # slice with step
            led.value = count[0:8:2]
            print("led = ", led)
            count.value += 1

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    fsm = th.start(10)

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

    uut = m.Instance(led, 'uut',
                     params=m.connect_params(led),
                     ports=m.connect_ports(led))

    # simulation.setup_waveform(m, uut)
    simulation.setup_clock(m, clk, hperiod=5)
    init = simulation.setup_reset(m, rst, m.make_reset(), period=100)

    init.add(
        Delay(10000),
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
