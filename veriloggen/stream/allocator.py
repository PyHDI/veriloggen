from __future__ import absolute_import
from __future__ import print_function


class Allocator(object):

    def __init__(self, **custom_methods):
        self.custom_methods = custom_methods

    def allocate(self, m, seq, nodes, valid_list, senable):
        for node in sorted(nodes, key=lambda x: (-1, x.object_id) if x.start_stage is None else
                           (x.start_stage, x.object_id)):

            index = node.start_stage if node.start_stage is not None else None
            svalid = (valid_list[index] if valid_list is not None and index is not None
                      else None)
            self.implement(m, seq, node, svalid, senable)

    def implement(self, m, seq, node, svalid, senable):
        if node.__class__.__name__ in self.custom_methods:
            self.custom_methods[node.__class__.__name__](node)
            return

        if hasattr(node, '_implement'):
            node._implement(m, seq, svalid, senable)
            return

        raise TypeError(
            "Not found implement() method for Type '%s'" % str(type(node)))
