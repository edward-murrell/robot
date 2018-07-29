from argparse import ArgumentParser, FileType


class CliArgs:

    @staticmethod
    def parse(arguments):
        parser = CliArgs.__build()
        return parser.parse_args(arguments)



    @staticmethod
    def __build() -> ArgumentParser:
        argparser = ArgumentParser()
        argparser.add_argument('--file', nargs='+', type=FileType('r'))
        return argparser