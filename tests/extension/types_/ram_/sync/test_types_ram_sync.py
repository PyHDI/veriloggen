from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_ram_sync

expected_verilog = """
module test;

  reg CLK;
  reg RST;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST);
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



module main
(
  input CLK,
  input RST
);

  wire [14-1:0] myram_0_addr;
  wire [32-1:0] myram_0_rdata;
  wire [32-1:0] myram_0_wdata;
  wire myram_0_wenable;
  wire [14-1:0] myram_1_addr;
  wire [32-1:0] myram_1_rdata;
  wire [32-1:0] myram_1_wdata;
  wire myram_1_wenable;

  myram
  myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable),
    .myram_1_addr(myram_1_addr),
    .myram_1_rdata(myram_1_rdata),
    .myram_1_wdata(myram_1_wdata),
    .myram_1_wenable(myram_1_wenable)
  );

  reg [32-1:0] waddr;
  reg [32-1:0] wdata;
  assign myram_0_addr = waddr;
  assign myram_0_wdata = wdata;
  assign myram_0_wenable = waddr < 16;
  reg [32-1:0] raddr;
  localparam _tmp_0 = 1;
  wire signed [_tmp_0-1:0] _tmp_1;
  assign _tmp_1 = 1;
  reg signed [_tmp_0-1:0] __tmp_1_1;
  reg signed [_tmp_0-1:0] __tmp_1_2;
  reg signed [_tmp_0-1:0] __tmp_1_3;
  reg signed [_tmp_0-1:0] __tmp_1_4;
  assign myram_1_addr = raddr;
  assign myram_1_wdata = 0;
  assign myram_1_wenable = 0;
  localparam _tmp_2 = (_tmp_0 >= 1)? _tmp_0 : 1;
  wire [_tmp_2-1:0] _tmp_3;
  assign _tmp_3 = __tmp_1_4 && (raddr < 16);
  reg [_tmp_2-1:0] __tmp_3_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      waddr <= 0;
      wdata <= 0;
      __tmp_1_1 <= 0;
      __tmp_1_2 <= 0;
      __tmp_1_3 <= 0;
      __tmp_1_4 <= 0;
      raddr <= 0;
      __tmp_3_1 <= 0;
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d", sum);
      end 
      if(waddr < 16) begin
        waddr <= waddr + 1;
        wdata <= wdata + 1;
      end 
      __tmp_1_1 <= _tmp_1;
      __tmp_1_2 <= __tmp_1_1;
      __tmp_1_3 <= __tmp_1_2;
      __tmp_1_4 <= __tmp_1_3;
      if(__tmp_1_4 && (raddr < 16)) begin
        raddr <= raddr + 1;
      end 
      __tmp_3_1 <= _tmp_3;
      if(__tmp_3_1) begin
        sum <= sum + myram_1_rdata;
      end 
      _seq_cond_0_1 <= __tmp_3_1;
    end
  end


endmodule



module myram
(
  input CLK,
  input [14-1:0] myram_0_addr,
  output [32-1:0] myram_0_rdata,
  input [32-1:0] myram_0_wdata,
  input myram_0_wenable,
  input [14-1:0] myram_1_addr,
  output [32-1:0] myram_1_rdata,
  input [32-1:0] myram_1_wdata,
  input myram_1_wenable
);

  reg [14-1:0] myram_0_daddr;
  reg [14-1:0] myram_1_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(myram_0_wenable) begin
      mem[myram_0_addr] <= myram_0_wdata;
    end 
    myram_0_daddr <= myram_0_addr;
  end

  assign myram_0_rdata = mem[myram_0_daddr];

  always @(posedge CLK) begin
    if(myram_1_wenable) begin
      mem[myram_1_addr] <= myram_1_wdata;
    end 
    myram_1_daddr <= myram_1_addr;
  end

  assign myram_1_rdata = mem[myram_1_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_ram_sync.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
