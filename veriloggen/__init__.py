import sys
import os
if sys.version_info[0] < 3:
    import utils
    from veriloggen import *
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from veriloggen.veriloggen import *
