import json
from typing import Literal
from warnings import warn
from pathlib import Path
import re
from rectpack import newPacker, SORT_NONE
from pyverilog.vparser import ast as vast
from pyverilog.vparser.parser import VerilogParser


def place_macros(
    macro_shapes: list[tuple[int | float, int | float]],
    die_shape: tuple[int | float, int | float],
    halo_min: int | float = 0,
    halo_max: int | float | None = None,
    threshold: int | float = 0.1,
    allow_rotation: bool = False,
) -> list[tuple[float, float, bool]]:
    if halo_max is None:
        halo_max = max(die_shape)
    halo_lb = halo_min
    halo_ub = halo_max
    while halo_ub - halo_lb > threshold:
        halo = (halo_lb + halo_ub) / 2
        packer = newPacker(sort_algo=SORT_NONE, rotation=allow_rotation)
        for width, height in macro_shapes:
            packer.add_rect(width + 2*halo, height + 2*halo)
        packer.add_bin(*die_shape)
        packer.pack()
        if len(packer.rect_list()) == len(macro_shapes):
            halo_lb = halo
        else:
            halo_ub = halo
    halo = halo_lb
    packer = newPacker(sort_algo=SORT_NONE, rotation=allow_rotation)
    for width, height in macro_shapes:
        packer.add_rect(width + 2*halo, height + 2*halo)
    packer.add_bin(*die_shape)
    packer.pack()
    result: list[tuple[float, float, bool]] = []
    for (width, height), (_, x, y, w, h, _) in zip(macro_shapes, packer.rect_list()):
        if (allow_rotation and
            (w - height - 2*halo)**2 + (h - width - 2*halo)**2 < (w - width - 2*halo)**2 + (h - height - 2*halo)**2):
            result.append((x + halo, y + halo, True))
        else:
            result.append((x + halo, y + halo, False))
    return result


def extract_macros_sub(
    node: vast.ModuleDef,
    prefix: list[str],
    macros: list[tuple[str, str]],
    modules: dict[str, vast.ModuleDef],
) -> None:
    for item in node.items:
        if isinstance(item, vast.InstanceList):
            for inst in item.instances:
                if not isinstance(inst, vast.Instance):
                    raise RuntimeError
                if inst.module in modules:
                    extract_macros_sub(modules[inst.module],
                                       prefix + [inst.name], macros, modules)
                else:
                    macros.append((inst.module, '.'.join(prefix + [inst.name])))


def extract_macros(verilog: str, top: str) -> list[tuple[str, str]]:
    modules: dict[str, vast.ModuleDef] = {}
    parser = VerilogParser()
    src = parser.parse(verilog)
    if not isinstance(src, vast.Source):
        raise RuntimeError
    desc = src.description
    if not isinstance(desc, vast.Description):
        raise RuntimeError
    defs = desc.definitions
    if not isinstance(defs, tuple):
        raise RuntimeError
    for d in defs:
        if isinstance(d, vast.ModuleDef):
            modules[d.name] = d

    macros: list[tuple[str, str]] = []
    extract_macros_sub(modules[top], [], macros, modules)
    return macros


def generate_config(
    src_local_path: str,
    top: str,
    clk: str,
    clock_period: int | float,
    die_shape: tuple[int | float, int | float],
    pdk: Literal['sky130', 'gf180mcu', 'sky130A', 'sky130B', 'gf180mcuA', 'gf180mcuB', 'gf180mcuC'],
    pdk_root: str | None = None,
    macro_local_path: str | None = None,
    macro_docker_path: str | None = None,
    vdd: str | None = None,
    gnd: str | None = None,
):
    if pdk not in ['sky130', 'gf180mcu', 'sky130A', 'sky130B', 'gf180mcuA', 'gf180mcuB', 'gf180mcuC']:
        raise ValueError('Invalid PDK:', pdk)
    if pdk == 'sky130':
        # sky130A is default for sky130
        pdk = pdk + 'A'
    if pdk == 'gf180mcu':
        # gf180mcuC is default for gf180mcu
        pdk = pdk + 'C'

    if (vdd is None) != (gnd is None):
        raise TypeError('Specify both or neither of `vdd` and `gnd`')
    if vdd is None and gnd is None:
        if pdk.startswith('sky130'):
            vdd = 'vccd1'
            gnd = 'vssd1'
        else:
            vdd = 'VDD'
            gnd = 'VSS'

    if (macro_local_path is None) != (macro_docker_path is None):
        raise TypeError('Specify both or neither of `macro_local_path` and `macro_docker_path`')
    if macro_local_path is None and macro_docker_path is None:
        if pdk_root is None:
            raise TypeError('`pdk_root` must be specified if `macro_local_path` and `macro_docker_path` are not specified')
        macro_local_path = str(Path(pdk_root) / pdk / 'libs.ref')
        macro_docker_path = '/'.join(['/openlane/pdks', pdk, 'libs.ref'])

    with open(src_local_path) as f:
        src = f.read()

    macros = extract_macros(src, top)
    macro_modules = list({mod for mod, _ in macros})
    macro_insts = [inst for _, inst in macros]
    macro_shapes: dict[str, tuple[int | float, int | float]] = {}

    config_json = {}

    config_json['PDK'] = pdk
    config_json['DESIGN_NAME'] = top
    config_json['VERILOG_FILES'] = 'dir::src/*.v'
    config_json['CLOCK_PORT'] = clk
    config_json['CLOCK_PERIOD'] = clock_period
    config_json['DESIGN_IS_CORE'] = True

    config_json['FP_SIZING'] = 'absolute'
    config_json['DIE_AREA'] = ' '.join([str(num) for num in [0, 0] + list(die_shape)])
    config_json['PL_TARGET_DENSITY'] = 0.5

    config_json['VDD_NETS'] = vdd
    config_json['GND_NETS'] = gnd
    config_json['FP_PDN_MACRO_HOOKS'] = ', '.join([' '.join([inst, vdd, gnd, vdd, gnd]) for inst in macro_insts])

    config_json['MACRO_PLACEMENT_CFG'] = 'dir::macro_placement.cfg'

    pdk_lefs = list(Path(macro_local_path).glob('**/*.lef'))
    pdk_gdss = list(Path(macro_local_path).glob('**/*.gds'))
    pdk_libs = list(Path(macro_local_path).glob('**/*.lib'))
    extra_lefs: list[str] = []
    extra_gds_files: list[str] = []
    extra_libs: list[str] = []
    for mod in macro_modules:
        lefs: list[Path] = []
        for lef in pdk_lefs:
            if lef.name.startswith(mod):
                lefs.append(lef)
        if not lefs:
            raise RuntimeError('No LEF file found')
        if len(lefs) > 1:
            warn('\n'.join(['More than one LEF files found:'] + [str(lef) for lef in lefs]), RuntimeWarning)
        extra_lefs.append(str(Path(macro_docker_path) / lefs[0].relative_to(macro_local_path)))
        with lefs[0].open() as f:
            for l in f:
                m = re.search(r'SIZE ([0-9\.]+) BY ([0-9\.]+)', l)
                if m:
                    try:
                        x = int(m[1])
                    except ValueError:
                        x = float(m[1])
                    try:
                        y = int(m[2])
                    except ValueError:
                        y = float(m[2])
                    break
            else:
                raise RuntimeError(f'The found LEF file ({lefs[0]}) does not contain size information')
        macro_shapes[mod] = (x, y)
        gdss: list[Path] = []
        for gds in pdk_gdss:
            if gds.name.startswith(mod):
                gdss.append(gds)
        if not gdss:
            raise RuntimeError('No GDS file found')
        if len(gdss) > 1:
            warn('\n'.join(['More than one GDS files found:'] + [str(gds) for gds in gdss]), RuntimeWarning)
        extra_gds_files.append(str(Path(macro_docker_path) / gdss[0].relative_to(macro_local_path)))
        libs: list[Path] = []
        for lib in pdk_libs:
            if lib.name.startswith(mod):
                libs.append(lib)
        if not libs:
            raise RuntimeError('No LIB file found')
        if len(libs) > 1:
            warn('\n'.join(['More than one LIB files found:'] + [str(lib) for lib in libs]), RuntimeWarning)
        extra_libs.append(str(Path(macro_docker_path) / libs[0].relative_to(macro_local_path)))
    config_json['EXTRA_LEFS'] = ' '.join(extra_lefs)
    config_json['EXTRA_GDS_FILES'] = ' '.join(extra_gds_files)
    config_json['EXTRA_LIBS'] = ' '.join(extra_libs)

    config_json['RUN_KLAYOUT_XOR'] = False
    config_json['MAGIC_DRC_USE_GDS'] = False
    config_json['QUIT_ON_MAGIC_DRC'] = False

    with open('config.json', 'w') as f:
        json.dump(config_json, f, indent=4)

    macro_placement_cfg: list[str] = []
    macro_placement = place_macros([macro_shapes[mod] for mod, _ in macros],
                                   die_shape, allow_rotation=True)
    for (_, inst), (x, y, r) in zip(macros, macro_placement):
        macro_placement_cfg.append(' '.join([inst, str(x), str(y), 'R90' if r else 'R0']))
    with open('macro_placement.cfg', 'w') as f:
        f.write('\n'.join(macro_placement_cfg))
