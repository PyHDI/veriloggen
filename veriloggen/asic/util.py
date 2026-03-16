from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import SupportsInt
    from collections.abc import Sequence
    from ..core.module import Module


def make_arr(m: Module, name: str, vals: Sequence[SupportsInt], width=32, signed=True):
    arr = m.Reg(name, width, len(vals), signed)
    m.Initial(*[arr[i](int(x)) for i, x in enumerate(vals)])
    return arr
