import led

expected_verilog = """
module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] x;
  reg vx;
  wire rx;
  reg [32-1:0] y;
  reg vy;
  wire ry;
  wire [32-1:0] z;
  wire vz;
  reg rz;
  wire [32-1:0] a;
  wire va;
  reg ra;

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
    .ry(ry),
    .z(z),
    .vz(vz),
    .rz(rz),
    .a(a),
    .va(va),
    .ra(ra)
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
    y = 0;
    vx = 0;
    vy = 0;
    rz = 0;
    ra = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end


  initial begin
    #2000;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    rz = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    rz = 1;
  end


  initial begin
    #2000;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = vx;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    #3;
    ra = 0;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    ra = 1;
  end


  initial begin
    #1000;
    @(posedge CLK);
    #1;
    vx = 1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    while((!rx)) begin
      @(posedge CLK);
      #1;
    end
    x = (x + 1);
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    vx = 0;
  end


  initial begin
    #1000;
    @(posedge CLK);
    #1;
    vy = 1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    while((!ry)) begin
      @(posedge CLK);
      #1;
    end
    y = (y + 2);
    @(posedge CLK);
    #1;
    @(posedge CLK);
    #1;
    vy = 0;
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  input [32-1:0] x,
  input vx,
  output rx,
  input [32-1:0] y,
  input vy,
  output ry,
  output [32-1:0] z,
  output vz,
  input rz,
  output [32-1:0] a,
  output va,
  input ra
);

  reg [32-1:0] _pipe_data_0;
  reg _pipe_valid_0;
  wire _pipe_ready_0;
  assign rx = (_pipe_ready_0 && _pipe_ready_1);
  assign ry = (_pipe_ready_0 && _pipe_ready_1);
  reg [32-1:0] _pipe_data_1;
  reg _pipe_valid_1;
  wire _pipe_ready_1;
  assign z = _pipe_data_0;
  assign vz = _pipe_valid_0;
  assign _pipe_ready_0 = rz;
  assign a = _pipe_data_1;
  assign va = _pipe_valid_1;
  assign _pipe_ready_1 = ra;

  always @(posedge CLK) begin
    if(RST) begin
      _pipe_data_0 <= 0;
      _pipe_valid_0 <= 0;
      _pipe_data_1 <= 0;
      _pipe_valid_1 <= 0;
    end else begin
      if(((vx && vy) && _pipe_ready_0)) begin
        _pipe_data_0 <= (x + y);
      end 
      if(_pipe_ready_0) begin
        _pipe_valid_0 <= (vx && vy);
      end 
      if(((vy && vx) && _pipe_ready_1)) begin
        _pipe_data_1 <= (y - x);
      end 
      if(_pipe_ready_1) begin
        _pipe_valid_1 <= (vy && vx);
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
