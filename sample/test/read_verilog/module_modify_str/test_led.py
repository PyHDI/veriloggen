import led

expected_verilog = """
module modified_led #
  (
   parameter WIDTH = 8
  )
  (
   input [(0+1)-1:0] CLK, 
   input [(0+1)-1:0] RST, 
   output reg [((WIDTH-1)+1)-1:0] LED,
   input enable,
   output busy
  );
  reg [((32-1)+1)-1:0] count;
  always @(posedge CLK) begin
    if(RST) begin        
      count <= 0;
    end else if(enable) begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end 
  end 
  always @(posedge CLK) begin
    if(RST) begin        
      LED <= 0;
    end else begin
      if(count == 1023) begin        
        LED <= LED + 1;
      end  
    end 
  end 
  assign busy = count < 1023;
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
