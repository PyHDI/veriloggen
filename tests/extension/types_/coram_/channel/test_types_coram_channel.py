from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_coram_channel

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

  reg cthread_channel_0_ENQ;
  reg [32-1:0] cthread_channel_0_D;
  wire cthread_channel_0_FULL;
  wire cthread_channel_0_ALM_FULL;
  reg cthread_channel_0_DEQ;
  wire [32-1:0] cthread_channel_0_Q;
  wire cthread_channel_0_EMPTY;
  wire cthread_channel_0_ALM_EMPTY;

  CoramChannel
  #(
    .CORAM_THREAD_NAME("cthread"),
    .CORAM_THREAD_ID(0),
    .CORAM_ID(0),
    .CORAM_ADDR_LEN(4),
    .CORAM_DATA_WIDTH(32)
  )
  inst_cthread_channel_0
  (
    .CLK(CLK),
    .RST(RST),
    .ENQ(cthread_channel_0_ENQ),
    .D(cthread_channel_0_D),
    .FULL(cthread_channel_0_FULL),
    .ALM_FULL(cthread_channel_0_ALM_FULL),
    .DEQ(cthread_channel_0_DEQ),
    .Q(cthread_channel_0_Q),
    .EMPTY(cthread_channel_0_EMPTY),
    .ALM_EMPTY(cthread_channel_0_ALM_EMPTY)
  );

  reg [14-1:0] cthread_memory_0_ADDR;
  wire [32-1:0] cthread_memory_0_Q;
  reg [32-1:0] cthread_memory_0_D;
  reg cthread_memory_0_WE;

  CoramMemory1P
  #(
    .CORAM_THREAD_NAME("cthread"),
    .CORAM_THREAD_ID(0),
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
  reg _tmp_0;
  reg _cthread_channel_0_cond_0_1;
  reg _cthread_channel_0_cond_1_1;
  reg _cthread_channel_0_cond_2_1;
  reg _cthread_channel_0_cond_2_2;
  reg _cthread_memory_0_cond_0_1;
  reg _tmp_1;
  reg _cthread_memory_0_cond_1_1;
  reg _cthread_memory_0_cond_2_1;
  reg _cthread_memory_0_cond_2_2;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_3_0_1;
  reg _fsm_cond_4_1_1;
  reg _fsm_cond_5_2_1;
  reg _cthread_channel_0_cond_3_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;
  localparam fsm_7 = 7;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      addr <= 0;
      count <= 0;
      sum <= 0;
      _fsm_cond_3_0_1 <= 0;
      _fsm_cond_4_1_1 <= 0;
      _fsm_cond_5_2_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_3: begin
          if(_fsm_cond_3_0_1) begin
            $display("sum=%d", sum);
          end 
        end
        fsm_4: begin
          if(_fsm_cond_4_1_1) begin
            $display("sum=%d", sum);
          end 
        end
        fsm_5: begin
          if(_fsm_cond_5_2_1) begin
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
          if(!cthread_channel_0_EMPTY) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          addr <= addr + 1;
          count <= count + 1;
          if(count == 15) begin
            addr <= 0;
            count <= 0;
          end 
          if(count == 15) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          addr <= addr + 1;
          count <= count + 1;
          if(_tmp_1) begin
            sum <= sum + cthread_memory_0_Q;
          end 
          _fsm_cond_3_0_1 <= _tmp_1;
          if(count == 15) begin
            addr <= 0;
            count <= 0;
          end 
          if(count == 15) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          if(_tmp_1) begin
            sum <= sum + cthread_memory_0_Q;
          end 
          _fsm_cond_4_1_1 <= _tmp_1;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(_tmp_1) begin
            sum <= sum + cthread_memory_0_Q;
          end 
          _fsm_cond_5_2_1 <= _tmp_1;
          fsm <= fsm_6;
        end
        fsm_6: begin
          if(!cthread_channel_0_ALM_FULL) begin
            fsm <= fsm_7;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      cthread_channel_0_DEQ <= 0;
      _cthread_channel_0_cond_0_1 <= 0;
      _tmp_0 <= 0;
      _cthread_channel_0_cond_1_1 <= 0;
      _cthread_channel_0_cond_2_1 <= 0;
      _cthread_channel_0_cond_2_2 <= 0;
      cthread_channel_0_D <= 0;
      cthread_channel_0_ENQ <= 0;
      _cthread_channel_0_cond_3_1 <= 0;
    end else begin
      if(_cthread_channel_0_cond_2_2) begin
        _tmp_0 <= 0;
      end 
      if(_cthread_channel_0_cond_0_1) begin
        _tmp_0 <= !cthread_channel_0_EMPTY && cthread_channel_0_DEQ;
      end 
      if(_cthread_channel_0_cond_1_1) begin
        cthread_channel_0_DEQ <= 0;
      end 
      _cthread_channel_0_cond_2_2 <= _cthread_channel_0_cond_2_1;
      if(_cthread_channel_0_cond_3_1) begin
        cthread_channel_0_ENQ <= 0;
      end 
      if((fsm == 1) && !cthread_channel_0_EMPTY) begin
        cthread_channel_0_DEQ <= 1;
      end 
      _cthread_channel_0_cond_0_1 <= (fsm == 1) && !cthread_channel_0_EMPTY;
      _cthread_channel_0_cond_1_1 <= 1;
      _cthread_channel_0_cond_2_1 <= 1;
      if((fsm == 6) && !cthread_channel_0_FULL) begin
        cthread_channel_0_D <= sum;
      end 
      if((fsm == 6) && !cthread_channel_0_FULL) begin
        cthread_channel_0_ENQ <= 1;
      end 
      _cthread_channel_0_cond_3_1 <= 1;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      cthread_memory_0_ADDR <= 0;
      cthread_memory_0_D <= 0;
      cthread_memory_0_WE <= 0;
      _cthread_memory_0_cond_0_1 <= 0;
      _cthread_memory_0_cond_1_1 <= 0;
      _tmp_1 <= 0;
      _cthread_memory_0_cond_2_1 <= 0;
      _cthread_memory_0_cond_2_2 <= 0;
    end else begin
      if(_cthread_memory_0_cond_2_2) begin
        _tmp_1 <= 0;
      end 
      if(_cthread_memory_0_cond_0_1) begin
        cthread_memory_0_WE <= 0;
      end 
      if(_cthread_memory_0_cond_1_1) begin
        _tmp_1 <= 1;
      end 
      _cthread_memory_0_cond_2_2 <= _cthread_memory_0_cond_2_1;
      if(fsm == 2) begin
        cthread_memory_0_ADDR <= addr;
        cthread_memory_0_D <= count;
        cthread_memory_0_WE <= 1;
      end 
      _cthread_memory_0_cond_0_1 <= fsm == 2;
      if(fsm == 3) begin
        cthread_memory_0_ADDR <= addr;
      end 
      _cthread_memory_0_cond_1_1 <= fsm == 3;
      _cthread_memory_0_cond_2_1 <= fsm == 3;
    end
  end


endmodule



module CoramChannel #
(
  parameter CORAM_THREAD_NAME = "none",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  input ENQ,
  input [CORAM_DATA_WIDTH-1:0] D,
  output FULL,
  output ALM_FULL,
  input DEQ,
  output [CORAM_DATA_WIDTH-1:0] Q,
  output EMPTY,
  output ALM_EMPTY
);

  assign FULL = 0;
  assign ALM_FULL = 0;
  assign Q = 1;
  assign EMPTY = 0;
  assign ALM_EMPTY = 0;

endmodule



module CoramMemory1P #
(
  parameter CORAM_THREAD_NAME = "none",
  parameter CORAM_THREAD_ID = 0,
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
    test_module = types_coram_channel.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
