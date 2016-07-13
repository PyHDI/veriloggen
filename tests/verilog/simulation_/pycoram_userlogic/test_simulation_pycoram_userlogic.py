from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import simulation_pycoram_userlogic

expected_verilog = """
module test #
(
  parameter DATA_WIDTH = 32,
  parameter ADDR_LEN = 10
);

  reg CLK;
  reg RST;
  wire [ADDR_LEN-1:0] mem_addr;
  wire [DATA_WIDTH-1:0] mem_wdata;
  reg [DATA_WIDTH-1:0] mem_rdata;
  wire mem_wvalid;
  wire mem_rvalid;
  wire [DATA_WIDTH-1:0] ch_wdata;
  wire ch_enq;
  reg ch_almfull;
  reg [DATA_WIDTH-1:0] ch_rdata;
  wire ch_deq;
  reg ch_empty;

  userlogic
  #(
    .DATA_WIDTH(DATA_WIDTH),
    .ADDR_LEN(ADDR_LEN)
  )
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .mem_addr(mem_addr),
    .mem_wdata(mem_wdata),
    .mem_rdata(mem_rdata),
    .mem_wvalid(mem_wvalid),
    .mem_rvalid(mem_rvalid),
    .ch_wdata(ch_wdata),
    .ch_enq(ch_enq),
    .ch_almfull(ch_almfull),
    .ch_rdata(ch_rdata),
    .ch_deq(ch_deq),
    .ch_empty(ch_empty)
  );

  reg [32-1:0] test_fsm;
  localparam test_fsm_init = 0;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, test_fsm);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    mem_rdata = 0;
    ch_almfull = 0;
    ch_rdata = 0;
    ch_empty = 1;
    test_fsm = test_fsm_init;
    #100;
    RST = 1;
    #100;
    RST = 0;
  end

  reg [32-1:0] _d1_test_fsm;
  reg _test_fsm_cond_12_0_1;
  localparam test_fsm_1 = 1;
  localparam test_fsm_2 = 2;
  localparam test_fsm_3 = 3;
  localparam test_fsm_4 = 4;
  localparam test_fsm_5 = 5;
  localparam test_fsm_6 = 6;
  localparam test_fsm_7 = 7;
  localparam test_fsm_8 = 8;
  localparam test_fsm_9 = 9;
  localparam test_fsm_10 = 10;
  localparam test_fsm_11 = 11;
  localparam test_fsm_12 = 12;
  localparam test_fsm_13 = 13;

  always @(posedge CLK) begin
    if(RST) begin
      test_fsm <= test_fsm_init;
      _d1_test_fsm <= test_fsm_init;
      ch_empty <= 1;
      ch_rdata <= 0;
      mem_rdata <= 0;
      _test_fsm_cond_12_0_1 <= 0;
    end else begin
      _d1_test_fsm <= test_fsm;
      case(_d1_test_fsm)
        test_fsm_12: begin
          if(_test_fsm_cond_12_0_1) begin
            mem_rdata <= mem_rdata + 1;
          end 
        end
      endcase
      case(test_fsm)
        test_fsm_init: begin
          test_fsm <= test_fsm_1;
        end
        test_fsm_1: begin
          test_fsm <= test_fsm_2;
        end
        test_fsm_2: begin
          test_fsm <= test_fsm_3;
        end
        test_fsm_3: begin
          test_fsm <= test_fsm_4;
        end
        test_fsm_4: begin
          test_fsm <= test_fsm_5;
        end
        test_fsm_5: begin
          test_fsm <= test_fsm_6;
        end
        test_fsm_6: begin
          test_fsm <= test_fsm_7;
        end
        test_fsm_7: begin
          test_fsm <= test_fsm_8;
        end
        test_fsm_8: begin
          test_fsm <= test_fsm_9;
        end
        test_fsm_9: begin
          test_fsm <= test_fsm_10;
        end
        test_fsm_10: begin
          ch_empty <= 0;
          ch_rdata <= 10;
          test_fsm <= test_fsm_11;
        end
        test_fsm_11: begin
          if(ch_deq) begin
            ch_empty <= 1;
          end 
          mem_rdata <= 0;
          if(ch_deq) begin
            test_fsm <= test_fsm_12;
          end 
        end
        test_fsm_12: begin
          _test_fsm_cond_12_0_1 <= mem_rvalid;
          if(ch_enq) begin
            test_fsm <= test_fsm_13;
          end 
        end
        test_fsm_13: begin
          $finish;
        end
      endcase
    end
  end


endmodule



module userlogic #
(
  parameter DATA_WIDTH = 32,
  parameter ADDR_LEN = 10
)
(
  input CLK,
  input RST,
  output reg [ADDR_LEN-1:0] mem_addr,
  output reg [DATA_WIDTH-1:0] mem_wdata,
  input [DATA_WIDTH-1:0] mem_rdata,
  output reg mem_wvalid,
  output reg mem_rvalid,
  output reg [DATA_WIDTH-1:0] ch_wdata,
  output reg ch_enq,
  input ch_almfull,
  input [DATA_WIDTH-1:0] ch_rdata,
  output reg ch_deq,
  input ch_empty
);

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] read_count;
  reg [32-1:0] sum;
  reg [32-1:0] size;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_2_0_1;
  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_2_1_1;
  reg _fsm_cond_2_1_2;
  reg _fsm_cond_4_2_1;
  reg _fsm_cond_4_3_1;
  reg _fsm_cond_4_3_2;
  reg [32-1:0] _d3_fsm;
  reg _fsm_cond_4_4_1;
  reg _fsm_cond_4_4_2;
  reg _fsm_cond_4_4_3;
  reg _fsm_cond_6_5_1;
  reg _fsm_cond_6_5_2;
  reg _fsm_cond_6_6_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;
  localparam fsm_6 = 6;

  always @(posedge CLK) begin
    if(RST) begin
      mem_addr <= 0;
      mem_wdata <= 0;
      mem_wvalid <= 0;
      mem_rvalid <= 0;
      ch_wdata <= 0;
      ch_enq <= 0;
      ch_deq <= 0;
      fsm <= fsm_init;
      read_count <= 0;
      sum <= 0;
      size <= 0;
      _d1_fsm <= fsm_init;
      _fsm_cond_2_0_1 <= 0;
      _d2_fsm <= fsm_init;
      _fsm_cond_2_1_1 <= 0;
      _fsm_cond_2_1_2 <= 0;
      _fsm_cond_4_2_1 <= 0;
      _fsm_cond_4_3_1 <= 0;
      _fsm_cond_4_3_2 <= 0;
      _d3_fsm <= fsm_init;
      _fsm_cond_4_4_1 <= 0;
      _fsm_cond_4_4_2 <= 0;
      _fsm_cond_4_4_3 <= 0;
      _fsm_cond_6_5_1 <= 0;
      _fsm_cond_6_5_2 <= 0;
      _fsm_cond_6_6_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      _d3_fsm <= _d2_fsm;
      case(_d3_fsm)
        fsm_4: begin
          if(_fsm_cond_4_4_3) begin
            sum <= sum + mem_rdata;
          end 
        end
      endcase
      case(_d2_fsm)
        fsm_2: begin
          if(_fsm_cond_2_1_2) begin
            size <= ch_rdata;
          end 
        end
        fsm_4: begin
          if(_fsm_cond_4_3_2) begin
            sum <= sum + mem_rdata;
          end 
          _fsm_cond_4_4_3 <= _fsm_cond_4_4_2;
        end
        fsm_6: begin
          if(_fsm_cond_6_5_2) begin
            $display("sum=%d", sum);
          end 
        end
      endcase
      case(_d1_fsm)
        fsm_2: begin
          if(_fsm_cond_2_0_1) begin
            ch_deq <= 0;
          end 
          _fsm_cond_2_1_2 <= _fsm_cond_2_1_1;
        end
        fsm_4: begin
          if(_fsm_cond_4_2_1) begin
            mem_rvalid <= 0;
          end 
          _fsm_cond_4_3_2 <= _fsm_cond_4_3_1;
          _fsm_cond_4_4_2 <= _fsm_cond_4_4_1;
        end
        fsm_6: begin
          _fsm_cond_6_5_2 <= _fsm_cond_6_5_1;
          if(_fsm_cond_6_6_1) begin
            ch_enq <= 0;
          end 
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
          _fsm_cond_2_0_1 <= 1;
          _fsm_cond_2_1_1 <= 1;
          if(!ch_empty) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          mem_addr <= -1;
          fsm <= fsm_4;
        end
        fsm_4: begin
          mem_rvalid <= 1;
          mem_addr <= mem_addr + 1;
          read_count <= read_count + 1;
          _fsm_cond_4_2_1 <= 1;
          _fsm_cond_4_3_1 <= 1;
          _fsm_cond_4_4_1 <= 1;
          if(read_count == size - 1) begin
            fsm <= fsm_5;
          end 
        end
        fsm_5: begin
          fsm <= fsm_6;
        end
        fsm_6: begin
          _fsm_cond_6_5_1 <= 1;
          if(!ch_almfull) begin
            ch_enq <= 1;
          end 
          _fsm_cond_6_6_1 <= 1;
          ch_wdata <= sum;
          fsm <= fsm_2;
        end
      endcase
    end
  end


endmodule
"""

def test():
    veriloggen.reset()
    test_module = simulation_pycoram_userlogic.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
