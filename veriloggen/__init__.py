#-------------------------------------------------------------------------------
# Veriloggen: A library for constructing a Verilog HDL source code in Python
# 
# Copyright (C) 2015, Shinya Takamaeda-Yamazaki
# License: Apache 2.0
#-------------------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import print_function
import os
import sys

from .vtypes import *
from .module import Module, StubModule, Instance, GenerateFor, GenerateIf, connect_same_name
from .function import Function, FunctionCall
from .task import Task, TaskCall
from .from_verilog import read_verilog_stubmodule, read_verilog_module, read_verilog_stubmodule_str, read_verilog_module_str
from . import lib
