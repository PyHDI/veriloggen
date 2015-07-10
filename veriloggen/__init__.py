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
import vtypes

from module import Module
from interface import Interface
from function import Function
from vtypes import *

import lib
