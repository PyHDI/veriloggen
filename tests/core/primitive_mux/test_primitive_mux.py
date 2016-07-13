from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import primitive_mux

expected_verilog = """
module blinkled #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [WIDTH-1:0] LED
);

  reg [32-1:0] count;

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      count <= _tmp_3;
    end
  end

  wire _tmp_0;
  wire [32-1:0] _tmp_1;
  wire [32-1:0] _tmp_2;
  wire [32-1:0] _tmp_3;
  assign _tmp_0 = count == 1023;
  assign _tmp_1 = 0;
  assign _tmp_2 = count + 1;

  prim_mux
  #(
    .WIDTH(32)
  )
  inst_prim_mux__tmp_3
  (
    .sel(_tmp_0),
    .ina(_tmp_1),
    .inb(_tmp_2),
    .out(_tmp_3)
  );


  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      LED <= _tmp_7;
    end
  end

  wire _tmp_4;
  wire [WIDTH-1:0] _tmp_5;
  wire [WIDTH-1:0] _tmp_6;
  wire [WIDTH-1:0] _tmp_7;
  assign _tmp_4 = count == 1023;
  assign _tmp_5 = LED + 1;
  assign _tmp_6 = LED;

  prim_mux
  #(
    .WIDTH(WIDTH)
  )
  inst_prim_mux__tmp_7
  (
    .sel(_tmp_4),
    .ina(_tmp_5),
    .inb(_tmp_6),
    .out(_tmp_7)
  );


endmodule



module prim_mux #
(
  parameter WIDTH = 1
)
(
  input sel,
  input [WIDTH-1:0] ina,
  input [WIDTH-1:0] inb,
  output [WIDTH-1:0] out
);

  assign out = (sel)? ina : inb;

endmodule
"""

def test():
    veriloggen.reset()
    test_module = primitive_mux.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
