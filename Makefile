.PHONY: all
all: clean

.PHONY: clean
clean:
	make clean -C ./veriloggen
	make clean -C ./sample
	rm -rf *.pyc __pycache__ pycoram.egg-info build dist

.PHONY: release
release:
	pandoc README.md -t rst > README.rst
