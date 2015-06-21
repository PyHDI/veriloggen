import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import module
import vtypes

import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

#-------------------------------------------------------------------------------
def toVerilog(node):
    visitor = VerilogModuleVisitor()
    verilogdef = visitor.visit(node)
    codegen = ASTCodeGenerator()
    return codegen.visit(verilogdef)

#-------------------------------------------------------------------------------
class VerilogModuleVisitor(object):
    def __init__(self):
        self.bind_visitor = VerilogBindVisitor()
        self.module = None
    
    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))
    
    def visit(self, node):
        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    #---------------------------------------------------------------------------
    def visit_Module(self, node):
        self.module = node
        name = node.name
        params = ([ self.visit(v) for v in node.global_constant.values() ])
        params = [ i for i in params if i is not None ]
        paramlist = vast.Paramlist(params)
        ports = [ self.visit(v) for v in node.io_variable.values() ]
        ports = [ i for i in ports if i is not None ]
        portlist = vast.Portlist(ports)
        items = ([ self.visit(v) for v in node.constant.values() ] + 
                 [ self.visit(v) for v in node.variable.values() ] + 
                 [ self.visit(v) for v in node.assign ] +
                 [ self.visit(v) for v in node.always ] +
                 [ self.visit(v) for v in node.instance.values() ])
        items = [ i for i in items if i is not None ]
        m = vast.ModuleDef(name, paramlist, portlist, items)
        self.module = None
        return m

    #---------------------------------------------------------------------------
    def visit_Parameter(self, node):
        name = node.name
        value = self.visit(node.value)
        width = None if node.width is None else self.visit(node.width)
        signed = node.signed
        return vast.Parameter(name, value, width, signed)

    def visit_Localparam(self, node):
        name = node.name
        value = self.visit(node.value)
        width = None if node.width is None else self.visit(node.width)
        signed = node.signed
        return vast.Localparam(name, value, width, signed)
    
    #---------------------------------------------------------------------------
    def visit_Input(self, node):
        name = node.name
        width = None if node.width is None else self.mkWidth(node.width)
        signed = node.signed
        return vast.Ioport(vast.Input(name, width, signed))
    
    def visit_Output(self, node):
        name = node.name
        width = None if node.width is None else self.mkWidth(node.width)
        signed = node.signed
        first = vast.Output(name, width, signed)
        second = vast.Reg(name, width, signed) if self.module.isReg(name) else None
        return vast.Ioport(first, second)
    
    def visit_Inout(self, node):
        name = node.name
        width = None if node.width is None else self.mkWidth(node.width)
        signed = node.signed
        return vast.Ioport(vast.Inout(name, width, signed))
    
    def visit_Reg(self, node):
        name = node.name
        if self.module.isOutput(name): return None
        width = None if node.width is None else self.mkWidth(node.width)
        length = None if node.length is None else self.mkLength(node.width)
        signed = node.signed
        if length is not None:
            return vast.RegArray(name, width, length, signed)
        return vast.Reg(name, width, signed)
    
    def visit_Wire(self, node):
        name = node.name
        width = None if node.width is None else self.mkWidth(node.width)
        length = None if node.length is None else self.mkLength(node.width)
        signed = node.signed
        if length is not None:
            return vast.WireArray(name, width, length, signed)
        return vast.Wire(name, width, signed)
    
    #---------------------------------------------------------------------------
    def visit_Always(self, node):
        sensitivity = None
        if isinstance(node.sensitivity, list) or isinstance(node.sensitivity, tuple):
            sensitivity = vast.SensList(tuple([ self.visit(n) if isinstance(n, vtypes.Edge) else
                                                vast.Sens(self.visit(n))
                                                for n in node.sensitivity ]))
        else:
            sensitivity = vast.SensList((self.visit(node.sensitivity),)
                                        if isinstance(node.sensitivity, vtypes.Edge) else
                                        vast.Sens(self.visit(node.sensitivity)))

        statement = vast.Block([])
        if isinstance(node.statement, list) or isinstance(node.statement, tuple):
            statement = vast.Block(tuple([ self.bind_visitor.visit(n) for n in node.statement ]))
        else:
            statement = self.bind_visitor.visit(node.statement)
        return vast.Always(sensitivity, statement)

    #---------------------------------------------------------------------------
    def visit_Assign(self, node):
        left = self.bind_visitor.visit(node.left)
        right = self.bind_visitor.visit(node.right)
        return vast.Assign(left, right)
    
    #---------------------------------------------------------------------------
    def visit_Instance(self, node):
        module = node.module.name
        parameterlist = [ vast.ParamArg(p, self.bind_visitor.visit(a)) for p, a in node.params ] 
        portlist = [ vast.PortArg(p, self.bind_visitor.visit(a)) for p, a in node.ports ]
        name = node.instname
        instance = vast.Instance(module, name, portlist, parameterlist)
        return vast.InstanceList(module, parameterlist, (instance,) )
        
    #---------------------------------------------------------------------------
    def visit_Posedge(self, node):
        sig = self.bind_visitor.visit(node.name)
        t = 'posedge'
        return vast.Sens(sig, t)
    
    def visit_Negedge(self, node):
        sig = self.bind_visitor.visit(node.name)
        t = 'negedge'
        return vast.Sens(sig, t)
    
    #---------------------------------------------------------------------------
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
    
    #---------------------------------------------------------------------------
    def visit_int(self, node):
        return vast.IntConst(str(node))

    def visit_str(self, node):
        return vast.StringConst(node)

    def visit_float(self, node):
        return vast.FloatConst(str(node))
    
    #---------------------------------------------------------------------------
    def mkWidth(self, node):
        msb = vast.Minus(self.bind_visitor.visit(node), vast.IntConst('1'))
        lsb = vast.IntConst('0')
        return vast.Width(msb, lsb)
    
    def mkLength(self, node):
        msb = vast.IntConst('0')
        lsb = vast.Minus(self.bind_visitor.visit(node), vast.IntConst('1'))
        return vast.Length(msb, lsb)
    
#-------------------------------------------------------------------------------
class VerilogBindVisitor(object):
    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))
    
    def visit(self, node):
        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    #---------------------------------------------------------------------------
    def visit_Parameter(self, node):
        name = node.name
        return vast.Identifier(name)

    def visit_Localparam(self, node):
        name = node.name
        return vast.Identifier(name)
    
    #---------------------------------------------------------------------------
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
    
    #---------------------------------------------------------------------------
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
    
    #---------------------------------------------------------------------------
    def visit_Bit(self, node):
        var = self.visit(node.var)
        pos = self.visit(node.pos)
        return vast.Pointer(var, pos)

    def visit_Slice(self, node):
        var = self.visit(node.var)
        msb = self.visit(node.msb)
        lsb = self.visit(node.lsb)
        return vast.Partselect(var, msb, lsb)

    def visit_Cond(self, node):
        cond = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        return vast.Cond(cond, true_value, false_value)
    
    #---------------------------------------------------------------------------
    def visit_int(self, node):
        return vast.IntConst(str(node))

    def visit_str(self, node):
        return vast.StringConst(node)

    def visit_float(self, node):
        return vast.FloatConst(str(node))
    
    def visit_list(self, node):
        return vast.Block(tuple([ self.visit(n) for n in node ]))

    def visit_tuple(self, node):
        return self.visit_list(node)

    #---------------------------------------------------------------------------
    def visit_If(self, node):
        cond = self.visit(node.condition)
        true_statement = self.visit(node.true_statement)
        false_statement = (self.visit(node.false_statement)
                           if node.false_statement is not None else None)
        return vast.IfStatement(cond, true_statement, false_statement)

    def visit_Subst(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.NonblockingSubstitution(left, right)
