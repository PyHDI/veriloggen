from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_coram_memory

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

  reg [14-1:0] cthread_memory_0_ADDR;
  wire [32-1:0] cthread_memory_0_Q;
  reg [32-1:0] cthread_memory_0_D;
  reg cthread_memory_0_WE;

  CoramMemory1P
  #(
    .CORAM_THREAD_NAME("cthread"),
    .CORAM_ID(0),
    .CORAM_ADDR_LEN(14),
    .CORAM_DATA_WIDTH(32)
  )
  inst_cthread_memory_0
  (
    .CLK(CLK),
    .ADDR(cthread_memory_0_ADDR),
    .Q(cthread_memory_0_Q),
    .D(cthread_memory_0_D),
    .WE(cthread_memory_0_WE)
  );

  reg [32-1:0] count;
  reg [32-1:0] sum;
  reg [32-1:0] addr;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg _cthread_memory_0_cond_0_1;
  reg _tmp_0;
  reg _cthread_memory_0_cond_1_1;
  reg _cthread_memory_0_cond_2_1;
  reg _cthread_memory_0_cond_2_2;
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
            sum <= sum + cthread_memory_0_Q;
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
            sum <= sum + cthread_memory_0_Q;
          end 
          _fsm_cond_3_1_1 <= _tmp_0;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      cthread_memory_0_ADDR <= 0;
      cthread_memory_0_D <= 0;
      cthread_memory_0_WE <= 0;
      _cthread_memory_0_cond_0_1 <= 0;
      _cthread_memory_0_cond_1_1 <= 0;
      _tmp_0 <= 0;
      _cthread_memory_0_cond_2_1 <= 0;
      _cthread_memory_0_cond_2_2 <= 0;
    end else begin
      if(_cthread_memory_0_cond_2_2) begin
        _tmp_0 <= 0;
      end 
      if(_cthread_memory_0_cond_0_1) begin
        cthread_memory_0_WE <= 0;
      end 
      if(_cthread_memory_0_cond_1_1) begin
        _tmp_0 <= 1;
      end 
      _cthread_memory_0_cond_2_2 <= _cthread_memory_0_cond_2_1;
      if(fsm == 1) begin
        cthread_memory_0_ADDR <= addr;
        cthread_memory_0_D <= count;
        cthread_memory_0_WE <= 1;
      end 
      _cthread_memory_0_cond_0_1 <= fsm == 1;
      if(fsm == 2) begin
        cthread_memory_0_ADDR <= addr;
      end 
      _cthread_memory_0_cond_1_1 <= fsm == 2;
      _cthread_memory_0_cond_2_1 <= fsm == 2;
    end
  end


endmodule



module CoramMemory1P #
(
  parameter CORAM_THREAD_NAME = "none",
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input [CORAM_ADDR_LEN-1:0] ADDR,
  output [CORAM_DATA_WIDTH-1:0] Q,
  input [CORAM_DATA_WIDTH-1:0] D,
  input WE
);

  reg [CORAM_ADDR_LEN-1:0] D_ADDR;
  reg [CORAM_DATA_WIDTH-1:0] mem [0:2**CORAM_ADDR_LEN-1];

  always @(posedge CLK) begin
    if(WE) begin
      mem[ADDR] <= D;
    end 
    D_ADDR <= ADDR;
  end

  assign Q = mem[D_ADDR];

endmodule
"""

def test():
    veriloggen.reset()
    test_module = types_coram_memory.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
