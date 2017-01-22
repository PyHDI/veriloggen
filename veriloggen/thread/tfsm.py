from __future__ import absolute_import
from __future__ import print_function
import os
import sys
from collections import OrderedDict

import veriloggen.core.vtypes as vtypes


class Bind(object):

    def __init__(self, dst, value, cond=None):
        self.dst = dst
        self.value = value
        self.cond = cond

    def __repr__(self):
        ret = []
        ret.append(str(self.dst))
        ret.append('<-')
        ret.append(str(self.value))
        if self.cond is not None:
            ret.append(' if ')
            ret.append(str(self.cond))
        return ''.join(ret)


class TfsmNode(object):

    def __init__(self, src, dst, cond, elsedst):
        self.src = src
        self.dst = dst
        self.cond = cond
        self.elsedst = elsedst

    def __repr__(self):
        ret = []
        ret.append('SRC:%d' % self.src)
        ret.append(' DST:%d' % self.dst)
        if self.cond:
            ret.append(' COND:%s' % str(self.cond))
        if self.elsedst:
            ret.append(' ELSE:%s' % str(self.elsedst))
        return ''.join(ret)

    def __eq__(self, other):
        if not isinstance(other, TfsmNode):
            return False
        if self.src != other.src:
            return False
        if self.dst != other.dst:
            return False
        if self.cond != other.cond:
            return False
        if self.elsedst != other.elsedst:
            return False
        return True

    def __nq__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.src, self.dst, self.cond, self.elsedst))


class Tfsm(object):

    def __init__(self):
        self.dict = OrderedDict()
        self.count = 0
        self.bind = OrderedDict()
        self.object_bind = OrderedDict()
        self.constant = OrderedDict()
        self.loop = OrderedDict()

    def set(self, src=None, dst=None, cond=None, elsedst=None):
        if src is None:
            src = self.getCount()
        if dst is None:
            dst = src + 1
        self.add(src, dst, cond, elsedst)

    def add(self, src, dst, cond, elsedst):
        if src not in self.dict:
            self.dict[src] = []
        for n in self.dict[src]:
            if n.cond == cond or n.cond is None:
                n.cond = cond
                n.dst = dst
                n.elsedst = elsedst
                return
        self.dict[src].append(TfsmNode(src, dst, cond, elsedst))

    def get(self, src):
        if src not in self.dict:
            return ()
        return tuple(self.dict[src])

    def getCount(self):
        return self.count

    def incCount(self):
        self.count += 1

    def setBind(self, dst, value, st=None, cond=None):
        state = self.getCount() if st is None else st
        if state not in self.bind:
            self.bind[state] = []
        self.bind[state].append(Bind(dst, value, cond=cond))
        if isinstance(value, vtypes._Constant):
            self.setConstant(dst, value)
        else:
            self.unsetConstant(dst)

    def setObjectBind(self, dst, value, st=None, cond=None):
        state = self.getCount() if st is None else st
        if state not in self.object_bind:
            self.object_bind[state] = []
        self.object_bind[state].append(Bind(dst, value, cond=cond))

    def setConstant(self, dst, value):
        self.constant[dst] = value

    def unsetConstant(self, dst):
        if dst not in self.constant:
            return
        self.constant[dst] = None

    def getConstant(self, dst):
        if dst not in self.constant:
            return None
        return self.constant[dst]

    def setLoop(self, begin, end, iter_node=None, step_node=None):
        self.loop[begin] = (end, iter_node, step_node)

    def getCandidateLoops(self, pos):
        candidates = [(b, e) for b, (e, inode, unode)
                      in self.loop.items() if b <= pos and pos <= e]
        return candidates

    def getLoops(self):
        return self.loop

    def __repr__(self):
        ret = []
        ret.append('Count:%d' % self.count)
        ret.append(' Tfsm:')
        ret.append(str(self.dict))
        ret.append(' Bind:')
        ret.append(str(self.bind))
        ret.append(' Loop:')
        ret.append(str(self.loop))
        return ''.join(ret)
