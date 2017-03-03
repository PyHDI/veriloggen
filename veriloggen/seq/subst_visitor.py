from __future__ import absolute_import
from __future__ import print_function

import os
import sys

import veriloggen.core.vtypes as vtypes


class SubstDstVisitor(object):

    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))

    def visit(self, node):
        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        visitor = getattr(
            self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit__Variable(self, node):
        return [node]

    def visit_list(self, node):
        ret = []
        for n in node:
            ret.extend(self.visit(n))
        return ret

    def visit_tuple(self, node):
        ret = []
        for n in node:
            ret.extend(self.visit(n))
        return ret

    def visit_If(self, node):
        true_statement = self.visit(node.true_statement)
        false_statement = (self.visit(node.false_statement)
                           if node.false_statement is not None else [])
        return true_statement + false_statement

    def visit_For(self, node):
        statement = self.visit(node.statement)
        return statement

    def visit_While(self, node):
        statement = self.visit(node.statement)
        return statement

    def visit_Pointer(self, node):
        return [node]

    def visit_Slice(self, node):
        return [node]

    def visit_Cat(self, node):
        return [node]

    def visit_Subst(self, node):
        return self.visit(node.left)

    def visit_SingleStatement(self, node):
        return []
