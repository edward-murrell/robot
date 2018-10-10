#!/usr/bin/python
"""
Robot Program.

Copyright 2018, Edward Murrell
"""
import sys
from runner import CliArgs, FileToFileRunner
from robot import Robot, Board, Parser


def main(config):
    """
    Run the program using file as input.

    Output is to written standard out.

    :param config: Configuration dict. Must contain a key of 'file' that points to an open file handle.
    """
    runner = FileToFileRunner(config.file, sys.stdout, Parser(Robot(Board(5, 5))))
    runner.run()
    config.file.close()


if __name__ == '__main__':
    main(CliArgs.parse(sys.argv))
