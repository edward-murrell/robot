import io
import sys
from runner import CliArgs
from unittest import TestCase


class TestCliArgs(TestCase):
    """
    Test(s) for parsing the CLI arguments.
    """

    def test_file_input(self):
        """
        Extract the file type
        """
        expected = "Nothing."

        args = ["robot.py", "--file", "./tests/provided/empty.txt"]
        config = CliArgs.parse(args)

        self.assertIsInstance(config.file, io.TextIOWrapper)
        self.assertEqual(expected, config.file.readline().rstrip())

        config.file.close()

    def test_missing_file_input(self):
        """
        Extract the file type
        """
        expected = ["usage: robot.py [-h] --file FILE\n",
                    "robot.py: error: the following arguments are required: --file\n"]

        args = ["robot.py"]

        real_stderr = sys.stderr
        sys.stderr = capture = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            config = CliArgs.parse(args)

        capture.seek(0)
        self.assertEqual(cm.exception.code, 2)
        self.assertEqual(capture.readlines(), expected)

        sys.stderr = real_stderr
