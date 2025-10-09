from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import raw_dims

expected_verilog = """
module test_raw_dims
(
  input [3:0] input_array [15:0],
  output [7:0] output_array [3:0],
  output reg [15:0] outputreg_array [1:0],
  input clk,
  input rst
);

  reg [7:0] reg_array [3:0][1:0];
  wire [15:0] wire_array [7:0];
  integer int_array;
  reg [7:0] _tmp_0 [3:0];

  always @(posedge clk) begin
    if(rst) begin
      reg_array[0][0] <= 0;
    end else begin
      reg_array[0][0] <= reg_array[0][0] + 1;
    end
  end

  assign wire_array[0] = reg_array[0][0];
  assign output_array[0] = wire_array[0];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = raw_dims.mkRawDims()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)

