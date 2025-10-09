TARGET=raw_dims
TEST=test_$(TARGET).py
SOURCES=$(TARGET).py $(TEST)

.PHONY: all
all: test

.PHONY: test
test: $(SOURCES)
	python3 $(TEST)

.PHONY: test2
test2: $(SOURCES)
	python2 $(TEST)

.PHONY: clean
clean:
	rm -rf *.pyc __pycache__ parsetab.py parser.out .cache *.egg-info dist build

