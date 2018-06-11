from __future__ import absolute_import
from __future__ import print_function

import veriloggen
import thread_memorymodel_readwrite


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_memorymodel_readwrite.run(filename=None, simtype=simtype)

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')
