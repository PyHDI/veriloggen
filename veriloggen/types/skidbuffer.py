from __future__ import absolute_import
from __future__ import print_function

import veriloggen.core.vtypes as vtypes
from veriloggen.seq.seq import TmpSeq


class SkidBuffer(vtypes.VeriloggenNode):

    def __init__(self, m, clk, rst,
                 s_valid, m_ready, *s_values, prefix=None):

        if prefix is None:
            prefix = 'skidbuffer'

        if not s_values:
            raise ValueError("'s_values' must not be empty.")

        self.m = m
        self.clk = clk
        self.rst = rst
        self.s_values = s_values
        self.s_valid = s_valid
        self.m_ready = m_ready

        width = 0
        _s_values = []
        for s_value in s_values:
            v = m.TmpWireLike(s_value, prefix=prefix + '_s_value')
            v.assign(s_value)
            _s_values.append(v)
            w = s_value.get_width()
            if w is None:
                w = 1
            width += w

        _s_data = m.TmpWire(width, prefix=prefix + '_s_data')
        _s_data.assign(vtypes.Cat(*_s_values))

        _s_valid = m.TmpWire(prefix=prefix + '_s_valid')
        _s_valid.assign(s_valid)
        _m_ready = m.TmpWire(prefix=prefix + '_m_ready')
        _m_ready.assign(m_ready)

        (m_data, m_valid, s_ready) = make_skidbuffer(m, clk, rst,
                                                     _s_data, _s_valid, _m_ready,
                                                     prefix=prefix)

        self.m_values = []
        msb = width - 1
        for s_value in s_values:
            v = m.TmpWireLike(s_value, prefix=prefix + '_m_value')
            w = v.get_width()
            if w is None:
                w = 1
            lsb = msb - w + 1
            v.assign(vtypes.Slice(m_data, msb, lsb))
            self.m_values.append(v)
            msb -= w

        self.m_valid = m_valid
        self.s_ready = s_ready

    @property
    def values(self):
        return self.m_values

    @property
    def valid(self):
        return self.m_valid

    @property
    def ready(self):
        return self.s_ready

    def __getitem__(self, index):
        return self.m_values[index]


def make_skidbuffer(m, clk, rst,
                    s_data, s_valid, m_ready,
                    prefix=None):

    if prefix is None:
        if hasattr(s_data, 'name'):
            prefix = '_'.join([s_data.name, 'skidbuffer'])
        else:
            prefix = 'skidbuffer'

    m_data = m.TmpRegLike(s_data, prefix=prefix + '_data', initval=0)
    m_valid = m.TmpReg(prefix=prefix + '_valid', initval=0)

    s_ready = m.TmpWire(prefix=prefix + '_ready')

    tmp_data = m.TmpRegLike(s_data, prefix=prefix + '_tmp_data', initval=0)
    tmp_valid = m.TmpReg(prefix=prefix + '_tmp_valid', initval=0)

    next_data = m.TmpWireLike(s_data, prefix=prefix + '_next_data')
    next_valid = m.TmpWire(prefix=prefix + '_next_valid')

    s_ready.assign(vtypes.Not(tmp_valid))

    next_data.assign(vtypes.Mux(tmp_valid, tmp_data, s_data))
    next_valid.assign(vtypes.Ors(tmp_valid, s_valid))

    seq = TmpSeq(m, clk, rst, prefix=prefix + '_seq')

    seq.If(vtypes.Ors(m_ready, vtypes.Not(m_valid)))(
        m_data(next_data),
        m_valid(next_valid),
    )
    seq.If(vtypes.Not(tmp_valid), m_valid, vtypes.Not(m_ready))(
        tmp_data(s_data),
        tmp_valid(s_valid),
    )
    seq.If(tmp_valid, m_ready)(
        tmp_valid(0)
    )

    return m_data, m_valid, s_ready
