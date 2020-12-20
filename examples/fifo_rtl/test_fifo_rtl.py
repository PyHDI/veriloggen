from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import fifo_rtl

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

  wire myfifo_enq;
  wire [32-1:0] myfifo_wdata;
  wire myfifo_full;
  wire myfifo_almost_full;
  wire myfifo_deq;
  wire [32-1:0] myfifo_rdata;
  wire myfifo_empty;
  wire myfifo_almost_empty;

  myfifo
  inst_myfifo
  (
    .CLK(CLK),
    .RST(RST),
    .myfifo_enq(myfifo_enq),
    .myfifo_wdata(myfifo_wdata),
    .myfifo_full(myfifo_full),
    .myfifo_almost_full(myfifo_almost_full),
    .myfifo_deq(myfifo_deq),
    .myfifo_rdata(myfifo_rdata),
    .myfifo_empty(myfifo_empty),
    .myfifo_almost_empty(myfifo_almost_empty)
  );

  reg [8-1:0] count_myfifo;
  reg [32-1:0] count;
  reg [32-1:0] sum;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  assign myfifo_wdata = (fsm == 1)? count : 'hx;
  assign myfifo_enq = (fsm == 1)? (fsm == 1) && !myfifo_almost_full : 0;
  localparam _tmp_0 = 1;
  wire [_tmp_0-1:0] _tmp_1;
  assign _tmp_1 = !myfifo_almost_full;
  reg [_tmp_0-1:0] __tmp_1_1;
  assign myfifo_deq = ((fsm == 3) && !myfifo_empty)? 1 : 0;
  localparam _tmp_2 = 1;
  wire [_tmp_2-1:0] _tmp_3;
  assign _tmp_3 = (fsm == 3) && !myfifo_empty;
  reg [_tmp_2-1:0] __tmp_3_1;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_3_0_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      count <= 0;
      sum <= 0;
      _fsm_cond_3_0_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_3: begin
          if(_fsm_cond_3_0_1) begin
            $display("sum=%d", sum);
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          count <= 0;
          fsm <= fsm_1;
        end
        fsm_1: begin
          if(!myfifo_almost_full) begin
            count <= count + 1;
          end 
          if(__tmp_1_1) begin
            $display("count=%d space=%d has_space=%d", count_myfifo, (127 - count_myfifo), (count_myfifo + 1 < 127));
          end 
          if(!myfifo_almost_full && (count == 125)) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          count <= 0;
          fsm <= fsm_3;
        end
        fsm_3: begin
          if(__tmp_3_1) begin
            sum <= sum + myfifo_rdata;
            count <= count + 1;
            $write("count=%d space=%d has_space=%d ", count_myfifo, (127 - count_myfifo), (count_myfifo + 1 < 127));
          end 
          _fsm_cond_3_0_1 <= __tmp_3_1;
          if(count == 126) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          $display("expected_sum=%d", 7875);
          fsm <= fsm_5;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      count_myfifo <= 0;
      __tmp_1_1 <= 0;
      __tmp_3_1 <= 0;
    end else begin
      if(myfifo_enq && !myfifo_full && (myfifo_deq && !myfifo_empty)) begin
        count_myfifo <= count_myfifo;
      end else if(myfifo_enq && !myfifo_full) begin
        count_myfifo <= count_myfifo + 1;
      end else if(myfifo_deq && !myfifo_empty) begin
        count_myfifo <= count_myfifo - 1;
      end 
      __tmp_1_1 <= _tmp_1;
      __tmp_3_1 <= _tmp_3;
    end
  end


endmodule



module myfifo
(
  input CLK,
  input RST,
  input myfifo_enq,
  input [32-1:0] myfifo_wdata,
  output myfifo_full,
  output myfifo_almost_full,
  input myfifo_deq,
  output [32-1:0] myfifo_rdata,
  output myfifo_empty,
  output myfifo_almost_empty
);

  reg [32-1:0] mem [0:128-1];
  reg [7-1:0] head;
  reg [7-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 127);
  assign is_full = (head + 1 & 127) == tail;
  assign is_almost_full = (head + 2 & 127) == tail;
  reg [32-1:0] rdata_reg;
  assign myfifo_full = is_full;
  assign myfifo_almost_full = is_almost_full || is_full;
  assign myfifo_empty = is_empty;
  assign myfifo_almost_empty = is_almost_empty || is_empty;
  assign myfifo_rdata = rdata_reg;

  always @(posedge CLK) begin
    if(RST) begin
      head <= 0;
      rdata_reg <= 0;
      tail <= 0;
    end else begin
      if(myfifo_enq && !is_full) begin
        mem[head] <= myfifo_wdata;
        head <= head + 1;
      end 
      if(myfifo_deq && !is_empty) begin
        rdata_reg <= mem[tail];
        tail <= tail + 1;
      end 
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = fifo_rtl.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
