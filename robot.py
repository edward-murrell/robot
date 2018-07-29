#!/usr/bin/python
"""
Robot Program.

Copyright 2018, Edward Murrell
"""
import sys
from runner import CliArgs, FileToFileRunner
from robot import Robot, Board, Parser


def main(arguments):
    """
    Run the program using file as input.

    Out is written standard out.

    Argument list should contain ['--file', <filename>]

    :param arguments: Arguments from sys.argv, with script name removed.
    """
    config = CliArgs.parse(arguments)
    runner = FileToFileRunner(config.file, sys.stdout, Parser(Robot(Board(5, 5))))
    runner.run()
    config.file.close()


if __name__ == '__main__':
    main(sys.argv[1:])
