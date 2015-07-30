import sys
import os
import collections

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import module
import vtypes

import pyverilog.vparser.ast as vast
from pyverilog.vparser.parser import VerilogCodeParser
from pyverilog.dataflow.modulevisitor import ModuleVisitor

#-------------------------------------------------------------------------------
class VerilogModules(object):
    def __init__(self, module_dict):
        self.module_dict = module_dict

    def get_stubmodules(self):
        return collections.OrderedDict([ (name, module.StubModule(name))
                                         for name in self.module_dict.keys() ])

    def get_modules(self):
        modules = collections.OrderedDict([ (name, module.Module(name))
                                         for name in self.module_dict.keys() ])
        return modules

#-------------------------------------------------------------------------------
class VerilogModuleVisitor(object):
    def __init__(self):
        self.m = None
    
    def generic_visit(self, node):
        for c in node.children():
            self.visit(c)
            
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def visit_ModuleDef(self, node):
        if not isinstance(node, vast.Module):
            raise TypeError("node must be ast.Module, not %s." % type(node))
        self.m = module.Module(node.name)
        self.generic_visit(node)

    def visit_Paramlist(self, node): pass
    def visit_Portlist(self, node): pass
    def visit_Port(self, node): pass
    def visit_Width(self, node): pass
    def visit_Length(self, node): pass
    def visit_Identifier(self, node): pass
    def visit_Value(self, node): pass
    def visit_Constant(self, node): pass
    def visit_IntConst(self, node): pass
    def visit_FloatConst(self, node): pass
    def visit_StringConst(self, node): pass
    def visit_Variable(self, node): pass
    def visit_Input(self, node): pass
    def visit_Output(self, node): pass
    def visit_Inout(self, node): pass
    def visit_Tri(self, node): pass
    def visit_Wire(self, node): pass
    def visit_Reg(self, node): pass
    def visit_WireArray(self, node): pass
    def visit_RegArray(self, node): pass
    def visit_Integer(self, node): pass
    def visit_Real(self, node): pass
    def visit_Genvar(self, node): pass
    def visit_Ioport(self, node): pass
    def visit_Parameter(self, node): pass
    def visit_Localparam(self, node): pass
    def visit_Supply(self, node) : pass
    def visit_Decl(self, node): pass
    def visit_Concat(self, node): pass
    def visit_LConcat(self, node): pass
    def visit_Repeat(self, node): pass
    def visit_Partselect(self, node): pass
    def visit_Pointer(self, node): pass
    def visit_Lvalue(self, node): pass
    def visit_Rvalue(self, node): pass
    def visit_Operator(self, node): pass
    def visit_UnaryOperator(self, node): pass
    def visit_Uplus(self, node): pass
    def visit_Uminus(self, node): pass
    def visit_Ulnot(self, node): pass
    def visit_Unot(self, node): pass
    def visit_Uand(self, node): pass
    def visit_Unand(self, node): pass
    def visit_Uor(self, node): pass
    def visit_Unor(self, node): pass
    def visit_Uxor(self, node): pass
    def visit_Uxnor(self, node): pass
    def visit_Power(self, node): pass
    def visit_Times(self, node): pass
    def visit_Divide(self, node): pass
    def visit_Mod(self, node): pass
    def visit_Plus(self, node): pass
    def visit_Minus(self, node): pass
    def visit_Sll(self, node): pass
    def visit_Srl(self, node): pass
    def visit_Sra(self, node): pass
    def visit_LessThan(self, node): pass
    def visit_GreaterThan(self, node): pass
    def visit_LessEq(self, node): pass
    def visit_GreaterEq(self, node): pass
    def visit_Eq(self, node): pass
    def visit_NotEq(self, node): pass
    def visit_Eql(self, node):  pass
    def visit_NotEql(self, node):  pass
    def visit_And(self, node): pass
    def visit_Xor(self, node): pass
    def visit_Xnor(self, node): pass
    def visit_Or(self, node): pass
    def visit_Land(self, node): pass
    def visit_Lor(self, node): pass
    def visit_Cond(self, node): pass
    def visit_Assign(self, node): pass
    def visit_Always(self, node): pass
    def visit_SensList(self, node): pass
    def visit_Sens(self, node): pass
    def visit_Substitution(self, node): pass
    def visit_BlockingSubstitution(self, node): pass
    def visit_NonblockingSubstitution(self, node): pass
    def visit_IfStatement(self, node): pass
    def visit_ForStatement(self, node): pass
    def visit_WhileStatement(self, node): pass
    def visit_CaseStatement(self, node): pass
    def visit_CasexStatement(self, node): pass
    def visit_Case(self, node): pass
    def visit_Block(self, node): pass
    def visit_Initial(self, node): pass
    def visit_EventStatement(self, node): pass
    def visit_WaitStatement(self, node): pass
    def visit_ForeverStatement(self, node): pass
    def visit_DelayStatement(self, node): pass
    def visit_InstanceList(self, node): pass
    def visit_Instance(self, node): pass
    def visit_ParamArg(self, node): pass
    def visit_PortArg(self, node): pass
    def visit_Function(self, node): pass
    def visit_FunctionCall(self, node): pass
    def visit_Task(self, node): pass
    def visit_TaskCall(self, node): pass
    def visit_GenerateStatement(self, node): pass
    def visit_SystemCall(self, node): pass
    def visit_IdentifierScopeLabel(self, node): pass
    def visit_IdentifierScope(self, node): pass
    def visit_Pragma(self, node): pass
    def visit_PragmaEntry(self, node): pass
    def visit_Disable(self, node): pass
    def visit_ParallelBlock(self, node): pass
    def visit_SingleStatement(self, node): pass
    
#-------------------------------------------------------------------------------
def read_verilog(*filelist, **opt):
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
    
    module_visitor = ModuleVisitor()
    module_visitor.visit(ast)
    module_names = module_visitor.get_modulenames()
    moduleinfotable = module_visitor.get_moduleinfotable()
    moduleinfo = moduleinfotable.getDefinitions()
    
    module_dict = collections.OrderedDict([ (n, d.definition) for n, d in moduleinfo.items() ])

    return VerilogModules(module_dict)
