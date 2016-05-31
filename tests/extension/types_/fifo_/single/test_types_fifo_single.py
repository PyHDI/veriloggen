from __future__ import absolute_import
from __future__ import print_function
import types_fifo_single

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

  reg myfifo_enq;
  reg [32-1:0] myfifo_wdata;
  wire myfifo_full;
  wire myfifo_almost_full;
  reg myfifo_deq;
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

  reg [32-1:0] count;
  reg [32-1:0] sum;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_1_0_1;
  reg _fsm_cond_3_1_1;
  reg _tmp_0;
  reg [32-1:0] _d2_fsm;
  reg _fsm_cond_3_2_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      _d2_fsm <= fsm_init;
      count <= 0;
      myfifo_wdata <= 0;
      myfifo_enq <= 0;
      _fsm_cond_1_0_1 <= 0;
      myfifo_deq <= 0;
      _fsm_cond_3_1_1 <= 0;
      _tmp_0 <= 0;
      sum <= 0;
      _fsm_cond_3_2_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      _d2_fsm <= _d1_fsm;
      case(_d2_fsm)
        fsm_3: begin
          _tmp_0 <= 0;
        end
      endcase
      case(_d1_fsm)
        fsm_1: begin
          if(_fsm_cond_1_0_1) begin
            myfifo_enq <= 0;
          end 
        end
        fsm_3: begin
          if(_fsm_cond_3_1_1) begin
            myfifo_deq <= 0;
          end 
          _tmp_0 <= !myfifo_empty;
          if(_fsm_cond_3_2_1) begin
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
          myfifo_wdata <= count;
          if(!myfifo_full) begin
            myfifo_enq <= 1;
          end 
          _fsm_cond_1_0_1 <= !myfifo_full;
          if(!myfifo_full) begin
            count <= count + 1;
          end 
          if(!myfifo_full && (count == 9)) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          count <= 0;
          fsm <= fsm_3;
        end
        fsm_3: begin
          if(!myfifo_empty) begin
            myfifo_deq <= 1;
          end 
          _fsm_cond_3_1_1 <= !myfifo_empty;
          if(_tmp_0) begin
            sum <= sum + myfifo_rdata;
            count <= count + 1;
          end 
          _fsm_cond_3_2_1 <= _tmp_0;
          if(count == 10) begin
            fsm <= fsm_4;
          end 
        end
      endcase
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

  reg [32-1:0] mem [0:16384-1];
  reg [14-1:0] head;
  reg [14-1:0] tail;
  wire is_empty;
  wire is_almost_empty;
  wire is_full;
  wire is_almost_full;
  assign is_empty = head == tail;
  assign is_almost_empty = head == (tail + 1 & 16383);
  assign is_full = (head + 1 & 16383) == tail;
  assign is_almost_full = (head + 2 & 16383) == tail;
  reg [32-1:0] rdata_reg;
  assign myfifo_full = is_full;
  assign myfifo_almost_full = is_almost_full;
  assign myfifo_empty = is_empty;
  assign myfifo_almost_empty = is_almost_empty;
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
    test_module = types_fifo_single.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
