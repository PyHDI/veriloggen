import vtypes

#-------------------------------------------------------------------------------
class FSM(object):
    """ Finite State Machine Generator """
    def __init__(self, m, name, width=32, initname='init'):
        self.m = m
        self.name = name
        self.state = self.m.Reg(name, width)
        self.state_count = 0
        self.mark = {}
        self.set_mark(0, self.name + '_' + initname)

    def get_index(self):
        return self.state_count
        
    def init(self):
        return self.goto(0)
    
    def next(self):
        index = self.state_count + 1
        if index not in self.mark:
            self.set_mark(index)
        return self.state( self.mark[index] )

    def goto(self, index):
        if index not in self.mark:
            self.set_mark(index)
        return self.state( self.mark[index] )

    def set_mark(self, index=None, name=None):
        if index is None:
            index = self.state_count
        if name is None:
            name = self.name + '_' + str(index)
        self.mark[index] = self.m.Localparam(name, index)

    def get_mark(self, index=None):
        if index is None:
            index = self.state_count
        return self.mark[index]
        
    def cond(self):
        ret = (self.state == self.mark[self.state_count])
        self.state_count += 1
        return ret

    def add_stage(self, *statement):
        return vtypes.If(self.cond())( *statement )
    
    def __call__(self, *statement):
        return self.add_stage(*statement)

    def __getitem__(self, index):
        return self.mark[index]

    def __len__(self):
        return self.state_count + 1
