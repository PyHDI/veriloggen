from __future__ import absolute_import
from __future__ import print_function

def make_port(m, _type, *args, **kwargs):
    if 'initval' in kwargs and 'Reg' not in _type:
        del kwargs['initval']
    return getattr(m, _type)(*args, **kwargs)

def connect_port(left, right):
    if isinstance(left, vtypes.Reg):
        left.module.Always()( left(right, blk=True) )
    else:
        left.assign(right)
