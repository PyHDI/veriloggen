import sort

expected_verilog = """
module sort #
 (
  parameter WIDTH = 32
 )
 (
  input CLK,
  input RST,
  input [WIDTH-1:0] input_0,
  input [WIDTH-1:0] input_1,
  input [WIDTH-1:0] input_2,
  input [WIDTH-1:0] input_3,
  output [WIDTH-1:0] output_0,
  output [WIDTH-1:0] output_1,
  output [WIDTH-1:0] output_2,
  output [WIDTH-1:0] output_3,
  input kick,
  output reg busy
 );

  reg [WIDTH-1:0] registers_0;
  reg [WIDTH-1:0] registers_1;
  reg [WIDTH-1:0] registers_2;
  reg [WIDTH-1:0] registers_3;

  assign output_0 = registers_0;
  assign output_1 = registers_1;
  assign output_2 = registers_2;
  assign output_3 = registers_3;

  reg [(32 - 1):0] fsm;

  localparam fsm_init = 0;

  localparam fsm_1 = 1;
  wire [(WIDTH - 1):0] small_0;
  wire [(WIDTH - 1):0] large_0;
  assign small_0 = (((registers_0 < registers_1))? registers_0 : registers_1);
  assign large_0 = (((registers_0 < registers_1))? registers_1 : registers_0);

  wire [(WIDTH - 1):0] small_1;
  wire [(WIDTH - 1):0] large_1;
  assign small_1 = (((large_0 < registers_2))? large_0 : registers_2);
  assign large_1 = (((large_0 < registers_2))? registers_2 : large_0);

  wire [(WIDTH - 1):0] small_2;
  wire [(WIDTH - 1):0] large_2;
  assign small_2 = (((large_1 < registers_3))? large_1 : registers_3);
  assign large_2 = (((large_1 < registers_3))? registers_3 : large_1);

  localparam fsm_2 = 2;
  wire [(WIDTH - 1):0] small_3;
  wire [(WIDTH - 1):0] large_3;
  assign small_3 = (((registers_0 < registers_1))? registers_0 : registers_1);
  assign large_3 = (((registers_0 < registers_1))? registers_1 : registers_0);

  wire [(WIDTH - 1):0] small_4;
  wire [(WIDTH - 1):0] large_4;
  assign small_4 = (((large_3 < registers_2))? large_3 : registers_2);
  assign large_4 = (((large_3 < registers_2))? registers_2 : large_3);

  localparam fsm_3 = 3;
  wire [(WIDTH - 1):0] small_5;
  wire [(WIDTH - 1):0] large_5;
  assign small_5 = (((registers_0 < registers_1))? registers_0 : registers_1);
  assign large_5 = (((registers_0 < registers_1))? registers_1 : registers_0);

  localparam fsm_4 = 4;

  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      busy <= 0;
      registers_0 <= 0;
      registers_1 <= 0;
      registers_2 <= 0;
      registers_3 <= 0;
      fsm <= fsm_init;
    end else begin
      case(fsm)
      fsm_init: begin
        begin
          if(kick) begin
            begin
              registers_0 <= input_0;
              registers_1 <= input_1;
              registers_2 <= input_2;
              registers_3 <= input_3;
              busy <= 1;
              fsm <= fsm_1;
            end
          end 
        end
      end
      fsm_1: begin
        begin
          registers_0 <= small_0;
          registers_1 <= small_1;
          registers_2 <= small_2;
          registers_3 <= large_2;
        end
        fsm <= fsm_2;
      end
      fsm_2: begin
        begin
          registers_0 <= small_3;
          registers_1 <= small_4;
          registers_2 <= large_4;
          registers_3 <= registers_3;
        end
        fsm <= fsm_3;
      end
      fsm_3: begin
        begin
          registers_0 <= small_5;
          registers_1 <= large_5;
          registers_2 <= registers_2;
          registers_3 <= registers_3;
        end
        fsm <= fsm_4;
      end
      fsm_4: begin
        begin
          registers_0 <= registers_0;
          registers_1 <= registers_1;
          registers_2 <= registers_2;
          registers_3 <= registers_3;
        end
        fsm <= fsm_5;
      end
      fsm_5: begin
        busy <= 0;
        fsm <= fsm_init;
      end
      endcase
    end
  end
endmodule
"""

def test_sort():
    sort_module = sort.mkSort()
    sort_code = sort_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == sort_code)
