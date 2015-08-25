import bram

expected_verilog = """
module TOP #
  (
   parameter ADDR_WIDTH = 10, 
   parameter DATA_WIDTH = 32
   )
  (
   input CLK, 
   input RST
   );
  reg [ADDR_WIDTH-1:0] addr;
  reg [DATA_WIDTH-1:0] datain;
  reg [1-1:0] write;
  wire [DATA_WIDTH-1:0] dataout;

  my_bram
    #(
      .ADDR_WIDTH(ADDR_WIDTH),
      .DATA_WIDTH(DATA_WIDTH)
      )
  inst_bram
    (
     .CLK(CLK),
     .addr(addr),
     .datain(datain),
     .write(write),
     .dataout(dataout)
     );
  
  reg [32-1:0] fsm;

  localparam fsm_init = 0;
  localparam fsm_1 = 1;
  localparam fsm_2 = 2;
  localparam fsm_3 = 3;

  always @(posedge CLK) begin
    if(RST) begin        
      addr <= 0;        
      datain <= 0;        
      write <= 0;        
      fsm <= fsm_init;
    end else begin
      if(fsm == fsm_init) begin        
        addr <= 0;        
        datain <= 0;        
        write <= 0;
        fsm <= fsm_1;
      end  
      if(fsm == fsm_1) begin        
        datain <= datain + 4;
        fsm <= fsm_2;
      end  
      if(fsm == fsm_2) begin        
        write <= 0;        
        fsm <= fsm_3;
      end  
      if(fsm == fsm_3) begin        
        if(addr == 128) begin        
          addr <= 0;        
          fsm <= fsm_init;
        end  
        else begin        
          addr <= addr + 1;        
          fsm <= fsm_1;
        end 
      end  
    end 
  end
  
endmodule

module my_bram #
  (
   parameter ADDR_WIDTH = 10, 
   parameter DATA_WIDTH = 32
   )
  (
   input CLK, 
   input [ADDR_WIDTH-1:0] addr, 
   input [DATA_WIDTH-1:0] datain, 
   input [1-1:0] write, 
   output [DATA_WIDTH-1:0] dataout
   );

  reg [DATA_WIDTH-1:0] d_addr;
  reg [DATA_WIDTH-1:0] mem [0:DATA_WIDTH-1];

  always @(posedge CLK) begin
    if(write) begin        
      mem[addr] <= datain;
    end  
    d_addr <= addr;
  end 

  assign dataout = mem[d_addr];
endmodule
"""

def test_bram():
    bram_module = bram.mkTop()
    bram_code = bram_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == bram_code)
