

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
    end else case(state)
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
        if((__s0_i < 8)) state <= 5; 
        else state <= 17;
      end
      5: begin
        if((corammemory_0_ready == 1)) state <= 6; 
        else state <= 5;
      end
      6: begin
        if((corammemory_0_busy == 1)) state <= 7; 
        else state <= 6;
      end
      7: begin
        if((corammemory_0_busy == 0)) state <= 8; 
        else state <= 7;
      end
      8: begin
        if((coramchannel_0_almost_full == 0)) state <= 9; 
        else state <= 8;
      end
      9: begin
        if((coramchannel_0_empty == 0)) state <= 10; 
        else state <= 9;
      end
      10: begin
        if((coramchannel_0_empty == 0)) state <= 11; 
        else state <= 10;
      end
      11: begin
        state <= 12;
      end
      12: begin
        if((corammemory_0_ready == 1)) state <= 13; 
        else state <= 12;
      end
      13: begin
        if((corammemory_0_busy == 1)) state <= 14; 
        else state <= 13;
      end
      14: begin
        if((corammemory_0_busy == 0)) state <= 15; 
        else state <= 14;
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
        if((corammemory_0_ready == 1)) corammemory_0_write_enable <= 1; 
        if((corammemory_0_ready == 1)) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 write issue size:%d B[%d]<-D[%d]", $stime, 128, 0, __s0_addr); 
        if(((corammemory_0_ready == 1) && (128 > 1024))) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 too large request size:%d > capacity:%d", $stime, 128, 1024); 
        if(((corammemory_0_ready == 1) && ((0 + 128) > 1024))) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 illegal local address capacity:%d B[%d:%d]", $stime, 1024, 0, ((0 + 128) - 1)); 
      end
      6: begin
        corammemory_0_write_enable <= 0;
      end
      7: begin
        if((corammemory_0_busy == 0)) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 write done size:%d B[%d]<-D[%d]", $stime, 128, 0, __s0_addr); 
      end
      8: begin
        coramchannel_0_d <= __s0_addr;
        coramchannel_0_enq <= (coramchannel_0_almost_full == 0);
        if((coramchannel_0_almost_full == 0)) $display("[CoRAM] time:%d thread:ctrl_thread channel:coramchannel_0 write data:%d", $stime, __s0_addr); 
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
        if((corammemory_0_ready == 1)) corammemory_0_read_enable <= 1; 
        if((corammemory_0_ready == 1)) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 read issue size:%d B[%d]->D[%d]", $stime, 128, 0, (__s0_addr + 16384)); 
        if(((corammemory_0_ready == 1) && (128 > 1024))) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 too large request size:%d > capacity:%d", $stime, 128, 1024); 
        if(((corammemory_0_ready == 1) && ((0 + 128) > 1024))) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 illegal local address capacity:%d B[%d:%d]", $stime, 1024, 0, ((0 + 128) - 1)); 
      end
      13: begin
        corammemory_0_read_enable <= 0;
      end
      14: begin
        if((corammemory_0_busy == 0)) $display("[CoRAM] time:%d thread:ctrl_thread memory:corammemory_0 read done size:%d B[%d]->D[%d]", $stime, 128, 0, (__s0_addr + 16384)); 
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

