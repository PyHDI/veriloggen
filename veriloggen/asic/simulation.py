from typing import Literal
from pathlib import Path
from veriloggen.core.module import Module
from veriloggen.simulation.simulation import run_iverilog


def asic_sim(
    test_bench: Module,
    pdk: Literal['sky130', 'gf180mcu', 'sky130A', 'sky130B', 'gf180mcuA', 'gf180mcuB', 'gf180mcuC'] | None = None,
    pdk_root: str | None = None,
    macro_model_path: str | None = None,
):
    if pdk is not None:
        if pdk not in ['sky130', 'gf180mcu', 'sky130A', 'sky130B', 'gf180mcuA', 'gf180mcuB', 'gf180mcuC']:
            raise ValueError(f'Invalid PDK: {pdk}')
        if pdk == 'sky130':
            # sky130A is default for sky130
            pdk += 'A'
        if pdk == 'gf180mcu':
            # gf180mcuC is default for gf180mcu
            pdk += 'C'
    if macro_model_path is None and pdk is not None:
        if pdk_root is None:
            raise RuntimeError('`pdk_root` is necessary')
        if pdk.startswith('sky130'):
            macro_model_path = str(Path(pdk_root) / pdk / 'libs.ref' / 'sky130_sram_macros' / 'verilog')
        if pdk.startswith('gf180mcu'):
            macro_model_path = str(Path(pdk_root) / pdk / 'libs.ref' / 'gf180mcu_fd_ip_sram' / 'verilog')

    if macro_model_path is None:
        return run_iverilog([test_bench])
    else:
        return run_iverilog([test_bench], libdir=[macro_model_path])
