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
cd tests
make run
make clean
cd ..
cd examples
make run
make clean
cd ..
cd tests
make test
cd ..
cd examples
make test
cd ..
mv veriloggen.old veriloggen
cd ..
cd ..
