from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import resolver_div

expected_verilog = """
module Divider #
(
  parameter W_D = 32,
  parameter A_SIGNED = 1,
  parameter B_SIGNED = 1,
  parameter O_SIGNED = 1
)
(
  input CLK,
  input RST,
  input [32-1:0] in_a,
  input [32-1:0] in_b,
  input update,
  input enable,
  output reg [32-1:0] rslt,
  output reg [32-1:0] mod,
  output reg valid
);

  localparam DEPTH = 33;

  function [0:0] getsign;
    input [W_D-1:0] in;
    begin
      getsign = in[W_D - 1];
    end
  endfunction


  function [0:0] is_positive;
    input [W_D-1:0] in;
    begin
      is_positive = getsign(in) == 0;
    end
  endfunction


  function [W_D-1:0] complement2;
    input [W_D-1:0] in;
    begin
      complement2 = ~in + { { W_D - 1{ 1'b0 } }, 1'b1 };
    end
  endfunction


  function [W_D*2-1:0] complement2_2x;
    input [W_D*2-1:0] in;
    begin
      complement2_2x = ~in + { { W_D * 2 - 1{ 1'b0 } }, 1'b1 };
    end
  endfunction


  function [W_D-1:0] absolute;
    input [W_D-1:0] in;
    begin
      if(getsign(in)) begin
        absolute = complement2(in);
      end else begin
        absolute = in;
      end
    end
  endfunction

  wire [32-1:0] abs_in_a;
  wire [32-1:0] abs_in_b;
  assign abs_in_a = (1)? absolute(in_a) : in_a;
  assign abs_in_b = (1)? absolute(in_b) : in_b;
  genvar d;

  generate for(d=0; d<DEPTH; d=d+1) begin : s_depth
    reg stage_valid;
    reg in_a_positive;
    reg in_b_positive;
    reg [W_D*2-1:0] dividend;
    reg [W_D*2-1:0] divisor;
    reg [W_D*2-1:0] stage_rslt;
    wire [W_D*2-1:0] sub_value;
    wire is_large;
    assign sub_value = dividend - divisor;
    assign is_large = !sub_value[W_D * 2 - 1];
    if(d == 0) begin

      always @(posedge CLK) begin
        if(RST) begin
          stage_valid <= 0;
          in_a_positive <= 0;
          in_b_positive <= 0;
        end else begin
          if(update) begin
            stage_valid <= enable;
            in_a_positive <= is_positive(in_a);
            in_b_positive <= is_positive(in_b);
          end 
        end
      end

    end else begin

      always @(posedge CLK) begin
        if(RST) begin
          stage_valid <= 0;
          in_a_positive <= 0;
          in_b_positive <= 0;
        end else begin
          if(update) begin
            stage_valid <= s_depth[(d - 1)].stage_valid;
            in_a_positive <= s_depth[(d - 1)].in_a_positive;
            in_b_positive <= s_depth[(d - 1)].in_b_positive;
          end 
        end
      end

    end
    if(d == 0) begin

      always @(posedge CLK) begin
        if(update) begin
          dividend <= abs_in_a;
          divisor <= abs_in_b << W_D - 1;
          stage_rslt <= 0;
        end 
      end

    end else begin

      always @(posedge CLK) begin
        if(update) begin
          dividend <= (s_depth[(d - 1)].is_large)? s_depth[(d - 1)].sub_value : s_depth[(d - 1)].dividend;
          divisor <= s_depth[(d - 1)].divisor >> 1;
          stage_rslt <= { s_depth[(d - 1)].stage_rslt, s_depth[(d - 1)].is_large };
        end 
      end

    end
  end
  endgenerate


  always @(posedge CLK) begin
    if(RST) begin
      valid <= 0;
    end else begin
      if(update) begin
        valid <= s_depth[32].stage_valid;
      end 
    end
  end


  generate if(O_SIGNED) begin

    always @(posedge CLK) begin
      if(update) begin
        rslt <= (s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].stage_rslt : 
                (!s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].stage_rslt) : 
                (s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].stage_rslt) : 
                (!s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].stage_rslt : 'hx;
        mod <= (s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].dividend[W_D-1:0] : 
               (!s_depth[(DEPTH - 1)].in_a_positive && s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].dividend[W_D-1:0]) : 
               (s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? s_depth[(DEPTH - 1)].dividend[W_D-1:0] : 
               (!s_depth[(DEPTH - 1)].in_a_positive && !s_depth[(DEPTH - 1)].in_b_positive)? complement2_2x(s_depth[(DEPTH - 1)].dividend[W_D-1:0]) : 'hx;
      end 
    end

  end else begin

    always @(posedge CLK) begin
      if(update) begin
        rslt <= s_depth[(DEPTH - 1)].stage_rslt;
        mod <= s_depth[(DEPTH - 1)].dividend[W_D-1:0];
      end 
    end

  end
  endgenerate


endmodule
"""


def test():
    veriloggen.reset()
    test_module = resolver_div.mkOrig()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
