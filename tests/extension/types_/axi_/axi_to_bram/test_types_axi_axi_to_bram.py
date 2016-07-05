from __future__ import absolute_import
from __future__ import print_function
import types_axi_axi_to_bram

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
  wire _tmp_0;
  assign _tmp_0 = 1;

  always @(*) begin
    myaxi_awready <= _tmp_0;
  end

  wire _tmp_1;
  assign _tmp_1 = 1;

  always @(*) begin
    myaxi_wready <= _tmp_1;
  end

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
          if(myaxi_rvalid && !myaxi_rready) begin
            myaxi_rvalid <= myaxi_rvalid;
            myaxi_rlast <= myaxi_rlast;
          end 
          if(myaxi_rvalid && myaxi_rready && myaxi_rlast) begin
            raddr <= raddr_4;
          end 
        end
        raddr_4: begin
          raddr <= raddr_5;
        end
        raddr_5: begin
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
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_araddr, myaxi_arlen, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rlast, myaxi_rvalid, myaxi_rready, _tmp_0, _tmp_1, raddr, _arlen, _d1_raddr, _raddr_cond_3_0_1);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
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

  reg [10-1:0] mybram_0_addr;
  wire [32-1:0] mybram_0_rdata;
  reg [32-1:0] mybram_0_wdata;
  reg mybram_0_wenable;

  mybram
  inst_mybram
  (
    .CLK(CLK),
    .mybram_0_addr(mybram_0_addr),
    .mybram_0_rdata(mybram_0_rdata),
    .mybram_0_wdata(mybram_0_wdata),
    .mybram_0_wenable(mybram_0_wenable)
  );

  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [8-1:0] _tmp_0;
  reg _myaxi_cond_0_1;
  reg [8-1:0] _tmp_1;
  reg [8-1:0] _tmp_2;
  wire _tmp_3;
  wire _tmp_4;
  assign _tmp_3 = 1 && ((_tmp_ready_6 || !_tmp_valid_6) && (myaxi_rvalid && myaxi_rvalid));
  assign _tmp_4 = 1 && ((_tmp_ready_6 || !_tmp_valid_6) && (myaxi_rvalid && myaxi_rvalid)) && ((_tmp_ready_7 || !_tmp_valid_7) && myaxi_rvalid);
  assign myaxi_rready = _tmp_3 && _tmp_4;
  reg [32-1:0] _tmp_data_5;
  reg [32-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  reg [32-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  wire [32-1:0] sum_data;
  wire sum_valid;
  assign sum_data = _tmp_data_6;
  assign sum_valid = _tmp_valid_6;
  assign _tmp_ready_6 = 1;
  wire [32-1:0] axi_last_data;
  wire axi_last_valid;
  assign axi_last_data = _tmp_data_7;
  assign axi_last_valid = _tmp_valid_7;
  assign _tmp_ready_7 = 1;
  reg _tmp_8;
  reg _mybram_cond_0_1;
  reg [8-1:0] _tmp_9;
  reg [8-1:0] _tmp_10;
  wire _tmp_11;
  wire _tmp_12;
  assign _tmp_11 = 1 && 1;
  assign _tmp_12 = 1 && 1;
  reg _tmp_13;
  reg _tmp_14;
  reg _mybram_cond_1_1;
  reg _mybram_cond_2_1;
  reg _mybram_cond_3_1;
  reg _mybram_cond_3_2;
  wire [32-1:0] rslt_data;
  wire rslt_valid;
  assign rslt_data = mybram_0_rdata;
  assign rslt_valid = _tmp_13;
  wire [32-1:0] last_data;
  wire last_valid;
  assign last_data = _tmp_14;
  assign last_valid = _tmp_13;
  reg [32-1:0] sum;
  reg _seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      myaxi_wdata <= 0;
      myaxi_wstrb <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_0 <= 0;
      _myaxi_cond_0_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      myaxi_wdata <= 0;
      myaxi_wstrb <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      if((fsm == 0) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_0 == 0))) begin
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
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      mybram_0_addr <= 0;
      mybram_0_wdata <= 0;
      mybram_0_wenable <= 0;
      _tmp_8 <= 0;
      _mybram_cond_0_1 <= 0;
      _tmp_9 <= 0;
      _tmp_10 <= 0;
      _mybram_cond_1_1 <= 0;
      _tmp_13 <= 0;
      _tmp_14 <= 0;
      _mybram_cond_2_1 <= 0;
      _mybram_cond_3_1 <= 0;
      _mybram_cond_3_2 <= 0;
    end else begin
      if(_mybram_cond_3_2) begin
        _tmp_13 <= 0;
        _tmp_14 <= 0;
      end 
      if(_mybram_cond_0_1) begin
        mybram_0_wenable <= 0;
        _tmp_8 <= 0;
      end 
      if(_mybram_cond_1_1) begin
        _tmp_13 <= 1;
        _tmp_14 <= 0;
      end 
      if(_mybram_cond_2_1) begin
        _tmp_14 <= 1;
      end 
      _mybram_cond_3_2 <= _mybram_cond_3_1;
      if((fsm == 1) && (_tmp_1 == 0)) begin
        _tmp_1 <= 64;
        _tmp_2 <= 0;
      end 
      if(sum_valid && ((fsm == 2) && (_tmp_1 > 0)) && (_tmp_1 > 0)) begin
        mybram_0_addr <= _tmp_2;
        mybram_0_wdata <= sum_data;
        mybram_0_wenable <= 1;
        _tmp_2 <= _tmp_2 + 1;
        _tmp_1 <= _tmp_1 - 1;
      end 
      if(sum_valid && ((fsm == 2) && (_tmp_1 > 0)) && (_tmp_1 > 0) && (_tmp_1 == 1)) begin
        _tmp_8 <= 1;
      end 
      _mybram_cond_0_1 <= 1;
      if((fsm == 3) && (_tmp_9 == 0)) begin
        _tmp_9 <= 64;
        _tmp_10 <= 0;
      end 
      if((_tmp_9 > 0) && ((fsm == 4) && _tmp_11 && _tmp_12)) begin
        mybram_0_addr <= _tmp_10;
        _tmp_9 <= _tmp_9 - 1;
        _tmp_10 <= _tmp_10 + 1;
      end 
      _mybram_cond_1_1 <= (_tmp_9 > 0) && ((fsm == 4) && _tmp_11 && _tmp_12);
      _mybram_cond_2_1 <= (_tmp_9 > 0) && ((fsm == 4) && _tmp_11 && _tmp_12) && (_tmp_9 == 1);
      _mybram_cond_3_1 <= 1;
      if((_tmp_9 > 0) && !((fsm == 4) && _tmp_11 && _tmp_12)) begin
        _tmp_9 <= _tmp_9;
        _tmp_10 <= _tmp_10;
        _tmp_13 <= _tmp_13;
      end 
    end
  end

  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;
  localparam fsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
    end else begin
      case(fsm)
        fsm_init: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          if(_tmp_1 == 0) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          if(_tmp_8) begin
            fsm <= fsm_3;
          end 
        end
        fsm_3: begin
          if(_tmp_9 == 0) begin
            fsm <= fsm_4;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_5 <= 0;
      _tmp_data_6 <= 1'd0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
    end else begin
      if(myaxi_rvalid && _tmp_4) begin
        _tmp_data_5 <= myaxi_rlast;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_3 && _tmp_4) && (myaxi_rvalid && myaxi_rvalid)) begin
        _tmp_data_6 <= _tmp_data_6 + myaxi_rdata;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_3 && _tmp_4)) begin
        _tmp_valid_6 <= myaxi_rvalid && myaxi_rvalid;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && (_tmp_3 && _tmp_4) && (myaxi_rvalid && myaxi_rvalid) && _tmp_data_5) begin
        _tmp_data_6 <= 1'd0 + myaxi_rdata;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_4 && myaxi_rvalid) begin
        _tmp_data_7 <= myaxi_rlast;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_4) begin
        _tmp_valid_7 <= myaxi_rvalid;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      sum <= 0;
      _seq_cond_0_1 <= 0;
    end else begin
      if(_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", sum, 2173600);
      end 
      if(rslt_valid) begin
        sum <= sum + rslt_data;
      end 
      _seq_cond_0_1 <= rslt_valid && (last_data == 1);
    end
  end


endmodule



module mybram
(
  input CLK,
  input [10-1:0] mybram_0_addr,
  output [32-1:0] mybram_0_rdata,
  input [32-1:0] mybram_0_wdata,
  input mybram_0_wenable
);

  reg [10-1:0] mybram_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(mybram_0_wenable) begin
      mem[mybram_0_addr] <= mybram_0_wdata;
    end 
    mybram_0_daddr <= mybram_0_addr;
  end

  assign mybram_0_rdata = mem[mybram_0_daddr];

endmodule
"""


def test():
    test_module = types_axi_axi_to_bram.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
