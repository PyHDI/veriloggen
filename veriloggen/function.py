import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vtypes

class Function(vtypes.VeriloggenNode):
    def __init__(self, name, width=1):
        self.name = name
        self.width = width
        self.io_variable = collections.OrderedDict()
        self.variable = collections.OrderedDict()
        self.statement = None

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

    def __call__(self, r):
        return vtypes.Subst(self, r)

    def next(self, r):
        return self.__call__(r)
    
    def call(self, *args):
        return FunctionCall(self.name, *args)

class FunctionCall(vtypes.VeriloggenNode):
    def __init__(self, name, *args):
        self.name = name
        self.args = tuple(args)
