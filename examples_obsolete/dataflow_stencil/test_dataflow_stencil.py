from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_stencil

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg start;
  wire busy;
  reg [4-1:0] ext_src_ram0_addr;
  wire [32-1:0] ext_src_ram0_rdata;
  reg [32-1:0] ext_src_ram0_wdata;
  reg ext_src_ram0_wenable;
  reg [4-1:0] ext_src_ram1_addr;
  wire [32-1:0] ext_src_ram1_rdata;
  reg [32-1:0] ext_src_ram1_wdata;
  reg ext_src_ram1_wenable;
  reg [4-1:0] ext_src_ram2_addr;
  wire [32-1:0] ext_src_ram2_rdata;
  reg [32-1:0] ext_src_ram2_wdata;
  reg ext_src_ram2_wenable;
  reg [4-1:0] ext_dst_ram_addr;
  wire [32-1:0] ext_dst_ram_rdata;
  reg [32-1:0] ext_dst_ram_wdata;
  reg ext_dst_ram_wenable;

  stencil
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .start(start),
    .busy(busy),
    .ext_src_ram0_addr(ext_src_ram0_addr),
    .ext_src_ram0_rdata(ext_src_ram0_rdata),
    .ext_src_ram0_wdata(ext_src_ram0_wdata),
    .ext_src_ram0_wenable(ext_src_ram0_wenable),
    .ext_src_ram1_addr(ext_src_ram1_addr),
    .ext_src_ram1_rdata(ext_src_ram1_rdata),
    .ext_src_ram1_wdata(ext_src_ram1_wdata),
    .ext_src_ram1_wenable(ext_src_ram1_wenable),
    .ext_src_ram2_addr(ext_src_ram2_addr),
    .ext_src_ram2_rdata(ext_src_ram2_rdata),
    .ext_src_ram2_wdata(ext_src_ram2_wdata),
    .ext_src_ram2_wenable(ext_src_ram2_wenable),
    .ext_dst_ram_addr(ext_dst_ram_addr),
    .ext_dst_ram_rdata(ext_dst_ram_rdata),
    .ext_dst_ram_wdata(ext_dst_ram_wdata),
    .ext_dst_ram_wenable(ext_dst_ram_wenable)
  );

  reg reset_done;

  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    reset_done = 0;
    start = 0;
    ext_src_ram0_addr = 0;
    ext_src_ram0_wdata = 0;
    ext_src_ram0_wenable = 0;
    ext_src_ram1_addr = 0;
    ext_src_ram1_wdata = 0;
    ext_src_ram1_wenable = 0;
    ext_src_ram2_addr = 0;
    ext_src_ram2_wdata = 0;
    ext_src_ram2_wenable = 0;
    ext_dst_ram_addr = 2;
    ext_dst_ram_wdata = 0;
    ext_dst_ram_wenable = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #100000;
    $finish;
  end

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_4_0_1;
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
      _fsm_cond_4_0_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_4: begin
          if(_fsm_cond_4_0_1) begin
            start <= 0;
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          if(reset_done) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          ext_src_ram0_addr <= -1;
          ext_src_ram1_addr <= -1;
          ext_src_ram2_addr <= -1;
          fsm <= fsm_2;
        end
        fsm_2: begin
          ext_src_ram0_addr <= ext_src_ram0_addr + 1;
          ext_src_ram0_wdata <= 'sd5898240;
          ext_src_ram0_wenable <= 1;
          if(ext_src_ram0_wenable && (ext_src_ram0_addr == 15)) begin
            ext_src_ram0_wenable <= 0;
          end 
          ext_src_ram1_addr <= ext_src_ram1_addr + 1;
          ext_src_ram1_wdata <= 'sd5898240;
          ext_src_ram1_wenable <= 1;
          if(ext_src_ram1_wenable && (ext_src_ram1_addr == 15)) begin
            ext_src_ram1_wenable <= 0;
          end 
          ext_src_ram2_addr <= ext_src_ram2_addr + 1;
          ext_src_ram2_wdata <= 'sd5898240;
          ext_src_ram2_wenable <= 1;
          if(ext_src_ram2_wenable && (ext_src_ram2_addr == 15)) begin
            ext_src_ram2_wenable <= 0;
          end 
          if(ext_src_ram2_wenable && (ext_src_ram0_addr == 15)) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(!busy) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          start <= 1;
          _fsm_cond_4_0_1 <= 1;
          fsm <= fsm_5;
        end
        fsm_5: begin
          if(busy) begin
            fsm <= fsm_6;
          end 
        end
        fsm_6: begin
          if(!busy) begin
            fsm <= fsm_7;
          end 
        end
        fsm_7: begin
          $finish;
        end
      endcase
    end
  end


endmodule



module stencil
(
  input CLK,
  input RST,
  input start,
  output reg busy,
  input [4-1:0] ext_src_ram0_addr,
  output [32-1:0] ext_src_ram0_rdata,
  input [32-1:0] ext_src_ram0_wdata,
  input ext_src_ram0_wenable,
  input [4-1:0] ext_src_ram1_addr,
  output [32-1:0] ext_src_ram1_rdata,
  input [32-1:0] ext_src_ram1_wdata,
  input ext_src_ram1_wenable,
  input [4-1:0] ext_src_ram2_addr,
  output [32-1:0] ext_src_ram2_rdata,
  input [32-1:0] ext_src_ram2_wdata,
  input ext_src_ram2_wenable,
  input [4-1:0] ext_dst_ram_addr,
  output [32-1:0] ext_dst_ram_rdata,
  input [32-1:0] ext_dst_ram_wdata,
  input ext_dst_ram_wenable
);

  reg _tmp_0;
  wire [8-1:0] src_ram0_0_addr;
  wire [32-1:0] src_ram0_0_rdata;
  wire [32-1:0] src_ram0_0_wdata;
  wire src_ram0_0_wenable;
  wire src_ram0_0_enable;
  wire [8-1:0] src_ram0_1_addr;
  wire [32-1:0] src_ram0_1_rdata;
  wire [32-1:0] src_ram0_1_wdata;
  wire src_ram0_1_wenable;
  wire src_ram0_1_enable;
  assign src_ram0_0_wdata = 'hx;
  assign src_ram0_0_wenable = 0;

  src_ram0
  inst_src_ram0
  (
    .CLK(CLK),
    .src_ram0_0_addr(src_ram0_0_addr),
    .src_ram0_0_rdata(src_ram0_0_rdata),
    .src_ram0_0_wdata(src_ram0_0_wdata),
    .src_ram0_0_wenable(src_ram0_0_wenable),
    .src_ram0_0_enable(src_ram0_0_enable),
    .src_ram0_1_addr(src_ram0_1_addr),
    .src_ram0_1_rdata(src_ram0_1_rdata),
    .src_ram0_1_wdata(src_ram0_1_wdata),
    .src_ram0_1_wenable(src_ram0_1_wenable),
    .src_ram0_1_enable(src_ram0_1_enable)
  );

  wire [8-1:0] src_ram1_0_addr;
  wire [32-1:0] src_ram1_0_rdata;
  wire [32-1:0] src_ram1_0_wdata;
  wire src_ram1_0_wenable;
  wire src_ram1_0_enable;
  wire [8-1:0] src_ram1_1_addr;
  wire [32-1:0] src_ram1_1_rdata;
  wire [32-1:0] src_ram1_1_wdata;
  wire src_ram1_1_wenable;
  wire src_ram1_1_enable;
  assign src_ram1_0_wdata = 'hx;
  assign src_ram1_0_wenable = 0;

  src_ram1
  inst_src_ram1
  (
    .CLK(CLK),
    .src_ram1_0_addr(src_ram1_0_addr),
    .src_ram1_0_rdata(src_ram1_0_rdata),
    .src_ram1_0_wdata(src_ram1_0_wdata),
    .src_ram1_0_wenable(src_ram1_0_wenable),
    .src_ram1_0_enable(src_ram1_0_enable),
    .src_ram1_1_addr(src_ram1_1_addr),
    .src_ram1_1_rdata(src_ram1_1_rdata),
    .src_ram1_1_wdata(src_ram1_1_wdata),
    .src_ram1_1_wenable(src_ram1_1_wenable),
    .src_ram1_1_enable(src_ram1_1_enable)
  );

  wire [8-1:0] src_ram2_0_addr;
  wire [32-1:0] src_ram2_0_rdata;
  wire [32-1:0] src_ram2_0_wdata;
  wire src_ram2_0_wenable;
  wire src_ram2_0_enable;
  wire [8-1:0] src_ram2_1_addr;
  wire [32-1:0] src_ram2_1_rdata;
  wire [32-1:0] src_ram2_1_wdata;
  wire src_ram2_1_wenable;
  wire src_ram2_1_enable;
  assign src_ram2_0_wdata = 'hx;
  assign src_ram2_0_wenable = 0;

  src_ram2
  inst_src_ram2
  (
    .CLK(CLK),
    .src_ram2_0_addr(src_ram2_0_addr),
    .src_ram2_0_rdata(src_ram2_0_rdata),
    .src_ram2_0_wdata(src_ram2_0_wdata),
    .src_ram2_0_wenable(src_ram2_0_wenable),
    .src_ram2_0_enable(src_ram2_0_enable),
    .src_ram2_1_addr(src_ram2_1_addr),
    .src_ram2_1_rdata(src_ram2_1_rdata),
    .src_ram2_1_wdata(src_ram2_1_wdata),
    .src_ram2_1_wenable(src_ram2_1_wenable),
    .src_ram2_1_enable(src_ram2_1_enable)
  );

  wire [8-1:0] dst_ram_0_addr;
  wire [32-1:0] dst_ram_0_rdata;
  wire [32-1:0] dst_ram_0_wdata;
  wire dst_ram_0_wenable;
  wire dst_ram_0_enable;
  wire [8-1:0] dst_ram_1_addr;
  wire [32-1:0] dst_ram_1_rdata;
  wire [32-1:0] dst_ram_1_wdata;
  wire dst_ram_1_wenable;
  wire dst_ram_1_enable;

  dst_ram
  inst_dst_ram
  (
    .CLK(CLK),
    .dst_ram_0_addr(dst_ram_0_addr),
    .dst_ram_0_rdata(dst_ram_0_rdata),
    .dst_ram_0_wdata(dst_ram_0_wdata),
    .dst_ram_0_wenable(dst_ram_0_wenable),
    .dst_ram_0_enable(dst_ram_0_enable),
    .dst_ram_1_addr(dst_ram_1_addr),
    .dst_ram_1_rdata(dst_ram_1_rdata),
    .dst_ram_1_wdata(dst_ram_1_wdata),
    .dst_ram_1_wenable(dst_ram_1_wenable),
    .dst_ram_1_enable(dst_ram_1_enable)
  );

  assign src_ram0_1_addr = ext_src_ram0_addr;
  assign ext_src_ram0_rdata = src_ram0_1_rdata;
  assign src_ram0_1_wdata = ext_src_ram0_wdata;
  assign src_ram0_1_wenable = ext_src_ram0_wenable;
  assign src_ram0_1_enable = 1;
  assign src_ram1_1_addr = ext_src_ram1_addr;
  assign ext_src_ram1_rdata = src_ram1_1_rdata;
  assign src_ram1_1_wdata = ext_src_ram1_wdata;
  assign src_ram1_1_wenable = ext_src_ram1_wenable;
  assign src_ram1_1_enable = 1;
  assign src_ram2_1_addr = ext_src_ram2_addr;
  assign ext_src_ram2_rdata = src_ram2_1_rdata;
  assign src_ram2_1_wdata = ext_src_ram2_wdata;
  assign src_ram2_1_wenable = ext_src_ram2_wenable;
  assign src_ram2_1_enable = 1;
  assign dst_ram_1_addr = ext_dst_ram_addr;
  assign ext_dst_ram_rdata = dst_ram_1_rdata;
  assign dst_ram_1_wdata = ext_dst_ram_wdata;
  assign dst_ram_1_wenable = ext_dst_ram_wenable;
  assign dst_ram_1_enable = 1;
  reg [32-1:0] read_fsm;
  localparam read_fsm_init = 0;
  reg [32-1:0] read_count;
  reg [32-1:0] read_addr;
  assign src_ram0_0_addr = (read_fsm == 1)? read_addr : 'hx;
  assign src_ram0_0_enable = (read_fsm == 1)? 1'd1 : 0;
  localparam _tmp_1 = 1;
  wire [_tmp_1-1:0] _tmp_2;
  assign _tmp_2 = read_fsm == 1;
  reg [_tmp_1-1:0] __tmp_2_1;
  assign src_ram1_0_addr = (read_fsm == 1)? read_addr : 'hx;
  assign src_ram1_0_enable = (read_fsm == 1)? 1'd1 : 0;
  localparam _tmp_3 = 1;
  wire [_tmp_3-1:0] _tmp_4;
  assign _tmp_4 = read_fsm == 1;
  reg [_tmp_3-1:0] __tmp_4_1;
  assign src_ram2_0_addr = (read_fsm == 1)? read_addr : 'hx;
  assign src_ram2_0_enable = (read_fsm == 1)? 1'd1 : 0;
  localparam _tmp_5 = 1;
  wire [_tmp_5-1:0] _tmp_6;
  assign _tmp_6 = read_fsm == 1;
  reg [_tmp_5-1:0] __tmp_6_1;
  localparam read_fsm_1 = 1;
  localparam read_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      read_fsm <= read_fsm_init;
      read_addr <= 0;
      read_count <= 0;
      busy <= 0;
    end else begin
      case(read_fsm)
        read_fsm_init: begin
          read_addr <= 0;
          read_count <= 0;
          busy <= 0;
          if(start) begin
            busy <= 1;
          end 
          if(start) begin
            read_fsm <= read_fsm_1;
          end 
        end
        read_fsm_1: begin
          read_addr <= read_addr + 1;
          read_count <= read_count + 1;
          if(read_count == 15) begin
            read_addr <= 0;
            read_count <= 0;
          end 
          if(read_count == 15) begin
            read_fsm <= read_fsm_2;
          end 
        end
        read_fsm_2: begin
          if(_tmp_0) begin
            busy <= 0;
          end 
          if(_tmp_0) begin
            read_fsm <= read_fsm_init;
          end 
        end
      endcase
    end
  end

  wire [32-1:0] odata;
  wire ovalid;

  stencil_pipeline_2d
  inst_stencil
  (
    .CLK(CLK),
    .RST(RST),
    .idata0(src_ram0_0_rdata),
    .ivalid0(__tmp_2_1),
    .idata1(src_ram1_0_rdata),
    .ivalid1(__tmp_4_1),
    .idata2(src_ram2_0_rdata),
    .ivalid2(__tmp_6_1),
    .odata(odata),
    .ovalid(ovalid)
  );

  reg [32-1:0] write_fsm;
  localparam write_fsm_init = 0;
  reg [32-1:0] write_count;
  reg [32-1:0] write_addr;
  assign dst_ram_0_addr = ((write_fsm == 0) && (ovalid && (write_count > 1)))? write_addr : 'hx;
  assign dst_ram_0_wdata = ((write_fsm == 0) && (ovalid && (write_count > 1)))? odata : 'hx;
  assign dst_ram_0_wenable = ((write_fsm == 0) && (ovalid && (write_count > 1)))? 1'd1 : 0;
  assign dst_ram_0_enable = ((write_fsm == 0) && (ovalid && (write_count > 1)))? 1'd1 : 0;

  always @(posedge CLK) begin
    if(RST) begin
      write_fsm <= write_fsm_init;
      _tmp_0 <= 0;
      write_addr <= 1;
      write_count <= 0;
    end else begin
      case(write_fsm)
        write_fsm_init: begin
          _tmp_0 <= 0;
          if(ovalid && (write_count > 1)) begin
            write_addr <= write_addr + 1;
          end 
          if(ovalid) begin
            write_count <= write_count + 1;
          end 
          if(write_count == 16) begin
            write_count <= 0;
            write_addr <= 1;
            _tmp_0 <= 1;
          end 
          if(write_count == 16) begin
            write_fsm <= write_fsm_init;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_2_1 <= 0;
    end else begin
      __tmp_2_1 <= _tmp_2;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_4_1 <= 0;
    end else begin
      __tmp_4_1 <= _tmp_4;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      __tmp_6_1 <= 0;
    end else begin
      __tmp_6_1 <= _tmp_6;
    end
  end


endmodule



module src_ram0
(
  input CLK,
  input [8-1:0] src_ram0_0_addr,
  output [32-1:0] src_ram0_0_rdata,
  input [32-1:0] src_ram0_0_wdata,
  input src_ram0_0_wenable,
  input src_ram0_0_enable,
  input [8-1:0] src_ram0_1_addr,
  output [32-1:0] src_ram0_1_rdata,
  input [32-1:0] src_ram0_1_wdata,
  input src_ram0_1_wenable,
  input src_ram0_1_enable
);

  reg [32-1:0] src_ram0_0_rdata_out;
  assign src_ram0_0_rdata = src_ram0_0_rdata_out;
  reg [32-1:0] src_ram0_1_rdata_out;
  assign src_ram0_1_rdata = src_ram0_1_rdata_out;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(src_ram0_0_enable) begin
      if(src_ram0_0_wenable) begin
        mem[src_ram0_0_addr] <= src_ram0_0_wdata;
        src_ram0_0_rdata_out <= src_ram0_0_wdata;
      end else begin
        src_ram0_0_rdata_out <= mem[src_ram0_0_addr];
      end
    end 
  end


  always @(posedge CLK) begin
    if(src_ram0_1_enable) begin
      if(src_ram0_1_wenable) begin
        mem[src_ram0_1_addr] <= src_ram0_1_wdata;
        src_ram0_1_rdata_out <= src_ram0_1_wdata;
      end else begin
        src_ram0_1_rdata_out <= mem[src_ram0_1_addr];
      end
    end 
  end


endmodule



module src_ram1
(
  input CLK,
  input [8-1:0] src_ram1_0_addr,
  output [32-1:0] src_ram1_0_rdata,
  input [32-1:0] src_ram1_0_wdata,
  input src_ram1_0_wenable,
  input src_ram1_0_enable,
  input [8-1:0] src_ram1_1_addr,
  output [32-1:0] src_ram1_1_rdata,
  input [32-1:0] src_ram1_1_wdata,
  input src_ram1_1_wenable,
  input src_ram1_1_enable
);

  reg [32-1:0] src_ram1_0_rdata_out;
  assign src_ram1_0_rdata = src_ram1_0_rdata_out;
  reg [32-1:0] src_ram1_1_rdata_out;
  assign src_ram1_1_rdata = src_ram1_1_rdata_out;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(src_ram1_0_enable) begin
      if(src_ram1_0_wenable) begin
        mem[src_ram1_0_addr] <= src_ram1_0_wdata;
        src_ram1_0_rdata_out <= src_ram1_0_wdata;
      end else begin
        src_ram1_0_rdata_out <= mem[src_ram1_0_addr];
      end
    end 
  end


  always @(posedge CLK) begin
    if(src_ram1_1_enable) begin
      if(src_ram1_1_wenable) begin
        mem[src_ram1_1_addr] <= src_ram1_1_wdata;
        src_ram1_1_rdata_out <= src_ram1_1_wdata;
      end else begin
        src_ram1_1_rdata_out <= mem[src_ram1_1_addr];
      end
    end 
  end


endmodule



module src_ram2
(
  input CLK,
  input [8-1:0] src_ram2_0_addr,
  output [32-1:0] src_ram2_0_rdata,
  input [32-1:0] src_ram2_0_wdata,
  input src_ram2_0_wenable,
  input src_ram2_0_enable,
  input [8-1:0] src_ram2_1_addr,
  output [32-1:0] src_ram2_1_rdata,
  input [32-1:0] src_ram2_1_wdata,
  input src_ram2_1_wenable,
  input src_ram2_1_enable
);

  reg [32-1:0] src_ram2_0_rdata_out;
  assign src_ram2_0_rdata = src_ram2_0_rdata_out;
  reg [32-1:0] src_ram2_1_rdata_out;
  assign src_ram2_1_rdata = src_ram2_1_rdata_out;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(src_ram2_0_enable) begin
      if(src_ram2_0_wenable) begin
        mem[src_ram2_0_addr] <= src_ram2_0_wdata;
        src_ram2_0_rdata_out <= src_ram2_0_wdata;
      end else begin
        src_ram2_0_rdata_out <= mem[src_ram2_0_addr];
      end
    end 
  end


  always @(posedge CLK) begin
    if(src_ram2_1_enable) begin
      if(src_ram2_1_wenable) begin
        mem[src_ram2_1_addr] <= src_ram2_1_wdata;
        src_ram2_1_rdata_out <= src_ram2_1_wdata;
      end else begin
        src_ram2_1_rdata_out <= mem[src_ram2_1_addr];
      end
    end 
  end


endmodule



module dst_ram
(
  input CLK,
  input [8-1:0] dst_ram_0_addr,
  output [32-1:0] dst_ram_0_rdata,
  input [32-1:0] dst_ram_0_wdata,
  input dst_ram_0_wenable,
  input dst_ram_0_enable,
  input [8-1:0] dst_ram_1_addr,
  output [32-1:0] dst_ram_1_rdata,
  input [32-1:0] dst_ram_1_wdata,
  input dst_ram_1_wenable,
  input dst_ram_1_enable
);

  reg [32-1:0] dst_ram_0_rdata_out;
  assign dst_ram_0_rdata = dst_ram_0_rdata_out;
  reg [32-1:0] dst_ram_1_rdata_out;
  assign dst_ram_1_rdata = dst_ram_1_rdata_out;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(dst_ram_0_enable) begin
      if(dst_ram_0_wenable) begin
        mem[dst_ram_0_addr] <= dst_ram_0_wdata;
        dst_ram_0_rdata_out <= dst_ram_0_wdata;
      end else begin
        dst_ram_0_rdata_out <= mem[dst_ram_0_addr];
      end
    end 
  end


  always @(posedge CLK) begin
    if(dst_ram_1_enable) begin
      if(dst_ram_1_wenable) begin
        mem[dst_ram_1_addr] <= dst_ram_1_wdata;
        dst_ram_1_rdata_out <= dst_ram_1_wdata;
      end else begin
        dst_ram_1_rdata_out <= mem[dst_ram_1_addr];
      end
    end 
  end


endmodule



module stencil_pipeline_2d
(
  input CLK,
  input RST,
  input signed [32-1:0] idata0,
  input ivalid0,
  input signed [32-1:0] idata1,
  input ivalid1,
  input signed [32-1:0] idata2,
  input ivalid2,
  output signed [32-1:0] odata,
  output ovalid
);

  reg signed [32-1:0] _dataflow__prev_data_12;
  reg signed [32-1:0] _dataflow__prev_data_13;
  reg signed [32-1:0] _dataflow__prev_data_14;
  reg signed [32-1:0] _dataflow__prev_data_15;
  reg signed [32-1:0] _dataflow__prev_data_16;
  reg signed [32-1:0] _dataflow__prev_data_17;
  wire signed [32-1:0] _dataflow_times_data_18;
  wire _dataflow_times_valid_18;
  wire _dataflow_times_ready_18;
  wire signed [46-1:0] _dataflow_times_mul_odata_18;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_18;
  assign _dataflow_times_data_18 = _dataflow_times_mul_odata_reg_18;
  wire _dataflow_times_mul_ovalid_18;
  reg _dataflow_times_mul_valid_reg_18;
  assign _dataflow_times_valid_18 = _dataflow_times_mul_valid_reg_18;
  wire _dataflow_times_mul_enable_18;
  wire _dataflow_times_mul_update_18;
  assign _dataflow_times_mul_enable_18 = (_dataflow_times_ready_18 || !_dataflow_times_valid_18) && 1 && ivalid0;
  assign _dataflow_times_mul_update_18 = _dataflow_times_ready_18 || !_dataflow_times_valid_18;

  multiplier_0
  _dataflow_times_mul_18
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_18),
    .enable(_dataflow_times_mul_enable_18),
    .valid(_dataflow_times_mul_ovalid_18),
    .a(idata0),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_18)
  );

  wire signed [32-1:0] _dataflow_times_data_19;
  wire _dataflow_times_valid_19;
  wire _dataflow_times_ready_19;
  wire signed [46-1:0] _dataflow_times_mul_odata_19;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_19;
  assign _dataflow_times_data_19 = _dataflow_times_mul_odata_reg_19;
  wire _dataflow_times_mul_ovalid_19;
  reg _dataflow_times_mul_valid_reg_19;
  assign _dataflow_times_valid_19 = _dataflow_times_mul_valid_reg_19;
  wire _dataflow_times_mul_enable_19;
  wire _dataflow_times_mul_update_19;
  assign _dataflow_times_mul_enable_19 = (_dataflow_times_ready_19 || !_dataflow_times_valid_19) && 1 && ivalid0;
  assign _dataflow_times_mul_update_19 = _dataflow_times_ready_19 || !_dataflow_times_valid_19;

  multiplier_1
  _dataflow_times_mul_19
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_19),
    .enable(_dataflow_times_mul_enable_19),
    .valid(_dataflow_times_mul_ovalid_19),
    .a(_dataflow__prev_data_12),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_19)
  );

  wire signed [32-1:0] _dataflow_times_data_21;
  wire _dataflow_times_valid_21;
  wire _dataflow_times_ready_21;
  wire signed [46-1:0] _dataflow_times_mul_odata_21;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_21;
  assign _dataflow_times_data_21 = _dataflow_times_mul_odata_reg_21;
  wire _dataflow_times_mul_ovalid_21;
  reg _dataflow_times_mul_valid_reg_21;
  assign _dataflow_times_valid_21 = _dataflow_times_mul_valid_reg_21;
  wire _dataflow_times_mul_enable_21;
  wire _dataflow_times_mul_update_21;
  assign _dataflow_times_mul_enable_21 = (_dataflow_times_ready_21 || !_dataflow_times_valid_21) && 1 && ivalid0;
  assign _dataflow_times_mul_update_21 = _dataflow_times_ready_21 || !_dataflow_times_valid_21;

  multiplier_2
  _dataflow_times_mul_21
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_21),
    .enable(_dataflow_times_mul_enable_21),
    .valid(_dataflow_times_mul_ovalid_21),
    .a(_dataflow__prev_data_13),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_21)
  );

  wire signed [32-1:0] _dataflow_times_data_23;
  wire _dataflow_times_valid_23;
  wire _dataflow_times_ready_23;
  wire signed [46-1:0] _dataflow_times_mul_odata_23;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_23;
  assign _dataflow_times_data_23 = _dataflow_times_mul_odata_reg_23;
  wire _dataflow_times_mul_ovalid_23;
  reg _dataflow_times_mul_valid_reg_23;
  assign _dataflow_times_valid_23 = _dataflow_times_mul_valid_reg_23;
  wire _dataflow_times_mul_enable_23;
  wire _dataflow_times_mul_update_23;
  assign _dataflow_times_mul_enable_23 = (_dataflow_times_ready_23 || !_dataflow_times_valid_23) && 1 && ivalid1;
  assign _dataflow_times_mul_update_23 = _dataflow_times_ready_23 || !_dataflow_times_valid_23;

  multiplier_3
  _dataflow_times_mul_23
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_23),
    .enable(_dataflow_times_mul_enable_23),
    .valid(_dataflow_times_mul_ovalid_23),
    .a(idata1),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_23)
  );

  wire signed [32-1:0] _dataflow_times_data_25;
  wire _dataflow_times_valid_25;
  wire _dataflow_times_ready_25;
  wire signed [46-1:0] _dataflow_times_mul_odata_25;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_25;
  assign _dataflow_times_data_25 = _dataflow_times_mul_odata_reg_25;
  wire _dataflow_times_mul_ovalid_25;
  reg _dataflow_times_mul_valid_reg_25;
  assign _dataflow_times_valid_25 = _dataflow_times_mul_valid_reg_25;
  wire _dataflow_times_mul_enable_25;
  wire _dataflow_times_mul_update_25;
  assign _dataflow_times_mul_enable_25 = (_dataflow_times_ready_25 || !_dataflow_times_valid_25) && 1 && ivalid1;
  assign _dataflow_times_mul_update_25 = _dataflow_times_ready_25 || !_dataflow_times_valid_25;

  multiplier_4
  _dataflow_times_mul_25
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_25),
    .enable(_dataflow_times_mul_enable_25),
    .valid(_dataflow_times_mul_ovalid_25),
    .a(_dataflow__prev_data_14),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_25)
  );

  wire signed [32-1:0] _dataflow_times_data_27;
  wire _dataflow_times_valid_27;
  wire _dataflow_times_ready_27;
  wire signed [46-1:0] _dataflow_times_mul_odata_27;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_27;
  assign _dataflow_times_data_27 = _dataflow_times_mul_odata_reg_27;
  wire _dataflow_times_mul_ovalid_27;
  reg _dataflow_times_mul_valid_reg_27;
  assign _dataflow_times_valid_27 = _dataflow_times_mul_valid_reg_27;
  wire _dataflow_times_mul_enable_27;
  wire _dataflow_times_mul_update_27;
  assign _dataflow_times_mul_enable_27 = (_dataflow_times_ready_27 || !_dataflow_times_valid_27) && 1 && ivalid1;
  assign _dataflow_times_mul_update_27 = _dataflow_times_ready_27 || !_dataflow_times_valid_27;

  multiplier_5
  _dataflow_times_mul_27
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_27),
    .enable(_dataflow_times_mul_enable_27),
    .valid(_dataflow_times_mul_ovalid_27),
    .a(_dataflow__prev_data_15),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_27)
  );

  wire signed [32-1:0] _dataflow_times_data_29;
  wire _dataflow_times_valid_29;
  wire _dataflow_times_ready_29;
  wire signed [46-1:0] _dataflow_times_mul_odata_29;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_29;
  assign _dataflow_times_data_29 = _dataflow_times_mul_odata_reg_29;
  wire _dataflow_times_mul_ovalid_29;
  reg _dataflow_times_mul_valid_reg_29;
  assign _dataflow_times_valid_29 = _dataflow_times_mul_valid_reg_29;
  wire _dataflow_times_mul_enable_29;
  wire _dataflow_times_mul_update_29;
  assign _dataflow_times_mul_enable_29 = (_dataflow_times_ready_29 || !_dataflow_times_valid_29) && 1 && ivalid2;
  assign _dataflow_times_mul_update_29 = _dataflow_times_ready_29 || !_dataflow_times_valid_29;

  multiplier_6
  _dataflow_times_mul_29
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_29),
    .enable(_dataflow_times_mul_enable_29),
    .valid(_dataflow_times_mul_ovalid_29),
    .a(idata2),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_29)
  );

  wire signed [32-1:0] _dataflow_times_data_31;
  wire _dataflow_times_valid_31;
  wire _dataflow_times_ready_31;
  wire signed [46-1:0] _dataflow_times_mul_odata_31;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_31;
  assign _dataflow_times_data_31 = _dataflow_times_mul_odata_reg_31;
  wire _dataflow_times_mul_ovalid_31;
  reg _dataflow_times_mul_valid_reg_31;
  assign _dataflow_times_valid_31 = _dataflow_times_mul_valid_reg_31;
  wire _dataflow_times_mul_enable_31;
  wire _dataflow_times_mul_update_31;
  assign _dataflow_times_mul_enable_31 = (_dataflow_times_ready_31 || !_dataflow_times_valid_31) && 1 && ivalid2;
  assign _dataflow_times_mul_update_31 = _dataflow_times_ready_31 || !_dataflow_times_valid_31;

  multiplier_7
  _dataflow_times_mul_31
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_31),
    .enable(_dataflow_times_mul_enable_31),
    .valid(_dataflow_times_mul_ovalid_31),
    .a(_dataflow__prev_data_16),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_31)
  );

  wire signed [32-1:0] _dataflow_times_data_33;
  wire _dataflow_times_valid_33;
  wire _dataflow_times_ready_33;
  wire signed [46-1:0] _dataflow_times_mul_odata_33;
  reg signed [46-1:0] _dataflow_times_mul_odata_reg_33;
  assign _dataflow_times_data_33 = _dataflow_times_mul_odata_reg_33;
  wire _dataflow_times_mul_ovalid_33;
  reg _dataflow_times_mul_valid_reg_33;
  assign _dataflow_times_valid_33 = _dataflow_times_mul_valid_reg_33;
  wire _dataflow_times_mul_enable_33;
  wire _dataflow_times_mul_update_33;
  assign _dataflow_times_mul_enable_33 = (_dataflow_times_ready_33 || !_dataflow_times_valid_33) && 1 && ivalid2;
  assign _dataflow_times_mul_update_33 = _dataflow_times_ready_33 || !_dataflow_times_valid_33;

  multiplier_8
  _dataflow_times_mul_33
  (
    .CLK(CLK),
    .RST(RST),
    .update(_dataflow_times_mul_update_33),
    .enable(_dataflow_times_mul_enable_33),
    .valid(_dataflow_times_mul_ovalid_33),
    .a(_dataflow__prev_data_17),
    .b(14'sd7281),
    .c(_dataflow_times_mul_odata_33)
  );

  reg signed [32-1:0] _dataflow_plus_data_20;
  reg _dataflow_plus_valid_20;
  wire _dataflow_plus_ready_20;
  assign _dataflow_times_ready_18 = (_dataflow_plus_ready_20 || !_dataflow_plus_valid_20) && (_dataflow_times_valid_18 && _dataflow_times_valid_19);
  assign _dataflow_times_ready_19 = (_dataflow_plus_ready_20 || !_dataflow_plus_valid_20) && (_dataflow_times_valid_18 && _dataflow_times_valid_19);
  reg signed [32-1:0] _dataflow__delay_data_35;
  reg _dataflow__delay_valid_35;
  wire _dataflow__delay_ready_35;
  assign _dataflow_times_ready_21 = (_dataflow__delay_ready_35 || !_dataflow__delay_valid_35) && _dataflow_times_valid_21;
  reg signed [32-1:0] _dataflow__delay_data_36;
  reg _dataflow__delay_valid_36;
  wire _dataflow__delay_ready_36;
  assign _dataflow_times_ready_23 = (_dataflow__delay_ready_36 || !_dataflow__delay_valid_36) && _dataflow_times_valid_23;
  reg signed [32-1:0] _dataflow__delay_data_38;
  reg _dataflow__delay_valid_38;
  wire _dataflow__delay_ready_38;
  assign _dataflow_times_ready_25 = (_dataflow__delay_ready_38 || !_dataflow__delay_valid_38) && _dataflow_times_valid_25;
  reg signed [32-1:0] _dataflow__delay_data_41;
  reg _dataflow__delay_valid_41;
  wire _dataflow__delay_ready_41;
  assign _dataflow_times_ready_27 = (_dataflow__delay_ready_41 || !_dataflow__delay_valid_41) && _dataflow_times_valid_27;
  reg signed [32-1:0] _dataflow__delay_data_45;
  reg _dataflow__delay_valid_45;
  wire _dataflow__delay_ready_45;
  assign _dataflow_times_ready_29 = (_dataflow__delay_ready_45 || !_dataflow__delay_valid_45) && _dataflow_times_valid_29;
  reg signed [32-1:0] _dataflow__delay_data_50;
  reg _dataflow__delay_valid_50;
  wire _dataflow__delay_ready_50;
  assign _dataflow_times_ready_31 = (_dataflow__delay_ready_50 || !_dataflow__delay_valid_50) && _dataflow_times_valid_31;
  reg signed [32-1:0] _dataflow__delay_data_56;
  reg _dataflow__delay_valid_56;
  wire _dataflow__delay_ready_56;
  assign _dataflow_times_ready_33 = (_dataflow__delay_ready_56 || !_dataflow__delay_valid_56) && _dataflow_times_valid_33;
  reg signed [32-1:0] _dataflow_plus_data_22;
  reg _dataflow_plus_valid_22;
  wire _dataflow_plus_ready_22;
  assign _dataflow_plus_ready_20 = (_dataflow_plus_ready_22 || !_dataflow_plus_valid_22) && (_dataflow_plus_valid_20 && _dataflow__delay_valid_35);
  assign _dataflow__delay_ready_35 = (_dataflow_plus_ready_22 || !_dataflow_plus_valid_22) && (_dataflow_plus_valid_20 && _dataflow__delay_valid_35);
  reg signed [32-1:0] _dataflow__delay_data_37;
  reg _dataflow__delay_valid_37;
  wire _dataflow__delay_ready_37;
  assign _dataflow__delay_ready_36 = (_dataflow__delay_ready_37 || !_dataflow__delay_valid_37) && _dataflow__delay_valid_36;
  reg signed [32-1:0] _dataflow__delay_data_39;
  reg _dataflow__delay_valid_39;
  wire _dataflow__delay_ready_39;
  assign _dataflow__delay_ready_38 = (_dataflow__delay_ready_39 || !_dataflow__delay_valid_39) && _dataflow__delay_valid_38;
  reg signed [32-1:0] _dataflow__delay_data_42;
  reg _dataflow__delay_valid_42;
  wire _dataflow__delay_ready_42;
  assign _dataflow__delay_ready_41 = (_dataflow__delay_ready_42 || !_dataflow__delay_valid_42) && _dataflow__delay_valid_41;
  reg signed [32-1:0] _dataflow__delay_data_46;
  reg _dataflow__delay_valid_46;
  wire _dataflow__delay_ready_46;
  assign _dataflow__delay_ready_45 = (_dataflow__delay_ready_46 || !_dataflow__delay_valid_46) && _dataflow__delay_valid_45;
  reg signed [32-1:0] _dataflow__delay_data_51;
  reg _dataflow__delay_valid_51;
  wire _dataflow__delay_ready_51;
  assign _dataflow__delay_ready_50 = (_dataflow__delay_ready_51 || !_dataflow__delay_valid_51) && _dataflow__delay_valid_50;
  reg signed [32-1:0] _dataflow__delay_data_57;
  reg _dataflow__delay_valid_57;
  wire _dataflow__delay_ready_57;
  assign _dataflow__delay_ready_56 = (_dataflow__delay_ready_57 || !_dataflow__delay_valid_57) && _dataflow__delay_valid_56;
  reg signed [32-1:0] _dataflow_plus_data_24;
  reg _dataflow_plus_valid_24;
  wire _dataflow_plus_ready_24;
  assign _dataflow_plus_ready_22 = (_dataflow_plus_ready_24 || !_dataflow_plus_valid_24) && (_dataflow_plus_valid_22 && _dataflow__delay_valid_37);
  assign _dataflow__delay_ready_37 = (_dataflow_plus_ready_24 || !_dataflow_plus_valid_24) && (_dataflow_plus_valid_22 && _dataflow__delay_valid_37);
  reg signed [32-1:0] _dataflow__delay_data_40;
  reg _dataflow__delay_valid_40;
  wire _dataflow__delay_ready_40;
  assign _dataflow__delay_ready_39 = (_dataflow__delay_ready_40 || !_dataflow__delay_valid_40) && _dataflow__delay_valid_39;
  reg signed [32-1:0] _dataflow__delay_data_43;
  reg _dataflow__delay_valid_43;
  wire _dataflow__delay_ready_43;
  assign _dataflow__delay_ready_42 = (_dataflow__delay_ready_43 || !_dataflow__delay_valid_43) && _dataflow__delay_valid_42;
  reg signed [32-1:0] _dataflow__delay_data_47;
  reg _dataflow__delay_valid_47;
  wire _dataflow__delay_ready_47;
  assign _dataflow__delay_ready_46 = (_dataflow__delay_ready_47 || !_dataflow__delay_valid_47) && _dataflow__delay_valid_46;
  reg signed [32-1:0] _dataflow__delay_data_52;
  reg _dataflow__delay_valid_52;
  wire _dataflow__delay_ready_52;
  assign _dataflow__delay_ready_51 = (_dataflow__delay_ready_52 || !_dataflow__delay_valid_52) && _dataflow__delay_valid_51;
  reg signed [32-1:0] _dataflow__delay_data_58;
  reg _dataflow__delay_valid_58;
  wire _dataflow__delay_ready_58;
  assign _dataflow__delay_ready_57 = (_dataflow__delay_ready_58 || !_dataflow__delay_valid_58) && _dataflow__delay_valid_57;
  reg signed [32-1:0] _dataflow_plus_data_26;
  reg _dataflow_plus_valid_26;
  wire _dataflow_plus_ready_26;
  assign _dataflow_plus_ready_24 = (_dataflow_plus_ready_26 || !_dataflow_plus_valid_26) && (_dataflow_plus_valid_24 && _dataflow__delay_valid_40);
  assign _dataflow__delay_ready_40 = (_dataflow_plus_ready_26 || !_dataflow_plus_valid_26) && (_dataflow_plus_valid_24 && _dataflow__delay_valid_40);
  reg signed [32-1:0] _dataflow__delay_data_44;
  reg _dataflow__delay_valid_44;
  wire _dataflow__delay_ready_44;
  assign _dataflow__delay_ready_43 = (_dataflow__delay_ready_44 || !_dataflow__delay_valid_44) && _dataflow__delay_valid_43;
  reg signed [32-1:0] _dataflow__delay_data_48;
  reg _dataflow__delay_valid_48;
  wire _dataflow__delay_ready_48;
  assign _dataflow__delay_ready_47 = (_dataflow__delay_ready_48 || !_dataflow__delay_valid_48) && _dataflow__delay_valid_47;
  reg signed [32-1:0] _dataflow__delay_data_53;
  reg _dataflow__delay_valid_53;
  wire _dataflow__delay_ready_53;
  assign _dataflow__delay_ready_52 = (_dataflow__delay_ready_53 || !_dataflow__delay_valid_53) && _dataflow__delay_valid_52;
  reg signed [32-1:0] _dataflow__delay_data_59;
  reg _dataflow__delay_valid_59;
  wire _dataflow__delay_ready_59;
  assign _dataflow__delay_ready_58 = (_dataflow__delay_ready_59 || !_dataflow__delay_valid_59) && _dataflow__delay_valid_58;
  reg signed [32-1:0] _dataflow_plus_data_28;
  reg _dataflow_plus_valid_28;
  wire _dataflow_plus_ready_28;
  assign _dataflow_plus_ready_26 = (_dataflow_plus_ready_28 || !_dataflow_plus_valid_28) && (_dataflow_plus_valid_26 && _dataflow__delay_valid_44);
  assign _dataflow__delay_ready_44 = (_dataflow_plus_ready_28 || !_dataflow_plus_valid_28) && (_dataflow_plus_valid_26 && _dataflow__delay_valid_44);
  reg signed [32-1:0] _dataflow__delay_data_49;
  reg _dataflow__delay_valid_49;
  wire _dataflow__delay_ready_49;
  assign _dataflow__delay_ready_48 = (_dataflow__delay_ready_49 || !_dataflow__delay_valid_49) && _dataflow__delay_valid_48;
  reg signed [32-1:0] _dataflow__delay_data_54;
  reg _dataflow__delay_valid_54;
  wire _dataflow__delay_ready_54;
  assign _dataflow__delay_ready_53 = (_dataflow__delay_ready_54 || !_dataflow__delay_valid_54) && _dataflow__delay_valid_53;
  reg signed [32-1:0] _dataflow__delay_data_60;
  reg _dataflow__delay_valid_60;
  wire _dataflow__delay_ready_60;
  assign _dataflow__delay_ready_59 = (_dataflow__delay_ready_60 || !_dataflow__delay_valid_60) && _dataflow__delay_valid_59;
  reg signed [32-1:0] _dataflow_plus_data_30;
  reg _dataflow_plus_valid_30;
  wire _dataflow_plus_ready_30;
  assign _dataflow_plus_ready_28 = (_dataflow_plus_ready_30 || !_dataflow_plus_valid_30) && (_dataflow_plus_valid_28 && _dataflow__delay_valid_49);
  assign _dataflow__delay_ready_49 = (_dataflow_plus_ready_30 || !_dataflow_plus_valid_30) && (_dataflow_plus_valid_28 && _dataflow__delay_valid_49);
  reg signed [32-1:0] _dataflow__delay_data_55;
  reg _dataflow__delay_valid_55;
  wire _dataflow__delay_ready_55;
  assign _dataflow__delay_ready_54 = (_dataflow__delay_ready_55 || !_dataflow__delay_valid_55) && _dataflow__delay_valid_54;
  reg signed [32-1:0] _dataflow__delay_data_61;
  reg _dataflow__delay_valid_61;
  wire _dataflow__delay_ready_61;
  assign _dataflow__delay_ready_60 = (_dataflow__delay_ready_61 || !_dataflow__delay_valid_61) && _dataflow__delay_valid_60;
  reg signed [32-1:0] _dataflow_plus_data_32;
  reg _dataflow_plus_valid_32;
  wire _dataflow_plus_ready_32;
  assign _dataflow_plus_ready_30 = (_dataflow_plus_ready_32 || !_dataflow_plus_valid_32) && (_dataflow_plus_valid_30 && _dataflow__delay_valid_55);
  assign _dataflow__delay_ready_55 = (_dataflow_plus_ready_32 || !_dataflow_plus_valid_32) && (_dataflow_plus_valid_30 && _dataflow__delay_valid_55);
  reg signed [32-1:0] _dataflow__delay_data_62;
  reg _dataflow__delay_valid_62;
  wire _dataflow__delay_ready_62;
  assign _dataflow__delay_ready_61 = (_dataflow__delay_ready_62 || !_dataflow__delay_valid_62) && _dataflow__delay_valid_61;
  reg signed [32-1:0] _dataflow_plus_data_34;
  reg _dataflow_plus_valid_34;
  wire _dataflow_plus_ready_34;
  assign _dataflow_plus_ready_32 = (_dataflow_plus_ready_34 || !_dataflow_plus_valid_34) && (_dataflow_plus_valid_32 && _dataflow__delay_valid_62);
  assign _dataflow__delay_ready_62 = (_dataflow_plus_ready_34 || !_dataflow_plus_valid_34) && (_dataflow_plus_valid_32 && _dataflow__delay_valid_62);
  assign odata = _dataflow_plus_data_34;
  assign ovalid = _dataflow_plus_valid_34;
  assign _dataflow_plus_ready_34 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow__prev_data_12 <= 0;
      _dataflow__prev_data_13 <= 0;
      _dataflow__prev_data_14 <= 0;
      _dataflow__prev_data_15 <= 0;
      _dataflow__prev_data_16 <= 0;
      _dataflow__prev_data_17 <= 0;
      _dataflow_times_mul_odata_reg_18 <= 0;
      _dataflow_times_mul_valid_reg_18 <= 0;
      _dataflow_times_mul_odata_reg_19 <= 0;
      _dataflow_times_mul_valid_reg_19 <= 0;
      _dataflow_times_mul_odata_reg_21 <= 0;
      _dataflow_times_mul_valid_reg_21 <= 0;
      _dataflow_times_mul_odata_reg_23 <= 0;
      _dataflow_times_mul_valid_reg_23 <= 0;
      _dataflow_times_mul_odata_reg_25 <= 0;
      _dataflow_times_mul_valid_reg_25 <= 0;
      _dataflow_times_mul_odata_reg_27 <= 0;
      _dataflow_times_mul_valid_reg_27 <= 0;
      _dataflow_times_mul_odata_reg_29 <= 0;
      _dataflow_times_mul_valid_reg_29 <= 0;
      _dataflow_times_mul_odata_reg_31 <= 0;
      _dataflow_times_mul_valid_reg_31 <= 0;
      _dataflow_times_mul_odata_reg_33 <= 0;
      _dataflow_times_mul_valid_reg_33 <= 0;
      _dataflow_plus_data_20 <= 0;
      _dataflow_plus_valid_20 <= 0;
      _dataflow__delay_data_35 <= 0;
      _dataflow__delay_valid_35 <= 0;
      _dataflow__delay_data_36 <= 0;
      _dataflow__delay_valid_36 <= 0;
      _dataflow__delay_data_38 <= 0;
      _dataflow__delay_valid_38 <= 0;
      _dataflow__delay_data_41 <= 0;
      _dataflow__delay_valid_41 <= 0;
      _dataflow__delay_data_45 <= 0;
      _dataflow__delay_valid_45 <= 0;
      _dataflow__delay_data_50 <= 0;
      _dataflow__delay_valid_50 <= 0;
      _dataflow__delay_data_56 <= 0;
      _dataflow__delay_valid_56 <= 0;
      _dataflow_plus_data_22 <= 0;
      _dataflow_plus_valid_22 <= 0;
      _dataflow__delay_data_37 <= 0;
      _dataflow__delay_valid_37 <= 0;
      _dataflow__delay_data_39 <= 0;
      _dataflow__delay_valid_39 <= 0;
      _dataflow__delay_data_42 <= 0;
      _dataflow__delay_valid_42 <= 0;
      _dataflow__delay_data_46 <= 0;
      _dataflow__delay_valid_46 <= 0;
      _dataflow__delay_data_51 <= 0;
      _dataflow__delay_valid_51 <= 0;
      _dataflow__delay_data_57 <= 0;
      _dataflow__delay_valid_57 <= 0;
      _dataflow_plus_data_24 <= 0;
      _dataflow_plus_valid_24 <= 0;
      _dataflow__delay_data_40 <= 0;
      _dataflow__delay_valid_40 <= 0;
      _dataflow__delay_data_43 <= 0;
      _dataflow__delay_valid_43 <= 0;
      _dataflow__delay_data_47 <= 0;
      _dataflow__delay_valid_47 <= 0;
      _dataflow__delay_data_52 <= 0;
      _dataflow__delay_valid_52 <= 0;
      _dataflow__delay_data_58 <= 0;
      _dataflow__delay_valid_58 <= 0;
      _dataflow_plus_data_26 <= 0;
      _dataflow_plus_valid_26 <= 0;
      _dataflow__delay_data_44 <= 0;
      _dataflow__delay_valid_44 <= 0;
      _dataflow__delay_data_48 <= 0;
      _dataflow__delay_valid_48 <= 0;
      _dataflow__delay_data_53 <= 0;
      _dataflow__delay_valid_53 <= 0;
      _dataflow__delay_data_59 <= 0;
      _dataflow__delay_valid_59 <= 0;
      _dataflow_plus_data_28 <= 0;
      _dataflow_plus_valid_28 <= 0;
      _dataflow__delay_data_49 <= 0;
      _dataflow__delay_valid_49 <= 0;
      _dataflow__delay_data_54 <= 0;
      _dataflow__delay_valid_54 <= 0;
      _dataflow__delay_data_60 <= 0;
      _dataflow__delay_valid_60 <= 0;
      _dataflow_plus_data_30 <= 0;
      _dataflow_plus_valid_30 <= 0;
      _dataflow__delay_data_55 <= 0;
      _dataflow__delay_valid_55 <= 0;
      _dataflow__delay_data_61 <= 0;
      _dataflow__delay_valid_61 <= 0;
      _dataflow_plus_data_32 <= 0;
      _dataflow_plus_valid_32 <= 0;
      _dataflow__delay_data_62 <= 0;
      _dataflow__delay_valid_62 <= 0;
      _dataflow_plus_data_34 <= 0;
      _dataflow_plus_valid_34 <= 0;
    end else begin
      if(ivalid0) begin
        _dataflow__prev_data_12 <= idata0;
      end 
      if(ivalid0) begin
        _dataflow__prev_data_13 <= _dataflow__prev_data_12;
      end 
      if(ivalid1) begin
        _dataflow__prev_data_14 <= idata1;
      end 
      if(ivalid1) begin
        _dataflow__prev_data_15 <= _dataflow__prev_data_14;
      end 
      if(ivalid2) begin
        _dataflow__prev_data_16 <= idata2;
      end 
      if(ivalid2) begin
        _dataflow__prev_data_17 <= _dataflow__prev_data_16;
      end 
      if(_dataflow_times_ready_18 || !_dataflow_times_valid_18) begin
        _dataflow_times_mul_odata_reg_18 <= _dataflow_times_mul_odata_18 >>> 16;
      end 
      if(_dataflow_times_ready_18 || !_dataflow_times_valid_18) begin
        _dataflow_times_mul_valid_reg_18 <= _dataflow_times_mul_ovalid_18;
      end 
      if(_dataflow_times_ready_19 || !_dataflow_times_valid_19) begin
        _dataflow_times_mul_odata_reg_19 <= _dataflow_times_mul_odata_19 >>> 16;
      end 
      if(_dataflow_times_ready_19 || !_dataflow_times_valid_19) begin
        _dataflow_times_mul_valid_reg_19 <= _dataflow_times_mul_ovalid_19;
      end 
      if(_dataflow_times_ready_21 || !_dataflow_times_valid_21) begin
        _dataflow_times_mul_odata_reg_21 <= _dataflow_times_mul_odata_21 >>> 16;
      end 
      if(_dataflow_times_ready_21 || !_dataflow_times_valid_21) begin
        _dataflow_times_mul_valid_reg_21 <= _dataflow_times_mul_ovalid_21;
      end 
      if(_dataflow_times_ready_23 || !_dataflow_times_valid_23) begin
        _dataflow_times_mul_odata_reg_23 <= _dataflow_times_mul_odata_23 >>> 16;
      end 
      if(_dataflow_times_ready_23 || !_dataflow_times_valid_23) begin
        _dataflow_times_mul_valid_reg_23 <= _dataflow_times_mul_ovalid_23;
      end 
      if(_dataflow_times_ready_25 || !_dataflow_times_valid_25) begin
        _dataflow_times_mul_odata_reg_25 <= _dataflow_times_mul_odata_25 >>> 16;
      end 
      if(_dataflow_times_ready_25 || !_dataflow_times_valid_25) begin
        _dataflow_times_mul_valid_reg_25 <= _dataflow_times_mul_ovalid_25;
      end 
      if(_dataflow_times_ready_27 || !_dataflow_times_valid_27) begin
        _dataflow_times_mul_odata_reg_27 <= _dataflow_times_mul_odata_27 >>> 16;
      end 
      if(_dataflow_times_ready_27 || !_dataflow_times_valid_27) begin
        _dataflow_times_mul_valid_reg_27 <= _dataflow_times_mul_ovalid_27;
      end 
      if(_dataflow_times_ready_29 || !_dataflow_times_valid_29) begin
        _dataflow_times_mul_odata_reg_29 <= _dataflow_times_mul_odata_29 >>> 16;
      end 
      if(_dataflow_times_ready_29 || !_dataflow_times_valid_29) begin
        _dataflow_times_mul_valid_reg_29 <= _dataflow_times_mul_ovalid_29;
      end 
      if(_dataflow_times_ready_31 || !_dataflow_times_valid_31) begin
        _dataflow_times_mul_odata_reg_31 <= _dataflow_times_mul_odata_31 >>> 16;
      end 
      if(_dataflow_times_ready_31 || !_dataflow_times_valid_31) begin
        _dataflow_times_mul_valid_reg_31 <= _dataflow_times_mul_ovalid_31;
      end 
      if(_dataflow_times_ready_33 || !_dataflow_times_valid_33) begin
        _dataflow_times_mul_odata_reg_33 <= _dataflow_times_mul_odata_33 >>> 16;
      end 
      if(_dataflow_times_ready_33 || !_dataflow_times_valid_33) begin
        _dataflow_times_mul_valid_reg_33 <= _dataflow_times_mul_ovalid_33;
      end 
      if((_dataflow_plus_ready_20 || !_dataflow_plus_valid_20) && (_dataflow_times_ready_18 && _dataflow_times_ready_19) && (_dataflow_times_valid_18 && _dataflow_times_valid_19)) begin
        _dataflow_plus_data_20 <= _dataflow_times_data_18 + _dataflow_times_data_19;
      end 
      if(_dataflow_plus_valid_20 && _dataflow_plus_ready_20) begin
        _dataflow_plus_valid_20 <= 0;
      end 
      if((_dataflow_plus_ready_20 || !_dataflow_plus_valid_20) && (_dataflow_times_ready_18 && _dataflow_times_ready_19)) begin
        _dataflow_plus_valid_20 <= _dataflow_times_valid_18 && _dataflow_times_valid_19;
      end 
      if((_dataflow__delay_ready_35 || !_dataflow__delay_valid_35) && _dataflow_times_ready_21 && _dataflow_times_valid_21) begin
        _dataflow__delay_data_35 <= _dataflow_times_data_21;
      end 
      if(_dataflow__delay_valid_35 && _dataflow__delay_ready_35) begin
        _dataflow__delay_valid_35 <= 0;
      end 
      if((_dataflow__delay_ready_35 || !_dataflow__delay_valid_35) && _dataflow_times_ready_21) begin
        _dataflow__delay_valid_35 <= _dataflow_times_valid_21;
      end 
      if((_dataflow__delay_ready_36 || !_dataflow__delay_valid_36) && _dataflow_times_ready_23 && _dataflow_times_valid_23) begin
        _dataflow__delay_data_36 <= _dataflow_times_data_23;
      end 
      if(_dataflow__delay_valid_36 && _dataflow__delay_ready_36) begin
        _dataflow__delay_valid_36 <= 0;
      end 
      if((_dataflow__delay_ready_36 || !_dataflow__delay_valid_36) && _dataflow_times_ready_23) begin
        _dataflow__delay_valid_36 <= _dataflow_times_valid_23;
      end 
      if((_dataflow__delay_ready_38 || !_dataflow__delay_valid_38) && _dataflow_times_ready_25 && _dataflow_times_valid_25) begin
        _dataflow__delay_data_38 <= _dataflow_times_data_25;
      end 
      if(_dataflow__delay_valid_38 && _dataflow__delay_ready_38) begin
        _dataflow__delay_valid_38 <= 0;
      end 
      if((_dataflow__delay_ready_38 || !_dataflow__delay_valid_38) && _dataflow_times_ready_25) begin
        _dataflow__delay_valid_38 <= _dataflow_times_valid_25;
      end 
      if((_dataflow__delay_ready_41 || !_dataflow__delay_valid_41) && _dataflow_times_ready_27 && _dataflow_times_valid_27) begin
        _dataflow__delay_data_41 <= _dataflow_times_data_27;
      end 
      if(_dataflow__delay_valid_41 && _dataflow__delay_ready_41) begin
        _dataflow__delay_valid_41 <= 0;
      end 
      if((_dataflow__delay_ready_41 || !_dataflow__delay_valid_41) && _dataflow_times_ready_27) begin
        _dataflow__delay_valid_41 <= _dataflow_times_valid_27;
      end 
      if((_dataflow__delay_ready_45 || !_dataflow__delay_valid_45) && _dataflow_times_ready_29 && _dataflow_times_valid_29) begin
        _dataflow__delay_data_45 <= _dataflow_times_data_29;
      end 
      if(_dataflow__delay_valid_45 && _dataflow__delay_ready_45) begin
        _dataflow__delay_valid_45 <= 0;
      end 
      if((_dataflow__delay_ready_45 || !_dataflow__delay_valid_45) && _dataflow_times_ready_29) begin
        _dataflow__delay_valid_45 <= _dataflow_times_valid_29;
      end 
      if((_dataflow__delay_ready_50 || !_dataflow__delay_valid_50) && _dataflow_times_ready_31 && _dataflow_times_valid_31) begin
        _dataflow__delay_data_50 <= _dataflow_times_data_31;
      end 
      if(_dataflow__delay_valid_50 && _dataflow__delay_ready_50) begin
        _dataflow__delay_valid_50 <= 0;
      end 
      if((_dataflow__delay_ready_50 || !_dataflow__delay_valid_50) && _dataflow_times_ready_31) begin
        _dataflow__delay_valid_50 <= _dataflow_times_valid_31;
      end 
      if((_dataflow__delay_ready_56 || !_dataflow__delay_valid_56) && _dataflow_times_ready_33 && _dataflow_times_valid_33) begin
        _dataflow__delay_data_56 <= _dataflow_times_data_33;
      end 
      if(_dataflow__delay_valid_56 && _dataflow__delay_ready_56) begin
        _dataflow__delay_valid_56 <= 0;
      end 
      if((_dataflow__delay_ready_56 || !_dataflow__delay_valid_56) && _dataflow_times_ready_33) begin
        _dataflow__delay_valid_56 <= _dataflow_times_valid_33;
      end 
      if((_dataflow_plus_ready_22 || !_dataflow_plus_valid_22) && (_dataflow_plus_ready_20 && _dataflow__delay_ready_35) && (_dataflow_plus_valid_20 && _dataflow__delay_valid_35)) begin
        _dataflow_plus_data_22 <= _dataflow_plus_data_20 + _dataflow__delay_data_35;
      end 
      if(_dataflow_plus_valid_22 && _dataflow_plus_ready_22) begin
        _dataflow_plus_valid_22 <= 0;
      end 
      if((_dataflow_plus_ready_22 || !_dataflow_plus_valid_22) && (_dataflow_plus_ready_20 && _dataflow__delay_ready_35)) begin
        _dataflow_plus_valid_22 <= _dataflow_plus_valid_20 && _dataflow__delay_valid_35;
      end 
      if((_dataflow__delay_ready_37 || !_dataflow__delay_valid_37) && _dataflow__delay_ready_36 && _dataflow__delay_valid_36) begin
        _dataflow__delay_data_37 <= _dataflow__delay_data_36;
      end 
      if(_dataflow__delay_valid_37 && _dataflow__delay_ready_37) begin
        _dataflow__delay_valid_37 <= 0;
      end 
      if((_dataflow__delay_ready_37 || !_dataflow__delay_valid_37) && _dataflow__delay_ready_36) begin
        _dataflow__delay_valid_37 <= _dataflow__delay_valid_36;
      end 
      if((_dataflow__delay_ready_39 || !_dataflow__delay_valid_39) && _dataflow__delay_ready_38 && _dataflow__delay_valid_38) begin
        _dataflow__delay_data_39 <= _dataflow__delay_data_38;
      end 
      if(_dataflow__delay_valid_39 && _dataflow__delay_ready_39) begin
        _dataflow__delay_valid_39 <= 0;
      end 
      if((_dataflow__delay_ready_39 || !_dataflow__delay_valid_39) && _dataflow__delay_ready_38) begin
        _dataflow__delay_valid_39 <= _dataflow__delay_valid_38;
      end 
      if((_dataflow__delay_ready_42 || !_dataflow__delay_valid_42) && _dataflow__delay_ready_41 && _dataflow__delay_valid_41) begin
        _dataflow__delay_data_42 <= _dataflow__delay_data_41;
      end 
      if(_dataflow__delay_valid_42 && _dataflow__delay_ready_42) begin
        _dataflow__delay_valid_42 <= 0;
      end 
      if((_dataflow__delay_ready_42 || !_dataflow__delay_valid_42) && _dataflow__delay_ready_41) begin
        _dataflow__delay_valid_42 <= _dataflow__delay_valid_41;
      end 
      if((_dataflow__delay_ready_46 || !_dataflow__delay_valid_46) && _dataflow__delay_ready_45 && _dataflow__delay_valid_45) begin
        _dataflow__delay_data_46 <= _dataflow__delay_data_45;
      end 
      if(_dataflow__delay_valid_46 && _dataflow__delay_ready_46) begin
        _dataflow__delay_valid_46 <= 0;
      end 
      if((_dataflow__delay_ready_46 || !_dataflow__delay_valid_46) && _dataflow__delay_ready_45) begin
        _dataflow__delay_valid_46 <= _dataflow__delay_valid_45;
      end 
      if((_dataflow__delay_ready_51 || !_dataflow__delay_valid_51) && _dataflow__delay_ready_50 && _dataflow__delay_valid_50) begin
        _dataflow__delay_data_51 <= _dataflow__delay_data_50;
      end 
      if(_dataflow__delay_valid_51 && _dataflow__delay_ready_51) begin
        _dataflow__delay_valid_51 <= 0;
      end 
      if((_dataflow__delay_ready_51 || !_dataflow__delay_valid_51) && _dataflow__delay_ready_50) begin
        _dataflow__delay_valid_51 <= _dataflow__delay_valid_50;
      end 
      if((_dataflow__delay_ready_57 || !_dataflow__delay_valid_57) && _dataflow__delay_ready_56 && _dataflow__delay_valid_56) begin
        _dataflow__delay_data_57 <= _dataflow__delay_data_56;
      end 
      if(_dataflow__delay_valid_57 && _dataflow__delay_ready_57) begin
        _dataflow__delay_valid_57 <= 0;
      end 
      if((_dataflow__delay_ready_57 || !_dataflow__delay_valid_57) && _dataflow__delay_ready_56) begin
        _dataflow__delay_valid_57 <= _dataflow__delay_valid_56;
      end 
      if((_dataflow_plus_ready_24 || !_dataflow_plus_valid_24) && (_dataflow_plus_ready_22 && _dataflow__delay_ready_37) && (_dataflow_plus_valid_22 && _dataflow__delay_valid_37)) begin
        _dataflow_plus_data_24 <= _dataflow_plus_data_22 + _dataflow__delay_data_37;
      end 
      if(_dataflow_plus_valid_24 && _dataflow_plus_ready_24) begin
        _dataflow_plus_valid_24 <= 0;
      end 
      if((_dataflow_plus_ready_24 || !_dataflow_plus_valid_24) && (_dataflow_plus_ready_22 && _dataflow__delay_ready_37)) begin
        _dataflow_plus_valid_24 <= _dataflow_plus_valid_22 && _dataflow__delay_valid_37;
      end 
      if((_dataflow__delay_ready_40 || !_dataflow__delay_valid_40) && _dataflow__delay_ready_39 && _dataflow__delay_valid_39) begin
        _dataflow__delay_data_40 <= _dataflow__delay_data_39;
      end 
      if(_dataflow__delay_valid_40 && _dataflow__delay_ready_40) begin
        _dataflow__delay_valid_40 <= 0;
      end 
      if((_dataflow__delay_ready_40 || !_dataflow__delay_valid_40) && _dataflow__delay_ready_39) begin
        _dataflow__delay_valid_40 <= _dataflow__delay_valid_39;
      end 
      if((_dataflow__delay_ready_43 || !_dataflow__delay_valid_43) && _dataflow__delay_ready_42 && _dataflow__delay_valid_42) begin
        _dataflow__delay_data_43 <= _dataflow__delay_data_42;
      end 
      if(_dataflow__delay_valid_43 && _dataflow__delay_ready_43) begin
        _dataflow__delay_valid_43 <= 0;
      end 
      if((_dataflow__delay_ready_43 || !_dataflow__delay_valid_43) && _dataflow__delay_ready_42) begin
        _dataflow__delay_valid_43 <= _dataflow__delay_valid_42;
      end 
      if((_dataflow__delay_ready_47 || !_dataflow__delay_valid_47) && _dataflow__delay_ready_46 && _dataflow__delay_valid_46) begin
        _dataflow__delay_data_47 <= _dataflow__delay_data_46;
      end 
      if(_dataflow__delay_valid_47 && _dataflow__delay_ready_47) begin
        _dataflow__delay_valid_47 <= 0;
      end 
      if((_dataflow__delay_ready_47 || !_dataflow__delay_valid_47) && _dataflow__delay_ready_46) begin
        _dataflow__delay_valid_47 <= _dataflow__delay_valid_46;
      end 
      if((_dataflow__delay_ready_52 || !_dataflow__delay_valid_52) && _dataflow__delay_ready_51 && _dataflow__delay_valid_51) begin
        _dataflow__delay_data_52 <= _dataflow__delay_data_51;
      end 
      if(_dataflow__delay_valid_52 && _dataflow__delay_ready_52) begin
        _dataflow__delay_valid_52 <= 0;
      end 
      if((_dataflow__delay_ready_52 || !_dataflow__delay_valid_52) && _dataflow__delay_ready_51) begin
        _dataflow__delay_valid_52 <= _dataflow__delay_valid_51;
      end 
      if((_dataflow__delay_ready_58 || !_dataflow__delay_valid_58) && _dataflow__delay_ready_57 && _dataflow__delay_valid_57) begin
        _dataflow__delay_data_58 <= _dataflow__delay_data_57;
      end 
      if(_dataflow__delay_valid_58 && _dataflow__delay_ready_58) begin
        _dataflow__delay_valid_58 <= 0;
      end 
      if((_dataflow__delay_ready_58 || !_dataflow__delay_valid_58) && _dataflow__delay_ready_57) begin
        _dataflow__delay_valid_58 <= _dataflow__delay_valid_57;
      end 
      if((_dataflow_plus_ready_26 || !_dataflow_plus_valid_26) && (_dataflow_plus_ready_24 && _dataflow__delay_ready_40) && (_dataflow_plus_valid_24 && _dataflow__delay_valid_40)) begin
        _dataflow_plus_data_26 <= _dataflow_plus_data_24 + _dataflow__delay_data_40;
      end 
      if(_dataflow_plus_valid_26 && _dataflow_plus_ready_26) begin
        _dataflow_plus_valid_26 <= 0;
      end 
      if((_dataflow_plus_ready_26 || !_dataflow_plus_valid_26) && (_dataflow_plus_ready_24 && _dataflow__delay_ready_40)) begin
        _dataflow_plus_valid_26 <= _dataflow_plus_valid_24 && _dataflow__delay_valid_40;
      end 
      if((_dataflow__delay_ready_44 || !_dataflow__delay_valid_44) && _dataflow__delay_ready_43 && _dataflow__delay_valid_43) begin
        _dataflow__delay_data_44 <= _dataflow__delay_data_43;
      end 
      if(_dataflow__delay_valid_44 && _dataflow__delay_ready_44) begin
        _dataflow__delay_valid_44 <= 0;
      end 
      if((_dataflow__delay_ready_44 || !_dataflow__delay_valid_44) && _dataflow__delay_ready_43) begin
        _dataflow__delay_valid_44 <= _dataflow__delay_valid_43;
      end 
      if((_dataflow__delay_ready_48 || !_dataflow__delay_valid_48) && _dataflow__delay_ready_47 && _dataflow__delay_valid_47) begin
        _dataflow__delay_data_48 <= _dataflow__delay_data_47;
      end 
      if(_dataflow__delay_valid_48 && _dataflow__delay_ready_48) begin
        _dataflow__delay_valid_48 <= 0;
      end 
      if((_dataflow__delay_ready_48 || !_dataflow__delay_valid_48) && _dataflow__delay_ready_47) begin
        _dataflow__delay_valid_48 <= _dataflow__delay_valid_47;
      end 
      if((_dataflow__delay_ready_53 || !_dataflow__delay_valid_53) && _dataflow__delay_ready_52 && _dataflow__delay_valid_52) begin
        _dataflow__delay_data_53 <= _dataflow__delay_data_52;
      end 
      if(_dataflow__delay_valid_53 && _dataflow__delay_ready_53) begin
        _dataflow__delay_valid_53 <= 0;
      end 
      if((_dataflow__delay_ready_53 || !_dataflow__delay_valid_53) && _dataflow__delay_ready_52) begin
        _dataflow__delay_valid_53 <= _dataflow__delay_valid_52;
      end 
      if((_dataflow__delay_ready_59 || !_dataflow__delay_valid_59) && _dataflow__delay_ready_58 && _dataflow__delay_valid_58) begin
        _dataflow__delay_data_59 <= _dataflow__delay_data_58;
      end 
      if(_dataflow__delay_valid_59 && _dataflow__delay_ready_59) begin
        _dataflow__delay_valid_59 <= 0;
      end 
      if((_dataflow__delay_ready_59 || !_dataflow__delay_valid_59) && _dataflow__delay_ready_58) begin
        _dataflow__delay_valid_59 <= _dataflow__delay_valid_58;
      end 
      if((_dataflow_plus_ready_28 || !_dataflow_plus_valid_28) && (_dataflow_plus_ready_26 && _dataflow__delay_ready_44) && (_dataflow_plus_valid_26 && _dataflow__delay_valid_44)) begin
        _dataflow_plus_data_28 <= _dataflow_plus_data_26 + _dataflow__delay_data_44;
      end 
      if(_dataflow_plus_valid_28 && _dataflow_plus_ready_28) begin
        _dataflow_plus_valid_28 <= 0;
      end 
      if((_dataflow_plus_ready_28 || !_dataflow_plus_valid_28) && (_dataflow_plus_ready_26 && _dataflow__delay_ready_44)) begin
        _dataflow_plus_valid_28 <= _dataflow_plus_valid_26 && _dataflow__delay_valid_44;
      end 
      if((_dataflow__delay_ready_49 || !_dataflow__delay_valid_49) && _dataflow__delay_ready_48 && _dataflow__delay_valid_48) begin
        _dataflow__delay_data_49 <= _dataflow__delay_data_48;
      end 
      if(_dataflow__delay_valid_49 && _dataflow__delay_ready_49) begin
        _dataflow__delay_valid_49 <= 0;
      end 
      if((_dataflow__delay_ready_49 || !_dataflow__delay_valid_49) && _dataflow__delay_ready_48) begin
        _dataflow__delay_valid_49 <= _dataflow__delay_valid_48;
      end 
      if((_dataflow__delay_ready_54 || !_dataflow__delay_valid_54) && _dataflow__delay_ready_53 && _dataflow__delay_valid_53) begin
        _dataflow__delay_data_54 <= _dataflow__delay_data_53;
      end 
      if(_dataflow__delay_valid_54 && _dataflow__delay_ready_54) begin
        _dataflow__delay_valid_54 <= 0;
      end 
      if((_dataflow__delay_ready_54 || !_dataflow__delay_valid_54) && _dataflow__delay_ready_53) begin
        _dataflow__delay_valid_54 <= _dataflow__delay_valid_53;
      end 
      if((_dataflow__delay_ready_60 || !_dataflow__delay_valid_60) && _dataflow__delay_ready_59 && _dataflow__delay_valid_59) begin
        _dataflow__delay_data_60 <= _dataflow__delay_data_59;
      end 
      if(_dataflow__delay_valid_60 && _dataflow__delay_ready_60) begin
        _dataflow__delay_valid_60 <= 0;
      end 
      if((_dataflow__delay_ready_60 || !_dataflow__delay_valid_60) && _dataflow__delay_ready_59) begin
        _dataflow__delay_valid_60 <= _dataflow__delay_valid_59;
      end 
      if((_dataflow_plus_ready_30 || !_dataflow_plus_valid_30) && (_dataflow_plus_ready_28 && _dataflow__delay_ready_49) && (_dataflow_plus_valid_28 && _dataflow__delay_valid_49)) begin
        _dataflow_plus_data_30 <= _dataflow_plus_data_28 + _dataflow__delay_data_49;
      end 
      if(_dataflow_plus_valid_30 && _dataflow_plus_ready_30) begin
        _dataflow_plus_valid_30 <= 0;
      end 
      if((_dataflow_plus_ready_30 || !_dataflow_plus_valid_30) && (_dataflow_plus_ready_28 && _dataflow__delay_ready_49)) begin
        _dataflow_plus_valid_30 <= _dataflow_plus_valid_28 && _dataflow__delay_valid_49;
      end 
      if((_dataflow__delay_ready_55 || !_dataflow__delay_valid_55) && _dataflow__delay_ready_54 && _dataflow__delay_valid_54) begin
        _dataflow__delay_data_55 <= _dataflow__delay_data_54;
      end 
      if(_dataflow__delay_valid_55 && _dataflow__delay_ready_55) begin
        _dataflow__delay_valid_55 <= 0;
      end 
      if((_dataflow__delay_ready_55 || !_dataflow__delay_valid_55) && _dataflow__delay_ready_54) begin
        _dataflow__delay_valid_55 <= _dataflow__delay_valid_54;
      end 
      if((_dataflow__delay_ready_61 || !_dataflow__delay_valid_61) && _dataflow__delay_ready_60 && _dataflow__delay_valid_60) begin
        _dataflow__delay_data_61 <= _dataflow__delay_data_60;
      end 
      if(_dataflow__delay_valid_61 && _dataflow__delay_ready_61) begin
        _dataflow__delay_valid_61 <= 0;
      end 
      if((_dataflow__delay_ready_61 || !_dataflow__delay_valid_61) && _dataflow__delay_ready_60) begin
        _dataflow__delay_valid_61 <= _dataflow__delay_valid_60;
      end 
      if((_dataflow_plus_ready_32 || !_dataflow_plus_valid_32) && (_dataflow_plus_ready_30 && _dataflow__delay_ready_55) && (_dataflow_plus_valid_30 && _dataflow__delay_valid_55)) begin
        _dataflow_plus_data_32 <= _dataflow_plus_data_30 + _dataflow__delay_data_55;
      end 
      if(_dataflow_plus_valid_32 && _dataflow_plus_ready_32) begin
        _dataflow_plus_valid_32 <= 0;
      end 
      if((_dataflow_plus_ready_32 || !_dataflow_plus_valid_32) && (_dataflow_plus_ready_30 && _dataflow__delay_ready_55)) begin
        _dataflow_plus_valid_32 <= _dataflow_plus_valid_30 && _dataflow__delay_valid_55;
      end 
      if((_dataflow__delay_ready_62 || !_dataflow__delay_valid_62) && _dataflow__delay_ready_61 && _dataflow__delay_valid_61) begin
        _dataflow__delay_data_62 <= _dataflow__delay_data_61;
      end 
      if(_dataflow__delay_valid_62 && _dataflow__delay_ready_62) begin
        _dataflow__delay_valid_62 <= 0;
      end 
      if((_dataflow__delay_ready_62 || !_dataflow__delay_valid_62) && _dataflow__delay_ready_61) begin
        _dataflow__delay_valid_62 <= _dataflow__delay_valid_61;
      end 
      if((_dataflow_plus_ready_34 || !_dataflow_plus_valid_34) && (_dataflow_plus_ready_32 && _dataflow__delay_ready_62) && (_dataflow_plus_valid_32 && _dataflow__delay_valid_62)) begin
        _dataflow_plus_data_34 <= _dataflow_plus_data_32 + _dataflow__delay_data_62;
      end 
      if(_dataflow_plus_valid_34 && _dataflow_plus_ready_34) begin
        _dataflow_plus_valid_34 <= 0;
      end 
      if((_dataflow_plus_ready_34 || !_dataflow_plus_valid_34) && (_dataflow_plus_ready_32 && _dataflow__delay_ready_62)) begin
        _dataflow_plus_valid_34 <= _dataflow_plus_valid_32 && _dataflow__delay_valid_62;
      end 
    end
  end


endmodule



module multiplier_0
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_0
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_0
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_1
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_1
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_1
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_2
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_2
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_2
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_3
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_3
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_3
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_4
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_4
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_4
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_5
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_5
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_5
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_6
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_6
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_6
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_7
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_7
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_7
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule



module multiplier_8
(
  input CLK,
  input RST,
  input update,
  input enable,
  output valid,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg valid_reg0;
  reg valid_reg1;
  reg valid_reg2;
  reg valid_reg3;
  reg valid_reg4;
  reg valid_reg5;
  assign valid = valid_reg5;

  always @(posedge CLK) begin
    if(RST) begin
      valid_reg0 <= 0;
      valid_reg1 <= 0;
      valid_reg2 <= 0;
      valid_reg3 <= 0;
      valid_reg4 <= 0;
      valid_reg5 <= 0;
    end else begin
      if(update) begin
        valid_reg0 <= enable;
        valid_reg1 <= valid_reg0;
        valid_reg2 <= valid_reg1;
        valid_reg3 <= valid_reg2;
        valid_reg4 <= valid_reg3;
        valid_reg5 <= valid_reg4;
      end 
    end
  end


  multiplier_core_8
  mult
  (
    .CLK(CLK),
    .update(update),
    .a(a),
    .b(b),
    .c(c)
  );


endmodule



module multiplier_core_8
(
  input CLK,
  input update,
  input [32-1:0] a,
  input [14-1:0] b,
  output [46-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [14-1:0] _b;
  wire signed [46-1:0] _mul;
  reg signed [46-1:0] _pipe_mul0;
  reg signed [46-1:0] _pipe_mul1;
  reg signed [46-1:0] _pipe_mul2;
  reg signed [46-1:0] _pipe_mul3;
  reg signed [46-1:0] _pipe_mul4;
  assign _mul = _a * _b;
  assign c = _pipe_mul4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _pipe_mul0 <= _mul;
      _pipe_mul1 <= _pipe_mul0;
      _pipe_mul2 <= _pipe_mul1;
      _pipe_mul3 <= _pipe_mul2;
      _pipe_mul4 <= _pipe_mul3;
    end 
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = dataflow_stencil.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
