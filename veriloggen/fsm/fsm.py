from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import collections
import functools

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.subst_visitor import SubstDstVisitor
from veriloggen.seq.reset_visitor import ResetVisitor
from veriloggen.seq.seq import Seq

_tmp_count = 0
def _tmp_name(prefix='_tmp_fsm'):
    global _tmp_count
    v = _tmp_count
    _tmp_count += 1
    ret = '_'.join([prefix, str(v)])
    return ret

def TmpFSM(m, clk, rst, width=32, initname='init'):
    name = _tmp_name()
    return FSM(m, name, clk, rst, width, initname)

class FSM(vtypes.VeriloggenNode):
    """ Finite State Machine Generator """
    def __init__(self, m, name, clk, rst, width=32, initname='init'):
        self.m = m
        self.name = name
        self.clk = clk
        self.rst = rst
        self.width = width
        self.state_count = 0
        self.state = self.m.Reg(name, width)  # set initval later

        self.mark = {} # key:index
        self._set_mark(0, self.name + '_' + initname)
        self.state.initval = self._get_mark(0)
        
        self.body = collections.defaultdict(list)
        self.jump = collections.defaultdict(list)
        
        self.delay_amount = 0
        self.delayed_state = {} # key:delay
        self.delayed_body = collections.defaultdict(
            functools.partial(collections.defaultdict, list)) # key:delay
        self.tmp_count = 0
        
        self.dst_var = collections.OrderedDict()
        self.dst_visitor = SubstDstVisitor()
        self.reset_visitor = ResetVisitor()

        self.seq = Seq(self.m, self.name + '_par', clk, rst)
        
        self.done = False

        self.next_kwargs = {}
        self.last_statement = None
        self.last_cond = []
        self.next_call = None
        
    #---------------------------------------------------------------------------
    def current(self):
        return self.state_count
        
    def next(self):
        return self.current() + 1
        
    def inc(self):
        self._set_index(None)
    
    #---------------------------------------------------------------------------
    def goto(self, dst, cond=None, else_dst=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']
        self._clear_next_kwargs()
        self._clear_last_statement()
        self._clear_last_cond()
        
        src = self.current()
        return self._go(src, dst, cond, else_dst)

    def goto_init(self, cond=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']
        self._clear_next_kwargs()
        self._clear_last_statement()
        self._clear_last_cond()
        
        src = self.current()
        dst = 0
        return self._go(src, dst, cond)

    def goto_next(self, cond=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']
        self._clear_next_kwargs()
        self._clear_last_statement()
        self._clear_last_cond()
        
        src = self.current()
        dst = self.current() + 1
        ret = self._go(src, dst, cond=cond)
        self.inc()
        return ret

    def goto_from(self, src, dst, cond=None, else_dst=None):
        if cond is None and 'cond' in self.next_kwargs:
            cond = self.next_kwargs['cond']
        self._clear_next_kwargs()
        self._clear_last_statement()
        self._clear_last_cond()
        
        return self._go(src, dst, cond, else_dst)

    #---------------------------------------------------------------------------
    def prev(self, var, delay, initval=0):
        return self.seq.prev(var, delay, initval)
        
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
        index = self._to_index(kwargs['index']) if 'index' in kwargs else self.current()
        
        if keep is not None:
            del kwargs['keep']
            for i in range(keep):
                kwargs['delay'] = i if delay is None else delay + i
                self.add(*statement, **kwargs)
            return self
        
        if delay is not None and delay > 0:
            self._add_delayed_state(delay)
            if eager_val:
                statement = [ self._add_delayed_subst(s, index, delay) for s in statement ]
                
            if cond is not None:
                if not lazy_cond:
                    cond = self._add_delayed_cond(cond, index, delay)
                statement = [ vtypes.If(cond)(*statement) ]
                self.last_statement = statement[0]
                
            self.delayed_body[delay][index].extend(statement)
            self._add_dst_var(statement)
            return self
            
        if cond is not None:
            statement = [ vtypes.If(cond)(*statement) ]
            self.last_statement = statement[0]
            
        self.body[index].extend(statement)
        self._add_dst_var(statement)
        return self

    #---------------------------------------------------------------------------
    def Cond(self, cond):
        if cond is None:
            self.last_cond = []
            return self

        if 'cond' not in self.next_kwargs:
            self.next_kwargs['cond'] = cond
        else:
            self.next_kwargs['cond'] = vtypes.Ands(self.next_kwargs['cond'], cond)
            
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
    def make_always(self, reset=(), body=(), case=True):
        if self.done:
            raise ValueError('make_always() has been already called.')
        self.done = True
        
        part_reset = self.make_reset(reset)
        part_body = list(body) + list( self.make_case() if case else self.make_if() )
        self.m.Always(vtypes.Posedge(self.clk))(
            vtypes.If(self.rst)(
                part_reset,
            )(
                part_body,
            ))
    
    #---------------------------------------------------------------------------
    def make_case(self):
        indexes = set(self.body.keys())
        indexes.update( set(self.jump.keys()) )
        
        for index in indexes:
            self._add_mark(index)
        
        ret = []
        ret.extend( self.seq.make_code() )
        ret.extend( self._get_delayed_substs() )
        
        for delay, dct in sorted(self.delayed_body.items(),
                                 key=lambda x:x[0], reverse=True):
            body = tuple([ self._get_delayed_when_statement(index, delay)
                           for index in sorted(dct.keys(), key=lambda x:x) ])
            case = vtypes.Case(self._get_delayed_state(delay))(*body)
            ret.append(case)
            
        body = tuple([ self._get_when_statement(index)
                       for index in sorted(indexes, key=lambda x:x) ])
        case = vtypes.Case(self.state)(*body)
        ret.append(case)

        return ret
    
    def make_if(self):
        indexes = set(self.body.keys())
        indexes.update( set(self.jump.keys()) )

        for index in indexes:
            self._add_mark(index)
            
        ret = []
        ret.extend( self.seq.make_code() )
        ret.extend( self._get_delayed_substs() )
        
        for delay, dct in sorted(self.delayed_body.items(),
                                 key=lambda x:x[0], reverse=True):
            ret.append([ self._get_delayed_if_statement(index, delay)
                         for index in sorted(dct.keys(), key=lambda x:x) ])

        ret.extend([ self._get_if_statement(index)
                     for index in sorted(indexes, key=lambda x:x) ])
        return ret

    #---------------------------------------------------------------------------
    def make_reset(self, reset):
        ret = collections.OrderedDict()

        for v in reset:
            if not isinstance(v, vtypes.Subst):
                raise TypeError('make_reset requires Subst, not %s' % str(type(v)))
            key = str(v.left)
            if key not in ret:
                ret[key] = v
            
        v = self.reset_visitor.visit(self.state)
        key = str(self.state)
        if v is not None and key not in ret:
            ret[key] = v
            
        for dst in self.delayed_state.values():
            v = self.reset_visitor.visit(dst)
            if v is None: continue
            key = str(v.left)
            if key not in ret:
                ret[key] = v

        for dst in self.dst_var.values():
            v = self.reset_visitor.visit(dst)
            if v is None: continue
            key = str(v.left)
            if key not in ret:
                ret[key] = v

        for v in self.seq.make_reset():
            if not isinstance(v, vtypes.Subst):
                raise TypeError('make_reset requires Subst, not %s' % str(type(v)))
            key = str(v.left)
            if key not in ret:
                ret[key] = v
            
        return list(ret.values())
        
    #---------------------------------------------------------------------------
    def _go(self, src, dst, cond=None, else_dst=None):
        self._add_jump(src, dst, cond, else_dst)
        return self

    def _add_jump(self, src, dst, cond=None, else_dst=None):
        self.jump[src].append( (dst, cond, else_dst) )
    
    #---------------------------------------------------------------------------
    def _add_dst_var(self, statement):
        for s in statement:
            values = self.dst_visitor.visit(s)
            for v in values:
                k = str(v)
                if k not in self.dst_var:
                    self.dst_var[k] = v
                
    #---------------------------------------------------------------------------
    def _add_delayed_cond(self, statement, index, delay):
        name_prefix = '_'.join(['', self.name, 'cond', str(index), str(self.tmp_count)])
        self.tmp_count += 1
        prev = statement
        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i+1)])
            tmp = self.m.Reg(tmp_name, initval=0)
            self.add(tmp(prev), delay=i)
            prev = tmp
        return prev
    
    #---------------------------------------------------------------------------
    def _add_delayed_subst(self, subst, index, delay):
        if not isinstance(subst, vtypes.Subst):
            return subst
        left = subst.left
        right = subst.right
        if isinstance(right, (bool, int, float, str,
                              vtypes._Constant, vtypes._ParameterVairable)):
            return subst
        width = left.bit_length()
        prev = right
        
        name_prefix = ('_'.join(['', left.name, str(index), str(self.tmp_count)]) 
                       if isinstance(left, vtypes._Variable) else
                       '_'.join(['', self.name, 'sbst', str(index), str(self.tmp_count)]))
        self.tmp_count += 1

        for i in range(delay):
            tmp_name = '_'.join([name_prefix, str(i+1)])
            tmp = self.m.Reg(tmp_name, width, initval=0)
            self.add(tmp(prev), delay=i)
            prev = tmp
        return left(prev)
    
    #---------------------------------------------------------------------------
    def _set_index(self, index=None):
        if index is None:
            self.state_count += 1
            return self.state_count
        self.state_count = index
        return self.state_count
        
    def _get_mark(self, index=None):
        if index is None:
            index = self.state_count
        if index not in self.mark:
            raise KeyError("No such index in FSM marks: %s" % index)
        return self.mark[index]
    
    def _set_mark(self, index=None, name=None):
        if index is None:
            index = self.state_count
        if name is None:
            name = self.name + '_' + str(index)
        self.mark[index] = self.m.Localparam(name, index)

    def _get_mark_index(self, s):
        for index, m in self.mark.items():
            if m.name == s.name:
                return index
        raise KeyError("No such mark in FSM marks: %s" % s.name)
    
    #---------------------------------------------------------------------------
    def _add_mark(self, index):
        index = self._to_index(index)
        if index not in self.mark:
            self._set_mark(index)
        mark = self._get_mark(index)
        return mark

    def _to_index(self, index):
        if not isinstance(index, int):
            index = self._get_mark_index(index)
        return index
    
    #---------------------------------------------------------------------------
    def _add_delayed_state(self, value):
        if not isinstance(value, int):
            raise TypeError("Delay amount must be int, not '%s'" % str(type(value)))
        
        if value < 0:
            raise ValueError("Delay amount must be positive number")
        
        if value == 0:
            return self.state
        
        if value <= self.delay_amount:
            return self._get_delayed_state(value)

        for i in range(self.delay_amount+1, value+1):
            d = self.m.Reg(''.join(['_d', str(i), '_', self.name]), self.width,
                           initval=self._get_mark(0))
            self.delayed_state[i] = d

        self.delay_amount = value
        return d

    def _get_delayed_state(self, value):
        if value == 0: return self.state
        if value not in self.delayed_state:
            raise IndexError('No such index %d in delayed state' % value)
        return self.delayed_state[value]

    def _get_delayed_substs(self):
        ret = []
        prev = self.state
        for d in range(1, self.delay_amount+1):
            ret.append(vtypes.Subst(self.delayed_state[d], prev))
            prev = self.delayed_state[d]
        return ret
            
    def _init_delayed_state(self):
        ret = []
        for d in range(1, self.delay_amount+1):
            ret.append(vtypes.Subst(self.delayed_state[d], self._get_mark(0)))
        return ret

    def _to_state_assign(self, dst, cond=None, else_dst=None):
        dst_mark = self._get_mark(dst)
        value = self.state(dst_mark)
        if cond is not None:
            value = vtypes.If(cond)(value)
            if else_dst is not None:
                else_dst_mark = self._get_mark(else_dst)
                value = value.Else( self.state(else_dst_mark) )
        return value
    
    #---------------------------------------------------------------------------
    def _cond_case(self, index):
        if index not in self.mark:
            self._set_mark(index)
        return self._get_mark(index)

    def _cond_if(self, index):
        if index not in self.mark:
            self._set_mark(index)
        return (self.state == self._get_mark(index))

    def _delayed_cond_if(self, index, delay):
        if index not in self.mark:
            self._set_mark(index)
        if delay > 0 and delay not in self.delayed_state:
            self._add_delayed_state(delay)
        return (self._get_delayed_state(delay) == self._get_mark(index))

    def _get_when_statement(self, index):
        body = []
        body.extend( self.body[index] )
        for dst, cond, else_dst in self.jump[index]:
            self._add_mark(dst)
            if else_dst is not None:
                self._add_mark(else_dst)
            body.append( self._to_state_assign(dst, cond, else_dst) )
        return vtypes.When(self._cond_case(index))( *body )
    
    def _get_delayed_when_statement(self, index, delay):
        return vtypes.When(self._cond_case(index))( *self.delayed_body[delay][index] )
    
    def _get_if_statement(self, index):
        body = []
        body.extend( self.body[index] )
        for dst, cond, else_dst in self.jump[index]:
            self._add_mark(dst)
            if else_dst is not None:
                self._add_mark(else_dst)
            body.append( self._to_state_assign(dst, cond, else_dst) )
        return vtypes.If(self._cond_if(index))( *body )

    def _get_delayed_if_statement(self, index, delay):
        return vtypes.If(self._delayed_cond_if(index, delay))( *self.delayed_body[delay][index] )
    
    #---------------------------------------------------------------------------
    def __call__(self, *statement, **kwargs):
        return self.add(*statement, **kwargs)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self):
        return self.state_count + 1
