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
        self.vars = []

    #---------------------------------------------------------------------------
    def input(self, data, valid=None, ready=None, width=None):
        ret = _PipelineVariable(self, 0, data, valid, ready)
        self.vars.append(ret)
        return ret
        
    #---------------------------------------------------------------------------
    def stage(self, data, width=None, initval=0):
        if width is None: width = self.width
        stage_id, raw_data, raw_valid, raw_ready = self.data_visitor.visit(data)
        tmp_data, tmp_valid, tmp_ready = self.make_tmp(raw_data, raw_valid, raw_ready,
                                                       width, initval)
        next_stage_id = stage_id + 1 if stage_id is not None else None
        ret = _PipelineVariable(self, next_stage_id, tmp_data, tmp_valid, tmp_ready)
        self.vars.append(ret)
        return ret

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
    def make_tmp(self, data, valid, ready, width=None, initval=0):
        tmp_data = self.add_reg('data', self.tmp_count, width=width, initval=initval)
        
        if valid is not None:
            tmp_valid = self.add_reg('valid', self.tmp_count, initval=0)
        else:
            tmp_valid = None

        if ready:
            tmp_ready = self.add_wire('ready', self.tmp_count)
        else:
            tmp_ready = None
            
        self.tmp_count += 1

        # data
        data_valid_vars = []
        if valid is not None:
            data_valid_vars.append(valid)
        if tmp_ready is not None:
            data_valid_vars.append(tmp_ready)

        if len(data_valid_vars) == 0:
            data_cond = None
        elif len(data_valid_vars) == 1:
            data_cond = data_valid_vars[0]
        else:
            data_cond = vtypes.AndList(*data_valid_vars)

        self.par.add( tmp_data(data), cond=data_cond )
            
        # valid
        valid_valid_vars = []
        if tmp_ready is not None:
            valid_valid_vars.append( tmp_ready )

        if len(valid_valid_vars) == 0:
            valid_cond = None
        elif len(valid_valid_vars) == 1:
            valid_cond = valid_valid_vars[0]
        else:
            valid_cond = vtypes.AndList(*valid_valid_vars)

        if tmp_valid is not None:
            self.par.add( tmp_valid(valid), cond=tmp_ready )

        # ready
        if tmp_ready is not None:
            for r in ready:
                if r: self.m.Assign( r(tmp_ready) )
        
        return tmp_data, tmp_valid, tmp_ready
    
    #---------------------------------------------------------------------------
    def make_prev(self, data, valid, ready, root_valid=None, width=None, initval=0):
        tmp_data = self.add_reg('data', self.tmp_count, width=width, initval=initval)
        
        if valid is not None:
            tmp_valid = self.add_reg('valid', self.tmp_count, initval=0)
        else:
            tmp_valid = None
            
        if ready is not None:
            tmp_ready = self.add_wire('ready', self.tmp_count)
        else:
            tmp_ready = None

        if valid or ready:
            next_valid = self.add_wire('nvalid', self.tmp_count)
        else:
            next_valid = None
            
        self.tmp_count += 1

        # data
        data_valid_vars = []
        if valid is not None:
            data_valid_vars.append(valid)
        if tmp_ready is not None:
            data_valid_vars.append(tmp_ready)

        if len(data_valid_vars) == 0:
            data_cond = None
        elif len(data_valid_vars) == 1:
            data_cond = data_valid_vars[0]
        else:
            data_cond = vtypes.AndList(*data_valid_vars)
        
        self.par.add( tmp_data(data), cond=data_cond )

        # valid
        valid_valid_vars = []
        if valid is not None:
            valid_valid_vars.append(valid)
        if tmp_ready is not None:
            valid_valid_vars.append(tmp_ready)

        if len(valid_valid_vars) == 0:
            valid_cond = None
        elif len(valid_valid_vars) == 1:
            valid_cond = valid_valid_vars[0]
        else:
            valid_cond = vtypes.AndList(*valid_valid_vars)
        
        if tmp_valid is not None:
            self.par.add( tmp_valid(valid), cond=valid_cond )

        next_valid_valid_vars = []
        if root_valid is not None:
            next_valid_valid_vars.append(root_valid)
        if tmp_valid is not None:
            next_valid_valid_vars.append(tmp_valid)
        if tmp_ready is not None:
            next_valid_valid_vars.append(tmp_ready)
            
        if len(next_valid_valid_vars) == 0:
            next_valid_cond = None
        elif len(next_valid_valid_vars) == 1:
            next_valid_cond = next_valid_valid_vars[0]
        else:
            next_valid_cond = vtypes.AndList(*next_valid_valid_vars)
        
        if next_valid is not None:
            self.m.Assign( next_valid(next_valid_cond) )
            
        # ready
        if ready is not None:
            self.m.Assign( ready(tmp_ready) )
        
        return tmp_data, next_valid, tmp_ready
    
    #---------------------------------------------------------------------------
    def make_reset(self):
        return self.par.make_reset()
    
    #---------------------------------------------------------------------------
    def make_code(self):
        return self.par.make_code()
    
    #---------------------------------------------------------------------------
    def make_always(self, clk, rst, reset=(), body=()):
        self.m.Always(vtypes.Posedge(clk))(
            vtypes.If(rst)(
                reset,
                self.make_reset()
            )(
                body,
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
        if index == 0:
            return self
        if index < 0:
            raise ValueError('Index to a previous value must be positive.')
        
        if index in self.prev_dict:
            return self.prev_dict[index]

        width = self.data.bit_length()
        p = self
        
        for i in range(index):
            if (i+1) in self.prev_dict:
                p = self.prev_dict[i+1]
                continue
            
            tmp_data, tmp_valid, tmp_ready = self.pipe.make_prev(p.data, p.valid, p.ready,
                                                                 self.valid, width, initval)
            p = _PipelineVariable(self, p.stage_id, tmp_data, tmp_valid, tmp_ready)
            self.pipe.vars.append(p)
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

        if not ready:
            ready = vtypes.Int(1)

        if self.ready is not None:
            self.pipe.m.Assign( self.ready(ready) )

    def reset(self, cond, initval=0):
        self.pipe.par.add( self.data(initval), cond=cond )
        if self.valid is not None:
            self.pipe.par.add( self.valid(0), cond=cond )
            
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

    def make_valid(self, lvalid, rvalid):
        if rvalid is not None and lvalid is not None:
            return vtypes.AndList(lvalid, rvalid)
        elif rvalid is None and lvalid is None:
            return None
        elif rvalid is None:
            return lvalid
        elif lvalid is None:
            return rvalid
        return None

    def make_ready(self, lready, rready):
        return lready + rready
    
    def visit__PipelineVariable(self, node):
        ready = [] if node.ready is None else [ node.ready ]
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
        
        valid = self.make_valid(lvalid, rvalid)
        ready = self.make_ready(lready, rready)
        
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
            valid = self.make_valid(lvalid, p.valid)
            rready = [] if p.ready is None else [ p.ready ]
            ready = self.make_ready(lready, rready)
            return (max(lstage, rstage), data, valid, ready)

        if lstage < rstage:
            diff = rstage - lstage
            p = node.left
            for i in range(diff):
                width = ldata.bit_length()
                p = self.pipe.stage(p, width=width)
            data = cls(p.data, rdata)
            valid = self.make_valid(p.valid, rvalid)
            lready = [] if p.ready is None else [ p.ready ]
            ready = self.make_ready(lready, rready)
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
