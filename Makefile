PYTHON=python3
#PYTHON=python

.PHONY: all
all: clean

.PHONY: test
test:
	$(PYTHON) -m pytest -vv tests examples tests_obsolete examples_obsolete

.PHONY: clean
clean:
	make clean -C ./veriloggen
	make clean -C ./examples
	make clean -C ./tests
	make clean -C ./examples_obsolete
	make clean -C ./tests_obsolete
	rm -rf *.egg-info build dist *.pyc __pycache__ parsetab.py .cache *.out *.png *.dot tmp.v uut.vcd

#.PHONY: release
#release:
#	pandoc README.md -t rst > README.rst
