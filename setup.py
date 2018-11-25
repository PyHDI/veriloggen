from setuptools import setup, find_packages

import re
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename), encoding='utf8').read()


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
      package_data={'veriloggen.utils': ['VERSION'],
                    'veriloggen.simulation': ['*.cpp'], },
      install_requires=['pyverilog>=1.1.3', 'ipgen>=1.0.1', 'Jinja2>=2.10'],
      extras_require={
          'graph': ['pygraphviz>=1.3.1'],
          'test': ['pytest>=3.2', 'pytest-pythonpath>=0.7'],
          'memimg': ['numpy>=1.14'],
      },
      )
