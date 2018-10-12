from robot import Board, Robot, Aim
from . import fixtures
import pytest


class TestRobot(object):
    """
    Tests for a robot object to receive commands and issue reports.
    """

    @pytest.mark.parametrize("label,board,commands,expected", fixtures.get_place_and_move_scenarios())
    def test_move_scenarios(self, label, board, commands, expected):
        """
        Test normal scenarios.
        """
        robot = Robot(board)
        for command, args in commands:
            robot.__getattribute__(command)(**args)

        actual = robot.report()
        assert expected == actual, f"Failed on scenario: {label}"

    def test_invalid_does_not_override(self):
        """
        Robot will not be replaced after place command.
        """
        expected = '2,3,EAST'

        robot = Robot(Board(16, 4))
        robot.place(2, 3, Aim.EAST)
        robot.place(16, 7, Aim.NORTH)
        actual = robot.report()

        assert expected == actual

    @pytest.mark.parametrize("label,board,commands", fixtures.get_bad_place_scenarios())
    def test_bad_place_values(self, label, board, commands):
        """
        Test scenarios where the robot never gets placed.
        """
        expected = None
        robot = Robot(board)
        for command, args in commands:
            robot.__getattribute__(command)(**args)
        actual = robot.report()
        assert expected == actual, f"Failed on scenario: {label}"

    def test_multiple_placing(self):
        """
        Move the robot around a 5x5 board, requesting progress along the way.
        """
        robot = Robot(Board(5, 5))

        robot.place(13, 13, Aim.SOUTH)
        assert None == robot.report()

        robot.place(2, 2, Aim.WEST)
        robot.place(13, 13, Aim.SOUTH)
        assert '2,2,WEST' == robot.report()

        robot.place(1, 1, Aim.NORTH)
        robot.move()
        robot.move()
        robot.turn_right()
        robot.move()
        assert '2,3,EAST' == robot.report()

        robot.place(0, 5, Aim.NORTH)
        assert '2,3,EAST' == robot.report()

        robot.place(3, 4, Aim.SOUTH)
        assert '3,4,SOUTH' == robot.report()

        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.turn_left()  # Turn to the East
        robot.move()
        robot.move()       # Try to walk off the table.
        assert '4,0,EAST' == robot.report()
