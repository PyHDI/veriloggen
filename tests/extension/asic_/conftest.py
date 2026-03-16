from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Literal

import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def simulation_model_path():
    subprocess.run('git clone https://github.com/VLSIDA/sky130_sram_macros.git',
                   shell=True, check=True)
    subprocess.run('git clone https://github.com/google/globalfoundries-pdk-ip-gf180mcu_fd_ip_sram.git',
                   shell=True, check=True)
    path_dict: dict[Literal['sky130', 'gf180mcu'], list[str]] = {}
    path_dict['sky130'] = [str(p.absolute()) for p in Path('sky130_sram_macros').iterdir() if p.is_dir()]
    path_dict['gf180mcu'] = [str(p.absolute()) for p in Path('globalfoundries-pdk-ip-gf180mcu_fd_ip_sram/cells').iterdir()]
    yield path_dict
    subprocess.run('rm -rf sky130_sram_macros', shell=True, check=True)
    subprocess.run('rm -rf globalfoundries-pdk-ip-gf180mcu_fd_ip_sram',
                   shell=True, check=True)
