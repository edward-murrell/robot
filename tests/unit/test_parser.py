from robot import Parser, Robot
from unittest import TestCase
from unittest.mock import Mock


class TestParser(TestCase):
    """
    Tests for turning textual commands into a parsed command.
    """

    def test_parse_move(self):
        """
        Reading MOVE calls Robot.move()
        """
        robot = Mock(Robot)

        parser = Parser(robot)
        parser.read("MOVE")

        robot.move.assert_called_once()

    def test_parse_left(self):
        """
        Reading LEFT calls Robot.turn_left()
        """
        robot = Mock(Robot)

        parser = Parser(robot)
        parser.read("LEFT")

        robot.turn_left.assert_called_once()

    def test_parse_right(self):
        """
        Reading RIGHT calls Robot.turn_right()
        """
        robot = Mock(Robot)

        parser = Parser(robot)
        parser.read("RIGHT")

        robot.turn_right.assert_called_once()

    def test_parse_report(self):
        """
        Reading RIGHT calls Robot.turn_right()
        """
        robot = Mock(Robot)
        robot.report.return_value = "Some Text"

        parser = Parser(robot)
        response = parser.read("REPORT")

        robot.report.assert_called_once()
        self.assertEqual("Some Text", response)

    def test_ignore_rubbish(self):
        """
        Invalid commands are ignored.
        """
        robot = Mock(Robot)

        parser = Parser(robot)
        parser.read("OPEN")

        robot.assert_not_called()
