from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import collections
import tempfile

import veriloggen.core.vtypes as vtypes
import veriloggen.core.module as module
import veriloggen.core.function as function
import veriloggen.core.task as task

import pyverilog.vparser.ast as vast
from pyverilog.vparser.parser import VerilogCodeParser
from pyverilog.dataflow.modulevisitor import ModuleVisitor
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator


# -------------------------------------------------------------------------
# User interfaces to read Verilog source code
# -------------------------------------------------------------------------
def read_verilog_stubmodule(*filelist, **opt):
    module_dict = to_module_dict(*filelist, **opt)
    codegen = ASTCodeGenerator()
    stubs = collections.OrderedDict()
    for name, m in module_dict.items():
        description = vast.Description((m,))
        source = vast.Source('', description)
        code = codegen.visit(source)
        stubs[name] = module.StubModule(name, code=code)
    return stubs


def read_verilog_module(*filelist, **opt):
    module_dict = to_module_dict(*filelist, **opt)
    visitor = VerilogReadVisitor(module_dict)
    for name, m in module_dict.items():
        visitor.visit(m)
    modules = visitor.converted_modules
    return modules


def read_verilog_module_str(code, encode='utf-8'):
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(code.encode(encode))
    tmp.read()
    filename = tmp.name
    ret = read_verilog_module(filename)
    tmp.close()
    return ret


def read_verilog_stubmodule_str(code, encode='utf-8'):
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(code.encode(encode))
    tmp.read()
    filename = tmp.name
    ret = read_verilog_stubmodule(filename)
    tmp.close()
    return ret


# -------------------------------------------------------------------------
def to_module_dict(*filelist, **opt):
    ast = to_ast(*filelist, **opt)

    module_visitor = ModuleVisitor()
    module_visitor.visit(ast)
    module_names = module_visitor.get_modulenames()
    moduleinfotable = module_visitor.get_moduleinfotable()
    moduleinfo = moduleinfotable.getDefinitions()
    module_dict = collections.OrderedDict(
        [(n, d.definition) for n, d in moduleinfo.items()])

    return module_dict


# -------------------------------------------------------------------------
def to_ast(*filelist, **opt):
    include = opt['include'] if 'include' in opt else ()
    define = opt['define'] if 'define' in opt else ()
    if not isinstance(include, tuple) and not isinstance(include, list):
        raise TypeError('"include" option of read_verilog must be tuple or list, not %s' %
                        type(include))
    if not isinstance(include, tuple) and not isinstance(include, list):
        raise TypeError('"include" option of read_verilog must be tuple or list, not %s' %
                        type(include))

    code_parser = VerilogCodeParser(filelist,
                                    preprocess_include=include,
                                    preprocess_define=define)
    ast = code_parser.parse()

    return ast


# -------------------------------------------------------------------------
def to_tuple(s):
    if not isinstance(s, (list, tuple)):
        return tuple([s])
    return s


# -------------------------------------------------------------------------
class ReadOnlyModule(object):

    def __init__(self, m):
        self.m = m

    def __getattr__(self, attr):
        return getattr(self.m, attr)


# -------------------------------------------------------------------------
class VerilogReadVisitor(object):

    def __init__(self, ast_module_dict, converted_modules=None):
        self.ast_module_dict = ast_module_dict
        self.converted_modules = (collections.OrderedDict()
                                  if converted_modules is None
                                  else converted_modules)
        self.m = None
        self.module_stack = []

    def get_module(self, name):
        if name in self.converted_modules:
            return self.converted_modules[name]
        if name not in self.ast_module_dict:
            return module.StubModule(name)
        visitor = VerilogReadVisitor(
            self.ast_module_dict, self.converted_modules)
        mod = visitor.visit(self.ast_module_dict[name])
        self.converted_modules[name] = mod
        self.converted_modules.update(visitor.converted_modules)
        return mod

    def push_module(self, m):
        self.module_stack.append(self.m)
        self.m = m

    def push_read_only_module(self):
        self.push_module(ReadOnlyModule(self.m))

    def pop_module(self):
        self.m = self.module_stack.pop()

    def add_object(self, obj):
        if isinstance(self.m, module.Module):
            self.m.add_object(obj)
            if isinstance(obj, vtypes._Variable):
                obj.module = self.m

    def generic_visit(self, node):
        for c in node.children():
            self.visit(c)
        #raise TypeError("Unsupported object '%s'" % str(type(node)))

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def visit_ModuleDef(self, node):
        # check module cache
        if node.name in self.converted_modules:
            return self.converted_modules[node.name]

        # create new Verilog module
        m = module.Module(node.name)
        self.push_module(m)
        self.generic_visit(node)
        self.pop_module()

        self.converted_modules[node.name] = m
        return m

    def visit_Paramlist(self, node):
        params = []
        for param in node.params:
            p = self.visit(param)
            params.append(p)
        return params

    def visit_Portlist(self, node):
        ports = []
        for port in node.ports:
            p = self.visit(port)
            ports.append(p)
        return ports

    def visit_Port(self, node):
        if node.type is None:
            name = node.name
            p = vtypes.AnyType(name=name)
            self.add_object(p)
            return p

        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        _type = getattr(vtypes, node.type, None)
        if _type is None:
            raise TypeError("No such port type '%s'" % node.type)
        p = _type(name, width, dims, raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(p)
        return p

    def visit_Width(self, node):
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        return msb, lsb

    def visit_Length(self, node):
        l = self.visit(node.msb)
        r = self.visit(node.lsb)
        return l, r

    def visit_Dimensions(self, node):
        dims = []
        for length in node.lengths:
            dims.append(self.visit(length))
        return tuple(dims)

    def visit_Identifier(self, node):
        if node.scope is not None:
            labels = self.visit(node.scope)

            if not isinstance(self.m, (module.Module, ReadOnlyModule)):
                lables.append(vtypes.AnyType(name=node.name))
                return vtypes.Scope(*labels)

            m = self.m
            for label in labels:
                name = label.name if isinstance(label, vtypes.ScopeIndex) else label
                m = m.find_identifier(name)

            v = m.find_identifier(node.name)
            if v is None:
                labels.append(vtypes.AnyType(name=node.name))
            elif v.name in m.variable:
                labels.append(m.variable[v.name])
            else:
                labels.append(v)

            return vtypes.Scope(*labels)

        if not isinstance(self.m, (module.Module, ReadOnlyModule)):
            return vtypes.AnyType(name=node.name)

        ret = self.m.find_identifier(node.name)
        if ret is None:
            return vtypes.AnyType(name=node.name)
        if ret.name in self.m.variable:
            return self.m.variable[ret.name]
        return ret

    def visit_IntConst(self, node):
        return vtypes.Int(node.value)

    def visit_FloatConst(self, node):
        return vtypes.Float(node.value)

    def visit_StringConst(self, node):
        return vtypes.Str(node.value)

    def visit_Input(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Input(width, dims, signed=signed, name=name,
                           raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Output(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Output(width, dims, signed=signed, name=name,
                            raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Inout(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Inout(width, dims, signed=signed, name=name,
                           raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Tri(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Tri(width, dims, signed=signed, name=name,
                         raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Wire(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Wire(width, dims, signed=signed, name=name,
                          raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Reg(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Reg(width, dims, signed=signed, name=name,
                         raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Integer(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        signed = node.signed
        obj = vtypes.Integer(width, dims, signed=signed, name=name,
                             raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Real(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        obj = vtypes.Real(width, dims, name=name, raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Genvar(self, node):
        name = node.name
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        raw_dims = self.visit(node.dimensions) if node.dimensions is not None else None
        dims = to_dims(raw_dims)
        obj = vtypes.Genvar(width, dims, name=name, raw_width=raw_width, raw_dims=raw_dims)
        self.add_object(obj)
        return obj

    def visit_Ioport(self, node):
        first = self.visit(node.first)
        second = self.visit(node.second) if node.second is not None else None
        return (first, second)

    def visit_Parameter(self, node):
        name = node.name
        value = self.visit(node.value)
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        signed = node.signed
        param = vtypes.Parameter(value, width, signed, name=name, raw_width=raw_width)
        self.add_object(param)
        return param

    def visit_Localparam(self, node):
        name = node.name
        value = self.visit(node.value)
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        signed = node.signed
        param = vtypes.Localparam(value, width, signed, name=name, raw_width=raw_width)
        self.add_object(param)
        return param

    def visit_Supply(self, node):
        name = node.name
        value = self.visit(node.value)
        raw_width = self.visit(node.width) if node.width is not None else None
        width = to_width(raw_width)
        signed = node.signed
        param = vtypes.Supply(value, width, signed, name=name, raw_width=raw_width)
        self.add_object(param)
        return param

    def visit_Decl(self, node):
        decl = [self.visit(d) for d in node.list]
        return decl

    def visit_Concat(self, node):
        vars = [self.visit(var) for var in node.list]
        return vtypes.Cat(*vars)

    def visit_LConcat(self, node):
        vars = [self.visit(var) for var in node.list]
        return vtypes.Cat(*vars)

    def visit_Repeat(self, node):
        var = self.visit(node.value)
        times = self.visit(node.times)
        return vtypes.Repeat(var, times)

    def visit_Partselect(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        return vtypes.Slice(var, msb, lsb)

    def visit_Pointer(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.ptr)
        return vtypes.Pointer(var, pos)

    def visit_Lvalue(self, node):
        return self.visit(node.var)

    def visit_Rvalue(self, node):
        return self.visit(node.var)

    def visit_Uplus(self, node):
        return vtypes.Uplus(self.visit(node.right))

    def visit_Uminus(self, node):
        return vtypes.Uminus(self.visit(node.right))

    def visit_Ulnot(self, node):
        return vtypes.Ulnot(self.visit(node.right))

    def visit_Unot(self, node):
        return vtypes.Unot(self.visit(node.right))

    def visit_Uand(self, node):
        return vtypes.Uand(self.visit(node.right))

    def visit_Unand(self, node):
        return vtypes.Unand(self.visit(node.right))

    def visit_Uor(self, node):
        return vtypes.Uor(self.visit(node.right))

    def visit_Unor(self, node):
        return vtypes.Unor(self.visit(node.right))

    def visit_Uxor(self, node):
        return vtypes.Uxor(self.visit(node.right))

    def visit_Uxnor(self, node):
        return vtypes.Uxnor(self.visit(node.right))

    def visit_Power(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Power(left, right)

    def visit_Times(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Times(left, right)

    def visit_Divide(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Divide(left, right)

    def visit_Mod(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Mod(left, right)

    def visit_Plus(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Plus(left, right)

    def visit_Minus(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Minus(left, right)

    def visit_Sll(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Sll(left, right)

    def visit_Srl(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Srl(left, right)

    def visit_Sra(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Sra(left, right)

    def visit_LessThan(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.LessThan(left, right)

    def visit_GreaterThan(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.GreaterThan(left, right)

    def visit_LessEq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.LessEq(left, right)

    def visit_GreaterEq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.GreaterEq(left, right)

    def visit_Eq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Eq(left, right)

    def visit_NotEq(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.NotEq(left, right)

    def visit_Eql(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Eql(left, right)

    def visit_NotEql(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.NotEql(left, right)

    def visit_And(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.And(left, right)

    def visit_Xor(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Xor(left, right)

    def visit_Xnor(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Xnor(left, right)

    def visit_Or(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Or(left, right)

    def visit_Land(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Land(left, right)

    def visit_Lor(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vtypes.Lor(left, right)

    def visit_Cond(self, node):
        condition = self.visit(node.cond)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        return vtypes.Cond(condition, true_value, false_value)

    def visit_Assign(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay = self.visit(
            node.ldelay.value) if node.ldelay is not None else None
        rdelay = self.visit(
            node.rdelay.value) if node.rdelay is not None else None
        subst = vtypes.Subst(left, right, ldelay=ldelay, rdelay=rdelay)
        assign = vtypes.Assign(subst)
        self.add_object(assign)
        return assign

    def visit_Always(self, node):
        # to avoid to call self.add_object() for the current Module
        self.push_read_only_module()

        sensitivity = self.visit(node.sens_list)
        statement = to_tuple(self.visit(node.statement))
        always = vtypes.Always(*sensitivity)
        always = always(*statement)

        # to restore the current Module
        self.pop_module()

        self.add_object(always)
        return always

    def visit_SensList(self, node):
        return [self.visit(s) for s in node.list]

    def visit_Sens(self, node):
        if node.type == 'posedge':
            sig = self.visit(node.sig)
            return vtypes.Posedge(sig)
        if node.type == 'negedge':
            sig = self.visit(node.sig)
            return vtypes.Negedge(sig)
        if node.type == 'all':
            return vtypes.SensitiveAll()
        if node.type == 'level':
            sig = self.visit(node.sig)
            return sig
        raise TypeError("Unsupported sensitivity type '%s'" % node.type)

    def visit_BlockingSubstitution(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay = self.visit(
            node.ldelay.delay) if node.ldelay is not None else None
        rdelay = self.visit(
            node.rdelay.delay) if node.rdelay is not None else None
        return vtypes.Subst(left, right, blk=True, ldelay=ldelay, rdelay=rdelay)

    def visit_NonblockingSubstitution(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay = self.visit(
            node.ldelay.delay) if node.ldelay is not None else None
        rdelay = self.visit(
            node.rdelay.delay) if node.rdelay is not None else None
        return vtypes.Subst(left, right, blk=False, ldelay=ldelay, rdelay=rdelay)

    def visit_IfStatement(self, node):
        if isinstance(self.m, (module.GenerateFor, module.GenerateIf)):
            return self._visit_GenerateIf(node)
        condition = self.visit(node.cond)
        true_statement = self.visit(node.true_statement)
        false_statement = (self.visit(node.false_statement)
                           if node.false_statement is not None else None)
        true_statement = to_tuple(true_statement)
        false_statement = (to_tuple(false_statement)
                           if false_statement is not None else None)
        _if = vtypes.If(condition)
        _if = _if(*true_statement)
        if false_statement is not None:
            _if = _if(*false_statement)
        return _if

    def visit_ForStatement(self, node):
        if isinstance(self.m, (module.GenerateFor, module.GenerateIf)):
            return self._visit_GenerateFor(node)
        pre = self.visit(node.pre)
        condition = self.visit(node.cond)
        post = self.visit(node.post)
        statement = to_tuple(self.visit(node.statement))
        _for = vtypes.For(pre, condition, post)
        _for = _for(*statement)
        return _for

    def visit_WhileStatement(self, node):
        condition = self.visit(node.cond)
        statement = to_tuple(self.visit(node.statement))
        _while = vtypes.While(condition)
        _while = _while(*statement)
        return _while

    def visit_CaseStatement(self, node):
        comp = self.visit(node.comp)
        statement = tuple([self.visit(case) for case in node.caselist])
        case = vtypes.Case(comp)
        case = case(*statement)
        return case

    def visit_CasexStatement(self, node):
        comp = self.visit(node.comp)
        statement = tuple([self.visit(case) for case in node.caselist])
        case = vtypes.Casex(comp)
        case = case(*statement)
        return case

    def visit_Case(self, node):
        condition = tuple([self.visit(c)
                           for c in node.cond]) if node.cond else [None]
        statement = to_tuple(self.visit(node.statement))
        when = vtypes.When(*condition)
        when = when(*statement)
        return when

    def visit_Block(self, node):
        statements = [self.visit(statement) for statement in node.statements]
        return statements

    def visit_Initial(self, node):
        statement = to_tuple(self.visit(node.statement))
        initial = vtypes.Initial(*statement)
        self.add_object(initial)
        return initial

    def visit_EventStatement(self, node):
        sensitivity = self.visit(node.sens_list)
        event = vtypes.Event(*sensitivity)
        return event

    def visit_WaitStatement(self, node):
        condition = self.visit(node.cond)
        statement = to_tuple(self.visit(node.statement)
                             ) if node.statement else None
        wait = vtypes.Wait(condition)
        if statement:
            wait = wait(*statement)
        return wait

    def visit_ForeverStatement(self, node):
        statement = to_tuple(self.visit(node.statement))
        forever = vtypes.Forever(*statement)
        return forever

    def visit_DelayStatement(self, node):
        value = self.visit(node.delay)
        delay = vtypes.Delay(value)
        return delay

    def visit_InstanceList(self, node):
        return [self.visit(instance) for instance in node.instances]

    def visit_Instance(self, node):
        m = self.get_module(node.module)
        instname = node.name
        params = [self.visit(param) for param in node.parameterlist]
        ports = [self.visit(port) for port in node.portlist]
        if node.array is not None:
            raise ValueError("Instance array is not currently supported.")
        instance = module.Instance(m, instname, params, ports)
        self.add_object(instance)
        return instance

    def visit_ParamArg(self, node):
        paramname = node.paramname
        argname = self.visit(node.argname)
        return (paramname, argname)

    def visit_PortArg(self, node):
        portname = node.portname
        argname = self.visit(
            node.argname) if node.argname is not None else None
        return (portname, argname)

    def visit_Function(self, node):
        # to avoid to call self.add_object() for the current Module
        self.push_read_only_module()

        name = node.name
        raw_width = (self.visit(node.retwidth)
                     if node.retwidth is not None else None)
        width = to_width(raw_width)
        func = function.Function(name, width, raw_width=raw_width)
        statement = [self.visit(s) for s in node.statement]
        body = []

        for s in statement:
            if isinstance(s, (tuple, list)):  # from the visitor result of decl
                for d in s:
                    if isinstance(d, vtypes.Input):
                        t = func.Input(d.name, d.width, d.dims, d.signed, d.value)
                        t.raw_width = d.raw_width
                        t.raw_dims = d.raw_dims
                    elif isinstance(d, vtypes.Reg):
                        t = func.Reg(d.name, d.width, d.dims, d.signed, d.value)
                        t.raw_width = d.raw_width
                        t.raw_dims = d.raw_dims
                    elif isinstance(d, vtypes.Integer):
                        t = func.Integer(d.name, d.width, d.dims, d.signed, d.value)
                        t.raw_width = d.raw_width
                        t.raw_dims = d.raw_dims
                    else:
                        body.append(s)
            else:
                body.append(s)

        func.Body(*body)

        # to restore the current Module
        self.pop_module()

        self.add_object(func)
        return func

    def visit_FunctionCall(self, node):
        name = self.visit(node.name)
        args = tuple([self.visit(arg) for arg in node.args])
        call = function.FunctionCall(name, *args)
        return call

    def visit_Task(self, node):
        # to avoid to call self.add_object() for the current Module
        self.push_read_only_module()

        name = node.name
        _task = task.Task(name)
        statement = [self.visit(s) for s in node.statement]
        body = []

        for s in statement:
            if isinstance(s, (tuple, list)):  # from the visitor result of decl
                for d in s:
                    if isinstance(d, vtypes.Input):
                        t = _task.Input(d.name, d.width, d.dims, d.signed, d.value)
                        t.raw_width = d.raw_width
                        t.raw_dims = d.raw_dims
                    elif isinstance(d, vtypes.Reg):
                        t = _task.Reg(d.name, d.width, d.dims, d.signed, d.value)
                        t.raw_width = d.raw_width
                        t.raw_dims = d.raw_dims
                    elif isinstance(d, vtypes.Integer):
                        t = _task.Integer(d.name, d.width, d.dims, d.signed, d.value)
                        t.raw_width = d.raw_width
                        t.raw_dims = d.raw_dims
                    else:
                        body.append(s)
            else:
                body.append(s)

        _task.Body(*body)

        # to restore the current Module
        self.pop_module()

        self.add_object(_task)
        return _task

    def visit_TaskCall(self, node):
        name = self.visit(node.name)
        args = tuple([self.visit(arg) for arg in node.args])
        call = task.TaskCall(name, args)
        return call

    def _visit_GenerateFor(self, item):
        pre = self.visit(item.pre)
        cond = self.visit(item.cond)
        post = self.visit(item.post)
        scope = (item.statement.scope
                 if isinstance(item.statement, vast.Block)
                 else None)
        _for = module.GenerateFor(self.m, pre, cond, post, scope)
        ret = _for
        self.add_object(_for)
        self.push_module(_for)
        statement = self.visit(item.statement)
        self.pop_module()
        return ret

    def _visit_GenerateIf(self, item):
        cond = self.visit(item.cond)
        true_scope = (item.true_statement.scope
                      if isinstance(item.true_statement, vast.Block)
                      else None)
        false_scope = (item.false_statement.scope
                       if isinstance(item.false_statement, vast.Block)
                       else None)
        _if_true = module.GenerateIf(self.m, cond, true_scope)
        ret = _if_true
        self.add_object(_if_true)
        self.push_module(_if_true)
        statement = self.visit(item.true_statement)
        self.pop_module()
        _if_false = _if_true.Else(false_scope)
        self.add_object(_if_false)
        self.push_module(_if_false)
        statement = (self.visit(item.false_statement)
                     if item.false_statement is not None else None)
        self.pop_module()
        return ret

    def visit_GenerateStatement(self, node):
        ret = []
        for item in node.items:
            if isinstance(item, vast.ForStatement):
                ret.append(self._visit_GenerateFor(item))
            elif isinstance(item, vast.IfStatement):
                ret.append(self._visit_GenerateIf(item))
            else:
                raise TypeError(
                    "Only generate-for and generate-if statements are supported.")
        return ret

    def visit_SystemCall(self, node):
        cmd = node.syscall
        args = tuple([self.visit(arg) for arg in node.args])
        systask = vtypes.SystemTask(cmd, *args)
        return systask

    def visit_IdentifierScopeLabel(self, node):
        if node.loop is None:
            return node.name
        index = self.visit(node.loop)
        return vtypes.ScopeIndex(node.name, index)

    def visit_IdentifierScope(self, node):
        args = [self.visit(label) for label in node.labellist]
        return args

    def visit_Pragma(self, node):
        raise TypeError("Pragma is not currently supported.")

    def visit_PragmaEntry(self, node):
        raise TypeError("Pragma is not currently supported.")

    def visit_Disable(self, node):
        raise TypeError("Disable is not currently supported.")

    def visit_ParallelBlock(self, node):
        raise TypeError("Fork/Join is not currently supported.")

    def visit_SingleStatement(self, node):
        statement = self.visit(node.statement)
        if isinstance(statement, vtypes.Delay):
            return statement
        return vtypes.SingleStatement(statement)


def to_width(raw_width):
    if raw_width is None:
        return None

    msb = raw_width[0]
    lsb = raw_width[1]

    if isinstance(msb, vtypes.Int):
        msb = msb.value

    if isinstance(lsb, vtypes.Int):
        lsb = lsb.value

    if isinstance(lsb, int):
        if lsb == 0:
            return msb + 1
        return msb - (lsb - 1)

    if isinstance(msb, vtypes._Numeric):
        return msb - lsb + 1

    msb = vtypes.Int(msb)

    return msb - lsb + 1


def to_dims(raw_dims):
    if raw_dims is None:
        return None

    dims = []

    for raw_dim in raw_dims:
        dims.append(to_width((raw_dim[1], raw_dim[0])))

    return tuple(dims)
