from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_axi_read_dataflow

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire [3-1:0] myaxi_awsize;
  wire [2-1:0] myaxi_awburst;
  wire [1-1:0] myaxi_awlock;
  wire [4-1:0] myaxi_awcache;
  wire [3-1:0] myaxi_awprot;
  wire [4-1:0] myaxi_awqos;
  wire [2-1:0] myaxi_awuser;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [32-1:0] myaxi_wdata;
  wire [4-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  reg [2-1:0] myaxi_bresp;
  reg myaxi_bvalid;
  wire myaxi_bready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire [3-1:0] myaxi_arsize;
  wire [2-1:0] myaxi_arburst;
  wire [1-1:0] myaxi_arlock;
  wire [4-1:0] myaxi_arcache;
  wire [3-1:0] myaxi_arprot;
  wire [4-1:0] myaxi_arqos;
  wire [2-1:0] myaxi_aruser;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [32-1:0] myaxi_rdata;
  reg [2-1:0] myaxi_rresp;
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
    .myaxi_awsize(myaxi_awsize),
    .myaxi_awburst(myaxi_awburst),
    .myaxi_awlock(myaxi_awlock),
    .myaxi_awcache(myaxi_awcache),
    .myaxi_awprot(myaxi_awprot),
    .myaxi_awqos(myaxi_awqos),
    .myaxi_awuser(myaxi_awuser),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_bresp(myaxi_bresp),
    .myaxi_bvalid(myaxi_bvalid),
    .myaxi_bready(myaxi_bready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arsize(myaxi_arsize),
    .myaxi_arburst(myaxi_arburst),
    .myaxi_arlock(myaxi_arlock),
    .myaxi_arcache(myaxi_arcache),
    .myaxi_arprot(myaxi_arprot),
    .myaxi_arqos(myaxi_arqos),
    .myaxi_aruser(myaxi_aruser),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rresp(myaxi_rresp),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut, CLK, RST, myaxi_awaddr, myaxi_awlen, myaxi_awsize, myaxi_awburst, myaxi_awlock, myaxi_awcache, myaxi_awprot, myaxi_awqos, myaxi_awuser, myaxi_awvalid, myaxi_awready, myaxi_wdata, myaxi_wstrb, myaxi_wlast, myaxi_wvalid, myaxi_wready, myaxi_bresp, myaxi_bvalid, myaxi_bready, myaxi_araddr, myaxi_arlen, myaxi_arsize, myaxi_arburst, myaxi_arlock, myaxi_arcache, myaxi_arprot, myaxi_arqos, myaxi_aruser, myaxi_arvalid, myaxi_arready, myaxi_rdata, myaxi_rresp, myaxi_rlast, myaxi_rvalid, myaxi_rready, _tmp_0, _tmp_1, raddr, _arlen, _d1_raddr, _raddr_cond_3_0_1);
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
  output [3-1:0] myaxi_awsize,
  output [2-1:0] myaxi_awburst,
  output [1-1:0] myaxi_awlock,
  output [4-1:0] myaxi_awcache,
  output [3-1:0] myaxi_awprot,
  output [4-1:0] myaxi_awqos,
  output [2-1:0] myaxi_awuser,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [32-1:0] myaxi_wdata,
  output reg [4-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  input [2-1:0] myaxi_bresp,
  input myaxi_bvalid,
  output myaxi_bready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output [3-1:0] myaxi_arsize,
  output [2-1:0] myaxi_arburst,
  output [1-1:0] myaxi_arlock,
  output [4-1:0] myaxi_arcache,
  output [3-1:0] myaxi_arprot,
  output [4-1:0] myaxi_arqos,
  output [2-1:0] myaxi_aruser,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [32-1:0] myaxi_rdata,
  input [2-1:0] myaxi_rresp,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  assign myaxi_awsize = 2;
  assign myaxi_awburst = 1;
  assign myaxi_awlock = 0;
  assign myaxi_awcache = 3;
  assign myaxi_awprot = 0;
  assign myaxi_awqos = 0;
  assign myaxi_awuser = 0;
  assign myaxi_bready = 1;
  assign myaxi_arsize = 2;
  assign myaxi_arburst = 1;
  assign myaxi_arlock = 0;
  assign myaxi_arcache = 3;
  assign myaxi_arprot = 0;
  assign myaxi_arqos = 0;
  assign myaxi_aruser = 0;
  reg [32-1:0] outstanding_wreq_count_0;
  reg [32-1:0] req_fsm;
  localparam req_fsm_init = 0;
  reg [9-1:0] counter_1;
  reg _myaxi_cond_0_1;
  wire data_ready_2;
  wire last_ready_3;
  assign myaxi_rready = data_ready_2 && last_ready_3;
  wire signed [32-1:0] _dataflow_reduceadd_odata_4;
  wire _dataflow_reduceadd_ovalid_4;
  wire _dataflow_reduceadd_oready_4;
  assign _dataflow_reduceadd_oready_4 = 1;
  wire [1-1:0] _dataflow__variable_odata_1;
  wire _dataflow__variable_ovalid_1;
  wire _dataflow__variable_oready_1;
  assign _dataflow__variable_oready_1 = 1;
  reg _data_seq_cond_0_1;

  always @(posedge CLK) begin
    if(RST) begin
      outstanding_wreq_count_0 <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      myaxi_wdata <= 0;
      myaxi_wstrb <= 0;
      myaxi_wlast <= 0;
      myaxi_wvalid <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      counter_1 <= 0;
      _myaxi_cond_0_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_arvalid <= 0;
      end 
      if(myaxi_awvalid && myaxi_awready && !(myaxi_bvalid && myaxi_bready)) begin
        outstanding_wreq_count_0 <= outstanding_wreq_count_0 + 1;
      end 
      if(!(myaxi_awvalid && myaxi_awready) && (myaxi_bvalid && myaxi_bready) && (outstanding_wreq_count_0 > 0)) begin
        outstanding_wreq_count_0 <= outstanding_wreq_count_0 - 1;
      end 
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      myaxi_wdata <= 0;
      myaxi_wstrb <= 0;
      myaxi_wlast <= 0;
      myaxi_wvalid <= 0;
      if((req_fsm == 0) && ((myaxi_arready || !myaxi_arvalid) && (counter_1 == 0))) begin
        myaxi_araddr <= 1024;
        myaxi_arlen <= 63;
        myaxi_arvalid <= 1;
        counter_1 <= 64;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (counter_1 > 0)) begin
        counter_1 <= counter_1 - 1;
      end 
    end
  end

  assign _dataflow__variable_odata_1 = myaxi_rlast;
  assign _dataflow__variable_ovalid_1 = myaxi_rvalid;
  reg [1-1:0] _dataflow__prev_data_2;
  reg signed [32-1:0] _dataflow_reduceadd_data_4;
  reg _dataflow_reduceadd_valid_4;
  wire _dataflow_reduceadd_ready_4;
  assign data_ready_2 = 1 && ((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (myaxi_rvalid && myaxi_rvalid));
  assign last_ready_3 = 1 && _dataflow__variable_oready_1 && ((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (myaxi_rvalid && myaxi_rvalid));
  assign _dataflow_reduceadd_odata_4 = _dataflow_reduceadd_data_4;
  assign _dataflow_reduceadd_ovalid_4 = _dataflow_reduceadd_valid_4;
  assign _dataflow_reduceadd_ready_4 = _dataflow_reduceadd_oready_4;

  always @(posedge CLK) begin
    if(RST) begin
      _dataflow__prev_data_2 <= 0;
      _dataflow_reduceadd_data_4 <= 1'sd0;
      _dataflow_reduceadd_valid_4 <= 0;
    end else begin
      if(myaxi_rvalid && last_ready_3) begin
        _dataflow__prev_data_2 <= myaxi_rlast;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (data_ready_2 && last_ready_3) && (myaxi_rvalid && myaxi_rvalid)) begin
        _dataflow_reduceadd_data_4 <= _dataflow_reduceadd_data_4 + myaxi_rdata;
      end 
      if(_dataflow_reduceadd_valid_4 && _dataflow_reduceadd_ready_4) begin
        _dataflow_reduceadd_valid_4 <= 0;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (data_ready_2 && last_ready_3)) begin
        _dataflow_reduceadd_valid_4 <= myaxi_rvalid && myaxi_rvalid;
      end 
      if((_dataflow_reduceadd_ready_4 || !_dataflow_reduceadd_valid_4) && (data_ready_2 && last_ready_3) && (myaxi_rvalid && myaxi_rvalid) && _dataflow__prev_data_2) begin
        _dataflow_reduceadd_data_4 <= 1'sd0 + myaxi_rdata;
      end 
    end
  end

  localparam req_fsm_1 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      req_fsm <= req_fsm_init;
    end else begin
      case(req_fsm)
        req_fsm_init: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            req_fsm <= req_fsm_1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _data_seq_cond_0_1 <= 0;
    end else begin
      if(_data_seq_cond_0_1) begin
        $display("sum=%d expected_sum=%d", _dataflow_reduceadd_odata_4, 67552);
      end 
      _data_seq_cond_0_1 <= _dataflow_reduceadd_ovalid_4 && _dataflow__variable_ovalid_1 && (_dataflow__variable_odata_1 == 1);
    end
  end


endmodule
"""


def test():
    veriloggen.reset()
    test_module = types_axi_read_dataflow.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
