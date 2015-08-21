from __future__ import absolute_import
from __future__ import print_function
import sys
import os
import re
import collections
import tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import module
import vtypes
import function
import task

import pyverilog.vparser.ast as vast
from pyverilog.vparser.parser import VerilogCodeParser
from pyverilog.dataflow.modulevisitor import ModuleVisitor

#-------------------------------------------------------------------------------
# User interfaces to read Verilog source code
#-------------------------------------------------------------------------------
def read_verilog_stubmodule(*filelist, **opt):
    module_dict = to_module_dict(*filelist, **opt)
    stubs = collections.OrderedDict([ (name, module.StubModule(name)) 
                                      for name in module_dict.keys() ])
    return stubs
    
def read_verilog_module(*filelist, **opt):
    module_dict = to_module_dict(*filelist, **opt)
    visitor = VerilogReadVisitor()
    modules = collections.OrderedDict([ (name, visitor.visit(m) )
                                        for name, m in module_dict.items() ])
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
    
#-------------------------------------------------------------------------------
def to_module_dict(*filelist, **opt):
    ast = to_ast(*filelist, **opt)
    
    module_visitor = ModuleVisitor()
    module_visitor.visit(ast)
    module_names = module_visitor.get_modulenames()
    moduleinfotable = module_visitor.get_moduleinfotable()
    moduleinfo = moduleinfotable.getDefinitions()
    module_dict = collections.OrderedDict([ (n, d.definition) for n, d in moduleinfo.items() ])

    return module_dict

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
def str_to_signed(s):
    targ = s.replace('_','')
    match = re.search(r's(.+)', targ)
    if match is not None:
        return True
    return False

def str_to_value(s):
    targ = s.replace('_','')
    match = re.search(r'h(.+)', targ)
    if match is not None:
        return int(match.group(1), 16), 16
    match = re.search(r'd(.+)', targ)
    if match is not None:
        return int(match.group(1), 10), 10
    match = re.search(r'o(.+)', targ)
    if match is not None:
        return int(match.group(1), 8), 8
    match = re.search(r'b(.+)', targ)
    if match is not None:
        return int(match.group(1), 2), 2
    return int(targ, 10), None
        
def str_to_width(s):
    targ = s.replace('_','')
    match = re.search(r'(.+)\'h.+', targ)
    if match is not None:
        return int(match.group(1), 10)
    match = re.search(r'(.+)\'d.+', targ)
    if match is not None:
        return int(match.group(1), 10)
    match = re.search(r'(.+)\'o.+', targ)
    if match is not None:
        return int(match.group(1), 10)
    match = re.search(r'(.+)\'b.+', targ)
    if match is not None:
        return int(match.group(1), 10)
    return None

def to_tuple(s):
    if not isinstance(s, (list, tuple)):
        return tuple([s])
    return s

#-------------------------------------------------------------------------------
class VerilogReadVisitor(object):
    def __init__(self):
        self.m = None
        self.module_stack = []

    def push_module(self, m):
        self.module_stack.append(self.m)
        self.m = m

    def pop_module(self):
        self.m = self.module_stack.pop()
        
    def add_object(self, obj):
        if isinstance(self.m, module.Module):
            self.m.add_object(obj)
        
    def generic_visit(self, node):
        for c in node.children():
            self.visit(c)
        #raise TypeError("Unsupported object '%s'" % str(type(node)))
            
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def visit_ModuleDef(self, node):
        # create new Verilog module
        m = module.Module(node.name)
        self.push_module(m)
        self.generic_visit(node)
        self.pop_module()
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
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        _type = getattr(vtypes, node.type, None)
        if _type is None:
            raise TypeError("No such port type '%s'" % node.type)
        p = _type(name, width)
        self.add_object(p)
        return p
        
    def visit_Width(self, node):
        msb = self.visit(node.msb)
        width = msb + 1
        return width
        
    def visit_Length(self, node):
        lsb = self.visit(node.lsb)
        length = lsb + 1
        return length
        
    def visit_Identifier(self, node):
        if node.scope is not None:
            labels = self.visit(node.scope)
            labels.append(node.name)
            return vtypes.Scope(*labels)
        if not isinstance(self.m, module.Module):
            return vtypes.AnyType(node.name)
        return self.m.find_identifier(node.name)
        
    def visit_IntConst(self, node):
        value, base = str_to_value(node.value)
        width = str_to_width(node.value)
        signed = str_to_signed(node.value)
        return vtypes.Int(value, width, base, signed)

    def visit_FloatConst(self, node):
        return vtypes.Float(node.value)
        
    def visit_StringConst(self, node):
        return vtypes.Str(node.value)
        
    def visit_Input(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Input(name, width, signed=signed)
        self.add_object(obj)
        return obj
        
    def visit_Output(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Output(name, width, signed=signed)
        self.add_object(obj)
        return obj
        
    def visit_Inout(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Inout(name, width, signed=signed)
        self.add_object(obj)
        return obj
        
    def visit_Tri(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Tri(name, width, signed=signed)
        self.add_object(obj)
        return obj
        
    def visit_Wire(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Wire(name, width, signed=signed)
        self.add_object(obj)
        return obj
    
    def visit_Reg(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Reg(name, width, signed=signed)
        self.add_object(obj)
        return obj
    
    def visit_WireArray(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        length = self.visit(node.length)
        signed = node.signed
        obj = vtypes.Wire(name, width, length=length, signed=signed)
        self.add_object(obj)
        return obj
    
    def visit_RegArray(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        length = self.visit(node.length)
        signed = node.signed
        obj = vtypes.Reg(name, width, length=length, signed=signed)
        self.add_object(obj)
        return obj
        
    def visit_Integer(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        obj = vtypes.Integer(name, width, signed=signed)
        self.add_object(obj)
        return obj
        
    def visit_Real(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        obj = vtypes.Real(name, width)
        self.add_object(obj)
        return obj
        
    def visit_Genvar(self, node):
        name = node.name
        width = self.visit(node.width) if node.width is not None else None
        obj = vtypes.Genvar(name, width)
        self.add_object(obj)
        return obj
        
    def visit_Ioport(self, node):
        first = self.visit(node.first)
        second = self.visit(node.second) if node.second is not None else None
        return (first, second)
        
    def visit_Parameter(self, node):
        name = node.name
        value = self.visit(node.value)
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        param = vtypes.Parameter(name, value, width, signed)
        self.add_object(param)
        return param

    def visit_Localparam(self, node):
        name = node.name
        value = self.visit(node.value)
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        param = vtypes.Localparam(name, value, width, signed)
        self.add_object(param)
        return param
        
    def visit_Supply(self, node):
        name = node.name
        value = self.visit(node.value)
        width = self.visit(node.width) if node.width is not None else None
        signed = node.signed
        param = vtypes.Supply(name, value, width, signed)
        self.add_object(param)
        return param
        
    def visit_Decl(self, node):
        decl = [ self.visit(d) for d in node.list ]
        return decl
        
    def visit_Concat(self, node):
        vars = [ self.visit(var) for var in node.list ]
        return vtypes.Cat(*vars)
        
    def visit_LConcat(self, node):
        vars = [ self.visit(var) for var in node.list ]
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
        return vtype.Uminus(self.visit(node.right))
        
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
        ldelay= self.visit(node.ldelay) if node.ldelay is not None else None
        rdelay = self.visit(node.rdelay) if node.rdelay is not None else None
        subst = vtypes.Subst(left, right, ldelay=ldelay, rdelay=rdelay)
        assign = vtypes.Assign(subst)
        self.add_object(assign)
        return assign
        
    def visit_Always(self, node):
        sensitivity = self.visit(node.sens_list)
        statement = to_tuple(self.visit(node.statement))
        always = vtypes.Always(sensitivity)
        always = always(*statement)
        self.add_object(always)
        return always
        
    def visit_SensList(self, node):
        return [ self.visit(s) for s in node.list ]
        
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
        
    def visit_BlockingSubstitution(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay= self.visit(node.ldelay) if node.ldelay is not None else None
        rdelay = self.visit(node.rdelay) if node.rdelay is not None else None
        return vtypes.Subst(left, right, blk=True, ldelay=ldelay, rdelay=rdelay)
        
    def visit_NonblockingSubstitution(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        ldelay= self.visit(node.ldelay) if node.ldelay is not None else None
        rdelay = self.visit(node.rdelay) if node.rdelay is not None else None
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
        _while = vtypes.While(pre, condition, post)
        _while = _while(*statement)
        return _while
        
    def visit_CaseStatement(self, node):
        comp = self.visit(node.comp)
        statement = tuple([ self.visit(case) for case in node.caselist ])
        case = vtypes.Case(comp)
        case = case(*statement)
        return case
        
    def visit_CasexStatement(self, node):
        comp = self.visit(node.comp)
        statement = tuple([ self.visit(case) for case in node.caselist ])
        case = vtypes.Casex(comp)
        case = case(*statement)
        return case
        
    def visit_Case(self, node):
        condition = tuple([ self.visit(c) for c in node.cond ])
        statement = to_tuple(self.visit(node.statement))
        when = vtypes.When(*condition)
        when = when(*statement)
        return when
        
    def visit_Block(self, node):
        statements = [ self.visit(statement) for statement in  node.statements ]
        return statements
        
    def visit_Initial(self, node):
        statement = to_tuple(self.visit(node.statement))
        initial = vtypes.Initial(*statement)
        self.add_object(initial)
        return initial
        
    def visit_EventStatement(self, node):
        sensitivity = self.visit(node.sens_list)
        event = vtypes.Event(sensitivity)
        return event
        
    def visit_WaitStatement(self, node):
        condition = self.visit(node.cond)
        statement = to_tuple(self.visit(node.statement))
        wait = vtypes.Wait()
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
        return [ self.visit(instance) for instance in node.instances ]
        
    def visit_Instance(self, node):
        module = module.StubModule(node.module)
        instname = node.name
        params = [ self.visit(param) for param in node.parameterlist ]
        ports = [ self.visit(port) for port in node.portlist ]
        if node.array is not None:
            raise ValueError("Instance array is not currently supported.")
        instance = vtypes.Instance(module, instname, params, ports)
        self.add_object(instance)
        return instance
        
    def visit_ParamArg(self, node):
        paramname = node.paramname
        argname = self.visit(node.argname)
        return (paramname, argname)
        
    def visit_PortArg(self, node):
        portname = node.portname
        argname = self.visit(node.argname)
        return (portname, argname)
    
    def visit_Function(self, node):
        name = node.name
        width = self.visit(retwidth) if node.width is not None else None
        function = vtypes.Function(name, width)
        statement = [ self.visit(s) for s in node.statement ]
        body = []
        for s in statement:
            if isinstance(s, vtypes.Input):
                function.Input(s.name, s.width, s.length, s.signed, s.value)
            elif isinstance(s, vtypes.Reg):
                function.Reg(s.name, s.width, s.length, s.signed, s.value)
            elif isinstance(s, vtypes.Integer):
                function.Integer(s.name, s.width, s.length, s.signed, s.value)
            else:
                body.append(s)
        function.Body(*body)
        self.add_object(function)
        return function
        
    def visit_FunctionCall(self, node):
        name = self.visit(node.name)
        args = tuple([ self.visit(arg) for arg in ndoe.args ])
        call = vtypes.FunctionCall(name, args)
        return call
        
    def visit_Task(self, node):
        name = node.name
        width = self.visit(retwidth) if node.width is not None else None
        task = vtypes.Task(name, width)
        statement = [ self.visit(s) for s in node.statement ]
        body = []
        for s in statement:
            if isinstance(s, vtypes.Input):
                task.Input(s.name, s.width, s.length, s.signed, s.value)
            elif isinstance(s, vtypes.Reg):
                task.Reg(s.name, s.width, s.length, s.signed, s.value)
            elif isinstance(s, vtypes.Integer):
                task.Integer(s.name, s.width, s.length, s.signed, s.value)
            else:
                body.append(s)
        task.Body(*body)
        self.add_object(task)
        return task
        
    def visit_TaskCall(self, node):
        name = self.visit(node.name)
        args = tuple([ self.visit(arg) for arg in ndoe.args ])
        call = vtypes.TaskCall(name, args)
        return call

    def _visit_GenerateFor(self, item):
        pre = self.visit(item.pre)
        cond = self.visit(item.cond)
        post = self.visit(item.post)
        scope = (item.statement.scope
                 if isinstance(item.statement, vast.Block)
                 else None)
        _for = module.GenerateFor(pre, cond, post, scope)
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
        _if_true = module.GenerateIf(cond, true_scope)
        ret = _if_true
        self.add_object(_if_true)
        self.push_module(_if_true)
        statement = self.visit(item.true_statement)
        self.pop_module()
        _if_false = _if_true.Else(false_scope)
        self.push_module(_if_false)
        statement = self.visit(item.false_statement)
        self.pop_module()
        return ret
        
    def visit_GenerateStatement(self, node):
        ret = []
        for item in node.items:
            if isinstance(item, vast.ForStatement):
                ret.append( self._visit_GenerateFor(item) )
            elif isinstance(item, vast.IfStatement):
                ret.append( self._visit_GenerateIf(item) )
            else:
                raise TypeError("Only generate-for and generate-if statements are supported.")
        return ret
    
    def visit_SystemCall(self, node):
        cmd = node.syscall
        args = tuple([ self.visit(a) for arg in node.args ])
        systask = vtypes.SystemTask(cmd, *args)
        return systask
    
    def visit_IdentifierScopeLabel(self, node):
        if node.loop is None:
            return node.name
        index = self.visit(node.loop)
        return vtypes.ScopeIndex(node.name, index)
    
    def visit_IdentifierScope(self, node):
        args = [ self.visit(label) for label in node.labellist ]
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
        return self.visit(node.statement)
        
