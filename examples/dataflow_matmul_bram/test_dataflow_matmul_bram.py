from __future__ import absolute_import
from __future__ import print_function
import dataflow_matmul_bram

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  reg [8-1:0] bram_addr0;
  reg [32-1:0] bram_din0;
  reg bram_we0;
  wire [32-1:0] bram_dout0;
  reg [8-1:0] bram_addr1;
  reg [32-1:0] bram_din1;
  reg bram_we1;
  wire [32-1:0] bram_dout1;
  reg [8-1:0] bram_addr2;
  reg [32-1:0] bram_din2;
  reg bram_we2;
  wire [32-1:0] bram_dout2;
  reg start;
  wire busy;

  Matmul
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .bram_addr0(bram_addr0),
    .bram_din0(bram_din0),
    .bram_we0(bram_we0),
    .bram_dout0(bram_dout0),
    .bram_addr1(bram_addr1),
    .bram_din1(bram_din1),
    .bram_we1(bram_we1),
    .bram_dout1(bram_dout1),
    .bram_addr2(bram_addr2),
    .bram_din2(bram_din2),
    .bram_we2(bram_we2),
    .bram_dout2(bram_dout2),
    .start(start),
    .busy(busy)
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
    bram_addr0 = 0;
    bram_din0 = 0;
    bram_we0 = 0;
    bram_addr1 = 0;
    bram_din1 = 0;
    bram_we1 = 0;
    bram_addr2 = 0;
    bram_din2 = 0;
    bram_we2 = 0;
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
          bram_addr0 <= -1;
          bram_addr1 <= -1;
          bram_addr2 <= -1;
          fsm <= fsm_2;
        end
        fsm_2: begin
          bram_addr0 <= bram_addr0 + 1;
          bram_din0 <= (bram_addr0 + 1) % 256;
          bram_we0 <= 1;
          if(bram_we0 && (bram_addr0 == 255)) begin
            bram_we0 <= 0;
          end 
          bram_addr1 <= bram_addr1 + 1;
          bram_din1 <= ((bram_addr1 + 1) % 256 % 16 == (bram_addr1 + 1) % 256 / 16)? 2 : 0;
          bram_we1 <= 1;
          if(bram_we1 && (bram_addr1 == 255)) begin
            bram_we1 <= 0;
          end 
          bram_addr2 <= bram_addr2 + 1;
          bram_din2 <= ((bram_addr2 + 1) % 256 % 16 == (bram_addr2 + 1) % 256 / 16)? 2 : 0;
          bram_we2 <= 1;
          if(bram_we2 && (bram_addr2 == 255)) begin
            bram_we2 <= 0;
          end 
          if(bram_we2 && (bram_addr0 == 255)) begin
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


  always @(posedge CLK) begin
    if(uut.zwe) begin
      $display("zaddr=%10d zdout=%10d", uut.zaddr, uut.zdout);
      if(uut.zaddr * 2 != uut.zdout) begin
        $display("## wrong result");
      end 
    end 
  end


endmodule



module Matmul
(
  input CLK,
  input RST,
  input [8-1:0] bram_addr0,
  input [32-1:0] bram_din0,
  input bram_we0,
  output [32-1:0] bram_dout0,
  input [8-1:0] bram_addr1,
  input [32-1:0] bram_din1,
  input bram_we1,
  output [32-1:0] bram_dout1,
  input [8-1:0] bram_addr2,
  input [32-1:0] bram_din2,
  input bram_we2,
  output [32-1:0] bram_dout2,
  input start,
  output reg busy
);

  wire [8-1:0] _addr0;
  wire [32-1:0] _din0;
  wire _we0;
  wire [32-1:0] _dout0;
  wire [8-1:0] _addr1;
  wire [32-1:0] _din1;
  wire _we1;
  wire [32-1:0] _dout1;
  wire [8-1:0] _addr2;
  wire [32-1:0] _din2;
  wire _we2;
  wire [32-1:0] _dout2;

  BRAM2
  inst_bram0
  (
    .CLK(CLK),
    .ADDR0(bram_addr0),
    .DIN0(bram_din0),
    .WE0(bram_we0),
    .DOUT0(bram_dout0),
    .ADDR1(_addr0),
    .DIN1(_din0),
    .WE1(_we0),
    .DOUT1(_dout0)
  );


  BRAM2
  inst_bram1
  (
    .CLK(CLK),
    .ADDR0(bram_addr1),
    .DIN0(bram_din1),
    .WE0(bram_we1),
    .DOUT0(bram_dout1),
    .ADDR1(_addr1),
    .DIN1(_din1),
    .WE1(_we1),
    .DOUT1(_dout1)
  );


  BRAM2
  inst_bram2
  (
    .CLK(CLK),
    .ADDR0(bram_addr2),
    .DIN0(bram_din2),
    .WE0(bram_we2),
    .DOUT0(bram_dout2),
    .ADDR1(_addr2),
    .DIN1(_din2),
    .WE1(_we2),
    .DOUT1(_dout2)
  );

  reg [8-1:0] xaddr;
  wire [32-1:0] xdin;
  reg [8-1:0] yaddr;
  wire [32-1:0] ydin;
  reg [8-1:0] zaddr;
  reg [32-1:0] zdout;
  reg zwe;
  assign _addr0 = xaddr;
  assign _we0 = 0;
  assign xdin = _dout0;
  assign _addr1 = yaddr;
  assign _we1 = 0;
  assign ydin = _dout1;
  assign _addr2 = zaddr;
  assign _din2 = zdout;
  assign _we2 = zwe;
  reg ivalid;
  wire [32-1:0] odata;
  wire ovalid;
  reg vreset;

  madd
  madd
  (
    .CLK(CLK),
    .RST(RST),
    .xd(xdin),
    .xv(ivalid),
    .yd(ydin),
    .yv(ivalid),
    .zd(odata),
    .zv(ovalid),
    .vreset_data(vreset),
    .vreset(ivalid)
  );

  reg [5-1:0] _tmp_0;
  reg [32-1:0] _tmp_1;
  reg [5-1:0] _tmp_2;
  reg [32-1:0] fsm;
  localparam fsm_init = 0;
  reg [32-1:0] _d1_fsm;
  reg _fsm_cond_1_0_1;
  reg _fsm_cond_1_1_1;
  reg _fsm_cond_1_2_1;
  reg _fsm_cond_1_3_1;
  reg _fsm_cond_2_4_1;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      fsm <= fsm_init;
      _d1_fsm <= fsm_init;
      xaddr <= 0;
      yaddr <= 0;
      zaddr <= 0;
      busy <= 0;
      vreset <= 0;
      ivalid <= 0;
      _tmp_0 <= 0;
      _tmp_1 <= 0;
      _tmp_2 <= 0;
      _fsm_cond_1_0_1 <= 0;
      _fsm_cond_1_1_1 <= 0;
      _fsm_cond_1_2_1 <= 0;
      _fsm_cond_1_3_1 <= 0;
      zdout <= 0;
      _fsm_cond_2_4_1 <= 0;
    end else begin
      _d1_fsm <= fsm;
      case(_d1_fsm)
        fsm_1: begin
          if(_fsm_cond_1_0_1) begin
            vreset <= 0;
          end 
          if(_fsm_cond_1_1_1) begin
            vreset <= 1;
          end 
          if(_fsm_cond_1_2_1) begin
            ivalid <= 0;
          end 
          if(_fsm_cond_1_3_1) begin
            ivalid <= 1;
          end 
        end
        fsm_2: begin
          if(_fsm_cond_2_4_1) begin
            zwe <= 0;
          end 
        end
      endcase
      case(fsm)
        fsm_init: begin
          xaddr <= -1;
          yaddr <= -1;
          zaddr <= -1;
          zwe <= 0;
          busy <= 0;
          vreset <= 0;
          ivalid <= 0;
          _tmp_0 <= 0;
          _tmp_1 <= 0;
          _tmp_2 <= 0;
          if(start) begin
            busy <= 1;
          end 
          if(start) begin
            fsm <= fsm_1;
          end 
        end
        fsm_1: begin
          _fsm_cond_1_0_1 <= 1;
          _fsm_cond_1_1_1 <= _tmp_0 == 0;
          if(_tmp_0 < 16) begin
            xaddr <= xaddr + 1;
            yaddr <= yaddr + 1;
          end 
          _fsm_cond_1_2_1 <= 1;
          _fsm_cond_1_3_1 <= _tmp_0 < 16;
          if(_tmp_0 < 16) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if(ovalid) begin
            _tmp_2 <= _tmp_2 + 1;
          end 
          if(ovalid) begin
            _tmp_1 <= odata;
          end 
          if(_tmp_2 == 16) begin
            fsm <= fsm_2;
          end 
        end
        fsm_2: begin
          zaddr <= zaddr + 1;
          zdout <= _tmp_1;
          zwe <= 1;
          _fsm_cond_2_4_1 <= 1;
          if(yaddr == 255) begin
            yaddr <= -1;
          end 
          if(yaddr < 255) begin
            xaddr <= xaddr - 16;
          end 
          _tmp_0 <= 0;
          _tmp_2 <= 0;
          if(!(zaddr == 254)) begin
            fsm <= fsm_1;
          end 
          if(zaddr == 254) begin
            fsm <= fsm_init;
          end 
        end
      endcase
    end
  end


endmodule



module BRAM2
(
  input CLK,
  input [8-1:0] ADDR0,
  input [32-1:0] DIN0,
  input WE0,
  output [32-1:0] DOUT0,
  input [8-1:0] ADDR1,
  input [32-1:0] DIN1,
  input WE1,
  output [32-1:0] DOUT1
);

  reg [8-1:0] delay_ADDR0;
  reg [8-1:0] delay_ADDR1;
  reg [32-1:0] mem [0:256-1];

  always @(posedge CLK) begin
    if(WE0) begin
      mem[ADDR0] <= DIN0;
    end 
    delay_ADDR0 <= ADDR0;
  end

  assign DOUT0 = mem[delay_ADDR0];

  always @(posedge CLK) begin
    if(WE1) begin
      mem[ADDR1] <= DIN1;
    end 
    delay_ADDR1 <= ADDR1;
  end

  assign DOUT1 = mem[delay_ADDR1];

endmodule



module madd
(
  input CLK,
  input RST,
  input signed [32-1:0] xd,
  input xv,
  input signed [32-1:0] yd,
  input yv,
  input [1-1:0] vreset_data,
  input vreset,
  output signed [32-1:0] zd,
  output zv
);

  wire signed [32-1:0] _tmp_data_0;
  wire _tmp_valid_0;
  wire _tmp_ready_0;
  wire signed [64-1:0] _tmp_odata_0;
  reg signed [64-1:0] _tmp_data_reg_0;
  assign _tmp_data_0 = _tmp_data_reg_0;
  wire _tmp_ovalid_0;
  reg _tmp_valid_reg_0;
  assign _tmp_valid_0 = _tmp_valid_reg_0;
  wire _tmp_enable_0;
  wire _tmp_update_0;
  assign _tmp_enable_0 = (_tmp_ready_0 || !_tmp_valid_0) && 1 && (xv && yv);
  assign _tmp_update_0 = _tmp_ready_0 || !_tmp_valid_0;

  multiplier_0
  mul0
  (
    .CLK(CLK),
    .RST(RST),
    .update(_tmp_update_0),
    .enable(_tmp_enable_0),
    .valid(_tmp_ovalid_0),
    .a(xd),
    .b(yd),
    .c(_tmp_odata_0)
  );

  assign _tmp_ready_0 = (_tmp_ready_8 || !_tmp_valid_8) && (_tmp_valid_0 && _tmp_valid_7);
  reg [1-1:0] _tmp_data_1;
  reg _tmp_valid_1;
  wire _tmp_ready_1;
  assign _tmp_ready_1 = (_tmp_ready_2 || !_tmp_valid_2) && _tmp_valid_1;
  reg [1-1:0] _tmp_data_2;
  reg _tmp_valid_2;
  wire _tmp_ready_2;
  assign _tmp_ready_2 = (_tmp_ready_3 || !_tmp_valid_3) && _tmp_valid_2;
  reg [1-1:0] _tmp_data_3;
  reg _tmp_valid_3;
  wire _tmp_ready_3;
  assign _tmp_ready_3 = (_tmp_ready_4 || !_tmp_valid_4) && _tmp_valid_3;
  reg [1-1:0] _tmp_data_4;
  reg _tmp_valid_4;
  wire _tmp_ready_4;
  assign _tmp_ready_4 = (_tmp_ready_5 || !_tmp_valid_5) && _tmp_valid_4;
  reg [1-1:0] _tmp_data_5;
  reg _tmp_valid_5;
  wire _tmp_ready_5;
  assign _tmp_ready_5 = (_tmp_ready_6 || !_tmp_valid_6) && _tmp_valid_5;
  reg [1-1:0] _tmp_data_6;
  reg _tmp_valid_6;
  wire _tmp_ready_6;
  assign _tmp_ready_6 = (_tmp_ready_7 || !_tmp_valid_7) && _tmp_valid_6;
  reg [1-1:0] _tmp_data_7;
  reg _tmp_valid_7;
  wire _tmp_ready_7;
  assign _tmp_ready_7 = (_tmp_ready_8 || !_tmp_valid_8) && (_tmp_valid_0 && _tmp_valid_7);
  reg signed [32-1:0] _tmp_data_8;
  reg _tmp_valid_8;
  wire _tmp_ready_8;
  assign zd = _tmp_data_8;
  assign zv = _tmp_valid_8;
  assign _tmp_ready_8 = 1;

  always @(posedge CLK) begin
    if(RST) begin
      _tmp_data_reg_0 <= 0;
      _tmp_valid_reg_0 <= 0;
      _tmp_data_1 <= 0;
      _tmp_valid_1 <= 0;
      _tmp_data_2 <= 0;
      _tmp_valid_2 <= 0;
      _tmp_data_3 <= 0;
      _tmp_valid_3 <= 0;
      _tmp_data_4 <= 0;
      _tmp_valid_4 <= 0;
      _tmp_data_5 <= 0;
      _tmp_valid_5 <= 0;
      _tmp_data_6 <= 0;
      _tmp_valid_6 <= 0;
      _tmp_data_7 <= 0;
      _tmp_valid_7 <= 0;
      _tmp_data_8 <= 1'd0;
      _tmp_valid_8 <= 0;
    end else begin
      if(_tmp_ready_0 || !_tmp_valid_0) begin
        _tmp_data_reg_0 <= _tmp_odata_0;
      end 
      if(_tmp_ready_0 || !_tmp_valid_0) begin
        _tmp_valid_reg_0 <= _tmp_ovalid_0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1 && vreset) begin
        _tmp_data_1 <= vreset_data;
      end 
      if(_tmp_valid_1 && _tmp_ready_1) begin
        _tmp_valid_1 <= 0;
      end 
      if((_tmp_ready_1 || !_tmp_valid_1) && 1) begin
        _tmp_valid_1 <= vreset;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_1 && _tmp_valid_1) begin
        _tmp_data_2 <= _tmp_data_1;
      end 
      if(_tmp_valid_2 && _tmp_ready_2) begin
        _tmp_valid_2 <= 0;
      end 
      if((_tmp_ready_2 || !_tmp_valid_2) && _tmp_ready_1) begin
        _tmp_valid_2 <= _tmp_valid_1;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_2 && _tmp_valid_2) begin
        _tmp_data_3 <= _tmp_data_2;
      end 
      if(_tmp_valid_3 && _tmp_ready_3) begin
        _tmp_valid_3 <= 0;
      end 
      if((_tmp_ready_3 || !_tmp_valid_3) && _tmp_ready_2) begin
        _tmp_valid_3 <= _tmp_valid_2;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_3 && _tmp_valid_3) begin
        _tmp_data_4 <= _tmp_data_3;
      end 
      if(_tmp_valid_4 && _tmp_ready_4) begin
        _tmp_valid_4 <= 0;
      end 
      if((_tmp_ready_4 || !_tmp_valid_4) && _tmp_ready_3) begin
        _tmp_valid_4 <= _tmp_valid_3;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && _tmp_ready_4 && _tmp_valid_4) begin
        _tmp_data_5 <= _tmp_data_4;
      end 
      if(_tmp_valid_5 && _tmp_ready_5) begin
        _tmp_valid_5 <= 0;
      end 
      if((_tmp_ready_5 || !_tmp_valid_5) && _tmp_ready_4) begin
        _tmp_valid_5 <= _tmp_valid_4;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5 && _tmp_valid_5) begin
        _tmp_data_6 <= _tmp_data_5;
      end 
      if(_tmp_valid_6 && _tmp_ready_6) begin
        _tmp_valid_6 <= 0;
      end 
      if((_tmp_ready_6 || !_tmp_valid_6) && _tmp_ready_5) begin
        _tmp_valid_6 <= _tmp_valid_5;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_6 && _tmp_valid_6) begin
        _tmp_data_7 <= _tmp_data_6;
      end 
      if(_tmp_valid_7 && _tmp_ready_7) begin
        _tmp_valid_7 <= 0;
      end 
      if((_tmp_ready_7 || !_tmp_valid_7) && _tmp_ready_6) begin
        _tmp_valid_7 <= _tmp_valid_6;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_0 && _tmp_ready_7) && (_tmp_valid_0 && _tmp_valid_7)) begin
        _tmp_data_8 <= _tmp_data_8 + _tmp_data_0;
      end 
      if(_tmp_valid_8 && _tmp_ready_8) begin
        _tmp_valid_8 <= 0;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_0 && _tmp_ready_7)) begin
        _tmp_valid_8 <= _tmp_valid_0 && _tmp_valid_7;
      end 
      if((_tmp_ready_8 || !_tmp_valid_8) && (_tmp_ready_0 && _tmp_ready_7) && (_tmp_valid_0 && _tmp_valid_7) && _tmp_data_7) begin
        _tmp_data_8 <= 1'd0 + _tmp_data_0;
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
  input [32-1:0] b,
  output [64-1:0] c
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
  input [32-1:0] b,
  output [64-1:0] c
);

  reg signed [32-1:0] _a;
  reg signed [32-1:0] _b;
  reg signed [64-1:0] _tmpval0;
  reg signed [64-1:0] _tmpval1;
  reg signed [64-1:0] _tmpval2;
  reg signed [64-1:0] _tmpval3;
  reg signed [64-1:0] _tmpval4;
  wire signed [64-1:0] rslt;
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
    test_module = dataflow_matmul_bram.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
