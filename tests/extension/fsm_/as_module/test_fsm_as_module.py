from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fsm_as_module

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
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  wire [32-1:0] _fsm_out_0;

  always @(*) begin
    fsm = _fsm_out_0;
  end

  wire [32-1:0] _fsm_count_1;

  always @(*) begin
    count = _fsm_count_1;
  end

  wire [WIDTH-1:0] _fsm_LED_2;

  always @(*) begin
    LED = _fsm_LED_2;
  end

  localparam _fsm_WIDTH = WIDTH;

  sub_fsm
  #(
    .WIDTH(_fsm_WIDTH)
  )
  inst_sub_fsm
  (
    .CLK(CLK),
    .RST(RST),
    .fsm(_fsm_out_0),
    .i_count(count),
    .i_LED(LED),
    .count(_fsm_count_1),
    .LED(_fsm_LED_2)
  );


endmodule



module sub_fsm #
(
  parameter WIDTH = 8
)
(
  input CLK,
  input RST,
  output reg [32-1:0] fsm,
  input [32-1:0] i_count,
  input [WIDTH-1:0] i_LED,
  output reg [32-1:0] count,
  output reg [WIDTH-1:0] LED
);

  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      count <= 0;
      LED <= 0;
    end else begin
      case(fsm)
        fsm_init: begin
          count <= i_count + 1;
          fsm <= fsm_1;
        end
        fsm_1: begin
          count <= i_count + 2;
          fsm <= fsm_2;
        end
        fsm_2: begin
          count <= i_count + 3;
          fsm <= fsm_3;
        end
        fsm_3: begin
          if(i_count < 1024) begin
            fsm <= fsm_init;
          end else begin
            fsm <= fsm_4;
          end
        end
        fsm_4: begin
          LED <= i_LED + 1;
          fsm <= fsm_2;
        end
      endcase
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = fsm_as_module.mkLed()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
