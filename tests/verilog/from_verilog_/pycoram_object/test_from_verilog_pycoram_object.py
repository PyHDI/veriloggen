from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import from_verilog_pycoram_object

expected_verilog = """
module CoramMemoryBE1P #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input [CORAM_ADDR_LEN - 1:0] ADDR,
  input [CORAM_DATA_WIDTH - 1:0] D,
  input WE,
  input [CORAM_MASK_WIDTH - 1:0] MASK,
  output [CORAM_DATA_WIDTH - 1:0] Q
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);
  localparam CORAM_MASK_WIDTH = (CORAM_DATA_WIDTH / 8);

endmodule

module CoramMemory2P #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input [CORAM_ADDR_LEN - 1:0] ADDR0,
  input [CORAM_DATA_WIDTH - 1:0] D0,
  input WE0,
  output [CORAM_DATA_WIDTH - 1:0] Q0,
  input [CORAM_ADDR_LEN - 1:0] ADDR1,
  input [CORAM_DATA_WIDTH - 1:0] D1,
  input WE1,
  output [CORAM_DATA_WIDTH - 1:0] Q1
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

module CoramMemoryBE2P #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input [CORAM_ADDR_LEN - 1:0] ADDR0,
  input [CORAM_DATA_WIDTH - 1:0] D0,
  input WE0,
  input [CORAM_MASK_WIDTH - 1:0] MASK0,
  output [CORAM_DATA_WIDTH - 1:0] Q0,
  input [CORAM_ADDR_LEN - 1:0] ADDR1,
  input [CORAM_DATA_WIDTH - 1:0] D1,
  input WE1,
  input [CORAM_MASK_WIDTH - 1:0] MASK1,
  output [CORAM_DATA_WIDTH - 1:0] Q1
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);
  localparam CORAM_MASK_WIDTH = (CORAM_DATA_WIDTH / 8);

endmodule

module CoramInStream #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  output [CORAM_DATA_WIDTH - 1:0] Q,
  input DEQ,
  output EMPTY,
  output ALM_EMPTY
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

module CoramOutStream #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 4,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  input [CORAM_DATA_WIDTH - 1:0] D,
  input ENQ,
  output FULL,
  output ALM_FULL
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

module CoramRegister #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input [CORAM_DATA_WIDTH - 1:0] D,
  input WE,
  output [CORAM_DATA_WIDTH - 1:0] Q
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

module CoramSlaveStream #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 4,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  input [CORAM_DATA_WIDTH - 1:0] D,
  input ENQ,
  output FULL,
  output ALM_FULL,
  output [CORAM_DATA_WIDTH - 1:0] Q,
  input DEQ,
  output EMPTY,
  output ALM_EMPTY
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

module userlogic #
(
  parameter W_A = 10,
  parameter W_D = 32,
  parameter W_COMM_A = 4
)
(
  input CLK,
  input RST
);

  reg [W_A - 1:0] mem_addr;
  reg [W_D - 1:0] mem_d;
  reg mem_we;
  wire [W_D - 1:0] mem_q;
  reg [W_D - 1:0] comm_d;
  reg comm_enq;
  wire comm_full;
  wire [W_D - 1:0] comm_q;
  reg comm_deq;
  wire comm_empty;

  always @(posedge CLK) begin
    if(RST) begin
      mem_addr <= 0;
      mem_d <= 0;
      mem_we <= 0;
      comm_d <= 0;
      comm_deq <= 0;
      comm_enq <= 0;
    end else begin
      mem_addr <= 0;
      mem_d <= 0;
      mem_we <= 0;
      comm_d <= 0;
      comm_deq <= 0;
      comm_enq <= 0;
    end
  end

  CoramMemory1P
  #(
    .CORAM_THREAD_NAME("ctrl_thread"),
    .CORAM_ID(0),
    .CORAM_SUB_ID(0),
    .CORAM_ADDR_LEN(W_A),
    .CORAM_DATA_WIDTH(W_D)
  )
  inst_data_memory
  (
    .CLK(CLK),
    .ADDR(mem_addr),
    .D(mem_d),
    .WE(mem_we),
    .Q(mem_q)
  );

  CoramChannel
  #(
    .CORAM_THREAD_NAME("ctrl_thread"),
    .CORAM_ID(0),
    .CORAM_ADDR_LEN(W_COMM_A),
    .CORAM_DATA_WIDTH(W_D)
  )
  inst_comm_channel
  (
    .CLK(CLK),
    .RST(RST),
    .D(comm_d),
    .ENQ(comm_enq),
    .FULL(comm_full),
    .Q(comm_q),
    .DEQ(comm_deq),
    .EMPTY(comm_empty)
  );

endmodule

module CoramMemory1P #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 10,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input [CORAM_ADDR_LEN - 1:0] ADDR,
  input [CORAM_DATA_WIDTH - 1:0] D,
  input WE,
  output [CORAM_DATA_WIDTH - 1:0] Q
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

module CoramChannel #
(
  parameter CORAM_THREAD_NAME = "undefined",
  parameter CORAM_THREAD_ID = 0,
  parameter CORAM_ID = 0,
  parameter CORAM_SUB_ID = 0,
  parameter CORAM_ADDR_LEN = 4,
  parameter CORAM_DATA_WIDTH = 32
)
(
  input CLK,
  input RST,
  input [CORAM_DATA_WIDTH - 1:0] D,
  input ENQ,
  output FULL,
  output ALM_FULL,
  output [CORAM_DATA_WIDTH - 1:0] Q,
  input DEQ,
  output EMPTY,
  output ALM_EMPTY
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule
"""

def test():
    veriloggen.reset()
    modules = from_verilog_pycoram_object.mkUserlogic()
    code = ''.join([ m.to_verilog() for m in modules.values() if not m.used ])

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
