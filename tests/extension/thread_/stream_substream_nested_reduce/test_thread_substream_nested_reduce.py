from __future__ import absolute_import
from __future__ import print_function

import os
import veriloggen
import thread_stream_substream_nested_reduce


def test(request):
    veriloggen.reset()

    simtype = request.config.getoption('--sim')

    rslt = thread_stream_substream_nested_reduce.run(
        filename=None, simtype=simtype,
        outputfile=os.path.splitext(os.path.basename(__file__))[0] + '.out')

    verify_rslt = rslt.splitlines()[-1]
    assert(verify_rslt == '# verify: PASSED')
