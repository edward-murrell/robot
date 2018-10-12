# Robot
Toy robot demo program. 29 / July 2018.

# Requirements
- Python 3.6 or better.
- Make and/or Docker for running tests.

# Running
```
python robot.py --file example.txt
# OR
python3.6 robot.py --file example.txt
```
The program will fail if you are using Python 3.5 or lower.

Note that Ubuntu 16.04 ships with Python 3.5. A Dockerfile is included for
 running the program and it's tests with Python 3.6.


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
docker run -v `pwd`:/robot:rw -u `id -u`:`id -g` --rm robot-ekm python ./robot.py --file tests/provided/complex.txt
```

## Instructions
Input files can be any text files with following commands, separated by newlines.
```
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

The board is five by five squares, with the the co-ordinates 0,0 being in the
 lower left (SOUTH-WEST) corner. The direction for `F` in the `PLACE` command
 must be one of `NORTH`, `SOUTH`, `EAST`, or `WEST`.

The `LEFT` and `RIGHT` commands will turn the robot 90 degrees to the left or
 right. `MOVE` will move the robot exactly one square in the direction it is
 facing, if it is able.

These commands can be in any order. Invalid commands are ignored, including
 `PLACE` commands that are out of bounds, and `MOVE` commands that would take
 it off the edge of the board.

At the end of the file, the program will exit.

## Example of Instructions
```
PLACE 2,4,SOUTH
MOVE
MOVE
RIGHT
MOVE
LEFT
MOVE
REPORT
```

This program will now print out `1,1,SOUTH` and exit.

## Example files
The following files are provided as examples:
* `example.txt`
* `tests/provided/complex.txt`
* `tests/provided/example1.txt`
* `tests/provided/example3.txt`
* `tests/provided/example2.txt`

# Tests
Tests require pyunit to run, and need it installed. Install pyunit locally by running:
```
make install_requirements
OR
python3.6 -m pip install -rrequirements.txt
```
Alternatively, use the provided docker container.

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
make unit_tests
# OR
python3.6 -m unittest tests.unit
# OR
docker run --rm robot-ekm make unit_tests
```

## Functional
```
make functional_tests
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

# Source
`https://github.com/edward-murrell/robot`
