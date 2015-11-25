`include "pycoram.v"

`define THREAD_NAME "ctrl_thread"

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

  reg [W_A-1:0] mem_addr;
  reg [W_D-1:0] mem_d;
  reg           mem_we;
  wire [W_D-1:0] mem_q;
  
  reg [W_D-1:0]  comm_d;
  reg            comm_enq;
  wire           comm_full;
  wire [W_D-1:0] comm_q;
  reg            comm_deq;
  wire           comm_empty;
  
  always @(posedge CLK) begin
    if(RST) begin
      mem_addr <= 0;
      mem_d <= 0;
      mem_we <= 0;
      comm_d <= 0;
      comm_deq <= 0;
      comm_enq <= 0;
    end else begin
      // do nothing
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
    .CORAM_THREAD_NAME(`THREAD_NAME),
    .CORAM_ID(0),
    .CORAM_SUB_ID(0),
    .CORAM_ADDR_LEN(W_A),
    .CORAM_DATA_WIDTH(W_D)
    )
  inst_data_memory
  (.CLK(CLK),
   .ADDR(mem_addr),
   .D(mem_d),
   .WE(mem_we),
   .Q(mem_q)
   );

  CoramChannel
  #(
    .CORAM_THREAD_NAME(`THREAD_NAME),
    .CORAM_ID(0),
    .CORAM_ADDR_LEN(W_COMM_A),
    .CORAM_DATA_WIDTH(W_D)
    )
  inst_comm_channel
  (.CLK(CLK),
   .RST(RST),
   .D(comm_d),
   .ENQ(comm_enq),
   .FULL(comm_full),
   .Q(comm_q),
   .DEQ(comm_deq),
   .EMPTY(comm_empty)
   );

endmodule
  
