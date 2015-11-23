#!/bin/sh
set -e

mkdir 2.7
cd 2.7
virtualenv --python=python .
source bin/activate
git clone https://github.com/PyHDI/veriloggen.git
cd veriloggen
python setup.py install
pip install pytest pytest-pythonpath
mv veriloggen veriloggen.old
make run -C tests PYTHON=python
make clean -C tests
make run -C examples PYTHON=python
make clean -C examples
make test PYTHON=python
mv veriloggen.old veriloggen
cd ..
deactivate
cd ..
