from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal


# --- to run without installation ---

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

# --- to run without installation ---


from veriloggen import *
from veriloggen.asic import ASICSRAM, asic_sim
from veriloggen.thread import Thread


clock_period = 50
simulation_time = 1_000_000


def make_uut(pdk, datawidth, addrwidth):
    iter_num = 2**addrwidth

    m = Module('asic_sram')
    clk = m.Input('clk')
    rst = m.Input('rst')
    ok = m.OutputReg('ok', initval=0)

    ram = ASICSRAM(m, 'ram', clk, rst, datawidth, addrwidth, pdk=pdk)

    def comp():
        ok_flag = True

        write_sum = 0
        for i in range(iter_num):
            # `i[:4]` rather than `i` is used to avoid overflow
            write_data = i[:4]
            ram.write(i, write_data)
            write_sum += write_data

        read_sum = 0
        for i in range(iter_num):
            read_data = ram.read(i)
            read_sum += read_data
            # `i[:4]` rather than `i` is used to avoid overflow
            if read_data != i[:4]:
                ok_flag = False

        if read_sum != write_sum:
            ok_flag = False

        if ok_flag:
            ok.value = 1

    # `datawidth=32` rather than `datawidth=datawidth`
    # is used to avoid overflow
    thd = Thread(m, 'thd', clk, rst, comp, datawidth=32)
    thd.start()

    return m


def make_tb(pdk, datawidth, addrwidth):
    m = Module('tb')

    uut = Submodule(m, make_uut(pdk, datawidth, addrwidth), 'uut')
    clk = uut['clk']
    rst = uut['rst']
    ok = uut['ok']

    simulation.setup_clock(m, clk, hperiod=clock_period)
    init = simulation.setup_reset(m, rst, m.make_reset(),
                                  period=10 * clock_period)
    init.add(
        Delay(simulation_time),
        If(ok)(
            Display('# verify: PASSED')
        ).Else(
            Display('# verify: FAILED')
        ),
        Finish(),
    )

    return m


def run(
    pdk: Literal['sky130', 'gf180mcu'],
    datawidth: int,
    addrwidth: int,
    simulation_model_path: list[str],
) -> str:
    tb = make_tb(pdk, datawidth, addrwidth)
    rslt = asic_sim(tb, pdk, macro_model_path=simulation_model_path)
    return rslt
