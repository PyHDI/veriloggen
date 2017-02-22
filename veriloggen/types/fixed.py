from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import copy

import veriloggen.core.vtypes as vtypes
from veriloggen.core.vtypes import _Numeric
from veriloggen.core.vtypes import _Variable
from veriloggen.core.vtypes import _Constant

def to_fixed(value, point, signed=False):
    if point < 0:
        raise ValueError('point must be more than 0')
    
    if point == 0:
        return value
    
    if isinstance(value, (int, bool, float)) and isinstance(point, int):
        mag = 2 ** point
        return int(value * mag)
    
    if isinstance(value, (int, bool)):
        mag = vtypes.Int(2) ** point
        return vtypes.Int(value) * mag
    
    if isinstance(value, float):
        mag = vtypes.Int(2) ** point
        return vtypes.Float(value) * mag
    
    if hasattr(value, 'signed') and value.signed:
        signed = True
        
    return shift_left(value, point, signed)

def fixed_to_int(value, point, signed=False):
    if point < 0:
        raise ValueError('point must be more than 0')
    
    if point == 0:
        return value
    
    if isinstance(value, (int, bool, float)) and isinstance(point, int):
        mag = 2 ** point
        return int(value / mag)
    
    if isinstance(value, (int, bool, float)):
        mag = vtypes.Int(2) ** point
        return vtypes.Int(value) / mag
    
    if hasattr(value, 'signed') and value.signed:
        signed = True
        
    return shift_right(value, point, signed)

def fixed_to_int_low(value, point):
    if point < 0:
        raise ValueError('point must be more than 0')
    
    if point == 0:
        return 0
    
    if isinstance(value, (int, bool, float)) and isinstance(point, int):
        mag = 2 ** point
        return int(value % mag)
    
    return vtypes.And(value, vtypes.Repeat(vtypes.Int(1, 1), point))

def fixed_to_real(value, point, signed=False):
    if point < 0:
        raise ValueError('point must be more than 0')
    
    if point == 0:
        return vtypes.SystemTask('itor', value)

    if isinstance(value, float):
        raise TypeError("value is already float.")
    
    if isinstance(value, (int, bool)) and isinstance(point, int):
        mag = 2 ** point
        return float(value) / mag

    if hasattr(value, 'signed') and value.signed:
        signed = True

    width = value.bit_length()
    msb = (value[width - 1] if isinstance(value, vtypes._Variable) else
           (value >> (width - 1)) & 0x1)
    
    v0 = (vtypes.SystemTask('itor', fixed_to_int(value, point)) +
          vtypes.SystemTask('itor', fixed_to_int_low(value, point)) /
          vtypes.SystemTask('itor', vtypes.Int(2) ** point))
    
    nv = vtypes.Unot(value) + 1
    v1 = ((vtypes.SystemTask('itor', fixed_to_int(nv, point)) +
           vtypes.SystemTask('itor', fixed_to_int_low(nv, point)) /
           vtypes.SystemTask('itor', vtypes.Int(2) ** point))) * vtypes.SystemTask('itor', -1)
    
    return vtypes.Mux(signed and msb == 0, v0, v1)

#-------------------------------------------------------------------------------
def adjust(left, right, lpoint, rpoint, signed=True):
    diff_lpoint = vtypes.Mux(rpoint < lpoint, 0, rpoint - lpoint)
    diff_rpoint = vtypes.Mux(lpoint < rpoint, 0, lpoint - rpoint)
    ldata = vtypes.Mux(diff_lpoint == 0, left, shift_left(left, diff_lpoint, signed))
    rdata = vtypes.Mux(diff_rpoint == 0, right, shift_left(right, diff_rpoint, signed))
    _ldata = vtypes.Mux(signed, vtypes.SystemTask('signed', ldata), ldata)
    _rdata = vtypes.Mux(signed, vtypes.SystemTask('signed', rdata), rdata)
    return _ldata, _rdata
    
def shift_left(value, size, signed=True):
    if isinstance(value, vtypes.Int):
        value = value.value
        
    if isinstance(value, int) and isinstance(size, int):
        return value << size
    
    if isinstance(value, bool) and isinstance(size, int):
        return value << size
    
    return vtypes.Sll(value, size)

def shift_right(value, size, signed=True):
    if isinstance(value, vtypes.Int):
        value = value.value
        
    if isinstance(value, int) and isinstance(size, int):
        return value >> size
    
    if isinstance(value, bool) and isinstance(size, int):
        return value >> size
    
    return vtypes.Mux(signed, vtypes.Sra(value, size), vtypes.Srl(value, size))

#-------------------------------------------------------------------------------
def _max_mux(a, b):
    return vtypes.Mux(a > b, a, b)

def _min_mux(a, b):
    return vtypes.Mux(a < b, a, b)

#-------------------------------------------------------------------------------
def FixedInput(m, name, width=32, point=0, signed=False):
    var = m.Input(name, width, signed=signed)
    return Fixed(var, point, signed)

def FixedOutput(m, name, width=32, point=0, signed=False):
    var = m.Output(name, width, signed=signed)
    return Fixed(var, point, signed)

def FixedOutputReg(m, name, width=32, point=0, signed=False):
    var = m.OutputReg(name, width, signed=signed)
    return Fixed(var, point, signed)

def FixedReg(m, name, width=32, point=0, signed=False):
    var = m.Reg(name, width, signed=signed)
    return Fixed(var, point, signed)

def FixedWire(m, name, width=32, point=0, signed=False):
    var = m.Wire(name, width, signed=signed)
    return Fixed(var, point, signed)

#-------------------------------------------------------------------------------
class Fixed(vtypes.VeriloggenNode):
    def __init__(self, value, point, signed=None, raw=True):
        vtypes.VeriloggenNode.__init__(self)
        self.value = value if raw else to_fixed(value, point)
        self.point = point
        self.signed = vtypes.get_signed(value) if signed is None else signed
    
    def __hash__(self):
        return hash((id(self), self.object_id))

    def _adjust(self, value):
        lpoint = self.point
        if not isinstance(value, Fixed):
            rvalue = value
            rsigned = vtypes.get_signed(value)
            rpoint = 0
        else:
            rvalue = value.value
            rsigned = value.signed
            rpoint = value.point

        ldiff = vtypes.Mux(lpoint <= rpoint, 0, lpoint - rpoint)
        rdiff = vtypes.Mux(lpoint >= rpoint, 0, rpoint - lpoint)
        v = vtypes.Mux(lpoint>rpoint, shift_left(rvalue, ldiff, rsigned),
            vtypes.Mux(lpoint<rpoint, shift_right(rvalue, rdiff, rsigned), rvalue))

        return v
    
    def write(self, value, blk=False, ldelay=None, rdelay=None):
        v = self._adjust(value)
        return self.value.write(v, blk=blk, ldelay=ldelay, rdelay=rdelay)

    def write_raw(self, value, blk=False, ldelay=None, rdelay=None):
        return self.value.write(value, blk=blk, ldelay=ldelay, rdelay=rdelay)

    def read(self):
        return self.value.read()

    def assign(self, value):
        v = self._adjust(value)
        return self.value.assign(v)

    def reset(self):
        return self.value.reset()

    def bit_length(self):
        return self.value.bit_length()

    def get_signed(self):
        return self.signed

    def add(self, r):
        return self.write(self + r)

    def sub(self, r):
        return self.write(self - r)

    def inc(self):
        return self.add(1)

    def dec(self):
        return self.sub(1)

    def __call__(self, value, blk=False, ldelay=None, rdelay=None):
        return self.write(value, blk=blk, ldelay=ldelay, rdelay=rdelay)

    #-------------------------------------------------------------------------------
    @property
    def raw(self):
        return self.value

    @property
    def int_part(self):
        return self.value >> self.point

    @property
    def dec_part(self):
        mask = vtypes.Mux(self.point==0, 0, vtypes.Repeat(vtypes.Int(1, width=1), self.point))
        return self.value & mask

    def _binary_op(self, op, r):
        lvalue = self.value
        lpoint = self.point
        lsigned = self.signed
        
        if not isinstance(r, Fixed):
            rvalue = r
            rsigned = vtypes.get_signed(r)
            rpoint = 0
        else:
            rvalue = r.value
            rsigned = r.signed
            rpoint = r.point

        point = _max_mux(lpoint, rpoint)
        signed = lsigned and rsigned
        ldata, rdata = adjust(lvalue, rvalue, lpoint, rpoint, signed)

        data = op(ldata, rdata)

        return Fixed(data, point, signed)

    def _binary_op_mul(self, op, r):
        lvalue = self.value
        lpoint = self.point
        lsigned = self.signed
        
        if not isinstance(r, Fixed):
            rvalue = r
            rsigned = vtypes.get_signed(r)
            rpoint = 0
        else:
            rvalue = r.value
            rsigned = r.signed
            rpoint = r.point

        point = _max_mux(lpoint, rpoint)
        signed = lsigned and rsigned
        ldata = vtypes.SystemTask('signed', lvalue)
        rdata = vtypes.SystemTask('signed', rvalue)
        shift_size = _min_mux(lpoint, rpoint)

        data = op(ldata, rdata)
        data = shift_right(data, shift_size, signed=signed)

        return Fixed(data, point, signed)

    def _binary_op_div(self, op, r):
        lvalue = self.value
        lpoint = self.point
        lsigned = self.signed
        
        if not isinstance(r, Fixed):
            rvalue = r
            rsigned = vtypes.get_signed(r)
            rpoint = 0
        else:
            rvalue = r.value
            rsigned = r.signed
            rpoint = r.point

        point = _max_mux(lpoint, rpoint)
        signed = lsigned and rsigned
        lwidth = lvalue.bit_length()
        rwidth = rvalue.bit_length()
        ldata, rdata = adjust(lvalue, rvalue, lpoint, rpoint, signed)

        try:
            lmsb = ldata[lwidth-1]
        except:
            lmsb = (ldata >> (lwidth - 1) & 0x1)
            
        try:
            rmsb = rdata[lwidth-1]
        except:
            rmsb = (rdata >> (rwidth - 1) & 0x1)
            
        abs_ldata = (ldata if not lsigned else
                     vtypes.Mux(lmsb == 0, ldata, vtypes.Unot(ldata) + 1))
        abs_rdata = (rdata if not rsigned else
                     vtypes.Mux(rmsb == 0, rdata, vtypes.Unot(rdata) + 1))
        abs_data = op(abs_ldata, abs_rdata)
        data = (abs_data if not signed else
                vtypes.Mux(vtypes.Ors(vtypes.Ands(lmsb, rmsb),
                                      vtypes.Ands(vtypes.Not(lmsb), vtypes.Not(rmsb))),
                           abs_data, vtypes.Unot(abs_data) + 1))

        return Fixed(data, point, signed)

    def _binary_logical_op(self, op, r):
        lvalue = self.value
        
        if not isinstance(r, Fixed):
            rvalue = r
        else:
            rvalue = r.value

        return op(lvalue, rvalue)

    def __add__(self, r):
        return self._binary_op(vtypes.Plus, r)

    def __sub__(self, r):
        return self._binary_op(vtypes.Minus, r)

    def __mul__(self, r):
        return self._binary_op_mul(vtypes.Times, r)

    def __div__(self, r):
        return self._binary_op_div(vtypes.Divide, r)

    def __truediv__(self, r):
        return self._binary_op_div(vtypes.Divide, r)


def FixedConst(value, point, raw=False):
    return Fixed(value, point, raw=raw)
