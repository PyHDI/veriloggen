import sys
import os
import collections

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import module
import vtypes

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
    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))
    
    def visit(self, node):
        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)

    def visit_Source(self, node):
        pass

    def visit_Description(self, node):
        pass

    def visit_ModuleDef(self, node):
        pass
    
#-------------------------------------------------------------------------------
def read_verilog(*filelist, **opt):
    include = opt['include'] if 'include' in opt else ()
    define = opt['define'] if 'define' in opt else ()
    if not isinstance(include, tuple) and not isinstance(include, list):
        raise TypeError('"include" option of read_verilog should be tuple or list, not %s' %
                        type(include))
    if not isinstance(include, tuple) and not isinstance(include, list):
        raise TypeError('"include" option of read_verilog should be tuple or list, not %s' %
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
