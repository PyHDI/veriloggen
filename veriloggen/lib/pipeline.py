from __future__ import absolute_import
from __future__ import print_function
import os
import sys
from functools import reduce

import veriloggen.vtypes as vtypes
from veriloggen.lib.seq import Seq

class Pipeline(vtypes.VeriloggenNode):
    """ Pipeline Generator """
    def __init__(self, m, name, clk, rst, width=32):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = 32
        self.tmp_count = 0
        self.seq = Seq(self.m, self.name, clk, rst)
        self.data_visitor = DataVisitor(self)
        self.vars = []

    #---------------------------------------------------------------------------
    def input(self, data, valid=None, ready=None, width=None):
        if ready is not None and not isinstance(ready, (vtypes.Wire, vtypes.Output)):
            raise TypeError('ready port of PipelineVariable must be Wire., not %s' %
                            str(type(ready)))
        ret = _PipelineVariable(self, 0, data, valid, ready)
        self.vars.append(ret)
        return ret
        
    #---------------------------------------------------------------------------
    # self.__call__() calls this method
    def stage(self, data, initval=0, width=None):
        if width is None: width = self.width
        stage_id, raw_data, raw_valid, raw_ready = self.data_visitor.visit(data)
        tmp_data, tmp_valid, tmp_ready = self._make_tmp(raw_data, raw_valid, raw_ready,
                                                       width, initval)
        next_stage_id = stage_id + 1 if stage_id is not None else None
        ret = _PipelineVariable(self, next_stage_id, tmp_data, tmp_valid, tmp_ready)
        self.vars.append(ret)
        return ret

    #---------------------------------------------------------------------------
    # Accumulator 
    def acc_and(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.And], data, width, initval, resetcond)

    def acc_nand(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.And, vtypes.Unot], data, width, initval, resetcond)

    def acc_or(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Or], data, width, initval, resetcond)

    def acc_xor(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Xor], data, width, initval, resetcond)

    def acc_xnor(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Xor, vtypes.Unot], data, width, initval, resetcond)

    def acc_nor(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Or, vtypes.Unot], data, width, initval, resetcond)

    def acc_add(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Plus], data, width, initval, resetcond)

    def acc_sub(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Minus], data, width, initval, resetcond)

    def acc_mul(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Times], data, width, initval, resetcond)

    def acc_div(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Divide], data, width, initval, resetcond)

    def acc_mod(self, data, initval=0, resetcond=None, width=None):
        return self._accumulate([vtypes.Mod], data, width, initval, resetcond)
    
    #---------------------------------------------------------------------------
    def make_always(self, reset=(), body=()):
        self.m.Always(vtypes.Posedge(self.clk))(
            vtypes.If(self.rst)(
                reset,
                self.make_reset()
            )(
                body,
                self.make_code()
            ))
        
    #---------------------------------------------------------------------------
    def make_reset(self):
        return self.seq.make_reset()
    
    #---------------------------------------------------------------------------
    def make_code(self):
        return self.seq.make_code()
    
    #---------------------------------------------------------------------------
    def _accumulate(self, ops, data, width=None, initval=0, resetcond=None):
        if width is None: width = self.width
        stage_id, raw_data, raw_valid, raw_ready = self.data_visitor.visit(data)
        tmp_data, tmp_valid, tmp_ready = self._make_tmp(raw_data, raw_valid, raw_ready,
                                                       width, initval, acc_ops=ops)
        next_stage_id = stage_id + 1 if stage_id is not None else None
        ret = _PipelineVariable(self, next_stage_id, tmp_data, tmp_valid, tmp_ready)
        if resetcond is not None:
            ret.reset(resetcond, initval)
        self.vars.append(ret)
        return ret
    
    #---------------------------------------------------------------------------
    def _add_reg(self, prefix, count, width=None, initval=0):
        tmp_name = '_'.join(['', self.name, prefix, str(count)])
        tmp = self.m.Reg(tmp_name, width, initval=initval)
        return tmp
        
    def _add_wire(self, prefix, count, width=None):
        tmp_name = '_'.join(['', self.name, prefix, str(count)])
        tmp = self.m.Wire(tmp_name, width)
        return tmp
        
    #---------------------------------------------------------------------------
    def _make_tmp(self, data, valid, ready, width=None, initval=0, acc_ops=()):
        tmp_data = self._add_reg('data', self.tmp_count, width=width, initval=initval)
        
        if valid is not None:
            tmp_valid = self._add_reg('valid', self.tmp_count, initval=0)
        else:
            tmp_valid = None

        if ready:
            tmp_ready = self._add_wire('ready', self.tmp_count)
        else:
            tmp_ready = None

        self.tmp_count += 1

        # data
        data_cond_vars = []
        if valid is not None:
            data_cond_vars.append(valid)
        if tmp_ready is not None:
            if tmp_valid is not None:
                data_cond_vars.append(vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid)))
            else:
                data_cond_vars.append(tmp_ready)

        if len(data_cond_vars) == 0:
            data_cond = None
        elif len(data_cond_vars) == 1:
            data_cond = data_cond_vars[0]
        else:
            data_cond = vtypes.AndList(*data_cond_vars)

        # Accumulator
        for op in acc_ops:
            if issubclass(op, vtypes._BinaryOperator):
                data = op(tmp_data, data)
            elif issubclass(op, vtypes._UnaryOperator):
                data = op(data)
            
        self.seq.add( tmp_data(data), cond=data_cond )
            
        # valid
        valid_cond_vars = []
        if tmp_ready is not None:
            ordy = vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid))
            valid_cond_vars.append(ordy)

        if len(valid_cond_vars) == 0:
            valid_cond = None
        elif len(valid_cond_vars) == 1:
            valid_cond = valid_cond_vars[0]
        else:
            valid_cond = vtypes.AndList(*valid_cond_vars)

        if tmp_valid is not None:
            self.seq.add( tmp_valid(valid), cond=valid_cond )

        # ready
        if tmp_ready is not None:
            ordy = vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid))
            for r in ready:
                if not r: continue
                if len(r.subst) == 0:
                    self.m.Assign( r(ordy) )
                elif isinstance(r.subst[0].right, vtypes.Int) and (r.subst[0].right.value==1):
                    r.subst[0].overwrite_right( ordy )
                else:
                    r.subst[0].overwrite_right( vtypes.AndList(r.subst[0].right, ordy ) )
        
        return tmp_data, tmp_valid, tmp_ready
    
    #---------------------------------------------------------------------------
    def _make_prev(self, data, valid, ready, root_valid=None, width=None, initval=0):
        tmp_data = self._add_reg('data', self.tmp_count, width=width, initval=initval)
        
        if valid is not None:
            tmp_valid = self._add_reg('valid', self.tmp_count, initval=0)
        else:
            tmp_valid = None
            
        if ready is not None:
            tmp_ready = self._add_wire('ready', self.tmp_count)
        else:
            tmp_ready = None

        if valid or ready:
            next_valid = self._add_wire('nvalid', self.tmp_count)
        else:
            next_valid = None
            
        self.tmp_count += 1

        # data
        data_cond_vars = []
        if valid is not None:
            data_cond_vars.append(valid)
        if tmp_ready is not None:
            if tmp_valid is not None:
                data_cond_vars.append(vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid)))
            else:
                data_cond_vars.append(tmp_ready)

        if len(data_cond_vars) == 0:
            data_cond = None
        elif len(data_cond_vars) == 1:
            data_cond = data_cond_vars[0]
        else:
            data_cond = vtypes.AndList(*data_cond_vars)
        
        self.seq.add( tmp_data(data), cond=data_cond )

        # valid
        valid_cond_vars = []
        if valid is not None:
            valid_cond_vars.append(valid)
        if tmp_ready is not None:
            ordy = vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid))
            valid_cond_vars.append(ordy)

        if len(valid_cond_vars) == 0:
            valid_cond = None
        elif len(valid_cond_vars) == 1:
            valid_cond = valid_cond_vars[0]
        else:
            valid_cond = vtypes.AndList(*valid_cond_vars)
        
        if tmp_valid is not None:
            self.seq.add( tmp_valid(valid), cond=valid_cond )

        # next_valid
        next_valid_cond_vars = []
        if root_valid is not None:
            next_valid_cond_vars.append(root_valid)
        if tmp_valid is not None:
            next_valid_cond_vars.append(tmp_valid)
        if tmp_ready is not None:
            next_valid_cond_vars.append(tmp_ready)
            
        if len(next_valid_cond_vars) == 0:
            next_valid_cond = None
        elif len(next_valid_cond_vars) == 1:
            next_valid_cond = next_valid_cond_vars[0]
        else:
            next_valid_cond = vtypes.AndList(*next_valid_cond_vars)
        
        if next_valid is not None:
            self.m.Assign( next_valid(next_valid_cond) )
            
        # ready
        if tmp_ready is not None:
            ordy = vtypes.OrList(tmp_ready, vtypes.Not(tmp_valid))
            if len(ready.subst) == 0:
                self.m.Assign( ready(ordy) )
            elif isinstance(ready.subst[0].right, vtypes.Int) and (ready.subst[0].right.value == 1):
                ready.subst[0].overwrite_right( ordy )
            else:
                ready.subst[0].overwrite_right( vtypes.AndList(ready.subst[0].right, ordy ) )
        
        return tmp_data, next_valid, tmp_ready
    
    #---------------------------------------------------------------------------
    def __call__(self, data, initval=0, width=None):
        return self.stage(data, initval=initval, width=width)
    
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
        if self.ready is not None:
            ready = vtypes.Int(1)
            self.pipe.m.Assign( self.ready(ready) )

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
            
            tmp_data, tmp_valid, tmp_ready = self.pipe._make_prev(p.data, p.valid, p.ready,
                                                                 self.valid, width, initval)
            p = _PipelineVariable(self.pipe, p.stage_id, tmp_data, tmp_valid, tmp_ready)
            self.pipe.vars.append(p)
            self.prev_dict[i+1] = p
            
        return p
        
    def output(self, data, valid=None, ready=None, nobuf=False):
        # Inserting output stage register
        if nobuf:
            ovar = self
        else:
            ovar = self.pipe.stage(self)
        
        if not isinstance(data, (vtypes.Wire, vtypes.Output)):
            raise TypeError('Data signal must be Wire, not %s' % str(type(data)))
        else:
            ovar.pipe.m.Assign( data(ovar.data) )

        my_valid = vtypes.Int(1) if ovar.valid is None else ovar.valid 
        if valid is None:
            pass
        elif not isinstance(valid, (vtypes.Wire, vtypes.Output)):
            raise TypeError('Valid signal must be Wire, not %s' % str(type(valid)))
        else:
            ovar.pipe.m.Assign( valid(my_valid) )

        if not ready:
            ready = vtypes.Int(1)

        if ovar.ready is not None:
            prev_subst = ovar.ready.get_subst()
            if len(prev_subst) == 0:
                ovar.pipe.m.Assign( ovar.ready(ready) )
            elif isinstance(prev_subst[0].right, vtypes.Int) and (prev_subst[0].right.value==1):
                ovar.ready.subst[0].overwrite_right( ready )
            else:
                ovar.ready.subst[0].overwrite_right( vtypes.AndList(prev_subst[0].right, ready) )

    def reset(self, cond, initval=0):
        self.pipe.seq.add( self.data(initval), cond=cond )
        if self.valid is not None:
            self.pipe.seq.add( self.valid(0), cond=cond )
            
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

    def visit_Pointer(self, node):
        raise NotImplementedError('visit_Pointer() must be implemented')
    
    def visit_Slice(self, node):
        raise NotImplementedError('visit_Slice() must be implemented')
    
    def visit_Cat(self, node):
        raise NotImplementedError('visit_Cat() must be implemented')
    
    def visit_Repeat(self, node):
        raise NotImplementedError('visit_Repeat() must be implemented')
    
    def visit_Cond(self, node):
        raise NotImplementedError('visit_Cond() must be implemented')
    
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

    def pack_valid(self, lvalid, rvalid):
        if rvalid is not None and lvalid is not None:
            return vtypes.AndList(lvalid, rvalid)
        elif rvalid is None and lvalid is None:
            return None
        elif rvalid is None:
            return lvalid
        elif lvalid is None:
            return rvalid
        return None

    def pack_ready(self, lready, rready):
        return lready + rready

    def pack(self, *args):
        rslts = [ self.visit(arg) for arg in args ]
        all_stage_none = reduce(lambda t,x:t and x is None, [ rslt[0] for rslt in rslts ], True)

        if all_stage_none:
            data = [ rslt[1] for rslt in rslts ]
            valid = reduce(self.pack_valid, [ rslt[2] for rslt in rslts ], None)
            ready = reduce(self.pack_ready, [ rslt[3] for rslt in rslts ], [])
            return (None, data, valid, ready)

        max_stage = reduce(lambda x,y:
                           None if x is None and y is None else
                           x if x is not None and y is None else
                           y if y is not None and x is None else
                           max(x, y), [ rslt[0] for rslt in rslts ], None)
        
        new_args = []
        for rslt, arg in zip(rslts, args):
            stage = rslt[0]
            if stage is None:
                new_args.append(arg)
                continue
            if stage == max_stage:
                new_args.append(arg)
                continue
            
            diff = max_stage - stage
            p = arg
            for i in range(diff):
                width = rslt[1].bit_length()
                p = self.pipe.stage(p, width=width)

            new_args.append(p)

        new_rslts = [ self.visit(arg) for arg in new_args ]
        data = [ rslt[1] for rslt in new_rslts ]
        valid = reduce(self.pack_valid, [ rslt[2] for rslt in new_rslts ], None)
        ready = reduce(self.pack_ready, [ rslt[3] for rslt in new_rslts ], [])

        return (max_stage, data, valid, ready)
        
    def make_valid(self, valid, ready):
        if ready is not None and valid is not None:
            next_valid = vtypes.AndList(valid, ready)
        elif ready is not None:
            next_valid = ready
        elif valid is not None:
            next_valid = valid
        else:
            next_valid = None
        return next_valid
    
    def visit__PipelineVariable(self, node):
        ready = [] if node.ready is None else [ node.ready ]
        valid = self.make_valid(node.valid, node.ready)
        return (node.stage_id, node.data, valid, ready )

    def visit__Variable(self, node):
        return (None, node, None, [])
    
    def visit__Constant(self, node):
        return (None, node, None, [])

    def visit__BinaryOperator(self, node):
        stage, data, valid, ready = self.pack(node.left, node.right)
        cls = type(node)
        return stage, cls(*data), valid, ready
    
    def visit__UnaryOperator(self, node):
        return self.visit(node.right)
        
    def visit_Pointer(self, node):
        stage, data, valid, ready = self.pack(node.var, node.pos)
        cls = type(node)
        return stage, cls(*data), valid, ready
    
    def visit_Slice(self, node):
        stage, data, valid, ready = self.pack(node.var, node.msb, node.lsb)
        cls = type(node)
        return stage, cls(*data), valid, ready
    
    def visit_Cat(self, node):
        stage, data, valid, ready = self.pack(*node.vars)
        cls = type(node)
        return stage, cls(*data), valid, ready
    
    def visit_Repeat(self, node):
        stage, data, valid, ready = self.pack(node.var, node.times)
        cls = type(node)
        return stage, cls(*data), valid, ready
    
    def visit_Cond(self, node):
        stage, data, valid, ready = self.pack(node.condition, node.true_value, node.false_value)
        cls = type(node)
        return stage, cls(*data), valid, ready
    
    def visit_bool(self, node):
        if node: return (None, vtypes.Int(1), None, [])
        return (None, vtypes.Int(0), None, [])
    
    def visit_int(self, node):
        return (None, vtypes.Int(node), None, [])

    def visit_str(self, node):
        return (None, vtypes.Str(node), None, [])

    def visit_float(self, node):
        return (None, vtypes.Float(node), None, [])
