from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes

class TempVariableGenerator(object):
    def __init__(self, tmp_prefix='_'):
        self.tmp_prefix = tmp_prefix
        self.tmp_count = 0

    def Wire(width=1, length=None, signed=False, value=None, initval=None):
        name = ''.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return vtypes.Wire(name, width, length, signed, value, initval)
    
    def Reg(width=1, length=None, signed=False, value=None, initval=None, prefix=None):
        name = ''.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return vtypes.Reg(name, width, length, signed, value, initval)

    def Integer(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return vtypes.Integer(name, width, length, signed, value, initval)
    
    def TmpReal(self, width=None, length=None, signed=False, value=None, initval=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return vtypes.Real(name, width, length, signed, value, initval)

    def TmpGenvar(self, width=None, length=None, signed=False, value=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return vtypes.Genvar(name, width, length, signed, value)

    def TmpLocalparam(self, value, width=None, signed=False, length=None):
        name = '_'.join([self.tmp_prefix, str(self.tmp_count)])
        self.tmp_count += 1
        return vtypes.Localparam(name, value, width, signed, length)
