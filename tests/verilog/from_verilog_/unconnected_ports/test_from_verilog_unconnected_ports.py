from __future__ import absolute_import
from __future__ import print_function

import collections
import io

from pyverilog.vparser.parser import VerilogParser

import veriloggen
from veriloggen.verilog.from_verilog import VerilogReadVisitor


def test_unconnected_instance_port(tmpdir):
    veriloggen.reset()
    source = '''
module test;
  wire CLK, RST;
  adder u_adder (
    .clk(CLK),
    .rst(RST),
    .B(1'b0),
    .A()
  );
endmodule
'''
    parser = VerilogParser(outputdir=str(tmpdir), debug=False)
    ast = parser.parse(source)
    definitions = collections.OrderedDict(
        (node.name, node) for node in ast.description.definitions)
    visitor = VerilogReadVisitor(definitions)
    visitor.visit(definitions['test'])

    generated = visitor.converted_modules['test'].to_verilog()
    reparsed = parser.parse(generated)
    original_instance = definitions['test'].items[-1]
    generated_instance = reparsed.description.definitions[0].items[-1]
    original_tree = io.StringIO()
    generated_tree = io.StringIO()
    original_instance.show(buf=original_tree, showlineno=False)
    generated_instance.show(buf=generated_tree, showlineno=False)
    assert generated_tree.getvalue() == original_tree.getvalue()
    ports = generated_instance.instances[0].portlist
    assert [port.portname for port in ports] == ['clk', 'rst', 'B', 'A']
    assert ports[2].argname.value == "1'b0"
    assert ports[3].argname is None
