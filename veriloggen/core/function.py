from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections

import veriloggen.core.vtypes as vtypes

#-------------------------------------------------------------------------------
class Function(vtypes.VeriloggenNode):
    def __init__(self, name, width=1):
        self.name = name
        self.width = width
        self.width_msb = None
        self.width_lsb = None
        self.io_variable = collections.OrderedDict()
        self.variable = collections.OrderedDict()
        self.statement = None
        self.subst = []

    #---------------------------------------------------------------------------
    def Input(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Input(width, length, signed, value, name=name)
        self.io_variable[name] = t
        return t
    
    def Reg(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Reg(width, length, signed, value, name=name)
        self.variable[name] = t
        return t
    
    def Integer(self, name, width=None, length=None, signed=False, value=None):
        t = vtypes.Integer(width, length, signed, value, name=name)
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

    def next(self, r):
        return self.__call__(r)
    
    def add_subst(self, s):
        self.subst.append(s)

    def set_raw_width(self, msb, lsb):
        self.width_msb = msb
        self.width_lsb = lsb
    
    def __setattr__(self, attr, value):
        # when width or length is overwritten, msb and lsb values are reset.
        if attr == 'width':
            object.__setattr__(self, 'width_msb', None)
            object.__setattr__(self, 'width_lsb', None)
        object.__setattr__(self, attr, value)
            
    def __call__(self, r):
        return vtypes.Subst(self, r)

class FunctionCall(vtypes._Numeric):
    def __init__(self, func, *args):
        self.func = func
        self.args = tuple(args)
