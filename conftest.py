import pytest
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption('--sim', default='iverilog', help='Simulator')


@pytest.fixture(scope='session', autouse=True)
def clean():
    yield
    for p in Path('.').glob('*.out'):
        p.unlink()
    for p in Path('.').glob('**/*.pyc'):
        p.unlink()
    for p in Path('.').glob('**/__pycache__'):
        p.rmdir()
    for p in Path('.').glob('parsetab.py'):
        p.unlink()
