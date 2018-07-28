.PHONY: tests unit_tests

tests: unit_tests

unit_tests:
	python3.6 -m unittest tests.unit
