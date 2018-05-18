
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>

#include "V{{ verilog_prefix }}.h"
#define Top V{{ verilog_prefix }}

#define MAX_SIM_TIME ({{ sim_time }})
#define TIME_STEP ({{ time_step }})

{% if dumpfile %}
#define TRACE
{% endif %}

vluint64_t main_time = 0;

double sc_time_stamp(){
  return main_time;
}

int main(int argc, char** argv)
{
  Verilated::commandArgs(argc, argv);
  
  Top *top = new Top();

#ifdef TRACE  
  Verilated::traceEverOn(true);
  VerilatedVcdC* tfp = new VerilatedVcdC;
  top->trace(tfp, 99);
  tfp->open("{{ dumpfile }}");
#endif

  {%- for clk in clks.keys() %}
  top->{{ clk }} = 0;
  {% endfor %}
  
  {%- for rst, (period, positive) in rsts.items() %}
  top->{{ rst }} = {% if positive %}0{% else %}1{% endif %};
  {% endfor %}

  {%- for init_name, init_val in inits.items() %}
  top->{{ init_name }} = {{ init_val }};
  {% endfor %}

  // input initialization 
  {%- for input_name in inputs %}
  top->{{ input_name }} = 0;
  {%- endfor %}

  while(!Verilated::gotFinish()){
    {%- for clk, hperiod in clks.items() %}
    if(main_time % {{ hperiod }} == 0){
      top->{{ clk }} = !top->{{ clk }};
    }
    {%- endfor %}
    
    {%- for rst, (period, positive) in rsts.items() %}
    if(main_time == {{ period }}){
      top->{{ rst }} = {% if positive %}1{% else %}0{% endif %};
    }
    if(main_time == {{ period }} * 2){
      top->{{ rst }} = {% if positive %}0{% else %}1{% endif %};
    }
    {%- endfor %}

    // update input 
    {%- for input_name in inputs %}
    top->{{ input_name }} = 0;
    {%- endfor %}

    top->eval();
    
#ifdef TRACE    
    tfp->dump(main_time);
#endif

    if(MAX_SIM_TIME > 0 && main_time >= MAX_SIM_TIME){
      //std::cout << "# simulation time: " << main_time << std::endl;
      break;
    }

    main_time += TIME_STEP;
  }

#ifdef TRACE    
  tfp->close();
#endif
  
  top->final();

  return 0;
}

