from setuptools import setup, find_packages

import re
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


m = re.search(r'(\d+\.\d+\.\d+(-.+)?)',
              read('veriloggen/utils/VERSION').splitlines()[0])
version = m.group(1) if m is not None else '0.0.0'

setup(name='veriloggen',
      version=version,
      description='A library for constructing a Verilog HDL source code in Python',
      long_description=read('README.rst'),
      keywords='FPGA, Verilog HDL, High-Level Synthesis',
      author='Shinya Takamaeda-Yamazaki',
      license="Apache License 2.0",
      url='https://github.com/PyHDI/veriloggen',
      packages=find_packages(),
      #package_data={ 'path' : ['*.*'], },
      install_requires=['pyverilog>=1.1.1', 'ipgen>=0.3.1', 'Jinja2>=2.8'],
      extras_require={
          'graph': ['pygraphviz>=1.3.1'],
          'test': ['pytest>=2.8.2', 'pytest-pythonpath>=0.7'],
          'memimg': ['numpy>=1.14'],
      },
      )
