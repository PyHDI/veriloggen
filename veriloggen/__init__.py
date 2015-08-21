#-------------------------------------------------------------------------------
# Veriloggen: A library for constructing a Verilog HDL source code in Python
# 
# Copyright (C) 2015, Shinya Takamaeda-Yamazaki
# License: Apache 2.0
#-------------------------------------------------------------------------------
from __future__ import absolute_import
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vtypes import *
from module import Module, StubModule, Instance, GenerateFor, GenerateIf
from function import Function, FunctionCall
from task import Task, TaskCall
from from_verilog import read_verilog_stubmodule, read_verilog_module, read_verilog_stubmodule_str, read_verilog_module_str
import lib
