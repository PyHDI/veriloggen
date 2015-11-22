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
cd tests
make run PYTHON=python
make clean
cd ..
cd examples
make run PYTHON=python
make clean
cd ..
cd tests
make test PYTHON=python
cd ..
cd examples
make test PYTHON=python
cd ..
mv veriloggen.old veriloggen
cd ..
deactivate
cd ..
