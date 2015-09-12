from __future__ import absolute_import
import os
import sys
import collections
import functools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import vtypes
import lib.parallel

def to_pipeline_node():
    pass

class Pipeline(vtypes.VeriloggenNode):
    """ Pipeline Generator """
    def __init__(self, m, name, width=32):
        self.m = m
        self.name = name
        self.width = 32
        self.tmp_count = 0
        self.par = lib.parallel.Parallel(self.m, self.name)
        self.data_visitor = DataVisitor(self)

    #---------------------------------------------------------------------------
    def add_reg(self, prefix, count, width=None, initval=0):
        tmp_name = '_'.join(['', self.name, prefix, str(count)])
        tmp = self.m.Reg(tmp_name, width, initval=initval)
        return tmp
        
    def add_wire(self, prefix, count, width=None):
        tmp_name = '_'.join(['', self.name, prefix, str(count)])
        tmp = self.m.Wire(tmp_name, width)
        return tmp
        
    #---------------------------------------------------------------------------
    def input(self, data, valid=None, ready=None, width=None):
        return _PipelineVariable(self, 0, data, valid, ready)
        
    def stage(self, data, width=None, initval=0):
        if width is None: width = self.width
        stage_id, raw_data, raw_valid, raw_ready = self.data_visitor.visit(data)
        tmp_data, tmp_valid, tmp_ready = self.make_tmp(raw_data, raw_valid, raw_ready,
                                                       width, initval)
        next_stage_id = stage_id + 1 if stage_id is not None else 0
        return _PipelineVariable(self, next_stage_id, tmp_data, tmp_valid, tmp_ready)

    def make_tmp(self, data, valid, ready, width=None, initval=0):
        tmp_data = self.add_reg('data', self.tmp_count, width=width, initval=initval)
        #tmp_valid = self.add_reg('valid', self.tmp_count, initval=0)
        #tmp_ready = self.add_wire('ready', self.tmp_count)
        tmp_valid = None
        tmp_ready = None
        self.tmp_count += 1
        self.par.add( tmp_data(data), cond=valid )
        #self.par.add( tmp_valid(valid) )
        #for r in ready:
        #    if r: self.m.Assign( r(tmp_ready) )
        return tmp_data, tmp_valid, tmp_ready
    
    def make_code(self):
        return self.par.make_code()
    
    def make_always(self, clk, rst):
        self.m.Always(vtypes.Posedge(clk))(
            vtypes.If(rst)(
                self.m.make_reset()
            )(
                self.make_code()
            ))
        
    def __call__(self, data, width=None, initval=0):
        return self.stage(data, width, initval)
    
#-------------------------------------------------------------------------------
class _PipelineNumeric(vtypes._Numeric): pass

class _PipelineVariable(_PipelineNumeric):
    def __init__(self, pipe, stage_id, data, valid=None, ready=None):
        self.pipe = pipe
        self.stage_id = stage_id
        self.data = data
        self.valid = valid
        self.ready = ready
        self.prev_dict = {}
        
    def prev(self, index, initval=0):
        if index in self.prev_dict:
            return self.prev_dict[index]

        width = self.data.bit_length()
        p = self
        
        for i in range(index):
            if (i+1) in self.prev_dict:
                p = self.prev_dict[i+1]
                continue
            
            tmp_data, tmp_valid, tmp_ready = self.pipe.make_tmp(p.data, p.valid, p.ready,
                                                                width, initval)
            p = _PipelineVariable(self, p.stage_id, tmp_data, tmp_valid, tmp_ready)
            self.prev_dict[i+1] = p
            
        return p
        
    def output(self, data, valid=None, ready=None):
        if isinstance(data, vtypes.Reg):
            self.pipe.par.add( data(self.data) )
        else:
            self.pipe.m.Assign( data(self.data) )

        my_valid = vtypes.Int(1) if self.valid is None else self.valid 
        if valid is None:
            pass
        elif isinstance(valid, vtypes.Reg):
            self.pipe.par.add( valid(my_valid) )
        else:
            self.pipe.m.Assign( valid(my_valid) )

        if ready is None:
            ready = vtypes.Int(1)
            
        if self.ready is not None:
            self.pipe.m.Assign( self.ready(read) )

    def bit_length(self):
        return self.data.bit_length()
            
#-------------------------------------------------------------------------------
class _PipelineVisitor(object):
    def generic_visit(self, node):
        raise TypeError("Type %s is not supported." % str(type(node)))
    
    def visit(self, node):
        if isinstance(node, vtypes._BinaryOperator):
            return self.visit__BinaryOperator(node)

        if isinstance(node, vtypes._UnaryOperator):
            return self.visit__UnaryOperator(node)

        if isinstance(node, vtypes._Variable):
            return self.visit__Variable(node)

        if isinstance(node, vtypes._Constant):
            return self.visit__Constant(node)

        visitor = getattr(self, 'visit_' + node.__class__.__name__, self.generic_visit)
        return visitor(node)
    
    def visit__PipelineVariable(self, node):
        raise NotImplementedError('visit__PipelineVariable() must be implemented')
        
    def visit__BinaryOperator(self, node):
        raise NotImplementedError('visit__BinaryOperator() must be implemented')
        
    def visit__UnaryOperator(self, node):
        raise NotImplementedError('visit__UnaryOperator() must be implemented')        

    def visit__Variable(self, node):
        raise NotImplementedError('visit__Variable() must be implemented')        
    
    def visit__Constant(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_bool(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')
    
    def visit_int(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_str(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')

    def visit_float(self, node):
        raise NotImplementedError('visit__Constant() must be implemented')
    
#-------------------------------------------------------------------------------
class DataVisitor(_PipelineVisitor):
    def __init__(self, pipe):
        self.pipe = pipe

    def visit__PipelineVariable(self, node):
        ready = [] if node.ready is None else node.ready
        return (node.stage_id, node.data, node.valid, ready )

    def visit__Variable(self, node):
        return (None, node, None, [])
    
    def visit__Constant(self, node):
        return (None, node, None, [])
    
    def visit__BinaryOperator(self, node):
        rstage, rdata, rvalid, rready = self.visit(node.right)
        lstage, ldata, lvalid, lready = self.visit(node.left)
        
        cls = type(node)
        data = cls(ldata, rdata)
        
        valid = None
        if rvalid is not None and lvalid is not None:
            valid = vtypes.And(lvalid, rvalid)
        elif rvalid is None and lvalid is None:
            valid = None
        elif rvalid is None:
            valid = lvalid
        elif lvalid is None:
            valid = rvalid
            
        ready = lready + rready
        
        if rstage is None and lstage is None:
            return (None, data, valid, ready)
        if rstage is None:
            return (lstage, data, valid, ready)
        if lstage is None:
            return (rstage, data, valid, ready)
        
        if lstage > rstage:
            diff = lstage - rstage
            p = node.right
            for i in range(diff):
                width = rdata.bit_length()
                p = self.pipe.stage(p, width=width)
            data = cls(ldata, p.data)
            valid = None ##
            ready = [] ##
            return (max(lstage, rstage), data, valid, ready)

        if lstage < rstage:
            diff = rstage - lstage
            p = node.left
            for i in range(diff):
                width = ldata.bit_length()
                p = self.pipe.stage(p, width=width)
            data = cls(p.data, rdata)
            valid = None ##
            ready = [] ##
            return (max(lstage, rstage), data, valid, ready)

        return (max(lstage, rstage), data, valid, ready)
        
    def visit__UnaryOperator(self, node):
        return self.visit(node.right)
        
    def visit_bool(self, node):
        if node: return (None, vtypes.Int(1), None, [])
        return (None, vtypes.Int(0), None, [])
    
    def visit_int(self, node):
        return (None, vtypes.Int(node), None, [])

    def visit_str(self, node):
        return (None, vtypes.Str(node), None, [])

    def visit_float(self, node):
        return (None, vtypes.Float(node), None, [])
