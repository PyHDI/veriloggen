import led

expected_verilog = """
module userlogic #
  (
   parameter DATA_WIDTH = 32,
   parameter ADDR_LEN = 10
  )
  (
   input CLK,
   input RST
  );

  reg [ADDR_LEN-1:0] mem_addr;
  reg [DATA_WIDTH-1:0] mem_wdata;
  wire [DATA_WIDTH-1:0] mem_rdata;
  reg mem_wvalid;
  reg [DATA_WIDTH-1:0] ch_wdata;
  reg ch_enq;
  wire ch_almfull;
  wire [DATA_WIDTH-1:0] ch_rdata;
  reg ch_deq;
  wire ch_empty;

  CoramMemory1P
  #(
    .CORAM_THREAD_NAME("ctrl_thread"),
    .CORAM_THREAD_ID(0),
    .CORAM_ID(0),
    .CORAM_SUB_ID(0),
    .CORAM_ADDR_LEN(ADDR_LEN),
    .CORAM_DATA_WIDTH(DATA_WIDTH)
  )
  mem
  (
    .CLK(CLK),
    .ADDR(mem_addr),
    .D(mem_wdata),
    .WE(mem_wvalid),
    .Q(mem_rdata)
  );

  CoramChannel
  #(
    .CORAM_THREAD_NAME("ctrl_thread"),
    .CORAM_THREAD_ID(0),
    .CORAM_ID(0),
    .CORAM_SUB_ID(0),
    .CORAM_ADDR_LEN(4),
    .CORAM_DATA_WIDTH(DATA_WIDTH)
  )
  ch
  (
    .CLK(CLK),
    .RST(RST),
    .D(ch_wdata),
    .ENQ(ch_enq),
    .ALM_FULL(ch_almfull),
    .Q(ch_rdata),
    .DEQ(ch_deq),
    .EMPTY(ch_empty)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;

  reg [32-1:0] read_count;
  reg [32-1:0] sum;
  reg [32-1:0] size;

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  reg [32-1:0] d1_fsm;
  reg [32-1:0] d2_fsm;

  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      mem_addr <= 0;
      mem_wdata <= 0;
      mem_wvalid <= 0;
      ch_wdata <= 0;
      ch_enq <= 0;
      ch_deq <= 0;
      read_count <= 0;
      sum <= 0;
      size <= 0;
      fsm <= fsm_init;
      d1_fsm <= fsm_init;
      d2_fsm <= fsm_init;
    end else begin
      d1_fsm <= fsm;
      d2_fsm <= d1_fsm;
      case(d2_fsm)
        fsm_2: begin
          size <= ch_rdata;
        end
        fsm_4: begin
          sum <= mem_rdata;
        end
        fsm_5: begin
          $display("sum=%d", sum);
        end
      endcase
      case(d1_fsm)
        fsm_2: begin
          ch_deq <= 0;
        end
        fsm_5: begin
          ch_enq <= 0;
        end
      endcase
      case(fsm)
        fsm_init: begin
          fsm <= fsm_1;
        end
        fsm_1: begin
          fsm <= fsm_2;
        end
        fsm_2: begin
          if(!ch_empty) begin
            ch_deq <= 1;
          end 
          fsm <= fsm_3;
        end
        fsm_3: begin
          fsm <= fsm_4;
        end
        fsm_4: begin
          mem_addr <= 0;
          read_count <= read_count + 1;
          if(read_count == size - 1) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          if(!ch_almfull) begin
            ch_enq <= 1;
          end 
          ch_wdata <= sum;
          fsm <= fsm_2;
        end
      endcase
    end
  end
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
  input [(((CORAM_ADDR_LEN - 1) + 1) - 1):0] ADDR,
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D,
  input WE,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule

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
  input [(((CORAM_ADDR_LEN - 1) + 1) - 1):0] ADDR,
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D,
  input WE,
  input [(((CORAM_MASK_WIDTH - 1) + 1) - 1):0] MASK,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q
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
  input [(((CORAM_ADDR_LEN - 1) + 1) - 1):0] ADDR0,
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D0,
  input WE0,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q0,
  input [(((CORAM_ADDR_LEN - 1) + 1) - 1):0] ADDR1,
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D1,
  input WE1,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q1
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
  input [(((CORAM_ADDR_LEN - 1) + 1) - 1):0] ADDR0,
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D0,
  input WE0,
  input [(((CORAM_MASK_WIDTH - 1) + 1) - 1):0] MASK0,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q0,
  input [(((CORAM_ADDR_LEN - 1) + 1) - 1):0] ADDR1,
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D1,
  input WE1,
  input [(((CORAM_MASK_WIDTH - 1) + 1) - 1):0] MASK1,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q1
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
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q,
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
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D,
  input ENQ,
  output FULL,
  output ALM_FULL
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
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D,
  input ENQ,
  output FULL,
  output ALM_FULL,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q,
  input DEQ,
  output EMPTY,
  output ALM_EMPTY
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
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D,
  input WE,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q
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
  input [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] D,
  input ENQ,
  output FULL,
  output ALM_FULL,
  output [(((CORAM_DATA_WIDTH - 1) + 1) - 1):0] Q,
  input DEQ,
  output EMPTY,
  output ALM_EMPTY
);

  localparam CORAM_MEM_SIZE = (2 ** CORAM_ADDR_LEN);

endmodule
"""

def test_led():
    userlogic = led.mkUserlogic()
    pycoram_modules = led.mkPycoram()
    code = ''.join([userlogic.to_verilog()] +
                   [p.to_verilog() for p in pycoram_modules.values()])

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
