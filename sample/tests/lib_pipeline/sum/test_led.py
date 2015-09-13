import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  wire [32-1:0] y;
  reg prst;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .y(y),
    .prst(prst)
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
    prst = 0;
    x = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    x = 0;
    @(posedge CLK);
    #1;
    x = 1;
    @(posedge CLK);
    #1;
    x = 2;
    @(posedge CLK);
    #1;
    x = 3;
    @(posedge CLK);
    #1;
    x = 4;
    @(posedge CLK);
    #1;
    x = 5;
    @(posedge CLK);
    #1;
    x = 6;
    @(posedge CLK);
    #1;
    x = 7;
    @(posedge CLK);
    #1;
    x = 8;
    @(posedge CLK);
    #1;
    x = 9;
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
    @(posedge CLK);
    #1;
    $finish;
  end
endmodule

module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] x,
  output [32-1:0] y,
  input prst
);

  wire [32-1:0] sum;
  reg [32-1:0] _pipe_data_0;
  assign sum = _pipe_data_0;
  assign y = sum;

  always @(posedge CLK) begin
    if(RST) begin
      _pipe_data_0 <= 0;
    end else begin
      _pipe_data_0 <= x + sum;
      if(prst) begin
        _pipe_data_0 <= 0;
      end 
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
