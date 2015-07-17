import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import vtypes

class FSM(vtypes.VeriloggenNode):
    """ Finite State Machine Generator """
    def __init__(self, m, name, width=32, initname='init'):
        self.m = m
        self.name = name
        self.state = self.m.Reg(name, width)
        self.state_count = 0
        self.mark = collections.OrderedDict()
        self.set_mark(0, self.name + '_' + initname)
        self.body = collections.OrderedDict()

    def to_case(self):
        ret = [ self.get_when_statement(index) for index in self.body.keys() ]
        return vtypes.Case(self.state)(*ret)
    
    def to_if(self):
        ret = [ self.get_if_statement(index) for index in self.body.keys() ]
        return tuple(ret)
    
    def init(self):
        return self.goto(0)
    
    def next(self):
        index = self.get_index() + 1
        if index not in self.mark:
            self.set_mark(index)
        return self.state( self.mark[index] )

    def goto(self, index):
        if isinstance(index, vtypes.Localparam):
            index = self.get_mark_index(index)
        if index not in self.mark:
            self.set_mark(index)
        return self.state( self.mark[index] )

    def get_index(self):
        return self.state_count
        
    def set_mark(self, index=None, name=None):
        if index is None:
            index = self.state_count
        if name is None:
            name = self.name + '_' + str(index)
        self.mark[index] = self.m.Localparam(name, index)

    def get_mark(self, index=None):
        if index is None:
            index = self.state_count
        if index not in self.mark:
            raise KeyError("No such index in FSM marks: %s" % index)
        return self.mark[index]

    def get_mark_index(self, s):
        for index, m in self.mark.items():
            if m.name == s.name:
                return index
        raise KeyError("No such mark in FSM marks: %s" % s.name)
    
    def add(self, *statement):
        index = self.get_index()
        self.body[index] = statement # tuple
        self.set_index()
        ret = self.get_if_statement(index)
        return ret

    def get_when_statement(self, index):
        return vtypes.When(self.cond_case(index))( *self.body[index] )
    
    def get_if_statement(self, index):
        return vtypes.If(self.cond_if(index))( *self.body[index] )
    
    def set_index(self, index=None):
        if index is None:
            self.state_count += 1
            return self.state_count
        self.state_count = index
        return self.state_count
        
    def cond_case(self, index):
        if index not in self.mark:
            self.set_mark(index)
        return self.mark[index]

    def cond_if(self, index):
        if index not in self.mark:
            self.set_mark(index)
        return (self.state == self.mark[index])

    def __call__(self, *statement):
        return self.add(*statement)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self):
        return self.state_count + 1
