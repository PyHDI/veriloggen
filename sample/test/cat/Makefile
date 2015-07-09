TARGET=led.py
ARGS=

PYTHON=python3
#PYTHON=python
#OPT=-m pdb
#OPT=-m cProfile -s time
#OPT=-m cProfile -o profile.rslt

.PHONY: all
all: run

.PHONY: run
run:
	$(PYTHON) $(OPT) $(TARGET) $(ARGS)

.PHONY: check
check:
	$(PYTHON) $(OPT) $(TARGET) $(ARGS) > tmp.v
	iverilog -tnull -Wall tmp.v
	rm -f tmp.v

.PHONY: clean
clean:
	rm -rf *.pyc __pycache__ parsetab.py *.out
