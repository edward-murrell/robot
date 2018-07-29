.PHONY: tests unit_tests functional_tests

tests: unit_tests functional_tests

unit_tests:
	python3.6 -m unittest tests.unit

functional_tests:
	python3.6 -m unittest tests.functional

build_docker:
	docker build -t robot-ekm ./

run_docker_tests:
	docker run --rm robot-ekm make tests

run_docker_example:
	docker run --rm robot-ekm python ./robot.py --file tests/provided/complex.txt
