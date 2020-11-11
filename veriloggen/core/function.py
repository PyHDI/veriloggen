from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

import veriloggen.core.vtypes as vtypes


class Function(vtypes.VeriloggenNode):

    def __init__(self, name, width=1, raw_width=None):
        vtypes.VeriloggenNode.__init__(self)
        self.name = name
        self.width = width
        self.raw_width = raw_width
        self.io_variable = collections.OrderedDict()
        self.variable = collections.OrderedDict()
        self.statement = None
        self.subst = []

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

    # function call
    def call(self, *args):
        return FunctionCall(self, *args)

    def write(self, value):
        return vtypes.Subst(self, value)

    def read(self):
        return self

    def get_width(self):
        return self.width

    def _add_subst(self, s):
        self.subst.append(s)

    def _get_subst(self):
        return self.subst

    def __setattr__(self, attr, value):
        if attr == 'width':
            object.__setattr__(self, 'raw_width', None)
        object.__setattr__(self, attr, value)

    def __call__(self, value):
        return self.write(value)


class FunctionCall(vtypes._Numeric):

    def __init__(self, func, *args):
        vtypes._Numeric.__init__(self)
        self.func = func
        self.args = tuple(args)
