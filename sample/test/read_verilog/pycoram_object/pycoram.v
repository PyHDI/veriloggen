//------------------------------------------------------------------------------
// Single-Port CoRAM
//------------------------------------------------------------------------------
module CoramMemory1P(CLK, ADDR, D, WE, Q);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 10;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input  [CORAM_ADDR_LEN-1:0]   ADDR;
  input  [CORAM_DATA_WIDTH-1:0] D;
  input                         WE;
  output [CORAM_DATA_WIDTH-1:0] Q;
endmodule

module CoramMemoryBE1P(CLK, ADDR, D, WE, MASK, Q);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 10;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;
  localparam CORAM_MASK_WIDTH = CORAM_DATA_WIDTH / 8;

  input                         CLK;
  input  [CORAM_ADDR_LEN-1:0]   ADDR;
  input  [CORAM_DATA_WIDTH-1:0] D;
  input                         WE;
  input  [CORAM_MASK_WIDTH-1:0] MASK;
  output [CORAM_DATA_WIDTH-1:0] Q;
endmodule

//------------------------------------------------------------------------------
// Dual-Port CoRAM
//------------------------------------------------------------------------------
module CoramMemory2P(CLK, ADDR0, D0, WE0, Q0, ADDR1, D1, WE1, Q1);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 10;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input  [CORAM_ADDR_LEN-1:0]   ADDR0;
  input  [CORAM_DATA_WIDTH-1:0] D0;
  input                         WE0;
  output [CORAM_DATA_WIDTH-1:0] Q0;
  input  [CORAM_ADDR_LEN-1:0]   ADDR1;
  input  [CORAM_DATA_WIDTH-1:0] D1;
  input                         WE1;
  output [CORAM_DATA_WIDTH-1:0] Q1;
endmodule

module CoramMemoryBE2P(CLK, ADDR0, D0, WE0, MASK0, Q0, ADDR1, D1, WE1, MASK1, Q1);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 10;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;
  localparam CORAM_MASK_WIDTH = CORAM_DATA_WIDTH / 8;

  input                         CLK;
  input  [CORAM_ADDR_LEN-1:0]   ADDR0;
  input  [CORAM_DATA_WIDTH-1:0] D0;
  input                         WE0;
  input  [CORAM_MASK_WIDTH-1:0] MASK0;
  output [CORAM_DATA_WIDTH-1:0] Q0;
  input  [CORAM_ADDR_LEN-1:0]   ADDR1;
  input  [CORAM_DATA_WIDTH-1:0] D1;
  input                         WE1;
  input  [CORAM_MASK_WIDTH-1:0] MASK1;
  output [CORAM_DATA_WIDTH-1:0] Q1;
endmodule

//------------------------------------------------------------------------------
// CoRAM Input Stream (DRAM -> BRAM) (Non-Transparent FIFO with BlockRAM)
//------------------------------------------------------------------------------
module CoramInStream(CLK, RST, Q, DEQ, EMPTY, ALM_EMPTY);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 10;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input                         RST;
  output [CORAM_DATA_WIDTH-1:0] Q;
  input                         DEQ;
  output                        EMPTY;
  output                        ALM_EMPTY;
endmodule

//------------------------------------------------------------------------------
// CoRAM Output Stream (BRAM -> DRAM) (Non-Transparent FIFO with BlockRAM)
//------------------------------------------------------------------------------
module CoramOutStream(CLK, RST, D, ENQ, FULL, ALM_FULL);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 4;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input                         RST;
  input  [CORAM_DATA_WIDTH-1:0] D;
  input                         ENQ;
  output                        FULL;
  output                        ALM_FULL;
endmodule

//------------------------------------------------------------------------------
// CoRAM Channel (Non-Transparent FIFO with BlockRAM)
//------------------------------------------------------------------------------
module CoramChannel(CLK, RST,
                    D, ENQ, FULL, ALM_FULL,
                    Q, DEQ, EMPTY, ALM_EMPTY);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 4;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input                         RST;
  input  [CORAM_DATA_WIDTH-1:0] D;
  input                         ENQ;
  output                        FULL;
  output                        ALM_FULL;
  output [CORAM_DATA_WIDTH-1:0] Q;
  input                         DEQ;
  output                        EMPTY;
  output                        ALM_EMPTY;
endmodule

//------------------------------------------------------------------------------
// CoRAM Register
//------------------------------------------------------------------------------
module CoramRegister(CLK, D, WE, Q);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 10;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input  [CORAM_DATA_WIDTH-1:0] D;
  input                         WE;
  output [CORAM_DATA_WIDTH-1:0] Q;
endmodule

//------------------------------------------------------------------------------
// CoRAM Slave Stream (Non-Transparent FIFO with BlockRAM)
//------------------------------------------------------------------------------
module CoramSlaveStream(CLK, RST,
                        D, ENQ, FULL, ALM_FULL,
                        Q, DEQ, EMPTY, ALM_EMPTY);
  parameter CORAM_THREAD_NAME = "undefined";
  parameter CORAM_THREAD_ID = 0;
  parameter CORAM_ID = 0;
  parameter CORAM_SUB_ID = 0;
  parameter CORAM_ADDR_LEN = 4;
  parameter CORAM_DATA_WIDTH = 32;
  localparam CORAM_MEM_SIZE = 2 ** CORAM_ADDR_LEN;

  input                         CLK;
  input                         RST;
  input  [CORAM_DATA_WIDTH-1:0] D;
  input                         ENQ;
  output                        FULL;
  output                        ALM_FULL;
  output [CORAM_DATA_WIDTH-1:0] Q;
  input                         DEQ;
  output                        EMPTY;
  output                        ALM_EMPTY;
endmodule

