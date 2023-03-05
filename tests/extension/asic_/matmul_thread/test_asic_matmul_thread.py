from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal

import pytest

import veriloggen
import asic_matmul_thread


@pytest.mark.parametrize('pdk', ['sky130', 'gf180mcu'])
def test(
    pdk: Literal['sky130', 'gf180mcu'],
    simulation_model_path: dict[Literal['sky130', 'gf180mcu'], list[str]],
):
    veriloggen.reset()
    rslt = asic_matmul_thread.run(
        pdk, simulation_model_path[pdk],
        matrix_size=15, baudrate=20_000_000, clockfreq=200_000_000)
    verify_rslt = rslt.splitlines()[-1]
    assert verify_rslt == '# verify: PASSED'
