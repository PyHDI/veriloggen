#-------------------------------------------------------------------------------
# veriloggen.py
#
# Veriloggen: A library for constructing a Verilog HDL source code in Python
# 
# Copyright (C) 2015, Shinya Takamaeda-Yamazaki
# License: Apache 2.0
#-------------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import utils.version

import module
from module import Module
import vtypes
from vtypes import (Posedge, Negedge, Subst,
                    If, For, While,
                    Bit, Slice, Cond,
                    Not, Unot, Ulnot, Land, Lor,
                    LandList, LorList)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    INFO = "Veriloggen: A library for constructing a Verilog HDL source code in Python"
    VERSION = utils.version.VERSION
    print(INFO)
    print(VERSION)
