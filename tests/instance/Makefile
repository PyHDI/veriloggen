.PHONY: clean
clean:
	rm -rf *.pyc __pycache__ parsetab.py *.out tmp.v uut.vcd
	find . -maxdepth 1 -type d |grep "./" | xargs -I {} make clean -C {} 

.PHONY: test
test:
	find . -maxdepth 1 -type d |grep "./" | xargs -I {} make test -C {} 
