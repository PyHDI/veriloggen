from __future__ import absolute_import
from __future__ import print_function


class Allocator(object):

    def __init__(self, **custom_methods):
        self.custom_methods = custom_methods

    def allocate(self, m, seq, nodes):
        for node in sorted(nodes, key=lambda x: (-1, x.object_id) if x.start_stage is None else
                           (x.start_stage, x.object_id)):
            self.implement(m, seq, node)

    def implement(self, m, seq, node):
        if node.__class__.__name__ in self.custom_methods:
            self.custom_methods[node.__class__.__name__](node)
            return

        if hasattr(node, '_implement'):
            node._implement(m, seq)
            return

        raise TypeError(
            "Not found implement() method for Type '%s'" % str(type(node)))
