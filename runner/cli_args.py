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
        parser = ArgumentParser(add_help=True, prog="robot.py")
        parser.add_argument('--file', dest="file", type=FileType('r'), required=True)
        config, _ = parser.parse_known_args(args=arguments)
        return config
