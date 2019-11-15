FROM ubuntu:18.04
RUN apt update && apt upgrade -y
RUN apt install build-essential -y
RUN apt install git -y
RUN apt install python3 python3-pip -y
RUN apt install iverilog gtkwave -y
RUN pip3 install jinja2 numpy pytest pytest-pythonpath pyverilog
RUN mkdir /home/veriloggen/
WORKDIR "/home/veriloggen"
RUN git clone https://github.com/PyHDI/veriloggen.git
RUN cd veriloggen && python3 setup.py install && cd ../
