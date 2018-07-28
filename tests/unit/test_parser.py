from robot import Parser, Robot, Aim
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

    def test_parse_place(self):
        """
        Reading PLACE calls Robot.place()
        """
        robot = Mock(Robot)

        parser = Parser(robot)

        parser.read("PLACE 3,4,NORTH")
        robot.place.assert_called_with(3, 4, Aim.NORTH)
        parser.read("PLACE 1,7,SOUTH")
        robot.place.assert_called_with(1, 7, Aim.SOUTH)
        parser.read("PLACE 61,9,EAST")
        robot.place.assert_called_with(61, 9, Aim.EAST)
        parser.read("PLACE 66,77,SOUTH")
        robot.place.assert_called_with(66, 77, Aim.SOUTH)

    def test_parse_bad_place(self):
        """
        Reading bad PLACE calls does not call anything.
        """
        robot = Mock(Robot)

        parser = Parser(robot)
        parser.read("PLACE -3,4,SW")
        parser.read("PLACE12,2,EAST")
        parser.read("PLACE   4,4,EAST")
        parser.read("PLACE7 ,9,NORTHY")
        parser.read("PLACE ")
        parser.read("PLACE X,Y,NORTH")
        parser.read("PLACE -1,0,NORTH")

        robot.place.assert_not_called()

    def test_ignore_rubbish(self):
        """
        Invalid commands are ignored.
        """
        robot = Mock(Robot)

        parser = Parser(robot)
        parser.read("OPEN")

        robot.assert_not_called()
