module blinkled #
  (
   parameter WIDTH = 8
  )
  (
   input CLK, 
   input RST, 
   output reg [WIDTH-1:0] LED
  );
  
  reg [32-1:0] count;
  reg [WIDTH-1:0] led_count;
  
  always @(posedge CLK) begin
    if(RST) begin        
      count <= 0;
    end else begin
      if(count == 1023) begin
        count <= 0;
      end else begin
        count <= count + 1;
      end
    end 
  end
  
  always @(posedge CLK) begin
    if(RST) begin        
      led_count <= 0;
    end else begin
      if(count == 1023) begin        
        led_count <= led_count + 1;
      end  
    end 
  end

  always @* begin
    LED = led_count;
  end
  
endmodule
