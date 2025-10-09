from __future__ import absolute_import
from __future__ import print_function
import sys
import os

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from veriloggen import *


def mkRawDims():
    m = Module('test_raw_dims')
    
    # Test raw_dims with Reg - 2D array [3:0][1:0]
    reg_with_raw_dims = m.Reg('reg_array', 8, dims=None, signed=False, 
                               initval=None, raw_width=(7, 0), 
                               raw_dims=[(3, 0), (1, 0)])
    
    # Test raw_dims with Wire - 1D array [7:0]
    wire_with_raw_dims = m.Wire('wire_array', 16, dims=None, signed=False,
                                 raw_width=(15, 0),
                                 raw_dims=[(7, 0)])
    
    # Test raw_dims with Integer - 1D array [9:0]
    int_with_raw_dims = m.Integer('int_array', 32, dims=None, signed=True,
                                   raw_width=(31, 0),
                                   raw_dims=[(9, 0)])
    
    # Test raw_dims with Input - 1D array [15:0]
    input_with_raw_dims = m.Input('input_array', 4, dims=None, signed=False,
                                   raw_width=(3, 0),
                                   raw_dims=[(15, 0)])
    
    # Test raw_dims with Output - 1D array [3:0]
    output_with_raw_dims = m.Output('output_array', 8, dims=None, signed=False,
                                     raw_width=(7, 0),
                                     raw_dims=[(3, 0)])
    
    # Test raw_dims with OutputReg - 1D array [1:0]
    outputreg_with_raw_dims = m.OutputReg('outputreg_array', 16, dims=None, 
                                          signed=False, initval=None,
                                          raw_width=(15, 0),
                                          raw_dims=[(1, 0)])
    
    # Test TmpReg with raw_dims - 1D array [3:0]
    tmp_reg = m.TmpReg(8, dims=None, raw_width=(7, 0), raw_dims=[(3, 0)])
    
    # Simple logic to use the variables
    clk = m.Input('clk')
    rst = m.Input('rst')
    
    m.Always(Posedge(clk))(
        If(rst)(
            reg_with_raw_dims[0][0](0)
        ).Else(
            reg_with_raw_dims[0][0](reg_with_raw_dims[0][0] + 1)
        ))
    
    wire_with_raw_dims[0].assign(reg_with_raw_dims[0][0])
    output_with_raw_dims[0].assign(wire_with_raw_dims[0])
    
    return m


if __name__ == '__main__':
    test = mkRawDims()
    verilog = test.to_verilog()
    print(verilog)

