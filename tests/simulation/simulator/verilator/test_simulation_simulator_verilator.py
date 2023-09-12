from __future__ import absolute_import
from __future__ import print_function

import veriloggen as vg
import simulation_simulator_verilator

expected_rslt = """\
LED:  0 count:         0
LED:  0 count:         1
LED:  0 count:         2
LED:  0 count:         3
LED:  0 count:         4
LED:  0 count:         5
LED:  0 count:         6
LED:  0 count:         7
LED:  0 count:         8
LED:  0 count:         9
LED:  0 count:        10
LED:  0 count:         0
LED:  0 count:         1
LED:  0 count:         2
LED:  0 count:         3
LED:  0 count:         4
LED:  0 count:         5
LED:  0 count:         6
LED:  0 count:         7
LED:  0 count:         8
LED:  0 count:         9
LED:  0 count:        10
LED:  0 count:        11
LED:  0 count:        12
LED:  0 count:        13
LED:  0 count:        14
LED:  0 count:        15
LED:  0 count:        16
LED:  0 count:        17
LED:  0 count:        18
LED:  0 count:        19
LED:  0 count:        20
LED:  0 count:        21
LED:  0 count:        22
LED:  0 count:        23
LED:  0 count:        24
LED:  0 count:        25
LED:  0 count:        26
LED:  0 count:        27
LED:  0 count:        28
LED:  0 count:        29
LED:  0 count:        30
LED:  0 count:        31
LED:  1 count:         0
LED:  1 count:         1
LED:  1 count:         2
LED:  1 count:         3
LED:  1 count:         4
LED:  1 count:         5
LED:  1 count:         6
LED:  1 count:         7
LED:  1 count:         8
LED:  1 count:         9
LED:  1 count:        10
LED:  1 count:        11
LED:  1 count:        12
LED:  1 count:        13
LED:  1 count:        14
LED:  1 count:        15
LED:  1 count:        16
LED:  1 count:        17
LED:  1 count:        18
LED:  1 count:        19
LED:  1 count:        20
LED:  1 count:        21
LED:  1 count:        22
LED:  1 count:        23
LED:  1 count:        24
LED:  1 count:        25
LED:  1 count:        26
LED:  1 count:        27
LED:  1 count:        28
LED:  1 count:        29
LED:  1 count:        30
LED:  1 count:        31
LED:  2 count:         0
LED:  2 count:         1
LED:  2 count:         2
LED:  2 count:         3
LED:  2 count:         4
LED:  2 count:         5
LED:  2 count:         6
LED:  2 count:         7
LED:  2 count:         8
LED:  2 count:         9
LED:  2 count:        10
LED:  2 count:        11
LED:  2 count:        12
LED:  2 count:        13
LED:  2 count:        14
LED:  2 count:        15
"""


def test():
    vg.reset()
    test_module = simulation_simulator_verilator.mkTest()
    sim = vg.simulation.Simulator(test_module, sim='verilator')
    rslt = sim.run(sim_time=1000)
    rslt = '\n'.join([line for line in rslt.splitlines() if line.startswith('LED:')] + [''])
    assert(expected_rslt == rslt)
