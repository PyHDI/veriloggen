from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import chatter_clear

expected_verilog = """
module test #
(
  parameter length = 1024
);

  reg CLK;
  reg RST;
  reg din;
  wire dout;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _tmp_0 <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          din <= 0;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 2000) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 2000) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          din <= 1;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 10) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 10) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          din <= 0;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 10) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 10) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          din <= 1;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 2000) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 2000) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          din <= 0;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 10) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 10) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          din <= 1;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 10) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 10) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          din <= 0;
          _tmp_0 <= _tmp_0 + 1;
          if(_tmp_0 == 2000) begin
            _tmp_0 <= 0;
          end 
          if(_tmp_0 == 2000) begin
            fsm <= fsm_7;
          end 
        end
      endcase
    end
  end


  chatter_clear
  #(
    .length(length)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .din(din),
    .dout(dout)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, din, dout, fsm, _tmp_0);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    fsm = fsm_init;
    _tmp_0 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end


endmodule



module chatter_clear #
(
  parameter length = 1024
)
(
  input CLK,
  input RST,
  input din,
  output reg dout
);

  reg [32-1:0] _tmp_0;

  always @(posedge CLK) begin
    if(RST) begin
      dout <= 0;
    end else begin
      if(din == dout) begin
        _tmp_0 <= 0;
      end 
      if(din != dout) begin
        _tmp_0 <= _tmp_0 + 1;
      end 
      if(_tmp_0 == length) begin
        _tmp_0 <= 0;
      end 
      if(_tmp_0 == length) begin
        dout <= din;
      end 
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = chatter_clear.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
