mkdir 3.4
cd 3.4
virtualenv --python=python3 .
source bin/activate
git clone https://github.com/PyHDI/veriloggen.git
cd veriloggen
python3 setup.py install
pip install pytest pytest-pythonpath
mv veriloggen veriloggen.old
cd tests
make test
make clean
make run
cd ..
cd examples
make test
make clean
make run
cd ..
mv veriloggen.old veriloggen
cd ..
cd ..
