import io
from runner import CliArgs
from unittest import TestCase


class TestCliArgs(TestCase):
    """
    Test(s) for parsing the CLI arguments.
    """

    def test_file_input(self):
        """
        Extract single argument of file, and return t
        """
        expected = "Nothing."

        args = ["--file", "./tests/provided/empty.txt"]
        config = CliArgs.parse(args)

        self.assertIsInstance(config.file, io.TextIOWrapper)
        self.assertEqual(expected, config.file.readline())

        config.file.close()
