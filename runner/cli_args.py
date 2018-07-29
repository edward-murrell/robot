from argparse import ArgumentParser, FileType


class CliArgs:

    @staticmethod
    def parse(arguments):
        parser = CliArgs.__build()
        config = parser.parse_args(arguments)
        return config

    @staticmethod
    def __build() -> ArgumentParser:
        argparser = ArgumentParser()
        argparser.add_argument('--file', dest="file", type=FileType('r'))
        return argparser