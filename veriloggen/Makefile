PYTHON = python3
#OPT=-m pdb

VERILOGGEN=veriloggen.py
#SRCS=

.PHONY: clean
clean:
	make clean -C utils
	rm -rf *.pyc __pycache__ parsetab.py *.out *.html

.PHONY: run
run:
	$(PYTHON) $(OPT) $(VERILOGGEN) $(SRCS)
