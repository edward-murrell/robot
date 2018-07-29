import io
from robot import Parser
from runner import FileToFileRunner
from unittest import TestCase
from unittest.mock import Mock, _Call as Call


class TestFileToFileRunner(TestCase):
    """
    Test(s) that FileToFileRunner passes the contents of input file/streams
     to a parser, and saves results to output file.
    """

    def test_file_passed_to_parser(self):
        """
        FileToFile takes lines from input file, feeds to parser, and returns any results to the output.
        """
        contents = io.StringIO(initial_value="REPORT\nPLACE 1,1,NORTH \nMOVE\nREPORT", newline="\n")
        expected_calls = [
            Call(("read", ("REPORT",)), ),
            Call(("read", ("PLACE 1,1,NORTH",)), ),
            Call(("read", ("MOVE",)), ),
            Call(("read", ("REPORT",)), ),
        ]
        expected_response = "1,2,NORTH\n"

        output = io.StringIO()

        parser = Mock(Parser)
        parser.read.side_effect = [None, None, None, "1,2,NORTH"]

        main = FileToFileRunner(contents, output, parser)
        main.run()
        output.seek(0)

        parser.assert_has_calls(expected_calls)
        self.assertEqual(expected_response, output.readline())
