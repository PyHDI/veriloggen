from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import axi_vecadd

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
  reg [32-1:0] waddr;
  localparam waddr_init = 0;
  reg [32-1:0] _awlen;
  reg [32-1:0] raddr;
  localparam raddr_init = 0;
  reg [32-1:0] _arlen;
  reg [32-1:0] _d1_raddr;
  reg _raddr_cond_3_0_1;
  localparam raddr_1 = 1;
  localparam raddr_2 = 2;
  localparam raddr_3 = 3;
  localparam raddr_4 = 4;
  localparam raddr_5 = 5;
  localparam raddr_6 = 6;
  localparam raddr_7 = 7;
  localparam raddr_8 = 8;
  localparam raddr_9 = 9;
  localparam raddr_10 = 10;

  always @(posedge CLK) begin
    if(RST) begin
      raddr <= raddr_init;
      _d1_raddr <= raddr_init;
      _arlen <= 0;
      _raddr_cond_3_0_1 <= 0;
    end else begin
      _d1_raddr <= raddr;
      case(_d1_raddr)
        raddr_3: begin
          if(_raddr_cond_3_0_1) begin
            myaxi_rvalid <= 0;
            myaxi_rlast <= 0;
          end 
        end
      endcase
      case(raddr)
        raddr_init: begin
          myaxi_arready <= 0;
          myaxi_rdata <= -1;
          myaxi_rvalid <= 0;
          myaxi_rlast <= 0;
          if(myaxi_arvalid) begin
            raddr <= raddr_1;
          end 
        end
        raddr_1: begin
          if(myaxi_arvalid) begin
            myaxi_arready <= 1;
            myaxi_rdata <= myaxi_araddr - 1;
          end 
          raddr <= raddr_2;
        end
        raddr_2: begin
          myaxi_arready <= 0;
          _arlen <= myaxi_arlen;
          raddr <= raddr_3;
        end
        raddr_3: begin
          if((myaxi_rready || !myaxi_rvalid) && !myaxi_rlast) begin
            myaxi_rdata <= myaxi_rdata + 1;
            myaxi_rvalid <= 1;
            myaxi_rlast <= 0;
            _arlen <= _arlen - 1;
          end 
          if((myaxi_rready || !myaxi_rvalid) && !myaxi_rlast && (_arlen == 0)) begin
            myaxi_rlast <= 1;
          end 
          _raddr_cond_3_0_1 <= 1;
          raddr <= raddr_4;
        end
        raddr_4: begin
          if(myaxi_rvalid && !myaxi_rready) begin
            myaxi_rvalid <= myaxi_rvalid;
            myaxi_rlast <= myaxi_rlast;
          end 
          if(myaxi_rvalid && myaxi_rready) begin
            raddr <= raddr_5;
          end 
        end
        raddr_5: begin
          raddr <= raddr_6;
        end
        raddr_6: begin
          raddr <= raddr_7;
        end
        raddr_7: begin
          raddr <= raddr_8;
        end
        raddr_8: begin
          if((_arlen + 1 & 255) != 0) begin
            raddr <= raddr_3;
          end 
          if((_arlen + 1 & 255) == 0) begin
            raddr <= raddr_9;
          end 
        end
        raddr_9: begin
          raddr <= raddr_10;
        end
        raddr_10: begin
          raddr <= raddr_init;
        end
      endcase
    end
  end


  main
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
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, waddr, _awlen, raddr, _arlen, _d1_raddr, _raddr_cond_3_0_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    waddr = waddr_init;
    _awlen = 0;
    raddr = raddr_init;
    _arlen = 0;
    _d1_raddr = raddr_init;
    _raddr_cond_3_0_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end

  localparam waddr_1 = 1;
  localparam waddr_2 = 2;
  localparam waddr_3 = 3;
  localparam waddr_4 = 4;
  localparam waddr_5 = 5;
  localparam waddr_6 = 6;
  localparam waddr_7 = 7;
  localparam waddr_8 = 8;

  always @(posedge CLK) begin
    if(RST) begin
      waddr <= waddr_init;
      _awlen <= 0;
    end else begin
      case(waddr)
        waddr_init: begin
          myaxi_awready <= 0;
          myaxi_wready <= 0;
          _awlen <= 0;
          if(myaxi_awvalid) begin
            waddr <= waddr_1;
          end 
        end
        waddr_1: begin
          if(myaxi_awvalid) begin
            myaxi_awready <= 1;
          end 
          waddr <= waddr_2;
        end
        waddr_2: begin
          myaxi_awready <= 0;
          _awlen <= myaxi_awlen;
          waddr <= waddr_3;
        end
        waddr_3: begin
          myaxi_wready <= 0;
          if(myaxi_wvalid) begin
            waddr <= waddr_4;
          end 
        end
        waddr_4: begin
          if(myaxi_wvalid) begin
            myaxi_wready <= 1;
          end 
          waddr <= waddr_5;
        end
        waddr_5: begin
          myaxi_wready <= 0;
          waddr <= waddr_6;
        end
        waddr_6: begin
          waddr <= waddr_7;
        end
        waddr_7: begin
          waddr <= waddr_8;
        end
        waddr_8: begin
          _awlen <= _awlen - 1;
          waddr <= waddr_3;
          if(_awlen == 0) begin
            waddr <= waddr_init;
          end 
        end
      endcase
    end
  end


endmodule



module main
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

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _tmp_fsm_0;
  localparam _tmp_fsm_0_init = 0;
  reg [8-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  wire _tmp_1;
  wire _tmp_2;
  assign _tmp_1 = 1 && _tmp_ready_5;
  assign _tmp_2 = 1;
  assign myaxi_rready = _tmp_1 && _tmp_2 || _tmp_7 && _tmp_8;
  reg [8-1:0] _tmp_3;
  reg _tmp_4;
  wire [32-1:0] _tmp_data_5;
  wire _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (_tmp_fsm_0 == 2) && !_tmp_4;
  reg _ram_a_cond_0_1;
  reg [32-1:0] _tmp_fsm_1;
  localparam _tmp_fsm_1_init = 0;
  reg [8-1:0] _tmp_6;
  reg _myaxi_cond_1_1;
  wire _tmp_7;
  wire _tmp_8;
  assign _tmp_7 = 1 && _tmp_ready_11;
  assign _tmp_8 = 1;
  reg [8-1:0] _tmp_9;
  reg _tmp_10;
  wire [32-1:0] _tmp_data_11;
  wire _tmp_valid_11;
  wire _tmp_ready_11;
  assign _tmp_ready_11 = (_tmp_fsm_1 == 2) && !_tmp_10;
  reg _ram_b_cond_0_1;
  reg _tmp_12;
  reg _tmp_13;
  wire _tmp_14;
  wire _tmp_15;
  assign _tmp_14 = 1 && ((_tmp_ready_54 || !_tmp_valid_54) && (_tmp_12 && _tmp_24));
  assign _tmp_15 = 1;
  localparam _tmp_16 = 1;
  wire [_tmp_16-1:0] _tmp_17;
  assign _tmp_17 = (_tmp_14 || !_tmp_12) && (_tmp_15 || !_tmp_13);
  reg [_tmp_16-1:0] __tmp_17_1;
  wire [32-1:0] _tmp_18;
  reg [32-1:0] __tmp_18_1;
  assign _tmp_18 = (__tmp_17_1)? ram_a_0_rdata : __tmp_18_1;
  reg [8-1:0] _tmp_19;
  reg _tmp_20;
  reg _tmp_21;
  reg _tmp_22;
  reg _tmp_23;
  reg _tmp_24;
  reg _tmp_25;
  wire _tmp_26;
  wire _tmp_27;
  assign _tmp_26 = 1 && ((_tmp_ready_54 || !_tmp_valid_54) && (_tmp_12 && _tmp_24));
  assign _tmp_27 = 1;
  localparam _tmp_28 = 1;
  wire [_tmp_28-1:0] _tmp_29;
  assign _tmp_29 = (_tmp_26 || !_tmp_24) && (_tmp_27 || !_tmp_25);
  reg [_tmp_28-1:0] __tmp_29_1;
  wire [32-1:0] _tmp_30;
  reg [32-1:0] __tmp_30_1;
  assign _tmp_30 = (__tmp_29_1)? ram_b_0_rdata : __tmp_30_1;
  reg [8-1:0] _tmp_31;
  reg _tmp_32;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg [8-1:0] _tmp_36;
  reg _tmp_37;
  wire [32-1:0] _tmp_data_38;
  wire _tmp_valid_38;
  wire _tmp_ready_38;
  assign _tmp_ready_38 = !_tmp_37;
  reg _ram_c_cond_0_1;
  reg [32-1:0] _tmp_fsm_2;
  localparam _tmp_fsm_2_init = 0;
  reg [8-1:0] _tmp_39;
  reg _myaxi_cond_2_1;
  reg _tmp_40;
  reg _tmp_41;
  wire _tmp_42;
  wire _tmp_43;
  assign _tmp_42 = 1 && _tmp_ready_53;
  assign _tmp_43 = 1;
  localparam _tmp_44 = 1;
  wire [_tmp_44-1:0] _tmp_45;
  assign _tmp_45 = (_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41);
  reg [_tmp_44-1:0] __tmp_45_1;
  wire [32-1:0] _tmp_46;
  reg [32-1:0] __tmp_46_1;
  assign _tmp_46 = (__tmp_45_1)? ram_c_0_rdata : __tmp_46_1;
  reg [8-1:0] _tmp_47;
  reg _tmp_48;
  reg _tmp_49;
  reg _tmp_50;
  reg _tmp_51;
  reg _tmp_52;
  wire [32-1:0] _tmp_data_53;
  wire _tmp_valid_53;
  wire _tmp_ready_53;
  assign _tmp_ready_53 = (_tmp_fsm_2 == 2) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_3_1;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
      _tmp_6 <= 0;
      _myaxi_cond_1_1 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_39 <= 0;
      _myaxi_cond_2_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_52 <= 0;
      _myaxi_cond_3_1 <= 0;
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
        _tmp_52 <= 0;
      end 
      if((_tmp_fsm_0 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_0 == 0))) begin
        myaxi_araddr <= 1024;
        myaxi_arlen <= 63;
        myaxi_arvalid <= 1;
        _tmp_0 <= 64;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_0 > 0)) begin
        _tmp_0 <= _tmp_0 - 1;
      end 
      if((_tmp_fsm_1 == 1) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_6 == 0))) begin
        myaxi_araddr <= 2048;
        myaxi_arlen <= 63;
        myaxi_arvalid <= 1;
        _tmp_6 <= 64;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_6 > 0)) begin
        _tmp_6 <= _tmp_6 - 1;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_39 == 0))) begin
        myaxi_awaddr <= 3072;
        myaxi_awlen <= 63;
        myaxi_awvalid <= 1;
        _tmp_39 <= 64;
      end 
      if((_tmp_fsm_2 == 1) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_39 == 0)) && 0) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_tmp_valid_53 && ((_tmp_fsm_2 == 2) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0))) begin
        myaxi_wdata <= _tmp_data_53;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 4{ 1'd1 } };
        _tmp_39 <= _tmp_39 - 1;
      end 
      if(_tmp_valid_53 && ((_tmp_fsm_2 == 2) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_39 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_39 > 0)) && (_tmp_39 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_52 <= 1;
      end 
      _myaxi_cond_3_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_52 <= _tmp_52;
      end 
    end
  end

  assign _tmp_data_5 = myaxi_rdata;
  assign _tmp_valid_5 = myaxi_rvalid;
  assign _tmp_data_11 = myaxi_rdata;
  assign _tmp_valid_11 = myaxi_rvalid;

  always @(posedge CLK) begin
    if(RST) begin
      ram_a_0_addr <= 0;
      ram_a_0_wdata <= 0;
      ram_a_0_wenable <= 0;
      _tmp_3 <= 0;
      _tmp_4 <= 0;
      _ram_a_cond_0_1 <= 0;
      __tmp_17_1 <= 0;
      __tmp_18_1 <= 0;
      _tmp_23 <= 0;
      _tmp_12 <= 0;
      _tmp_13 <= 0;
      _tmp_21 <= 0;
      _tmp_22 <= 0;
      _tmp_20 <= 0;
      _tmp_19 <= 0;
    end else begin
      if(_ram_a_cond_0_1) begin
        ram_a_0_wenable <= 0;
        _tmp_4 <= 0;
      end 
      if(_tmp_valid_5 && ((_tmp_fsm_0 == 2) && !_tmp_4) && (_tmp_3 == 0)) begin
        ram_a_0_addr <= 0;
        ram_a_0_wdata <= _tmp_data_5;
        ram_a_0_wenable <= 1;
        _tmp_3 <= 63;
      end 
      if(_tmp_valid_5 && ((_tmp_fsm_0 == 2) && !_tmp_4) && (_tmp_3 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        ram_a_0_wdata <= _tmp_data_5;
        ram_a_0_wenable <= 1;
        _tmp_3 <= _tmp_3 - 1;
      end 
      if(_tmp_valid_5 && ((_tmp_fsm_0 == 2) && !_tmp_4) && (_tmp_3 == 1)) begin
        _tmp_4 <= 1;
      end 
      _ram_a_cond_0_1 <= 1;
      __tmp_17_1 <= _tmp_17;
      __tmp_18_1 <= _tmp_18;
      if((_tmp_14 || !_tmp_12) && (_tmp_15 || !_tmp_13) && _tmp_21) begin
        _tmp_23 <= 0;
        _tmp_12 <= 0;
        _tmp_13 <= 0;
        _tmp_21 <= 0;
      end 
      if((_tmp_14 || !_tmp_12) && (_tmp_15 || !_tmp_13) && _tmp_20) begin
        _tmp_12 <= 1;
        _tmp_13 <= 1;
        _tmp_23 <= _tmp_22;
        _tmp_22 <= 0;
        _tmp_20 <= 0;
        _tmp_21 <= 1;
      end 
      if((_tmp_14 || !_tmp_12) && (_tmp_15 || !_tmp_13) && (fsm == 2) && (_tmp_19 == 0) && !_tmp_22 && !_tmp_23) begin
        ram_a_0_addr <= 0;
        _tmp_19 <= 63;
        _tmp_20 <= 1;
      end 
      if((_tmp_14 || !_tmp_12) && (_tmp_15 || !_tmp_13) && (_tmp_19 > 0)) begin
        ram_a_0_addr <= ram_a_0_addr + 1;
        _tmp_19 <= _tmp_19 - 1;
        _tmp_20 <= 1;
        _tmp_22 <= 0;
      end 
      if((_tmp_14 || !_tmp_12) && (_tmp_15 || !_tmp_13) && (_tmp_19 == 1)) begin
        _tmp_22 <= 1;
      end 
    end
  end

  reg [32-1:0] _tmp_data_54;
  reg _tmp_valid_54;
  wire _tmp_ready_54;
  assign _tmp_data_38 = _tmp_data_54;
  assign _tmp_valid_38 = _tmp_valid_54;
  assign _tmp_ready_54 = _tmp_ready_38;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_54 <= 0;
      _tmp_valid_54 <= 0;
    end else begin
      if((_tmp_ready_54 || !_tmp_valid_54) && (_tmp_14 && _tmp_26) && (_tmp_12 && _tmp_24)) begin
        _tmp_data_54 <= _tmp_18 + _tmp_30;
      end 
      if(_tmp_valid_54 && _tmp_ready_54) begin
        _tmp_valid_54 <= 0;
      end 
      if((_tmp_ready_54 || !_tmp_valid_54) && (_tmp_14 && _tmp_26)) begin
        _tmp_valid_54 <= _tmp_12 && _tmp_24;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_b_0_addr <= 0;
      ram_b_0_wdata <= 0;
      ram_b_0_wenable <= 0;
      _tmp_9 <= 0;
      _tmp_10 <= 0;
      _ram_b_cond_0_1 <= 0;
      __tmp_29_1 <= 0;
      __tmp_30_1 <= 0;
      _tmp_35 <= 0;
      _tmp_24 <= 0;
      _tmp_25 <= 0;
      _tmp_33 <= 0;
      _tmp_34 <= 0;
      _tmp_32 <= 0;
      _tmp_31 <= 0;
    end else begin
      if(_ram_b_cond_0_1) begin
        ram_b_0_wenable <= 0;
        _tmp_10 <= 0;
      end 
      if(_tmp_valid_11 && ((_tmp_fsm_1 == 2) && !_tmp_10) && (_tmp_9 == 0)) begin
        ram_b_0_addr <= 0;
        ram_b_0_wdata <= _tmp_data_11;
        ram_b_0_wenable <= 1;
        _tmp_9 <= 63;
      end 
      if(_tmp_valid_11 && ((_tmp_fsm_1 == 2) && !_tmp_10) && (_tmp_9 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        ram_b_0_wdata <= _tmp_data_11;
        ram_b_0_wenable <= 1;
        _tmp_9 <= _tmp_9 - 1;
      end 
      if(_tmp_valid_11 && ((_tmp_fsm_1 == 2) && !_tmp_10) && (_tmp_9 == 1)) begin
        _tmp_10 <= 1;
      end 
      _ram_b_cond_0_1 <= 1;
      __tmp_29_1 <= _tmp_29;
      __tmp_30_1 <= _tmp_30;
      if((_tmp_26 || !_tmp_24) && (_tmp_27 || !_tmp_25) && _tmp_33) begin
        _tmp_35 <= 0;
        _tmp_24 <= 0;
        _tmp_25 <= 0;
        _tmp_33 <= 0;
      end 
      if((_tmp_26 || !_tmp_24) && (_tmp_27 || !_tmp_25) && _tmp_32) begin
        _tmp_24 <= 1;
        _tmp_25 <= 1;
        _tmp_35 <= _tmp_34;
        _tmp_34 <= 0;
        _tmp_32 <= 0;
        _tmp_33 <= 1;
      end 
      if((_tmp_26 || !_tmp_24) && (_tmp_27 || !_tmp_25) && (fsm == 2) && (_tmp_31 == 0) && !_tmp_34 && !_tmp_35) begin
        ram_b_0_addr <= 0;
        _tmp_31 <= 63;
        _tmp_32 <= 1;
      end 
      if((_tmp_26 || !_tmp_24) && (_tmp_27 || !_tmp_25) && (_tmp_31 > 0)) begin
        ram_b_0_addr <= ram_b_0_addr + 1;
        _tmp_31 <= _tmp_31 - 1;
        _tmp_32 <= 1;
        _tmp_34 <= 0;
      end 
      if((_tmp_26 || !_tmp_24) && (_tmp_27 || !_tmp_25) && (_tmp_31 == 1)) begin
        _tmp_34 <= 1;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      ram_c_0_addr <= 0;
      ram_c_0_wdata <= 0;
      ram_c_0_wenable <= 0;
      _tmp_36 <= 0;
      _tmp_37 <= 0;
      _ram_c_cond_0_1 <= 0;
      __tmp_45_1 <= 0;
      __tmp_46_1 <= 0;
      _tmp_51 <= 0;
      _tmp_40 <= 0;
      _tmp_41 <= 0;
      _tmp_49 <= 0;
      _tmp_50 <= 0;
      _tmp_48 <= 0;
      _tmp_47 <= 0;
    end else begin
      if(_ram_c_cond_0_1) begin
        ram_c_0_wenable <= 0;
        _tmp_37 <= 0;
      end 
      if(_tmp_valid_38 && !_tmp_37 && (_tmp_36 == 0)) begin
        ram_c_0_addr <= 0;
        ram_c_0_wdata <= _tmp_data_38;
        ram_c_0_wenable <= 1;
        _tmp_36 <= 63;
      end 
      if(_tmp_valid_38 && !_tmp_37 && (_tmp_36 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        ram_c_0_wdata <= _tmp_data_38;
        ram_c_0_wenable <= 1;
        _tmp_36 <= _tmp_36 - 1;
      end 
      if(_tmp_valid_38 && !_tmp_37 && (_tmp_36 == 1)) begin
        _tmp_37 <= 1;
      end 
      _ram_c_cond_0_1 <= 1;
      __tmp_45_1 <= _tmp_45;
      __tmp_46_1 <= _tmp_46;
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && _tmp_49) begin
        _tmp_51 <= 0;
        _tmp_40 <= 0;
        _tmp_41 <= 0;
        _tmp_49 <= 0;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && _tmp_48) begin
        _tmp_40 <= 1;
        _tmp_41 <= 1;
        _tmp_51 <= _tmp_50;
        _tmp_50 <= 0;
        _tmp_48 <= 0;
        _tmp_49 <= 1;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && (_tmp_fsm_2 == 2) && (_tmp_47 == 0) && !_tmp_50 && !_tmp_51) begin
        ram_c_0_addr <= 0;
        _tmp_47 <= 63;
        _tmp_48 <= 1;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && (_tmp_47 > 0)) begin
        ram_c_0_addr <= ram_c_0_addr + 1;
        _tmp_47 <= _tmp_47 - 1;
        _tmp_48 <= 1;
        _tmp_50 <= 0;
      end 
      if((_tmp_42 || !_tmp_40) && (_tmp_43 || !_tmp_41) && (_tmp_47 == 1)) begin
        _tmp_50 <= 1;
      end 
    end
  end

  assign _tmp_data_53 = _tmp_46;
  assign _tmp_valid_53 = _tmp_40;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;
  localparam fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
    end else begin
      case(fsm)
        fsm_init: begin
          if(_tmp_4) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_tmp_10) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_tmp_23) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_tmp_37) begin
            fsm <= fsm_4;
          end 
        end
        fsm_4: begin
          if(_tmp_52) begin
            fsm <= fsm_5;
          end 
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
    end else begin
      case(_tmp_fsm_0)
        _tmp_fsm_0_init: begin
          if(fsm == 0) begin
            _tmp_fsm_0 <= _tmp_fsm_0_1;
          end 
        end
        _tmp_fsm_0_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_0 <= _tmp_fsm_0_2;
          end 
        end
        _tmp_fsm_0_2: begin
          if(_tmp_4) begin
            _tmp_fsm_0 <= _tmp_fsm_0_3;
          end 
        end
        _tmp_fsm_0_3: begin
          _tmp_fsm_0 <= _tmp_fsm_0_init;
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
    end else begin
      case(_tmp_fsm_1)
        _tmp_fsm_1_init: begin
          if(fsm == 1) begin
            _tmp_fsm_1 <= _tmp_fsm_1_1;
          end 
        end
        _tmp_fsm_1_1: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _tmp_fsm_1 <= _tmp_fsm_1_2;
          end 
        end
        _tmp_fsm_1_2: begin
          if(_tmp_10) begin
            _tmp_fsm_1 <= _tmp_fsm_1_3;
          end 
        end
        _tmp_fsm_1_3: begin
          _tmp_fsm_1 <= _tmp_fsm_1_init;
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
          if(fsm == 4) begin
            _tmp_fsm_2 <= _tmp_fsm_2_1;
          end 
        end
        _tmp_fsm_2_1: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _tmp_fsm_2 <= _tmp_fsm_2_2;
          end 
        end
        _tmp_fsm_2_2: begin
          if(_tmp_52) begin
            _tmp_fsm_2 <= _tmp_fsm_2_3;
          end 
        end
        _tmp_fsm_2_3: begin
          _tmp_fsm_2 <= _tmp_fsm_2_init;
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", sum, 200640);
      end 
      if(myaxi_wvalid && myaxi_wready) begin
        sum <= sum + myaxi_wdata;
      end 
      _seq_cond_0_1 <= myaxi_wvalid && myaxi_wready && myaxi_wlast;
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
    test_module = axi_vecadd.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
