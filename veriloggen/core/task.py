from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

import veriloggen.core.vtypes as vtypes


class Task(vtypes.VeriloggenNode):

    def __init__(self, name):
        vtypes.VeriloggenNode.__init__(self)
        self.name = name
        self.io_variable = collections.OrderedDict()
        self.variable = collections.OrderedDict()
        self.statement = None

    def Input(self, name, width=None, dims=None, signed=False, value=None):
        t = vtypes.Input(width, dims, signed, value, name=name)
        self.io_variable[name] = t
        return t

    def Reg(self, name, width=None, dims=None, signed=False, value=None):
        t = vtypes.Reg(width, dims, signed, value, name=name)
        self.variable[name] = t
        return t

    def Integer(self, name, width=None, dims=None, signed=False, value=None):
        t = vtypes.Integer(width, dims, signed, value, name=name)
        self.variable[name] = t
        return t

    def Body(self, *statement):
        if self.statement is not None:
            raise ValueError("Statement is already assigned.")
        self.statement = tuple(statement)
        return self

    def call(self, *args):
        return TaskCall(self.name, *args)


class TaskCall(vtypes._Numeric):

    def __init__(self, name, *args):
        vtypes._Numeric.__init__(self)
        self.name = name
        self.args = tuple(args)
