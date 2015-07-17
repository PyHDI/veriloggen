import sys
import os
import collections

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import module
import vtypes

import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

#-------------------------------------------------------------------------------
def to_verilog(node, filename=None):
    visitor = VerilogModuleVisitor()
    modules = tuple(get_modules(node).values())
    
    module_ast_list = [ visitor.visit(module) for module in modules ]
    description = vast.Description(module_ast_list)
    source = vast.Source(filename, description)
    
    codegen = ASTCodeGenerator()
    code = codegen.visit(source)
    if filename:
        with open(filename, 'w') as f:
            f.write(code)
    return code

def get_modules(node):
    modules = collections.OrderedDict()
    modules[node.name] = node
    modules.update(node.submodule)
    for sub in node.submodule.values():
        modules.update( get_modules(sub) )
    return modules
    
#-------------------------------------------------------------------------------
class VerilogCommonVisitor(object):
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
    
    def visit_Integer(self, node):
        name = node.name
        return vast.Identifier(name)
    
    def visit_Real(self, node):
        name = node.name
        return vast.Identifier(name)
    
    def visit_Genvar(self, node):
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
    def visit_Unot(self, node):
        right = self.visit(node.right)
        return vast.Unot(right)
    
    def visit_Ulnot(self, node):
        right = self.visit(node.right)
        return vast.Ulnot(right)
    
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
        vars = tuple([ self.visit(var) for var in node.vars ])
        return vast.Concat(vars)

    #---------------------------------------------------------------------------
    def visit_Cond(self, node):
        cond = self.visit(node.condition)
        true_value = self.visit(node.true_value)
        false_value = self.visit(node.false_value)
        return vast.Cond(cond, true_value, false_value)
    
    #---------------------------------------------------------------------------
    # First class object wrapper
    def visit_Int(self, node):
        value_list = []
        if node.width:
            value_list.append(str(node.width))
            
        if node.base is None:
            if node.width:
                value_list.append("'d")
            value_list.append(str(node.value))
        elif node.base == 2:
            value_list.append("'b")
            value_list.append(bin(node.value).replace('0b', ''))
        elif node.base == 8:
            value_list.append("'o")
            value_list.append(oct(node.value).replace('0o', ''))
        elif node.base == 10:
            value_list.append("'d")
            value_list.append(str(node.value))
        elif node.base == 16:
            value_list.append("'h")
            value_list.append(hex(node.value).replace('0x', ''))
        else:
            raise ValueError("Int.base should be 2, 8, 10, or 16")
        
        return vast.IntConst(''.join(value_list))

    def visit_Float(self, node):
        return vast.FloatConst(str(node.value))
    
    def visit_Str(self, node):
        return vast.StringConst(node.value)

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

    #---------------------------------------------------------------------------
    def visit_For(self, node):
        pre = self.visit(node.pre)
        cond = self.visit(node.condition)
        post = self.visit(node.post)
        statement = self.visit(node.statement)
        return vast.ForStatement(pre, cond, post, statement)

    #---------------------------------------------------------------------------
    def visit_While(self, node):
        cond = self.visit(node.condition)
        statement = self.visit(node.statement)
        return vast.WhileStatement(cond, statement)

    #---------------------------------------------------------------------------
    def visit_Case(self, node):
        comp = self.visit(node.comp)
        statement = tuple([ self.visit(s) for s in node.statement ])
        return vast.CaseStatement(comp, statement)
    
    #---------------------------------------------------------------------------
    def visit_When(self, node):
        cond = tuple([ self.visit(c) for c in node.condition ]) if node.condition else None
        statement = self.visit(node.statement)
        return vast.Case(cond, statement)
    
    #---------------------------------------------------------------------------
    def visit_Function(self, node):
        name = node.name
        return vast.Identifier(name)
    
    def visit_FunctionCall(self, node):
        name = vast.Identifier(node.name)
        args = tuple([ self.visit(a) for a in node.args ])
        return vast.FunctionCall(name, args)
    
#-------------------------------------------------------------------------------
class VerilogModuleVisitor(VerilogCommonVisitor):
    def __init__(self):
        VerilogCommonVisitor.__init__(self)
        self.bind_visitor = VerilogBindVisitor()
        self.always_visitor = VerilogAlwaysVisitor()
        self.function_visitor = VerilogFunctionVisitor()
        self.module = None
    
    #---------------------------------------------------------------------------
    def make_width(self, node):
        msb = vast.Minus(self.bind_visitor.visit(node), vast.IntConst('1'))
        lsb = vast.IntConst('0')
        return vast.Width(msb, lsb)
    
    def make_length(self, node):
        msb = vast.IntConst('0')
        lsb = vast.Minus(self.bind_visitor.visit(node), vast.IntConst('1'))
        return vast.Length(msb, lsb)

    #---------------------------------------------------------------------------
    def visit(self, node):
        if isinstance(node, module.Module): return self.visit_Module(node)
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
                 [ self.visit(v) for v in node.function ] +
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
        width = None if node.width is None else self.make_width(node.width)
        signed = node.signed
        return vast.Ioport(vast.Input(name, width, signed))
    
    def visit_Output(self, node):
        name = node.name
        width = None if node.width is None else self.make_width(node.width)
        signed = node.signed
        first = vast.Output(name, width, signed)
        second = vast.Reg(name, width, signed) if self.module.is_reg(name) else None
        return vast.Ioport(first, second)
    
    def visit_Inout(self, node):
        name = node.name
        width = None if node.width is None else self.make_width(node.width)
        signed = node.signed
        return vast.Ioport(vast.Inout(name, width, signed))
    
    def visit_Reg(self, node):
        name = node.name
        if self.module.is_output(name): return None
        width = None if node.width is None else self.make_width(node.width)
        length = None if node.length is None else self.make_length(node.width)
        signed = node.signed
        if length is not None:
            return vast.RegArray(name, width, length, signed)
        return vast.Reg(name, width, signed)
    
    def visit_Wire(self, node):
        name = node.name
        width = None if node.width is None else self.make_width(node.width)
        length = None if node.length is None else self.make_length(node.width)
        signed = node.signed
        if length is not None:
            return vast.WireArray(name, width, length, signed)
        return vast.Wire(name, width, signed)
    
    def visit_Integer(self, node):
        name = node.name
        width = None if node.width is None else self.make_width(node.width)
        signed = node.signed
        return vast.Integer(name, width, signed)
    
    def visit_Real(self, node):
        name = node.name
        width = None if node.width is None else self.make_width(node.width)
        signed = node.signed
        return vast.Real(name, width, signed)
    
    def visit_Genvar(self, node):
        name = node.name
        width = None if node.width is None else self.make_width(node.width)
        signed = node.signed
        return vast.Genvar(name, width, signed)
    
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
            statement = vast.Block(tuple([ self.always_visitor.visit(n) for n in node.statement ]))
        else:
            statement = self.always_visitor.visit(node.statement)
        return vast.Always(sensitivity, statement)

    #---------------------------------------------------------------------------
    def visit_Assign(self, node):
        if not isinstance(node.statement, vtypes.Subst):
            raise TypeError("Assign expects Subst object.")
        left = self.bind_visitor.visit(node.statement.left)
        right = self.bind_visitor.visit(node.statement.right)
        return vast.Assign(left, right)
    
    #---------------------------------------------------------------------------
    def visit_Function(self, node):
        name = node.name
        retwidth = None if node.width is None else self.make_width(node.width)
        statement = ([ self.visit(v).first for v in node.io_variable.values() ] +
                     [ self.visit(v) for v in node.variable.values() ])
        statement.append(vast.Block(tuple([ self.function_visitor.visit(s) for s in node.statement])))
        return vast.Function(name, retwidth, statement)
    
    #---------------------------------------------------------------------------
    def visit_Instance(self, node):
        module = node.module.name
        parameterlist = [ vast.ParamArg(p, self.bind_visitor.visit(a)) for p, a in node.params.items() ] 
        portlist = [ vast.PortArg(p, self.bind_visitor.visit(a)) for p, a in node.ports.items() ]
        name = node.instname
        instance = vast.Instance(module, name, portlist, parameterlist)
        return vast.InstanceList(module, parameterlist, (instance,) )

    
#-------------------------------------------------------------------------------
class VerilogBindVisitor(VerilogCommonVisitor):
    pass

#-------------------------------------------------------------------------------
class VerilogAlwaysVisitor(VerilogCommonVisitor):
    def visit_Subst(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.NonblockingSubstitution(left, right)

#-------------------------------------------------------------------------------
class VerilogFunctionVisitor(VerilogCommonVisitor):
    def visit_Subst(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return vast.BlockingSubstitution(left, right)
