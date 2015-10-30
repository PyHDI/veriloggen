.PHONY: all
all: clean

.PHONY: clean
clean:
	make clean -C ./veriloggen
	make clean -C ./utils
	make clean -C ./sample
	make clean -C ./tests
	rm -rf *.pyc __pycache__ veriloggen.egg-info build dist

.PHONY: release
release:
	pandoc README.md -t rst > README.rst
