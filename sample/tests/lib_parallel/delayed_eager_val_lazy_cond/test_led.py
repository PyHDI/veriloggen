import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  wire led0;
  wire led1;
  wire led2;
  wire led3;
  wire led4;
  wire led5;
  wire led6;
  wire led7;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .led0(led0),
    .led1(led1),
    .led2(led2),
    .led3(led3),
    .led4(led4),
    .led5(led5),
    .led6(led6),
    .led7(led7)
  );

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
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    $finish;
  end

endmodule

module blinkled
  (
   input CLK,
   input RST,
   output reg led0,
   output reg led1,
   output reg led2,
   output reg led3,
   output reg led4,
   output reg led5,
   output reg led6,
   output reg led7
  );

  wire _tmp_0;
  assign _tmp_0 = 0;

  reg [35-1:0] count;
  reg [35-1:0] _count_1_0;
  reg _par_cond_2_1;
  reg _par_cond_2_2;
  reg _par_cond_2_3;
  reg _par_cond_2_4;
  reg _par_cond_2_5;
  reg _par_cond_2_6;
  reg _par_cond_2_7;
  reg _par_cond_2_8;
  reg _par_cond_2_9;
  reg _par_cond_2_10;
  reg _par_cond_2_11;
  reg _par_cond_2_12;
  reg _par_cond_2_13;
  reg _par_cond_2_14;
  reg _par_cond_2_15;
  reg _par_cond_2_16;
  reg _par_cond_2_17;
  reg _par_cond_2_18;

  always @(posedge CLK) begin
    if(RST) begin
      led0 <= 0;
      led1 <= 0;
      led2 <= 0;
      led3 <= 0;
      led4 <= 0;
      led5 <= 0;
      led6 <= 0;
      led7 <= 0;
      count <= 0;
      _count_1_0 <= 0;
      _par_cond_2_1 <= 0;
      _par_cond_2_2 <= 0;
      _par_cond_2_3 <= 0;
      _par_cond_2_4 <= 0;
      _par_cond_2_5 <= 0;
      _par_cond_2_6 <= 0;
      _par_cond_2_7 <= 0;
      _par_cond_2_8 <= 0;
      _par_cond_2_9 <= 0;
      _par_cond_2_10 <= 0;
      _par_cond_2_11 <= 0;
      _par_cond_2_12 <= 0;
      _par_cond_2_13 <= 0;
      _par_cond_2_14 <= 0;
      _par_cond_2_15 <= 0;
      _par_cond_2_16 <= 0;
      _par_cond_2_17 <= 0;
      _par_cond_2_18 <= 0;
    end else begin
      if(_par_cond_2_2) begin
        count <= (count + 1);
      end 
      if(_par_cond_2_4) begin
        led0 <= 0;
      end 
      if(_par_cond_2_6) begin
        led1 <= 0;
      end 
      if(_par_cond_2_8) begin
        led2 <= 0;
      end 
      if(_par_cond_2_10) begin
        led3 <= 0;
      end 
      if(_par_cond_2_12) begin
        led4 <= 0;
      end 
      if(_par_cond_2_14) begin
        led5 <= 0;
      end 
      if(_par_cond_2_16) begin
        led6 <= 0;
      end 
      if(_par_cond_2_18) begin
        led7 <= 0;
      end 
      if((count >= 7)) begin
        count <= _count_1_0;
      end 
      _par_cond_2_2 <= _par_cond_2_1;
      _par_cond_2_4 <= _par_cond_2_3;
      _par_cond_2_6 <= _par_cond_2_5;
      _par_cond_2_8 <= _par_cond_2_7;
      _par_cond_2_10 <= _par_cond_2_9;
      _par_cond_2_12 <= _par_cond_2_11;
      _par_cond_2_14 <= _par_cond_2_13;
      _par_cond_2_16 <= _par_cond_2_15;
      _par_cond_2_18 <= _par_cond_2_17;
      _count_1_0 <= _tmp_0;
      _par_cond_2_1 <= (count < 7);
      if((count == 0)) begin
        led0 <= 1;
      end 
      _par_cond_2_3 <= (count == 0);
      if((count == 1)) begin
        led1 <= 1;
      end 
      _par_cond_2_5 <= (count == 1);
      if((count == 2)) begin
        led2 <= 1;
      end 
      _par_cond_2_7 <= (count == 2);
      if((count == 3)) begin
        led3 <= 1;
      end 
      _par_cond_2_9 <= (count == 3);
      if((count == 4)) begin
        led4 <= 1;
      end 
      _par_cond_2_11 <= (count == 4);
      if((count == 5)) begin
        led5 <= 1;
      end 
      _par_cond_2_13 <= (count == 5);
      if((count == 6)) begin
        led6 <= 1;
      end 
      _par_cond_2_15 <= (count == 6);
      if((count == 7)) begin
        led7 <= 1;
      end 
      _par_cond_2_17 <= (count == 7);
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
