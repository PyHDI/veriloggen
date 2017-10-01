#!/bin/sh
set -e

mkdir python
cd python
virtualenv --python=python .
source bin/activate

git clone https://github.com/PyHDI/veriloggen.git
cd veriloggen
python setup.py install
pip install pytest pytest-pythonpath
mv veriloggen veriloggen.old

python -m pytest -vv .

mv veriloggen.old veriloggen
cd ..
deactivate
cd ..
