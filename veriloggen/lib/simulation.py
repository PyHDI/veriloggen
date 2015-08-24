from __future__ import absolute_import
import os
import sys
import collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import vtypes

def setup_waveform(m, uut):
    ret = m.Initial(
        vtypes.Systask('dumpfile', 'uut.vcd'),
        vtypes.Systask('dumpvars', 0, uut)
    )
    return ret

def setup_clock(m, clk, hperiod=5):
    ret = m.Initial(
        clk(0),
        vtypes.Forever(clk(vtypes.Not(clk), ldelay=hperiod))
    )
    return ret

def setup_reset(m, reset, period=100):
    ret = m.Initial(
        reset(0),
        vtypes.Delay(100),
        reset(1),
        vtypes.Delay(100),
        reset(0),
    )
    return ret

def next_clock(clk):
    return vtypes.Event(vtypes.Posedge(clk))

