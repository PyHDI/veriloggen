import vtypes

#-------------------------------------------------------------------------------
class FSM(object):
    """ Finite State Machine Generator """
    def __init__(self, m, name, width=32):
        self.m = m
        self.state = self.m.Reg(name + 'fsm', width)
        self.label = []
        self.label.append(self.m.Localparam(name + 'INIT', 0))

    def next(self, index=None):
        if index is None:
            return self.state( len(self) )
        return self.state(index)

    def cond(self, name='fsm_label'):
        ret = self.state == self.label[-1]
        self.label.append(self.m.Localparam(name + str(len(self.label)), len(self.label)))
        return ret

    def stage(self, *statement):
        return vtypes.If(self.cond())( statement )
    
    def __call__(self, *statement):
        return self.stage(*statement)

    def __getitem__(self, index):
        return self.label[index]

    def __len__(self):
        return len(self.label)
