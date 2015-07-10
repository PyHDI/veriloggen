.PHONY: all
all: clean

.PHONY: clean
clean:
	find . -maxdepth 1 -type d |grep "./" | xargs -I {} make clean -C {} 
