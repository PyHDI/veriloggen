from __future__ import absolute_import
from __future__ import print_function

import veriloggen
import thread_stream_pattern_len1


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_stream_pattern_len1.run(filename=None, simtype=simtype)

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')
