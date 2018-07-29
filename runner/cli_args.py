from argparse import ArgumentParser, FileType


class CliArgs:
    """
    Parse and open input files for use in robot.py
    """

    @staticmethod
    def parse(arguments: list):
        """
        Parse a list of arguments.

        :param arguments: List key/value pairs arguments, such as from sys.argv.
        :return: Namespace, with open file in file key.
        """
        parser = ArgumentParser()
        parser.add_argument('--file', dest="file", type=FileType('r'))
        config = parser.parse_args(arguments)
        return config
