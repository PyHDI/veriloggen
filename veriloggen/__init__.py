#-------------------------------------------------------------------------------
# Veriloggen: A library for constructing a Verilog HDL source code in Python
# 
# Copyright (C) 2015, Shinya Takamaeda-Yamazaki
# License: Apache 2.0
#-------------------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import print_function

# expand the recursive call limit for python 3.6 and later
import sys
sys.setrecursionlimit(1000 * 10)

# Verilog HDL Core
from .core.vtypes import *
from .core.module import Module, StubModule, Instance, GenerateFor, GenerateIf, connect_same_name
from .core.function import Function, FunctionCall
from .core.task import Task, TaskCall

# Code Generator
from .verilog import from_verilog

# Verilog Simulator
from .simulation import simulation

# Abstract Extension
from .seq.seq import Seq, TmpSeq, make_condition
from .fsm.fsm import FSM, TmpFSM
from .pipeline.pipeline import Pipeline

# Extension reset
from .seq.seq import reset as seq_reset
from .fsm.fsm import reset as fsm_reset
from .dataflow.dataflow import reset as dataflow_reset

def reset():
    seq_reset()
    fsm_reset()
    dataflow_reset()
