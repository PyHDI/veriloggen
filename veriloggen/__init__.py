"""
   Veriloggen: A library for constructing a Verilog HDL source code in Python

   Copyright 2015, Shinya Takamaeda-Yamazaki and Contributors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import
from __future__ import print_function

import os
import sys


__version__ = open(os.path.join(os.path.dirname(__file__), "VERSION")).read().splitlines()[0]

# expand the recursive call limit for python 3.6 and later
sys.setrecursionlimit(1000 * 10)

# Verilog HDL Core
from .core.vtypes import *
from .core.module import Module, StubModule, Instance, GenerateFor, GenerateIf, connect_same_name
from .core.function import Function, FunctionCall
from .core.task import Task, TaskCall
from .core.submodule import Submodule

# Code Generator
from .verilog import from_verilog

# Verilog Simulator
from .simulation import simulation

# Abstract Extension
from .seq.seq import Seq, TmpSeq, make_condition
from .fsm.fsm import FSM, TmpFSM
from .pipeline.pipeline import Pipeline

# Extension reset
from .seq import reset as seq_reset
from .fsm import reset as fsm_reset
from .dataflow import reset as dataflow_reset
from .stream import reset as stream_reset
from .thread import reset as thread_reset
from .types import reset as types_reset


def reset():
    seq_reset()
    fsm_reset()
    dataflow_reset()
    stream_reset()
    thread_reset()
    types_reset()
