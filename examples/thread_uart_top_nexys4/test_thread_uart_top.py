from __future__ import absolute_import
from __future__ import print_function

import veriloggen
import thread_uart_top


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_uart_top.run(filename=None, simtype=simtype)

    verify_rslt = [line for line in rslt.splitlines() if line.startswith('# verify:')][0]
    assert(verify_rslt == '# verify: PASSED')
