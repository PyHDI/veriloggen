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
    ast.RShift: vtypes.Srl,
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
    ast.Div: '__div__'
}


def getMethodName(op):
    t = type(op)
    return methods[t]
