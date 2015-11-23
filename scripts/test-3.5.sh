#!/bin/sh
set -e

mkdir 3.5
cd 3.5
virtualenv --python=python3 .
source bin/activate
git clone https://github.com/PyHDI/veriloggen.git
cd veriloggen
python3 setup.py install
pip install pytest pytest-pythonpath
mv veriloggen veriloggen.old
make run -C tests
make clean -C tests
make run -C examples
make clean -C examples
make test
mv veriloggen.old veriloggen
cd ..
deactivate
cd ..
