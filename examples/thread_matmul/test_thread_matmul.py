from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_matmul

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [32-1:0] myaxi_rdata;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire memory_awvalid;
  reg memory_awready;
  wire [32-1:0] memory_wdata;
  wire [4-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire memory_arvalid;
  reg memory_arready;
  reg [32-1:0] memory_rdata;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("mymem.out", _memory_mem);
  end

  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_count;
  reg [32-1:0] _d1__memory_fsm;
  reg __memory_fsm_cond_100_0_1;
  reg __memory_fsm_cond_200_1_1;
  reg __memory_fsm_cond_211_2_1;
  assign memory_awaddr = myaxi_awaddr;
  assign memory_awlen = myaxi_awlen;
  assign memory_awvalid = myaxi_awvalid;
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    myaxi_awready = _tmp_0;
  end

  assign memory_wdata = myaxi_wdata;
  assign memory_wstrb = myaxi_wstrb;
  assign memory_wlast = myaxi_wlast;
  assign memory_wvalid = myaxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    myaxi_wready = _tmp_1;
  end

  assign memory_araddr = myaxi_araddr;
  assign memory_arlen = myaxi_arlen;
  assign memory_arvalid = myaxi_arvalid;
  wire _tmp_2;
  assign _tmp_2 = memory_arready;

  always @(*) begin
    myaxi_arready = _tmp_2;
  end


  always @(*) begin
    myaxi_rdata <= memory_rdata;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_rlast;

  always @(*) begin
    myaxi_rlast = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = memory_rvalid;

  always @(*) begin
    myaxi_rvalid = _tmp_4;
  end

  assign memory_rready = myaxi_rready;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


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
    memory_awready = 0;
    memory_wready = 0;
    memory_arready = 0;
    memory_rdata = 0;
    memory_rlast = 0;
    memory_rvalid = 0;
    _memory_fsm = _memory_fsm_init;
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_count = 0;
    _d1__memory_fsm = _memory_fsm_init;
    __memory_fsm_cond_100_0_1 = 0;
    __memory_fsm_cond_200_1_1 = 0;
    __memory_fsm_cond_211_2_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000000;
    $finish;
  end

  localparam _memory_fsm_200 = 200;
  localparam _memory_fsm_201 = 201;
  localparam _memory_fsm_202 = 202;
  localparam _memory_fsm_203 = 203;
  localparam _memory_fsm_204 = 204;
  localparam _memory_fsm_205 = 205;
  localparam _memory_fsm_206 = 206;
  localparam _memory_fsm_207 = 207;
  localparam _memory_fsm_208 = 208;
  localparam _memory_fsm_209 = 209;
  localparam _memory_fsm_210 = 210;
  localparam _memory_fsm_211 = 211;
  localparam _memory_fsm_100 = 100;
  localparam _memory_fsm_101 = 101;
  localparam _memory_fsm_102 = 102;
  localparam _memory_fsm_103 = 103;
  localparam _memory_fsm_104 = 104;
  localparam _memory_fsm_105 = 105;
  localparam _memory_fsm_106 = 106;
  localparam _memory_fsm_107 = 107;
  localparam _memory_fsm_108 = 108;
  localparam _memory_fsm_109 = 109;
  localparam _memory_fsm_110 = 110;
  localparam _memory_fsm_111 = 111;
  localparam _memory_fsm_112 = 112;

  always @(posedge CLK) begin
    if(RST) begin
      _memory_fsm <= _memory_fsm_init;
      _d1__memory_fsm <= _memory_fsm_init;
      memory_awready <= 0;
      _write_addr <= 0;
      _write_count <= 0;
      __memory_fsm_cond_100_0_1 <= 0;
      memory_wready <= 0;
      memory_arready <= 0;
      _read_addr <= 0;
      _read_count <= 0;
      __memory_fsm_cond_200_1_1 <= 0;
      memory_rdata[7:0] <= (0 >> 0) & { 8{ 1'd1 } };
      memory_rdata[15:8] <= (0 >> 8) & { 8{ 1'd1 } };
      memory_rdata[23:16] <= (0 >> 16) & { 8{ 1'd1 } };
      memory_rdata[31:24] <= (0 >> 24) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_fsm_cond_211_2_1 <= 0;
      memory_rdata <= 0;
      _sleep_count <= 0;
    end else begin
      _sleep_count <= _sleep_count + 1;
      if(_sleep_count == 3) begin
        _sleep_count <= 0;
      end 
      _d1__memory_fsm <= _memory_fsm;
      case(_d1__memory_fsm)
        _memory_fsm_100: begin
          if(__memory_fsm_cond_100_0_1) begin
            memory_awready <= 0;
          end 
        end
        _memory_fsm_200: begin
          if(__memory_fsm_cond_200_1_1) begin
            memory_arready <= 0;
          end 
        end
        _memory_fsm_211: begin
          if(__memory_fsm_cond_211_2_1) begin
            memory_rvalid <= 0;
            memory_rlast <= 0;
          end 
        end
      endcase
      case(_memory_fsm)
        _memory_fsm_init: begin
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_100;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_200;
          end 
        end
        _memory_fsm_100: begin
          if(memory_awvalid) begin
            memory_awready <= 1;
            _write_addr <= memory_awaddr;
            _write_count <= memory_awlen + 1;
          end 
          __memory_fsm_cond_100_0_1 <= 1;
          if(!memory_awvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_101;
          end 
        end
        _memory_fsm_101: begin
          _memory_fsm <= _memory_fsm_102;
        end
        _memory_fsm_102: begin
          _memory_fsm <= _memory_fsm_103;
        end
        _memory_fsm_103: begin
          _memory_fsm <= _memory_fsm_104;
        end
        _memory_fsm_104: begin
          _memory_fsm <= _memory_fsm_105;
        end
        _memory_fsm_105: begin
          _memory_fsm <= _memory_fsm_106;
        end
        _memory_fsm_106: begin
          _memory_fsm <= _memory_fsm_107;
        end
        _memory_fsm_107: begin
          _memory_fsm <= _memory_fsm_108;
        end
        _memory_fsm_108: begin
          _memory_fsm <= _memory_fsm_109;
        end
        _memory_fsm_109: begin
          _memory_fsm <= _memory_fsm_110;
        end
        _memory_fsm_110: begin
          _memory_fsm <= _memory_fsm_111;
        end
        _memory_fsm_111: begin
          memory_wready <= 1;
          _memory_fsm <= _memory_fsm_112;
        end
        _memory_fsm_112: begin
          if(memory_wvalid && memory_wstrb[0]) begin
            _memory_mem[_write_addr + 0] <= memory_wdata[7:0];
          end 
          if(memory_wvalid && memory_wstrb[1]) begin
            _memory_mem[_write_addr + 1] <= memory_wdata[15:8];
          end 
          if(memory_wvalid && memory_wstrb[2]) begin
            _memory_mem[_write_addr + 2] <= memory_wdata[23:16];
          end 
          if(memory_wvalid && memory_wstrb[3]) begin
            _memory_mem[_write_addr + 3] <= memory_wdata[31:24];
          end 
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 4;
            _write_count <= _write_count - 1;
          end 
          if(_sleep_count == 3) begin
            memory_wready <= 0;
          end else begin
            memory_wready <= 1;
          end
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            memory_wready <= 0;
          end 
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
        _memory_fsm_200: begin
          if(memory_arvalid) begin
            memory_arready <= 1;
            _read_addr <= memory_araddr;
            _read_count <= memory_arlen + 1;
          end 
          __memory_fsm_cond_200_1_1 <= 1;
          if(!memory_arvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_201;
          end 
        end
        _memory_fsm_201: begin
          _memory_fsm <= _memory_fsm_202;
        end
        _memory_fsm_202: begin
          _memory_fsm <= _memory_fsm_203;
        end
        _memory_fsm_203: begin
          _memory_fsm <= _memory_fsm_204;
        end
        _memory_fsm_204: begin
          _memory_fsm <= _memory_fsm_205;
        end
        _memory_fsm_205: begin
          _memory_fsm <= _memory_fsm_206;
        end
        _memory_fsm_206: begin
          _memory_fsm <= _memory_fsm_207;
        end
        _memory_fsm_207: begin
          _memory_fsm <= _memory_fsm_208;
        end
        _memory_fsm_208: begin
          _memory_fsm <= _memory_fsm_209;
        end
        _memory_fsm_209: begin
          _memory_fsm <= _memory_fsm_210;
        end
        _memory_fsm_210: begin
          _memory_fsm <= _memory_fsm_211;
        end
        _memory_fsm_211: begin
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[7:0] <= _memory_mem[_read_addr + 0];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[15:8] <= _memory_mem[_read_addr + 1];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[23:16] <= _memory_mem[_read_addr + 2];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[31:24] <= _memory_mem[_read_addr + 3];
          end 
          if((_sleep_count < 3) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 4;
            _read_count <= _read_count - 1;
          end 
          if((_sleep_count < 3) && (_read_count == 1) && memory_rready | !memory_rvalid) begin
            memory_rlast <= 1;
          end 
          __memory_fsm_cond_211_2_1 <= 1;
          if(memory_rvalid && !memory_rready) begin
            memory_rvalid <= memory_rvalid;
            memory_rdata <= memory_rdata;
            memory_rlast <= memory_rlast;
          end 
          if(memory_rvalid && memory_rready && (_read_count == 0)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [32-1:0] myaxi_awaddr,
  output reg [8-1:0] myaxi_awlen,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [32-1:0] myaxi_rdata,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  reg [32-1:0] timer;
  reg [10-1:0] ram_a_0_addr;
  wire [32-1:0] ram_a_0_rdata;
  reg [32-1:0] ram_a_0_wdata;
  reg ram_a_0_wenable;

  ram_a
  inst_ram_a
  (
    .CLK(CLK),
    .ram_a_0_addr(ram_a_0_addr),
    .ram_a_0_rdata(ram_a_0_rdata),
    .ram_a_0_wdata(ram_a_0_wdata),
    .ram_a_0_wenable(ram_a_0_wenable)
  );

  reg [10-1:0] ram_b_0_addr;
  wire [32-1:0] ram_b_0_rdata;
  reg [32-1:0] ram_b_0_wdata;
  reg ram_b_0_wenable;

  ram_b
  inst_ram_b
  (
    .CLK(CLK),
    .ram_b_0_addr(ram_b_0_addr),
    .ram_b_0_rdata(ram_b_0_rdata),
    .ram_b_0_wdata(ram_b_0_wdata),
    .ram_b_0_wenable(ram_b_0_wenable)
  );

  reg [10-1:0] ram_c_0_addr;
  wire [32-1:0] ram_c_0_rdata;
  reg [32-1:0] ram_c_0_wdata;
  reg ram_c_0_wenable;

  ram_c
  inst_ram_c
  (
    .CLK(CLK),
    .ram_c_0_addr(ram_c_0_addr),
    .ram_c_0_rdata(ram_c_0_rdata),
    .ram_c_0_wdata(ram_c_0_wdata),
    .ram_c_0_wenable(ram_c_0_wenable)
  );

  reg [32-1:0] th_matmul;
  localparam th_matmul_init = 0;
  reg signed [32-1:0] _th_matmul_matrix_size_0;
  reg signed [32-1:0] _th_matmul_a_offset_1;
  reg signed [32-1:0] _th_matmul_b_offset_2;
  reg signed [32-1:0] _th_matmul_c_offset_3;
  reg signed [32-1:0] _th_matmul_start_time_4;
  reg signed [32-1:0] _th_matmul_matrix_size_5;
  reg signed [32-1:0] _th_matmul_a_offset_6;
  reg signed [32-1:0] _th_matmul_b_offset_7;
  reg signed [32-1:0] _th_matmul_c_offset_8;
  reg signed [32-1:0] _th_matmul_a_addr_9;
  reg signed [32-1:0] _th_matmul_c_addr_10;
  reg signed [32-1:0] _th_matmul_i_11;
  reg [10-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg [32-1:0] _tmp_2;
  reg [32-1:0] _tmp_3;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [9-1:0] _tmp_4;
  reg _myaxi_cond_0_1;
  reg [32-1:0] _tmp_5;
  reg _tmp_6;
  reg [33-1:0] _tmp_7;
  reg _tmp_8;
  wire [32-1:0] _tmp_data_9;
  wire _tmp_valid_9;
  wire _tmp_ready_9;
  assign _tmp_ready_9 = (_tmp_7 > 0) && !_tmp_8;
  reg _ram_a_cond_0_1;
  reg signed [32-1:0] _th_matmul_b_addr_12;
  reg signed [32-1:0] _th_matmul_j_13;
  reg [10-1:0] _tmp_10;
  reg [32-1:0] _tmp_11;
  reg [32-1:0] _tmp_12;
  reg [32-1:0] _tmp_13;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [9-1:0] _tmp_14;
  reg _myaxi_cond_1_1;
  reg [32-1:0] _tmp_15;
  reg _tmp_16;
  reg [33-1:0] _tmp_17;
  reg _tmp_18;
  wire [32-1:0] _tmp_data_19;
  wire _tmp_valid_19;
  wire _tmp_ready_19;
  assign _tmp_ready_19 = (_tmp_17 > 0) && !_tmp_18;
  reg _ram_b_cond_0_1;
  reg signed [32-1:0] _th_matmul_sum_14;
  reg signed [32-1:0] _th_matmul_k_15;
  reg _tmp_20;
  reg _ram_a_cond_1_1;
  reg _ram_a_cond_2_1;
  reg _ram_a_cond_2_2;
  reg signed [32-1:0] _tmp_21;
  reg signed [32-1:0] _th_matmul_x_16;
  reg _tmp_22;
  reg _ram_b_cond_1_1;
  reg _ram_b_cond_2_1;
  reg _ram_b_cond_2_2;
  reg signed [32-1:0] _tmp_23;
  reg signed [32-1:0] _th_matmul_y_17;
  reg _ram_c_cond_0_1;
  reg [10-1:0] _tmp_24;
  reg [32-1:0] _tmp_25;
  reg [32-1:0] _tmp_26;
  reg [32-1:0] _tmp_27;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [9-1:0] _tmp_28;
  reg _myaxi_cond_2_1;
  reg _tmp_29;
  reg _tmp_30;
  wire _tmp_31;
  wire _tmp_32;
  assign _tmp_32 = 1;
  localparam _tmp_33 = 1;
  wire [_tmp_33-1:0] _tmp_34;
  assign _tmp_34 = (_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30);
  reg [_tmp_33-1:0] __tmp_34_1;
  wire [32-1:0] _tmp_35;
  reg [32-1:0] __tmp_35_1;
  assign _tmp_35 = (__tmp_34_1)? ram_c_0_rdata : __tmp_35_1;
  reg [33-1:0] _tmp_36;
  reg _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  reg _tmp_40;
  reg _tmp_41;
  wire [32-1:0] _tmp_data_42;
  wire _tmp_valid_42;
  wire _tmp_ready_42;
  assign _tmp_ready_42 = (_tmp_fsm_2 == 3) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg signed [32-1:0] _th_matmul_end_time_18;
  reg signed [32-1:0] _th_matmul_time_19;
  reg signed [32-1:0] _th_matmul_matrix_size_20;
  reg signed [32-1:0] _th_matmul_a_offset_21;
  reg signed [32-1:0] _th_matmul_b_offset_22;
  reg signed [32-1:0] _th_matmul_c_offset_23;
  reg signed [32-1:0] _th_matmul_all_ok_24;
  reg signed [32-1:0] _th_matmul_c_addr_25;
  reg signed [32-1:0] _th_matmul_i_26;
  reg [10-1:0] _tmp_43;
  reg [32-1:0] _tmp_44;
  reg [32-1:0] _tmp_45;
  reg [32-1:0] _tmp_46;
  reg [32-1:0] _tmp_fsm_3;
  localparam _tmp_fsm_3_init = 0;
  reg [9-1:0] _tmp_47;
  reg _myaxi_cond_4_1;
  reg [32-1:0] _tmp_48;
  reg _tmp_49;
  reg [33-1:0] _tmp_50;
  reg _tmp_51;
  wire [32-1:0] _tmp_data_52;
  wire _tmp_valid_52;
  wire _tmp_ready_52;
  assign _tmp_ready_52 = (_tmp_50 > 0) && !_tmp_51;
  reg _ram_c_cond_1_1;
  assign myaxi_rready = 1 || 1 || 1;
  reg signed [32-1:0] _th_matmul_j_27;
  reg _tmp_53;
  reg _ram_c_cond_2_1;
  reg _ram_c_cond_3_1;
  reg _ram_c_cond_3_2;
  reg signed [32-1:0] _tmp_54;
  reg signed [32-1:0] _th_matmul_v_28;

  always @(posedge CLK) begin
    if(RST) begin
      timer <= 0;
    end else begin
      timer <= timer + 1;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      _tmp_7 <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_8 <= 0;
      _ram_a_cond_0_1 <= 0;
      _ram_a_cond_1_1 <= 0;
      _tmp_20 <= 0;
      _ram_a_cond_2_1 <= 0;
      _ram_a_cond_2_2 <= 0;
    end else begin
      if(_ram_a_cond_2_2) begin
        _tmp_20 <= 0;
      end 
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_8 <= 0;
      end 
      if(_ram_a_cond_1_1) begin
        _tmp_20 <= 1;
      end 
      _ram_a_cond_2_2 <= _ram_a_cond_2_1;
      if((_tmp_fsm_0 == 2) && (_tmp_7 == 0)) begin
        ram_a_0_addr <= _tmp_0 - 1;
        _tmp_7 <= _tmp_2;
      end 
      if(_tmp_valid_9 && ((_tmp_7 > 0) && !_tmp_8) && (_tmp_7 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_9;
        ram_a_0_wenable <= 1;
        _tmp_7 <= _tmp_7 - 1;
      end 
      if(_tmp_valid_9 && ((_tmp_7 > 0) && !_tmp_8) && (_tmp_7 == 1)) begin
        _tmp_8 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      if(th_matmul == 18) begin
        ram_a_0_addr <= _th_matmul_k_15;
      end 
      _ram_a_cond_1_1 <= th_matmul == 18;
      _ram_a_cond_2_1 <= th_matmul == 18;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      _tmp_17 <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_18 <= 0;
      _ram_b_cond_0_1 <= 0;
      _ram_b_cond_1_1 <= 0;
      _tmp_22 <= 0;
      _ram_b_cond_2_1 <= 0;
      _ram_b_cond_2_2 <= 0;
    end else begin
      if(_ram_b_cond_2_2) begin
        _tmp_22 <= 0;
      end 
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_18 <= 0;
      end 
      if(_ram_b_cond_1_1) begin
        _tmp_22 <= 1;
      end 
      _ram_b_cond_2_2 <= _ram_b_cond_2_1;
      if((_tmp_fsm_1 == 2) && (_tmp_17 == 0)) begin
        ram_b_0_addr <= _tmp_10 - 1;
        _tmp_17 <= _tmp_12;
      end 
      if(_tmp_valid_19 && ((_tmp_17 > 0) && !_tmp_18) && (_tmp_17 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_19;
        ram_b_0_wenable <= 1;
        _tmp_17 <= _tmp_17 - 1;
      end 
      if(_tmp_valid_19 && ((_tmp_17 > 0) && !_tmp_18) && (_tmp_17 == 1)) begin
        _tmp_18 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      if(th_matmul == 20) begin
        ram_b_0_addr <= _th_matmul_k_15;
      end 
      _ram_b_cond_1_1 <= th_matmul == 20;
      _ram_b_cond_2_1 <= th_matmul == 20;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_34_1 <= 0;
      __tmp_35_1 <= 0;
      _tmp_40 <= 0;
      _tmp_29 <= 0;
      _tmp_30 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_37 <= 0;
      _tmp_36 <= 0;
      _tmp_50 <= 0;
      _tmp_51 <= 0;
      _ram_c_cond_1_1 <= 0;
      _ram_c_cond_2_1 <= 0;
      _tmp_53 <= 0;
      _ram_c_cond_3_1 <= 0;
      _ram_c_cond_3_2 <= 0;
    end else begin
      if(_ram_c_cond_3_2) begin
        _tmp_53 <= 0;
      end 
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
      end 
      if(_ram_c_cond_1_1) begin
        ram_c_0_wenable <= 0;
        _tmp_51 <= 0;
      end 
      if(_ram_c_cond_2_1) begin
        _tmp_53 <= 1;
      end 
      _ram_c_cond_3_2 <= _ram_c_cond_3_1;
      if(th_matmul == 24) begin
        ram_c_0_addr <= _th_matmul_j_13;
        ram_c_0_wdata <= _th_matmul_sum_14;
        ram_c_0_wenable <= 1;
      end 
      _ram_c_cond_0_1 <= th_matmul == 24;
      __tmp_34_1 <= _tmp_34;
      __tmp_35_1 <= _tmp_35;
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && _tmp_38) begin
        _tmp_40 <= 0;
        _tmp_29 <= 0;
        _tmp_30 <= 0;
        _tmp_38 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && _tmp_37) begin
        _tmp_29 <= 1;
        _tmp_30 <= 1;
        _tmp_40 <= _tmp_39;
        _tmp_39 <= 0;
        _tmp_37 <= 0;
        _tmp_38 <= 1;
      end 
      if((_tmp_fsm_2 == 2) && (_tmp_36 == 0) && !_tmp_39 && !_tmp_40) begin
        ram_c_0_addr <= _tmp_24;
        _tmp_36 <= _tmp_26 - 1;
        _tmp_37 <= 1;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_36 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_36 <= _tmp_36 - 1;
        _tmp_37 <= 1;
        _tmp_39 <= 0;
      end 
      if((_tmp_31 || !_tmp_29) && (_tmp_32 || !_tmp_30) && (_tmp_36 == 1)) begin
        _tmp_39 <= 1;
      end 
      if((_tmp_fsm_3 == 2) && (_tmp_50 == 0)) begin
        ram_c_0_addr <= _tmp_43 - 1;
        _tmp_50 <= _tmp_45;
      end 
      if(_tmp_valid_52 && ((_tmp_50 > 0) && !_tmp_51) && (_tmp_50 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_52;
        ram_c_0_wenable <= 1;
        _tmp_50 <= _tmp_50 - 1;
      end 
      if(_tmp_valid_52 && ((_tmp_50 > 0) && !_tmp_51) && (_tmp_50 == 1)) begin
        _tmp_51 <= 1;
      end 
      _ram_c_cond_1_1 <= 1;
      if(th_matmul == 46) begin
        ram_c_0_addr <= _th_matmul_j_27;
      end 
      _ram_c_cond_2_1 <= th_matmul == 46;
      _ram_c_cond_3_1 <= th_matmul == 46;
    end
  end

  assign _tmp_data_42 = _tmp_35;
  assign _tmp_valid_42 = _tmp_29;
  assign _tmp_31 = 1 && _tmp_ready_42;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_4 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_14 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_28 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_41 <= 0;
      _myaxi_cond_3_1 <= 0;
      _tmp_47 <= 0;
      _myaxi_cond_4_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_arvalid <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_3_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_41 <= 0;
      end 
      if(_myaxi_cond_4_1) begin
        myaxi_arvalid <= 0;
      end 
      if((_tmp_fsm_0 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_4 == 0))) begin
        myaxi_araddr <= _tmp_1;
        myaxi_arlen <= _tmp_2 - 1;
        myaxi_arvalid <= 1;
        _tmp_4 <= _tmp_2;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_4 > 0)) begin
        _tmp_4 <= _tmp_4 - 1;
      end 
      if((_tmp_fsm_1 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_14 == 0))) begin
        myaxi_araddr <= _tmp_11;
        myaxi_arlen <= _tmp_12 - 1;
        myaxi_arvalid <= 1;
        _tmp_14 <= _tmp_12;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_14 > 0)) begin
        _tmp_14 <= _tmp_14 - 1;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_28 == 0))) begin
        myaxi_awaddr <= _tmp_25;
        myaxi_awlen <= _tmp_26 - 1;
        myaxi_awvalid <= 1;
        _tmp_28 <= _tmp_26;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_28 == 0)) && (_tmp_26 == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_42 && ((_tmp_fsm_2 == 3) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_28 > 0))) begin
        myaxi_wdata <= _tmp_data_42;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_28 <= _tmp_28 - 1;
      end 
      if(_tmp_valid_42 && ((_tmp_fsm_2 == 3) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_28 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_28 > 0)) && (_tmp_28 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_41 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_41 <= _tmp_41;
      end 
      if((_tmp_fsm_3 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_47 == 0))) begin
        myaxi_araddr <= _tmp_44;
        myaxi_arlen <= _tmp_45 - 1;
        myaxi_arvalid <= 1;
        _tmp_47 <= _tmp_45;
      end 
      _myaxi_cond_4_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_47 > 0)) begin
        _tmp_47 <= _tmp_47 - 1;
      end 
    end
  end

  assign _tmp_data_9 = _tmp_5;
  assign _tmp_valid_9 = _tmp_6;
  assign _tmp_data_19 = _tmp_15;
  assign _tmp_valid_19 = _tmp_16;
  assign _tmp_data_52 = _tmp_48;
  assign _tmp_valid_52 = _tmp_49;
  localparam th_matmul_1 = 1;
  localparam th_matmul_2 = 2;
  localparam th_matmul_3 = 3;
  localparam th_matmul_4 = 4;
  localparam th_matmul_5 = 5;
  localparam th_matmul_6 = 6;
  localparam th_matmul_7 = 7;
  localparam th_matmul_8 = 8;
  localparam th_matmul_9 = 9;
  localparam th_matmul_10 = 10;
  localparam th_matmul_11 = 11;
  localparam th_matmul_12 = 12;
  localparam th_matmul_13 = 13;
  localparam th_matmul_14 = 14;
  localparam th_matmul_15 = 15;
  localparam th_matmul_16 = 16;
  localparam th_matmul_17 = 17;
  localparam th_matmul_18 = 18;
  localparam th_matmul_19 = 19;
  localparam th_matmul_20 = 20;
  localparam th_matmul_21 = 21;
  localparam th_matmul_22 = 22;
  localparam th_matmul_23 = 23;
  localparam th_matmul_24 = 24;
  localparam th_matmul_25 = 25;
  localparam th_matmul_26 = 26;
  localparam th_matmul_27 = 27;
  localparam th_matmul_28 = 28;
  localparam th_matmul_29 = 29;
  localparam th_matmul_30 = 30;
  localparam th_matmul_31 = 31;
  localparam th_matmul_32 = 32;
  localparam th_matmul_33 = 33;
  localparam th_matmul_34 = 34;
  localparam th_matmul_35 = 35;
  localparam th_matmul_36 = 36;
  localparam th_matmul_37 = 37;
  localparam th_matmul_38 = 38;
  localparam th_matmul_39 = 39;
  localparam th_matmul_40 = 40;
  localparam th_matmul_41 = 41;
  localparam th_matmul_42 = 42;
  localparam th_matmul_43 = 43;
  localparam th_matmul_44 = 44;
  localparam th_matmul_45 = 45;
  localparam th_matmul_46 = 46;
  localparam th_matmul_47 = 47;
  localparam th_matmul_48 = 48;
  localparam th_matmul_49 = 49;
  localparam th_matmul_50 = 50;
  localparam th_matmul_51 = 51;
  localparam th_matmul_52 = 52;
  localparam th_matmul_53 = 53;
  localparam th_matmul_54 = 54;
  localparam th_matmul_55 = 55;
  localparam th_matmul_56 = 56;
  localparam th_matmul_57 = 57;
  localparam th_matmul_58 = 58;
  localparam th_matmul_59 = 59;
  localparam th_matmul_60 = 60;
  localparam th_matmul_61 = 61;

  always @(posedge CLK) begin
    if(RST) begin
      th_matmul <= th_matmul_init;
      _th_matmul_matrix_size_0 <= 0;
      _th_matmul_a_offset_1 <= 0;
      _th_matmul_b_offset_2 <= 0;
      _th_matmul_c_offset_3 <= 0;
      _th_matmul_start_time_4 <= 0;
      _th_matmul_matrix_size_5 <= 0;
      _th_matmul_a_offset_6 <= 0;
      _th_matmul_b_offset_7 <= 0;
      _th_matmul_c_offset_8 <= 0;
      _th_matmul_a_addr_9 <= 0;
      _th_matmul_c_addr_10 <= 0;
      _th_matmul_i_11 <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_3 <= 0;
      _tmp_2 <= 0;
      _th_matmul_b_addr_12 <= 0;
      _th_matmul_j_13 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_13 <= 0;
      _tmp_12 <= 0;
      _th_matmul_sum_14 <= 0;
      _th_matmul_k_15 <= 0;
      _tmp_21 <= 0;
      _th_matmul_x_16 <= 0;
      _tmp_23 <= 0;
      _th_matmul_y_17 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_27 <= 0;
      _tmp_26 <= 0;
      _th_matmul_end_time_18 <= 0;
      _th_matmul_time_19 <= 0;
      _th_matmul_matrix_size_20 <= 0;
      _th_matmul_a_offset_21 <= 0;
      _th_matmul_b_offset_22 <= 0;
      _th_matmul_c_offset_23 <= 0;
      _th_matmul_all_ok_24 <= 0;
      _th_matmul_c_addr_25 <= 0;
      _th_matmul_i_26 <= 0;
      _tmp_43 <= 0;
      _tmp_44 <= 0;
      _tmp_46 <= 0;
      _tmp_45 <= 0;
      _th_matmul_j_27 <= 0;
      _tmp_54 <= 0;
      _th_matmul_v_28 <= 0;
    end else begin
      case(th_matmul)
        th_matmul_init: begin
          _th_matmul_matrix_size_0 <= 16;
          _th_matmul_a_offset_1 <= 0;
          _th_matmul_b_offset_2 <= 1024;
          _th_matmul_c_offset_3 <= 2048;
          th_matmul <= th_matmul_1;
        end
        th_matmul_1: begin
          _th_matmul_start_time_4 <= timer;
          th_matmul <= th_matmul_2;
        end
        th_matmul_2: begin
          _th_matmul_matrix_size_5 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_6 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_7 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_8 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_3;
        end
        th_matmul_3: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_offset_6;
          _th_matmul_c_addr_10 <= _th_matmul_c_offset_8;
          th_matmul <= th_matmul_4;
        end
        th_matmul_4: begin
          _th_matmul_i_11 <= 0;
          th_matmul <= th_matmul_5;
        end
        th_matmul_5: begin
          if(_th_matmul_i_11 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_6;
          end else begin
            th_matmul <= th_matmul_33;
          end
        end
        th_matmul_6: begin
          _tmp_0 <= 0;
          _tmp_1 <= _th_matmul_a_addr_9;
          _tmp_3 <= _th_matmul_matrix_size_5;
          th_matmul <= th_matmul_7;
        end
        th_matmul_7: begin
          if(_tmp_3 <= 256) begin
            _tmp_2 <= _tmp_3;
            _tmp_3 <= 0;
          end else begin
            _tmp_2 <= 256;
            _tmp_3 <= _tmp_3 - 256;
          end
          th_matmul <= th_matmul_8;
        end
        th_matmul_8: begin
          if(_tmp_8) begin
            _tmp_0 <= _tmp_0 + _tmp_2;
            _tmp_1 <= _tmp_1 + (_tmp_2 << 2);
          end 
          if(_tmp_8 && (_tmp_3 > 0)) begin
            th_matmul <= th_matmul_7;
          end 
          if(_tmp_8 && (_tmp_3 == 0)) begin
            th_matmul <= th_matmul_9;
          end 
        end
        th_matmul_9: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_offset_7;
          th_matmul <= th_matmul_10;
        end
        th_matmul_10: begin
          _th_matmul_j_13 <= 0;
          th_matmul <= th_matmul_11;
        end
        th_matmul_11: begin
          if(_th_matmul_j_13 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_12;
          end else begin
            th_matmul <= th_matmul_27;
          end
        end
        th_matmul_12: begin
          _tmp_10 <= 0;
          _tmp_11 <= _th_matmul_b_addr_12;
          _tmp_13 <= _th_matmul_matrix_size_5;
          th_matmul <= th_matmul_13;
        end
        th_matmul_13: begin
          if(_tmp_13 <= 256) begin
            _tmp_12 <= _tmp_13;
            _tmp_13 <= 0;
          end else begin
            _tmp_12 <= 256;
            _tmp_13 <= _tmp_13 - 256;
          end
          th_matmul <= th_matmul_14;
        end
        th_matmul_14: begin
          if(_tmp_18) begin
            _tmp_10 <= _tmp_10 + _tmp_12;
            _tmp_11 <= _tmp_11 + (_tmp_12 << 2);
          end 
          if(_tmp_18 && (_tmp_13 > 0)) begin
            th_matmul <= th_matmul_13;
          end 
          if(_tmp_18 && (_tmp_13 == 0)) begin
            th_matmul <= th_matmul_15;
          end 
        end
        th_matmul_15: begin
          _th_matmul_sum_14 <= 0;
          th_matmul <= th_matmul_16;
        end
        th_matmul_16: begin
          _th_matmul_k_15 <= 0;
          th_matmul <= th_matmul_17;
        end
        th_matmul_17: begin
          if(_th_matmul_k_15 < _th_matmul_matrix_size_5) begin
            th_matmul <= th_matmul_18;
          end else begin
            th_matmul <= th_matmul_24;
          end
        end
        th_matmul_18: begin
          if(_tmp_20) begin
            _tmp_21 <= ram_a_0_rdata;
          end 
          if(_tmp_20) begin
            th_matmul <= th_matmul_19;
          end 
        end
        th_matmul_19: begin
          _th_matmul_x_16 <= _tmp_21;
          th_matmul <= th_matmul_20;
        end
        th_matmul_20: begin
          if(_tmp_22) begin
            _tmp_23 <= ram_b_0_rdata;
          end 
          if(_tmp_22) begin
            th_matmul <= th_matmul_21;
          end 
        end
        th_matmul_21: begin
          _th_matmul_y_17 <= _tmp_23;
          th_matmul <= th_matmul_22;
        end
        th_matmul_22: begin
          _th_matmul_sum_14 <= _th_matmul_sum_14 + _th_matmul_x_16 * _th_matmul_y_17;
          th_matmul <= th_matmul_23;
        end
        th_matmul_23: begin
          _th_matmul_k_15 <= _th_matmul_k_15 + 1;
          th_matmul <= th_matmul_17;
        end
        th_matmul_24: begin
          th_matmul <= th_matmul_25;
        end
        th_matmul_25: begin
          _th_matmul_b_addr_12 <= _th_matmul_b_addr_12 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_26;
        end
        th_matmul_26: begin
          _th_matmul_j_13 <= _th_matmul_j_13 + 1;
          th_matmul <= th_matmul_11;
        end
        th_matmul_27: begin
          _tmp_24 <= 0;
          _tmp_25 <= _th_matmul_c_addr_10;
          _tmp_27 <= _th_matmul_matrix_size_5;
          th_matmul <= th_matmul_28;
        end
        th_matmul_28: begin
          if(_tmp_27 <= 256) begin
            _tmp_26 <= _tmp_27;
            _tmp_27 <= 0;
          end else begin
            _tmp_26 <= 256;
            _tmp_27 <= _tmp_27 - 256;
          end
          th_matmul <= th_matmul_29;
        end
        th_matmul_29: begin
          if(_tmp_41) begin
            _tmp_24 <= _tmp_24 + _tmp_26;
            _tmp_25 <= _tmp_25 + (_tmp_26 << 2);
          end 
          if(_tmp_41 && (_tmp_27 > 0)) begin
            th_matmul <= th_matmul_28;
          end 
          if(_tmp_41 && (_tmp_27 == 0)) begin
            th_matmul <= th_matmul_30;
          end 
        end
        th_matmul_30: begin
          _th_matmul_a_addr_9 <= _th_matmul_a_addr_9 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_31;
        end
        th_matmul_31: begin
          _th_matmul_c_addr_10 <= _th_matmul_c_addr_10 + (_th_matmul_matrix_size_5 << 2);
          th_matmul <= th_matmul_32;
        end
        th_matmul_32: begin
          _th_matmul_i_11 <= _th_matmul_i_11 + 1;
          th_matmul <= th_matmul_5;
        end
        th_matmul_33: begin
          _th_matmul_end_time_18 <= timer;
          th_matmul <= th_matmul_34;
        end
        th_matmul_34: begin
          _th_matmul_time_19 <= _th_matmul_end_time_18 - _th_matmul_start_time_4;
          th_matmul <= th_matmul_35;
        end
        th_matmul_35: begin
          $display("Time (cycles): %d", _th_matmul_time_19);
          th_matmul <= th_matmul_36;
        end
        th_matmul_36: begin
          _th_matmul_matrix_size_20 <= _th_matmul_matrix_size_0;
          _th_matmul_a_offset_21 <= _th_matmul_a_offset_1;
          _th_matmul_b_offset_22 <= _th_matmul_b_offset_2;
          _th_matmul_c_offset_23 <= _th_matmul_c_offset_3;
          th_matmul <= th_matmul_37;
        end
        th_matmul_37: begin
          _th_matmul_all_ok_24 <= 1;
          th_matmul <= th_matmul_38;
        end
        th_matmul_38: begin
          _th_matmul_c_addr_25 <= _th_matmul_c_offset_23;
          th_matmul <= th_matmul_39;
        end
        th_matmul_39: begin
          _th_matmul_i_26 <= 0;
          th_matmul <= th_matmul_40;
        end
        th_matmul_40: begin
          if(_th_matmul_i_26 < _th_matmul_matrix_size_20) begin
            th_matmul <= th_matmul_41;
          end else begin
            th_matmul <= th_matmul_57;
          end
        end
        th_matmul_41: begin
          _tmp_43 <= 0;
          _tmp_44 <= _th_matmul_c_addr_25;
          _tmp_46 <= _th_matmul_matrix_size_20;
          th_matmul <= th_matmul_42;
        end
        th_matmul_42: begin
          if(_tmp_46 <= 256) begin
            _tmp_45 <= _tmp_46;
            _tmp_46 <= 0;
          end else begin
            _tmp_45 <= 256;
            _tmp_46 <= _tmp_46 - 256;
          end
          th_matmul <= th_matmul_43;
        end
        th_matmul_43: begin
          if(_tmp_51) begin
            _tmp_43 <= _tmp_43 + _tmp_45;
            _tmp_44 <= _tmp_44 + (_tmp_45 << 2);
          end 
          if(_tmp_51 && (_tmp_46 > 0)) begin
            th_matmul <= th_matmul_42;
          end 
          if(_tmp_51 && (_tmp_46 == 0)) begin
            th_matmul <= th_matmul_44;
          end 
        end
        th_matmul_44: begin
          _th_matmul_j_27 <= 0;
          th_matmul <= th_matmul_45;
        end
        th_matmul_45: begin
          if(_th_matmul_j_27 < _th_matmul_matrix_size_20) begin
            th_matmul <= th_matmul_46;
          end else begin
            th_matmul <= th_matmul_55;
          end
        end
        th_matmul_46: begin
          if(_tmp_53) begin
            _tmp_54 <= ram_c_0_rdata;
          end 
          if(_tmp_53) begin
            th_matmul <= th_matmul_47;
          end 
        end
        th_matmul_47: begin
          _th_matmul_v_28 <= _tmp_54;
          th_matmul <= th_matmul_48;
        end
        th_matmul_48: begin
          if((_th_matmul_i_26 == _th_matmul_j_27) && (_th_matmul_v_28 != (_th_matmul_i_26 + 1 << 1))) begin
            th_matmul <= th_matmul_49;
          end else begin
            th_matmul <= th_matmul_51;
          end
        end
        th_matmul_49: begin
          _th_matmul_all_ok_24 <= 0;
          th_matmul <= th_matmul_50;
        end
        th_matmul_50: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_26, _th_matmul_j_27, _th_matmul_v_28);
          th_matmul <= th_matmul_51;
        end
        th_matmul_51: begin
          if((_th_matmul_i_26 != _th_matmul_j_27) && (_th_matmul_v_28 != 0)) begin
            th_matmul <= th_matmul_52;
          end else begin
            th_matmul <= th_matmul_54;
          end
        end
        th_matmul_52: begin
          _th_matmul_all_ok_24 <= 0;
          th_matmul <= th_matmul_53;
        end
        th_matmul_53: begin
          $display("NG [%d,%d] = %d", _th_matmul_i_26, _th_matmul_j_27, _th_matmul_v_28);
          th_matmul <= th_matmul_54;
        end
        th_matmul_54: begin
          _th_matmul_j_27 <= _th_matmul_j_27 + 1;
          th_matmul <= th_matmul_45;
        end
        th_matmul_55: begin
          _th_matmul_c_addr_25 <= _th_matmul_c_addr_25 + (_th_matmul_matrix_size_20 << 2);
          th_matmul <= th_matmul_56;
        end
        th_matmul_56: begin
          _th_matmul_i_26 <= _th_matmul_i_26 + 1;
          th_matmul <= th_matmul_40;
        end
        th_matmul_57: begin
          if(_th_matmul_all_ok_24) begin
            th_matmul <= th_matmul_58;
          end else begin
            th_matmul <= th_matmul_60;
          end
        end
        th_matmul_58: begin
          $display("OK");
          th_matmul <= th_matmul_59;
        end
        th_matmul_59: begin
          th_matmul <= th_matmul_61;
        end
        th_matmul_60: begin
          $display("NG");
          th_matmul <= th_matmul_61;
        end
      endcase
    end
  end

  localparam _tmp_fsm_0_1 = 1;
  localparam _tmp_fsm_0_2 = 2;
  localparam _tmp_fsm_0_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_0 <= _tmp_fsm_0_init;
      _tmp_6 <= 0;
      _tmp_5 <= 0;
    end else begin
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(th_matmul == 8) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
        end
        _tmp_fsm_0_2: begin
          _tmp_fsm_0 <= _tmp_fsm_0_3;
        end
        _tmp_fsm_0_3: begin
          _tmp_6 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_5 <= myaxi_rdata;
            _tmp_6 <= 1;
          end 
          if(_tmp_8) begin
            _tmp_fsm_0 <= _tmp_fsm_0_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_1_1 = 1;
  localparam _tmp_fsm_1_2 = 2;
  localparam _tmp_fsm_1_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_1 <= _tmp_fsm_1_init;
      _tmp_16 <= 0;
      _tmp_15 <= 0;
    end else begin
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(th_matmul == 14) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
        end
        _tmp_fsm_1_2: begin
          _tmp_fsm_1 <= _tmp_fsm_1_3;
        end
        _tmp_fsm_1_3: begin
          _tmp_16 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_15 <= myaxi_rdata;
            _tmp_16 <= 1;
          end 
          if(_tmp_18) begin
            _tmp_fsm_1 <= _tmp_fsm_1_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_2_1 = 1;
  localparam _tmp_fsm_2_2 = 2;
  localparam _tmp_fsm_2_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_2 <= _tmp_fsm_2_init;
    end else begin
      case(_tmp_fsm_2)
        _tmp_fsm_2_init: begin
          if(th_matmul == 29) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
        end
        _tmp_fsm_2_2: begin
          _tmp_fsm_2 <= _tmp_fsm_2_3;
        end
        _tmp_fsm_2_3: begin
          if(_tmp_41) begin
            _tmp_fsm_2 <= _tmp_fsm_2_init;
          end 
        end
      endcase
    end
  end

  localparam _tmp_fsm_3_1 = 1;
  localparam _tmp_fsm_3_2 = 2;
  localparam _tmp_fsm_3_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_fsm_3 <= _tmp_fsm_3_init;
      _tmp_49 <= 0;
      _tmp_48 <= 0;
    end else begin
      case(_tmp_fsm_3)
        _tmp_fsm_3_init: begin
          if(th_matmul == 43) begin
            _tmp_fsm_3 <= _tmp_fsm_3_1;
          end 
        end
        _tmp_fsm_3_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_3 <= _tmp_fsm_3_2;
          end 
        end
        _tmp_fsm_3_2: begin
          _tmp_fsm_3 <= _tmp_fsm_3_3;
        end
        _tmp_fsm_3_3: begin
          _tmp_49 <= 0;
          if(myaxi_rready && myaxi_rvalid) begin
            _tmp_48 <= myaxi_rdata;
            _tmp_49 <= 1;
          end 
          if(_tmp_51) begin
            _tmp_fsm_3 <= _tmp_fsm_3_init;
          end 
        end
      endcase
    end
  end


endmodule



module ram_a
(
  input CLK,
  input [10-1:0] ram_a_0_addr,
  output [32-1:0] ram_a_0_rdata,
  input [32-1:0] ram_a_0_wdata,
  input ram_a_0_wenable
);

  reg [10-1:0] ram_a_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_a_0_wenable) begin
      mem[ram_a_0_addr] <= ram_a_0_wdata;
    end 
    ram_a_0_daddr <= ram_a_0_addr;
  end

  assign ram_a_0_rdata = mem[ram_a_0_daddr];

endmodule



module ram_b
(
  input CLK,
  input [10-1:0] ram_b_0_addr,
  output [32-1:0] ram_b_0_rdata,
  input [32-1:0] ram_b_0_wdata,
  input ram_b_0_wenable
);

  reg [10-1:0] ram_b_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_b_0_wenable) begin
      mem[ram_b_0_addr] <= ram_b_0_wdata;
    end 
    ram_b_0_daddr <= ram_b_0_addr;
  end

  assign ram_b_0_rdata = mem[ram_b_0_daddr];

endmodule



module ram_c
(
  input CLK,
  input [10-1:0] ram_c_0_addr,
  output [32-1:0] ram_c_0_rdata,
  input [32-1:0] ram_c_0_wdata,
  input ram_c_0_wenable
);

  reg [10-1:0] ram_c_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(ram_c_0_wenable) begin
      mem[ram_c_0_addr] <= ram_c_0_wdata;
    end 
    ram_c_0_daddr <= ram_c_0_addr;
  end

  assign ram_c_0_rdata = mem[ram_c_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_matmul.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
