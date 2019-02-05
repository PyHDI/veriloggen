from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import ast

import veriloggen.core.vtypes as vtypes

operators = {
    ast.Add: vtypes.Plus,
    ast.Sub: vtypes.Minus,
    ast.Mult: vtypes.Times,
    ast.Div: vtypes.Divide,
    ast.Mod: vtypes.Mod,
    ast.Pow: vtypes.Power,
    ast.LShift: vtypes.Sll,
    ast.RShift: vtypes.Sra,
    ast.BitOr: vtypes.Or,
    ast.BitXor: vtypes.Xor,
    ast.BitAnd: vtypes.And,
    ast.FloorDiv: vtypes.Divide,
    ast.And: vtypes.Land,
    ast.Or: vtypes.Lor,
    ast.Invert: vtypes.Unot,
    ast.Not: vtypes.Ulnot,
    ast.UAdd: vtypes.Uplus,
    ast.USub: vtypes.Uminus,
    ast.Eq: vtypes.Eq,
    ast.NotEq: vtypes.NotEq,
    ast.Lt: vtypes.LessThan,
    ast.LtE: vtypes.LessEq,
    ast.Gt: vtypes.GreaterThan,
    ast.GtE: vtypes.GreaterEq,
    ast.Is: vtypes.Eq,  # ?
    ast.IsNot: vtypes.NotEq,  # ?
    ast.In: None,
    ast.NotIn: None,
}


def getVeriloggenOp(op):
    t = type(op)
    return operators[t]


methods = {
    ast.Add: '__add__',
    ast.Sub: '__sub__',
    ast.Mult: '__mul__',
    ast.Div: '__truediv__',
    ast.Mod: '__mod__',
    ast.Pow: '__pow__',
    ast.LShift: '__lshift__',
    ast.RShift: None,
    ast.BitOr: '__or__',
    ast.BitXor: '__xor__',
    ast.BitAnd: '__and__',
    ast.FloorDiv: '__div__',
    ast.And: None,
    ast.Or: None,
    ast.Invert: '__invert__',
    ast.Not: None,
    ast.UAdd: '__pos__',
    ast.USub: '__neg__',
    ast.Eq: '__eq__',
    ast.NotEq: '__ne__',
    ast.Lt: '__lt__',
    ast.LtE: ('__lt__', '__eq__'),
    ast.Gt: '__gt__',
    ast.GtE: ('__gt__', '__eq__'),
    ast.Is: None,
    ast.IsNot: None,
    ast.In: None,
    ast.NotIn: None
}


def getMethodName(op):
    t = type(op)
    return methods[t]


def applyMethod(var, method, *args):
    if method is None:
        raise NotImplementedError()

    if isinstance(method, (tuple, list)):
        ret = None
        for mt in method:
            func = getattr(var, mt, None)
            if func is None:
                raise NotImplementedError()

            v = func(*args)
            if isinstance(v, type(NotImplemented)):
                raise NotImplementedError()

            if ret is None:
                ret = v
            else:
                ret = vtypes.Lor(ret, v)
        return ret

    func = getattr(var, method, None)
    if func is None:
        raise NotImplementedError()

    v = func(*args)
    if isinstance(v, type(NotImplemented)):
        raise NotImplementedError()

    return v
