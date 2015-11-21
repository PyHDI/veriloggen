from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

import veriloggen.vtypes as vtypes

#-------------------------------------------------------------------------------
class Function(vtypes.VeriloggenNode):
    def __init__(self, name, width=1):
        self.name = name
        self.width = width
        self.io_variable = collections.OrderedDict()
        self.variable = collections.OrderedDict()
        self.statement = None
        self.width_msb = None
        self.width_lsb = None
        self.subst = []

    #---------------------------------------------------------------------------
    def Input(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Input(name, width, length, signed, value)
        self.io_variable[name] = t
        return t
    
    def Reg(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Reg(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Integer(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Integer(name, width, length, signed, value)
        self.variable[name] = t
        return t
    
    def Body(self, *statement):
        if self.statement is not None:
            raise ValueError("Statement is already assigned.")
        self.statement = tuple(statement)
        return self

    def add_subst(self, s):
        self.subst.append(s)

    def set_raw_width(self, msb, lsb):
        self.width_msb = msb
        self.width_lsb = lsb
    
    def __call__(self, r):
        return vtypes.Subst(self, r)

    def next(self, r):
        return self.__call__(r)
    
    def call(self, *args):
        return FunctionCall(self, *args)

class FunctionCall(vtypes._Numeric):
    def __init__(self, func, *args):
        self.func = func
        self.args = tuple(args)
