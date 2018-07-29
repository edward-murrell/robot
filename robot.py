#!/usr/bin/python
import sys
from runner import CliArgs, FileToFileRunner
from robot import Robot, Board, Parser


def main(arguments):
    config = CliArgs.parse(arguments)
    runner = FileToFileRunner(config.file, sys.stdout, Parser(Robot(Board(5, 5))))
    runner.run()
    config.file.close()


if __name__ == '__main__':
    main(sys.argv[1:])
