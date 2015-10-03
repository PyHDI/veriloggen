import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  wire [32-1:0] y;
  reg prst;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .y(y),
    .prst(prst)
  );

  reg reset_done;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = (!CLK);
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
    prst = 0;
    x = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] _tmp_0;
  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          x <= (x + 1);
          _tmp_0 <= (_tmp_0 + 1);
          if(_tmp_0 == 10) begin
            xfsm <= xfsm_2;
          end 
        end
        xfsm_2: begin
          $finish;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      $display("x=%d", x);
      $display("y=%d", y);
    end 
  end


endmodule

module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] x,
  output [32-1:0] y,
  input prst
);

  wire [32-1:0] sum;
  reg [32-1:0] count;
  reg [32-1:0] _pipe_data_0;
  reg [32-1:0] _pipe_data_1;
  assign sum = _pipe_data_1;
  assign y = sum;

  always @(posedge CLK) begin
    if(RST) begin
      _pipe_data_0 <= 0;
      _pipe_data_1 <= 0;
    end else begin
      _pipe_data_0 <= (x + sum);
      _pipe_data_1 <= _pipe_data_0;
      if(prst) begin
        _pipe_data_0 <= 0;
      end 
    end
  end

  always @(posedge CLK) begin
    if(RST) begin
      count <= 0;
    end else begin
      count <= (count + 1);
      if(count == 1023) begin
        count <= 0;
      end 
    end
  end

endmodule
"""

def test_led():
    test_module = led.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
