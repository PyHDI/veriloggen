from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import seq_multiple_add

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] idata_00;
  reg [32-1:0] idata_01;
  reg [32-1:0] idata_02;
  reg [32-1:0] idata_03;
  reg [32-1:0] idata_04;
  reg [32-1:0] idata_05;
  reg [32-1:0] idata_06;
  reg [32-1:0] idata_07;
  reg ivalid_00;
  reg ivalid_01;
  reg ivalid_02;
  reg ivalid_03;
  reg ivalid_04;
  reg ivalid_05;
  reg ivalid_06;
  reg ivalid_07;
  wire [32-1:0] odata;
  wire ovalid;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .idata_00(idata_00),
    .idata_01(idata_01),
    .idata_02(idata_02),
    .idata_03(idata_03),
    .idata_04(idata_04),
    .idata_05(idata_05),
    .idata_06(idata_06),
    .idata_07(idata_07),
    .ivalid_00(ivalid_00),
    .ivalid_01(ivalid_01),
    .ivalid_02(ivalid_02),
    .ivalid_03(ivalid_03),
    .ivalid_04(ivalid_04),
    .ivalid_05(ivalid_05),
    .ivalid_06(ivalid_06),
    .ivalid_07(ivalid_07),
    .odata(odata),
    .ovalid(ovalid)
  );

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end

  initial begin
    RST = 0;
    idata_00 = 0;
    idata_01 = 0;
    idata_02 = 0;
    idata_03 = 0;
    idata_04 = 0;
    idata_05 = 0;
    idata_06 = 0;
    idata_07 = 0;
    ivalid_00 = 0;
    ivalid_01 = 0;
    ivalid_02 = 0;
    ivalid_03 = 0;
    ivalid_04 = 0;
    ivalid_05 = 0;
    ivalid_06 = 0;
    ivalid_07 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    idata_00 = 0;
    idata_01 = 0;
    idata_02 = 0;
    idata_03 = 0;
    idata_04 = 0;
    idata_05 = 0;
    idata_06 = 0;
    idata_07 = 0;
    ivalid_00 = 0;
    ivalid_01 = 0;
    ivalid_02 = 0;
    ivalid_03 = 0;
    ivalid_04 = 0;
    ivalid_05 = 0;
    ivalid_06 = 0;
    ivalid_07 = 0;
    @(posedge CLK);
    #1;
    idata_00 = 1;
    idata_01 = 2;
    idata_02 = 3;
    idata_03 = 4;
    idata_04 = 5;
    idata_05 = 6;
    idata_06 = 7;
    idata_07 = 8;
    ivalid_00 = 1;
    ivalid_01 = 1;
    ivalid_02 = 1;
    ivalid_03 = 1;
    ivalid_04 = 1;
    ivalid_05 = 1;
    ivalid_06 = 1;
    ivalid_07 = 1;
    @(posedge CLK);
    #1;
    idata_00 = 1;
    idata_01 = 1;
    idata_02 = 1;
    idata_03 = 1;
    idata_04 = 1;
    idata_05 = 1;
    idata_06 = 1;
    idata_07 = 1;
    ivalid_00 = 0;
    ivalid_01 = 0;
    ivalid_02 = 0;
    ivalid_03 = 0;
    ivalid_04 = 0;
    ivalid_05 = 0;
    ivalid_06 = 0;
    ivalid_07 = 0;
    @(posedge CLK);
    #1;
    idata_00 = 10;
    idata_01 = 11;
    idata_02 = 12;
    idata_03 = 13;
    idata_04 = 14;
    idata_05 = 15;
    idata_06 = 16;
    idata_07 = 17;
    ivalid_00 = 1;
    ivalid_01 = 1;
    ivalid_02 = 1;
    ivalid_03 = 1;
    ivalid_04 = 1;
    ivalid_05 = 1;
    ivalid_06 = 1;
    ivalid_07 = 1;
    @(posedge CLK);
    #1;
    ivalid_00 = 0;
    ivalid_01 = 0;
    ivalid_02 = 0;
    ivalid_03 = 0;
    ivalid_04 = 0;
    ivalid_05 = 0;
    ivalid_06 = 0;
    ivalid_07 = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    $finish;
  end

endmodule

module blinkled
  (
   input CLK,
   input RST,
   input [32-1:0] idata_00,
   input [32-1:0] idata_01,
   input [32-1:0] idata_02,
   input [32-1:0] idata_03,
   input [32-1:0] idata_04,
   input [32-1:0] idata_05,
   input [32-1:0] idata_06,
   input [32-1:0] idata_07,
   input ivalid_00,
   input ivalid_01,
   input ivalid_02,
   input ivalid_03,
   input ivalid_04,
   input ivalid_05,
   input ivalid_06,
   input ivalid_07,
   output reg [32-1:0] odata,
   output reg ovalid
  );

  reg [32-1:0] _tmp_0;
  reg _tmp_1;
  reg [32-1:0] _tmp_2;
  reg _tmp_3;
  reg [32-1:0] _tmp_4;
  reg _tmp_5;
  reg [32-1:0] _tmp_6;
  reg _tmp_7;
  reg [32-1:0] _tmp_8;
  reg _tmp_9;
  reg [32-1:0] _tmp_10;
  reg _tmp_11;
  reg [32-1:0] _tmp_12;
  reg _tmp_13;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_5 <= 0;
      _tmp_6 <= 0;
      _tmp_7 <= 0;
      _tmp_8 <= 0;
      _tmp_9 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_12 <= 0;
      _tmp_13 <= 0;
      odata <= 0;
      ovalid <= 0;
    end else begin
      if((ivalid_00 && ivalid_01)) begin
        _tmp_0 <= (idata_00 + idata_01);
      end 
      _tmp_1 <= (ivalid_00 && ivalid_01);
      if((ivalid_02 && ivalid_03)) begin
        _tmp_2 <= (idata_02 + idata_03);
      end 
      _tmp_3 <= (ivalid_02 && ivalid_03);
      if((ivalid_04 && ivalid_05)) begin
        _tmp_4 <= (idata_04 + idata_05);
      end 
      _tmp_5 <= (ivalid_04 && ivalid_05);
      if((ivalid_06 && ivalid_07)) begin
        _tmp_6 <= (idata_06 + idata_07);
      end 
      _tmp_7 <= (ivalid_06 && ivalid_07);
      if((_tmp_1 && _tmp_3)) begin
        _tmp_8 <= (_tmp_0 + _tmp_2);
      end 
      _tmp_9 <= (_tmp_1 && _tmp_3);
      if((_tmp_5 && _tmp_7)) begin
        _tmp_10 <= (_tmp_4 + _tmp_6);
      end 
      _tmp_11 <= (_tmp_5 && _tmp_7);
      if((_tmp_9 && _tmp_11)) begin
        _tmp_12 <= (_tmp_8 + _tmp_10);
      end 
      _tmp_13 <= (_tmp_9 && _tmp_11);
      odata <= _tmp_12;
      ovalid <= _tmp_13;
    end
  end

endmodule
"""


def test():
    veriloggen.reset()
    test_module = seq_multiple_add.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
