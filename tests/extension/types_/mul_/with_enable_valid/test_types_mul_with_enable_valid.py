from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_mul_with_enable_valid

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    $finish;
  end


endmodule



module main
(
  input CLK,
  input RST
);

  reg [16-1:0] a;
  reg [16-1:0] b;
  wire [32-1:0] c;
  reg enable;
  wire mymul_valid;
  wire [32-1:0] mymul_value;

  mymul
  #(
    .lwidth(16),
    .rwidth(16)
  )
  mymul
  (
    .CLK(CLK),
    .RST(RST),
    .enable(enable),
    .valid(mymul_valid),
    .a(a),
    .b(b),
    .c(mymul_value)
  );


  always @(posedge CLK) begin
    if(RST) begin
      a <= 0;
      b <= 0;
      enable <= 0;
    end else begin
      a <= a + 1;
      b <= b + 1;
      enable <= !enable;
      if(mymul_valid) begin
        $display("mymul.value = %d", mymul_value);
      end 
    end
  end


endmodule



module mymul #
(
  parameter lwidth = 32,
  parameter rwidth = 32
)
(
  input CLK,
  input RST,
  input enable,
  output valid,
  input [lwidth-1:0] a,
  input [rwidth-1:0] b,
  output [lwidth+rwidth-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      valid_reg0 <= enable;
      valid_reg1 <= valid_reg0;
      valid_reg2 <= valid_reg1;
      valid_reg3 <= valid_reg2;
      valid_reg4 <= valid_reg3;
      valid_reg5 <= valid_reg4;
    end
  end


  mymul_core
  #(
    .lwidth(lwidth),
    .rwidth(rwidth)
  )
  mult
  (
    .CLK(CLK),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module mymul_core #
(
  parameter lwidth = 32,
  parameter rwidth = 32
)
(
  input CLK,
  input [lwidth-1:0] a,
  input [rwidth-1:0] b,
  output [lwidth+rwidth-1:0] c
);

  reg signed [lwidth-1:0] _a;
  reg signed [rwidth-1:0] _b;
  reg signed [lwidth+rwidth-1:0] _tmpval0;
  reg signed [lwidth+rwidth-1:0] _tmpval1;
  reg signed [lwidth+rwidth-1:0] _tmpval2;
  reg signed [lwidth+rwidth-1:0] _tmpval3;
  reg signed [lwidth+rwidth-1:0] _tmpval4;
  wire signed [lwidth+rwidth-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    _a <= a;
    _b <= b;
    _tmpval0 <= rslt;
    _tmpval1 <= _tmpval0;
    _tmpval2 <= _tmpval1;
    _tmpval3 <= _tmpval2;
    _tmpval4 <= _tmpval3;
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_mul_with_enable_valid.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
