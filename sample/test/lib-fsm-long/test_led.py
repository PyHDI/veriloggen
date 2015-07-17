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
  
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;
  localparam fsm_8 = 8;
  localparam fsm_9 = 9;
  localparam fsm_10 = 10;
  localparam fsm_11 = 11;
  localparam fsm_12 = 12;
  localparam fsm_13 = 13;
  localparam fsm_14 = 14;
  localparam fsm_15 = 15;
  reg [32-1:0] fsm;
  
  always @(posedge CLK) begin
    if(RST) begin        
      LED <= 0;        
      fsm <= fsm_init;
    end else begin
      case(fsm)
        fsm_init: begin        
          fsm <= fsm_1;
        end  
        fsm_1: begin        
          fsm <= fsm_2;
        end  
        fsm_2: begin        
          fsm <= fsm_3;
        end  
        fsm_3: begin        
          fsm <= fsm_4;
        end  
        fsm_4: begin        
          fsm <= fsm_5;
        end  
        fsm_5: begin        
          fsm <= fsm_6;
        end  
        fsm_6: begin        
          fsm <= fsm_7;
        end  
        fsm_7: begin        
          fsm <= fsm_8;
        end  
        fsm_8: begin        
          fsm <= fsm_9;
        end  
        fsm_9: begin        
          fsm <= fsm_10;
        end  
        fsm_10: begin        
          fsm <= fsm_11;
        end  
        fsm_11: begin        
          fsm <= fsm_12;
        end  
        fsm_12: begin        
          fsm <= fsm_13;
        end  
        fsm_13: begin        
          fsm <= fsm_14;
        end  
        fsm_14: begin        
          fsm <= fsm_15;
        end  
        fsm_15: begin        
          LED <= LED + 1;
          fsm <= fsm_init;
        end  
      endcase
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
