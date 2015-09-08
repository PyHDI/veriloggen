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

  wire up;
  wire down;
  assign up = 1;
  assign down = 0;

  reg [3-1:0] count;
  reg _led0_2_0;
  reg _led0_2_1;
  reg _par_cond_2_2;
  reg _par_cond_2_3;
  reg _led1_2_4;
  reg _led1_2_5;
  reg _par_cond_2_6;
  reg _par_cond_2_7;
  reg _led2_2_8;
  reg _led2_2_9;
  reg _par_cond_2_10;
  reg _par_cond_2_11;
  reg _led3_2_12;
  reg _led3_2_13;
  reg _par_cond_2_14;
  reg _par_cond_2_15;
  reg _led4_2_16;
  reg _led4_2_17;
  reg _par_cond_2_18;
  reg _par_cond_2_19;
  reg _led5_2_20;
  reg _led5_2_21;
  reg _par_cond_2_22;
  reg _par_cond_2_23;
  reg _led6_2_24;
  reg _led6_2_25;
  reg _par_cond_2_26;
  reg _par_cond_2_27;
  reg _led7_2_28;
  reg _led7_2_29;
  reg _par_cond_2_30;
  reg _par_cond_2_31;

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
      _led0_2_0 <= 0;
      _led0_2_1 <= 0;
      _par_cond_2_2 <= 0;
      _par_cond_2_3 <= 0;
      _led1_2_4 <= 0;
      _led1_2_5 <= 0;
      _par_cond_2_6 <= 0;
      _par_cond_2_7 <= 0;
      _led2_2_8 <= 0;
      _led2_2_9 <= 0;
      _par_cond_2_10 <= 0;
      _par_cond_2_11 <= 0;
      _led3_2_12 <= 0;
      _led3_2_13 <= 0;
      _par_cond_2_14 <= 0;
      _par_cond_2_15 <= 0;
      _led4_2_16 <= 0;
      _led4_2_17 <= 0;
      _par_cond_2_18 <= 0;
      _par_cond_2_19 <= 0;
      _led5_2_20 <= 0;
      _led5_2_21 <= 0;
      _par_cond_2_22 <= 0;
      _par_cond_2_23 <= 0;
      _led6_2_24 <= 0;
      _led6_2_25 <= 0;
      _par_cond_2_26 <= 0;
      _par_cond_2_27 <= 0;
      _led7_2_28 <= 0;
      _led7_2_29 <= 0;
      _par_cond_2_30 <= 0;
      _par_cond_2_31 <= 0;
    end else begin
      if(_par_cond_2_3) begin
        led0 <= _led0_2_1;
      end 
      if(_par_cond_2_7) begin
        led1 <= _led1_2_5;
      end 
      if(_par_cond_2_11) begin
        led2 <= _led2_2_9;
      end 
      if(_par_cond_2_15) begin
        led3 <= _led3_2_13;
      end 
      if(_par_cond_2_19) begin
        led4 <= _led4_2_17;
      end 
      if(_par_cond_2_23) begin
        led5 <= _led5_2_21;
      end 
      if(_par_cond_2_27) begin
        led6 <= _led6_2_25;
      end 
      if(_par_cond_2_31) begin
        led7 <= _led7_2_29;
      end 
      _led0_2_1 <= _led0_2_0;
      _par_cond_2_3 <= _par_cond_2_2;
      _led1_2_5 <= _led1_2_4;
      _par_cond_2_7 <= _par_cond_2_6;
      _led2_2_9 <= _led2_2_8;
      _par_cond_2_11 <= _par_cond_2_10;
      _led3_2_13 <= _led3_2_12;
      _par_cond_2_15 <= _par_cond_2_14;
      _led4_2_17 <= _led4_2_16;
      _par_cond_2_19 <= _par_cond_2_18;
      _led5_2_21 <= _led5_2_20;
      _par_cond_2_23 <= _par_cond_2_22;
      _led6_2_25 <= _led6_2_24;
      _par_cond_2_27 <= _par_cond_2_26;
      _led7_2_29 <= _led7_2_28;
      _par_cond_2_31 <= _par_cond_2_30;
      count <= (count + 1);
      if((count == 0)) begin
        led0 <= up;
      end 
      _led0_2_0 <= down;
      _par_cond_2_2 <= (count == 0);
      if((count == 1)) begin
        led1 <= up;
      end 
      _led1_2_4 <= down;
      _par_cond_2_6 <= (count == 1);
      if((count == 2)) begin
        led2 <= up;
      end 
      _led2_2_8 <= down;
      _par_cond_2_10 <= (count == 2);
      if((count == 3)) begin
        led3 <= up;
      end 
      _led3_2_12 <= down;
      _par_cond_2_14 <= (count == 3);
      if((count == 4)) begin
        led4 <= up;
      end 
      _led4_2_16 <= down;
      _par_cond_2_18 <= (count == 4);
      if((count == 5)) begin
        led5 <= up;
      end 
      _led5_2_20 <= down;
      _par_cond_2_22 <= (count == 5);
      if((count == 6)) begin
        led6 <= up;
      end 
      _led6_2_24 <= down;
      _par_cond_2_26 <= (count == 6);
      if((count == 7)) begin
        led7 <= up;
      end 
      _led7_2_28 <= down;
      _par_cond_2_30 <= (count == 7);
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
