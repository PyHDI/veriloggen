from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import ram_rtl

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
  wire myram_0_enable;

  myram
  inst_myram
  (
    .CLK(CLK),
    .myram_0_addr(myram_0_addr),
    .myram_0_rdata(myram_0_rdata),
    .myram_0_wdata(myram_0_wdata),
    .myram_0_wenable(myram_0_wenable),
    .myram_0_enable(myram_0_enable)
  );

  reg [32-1:0] count;
  reg [32-1:0] sum;
  reg [32-1:0] addr;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  assign myram_0_wdata = (fsm == 1)? count : 'hx;
  assign myram_0_wenable = (fsm == 1)? 1'd1 : 0;
  assign myram_0_addr = (fsm == 2)? addr : 
                        (fsm == 1)? addr : 'hx;
  assign myram_0_enable = (fsm == 2)? 1'd1 : 
                          (fsm == 1)? 1'd1 : 0;
  localparam _tmp_0 = 1;
  wire [_tmp_0-1:0] _tmp_1;
  assign _tmp_1 = fsm == 2;
  reg [_tmp_0-1:0] __tmp_1_1;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  reg _fsm_cond_3_1_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

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
          if(__tmp_1_1) begin
            sum <= sum + myram_0_rdata;
          end 
          _fsm_cond_2_0_1 <= __tmp_1_1;
          if(count == 15) begin
            addr <= 0;
            count <= 0;
          end 
          if(count == 15) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(__tmp_1_1) begin
            sum <= sum + myram_0_rdata;
          end 
          _fsm_cond_3_1_1 <= __tmp_1_1;
          fsm <= fsm_4;
        end
        fsm_4: begin
          $display("expected_sum=%d", 120);
          fsm <= fsm_5;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_1_1 <= 0;
    end else begin
      __tmp_1_1 <= _tmp_1;
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
  input myram_0_enable
);

  reg [32-1:0] myram_0_rdata_out;
  assign myram_0_rdata = myram_0_rdata_out;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(myram_0_enable) begin
      if(myram_0_wenable) begin
        mem[myram_0_addr] <= myram_0_wdata;
        myram_0_rdata_out <= myram_0_wdata;
      end else begin
        myram_0_rdata_out <= mem[myram_0_addr];
      end
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = ram_rtl.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
