from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import copy
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes
from veriloggen.core.collect_visitor import CollectVisitor
from veriloggen.core.rename_visitor import RenameVisitor


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

    def visit_Case(self, node):
        statement = self.visit(node.statement)
        return statement

    def visit_Casex(self, node):
        return self.visit(node)

    def visit_When(self, node):
        statement = self.visit(node.statement)
        return statement

    def visit_For(self, node):
        pre = self.visit(node.pre)
        post = self.visit(node.post)
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

    def visit_EmbeddedCode(self, node):
        """ No analysis """
        return []


class SubstSrcVisitor(CollectVisitor):

    def __init__(self):
        self.srcs = OrderedDict()

    def visit__Variable(self, node):
        self.srcs[node.name] = node

        self.visit(node.width)
        if hasattr(node, 'initval'):
            self.visit(node.initval)

    def visit_list(self, node):
        for n in node:
            self.visit(n)

    def visit_tuple(self, node):
        for n in node:
            self.visit(n)

    def visit_If(self, node):
        self.visit(node.condition)
        self.visit(node.true_statement)
        if node.false_statement is not None:
            self.visit(node.false_statement)

    def visit_Case(self, node):
        self.visit(node.comp)
        self.visit(node.statement)

    def visit_Casex(self, node):
        return self.visit(node)

    def visit_When(self, node):
        self.visit(node.condition)
        self.visit(node.statement)

    def visit_For(self, node):
        self.visit(node.pre)
        self.visit(node.condition)
        self.visit(node.post)
        self.visit(node.statement)

    def visit_While(self, node):
        self.visit(node.condition)
        self.visit(node.statement)

    def visit_SystemTask(self, node):
        for arg in node.args:
            self.visit(arg)

    def visit_Subst(self, node):
        self.visit(node.right)

    def visit_SingleStatement(self, node):
        self.visit(node.statement)

    def visit_EmbeddedCode(self, node):
        """ No analysis """
        pass


class SrcRenameVisitor(RenameVisitor):

    def __init__(self, rename_dict):
        self.rename_dict = rename_dict

    def visit_list(self, node):
        return [self.visit(n) for n in node]

    def visit_tuple(self, node):
        return [self.visit(n) for n in node]

    def visit__Variable(self, node):
        if node.name in self.rename_dict:
            return self.rename_dict[node.name]
        return node

    def visit_If(self, node):
        condition = self.visit(node.condition)
        true_statement = self.visit(node.true_statement)
        if node.false_statement is not None:
            false_statement = self.visit(node.false_statement)
        else:
            false_statement = None

        ret = vtypes.If(condition)
        ret.true_statement = true_statement
        ret.false_statement = false_statement
        return ret

    def visit_Case(self, node):
        comp = self.visit(node.comp)
        statement = self.visit(node.statement)
        ret = vtypes.Case(comp)
        ret.statement = statement
        ret.last = node.last
        return ret

    def visit_Casex(self, node):
        return self.visit(node)

    def visit_When(self, node):
        condition = self.visit(node.condition)
        statement = self.visit(node.statement)
        ret = vtypes.When(*condition)
        ret.statement = statement
        return ret

    def visit_For(self, node):
        pre = self.visit(node.pre)
        condition = self.visit(node.condition)
        post = self.visit(node.post)
        statement = self.visit(node.statement)
        ret = vtypes.For(pre, condition, post)
        ret.statement = statement
        return ret

    def visit_While(self, node):
        condition = self.visit(node.condition)
        statement = self.visit(node.statement)
        ret = vtypes.While(condition)
        ret.statement = statement
        return ret

    def visit_SystemTask(self, node):
        args = [self.visit(arg) for arg in node.args]
        return vtypes.SystemTask(node.cmd, *args)

    def visit_Subst(self, node):
        left = node.left
        right = self.visit(node.right)
        return vtypes.Subst(left, right)

    def visit_SingleStatement(self, node):
        statement = self.visit(node.statement)
        return vtypes.SingleStatement(statement)

    def visit_EmbeddedCode(self, node):
        return node


class DstRenameVisitor(SrcRenameVisitor):

    def visit_Subst(self, node):
        left = self.visit(node.left)
        right = node.right
        return vtypes.Subst(left, right)
