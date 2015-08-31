from __future__ import absolute_import
import os
import sys
import collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import vtypes

def setup_waveform(m, *uuts):
    new_uuts = []
    for u in uuts:
        if isinstance(u, (tuple, list)):
            new_uuts.extend(u)
        elif isinstance(u, dict):
            new_uuts.extend(list(u.values()))
        else:
            new_uuts.append(u)
    uuts = new_uuts
    ret = m.Initial(
        vtypes.Systask('dumpfile', 'uut.vcd'),
        vtypes.Systask('dumpvars', 0, *uuts)
    )
    return ret

def setup_clock(m, clk, hperiod=5):
    ret = m.Initial(
        clk(0),
        vtypes.Forever(clk(vtypes.Not(clk), ldelay=hperiod))
    )
    return ret

def setup_reset(m, reset, *statement, **kwargs):
    period = kwargs['period'] if 'period' in kwargs else 100
    ret = m.Initial(
        reset(0),
        statement,
        vtypes.Delay(100),
        reset(1),
        vtypes.Delay(100),
        reset(0),
    )
    return ret

def next_clock(clk):
    return vtypes.Event(vtypes.Posedge(clk))
