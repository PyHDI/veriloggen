from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import submodule_read_verilog

expected_verilog = """
module top #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output [WIDTH-1:0] LED,
  output [inst_blinkled_WIDTH-1+1-1:0] inst_blinkled_dummy_out0,
  input [inst_blinkled_WIDTH-1+1-1:0] inst_blinkled_dummy_in0
);

  localparam inst_blinkled_WIDTH = WIDTH;
  wire [inst_blinkled_WIDTH-1+1-1:0] inst_blinkled_dummy_out2;
  reg [inst_blinkled_WIDTH-1+1-1:0] inst_blinkled_dummy_in2;
  wire [inst_blinkled_WIDTH-1+1-1:0] inst_blinkled_dummy_out1;
  wire [inst_blinkled_WIDTH-1+1-1:0] inst_blinkled_dummy_in1;

  blinkled
  #(
    .WIDTH(inst_blinkled_WIDTH)
  )
  inst_blinkled
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED),
    .dummy_out0(inst_blinkled_dummy_out0),
    .dummy_out1(inst_blinkled_dummy_out1),
    .dummy_out2(inst_blinkled_dummy_out2),
    .dummy_in0(inst_blinkled_dummy_in0),
    .dummy_in1(inst_blinkled_dummy_in1),
    .dummy_in2(inst_blinkled_dummy_in2)
  );


endmodule



module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [WIDTH-1:0] LED,
  output [WIDTH-1:0] dummy_out0,
  output [WIDTH-1:0] dummy_out1,
  output [WIDTH-1:0] dummy_out2,
  input [WIDTH-1:0] dummy_in0,
  input [WIDTH-1:0] dummy_in1,
  input [WIDTH-1:0] dummy_in2
);

  reg [32-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(count == 1023) begin
        LED <= LED + 1;
      end 
    end
  end


endmodule
"""


def test():
    test_module = submodule_read_verilog.mkTop()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
