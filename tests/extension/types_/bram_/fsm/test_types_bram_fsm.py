from __future__ import absolute_import
from __future__ import print_function
import types_bram_fsm

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

  mybram
  inst_mybram
  (
    .CLK(CLK),
    .mybram_0_addr(mybram_0_addr),
    .mybram_0_rdata(mybram_0_rdata),
    .mybram_0_wdata(mybram_0_wdata),
    .mybram_0_wenable(mybram_0_wenable)
  );

  reg [32-1:0] count;
  reg [32-1:0] sum;
  reg [32-1:0] addr;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg _mybram_cond_0_1;
  reg _tmp_0;
  reg _mybram_cond_1_1;
  reg _mybram_cond_2_1;
  reg _mybram_cond_2_2;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  reg _fsm_cond_3_1_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      addr <= 0;
      count <= 0;
      sum <= 0;
      _fsm_cond_2_0_1 <= 0;
      _fsm_cond_3_1_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_2: begin
          if(_fsm_cond_2_0_1) begin
            $display("sum=%d", sum);
          end 
        end
        fsm_3: begin
          if(_fsm_cond_3_1_1) begin
            $display("sum=%d", sum);
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          addr <= 0;
          count <= 0;
          sum <= 0;
          fsm <= fsm_1;
        end
        fsm_1: begin
          addr <= addr + 1;
          count <= count + 1;
          if(count == 15) begin
            addr <= 0;
            count <= 0;
          end 
          if(count == 15) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          addr <= addr + 1;
          count <= count + 1;
          if(_tmp_0) begin
            sum <= sum + mybram_0_rdata;
          end 
          _fsm_cond_2_0_1 <= _tmp_0;
          if(count == 15) begin
            addr <= 0;
            count <= 0;
          end 
          if(count == 15) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_tmp_0) begin
            sum <= sum + mybram_0_rdata;
          end 
          _fsm_cond_3_1_1 <= _tmp_0;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      mybram_0_addr <= 0;
      mybram_0_wdata <= 0;
      mybram_0_wenable <= 0;
      _mybram_cond_0_1 <= 0;
      _mybram_cond_1_1 <= 0;
      _tmp_0 <= 0;
      _mybram_cond_2_1 <= 0;
      _mybram_cond_2_2 <= 0;
    end else begin
      if(_mybram_cond_2_2) begin
        _tmp_0 <= 0;
      end 
      if(_mybram_cond_0_1) begin
        mybram_0_wenable <= 0;
      end 
      if(_mybram_cond_1_1) begin
        _tmp_0 <= 1;
      end 
      _mybram_cond_2_2 <= _mybram_cond_2_1;
      if(fsm == 1) begin
        mybram_0_addr <= addr;
        mybram_0_wdata <= count;
        mybram_0_wenable <= 1;
      end 
      _mybram_cond_0_1 <= fsm == 1;
      if(fsm == 2) begin
        mybram_0_addr <= addr;
      end 
      _mybram_cond_1_1 <= fsm == 2;
      _mybram_cond_2_1 <= fsm == 2;
    end
  end


endmodule



module mybram
(
  input CLK,
  input [14-1:0] mybram_0_addr,
  output [32-1:0] mybram_0_rdata,
  input [32-1:0] mybram_0_wdata,
  input mybram_0_wenable
);

  reg [14-1:0] mybram_0_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(mybram_0_wenable) begin
      mem[mybram_0_addr] <= mybram_0_wdata;
    end 
    mybram_0_daddr <= mybram_0_addr;
  end

  assign mybram_0_rdata = mem[mybram_0_daddr];

endmodule
"""

def test():
    test_module = types_bram_fsm.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
