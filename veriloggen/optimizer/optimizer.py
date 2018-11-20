from __future__ import absolute_import
from __future__ import print_function
import sys
import os

import veriloggen.core.vtypes as vtypes
import veriloggen.types.fixed as fxd
import pyverilog.dataflow.reorder as reorder
import pyverilog.dataflow.optimizer as voptimizer
from pyverilog.dataflow.dataflow import *


def try_optimize(node, width=32):
    try:
        return optimize(node, width)
    except:
        return node
    return node


def optimize(node, width=32):
    df_tree = makeDFTree(node)
    opt = voptimizer.VerilogOptimizer({}, default_width=width)
    opt_dfnode = opt.optimize(df_tree)
    opt_node = makeASTTree(opt_dfnode)
    return opt_node


def makeDFTree(node):
    if isinstance(node, fxd._FixedBase):
        raise TypeError('FixedPoint is not supported.')

    if isinstance(node, vtypes._Variable):
        name = node.name
        v = DFTerminal(name)
        v.original = node
        return v

    if isinstance(node, bool):
        v = 1 if node else 0
        return DFIntConst(str(v))

    if isinstance(node, int):
        return DFIntConst(str(node))

    if isinstance(node, float):
        return DFFloatConst(str(node))

    if isinstance(node, str):
        return DFStringConst(node)

    if isinstance(node, vtypes.Int):
        return DFIntConst(str(node.value))

    if isinstance(node, vtypes.Float):
        return DFFloatConst(str(node.value))

    if isinstance(node, vtypes.Str):
        return DFStringConst(node.value)

    if isinstance(node, vtypes.Cond):
        true_df = makeDFTree(node.true_value)
        false_df = makeDFTree(node.false_value)
        cond_df = makeDFTree(node.cond)
        if isinstance(cond_df, DFBranch):
            return reorder.insertCond(cond_df, true_df, false_df)
        return DFBranch(cond_df, true_df, false_df)

    if isinstance(node, vtypes._UnaryOperator):
        right_df = makeDFTree(node.right)
        if isinstance(right_df, DFBranch):
            return reorder.insertUnaryOp(right_df, node.__class__.__name__)
        return DFOperator((right_df,), node.__class__.__name__)

    if isinstance(node, vtypes._BinaryOperator):
        left_df = makeDFTree(node.left)
        right_df = makeDFTree(node.right)
        if isinstance(left_df, DFBranch) or isinstance(right_df, DFBranch):
            return reorder.insertOp(left_df, right_df, node.__class__.__name__)
        return DFOperator((left_df, right_df,), node.__class__.__name__)

    if isinstance(node, vtypes.SystemTask):
        return DFSyscall(node.cmd, tuple([makeDFTree(n) for n in node.args]))

    raise TypeError("unsupported type: %s %s" % (str(type(node)), str(node)))


operators = {
    'Plus': vtypes.Plus,
    'Minus': vtypes.Minus,
    'Times': vtypes.Times,
    'Divide': vtypes.Divide,
    'Mod': vtypes.Mod,
    'Power': vtypes.Power,
    'Sll': vtypes.Sll,
    'Srl': vtypes.Srl,
    'Sra': vtypes.Sra,
    'Or': vtypes.Or,
    'Xor': vtypes.Xor,
    'And': vtypes.And,
    'Divide': vtypes.Divide,
    'Land': vtypes.Land,
    'Lor': vtypes.Lor,
    'Unot': vtypes.Unot,
    'Ulnot': vtypes.Ulnot,
    'Uplus': vtypes.Uplus,
    'Uminus': vtypes.Uminus,
    'Eq': vtypes.Eq,
    'NotEq': vtypes.NotEq,
    'LessThan': vtypes.LessThan,
    'LessEq': vtypes.LessEq,
    'GreaterThan': vtypes.GreaterThan,
    'GreaterEq': vtypes.GreaterEq,
    'Eq': vtypes.Eq,
    'NotEq': vtypes.NotEq,
}


def getOp(op):
    return operators[op]


def makeASTTree(node):
    if isinstance(node, DFBranch):
        return Cond(makeASTTree(node.condnode),
                    makeASTTree(node.truenode),
                    makeASTTree(node.falsenode))

    if isinstance(node, DFIntConst):
        return vtypes.Int(int(node.value))

    if isinstance(node, DFFloatConst):
        return vtypes.Float(float(node.value))

    if isinstance(node, DFStringConst):
        return vtypes.Str(node.value)

    if isinstance(node, DFEvalValue):
        if isinstance(node.value, int):
            return vtypes.Int(node.value)
        if isinstance(node.value, float):
            return vtypes.Float(node.value)
        if isinstance(node.value, DFStringConst):
            return vtypes.Str(node.value)
        raise TypeError('Unknown constant')

    if isinstance(node, DFTerminal):
        return node.original

    if isinstance(node, DFUndefined):
        return vtypes.IntX()

    if isinstance(node, DFHighImpedance):
        return vtypes.IntZ()

    if isinstance(node, DFOperator):
        if len(node.nextnodes) == 1:
            return getOp(node.operator)(makeASTTree(node.nextnodes[0]))
        return getOp(node.operator)(makeASTTree(node.nextnodes[0]), makeASTTree(node.nextnodes[1]))

    if isinstance(node, DFSyscall):
        return vtypes.SystemTask(node.syscall, tuple([makeASTTree(n) for n in node.nextnodes]))

    raise TypeError("Unsupported DFNode %s" % type(node))
