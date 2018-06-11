from __future__ import absolute_import
from __future__ import print_function

import veriloggen
import thread_axi_dma


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_axi_dma.run(filename=None, simtype=simtype)

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')
