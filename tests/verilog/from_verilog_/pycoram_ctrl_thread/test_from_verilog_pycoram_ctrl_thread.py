from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import from_verilog_pycoram_ctrl_thread

expected_verilog = """
module ctrl_thread
(
  input CLK,
  input RST,
  output reg finish,
  output reg [63:0] corammemory_0_ext_addr,
  output reg [63:0] corammemory_0_core_addr,
  output reg corammemory_0_read_enable,
  output reg corammemory_0_write_enable,
  output reg [64:0] corammemory_0_word_size,
  input corammemory_0_ready,
  input corammemory_0_busy,
  input [31:0] coramchannel_0_q,
  output reg coramchannel_0_deq,
  input coramchannel_0_empty,
  output reg [31:0] coramchannel_0_d,
  output reg coramchannel_0_enq,
  input coramchannel_0_almost_full
);

  reg [63:0] __s0_ram;
  reg [63:0] __s0_channel;
  reg [63:0] __s0_addr;
  reg [63:0] __s0_sum;
  reg [63:0] __s0_i;
  reg [63:0] __s0_s1_tmp0;
  reg [5:0] state;

  always @(posedge CLK) begin
    if((RST == 1)) begin
      state <= 0;
    end else begin
      case(state)
      0: begin
        state <= 1;
      end
      1: begin
        state <= 2;
      end
      2: begin
        state <= 3;
      end
      3: begin
        state <= 4;
      end
      4: begin
        if((__s0_i < 8)) begin
          state <= 5; 
        end else begin 
          state <= 17;
        end
      end
      5: begin
        if((corammemory_0_ready == 1)) begin
          state <= 6;
        end else begin
          state <= 5;
        end
      end
      6: begin
        if((corammemory_0_busy == 1)) begin
          state <= 7; 
        end else begin
          state <= 6;
        end
      end
      7: begin
        if((corammemory_0_busy == 0)) begin
          state <= 8; 
        end else begin
          state <= 7;
        end
      end
      8: begin
        if((coramchannel_0_almost_full == 0)) begin
          state <= 9; 
        end else begin
          state <= 8;
        end
      end
      9: begin
        if((coramchannel_0_empty == 0)) begin
          state <= 10;
        end else begin
          state <= 9;
        end
      end
      10: begin
        if((coramchannel_0_empty == 0)) begin
          state <= 11; 
        end else begin
          state <= 10;
        end
      end
      11: begin
        state <= 12;
      end
      12: begin
        if((corammemory_0_ready == 1)) begin
          state <= 13; 
        end else begin
          state <= 12;
        end
      end
      13: begin
        if((corammemory_0_busy == 1)) begin
          state <= 14; 
        end else begin
          state <= 13;
        end
      end
      14: begin
        if((corammemory_0_busy == 0)) begin
          state <= 15; 
        end else begin
          state <= 14;
        end
      end
      15: begin
        state <= 16;
      end
      16: begin
        state <= 4;
      end
      17: begin
        state <= 18;
      end
      18: begin
        state <= 19;
      end
    endcase
    end
  end


  always @(posedge CLK) begin
    case(state)
      0: begin
        finish <= 0;
        corammemory_0_read_enable <= 0;
        corammemory_0_write_enable <= 0;
        coramchannel_0_enq <= 0;
        coramchannel_0_deq <= 0;
      end
      1: begin
        __s0_addr <= 0;
      end
      2: begin
        __s0_sum <= 0;
      end
      3: begin
        __s0_i <= 0;
      end
      5: begin
        corammemory_0_ext_addr <= __s0_addr;
        corammemory_0_core_addr <= 0;
        corammemory_0_word_size <= 128;
        if((corammemory_0_ready == 1)) begin
          corammemory_0_write_enable <= 1; 
        end
        if((corammemory_0_ready == 1)) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 write issue size:%d B[%d]<-D[%d]", $stime, 128, 0, __s0_addr); 
        end
        if(((corammemory_0_ready == 1) && (128 > 1024))) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 too large request size:%d > capacity:%d", $stime, 128, 1024); 
        end
        if(((corammemory_0_ready == 1) && ((0 + 128) > 1024))) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 illegal local address capacity:%d B[%d:%d]", $stime, 1024, 0, ((0 + 128) - 1)); 
        end
      end
      6: begin
        corammemory_0_write_enable <= 0;
      end
      7: begin
        if((corammemory_0_busy == 0)) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 write done size:%d B[%d]<-D[%d]", $stime, 128, 0, __s0_addr); 
        end
      end
      8: begin
        coramchannel_0_d <= __s0_addr;
        coramchannel_0_enq <= (coramchannel_0_almost_full == 0);
        if((coramchannel_0_almost_full == 0)) begin
          $display("[CoRAM] time:%d thread:ctrl_thread channel:coramchannel_0 write data:%d", $stime, __s0_addr); 
        end
      end
      9: begin
        coramchannel_0_enq <= 0;
        coramchannel_0_deq <= (coramchannel_0_empty == 0);
      end
      10: begin
        __s0_s1_tmp0 <= coramchannel_0_q;
        coramchannel_0_deq <= 0;
        $display("[CoRAM] time:%d thread:ctrl_thread channel:coramchannel_0 read data:%d", $stime, coramchannel_0_q);
      end
      11: begin
        __s0_sum <= __s0_s1_tmp0;
      end
      12: begin
        corammemory_0_ext_addr <= (__s0_addr + 16384);
        corammemory_0_core_addr <= 0;
        corammemory_0_word_size <= 128;
        if((corammemory_0_ready == 1)) begin
          corammemory_0_read_enable <= 1; 
        end
        if((corammemory_0_ready == 1)) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 read issue size:%d B[%d]->D[%d]", $stime, 128, 0, (__s0_addr + 16384)); 
        end
        if(((corammemory_0_ready == 1) && (128 > 1024))) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 too large request size:%d > capacity:%d", $stime, 128, 1024); 
        end
        if(((corammemory_0_ready == 1) && ((0 + 128) > 1024))) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 illegal local address capacity:%d B[%d:%d]", $stime, 1024, 0, ((0 + 128) - 1)); 
        end
      end
      13: begin
        corammemory_0_read_enable <= 0;
      end
      14: begin
        if((corammemory_0_busy == 0)) begin
          $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 read done size:%d B[%d]->D[%d]", $stime, 128, 0, (__s0_addr + 16384)); 
        end
      end
      15: begin
        __s0_addr <= (__s0_addr + 512);
      end
      16: begin
        __s0_i <= (__s0_i + 1);
      end
      17: begin
        $display("sum= %d", __s0_sum);
      end
      18: begin
        $display("[CoRAM] time:%d thread:ctrl_thread finished", $stime);
        finish <= 1;
      end
    endcase
  end
endmodule
"""

def test():
    veriloggen.reset()
    modules = from_verilog_pycoram_ctrl_thread.mkThread()
    code = ''.join([ m.to_verilog() for m in modules.values() ])

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
