from setuptools import setup, find_packages

import os


def read(filename):
    # return open(os.path.join(os.path.dirname(__file__), filename), encoding='utf8').read()
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(name='veriloggen',
      version=read('veriloggen/VERSION'),
      description='A Mixed-Paradigm Hardware Construction Framework',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      keywords='FPGA, Verilog HDL, High-Level Synthesis',
      author='Shinya Takamaeda-Yamazaki',
      license="Apache License 2.0",
      url='https://github.com/PyHDI/veriloggen',
      packages=find_packages(),
      package_data={'veriloggen': ['VERSION'],
                    'veriloggen.simulation': ['*.cpp'],
                    },
      install_requires=['Jinja2>=2.10',
                        'pyverilog>=1.2.0',
                        'numpy>=1.17'],
      extras_require={
          'test': ['pytest>=3.8.1', 'pytest-pythonpath>=0.7.3'],
          'graph': ['pygraphviz>=1.3.1'],
      },
      )
