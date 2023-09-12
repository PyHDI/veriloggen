from pathlib import Path
import pytest

from veriloggen.asic import check_file


files = ['correct.json', 'wrong1.json', 'wrong2.json']


@pytest.mark.parametrize('fname', files)
def test(fname: str):
    p = Path(__file__).parent / fname
    try:
        check_file(p)
    except (TypeError, ValueError):
        assert fname.startswith('wrong')
    else:
        assert fname.startswith('correct')
