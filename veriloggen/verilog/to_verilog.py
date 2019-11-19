from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections
import re

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module

import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator


#-------------------------------------------------------------------------
def write_verilog(node, filename=None, for_verilator=False):
    visitor = VerilogModuleVisitor(for_verilator)
    modules = tuple(node.get_modules().values())

    module_ast_list = [visitor.visit(mod) for mod in modules
                       if not isinstance(mod, module.StubModule)]
    description = vast.Description(module_ast_list)
    source = vast.Source(filename, description)

    codegen = ASTCodeGenerator()
    main = codegen.visit(source)

    stub = [mod.get_code()
            for mod in modules if isinstance(mod, module.StubModule)]

    code = ''.join([main] + stub)

    if filename:
        with open(filename, 'w') as f:
            f.write(code)
    return code


#-------------------------------------------------------------------------
class VerilogCommonVisitor(object):

    def __init__(self, for_verilator=False, in_initial=False):
        self.for_verilator = for_verilator
        self.in_initial = in_initial

    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))

    def visit(self, node):
        name = node.__class__.__name__
        if hasattr(node, 'ast_name') and node.ast_name is not None:
            name = node.ast_name
        visitor = getattr(self, 'visit_' + name, self.generic_visit)
        return visitor(node)

    #-------------------------------------------------------------------------
    # First class object wrapper
    def visit_Int(self, node):
        value_list = []
        value = node.value

        if isinstance(node.value, str) and node.value.find('-') >= 0:
            pos = node.value.find('-') + 1
            value = node.value[pos:]
            value_list.append('-')

        if isinstance(node.value, int) and node.value < 0:
            value = abs(node.value)
            value_list.append('-')

        if node.width:
            value_list.append(str(node.width))

        if node.base is None:
            if node.signed:
                value_list.append("'sd")
            elif node.width:
                value_list.append("'d")
            if isinstance(value, str):
                value_list.append(value)
            else:
                value_list.append(str(value))
        elif node.base == 2:
            if node.signed:
                value_list.append("'sb")
            else:
                value_list.append("'b")
            if isinstance(value, str):
                value_list.append(value)
            else:
                value_list.append(bin(value).replace('0b', ''))
        elif node.base == 8:
            if node.signed:
                value_list.append("'so")
            else:
                value_list.append("'o")
            if isinstance(value, str):
                value_list.append(value)
            else:
                value_list.append(oct(value).replace('0o', ''))
        elif node.base == 10:
            if node.signed:
                value_list.append("'sd")
            else:
                value_list.append("'d")
            if isinstance(value, str):
                value_list.append(value)
            else:
                value_list.append(str(value))
        elif node.base == 16:
            if node.signed:
                value_list.append("'sh")
            else:
                value_list.append("'h")
            if isinstance(value, str):
                value_list.append(value)
            else:
                value_list.append(hex(value).replace('0x', ''))
        else:
            raise ValueError("Int.base must be 2, 8, 10, or 16")

        return vast.IntConst(''.join(value_list))

    def visit_Float(self, node):
        return vast.FloatConst(str(node.value))

    def visit_Str(self, node):
        return vast.StringConst(node.value)

    #-------------------------------------------------------------------------
    def visit_bool(self, node):
        if node:
            return vast.IntConst('1')
        return vast.IntConst('0')

    def visit_int(self, node):
        return vast.IntConst(str(node))

    def visit_str(self, node):
        return vast.StringConst(node)

    def visit_float(self, node):
        return vast.FloatConst(str(node))

    def visit_list(self, node):
        return self._optimize_block(vast.Block(tuple([self.visit(n) for n in node])))

    def visit_tuple(self, node):
        return self.visit_list(node)

    def _optimize_block(self, node):
        if not isinstance(node, vast.Block):
            return node
        ret = []
        for n in node.statements:
            if isinstance(n, vast.Block) and n.scope is None:
                ret.extend(n.statements)
            else:
                ret.append(n)
        return vast.Block(tuple(ret))

    #-------------------------------------------------------------------------
    def visit_Parameter(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Localparam(self, node):
        name = node.name
        return vast.Identifier(name)

    #-------------------------------------------------------------------------
    def visit_Input(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Output(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Inout(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Reg(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Wire(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Integer(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Real(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Genvar(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_AnyType(self, node):
        name = node.name
        return vast.Identifier(name)

    #-------------------------------------------------------------------------
    def visit__SkipUnaryOperator(self, node):
        return self.visit(node.right)

    #-------------------------------------------------------------------------
    def visit_Power(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Power(left, right)

    def visit_Times(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Times(left, right)

    def visit_Divide(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Divide(left, right)

    def visit_Mod(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Mod(left, right)

    def visit_Plus(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Plus(left, right)

    def visit_Minus(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Minus(left, right)

    def visit_Sll(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Sll(left, right)

    def visit_Srl(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Srl(left, right)

    def visit_Sra(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Sra(left, right)

    def visit_LessThan(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.LessThan(left, right)

    def visit_GreaterThan(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.GreaterThan(left, right)

    def visit_LessEq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.LessEq(left, right)

    def visit_GreaterEq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.GreaterEq(left, right)

    def visit_Eq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Eq(left, right)

    def visit_NotEq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.NotEq(left, right)

    def visit_Eql(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Eql(left, right)

    def visit_NotEql(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.NotEql(left, right)

    def visit_And(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.And(left, right)

    def visit_Xor(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Xor(left, right)

    def visit_Xnor(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Xnor(left, right)

    def visit_Or(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Or(left, right)

    def visit_Land(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Land(left, right)

    def visit_Lor(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.Lor(left, right)

    #-------------------------------------------------------------------------
    def visit_Uplus(self, node):
        right = self.visit(node.right)
        return vast.Uplus(right)

    def visit_Uminus(self, node):
        right = self.visit(node.right)
        return vast.Uminus(right)

    def visit_Ulnot(self, node):
        right = self.visit(node.right)
        return vast.Ulnot(right)

    def visit_Unot(self, node):
        right = self.visit(node.right)
        return vast.Unot(right)

    def visit_Uand(self, node):
        right = self.visit(node.right)
        return vast.Uand(right)

    def visit_Unand(self, node):
        right = self.visit(node.right)
        return vast.Unand(right)

    def visit_Uor(self, node):
        right = self.visit(node.right)
        return vast.Uor(right)

    def visit_Unor(self, node):
        right = self.visit(node.right)
        return vast.Unor(right)

    def visit_Uxor(self, node):
        right = self.visit(node.right)
        return vast.Uxor(right)

    def visit_Uxnor(self, node):
        right = self.visit(node.right)
        return vast.Uxnor(right)

   #---------------------------------------------------------------------------
    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        return vast.Pointer(var, pos)

    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        return vast.Partselect(var, msb, lsb)

    def visit_Cat(self, node):
        vars = tuple([self.visit(var) for var in node.vars])
        return vast.Concat(vars)

    def visit_Repeat(self, node):
        var = (self.visit(node.var) if isinstance(node.var, vtypes.Cat) else
               self.visit(vtypes.Cat(node.var)))
        times = self.visit(node.times)
        return vast.Repeat(var, times)

    #-------------------------------------------------------------------------
    def visit_Cond(self, node):
        cond = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        return vast.Cond(cond, true_value, false_value)

    #-------------------------------------------------------------------------
    def visit_If(self, node):
        cond = self.visit(node.condition)
        true_statement = self.visit(node.true_statement)
        false_statement = (self.visit(node.false_statement)
                           if node.false_statement is not None else None)
        # remove a redundant begin-end, if the true_statement is not for reset
        cond_str = str(cond).lower()
        if ((not cond_str.count('rst') and not cond_str.count('reset')) and
            isinstance(false_statement, vast.Block) and
            len(false_statement.statements) == 1 and
                isinstance(false_statement.statements[0], vast.IfStatement)):
            false_statement = false_statement.statements[0]
        return vast.IfStatement(cond, true_statement, false_statement)

    #-------------------------------------------------------------------------
    def visit_For(self, node):
        for_visitor = VerilogBlockingVisitor(self.for_verilator, self.in_initial)
        pre = for_visitor.visit(node.pre)
        cond = self.visit(node.condition)
        post = for_visitor.visit(node.post)
        statement = self.visit(node.statement)
        return vast.ForStatement(pre, cond, post, statement)

    #-------------------------------------------------------------------------
    def visit_While(self, node):
        cond = self.visit(node.condition)
        statement = self.visit(node.statement)
        return vast.WhileStatement(cond, statement)

    #-------------------------------------------------------------------------
    def visit_Case(self, node):
        comp = self.visit(node.comp)
        statement = tuple([self.visit(s) for s in node.statement])
        return vast.CaseStatement(comp, statement)

    def visit_Casex(self, node):
        comp = self.visit(node.comp)
        statement = tuple([self.visit(s) for s in node.statement])
        return vast.CasexStatement(comp, statement)

    def visit_When(self, node):
        cond = tuple([self.visit(c)
                      for c in node.condition]) if node.condition else None
        statement = self.visit(node.statement)
        return vast.Case(cond, statement)

    #-------------------------------------------------------------------------
    def visit_ScopeIndex(self, node):
        name = node.name
        index = self.visit(node.index)
        return vast.IdentifierScopeLabel(name, index)

    def visit_Scope(self, node):
        scope = []
        for a in node.args:
            if isinstance(a, module.GenerateIf):
                if a.true_scope is None:
                    raise TypeError("GenerateIf statement without scope name"
                                    "can not be used as an scope index.")
                scope.append(vast.IdentifierScopeLabel(a.true_scope))
            elif isinstance(a, module.GenerateIfElse):
                if a.false_scope is None:
                    raise TypeError("GenerateIfElse statement without scope name"
                                    "can not be used as an scope index.")
                scope.append(vast.IdentifierScopeLabel(a.false_scope))
            elif isinstance(a, module.GenerateFor):
                raise TypeError("Scope index must not be GenerateFor. "
                                "Use slice, like 'obj[index]'")
            elif isinstance(a, vtypes.ScopeIndex):
                scope.append(self.visit(a))
            elif isinstance(a, str):
                scope.append(vast.IdentifierScopeLabel(a))
            else:
                _id = self.visit(a)
                if not isinstance(_id, vast.Identifier):
                    raise TypeError("Cannot convert into IdentifierScopeLabel from %s." %
                                    str(type(_id)))
                scope.append(vast.IdentifierScopeLabel(_id.name))

        if len(scope) == 1:
            return vast.Identifier(scope[0].name)
        return vast.Identifier(scope[-1].name, vast.IdentifierScope(tuple(scope[:-1])))

    #-------------------------------------------------------------------------
    def visit_SystemTask(self, node):
        cmd = node.cmd
        if (self.for_verilator and (cmd == 'dumpfile' or cmd == 'dumpvars')):
            return vast.SystemCall('write', (vast.StringConst(''),))
        if (self.for_verilator and self.in_initial and cmd == 'finish'):
            return vast.SystemCall('write', (vast.StringConst(''),))

        args = tuple([self.visit(a) for a in node.args])
        return vast.SystemCall(cmd, args)

    def visit_SingleStatement(self, node):
        statement = self.visit(node.statement)
        return vast.SingleStatement(statement)

    #-------------------------------------------------------------------------
    def visit_Event(self, node):
        sensitivity = vast.SensList(
            tuple([self.visit(n) if isinstance(n, vtypes.Sensitive) else
                   vast.Sens(self.visit(n)) for n in node.sensitivity]))
        return vast.EventStatement(sensitivity)

    def visit_Delay(self, node):
        if self.for_verilator:
            return vast.SingleStatement(vast.SystemCall('write', (vast.StringConst(''),)))
        delay = self.visit(node.value)
        return vast.SingleStatement(vast.DelayStatement(delay))

    #-------------------------------------------------------------------------
    def visit_Function(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_FunctionCall(self, node):
        func = self.visit(node.func)
        args = tuple([self.visit(a) for a in node.args])
        return vast.FunctionCall(func, args)

    #-------------------------------------------------------------------------
    def visit_Task(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_TaskCall(self, node):
        name = vast.Identifier(node.name)
        args = tuple([self.visit(a) for a in node.args])
        return vast.TaskCall(name, args)

    #-------------------------------------------------------------------------
    def visit_Instance(self, node):
        return vast.Identifier(node.instname)

    #-------------------------------------------------------------------------
    def visit_EmbeddedCode(self, node):
        return vast.EmbeddedCode(node.code)

    def visit_EmbeddedNumeric(self, node):
        return vast.EmbeddedCode(node.code)


#-------------------------------------------------------------------------
class VerilogModuleVisitor(VerilogCommonVisitor):

    def __init__(self, for_verilator=False):
        VerilogCommonVisitor.__init__(self, for_verilator)
        self.bind_visitor = VerilogBindVisitor(for_verilator)
        self.always_visitor = VerilogAlwaysVisitor(for_verilator)
        self.blocking_visitor = VerilogBlockingVisitor(for_verilator)
        self.module = None

    #-------------------------------------------------------------------------
    def make_width(self, node):
        if node.raw_width is not None:
            msb = self.bind_visitor.visit(node.raw_width[0])
            lsb = self.bind_visitor.visit(node.raw_width[1])
            return vast.Width(msb, lsb)

        if node.width is not None:
            msb = vast.Minus(self.bind_visitor.visit(node.width), vast.IntConst('1'))
            lsb = vast.IntConst('0')
            return vast.Width(msb, lsb)

        return None

    def make_dims(self, node):
        if node.raw_dims is not None:
            lengths = []
            for raw_dim in node.raw_dims:
                l = self.bind_visitor.visit(raw_dim[0])
                r = self.bind_visitor.visit(raw_dim[1])
                lengths.append(vast.Length(l, r))
            return vast.Dimensions(lengths)

        if node.dims is not None:
            lengths = []
            for dim in node.dims:
                l = vast.IntConst('0')
                r = vast.Minus(self.bind_visitor.visit(dim), vast.IntConst('1'))
                lengths.append(vast.Length(l, r))
            return vast.Dimensions(lengths)

        return None

    #-------------------------------------------------------------------------
    def visit(self, node):
        if isinstance(node, module.Module) and not isinstance(node, module.Generate):
            return self.visit_Module(node)
        name = node.__class__.__name__
        if hasattr(node, 'ast_name') and node.ast_name is not None:
            name = node.ast_name
        visitor = getattr(self, 'visit_' + name, self.generic_visit)
        return visitor(node)

    #-------------------------------------------------------------------------
    def visit_Module(self, node):
        self.module = node
        name = node.name

        params = ([self.visit(v) for v in node.global_constant.values()])
        params = [i for i in params if i is not None]
        paramlist = vast.Paramlist(tuple(params))

        ports = [self.visit(v) for v in node.io_variable.values()]
        ports = [i for i in ports if i is not None]
        portlist = vast.Portlist(tuple(ports))

        excludes = [vtypes.Input, vtypes.Output,
                    vtypes.Inout, vtypes.Parameter]

        items = [self.visit(i) for i in node.items
                 if not isinstance(i, tuple(excludes))]
        items = [i for i in items if i is not None]

        m = vast.ModuleDef(name, paramlist, portlist, items)

        self.module = None
        return m

    #-------------------------------------------------------------------------
    def visit_Parameter(self, node):
        name = node.name
        value = self.bind_visitor.visit(node.value)
        value = vast.Rvalue(value)
        width = self.make_width(node)
        signed = node.signed
        return vast.Parameter(name, value, width, signed)

    def visit_Localparam(self, node):
        name = node.name
        value = self.bind_visitor.visit(node.value)
        value = vast.Rvalue(value)
        width = self.make_width(node)
        signed = node.signed
        return vast.Localparam(name, value, width, signed)

    #-------------------------------------------------------------------------
    def visit_Input(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Ioport(vast.Input(name, width, signed, dims))

    def visit_Output(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        first = vast.Output(name, width, signed, dims)
        second = vast.Reg(name, width, signed, dims) if self.module.is_reg(name) else None
        return vast.Ioport(first, second)

    def visit_Inout(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Ioport(vast.Inout(name, width, signed, dims))

    def visit_Reg(self, node):
        name = node.name
        if self.module.is_output(name):
            return None
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Reg(name, width, signed, dims)

    def visit_Wire(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Wire(name, width, signed, dims)

    def visit_Integer(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Integer(name, width, signed, dims)

    def visit_Real(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Real(name, width, signed, dims)

    def visit_Genvar(self, node):
        name = node.name
        width = self.make_width(node)
        dims = self.make_dims(node)
        signed = node.signed
        return vast.Genvar(name, width, signed, dims)

    def visit_AnyType(self, node):
        return None

    #-------------------------------------------------------------------------
    def visit_Posedge(self, node):
        sig = self.bind_visitor.visit(node.name)
        t = 'posedge'
        return vast.Sens(sig, t)

    def visit_Negedge(self, node):
        sig = self.bind_visitor.visit(node.name)
        t = 'negedge'
        return vast.Sens(sig, t)

    def visit_SensitiveAll(self, node):
        sig = None
        t = 'all'
        return vast.Sens(sig, t)

    #-------------------------------------------------------------------------
    def visit_Always(self, node):
        sens = (tuple([self.visit(n) if isinstance(n, vtypes.Sensitive) else
                       vast.Sens(self.always_visitor.visit(n), 'level')
                       for n in node.sensitivity]) if node.sensitivity else
                tuple([vast.Sens(None, 'all')]))
        sensitivity = vast.SensList(sens)
        statement = self._optimize_block(
            vast.Block(tuple([self.always_visitor.visit(n) for n in node.statement])))
        return vast.Always(sensitivity, statement)

    #-------------------------------------------------------------------------
    def visit_Assign(self, node):
        if not isinstance(node.statement, vtypes.Subst):
            raise TypeError("Assign expects Subst object.")
        left = self.bind_visitor.visit(node.statement.left)
        right = self.bind_visitor.visit(node.statement.right)
        lvalue = vast.Lvalue(left)
        rvalue = vast.Rvalue(right)
        return vast.Assign(lvalue, rvalue)

    #-------------------------------------------------------------------------
    def visit_Initial(self, node):
        self.blocking_visitor.in_initial = True
        statement = self._optimize_block(
            vast.Block(tuple([self.blocking_visitor.visit(s) for s in node.statement])))
        self.blocking_visitor.in_initial = False
        return vast.Initial(statement)

    #-------------------------------------------------------------------------
    def visit_Function(self, node):
        name = node.name
        retwidth = self.make_width(node)
        statement = ([self.visit(v).first for v in node.io_variable.values()] +
                     [self.visit(v) for v in node.variable.values()])
        statement.append(self._optimize_block(
            vast.Block(tuple([self.blocking_visitor.visit(s) for s in node.statement]))))
        return vast.Function(name, retwidth, statement)

    #-------------------------------------------------------------------------
    def visit_Task(self, node):
        name = node.name
        statement = ([self.visit(v).first for v in node.io_variable.values()] +
                     [self.visit(v) for v in node.variable.values()])
        statement.append(self._optimize_block(
            vast.Block(tuple([self.blocking_visitor.visit(s) for s in node.statement]))))
        return vast.Task(name, statement)

    #-------------------------------------------------------------------------
    def visit_Instance(self, node):
        module = node.module.name
        parameterlist = [vast.ParamArg(
            p, self.bind_visitor.visit(a)) for p, a in node.params]
        portlist = [vast.PortArg(p, self.bind_visitor.visit(a))
                    for p, a in node.ports]
        name = node.instname
        instance = vast.Instance(module, name, portlist, parameterlist)
        return vast.InstanceList(module, parameterlist, (instance,))

    #-------------------------------------------------------------------------
    def _visit_Generate(self, node):
        params = ([self.visit(v) for v in node.global_constant.values()])
        params = [i for i in params if i is not None]
        paramlist = [vast.Decl(p) for p in params]
        items = [self.visit(i) for i in node.items
                 if not isinstance(i, (vtypes.Input, vtypes.Output,
                                       vtypes.Inout, vtypes.Parameter))]
        items = [i for i in items if i is not None]
        ret = paramlist
        for i in items:
            if isinstance(i, vast.GenerateStatement):
                ret.extend(i.items)
            else:
                ret.append(i)
        return tuple(ret)

    def visit_GenerateFor(self, node):
        genfor_visitor = VerilogBlockingVisitor(self.for_verilator)
        pre = genfor_visitor.visit(node.pre)
        cond = genfor_visitor.visit(node.cond)
        post = genfor_visitor.visit(node.post)
        items = self._visit_Generate(node)
        block = vast.Block(items, scope=node.scope)
        _for = vast.ForStatement(pre, cond, post, block)
        return vast.GenerateStatement(tuple([_for]))

    def visit_GenerateIf(self, node):
        genif_visitor = VerilogBlockingVisitor(self.for_verilator)
        cond = genif_visitor.visit(node.cond)
        true_items = self._visit_Generate(node)
        true_block = vast.Block(true_items, scope=node.true_scope)
        false_items = self._visit_Generate(node.Else)
        false_block = (vast.Block(false_items, scope=node.Else.false_scope)
                       if false_items else None)
        _if = vast.IfStatement(cond, true_block, false_block)
        return vast.GenerateStatement(tuple([_if]))

    def visit_GenerateIfElse(self, node):
        return None


#-------------------------------------------------------------------------
class VerilogBindVisitor(VerilogCommonVisitor):
    pass


#-------------------------------------------------------------------------
class VerilogAlwaysVisitor(VerilogCommonVisitor):

    def visit_Subst(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay = self.visit(node.ldelay) if node.ldelay else None
        rdelay = self.visit(node.rdelay) if node.rdelay else None
        lvalue = vast.Lvalue(left)
        rvalue = vast.Rvalue(right)
        if node.blk:
            return vast.BlockingSubstitution(lvalue, rvalue, ldelay, rdelay)
        return vast.NonblockingSubstitution(lvalue, rvalue, ldelay, rdelay)


#-------------------------------------------------------------------------
class VerilogBlockingVisitor(VerilogCommonVisitor):

    def visit_Subst(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay = vast.DelayStatement(self.visit(
            node.ldelay)) if node.ldelay else None
        rdelay = vast.DelayStatement(self.visit(
            node.rdelay)) if node.rdelay else None
        lvalue = vast.Lvalue(left)
        rvalue = vast.Rvalue(right)
        return vast.BlockingSubstitution(lvalue, rvalue, ldelay, rdelay)

    def visit_Forever(self, node):
        if self.for_verilator:
            return vast.SingleStatement(vast.SystemCall('write', (vast.StringConst(''),)))
        statement = self._optimize_block(
            vast.Block(tuple([self.visit(s) for s in node.statement])))
        return vast.ForeverStatement(statement)

    def visit_Wait(self, node):
        cond = self.visit(node.condition)
        if node.statement is None:
            return vast.WaitStatement(cond, None)
        statement = self._optimize_block(
            vast.Block(tuple([self.visit(s) for s in node.statement])))
        return vast.WaitStatement(cond, statement)

    def visit_Posedge(self, node):
        sig = self.visit(node.name)
        t = 'posedge'
        return vast.Sens(sig, t)

    def visit_Negedge(self, node):
        sig = self.visit(node.name)
        t = 'negedge'
        return vast.Sens(sig, t)
