import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  wire [32-1:0] y;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .y(y)
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
  output reg [32-1:0] y
);

  reg [32-1:0] _pipe_data_0;
  reg [32-1:0] _pipe_data_1;
  reg [32-1:0] _pipe_data_2;
  reg [32-1:0] _pipe_data_3;
  reg [32-1:0] _pipe_data_4;

  always @(posedge CLK) begin
    if(RST) begin
      y <= 0;
      _pipe_data_0 <= 0;
      _pipe_data_1 <= 0;
      _pipe_data_2 <= 0;
      _pipe_data_3 <= 0;
      _pipe_data_4 <= 0;
    end else begin
      _pipe_data_0 <= x;
      _pipe_data_1 <= _pipe_data_0;
      _pipe_data_2 <= _pipe_data_0 + _pipe_data_1;
      _pipe_data_3 <= x;
      _pipe_data_4 <= _pipe_data_2 + _pipe_data_3;
      y <= _pipe_data_4;
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
