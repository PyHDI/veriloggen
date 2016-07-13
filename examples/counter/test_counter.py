from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import counter

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [8-1:0] LED;

  blinkled
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
      #5 CLK = !CLK;
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



module blinkled
(
  input CLK,
  input RST,
  output [8-1:0] LED
);

  reg [11-1:0] _tmp_0;

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

  reg [8-1:0] _tmp_1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_1 <= 0;
    end else begin
      if(_tmp_0 == 1023) begin
        if(_tmp_1 == 2 ** 8 - 1) begin
          _tmp_1 <= 0;
        end else begin
          _tmp_1 <= _tmp_1 + 1;
        end
      end 
    end
  end

  assign LED = _tmp_1;

endmodule
"""

def test():
    veriloggen.reset()
    test_module = counter.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
