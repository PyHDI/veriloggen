from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal

import pytest

import veriloggen
import asic_sram


@pytest.mark.parametrize('pdk', ['sky130', 'gf180mcu'])
@pytest.mark.parametrize('datawidth', [8, 16, 32])
@pytest.mark.parametrize('addrwidth', list(range(6, 10)))
def test(
    pdk: Literal['sky130', 'gf180mcu'],
    datawidth: int,
    addrwidth: int,
    simulation_model_path: dict[Literal['sky130', 'gf180mcu'], list[str]],
):
    veriloggen.reset()
    rslt = asic_sram.run(pdk, simulation_model_path[pdk], datawidth, addrwidth,
                         clock_period=50, simulation_time=1_000_000)
    verify_rslt = rslt.splitlines()[-1]
    assert verify_rslt == '# verify: PASSED'
