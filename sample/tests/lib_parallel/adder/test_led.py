import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] idata0;
  reg [32-1:0] idata1;
  reg [32-1:0] idata2;
  reg [32-1:0] idata3;
  reg ivalid0;
  reg ivalid1;
  reg ivalid2;
  reg ivalid3;
  wire [32-1:0] odata;
  wire ovalid;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .idata0(idata0),
    .idata1(idata1),
    .idata2(idata2),
    .idata3(idata3),
    .ivalid0(ivalid0),
    .ivalid1(ivalid1),
    .ivalid2(ivalid2),
    .ivalid3(ivalid3),
    .odata(odata),
    .ovalid(ovalid)
  );

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end

  initial begin
    RST = 0;
    idata0 = 0;
    idata1 = 0;
    idata2 = 0;
    idata3 = 0;
    ivalid0 = 0;
    ivalid1 = 0;
    ivalid2 = 0;
    ivalid3 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    idata0 = 0;
    idata1 = 0;
    idata2 = 0;
    idata3 = 0;
    ivalid0 = 0;
    ivalid1 = 0;
    ivalid2 = 0;
    ivalid3 = 0;
    @(posedge CLK);
    #1;
    idata0 = 1;
    idata1 = 2;
    idata2 = 3;
    idata3 = 4;
    ivalid0 = 1;
    ivalid1 = 1;
    ivalid2 = 1;
    ivalid3 = 1;
    @(posedge CLK);
    #1;
    idata0 = 1;
    idata1 = 1;
    idata2 = 1;
    idata3 = 1;
    ivalid0 = 0;
    ivalid1 = 0;
    ivalid2 = 0;
    ivalid3 = 0;
    @(posedge CLK);
    #1;
    idata0 = 10;
    idata1 = 11;
    idata2 = 12;
    idata3 = 13;
    ivalid0 = 1;
    ivalid1 = 1;
    ivalid2 = 1;
    ivalid3 = 1;
    @(posedge CLK);
    #1;
    ivalid0 = 0;
    ivalid1 = 0;
    ivalid2 = 0;
    ivalid3 = 0;
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
   input [32-1:0] idata0,
   input [32-1:0] idata1,
   input [32-1:0] idata2,
   input [32-1:0] idata3,
   input ivalid0,
   input ivalid1,
   input ivalid2,
   input ivalid3,
   output reg [32-1:0] odata,
   output reg ovalid
  );

  reg [32-1:0] _tmp_0;
  reg _tmp_1;
  reg [32-1:0] _tmp_2;
  reg _tmp_3;
  reg [32-1:0] _tmp_4;
  reg _tmp_5;

  always @(posedge CLK) begin
    if(RST) begin
      odata <= 0;
      ovalid <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _tmp_5 <= 0;
    end else begin
      _tmp_1 <= ivalid0 && ivalid1;
      if(ivalid0 && ivalid1) begin
        _tmp_0 <= idata0 + idata1;
      end 
      _tmp_3 <= ivalid2 && ivalid3;
      if(ivalid2 && ivalid3) begin
        _tmp_2 <= idata2 + idata3;
      end 
      _tmp_5 <= _tmp_1 && _tmp_3;
      if(_tmp_1 && _tmp_3) begin
        _tmp_4 <= _tmp_0 + _tmp_2;
      end 
      odata <= _tmp_4;
      ovalid <= _tmp_5;
    end
  end

endmodule
"""

def test_led():
    test_module = led.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
