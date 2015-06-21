from setuptools import setup, find_packages

import veriloggen.utils.version
import re
import os

m = re.search(r'(\d+\.\d+\.\d+)', veriloggen.utils.version.VERSION)
version = m.group(1) if m is not None else '0.0.0'

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(name='veriloggen',
      version=version,
      description='Refactoring Tool for Verilog HDL',
      long_description=read('README.rst'),
      keywords = 'FPGA, Verilog HDL',
      author='Shinya Takamaeda-Yamazaki',
      author_email='shinya.takamaeda_at_gmail_com',
      license="Apache License 2.0",
      url='http://shtaxxx.github.io/veriloggen/',
      packages=find_packages(),
#      package_data={ 'veriloggen.template' : ['*.*'], },
)

