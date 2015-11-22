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
make test PYTHON=python
make clean
make run PYTHON=python
cd ..
cd examples
make test PYTHON=python
make clean
make run PYTHON=python
cd ..
mv veriloggen.old veriloggen
cd ..
cd ..
