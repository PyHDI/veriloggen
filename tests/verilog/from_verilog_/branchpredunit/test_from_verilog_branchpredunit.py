from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import from_verilog_branchpredunit

expected_verilog = """
`default_nettype none

`define BP_ON  
`ifdef BP_ON  
  
//Gshare Branch Predict
module BP #
  (
    parameter W_A = 19,
    parameter W_BHR = 6,
    parameter W_PHT = 10,
    parameter N_PHT = 1024,
    parameter BHR_OFFSET = 4
  )
  (
    input CLK,
    input RST_X,
    input EN,
    input [W_A-1:0] pc,
    output pred,
    input [W_A-1:0] update_pc,
    input update,
    input rslt
  );

    //Branch History Register
    reg [W_BHR-1:0] bhr;
    //Pattern History Table
    wire [1:0] read_pht;
    wire [1:0] update_read_pht;
    wire [1:0] write_pht;

    reg [W_BHR-1:0] d_bhr;
    reg d_update;
    reg d_rslt;
    reg [W_A-1:0] d_update_pc;

    pht_mem #(.W_PHT(W_PHT), .N_PHT(N_PHT))
    pht_mem(CLK, EN, pht_index(bhr, pc), read_pht,
            pht_index(bhr, update_pc), update_read_pht,
            pht_index(d_bhr, d_update_pc), write_pht, d_update);
    
    assign write_pht = pht_update(update_read_pht, d_rslt);
    assign pred = get_pred(read_pht);
    
    always @(posedge CLK or negedge RST_X) begin
        if(!RST_X) begin
            d_update <= 0;
            d_rslt <= 0;
            d_update_pc <= 0;
            d_bhr <= 0;
            bhr <= 0;
        end else begin
          if(EN) begin
            if(update) begin
                bhr <= {bhr, rslt};
            end
            d_update <= update;
            d_rslt <= rslt;
            d_update_pc <= update_pc;
            d_bhr <= bhr;
          end
        end
    end
    
    function [W_PHT-1:0] pht_index;
        input [W_BHR-1:0] bhr;
        input [W_A-1:0] pc;
        begin
          pht_index = (bhr << BHR_OFFSET) ^ (pc >> 2);
        end 
    endfunction

    function [1:0] pht_update;
        input [1:0] current;
        input rslt;
        begin
            if(rslt) begin
              pht_update = (current < 3)? current + 1: 3;
            end else begin
              pht_update = (current > 0)? current - 1: 0;
            end
        end
    endfunction
    
    function [0:0] get_pred;
        input [1:0] cnt;
        begin
          get_pred = (cnt >= 2)? 1:0;
        end
    endfunction
endmodule

module pht_mem #
 (
    parameter W_PHT = 10,
    parameter N_PHT = 1024
 )
 (
    input CLK,
    input EN,
    input [W_PHT-1:0] I_A0,
    output [1:0] O_Q0,
    input [W_PHT-1:0] I_A1,
    output [1:0] O_Q1,
    input [W_PHT-1:0] I_A2,
    input [1:0] I_D2,
    input I_WE2
 );

    reg [1:0] mem [0:N_PHT-1];
    reg [W_PHT-1:0] d_I_A0;
    reg [W_PHT-1:0] d_I_A1;

    integer i;
    initial begin
        d_I_A0 = 0;
        d_I_A1 = 0;
        for(i=0; i<N_PHT; i=i+1) begin
            mem[i] = 2'h3;
        end
    end
    always @(posedge CLK) begin
      if(EN) begin
            d_I_A0 <= I_A0;
            d_I_A1 <= I_A1;
            if(I_WE2) begin mem[I_A2] <= I_D2; end
      end
    end
    assign O_Q0 = mem[d_I_A0];
    assign O_Q1 = mem[d_I_A1];
endmodule

module BTB #
 (
    parameter N_WAY = 2, //2-way
    parameter W_A = 19,
    //parameter W_TAB = 10, //per way
    //parameter N_TAB = 1024, //per way
    parameter W_TAB = 5, //per way
    parameter N_TAB = 32 //per way
 )
 (
    input CLK, RST_X,
    input EN,
    input [W_A-1:0] pc,
    output [W_A-1:0] pred_target,
    output exist,
    output read_ras,
    input [W_A-1:0] update_pc,
    input [W_A-1:0] update_target,
    input update_read_ras,
    input update,
    input rslt
 );

    localparam W_TAG = W_A - (W_TAB + 2);

    reg [W_A-1:0] d_pc;
    reg [W_A-1:0] d_update_pc;
    reg [W_A-1:0] d_update_target;
    reg d_update;
    reg d_rslt;
    reg d_update_read_ras;
    
//    reg [0:0] last [0:N_TAB-1]; //LRU
//    reg [0:0] d_last;
    
    function [W_TAB-1:0] btb_index;
        input [W_A-1:0] pc;
        begin
          btb_index = pc >> 2;
        end
    endfunction
    
    function [W_TAG-1:0] get_tag;
        input [W_A-1:0] pc;
        begin
           get_tag = pc[W_A-1:(W_A-W_TAG)];
        end
    endfunction

/* -----\/----- EXCLUDED -----\/-----
    function lru;
        input last;
        input way;
        begin
          lru = ~(last == way);
        end
    endfunction
 -----/\----- EXCLUDED -----/\----- */

//    genvar w;
//    generate for(w=0;w<N_WAY;w=w+1) begin:way
        wire read_hit;
        wire update_hit;
        wire victim;
        reg [W_A-1:0] btb [0:N_TAB-1];
        reg [W_TAG-1:0] tag [0:N_TAB-1];
        wire [W_TAG-1:0] read_tag;
        wire [W_A-1:0] read_target;
        wire [W_TAG-1:0] update_tag;
        wire t_read_ras;
        reg [0:0] ras [0:N_TAB-1];
        wire btb_we;
        assign btb_we = d_rslt && d_update && (update_hit || victim);
        btb_mem #(.W_A(W_A), .W_TAB(W_TAB), .N_TAB(N_TAB))
        btb_mem (CLK, EN, btb_index(pc), read_target, 
                 btb_index(d_update_pc), d_update_target, btb_we);
        btb_tag #(.W_A(W_A), .W_TAB(W_TAB), .N_TAB(N_TAB))
        btb_tag (CLK, EN, btb_index(pc), read_tag, 
                 btb_index(update_pc), update_tag, 
                 btb_index(d_update_pc), get_tag(d_update_pc), btb_we);
        read_ras_mem #(.W_TAB(W_TAB), .N_TAB(N_TAB))
        ras_mem (CLK, EN, btb_index(pc), t_read_ras,
                 btb_index(d_update_pc), d_update_read_ras, btb_we);
        assign read_hit = get_tag(d_pc) == read_tag;
//    end endgenerate
  
/* -----\/----- EXCLUDED -----\/-----
    assign exist        = way[0].read_hit || way[1].read_hit;
    assign pred_target  = way[1].read_hit? way[1].read_target:
                         way[0].read_hit? way[0].read_target:
                         0;
    assign read_ras = way[1].read_hit? way[1].t_read_ras:
                      way[0].read_hit? way[0].t_read_ras:
                      0;
 -----/\----- EXCLUDED -----/\----- */
    assign exist        = read_hit;
    assign pred_target  = read_hit? read_target: 0;
    assign read_ras     = read_hit? t_read_ras: 0;
  
    integer j;
    always @(posedge CLK or negedge RST_X) begin
        if(!RST_X) begin
/* -----\/----- EXCLUDED -----\/-----
            for(j=0;j<N_TAB;j=j+1) begin
                last[j] <= 0;
            end
 -----/\----- EXCLUDED -----/\----- */
            d_pc <= 0;
            d_update_pc <= 0;
/* -----\/----- EXCLUDED -----\/-----
            d_last <= 0;
 -----/\----- EXCLUDED -----/\----- */
            d_update <= 0;
            d_rslt <= 0;
            d_update_read_ras <= 0;
        end else begin
          if(EN) begin
            d_pc <= pc;
            d_update_pc <= update_pc;
/* -----\/----- EXCLUDED -----\/-----
            d_last <= last[btb_index(update_pc)];
 -----/\----- EXCLUDED -----/\----- */
            d_update <= update;
            d_update_target <= update_target;
            d_rslt <= rslt;
            d_update_read_ras <= update_read_ras;
/* -----\/----- EXCLUDED -----\/-----
            if(d_rslt && d_update) begin
                if(way[0].update_hit)
                  last[btb_index(d_update_pc)] <= 0;
                else if(way[1].update_hit)
                  last[btb_index(d_update_pc)] <= 1;
            end
            if(way[0].read_hit) begin
              last[btb_index(d_pc)] <= 0;
            end 
            else begin if(way[1].read_hit) begin
              last[btb_index(d_pc)] <= 1;
            end
 -----/\----- EXCLUDED -----/\----- */
           end
        end
    end
    
/* -----\/----- EXCLUDED -----\/-----
    assign way[0].update_hit = (get_tag(d_update_pc) == way[0].update_tag);
    assign way[1].update_hit = (get_tag(d_update_pc) == way[1].update_tag) && ~way[0].update_hit;
    assign way[0].victim = ~way[0].update_hit && ~way[1].update_hit && 
                           lru(d_last, 0);
    assign way[1].victim = ~way[0].update_hit && ~way[1].update_hit && 
                           lru(d_last, 1);
 -----/\----- EXCLUDED -----/\----- */
    assign update_hit = (get_tag(d_update_pc) == update_tag);
    assign victim = ~update_hit;
endmodule

module btb_mem #
 (
    parameter W_A = 19,
    parameter W_TAB = 5, //per way
    parameter N_TAB = 32 //per way
 )
 (
    input CLK,
    input EN,
    input [W_TAB-1:0] I_A0,
    output [W_A-1:0] O_Q0,
    input [W_TAB-1:0] I_A1,
    input [W_A-1:0] I_D1,
    input I_WE1
  );  

    reg [W_A-1:0] btb [0:N_TAB-1];
    reg [W_TAB-1:0] d_I_A0;

    integer i;
    initial begin
        d_I_A0 = 0;
        for(i=0; i<N_TAB; i=i+1) begin
            btb[i] = 0;
        end
    end
    always @(posedge CLK) begin
      if(EN) begin
          d_I_A0 <= I_A0;
          if(I_WE1) begin btb[I_A1] <= I_D1; end
      end
    end
    assign O_Q0 = btb[d_I_A0];
endmodule

module btb_tag #
 (
    parameter W_A = 19,
    parameter W_TAB = 5, //per way
    parameter N_TAB = 32 //per way
 )
 (
    input CLK,
    input EN,
    input [W_TAB-1:0] I_A0,
    output [W_TAG-1:0] O_Q0,
    input [W_TAB-1:0] I_A1,
    output [W_TAG-1:0] O_Q1,
    input [W_TAB-1:0] I_A2,
    input [W_TAG-1:0] I_D2,
    input I_WE2
  );
    
    localparam W_TAG = W_A - (W_TAB + 2);
    reg [W_TAG-1:0] tag [0:N_TAB-1];
    reg [W_TAB-1:0] d_I_A0;
    reg [W_TAB-1:0] d_I_A1;

    integer i;
    initial begin
        d_I_A0 = 0;
        d_I_A1 = 0;
        for(i=0; i<N_TAB; i=i+1) begin
            tag[i] = ~0;
        end
    end
    
    always @(posedge CLK) begin
      if(EN) begin
            d_I_A0 <= I_A0;
            d_I_A1 <= I_A1;
            if(I_WE2) begin tag[I_A2] <= I_D2; end
      end
    end
    assign O_Q0 = tag[d_I_A0];
    assign O_Q1 = tag[d_I_A1];
endmodule

module read_ras_mem #
  (
    parameter W_TAB = 5, //per way
    parameter N_TAB = 32 //per way
  )
  (
    input CLK,
    input EN,
    input [W_TAB-1:0] I_A0,
    output [0:0] O_Q0,
    input [W_TAB-1:0] I_A1,
    input [0:0] I_D1,
    input I_WE1
  );

    reg [0:0] ras [0:N_TAB-1];
    reg [W_TAB-1:0] d_I_A0;
    
    integer i;
    initial begin
        d_I_A0 = 0;
        for(i=0; i<N_TAB; i=i+1) begin
            ras[i] = 0;
        end
    end
    
    always @(posedge CLK) begin
      if(EN) begin
            d_I_A0 <= I_A0;
            if(I_WE1) begin ras[I_A1] <= I_D1; end
      end
    end
    assign O_Q0 = ras[d_I_A0];
endmodule

//Return Address Stack
module RAS #
  (
    parameter W_A = 19,
    parameter W_STACK = 5,
    parameter N_STACK = 32,
    parameter W_CNT = 32
  )
  (
    input CLK,
    input RST_X,
    input EN,
    input I_PUSH,
    input I_POP,
    input [W_A-1:0] I_ADDR,
    output reg [W_A-1:0] O_ADDR,
    output O_OVERFLOW
  );

    reg [W_A-1:0] stack [0:N_STACK];
    reg [W_STACK-1:0] head;
    reg [W_CNT-1:0] over_cnt;
    
    assign O_OVERFLOW = (over_cnt > 0);
    wire [W_STACK-1:0] read_ptr;
    assign read_ptr = (head == 0)? 0 : head -1;
    //assign O_ADDR = (head == 0)? 0: stack[read_ptr];
    
    always @(posedge CLK or negedge RST_X) begin
        if(!RST_X) begin
            head <= 0;
            over_cnt <= 0;
        end else begin
          if(EN) begin
            O_ADDR <= (head == 0)? 0: stack[read_ptr];
            if(I_PUSH && head != N_STACK-1) begin
                stack[head] <= I_ADDR;
                head <= head +1;
            end
            if(I_POP && head != 0) begin
                if(over_cnt == 0) begin head <= head -1; end
            end
            if(I_PUSH && head == N_STACK-1) begin
                over_cnt <= over_cnt +1;
            end
            if(I_POP && head == N_STACK-1) begin
                over_cnt <= over_cnt -1;
            end
          end
        end
    end
endmodule

`else // !`ifdef BP_ON

module BP #
 (
    parameter W_A = 19,
    parameter W_BHR = 6,
    parameter W_PHT = 10,
    parameter N_PHT = 1024,
    parameter BHR_OFFSET = 4
 )    
    input CLK, RST_X;
    input EN;
    input [W_A-1:0] pc;
    output pred;
    input [W_A-1:0] update_pc;
    input update;
    input rslt;
    assign pred = 0;
endmodule



module BTB #
 (
    parameter N_WAY = 2, //2-way
    parameter W_A = 19,
    //parameter W_TAB = 10, //per way
    //parameter N_TAB = 1024, //per way
    parameter W_TAB = 5, //per way
    parameter N_TAB = 32 //per way
 )
 (
    input CLK, RST_X,
    input EN,
    input [W_A-1:0] pc,
    output [W_A-1:0] pred_target,
    output exist,
    output read_ras,
    input [W_A-1:0] update_pc,
    input [W_A-1:0] update_target,
    input update_read_ras,
    input update,
    input rslt
 );
    localparam W_TAG = W_A - (W_TAB + 2);
    assign pred_target = pc + 4;
    assign exist = 0;
    assign read_ras = 0;
endmodule

module RAS #
  (
    parameter W_A = 19,
    parameter W_STACK = 5,
    parameter N_STACK = 32,
    parameter W_CNT = 32
  )
  (
    input CLK,
    input RST_X,
    input EN,
    input I_PUSH,
    input I_POP,
    input [W_A-1:0] I_ADDR,
    output [W_A-1:0] O_ADDR,
    output O_OVERFLOW
  );
    assign O_ADDR = 0;
    assign O_OVERFLOW = 0;
endmodule
`endif

`default_nettype wire
"""

def test():
    veriloggen.reset()
    test_modules = from_verilog_branchpredunit.mkMips()
    code = ''.join([ m.to_verilog() for m in test_modules.values() if not m.used ])

    from pyverilog.vparser.parser import parse
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    import sys
    import tempfile
    
    # encoding: 'utf-8' ?
    encode = sys.getdefaultencoding()
    
    tmp = tempfile.NamedTemporaryFile()
    tmp.write(expected_verilog.encode(encode))
    tmp.read()
    filename = tmp.name
    print(filename)
    
    expected_ast, _ = parse([ filename ])
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)
