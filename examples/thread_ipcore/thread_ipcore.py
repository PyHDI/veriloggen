from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from veriloggen import *
import veriloggen.thread as vthread
import veriloggen.types.axi as axi
import veriloggen.types.ipcore as ipcore


def mkLed():
    m = Module('blinkled')
    clk = m.Input('CLK')
    rst = m.Input('RST')
    led = m.OutputReg('led', 8, initval=0)

    datawidth = 32
    addrwidth = 10

    saxi = vthread.AXISLiteRegister(m, 'saxi', clk, rst, datawidth)

    def wait(fsm, sleep):
        cnt = fsm.m.TmpReg(32, initval=0)
        fsm.If(cnt < sleep)(
            cnt.inc()
        )
        fsm.If(cnt >= sleep)(
            cnt(0)
        )
        fsm.Then().goto_next()

    def blink(size):
        while True:
            # wait start
            saxi.wait_flag(0, value=1, resetvalue=0)
            # reset done
            saxi.write(3, 0)

            sleep = saxi.read(1)
            size = saxi.read(2)

            for i in range(size):
                wait(sleep)
                led.value += 1

            # done
            saxi.write_flag(3, 1, resetvalue=0)

    th = vthread.Thread(m, 'th_blink', clk, rst, blink)
    th.add_intrinsics(wait)
    fsm = th.start(16)

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

    # AXI-Slave controller
    _saxi = vthread.AXIMLite(m, '_saxi', clk, rst, noio=True)
    _saxi.connect(ports, 'saxi')

    # Timer
    counter = m.Reg('counter', 32, initval=0)
    seq = Seq(m, 'seq', clk, rst)
    seq(
        counter.inc()
    )

    def ctrl():
        for i in range(100):
            pass

        awaddr = 4
        sleep = 16
        print('# sleep = %d' % sleep)
        _saxi.write(awaddr, sleep)

        awaddr = 8
        size = 128
        print('# size = %d' % size)
        _saxi.write(awaddr, size)

        awaddr = 0
        start_time = counter
        print('# start time = %d' % start_time)
        _saxi.write(awaddr, 1)

        araddr = 12
        v = _saxi.read(araddr)
        while v == 0:
            v = _saxi.read(araddr)

        end_time = counter
        print('# end time = %d' % end_time)
        time = end_time - start_time
        print('# exec time = %d' % time)

    th = vthread.Thread(m, 'th_ctrl', clk, rst, ctrl)
    fsm = th.start()

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

    return m

if __name__ == '__main__':
    test = mkTest()
    verilog = test.to_verilog('tmp.v')
    print(verilog)

    sim = simulation.Simulator(test)
    rslt = sim.run()
    print(rslt)

    simcode = """

reg [31:0] counter;
always @(posedge sim_clk) begin
  if(!sim_resetn) begin
    counter <= 0;
  end else begin
    counter <= counter + 1;
  end
end

reg [31:0] _start_time;
reg [31:0] _end_time;
reg [31:0] _time;

reg [31:0] _addr;
reg [31:0] _data;
initial begin
  #1000;
  _addr = 4;
  _data = 16;
  $display("# sleep = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_0(_data, _addr);

  _addr = 8;
  _data = 128;
  $display("# size = %d", _data);
  slave_write_ipgen_slave_lite_memory_saxi_0(_data, _addr);

  _addr = 0;
  _data = 1;
  _start_time = counter;
  $display("# start time = %d", _start_time);
  slave_write_ipgen_slave_lite_memory_saxi_0(_data, _addr);

  _addr = 12;
  _data = 0;
  while(_data == 0) begin
    slave_read_ipgen_slave_lite_memory_saxi_0(_data, _addr);
    nclk();
  end
  _end_time = counter;
  $display("# end time = %d", _end_time);
  _time = _end_time - _start_time;
  $display("# exec time = %d", _time);

  #10000;
  $finish;
end
"""

    m = mkLed()
    ipcore.to_ipcore(m, simcode=simcode, iftype='axi')
