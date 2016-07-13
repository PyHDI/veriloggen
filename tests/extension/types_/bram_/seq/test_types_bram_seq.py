from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_bram_seq

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

  reg [14-1:0] mybram_0_addr;
  wire [32-1:0] mybram_0_rdata;
  reg [32-1:0] mybram_0_wdata;
  reg mybram_0_wenable;
  reg [14-1:0] mybram_1_addr;
  wire [32-1:0] mybram_1_rdata;
  reg [32-1:0] mybram_1_wdata;
  reg mybram_1_wenable;

  mybram
  inst_mybram
  (
    .CLK(CLK),
    .mybram_0_addr(mybram_0_addr),
    .mybram_0_rdata(mybram_0_rdata),
    .mybram_0_wdata(mybram_0_wdata),
    .mybram_0_wenable(mybram_0_wenable),
    .mybram_1_addr(mybram_1_addr),
    .mybram_1_rdata(mybram_1_rdata),
    .mybram_1_wdata(mybram_1_wdata),
    .mybram_1_wenable(mybram_1_wenable)
  );

  reg [32-1:0] waddr;
  reg [32-1:0] count;
  reg _mybram_cond_0_1;
  reg [32-1:0] raddr;
  reg [32-1:0] sum;
  localparam _tmp_0 = 1;
  wire [_tmp_0-1:0] _tmp_1;
  assign _tmp_1 = 1;
  reg [_tmp_0-1:0] __tmp_1_1;
  reg [_tmp_0-1:0] __tmp_1_2;
  reg [_tmp_0-1:0] __tmp_1_3;
  reg [_tmp_0-1:0] __tmp_1_4;
  reg _tmp_2;
  reg _mybram_cond_1_1;
  reg _mybram_cond_2_1;
  reg _mybram_cond_2_2;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      waddr <= 0;
      count <= 0;
      __tmp_1_1 <= 0;
      __tmp_1_2 <= 0;
      __tmp_1_3 <= 0;
      __tmp_1_4 <= 0;
      raddr <= 0;
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d", sum);
      end 
      if(waddr < 16) begin
        waddr <= waddr + 1;
        count <= count + 1;
      end 
      __tmp_1_1 <= _tmp_1;
      __tmp_1_2 <= __tmp_1_1;
      __tmp_1_3 <= __tmp_1_2;
      __tmp_1_4 <= __tmp_1_3;
      if(__tmp_1_4 && (raddr < 16)) begin
        raddr <= raddr + 1;
      end 
      if(_tmp_2) begin
        sum <= sum + mybram_1_rdata;
      end 
      _seq_cond_0_1 <= _tmp_2;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      mybram_1_wdata <= 0;
      mybram_1_wenable <= 0;
      mybram_0_addr <= 0;
      mybram_0_wdata <= 0;
      mybram_0_wenable <= 0;
      _mybram_cond_0_1 <= 0;
      mybram_1_addr <= 0;
      _mybram_cond_1_1 <= 0;
      _tmp_2 <= 0;
      _mybram_cond_2_1 <= 0;
      _mybram_cond_2_2 <= 0;
    end else begin
      if(_mybram_cond_2_2) begin
        _tmp_2 <= 0;
      end 
      if(_mybram_cond_0_1) begin
        mybram_0_wenable <= 0;
      end 
      if(_mybram_cond_1_1) begin
        _tmp_2 <= 1;
      end 
      _mybram_cond_2_2 <= _mybram_cond_2_1;
      mybram_1_wdata <= 0;
      mybram_1_wenable <= 0;
      if(waddr < 16) begin
        mybram_0_addr <= waddr;
        mybram_0_wdata <= count;
        mybram_0_wenable <= 1;
      end 
      _mybram_cond_0_1 <= waddr < 16;
      if(__tmp_1_4 && (raddr < 16)) begin
        mybram_1_addr <= raddr;
      end 
      _mybram_cond_1_1 <= __tmp_1_4 && (raddr < 16);
      _mybram_cond_2_1 <= __tmp_1_4 && (raddr < 16);
    end
  end


endmodule



module mybram
(
  input CLK,
  input [14-1:0] mybram_0_addr,
  output [32-1:0] mybram_0_rdata,
  input [32-1:0] mybram_0_wdata,
  input mybram_0_wenable,
  input [14-1:0] mybram_1_addr,
  output [32-1:0] mybram_1_rdata,
  input [32-1:0] mybram_1_wdata,
  input mybram_1_wenable
);

  reg [14-1:0] mybram_0_daddr;
  reg [14-1:0] mybram_1_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(mybram_0_wenable) begin
      mem[mybram_0_addr] <= mybram_0_wdata;
    end 
    mybram_0_daddr <= mybram_0_addr;
  end

  assign mybram_0_rdata = mem[mybram_0_daddr];

  always @(posedge CLK) begin
    if(mybram_1_wenable) begin
      mem[mybram_1_addr] <= mybram_1_wdata;
    end 
    mybram_1_daddr <= mybram_1_addr;
  end

  assign mybram_1_rdata = mem[mybram_1_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_bram_seq.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
