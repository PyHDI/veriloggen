import cond

expected_verilog = """
module test #
(
  parameter WIDTH = 8
)
(
);

  reg CLK;
  reg RST;
  wire [(WIDTH - 1):0] LED;

  blinkled
  #(
    .WIDTH(WIDTH)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .LED(LED)
  );

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, LED);
  end

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end

  initial begin
    RST = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end
endmodule

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
      count <= (count == 1023)? 0 : count + 1;
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      LED <= (count == 1023)? LED + 1 : LED;
    end
  end
endmodule
"""

def test():
    test_module = cond.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
