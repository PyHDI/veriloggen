from __future__ import absolute_import
import os
import sys
import collections
import functools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import vtypes
import lib.parallel

class FSM(vtypes.VeriloggenNode):
    """ Finite State Machine Generator """
    def __init__(self, m, name, width=32, initname='init'):
        self.m = m
        self.name = name
        self.width = width
        self.state_count = 0
        self.state = self.m.Reg(name, width)  # set initval later
        
        self.mark = {} # key:index
        self.set_mark(0, self.name + '_' + initname)
        self.state.initval = self.get_mark(0)
        
        self.body = collections.defaultdict(list)
        self.delay_amount = 0
        self.delayed_state = {} # key:delay
        self.delayed_body = collections.defaultdict(
            functools.partial(collections.defaultdict, list)) # key:delay
        self.tmp_count = 0

        self.par = lib.parallel.Parallel(self.m, self.name + '_par')

    #---------------------------------------------------------------------------
    def current(self):
        return self.get_index()
        
    def next(self):
        return self.get_index() + 1
        
    #---------------------------------------------------------------------------
    def increment(self):
        self.set_index(None)
    
    def inc(self):
        self.increment()
    
    #---------------------------------------------------------------------------
    def set(self, index=None):
        if index is None: index = self.current() + 1
        if isinstance(index, vtypes.Localparam):
            index = self.get_mark_index(index)
        if index not in self.mark:
            self.set_mark(index)
        return self.state( self.mark[index] )

    def set_init(self):
        return [ self.set(0) ] + self.init_delayed_state()

    def set_next(self):
        return self.set(None)

    def reset(self):
        return self.set_init()
    
    #---------------------------------------------------------------------------
    def goto(self, index=None, cond=None, else_index=None):
        g = self.set(index)
        if cond is not None:
            g = vtypes.If(cond)(g)
            if else_index is not None:
                g = g.Else( self.set(else_index) )
        self.add(g)
        return self

    def goto_init(self, cond=None):
        self.goto(0, cond=cond)
        return self

    def goto_next(self, cond=None):
        self.goto(None, cond=cond)
        self.inc()
        return self

    #---------------------------------------------------------------------------
    def prev(self, var, delay, initval=0):
        return self.par.prev(var, delay, initval)
        
    #---------------------------------------------------------------------------
    def add_delayed_cond(self, statement, index, delay):
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
    def add_delayed_subst(self, subst, index, delay):
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
    def add(self, *statement, **kwargs):
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
            self.add_delayed_state(delay)
            index = self.current()
            if eager_val:
                statement = [ self.add_delayed_subst(s, index, delay) for s in statement ]
            if cond is not None:
                if not lazy_cond:
                    cond = self.add_delayed_cond(cond, index, delay)
                statement = [ vtypes.If(cond)(*statement) ]
            self.delayed_body[delay][index].extend(statement)
            return self
            
        if cond is not None:
            statement = [ vtypes.If(cond)(*statement) ]
            
        index = self.current()
        self.body[index].extend(statement)
        return self

    #---------------------------------------------------------------------------
    def make_case(self):
        ret = []
        ret.extend( self.par.make_code() )
        ret.extend( self.get_delayed_substs() )
        
        for delay, dct in sorted(self.delayed_body.items(),
                                 key=lambda x:x[0], reverse=True):
            body = tuple([ self.get_delayed_when_statement(index, delay)
                           for index in sorted(dct.keys(), key=lambda x:x) ])
            case = vtypes.Case(self.get_delayed_state(delay))(*body)
            ret.append(case)
            
        body = tuple([ self.get_when_statement(index)
                       for index in sorted(self.body.keys(), key=lambda x:x) ])
        case = vtypes.Case(self.state)(*body)
        ret.append(case)

        return tuple(ret)
    
    def make_if(self):
        ret = []
        ret.extend( self.par.make_code() )
        ret.extend( self.get_delayed_substs() )
        
        for delay, dct in sorted(self.delayed_body.items(),
                                 key=lambda x:x[0], reverse=True):
            ret.append([ self.get_delayed_if_statement(index, delay)
                         for index in sorted(dct.keys(), key=lambda x:x) ])
            
        ret.extend([ self.get_if_statement(index)
                     for index in sorted(self.body.keys(), key=lambda x:x) ])
        return tuple(ret)

    #---------------------------------------------------------------------------
    def make_always(self, clk, rst, reset=(), body=(), case=True):
        self.m.Always(vtypes.Posedge(clk))(
            vtypes.If(rst)(
                reset,
                self.m.make_reset()
            )(
                body,
                self.make_case() if case else self.make_if()
            ))
    
    #---------------------------------------------------------------------------
    def get_index(self):
        return self.state_count
        
    def set_index(self, index=None):
        if index is None:
            self.state_count += 1
            return self.state_count
        self.state_count = index
        return self.state_count
        
    def get_mark(self, index=None):
        if index is None:
            index = self.state_count
        if index not in self.mark:
            raise KeyError("No such index in FSM marks: %s" % index)
        return self.mark[index]
    
    def set_mark(self, index=None, name=None):
        if index is None:
            index = self.state_count
        if name is None:
            name = self.name + '_' + str(index)
        self.mark[index] = self.m.Localparam(name, index)

    def get_mark_index(self, s):
        for index, m in self.mark.items():
            if m.name == s.name:
                return index
        raise KeyError("No such mark in FSM marks: %s" % s.name)
    
    #---------------------------------------------------------------------------
    def add_delayed_state(self, value):
        if not isinstance(value, int):
            raise TypeError("Delay amount must be int, not '%s'" % str(type(value)))
        
        if value < 0:
            raise ValueError("Delay amount must be positive number")
        
        if value == 0:
            return self.state
        
        if value <= self.delay_amount:
            return self.get_delayed_state(value)

        for i in range(self.delay_amount+1, value+1):
            d = self.m.Reg(''.join(['_d', str(i), '_', self.name]), self.width,
                           initval=self.get_mark(0))
            self.delayed_state[i] = d

        self.delay_amount = value
        return d

    def get_delayed_state(self, value):
        if value == 0: return self.state
        if value not in self.delayed_state:
            raise IndexError('No such index %d in delayed state' % value)
        return self.delayed_state[value]

    def get_delayed_substs(self):
        ret = []
        prev = self.state
        for d in range(1, self.delay_amount+1):
            ret.append(vtypes.Subst(self.delayed_state[d], prev))
            prev = self.delayed_state[d]
        return ret
            
    def init_delayed_state(self):
        ret = []
        for d in range(1, self.delay_amount+1):
            ret.append(vtypes.Subst(self.delayed_state[d], self.mark[0]))
        return ret
            
    #---------------------------------------------------------------------------
    def cond_case(self, index):
        if index not in self.mark:
            self.set_mark(index)
        return self.mark[index]

    def cond_if(self, index):
        if index not in self.mark:
            self.set_mark(index)
        return (self.state == self.mark[index])

    def delayed_cond_if(self, index, delay):
        if index not in self.mark:
            self.set_mark(index)
        if delay > 0 and delay not in self.delayed_state:
            self.add_delayed_state(delay)
        return (self.get_delayed_state(delay) == self.mark[index])

    def get_when_statement(self, index):
        return vtypes.When(self.cond_case(index))( *self.body[index] )
    
    def get_delayed_when_statement(self, index, delay):
        return vtypes.When(self.cond_case(index))( *self.delayed_body[delay][index] )
    
    def get_if_statement(self, index):
        return vtypes.If(self.cond_if(index))( *self.body[index] )

    def get_delayed_if_statement(self, index, delay):
        return vtypes.If(self.delayed_cond_if(index, delay))( *self.delayed_body[delay][index] )
    
    #---------------------------------------------------------------------------
    def __call__(self, *statement, **kwargs):
        return self.add(*statement, **kwargs)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self):
        return self.state_count + 1

