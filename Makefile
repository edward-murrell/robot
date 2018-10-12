.PHONY: tests unit_tests functional_tests

UID:=`id -u`
GID:=`id -g`

tests: unit_tests functional_tests

install_requirements:
	python3.6 -m pip install -rrequirements.txt

unit_tests:
	python3.6 -m pytest tests/unit

functional_tests:
	python3.6 -m pytest tests/functional

build_docker:
	docker build -t robot-ekm ./

run_docker_tests:
	docker run -v $(CURDIR):/robot:rw -u $(UID):$(GID) --rm robot-ekm make tests

run_docker_example:
	docker run -v $(CURDIR):/robot:rw -u $(UID):$(GID) --rm robot-ekm python ./robot.py --file tests/provided/complex.txt
