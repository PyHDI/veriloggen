from veriloggen import *
from veriloggen.asic import ASICSRAM, generate_configs, asic_sim
from veriloggen.thread import Thread


pdk = 'sky130'  # sky130 or gf180mcu
pdk_root = '/Users/mu/research/google/OpenLane/pdks'  # change this path

datawidth = 16
addrwidth = 9

iter_num = 512

clock_period = 50
simulation_time = 1_000_000
die_shape = (1000, 1000)


def make_uut():
    m = Module('asic_sram')
    clk = m.Input('clk')
    rst = m.Input('rst')
    ok = m.OutputReg('ok', initval=0)

    ram = ASICSRAM(m, 'ram', clk, rst, datawidth, addrwidth, pdk=pdk)

    def comp():
        ok_flag = True

        write_sum = 0
        for i in range(iter_num):
            write_data = i
            ram.write(i, write_data)
            write_sum += write_data

        read_sum = 0
        for i in range(iter_num):
            read_data = ram.read(i)
            read_sum += read_data
            if read_data != i:
                ok_flag = False

        if read_sum != write_sum:
            ok_flag = False

        if ok_flag:
            ok.value = 1

    thd = Thread(m, 'thd', clk, rst, comp, datawidth=datawidth)
    thd.start()

    return m


def make_tb():
    m = Module('tb')

    uut = Submodule(m, make_uut(), 'uut')
    clk = uut['clk']
    rst = uut['rst']
    ok = uut['ok']

    simulation.setup_clock(m, clk, hperiod=clock_period)
    init = simulation.setup_reset(m, rst, m.make_reset(),
                                  period=10 * clock_period)
    init.add(
        Delay(simulation_time),
        If(ok)(
            Display('PASSED')
        ).Else(
            Display('FAILED')
        ),
        Finish(),
    )

    return m


def run():
    make_uut().to_verilog('asic_sram.v')
    generate_configs('asic_sram.v', 'asic_sram', 'clk',
                    clock_period, die_shape, pdk=pdk, pdk_root=pdk_root)

    print(asic_sim(make_tb(), pdk=pdk, pdk_root=pdk_root))


if __name__ == '__main__':
    run()
