from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import probe

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

  reg [32-1:0] _tmp_0;
  wire [32-1:0] _probe_1;
  assign _probe_1 = _tmp_0;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_0 <= 0;
    end else begin
      if(_tmp_0 == 1023) begin
        _tmp_0 <= 0;
      end else begin
        _tmp_0 <= _tmp_0 + 1;
      end
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      LED <= 0;
    end else begin
      if(_tmp_0 == 1023) begin
        LED <= LED + 1;
      end 
    end
  end

endmodule
"""

def test():
    veriloggen.reset()
    test_module = probe.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
