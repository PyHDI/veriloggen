from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import dataflow_pass_nocontrol

expected_verilog = """

module test
(

);

  reg CLK;
  reg RST;
  reg [32-1:0] xdata;
  wire [32-1:0] zdata;
  reg xvalid;
  wire xready;
  assign xready = 1;
  wire zvalid;
  reg zready;
  assign zvalid = 1;

  main
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .xdata(xdata),
    .zdata(zdata)
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
    xdata = 0;
    xvalid = 0;
    zready = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #1000;
    reset_done = 1;
    @(posedge CLK);
    #1;
    #10000;
    $finish;
  end

  reg [32-1:0] xfsm;
  localparam xfsm_init = 0;
  reg [32-1:0] _tmp_0;
  localparam xfsm_1 = 1;
  localparam xfsm_2 = 2;
  localparam xfsm_3 = 3;
  localparam xfsm_4 = 4;

  always @(posedge CLK) begin
    if(RST) begin
      xfsm <= xfsm_init;
      _tmp_0 <= 0;
    end else begin
      case(xfsm)
        xfsm_init: begin
          xvalid <= 0;
          if(reset_done) begin
            xfsm <= xfsm_1;
          end 
        end
        xfsm_1: begin
          xvalid <= 1;
          xfsm <= xfsm_2;
        end
        xfsm_2: begin
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 5) && xready) begin
            xfsm <= xfsm_3;
          end 
        end
        xfsm_3: begin
          if(xready) begin
            xdata <= xdata + 1;
          end 
          if(xready) begin
            _tmp_0 <= _tmp_0 + 1;
          end 
          if((_tmp_0 == 10) && xready) begin
            xfsm <= xfsm_4;
          end 
        end
      endcase
    end
  end

  reg [32-1:0] zfsm;
  localparam zfsm_init = 0;
  localparam zfsm_1 = 1;
  localparam zfsm_2 = 2;

  always @(posedge CLK) begin
    if(RST) begin
      zfsm <= zfsm_init;
    end else begin
      case(zfsm)
        zfsm_init: begin
          zready <= 0;
          if(reset_done) begin
            zfsm <= zfsm_1;
          end 
        end
        zfsm_1: begin
          zfsm <= zfsm_2;
        end
        zfsm_2: begin
          if(zvalid) begin
            zready <= 1;
          end 
        end
      endcase
    end
  end


  always @(posedge CLK) begin
    if(reset_done) begin
      $display("xdata=%d", xdata);
      $display("zdata=%d", zdata);
    end 
  end


endmodule



module main
(
  input CLK,
  input RST,
  input [32-1:0] xdata,
  output [32-1:0] zdata
);

  assign zdata = xdata;

endmodule

"""

def test():
    veriloggen.reset()
    test_module = dataflow_pass_nocontrol.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
