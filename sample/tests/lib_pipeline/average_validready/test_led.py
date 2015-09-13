import led

expected_verilog = """
module test;
  reg CLK;
  reg RST;
  reg [32-1:0] x;
  reg vx;
  wire rx;
  wire [32-1:0] y;
  wire vy;
  reg ry;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .x(x),
    .vx(vx),
    .rx(rx),
    .y(y),
    .vy(vy),
    .ry(ry)
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
    x = 0;
    vx = 0;
    ry = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    @(posedge CLK);
    #1;
    #3;
    ry = vx;
    @(posedge CLK);
    #1;
    #3;
    ry = 0;
    $finish;
  end

  initial begin
    #1000;
    @(posedge CLK);
    #1;
    while(1) begin
      vx = 1;
      if(rx) begin
        x = (x + 1);
      end 
      @(posedge CLK);
      #1;
    end
  end

endmodule

module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] x,
  input vx,
  output rx,
  output reg [32-1:0] y,
  output reg vy,
  input ry
);

  reg [32-1:0] _pipe_data_0;
  reg _pipe_valid_0;
  wire _pipe_ready_0;
  wire _pipe_nvalid_0;
  assign _pipe_nvalid_0 = ((_pipe_valid_0 && vx) && _pipe_ready_0);
  assign rx = _pipe_ready_0;
  reg [32-1:0] _pipe_data_1;
  reg _pipe_valid_1;
  wire _pipe_ready_1;
  wire _pipe_nvalid_1;
  assign _pipe_nvalid_1 = ((_pipe_valid_1 && vx) && _pipe_ready_1);
  assign _pipe_ready_0 = _pipe_ready_1;
  reg [32-1:0] _pipe_data_2;
  reg _pipe_valid_2;
  wire _pipe_ready_2;
  assign _pipe_ready_0 = _pipe_ready_2;
  assign _pipe_ready_1 = _pipe_ready_2;
  reg [32-1:0] _pipe_data_3;
  reg _pipe_valid_3;
  wire _pipe_ready_3;
  assign rx = _pipe_ready_3;
  reg [32-1:0] _pipe_data_4;
  reg _pipe_valid_4;
  wire _pipe_ready_4;
  assign _pipe_ready_2 = _pipe_ready_4;
  assign _pipe_ready_3 = _pipe_ready_4;
  assign _pipe_ready_4 = ry;

  always @(posedge CLK) begin
    if(RST) begin
      y <= 0;
      vy <= 0;
      _pipe_data_0 <= 0;
      _pipe_valid_0 <= 0;
      _pipe_data_1 <= 0;
      _pipe_valid_1 <= 0;
      _pipe_data_2 <= 0;
      _pipe_valid_2 <= 0;
      _pipe_data_3 <= 0;
      _pipe_valid_3 <= 0;
      _pipe_data_4 <= 0;
      _pipe_valid_4 <= 0;
    end else begin
      if((vx && _pipe_ready_0)) begin
        _pipe_data_0 <= x;
      end 
      if((vx && _pipe_ready_0)) begin
        _pipe_valid_0 <= vx;
      end 
      if((_pipe_nvalid_0 && _pipe_ready_1)) begin
        _pipe_data_1 <= _pipe_data_0;
      end 
      if((_pipe_nvalid_0 && _pipe_ready_1)) begin
        _pipe_valid_1 <= _pipe_nvalid_0;
      end 
      if(((_pipe_nvalid_0 & _pipe_nvalid_1) && _pipe_ready_2)) begin
        _pipe_data_2 <= (_pipe_data_0 + _pipe_data_1);
      end 
      if(_pipe_ready_2) begin
        _pipe_valid_2 <= (_pipe_nvalid_0 & _pipe_nvalid_1);
      end 
      if((vx && _pipe_ready_3)) begin
        _pipe_data_3 <= x;
      end 
      if(_pipe_ready_3) begin
        _pipe_valid_3 <= vx;
      end 
      if(((_pipe_valid_2 & _pipe_valid_3) && _pipe_ready_4)) begin
        _pipe_data_4 <= (_pipe_data_2 + _pipe_data_3);
      end 
      if(_pipe_ready_4) begin
        _pipe_valid_4 <= (_pipe_valid_2 & _pipe_valid_3);
      end 
      y <= _pipe_data_4;
      vy <= _pipe_valid_4;
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
