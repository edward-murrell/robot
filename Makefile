.PHONY: tests unit_tests functional_tests

tests: unit_tests functional_tests

unit_tests:
	python3.6 -m unittest tests.unit

functional_tests:
	python3.6 -m unittest tests.functional
