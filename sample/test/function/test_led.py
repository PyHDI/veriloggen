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
  reg [32-1:0] count;

  function [WIDTH-1:0] inc;
    input [WIDTH-1:0] v;
    input [WIDTH-1:0] o;
    reg [WIDTH-1:0] tmp;
    begin        
      tmp = v + 1;
      inc = tmp;
    end 
  endfunction

  always @(posedge CLK) begin
    if(RST) begin        
      count <= 0;
    end else begin
      count <= inc(count, 1);
    end 
  end 

  always @(posedge CLK) begin
    if(RST) begin        
      LED <= 1;
    end else begin
      if(count == 1023) begin        
        LED[0] <= LED[WIDTH-1];
        LED[WIDTH-1:1] <= LED[WIDTH-2:0];
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

    assert(led_code == expected_code)
