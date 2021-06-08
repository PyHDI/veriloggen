from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_prev_op

expected_verilog = """
module test #
(
  parameter WIDTH = 32
);

  reg CLK;
  reg RST;
  reg [WIDTH-1:0] x;
  wire [WIDTH-1:0] y;

  blinkled
  #(
    .WIDTH(WIDTH)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .y(y)
  );


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    x = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    x = 10;
    @(posedge CLK);
    #1;
    x = 11;
    @(posedge CLK);
    #1;
    x = 12;
    @(posedge CLK);
    #1;
    x = 13;
    @(posedge CLK);
    #1;
    x = 14;
    @(posedge CLK);
    #1;
    x = 15;
    @(posedge CLK);
    #1;
    x = 16;
    @(posedge CLK);
    #1;
    x = 17;
    @(posedge CLK);
    #1;
    x = 18;
    @(posedge CLK);
    #1;
    x = 19;
    @(posedge CLK);
    #1;
    x = 0;
    #1000;
    $finish;
  end


endmodule



module blinkled #
(
  parameter WIDTH = 32
)
(
  input CLK,
  input RST,
  input [WIDTH-1:0] x,
  output reg [WIDTH-1:0] y
);

  localparam _tmp_0 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_0-1:0] _tmp_1;
  assign _tmp_1 = x + 100;
  reg [_tmp_0-1:0] __tmp_1_1;
  localparam _tmp_2 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_2-1:0] _tmp_3;
  assign _tmp_3 = x + 100;
  reg [_tmp_2-1:0] __tmp_3_1;
  reg [_tmp_2-1:0] __tmp_3_2;
  localparam _tmp_4 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_4-1:0] _tmp_5;
  assign _tmp_5 = x + 100;
  reg [_tmp_4-1:0] __tmp_5_1;
  reg [_tmp_4-1:0] __tmp_5_2;
  reg [_tmp_4-1:0] __tmp_5_3;
  localparam _tmp_6 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_6-1:0] _tmp_7;
  assign _tmp_7 = x + 100;
  reg [_tmp_6-1:0] __tmp_7_1;
  reg [_tmp_6-1:0] __tmp_7_2;
  reg [_tmp_6-1:0] __tmp_7_3;
  reg [_tmp_6-1:0] __tmp_7_4;
  localparam _tmp_8 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_8-1:0] _tmp_9;
  assign _tmp_9 = x + 100;
  reg [_tmp_8-1:0] __tmp_9_1;
  reg [_tmp_8-1:0] __tmp_9_2;
  reg [_tmp_8-1:0] __tmp_9_3;
  reg [_tmp_8-1:0] __tmp_9_4;
  reg [_tmp_8-1:0] __tmp_9_5;
  localparam _tmp_10 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_10-1:0] _tmp_11;
  assign _tmp_11 = x + 100;
  reg [_tmp_10-1:0] __tmp_11_1;
  reg [_tmp_10-1:0] __tmp_11_2;
  reg [_tmp_10-1:0] __tmp_11_3;
  reg [_tmp_10-1:0] __tmp_11_4;
  reg [_tmp_10-1:0] __tmp_11_5;
  reg [_tmp_10-1:0] __tmp_11_6;
  localparam _tmp_12 = ((WIDTH >= 8)? WIDTH : 8) + 1;
  wire [_tmp_12-1:0] _tmp_13;
  assign _tmp_13 = x + 100;
  reg [_tmp_12-1:0] __tmp_13_1;
  reg [_tmp_12-1:0] __tmp_13_2;
  reg [_tmp_12-1:0] __tmp_13_3;
  reg [_tmp_12-1:0] __tmp_13_4;
  reg [_tmp_12-1:0] __tmp_13_5;
  reg [_tmp_12-1:0] __tmp_13_6;
  reg [_tmp_12-1:0] __tmp_13_7;
  reg [32-1:0] _tmp_14;

  always @(posedge CLK) begin
    if(RST) begin
      __tmp_1_1 <= 0;
      __tmp_3_1 <= 0;
      __tmp_3_2 <= 0;
      __tmp_5_1 <= 0;
      __tmp_5_2 <= 0;
      __tmp_5_3 <= 0;
      __tmp_7_1 <= 0;
      __tmp_7_2 <= 0;
      __tmp_7_3 <= 0;
      __tmp_7_4 <= 0;
      __tmp_9_1 <= 0;
      __tmp_9_2 <= 0;
      __tmp_9_3 <= 0;
      __tmp_9_4 <= 0;
      __tmp_9_5 <= 0;
      __tmp_11_1 <= 0;
      __tmp_11_2 <= 0;
      __tmp_11_3 <= 0;
      __tmp_11_4 <= 0;
      __tmp_11_5 <= 0;
      __tmp_11_6 <= 0;
      __tmp_13_1 <= 0;
      __tmp_13_2 <= 0;
      __tmp_13_3 <= 0;
      __tmp_13_4 <= 0;
      __tmp_13_5 <= 0;
      __tmp_13_6 <= 0;
      __tmp_13_7 <= 0;
      y <= 0;
    end else begin
      __tmp_1_1 <= _tmp_1;
      __tmp_3_1 <= _tmp_3;
      __tmp_3_2 <= __tmp_3_1;
      __tmp_5_1 <= _tmp_5;
      __tmp_5_2 <= __tmp_5_1;
      __tmp_5_3 <= __tmp_5_2;
      __tmp_7_1 <= _tmp_7;
      __tmp_7_2 <= __tmp_7_1;
      __tmp_7_3 <= __tmp_7_2;
      __tmp_7_4 <= __tmp_7_3;
      __tmp_9_1 <= _tmp_9;
      __tmp_9_2 <= __tmp_9_1;
      __tmp_9_3 <= __tmp_9_2;
      __tmp_9_4 <= __tmp_9_3;
      __tmp_9_5 <= __tmp_9_4;
      __tmp_11_1 <= _tmp_11;
      __tmp_11_2 <= __tmp_11_1;
      __tmp_11_3 <= __tmp_11_2;
      __tmp_11_4 <= __tmp_11_3;
      __tmp_11_5 <= __tmp_11_4;
      __tmp_11_6 <= __tmp_11_5;
      __tmp_13_1 <= _tmp_13;
      __tmp_13_2 <= __tmp_13_1;
      __tmp_13_3 <= __tmp_13_2;
      __tmp_13_4 <= __tmp_13_3;
      __tmp_13_5 <= __tmp_13_4;
      __tmp_13_6 <= __tmp_13_5;
      __tmp_13_7 <= __tmp_13_6;
      _tmp_14 <= x + 100 + __tmp_1_1 + __tmp_3_2 + __tmp_5_3 + __tmp_7_4 + __tmp_9_5 + __tmp_11_6 + __tmp_13_7;
      y <= _tmp_14 >> 3;
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = seq_prev_op.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
