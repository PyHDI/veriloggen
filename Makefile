.PHONY: clean
clean:
	make clean -C ./veriloggen
	make clean -C ./utils
	make clean -C ./examples
	make clean -C ./tests
	rm -rf *.pyc __pycache__ *.out uut.vcd veriloggen.egg-info build dist

.PHONY: release
release:
	pandoc README.md -t rst > README.rst
