import led

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
  reg [32-1:0] tmp_0;
  reg [32-1:0] tmp_1;
  wire [32-1:0] tmp_2;
  reg [32-1:0] tmp_3;
  wire [32-1:0] tmp_4;
  reg [32-1:0] tmp_5;
  wire [32-1:0] tmp_6;
  always @(posedge CLK) begin
    if(RST) begin
      tmp_0 <= 0;
    end else begin
      if(tmp_0 == 1023) begin
        tmp_0 <= 0;
      end else begin
        tmp_0 <= tmp_0 + 1;
      end
    end
  end
  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(tmp_0 == 1023) begin
        LED <= LED + 1;
      end 
    end
  end
endmodule
"""

def test_led():
    led_module = led.mkLed()
    led_code = led_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == led_code)
