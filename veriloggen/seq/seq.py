from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.subst_visitor import SubstDstVisitor
from veriloggen.seq.reset_visitor import ResetVisitor

_tmp_count = 0
def _tmp_name(prefix='_tmp_seq'):
    global _tmp_count
    v = _tmp_count
    _tmp_count += 1
    ret = '_'.join([prefix, str(v)])
    return ret

def TmpSeq(m, clk, rst=None):
    name = _tmp_name()
    return Seq(m, name, clk, rst)

class Seq(vtypes.VeriloggenNode):
    """ Sequential Logic Manager """
    def __init__(self, m, name, clk, rst=None):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst

        self.tmp_count = 0
        self.delay_amount = 0
        self.delayed_body = collections.defaultdict(list)
        self.prev_dict = collections.OrderedDict()
        self.body = []
        
        self.dst_var = collections.OrderedDict()
        self.dst_visitor = SubstDstVisitor()
        self.reset_visitor = ResetVisitor()
        
        self.done = False

        self.next_kwargs = {}
        self.last_statement = None
        self.last_cond = []
        self.next_call = None
        
    #---------------------------------------------------------------------------
    def prev(self, var, delay, initval=0):
        if isinstance(var, (bool, int, float, str,
                            vtypes._Constant, vtypes._ParameterVairable)):
            return var
        if not isinstance(var, vtypes._Variable):
            raise TypeError('var must be vtypes._Variable, not %s' % str(type(var)))
        if not isinstance(delay, int):
            raise TypeError('delay must be int, not %s' % str(type(delay)))
        if delay <= 0:
            return var
        
        name_prefix = '_' + var.name
        key = '_'.join([name_prefix, str(delay)])
        if key in self.prev_dict:
            return self.prev_dict[key]
        
        width = var.bit_length()
        p = var
        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i+1)])
            if tmp_name in self.prev_dict:
                p = self.prev_dict[tmp_name]
                continue
            tmp = self.m.Reg(tmp_name, width, initval=initval)
            self.prev_dict[tmp_name] = tmp;
            self.add(tmp(p))
            p = tmp
            
        return p
    
    #---------------------------------------------------------------------------
    def add(self, *statement, **kwargs):
        # for Elif statement
        if self.next_call is not None:
            self.next_call(*statement)
            self._add_dst_var(statement)
            self._clear_next_call()
            return self
        
        # merge the predefined keywords and flush them
        kwargs.update(self.next_kwargs)
        self._clear_next_kwargs()
        self._clear_last_statement()
        
        for k in kwargs.keys():
            if k not in ('keep', 'delay', 'cond', 'lazy_cond', 'eager_val'):
                raise NameError('Keyword argument %s is not supported.' % k)
            
        keep = kwargs['keep'] if 'keep' in kwargs else None
        delay = kwargs['delay'] if 'delay' in kwargs else None
        cond = kwargs['cond'] if 'cond' in kwargs else None
        lazy_cond = kwargs['lazy_cond'] if 'lazy_cond' in kwargs else False
        eager_val = kwargs['eager_val'] if 'eager_val' in kwargs else False
        
        if keep is not None:
            del kwargs['keep']
            for i in range(keep):
                kwargs['delay'] = i if delay is None else delay + i
                self.add(*statement, **kwargs)
            return self
        
        if delay is not None and delay > 0:
            if eager_val:
                statement = [ self._add_delayed_subst(s, delay) for s in statement ]
                
            if cond is not None:
                if not lazy_cond:
                    cond = self._add_delayed_cond(cond, delay)
                statement = [ vtypes.If(cond)(*statement) ]
                self.last_statement = statement[0]
                
            self.delayed_body[delay].extend(statement)
            self._add_dst_var(statement)
            
            return self
            
        if cond is not None:
            statement = [ vtypes.If(cond)(*statement) ]
            self.last_statement = statement[0]
            
        self.body.extend(statement)
        self._add_dst_var(statement)
        
        return self

    #---------------------------------------------------------------------------
    def Cond(self, cond):
        if 'cond' not in self.next_kwargs:
            self.next_kwargs['cond'] = cond
        else:
            self.next_kwargs['cond'] = vtyeps.Ands(self.next_kwargs['cond'], cond)
            
        self.last_cond = [ self.next_kwargs['cond'] ]
        
        return self

    def If(self, cond):
        return self.Cond(cond)

    def Else(self, *statement, **kwargs):
        if not isinstance(self.last_statement, vtypes.If):
            raise ValueError("Last statement is not If")
        self.last_statement.Else(*statement)
        self._add_dst_var(statement)
        
        old = self.last_cond.pop()
        self.last_cond.append(vtypes.Not(old))
        
        return self

    def Elif(self, cond):
        if not isinstance(self.last_statement, vtypes.If):
            raise ValueError("Last statement is not If")
        self.next_call = self.last_statement.Elif(cond)
        
        old = self.last_cond.pop()
        self.last_cond.append(vtypes.Not(old))
        self.last_cond.append(cond)
        
        return self
        
    @property
    def then(self):
        cond = self._make_cond(self.last_cond)
        self.Cond(cond)
        self._clear_last_cond()
        return self
        
    def Delay(self, delay):
        return self._add_next_kwarg('delay', delay)
        
    def Keep(self, keep):
        return self._add_next_kwarg('keep', keep)
        
    #---------------------------------------------------------------------------
    def _add_next_kwarg(self, name, value):
        if name not in self.next_kwargs:
            self.next_kwargs[name] = value
        else:
            raise ValueError("'%s' is already defined." % name)
        return self
    
    def _clear_next_kwargs(self):
        self.next_kwargs = {}

    def _clear_last_statement(self):
        self.last_statement = None
        
    def _clear_last_cond(self):
        self.last_cond = []

    def _clear_next_call(self):
        self.next_call = None

    def _make_cond(self, condlist):
        ret = None
        for cond in condlist:
            if ret is None:
                ret = cond
            else:
                ret = vtypes.Ands(ret, cond)
        return ret

    #---------------------------------------------------------------------------
    def make_always(self, reset=(), body=()):
        if self.done:
            raise ValueError('make_always() has been already called.')
        self.done = True
        
        part_reset = list(reset) + list(self.make_reset())
        part_body = list(body) + list(self.make_code())

        if not part_reset and not part_body:
            pass
        elif not part_reset or self.rst is None:
            self.m.Always(vtypes.Posedge(self.clk))(
                part_body,
            )
        else:
            self.m.Always(vtypes.Posedge(self.clk))(
                vtypes.If(self.rst)(
                    part_reset,
                )(
                    part_body,
                ))
    
    #---------------------------------------------------------------------------
    def make_code(self):
        ret = []
        
        for delay, body in sorted(self.delayed_body.items(), key=lambda x:x[0],
                                  reverse=True):
            ret.extend(body)
            
        ret.extend(self.body)
        return ret
    
    #---------------------------------------------------------------------------
    def make_reset(self):
        ret = []
        for dst in self.dst_var.values():
            v = self.reset_visitor.visit(dst)
            if v is not None:
                ret.append(v)
        return ret
        
    #---------------------------------------------------------------------------
    def _add_dst_var(self, statement):
        for s in statement:
            values = self.dst_visitor.visit(s)
            for v in values:
                k = str(v)
                if k not in self.dst_var:
                    self.dst_var[k] = v
                
    #---------------------------------------------------------------------------
    def _add_delayed_cond(self, statement, delay):
        name_prefix = '_'.join(['', self.name, 'cond', str(self.tmp_count)])
        self.tmp_count += 1
        prev = statement
        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i+1)])
            tmp = self.m.Reg(tmp_name, initval=0)
            self.add(tmp(prev), delay=i)
            prev = tmp
        return prev
    
    #---------------------------------------------------------------------------
    def _add_delayed_subst(self, subst, delay):
        if not isinstance(subst, vtypes.Subst):
            return subst
        left = subst.left
        right = subst.right
        if isinstance(right, (bool, int, float, str,
                              vtypes._Constant, vtypes._ParameterVairable)):
            return subst
        width = left.bit_length()
        prev = right

        name_prefix = ('_'.join(['', left.name, str(self.tmp_count)]) 
                       if isinstance(left, vtypes._Variable) else
                       '_'.join(['', self.name, 'sbst', str(self.tmp_count)]))
        self.tmp_count += 1
            
        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i+1)])
            tmp = self.m.Reg(tmp_name, width, initval=0)
            self.add(tmp(prev), delay=i)
            prev = tmp
        return left(prev)
    
    #---------------------------------------------------------------------------
    def __call__(self, *statement, **kwargs):
        return self.add(*statement, **kwargs)

