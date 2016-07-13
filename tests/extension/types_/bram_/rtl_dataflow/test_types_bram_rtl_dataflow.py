from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import types_bram_rtl_dataflow
import veriloggen

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

  reg [14-1:0] mybram_0_addr;
  wire [32-1:0] mybram_0_rdata;
  reg [32-1:0] mybram_0_wdata;
  reg mybram_0_wenable;
  reg [14-1:0] mybram_1_addr;
  wire [32-1:0] mybram_1_rdata;
  reg [32-1:0] mybram_1_wdata;
  reg mybram_1_wenable;

  mybram
  inst_mybram
  (
    .CLK(CLK),
    .mybram_0_addr(mybram_0_addr),
    .mybram_0_rdata(mybram_0_rdata),
    .mybram_0_wdata(mybram_0_wdata),
    .mybram_0_wenable(mybram_0_wenable),
    .mybram_1_addr(mybram_1_addr),
    .mybram_1_rdata(mybram_1_rdata),
    .mybram_1_wdata(mybram_1_wdata),
    .mybram_1_wenable(mybram_1_wenable)
  );

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] xaddr;
  reg [32-1:0] xcount;
  wire [32-1:0] xdata;
  wire xvalid;
  wire xready;
  reg [32-1:0] _tmp_data_0;
  reg _tmp_valid_0;
  wire _tmp_ready_0;
  assign xready = (_tmp_ready_0 || !_tmp_valid_0) && xvalid;
  wire [32-1:0] ydata;
  wire yvalid;
  wire yread;
  assign ydata = _tmp_data_0;
  assign yvalid = _tmp_valid_0;
  assign _tmp_ready_0 = yread;
  reg _mybram_cond_0_1;
  reg _tmp_1;
  reg _mybram_cond_1_1;
  reg _mybram_cond_2_1;
  reg _mybram_cond_2_2;
  reg [32-1:0] _tmp_2;
  assign xdata = _tmp_2;
  reg _tmp_3;
  assign xvalid = _tmp_3;
  reg __dataflow_seq_1_cond_0_1;
  reg [32-1:0] _xaddr_1;
  reg [32-1:0] _xaddr_2;
  reg [32-1:0] yfsm;
  localparam yfsm_init = 0;
  reg [32-1:0] yaddr;
  assign yread = yfsm == 1;
  reg _mybram_cond_3_1;
  reg _tmp_4;
  reg _mybram_cond_4_1;
  reg _mybram_cond_5_1;
  reg _mybram_cond_5_2;
  reg [32-1:0] _yaddr_1;
  reg [32-1:0] _yaddr_2;

  always @(posedge CLK) begin
    if(RST) begin
      mybram_0_addr <= 0;
      mybram_0_wdata <= 0;
      mybram_0_wenable <= 0;
      _mybram_cond_0_1 <= 0;
      _mybram_cond_1_1 <= 0;
      _tmp_1 <= 0;
      _mybram_cond_2_1 <= 0;
      _mybram_cond_2_2 <= 0;
      mybram_1_addr <= 0;
      mybram_1_wdata <= 0;
      mybram_1_wenable <= 0;
      _mybram_cond_3_1 <= 0;
      _mybram_cond_4_1 <= 0;
      _tmp_4 <= 0;
      _mybram_cond_5_1 <= 0;
      _mybram_cond_5_2 <= 0;
    end else begin
      if(_mybram_cond_2_2) begin
        _tmp_1 <= 0;
      end 
      if(_mybram_cond_5_2) begin
        _tmp_4 <= 0;
      end 
      if(_mybram_cond_0_1) begin
        mybram_0_wenable <= 0;
      end 
      if(_mybram_cond_1_1) begin
        _tmp_1 <= 1;
      end 
      _mybram_cond_2_2 <= _mybram_cond_2_1;
      if(_mybram_cond_3_1) begin
        mybram_1_wenable <= 0;
      end 
      if(_mybram_cond_4_1) begin
        _tmp_4 <= 1;
      end 
      _mybram_cond_5_2 <= _mybram_cond_5_1;
      if(xfsm == 1) begin
        mybram_0_addr <= xaddr;
        mybram_0_wdata <= xcount;
        mybram_0_wenable <= 1;
      end 
      _mybram_cond_0_1 <= xfsm == 1;
      if((xfsm == 2) && (xaddr < 16)) begin
        mybram_0_addr <= xaddr;
      end 
      _mybram_cond_1_1 <= (xfsm == 2) && (xaddr < 16);
      _mybram_cond_2_1 <= (xfsm == 2) && (xaddr < 16);
      if((yfsm == 1) && (yvalid && (yfsm == 1))) begin
        mybram_1_addr <= yaddr;
        mybram_1_wdata <= ydata;
        mybram_1_wenable <= 1;
      end 
      _mybram_cond_3_1 <= (yfsm == 1) && (yvalid && (yfsm == 1));
      if((yfsm == 2) && (yaddr < 16)) begin
        mybram_1_addr <= yaddr;
      end 
      _mybram_cond_4_1 <= (yfsm == 2) && (yaddr < 16);
      _mybram_cond_5_1 <= (yfsm == 2) && (yaddr < 16);
    end
  end

  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      xaddr <= 0;
      xcount <= 0;
      _xaddr_1 <= 0;
      _xaddr_2 <= 0;
    end else begin
      _xaddr_1 <= xaddr;
      _xaddr_2 <= _xaddr_1;
      case(xfsm)
        xfsm_init: begin
          xaddr <= 0;
          xcount <= 0;
          xfsm <= xfsm_1;
        end
        xfsm_1: begin
          xaddr <= xaddr + 1;
          xcount <= xcount + 1;
          if(xcount == 15) begin
            xaddr <= 0;
            xcount <= 0;
          end 
          if(xcount == 15) begin
            xfsm <= xfsm_2;
          end 
        end
        xfsm_2: begin
          xaddr <= xaddr + 1;
          if(_tmp_1) begin
            $display("BRAM0[%d] = %d", _xaddr_2, mybram_0_rdata);
          end 
          if(_xaddr_1 == 16) begin
            xfsm <= xfsm_3;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_0 <= 0;
      _tmp_valid_0 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      __dataflow_seq_1_cond_0_1 <= 0;
    end else begin
      if(__dataflow_seq_1_cond_0_1) begin
        _tmp_3 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && xready && xvalid) begin
        _tmp_data_0 <= xdata + 8'd100;
      end 
      if(_tmp_valid_0 && _tmp_ready_0) begin
        _tmp_valid_0 <= 0;
      end 
      if((_tmp_ready_0 || !_tmp_valid_0) && xready) begin
        _tmp_valid_0 <= xvalid;
      end 
      if(_tmp_1 && (xready || !_tmp_3)) begin
        _tmp_2 <= mybram_0_rdata;
      end 
      if(_tmp_1 && (xready || !_tmp_3)) begin
        _tmp_3 <= 1;
      end 
      __dataflow_seq_1_cond_0_1 <= 1;
      if(_tmp_3 && !xready) begin
        _tmp_3 <= _tmp_3;
      end 
    end
  end

  localparam yfsm_1 = 1;
  localparam yfsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      yfsm <= yfsm_init;
      yaddr <= 0;
      _yaddr_1 <= 0;
      _yaddr_2 <= 0;
    end else begin
      _yaddr_1 <= yaddr;
      _yaddr_2 <= _yaddr_1;
      case(yfsm)
        yfsm_init: begin
          yaddr <= 0;
          yfsm <= yfsm_1;
        end
        yfsm_1: begin
          if(yvalid && (yfsm == 1)) begin
            yaddr <= yaddr + 1;
          end 
          if(yaddr == 15) begin
            yaddr <= 0;
          end 
          if(yaddr == 15) begin
            yfsm <= yfsm_2;
          end 
        end
        yfsm_2: begin
          if(yaddr < 16) begin
            yaddr <= yaddr + 1;
          end 
          if(_tmp_4) begin
            $display("BRAM1[%d] = %d", _yaddr_2, mybram_1_rdata);
          end 
        end
      endcase
    end
  end


endmodule



module mybram
(
  input CLK,
  input [14-1:0] mybram_0_addr,
  output [32-1:0] mybram_0_rdata,
  input [32-1:0] mybram_0_wdata,
  input mybram_0_wenable,
  input [14-1:0] mybram_1_addr,
  output [32-1:0] mybram_1_rdata,
  input [32-1:0] mybram_1_wdata,
  input mybram_1_wenable
);

  reg [14-1:0] mybram_0_daddr;
  reg [14-1:0] mybram_1_daddr;
  reg [32-1:0] mem [0:16384-1];

  always @(posedge CLK) begin
    if(mybram_0_wenable) begin
      mem[mybram_0_addr] <= mybram_0_wdata;
    end 
    mybram_0_daddr <= mybram_0_addr;
  end

  assign mybram_0_rdata = mem[mybram_0_daddr];

  always @(posedge CLK) begin
    if(mybram_1_wenable) begin
      mem[mybram_1_addr] <= mybram_1_wdata;
    end 
    mybram_1_daddr <= mybram_1_addr;
  end

  assign mybram_1_rdata = mem[mybram_1_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    veriloggen.reset()
    
    test_module = types_bram_rtl_dataflow.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
