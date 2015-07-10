import collections
import vtypes

#-------------------------------------------------------------------------------
class FSM(object):
    """ Finite State Machine Generator """
    def __init__(self, m, name, width=32, initname='init'):
        self.m = m
        self.name = name
        self.state = self.m.Reg(name, width)
        self.state_count = 0
        self.mark = collections.OrderedDict()
        self.set_mark(0, self.name + '_' + initname)
        self.body = collections.OrderedDict()

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
        self.update_state()
        ret = self.get(index)
        return ret

    def get(self, index):
        return vtypes.If(self.cond(index))( *self.body[index] ) # tuple
    
    def get_all(self):
        ret = []
        for index in self.body.keys():
            ret.append(self.get(index))
        return tuple(ret)
    
    def update_state(self):
        self.state_count += 1
        
    def cond(self, index):
        if index not in self.mark:
            self.set_mark(index)
        return (self.state == self.mark[index])

    def __call__(self, *statement):
        return self.add(*statement)

    def __getitem__(self, index):
        return self.body[index]

    def __len__(self):
        return self.state_count + 1
