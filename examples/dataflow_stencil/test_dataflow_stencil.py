from __future__ import absolute_import
from __future__ import print_function
import dataflow_stencil

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg start;
  wire busy;
  reg [4-1:0] ext_src_bram0_addr;
  wire [32-1:0] ext_src_bram0_rdata;
  reg [32-1:0] ext_src_bram0_wdata;
  reg ext_src_bram0_wenable;
  reg [4-1:0] ext_src_bram1_addr;
  wire [32-1:0] ext_src_bram1_rdata;
  reg [32-1:0] ext_src_bram1_wdata;
  reg ext_src_bram1_wenable;
  reg [4-1:0] ext_src_bram2_addr;
  wire [32-1:0] ext_src_bram2_rdata;
  reg [32-1:0] ext_src_bram2_wdata;
  reg ext_src_bram2_wenable;
  reg [4-1:0] ext_dst_bram_addr;
  wire [32-1:0] ext_dst_bram_rdata;
  reg [32-1:0] ext_dst_bram_wdata;
  reg ext_dst_bram_wenable;

  stencil
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .start(start),
    .busy(busy),
    .ext_src_bram0_addr(ext_src_bram0_addr),
    .ext_src_bram0_rdata(ext_src_bram0_rdata),
    .ext_src_bram0_wdata(ext_src_bram0_wdata),
    .ext_src_bram0_wenable(ext_src_bram0_wenable),
    .ext_src_bram1_addr(ext_src_bram1_addr),
    .ext_src_bram1_rdata(ext_src_bram1_rdata),
    .ext_src_bram1_wdata(ext_src_bram1_wdata),
    .ext_src_bram1_wenable(ext_src_bram1_wenable),
    .ext_src_bram2_addr(ext_src_bram2_addr),
    .ext_src_bram2_rdata(ext_src_bram2_rdata),
    .ext_src_bram2_wdata(ext_src_bram2_wdata),
    .ext_src_bram2_wenable(ext_src_bram2_wenable),
    .ext_dst_bram_addr(ext_dst_bram_addr),
    .ext_dst_bram_rdata(ext_dst_bram_rdata),
    .ext_dst_bram_wdata(ext_dst_bram_wdata),
    .ext_dst_bram_wenable(ext_dst_bram_wenable)
  );

  reg reset_done;

  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


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
    ext_src_bram0_addr = 0;
    ext_src_bram0_wdata = 0;
    ext_src_bram0_wenable = 0;
    ext_src_bram1_addr = 0;
    ext_src_bram1_wdata = 0;
    ext_src_bram1_wenable = 0;
    ext_src_bram2_addr = 0;
    ext_src_bram2_wdata = 0;
    ext_src_bram2_wenable = 0;
    ext_dst_bram_addr = 2;
    ext_dst_bram_wdata = 0;
    ext_dst_bram_wenable = 0;
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
          ext_src_bram0_addr <= -1;
          ext_src_bram1_addr <= -1;
          ext_src_bram2_addr <= -1;
          fsm <= fsm_2;
        end
        fsm_2: begin
          ext_src_bram0_addr <= ext_src_bram0_addr + 1;
          ext_src_bram0_wdata <= 5898240;
          ext_src_bram0_wenable <= 1;
          if(ext_src_bram0_wenable && (ext_src_bram0_addr == 15)) begin
            ext_src_bram0_wenable <= 0;
          end 
          ext_src_bram1_addr <= ext_src_bram1_addr + 1;
          ext_src_bram1_wdata <= 5898240;
          ext_src_bram1_wenable <= 1;
          if(ext_src_bram1_wenable && (ext_src_bram1_addr == 15)) begin
            ext_src_bram1_wenable <= 0;
          end 
          ext_src_bram2_addr <= ext_src_bram2_addr + 1;
          ext_src_bram2_wdata <= 5898240;
          ext_src_bram2_wenable <= 1;
          if(ext_src_bram2_wenable && (ext_src_bram2_addr == 15)) begin
            ext_src_bram2_wenable <= 0;
          end 
          if(ext_src_bram2_wenable && (ext_src_bram0_addr == 15)) begin
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
  input [4-1:0] ext_src_bram0_addr,
  output [32-1:0] ext_src_bram0_rdata,
  input [32-1:0] ext_src_bram0_wdata,
  input ext_src_bram0_wenable,
  input [4-1:0] ext_src_bram1_addr,
  output [32-1:0] ext_src_bram1_rdata,
  input [32-1:0] ext_src_bram1_wdata,
  input ext_src_bram1_wenable,
  input [4-1:0] ext_src_bram2_addr,
  output [32-1:0] ext_src_bram2_rdata,
  input [32-1:0] ext_src_bram2_wdata,
  input ext_src_bram2_wenable,
  input [4-1:0] ext_dst_bram_addr,
  output [32-1:0] ext_dst_bram_rdata,
  input [32-1:0] ext_dst_bram_wdata,
  input ext_dst_bram_wenable
);

  reg _tmp_0;
  reg [8-1:0] src_bram0_0_addr;
  wire [32-1:0] src_bram0_0_rdata;
  reg [32-1:0] src_bram0_0_wdata;
  reg src_bram0_0_wenable;
  reg [8-1:0] src_bram0_1_addr;
  wire [32-1:0] src_bram0_1_rdata;
  reg [32-1:0] src_bram0_1_wdata;
  reg src_bram0_1_wenable;

  src_bram0
  inst_src_bram0
  (
    .CLK(CLK),
    .src_bram0_0_addr(src_bram0_0_addr),
    .src_bram0_0_rdata(src_bram0_0_rdata),
    .src_bram0_0_wdata(src_bram0_0_wdata),
    .src_bram0_0_wenable(src_bram0_0_wenable),
    .src_bram0_1_addr(src_bram0_1_addr),
    .src_bram0_1_rdata(src_bram0_1_rdata),
    .src_bram0_1_wdata(src_bram0_1_wdata),
    .src_bram0_1_wenable(src_bram0_1_wenable)
  );

  reg [8-1:0] src_bram1_0_addr;
  wire [32-1:0] src_bram1_0_rdata;
  reg [32-1:0] src_bram1_0_wdata;
  reg src_bram1_0_wenable;
  reg [8-1:0] src_bram1_1_addr;
  wire [32-1:0] src_bram1_1_rdata;
  reg [32-1:0] src_bram1_1_wdata;
  reg src_bram1_1_wenable;

  src_bram1
  inst_src_bram1
  (
    .CLK(CLK),
    .src_bram1_0_addr(src_bram1_0_addr),
    .src_bram1_0_rdata(src_bram1_0_rdata),
    .src_bram1_0_wdata(src_bram1_0_wdata),
    .src_bram1_0_wenable(src_bram1_0_wenable),
    .src_bram1_1_addr(src_bram1_1_addr),
    .src_bram1_1_rdata(src_bram1_1_rdata),
    .src_bram1_1_wdata(src_bram1_1_wdata),
    .src_bram1_1_wenable(src_bram1_1_wenable)
  );

  reg [8-1:0] src_bram2_0_addr;
  wire [32-1:0] src_bram2_0_rdata;
  reg [32-1:0] src_bram2_0_wdata;
  reg src_bram2_0_wenable;
  reg [8-1:0] src_bram2_1_addr;
  wire [32-1:0] src_bram2_1_rdata;
  reg [32-1:0] src_bram2_1_wdata;
  reg src_bram2_1_wenable;

  src_bram2
  inst_src_bram2
  (
    .CLK(CLK),
    .src_bram2_0_addr(src_bram2_0_addr),
    .src_bram2_0_rdata(src_bram2_0_rdata),
    .src_bram2_0_wdata(src_bram2_0_wdata),
    .src_bram2_0_wenable(src_bram2_0_wenable),
    .src_bram2_1_addr(src_bram2_1_addr),
    .src_bram2_1_rdata(src_bram2_1_rdata),
    .src_bram2_1_wdata(src_bram2_1_wdata),
    .src_bram2_1_wenable(src_bram2_1_wenable)
  );

  reg [8-1:0] dst_bram_0_addr;
  wire [32-1:0] dst_bram_0_rdata;
  reg [32-1:0] dst_bram_0_wdata;
  reg dst_bram_0_wenable;
  reg [8-1:0] dst_bram_1_addr;
  wire [32-1:0] dst_bram_1_rdata;
  reg [32-1:0] dst_bram_1_wdata;
  reg dst_bram_1_wenable;

  dst_bram
  inst_dst_bram
  (
    .CLK(CLK),
    .dst_bram_0_addr(dst_bram_0_addr),
    .dst_bram_0_rdata(dst_bram_0_rdata),
    .dst_bram_0_wdata(dst_bram_0_wdata),
    .dst_bram_0_wenable(dst_bram_0_wenable),
    .dst_bram_1_addr(dst_bram_1_addr),
    .dst_bram_1_rdata(dst_bram_1_rdata),
    .dst_bram_1_wdata(dst_bram_1_wdata),
    .dst_bram_1_wenable(dst_bram_1_wenable)
  );


  always @(*) begin
    src_bram0_1_addr = ext_src_bram0_addr;
  end

  assign ext_src_bram0_rdata = src_bram0_1_rdata;

  always @(*) begin
    src_bram0_1_wdata = ext_src_bram0_wdata;
  end


  always @(*) begin
    src_bram0_1_wenable = ext_src_bram0_wenable;
  end


  always @(*) begin
    src_bram1_1_addr = ext_src_bram1_addr;
  end

  assign ext_src_bram1_rdata = src_bram1_1_rdata;

  always @(*) begin
    src_bram1_1_wdata = ext_src_bram1_wdata;
  end


  always @(*) begin
    src_bram1_1_wenable = ext_src_bram1_wenable;
  end


  always @(*) begin
    src_bram2_1_addr = ext_src_bram2_addr;
  end

  assign ext_src_bram2_rdata = src_bram2_1_rdata;

  always @(*) begin
    src_bram2_1_wdata = ext_src_bram2_wdata;
  end


  always @(*) begin
    src_bram2_1_wenable = ext_src_bram2_wenable;
  end


  always @(*) begin
    dst_bram_1_addr = ext_dst_bram_addr;
  end

  assign ext_dst_bram_rdata = dst_bram_1_rdata;

  always @(*) begin
    dst_bram_1_wdata = ext_dst_bram_wdata;
  end


  always @(*) begin
    dst_bram_1_wenable = ext_dst_bram_wenable;
  end

  reg [32-1:0] read_fsm;
  localparam read_fsm_init = 0;
  reg [32-1:0] read_count;
  reg [32-1:0] read_addr;
  reg _tmp_1;
  reg [32-1:0] _d1_read_fsm;
  reg _read_fsm_cond_1_0_1;
  reg [32-1:0] _d2_read_fsm;
  reg _read_fsm_cond_1_1_1;
  reg _read_fsm_cond_1_1_2;
  reg _tmp_2;
  reg _read_fsm_cond_1_2_1;
  reg _read_fsm_cond_1_3_1;
  reg _read_fsm_cond_1_3_2;
  reg _tmp_3;
  reg _read_fsm_cond_1_4_1;
  reg _read_fsm_cond_1_5_1;
  reg _read_fsm_cond_1_5_2;
  localparam read_fsm_1 = 1;
  localparam read_fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      read_fsm <= read_fsm_init;
      _d1_read_fsm <= read_fsm_init;
      _d2_read_fsm <= read_fsm_init;
      read_addr <= 0;
      read_count <= 0;
      busy <= 0;
      src_bram0_0_addr <= 0;
      _read_fsm_cond_1_0_1 <= 0;
      _tmp_1 <= 0;
      _read_fsm_cond_1_1_1 <= 0;
      _read_fsm_cond_1_1_2 <= 0;
      src_bram1_0_addr <= 0;
      _read_fsm_cond_1_2_1 <= 0;
      _tmp_2 <= 0;
      _read_fsm_cond_1_3_1 <= 0;
      _read_fsm_cond_1_3_2 <= 0;
      src_bram2_0_addr <= 0;
      _read_fsm_cond_1_4_1 <= 0;
      _tmp_3 <= 0;
      _read_fsm_cond_1_5_1 <= 0;
      _read_fsm_cond_1_5_2 <= 0;
    end else begin
      _d1_read_fsm <= read_fsm;
      _d2_read_fsm <= _d1_read_fsm;
      case(_d2_read_fsm)
        read_fsm_1: begin
          if(_read_fsm_cond_1_1_2) begin
            _tmp_1 <= 0;
          end 
          if(_read_fsm_cond_1_3_2) begin
            _tmp_2 <= 0;
          end 
          if(_read_fsm_cond_1_5_2) begin
            _tmp_3 <= 0;
          end 
        end
      endcase
      case(_d1_read_fsm)
        read_fsm_1: begin
          if(_read_fsm_cond_1_0_1) begin
            _tmp_1 <= 1;
          end 
          _read_fsm_cond_1_1_2 <= _read_fsm_cond_1_1_1;
          if(_read_fsm_cond_1_2_1) begin
            _tmp_2 <= 1;
          end 
          _read_fsm_cond_1_3_2 <= _read_fsm_cond_1_3_1;
          if(_read_fsm_cond_1_4_1) begin
            _tmp_3 <= 1;
          end 
          _read_fsm_cond_1_5_2 <= _read_fsm_cond_1_5_1;
        end
      endcase
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
          src_bram0_0_addr <= read_addr;
          _read_fsm_cond_1_0_1 <= 1;
          _read_fsm_cond_1_1_1 <= 1;
          src_bram1_0_addr <= read_addr;
          _read_fsm_cond_1_2_1 <= 1;
          _read_fsm_cond_1_3_1 <= 1;
          src_bram2_0_addr <= read_addr;
          _read_fsm_cond_1_4_1 <= 1;
          _read_fsm_cond_1_5_1 <= 1;
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
    .idata0(src_bram0_0_rdata),
    .ivalid0(_tmp_1),
    .idata1(src_bram1_0_rdata),
    .ivalid1(_tmp_2),
    .idata2(src_bram2_0_rdata),
    .ivalid2(_tmp_3),
    .odata(odata),
    .ovalid(ovalid)
  );

  reg [32-1:0] write_fsm;
  localparam write_fsm_init = 0;
  reg [32-1:0] write_count;
  reg [32-1:0] write_addr;
  reg [32-1:0] _d1_write_fsm;
  reg _write_fsm_cond_0_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      write_fsm <= write_fsm_init;
      _d1_write_fsm <= write_fsm_init;
      _tmp_0 <= 0;
      write_addr <= 1;
      dst_bram_0_addr <= 0;
      dst_bram_0_wdata <= 0;
      dst_bram_0_wenable <= 0;
      _write_fsm_cond_0_0_1 <= 0;
      write_count <= 0;
    end else begin
      _d1_write_fsm <= write_fsm;
      case(_d1_write_fsm)
        write_fsm_init: begin
          if(_write_fsm_cond_0_0_1) begin
            dst_bram_0_wenable <= 0;
          end 
        end
      endcase
      case(write_fsm)
        write_fsm_init: begin
          _tmp_0 <= 0;
          if(ovalid && (write_count > 1)) begin
            write_addr <= write_addr + 1;
          end 
          if(ovalid && (write_count > 1)) begin
            dst_bram_0_addr <= write_addr;
            dst_bram_0_wdata <= odata;
            dst_bram_0_wenable <= 1;
          end 
          _write_fsm_cond_0_0_1 <= 1;
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


endmodule



module src_bram0
(
  input CLK,
  input [8-1:0] src_bram0_0_addr,
  output [32-1:0] src_bram0_0_rdata,
  input [32-1:0] src_bram0_0_wdata,
  input src_bram0_0_wenable,
  input [8-1:0] src_bram0_1_addr,
  output [32-1:0] src_bram0_1_rdata,
  input [32-1:0] src_bram0_1_wdata,
  input src_bram0_1_wenable
);

  reg [8-1:0] src_bram0_0_daddr;
  reg [8-1:0] src_bram0_1_daddr;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(src_bram0_0_wenable) begin
      mem[src_bram0_0_addr] <= src_bram0_0_wdata;
    end 
    src_bram0_0_daddr <= src_bram0_0_addr;
  end

  assign src_bram0_0_rdata = mem[src_bram0_0_daddr];

  always @(posedge CLK) begin
    if(src_bram0_1_wenable) begin
      mem[src_bram0_1_addr] <= src_bram0_1_wdata;
    end 
    src_bram0_1_daddr <= src_bram0_1_addr;
  end

  assign src_bram0_1_rdata = mem[src_bram0_1_daddr];

endmodule



module src_bram1
(
  input CLK,
  input [8-1:0] src_bram1_0_addr,
  output [32-1:0] src_bram1_0_rdata,
  input [32-1:0] src_bram1_0_wdata,
  input src_bram1_0_wenable,
  input [8-1:0] src_bram1_1_addr,
  output [32-1:0] src_bram1_1_rdata,
  input [32-1:0] src_bram1_1_wdata,
  input src_bram1_1_wenable
);

  reg [8-1:0] src_bram1_0_daddr;
  reg [8-1:0] src_bram1_1_daddr;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(src_bram1_0_wenable) begin
      mem[src_bram1_0_addr] <= src_bram1_0_wdata;
    end 
    src_bram1_0_daddr <= src_bram1_0_addr;
  end

  assign src_bram1_0_rdata = mem[src_bram1_0_daddr];

  always @(posedge CLK) begin
    if(src_bram1_1_wenable) begin
      mem[src_bram1_1_addr] <= src_bram1_1_wdata;
    end 
    src_bram1_1_daddr <= src_bram1_1_addr;
  end

  assign src_bram1_1_rdata = mem[src_bram1_1_daddr];

endmodule



module src_bram2
(
  input CLK,
  input [8-1:0] src_bram2_0_addr,
  output [32-1:0] src_bram2_0_rdata,
  input [32-1:0] src_bram2_0_wdata,
  input src_bram2_0_wenable,
  input [8-1:0] src_bram2_1_addr,
  output [32-1:0] src_bram2_1_rdata,
  input [32-1:0] src_bram2_1_wdata,
  input src_bram2_1_wenable
);

  reg [8-1:0] src_bram2_0_daddr;
  reg [8-1:0] src_bram2_1_daddr;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(src_bram2_0_wenable) begin
      mem[src_bram2_0_addr] <= src_bram2_0_wdata;
    end 
    src_bram2_0_daddr <= src_bram2_0_addr;
  end

  assign src_bram2_0_rdata = mem[src_bram2_0_daddr];

  always @(posedge CLK) begin
    if(src_bram2_1_wenable) begin
      mem[src_bram2_1_addr] <= src_bram2_1_wdata;
    end 
    src_bram2_1_daddr <= src_bram2_1_addr;
  end

  assign src_bram2_1_rdata = mem[src_bram2_1_daddr];

endmodule



module dst_bram
(
  input CLK,
  input [8-1:0] dst_bram_0_addr,
  output [32-1:0] dst_bram_0_rdata,
  input [32-1:0] dst_bram_0_wdata,
  input dst_bram_0_wenable,
  input [8-1:0] dst_bram_1_addr,
  output [32-1:0] dst_bram_1_rdata,
  input [32-1:0] dst_bram_1_wdata,
  input dst_bram_1_wenable
);

  reg [8-1:0] dst_bram_0_daddr;
  reg [8-1:0] dst_bram_1_daddr;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(dst_bram_0_wenable) begin
      mem[dst_bram_0_addr] <= dst_bram_0_wdata;
    end 
    dst_bram_0_daddr <= dst_bram_0_addr;
  end

  assign dst_bram_0_rdata = mem[dst_bram_0_daddr];

  always @(posedge CLK) begin
    if(dst_bram_1_wenable) begin
      mem[dst_bram_1_addr] <= dst_bram_1_wdata;
    end 
    dst_bram_1_daddr <= dst_bram_1_addr;
  end

  assign dst_bram_1_rdata = mem[dst_bram_1_daddr];

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

  reg signed [32-1:0] _tmp_data_0;
  reg signed [32-1:0] _tmp_data_1;
  reg signed [32-1:0] _tmp_data_2;
  reg signed [32-1:0] _tmp_data_3;
  reg signed [32-1:0] _tmp_data_4;
  reg signed [32-1:0] _tmp_data_5;
  wire signed [32-1:0] _tmp_data_6;
  wire _tmp_valid_6;
  wire _tmp_ready_6;
  wire signed [46-1:0] _tmp_odata_6;
  reg signed [46-1:0] _tmp_data_reg_6;
  assign _tmp_data_6 = _tmp_data_reg_6;
  wire _tmp_ovalid_6;
  reg _tmp_valid_reg_6;
  assign _tmp_valid_6 = _tmp_valid_reg_6;
  wire _tmp_enable_6;
  wire _tmp_update_6;
  assign _tmp_enable_6 = (_tmp_ready_6 || !_tmp_valid_6) && 1 && ivalid0;
  assign _tmp_update_6 = _tmp_ready_6 || !_tmp_valid_6;

  multiplier_0
  mul6
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_6),
    .enable(_tmp_enable_6),
    .valid(_tmp_ovalid_6),
    .a(idata0),
    .b(14'd7281),
    .c(_tmp_odata_6)
  );

  assign _tmp_ready_6 = (_tmp_ready_15 || !_tmp_valid_15) && (_tmp_valid_6 && _tmp_valid_7);
  wire signed [32-1:0] _tmp_data_7;
  wire _tmp_valid_7;
  wire _tmp_ready_7;
  wire signed [46-1:0] _tmp_odata_7;
  reg signed [46-1:0] _tmp_data_reg_7;
  assign _tmp_data_7 = _tmp_data_reg_7;
  wire _tmp_ovalid_7;
  reg _tmp_valid_reg_7;
  assign _tmp_valid_7 = _tmp_valid_reg_7;
  wire _tmp_enable_7;
  wire _tmp_update_7;
  assign _tmp_enable_7 = (_tmp_ready_7 || !_tmp_valid_7) && 1 && ivalid0;
  assign _tmp_update_7 = _tmp_ready_7 || !_tmp_valid_7;

  multiplier_1
  mul7
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_7),
    .enable(_tmp_enable_7),
    .valid(_tmp_ovalid_7),
    .a(_tmp_data_0),
    .b(14'd7281),
    .c(_tmp_odata_7)
  );

  assign _tmp_ready_7 = (_tmp_ready_15 || !_tmp_valid_15) && (_tmp_valid_6 && _tmp_valid_7);
  wire signed [32-1:0] _tmp_data_8;
  wire _tmp_valid_8;
  wire _tmp_ready_8;
  wire signed [46-1:0] _tmp_odata_8;
  reg signed [46-1:0] _tmp_data_reg_8;
  assign _tmp_data_8 = _tmp_data_reg_8;
  wire _tmp_ovalid_8;
  reg _tmp_valid_reg_8;
  assign _tmp_valid_8 = _tmp_valid_reg_8;
  wire _tmp_enable_8;
  wire _tmp_update_8;
  assign _tmp_enable_8 = (_tmp_ready_8 || !_tmp_valid_8) && 1 && ivalid0;
  assign _tmp_update_8 = _tmp_ready_8 || !_tmp_valid_8;

  multiplier_2
  mul8
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_8),
    .enable(_tmp_enable_8),
    .valid(_tmp_ovalid_8),
    .a(_tmp_data_1),
    .b(14'd7281),
    .c(_tmp_odata_8)
  );

  assign _tmp_ready_8 = (_tmp_ready_16 || !_tmp_valid_16) && _tmp_valid_8;
  wire signed [32-1:0] _tmp_data_9;
  wire _tmp_valid_9;
  wire _tmp_ready_9;
  wire signed [46-1:0] _tmp_odata_9;
  reg signed [46-1:0] _tmp_data_reg_9;
  assign _tmp_data_9 = _tmp_data_reg_9;
  wire _tmp_ovalid_9;
  reg _tmp_valid_reg_9;
  assign _tmp_valid_9 = _tmp_valid_reg_9;
  wire _tmp_enable_9;
  wire _tmp_update_9;
  assign _tmp_enable_9 = (_tmp_ready_9 || !_tmp_valid_9) && 1 && ivalid1;
  assign _tmp_update_9 = _tmp_ready_9 || !_tmp_valid_9;

  multiplier_3
  mul9
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_9),
    .enable(_tmp_enable_9),
    .valid(_tmp_ovalid_9),
    .a(idata1),
    .b(14'd7281),
    .c(_tmp_odata_9)
  );

  assign _tmp_ready_9 = (_tmp_ready_17 || !_tmp_valid_17) && _tmp_valid_9;
  wire signed [32-1:0] _tmp_data_10;
  wire _tmp_valid_10;
  wire _tmp_ready_10;
  wire signed [46-1:0] _tmp_odata_10;
  reg signed [46-1:0] _tmp_data_reg_10;
  assign _tmp_data_10 = _tmp_data_reg_10;
  wire _tmp_ovalid_10;
  reg _tmp_valid_reg_10;
  assign _tmp_valid_10 = _tmp_valid_reg_10;
  wire _tmp_enable_10;
  wire _tmp_update_10;
  assign _tmp_enable_10 = (_tmp_ready_10 || !_tmp_valid_10) && 1 && ivalid1;
  assign _tmp_update_10 = _tmp_ready_10 || !_tmp_valid_10;

  multiplier_4
  mul10
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_10),
    .enable(_tmp_enable_10),
    .valid(_tmp_ovalid_10),
    .a(_tmp_data_2),
    .b(14'd7281),
    .c(_tmp_odata_10)
  );

  assign _tmp_ready_10 = (_tmp_ready_18 || !_tmp_valid_18) && _tmp_valid_10;
  wire signed [32-1:0] _tmp_data_11;
  wire _tmp_valid_11;
  wire _tmp_ready_11;
  wire signed [46-1:0] _tmp_odata_11;
  reg signed [46-1:0] _tmp_data_reg_11;
  assign _tmp_data_11 = _tmp_data_reg_11;
  wire _tmp_ovalid_11;
  reg _tmp_valid_reg_11;
  assign _tmp_valid_11 = _tmp_valid_reg_11;
  wire _tmp_enable_11;
  wire _tmp_update_11;
  assign _tmp_enable_11 = (_tmp_ready_11 || !_tmp_valid_11) && 1 && ivalid1;
  assign _tmp_update_11 = _tmp_ready_11 || !_tmp_valid_11;

  multiplier_5
  mul11
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_11),
    .enable(_tmp_enable_11),
    .valid(_tmp_ovalid_11),
    .a(_tmp_data_3),
    .b(14'd7281),
    .c(_tmp_odata_11)
  );

  assign _tmp_ready_11 = (_tmp_ready_19 || !_tmp_valid_19) && _tmp_valid_11;
  wire signed [32-1:0] _tmp_data_12;
  wire _tmp_valid_12;
  wire _tmp_ready_12;
  wire signed [46-1:0] _tmp_odata_12;
  reg signed [46-1:0] _tmp_data_reg_12;
  assign _tmp_data_12 = _tmp_data_reg_12;
  wire _tmp_ovalid_12;
  reg _tmp_valid_reg_12;
  assign _tmp_valid_12 = _tmp_valid_reg_12;
  wire _tmp_enable_12;
  wire _tmp_update_12;
  assign _tmp_enable_12 = (_tmp_ready_12 || !_tmp_valid_12) && 1 && ivalid2;
  assign _tmp_update_12 = _tmp_ready_12 || !_tmp_valid_12;

  multiplier_6
  mul12
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_12),
    .enable(_tmp_enable_12),
    .valid(_tmp_ovalid_12),
    .a(idata2),
    .b(14'd7281),
    .c(_tmp_odata_12)
  );

  assign _tmp_ready_12 = (_tmp_ready_20 || !_tmp_valid_20) && _tmp_valid_12;
  wire signed [32-1:0] _tmp_data_13;
  wire _tmp_valid_13;
  wire _tmp_ready_13;
  wire signed [46-1:0] _tmp_odata_13;
  reg signed [46-1:0] _tmp_data_reg_13;
  assign _tmp_data_13 = _tmp_data_reg_13;
  wire _tmp_ovalid_13;
  reg _tmp_valid_reg_13;
  assign _tmp_valid_13 = _tmp_valid_reg_13;
  wire _tmp_enable_13;
  wire _tmp_update_13;
  assign _tmp_enable_13 = (_tmp_ready_13 || !_tmp_valid_13) && 1 && ivalid2;
  assign _tmp_update_13 = _tmp_ready_13 || !_tmp_valid_13;

  multiplier_7
  mul13
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_13),
    .enable(_tmp_enable_13),
    .valid(_tmp_ovalid_13),
    .a(_tmp_data_4),
    .b(14'd7281),
    .c(_tmp_odata_13)
  );

  assign _tmp_ready_13 = (_tmp_ready_21 || !_tmp_valid_21) && _tmp_valid_13;
  wire signed [32-1:0] _tmp_data_14;
  wire _tmp_valid_14;
  wire _tmp_ready_14;
  wire signed [46-1:0] _tmp_odata_14;
  reg signed [46-1:0] _tmp_data_reg_14;
  assign _tmp_data_14 = _tmp_data_reg_14;
  wire _tmp_ovalid_14;
  reg _tmp_valid_reg_14;
  assign _tmp_valid_14 = _tmp_valid_reg_14;
  wire _tmp_enable_14;
  wire _tmp_update_14;
  assign _tmp_enable_14 = (_tmp_ready_14 || !_tmp_valid_14) && 1 && ivalid2;
  assign _tmp_update_14 = _tmp_ready_14 || !_tmp_valid_14;

  multiplier_8
  mul14
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_14),
    .enable(_tmp_enable_14),
    .valid(_tmp_ovalid_14),
    .a(_tmp_data_5),
    .b(14'd7281),
    .c(_tmp_odata_14)
  );

  assign _tmp_ready_14 = (_tmp_ready_22 || !_tmp_valid_22) && _tmp_valid_14;
  reg signed [32-1:0] _tmp_data_15;
  reg _tmp_valid_15;
  wire _tmp_ready_15;
  assign _tmp_ready_15 = (_tmp_ready_23 || !_tmp_valid_23) && (_tmp_valid_15 && _tmp_valid_16);
  reg signed [32-1:0] _tmp_data_16;
  reg _tmp_valid_16;
  wire _tmp_ready_16;
  assign _tmp_ready_16 = (_tmp_ready_23 || !_tmp_valid_23) && (_tmp_valid_15 && _tmp_valid_16);
  reg signed [32-1:0] _tmp_data_17;
  reg _tmp_valid_17;
  wire _tmp_ready_17;
  assign _tmp_ready_17 = (_tmp_ready_24 || !_tmp_valid_24) && _tmp_valid_17;
  reg signed [32-1:0] _tmp_data_18;
  reg _tmp_valid_18;
  wire _tmp_ready_18;
  assign _tmp_ready_18 = (_tmp_ready_25 || !_tmp_valid_25) && _tmp_valid_18;
  reg signed [32-1:0] _tmp_data_19;
  reg _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_ready_26 || !_tmp_valid_26) && _tmp_valid_19;
  reg signed [32-1:0] _tmp_data_20;
  reg _tmp_valid_20;
  wire _tmp_ready_20;
  assign _tmp_ready_20 = (_tmp_ready_27 || !_tmp_valid_27) && _tmp_valid_20;
  reg signed [32-1:0] _tmp_data_21;
  reg _tmp_valid_21;
  wire _tmp_ready_21;
  assign _tmp_ready_21 = (_tmp_ready_28 || !_tmp_valid_28) && _tmp_valid_21;
  reg signed [32-1:0] _tmp_data_22;
  reg _tmp_valid_22;
  wire _tmp_ready_22;
  assign _tmp_ready_22 = (_tmp_ready_29 || !_tmp_valid_29) && _tmp_valid_22;
  reg signed [32-1:0] _tmp_data_23;
  reg _tmp_valid_23;
  wire _tmp_ready_23;
  assign _tmp_ready_23 = (_tmp_ready_30 || !_tmp_valid_30) && (_tmp_valid_23 && _tmp_valid_24);
  reg signed [32-1:0] _tmp_data_24;
  reg _tmp_valid_24;
  wire _tmp_ready_24;
  assign _tmp_ready_24 = (_tmp_ready_30 || !_tmp_valid_30) && (_tmp_valid_23 && _tmp_valid_24);
  reg signed [32-1:0] _tmp_data_25;
  reg _tmp_valid_25;
  wire _tmp_ready_25;
  assign _tmp_ready_25 = (_tmp_ready_31 || !_tmp_valid_31) && _tmp_valid_25;
  reg signed [32-1:0] _tmp_data_26;
  reg _tmp_valid_26;
  wire _tmp_ready_26;
  assign _tmp_ready_26 = (_tmp_ready_32 || !_tmp_valid_32) && _tmp_valid_26;
  reg signed [32-1:0] _tmp_data_27;
  reg _tmp_valid_27;
  wire _tmp_ready_27;
  assign _tmp_ready_27 = (_tmp_ready_33 || !_tmp_valid_33) && _tmp_valid_27;
  reg signed [32-1:0] _tmp_data_28;
  reg _tmp_valid_28;
  wire _tmp_ready_28;
  assign _tmp_ready_28 = (_tmp_ready_34 || !_tmp_valid_34) && _tmp_valid_28;
  reg signed [32-1:0] _tmp_data_29;
  reg _tmp_valid_29;
  wire _tmp_ready_29;
  assign _tmp_ready_29 = (_tmp_ready_35 || !_tmp_valid_35) && _tmp_valid_29;
  reg signed [32-1:0] _tmp_data_30;
  reg _tmp_valid_30;
  wire _tmp_ready_30;
  assign _tmp_ready_30 = (_tmp_ready_36 || !_tmp_valid_36) && (_tmp_valid_30 && _tmp_valid_31);
  reg signed [32-1:0] _tmp_data_31;
  reg _tmp_valid_31;
  wire _tmp_ready_31;
  assign _tmp_ready_31 = (_tmp_ready_36 || !_tmp_valid_36) && (_tmp_valid_30 && _tmp_valid_31);
  reg signed [32-1:0] _tmp_data_32;
  reg _tmp_valid_32;
  wire _tmp_ready_32;
  assign _tmp_ready_32 = (_tmp_ready_37 || !_tmp_valid_37) && _tmp_valid_32;
  reg signed [32-1:0] _tmp_data_33;
  reg _tmp_valid_33;
  wire _tmp_ready_33;
  assign _tmp_ready_33 = (_tmp_ready_38 || !_tmp_valid_38) && _tmp_valid_33;
  reg signed [32-1:0] _tmp_data_34;
  reg _tmp_valid_34;
  wire _tmp_ready_34;
  assign _tmp_ready_34 = (_tmp_ready_39 || !_tmp_valid_39) && _tmp_valid_34;
  reg signed [32-1:0] _tmp_data_35;
  reg _tmp_valid_35;
  wire _tmp_ready_35;
  assign _tmp_ready_35 = (_tmp_ready_40 || !_tmp_valid_40) && _tmp_valid_35;
  reg signed [32-1:0] _tmp_data_36;
  reg _tmp_valid_36;
  wire _tmp_ready_36;
  assign _tmp_ready_36 = (_tmp_ready_41 || !_tmp_valid_41) && (_tmp_valid_36 && _tmp_valid_37);
  reg signed [32-1:0] _tmp_data_37;
  reg _tmp_valid_37;
  wire _tmp_ready_37;
  assign _tmp_ready_37 = (_tmp_ready_41 || !_tmp_valid_41) && (_tmp_valid_36 && _tmp_valid_37);
  reg signed [32-1:0] _tmp_data_38;
  reg _tmp_valid_38;
  wire _tmp_ready_38;
  assign _tmp_ready_38 = (_tmp_ready_42 || !_tmp_valid_42) && _tmp_valid_38;
  reg signed [32-1:0] _tmp_data_39;
  reg _tmp_valid_39;
  wire _tmp_ready_39;
  assign _tmp_ready_39 = (_tmp_ready_43 || !_tmp_valid_43) && _tmp_valid_39;
  reg signed [32-1:0] _tmp_data_40;
  reg _tmp_valid_40;
  wire _tmp_ready_40;
  assign _tmp_ready_40 = (_tmp_ready_44 || !_tmp_valid_44) && _tmp_valid_40;
  reg signed [32-1:0] _tmp_data_41;
  reg _tmp_valid_41;
  wire _tmp_ready_41;
  assign _tmp_ready_41 = (_tmp_ready_45 || !_tmp_valid_45) && (_tmp_valid_41 && _tmp_valid_42);
  reg signed [32-1:0] _tmp_data_42;
  reg _tmp_valid_42;
  wire _tmp_ready_42;
  assign _tmp_ready_42 = (_tmp_ready_45 || !_tmp_valid_45) && (_tmp_valid_41 && _tmp_valid_42);
  reg signed [32-1:0] _tmp_data_43;
  reg _tmp_valid_43;
  wire _tmp_ready_43;
  assign _tmp_ready_43 = (_tmp_ready_46 || !_tmp_valid_46) && _tmp_valid_43;
  reg signed [32-1:0] _tmp_data_44;
  reg _tmp_valid_44;
  wire _tmp_ready_44;
  assign _tmp_ready_44 = (_tmp_ready_47 || !_tmp_valid_47) && _tmp_valid_44;
  reg signed [32-1:0] _tmp_data_45;
  reg _tmp_valid_45;
  wire _tmp_ready_45;
  assign _tmp_ready_45 = (_tmp_ready_48 || !_tmp_valid_48) && (_tmp_valid_45 && _tmp_valid_46);
  reg signed [32-1:0] _tmp_data_46;
  reg _tmp_valid_46;
  wire _tmp_ready_46;
  assign _tmp_ready_46 = (_tmp_ready_48 || !_tmp_valid_48) && (_tmp_valid_45 && _tmp_valid_46);
  reg signed [32-1:0] _tmp_data_47;
  reg _tmp_valid_47;
  wire _tmp_ready_47;
  assign _tmp_ready_47 = (_tmp_ready_49 || !_tmp_valid_49) && _tmp_valid_47;
  reg signed [32-1:0] _tmp_data_48;
  reg _tmp_valid_48;
  wire _tmp_ready_48;
  assign _tmp_ready_48 = (_tmp_ready_50 || !_tmp_valid_50) && (_tmp_valid_48 && _tmp_valid_49);
  reg signed [32-1:0] _tmp_data_49;
  reg _tmp_valid_49;
  wire _tmp_ready_49;
  assign _tmp_ready_49 = (_tmp_ready_50 || !_tmp_valid_50) && (_tmp_valid_48 && _tmp_valid_49);
  reg signed [32-1:0] _tmp_data_50;
  reg _tmp_valid_50;
  wire _tmp_ready_50;
  assign odata = _tmp_data_50;
  assign ovalid = _tmp_valid_50;
  assign _tmp_ready_50 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_data_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_data_reg_6 <= 0;
      _tmp_valid_reg_6 <= 0;
      _tmp_data_reg_7 <= 0;
      _tmp_valid_reg_7 <= 0;
      _tmp_data_reg_8 <= 0;
      _tmp_valid_reg_8 <= 0;
      _tmp_data_reg_9 <= 0;
      _tmp_valid_reg_9 <= 0;
      _tmp_data_reg_10 <= 0;
      _tmp_valid_reg_10 <= 0;
      _tmp_data_reg_11 <= 0;
      _tmp_valid_reg_11 <= 0;
      _tmp_data_reg_12 <= 0;
      _tmp_valid_reg_12 <= 0;
      _tmp_data_reg_13 <= 0;
      _tmp_valid_reg_13 <= 0;
      _tmp_data_reg_14 <= 0;
      _tmp_valid_reg_14 <= 0;
      _tmp_data_15 <= 0;
      _tmp_valid_15 <= 0;
      _tmp_data_16 <= 0;
      _tmp_valid_16 <= 0;
      _tmp_data_17 <= 0;
      _tmp_valid_17 <= 0;
      _tmp_data_18 <= 0;
      _tmp_valid_18 <= 0;
      _tmp_data_19 <= 0;
      _tmp_valid_19 <= 0;
      _tmp_data_20 <= 0;
      _tmp_valid_20 <= 0;
      _tmp_data_21 <= 0;
      _tmp_valid_21 <= 0;
      _tmp_data_22 <= 0;
      _tmp_valid_22 <= 0;
      _tmp_data_23 <= 0;
      _tmp_valid_23 <= 0;
      _tmp_data_24 <= 0;
      _tmp_valid_24 <= 0;
      _tmp_data_25 <= 0;
      _tmp_valid_25 <= 0;
      _tmp_data_26 <= 0;
      _tmp_valid_26 <= 0;
      _tmp_data_27 <= 0;
      _tmp_valid_27 <= 0;
      _tmp_data_28 <= 0;
      _tmp_valid_28 <= 0;
      _tmp_data_29 <= 0;
      _tmp_valid_29 <= 0;
      _tmp_data_30 <= 0;
      _tmp_valid_30 <= 0;
      _tmp_data_31 <= 0;
      _tmp_valid_31 <= 0;
      _tmp_data_32 <= 0;
      _tmp_valid_32 <= 0;
      _tmp_data_33 <= 0;
      _tmp_valid_33 <= 0;
      _tmp_data_34 <= 0;
      _tmp_valid_34 <= 0;
      _tmp_data_35 <= 0;
      _tmp_valid_35 <= 0;
      _tmp_data_36 <= 0;
      _tmp_valid_36 <= 0;
      _tmp_data_37 <= 0;
      _tmp_valid_37 <= 0;
      _tmp_data_38 <= 0;
      _tmp_valid_38 <= 0;
      _tmp_data_39 <= 0;
      _tmp_valid_39 <= 0;
      _tmp_data_40 <= 0;
      _tmp_valid_40 <= 0;
      _tmp_data_41 <= 0;
      _tmp_valid_41 <= 0;
      _tmp_data_42 <= 0;
      _tmp_valid_42 <= 0;
      _tmp_data_43 <= 0;
      _tmp_valid_43 <= 0;
      _tmp_data_44 <= 0;
      _tmp_valid_44 <= 0;
      _tmp_data_45 <= 0;
      _tmp_valid_45 <= 0;
      _tmp_data_46 <= 0;
      _tmp_valid_46 <= 0;
      _tmp_data_47 <= 0;
      _tmp_valid_47 <= 0;
      _tmp_data_48 <= 0;
      _tmp_valid_48 <= 0;
      _tmp_data_49 <= 0;
      _tmp_valid_49 <= 0;
      _tmp_data_50 <= 0;
      _tmp_valid_50 <= 0;
    end else begin
      if(ivalid0) begin
        _tmp_data_0 <= idata0;
      end 
      if(ivalid0) begin
        _tmp_data_1 <= _tmp_data_0;
      end 
      if(ivalid1) begin
        _tmp_data_2 <= idata1;
      end 
      if(ivalid1) begin
        _tmp_data_3 <= _tmp_data_2;
      end 
      if(ivalid2) begin
        _tmp_data_4 <= idata2;
      end 
      if(ivalid2) begin
        _tmp_data_5 <= _tmp_data_4;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_data_reg_6 <= _tmp_odata_6 >>> 16;
      end 
      if(_tmp_ready_6 || !_tmp_valid_6) begin
        _tmp_valid_reg_6 <= _tmp_ovalid_6;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_data_reg_7 <= _tmp_odata_7 >>> 16;
      end 
      if(_tmp_ready_7 || !_tmp_valid_7) begin
        _tmp_valid_reg_7 <= _tmp_ovalid_7;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_data_reg_8 <= _tmp_odata_8 >>> 16;
      end 
      if(_tmp_ready_8 || !_tmp_valid_8) begin
        _tmp_valid_reg_8 <= _tmp_ovalid_8;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_data_reg_9 <= _tmp_odata_9 >>> 16;
      end 
      if(_tmp_ready_9 || !_tmp_valid_9) begin
        _tmp_valid_reg_9 <= _tmp_ovalid_9;
      end 
      if(_tmp_ready_10 || !_tmp_valid_10) begin
        _tmp_data_reg_10 <= _tmp_odata_10 >>> 16;
      end 
      if(_tmp_ready_10 || !_tmp_valid_10) begin
        _tmp_valid_reg_10 <= _tmp_ovalid_10;
      end 
      if(_tmp_ready_11 || !_tmp_valid_11) begin
        _tmp_data_reg_11 <= _tmp_odata_11 >>> 16;
      end 
      if(_tmp_ready_11 || !_tmp_valid_11) begin
        _tmp_valid_reg_11 <= _tmp_ovalid_11;
      end 
      if(_tmp_ready_12 || !_tmp_valid_12) begin
        _tmp_data_reg_12 <= _tmp_odata_12 >>> 16;
      end 
      if(_tmp_ready_12 || !_tmp_valid_12) begin
        _tmp_valid_reg_12 <= _tmp_ovalid_12;
      end 
      if(_tmp_ready_13 || !_tmp_valid_13) begin
        _tmp_data_reg_13 <= _tmp_odata_13 >>> 16;
      end 
      if(_tmp_ready_13 || !_tmp_valid_13) begin
        _tmp_valid_reg_13 <= _tmp_ovalid_13;
      end 
      if(_tmp_ready_14 || !_tmp_valid_14) begin
        _tmp_data_reg_14 <= _tmp_odata_14 >>> 16;
      end 
      if(_tmp_ready_14 || !_tmp_valid_14) begin
        _tmp_valid_reg_14 <= _tmp_ovalid_14;
      end 
      if((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_ready_6 && _tmp_ready_7) && (_tmp_valid_6 && _tmp_valid_7)) begin
        _tmp_data_15 <= $signed(_tmp_data_6) + $signed(_tmp_data_7);
      end 
      if(_tmp_valid_15 && _tmp_ready_15) begin
        _tmp_valid_15 <= 0;
      end 
      if((_tmp_ready_15 || !_tmp_valid_15) && (_tmp_ready_6 && _tmp_ready_7)) begin
        _tmp_valid_15 <= _tmp_valid_6 && _tmp_valid_7;
      end 
      if((_tmp_ready_16 || !_tmp_valid_16) && _tmp_ready_8 && _tmp_valid_8) begin
        _tmp_data_16 <= _tmp_data_8;
      end 
      if(_tmp_valid_16 && _tmp_ready_16) begin
        _tmp_valid_16 <= 0;
      end 
      if((_tmp_ready_16 || !_tmp_valid_16) && _tmp_ready_8) begin
        _tmp_valid_16 <= _tmp_valid_8;
      end 
      if((_tmp_ready_17 || !_tmp_valid_17) && _tmp_ready_9 && _tmp_valid_9) begin
        _tmp_data_17 <= _tmp_data_9;
      end 
      if(_tmp_valid_17 && _tmp_ready_17) begin
        _tmp_valid_17 <= 0;
      end 
      if((_tmp_ready_17 || !_tmp_valid_17) && _tmp_ready_9) begin
        _tmp_valid_17 <= _tmp_valid_9;
      end 
      if((_tmp_ready_18 || !_tmp_valid_18) && _tmp_ready_10 && _tmp_valid_10) begin
        _tmp_data_18 <= _tmp_data_10;
      end 
      if(_tmp_valid_18 && _tmp_ready_18) begin
        _tmp_valid_18 <= 0;
      end 
      if((_tmp_ready_18 || !_tmp_valid_18) && _tmp_ready_10) begin
        _tmp_valid_18 <= _tmp_valid_10;
      end 
      if((_tmp_ready_19 || !_tmp_valid_19) && _tmp_ready_11 && _tmp_valid_11) begin
        _tmp_data_19 <= _tmp_data_11;
      end 
      if(_tmp_valid_19 && _tmp_ready_19) begin
        _tmp_valid_19 <= 0;
      end 
      if((_tmp_ready_19 || !_tmp_valid_19) && _tmp_ready_11) begin
        _tmp_valid_19 <= _tmp_valid_11;
      end 
      if((_tmp_ready_20 || !_tmp_valid_20) && _tmp_ready_12 && _tmp_valid_12) begin
        _tmp_data_20 <= _tmp_data_12;
      end 
      if(_tmp_valid_20 && _tmp_ready_20) begin
        _tmp_valid_20 <= 0;
      end 
      if((_tmp_ready_20 || !_tmp_valid_20) && _tmp_ready_12) begin
        _tmp_valid_20 <= _tmp_valid_12;
      end 
      if((_tmp_ready_21 || !_tmp_valid_21) && _tmp_ready_13 && _tmp_valid_13) begin
        _tmp_data_21 <= _tmp_data_13;
      end 
      if(_tmp_valid_21 && _tmp_ready_21) begin
        _tmp_valid_21 <= 0;
      end 
      if((_tmp_ready_21 || !_tmp_valid_21) && _tmp_ready_13) begin
        _tmp_valid_21 <= _tmp_valid_13;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && _tmp_ready_14 && _tmp_valid_14) begin
        _tmp_data_22 <= _tmp_data_14;
      end 
      if(_tmp_valid_22 && _tmp_ready_22) begin
        _tmp_valid_22 <= 0;
      end 
      if((_tmp_ready_22 || !_tmp_valid_22) && _tmp_ready_14) begin
        _tmp_valid_22 <= _tmp_valid_14;
      end 
      if((_tmp_ready_23 || !_tmp_valid_23) && (_tmp_ready_15 && _tmp_ready_16) && (_tmp_valid_15 && _tmp_valid_16)) begin
        _tmp_data_23 <= $signed(_tmp_data_15) + $signed(_tmp_data_16);
      end 
      if(_tmp_valid_23 && _tmp_ready_23) begin
        _tmp_valid_23 <= 0;
      end 
      if((_tmp_ready_23 || !_tmp_valid_23) && (_tmp_ready_15 && _tmp_ready_16)) begin
        _tmp_valid_23 <= _tmp_valid_15 && _tmp_valid_16;
      end 
      if((_tmp_ready_24 || !_tmp_valid_24) && _tmp_ready_17 && _tmp_valid_17) begin
        _tmp_data_24 <= _tmp_data_17;
      end 
      if(_tmp_valid_24 && _tmp_ready_24) begin
        _tmp_valid_24 <= 0;
      end 
      if((_tmp_ready_24 || !_tmp_valid_24) && _tmp_ready_17) begin
        _tmp_valid_24 <= _tmp_valid_17;
      end 
      if((_tmp_ready_25 || !_tmp_valid_25) && _tmp_ready_18 && _tmp_valid_18) begin
        _tmp_data_25 <= _tmp_data_18;
      end 
      if(_tmp_valid_25 && _tmp_ready_25) begin
        _tmp_valid_25 <= 0;
      end 
      if((_tmp_ready_25 || !_tmp_valid_25) && _tmp_ready_18) begin
        _tmp_valid_25 <= _tmp_valid_18;
      end 
      if((_tmp_ready_26 || !_tmp_valid_26) && _tmp_ready_19 && _tmp_valid_19) begin
        _tmp_data_26 <= _tmp_data_19;
      end 
      if(_tmp_valid_26 && _tmp_ready_26) begin
        _tmp_valid_26 <= 0;
      end 
      if((_tmp_ready_26 || !_tmp_valid_26) && _tmp_ready_19) begin
        _tmp_valid_26 <= _tmp_valid_19;
      end 
      if((_tmp_ready_27 || !_tmp_valid_27) && _tmp_ready_20 && _tmp_valid_20) begin
        _tmp_data_27 <= _tmp_data_20;
      end 
      if(_tmp_valid_27 && _tmp_ready_27) begin
        _tmp_valid_27 <= 0;
      end 
      if((_tmp_ready_27 || !_tmp_valid_27) && _tmp_ready_20) begin
        _tmp_valid_27 <= _tmp_valid_20;
      end 
      if((_tmp_ready_28 || !_tmp_valid_28) && _tmp_ready_21 && _tmp_valid_21) begin
        _tmp_data_28 <= _tmp_data_21;
      end 
      if(_tmp_valid_28 && _tmp_ready_28) begin
        _tmp_valid_28 <= 0;
      end 
      if((_tmp_ready_28 || !_tmp_valid_28) && _tmp_ready_21) begin
        _tmp_valid_28 <= _tmp_valid_21;
      end 
      if((_tmp_ready_29 || !_tmp_valid_29) && _tmp_ready_22 && _tmp_valid_22) begin
        _tmp_data_29 <= _tmp_data_22;
      end 
      if(_tmp_valid_29 && _tmp_ready_29) begin
        _tmp_valid_29 <= 0;
      end 
      if((_tmp_ready_29 || !_tmp_valid_29) && _tmp_ready_22) begin
        _tmp_valid_29 <= _tmp_valid_22;
      end 
      if((_tmp_ready_30 || !_tmp_valid_30) && (_tmp_ready_23 && _tmp_ready_24) && (_tmp_valid_23 && _tmp_valid_24)) begin
        _tmp_data_30 <= $signed(_tmp_data_23) + $signed(_tmp_data_24);
      end 
      if(_tmp_valid_30 && _tmp_ready_30) begin
        _tmp_valid_30 <= 0;
      end 
      if((_tmp_ready_30 || !_tmp_valid_30) && (_tmp_ready_23 && _tmp_ready_24)) begin
        _tmp_valid_30 <= _tmp_valid_23 && _tmp_valid_24;
      end 
      if((_tmp_ready_31 || !_tmp_valid_31) && _tmp_ready_25 && _tmp_valid_25) begin
        _tmp_data_31 <= _tmp_data_25;
      end 
      if(_tmp_valid_31 && _tmp_ready_31) begin
        _tmp_valid_31 <= 0;
      end 
      if((_tmp_ready_31 || !_tmp_valid_31) && _tmp_ready_25) begin
        _tmp_valid_31 <= _tmp_valid_25;
      end 
      if((_tmp_ready_32 || !_tmp_valid_32) && _tmp_ready_26 && _tmp_valid_26) begin
        _tmp_data_32 <= _tmp_data_26;
      end 
      if(_tmp_valid_32 && _tmp_ready_32) begin
        _tmp_valid_32 <= 0;
      end 
      if((_tmp_ready_32 || !_tmp_valid_32) && _tmp_ready_26) begin
        _tmp_valid_32 <= _tmp_valid_26;
      end 
      if((_tmp_ready_33 || !_tmp_valid_33) && _tmp_ready_27 && _tmp_valid_27) begin
        _tmp_data_33 <= _tmp_data_27;
      end 
      if(_tmp_valid_33 && _tmp_ready_33) begin
        _tmp_valid_33 <= 0;
      end 
      if((_tmp_ready_33 || !_tmp_valid_33) && _tmp_ready_27) begin
        _tmp_valid_33 <= _tmp_valid_27;
      end 
      if((_tmp_ready_34 || !_tmp_valid_34) && _tmp_ready_28 && _tmp_valid_28) begin
        _tmp_data_34 <= _tmp_data_28;
      end 
      if(_tmp_valid_34 && _tmp_ready_34) begin
        _tmp_valid_34 <= 0;
      end 
      if((_tmp_ready_34 || !_tmp_valid_34) && _tmp_ready_28) begin
        _tmp_valid_34 <= _tmp_valid_28;
      end 
      if((_tmp_ready_35 || !_tmp_valid_35) && _tmp_ready_29 && _tmp_valid_29) begin
        _tmp_data_35 <= _tmp_data_29;
      end 
      if(_tmp_valid_35 && _tmp_ready_35) begin
        _tmp_valid_35 <= 0;
      end 
      if((_tmp_ready_35 || !_tmp_valid_35) && _tmp_ready_29) begin
        _tmp_valid_35 <= _tmp_valid_29;
      end 
      if((_tmp_ready_36 || !_tmp_valid_36) && (_tmp_ready_30 && _tmp_ready_31) && (_tmp_valid_30 && _tmp_valid_31)) begin
        _tmp_data_36 <= $signed(_tmp_data_30) + $signed(_tmp_data_31);
      end 
      if(_tmp_valid_36 && _tmp_ready_36) begin
        _tmp_valid_36 <= 0;
      end 
      if((_tmp_ready_36 || !_tmp_valid_36) && (_tmp_ready_30 && _tmp_ready_31)) begin
        _tmp_valid_36 <= _tmp_valid_30 && _tmp_valid_31;
      end 
      if((_tmp_ready_37 || !_tmp_valid_37) && _tmp_ready_32 && _tmp_valid_32) begin
        _tmp_data_37 <= _tmp_data_32;
      end 
      if(_tmp_valid_37 && _tmp_ready_37) begin
        _tmp_valid_37 <= 0;
      end 
      if((_tmp_ready_37 || !_tmp_valid_37) && _tmp_ready_32) begin
        _tmp_valid_37 <= _tmp_valid_32;
      end 
      if((_tmp_ready_38 || !_tmp_valid_38) && _tmp_ready_33 && _tmp_valid_33) begin
        _tmp_data_38 <= _tmp_data_33;
      end 
      if(_tmp_valid_38 && _tmp_ready_38) begin
        _tmp_valid_38 <= 0;
      end 
      if((_tmp_ready_38 || !_tmp_valid_38) && _tmp_ready_33) begin
        _tmp_valid_38 <= _tmp_valid_33;
      end 
      if((_tmp_ready_39 || !_tmp_valid_39) && _tmp_ready_34 && _tmp_valid_34) begin
        _tmp_data_39 <= _tmp_data_34;
      end 
      if(_tmp_valid_39 && _tmp_ready_39) begin
        _tmp_valid_39 <= 0;
      end 
      if((_tmp_ready_39 || !_tmp_valid_39) && _tmp_ready_34) begin
        _tmp_valid_39 <= _tmp_valid_34;
      end 
      if((_tmp_ready_40 || !_tmp_valid_40) && _tmp_ready_35 && _tmp_valid_35) begin
        _tmp_data_40 <= _tmp_data_35;
      end 
      if(_tmp_valid_40 && _tmp_ready_40) begin
        _tmp_valid_40 <= 0;
      end 
      if((_tmp_ready_40 || !_tmp_valid_40) && _tmp_ready_35) begin
        _tmp_valid_40 <= _tmp_valid_35;
      end 
      if((_tmp_ready_41 || !_tmp_valid_41) && (_tmp_ready_36 && _tmp_ready_37) && (_tmp_valid_36 && _tmp_valid_37)) begin
        _tmp_data_41 <= $signed(_tmp_data_36) + $signed(_tmp_data_37);
      end 
      if(_tmp_valid_41 && _tmp_ready_41) begin
        _tmp_valid_41 <= 0;
      end 
      if((_tmp_ready_41 || !_tmp_valid_41) && (_tmp_ready_36 && _tmp_ready_37)) begin
        _tmp_valid_41 <= _tmp_valid_36 && _tmp_valid_37;
      end 
      if((_tmp_ready_42 || !_tmp_valid_42) && _tmp_ready_38 && _tmp_valid_38) begin
        _tmp_data_42 <= _tmp_data_38;
      end 
      if(_tmp_valid_42 && _tmp_ready_42) begin
        _tmp_valid_42 <= 0;
      end 
      if((_tmp_ready_42 || !_tmp_valid_42) && _tmp_ready_38) begin
        _tmp_valid_42 <= _tmp_valid_38;
      end 
      if((_tmp_ready_43 || !_tmp_valid_43) && _tmp_ready_39 && _tmp_valid_39) begin
        _tmp_data_43 <= _tmp_data_39;
      end 
      if(_tmp_valid_43 && _tmp_ready_43) begin
        _tmp_valid_43 <= 0;
      end 
      if((_tmp_ready_43 || !_tmp_valid_43) && _tmp_ready_39) begin
        _tmp_valid_43 <= _tmp_valid_39;
      end 
      if((_tmp_ready_44 || !_tmp_valid_44) && _tmp_ready_40 && _tmp_valid_40) begin
        _tmp_data_44 <= _tmp_data_40;
      end 
      if(_tmp_valid_44 && _tmp_ready_44) begin
        _tmp_valid_44 <= 0;
      end 
      if((_tmp_ready_44 || !_tmp_valid_44) && _tmp_ready_40) begin
        _tmp_valid_44 <= _tmp_valid_40;
      end 
      if((_tmp_ready_45 || !_tmp_valid_45) && (_tmp_ready_41 && _tmp_ready_42) && (_tmp_valid_41 && _tmp_valid_42)) begin
        _tmp_data_45 <= $signed(_tmp_data_41) + $signed(_tmp_data_42);
      end 
      if(_tmp_valid_45 && _tmp_ready_45) begin
        _tmp_valid_45 <= 0;
      end 
      if((_tmp_ready_45 || !_tmp_valid_45) && (_tmp_ready_41 && _tmp_ready_42)) begin
        _tmp_valid_45 <= _tmp_valid_41 && _tmp_valid_42;
      end 
      if((_tmp_ready_46 || !_tmp_valid_46) && _tmp_ready_43 && _tmp_valid_43) begin
        _tmp_data_46 <= _tmp_data_43;
      end 
      if(_tmp_valid_46 && _tmp_ready_46) begin
        _tmp_valid_46 <= 0;
      end 
      if((_tmp_ready_46 || !_tmp_valid_46) && _tmp_ready_43) begin
        _tmp_valid_46 <= _tmp_valid_43;
      end 
      if((_tmp_ready_47 || !_tmp_valid_47) && _tmp_ready_44 && _tmp_valid_44) begin
        _tmp_data_47 <= _tmp_data_44;
      end 
      if(_tmp_valid_47 && _tmp_ready_47) begin
        _tmp_valid_47 <= 0;
      end 
      if((_tmp_ready_47 || !_tmp_valid_47) && _tmp_ready_44) begin
        _tmp_valid_47 <= _tmp_valid_44;
      end 
      if((_tmp_ready_48 || !_tmp_valid_48) && (_tmp_ready_45 && _tmp_ready_46) && (_tmp_valid_45 && _tmp_valid_46)) begin
        _tmp_data_48 <= $signed(_tmp_data_45) + $signed(_tmp_data_46);
      end 
      if(_tmp_valid_48 && _tmp_ready_48) begin
        _tmp_valid_48 <= 0;
      end 
      if((_tmp_ready_48 || !_tmp_valid_48) && (_tmp_ready_45 && _tmp_ready_46)) begin
        _tmp_valid_48 <= _tmp_valid_45 && _tmp_valid_46;
      end 
      if((_tmp_ready_49 || !_tmp_valid_49) && _tmp_ready_47 && _tmp_valid_47) begin
        _tmp_data_49 <= _tmp_data_47;
      end 
      if(_tmp_valid_49 && _tmp_ready_49) begin
        _tmp_valid_49 <= 0;
      end 
      if((_tmp_ready_49 || !_tmp_valid_49) && _tmp_ready_47) begin
        _tmp_valid_49 <= _tmp_valid_47;
      end 
      if((_tmp_ready_50 || !_tmp_valid_50) && (_tmp_ready_48 && _tmp_ready_49) && (_tmp_valid_48 && _tmp_valid_49)) begin
        _tmp_data_50 <= $signed(_tmp_data_48) + $signed(_tmp_data_49);
      end 
      if(_tmp_valid_50 && _tmp_ready_50) begin
        _tmp_valid_50 <= 0;
      end 
      if((_tmp_ready_50 || !_tmp_valid_50) && (_tmp_ready_48 && _tmp_ready_49)) begin
        _tmp_valid_50 <= _tmp_valid_48 && _tmp_valid_49;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
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
  reg signed [46-1:0] _tmpval0;
  reg signed [46-1:0] _tmpval1;
  reg signed [46-1:0] _tmpval2;
  reg signed [46-1:0] _tmpval3;
  reg signed [46-1:0] _tmpval4;
  wire signed [46-1:0] rslt;
  assign rslt = _a * _b;
  assign c = _tmpval4;

  always @(posedge CLK) begin
    if(update) begin
      _a <= a;
      _b <= b;
      _tmpval0 <= rslt;
      _tmpval1 <= _tmpval0;
      _tmpval2 <= _tmpval1;
      _tmpval3 <= _tmpval2;
      _tmpval4 <= _tmpval3;
    end 
  end


endmodule
"""

def test():
    test_module = dataflow_stencil.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
