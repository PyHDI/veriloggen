from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import copy

import veriloggen.core.vtypes as vtypes


class ResetVisitor(object):

    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))

    def visit(self, node):
        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        visitor = getattr(
            self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__Variable(self, node):
        if node.initval is None:
            return None
        return vtypes.Subst(node, node.initval)

    def visit_Pointer(self, node):
        val = self.visit(node.var)
        if val is None:
            return None
        left = vtypes.Pointer(val.left, node.pos)
        if not isinstance(val.right, (vtypes._Variable, vtypes.Scope)):
            if isinstance(val.right, (int, bool)):
                val_right = vtypes.Int(val.right)
            elif isinstance(val.right, float):
                val_right = vtypes.Float(val.right)
            else:
                raise TypeError("unsupported value type: %s" % str(val.right))
            right = vtypes.And(vtypes.Srl(
                val_right, node.pos), vtypes.Int(1, width=1))
        else:
            right = vtypes.Pointer(val.right, node.pos)
        return vtypes.Subst(left, right)

    def visit_Slice(self, node):
        val = self.visit(node.var)
        if val is None:
            return None
        if isinstance(val.right, vtypes._Variable):
            right = vtypes.Slice(val.right, node.msb, node.lsb)
        else:
            right = vtypes.And(vtypes.Srl(val.right, node.lsb),
                               vtypes.Repeat(vtypes.Int(1, width=1), node.msb - node.lsb + 1))
        return vtypes.Subst(vtypes.Slice(val.left, node.msb, node.lsb), right)

    def visit_Cat(self, node):
        left_values = []
        right_values = []

        for v in node.vars:
            val = self.visit(v)
            width = vtypes.get_width(v)
            if width is None:
                width = 1
            if val is None:
                right = vtypes.IntX(width)
            elif isinstance(val.right, int):
                right = vtypes.Int(val.right, width)
            elif isinstance(val.right, vtypes._Constant):
                right = copy.deepcopy(val.right)
                right.width = width
            else:
                right = v._get_module().TmpLocalparam(val.right, width)

            left_values.append(v)
            right_values.append(right)

        return vtypes.Subst(vtypes.Cat(*left_values), vtypes.Cat(*right_values))
