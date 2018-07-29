# Robot
Toy robot demo program. 29 / July 2018.

# Requirements
- Python 3.6 or better.
- Make and/or Docker for running tests.

# Running
```
python3.6 robot.py --file example.txt
```
The program will fail if you are using Python 3.5 or lower.

Note that Ubuntu 16.04 ships with Python 3.5. A Dockerfile is included for
 running with Python 3.6.


```
# The following command will output:
# 0,1,NORTH
python3.6 robot.py --file example.txt

# The following command will output:
# 2,2,EAST
# 4,4,SOUTH
# 4,0,SOUTH
python3.6 robot.py --file tests/provided/complex.txt

# OR
make build_docker && make run_docker_example

# OR
docker build -t robot-ekm ./
docker run --rm robot-ekm python ./robot.py --file tests/provided/complex.txt
```


# Tests
All tests can be run by calling:
```
make tests
# OR
python3.6 -m unittest tests
# OR
make build_docker && make run_docker_tests
# OR
docker build -t robot-ekm ./
docker run --rm robot-ekm make tests
```

## Unit
To run unit tests, use the following shell commands:
```
make unit.tests
# OR
python3.6 -m unittest tests.unit
# OR
docker run --rm robot-ekm make unit_tests
```

## Functional
```
make unit.functional
# OR
python3.6 -m unittest tests.functional
# OR
docker run --rm robot-ekm make functional_tests
```


# Limitations & Notes
- Board class height & width can be zero, or negative.
- Board height and width is hard coded.
- No setup.py.
- Program was only tested under Linux.

# Credits
- Edward Murrell / edward@codefoundation.com.au
